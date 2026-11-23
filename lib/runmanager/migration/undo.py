"""Undoing a unit from its record, never the snapshot, and the record check that sorts a failed
migrator's units (spec-run-manager.md 08.1; 09.1 items 2, 4, 5, 6; spec-migration-verifier.md 07 item 3;
CONTRACT.md 5.3 items 6 and 10).

Lines are found by exact text. The snapshot tells identical lines apart: a line the snapshot explains is
the writer's, so only a line it doesn't explain is taken for the unit's (08.1 item 1)."""
import json
import os
import re

from .. import lines as ln
from .. import research as rs
from .. import snapshot
from . import cycle
from .scan import POINTER, QUESTION, frontmatter_end

LINK = re.compile(r"\[\[([^\]|#]+)[^\]]*\]\]")
MARKER = re.compile(r"^(\s*(?:[-*+]|\d+[.)]) )")  # a bullet's indent and marker


def without_pointer(text):
    """The line with its `[migrated-to:: …]` pointer and the space before it taken off."""
    m = POINTER.search(text)
    if not m:
        return text
    start = m.start() - 1 if m.start() and text[m.start() - 1] == " " else m.start()
    return text[:start]


def bare(text):
    """A source line as it reads with no pointer and no `[?]`: what stays put while pointers come and go."""
    return QUESTION.sub(r"\1", without_pointer(text), count=1)


def pointer_links(text, name):
    """The links in a line's pointer, in order, each as (its path inside the project, start, end)
    (CONTRACT.md 5.2 item 7)."""
    m = POINTER.search(text)
    if not m:
        return []
    prefix = f"Projects/{name}/"
    return [((t[len(prefix):] if (t := k.group(1)).startswith(prefix) else t) + ".md", k.start(), k.end())
            for k in LINK.finditer(text, m.start(1), m.end(1))]


def locate(snap, lines, text, line_no, forms=None):
    """Where a source line sits now: matched by its bare text, so a pointer written, rewritten, or taken
    off doesn't lose it. Among lines with the same bare text, the one at the same place among them as in
    the snapshot, counting from the top (spec-run-manager.md 08.1 item 1). `forms`, when given, are every
    text the line may read now (edit_forms), the record text among them: a line the run's own edits
    changed is still found (CONTRACT.md 5.4 item 9). None when it isn't there."""
    keys = {bare(t) for t in (forms or [text])}
    hits = [j for j, t in enumerate(lines) if bare(t) in keys]
    i = ln.snapshot_index(snap, text, line_no)
    k = 0 if i is None else sum(1 for t in snap[:i] if bare(t) in keys)
    return hits[k] if k < len(hits) else None


def edit_forms(state, run, find):
    """A function from (note, a source line's record text) to every text that line may read now: the
    text itself, then each `after` of an `edits` entry in the same note whose `before` is one of these
    texts, followed as a chain (CONTRACT.md 5.4 item 9). The entries are those of this run's units the
    unit index doesn't list as undone, so an edit that was undone no longer counts. Only a change the run
    didn't make leaves the line unfound."""
    entries = {}
    for e in state["unit_index"]:
        if e.get("run") != run["id"] or e.get("state") == "undone":
            continue
        found = find(e.get("unit"))
        for x in (found[1]["edits"] if found else []):
            entries.setdefault(x["note"], []).append(x)

    def forms(note, text):
        out, grew = [text], True
        while grew:
            grew = False
            for x in entries.get(note, []):
                if x["before"] in out and x["after"] not in out:
                    out.append(x["after"])
                    grew = True
        return out
    return forms


def _drop_links(text, drop, name):
    """The line with the destinations in `drop` taken off its pointer. Those left keep their order and
    their link text; a pointer left with none is removed with the space before it (CONTRACT.md 5.5 item 6)."""
    links = pointer_links(text, name)
    keep = [k for k in links if k[0] not in drop]
    if len(keep) == len(links):
        return text
    if not keep:
        return without_pointer(text)
    lead, tail = text[:links[0][1]], text[links[-1][2]:]
    return lead + ", ".join(text[s:e] for _, s, e in keep) + tail


def unit_versions(project, brun, unit):
    """The unit as each saved record holds it, newest first: the record file's unit, then each saved
    copy's that differs from those already listed (CONTRACT.md 5.3 item 10)."""
    versions = [unit]
    for r in cycle.saved_rounds(project, brun):
        saved = cycle.units_by_id(json.loads(cycle.copy_text(project, brun, r))).get(unit["id"])
        if saved is not None and saved not in versions:
            versions.append(saved)
    return versions


def _take_pointer_off(project, state, run, entry, brun, unit, find):
    """Take a pointer-written unit's destinations off each of its source lines (spec-run-manager.md 09.1
    item 2, last bullet; CONTRACT.md 5.5 item 6). A destination stays when the snapshot line named it, or
    when another unit of this run that isn't undone points there from the same line. If the snapshot line
    was `- [?]` and no destination this run added is left, `[?]` goes back. Every other unit of this run
    whose pointed_lines holds the line's old text gets its new text. Returns the lines it couldn't find."""
    name = rs.project_name(project)
    mine = list(dict.fromkeys(c["note"] for c in unit["copies"]))
    others = []
    for e in state["unit_index"]:
        if e is not entry and e.get("run") == run["id"] and e.get("state") == "pointer-written":
            found = find(e.get("unit"))
            if found:
                others.append(found[1])
    misses = []
    # The unit's own edits still stand while its pointer comes off, so they count (CONTRACT.md 5.4 item 9).
    forms = edit_forms(state, run, find)
    for k, s in enumerate(unit["sources"]):
        path = os.path.join(project, s["note"])
        old_text = entry["pointed_lines"][k] if k < len(entry.get("pointed_lines") or []) else s["text"]
        note = ln.read_note(path) if os.path.isfile(path) else None
        snap = _snap_lines(project, brun, s["note"])
        j = None if note is None else locate(snap, note.lines, s["text"], s["line"], forms(s["note"], s["text"]))
        if j is None:
            misses.append({"unit": entry["unit"], "note": s["note"], "text": old_text})
            continue
        old = note.lines[j]
        i = ln.snapshot_index(snap, s["text"], s["line"])
        snap_text = snap[i] if i is not None else s["text"]
        keep = {p for p, _, _ in pointer_links(snap_text, name)}
        for u in others:
            if any(o["note"] == s["note"]
                   and locate(snap, note.lines, o["text"], o["line"], forms(o["note"], o["text"])) == j
                   for o in u["sources"]):
                keep |= {c["note"] for c in u["copies"]}
        new = _drop_links(old, [d for d in mine if d not in keep], name)
        added_left = {p for p, _, _ in pointer_links(new, name)} - {p for p, _, _ in pointer_links(snap_text, name)}
        if QUESTION.match(snap_text) and not QUESTION.match(new) and not added_left:
            new = MARKER.sub(r"\1[?] ", new, count=1)
        if new != old:
            note.lines[j] = new
            ln.write_note(path, note)
        for e in state["unit_index"]:
            if e is not entry and e.get("run") == run["id"]:
                e["pointed_lines"] = [new if t == old else t for t in e.get("pointed_lines") or []]
    return misses


def builds_on(later, earlier):
    """Whether a unit's edit built on another's: one of `later`'s `edits` entries has, in the same note, a
    `before` that is one of `earlier`'s `after` texts (CONTRACT.md 5.3 item 13)."""
    afters = {(x["note"], x["after"]) for x in earlier["edits"]}
    return any((x["note"], x["before"]) in afters for x in later["edits"])


def undo_built_on(project, state, run, key, unit, find):
    """Before undoing `unit`, undo each unit of this run the unit index lists approved or pointer-written
    whose edit built on one of its edits, newest first: each of those undoes the ones built on it first
    (CONTRACT.md 5.3 item 13). The reason saved for the run log is `chain-undone`. Returns (undo's
    misses, whether a note changed)."""
    misses, changed = [], False
    if not unit["edits"]:
        return misses, changed
    for e in list(state["unit_index"]):
        if e.get("run") != run["id"] or e.get("unit") == key or e.get("state") not in ("approved", "pointer-written"):
            continue
        found = find(e.get("unit"))
        if found and builds_on(found[1], unit):
            cycle.note_undone(project, run, e["unit"], {"why": CHAIN_UNDONE, "unit": key})
            m, did = undo_entry(project, state, run, e, find)
            misses += m
            changed |= did
    return misses, changed


def undo_order(units):
    """Units in the order undo takes them: a unit whose edit built on another's comes before it, so the
    chain comes undone newest first (CONTRACT.md 5.3 item 13); otherwise the order given."""
    left, out = list(units), []
    while left:
        u = next((u for u in left if not any(v is not u and builds_on(v, u) for v in left)), left[0])
        left.remove(u)
        out.append(u)
    return out


def undo_entry(project, state, run, entry, find):
    """Undo one unit the unit index lists for this run, pointer included (CONTRACT.md 5.5 item 6), then as
    Milestone 9's undo does, from its record file and its earlier saved copies (5.3 item 10). Units whose
    edits built on this unit's are undone first (5.3 item 13). The entry becomes `undone`, `pointed_lines`
    []. Returns (the lines undo couldn't find, whether a note changed)."""
    brun, unit = find(entry["unit"])
    misses, chained = undo_built_on(project, state, run, entry["unit"], unit, find)
    notes = list(dict.fromkeys([s["note"] for s in unit["sources"]] + _notes(unit)))
    before = _texts(project, notes)
    renamed = []
    if entry.get("state") == "pointer-written":
        misses += _take_pointer_off(project, state, run, entry, brun, unit, find)
    misses += undo_unit(project, brun, unit_versions(project, brun, unit), renamed)
    # An edit put back on a line another unit points from: that unit's pointed_lines gets the line's new
    # text, so pointed_lines always matches the note (CONTRACT.md 5.3 item 10; 5.5 item 6).
    for old, new in renamed:
        for e in state["unit_index"]:
            if e is not entry and e.get("run") == run["id"]:
                e["pointed_lines"] = [new if t == old else t for t in e.get("pointed_lines") or []]
    entry.update(state="undone", pointed_lines=[])
    return misses, chained or _texts(project, notes) != before


def _texts(project, notes):
    out = {}
    for note in notes:
        path = os.path.join(project, note)
        out[note] = ln.read_text(path) if os.path.isfile(path) else None
    return out


def _snap_lines(project, run, note):
    """The note's run-start copy, as lines; [] for a note the snapshot has no copy of, such as a note the
    run created."""
    path = os.path.join(snapshot.run_folder(project, run["id"]), "snapshot", *note.split("/"))
    return ln.read_note(path).lines if os.path.isfile(path) else []


def _notes(unit):
    """Every note the unit writes to, in record order."""
    found = [c["note"] for c in unit["copies"]] + [e["note"] for e in unit["edits"]]
    if unit["action"] == "reject":
        found += [s["note"] for s in unit["sources"]]
    return list(dict.fromkeys(found))


def _copy_lines(unit, note):
    """The unit's copy lines in one note. Blank lines are not recorded (spec-migrator.md 05.5 item 7)."""
    return [t for c in unit["copies"] if c["note"] == note for t in c["lines"] if t.strip()]


def prefer(unit, note):
    """The texts the unit's record says changed in one note, its copy lines and a reject's source lines:
    the reading where these changed wins a tie (lines.align)."""
    found = set(_copy_lines(unit, note))
    if unit["action"] == "reject":
        found |= {s["text"] for s in unit["sources"] if s["note"] == note}
    return found


def written(project, run, unit, others=()):
    """Sort a unit by the record check (spec-migration-verifier.md 07 item 3; CONTRACT.md 5.3 item 6):
    its writes are each copy line present, each edit's `after` present, and, for a `reject` unit, each
    source line gone from where it sat. Returns "whole", "partly written", or "not started"."""
    present = total = 0
    for note in _notes(unit):
        path = os.path.join(project, note)
        cur = ln.read_note(path).lines if os.path.isfile(path) else []
        snap = _snap_lines(project, run, note)
        _, new, gone = ln.align(snap, cur, prefer(unit, note))
        used = set()
        wants = _copy_lines(unit, note) + [e["after"] for e in unit["edits"] if e["note"] == note]
        for text in wants:
            total += 1
            # An edit's after that a later edit of the checked units built on reads as that later after
            # (CONTRACT.md 5.3 item 13).
            forms = _later_forms(note, text, others)
            j = next((k for k in sorted(new - used) if cur[k] in forms), None)
            if j is not None:
                used.add(j)
                present += 1
        if unit["action"] == "reject":
            for s in (s for s in unit["sources"] if s["note"] == note):
                total += 1
                i = ln.snapshot_index(snap, s["text"], s["line"])
                present += i is not None and i in gone
    if present == total:
        return "whole"
    return "not started" if present == 0 else "partly written"


def _later_forms(note, text, units):
    """`text`, then each `after` of the units' edits in `note` that build on it, followed as a chain."""
    out, grew = [text], True
    while grew:
        grew = False
        for x in (x for u in units for x in u["edits"] if x["note"] == note):
            if x["before"] in out and x["after"] not in out:
                out.append(x["after"])
                grew = True
    return out


def undo_unit(project, run, versions, renamed=None):
    """Undo one unit from its record, never the snapshot (spec-run-manager.md 09.1 items 2 to 5; CONTRACT.md
    5.3 item 10). `versions` is the unit as each saved record holds it, newest first; the first is the last
    valid copy. From it, the unit's copy lines leave their notes, each edit's `after` goes back to
    `before`, and a rejected source line goes back under the nearest non-blank line that sat above it in
    the snapshot. Then each earlier version's writes still in the notes are undone too, so whatever of the
    unit exists is removed (09.1 item 3). Each note is written whole (08.1 item 2). A created note left
    with only frontmatter and blank lines moves to `.runs/{run-id}/removed/` (09.1 item 4). Returns the
    last valid copy's lines undo couldn't find, as undo-misses entries (09.1 item 5); an earlier
    version's line already gone isn't a miss. `renamed`, when given, gets (old text, new text) for each
    edit put back on a line that carries a pointer, for the caller's pointed_lines."""
    renamed = [] if renamed is None else renamed
    misses = _undo_version(project, run, versions[0], put_back=True, renamed=renamed)
    for version in versions[1:]:
        _undo_version(project, run, version, put_back=False, renamed=renamed)
    notes = dict.fromkeys(c["note"] for v in versions for c in v["copies"] if c.get("creates_note"))
    for note in notes:
        path = os.path.join(project, note)
        if not os.path.isfile(path):
            continue
        lines = ln.read_note(path).lines
        if not any(t.strip() for t in lines[frontmatter_end(lines):]):
            dest = os.path.join(snapshot.run_folder(project, run["id"]), "removed", *note.split("/"))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            os.replace(path, dest)
    return misses


def _undo_version(project, run, unit, put_back, renamed):
    """Undo one record version of a unit, note by note. Returns the lines it couldn't find."""
    misses = []
    name = cycle.unit_name(run, unit["id"])

    def miss(note, text):
        misses.append({"unit": name, "note": note, "text": text})

    for note in _notes(unit):
        path = os.path.join(project, note)
        rejected = [s for s in unit["sources"] if s["note"] == note] if put_back and unit["action"] == "reject" else []
        if not os.path.isfile(path):
            texts = _copy_lines(unit, note) + [e["after"] for e in unit["edits"] if e["note"] == note]
            for text in texts + [s["text"] for s in rejected]:
                miss(note, text)
            continue
        current = ln.read_note(path)
        snap = _snap_lines(project, run, note)
        changed = False
        wants = prefer(unit, note)
        for text in _copy_lines(unit, note):
            j = _unexplained(snap, current.lines, text, wants)
            if j is None:
                miss(note, text)
            else:
                current.delete(j)
                changed = True
        for e in (e for e in unit["edits"] if e["note"] == note):
            j = _unexplained(snap, current.lines, e["after"], wants)
            if j is not None:
                current.lines[j] = e["before"]
                changed = True
                continue
            # The edited line may carry a pointer `pointers` wrote since, for a migrate unit of this run
            # with the same source line (CONTRACT.md 5.4 item 9). `before` goes back with that pointer kept.
            j = _pointered(snap, current.lines, e["after"], wants)
            if j is None:
                miss(note, e["after"])
                continue
            old = current.lines[j]
            new = _repoint(e["before"], e["after"], old, rs.project_name(project))
            current.lines[j] = new
            renamed.append((old, new))
            changed = True
        for s in rejected:
            done = _put_back(snap, current, s)
            if done is None:
                miss(note, s["text"])
            changed = changed or done
        if changed:
            ln.write_note(path, current)
    return misses


def _pointered(snap, lines, after, wants=None):
    """The position of a line the snapshot doesn't explain that reads `after` with destinations added to
    its pointer, and its `[?]` gone if the pointer took it, or None (spec-run-manager.md 08.2 items 2 to 4)."""
    _, new, _ = ln.align(snap, lines, wants)
    base = without_pointer(after)
    forms = {base, QUESTION.sub(r"\1", base, count=1)}
    had = {p for p, _, _ in pointer_links(after, "")}
    for k in sorted(new):
        t = lines[k]
        if POINTER.search(t) and without_pointer(t) in forms:
            now = {p for p, _, _ in pointer_links(t, "")}
            if had < now:
                return k
    return None


def _repoint(before, after, now, name):
    """`before` with the destinations the line now has beyond those `after` had, as `pointers` writes
    them (CONTRACT.md 5.4 items 4 to 6)."""
    from .pointers import with_pointer  # pointers imports this module
    had = {p for p, _, _ in pointer_links(after, name)}
    added = [p for p, _, _ in pointer_links(now, name) if p not in had]
    return with_pointer(before, list(dict.fromkeys(added)), name)


def _unexplained(snap, lines, text, wants=None):
    """The position of a line with this text that the snapshot doesn't explain, or None. `wants` is the
    unit's texts that changed, which win a tie between readings (lines.align)."""
    _, new, _ = ln.align(snap, lines, wants)
    return next((k for k in sorted(new) if lines[k] == text), None)


def _put_back(snap, note, source):
    """Put a rejected source line back under the nearest non-blank line that sat above it in the
    snapshot (CONTRACT.md 4 item 11). Returns True when put back, False when it never left, and None
    when it can't be placed."""
    i = ln.snapshot_index(snap, source["text"], source["line"])
    if i is None:
        return None
    matched, _, gone = ln.align(snap, note.lines)
    if i not in gone:
        return False
    above = ln.nonblank_above(snap, i)
    if above is None:
        note.insert(0, source["text"])
        return True
    q = matched.get(above)
    if q is None:
        return None
    note.insert(q + 1, source["text"])
    return True


def save_misses(project, run, misses):
    """Add undo's misses to `.runs/{run-id}/undo-misses.json`, for the run log. Written as [] when undo
    ran and missed nothing (CONTRACT.md 5.3 item 10)."""
    path = os.path.join(snapshot.run_folder(project, run["id"]), "undo-misses.json")
    saved = []
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            saved = json.load(f)
    snapshot.write_json(path, saved + misses)


def undo_all(project, state, run, units, from_round, keep_misses=True, why=None):
    """Undo each unit, in record order, and add it to the unit index as `undone` (spec-run-manager.md 09.1
    item 6). `units` are the unit versions from the record at round `from_round`; the saved copies of
    earlier rounds are undone after it, newest first (CONTRACT.md 5.3 item 10). A sorted unit's
    unwritten lines were never written, so they aren't misses (keep_misses False). `why` is saved for the
    run log (cycle.note_undone). The caller saves the run state."""
    earlier = [cycle.units_by_id(json.loads(text)) for r in range(from_round - 1, -1, -1)
               if (text := cycle.copy_text(project, run, r)) is not None]
    misses, find = [], cycle.record_units(project, run)
    for unit in undo_order(units):
        # Units already approved whose edits built on this unit's come undone first (5.3 item 13).
        misses += undo_built_on(project, state, run, cycle.unit_name(run, unit["id"]), unit, find)[0]
        versions = [unit] + [v[unit["id"]] for v in earlier if unit["id"] in v]
        found = undo_unit(project, run, versions)
        misses += found if keep_misses else []
        cycle.join_index(state, run, unit["id"], "undone")
        cycle.note_undone(project, run, cycle.unit_name(run, unit["id"]), why)
    save_misses(project, run, misses)


EDIT_UNDONE = "edit-undone"
CHAIN_UNDONE = "chain-undone"


def _edited_source(project, brun, edit, source, chain):
    """Whether `edit`, an `edits` entry, changed the line `source` names (CONTRACT.md 5.3 item 13): same
    note, and its `before` is the source text, at the same snapshot line when both are there, or a later
    text in the source line's chain of the run's edits."""
    if edit["note"] != source["note"]:
        return False
    if edit["before"] != source["text"]:
        return edit["before"] in chain
    snap = _snap_lines(project, brun, source["note"])
    i = ln.snapshot_index(snap, edit["before"], edit["line"])
    k = ln.snapshot_index(snap, source["text"], source["line"])
    return i is None or k is None or i == k


def cascade(project, state, run):
    """Undo every migrate unit of this run whose source line an undone unit's edit changed, pointer and
    copies included, so the line goes back to `before` (CONTRACT.md 5.3 item 13). Repeated until nothing
    more is undone, since a migrate unit can carry edits of its own. The reason saved for the run log is
    `edit-undone`, naming the edit's unit. Only units the unit index lists approved or pointer-written are
    undone; a unit not yet in it is caught by the next command that cascades. The caller saves the run
    state. Returns (undo's misses, whether a note changed, the keys undone)."""
    find = cycle.record_units(project, run)
    misses, changed, keys = [], False, []
    while True:
        entries = [(e, find(e.get("unit"))) for e in state["unit_index"] if e.get("run") == run["id"]]
        entries = [(e, f) for e, f in entries if f is not None]
        all_edits = {}
        for _, (_, u) in entries:
            for x in u["edits"]:
                all_edits.setdefault(x["note"], []).append(x)

        def chain(note, text):
            out, grew = [text], True
            while grew:
                grew = False
                for x in all_edits.get(note, []):
                    if x["before"] in out and x["after"] not in out:
                        out.append(x["after"])
                        grew = True
            return out

        hit = None
        for e, (brun, u) in entries:
            if e.get("state") not in ("approved", "pointer-written") or u["action"] != "migrate":
                continue
            for d, (_, du) in entries:
                if d.get("state") != "undone" or d is e:
                    continue
                if any(_edited_source(project, brun, x, s, chain(s["note"], s["text"]))
                       for x in du["edits"] for s in u["sources"]):
                    hit = (e, d["unit"])
                    break
            if hit:
                break
        if hit is None:
            return misses, changed, keys
        e, edit_key = hit
        cycle.note_undone(project, run, e["unit"], {"why": EDIT_UNDONE, "unit": edit_key})
        found, did = undo_entry(project, state, run, e, find)
        misses += found
        changed |= did
        keys.append(e["unit"])


def cascade_saved(project, state, run):
    """cascade, then add its misses to undo-misses.json when it undid anything. Returns (whether a note
    changed, the keys undone)."""
    misses, changed, keys = cascade(project, state, run)
    if keys:
        save_misses(project, run, misses)
    return changed, keys
