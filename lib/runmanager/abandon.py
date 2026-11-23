"""`abandon`: close a run recover couldn't clear (spec-run-manager.md 09.3; CONTRACT.md 6). It edits no
note, adds nothing to the handled list, and changes no unit index entry. It writes the abandon log in
`Runs/`, adds the history entry, and clears the open run. The run's folder and snapshot stay. When the
log can't be written, the run still closes and the log's text is printed for the skill to show."""
import json
import os

from . import research as rs
from . import snapshot
from . import state as st
from .act import flags_path
from .lines import write_note_whole
from .migration import recover
from .runlog import note_link, quote
from .state import Refusal

COPIES = "Copies still in your notes"
REQUEST = "Your request"
NEVER = "Never checked"
OTHER = "Other notes"
FIRST_LINE = "Abandoned run, for {id}."
SECOND_LINE = "This run was closed without its last checks. Below is what was never checked."
DELETE_COPY = "Delete this copy before the next migration run, or the run copies this line again."
TYPE_AGAIN = "Type your request again on the next migration run."
MARKUP_UNCHECKED = "Markup wasn't checked after the run's last edit."
# Steps where an `act` already ran on the flags file `next_check` names: the migration-verifier is judging
# the flags act handed it (CONTRACT.md 5.5 items 2 and 5).
ACTED_ON = ("judging", "judged")


def _load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return default


def abandon(project, state):
    """Refuse with no open run, or one recover hasn't tried (spec-run-manager.md 09.3 item 1). Otherwise
    write the log first; then add the history entry and clear the open run, whether or not the log was
    written (09.3 items 2 and 3). Returns what the command prints: the log's path, or its whole text."""
    run = state["open_run"]
    if run is None:
        raise Refusal("There is no open run to abandon.")
    if not run.get("recover_tried"):
        raise Refusal("Run /script-asst:run recover first.")
    when = st.now().strftime(st.CLOCK_FORMAT)
    log_name, text = build(project, state, run, when)
    try:
        runs = os.path.join(project, "Runs")
        os.makedirs(runs, exist_ok=True)
        write_note_whole(os.path.join(runs, log_name), text)
        out = f"run log: Runs/{log_name}"
    except OSError as e:
        why = " ".join(str(e.strerror or e).split())
        out = f"The abandon log couldn't be written to Runs/{log_name} ({why}). Its text:\n\n{text}"
    # No `renamed`: abandon carries nothing over; a research run's `failed` is [] (spec-run-manager.md 04
    # item 17; 09.3 item 2).
    entry = {"id": run["id"], "kind": run["kind"], "run_number": run.get("run_number"),
             "started": run["started"], "ended": when, "how": "abandoned"}
    if run["kind"] == "research":
        entry["failed"] = []
    state["history"].append(entry)
    state["open_run"] = None
    st.save_state(project, state)
    return out


def build(project, state, run, when):
    """Return (the abandon log's file name, its text) (spec-run-manager.md 09.3 item 4). Reads only: the
    run state, the run's records and working files. An empty section is left out."""
    name = rs.project_name(project)
    folder = snapshot.run_folder(project, run["id"])
    copies, request = ([], []) if run["kind"] != "migration" else (copy_items(project, state, run, name),
                                                                   request_items(project, run, name))
    never = never_checked(project, run, name, folder)
    other = []
    for m in _load(os.path.join(folder, "undo-misses.json"), []):  # spec-run-manager.md 09.1 item 5
        other.append(f"- In {note_link(name, m.get('note') or '')}, undo couldn't find "
                     f"{quote(m.get('text') or '')}, so it was left alone.")
    other.append(f"- The run's before-snapshot is in `.runs/{run['id']}/snapshot/`, for comparing your notes "
                 "by hand.")
    log_id = f"run-{when[:10]}-{when[11:13]}{when[14:16]}-abandon"
    out = ["---", f"title: Run - {when[:10]} {when[11:13]}{when[14:16]} abandon", "type: [run-log]",
           f"created: {when[:10]}", "---", "", FIRST_LINE.format(id=run["id"]), "", SECOND_LINE, ""]
    for heading, items in ((COPIES, copies), (REQUEST, request), (NEVER, never), (OTHER, other)):
        if items:
            out += [f"## {heading}", "", *items, ""]
    return log_id + ".md", "\n".join(out)


def _units(project, run):
    """Every unit of the run, as (its key, the unit), from each batch's last valid record, as recover
    reads them (CONTRACT.md 5.6 item 7)."""
    out = []
    for b in range(1, (run.get("batch") or 1) + 1):
        _, last, _ = recover._batch_units(project, run, b)
        out += [(f"b{b}-{uid}", u) for uid, u in last.items()]
    return out


def copy_items(project, state, run, name):
    """Copies still in your notes: each unit of the run with copies that the unit index doesn't list as
    undone, its source lines quoted, each note its copies went to, and the warning (spec-run-manager.md
    09.3 item 4 section 1; 11 item 111)."""
    undone = {e.get("unit") for e in state["unit_index"]
              if e.get("run") == run["id"] and e.get("state") == "undone"}
    out = []
    for key, u in _units(project, run):
        if key in undone or not u.get("copies"):
            continue
        sources = ", ".join(f"{quote(s['text'])} in {note_link(name, s['note'])}" for s in u["sources"])
        dests = ", ".join(note_link(name, n) for n in dict.fromkeys(c["note"] for c in u["copies"]))
        out.append(f"- {sources} was copied to {dests}.\n    - {DELETE_COPY}")
    return out


def request_items(project, run, name):
    """Your request: the typed request quoted, each source line of the units it started, and the line
    asking the writer to type it again. Abandon writes no request comment (spec-run-manager.md 09.3 item
    4 section 2; 11 item 112)."""
    if not run.get("request"):
        return []
    out = [f"You typed {quote(run['request'])}."]
    sources = recover.request_sources(project, run)
    if sources:
        out += ["", "It started these lines:", ""]
        out += [f"- {quote(s['text'])} in {note_link(name, s['note'])}" for s in sources]
    return out + ["", TYPE_AGAIN]


def _flag_item(name, f):
    parts = [f"- `{f.get('rule')}` in {note_link(name, f.get('note') or '')}"]
    if f.get("before"):
        parts.append(f"before {quote(f['before'])}")
    if f.get("after"):
        parts.append(f"after {quote(f['after'])}")
    return ", ".join(parts) + "."


def never_checked(project, run, name, folder):
    """Never checked (spec-run-manager.md 09.3 item 4 section 3): the missing-markup sentence when the
    awaited flags file never appeared; each flag in the awaited flags file, which no `act` ran on; on a
    research run, each link line and close `mark` wrote, when no `act` ran on flags-1, the check that
    reads them (11 item 120)."""
    out = []
    n = run.get("next_check")
    if n is not None and run["step"] not in ACTED_ON:
        path = flags_path(project, run, n)
        if not os.path.isfile(path):
            out.append(f"- {MARKUP_UNCHECKED}")
        else:
            flags = _load(path, [])
            out += [_flag_item(name, f) for f in (flags if isinstance(flags, list) else []) if isinstance(f, dict)]
    if run["kind"] == "research" and not os.path.isfile(os.path.join(folder, "act-1.json")):
        mark = _load(os.path.join(folder, "mark.json"), {})
        closed = set(mark.get("closed") or [])
        requests = _load(os.path.join(folder, "requests.json"), [])
        outcomes = _load(os.path.join(folder, "outcomes.json"), [])
        outcomes = [o for o in outcomes if isinstance(o, dict)] if isinstance(outcomes, list) else []
        for r in requests:
            if r.get("id") not in closed:
                continue
            note = rs.passed_note(outcomes, r["id"]) or ""
            out.append(f"- {quote(rs.closed_text(r['text']))} in {note_link(name, r['note'])}: the run closed it "
                       f"and wrote a link line to {note_link(name, note)} under it.")
    return out
