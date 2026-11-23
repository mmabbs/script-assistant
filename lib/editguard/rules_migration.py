"""The migration-run rules and the record check (spec-edit-guard.md 03.3 and 04).

The record check (copy-mismatch, pointer-mismatch) reads the records and the notes. The other five rules
run only on changes explain.py explained (spec-edit-guard.md 05 item 3).
"""
import os
import re
from collections import Counter

from .compare import RMEdit, _split_pointer, read_body
from .explain import AGENT_LINE, HEADING, _rejected_section
from .flags import make_flag

STATUS_TAG = re.compile(r"#status/[\w-]+")
REJECTED_TAG = "#status/rejected"
TYPE_INLINE = re.compile(r"^type:\s*\[([^\]]*)\]")
TYPE_SCALAR = re.compile(r"^type:\s*([^\s\[#][^#]*?)\s*$")
TYPE_BLOCK_ITEM = re.compile(r"^\s+-\s+(.+?)\s*$")
STORY_KINDS = ("brain-dump", "idea-note", "area-note")


# ---- reading notes -------------------------------------------------------------------------------

def note_kind(path):
    """The note's kind: whichever of STORY_KINDS its frontmatter `type` list holds, in any position
    (migrator-rules.md 01.8), or "" when it holds none."""
    if not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    if not lines or lines[0].rstrip() != "---":
        return ""
    vals = []
    for i in range(1, len(lines)):
        line = lines[i]
        if line.rstrip() == "---":
            break
        m = TYPE_INLINE.match(line) or TYPE_SCALAR.match(line)
        if m:
            vals = m.group(1).split(",")
            break
        if line.rstrip() == "type:":
            for nxt in lines[i + 1:]:
                m = TYPE_BLOCK_ITEM.match(nxt)
                if not m:
                    break
                vals.append(m.group(1))
            break
    vals = [v.strip().strip("'\"") for v in vals]
    return next((v for v in vals if v in STORY_KINDS), "")


class Notes:
    """Each changed note's kind and the line numbers now inside its Rejected section."""

    def __init__(self, project, diffs):
        self.project = project
        self.diffs = {d.note: d for d in diffs}
        self._kinds, self._rejected = {}, {}

    def kind(self, note):
        if note not in self._kinds:
            self._kinds[note] = note_kind(os.path.join(self.project, note))
        return self._kinds[note]

    def in_rejected(self, note, line_no):
        if note not in self._rejected:
            d = self.diffs.get(note)
            inside = _rejected_section(d.after) if d else set()
            self._rejected[note] = {l.no for l in d.after if l.idx in inside} if d else set()
        return line_no in self._rejected[note]


def added_status_tags(change):
    """Status tags on the line now that its before text lacked."""
    return Counter(STATUS_TAG.findall(change.after)) - Counter(STATUS_TAG.findall(change.before))


def _flag(rule, e):
    return make_flag(rule, e.change, e.unit)


# ---- the record check (spec-edit-guard.md 03.3) --------------------------------------------------

def copy_mismatch(ctx, project):
    """Every copies line of a unit that isn't undone must sit in the note its record names, character
    for character. The flag names that note, with before empty and the record's text as after
    (spec-edit-guard.md 05 item 4). Adapted from the copy-presence check in evals/_tools/record-check.py,
    reading the note's body only and skipping undone units."""
    flags, cache = [], {}
    for u in ctx.units:
        if not u.active:
            continue
        for c in u.data.get("copies") or []:
            note = c["note"]
            if note not in cache:
                cache[note] = {l.text for l in read_body(os.path.join(project, note))}
            for text in c.get("lines") or []:
                if text.strip() and text not in cache[note]:
                    flags.append({"rule": "copy-mismatch", "note": note, "before": "", "after": text,
                                  "unit": u.key, "_order": (note, 0)})
    return flags


def _destination(link, project_name):
    """The note a pointer's wikilink names, as a path inside the project folder, or None when it isn't
    in the settled form [[Projects/{Project}/{path}|{name}]] (spec-run-manager.md 08.2 item 2)."""
    m = re.fullmatch(r"\[\[Projects/" + re.escape(project_name) + r"/([^\]|#]+)\|([^\]|]+)\]\]", link)
    if not m or m.group(2) != m.group(1).rsplit("/", 1)[-1]:
        return None
    return m.group(1) + ".md"


def _listed(text, project_name):
    """The destinations a line's pointer already names."""
    split = _split_pointer(text)
    return {_destination(d, project_name) for d in split[1]} if split else set()


def _source_spot(diff, source, taken):
    """The snapshot line a source names: its text, at its line number when the text repeats."""
    same = [l for l in diff.before if l.text == source["text"] and l.idx not in taken]
    return next((l for l in same if l.no == source["line"]), same[0]) if same else None


def pointer_mismatch(ctx, diffs, explained=()):
    """Every source line of a pointer-written migrate unit must carry a pointer naming each note its
    copies went to, no more and no fewer. Only destinations added since the snapshot are checked
    (spec-edit-guard.md 03.3 item 2). A source line a recorded edit of the run changed is checked too,
    on the line the edit explains (runmanager CONTRACT.md 5.4 item 9). A source line that changed in any
    other way is already a change of its own and is skipped here. The flag holds the source line's
    snapshot text and its text now (spec-edit-guard.md 05 item 6)."""
    by_note = {d.note: d for d in diffs}
    edited = {(e.change.note, e.info["snap"].idx): (e.info["now"], e.info.get("pointer"))
              for e in explained if e.how == "edit" and "snap" in e.info}
    # Units that share a source line share its pointer, so their destinations are pooled.
    wanted, owner = {}, {}
    for u in ctx.units:
        if u.state != "pointer-written" or u.data.get("action") != "migrate":
            continue
        dests = {c["note"] for c in u.data.get("copies") or []}
        for s in u.data.get("sources") or []:
            k = (s["note"], s["text"], s["line"])
            wanted.setdefault(k, set()).update(dests)
            owner.setdefault(k, u.key)

    flags = []
    taken = {}
    for (note, text, line), dests in wanted.items():
        diff = by_note.get(note)
        if diff is None:
            continue
        snap = _source_spot(diff, {"text": text, "line": line}, taken.setdefault(note, set()))
        if snap is None:
            continue
        if snap.idx in diff.matched:
            now = diff.after[diff.matched[snap.idx]]
            rm = next((i for i in diff.items if isinstance(i, RMEdit) and i.before.idx == snap.idx), None)
        elif (note, snap.idx) in edited:
            now, rm = edited[(note, snap.idx)]
        else:
            continue  # gone or changed: unexplained-change covers it
        taken[note].add(snap.idx)
        added = [_destination(d, ctx.project_name) for d in (rm.added_destinations if rm else [])]
        expected = dests - _listed(snap.text, ctx.project_name)
        if Counter(added) != Counter(expected):
            flags.append({"rule": "pointer-mismatch", "note": note, "before": snap.text, "after": now.text,
                          "unit": owner[(note, text, line)], "_order": (note, 0)})
    return flags


# ---- the markup rules, on explained changes only -------------------------------------------------

def writer_line_edited(explained):
    """Every recorded edit to one of the writer's existing lines, in any note (spec-edit-guard.md 04 item 1)."""
    return [_flag("writer-line-edited", e) for e in explained if e.how == "edit"]


def brain_dump_status_tag(explained, notes):
    """A status tag the run added in the Brain Dump doc, even when a comment asked (04 item 2)."""
    return [_flag("brain-dump-status-tag", e) for e in explained
            if notes.kind(e.change.note) == "brain-dump" and added_status_tags(e.change)]


def area_note_status_tag(explained, notes):
    """A status tag on a line the run added or changed in the live part of an Area Note. A tag the line
    already had is the writer's and passes (04 item 3)."""
    return [_flag("area-note-status-tag", e) for e in explained
            if notes.kind(e.change.note) == "area-note" and added_status_tags(e.change)
            and not notes.in_rejected(e.change.note, e.change.after_line)]


def _as_rejected(source_text):
    """A source line as it must read in a Rejected section: the Run manager's pointer left off, and its
    status tag set to #status/rejected (spec-edit-guard.md 04 item 4)."""
    split = _split_pointer(source_text)
    text = split[0] if split else source_text
    tags = STATUS_TAG.findall(text)
    if tags:
        return STATUS_TAG.sub(REJECTED_TAG, text, count=1) if len(tags) == 1 else None
    return text.rstrip() + " " + REJECTED_TAG


def rejected_move_changed(explained, notes, units):
    """A line a reject or migrate copy placed in a Rejected section must be its source line with its
    status tag set to #status/rejected. The reason comment and any heading aren't moved lines (04 item 4)."""
    flags = []
    for e in explained:
        if e.how != "copy" or not notes.in_rejected(e.change.note, e.change.after_line):
            continue
        text = e.change.after
        if text.lstrip().startswith("%%") or HEADING.match(text):
            continue
        sources = units[(e.run, e.unit)].data.get("sources") or []
        if not sources:
            continue
        if text not in {_as_rejected(s["text"]) for s in sources}:
            flags.append(_flag("rejected-move-changed", e))
    return flags


def agent_line_added(explained):
    """An [AGENT] line a migration run added: always flagged (04 item 5)."""
    return [_flag("agent-line-added", e) for e in explained
            if e.how in ("copy", "edit") and AGENT_LINE.match(e.change.after)
            and not AGENT_LINE.match(e.change.before)]


def run_all(explained, diffs, ctx, project):
    notes = Notes(project, diffs)
    units = {(u.run, u.key): u for u in ctx.units}
    return (copy_mismatch(ctx, project)
            + pointer_mismatch(ctx, diffs, explained)
            + writer_line_edited(explained)
            + brain_dump_status_tag(explained, notes)
            + area_note_status_tag(explained, notes)
            + rejected_move_changed(explained, notes, units)
            + agent_line_added(explained))
