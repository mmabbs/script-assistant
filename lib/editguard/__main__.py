"""The `editguard check` command."""
import argparse
import json
import sys

from . import rules_migration, rules_research
from .compare import diff_notes, notes_under
from .explain import InputError, build_context, explain, recorded_lines
from .flags import drop_asked, make_flag, number_flags, write_flags
from .inputs import check_inputs


def build_parser():
    ap = argparse.ArgumentParser(prog="editguard", description="Checks a run's changes to the writer's notes.")
    sub = ap.add_subparsers(dest="command", required=True)
    c = sub.add_parser("check", help="check one run and write a flags file")
    c.add_argument("--kind", required=True, choices=["research", "migration"], help="the run kind")
    c.add_argument("--project", required=True, help="the project folder")
    c.add_argument("--snapshot", required=True, help="the before-snapshot folder")
    c.add_argument("--fingerprints", required=True, help="the fingerprints file")
    c.add_argument("--out", required=True, help="the flags file to write")
    r = c.add_argument_group("research runs only (both required)")
    r.add_argument("--requests", help="the requests file")
    r.add_argument("--outcomes", help="the outcomes file")
    m = c.add_argument_group("migration runs only (all three required)")
    m.add_argument("--records", nargs="*", help="the unit record files; none when a batch failed before any valid record")
    m.add_argument("--run-state", dest="run_state", help="the run state file")
    m.add_argument("--run-id", dest="run_id", help="the run id")
    s = c.add_argument_group("second pass, migration runs only (both or neither)")
    s.add_argument("--judged", help="the first pass's flags file")
    s.add_argument("--findings", help="findings-flags.json from the migration-verifier")
    return ap, c


def check_arguments(ap, c, args):
    research = ("requests", "outcomes")
    migration = ("records", "run_state", "run_id")
    second = ("judged", "findings")
    flag = lambda n: "--" + n.replace("_", "-")
    if args.kind == "research":
        for n in research:
            if getattr(args, n) is None:
                c.error(f"--kind research requires {flag(n)}")
        for n in migration + second:
            if getattr(args, n) is not None:
                c.error(f"{flag(n)} is not allowed with --kind research")
    else:
        for n in migration:
            if getattr(args, n) is None:
                c.error(f"--kind migration requires {flag(n)}")
        for n in research:
            if getattr(args, n) is not None:
                c.error(f"{flag(n)} is not allowed with --kind migration")
        if (args.judged is None) != (args.findings is None):
            c.error("--judged and --findings go together: give both or neither")


def fail(problems):
    first = " ".join(problems[0].split())
    more = f" (and {len(problems) - 1} more)" if len(problems) > 1 else ""
    print(f"editguard: {first}{more}", file=sys.stderr)
    return 1


def run_rules(args, ctx, explained, diffs):
    """Run the markup rules on the explained changes (spec-edit-guard.md 05 item 3), plus the rules
    that look at whole notes. Returns a list of flags without ids."""
    if args.kind == "research":
        snapshot_notes = set(notes_under(args.snapshot)) | {r["note"] for r in ctx.requests}
        return (rules_research.link_line_invalid(explained, ctx, args.project)
                + rules_research.close_invalid(explained, ctx, args.project)
                + rules_research.unexpected_research_note(ctx, args.project, snapshot_notes)
                + rules_research.fingerprint_changed(ctx, args.project, snapshot_notes))
    snapshot_notes = set(notes_under(args.snapshot))
    return (rules_migration.run_all(explained, diffs, ctx, args.project)
            + rules_research.fingerprint_changed(ctx, args.project, snapshot_notes))


def main(argv=None):
    ap, c = build_parser()
    args = ap.parse_args(argv)
    check_arguments(ap, c, args)
    problems = check_inputs(args)
    if problems:
        return fail(problems)
    try:
        ctx = build_context(args)
        only = [r["note"] for r in ctx.requests] if args.kind == "research" else None
        diffs = diff_notes(args.snapshot, args.project, only, fingerprinted=ctx.fingerprints,
                           recorded=recorded_lines(ctx))
        # explained: every change a record entry or Run manager edit explains, with its unit.
        # The markup rules (Milestones 4 and 5) run on these only (spec-edit-guard.md 05 item 3).
        explained, unexplained = explain(diffs, ctx)
        flags = [make_flag("unexplained-change", c) for c in unexplained]
        flags += run_rules(args, ctx, explained, diffs)
        if args.judged:
            # The second pass (spec-edit-guard.md 07). Shapes were checked by check_inputs.
            with open(args.judged, encoding="utf-8") as f:
                judged = json.load(f)
            with open(args.findings, encoding="utf-8") as f:
                findings = json.load(f)
            try:
                flags = drop_asked(flags, judged, findings)
            except ValueError as e:
                raise InputError(f"{args.findings}: {e}")
    except InputError as e:
        return fail([str(e)])
    except UnicodeDecodeError as e:
        return fail([f"a note is not UTF-8 text: {e}"])
    except OSError as e:
        return fail([f"{e.filename or 'a note'}: cannot read: {e.strerror or e}"])
    try:
        write_flags(args.out, number_flags(flags))
    except OSError as e:
        return fail([f"{args.out}: cannot write: {e.strerror or e}"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
