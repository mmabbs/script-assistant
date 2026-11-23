"""The batch cycle's shared parts: its file paths, the unit index, and moving on to the next batch
(spec-run-manager.md 04 items 15, 22; 07.2 items 4 and 6; CONTRACT.md 5.3)."""
import os
import re

from .. import research as rs
from .. import snapshot
from .. import state as st
from ..lines import write_note_whole
from ..state import Refusal


def migration_run(state, step):
    """The open run, refusing unless it is a migration run at `step` (spec-run-manager.md 04 item 22)."""
    run = st.require_step(state, step)
    if run["kind"] != "migration":
        raise Refusal(f"Run {run['id']} is a {run['kind']} run; this step is for migration runs.")
    return run


def record_path(project, run):
    """The batch's record file, `.runs/units/{run-id}-b{N}.json` (spec-run-manager.md 07.2 item 6)."""
    return os.path.join(project, ".runs", "units", f"{run['id']}-b{run['batch']}.json")


def run_file(project, run, name):
    return os.path.join(snapshot.run_folder(project, run["id"]), name)


def copy_name(run, r=None):
    """The saved copy of a valid record: `record-b{N}-r{R}.json` (CONTRACT.md 5.3 item 1)."""
    return f"record-b{run['batch']}-r{run['round'] if r is None else r}.json"


def last_copy(project, run, upto):
    """The last valid record copy for this batch, at round `upto` or earlier: (round, its text), or
    (None, None) when there is none. Undo works from it (CONTRACT.md 5.3 item 10)."""
    for r in range(upto, -1, -1):
        text = copy_text(project, run, r)
        if text is not None:
            return r, text
    return None, None


def copy_text(project, run, r):
    """The saved record copy of this batch at round r, as text, or None."""
    path = run_file(project, run, copy_name(run, r))
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def save_copy(project, run, text):
    write_note_whole(run_file(project, run, copy_name(run)), text)


def units_by_id(record):
    return {u["id"]: u for u in record["units"]}


def join_index(state, run, unit_id, how):
    """A unit joins the unit index when it is approved or undone, named by batch: `b2-u3`
    (spec-run-manager.md 04 item 15; 07.2 item 6)."""
    state["unit_index"].append({"run": run["id"], "unit": unit_name(run, unit_id), "state": how,
                                "pointed_lines": []})


def unit_name(run, unit_id):
    return f"b{run['batch']}-{unit_id}"


def move_on(project, state):
    """No unit left to fix: the next batch at round 0, or `batches-done` after the last, with `batch`
    staying at the last (CONTRACT.md 5.3 item 8, last bullet). Saves the run state."""
    run = state["open_run"]
    batches = rs.load_json(run_file(project, run, "batches.json"), "batches file")
    last = len(batches.get("batches", [])) if isinstance(batches, dict) else 0
    if run["batch"] < last:
        run.update(batch=run["batch"] + 1, step="migrating")
    else:
        run["step"] = "batches-done"
    run.update(round=0, fixing=None, next_check=None)
    st.save_state(project, state)


UNIT_KEY = re.compile(r"b(\d+)-(u\d+)")


def record_units(project, run):
    """Each batch's record file in `.runs/units/`, read on first use: returns a function from a unit key
    (`b2-u3`) to (the run at that batch, the unit), or None when the unit isn't there (CONTRACT.md 5.4
    item 1). The record file is the batch's last valid record: `record --failed` on a fix round puts the
    last valid copy back there (CONTRACT.md 5.3 item 6). A key that isn't like b1-u2 is refused."""
    cache = {}

    def find(key):
        m = UNIT_KEY.fullmatch(key or "")
        if not m:
            raise Refusal(f"The unit key {key!r} isn't a unit key like b1-u2.")
        batch = int(m.group(1))
        if batch not in cache:
            path = os.path.join(project, ".runs", "units", f"{run['id']}-b{batch}.json")
            data = rs.load_json(path, f"record file for batch {batch}")
            ok = isinstance(data, dict) and isinstance(data.get("units"), list)
            cache[batch] = units_by_id(data) if ok else {}
        unit = cache[batch].get(m.group(2))
        return None if unit is None else (dict(run, batch=batch), unit)
    return find


def saved_rounds(project, run):
    """The rounds this batch has a saved record copy for, newest first (CONTRACT.md 5.3 item 10)."""
    folder = snapshot.run_folder(project, run["id"])
    pattern = re.compile(rf"record-b{run['batch']}-r(\d+)\.json")
    return sorted((int(m.group(1)) for name in os.listdir(folder) if (m := pattern.fullmatch(name))),
                  reverse=True)


def index_entry(state, run, key):
    """This run's unit index entry for `key`, or None."""
    return next((e for e in state["unit_index"] if e.get("run") == run["id"] and e.get("unit") == key), None)


def load_working(project, run, name, default):
    """A working file the run log reads, or `default` when it isn't there (CONTRACT.md 5.6 item 6)."""
    path = run_file(project, run, name)
    if not os.path.isfile(path):
        return default
    return rs.load_json(path, name)


def add_working(project, run, name, items):
    """Add items to a working list file in the run folder, kept for the run log (CONTRACT.md 5.6 item 6)."""
    if items:
        snapshot.write_json(run_file(project, run, name), load_working(project, run, name, []) + list(items))


UNDONE_WHY = "undone-why.json"


def note_undone(project, run, key, why):
    """Save why a unit was undone, for the run log's Units undone (spec-run-manager.md 07.3 item 2). `why`
    is a dict with `why` (fix-rounds, copy-mismatch, not-asked, migrator-stopped, verifier-failed,
    pointer-miss, edit-undone, chain-undone) and any details: `problems`, `flag`, or the edit's `unit`. The first reason
    saved for a unit stands."""
    if not why:
        return
    saved = load_working(project, run, UNDONE_WHY, {})
    if key not in saved:
        saved[key] = why
        snapshot.write_json(run_file(project, run, UNDONE_WHY), saved)


def next_flags_number(project, run):
    """The run's next flags file number: one past the highest flags file in the run folder, or 1
    (CONTRACT.md 5.3 item 6, second bullet)."""
    folder = snapshot.run_folder(project, run["id"])
    numbers = [int(m.group(1)) for name in os.listdir(folder) if (m := re.fullmatch(r"flags-(\d+)\.json", name))]
    return max(numbers, default=0) + 1
