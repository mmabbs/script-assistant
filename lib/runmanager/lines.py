"""Exact edits to the writer's notes: finding a line by its exact text, and writing a note whole
(spec-run-manager.md 08.1)."""
import difflib
import os
import tempfile


def write_note_whole(path, text):
    """Write a note whole, in one step (spec-run-manager.md 08.1 item 2). The new text goes into a new
    file beside the note, then os.replace swaps it in. A crash leaves the note as it was before the
    edit or after it, never half written. The text is written as given, with no line-ending changes."""
    path = os.fspath(path)
    folder = os.path.dirname(os.path.abspath(path))
    try:
        mode = os.stat(path).st_mode & 0o777
    except FileNotFoundError:
        mode = 0o644
    fd, temp = tempfile.mkstemp(dir=folder, prefix="." + os.path.basename(path) + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(temp, mode)
        os.replace(temp, path)
    except BaseException:
        try:
            os.unlink(temp)
        except FileNotFoundError:
            pass
        raise


def read_text(path):
    """A note's text exactly as stored, line endings kept."""
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


class Note:
    """A note as a list of lines, each with its own line ending kept, so writing it back changes only
    the lines an edit touched (spec-run-manager.md 08.1 item 2)."""

    def __init__(self, text):
        self.lines, self.ends = [], []
        parts = text.split("\n")
        for k, part in enumerate(parts):
            last = k == len(parts) - 1
            if last and part == "":
                break
            end = "" if last else "\n"
            if not last and part.endswith("\r"):
                part, end = part[:-1], "\r\n"
            self.lines.append(part)
            self.ends.append(end)
        self.newline = next((e for e in self.ends if e), "\n")

    def text(self):
        return "".join(line + end for line, end in zip(self.lines, self.ends))

    def insert(self, i, line):
        """Put a new line at position i, so it sits right under line i - 1."""
        end = self.newline
        if i > 0 and self.ends[i - 1] == "":  # inserting after a last line that had no line ending
            self.ends[i - 1], end = self.newline, ""
        self.lines.insert(i, line)
        self.ends.insert(i, end)

    def delete(self, i):
        self.lines.pop(i)
        if self.ends.pop(i) == "" and i > 0:
            self.ends[i - 1] = ""


def read_note(path):
    return Note(read_text(path))


def write_note(path, note):
    write_note_whole(path, note.text())


def snapshot_index(snap_lines, text, line_no):
    """The snapshot line a requests entry names: its text at its line number (counting from 1). When
    the line number doesn't hold that text, the first line that does (spec-run-manager.md 08.1 item 1)."""
    if 0 < line_no <= len(snap_lines) and snap_lines[line_no - 1] == text:
        return line_no - 1
    return next((i for i, t in enumerate(snap_lines) if t == text), None)


def find_same_line(snap_lines, snap_i, lines, forms):
    """Find the line now that is snapshot line `snap_i`, by exact text, never by line number alone
    (spec-run-manager.md 08.1 item 1). `forms` are the texts the line may have now, such as a request
    and its closed form. When several lines have one of those texts, the snapshot says which one it is:
    the line keeps its place among them, such as the second of three. Returns the index, or None."""
    k = sum(1 for t in snap_lines[:snap_i] if t in forms)
    hits = [i for i, t in enumerate(lines) if t in forms]
    return hits[k] if k < len(hits) else None


def _prefer_changed(sm, snap_lines, prefer):
    """Pick between equally long readings of a note's changes. A line moved past a neighbour reads two
    ways: the line moved, or the neighbour did. When a line whose text is in `prefer` (lines a record says
    it wrote or moved) came out unchanged, compare again with those lines swapped for tokens that match
    nothing, and keep that reading only when it leaves at least as many lines unchanged (the Edit guard's
    rule, spec-edit-guard.md 11 item 31)."""
    a, b = sm.a, sm.b
    if not any(a[i + k] in prefer for i, _, size in sm.get_matching_blocks() for k in range(size)):
        return sm
    alt = difflib.SequenceMatcher(None, [object() if t in prefer else t for t in a],
                                  [object() if t in prefer else t for t in b], autojunk=False)
    count = lambda m: sum(size for _, _, size in m.get_matching_blocks())
    return alt if count(alt) >= count(sm) else sm


def align(snap_lines, lines, prefer=None):
    """Match the snapshot's lines to the note's lines now, in order, by exact text (spec-run-manager.md
    08.1 item 1). Repeats count: each line matches at most one. `prefer`, when given, is texts a record
    says changed: between equally long readings, the one where they changed wins (_prefer_changed). With
    none, the comparison is as it always was. Returns (snapshot index -> index now, the indexes now the
    snapshot doesn't explain, the snapshot indexes no line now holds)."""
    matched, new, gone = {}, set(), set()
    sm = difflib.SequenceMatcher(None, snap_lines, lines, autojunk=False)
    if prefer:
        sm = _prefer_changed(sm, snap_lines, prefer)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            matched.update(zip(range(i1, i2), range(j1, j2)))
        else:
            gone.update(range(i1, i2))
            new.update(range(j1, j2))
    return matched, new, gone


def pick(candidates, preferred):
    """The first candidate in `preferred`, else the first candidate, else None."""
    best = [c for c in candidates if c in preferred]
    return (best or candidates or [None])[0]


def nonblank_above(snap_lines, i):
    """The nearest non-blank snapshot line above line i, or None (CONTRACT.md 4 item 11)."""
    return next((k for k in range(i - 1, -1, -1) if snap_lines[k].strip()), None)


def restore_line(note, snap, before, after, place_under=None):
    """Restore one flagged line in `note`, in memory (spec-run-manager.md 08.5; CONTRACT.md 4 items 5 and
    11; 5.5 item 5): a changed line goes back to `before`, an added line is removed, and a removed line
    goes back under the nearest non-blank line that sat above it in the snapshot. Lines are found by exact
    text; when the text repeats, the line the snapshot doesn't explain is the one meant.
    `place_under(above, matched)` gives the position to insert at for snapshot line `above`, or None; by
    default, right under that line when it is unchanged. Returns what was done, or None when the line
    can't be found."""
    cur = note.lines
    matched, cur_new, snap_gone = align(snap, cur)
    before, after = before or "", after or ""
    if after:
        j = pick([k for k, t in enumerate(cur) if t == after], cur_new)
        if j is None:
            return None
        if before:
            cur[j] = before
            return "changed back"
        note.delete(j)
        return "removed"
    i = pick([k for k, t in enumerate(snap) if t == before], snap_gone)
    if i is None:
        return None
    above = nonblank_above(snap, i)
    if above is None:
        note.insert(0, before)
        return "put back"
    if place_under is None:
        at = matched[above] + 1 if above in matched else None
    else:
        at = place_under(above, matched)
    if at is None:
        return None
    note.insert(at, before)
    return "put back"
