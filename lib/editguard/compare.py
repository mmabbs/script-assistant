"""The note diff (spec-edit-guard.md 03.1).

Each note's body is compared with its snapshot copy, line by line. Frontmatter and blank lines are
skipped. What the Run manager added since the snapshot (a pointer, a removed [?], a close) is stripped
before comparing, so the writer's line still lines up with its snapshot copy. Those stripped lines come
back as RMEdit items, for explain.py to check where they sit.

This module only finds the changes. It explains nothing.
"""
import difflib
import os
import re
from dataclasses import dataclass, field

# Folders that hold only run output. The snapshot never covers them (spec-run-manager.md 04 item 9).
NEVER_COVERED = {"Runs", ".runs", "llm-files"}

# The pointer's exact form (spec-run-manager.md 08.2 item 2): at the very end of the line.
POINTER_OPEN = " [migrated-to:: "
WIKILINK = re.compile(r"\[\[[^\]]*\]\]")
LIST_MARKER = re.compile(r"^(\s*(?:[-*+]|\d+[.)]) )(.*)$")
# A close: `- [r]` changed to `- [x]` (spec-run-manager.md 08.4 item 2).
CLOSED = re.compile(r"^(\s*- )\[x\]( .*)$")


@dataclass
class Line:
    no: int    # line number in the file, counting from 1, frontmatter included
    text: str
    idx: int   # position in the note's body list (frontmatter and blank lines left out)


@dataclass
class RMEdit:
    """A line that matches its snapshot copy once a Run manager addition is stripped."""
    note: str
    before: Line                 # the snapshot line
    after: Line                  # the line now
    kind: str                    # "pointer" or "close"
    question_removed: bool = False
    added_destinations: list = field(default_factory=list)  # pointer only: destinations added since the snapshot


@dataclass
class Hunk:
    """One spot where snapshot lines were removed and/or lines were added. Not yet paired."""
    note: str
    removed: list
    added: list


@dataclass
class NoteDiff:
    note: str        # path inside the project folder, with / separators
    before: list     # snapshot body lines
    after: list      # body lines now
    items: list      # Hunk and RMEdit, in note order
    matched: dict = field(default_factory=dict)  # snapshot body position -> body position now, for unchanged lines


def read_body(path):
    """Return the note's body as Line objects. Frontmatter and blank lines are skipped.

    A missing file is an empty note (spec-edit-guard.md 03.1 item 1). Frontmatter is the block from a
    first line `---` through the next `---` line (spec-edit-guard.md 03.1 item 7).
    """
    if path is None or not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    start = 0
    if lines and lines[0].rstrip() == "---":
        for i in range(1, len(lines)):
            if lines[i].rstrip() == "---":
                start = i + 1
                break
    body = []
    for i in range(start, len(lines)):
        if lines[i].strip():
            body.append(Line(i + 1, lines[i], len(body)))
    return body


# Adapted from notes_under in evals/_tools/record-check.py. Changes: paths use / separators, and the
# folders the snapshot never covers, plus dot-folders, are left out.
def notes_under(root):
    """Map each .md note's path inside root to its full path."""
    out = {}
    if not os.path.isdir(root):
        return out
    for dp, dirs, files in os.walk(root):
        at_root = dp == root
        dirs[:] = sorted(d for d in dirs
                         if not d.startswith(".") and not (at_root and d in NEVER_COVERED))
        for fn in files:
            if fn.endswith(".md"):
                full = os.path.join(dp, fn)
                out[os.path.relpath(full, root).replace(os.sep, "/")] = full
    return out


def _split_pointer(text):
    """Return (base, destinations) when text ends with a pointer, else None."""
    i = text.rfind(POINTER_OPEN)
    if i == -1 or not text.endswith("]"):
        return None
    inner = text[i + len(POINTER_OPEN):-1]
    links = WIKILINK.findall(inner)
    dests = links if links and ", ".join(links) == inner else [inner]
    return text[:i], dests


def strip_candidates(text):
    """Yield (snapshot form, kind, question_removed, added destinations) for each way the Run manager
    could have made `text` from a snapshot line (spec-run-manager.md 08.2 and 08.4)."""
    split = _split_pointer(text)
    if split:
        base, dests = split
        # A pointer new since the snapshot.
        yield base, "pointer", False, dests
        # A new pointer that also removed `[?]` (spec-run-manager.md 08.2 item 4).
        m = LIST_MARKER.match(base)
        if m:
            yield f"{m.group(1)}[?] {m.group(2)}", "pointer", True, dests
        # A pointer that gained destinations: the snapshot held the first j of them (08.2 item 3).
        for j in range(len(dests) - 1, 0, -1):
            yield base + POINTER_OPEN + ", ".join(dests[:j]) + "]", "pointer", False, dests[j:]
    m = CLOSED.match(text)
    if m:
        yield f"{m.group(1)}[r]{m.group(2)}", "close", False, []


# Adapted from diff_notes in evals/_tools/record-check.py. Changes: one note at a time; frontmatter is
# skipped; blank lines are dropped before diffing rather than after, so they can't split a changed line
# from its pair; Run manager additions are stripped first; and the result keeps whole blocks (Hunk) so
# explain.py can pair what's left after explaining each half.
def _matched_count(sm):
    return sum(size for _, _, size in sm.get_matching_blocks())


def _prefer_recorded(sm, a, b, after, recorded):
    """Pick between equally short readings of a note's changes.

    A line moved past a neighbour reads two ways: the line moved, or the neighbour did. Prefer the
    reading in which the lines the run's records name as changes (`recorded`: texts removed, texts
    added) are the changes, when it is as short as the default one. Otherwise, or when the default
    already leaves every such line unmatched, keep the default (spec-edit-guard.md 03.1 item 3).
    """
    removed, added = recorded
    hit_a = [i for i, t in enumerate(a) if t in removed]
    hit_b = [j for j, l in enumerate(after) if l.text in added]
    if not hit_a and not hit_b:
        return sm
    matched_a, matched_b = set(), set()
    for i, j, size in sm.get_matching_blocks():
        matched_a.update(range(i, i + size))
        matched_b.update(range(j, j + size))
    if not matched_a.intersection(hit_a) and not matched_b.intersection(hit_b):
        return sm
    # Each recorded line gets a token that equals nothing, so this reading can't match it.
    a2, b2 = list(a), list(b)
    for i in hit_a:
        a2[i] = object()
    for j in hit_b:
        b2[j] = object()
    alt = difflib.SequenceMatcher(a=a2, b=b2, autojunk=False)
    return alt if _matched_count(alt) >= _matched_count(sm) else sm


def diff_note(note, before, after, recorded=None):
    """Compare one note's snapshot body with its body now. Returns a NoteDiff.

    `recorded`, when given, is (texts the run's records remove from this note, texts they add to it),
    used only to choose between equally short readings (_prefer_recorded)."""
    snap = {l.text for l in before}
    keys, stripped = [], {}
    for l in after:
        key = l.text
        # Only what the Run manager added since the snapshot is stripped: a line identical to a
        # snapshot line stays as it is, pointer and all (spec-edit-guard.md 03.1 item 5).
        if l.text not in snap:
            for base, kind, question, dests in strip_candidates(l.text):
                if base in snap:
                    key = base
                    stripped[l.idx] = (kind, question, dests)
                    break
        keys.append(key)

    items, matched = [], {}
    a = [l.text for l in before]
    sm = difflib.SequenceMatcher(a=a, b=keys, autojunk=False)
    if recorded:
        sm = _prefer_recorded(sm, a, keys, after, recorded)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for i, j in zip(range(i1, i2), range(j1, j2)):
                matched[i] = j
                if j in stripped:
                    kind, question, dests = stripped[j]
                    items.append(RMEdit(note, before[i], after[j], kind, question, list(dests)))
        else:
            items.append(Hunk(note, before[i1:i2], after[j1:j2]))
    return NoteDiff(note, before, after, items, matched)


def diff_notes(snapshot_dir, project_dir, only=None, fingerprinted=(), recorded=None):
    """Diff the notes a run compares, sorted by path (spec-edit-guard.md 03.1 item 8).

    `only` given (a research run): just those notes, its request notes. A new note is left to the
    research rules. Otherwise (a migration run): every note the snapshot copied, plus every note in the
    project that is in neither the snapshot nor `fingerprinted`, which is new since the run started and
    is compared with an empty note. A fingerprinted note is never compared line by line.
    `recorded` maps a note to the (removed, added) texts its records name, for diff_note.
    """
    recorded = recorded or {}
    if only is not None:
        names = sorted(set(only))
        snap = {n: os.path.join(snapshot_dir, n) for n in names}
        now = {n: os.path.join(project_dir, n) for n in names}
    else:
        snap, now = notes_under(snapshot_dir), notes_under(project_dir)
        skip = set(fingerprinted)
        names = sorted(set(snap) | {n for n in now if n not in skip})
    return [diff_note(n, read_body(snap.get(n)), read_body(now.get(n)), recorded.get(n)) for n in names]


def pair_in_order(removed, added):
    """Pair removed and added lines from one spot in order (spec-edit-guard.md 03.1 item 6).
    Returns (pairs, leftover removed, leftover added)."""
    n = min(len(removed), len(added))
    return list(zip(removed[:n], added[:n])), removed[n:], added[n:]
