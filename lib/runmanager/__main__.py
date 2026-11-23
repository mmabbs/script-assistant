"""The `runmanager` command: one subcommand per step (spec-run-manager.md 01 item 1; CONTRACT.md 1).
Exit 0 when the step ran, 1 for a refusal or a bad input (one plain line on stderr), 2 for bad arguments."""
import argparse
import os
import shutil
import sys

from . import abandon, act, research, runlog, snapshot
from . import state as st
from .lines import write_note_whole
from .migration import close as migration_close
from .migration import findings, flags, pointers, record, recover, scan
from .state import Refusal

# The Research workflow script, in the plugin's lib/ folder.
WORKFLOW_SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "research.js")


def cmd_init(args, state):
    # init writes no permission rules: the plugin's hook approves the agents' writes (spec-run-manager.md
    # 11 item 89). init_state makes every refusal (04 item 10).
    st.init_state(args.project)
    print(f"run state created in {st.state_path(args.project)}")
    return 0


def next_step_text(run):
    """What comes next for the open run (spec-run-manager.md 04 item 18)."""
    step, n = run["step"], run.get("next_check")
    if step == "migrating":  # CONTRACT.md 5.1 item 6
        return f"run the migrator on batch {run.get('batch')}, round {run.get('round')}, then record"
    if step == "verifying":  # CONTRACT.md 5.3 item 12
        return (f"run the migration-verifier on batch {run.get('batch')}, round {run.get('round')}, "
                "save its findings, then findings")
    if step == "batches-done":
        return "pointers"
    if step in ("batch-failed", "pointed", "recovered"):  # CONTRACT.md 5.3 item 12; 5.4 item 12; 5.6 item 9
        return f"run editguard check for flags-{n}.json, then act"
    if step == "judging":  # CONTRACT.md 5.5 item 10
        return ("run the migration-verifier on verify-flags.json, save its findings as findings-flags.json, "
                "then findings")
    if step == "judged":
        return "act"
    if step == "started":
        return "run the research workflow, save its outcomes, then mark"
    if step == "marked":
        return f"run editguard check for flags-{n}.json, then act"
    if step == "acted":
        return f"run editguard check for flags-{n}.json, then close" if n else "close"
    return "recover"


def cmd_status(args, state):
    run = state["open_run"]
    if run is None:
        print("no open run")
    else:
        print(f"open run: {run['id']} ({run['kind']}), step: {run['step']}, next: {next_step_text(run)}")
    return 0


def cmd_start(args, state):
    """Claim the run, save the snapshot and fingerprints, write the requests file (spec-run-manager.md
    02 item 5; 04 items 8, 9, 12 to 14; 09.2 item 1). No open requests: refuse, claim nothing
    (CONTRACT.md 4 item 7). A migration run goes to start_migration."""
    st.refuse_if_open(state)
    if args.kind == "migration":
        return start_migration(args, state)
    requests, texts = research.find_requests(args.project, args.run_number)
    if not requests:
        raise Refusal(f"No open requests tagged #research/run-{args.run_number}.")
    # The Research workflow lives outside the plugin's workflows/ folder, so it is no slash command. The
    # Workflow tool runs a script only from a folder the session can read, so start copies it into the
    # project's .runs/ before claiming the run, overwriting the last run's copy.
    workflow = os.path.join(args.project, ".runs", "research.js")
    shutil.copyfile(WORKFLOW_SCRIPT, workflow)
    run = st.claim_run(args.project, "research", run_number=args.run_number)
    snapshot.save(args.project, run["id"], texts)
    snapshot.write_json(os.path.join(snapshot.run_folder(args.project, run["id"]), "requests.json"), requests)
    print(f"run_id: {run['id']}")
    print(f"requests: {len(requests)}")
    print(f"workflow: {workflow}")
    return 0


def start_migration(args, state):
    """Scan first; with no new work, refuse and claim nothing. Otherwise claim the run, copy every story
    note, fingerprint every other covered note, and write the batches file (spec-run-manager.md 04 items
    9, 21, 22; 07.1 item 1; CONTRACT.md 5.1)."""
    data, texts, carried = scan.scan(args.project, state["handled"])
    if not data["batches"]:
        raise Refusal("No new work since the last migration run.")
    run = st.claim_run(args.project, "migration", request=args.request)
    os.makedirs(os.path.join(args.project, ".runs", "units"), exist_ok=True)  # CONTRACT.md 5.1 item 4
    snapshot.save(args.project, run["id"], texts)
    snapshot.write_json(os.path.join(snapshot.run_folder(args.project, run["id"]), "batches.json"), data)
    # The handled entries the scan matched by link targets left out or in another story note, which close
    # brings up to date (spec-run-manager.md 07.1 item 13; CONTRACT.md 5.6 item 4).
    snapshot.write_json(os.path.join(snapshot.run_folder(args.project, run["id"]), scan.CARRIED), carried)
    print(f"run_id: {run['id']}")
    print(f"batches: {len(data['batches'])}")
    return 0


def _research_run(state, step):
    run = st.require_step(state, step)
    if run["kind"] != "research":
        raise Refusal(f"Run {run['id']} is a {run['kind']} run; this step is for research runs.")
    return run


def cmd_mark(args, state):
    """Connect each answered request to its research note: write the link lines and closes, then wait for
    flags-1 (spec-run-manager.md 04 items 18, 19; 08.4). With --stopped, the writer stopped the workflow:
    no note is edited, the open run gets `stopped: true`, and every request stays open with "You stopped
    this run." as why (09.4 item 2; CONTRACT.md 6 item 6)."""
    run = _research_run(state, "started")
    if args.stopped:
        research.mark_stopped(args.project, run)
        run["stopped"] = True
        st.set_step(args.project, state, "marked", 1)
        print(f"{research.STOPPED} Every request stays open. next: run editguard check for flags-1.json, then act")
        return 0
    result = research.mark(args.project, run)
    st.set_step(args.project, state, "marked", 1)
    if result["outcomes_refused"]:
        print(f"{result['outcomes_refused']} Every request stays open.")
    print(f"closed: {len(result['closed'])}; next: run editguard check for flags-1.json, then act")
    return 0


def cmd_act(args, state):
    """Act on the awaited flags file. If act edited anything, wait for one more check; otherwise
    next_check becomes null (spec-run-manager.md 04 item 18; CONTRACT.md 4 item 5). A migration run's
    act goes to flags.act (CONTRACT.md 5.5 items 2, 5, 8)."""
    if state["open_run"] is not None and state["open_run"]["kind"] == "migration":
        print(flags.act(args.project, state))
        return 0
    run = _research_run(state, "marked")
    edited, report = act.act(args.project, run)
    st.set_step(args.project, state, "acted", run["next_check"] + 1 if edited else None)
    print(f"closes undone: {len(report['closes_undone'])}; lines put back: {len(report['lines_put_back'])}; "
          f"notes named: {len(report['named'])}")
    return 0


def cmd_close(args, state):
    """Write the run log in Runs/, the history entry, clear the open run, then keep only the last 3
    snapshots (spec-run-manager.md 04 items 8, 17, 18; 06.1; CONTRACT.md 4 items 2 and 4). Refuses until
    the awaited flags file exists. A migration run goes to migration/close.py (CONTRACT.md 5.6)."""
    if state["open_run"] is not None and state["open_run"]["kind"] == "migration":
        print(migration_close.close(args.project, state))
        return 0
    run = _research_run(state, "acted")
    if run["next_check"] is not None:
        act.load_flags(args.project, run, run["next_check"])
    ended = st.now().strftime(st.CLOCK_FORMAT)
    log_name, text, failed = runlog.build(args.project, state, run)
    runs = os.path.join(args.project, "Runs")
    os.makedirs(runs, exist_ok=True)
    write_note_whole(os.path.join(runs, log_name), text)
    state["history"].append({"id": run["id"], "kind": run["kind"], "run_number": run.get("run_number"),
                             "started": run["started"], "ended": ended,
                             "how": "recovered" if run.get("recovering") else "closed", "failed": failed})
    state["open_run"] = None
    st.save_state(args.project, state)
    snapshot.prune(args.project)
    print(f"run log: Runs/{log_name}")
    return 0


def cmd_record(args, state):
    """Check the batch's record file and write the cut-down record; with --failed, deal with a migrator
    that failed for good (spec-run-manager.md 04 item 22; CONTRACT.md 5.3 items 1 to 6)."""
    print((record.record_failed if args.failed else record.record)(args.project, state))
    return 0


def cmd_findings(args, state):
    """Check the migration-verifier's findings and act on each verdict; with --failed, undo every unit
    the check didn't judge (spec-run-manager.md 04 item 22; CONTRACT.md 5.3 items 7 to 9). At `judging`,
    the flag findings instead (CONTRACT.md 5.5 item 4)."""
    run = state["open_run"]
    module = flags if run is not None and run["step"] == "judging" else findings
    print((module.findings_failed if args.failed else module.findings)(args.project, state))
    return 0


def cmd_pointers(args, state):
    """Write every pointer for the run's approved migrate units, then wait for the Edit guard
    (spec-run-manager.md 04 item 22; 05 item 1; 08.2; CONTRACT.md 5.4)."""
    print(pointers.pointers(args.project, state))
    return 0


def cmd_recover(args, state):
    """Pick up a crashed research run from the step it reached (spec-run-manager.md 09.2 item 4;
    CONTRACT.md 4 items 4, 14, 15). At started or marked, mark runs again; at acted, nothing is redone.
    The open run gets "recovering": true, so close writes a recover log. A crashed migration run has every
    unit undone instead (09.2 item 3; CONTRACT.md 5.6 item 7)."""
    run = state["open_run"]
    if run is None:
        raise Refusal("No open run to recover.")
    st.refuse_if_recover_tried(run)  # one try per run (spec-run-manager.md 09.2 item 6)
    if run["kind"] == "migration":  # CONTRACT.md 5.6 items 7 to 9
        print(recover.recover(args.project, state))
        return 0
    if run["step"] not in ("started", "marked", "acted"):
        raise Refusal(f"Run {run['id']} is at step '{run['step']}', which recover doesn't know.")
    # Saved before mark edits any note, so a recover that fails partway still counts as its try
    # (spec-run-manager.md 09.2 item 6; 11 item 108; CONTRACT.md 4 item 4).
    st.mark_recover_tried(args.project, state)
    n = run.get("next_check")
    unchecked = n is not None and not os.path.isfile(act.flags_path(args.project, run, n))
    run["markup_unchecked"] = bool(run.get("markup_unchecked") or unchecked)
    run.setdefault("recover_started", st.now().strftime(st.CLOCK_FORMAT))
    run["recovering"] = True
    if run["step"] in ("started", "marked"):
        research.mark(args.project, run)
        run["step"], run["next_check"] = "marked", 1
    st.save_state(args.project, state)
    print(f"recovering {run['id']}; next: {next_step_text(run)}")
    return 0


def cmd_abandon(args, state):
    """Close a run recover couldn't clear: edit no note, write the abandon log, add the history entry, and
    clear the open run. Refuses unless recover has had its try. When the log can't be written, the run
    still closes and the log's text is printed (spec-run-manager.md 09.3; CONTRACT.md 6)."""
    print(abandon.abandon(args.project, state))
    return 0


# One function per subcommand, taking (args, state), where state is the run state main() already loaded.
COMMANDS = {
    "init": cmd_init,
    "status": cmd_status,
    "start": cmd_start,
    "mark": cmd_mark,
    "act": cmd_act,
    "close": cmd_close,
    "recover": cmd_recover,
    "abandon": cmd_abandon,
    "record": cmd_record,
    "findings": cmd_findings,
    "pointers": cmd_pointers,
}


def build_parser():
    ap = argparse.ArgumentParser(prog="runmanager", description="Runs the pre-writing runs.")
    sub = ap.add_subparsers(dest="command", required=True)
    helps = {"init": "create the run state for a new project", "status": "print the open run and what comes next",
             "start": "claim a run and save its snapshot", "mark": "connect each answered request to its research note",
             "act": "act on the latest flags file", "close": "write the run log and close the run",
             "recover": "deal with a crashed or stalled run",
             "abandon": "close a run recover couldn't clear, editing no note",
             "record": "check the batch's record file and write the cut-down record",
             "findings": "check the migration-verifier's findings and act on them",
             "pointers": "write the migrated-to pointers for the run's approved units"}
    for name, text in helps.items():
        p = sub.add_parser(name, help=text)
        p.add_argument("--project", required=True, help="the project folder")
        if name == "start":
            p.add_argument("--kind", required=True, choices=["research", "migration"], help="the run kind")
            p.add_argument("--run-number", dest="run_number", type=int,
                           help="the research run number (research runs only, and required there)")
            p.add_argument("--request", help="the writer's typed request (migration runs)")
        if name == "mark":
            p.add_argument("--stopped", action="store_true",
                           help="the writer stopped the research workflow; edit nothing (research runs)")
        if name in ("record", "findings"):
            p.add_argument("--failed", action="store_true", help="the part before this step failed for good")
    return ap


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "start" and args.kind == "research" and args.run_number is None:
        parser.error("--run-number is required for a research run")
    try:
        # Every command except init stops here when the run state is missing or unreadable
        # (spec-run-manager.md 04 item 11).
        state = None if args.command == "init" else st.load_state(args.project)
        return COMMANDS[args.command](args, state)
    except Refusal as e:
        print(f"runmanager: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
