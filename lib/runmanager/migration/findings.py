"""`findings`: check the migration-verifier's saved findings for the batch check, then approve, send back
for a fix round, or undo each unit; `findings --failed` when the check failed for good
(spec-run-manager.md 04 items 15, 22; spec-migration-verifier.md 05.1 item 2, 05.2, 06 items 1 to 3,
07 item 1; CONTRACT.md 5.3 items 7 to 9)."""
import json
import os

from .. import research as rs
from .. import state as st
from ..state import Refusal
from . import cycle, undo

CHECKS = ("lost-detail", "status", "scope", "standalone")
MAX_ROUND = 2  # at most 2 fix rounds per unit (spec-migrator.md 09 item 2)


def findings_path(project, run):
    return cycle.run_file(project, run, f"findings-b{run['batch']}-r{run['round']}.json")


def _problem_problem(p, uid):
    if not isinstance(p, dict):
        return f"a problem of {uid} isn't an object"
    if p.get("check") not in CHECKS:
        return f"a problem of {uid} has the check {p.get('check')!r}, not one of {', '.join(CHECKS)}"
    if not isinstance(p.get("note"), str) or not isinstance(p.get("line"), int) or not isinstance(p.get("what"), str):
        return f"a problem of {uid} needs a note, a line, and what"
    return None


def shape_problem(data, run):
    """What is wrong with a batch findings file, or None (spec-migration-verifier.md 05.1 item 2, 05.2;
    CONTRACT.md 5.3 item 7)."""
    if not isinstance(data, dict):
        return "it isn't a JSON object"
    if data.get("batch") != f"b{run['batch']}":
        return f"its batch is {data.get('batch')!r}, not b{run['batch']}"
    r = data.get("round")
    if not isinstance(r, int) or isinstance(r, bool) or r != run["round"]:
        return f"its round is {r!r}, not {run['round']}"
    if not isinstance(data.get("units"), list):
        return "it has no units list"
    fixing, seen = run["fixing"] or [], []
    for u in data["units"]:
        if not isinstance(u, dict) or not isinstance(u.get("problems"), list):
            return "each unit needs unit, verdict, and problems"
        uid = u.get("unit")
        if uid not in fixing:
            return f"it judges {uid!r}, which this check wasn't handed"
        if uid in seen:
            return f"it judges {uid} twice"
        seen.append(uid)
        if u.get("verdict") == "approve" and u["problems"]:
            return f"{uid} is approved but has problems"
        if u.get("verdict") == "fix" and not u["problems"]:
            return f"{uid} is a fix with no problem"
        if u.get("verdict") not in ("approve", "fix"):
            return f"{uid} has the verdict {u.get('verdict')!r}, not approve or fix"
        for p in u["problems"]:
            if (why := _problem_problem(p, uid)):
                return why
    missing = [uid for uid in fixing if uid not in seen]
    if missing:
        return f"it has no verdict for {', '.join(missing)}"
    missed = data.get("missed")
    if not isinstance(missed, list):
        return "it has no missed list"
    for m in missed:
        if not isinstance(m, dict) or not isinstance(m.get("source"), dict) or not isinstance(m.get("what"), str):
            return "each missed entry needs a source and what"
    if missed and run["round"] > 0:
        return "a re-check has missed entries; missed is empty on a re-check"
    return None


def _last_units(project, run):
    """The last valid record copy's round and its units, by id: undo works from it (CONTRACT.md 5.3
    item 10)."""
    r, text = cycle.last_copy(project, run, run["round"])
    if text is None:
        raise Refusal(f"Batch {run['batch']} has no valid record copy to undo from.")
    return r, cycle.units_by_id(json.loads(text))


def findings(project, state):
    """`findings` (needs `verifying` and the findings file). Approved units join the unit index; a fix
    before round 2 sends the run back to `migrating` on the next round; a fix on round 2 undoes the unit.
    With no unit left to fix, the run moves on (CONTRACT.md 5.3 item 8)."""
    run = cycle.migration_run(state, "verifying")
    path = findings_path(project, run)
    if not os.path.isfile(path):
        raise Refusal(f"The findings file {path} isn't there yet. Save the migration-verifier's findings first.")
    data = rs.load_json(path, "findings file")
    why = shape_problem(data, run)
    if why:
        raise Refusal(f"The findings file {path} was refused: {why}.")
    verdicts = {u["unit"]: u["verdict"] for u in data["units"]}
    problems = {u["unit"]: u["problems"] for u in data["units"]}
    # Missed lines go to the run log and the handled list (spec-run-manager.md 05 item 7; CONTRACT.md 5.6).
    cycle.add_working(project, run, "missed.json", [dict(m, batch=f"b{run['batch']}") for m in data["missed"]])
    to_fix, undone = [], []
    # Approvals join the unit index first, so a unit undone below takes any approved unit whose edit
    # built on its own with it (CONTRACT.md 5.3 item 13).
    for uid in run["fixing"]:
        if verdicts[uid] == "approve":
            cycle.join_index(state, run, uid, "approved")
        elif run["round"] < MAX_ROUND:
            to_fix.append(uid)
        else:
            undone.append(uid)
    if undone:
        last = _last_units(project, run)
        for unit in undo.undo_order([last[1][u] for u in undone]):
            undo.undo_all(project, state, run, [unit], last[0],
                          why={"why": "fix-rounds", "problems": problems[unit["id"]]})
    undo.cascade_saved(project, state, run)  # CONTRACT.md 5.3 item 13
    if to_fix:
        run.update(step="migrating", round=run["round"] + 1, fixing=to_fix)
        st.save_state(project, state)
        return f"to fix: {', '.join(to_fix)}; next: run the migrator on batch {run['batch']}, round {run['round']}"
    cycle.move_on(project, state)
    return f"undone: {len(undone)}; step: {run['step']}"


def findings_failed(project, state):
    """`findings --failed` (needs `verifying`): every unit the check didn't judge is undone; units
    approved in earlier rounds stand. Then the run moves on (CONTRACT.md 5.3 item 9)."""
    run = cycle.migration_run(state, "verifying")
    r, units = _last_units(project, run)
    fixing = [units[uid] for uid in run["fixing"] or [] if uid in units]
    undo.undo_all(project, state, run, fixing, r, why={"why": "verifier-failed"})
    undo.cascade_saved(project, state, run)  # CONTRACT.md 5.3 item 13
    cycle.move_on(project, state)
    return f"undone: {len(fixing)}; step: {run['step']}"
