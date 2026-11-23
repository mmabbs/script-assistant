"""`recover` on a migration run: undo every unit of the crashed run, newest first, then wait for the Edit
guard (spec-run-manager.md 09.2 items 2, 3, 5; CONTRACT.md 5.6 items 7 to 9). Nothing goes on the handled
list. `act` at `recovered` is in `flags`; the recover log and the request comments are written in
`close`, from `request_sources`."""
import json
import os

from .. import state as st
from ..act import flags_path
from . import cycle, record, undo


def _batch_units(project, run, batch):
    """A batch's units, by id, from its last valid record copy, and the record file's units when the file
    is a valid record (CONTRACT.md 5.3 items 1 and 10). With no saved copy yet, as at `migrating` round 0,
    a valid record file is the last valid record."""
    brun = dict(run, batch=batch)
    path = os.path.join(project, ".runs", "units", f"{run['id']}-b{batch}.json")
    in_file = {}
    if os.path.isfile(path):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            data = None
        if data is not None and record.shape_problem(data) is None:
            in_file = cycle.units_by_id(data)
    rounds = cycle.saved_rounds(project, brun)
    last = cycle.units_by_id(json.loads(cycle.copy_text(project, brun, rounds[0]))) if rounds else in_file
    return brun, last, in_file


def request_sources(project, run):
    """The source lines of every unit of the crashed run that its typed request started (`trigger` kind
    `request`), each unit from its batch's last valid record, for recover's `close` to write the request
    as a comment under (spec-run-manager.md 09.2 item 3; 11 item 96; CONTRACT.md 5.6 item 8). None
    without a typed request."""
    if not run.get("request"):
        return []
    out = []
    for b in range(1, (run.get("batch") or 1) + 1):
        _, last, _ = _batch_units(project, run, b)
        out += [s for u in last.values() if u["trigger"]["kind"] == "request" for s in u["sources"]]
    return out


def recover(project, state):
    """Undo every unit of the crashed run not already undone, last batch first, each batch's units in
    reverse record order, pointer included (CONTRACT.md 5.6 item 7). Units the unit index lists become
    `undone` in place; the rest join it at the end, in undo order (5.6 item 8). Then step `recovered`,
    waiting for the next flags file. The open run gets "recovering": true, so `close` writes the recover
    log, and notes when the crashed run was waiting for a flags file that never appeared."""
    run = state["open_run"]
    st.refuse_if_recover_tried(run)
    # Saved before the undo edits any note, so a recover that crashes partway still counts as its try
    # (spec-run-manager.md 09.2 item 6; 11 item 108; CONTRACT.md 5.6 item 7).
    st.mark_recover_tried(project, state)
    n = run.get("next_check")
    unchecked = n is not None and not os.path.isfile(flags_path(project, run, n))
    batches = {b: _batch_units(project, run, b) for b in range(1, (run.get("batch") or 1) + 1)}

    def find(key):
        m = cycle.UNIT_KEY.fullmatch(key or "")
        if not m or int(m.group(1)) not in batches:
            return None
        brun, last, _ = batches[int(m.group(1))]
        unit = last.get(m.group(2))
        return None if unit is None else (brun, unit)

    for b in sorted(batches, reverse=True):
        brun, last, in_file = batches[b]
        for uid in reversed(list(last)):
            key = f"b{b}-{uid}"
            entry = cycle.index_entry(state, run, key)
            if entry is not None and entry.get("state") == "undone":
                continue
            if entry is not None:
                misses = undo.undo_entry(project, state, run, entry, find)[0]
            else:
                # A unit still in its batch cycle: undo every version of it, the record file's included.
                misses = undo.undo_built_on(project, state, run, key, last[uid], find)[0]
                versions = undo.unit_versions(project, brun, last[uid])
                if uid in in_file and in_file[uid] not in versions:
                    versions.append(in_file[uid])
                misses += undo.undo_unit(project, brun, versions)
                state["unit_index"].append({"run": run["id"], "unit": key, "state": "undone", "pointed_lines": []})
            # Saved after each unit, with its misses, so a recover that crashes on a later unit leaves the
            # unit index naming every unit already undone; the abandon log lists only the rest
            # (spec-run-manager.md 09.3 item 4; 11 item 119; CONTRACT.md 5.6 item 7).
            undo.save_misses(project, run, misses)
            st.save_state(project, state)

    run["markup_unchecked"] = bool(run.get("markup_unchecked") or unchecked)
    run.setdefault("recover_started", st.now().strftime(st.CLOCK_FORMAT))
    check = cycle.next_flags_number(project, run)
    # first_check null: the recover check is a first check, so nothing judged before the crash is
    # dropped from it (CONTRACT.md 5.6 item 7).
    run.update(recovering=True, step="recovered", fixing=None, next_check=check, recover_check=check,
               first_check=None)
    st.save_state(project, state)
    return f"recovering {run['id']}; next: run editguard check for flags-{check}.json, then act"
