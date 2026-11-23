"""Acting on a migration run's flags: `act` at `pointed`, `judged`, and `batch-failed`, and `findings` on
the migration-verifier's flag findings at `judging` (spec-run-manager.md 04 item 22; 05 items 3, 6, 7;
08.5; 09.1; spec-migration-verifier.md 03.2; 05.3; 06 items 5, 6; 07 item 2; spec-edit-guard.md 06 item 1;
CONTRACT.md 5.5)."""
import os

from .. import lines as ln
from .. import research as rs
from .. import snapshot
from .. import state as st
from ..act import load_flags
from ..state import Refusal
from . import cycle, pointers, undo
from .record import cut_down_unit

CODE_RULES = ("copy-mismatch", "pointer-mismatch")  # the flags the Run manager acts on itself (05 item 6)
VERIFY = "verify-flags.json"
FINDINGS = "findings-flags.json"
REFUSED = "findings-flags-refused.json"
STOOD = "stood-flags.json"  # flags on approved units that skip the flags call (spec-migration-verifier.md 06 item 7)
KINDS = ("comment", "request")


def act(project, state):
    """`act` on a migration run, at `pointed`, `judged`, or `batch-failed` (CONTRACT.md 5.5 items 2, 5, 8)."""
    run = state["open_run"]
    steps = {"pointed": _act_pointed, "judged": _act_judged, "batch-failed": _act_batch_failed,
             "recovered": _act_recovered}
    if run["step"] not in steps:
        raise Refusal(f"Run {run['id']} is at step '{run['step']}', but act needs 'pointed', 'judged', "
                      "'batch-failed', or 'recovered'.")
    return steps[run["step"]](project, state, run)


class _Undo:
    """The units undone in one `act` step, each once, with what undo couldn't find
    (CONTRACT.md 5.5 items 2, 5, 6)."""

    def __init__(self, project, state, run):
        self.project, self.state, self.run = project, state, run
        self.find = cycle.record_units(project, run)
        self.done, self.misses, self.ran = set(), [], False

    def unit(self, key, why):
        """Undo the unit `key` names, unless it was already undone, saving `why` for the run log. Returns
        True when a note changed."""
        if key in self.done:
            return False
        self.done.add(key)
        entry = cycle.index_entry(self.state, self.run, key)
        if entry is None or entry.get("state") == "undone" or self.find(key) is None:
            return False
        cycle.note_undone(self.project, self.run, key, why)
        misses, changed = undo.undo_entry(self.project, self.state, self.run, entry, self.find)
        self.misses += misses
        self.ran = True
        return changed

    def cascade(self):
        """Undo each migrate unit whose source line an undone unit's edit changed (CONTRACT.md 5.3 item
        13). Its flags are then skipped like any unit undone in this step. Returns True when a note
        changed."""
        misses, changed, keys = undo.cascade(self.project, self.state, self.run)
        self.done.update(keys)
        self.misses += misses
        self.ran = self.ran or bool(keys)
        return changed

    def save(self):
        if self.ran:
            undo.save_misses(self.project, self.run, self.misses)


def _chained_edits(state, run, find):
    """The `edits` entries on a line two or more of the run's units edited in turn (spec-migration-verifier.md
    06 item 7, third bullet; plan-run-manager.md 06 item 14 (4)), as (unit key, note, before, after). A chain
    joins entries in one note whose `before` is another's `after`, as 5.3 item 13's "built on" does; it
    counts when it holds entries of two or more units. Units the unit index lists undone don't count, since
    undo put their `before` back. A migrate unit's pointer is no `edits` entry, so it never counts."""
    chains = []
    for e in state["unit_index"]:
        if e.get("run") != run["id"] or e.get("state") == "undone":
            continue
        found = find(e.get("unit"))
        for x in (found[1]["edits"] if found else []):
            x = (e["unit"], x["note"], x["before"], x["after"])
            joined = [c for c in chains if any(x[1] == y[1] and (x[2] == y[3] or x[3] == y[2]) for y in c)]
            chains = [c for c in chains if all(c is not j for j in joined)] + [[x] + [y for c in joined for y in c]]
    return {x for c in chains if len({y[0] for y in c}) > 1 for x in c}


def _stands(state, run, f, find, chained):
    """Whether a flag stands without the flags call (spec-migration-verifier.md 06 item 7; CONTRACT.md 5.5
    item 2): it names a unit the batch check approved whose `trigger` kind is `comment` or `request`, and
    it isn't on a line two or more of the run's units edited in turn."""
    entry = cycle.index_entry(state, run, f.get("unit")) if f.get("unit") else None
    if entry is None or entry.get("state") not in ("approved", "pointer-written"):
        return False
    found = find(f["unit"])
    return found is not None and found[1]["trigger"]["kind"] in KINDS \
        and (f["unit"], f.get("note"), f.get("before"), f.get("after")) not in chained


def _stood_entry(f, find):
    """A flag that stood, as an `asked` entry for findings-flags.json, so the second check drops it as one
    judged asked for (spec-edit-guard.md 07 item 2; plan-run-manager.md 06 item 13). Its `asked_by` is the
    unit's trigger; the trigger records no note or line, so those are "" and null. The run log finds the
    comment itself (CONTRACT.md 5.6 item 6)."""
    t = find(f["unit"])[1]["trigger"]
    return {"flag": f["id"], "verdict": "asked", "asked_by": {"kind": t["kind"], "note": "", "line": None, "text": t["text"]}}


def _add_stood(project, run, entries):
    """findings-flags.json with the stood flags' entries after the verdicts (plan-run-manager.md 06 item 14
    (2)): added only once the migration-verifier's file is checked, or written by `act` when no call runs."""
    path = cycle.run_file(project, run, STOOD)
    stood = rs.load_json(path, "stood flags file") if os.path.isfile(path) else []
    snapshot.write_json(cycle.run_file(project, run, FINDINGS), {"flags": entries + stood})


def _act_pointed(project, state, run):
    """`act` at `pointed` (CONTRACT.md 5.5 item 2): `copy-mismatch` undoes its unit, pointer included;
    `pointer-mismatch` rewrites the line's pointer from the records. These go first, so a flag on a unit
    undone in this step is skipped wherever it sits. A flag on an approved unit a comment or the request
    started stands. Every other flag goes to the migration-verifier in verify-flags.json, the stood ones
    wait in stood-flags.json, and the step becomes `judging`; with none, `acted`, and the stood ones go
    straight into findings-flags.json."""
    n = run["next_check"]
    flags = load_flags(project, run, n)
    undoing, changed = _Undo(project, state, run), False
    for f in (f for f in flags if f.get("rule") == "copy-mismatch"):
        changed |= undoing.unit(f.get("unit"), {"why": "copy-mismatch"})
    changed |= undoing.cascade()
    for f in (f for f in flags if f.get("rule") == "pointer-mismatch"):
        if f.get("unit") not in undoing.done:
            changed |= pointers.rewrite(project, state, run, f, undoing.find)
    rest = [f for f in flags if f.get("rule") not in CODE_RULES and not (f.get("unit") and f.get("unit") in undoing.done)]
    chained = _chained_edits(state, run, undoing.find)
    stood = [_stood_entry(f, undoing.find) for f in rest if _stands(state, run, f, undoing.find, chained)]
    rest = [f for f in rest if f.get("id") not in {e["flag"] for e in stood}]
    undoing.save()
    if stood:
        snapshot.write_json(cycle.run_file(project, run, STOOD), stood)
    if stood and not rest:
        _add_stood(project, run, [])
    if rest:
        units = {}
        for f in rest:
            found = undoing.find(f["unit"]) if f.get("unit") else None
            if found is not None:
                units[f["unit"]] = cut_down_unit(found[1])
        snapshot.write_json(cycle.run_file(project, run, VERIFY), {"flags": rest, "units": units})
        run.update(step="judging", edited=changed)
    else:
        run.update(step="acted", edited=changed, next_check=n + 1 if changed else None)
    st.save_state(project, state)
    return f"step: {run['step']}; flags for the migration-verifier: {len(rest)}"


def _restore(project, run, f, misses):
    """Restore a line no unit explains (spec-run-manager.md 08.5; CONTRACT.md 5.5 item 5, third bullet):
    a changed line goes back to `before`, an added line is removed, and a removed line goes back under the
    nearest non-blank line above it in the snapshot. A line it can't find is left alone and added to
    `misses`. Returns True when the note changed."""
    path = os.path.join(project, f.get("note") or "")
    if not f.get("note") or not os.path.isfile(path):
        misses.append({"note": f.get("note"), "before": f.get("before"), "after": f.get("after")})
        return False
    note = ln.read_note(path)
    snap = undo._snap_lines(project, run, f["note"])

    def place_under(above, matched):
        # The line above may carry a pointer written since the snapshot; it is found by its bare text.
        q = matched.get(above)
        if q is None:
            q = undo.locate(snap, note.lines, snap[above], above + 1)
        return None if q is None else q + 1

    how = ln.restore_line(note, snap, f.get("before"), f.get("after"), place_under)
    if how is None:
        misses.append({"note": f["note"], "before": f.get("before"), "after": f.get("after")})
        return False
    ln.write_note(path, note)
    # Kept for the run log's Changes put back (spec-run-manager.md 07.3 item 2).
    cycle.add_working(project, run, "restored.json",
                      [{"note": f["note"], "before": f.get("before"), "after": f.get("after"), "how": how}])
    return True


def _save_restore_misses(project, run, misses):
    """Add restore misses to `.runs/{run-id}/restore-misses.json`, for the log's Other notes (CONTRACT.md
    5.5 item 5). Written only when there is a miss."""
    if not misses:
        return
    path = cycle.run_file(project, run, "restore-misses.json")
    saved = rs.load_json(path, "restore misses") if os.path.isfile(path) else []
    snapshot.write_json(path, saved + misses)


def _act_judged(project, state, run):
    """`act` at `judged` (CONTRACT.md 5.5 item 5; spec-edit-guard.md 06 item 1): an `asked` flag changes
    nothing; a `not-asked` flag undoes the unit it names, pointer included, once per unit, or restores the
    line when it names none. A `fingerprint-changed` note can't be restored. Then `acted`, waiting for a
    second check when this `act` or the one at `pointed` changed a note."""
    verify = rs.load_json(cycle.run_file(project, run, VERIFY), "verify-flags file")
    findings = rs.load_json(cycle.run_file(project, run, FINDINGS), "flag findings file")
    verdicts = {e["flag"]: e["verdict"] for e in findings["flags"]}
    undoing, changed, misses = _Undo(project, state, run), False, []
    for f in verify["flags"]:
        if verdicts.get(f.get("id")) == "asked":
            continue
        if f.get("unit"):
            changed |= undoing.unit(f["unit"], {"why": "not-asked", "flag": f})
        elif f.get("rule") != "fingerprint-changed":
            changed |= _restore(project, run, f, misses)
    changed |= undoing.cascade()
    undoing.save()
    _save_restore_misses(project, run, misses)
    edited = bool(run.get("edited")) or changed
    run.update(step="acted", edited=edited, next_check=run["first_check"] + 1 if edited else None)
    st.save_state(project, state)
    return f"step: acted; units undone: {len(undoing.done)}; lines not found: {len(misses)}"


def _act_batch_failed(project, state, run):
    """`act` at `batch-failed` (CONTRACT.md 5.5 item 8; spec-run-manager.md 07.2 item 4): every
    `unexplained-change` flag is restored; other flags are left for the check after `pointers`. Then the
    next batch, or `batches-done` after the last, with `next_check` null."""
    flags = load_flags(project, run, run["next_check"])
    misses = []
    for f in (f for f in flags if f.get("rule") == "unexplained-change"):
        _restore(project, run, f, misses)
    _save_restore_misses(project, run, misses)
    cycle.move_on(project, state)
    return f"step: {run['step']}; lines not found: {len(misses)}"


def _act_recovered(project, state, run):
    """`act` at `recovered` (CONTRACT.md 5.6 item 7): every `unexplained-change` flag is restored as at
    `batch-failed`; the rest are only named in the recover log. Then `acted`, with `next_check` null."""
    flags = load_flags(project, run, run["next_check"])
    misses = []
    for f in (f for f in flags if f.get("rule") == "unexplained-change"):
        _restore(project, run, f, misses)
    _save_restore_misses(project, run, misses)
    run.update(step="acted", next_check=None)
    st.save_state(project, state)
    return f"step: acted; lines not found: {len(misses)}"


def _asked_by_problem(a, fid):
    if not isinstance(a, dict) or a.get("kind") not in KINDS:
        return f"{fid}'s asked_by needs a kind, comment or request"
    if not isinstance(a.get("text"), str):
        return f"{fid}'s asked_by has no text"
    if a["kind"] == "request":
        if a.get("note") != "" or a.get("line") is not None:
            return f"{fid} was asked by the request, so its note is \"\" and its line null"
    elif not isinstance(a.get("note"), str) or not a["note"] or not isinstance(a.get("line"), int) \
            or isinstance(a.get("line"), bool) or a["line"] < 1:
        return f"{fid} was asked by a comment, so it needs the comment's note and line"
    return None


def shape_problem(data, ids):
    """What is wrong with a flag findings file, or None (spec-migration-verifier.md 05.1 item 2; 05.3;
    CONTRACT.md 5.5 item 4)."""
    if not isinstance(data, dict) or not isinstance(data.get("flags"), list):
        return "it has no flags list"
    seen = []
    for e in data["flags"]:
        if not isinstance(e, dict):
            return "each entry needs flag, verdict, and asked_by"
        fid = e.get("flag")
        if fid not in ids:
            return f"it judges {fid!r}, which verify-flags.json doesn't hold"
        if fid in seen:
            return f"it judges {fid} twice"
        seen.append(fid)
        if "asked_by" not in e:
            return f"{fid} has no asked_by"
        if e.get("verdict") == "asked":
            if (why := _asked_by_problem(e["asked_by"], fid)):
                return why
        elif e.get("verdict") == "not-asked":
            if e["asked_by"] is not None:
                return f"{fid} is not-asked, so its asked_by is null"
        else:
            return f"{fid} has the verdict {e.get('verdict')!r}, not asked or not-asked"
    missing = [fid for fid in ids if fid not in seen]
    if missing:
        return f"it has no verdict for {', '.join(missing)}"
    return None


def _verify_ids(project, run):
    verify = rs.load_json(cycle.run_file(project, run, VERIFY), "verify-flags file")
    return [f.get("id") for f in verify.get("flags", [])] if isinstance(verify, dict) else []


def findings(project, state):
    """`findings` at `judging` (needs findings-flags.json): check it; valid, the step is `judged`; refused,
    exit 1 and nothing changes (CONTRACT.md 5.5 item 4)."""
    run = cycle.migration_run(state, "judging")
    path = cycle.run_file(project, run, FINDINGS)
    if not os.path.isfile(path):
        raise Refusal(f"The flag findings file {path} isn't there yet. Save the migration-verifier's findings first.")
    data = rs.load_json(path, "flag findings file")
    why = shape_problem(data, _verify_ids(project, run))
    if why:
        raise Refusal(f"The flag findings file {path} was refused: {why}.")
    _add_stood(project, run, data["flags"])
    run["step"] = "judged"
    st.save_state(project, state)
    return "step: judged; next: act"


def findings_failed(project, state):
    """`findings --failed` at `judging`: every flag handed to the call counts as not asked for
    (spec-migration-verifier.md 07 item 2); a flag that stood still stands (plan-run-manager.md 06 item 14
    (3)). It writes findings-flags.json itself, in verify-flags.json order, then the stood entries, so the
    second check reads the same file, keeping a refused file as findings-flags-refused.json; then `judged`
    (CONTRACT.md 5.5 item 4)."""
    run = cycle.migration_run(state, "judging")
    path = cycle.run_file(project, run, FINDINGS)
    if os.path.isfile(path):
        os.replace(path, cycle.run_file(project, run, REFUSED))
    ids = _verify_ids(project, run)
    _add_stood(project, run, [{"flag": fid, "verdict": "not-asked", "asked_by": None} for fid in ids])
    run["step"] = "judged"
    st.save_state(project, state)
    return f"every flag counted as not asked for: {len(ids)}; next: act"
