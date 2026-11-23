"""The migration scan: the story notes, their trigger lines, what counts as new work, pieces, and batches
(spec-run-manager.md 04 items 4, 5, 20, 21; 07.1; 07.2 items 1 to 3; CONTRACT.md 5.2)."""
import os
import re

from .. import lines as ln
from .. import research as rs
from .. import snapshot

STORY_TYPES = ("brain-dump", "idea-note", "area-note")
CARRIED = "carried.json"  # the run folder's working file of matches close brings up to date
BATCH_SIZE = 20  # a setting (spec-run-manager.md 07.2 item 1)
BULLET = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\[(.)\]\s+)?(.*)$")
STATUS_TAG = re.compile(r"#status/\w[\w/-]*")
DATE_HEADING = re.compile(r"#{1,6}[ \t]+(\d{4}-\d{2}-\d{2})[ \t]*")
POINTER = re.compile(r"\[migrated-to::(.*)\]\s*$")
QUESTION = re.compile(r"^(\s*(?:[-*+]|\d+[.)]) )\[\?\] ")  # a `- [?] ` bullet (spec-run-manager.md 08.2 item 4)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
LINK = re.compile(r"(!?)\[\[([^\]|]*)(?:\|([^\]]*))?\]\]")  # an embed mark, the target, the shown text


def frontmatter_end(lines):
    """The index of the first body line: past the closing --- when the note opens with frontmatter, else 0.
    Frontmatter is never scanned (CONTRACT.md 5.2 item 4)."""
    if lines and lines[0].strip() == "---":
        for k in range(1, len(lines)):
            if lines[k].strip() == "---":
                return k + 1
    return 0


def type_values(lines):
    """Every value of the frontmatter's `type` list, inline, block, or a single value; [] when there is none."""
    end = frontmatter_end(lines)
    for k in range(1, max(end - 1, 1)):
        m = re.match(r"type:\s*(.*)$", lines[k])
        if not m:
            continue
        rest = m.group(1).strip()
        if rest:
            vals = rest.strip("[]").split(",")
        else:
            vals = []
            for t in lines[k + 1:end - 1]:
                if not t.strip():
                    continue
                if not t.strip().startswith("-"):
                    break
                vals.append(t.strip()[1:])
        return [v for v in (v.strip().strip("'\"") for v in vals) if v]
    return []


def note_kind(lines):
    """The note's kind: whichever of STORY_TYPES its `type` list holds, in any position, or None
    (spec-run-manager.md 04 item 21; migrator-rules.md 01.8)."""
    return next((v for v in type_values(lines) if v in STORY_TYPES), None)


def piece_key(snap, s):
    """The piece a source line sat in at run start, as (note, heading), the same key batches.json gives
    a piece (CONTRACT.md 5.2 item 9); None when the snapshot doesn't hold the line."""
    i = ln.snapshot_index(snap, s["text"], s["line"])
    if i is None:
        return None
    heading = None
    if note_kind(snap) == "brain-dump":
        start = frontmatter_end(snap)
        heading = next((snap[k] for k in range(i, start - 1, -1) if DATE_HEADING.fullmatch(snap[k])), None)
    return s["note"], heading


def piece_comments(batches, key):
    """The comments batches.json hands the migrator in a piece, in note order."""
    return [l["text"] for b in batches.get("batches", []) for p in b["pieces"]
            if (p["note"], p["heading"]) == key for l in p["lines"] if l["text"].lstrip().startswith("%%")]


def skipped_bullet(m):
    """A bullet migration never handles: `[r]` or `[b]`, a `[x]` research request, an `[AGENT]` line
    (spec-run-manager.md 07.1 item 5; CONTRACT.md 5.2 item 5)."""
    box, rest = m.group(1), m.group(2)
    return box in ("r", "b") or (box == "x" and "#research/run-" in m.group(0)) or rest.startswith("[AGENT] ")


def note_pieces(lines, brain_dump):
    """Split a story note's body into pieces, in note order, each with its non-skipped bullet count and
    its trigger lines as (line number, text, is a comment) (CONTRACT.md 5.2 items 2, 3, 5, 9). A comment
    starting directly below a skipped line is skipped too."""
    piece = {"heading": None, "date": None, "bullets": 0, "triggers": []}
    pieces = [piece]
    skip_above = False
    i = frontmatter_end(lines)
    while i < len(lines):
        text = lines[i]
        if text.lstrip().startswith("%%"):
            block = rs.comment_under(lines, i - 1)  # the block starting on line i
            if not skip_above:
                piece["triggers"].append((i + 1, block, True))
            i += block.count("\n") + 1
            skip_above = False
            continue
        date = DATE_HEADING.fullmatch(text) if brain_dump else None
        if date:
            piece = {"heading": text, "date": date.group(1), "bullets": 0, "triggers": []}
            pieces.append(piece)
        bullet = BULLET.match(text)
        skip_above = bool(bullet) and skipped_bullet(bullet)
        if bullet and not skip_above:
            piece["bullets"] += 1
            if STATUS_TAG.search(text) or "%%" in text:
                piece["triggers"].append((i + 1, text, False))
        i += 1
        if text.count("%%") % 2:  # an inline comment left open: the lines up to its close are comment text
            while i < len(lines) and lines[i].count("%%") % 2 == 0:
                i += 1
            i += 1
    return [pieces[0]] + sorted(pieces[1:], key=lambda p: p["date"])  # oldest date first (07.2 item 3)


def destinations(text, name):
    """The paths a line's `[migrated-to:: …]` pointer names, inside the project; None when it has none
    (CONTRACT.md 5.2 item 7)."""
    m = POINTER.search(text)
    if not m:
        return None
    prefix = f"Projects/{name}/"
    return {(t[len(prefix):] if t.startswith(prefix) else t) + ".md" for t in WIKILINK.findall(m.group(1))}


def pointer_match(text, note, lines, handled, name, used, matched=()):
    """For a tagged pointer line not matched by text: the one handled entry in the same note with the same
    destinations whose text is gone from the note, or None (spec-run-manager.md 07.1 item 4; CONTRACT.md
    5.2 item 8). Each entry is used at most once, in scan order: `used` holds the positions in `handled`
    already matched, and a line whose only candidate is used gets None. An entry a line `matched` by its
    text, link targets left out, is no candidate (5.2 item 14)."""
    dests = destinations(text, name)
    if not dests or not STATUS_TAG.search(text):
        return None
    present = set(lines)
    found = [k for k, e in enumerate(handled) if e.get("note") == note and e.get("pointer") and k not in matched
             and set(e["pointer"]) == dests and e.get("text") not in present]
    if len(found) != 1 or found[0] in used:
        return None
    used.add(found[0])
    return handled[found[0]]


def without_targets(text):
    """A tagged line with the target of each wikilink left out, the shown text after `|` kept: what the
    scan compares, so a renamed story note or a moved project folder makes nothing new
    (spec-run-manager.md 07.1 item 10; 11 item 102; CONTRACT.md 5.2 item 14)."""
    return LINK.sub(lambda m: f"{m.group(1)}[[{'' if m.group(3) is None else '|' + m.group(3)}]]", text)


def _rename_map(renames):
    """Each rename's old path, and its old file name for a short link, to its new target without .md.
    A file name two renames share isn't mapped."""
    out, names = {}, {}
    for r in renames:
        old, new = r["from"][:-3], r["to"][:-3]
        out[old] = new
        names.setdefault(old.rsplit("/", 1)[-1], set()).add(new.rsplit("/", 1)[-1])
    out.update({k: v.pop() for k, v in names.items() if len(v) == 1 and k not in out})
    return out


def comment_key(text, renames=()):
    """A comment as the scan compares it: its exact text, but each link target read as the path inside the
    project whatever the project folder is called, and an old path a rename the scan found gave read as its
    new one (spec-run-manager.md 07.1 item 11; 11 item 103; CONTRACT.md 5.2 item 15)."""
    moved = _rename_map(renames)

    def target(m):
        path, _, part = m.group(2).partition("#")
        path = re.sub(r"^Projects/[^/]+/", "", path)
        path = moved.get(path, path)
        shown = "" if m.group(3) is None else "|" + m.group(3)
        return f"{m.group(1)}[[{path}{'#' + part if part else ''}{shown}]]"
    return LINK.sub(target, text)


def scan(project, handled):
    """Scan every story note for new trigger lines (spec-run-manager.md 07.1 item 1). Returns the batches
    file's data (04 item 21), the text read for each story note, for the snapshot copies (04 item 9), and
    the matches `close` brings up to date (07.1 item 13)."""
    name = rs.project_name(project)
    dumps, others, texts = [], [], {}
    for note, full in snapshot.covered_notes(project).items():
        try:
            text = ln.read_text(full)
        except UnicodeDecodeError:
            continue
        lines = ln.Note(text).lines
        kind = note_kind(lines)
        if kind in STORY_TYPES:
            texts[note] = text
            (dumps if kind == "brain-dump" else others).append((note, lines, kind == "brain-dump"))
    notes = [(note, lines, note_pieces(lines, dump)) for note, lines, dump in dumps + others]
    match, renamed = Matcher(project, handled, notes).run()
    found, skipped, used = [], [], set()
    for note, lines, pieces in notes:  # Brain Dump docs first, each group by path (07.2 item 3)
        for piece in pieces:
            new, new_bullets, has_comment = [], 0, False
            for line, text, is_comment in piece["triggers"]:
                if (note, line) in match:  # matched to a handled entry (07.1 items 10 to 12)
                    continue
                was = None if is_comment else pointer_match(text, note, lines, handled, name, used,
                                                            {k for k, _ in match.values()})
                if was is not None and sorted(STATUS_TAG.findall(text)) == sorted(STATUS_TAG.findall(was["text"])):
                    skipped.append({"note": note, "line": line, "text": text, "was": was["text"]})
                    continue
                new.append({"line": line, "text": text})
                has_comment = has_comment or is_comment
                new_bullets += not is_comment
            if new:
                # A piece's size is its new trigger bullets; with a new comment, every bullet it holds
                # but the skipped lines (07.2 item 1; CONTRACT.md 5.2 item 11).
                size = piece["bullets"] if has_comment else new_bullets
                found.append(({"note": note, "heading": piece["heading"], "lines": new}, size))
    # Each match whose entry's text or note differs from the line, for `close` (07.1 item 13). The entry's
    # place in the handled list, which doesn't change before `close`, and its text, to check it by.
    carried = [{"entry": k, "was": handled[k].get("text"), "note": note, "line": line, "text": text}
               for (note, line), (k, text) in sorted(match.items())
               if handled[k].get("text") != text or handled[k].get("note") != note]
    return {"batches": cut_batches(found), "skipped": skipped, "renamed": renamed}, texts, carried


class Matcher:
    """Match each story note's trigger lines to handled entries (spec-run-manager.md 07.1 items 10 to 12;
    11 items 102 to 104; CONTRACT.md 5.2 items 6, 14 to 16). In order: every story note's lines against
    the entries that name it, exact text first, then with link targets left out (a comment by comment_key);
    then the renames a Brain Dump pointer gives; then the lines still unmatched against the entries whose
    story note no longer exists, each match a rename; then the comments still unmatched, read through the
    renames found. Each entry is used once; within a pass, lines go in scan order, so of repeats the first
    is handled (5.2 item 6)."""

    def __init__(self, project, handled, notes):
        self.project, self.handled, self.notes = project, handled, notes
        self.name = rs.project_name(project)
        self.used, self.match, self.renamed, self.by_note = set(), {}, [], {}
        for k, e in enumerate(handled):
            self.by_note.setdefault(e.get("note"), []).append(k)
        self.gone = {k for k, e in enumerate(handled)
                     if isinstance(e.get("note"), str) and not os.path.isfile(os.path.join(project, e["note"]))}

    def lines(self, comments):
        """Each unmatched trigger line in scan order, as (note, line number, text), comments or tagged lines."""
        return [(note, line, text) for note, _, pieces in self.notes for p in pieces
                for line, text, is_comment in p["triggers"] if is_comment == comments and (note, line) not in self.match]

    def take(self, lines, entries, key):
        """Match each line to the first unused entry of `entries` whose key is the line's. Returns the matches."""
        out, keys = [], {}
        for note, line, text in lines:
            want = key(text)
            k = next((k for k in entries(note) if k not in self.used
                      and (keys[k] if k in keys else keys.setdefault(k, key(self.handled[k].get("text") or "")))
                      == want), None)
            if k is not None:
                self.used.add(k)
                self.match[(note, line)] = (k, text)
                out.append((k, note))
        return out

    def own(self, note):
        return self.by_note.get(note, [])

    def gone_entries(self, note):
        return sorted(self.gone)

    def rename(self, old, new):
        if old != new and {"from": old, "to": new} not in self.renamed:
            self.renamed.append({"from": old, "to": new})

    def pointer_renames(self, dumps):
        """A Brain Dump line whose entry's pointer names a story note that no longer exists, where its
        pointer now names one that does, in the same place (07.1 item 12)."""
        for (note, line), (k, text) in list(self.match.items()):
            was, now = self.handled[k].get("pointer") or [], destinations_in_order(text, self.name)
            if note not in dumps or len(was) != len(now):
                continue
            for old, new in zip(was, now):
                if old != new and not os.path.isfile(os.path.join(self.project, old)) and new in self.stories:
                    self.rename(old, new)

    def run(self):
        self.stories = {note for note, _, _ in self.notes}
        dumps = {note for note, lines, _ in self.notes if note_kind(lines) == "brain-dump"}
        for comments, key in ((False, without_targets), (True, comment_key)):
            self.take(self.lines(comments), self.own, lambda t: t)
            self.take(self.lines(comments), self.own, key)
        self.pointer_renames(dumps)
        for k, note in self.take(self.lines(False), self.gone_entries, lambda t: t) \
                + self.take(self.lines(False), self.gone_entries, without_targets):
            self.rename(self.handled[k]["note"], note)
        key = lambda t: comment_key(t, self.renamed)
        self.take(self.lines(True), self.own, key)
        for k, note in self.take(self.lines(True), self.gone_entries, key):
            self.rename(self.handled[k]["note"], note)
        self.renamed.sort(key=lambda r: (r["from"], r["to"]))
        return self.match, self.renamed


def destinations_in_order(text, name):
    """The paths a line's pointer names, inside the project, in the order written (CONTRACT.md 5.2 item 7)."""
    m = POINTER.search(text)
    if not m:
        return []
    prefix = f"Projects/{name}/"
    return [(t[len(prefix):] if t.startswith(prefix) else t) + ".md" for t in WIKILINK.findall(m.group(1))]


def cut_batches(pieces):
    """Pack whole pieces in scan order: a piece joins the current batch if it stays at 20 or under,
    otherwise it starts a new one; a piece over 20 is a batch of its own (spec-run-manager.md 07.2 item 1;
    CONTRACT.md 5.2 items 11 and 12)."""
    batches, size = [], 0
    for piece, n in pieces:
        if not batches or size + n > BATCH_SIZE:
            batches.append({"batch": f"b{len(batches) + 1}", "pieces": []})
            size = 0
        batches[-1]["pieces"].append(piece)
        size += n
    return batches
