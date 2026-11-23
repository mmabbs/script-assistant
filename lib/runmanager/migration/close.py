"""`close` on a migration run: the handled list, the run log or recover log, the history entry, and the
snapshots kept (spec-run-manager.md 04 items 8, 17, 20, 22; 05 item 7; 07.1; 07.3; 09.2 items 2, 3;
spec-migrator.md 06; spec-edit-guard.md 07; spec-run-manager.md 11 items 93, 96, 97, 104 to 107; CONTRACT.md 5.6)."""
import os

from .. import lines as ln
from .. import research as rs
from .. import snapshot
from .. import state as st
from ..act import load_flags
from ..lines import write_note_whole
from ..runlog import MARKUP_UNCHECKED, note_link, quote
from . import cycle, recover, undo
from .scan import BULLET, CARRIED, STATUS_TAG, frontmatter_end, piece_comments, piece_key, skipped_bullet

ANSWER = "Answer with a comment on the source line, then start another migration run."
NEXT_RUN = "The next migration run tries this again."
KEEP = "Keep your comment {} until this migrates."
REQUEST_WRITTEN = "The run wrote your request as a comment under this line: {}. Keep it until this migrates."
COUNTED = ("approved", "pointer-written")
QUESTIONS, UNDONE, MISSED, PUT_BACK = ("Questions for you", "Units undone", "Lines the checker says were missed",
                                       "Changes put back")
MIGRATED, REJECTED, OTHER_EDITS = "Migrated", "Rejected", "Other edits you asked for"
LEFT, COULD_NOT, OTHER = "Left in place, and why", "Could not do", "Other notes"
EVERY_UNIT_UNDONE = "Every unit of the crashed run was undone. The next migration run does that work again."
WHY = {"copy-mismatch": "its copy didn't match its record.",
       "migrator-stopped": "the migrator stopped before writing it whole.",
       "verifier-failed": "the migration-verifier couldn't check it.",
       "pointer-miss": "its source line changed before its pointer was written.",
       "edit-undone": "the run's edit to this line was undone, so the copy made from the edited line came out too.",
       "chain-undone": "it changed a line the run had already edited, and that earlier edit was undone."}


def is_comment(text):
    return text.lstrip().startswith("%%")


def _note_only(source):
    """A `could_not` source naming a story note and no line (CONTRACT.md 5.3 item 2)."""
    return isinstance(source, dict) and "line" not in source and "text" not in source


def is_trigger(text):
    """A trigger line (CONTRACT.md 5.2 items 2 and 3): the start of a comment, or a bullet holding a status
    tag or an inline comment, not one of the lines the scan skips (5.2 item 5)."""
    if is_comment(text):
        return True
    m = BULLET.match(text)
    return bool(m) and not skipped_bullet(m) and bool(STATUS_TAG.search(text) or "%%" in text)


def comment_blocks(lines):
    """Each comment block in a note's body: (its first line's index, its whole text, line breaks kept)."""
    out, i = [], frontmatter_end(lines)
    while i < len(lines):
        if is_comment(lines[i]):
            block = rs.comment_under(lines, i - 1)
            out.append((i, block))
            i += block.count("\n") + 1
        else:
            i += 1
    return out


class Run:
    """What the run left in its folder, read once: batches, records, the unit index, flags, and the working
    files the batch cycle and `act` kept for the log."""

    def __init__(self, project, state, run):
        self.project, self.state, self.run = project, state, run
        self.name = rs.project_name(project)
        self.batches = cycle.load_working(project, run, "batches.json", {"batches": [], "skipped": []})
        self.records = {}  # batch number -> record, for each batch whose record was used
        for k in range(1, len(self.batches.get("batches", [])) + 1):
            path = os.path.join(project, ".runs", "units", f"{run['id']}-b{k}.json")
            if os.path.isfile(path):
                self.records[k] = rs.load_json(path, f"record file for batch {k}")
        self.find = cycle.record_units(project, run)
        self.entries = [e for e in state["unit_index"] if e.get("run") == run["id"]]
        self.counted = [(e["unit"], f[1]) for e in self.entries
                        if e.get("state") in COUNTED and (f := self.find(e["unit"]))]
        self.undone = [e["unit"] for e in self.entries if e.get("state") == "undone"]
        first = run.get("first_check")
        self.first = load_flags(project, run, first) if first and os.path.isfile(
            cycle.run_file(project, run, f"flags-{first}.json")) else []
        self.missed = cycle.load_working(project, run, "missed.json", [])
        self.restored = cycle.load_working(project, run, "restored.json", [])
        self.why = cycle.load_working(project, run, cycle.UNDONE_WHY, {})
        self.lines, self.snaps, self._named = {}, {}, None
        verify = cycle.load_working(project, run, "verify-flags.json", {"flags": []})
        findings = cycle.load_working(project, run, "findings-flags.json", {"flags": []})
        asked = {e.get("flag"): e.get("asked_by") for e in findings.get("flags", []) if e.get("verdict") == "asked"}
        # An asked flag verify-flags.json doesn't hold stood on its approved unit (spec-migration-verifier.md
        # 06 item 7); the log names what asked for it from the unit's trigger (CONTRACT.md 5.6 item 6).
        judged = {f.get("id") for f in verify.get("flags", [])}
        self.asked = [(f, asked[f.get("id")] if f.get("id") in judged or not f.get("unit") else stood_by(self, f))
                      for f in self.first if f.get("id") in asked]
        # The texts a source line may read at close, after this run's edits that weren't undone
        # (CONTRACT.md 5.4 item 9; 5.6 item 3).
        self.forms = undo.edit_forms(state, run, self.find)

    def link(self, note):
        return note_link(self.name, note or "")

    def note_lines(self, note):
        """The note's lines at close, or None when it is gone."""
        if note not in self.lines:
            path = os.path.join(self.project, note)
            self.lines[note] = ln.read_note(path).lines if os.path.isfile(path) else None
        return self.lines[note]

    def snap(self, note):
        if note not in self.snaps:
            self.snaps[note] = undo._snap_lines(self.project, self.run, note)
        return self.snaps[note]

    def record_lists(self, key):
        return [e for _, r in sorted(self.records.items()) for e in r.get(key, [])]

    def could_not_notes(self):
        """The story notes a `could_not` entry names with no line: the run couldn't read them, so every line
        of each stays off the handled list (spec-run-manager.md 07.1 item 14; 11 item 105)."""
        return {e["source"]["note"] for e in self.record_lists("could_not") if _note_only(e.get("source"))}

    def could_not_lines(self):
        """The lines a `could_not` entry names; only these stay off (07.1 item 14)."""
        return [e["source"] for e in self.record_lists("could_not")
                if isinstance(e.get("source"), dict) and not _note_only(e["source"])]

    def named(self):
        """Every line the record or the findings name, as (note, text): a unit's sources and edits' `before`,
        and each left_in_place, questions, missed, and could_not line (07.1 items 8 and 15)."""
        if self._named is not None:
            return self._named
        out = self._named = set()
        for record in self.records.values():
            for u in record.get("units", []):
                out |= {(s["note"], s["text"]) for s in u["sources"]}
                out |= {(e["note"], e["before"]) for e in u["edits"]}
        for e in self.record_lists("left_in_place") + self.record_lists("questions") + self.missed:
            if isinstance(e.get("source"), dict):
                out.add((e["source"]["note"], e["source"]["text"]))
        out |= {(s["note"], s["text"]) for s in self.could_not_lines()}
        return out

    def accounted(self, note, comment):
        """Whether the record accounts for a comment handed to the migrator (spec-run-manager.md 07.1 item 15;
        11 item 106): a unit's `trigger` holds its words; or the record names the line directly above it;
        or, for a comment on its own, not directly under a bullet, the record names any line in its piece."""
        if any(u["trigger"]["kind"] in ("comment", "request") and u["trigger"]["text"]
               and u["trigger"]["text"] in comment["text"] for rec in self.records.values() for u in rec.get("units", [])):
            return True
        snap, named = self.snap(note), self.named()
        above = snap[comment["line"] - 2] if 2 <= comment["line"] <= len(snap) + 1 else ""
        if BULLET.match(above):
            return (note, above) in named
        piece = self.piece_of({"note": note, "text": comment["text"].split("\n")[0], "line": comment["line"]})
        return any(n == note and self.piece_of({"note": n, "text": t, "line": 0}) == piece for n, t in named)

    def sources(self, sources):
        """Source lines quoted in code marks, each with its note's link."""
        return " and ".join(f"{quote(s['text'])} in {self.link(s['note'])}" for s in sources)

    def destinations(self, unit):
        return ", ".join(self.link(n) for n in dict.fromkeys(c["note"] for c in unit["copies"]))

    def piece_of(self, s):
        return piece_key(self.snap(s["note"]), s)

    def piece_comments(self, key):
        return piece_comments(self.batches, key)

    def source_line(self, s):
        """Where a source line sits at close, found as the handled list finds it (CONTRACT.md 5.4 item 9),
        or None."""
        lines = self.note_lines(s["note"])
        return None if lines is None else undo.locate(self.snap(s["note"]), lines, s["text"], s["line"],
                                                      self.forms(s["note"], s["text"]))


# ---------------------------------------------------------------- the handled list

class Handled:
    """The handled entries a run adds at close (spec-run-manager.md 04 item 20; 07.1; CONTRACT.md 5.6 items 3
    and 4). Lines are found in the notes as they read at close, so each entry's text is the line's text
    then. A place in a note is claimed once: a line counted twice gets one entry."""

    def __init__(self, r):
        self.r, self.found, self.excluded, self.written_used = r, {}, set(), {}
        self.skip_notes = r.could_not_notes()

    def writer_line(self, note, text, line):
        """A line that was in the note when the run started, found by its bare text, the snapshot telling
        identical lines apart (spec-run-manager.md 08.1 item 1). A line this run's edits changed is found
        by their `after` (CONTRACT.md 5.4 item 9)."""
        return self.r.source_line({"note": note, "text": text, "line": line})

    def written_line(self, note, text):
        """A line the run wrote: one with this text the snapshot doesn't explain, else any not yet taken."""
        lines = self.r.note_lines(note)
        if lines is None:
            return None
        used = self.written_used.setdefault(note, set())
        _, new, _ = ln.align(self.r.snap(note), lines)
        hits = [k for k in sorted(new) if lines[k] == text and k not in used]
        hits = hits or [k for k, t in enumerate(lines) if t == text and k not in used]
        if not hits:
            return None
        used.add(hits[0])
        return hits[0]

    def comment_line(self, note, text, line):
        """A comment block from the batches file: the one at the same place among blocks with its text as in
        the snapshot."""
        lines = self.r.note_lines(note)
        if lines is None:
            return None
        rank = sum(1 for i, t in comment_blocks(self.r.snap(note)) if t == text and i < line - 1)
        hits = [i for i, t in comment_blocks(lines) if t == text]
        return hits[rank] if rank < len(hits) else None

    def add(self, note, pos, outcome):
        if pos is None or note in self.skip_notes or (note, pos) in self.excluded or (note, pos) in self.found:
            return
        lines = self.r.note_lines(note)
        text = rs.comment_under(lines, pos - 1) if is_comment(lines[pos]) else lines[pos]
        self.found[(note, pos)] = (outcome, text)

    def build(self):
        r = self.r
        # Never: lines of undone units, nor a missed line. A source line an undone unit shares with a
        # counted unit stays off too, so the next run retries the undone unit (spec-run-manager.md 11
        # items 81 and 83, superseding item 79; CONTRACT.md 5.6 item 3). Every comment in a piece holding
        # one of these lines stays off, so the next run hands the piece to the migrator again.
        held, held_pieces = [], set()
        for key in r.undone:
            found = r.find(key)
            held += found[1]["sources"] if found else []
        held += [m["source"] for m in r.missed if isinstance(m.get("source"), dict)]
        # A could_not line is retried as a missed line is, and so are its piece's comments
        # (spec-run-manager.md 07.1 items 9 and 14; 11 items 105 and 107).
        held += r.could_not_lines()
        for s in held:
            pos = self.writer_line(s["note"], s["text"], s["line"])
            if pos is not None:
                self.excluded.add((s["note"], pos))
            held_pieces.add(r.piece_of(s))
        for _, unit in r.counted:
            if unit["action"] == "migrate":
                for s in unit["sources"]:
                    self.add(s["note"], self.writer_line(s["note"], s["text"], s["line"]), "migrated")
        for _, unit in r.counted:
            for c in unit["copies"]:
                for t in (t for t in c["lines"] if t.strip()):
                    pos = self.written_line(c["note"], t)
                    if not is_trigger(t):
                        continue
                    rejected = unit["action"] == "reject" and not is_comment(t)
                    self.add(c["note"], pos, "rejected" if rejected else "written")
        for _, unit in r.counted:
            for e in unit["edits"]:
                self.add(e["note"], self.written_line(e["note"], e["after"]), "edited")
            if unit["action"] == "edit":
                for s in unit["sources"]:
                    self.add(s["note"], self.writer_line(s["note"], s["text"], s["line"]), "edited")
        for e in r.record_lists("left_in_place") + r.record_lists("questions"):
            s = e.get("source")
            if isinstance(s, dict):
                self.add(s["note"], self.writer_line(s["note"], s["text"], s["line"]), "left in place")
        for k, batch in enumerate(r.batches.get("batches", []), 1):
            if k not in r.records:
                continue  # a batch-failed batch's lines stay off (spec-run-manager.md 07.1 item 9)
            for piece in batch["pieces"]:
                if (piece["note"], piece["heading"]) in held_pieces:
                    continue
                for l in (l for l in piece["lines"] if is_comment(l["text"])):
                    if r.accounted(piece["note"], l):  # 07.1 item 15
                        self.add(piece["note"], self.comment_line(piece["note"], l["text"], l["line"]), "comment")
        run_id = r.run["id"]
        out = []
        for (note, pos), (outcome, text) in sorted(self.found.items()):
            links = list(dict.fromkeys(p for p, _, _ in undo.pointer_links(text, r.name)))
            out.append({"note": note, "text": text, "outcome": outcome, "run": run_id, "pointer": links or None})
        return out

    def skipped(self, handled):
        """A skipped pointer line's handled entry gets the line's text at close (CONTRACT.md 5.6 item 4).
        Returns each skipped line's text at close, for the log."""
        texts, done = [], set()
        for s in self.r.batches.get("skipped", []):
            lines = self.r.note_lines(s["note"])
            snap = self.r.snap(s["note"])
            i = ln.snapshot_index(snap, s["text"], s["line"])
            pos = None if lines is None or i is None else ln.find_same_line(snap, i, lines, {s["text"]})
            now = s["text"] if pos is None else lines[pos]
            texts.append((s, now))
            if pos is None:
                continue
            for k, e in enumerate(handled):
                if k not in done and e.get("note") == s["note"] and e.get("text") == s["was"]:
                    e["text"] = now
                    done.add(k)
                    break
        return texts


def nothing_done_lines(r):
    """Batch lines the run did nothing with: tagged lines nothing names, no unit's source, no left_in_place,
    question, missed, or could_not source; and comments of a batch whose record was used that the record
    doesn't account for. None in a note a could_not entry names with no line (spec-run-manager.md 07.1
    items 8, 14, 15; CONTRACT.md 5.6 item 3)."""
    named, skip = r.named(), r.could_not_notes()
    out = []
    for k, batch in enumerate(r.batches.get("batches", []), 1):
        for piece in batch["pieces"]:
            for l in piece["lines"]:
                if piece["note"] in skip:
                    continue
                if is_comment(l["text"]):
                    if k in r.records and not r.accounted(piece["note"], l):
                        out.append((piece["note"], l["text"].strip()))
                elif (piece["note"], l["text"]) not in named:
                    out.append((piece["note"], l["text"]))
    return out


def carry_over(r, handled):
    """Bring each handled entry the scan matched by its link targets left out, or to a line in another
    story note, up to date: its `text` the line as it reads now, its `note` and `pointer` the new paths
    (spec-run-manager.md 04 item 20; 07.1 item 13; CONTRACT.md 5.6 item 4). The entry keeps its place,
    outcome, and run. Returns how many entries moved from each old note to each new one."""
    moved, finder = {}, Handled(r)
    for c in cycle.load_working(r.project, r.run, CARRIED, []):
        k = c.get("entry")
        if not isinstance(k, int) or not 0 <= k < len(handled) or handled[k].get("text") != c.get("was"):
            continue
        note = c["note"]
        if is_comment(c["text"]):
            pos = finder.comment_line(note, c["text"], c["line"])
        else:
            pos = r.source_line({"note": note, "text": c["text"], "line": c["line"]})
        lines = r.note_lines(note)
        text = c["text"] if pos is None else (rs.comment_under(lines, pos - 1) if is_comment(lines[pos]) else lines[pos])
        e = handled[k]
        if e.get("note") != note:
            moved[(e.get("note"), note)] = moved.get((e.get("note"), note), 0) + 1
        links = list(dict.fromkeys(p for p, _, _ in undo.pointer_links(text, r.name)))
        e.update(text=text, note=note, pointer=links or None)
    return moved


# ---------------------------------------------------------------- the request comments

def request_comment(run, line):
    """The writer's typed request as a comment for one line, indented one level below it
    (spec-run-manager.md 11 item 96)."""
    return (f"{rs.indent_of(line)}    %% [AGENT] Your request from the migration run of {run['started'][:10]}, "
            f'for this line: "{run["request"]}" %%')


def request_sources(r):
    """The lines that get the request comment, with a typed request (spec-run-manager.md 11 item 96): each
    source line of an undone unit whose `trigger` kind is `request`, and each missed line with no status
    tag. Their pieces stay off the handled list already (CONTRACT.md 5.6 item 3)."""
    if not r.run.get("request"):
        return []
    out = []
    for key in r.undone:
        found = r.find(key)
        if found and found[1]["trigger"]["kind"] == "request":
            out += found[1]["sources"]
    out += [m["source"] for m in r.missed
            if isinstance(m.get("source"), dict) and not STATUS_TAG.search(m["source"]["text"])]
    return out


def _comments_under(lines, i):
    """The comment blocks that sit one after another directly under line i."""
    out, j = [], i + 1
    while j < len(lines) and is_comment(lines[j]):
        block = rs.comment_under(lines, j - 1)
        out += block.split("\n")
        j += block.count("\n") + 1
    return out


def write_request_comments(r, sources):
    """Write the request comment on the line directly under each source line, above any comment already
    there, as a research link line goes (spec-run-manager.md 08.4 item 1; 11 item 96). Where the same
    comment already sits under the line, from an earlier run, it isn't written again. Written at close,
    after the last Edit guard check, and never put on the handled list, so the next scan finds it.
    Returns the sources that now have the comment under them, as (note, line, text); a line close can't
    find gets none."""
    placed, inserts = set(), {}
    for s in sources:
        pos = r.source_line(s)
        if pos is None:
            continue
        lines = r.note_lines(s["note"])
        placed.add((s["note"], s["line"], s["text"]))
        want = request_comment(r.run, lines[pos])
        if want not in _comments_under(lines, pos):
            inserts.setdefault(s["note"], {})[pos] = want
    for note, at in inserts.items():
        path = os.path.join(r.project, note)
        n = ln.read_note(path)
        for pos in sorted(at, reverse=True):
            n.insert(pos + 1, at[pos])
        ln.write_note(path, n)
        r.lines.pop(note, None)
    return placed


def _piece_comments(r, sources):
    """Each comment in the sources' pieces, once, in note order, mapped to its piece's note."""
    out = {}
    for s in sources:
        key = r.piece_of(s)
        for c in r.piece_comments(key):
            out.setdefault(c, key[0])
    return out


def _trigger_comment(comments, trigger):
    """The one comment whose words hold the trigger's text, or None when none or more than one does
    (spec-run-manager.md 11 item 97)."""
    hits = [c for c in comments if trigger is not None and trigger in c]
    return hits[0] if len(hits) == 1 else None


def keep_lines(r, sources, trigger=None):
    """A "Keep your comment `…` until this migrates." line for each comment that brings the work back
    (spec-run-manager.md 11 items 93 and 97): the one comment in the sources' pieces whose words hold the
    trigger's text, or every comment in those pieces when no single one does or there is no trigger."""
    comments = _piece_comments(r, sources)
    hit = _trigger_comment(comments, trigger)
    return [KEEP.format(quote(c.strip())) for c in ([hit] if hit else comments)]


def stood_by(r, f):
    """What asked for a flag that stood on its approved unit, in the shape of a judged flag's `asked_by`
    (spec-migration-verifier.md 06 item 7; plan-run-manager.md 06 item 14 (1)): the typed request, or the
    one comment in the unit's pieces holding the trigger's text, whole and with its note, as keep lines
    find it; when no single comment holds it, the trigger's text, with no note."""
    found = r.find(f["unit"])
    if found is None:
        return {"kind": "comment", "note": "", "text": ""}
    unit = found[1]
    trigger = unit["trigger"]
    if trigger["kind"] == "request":
        return {"kind": "request", "note": "", "text": trigger["text"]}
    comments = _piece_comments(r, unit["sources"])
    hit = _trigger_comment(comments, trigger["text"])
    if hit is None:
        return {"kind": "comment", "note": "", "text": trigger["text"]}
    return {"kind": "comment", "note": comments[hit], "text": hit.strip()}


def request_written(r, sources, placed):
    return [REQUEST_WRITTEN.format(quote(s["text"])) for s in sources if (s["note"], s["line"], s["text"]) in placed]


# ---------------------------------------------------------------- the run log

def _nested(items, depth=1):
    pad = "    " * depth
    return "".join(f"\n{pad}- {x}" for x in items)


def _flag_line(f):
    return f.get("after") or f.get("before") or ""


def put_back_items(r):
    out = []
    for f in r.restored:
        link = r.link(f["note"])
        if f.get("how") == "changed back":
            out.append(f"- In {link}, a changed line was put back. It read {quote(f['after'])}, "
                       f"and reads {quote(f['before'])} again.")
        elif f.get("how") == "removed":
            out.append(f"- In {link}, an added line was removed: {quote(f['after'])}.")
        else:
            out.append(f"- In {link}, a removed line was put back: {quote(f['before'])}.")
    return out


def miss_items(r):
    """Undo and restore misses, one bullet each (CONTRACT.md 5.6 item 6)."""
    out = []
    for m in cycle.load_working(r.project, r.run, "undo-misses.json", []):
        out.append(f"- In {r.link(m['note'])}, undo couldn't find {quote(m['text'])} from unit {m['unit']}, "
                   "so it was left alone.")
    for m in cycle.load_working(r.project, r.run, "restore-misses.json", []):
        out.append(f"- In {r.link(m.get('note'))}, a flagged line couldn't be found to put back, so it was left "
                   f"alone: {quote(m.get('after') or m.get('before') or '')}.")
    return out


def changed_outside(r, flags):
    return [f"- {r.link(f.get('note'))} changed outside the run (`fingerprint-changed`)."
            for f in flags if f.get("rule") == "fingerprint-changed"]


def undone_items(r, placed):
    out = []
    for key in r.undone:
        found = r.find(key)
        if found is None:
            out.append(f"- Unit {key} was undone.{_nested([NEXT_RUN])}")
            continue
        unit, why = found[1], r.why.get(key, {})
        parts = [f"Its copies went to {r.destinations(unit)}."] if unit["copies"] else []
        kind = why.get("why")
        if kind == "fix-rounds":
            problems = [f"{p['check']}: {p['what']}" for p in why.get("problems", [])]
            parts.append("It was undone because the migration-verifier still found problems after 2 fix rounds:"
                         + _nested(problems, 2))
        elif kind == "not-asked":
            f = why.get("flag", {})
            parts.append("It was undone because a change it made wasn't asked for:"
                         + _nested([f"`{f.get('rule')}`: {quote(_flag_line(f))}"], 2))
        elif kind in WHY:
            parts.append(f"It was undone because {WHY[kind]}")
        # The comment or request that brings the work back (spec-run-manager.md 11 items 93, 96, 97).
        trigger = unit["trigger"]
        if trigger["kind"] == "comment":
            parts += keep_lines(r, unit["sources"], trigger["text"])
        elif trigger["kind"] == "request":
            parts += request_written(r, unit["sources"], placed)
        parts.append(NEXT_RUN)
        out.append(f"- {r.sources(unit['sources'])}.{_nested(parts)}")
    return out


def other_edit_items(r):
    """Edit units, each naming what asked for it; then other flags judged asked for or that stood on an
    approved unit, each naming the comment or request in the same words (spec-run-manager.md 07.3 item 2,
    entry 4; 05 item 8)."""
    def asker(a):
        if a.get("kind") == "request":
            return "your typed request"
        where = f" in {r.link(a['note'])}" if a.get("note") else ""
        return f"your comment {quote(a.get('text', ''))}{where}"

    out, covered = [], set()
    for key, unit in r.counted:
        if unit["action"] != "edit":
            continue
        by = next((a for f, a in r.asked if f.get("unit") == key), None)
        covered |= {id(f) for f, a in r.asked if f.get("unit") == key}
        if by:
            who = asker(by)
        elif unit["trigger"]["kind"] == "request":
            who = "your typed request"
        else:
            who = f"your comment {quote(unit['trigger']['text'])}"
        for e in unit["edits"]:
            out.append(f"- In {r.link(e['note'])}, {quote(e['before'])} now reads {quote(e['after'])}, as {who} asked.")
    for f, a in r.asked:
        # A flag judged asked whose unit was undone anyway (another flag on it, or 5.3 item 13) stands no more.
        if id(f) not in covered and f.get("unit") not in r.undone:
            out.append(f"- In {r.link(f.get('note'))}, {quote(_flag_line(f))} stands (`{f.get('rule')}`), "
                       f"as {asker(a)} asked.")
    return out


def missed_items(r, placed):
    """Each missed line, what the migration-verifier says, and for a line with no status tag, which only a
    comment or the request could have asked for, the comments to keep and the request comment written
    (spec-run-manager.md 07.3 item 2, entry 8; 11 items 93, 96, 97)."""
    out = []
    for m in r.missed:
        s, parts = m["source"], [m["what"]]
        if not STATUS_TAG.search(s["text"]):
            parts += keep_lines(r, [s]) + request_written(r, [s], placed)
        out.append(f"- {r.sources([s])}.{_nested(parts + [NEXT_RUN])}")
    return out


def run_log(r, second, skipped, placed, moved=None):
    run = r.run
    questions = [f"- {r.sources([e['source']])}.{_nested([e['ask'], ANSWER])}"
                 for e in r.record_lists("questions") if isinstance(e.get("source"), dict)]
    missed = missed_items(r, placed)
    migrated, rejected = [], []
    for _, unit in r.counted:
        if unit["action"] == "migrate":
            migrated.append(f"- {r.sources(unit['sources'])} went to {r.destinations(unit)}. "
                            f"Status: {unit['status']}. {unit['why']}")
        elif unit["action"] == "reject":
            rejected.append(f"- {r.sources(unit['sources'])} moved to {r.destinations(unit)}'s Rejected section. "
                            f"{unit['why']}")
    left = [f"- {r.sources([e['source']])}: {e['why']}" for e in r.record_lists("left_in_place")]
    could_not = [f"- {r.link(e['source']['note'])}: {e['what']}" if _note_only(e.get("source"))
                 else f"- {r.sources([e['source']])}: {e['what']}" if isinstance(e.get("source"), dict)
                 else f"- {e['what']}" for e in r.record_lists("could_not")]

    other = []
    for s, now in skipped:
        other.append(f"- In {r.link(s['note'])}, {quote(now)} has a pointer and only its words changed, so the "
                     "run skipped it.")
    for note, text in nothing_done_lines(r):
        other.append(f"- {quote(text)} in {r.link(note)}: the run did nothing with it. The next migration run "
                     "tries it again.")
    for rn in r.batches.get("renamed", []):  # spec-run-manager.md 07.1 item 12; 07.3 item 2 entry 10
        n = (moved or {}).get((rn["from"], rn["to"]), 0)
        other.append(f"- {quote(rn['from'])} looks renamed to {quote(rn['to'])}. Its {n} handled "
                     f"{'line' if n == 1 else 'lines'} carried over.")
    other += changed_outside(r, r.first)
    for m in cycle.load_working(r.project, run, "pointer-misses.json", []):
        other.append(f"- In {r.link(m['note'])}, {quote(m['text'])} changed before its pointer was written, so "
                     f"unit {m['unit']} was undone.")
    other += miss_items(r)
    named = {(f.get("rule"), f.get("note")) for f in r.first if f.get("rule") == "fingerprint-changed"}
    for f in second or []:
        if (f.get("rule"), f.get("note")) in named:
            continue  # already named (CONTRACT.md 5.6 item 2)
        line = _flag_line(f)
        other.append(f"- {r.link(f.get('note'))} is still flagged after the second check (`{f.get('rule')}`)"
                     + (f": {quote(line)}." if line else "."))

    head = [f"Migration run, started {run['started']}."]
    if run.get("request"):
        head.append(f'Your request: "{run["request"]}"')
    # Only the questions ask the writer for anything; "Nothing needs you." means there are none
    # (spec-run-manager.md 07.3 item 2; 11 item 81; CONTRACT.md 5.6 item 6).
    sections = [(QUESTIONS, questions), (MIGRATED, migrated), (REJECTED, rejected), (OTHER_EDITS, other_edit_items(r)),
                (LEFT, left), (COULD_NOT, could_not), (UNDONE, undone_items(r, placed)), (MISSED, missed),
                (PUT_BACK, put_back_items(r)), (OTHER, other)]
    return _log(run["id"], run["started"], "migration", head, sections, bool(questions))


def recover_log(r):
    run = r.run
    flags = []
    n = run.get("recover_check")
    if n and os.path.isfile(cycle.run_file(r.project, run, f"flags-{n}.json")):
        flags = load_flags(r.project, run, n)
    other = miss_items(r) + changed_outside(r, flags)
    for f in flags:
        if f.get("rule") not in ("unexplained-change", "fingerprint-changed"):
            line = _flag_line(f)
            other.append(f"- {r.link(f.get('note'))} was flagged (`{f.get('rule')}`)"
                         + (f": {quote(line)}." if line else "."))
    if run.get("markup_unchecked"):
        other.append(f"- {MARKUP_UNCHECKED}")
    when = run["recover_started"]
    log_id = f"run-{when[:10]}-{when[11:13]}{when[14:16]}-recover"
    head = [f"Recover run, for {run['id']}.", "", EVERY_UNIT_UNDONE]
    put_back = put_back_items(r)
    # "Nothing needs you." when Changes put back is empty (CONTRACT.md 5.6 item 8).
    return _log(log_id, when, "recover", head, [(PUT_BACK, put_back), (OTHER, other)], bool(put_back))


def _log(log_id, when, kind, head, sections, needs_you):
    out = ["---", f"title: Run - {when[:10]} {when[11:13]}{when[14:16]} {kind}", "type: [run-log]",
           f"created: {when[:10]}", "---", "", *head, ""]
    if not needs_you:
        out += ["Nothing needs you.", ""]
    for heading, items in sections:
        if items:  # an empty section is left out (spec-run-manager.md 07.3 item 2)
            out += [f"## {heading}", "", *items, ""]
    return log_id + ".md", "\n".join(out)


# ---------------------------------------------------------------- close

def close(project, state):
    """`close` (needs `acted`, and the awaited flags file when `next_check` is set): read the second check's
    flags, build the handled entries, write the run log, add the history entry, clear the open run, and
    prune the snapshots (CONTRACT.md 5.6 item 1). A recovering run adds nothing to the handled list and
    writes the recover log (5.6 item 8). With a typed request, the request is written as a comment under
    each line of the request's undone or missed work, or, on a recovering run, of every unit it started
    (spec-run-manager.md 09.2 item 3; 11 item 96)."""
    run = cycle.migration_run(state, "acted")
    second = load_flags(project, run, run["next_check"]) if run.get("next_check") is not None else None
    ended = st.now().strftime(st.CLOCK_FORMAT)
    r = Run(project, state, run)
    if run.get("recovering"):
        write_request_comments(r, recover.request_sources(project, run))
        log_name, text = recover_log(r)
    else:
        handled = Handled(r)
        new = handled.build()
        moved = carry_over(r, state["handled"])
        skipped = handled.skipped(state["handled"])
        state["handled"] += new
        # After the handled list, so the comments stay off it (spec-run-manager.md 07.1 item 3).
        placed = write_request_comments(r, request_sources(r))
        log_name, text = run_log(r, second, skipped, placed, moved)
    runs = os.path.join(project, "Runs")
    os.makedirs(runs, exist_ok=True)
    write_note_whole(os.path.join(runs, log_name), text)
    entry = {"id": run["id"], "kind": "migration", "run_number": None, "started": run["started"],
             "ended": ended, "how": "recovered" if run.get("recovering") else "closed"}
    if not run.get("recovering"):
        entry["renamed"] = r.batches.get("renamed", [])  # for record's guard (spec-run-manager.md 04 item 17)
    state["history"].append(entry)
    state["open_run"] = None
    st.save_state(project, state)
    snapshot.prune(project)
    return f"run log: Runs/{log_name}"
