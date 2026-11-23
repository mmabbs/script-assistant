"""Explains each change, or leaves it unexplained (spec-edit-guard.md 03.2).

A change is explained by:
  1. a `copies` line in a unit record, in the note the record names
  2. an `edits` entry, with `before` matching the snapshot and `after` matching the note; when the line
     also carries a pointer the Run manager wrote for a `migrate` unit with that source line, the edit
     explains the line and the pointer is a Run manager edit (runmanager CONTRACT.md 5.4 item 9); several
     entries that changed the line in turn explain it together, each its own step (5.4 item 11)
  3. a `sources` line of a `reject` unit, removed from the live part of its note
  4. a Run manager edit, only where the Run manager makes it:
     - a pointer on a source line of a `migrate` unit that isn't undone (a removed `[?]` only with it)
     - a research link line or a close on a research run, at a request in the requests file
Requests are found by their snapshot text, so a reworded request still owns the line under it
(spec-edit-guard.md 04 item 6). Each change is matched only against entries for its own note. Undone units are skipped.
"""
import json
import os
import re
from dataclasses import dataclass, field

from .compare import Hunk, RMEdit, pair_in_order, strip_candidates
from .rules_research import indent_of, link_line_target

RECORD_NAME = re.compile(r"^(?P<run>.+)-b(?P<batch>\d+)\.json$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
# "An [AGENT] line is one whose text after the list marker and any checkbox starts with `[AGENT] `"
# (spec-edit-guard.md 04 item 5).
AGENT_LINE = re.compile(r"^\s*(?:(?:[-*+]|\d+[.)])\s+)?(?:\[.\]\s+)?\[AGENT\] ")
# A request line, open or closed. Used to pair a reworded request with its line now.
REQUEST_LIKE = re.compile(r"^\s*- \[[rx]\] ")
CLOSED_LINE = re.compile(r"^\s*- \[x\] ")


class InputError(Exception):
    """An input that passed the shape check but still can't be used. Ends the check like a crash."""


@dataclass
class Unit:
    run: str
    key: str            # batch and unit id, such as b1-u2 (spec-run-manager.md 07.2 item 6)
    data: dict          # the unit's entry in its record file
    state: str | None   # from the unit index; None when the index doesn't list it

    @property
    def active(self):
        return self.state != "undone"


@dataclass
class Context:
    kind: str                 # "migration" or "research"
    project_name: str         # the --project folder's own name, used in research link lines
    units: list = field(default_factory=list)      # every unit in the handed-over records, undone ones included
    requests: list = field(default_factory=list)   # research runs: the requests file
    outcomes: list = field(default_factory=list)   # research runs: the outcomes file
    fingerprints: dict = field(default_factory=dict)  # both run kinds: note path -> SHA-256 of the whole file


@dataclass
class Change:
    note: str
    before: str               # "" for an added line
    after: str                # "" for a removed line
    before_line: int | None   # line number in the snapshot copy
    after_line: int | None    # line number in the note now
    seq: int                  # order the change was found in, across all notes
    rm_edit: RMEdit | None = None


@dataclass
class Explained:
    change: Change
    how: str            # "copy", "edit", "reject-source", "pointer", "link-line", or "close"
    unit: str           # the unit that explains it, such as b1-u2, or "" (research runs)
    run: str            # that unit's run, or ""
    entry: dict         # the record entry or request that explains it
    # link lines: "under" (right under its request) and "request_line". Edits: "snap" and "now", the
    # snapshot Line and the Line now, and "pointer", the RMEdit when a pointer was written on the line too.
    info: dict = field(default_factory=dict)


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_context(args):
    """Read what explaining needs. The shapes were already checked by inputs.check_inputs."""
    ctx = Context(kind=args.kind, project_name=os.path.basename(os.path.normpath(os.path.abspath(args.project))))
    ctx.fingerprints = _load(args.fingerprints)
    if args.kind == "research":
        ctx.requests = _load(args.requests)
        ctx.outcomes = _load(args.outcomes)
        return ctx
    # A unit is found by its run and its unit key together (spec-edit-guard.md 03.2 item 5).
    # The Edit guard reads only unit_index from the run state.
    states = {(e["run"], e["unit"]): e["state"] for e in _load(args.run_state)["unit_index"]}
    named = []
    for path in args.records:
        m = RECORD_NAME.match(os.path.basename(path))
        if not m:
            raise InputError(f"{path}: file name is not {{run-id}}-b{{N}}.json, so its units can't be named")
        named.append((m.group("run"), int(m.group("batch")), path))
    for run, batch, path in sorted(named):
        for u in _load(path)["units"]:
            key = f"b{batch}-{u['id']}"
            ctx.units.append(Unit(run, key, u, states.get((run, key))))
    return ctx


def _rejected_section(lines):
    """Return the body positions that sit in a section headed "Rejected" (spec-edit-guard.md 04 item 4)."""
    inside, stack = set(), []
    for l in lines:
        m = HEADING.match(l.text)
        if m:
            level = len(m.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, m.group(2)))
            continue
        if any(title == "Rejected" for _, title in stack):
            inside.add(l.idx)
    return inside


def _comment_lines(lines):
    """Return the body positions of comment lines: a line that opens with %%, or sits inside a %% block."""
    out, open_ = set(), False
    for l in lines:
        if open_ or l.text.lstrip().startswith("%%"):
            out.add(l.idx)
        if l.text.count("%%") % 2:
            open_ = not open_
    return out


class _Pools:
    """The record entries for each note, from units that aren't undone. Copies, edits, and reject
    sources are used up as they explain a line, so one entry explains one line."""

    def __init__(self, ctx):
        self.copies, self.edits, self.rejects, self.pointed = {}, {}, {}, {}
        for u in ctx.units:
            if not u.active:
                continue
            d = u.data
            for c in d.get("copies") or []:
                for text in c.get("lines") or []:
                    if text.strip():  # blank lines are not recorded (spec-migrator.md 05.5 item 7)
                        self.copies.setdefault(c["note"], []).append([text, u, c, False])
            for e in d.get("edits") or []:
                self.edits.setdefault(e["note"], []).append([e["before"], e["after"], u, e, False])
            for s in d.get("sources") or []:
                if d.get("action") == "reject":
                    self.rejects.setdefault(s["note"], []).append([s["text"], u, s, False])
                elif d.get("action") == "migrate":
                    self.pointed.setdefault(s["note"], []).append([s["text"], u, s])

    @staticmethod
    def take(pool, match):
        for entry in pool:
            if not entry[-1] and match(entry):
                entry[-1] = True
                return entry
        return None


def recorded_lines(ctx):
    """For each note, the texts the run's records remove from it (a `reject` unit's sources) and add to
    it (copies), from units that aren't undone: the two halves of a move the record explains
    (spec-edit-guard.md 03.1 item 3; 03.2 items 1 and 3). The comparison uses them only to choose
    between equally short readings of a note's changes."""
    out = {}
    for u in ctx.units:
        if not u.active:
            continue
        if u.data.get("action") == "reject":
            for s in u.data.get("sources") or []:
                out.setdefault(s["note"], (set(), set()))[0].add(s["text"])
        for c in u.data.get("copies") or []:
            for text in c.get("lines") or []:
                if text.strip():
                    out.setdefault(c["note"], (set(), set()))[1].add(text)
    return out


def _change(note, before, after, seq, rm_edit=None):
    return Change(note,
                  before.text if before else "", after.text if after else "",
                  before.no if before else None, after.no if after else None,
                  seq, rm_edit)


@dataclass
class RequestSpots:
    """Where each of a note's requests sits now, and which added lines are their link lines."""
    paired: dict = field(default_factory=dict)  # snapshot body position -> (request, Line now), reworded requests
    links: dict = field(default_factory=dict)   # body position now -> (request, under, request's Line now)


def _snapshot_line(diff, r, taken):
    """The snapshot line a request names: its text, at its line number when the text repeats."""
    same = [l for l in diff.before if l.text == r["text"] and l.idx not in taken]
    if not same:
        raise InputError(f"requests file: {r['id']}: its text is not in the snapshot of {diff.note}")
    return next((l for l in same if l.no == r["line"]), same[0])


def _locate_requests(ctx, diff, comments):
    """Find each request by its snapshot text, then its line now, then the lines that are its link line.

    A request's line now is its unchanged or closed line, or, when it sits in a changed block, the line
    it pairs with in order among the block's request lines (spec-edit-guard.md 03.1 item 6). Any line
    added right under it is its link line, whatever its form. A settled-form link line added elsewhere in
    its block (the comment lines and deeper-indented lines under it) is its link line too, misplaced.
    Anywhere else a link line is a lookalike (spec-edit-guard.md 04 item 6).
    """
    spots = RequestSpots()
    if ctx.kind != "research":
        return spots
    hunk_of, added = {}, set()
    for item in diff.items:
        if isinstance(item, Hunk):
            for l in item.removed:
                hunk_of[l.idx] = item
            added.update(l.idx for l in item.added)

    now, taken = [], set()
    for r in ctx.requests:
        if r["note"] != diff.note:
            continue
        snap = _snapshot_line(diff, r, taken)
        taken.add(snap.idx)
        if snap.idx in diff.matched:
            now.append((r, diff.after[diff.matched[snap.idx]]))
        elif snap.idx in hunk_of:
            hunk = hunk_of[snap.idx]
            old = [l for l in hunk.removed if REQUEST_LIKE.match(l.text)]
            new = [l for l in hunk.added if REQUEST_LIKE.match(l.text)]
            k = old.index(snap) if snap in old else len(new)
            if k < len(new) and indent_of(new[k].text) == indent_of(snap.text):
                spots.paired[snap.idx] = (r, new[k])
                now.append((r, new[k]))

    request_now = {line.idx for _, line in now}
    for r, line in now:
        j = line.idx + 1
        if j < len(diff.after) and j in added and j not in request_now:
            spots.links[j] = (r, True, line)
        depth = len(indent_of(line.text))
        while j < len(diff.after) and j not in request_now and (
                j in comments or len(indent_of(diff.after[j].text)) > depth):
            if (j in added and j not in spots.links
                    and link_line_target(diff.after[j].text, line.text, ctx.project_name)):
                spots.links[j] = (r, False, line)
            j += 1
    return spots


def _explain_rm_edit(ctx, pools, item):
    """Return (how, unit, entry) when the Run manager edit sits where the Run manager makes it."""
    if item.kind == "pointer" and ctx.kind == "migration":
        for text, u, s in pools.pointed.get(item.note, []):
            if text == item.before.text:
                return "pointer", u, s
    if item.kind == "close" and ctx.kind == "research":
        for r in ctx.requests:
            if r["note"] == item.note and r["text"] == item.before.text:
                return "close", None, r
    return None


def _edited_then_pointed(pools, note, r, a):
    """An edit the run made to a source line, and the pointer `pointers` then wrote on it: the line now
    is an `edits` entry's `after` with a Run manager pointer added, its `before` is the snapshot line, and
    a `migrate` unit that isn't undone has that source line (runmanager CONTRACT.md 5.4 item 9;
    spec-edit-guard.md 03.1 item 2, 03.2 items 2 and 4). Takes the entry from the pool. Returns (the edits
    pool entry, the source's pool entry, the RMEdit) or None."""
    source = next((p for p in pools.pointed.get(note, []) if p[0] == r.text), None)
    if source is None:
        return None
    for base, kind, question, dests in strip_candidates(a.text):
        if kind != "pointer":
            continue
        e = pools.take(pools.edits.get(note, []), lambda en: en[0] == r.text and en[1] == base)
        if e:
            return e, source, RMEdit(note, r, a, "pointer", question, list(dests))
    return None


def _edit_chain(pools, note, r, a):
    """Two or more `edits` entries that changed one line in turn: the first's `before` is the snapshot
    line, each next one's `before` is the last one's `after`, and the last `after` is the line now, or the
    line now with a Run manager pointer stripped when a `migrate` unit that isn't undone has that source
    line (runmanager CONTRACT.md 5.4 item 11). Takes the entries from the pool. Returns (the edits pool
    entries in order, the source's pool entry or None, the RMEdit or None) or None."""
    free = [en for en in pools.edits.get(note, []) if not en[-1]]
    targets = [(a.text, None)]
    source = next((p for p in pools.pointed.get(note, []) if p[0] == r.text), None)
    if source is not None:
        targets += [(base, RMEdit(note, r, a, "pointer", question, list(dests)))
                    for base, kind, question, dests in strip_candidates(a.text) if kind == "pointer"]

    def search(text, path):
        if len(path) > 1:
            for target, rm in targets:
                if text == target:
                    return path, rm
        for en in free:
            if en[0] == text and not any(en is p for p in path):
                found = search(en[1], path + [en])
                if found:
                    return found
        return None

    found = search(r.text, [])
    if found is None:
        return None
    path, rm = found
    for en in path:
        en[-1] = True
    return path, (source if rm else None), rm


def explain(diffs, ctx):
    """Explain every change in the note diffs. Returns (explained, unexplained): a list of Explained
    and a list of Change. Each change lands in exactly one of them."""
    pools = _Pools(ctx)
    explained, unexplained = [], []
    seq = 0

    def done(change, how, unit, entry, info=None):
        explained.append(Explained(change, how, unit.key if unit else "", unit.run if unit else "", entry,
                                   info or {}))

    for diff in diffs:
        rejected = _rejected_section(diff.before)
        comments = _comment_lines(diff.after)
        spots = _locate_requests(ctx, diff, comments)
        for item in diff.items:
            if isinstance(item, RMEdit):
                seq += 1
                change = _change(item.note, item.before, item.after, seq, item)
                found = _explain_rm_edit(ctx, pools, item)
                if found:
                    done(change, *found)
                else:
                    # A lookalike anywhere else is unexplained-change (spec-edit-guard.md 03.2 item 4).
                    unexplained.append(change)
                continue

            assert isinstance(item, Hunk)
            removed, added = list(item.removed), list(item.added)

            # A reworded request still owns its line (spec-edit-guard.md 04 item 6). Closed, it is a close
            # for close-invalid to judge. Still open, it is a changed line no Run manager edit explains.
            for r in list(removed):
                if r.idx in spots.paired:
                    req, a = spots.paired[r.idx]
                    seq += 1
                    if CLOSED_LINE.match(a.text):
                        done(_change(diff.note, r, a, seq), "close", None, req)
                    else:
                        unexplained.append(_change(diff.note, r, a, seq))
                    removed.remove(r)
                    added.remove(a)

            # An edits entry explains a changed line when its before is the snapshot line and its after
            # is the line now (spec-edit-guard.md 03.2 item 2).
            for r in list(removed):
                for a in added:
                    e = pools.take(pools.edits.get(diff.note, []),
                                   lambda en: en[0] == r.text and en[1] == a.text)
                    if e:
                        seq += 1
                        done(_change(diff.note, r, a, seq), "edit", e[2], e[3], {"snap": r, "now": a})
                        removed.remove(r)
                        added.remove(a)
                        break
                    # The edit's line may carry a pointer too: the edit explains the line, with `after`
                    # its own text, and the pointer is the Run manager's (03.1 item 2; 03.2 item 4).
                    hit = _edited_then_pointed(pools, diff.note, r, a)
                    if hit:
                        e, (_, u, s), rm = hit
                        seq += 1
                        done(Change(diff.note, r.text, e[1], r.no, a.no, seq), "edit", e[2], e[3],
                             {"snap": r, "now": a, "pointer": rm})
                        seq += 1
                        done(Change(diff.note, e[1], a.text, r.no, a.no, seq, rm), "pointer", u, s)
                        removed.remove(r)
                        added.remove(a)
                        break
                    # Several of the run's edits changed the line in turn: each entry explains its own
                    # step, with its own before and after, and names its own unit; a pointer on the line
                    # is the Run manager's (runmanager CONTRACT.md 5.4 item 11).
                    hit = _edit_chain(pools, diff.note, r, a)
                    if hit:
                        path, source, rm = hit
                        info = {"snap": r, "now": a, "pointer": rm}
                        for en in path:
                            seq += 1
                            done(Change(diff.note, en[0], en[1], r.no, a.no, seq), "edit", en[2], en[3], info)
                        if rm:
                            _, u, s = source
                            seq += 1
                            done(Change(diff.note, path[-1][1], a.text, r.no, a.no, seq, rm), "pointer", u, s)
                        removed.remove(r)
                        added.remove(a)
                        break

            # Each remaining half is explained on its own, or left for pairing.
            left_removed, left_added = [], []
            for r in removed:
                e = None
                if r.idx not in rejected:  # removed from the live part (03.2 item 3)
                    e = pools.take(pools.rejects.get(diff.note, []), lambda en: en[0] == r.text)
                if e:
                    seq += 1
                    done(_change(diff.note, r, None, seq), "reject-source", e[1], e[2])
                else:
                    left_removed.append(r)
            for a in added:
                e = pools.take(pools.copies.get(diff.note, []), lambda en: en[0] == a.text)
                if e:
                    seq += 1
                    done(_change(diff.note, None, a, seq), "copy", e[1], e[2])
                    continue
                if a.idx in spots.links:
                    req, under, request_line = spots.links[a.idx]
                    seq += 1
                    done(_change(diff.note, None, a, seq), "link-line", None, req,
                         {"under": under, "request_line": request_line})
                    continue
                left_added.append(a)

            # What no entry explains pairs up in order: a changed line is one change with both texts
            # (spec-edit-guard.md 03.1 item 6). Leftovers are plain added or removed lines.
            pairs, rest_removed, rest_added = pair_in_order(left_removed, left_added)
            for r, a in pairs:
                seq += 1
                unexplained.append(_change(diff.note, r, a, seq))
            for r in rest_removed:
                seq += 1
                unexplained.append(_change(diff.note, r, None, seq))
            for a in rest_added:
                seq += 1
                unexplained.append(_change(diff.note, None, a, seq))
    return explained, unexplained
