"""A research run's requests: finding them, the requests file, the outcomes check, link lines and
closes (spec-run-manager.md 02 item 5; 04 item 13; 06 items 4 to 8; 08.4)."""
import json
import os
import re

from . import lines as ln
from . import snapshot
from .state import Refusal

OPEN = re.compile(r"^(\s*)- \[r\] (.*)$")
CLOSED = re.compile(r"^(\s*)- \[x\] (.*)$")
# An [AGENT] line: its text after the list marker and any checkbox starts with "[AGENT] "
# (spec-edit-guard.md 04 item 5).
AGENT_LINE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\[.\]\s+)?\[AGENT\] ")
OUTCOME_KINDS = ("passed", "failed", "no findings")
OUTCOME_KEYS = ("request", "outcome", "note", "reason", "failed_topics")
STOPPED = "You stopped this run."  # why every request of a stopped run stays open (spec-run-manager.md 09.4)


def tag_pattern(run_number):
    """The run's tag, matched exactly: #research/run-2 doesn't match #research/run-20 (CONTRACT.md 4
    item 8)."""
    return re.compile(r"(?:^|\s)#research/run-" + str(run_number) + r"(?![\w/-])")


def indent_of(text):
    return text[: len(text) - len(text.lstrip())]


def closed_text(text):
    """The request line with `- [r]` changed to `- [x]` and nothing else (spec-run-manager.md 08.4
    item 2)."""
    m = OPEN.match(text)
    return f"{m.group(1)}- [x] {m.group(2)}" if m else text


def project_name(project):
    return os.path.basename(os.path.abspath(project))


def link_line(request_text, name, note):
    """The link line: the request's indent plus four spaces, then `- [AGENT] [[Projects/{Project}/
    {path without .md}|{file name}]]` (spec-run-manager.md 08.4 item 1; CONTRACT.md 1 item 5)."""
    stem = note[:-3] if note.endswith(".md") else note
    return f"{indent_of(request_text)}    - [AGENT] [[Projects/{name}/{stem}|{stem.rsplit('/', 1)[-1]}]]"


def link_target(text, request_text, name):
    """The note a link line in the settled form points to, as a path inside the project; else None."""
    pattern = (re.escape(indent_of(request_text)) + r"    - \[AGENT\] \[\[Projects/" + re.escape(name)
               + r"/([^\]|#]+)\|([^\]|]+)\]\]")
    m = re.fullmatch(pattern, text)
    if not m or m.group(2) != m.group(1).rsplit("/", 1)[-1]:
        return None
    return m.group(1) + ".md"


def comment_lines(lines):
    """The positions of comment lines: a line that opens with %%, or sits inside a %% block."""
    out, inside = set(), False
    for i, text in enumerate(lines):
        if inside or text.lstrip().startswith("%%"):
            out.add(i)
        if text.count("%%") % 2:
            inside = not inside
    return out


def comment_under(lines, i):
    """The %% comment starting on the line right below line i, to the line that closes it, joined with
    \\n; or None (spec-run-manager.md 04 item 13; CONTRACT.md 4 item 10)."""
    j = i + 1
    if j >= len(lines) or not lines[j].lstrip().startswith("%%"):
        return None
    block, inside = [lines[j]], lines[j].count("%%") % 2 == 1
    while inside and j + 1 < len(lines):
        j += 1
        block.append(lines[j])
        if lines[j].count("%%") % 2:
            inside = False
    return "\n".join(block)


def find_requests(project, run_number):
    """Every open `- [r]` line with the run's tag, in every covered note (spec-run-manager.md 02 item 5;
    CONTRACT.md 4 item 9). Ids follow the note's path, then the line (CONTRACT.md 4 item 10). Returns
    the requests and, for each request note, the text read, so the snapshot matches the line numbers."""
    tag = tag_pattern(run_number)
    found, texts = [], {}
    for note, full in snapshot.covered_notes(project).items():
        try:
            text = ln.read_text(full)
        except UnicodeDecodeError:
            continue
        lines = ln.Note(text).lines
        hits = [i for i, t in enumerate(lines) if OPEN.match(t) and tag.search(t)]
        if hits:
            texts[note] = text
        for i in hits:
            found.append({"id": f"r{len(found) + 1}", "note": note, "line": i + 1, "text": lines[i],
                          "comment": comment_under(lines, i)})
    return found, texts


def load_json(path, what):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise Refusal(f"The {what} is missing: {path}.")
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        raise Refusal(f"The {what} at {path} can't be read ({e}).")


def check_outcomes(project, folder, requests):
    """Check the outcomes file before using it: every request appears exactly once, and every `passed`
    note exists (spec-run-manager.md 06 items 5 and 7). Returns (entries, None), or (None, why)."""
    path = os.path.join(folder, "outcomes.json")
    if not os.path.isfile(path):
        return None, "The research workflow's outcomes file was never saved."
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        return None, f"The outcomes file can't be read ({e})."
    if not isinstance(data, list):
        return None, "The outcomes file is not a list of entries."
    problems = []
    ids = [r["id"] for r in requests]
    for n, e in enumerate(data, 1):
        if not isinstance(e, dict):
            problems.append(f"entry {n} is not an object")
            continue
        missing = [k for k in OUTCOME_KEYS if k not in e]
        if missing:
            problems.append(f"entry {n} has no {', '.join(missing)}")
            continue
        if e["request"] not in ids:
            problems.append(f"entry {n} names {e['request']!r}, which isn't in the requests file")
        if e["outcome"] not in OUTCOME_KINDS:
            problems.append(f"entry {n} has the outcome {e['outcome']!r}")
        elif e["outcome"] == "passed":
            if not isinstance(e["note"], str) or not e["note"]:
                problems.append(f"{e['request']} passed but names no note")
            elif not os.path.isfile(os.path.join(project, e["note"])):
                problems.append(f"{e['request']} passed, but its note {e['note']} doesn't exist")
    named = [e.get("request") for e in data if isinstance(e, dict)]
    for rid in ids:
        count = named.count(rid)
        if count != 1:
            problems.append(f"{rid} is missing" if count == 0 else f"{rid} appears {count} times")
    if problems:
        return None, "The outcomes file was refused: " + "; ".join(problems) + "."
    return data, None


def passed_note(outcomes, request_id):
    """The note the outcomes file names for a request that passed, or None."""
    return next((o["note"] for o in outcomes if o["request"] == request_id and o["outcome"] == "passed"), None)


def mark(project, run):
    """Connect each answered request to its research note. Check the outcomes file, then write each passed
    request's link line and close, one request at a time, wherever its note sits: a note saved outside
    Research/ isn't moved, and the Edit guard flags the close (spec-run-manager.md 06 item 7; 08.4 items 1
    and 2; 11 item 94). An invalid or missing outcomes file moves to outcomes-refused.json, outcomes.json
    becomes [], and no note is edited (CONTRACT.md 4 item 1).
    Safe to run twice: a closed request is skipped, and a written link line isn't written again
    (CONTRACT.md 4 item 3). Writes mark.json for the run log. Returns it."""
    folder = snapshot.run_folder(project, run["id"])
    requests = load_json(os.path.join(folder, "requests.json"), "requests file")
    result_path = os.path.join(folder, "mark.json")
    prior = load_json(result_path, "mark result") if os.path.isfile(result_path) else {}
    result = {"outcomes_refused": prior.get("outcomes_refused"), "closed": [], "not_found": []}
    if result["outcomes_refused"] is None:
        outcomes, why = check_outcomes(project, folder, requests)
        if why:
            path = os.path.join(folder, "outcomes.json")
            if os.path.isfile(path):
                os.replace(path, os.path.join(folder, "outcomes-refused.json"))
            snapshot.write_json(path, [])
            result["outcomes_refused"] = why
    if result["outcomes_refused"] is None:
        name = project_name(project)
        for r in requests:
            note = passed_note(outcomes, r["id"])
            if note is None:
                continue
            done = _mark_one(project, folder, r, link_line(r["text"], name, note))
            result["closed" if done else "not_found"].append(r["id"])
    snapshot.write_json(result_path, result)
    return result


def mark_stopped(project, run):
    """`mark --stopped`: the writer stopped the research workflow. The path a missing outcomes file takes
    (CONTRACT.md 4 item 1): no note is edited, any outcomes file the session saved moves to
    outcomes-refused.json, outcomes.json becomes [] so the Edit guard can still run, and "You stopped this
    run." is saved as why, for the run log (spec-run-manager.md 04 item 19; 09.4 items 2 and 3). Writes
    mark.json, with `stopped` true, and returns it."""
    folder = snapshot.run_folder(project, run["id"])
    path = os.path.join(folder, "outcomes.json")
    if os.path.isfile(path):
        os.replace(path, os.path.join(folder, "outcomes-refused.json"))
    snapshot.write_json(path, [])
    result = {"outcomes_refused": STOPPED, "stopped": True, "closed": [], "not_found": []}
    snapshot.write_json(os.path.join(folder, "mark.json"), result)
    return result


def _mark_one(project, folder, r, link):
    """Write one request's link line right under it, then change `- [r]` to `- [x]`, each a whole-note
    write (spec-run-manager.md 08.4 items 1 and 2; 08.1 item 2). The request is found by its exact
    text; the snapshot tells identical lines apart (08.1 item 1). Returns False when it can't be found."""
    path = os.path.join(project, r["note"])
    snap = ln.read_note(os.path.join(folder, "snapshot", r["note"])).lines
    si = ln.snapshot_index(snap, r["text"], r["line"])
    note = ln.read_note(path)
    forms = {r["text"], closed_text(r["text"])}
    i = None if si is None else ln.find_same_line(snap, si, note.lines, forms)
    if i is None:
        return False
    if note.lines[i] != r["text"]:
        return True  # already closed by an earlier mark
    if i + 1 >= len(note.lines) or note.lines[i + 1] != link:
        note.insert(i + 1, link)
        ln.write_note(path, note)
    note.lines[i] = closed_text(r["text"])
    ln.write_note(path, note)
    return True
