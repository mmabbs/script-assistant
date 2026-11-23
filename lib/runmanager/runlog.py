"""The research run log in `Runs/`, and the history entry `close` writes (spec-run-manager.md 04 item 17;
06.1; CONTRACT.md 4 items 4, 6, 13, 14, and 16)."""
import glob
import json
import os
import re

from . import research as rs
from . import snapshot

OPEN = "Requests still open"
UNDONE = "Closes undone"
CHANGED = "Notes changed outside the run"
DONE = "Done"
STILL = "Still flagged after the second check"
NAME_ONLY = ("fingerprint-changed", "unexpected-research-note")
MARKUP_UNCHECKED = "Markup wasn't checked on the first try."
# A stopped run's Requests still open (spec-run-manager.md 09.4 items 3 and 4).
STOPPED_OPEN = "You stopped this run. Every request stays open."
WRITTEN_BEFORE = "Written before you stopped the run:"


def _load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return default


def note_link(name, note):
    """A log link: [[Projects/{folder name}/{path without .md}|{file name without .md}]] (CONTRACT.md 1
    item 5)."""
    stem = note[:-3] if note.endswith(".md") else note
    return f"[[Projects/{name}/{stem}|{stem.rsplit('/', 1)[-1]}]]"


def quote(text):
    """Quote a line in code marks, so a quoted tag or checkbox stays text in the log."""
    return f"`{text}`"


def _sentence(text):
    return text if text.endswith(".") else text + "."


def _earlier_note(history, text, now_note):
    """The note an earlier failed try left, found by the request's exact text (spec-run-manager.md 04
    item 17; 06 item 2). None when there is none, or it is this run's own note."""
    for entry in reversed(history):
        for f in entry.get("failed") or []:
            if f.get("text") == text and f.get("note") and f["note"] != now_note:
                return f["note"]
    return None


def _flag_numbers(folder):
    nums = []
    for path in glob.glob(os.path.join(folder, "flags-*.json")):
        m = re.fullmatch(r"flags-(\d+)\.json", os.path.basename(path))
        if m:
            nums.append(int(m.group(1)))
    return sorted(nums)


def failed_entries(requests, outcomes):
    """Each failed request that left a note: its exact text and the note (spec-run-manager.md 04 item 17)."""
    by_id = {r["id"]: r for r in requests}
    return [{"text": by_id[o["request"]]["text"], "note": o["note"]} for o in outcomes
            if o.get("outcome") == "failed" and o.get("note") and o.get("request") in by_id]


def build(project, state, run):
    """Return (the log's file name, its text, the history entry's failed list) for the open run."""
    name = rs.project_name(project)
    folder = snapshot.run_folder(project, run["id"])
    requests = _load(os.path.join(folder, "requests.json"), [])
    outcomes = _load(os.path.join(folder, "outcomes.json"), [])
    if not isinstance(outcomes, list):
        outcomes = []
    mark = _load(os.path.join(folder, "mark.json"), {})
    acts = sorted(glob.glob(os.path.join(folder, "act-*.json")))
    act = _load(acts[0], {}) if acts else {}
    first_check = int(re.search(r"\d+", act["flags"]).group()) if act.get("flags") else None
    history = state["history"]
    outcome_of = {o.get("request"): o for o in outcomes if isinstance(o, dict)}
    undone = {u["request"]: u for u in act.get("closes_undone", [])}
    closed = set(mark.get("closed", []))
    not_found = set(mark.get("not_found", []))

    still_open, closes_undone, changed, done = [], [], [], []
    for r in requests:
        rid, here = r["id"], note_link(name, r["note"])
        o = outcome_of.get(rid, {})
        if rid in undone:
            u = undone[rid]
            why = u["reason"] or f"the Edit guard flagged it ({', '.join(u['rules'])})"
            closes_undone.append(f"- {quote(r['text'])} in {here} was undone because {_sentence(why)} "
                                 "The request is open again.")
        elif rid in closed:
            line = f"- {quote(rs.closed_text(r['text']))} now points to {note_link(name, o.get('note') or '')}."
            if o.get("failed_topics"):
                line += f" Topics that failed: {', '.join(map(str, o['failed_topics']))}."
            earlier = _earlier_note(history, r["text"], o.get("note"))
            if earlier:
                line += f" An earlier try left {note_link(name, earlier)}."
            done.append(line)
        else:
            # One bullet per part, under the request (the writer's ruling, 2026-10-12;
            # spec-run-manager.md 11 item 69). A reason's later lines nest under "It failed".
            parts = []
            if mark.get("outcomes_refused"):
                parts.append(mark["outcomes_refused"])
            elif rid in not_found:
                parts.append("It passed, but its line couldn't be found to close it.")
            elif o.get("outcome") == "failed":
                first, *rest = [x.strip() for x in (o.get("reason") or "no reason given").split("\n") if x.strip()]
                parts.append(f"It failed: {_sentence(first)}" + "".join(f"\n        - {_sentence(x)}" for x in rest))
                if o.get("note"):
                    parts.append(f"The failed note is {note_link(name, o['note'])}.")
            elif o.get("outcome") == "no findings":
                parts.append("No findings.")
            else:
                parts.append("The outcomes file has no entry for it.")
            if o.get("failed_topics") and not mark.get("outcomes_refused"):
                parts.append(f"Topics that failed: {', '.join(map(str, o['failed_topics']))}.")
            earlier = _earlier_note(history, r["text"], o.get("note"))
            if earlier:
                parts.append(f"An earlier try left {note_link(name, earlier)}.")
            line = f"- {quote(r['text'])} in {here}." + "".join(f"\n    - {x}" for x in parts)
            still_open.append(line)

    fingerprints = _load(os.path.join(folder, "fingerprints.json"), {})
    stopped = bool(run.get("stopped") or mark.get("stopped"))
    written_before = []
    for f in act.get("named", []):
        note = f["note"] or ""
        if stopped and f["rule"] == "unexpected-research-note":
            # A research note the workflow wrote before the stop is listed once, at the end of
            # Requests still open, not under Notes changed outside the run (spec-run-manager.md 09.4
            # item 4; 11 item 115).
            line = f"- {note_link(name, note)}"
            if line not in written_before:
                written_before.append(line)
            continue
        if f["rule"] == "fingerprint-changed":
            # Say which of the three it was (spec-edit-guard.md 04 table, fingerprint-changed).
            if note not in fingerprints:
                what = "is a new note, added during the run"
            elif not os.path.exists(os.path.join(project, note)):
                what = "was removed during the run"
            else:
                what = "changed during the run"
        elif f["rule"] == "unexpected-research-note":
            what = "is a new research note the outcomes file doesn't name"
        else:
            what = "was flagged"
        changed.append(f"- {note_link(name, note)} {what} (`{f['rule']}`).")
    for f in act.get("lines_put_back", []):
        link = note_link(name, f["note"])
        if f["how"] == "changed back":
            changed.append(f"- In {link}, a changed line was put back. It read {quote(f['after'])}, "
                           f"and reads {quote(f['before'])} again.")
        elif f["how"] == "removed":
            changed.append(f"- In {link}, an added line was removed: {quote(f['after'])}.")
        else:
            changed.append(f"- In {link}, a removed line was put back: {quote(f['before'])}.")
    for f in act.get("not_found", []):
        text = f.get("after") or f.get("before") or ""
        changed.append(f"- In {note_link(name, f['note'] or '')}, a flagged line couldn't be found, so it was "
                       f"left alone (`{f['rule']}`): {quote(text)}.")
    if run.get("markup_unchecked"):
        changed.append(f"- {MARKUP_UNCHECKED}")
    if stopped:
        still_open = [STOPPED_OPEN, "", *still_open]
        if written_before:
            still_open += ["", WRITTEN_BEFORE, "", *written_before]

    still = []
    if first_check is not None:
        first = _load(os.path.join(folder, f"flags-{first_check}.json"), [])
        named = {(f.get("rule"), f.get("note")) for f in first if f.get("rule") in NAME_ONLY}
        for n in (n for n in _flag_numbers(folder) if n > first_check):
            for f in _load(os.path.join(folder, f"flags-{n}.json"), []):
                if (f.get("rule"), f.get("note")) in named:
                    continue  # CONTRACT.md 4 item 13
                parts = [f"- `{f.get('rule')}` in {note_link(name, f.get('note') or '')}"]
                if f.get("before"):
                    parts.append(f"before {quote(f['before'])}")
                if f.get("after"):
                    parts.append(f"after {quote(f['after'])}")
                still.append(", ".join(parts) + ".")

    if run.get("recovering"):
        when = run["recover_started"]
        log_id = f"run-{when[:10]}-{when[11:13]}{when[14:16]}-recover"
        first_line = f"Recover run, for {run['id']}."
    else:
        when = run["started"]
        log_id = run["id"]
        first_line = f"Research run {run.get('run_number')}, started {run['started']}."
    out = ["---", f"title: Run - {when[:10]} {when[11:13]}{when[14:16]} "
           f"{'recover' if run.get('recovering') else 'research'}",
           "type: [run-log]", f"created: {when[:10]}", "---", "", first_line, ""]
    if not (still_open or closes_undone or changed):
        out += ["Nothing needs you.", ""]
    for heading, items in ((OPEN, still_open), (UNDONE, closes_undone), (CHANGED, changed), (DONE, done),
                           (STILL, still)):
        if items:  # an empty section is left out (spec-run-manager.md 06.1 item 2)
            out += [f"## {heading}", "", *items, ""]
    return log_id + ".md", "\n".join(out), failed_entries(requests, outcomes)
