"""Reads and checks every input. Returns a list of problems; empty means every input is usable."""
import json
import os

# Copied from evals/_tools/record-check.py (constants used by check_schema).
UNIT_ACTIONS = {"migrate", "reject", "edit"}
STATUSES = {"tentative", "provisional", "committed", "rejected"}
STATUS_FROM = {"tag", "comment", "parent tag", "request", "default"}
TRIGGER_KINDS = {"tag", "comment", "request"}


# Copied from evals/_tools/record-check.py, unchanged.
def check_schema(rec):
    """Return a list of problems with the record's shape (spec-migrator.md 05.2)."""
    bad = []
    if not isinstance(rec, dict):
        return ["top level is not a JSON object"]
    for k in ("units", "left_in_place", "questions", "could_not"):
        if k not in rec:
            bad.append(f"top level: missing '{k}'")
        elif not isinstance(rec[k], list):
            bad.append(f"top level: '{k}' is not a list")

    def need(obj, keys, where):
        if not isinstance(obj, dict):
            bad.append(f"{where}: not an object")
            return False
        for k in keys:
            if k not in obj:
                bad.append(f"{where}: missing '{k}'")
        return True

    for i, u in enumerate(rec.get("units") or []):
        w = f"units[{i}]" + (f" ({u.get('id')})" if isinstance(u, dict) and u.get("id") else "")
        if not need(u, ("id", "action", "trigger", "sources", "copies", "edits", "status", "status_from", "why"), w):
            continue
        if "action" in u and u["action"] not in UNIT_ACTIONS:
            bad.append(f"{w}: action {u['action']!r} is not one of {sorted(UNIT_ACTIONS)}")
        if "status" in u and u["status"] not in STATUSES:
            bad.append(f"{w}: status {u['status']!r} is not one of {sorted(STATUSES)}")
        if "status_from" in u and u["status_from"] not in STATUS_FROM:
            bad.append(f"{w}: status_from {u['status_from']!r} is not one of {sorted(STATUS_FROM)}")
        if "trigger" in u and need(u["trigger"], ("kind", "text"), f"{w}.trigger"):
            if u["trigger"].get("kind") not in TRIGGER_KINDS:
                bad.append(f"{w}.trigger: kind {u['trigger'].get('kind')!r} is not one of {sorted(TRIGGER_KINDS)}")
        for field, keys in (("sources", ("note", "line", "text")),
                            ("copies", ("note", "under", "lines")),
                            ("edits", ("note", "line", "before", "after"))):
            v = u.get(field)
            if field in u and not isinstance(v, list):
                bad.append(f"{w}: '{field}' is not a list")
                continue
            for j, e in enumerate(v or []):
                if need(e, keys, f"{w}.{field}[{j}]") and field == "copies":
                    if "lines" in e and not (isinstance(e["lines"], list) and all(isinstance(x, str) for x in e["lines"])):
                        bad.append(f"{w}.copies[{j}]: 'lines' is not a list of strings")
    for field, extra in (("left_in_place", "why"), ("questions", "ask"), ("could_not", "what")):
        for i, e in enumerate(rec.get(field) or []):
            if need(e, (extra,), f"{field}[{i}]") and "source" in e:
                # A could_not entry for a story note the migrator couldn't read names the note alone
                # (spec-run-manager.md 07.1 item 14).
                only_note = field == "could_not" and isinstance(e["source"], dict) \
                    and "line" not in e["source"] and "text" not in e["source"]
                need(e["source"], ("note",) if only_note else ("note", "line", "text"), f"{field}[{i}].source")
    return bad


UNIT_STATES = {"approved", "pointer-written", "undone"}
OUTCOMES = {"passed", "failed", "no findings"}
VERDICTS = {"asked", "not-asked"}


def _load(path, label, problems):
    """Parse a JSON file. On failure, add one problem naming the file and return None."""
    if not os.path.isfile(path):
        problems.append(f"{label}: file not found: {path}")
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        problems.append(f"{label}: does not parse: {e}")
    except OSError as e:
        problems.append(f"{label}: cannot read: {e.strerror or e}")
    return None


def _entries(data, label, keys, problems, extra=None):
    """Check a list of objects that each hold the given keys. extra(entry, where) returns more problems."""
    if not isinstance(data, list):
        problems.append(f"{label}: top level is not a list")
        return
    for i, e in enumerate(data):
        where = f"{label}: entry {i}"
        if not isinstance(e, dict):
            problems.append(f"{where}: not an object")
            continue
        for k in keys:
            if k not in e:
                problems.append(f"{where}: missing '{k}'")
        if extra:
            problems.extend(extra(e, where))


def _check_folder(path, label, problems):
    if not os.path.isdir(path):
        problems.append(f"{label}: not an existing folder: {path}")


def check_inputs(args):
    """Check every input named in args. Returns a list of problem strings, each starting with the file."""
    problems = []
    _check_folder(args.project, "--project", problems)
    _check_folder(args.snapshot, "--snapshot", problems)

    # Both run kinds write a fingerprints file (spec-run-manager.md 04 item 14).
    data = _load(args.fingerprints, args.fingerprints, problems)
    if data is not None:
        if not isinstance(data, dict):
            problems.append(f"{args.fingerprints}: top level is not an object")
        else:
            for k, v in data.items():
                if not isinstance(v, str):
                    problems.append(f"{args.fingerprints}: value for {k!r} is not a string")

    if args.kind == "research":
        data = _load(args.requests, args.requests, problems)
        if data is not None:
            _entries(data, args.requests, ("id", "note", "line", "text", "comment"), problems)

        def outcome_extra(e, where):
            if "outcome" in e and e["outcome"] not in OUTCOMES:
                return [f"{where}: outcome {e['outcome']!r} is not one of {sorted(OUTCOMES)}"]
            return []
        data = _load(args.outcomes, args.outcomes, problems)
        if data is not None:
            _entries(data, args.outcomes, ("request", "outcome", "note", "reason", "failed_topics"),
                     problems, outcome_extra)
    else:
        for path in args.records:
            data = _load(path, path, problems)
            if data is not None:
                problems.extend(f"{path}: {p}" for p in check_schema(data))

        def unit_extra(e, where):
            out = []
            if "state" in e and e["state"] not in UNIT_STATES:
                out.append(f"{where}: state {e['state']!r} is not one of {sorted(UNIT_STATES)}")
            if "pointed_lines" in e and not (isinstance(e["pointed_lines"], list)
                                             and all(isinstance(x, str) for x in e["pointed_lines"])):
                out.append(f"{where}: 'pointed_lines' is not a list of strings")
            return out
        data = _load(args.run_state, args.run_state, problems)
        if data is not None:
            if not isinstance(data, dict):
                problems.append(f"{args.run_state}: top level is not an object")
            elif not isinstance(data.get("unit_index"), list):
                problems.append(f"{args.run_state}: 'unit_index' is missing or not a list")
            else:
                _entries(data["unit_index"], f"{args.run_state}: unit_index",
                         ("run", "unit", "state", "pointed_lines"), problems, unit_extra)

        if args.judged:
            data = _load(args.judged, args.judged, problems)
            if data is not None:
                _entries(data, args.judged, ("id", "rule", "note", "before", "after", "unit"), problems)

            def finding_extra(e, where):
                if "verdict" in e and e["verdict"] not in VERDICTS:
                    return [f"{where}: verdict {e['verdict']!r} is not one of {sorted(VERDICTS)}"]
                return []
            data = _load(args.findings, args.findings, problems)
            if data is not None:
                if not isinstance(data, dict) or not isinstance(data.get("flags"), list):
                    problems.append(f"{args.findings}: 'flags' is missing or not a list")
                else:
                    _entries(data["flags"], f"{args.findings}: flags", ("flag", "verdict", "asked_by"),
                             problems, finding_extra)
    return problems
