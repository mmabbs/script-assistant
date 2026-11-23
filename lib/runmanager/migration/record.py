"""`record`: check the batch's record file, save a copy, and write the cut-down record for the
migration-verifier; `record --failed` after the migrator failed for good (spec-run-manager.md 04 item 22;
07.2 item 4; spec-migrator.md 05.2, 09; spec-migration-verifier.md 03.1 item 1, 07 items 3 and 4;
CONTRACT.md 5.3 items 1 to 6, 14, 15)."""
import json
import os
import re

from .. import lines as ln
from .. import research as rs
from .. import snapshot
from .. import state as st
from ..lines import write_note_whole
from ..state import Refusal
from . import cycle, undo
from .scan import destinations, piece_comments, piece_key

ACTIONS = ("migrate", "reject", "edit")
TRIGGERS = ("tag", "comment", "request")
STATUSES = ("tentative", "provisional", "committed", "rejected")
STATUS_FROM = ("tag", "comment", "parent tag", "request", "default")
LISTS = ("units", "left_in_place", "questions", "could_not")
UNIT_ID = re.compile(r"u\d+")


def _note_problem(note):
    """A `note` is a relative path inside the project ending in .md, with no `..`."""
    if not isinstance(note, str) or not note.endswith(".md") or note.startswith("/") or ".." in note.split("/"):
        return f"the note {note!r} isn't a path inside the project ending in .md"
    return None


def _line_ok(n):
    return isinstance(n, int) and not isinstance(n, bool) and n >= 1


def _source_problem(s, where):
    if not isinstance(s, dict):
        return f"{where} isn't an object"
    if not _line_ok(s.get("line")):
        return f"{where} has no line of 1 or more"
    if not isinstance(s.get("text"), str):
        return f"{where} has no text"
    return _note_problem(s.get("note"))


def _unit_problem(u, k):
    where = f"unit {k}"
    if not isinstance(u, dict):
        return f"{where} isn't an object"
    if not isinstance(u.get("id"), str) or not UNIT_ID.fullmatch(u["id"]):
        return f"{where}'s id {u.get('id')!r} isn't u and a number"
    where = f"unit {u['id']}"
    if u.get("action") not in ACTIONS:
        return f"{where}'s action {u.get('action')!r} isn't one of {', '.join(ACTIONS)}"
    t = u.get("trigger")
    if not isinstance(t, dict) or t.get("kind") not in TRIGGERS or not isinstance(t.get("text"), str):
        return f"{where}'s trigger needs a kind ({', '.join(TRIGGERS)}) and a text"
    if u.get("status") not in STATUSES:
        return f"{where}'s status {u.get('status')!r} isn't one of {', '.join(STATUSES)}"
    if u.get("status_from") not in STATUS_FROM:
        return f"{where}'s status_from {u.get('status_from')!r} isn't one of {', '.join(STATUS_FROM)}"
    if not isinstance(u.get("why"), str):
        return f"{where} has no why"
    if not isinstance(u.get("sources"), list) or not u["sources"]:
        return f"{where} has no sources"
    for s in u["sources"]:
        if (p := _source_problem(s, f"a source of {where}")):
            return p
    if not isinstance(u.get("copies"), list):
        return f"{where} has no copies list"
    for c in u["copies"]:
        if not isinstance(c, dict) or not isinstance(c.get("under"), str):
            return f"a copy of {where} needs a note, under, and lines"
        lines = c.get("lines")
        if not isinstance(lines, list) or not lines or not all(isinstance(t, str) for t in lines):
            return f"a copy of {where} needs at least one line"
        if "creates_note" in c and not isinstance(c["creates_note"], bool):
            return f"a copy of {where} has creates_note that isn't true or false"
        if (p := _note_problem(c.get("note"))):
            return p
    if not isinstance(u.get("edits"), list):
        return f"{where} has no edits list"
    for e in u["edits"]:
        if not isinstance(e, dict) or not _line_ok(e.get("line")) or not isinstance(e.get("before"), str) \
                or not isinstance(e.get("after"), str):
            return f"an edit of {where} needs a note, a line of 1 or more, before, and after"
        if (p := _note_problem(e.get("note"))):
            return p
    return None


def shape_problem(data):
    """What is wrong with a record's shape, or None (spec-migrator.md 05.2; CONTRACT.md 5.3 item 2)."""
    if not isinstance(data, dict):
        return "it isn't a JSON object"
    for key in LISTS:
        if not isinstance(data.get(key), list):
            return f"it has no {key} list"
    seen = set()
    for k, u in enumerate(data["units"], 1):
        if (p := _unit_problem(u, k)):
            return p
        if u["id"] in seen:
            return f"the unit id {u['id']} appears twice"
        seen.add(u["id"])
    needs = {"left_in_place": "why", "questions": "ask", "could_not": "what"}
    for key, field in needs.items():
        for e in data[key]:
            if not isinstance(e, dict) or not isinstance(e.get(field), str):
                return f"a {key} entry has no {field}"
            if key == "could_not" and isinstance(e.get("source"), dict) and "line" not in e["source"] \
                    and "text" not in e["source"]:
                # A story note the migrator couldn't read: a source naming the note and no line
                # (spec-run-manager.md 07.1 item 14; CONTRACT.md 5.3 item 2).
                if (p := _note_problem(e["source"].get("note"))):
                    return p
            elif key != "could_not" or "source" in e:
                if (p := _source_problem(e.get("source"), f"a {key} entry's source")):
                    return p
    return None


def fix_round_problem(data, last, fixing):
    """In a fix round, every unit not being fixed must be exactly as in the last valid copy, and no unit
    may be added or left out (spec-migrator.md 09 item 1; CONTRACT.md 5.3 item 3)."""
    before, now = cycle.units_by_id(last), cycle.units_by_id(data)
    for uid in before:
        if uid not in now:
            return f"unit {uid} is left out; a fix round keeps every unit"
        if uid not in fixing and now[uid] != before[uid]:
            return f"unit {uid} isn't being fixed, but it changed since the last round"
    added = [uid for uid in now if uid not in before]
    if added:
        return f"unit {added[0]} is new; a fix round adds no unit"
    return None


def load_record(project, run):
    """Read and check the batch's record file. Returns (record, its text, None) or (None, None, why)."""
    path = cycle.record_path(project, run)
    if not os.path.isfile(path):
        return None, None, "is missing"
    try:
        with open(path, encoding="utf-8", newline="") as f:
            text = f.read()
        data = json.loads(text)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        return None, None, f"can't be read as JSON ({e})"
    why = shape_problem(data)
    if why is None and run["round"] > 0:
        _, last = cycle.last_copy(project, run, run["round"] - 1)
        why = fix_round_problem(data, json.loads(last), run["fixing"] or []) if last else None
    return (None, None, f"was refused: {why}") if why else (data, text, None)


def cut_down(data, ids, recheck):
    """The cut-down record (spec-migration-verifier.md 03.1 item 1; CONTRACT.md 5.3 item 4): the units
    handed to the check keep id, action, sources, copies, edits, and status. On round 0 each list entry
    keeps only its source, and an entry with none is dropped; on a re-check the lists are empty."""
    units = [cut_down_unit(u) for u in data["units"] if u["id"] in ids]
    out = {"units": units}
    for key in LISTS[1:]:
        out[key] = [] if recheck else [{"source": e["source"]} for e in data[key] if "source" in e]
    return out


def cut_down_unit(u):
    """One unit as the migration-verifier sees it: id, action, sources, copies, edits, and status
    (spec-migration-verifier.md 03.1 item 1; 03.2 item 2)."""
    return {k: u[k] for k in ("id", "action", "sources", "copies", "edits", "status")}


def _go_on(project, state, run, data, text, ids):
    """Save the record's copy, write the cut-down record, and move to `verifying` with `fixing` set
    (CONTRACT.md 5.3 items 1, 4, 5)."""
    cycle.save_copy(project, run, text)
    name = f"verify-b{run['batch']}-r{run['round']}.json"
    snapshot.write_json(cycle.run_file(project, run, name), cut_down(data, ids, run["round"] > 0))
    run.update(step="verifying", fixing=ids)
    st.save_state(project, state)


def copy_problem(project, run, units):
    """The first copy line of these units that isn't in its note, character for character, at a place the
    snapshot can't account for, or None (spec-migrator.md 05.5 item 2; spec-run-manager.md 11 item 81;
    CONTRACT.md 5.3 item 1). Going by place lets a reject's copy that reads the same as its source pass;
    each place in a note answers for one copy line only."""
    for note in dict.fromkeys(c["note"] for u in units for c in u["copies"]):
        path = os.path.join(project, note)
        cur = ln.read_note(path).lines if os.path.isfile(path) else []
        wants = set().union(*(undo.prefer(u, note) for u in units))
        _, new, _ = ln.align(undo._snap_lines(project, run, note), cur, wants)
        free = sorted(new)
        for u in units:
            for line in undo._copy_lines(u, note):
                j = next((k for k in free if cur[k] == line), None)
                if j is None:
                    return f"unit {u['id']}'s copy `{line}` isn't in {note} as a line the run wrote"
                free.remove(j)
    return None


def _run_edits(project, run, data):
    """Every `edits` entry in this record and in this run's earlier batches' records."""
    edits = [e for u in data["units"] for e in u["edits"]]
    for k in range(1, run["batch"]):
        path = os.path.join(project, ".runs", "units", f"{run['id']}-b{k}.json")
        if os.path.isfile(path):
            try:
                with open(path, encoding="utf-8") as f:
                    edits += [e for u in json.load(f).get("units", []) for e in u.get("edits", [])]
            except (OSError, ValueError, AttributeError):
                pass
    return edits


def edited_source(project, run, unit, edits):
    """The first source of a `migrate` unit recorded as an edit left it, not as it read when the run
    started, or None (CONTRACT.md 5.3 item 14): its text isn't a line of the note's snapshot and equals
    the `after` of one of `edits` in the same note."""
    if unit["action"] != "migrate":
        return None
    for s in unit["sources"]:
        if s["text"] in undo._snap_lines(project, run, s["note"]):
            continue
        if any(e["note"] == s["note"] and e["after"] == s["text"] for e in edits):
            return s
    return None


def source_problem(project, run, data, units):
    """The refusal for the first of these units with a source recorded as an edit left it, or None
    (CONTRACT.md 5.3 item 14)."""
    edits = _run_edits(project, run, data)
    for u in units:
        s = edited_source(project, run, u, edits)
        if s is not None:
            return (f"unit {u['id']}'s source in {s['note']} is the line as an edit left it; its text must be "
                    "the line as it read when the run started")
    return None


def _earlier_units(project, state, run):
    """The units of earlier runs' records in `.runs/units/`, never this run's, that the unit index lists
    `pointer-written`: the ones that sent a line to a note and gave it its pointer (spec-run-manager.md 11
    item 99). Each comes as (its run, the unit)."""
    written = {(e.get("run"), e.get("unit")) for e in state["unit_index"] if e.get("state") == "pointer-written"}
    folder = os.path.join(project, ".runs", "units")
    out = []
    for name in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
        m = re.fullmatch(r"(.+)-b(\d+)\.json", name)
        if not m or m.group(1) == run["id"]:
            continue
        try:
            with open(os.path.join(folder, name), encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        units = data.get("units") if isinstance(data, dict) else None
        out += [(m.group(1), u) for u in units or [] if isinstance(u, dict)
                and (m.group(1), f"b{m.group(2)}-{u.get('id')}") in written]
    return out


def follower(state, batches):
    """A function from (an earlier run's id, a story note path then) to the path now: the path followed
    through every rename found since that run, in order, from the later closed runs' history entries and
    then this run's batches file (spec-run-manager.md 04 item 17; 07.1 item 13; 11 item 104)."""
    history = state["history"]

    def follow(run_id, path):
        ids = [h.get("id") for h in history]
        start = ids.index(run_id) + 1 if run_id in ids else len(history)
        for renamed in [h.get("renamed") or [] for h in history[start:]] + [batches.get("renamed") or []]:
            for r in renamed:
                if isinstance(r, dict) and r.get("from") == path:
                    path = r.get("to")
        return path
    return follow


def _same_trigger(comments, earlier, unit):
    """The same kind; for a comment, one comment in the piece holds both units' trigger text, the matching
    of spec-run-manager.md 11 item 97; for a tag or a request, the same text (11 item 99). An earlier
    trigger no comment holds can't be matched, so it isn't the same."""
    a, b = earlier.get("trigger") or {}, unit["trigger"]
    if a.get("kind") != b["kind"] or not isinstance(a.get("text"), str):
        return False
    if b["kind"] == "comment":
        return bool(a["text"] and b["text"]) and any(a["text"] in c and b["text"] in c for c in comments)
    return a["text"] == b["text"]


def _sent(earlier, s, note, path=lambda p: p):
    """Whether an earlier unit sent source line `s` to `note`. Its source text is the line before its
    pointer, as that run started; this run's carries the pointer, so both are compared bare. `path` gives
    a note path the earlier unit wrote as it reads now, through the renames since (11 item 104)."""
    line = undo.bare(s["text"])
    return earlier.get("action") == "migrate" \
        and any(isinstance(x, dict) and path(x.get("note")) == s["note"] and undo.bare(str(x.get("text"))) == line
                for x in earlier.get("sources") or []) \
        and any(isinstance(c, dict) and path(c.get("note")) == note for c in earlier.get("copies") or [])


def pointer_copy(project, state, run, unit):
    """The first (source, copy) of a `migrate` unit whose copy goes into a note its source line's pointer
    already names, when an earlier run's unit sent that line to that note for the same trigger; or None
    (spec-run-manager.md 11 items 95 and 99; CONTRACT.md 5.3 item 15). The pointer is the one on the
    source line as the record holds it, the line as it read when the run started, so only earlier runs'
    pointers count. `reject` and `edit` units get no pointer, so they aren't checked. A copy the earlier
    units can't account for, such as a new comment's ask, passes. An earlier unit's notes are followed
    through the renames since its run (11 item 104)."""
    if unit["action"] != "migrate":
        return None
    name, earlier, batches = rs.project_name(project), None, None
    for s in unit["sources"]:
        named = destinations(s["text"], name) or set()
        for c in (c for c in unit["copies"] if c["note"] in named):
            if earlier is None:
                earlier = _earlier_units(project, state, run)
                batches = cycle.load_working(project, run, "batches.json", {"batches": []})
                follow = follower(state, batches)
            comments = piece_comments(batches, piece_key(undo._snap_lines(project, run, s["note"]), s))
            if any(_sent(e, s, c["note"], lambda p, i=i: follow(i, p)) and _same_trigger(comments, e, unit)
                   for i, e in earlier):
                return s, c
    return None


def pointer_problem(project, state, run, units):
    """The refusal for the first of these units with a copy pointer_copy finds, or None (CONTRACT.md 5.3
    item 15)."""
    for u in units:
        found = pointer_copy(project, state, run, u)
        if found is not None:
            s, c = found
            return (f"unit {u['id']} copies `{s['text']}` in {s['note']} into {c['note']}, which that line's "
                    "pointer already names; take that copy out of the note and the record")
    return None


def record(project, state):
    """`record` (needs `migrating`): a valid record goes on to the check; a missing or invalid one, one
    with a copy its note doesn't hold, or one with a copy into a note its source's pointer names, is
    refused with one line, and nothing changes (CONTRACT.md 5.3 items 1 and 15)."""
    run = cycle.migration_run(state, "migrating")
    data, text, why = load_record(project, run)
    ids = None
    if not why:
        ids = [u["id"] for u in data["units"]] if run["round"] == 0 else list(run["fixing"] or [])
        checked = [u for u in data["units"] if u["id"] in ids]
        why = (copy_problem(project, run, checked) or source_problem(project, run, data, checked)
               or pointer_problem(project, state, run, checked))
        why = why and f"was refused: {why}"
    if why:
        raise Refusal(f"The record file {cycle.record_path(project, run)} {why}.")
    _go_on(project, state, run, data, text, ids)
    return f"checking {len(ids)} unit(s) of batch {run['batch']}, round {run['round']}"


def record_failed(project, state):
    """`record --failed` (needs `migrating`), after the migrator failed for good (spec-run-manager.md 04
    item 22, "When a part fails"; CONTRACT.md 5.3 item 6)."""
    run = cycle.migration_run(state, "migrating")
    data, text, why = load_record(project, run)
    if why and run["round"] == 0:
        # No usable record: the batch has no units. The Edit guard runs on the spot (07.2 item 4). An
        # invalid record file leaves .runs/units/, which holds only the valid records the Edit guard is
        # handed (CONTRACT.md 5.3 item 6, second bullet).
        path = cycle.record_path(project, run)
        if os.path.isfile(path):
            os.replace(path, cycle.run_file(project, run, f"record-b{run['batch']}-invalid.json"))
        run.update(step="batch-failed", fixing=None, next_check=cycle.next_flags_number(project, run))
        st.save_state(project, state)
        return f"batch {run['batch']} failed; next: run editguard check for flags-{run['next_check']}.json"
    if why:
        # A fix round: the last valid copy goes back as the record file, and the units in fixing are
        # undone from it. Units already approved stand.
        r, last = cycle.last_copy(project, run, run["round"] - 1)
        if last is None:
            raise Refusal(f"Batch {run['batch']} has no valid record copy to undo round {run['round']} from.")
        write_note_whole(cycle.record_path(project, run), last)
        units = cycle.units_by_id(json.loads(last))
        fixing = [units[u] for u in run["fixing"] or [] if u in units]
        undo.undo_all(project, state, run, fixing, r, why={"why": "migrator-stopped"})
        undo.cascade_saved(project, state, run)  # CONTRACT.md 5.3 item 13
        cycle.move_on(project, state)
        return f"undid {len(fixing)} unit(s) being fixed"
    checked = data["units"] if run["round"] == 0 else [u for u in data["units"] if u["id"] in (run["fixing"] or [])]
    # A migrate unit whose source was recorded as an edit left it, or that copies into a note its source's
    # pointer names, is sorted as not whole (5.3 items 14 and 15).
    edits = _run_edits(project, run, data)
    whole = [u for u in checked if edited_source(project, run, u, edits) is None
             and pointer_copy(project, state, run, u) is None and undo.written(project, run, u, checked) == "whole"]
    rest = [u for u in checked if u not in whole]
    undo.undo_all(project, state, run, rest, run["round"], keep_misses=False, why={"why": "migrator-stopped"})
    undo.cascade_saved(project, state, run)  # CONTRACT.md 5.3 item 13
    if whole:
        _go_on(project, state, run, data, text, [u["id"] for u in whole])
    else:
        cycle.save_copy(project, run, text)
        cycle.move_on(project, state)
    return f"whole: {len(whole)}; undone: {len(rest)}"
