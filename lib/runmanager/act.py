"""Acting on a research run's flags (spec-edit-guard.md 06 item 3; spec-run-manager.md 05 item 4,
08.4 item 3, 08.5; CONTRACT.md 4 items 5, 11, and 12).

- link-line-invalid, close-invalid: the request line goes back to its snapshot text and the link line
  is removed.
- unexplained-change in a request note: the line is restored from the snapshot.
- fingerprint-changed, unexpected-research-note, and anything else: nothing is edited; the log names it.
"""
import os

from . import lines as ln
from . import research as rs
from . import snapshot
from .state import Refusal

# The fixed reasons for an undone close (spec-run-manager.md 06.1 item 3).
REASON_BELOW_COMMENT = "its link line sat below your comment"
REASON_NO_LINK = "it had no link line under it"
REASON_FORM = "its link line wasn't in the settled form"
REASON_TARGET = ("its link line pointed to a note that doesn't exist, or to a different note than the one "
                 "written for it")
REASON_WORDS = "the words on your request line had changed. Your words are put back."


def flags_path(project, run, n):
    return os.path.join(snapshot.run_folder(project, run["id"]), f"flags-{n}.json")


def load_flags(project, run, n):
    """The flags file the run waits for. act refuses until it exists (spec-run-manager.md 03; 04 item 18)."""
    path = flags_path(project, run, n)
    if not os.path.isfile(path):
        raise Refusal(f"flags-{n}.json isn't there yet. Run editguard check before this step.")
    flags = rs.load_json(path, f"flags file flags-{n}.json")
    if not isinstance(flags, list) or not all(isinstance(f, dict) for f in flags):
        raise Refusal(f"The flags file {path} is not a list of flags.")
    return flags


def act(project, run):
    """Act on the awaited flags file. Writes act-{N}.json for the run log and returns
    (edited anything, that report)."""
    folder = snapshot.run_folder(project, run["id"])
    n = run["next_check"]
    flags = load_flags(project, run, n)
    requests = rs.load_json(os.path.join(folder, "requests.json"), "requests file")
    try:
        outcomes = rs.load_json(os.path.join(folder, "outcomes.json"), "outcomes file")
    except Refusal:
        outcomes = []
    if not isinstance(outcomes, list):
        outcomes = []
    report = {"flags": f"flags-{n}.json", "closes_undone": [], "lines_put_back": [], "named": [],
              "not_found": []}
    by_note = {}
    for f in flags:
        rule = f.get("rule")
        snap_copy = os.path.join(folder, "snapshot", *str(f.get("note", "")).split("/"))
        if rule in ("close-invalid", "link-line-invalid", "unexplained-change") and os.path.isfile(snap_copy):
            by_note.setdefault(f["note"], []).append(f)
        else:
            report["named"].append(_flag_entry(f))
    edited = False
    for note, note_flags in by_note.items():
        path = os.path.join(project, note)
        if not os.path.isfile(path):
            report["not_found"] += [_flag_entry(f) for f in note_flags]
            continue
        current = ln.read_note(path)
        snap = ln.read_note(os.path.join(folder, "snapshot", note)).lines
        reqs = [r for r in requests if r["note"] == note]
        if _act_on_note(project, note, current, snap, note_flags, reqs, outcomes, report):
            ln.write_note(path, current)
            edited = True
    snapshot.write_json(os.path.join(folder, f"act-{n}.json"), report)
    return edited, report


def _flag_entry(f):
    return {k: f.get(k) for k in ("id", "rule", "note", "before", "after")}


def _act_on_note(project, note_path, note, snap, flags, reqs, outcomes, report):
    """Undo the flagged closes, then restore the unexplained lines, one flag at a time, all in memory.
    Returns True when the note changed."""
    lines = note.lines
    snap_i = {r["id"]: ln.snapshot_index(snap, r["text"], r["line"]) for r in reqs}
    extra = {r["id"]: set() for r in reqs}
    undo = {}  # request id -> {"close": flag or None, "links": [line index], "rules": [...]}

    for f in (f for f in flags if f["rule"] == "close-invalid"):
        owner = None
        for r in reqs:
            if r["text"] != f["before"] or snap_i[r["id"]] is None or "close" in undo.get(r["id"], {}):
                continue
            forms = {r["text"], rs.closed_text(r["text"]), f["after"]}
            i = ln.find_same_line(snap, snap_i[r["id"]], lines, forms)
            if i is not None and lines[i] == f["after"]:
                owner = r
                break
        if owner is None:
            report["not_found"].append(_flag_entry(f))
            continue
        extra[owner["id"]].add(f["after"])
        u = undo.setdefault(owner["id"], {"links": [], "rules": []})
        u["close"] = f
        u["rules"].append(f["rule"])

    pos = {}
    for r in reqs:
        if snap_i[r["id"]] is not None:
            forms = {r["text"], rs.closed_text(r["text"])} | extra[r["id"]]
            pos[r["id"]] = ln.find_same_line(snap, snap_i[r["id"]], lines, forms)
    stops = {p for p in pos.values() if p is not None}
    comments = rs.comment_lines(lines)

    for f in (f for f in flags if f["rule"] == "link-line-invalid"):
        found = None
        for r in reqs:
            p = pos.get(r["id"])
            if p is None:
                continue
            taken = undo.get(r["id"], {}).get("links", [])
            j = next((j for j in _block(lines, p, stops, comments) if lines[j] == f["after"] and j not in taken),
                     None)
            if j is not None:
                found = (r, j)
                break
        if found is None:
            report["not_found"].append(_flag_entry(f))
            continue
        r, j = found
        u = undo.setdefault(r["id"], {"links": [], "rules": []})
        u["links"].append(j)
        u["rules"].append(f["rule"])

    changed = False
    by_pos = sorted(((pos[rid], rid) for rid in undo if pos.get(rid) is not None), reverse=True)
    for p, rid in by_pos:
        r = next(r for r in reqs if r["id"] == rid)
        u = undo[rid]
        reason = _pick_reason(project, lines, p, r, u, snap, snap_i[rid], outcomes, comments)
        report["closes_undone"].append({"request": rid, "note": note_path, "text": r["text"], "now": lines[p],
                                        "reason": reason, "rules": sorted(set(u["rules"]))})
        remove = set(u["links"])
        under = _added_under(lines, p, snap, snap_i[rid])
        if under is not None and rs.AGENT_LINE.match(lines[under]):
            remove.add(under)
        lines[p] = r["text"]
        for j in sorted(remove, reverse=True):
            note.delete(j)
        changed = True

    for f in (f for f in flags if f["rule"] == "unexplained-change"):
        how = _restore_line(note, snap, f, reqs, snap_i)
        if how is None:
            report["not_found"].append(_flag_entry(f))
        else:
            report["lines_put_back"].append({**_flag_entry(f), "how": how})
            changed = True
    return changed


def _block(lines, p, stops, comments):
    """The positions in a request's block: the comment lines and deeper-indented lines under it, blank
    lines passed over, up to the next request (spec-edit-guard.md 04 item 6)."""
    depth = len(rs.indent_of(lines[p]))
    j = p + 1
    while j < len(lines) and j not in stops:
        if lines[j].strip():
            if j not in comments and len(rs.indent_of(lines[j])) <= depth:
                break
            yield j
        j += 1


def _added_under(lines, p, snap, si):
    """The position right under the request when the line there was added since the snapshot, else None."""
    if p + 1 >= len(lines):
        return None
    was = snap[si + 1] if si is not None and si + 1 < len(snap) else None
    return p + 1 if lines[p + 1] != was else None


def _pick_reason(project, lines, p, r, u, snap, si, outcomes, comments):
    """Pick the reason a close was undone from the fixed list, by re-reading the request's block
    (spec-run-manager.md 06.1 item 3). None when no reason fits; the log then names the rule."""
    close = u.get("close")
    if close and close["after"] != rs.closed_text(r["text"]):
        return REASON_WORDS
    link_j = min(u["links"]) if u["links"] else _added_under(lines, p, snap, si)
    if link_j is None:
        return REASON_NO_LINK
    if link_j != p + 1:
        return REASON_BELOW_COMMENT if any(k in comments for k in range(p + 1, link_j)) else None
    target = rs.link_target(lines[link_j], r["text"], rs.project_name(project))
    if target is None:
        return REASON_FORM
    if target != rs.passed_note(outcomes, r["id"]) or not os.path.isfile(os.path.join(project, target)):
        return REASON_TARGET
    return None


def _restore_line(note, snap, f, reqs, snap_i):
    """Restore one unexplained line (CONTRACT.md 4 items 5 and 11): a changed line goes back to
    `before`, an added line is removed, and a removed line goes back under the nearest non-blank line
    that sat above it in the snapshot, below that line's link line when it is a request that now has
    one. Lines are found by exact text; when the text repeats, the line the snapshot doesn't explain is
    the one meant. Returns what was done, or None when the line can't be found."""
    cur = note.lines

    def place_under(above, matched):
        """Under the line above, below its link line when it is a request that now has one."""
        owner = next((r for r in reqs if snap_i[r["id"]] == above), None)
        q = matched.get(above)
        if q is None and owner is not None:
            forms = {owner["text"], rs.closed_text(owner["text"])}
            q = ln.find_same_line(snap, above, cur, forms)
        if q is None:
            return None
        at = q + 1
        if owner is not None and at < len(cur) and rs.AGENT_LINE.match(cur[at]):
            at += 1
        return at

    return ln.restore_line(note, snap, f.get("before"), f.get("after"), place_under)
