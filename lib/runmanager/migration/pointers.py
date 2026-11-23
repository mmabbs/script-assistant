"""`pointers`: write the `migrated-to` pointer on every source line of the run's approved `migrate` units,
then wait for the Edit guard (spec-run-manager.md 04 items 15, 22; 05 item 1; 08.1; 08.2; CONTRACT.md
5.4); and rewriting a pointer from the records on a `pointer-mismatch` flag (CONTRACT.md 5.5 item 7).
Taking a pointer off again is in `undo` (5.5 item 6)."""
import os

from .. import lines as ln
from .. import research as rs
from .. import snapshot
from .. import state as st
from ..state import Refusal
from . import cycle, undo
from .scan import POINTER, QUESTION, destinations


def _link(name, note):
    """A destination as a wikilink, written as research link lines are (CONTRACT.md 5.4 item 3)."""
    stem = note[:-3] if note.endswith(".md") else note
    return f"[[Projects/{name}/{stem}|{stem.rsplit('/', 1)[-1]}]]"


def with_pointer(text, dests, name):
    """The line with the unit's destinations added to its pointer (spec-run-manager.md 08.2 items 2 to 4;
    CONTRACT.md 5.4 items 4 to 6). A line with no pointer gets ` [migrated-to:: …]` at its very end; a line
    with one gets the destinations it doesn't list yet, after the ones there. A `- [?]` loses its `[?]`."""
    text = QUESTION.sub(r"\1", text, count=1)
    new = [_link(name, d) for d in dests if d not in (destinations(text, name) or set())]
    if not new:
        return text
    m = POINTER.search(text)
    if m:
        return text[:m.end(1)] + ", " + ", ".join(new) + text[m.end(1):]
    return text + " [migrated-to:: " + ", ".join(new) + "]"


class Notes:
    """The notes the pointers go in, each read once, with its run-start copy for telling identical
    lines apart (spec-run-manager.md 08.1 item 1). Pointers change lines in place and never add or remove
    one, so a line's position stays put while the pointers go in."""

    def __init__(self, project, run, forms):
        self.project, self.run, self.forms = project, run, forms
        self.read, self.found, self.snaps = {}, {}, {}

    def note(self, path):
        if path not in self.read:
            full = os.path.join(self.project, path)
            self.read[path] = ln.read_note(full) if os.path.isfile(full) else None
            self.found[path] = list(self.read[path].lines) if self.read[path] else []
            self.snaps[path] = undo._snap_lines(self.project, self.run, path)
        return self.read[path]

    def find(self, source):
        """The position of a source line in its note, by exact text, or None. Among identical lines, the
        one at the same place among repeats as in the snapshot, counting from the top (CONTRACT.md 5.4
        item 2). A line an approved unit of this run edited is found by the edit's `after`, following a
        chain of edits (item 9). Found in the note as it read before any pointer went in."""
        if self.note(source["note"]) is None:
            return None
        snap, now, text = self.snaps[source["note"]], self.found[source["note"]], source["text"]
        forms = set(self.forms(source["note"], text))
        i = ln.snapshot_index(snap, text, source["line"])
        if i is not None:
            return ln.find_same_line(snap, i, now, forms)
        return next((j for j, t in enumerate(now) if t in forms), None)


def _approved(project, state, run):
    """The run's approved `migrate` units, in unit index order: (index entry, batch run, unit). A unit is
    approved when the unit index lists it `approved` for this run (CONTRACT.md 5.4 items 1, 2, 7)."""
    find, out = cycle.record_units(project, run), []
    for entry in state["unit_index"]:
        if entry.get("run") != run["id"] or entry.get("state") != "approved":
            continue
        found = find(entry.get("unit"))
        if found is None:
            raise Refusal(f"Unit {entry['unit']} isn't in its batch's record file.")
        if found[1]["action"] == "migrate":  # reject and edit units get no pointer (08.2 item 1)
            out.append((entry, *found))
    return out


def _undo_missed(project, run, missed):
    """Undo each unit whose source line can't be found, as Milestone 9's undo does, from its record and
    its earlier saved copies, newest first (CONTRACT.md 5.3 item 10; 5.4 item 9). The unit index entry
    becomes undone. Returns undo's misses."""
    misses = []
    for entry, brun, unit in missed:
        misses += undo.undo_unit(project, brun, undo.unit_versions(project, brun, unit))
        entry.update(state="undone", pointed_lines=[])
        cycle.note_undone(project, run, entry["unit"], {"why": "pointer-miss"})
    return misses


def rewrite(project, state, run, flag, find):
    """Rewrite the pointer on the source line a `pointer-mismatch` flag names (spec-run-manager.md 05 item
    6; CONTRACT.md 5.5 item 7): its destinations become the ones its snapshot line named, then those of
    every `pointer-written` unit of this run that points from it, in unit index order, each once. The
    rest of the line stays as it is now. Each such unit's pointed_lines gets the line's new text. Returns
    True when the note changed; False when nothing changed or the line can't be found."""
    found = find(flag.get("unit"))
    if found is None:
        return False
    brun, unit = found
    source = next((s for s in unit["sources"] if s["note"] == flag.get("note") and s["text"] == flag.get("before")),
                  next((s for s in unit["sources"] if s["note"] == flag.get("note")), None))
    path = os.path.join(project, flag.get("note") or "")
    if source is None or not os.path.isfile(path):
        return False
    note = ln.read_note(path)
    snap = undo._snap_lines(project, brun, source["note"])
    forms = undo.edit_forms(state, run, find)  # a line the run's edits changed (CONTRACT.md 5.4 item 9)
    j = undo.locate(snap, note.lines, source["text"], source["line"], forms(source["note"], source["text"]))
    if j is None:
        return False
    i = ln.snapshot_index(snap, source["text"], source["line"])
    snap_text = snap[i] if i is not None else source["text"]
    name = rs.project_name(project)
    dests = [p for p, _, _ in undo.pointer_links(snap_text, name)]
    pointing = []
    for entry in state["unit_index"]:
        if entry.get("run") != run["id"] or entry.get("state") != "pointer-written":
            continue
        other = find(entry.get("unit"))
        if other is None:
            continue
        for k, s in enumerate(other[1]["sources"]):
            if s["note"] == source["note"] and undo.locate(snap, note.lines, s["text"], s["line"],
                                                           forms(s["note"], s["text"])) == j:
                pointing.append((entry, k))
                dests += [c["note"] for c in other[1]["copies"]]
    m = POINTER.search(snap_text)
    new = undo.without_pointer(note.lines[j]) + (" " + snap_text[m.start():] if m else "")
    new = with_pointer(new, list(dict.fromkeys(dests)), name)
    for entry, k in pointing:
        lines = list(entry.get("pointed_lines") or [])
        lines += [""] * (k + 1 - len(lines))
        lines[k] = new
        entry["pointed_lines"] = lines
    if new == note.lines[j]:
        return False
    note.lines[j] = new
    ln.write_note(path, note)
    return True


def pointers(project, state):
    """`pointers` (needs `batches-done`): write every pointer, then move to `pointed` with `next_check` the
    next flags file number (CONTRACT.md 5.4 item 1). A unit with a source line that can't be found, by its
    own text or by the `after` of this run's edits to it, gets no pointer and is undone, and the line goes
    in `pointer-misses.json` (item 9). Each note is written whole,
    once, after all its pointers are in (item 10)."""
    run = cycle.migration_run(state, "batches-done")
    name = rs.project_name(project)
    todo, pointer_misses, undo_misses = _approved(project, state, run), [], []
    find = cycle.record_units(project, run)
    while True:
        # Find every source line first. A unit with a line missing is undone before any pointer is written,
        # since undo edits notes too; then the lines are found again in the notes undo left. The edits
        # that count are read again each time, so an edit undone here no longer does (item 9).
        notes = Notes(project, run, undo.edit_forms(state, run, find))
        spots = {id(u): [notes.find(s) for s in u["sources"]] for _, _, u in todo}
        missed = [t for t in todo if None in spots[id(t[2])]]
        if not missed:
            break
        for entry, brun, unit in missed:
            pointer_misses += [{"unit": entry["unit"], "note": s["note"], "text": s["text"]}
                               for s, j in zip(unit["sources"], spots[id(unit)]) if j is None]
        undo_misses += _undo_missed(project, run, missed)
        # A migrate unit whose source line an undone unit's edit changed is undone too (CONTRACT.md 5.3
        # item 13); it gets no pointer either.
        undo_misses += undo.cascade(project, state, run)[0]
        todo = [t for t in todo if t not in missed and t[0].get("state") == "approved"]

    changed = set()
    for entry, _, unit in todo:
        dests = list(dict.fromkeys(c["note"] for c in unit["copies"]))  # distinct, in record order (item 3)
        pointed = []
        for s, j in zip(unit["sources"], spots[id(unit)]):
            note = notes.note(s["note"])
            new = with_pointer(note.lines[j], dests, name)
            if new != note.lines[j]:
                note.lines[j] = new
                changed.add(s["note"])
            pointed.append(new)
        entry.update(state="pointer-written", pointed_lines=pointed)
    for path in sorted(changed):
        ln.write_note(os.path.join(project, path), notes.note(path))

    if pointer_misses:
        snapshot.write_json(cycle.run_file(project, run, "pointer-misses.json"), pointer_misses)
        undo.save_misses(project, run, undo_misses)
    # first_check is the flags file the migration-verifier judges (CONTRACT.md 5.5 item 1).
    n = cycle.next_flags_number(project, run)
    run.update(step="pointed", next_check=n, first_check=n)
    st.save_state(project, state)
    undone = len({m["unit"] for m in pointer_misses})
    return (f"pointers written for {len(todo)} unit(s); undone: {undone}; "
            f"next: run editguard check for flags-{run['next_check']}.json, then act")
