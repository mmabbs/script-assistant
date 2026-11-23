"""The run state: `{project}/.runs/run-state.json` (spec-run-manager.md 04 items 2, 3, 11, 16, 18;
09.2 item 1). Every command except `init` reads it first. It is written whole through a temp file."""
import json
import os
from datetime import datetime

from .lines import write_note_whole

INIT_LINE = "If this is a new project, run /script-asst:run init."
CLOCK_FORMAT = "%Y-%m-%d %H:%M"


class Refusal(Exception):
    """A refusal or a bad input. The message is the one plain line the command prints; exit code 1."""


def state_path(project):
    return os.path.join(project, ".runs", "run-state.json")


def now():
    """The current time. RUNMANAGER_NOW (YYYY-MM-DD HH:MM) wins when set (CONTRACT.md 1 item 3)."""
    text = os.environ.get("RUNMANAGER_NOW")
    if not text:
        return datetime.now().replace(second=0, microsecond=0)
    try:
        return datetime.strptime(text, CLOCK_FORMAT)
    except ValueError:
        raise Refusal(f"RUNMANAGER_NOW must look like 2026-10-10 16:00, not {text!r}.")


def run_id_for(kind, when):
    """The run id is the run log's name without .md (spec-run-manager.md 04 item 12)."""
    return f"run-{when.strftime('%Y-%m-%d-%H%M')}-{kind}"


def _shape_problem(state):
    """Return what is wrong with a parsed run state, or None (spec-run-manager.md 04 item 16)."""
    if not isinstance(state, dict):
        return "the top level is not an object"
    for key in ("open_run", "history", "handled", "unit_index"):
        if key not in state:
            return f"'{key}' is missing"
    for key in ("history", "handled", "unit_index"):
        if not isinstance(state[key], list):
            return f"'{key}' is not a list"
    run = state["open_run"]
    if run is not None:
        if not isinstance(run, dict):
            return "'open_run' is neither null nor an object"
        for key in ("id", "kind", "step"):
            if key not in run:
                return f"'open_run' has no '{key}'"
    return None


def load_state(project):
    """Read the run state. A missing or unreadable one stops the command with the init line
    (spec-run-manager.md 04 item 11). Never creates one."""
    path = state_path(project)
    if not os.path.isfile(path):
        raise Refusal(f"There is no run state at {path}. {INIT_LINE}")
    try:
        with open(path, encoding="utf-8") as f:
            state = json.load(f)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        why = " ".join(str(getattr(e, "strerror", None) or e).split())
        raise Refusal(f"The run state at {path} can't be read ({why}). Restore it from a backup, or, if no run is open, move it out of .runs/ and run /script-asst:run init. A new run state treats every tagged line as new.")
    problem = _shape_problem(state)
    if problem:
        raise Refusal(f"The run state at {path} is not a valid run state ({problem}). Restore it from a backup, or, if no run is open, move it out of .runs/ and run /script-asst:run init. A new run state treats every tagged line as new.")
    return state


def save_state(project, state):
    """Write the whole run state in one step."""
    write_note_whole(state_path(project), json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def init_state(project):
    """Create the run state for a new project. Refuses if one exists (spec-run-manager.md 04 item 10)."""
    if not os.path.isdir(project):
        raise Refusal(f"The project folder {project} does not exist.")
    path = state_path(project)
    if os.path.exists(path):
        raise Refusal(f"A run state already exists at {path}. init never replaces it.")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    state = {"open_run": None, "history": [], "handled": [], "unit_index": []}
    save_state(project, state)
    return state


def claim_run(project, kind, run_number=None, request=None, when=None):
    """Claim the open run in one write (spec-run-manager.md 09.2 item 1). Reads the run state fresh,
    refuses if a run is open, and returns the new open run: a research run at step `started`; a migration
    run at `migrating`, batch 1, round 0. Only a migration run gets `batch` and `round`
    (spec-run-manager.md 04 items 16 and 22)."""
    state = load_state(project)
    refuse_if_open(state)
    when = when or now()
    run = {"id": run_id_for(kind, when), "kind": kind, "run_number": run_number, "request": request,
           "step": "started", "next_check": None, "started": when.strftime(CLOCK_FORMAT)}
    if kind == "migration":
        run.update(step="migrating", batch=1, round=0)
    state["open_run"] = run
    save_state(project, state)
    return run


def refuse_if_open(state):
    """A run that finds another run still open stops, and tells the writer to type recover
    (spec-run-manager.md 04 item 3; 09.2 items 1 and 2)."""
    open_run = state["open_run"]
    if open_run is not None:
        raise Refusal(f"Run {open_run['id']} is still open. Type /script-asst:run recover to deal with it.")


def set_step(project, state, step, next_check):
    """Move the open run to its next step and save the run state (spec-run-manager.md 04 item 18)."""
    state["open_run"]["step"] = step
    state["open_run"]["next_check"] = next_check
    save_state(project, state)


def require_step(state, step):
    """Refuse unless the open run is at `step` (spec-run-manager.md 01 item 3, 04 item 18). The refusal
    is one plain line naming the step it expected. Returns the open run."""
    run = state["open_run"]
    if run is None:
        raise Refusal(f"There is no open run. This step needs a run at step '{step}'.")
    if run["step"] != step:
        raise Refusal(f"Run {run['id']} is at step '{run['step']}', but this step needs '{step}'.")
    return run


def refuse_if_recover_tried(run):
    """Recover gets one try per run. A second recover on the same run refuses and points to abandon
    (spec-run-manager.md 09.2 item 6; 09.3)."""
    if run.get("recover_tried"):
        raise Refusal(f"Recover already ran once on {run['id']}. Type /script-asst:run abandon.")


def mark_recover_tried(project, state):
    """Save `recover_tried: true` on the open run, before recover edits any note, so a recover that
    crashes partway still counts as its try (spec-run-manager.md 04 item 16; 09.2 item 6; 11 item 108)."""
    state["open_run"]["recover_tried"] = True
    save_state(project, state)
