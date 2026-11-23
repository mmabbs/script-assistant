#!/usr/bin/env python3
"""Code checks on one migrator run against its unit record (spec-migrator.md 05 and 11).

Usage: record-check.py <work-dir> <before-dir> [--stream PATH]

<work-dir>   the folder the agent ran in. It holds project/ and run/unit-records.json.
<before-dir> a copy of project/ taken after the fixture ran and before the agent ran.
--stream     the run's stream-json log. Default: <work-dir>/stream.jsonl, then <work-dir>/../stream.jsonl.

Prints one PASS/FAIL line per check, with each offending line indented under a FAIL.
Exits 1 if any check fails. Standard library only.
"""
import argparse, difflib, json, os, sys

UNIT_ACTIONS = {"migrate", "reject", "edit"}
STATUSES = {"tentative", "provisional", "committed", "rejected"}
STATUS_FROM = {"tag", "comment", "parent tag", "request", "default"}
TRIGGER_KINDS = {"tag", "comment", "request"}
RECORD_REL = os.path.join("run", "unit-records.json")


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()


def notes_under(root):
    out = {}
    if not os.path.isdir(root):
        return out
    for dp, _, files in os.walk(root):
        for fn in files:
            if fn.endswith(".md"):
                full = os.path.join(dp, fn)
                out[os.path.relpath(full, root)] = full
    return out


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


def diff_notes(before_dir, project_dir):
    """Return (added, removed): lists of (note, line_no, text). Blank lines are skipped."""
    before, after = notes_under(before_dir), notes_under(project_dir)
    added, removed = [], []
    for note in sorted(set(before) | set(after)):
        a = read_lines(before[note]) if note in before else []
        b = read_lines(after[note]) if note in after else []
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag in ("replace", "delete"):
                removed += [(note, i + 1, a[i]) for i in range(i1, i2) if a[i].strip()]
            if tag in ("replace", "insert"):
                added += [(note, j + 1, b[j]) for j in range(j1, j2) if b[j].strip()]
    return added, removed


def tool_calls(stream_path):
    """Yield (index, name, file_path, tool_use_id) for each Write/Edit tool call, plus a set of errored ids."""
    calls, errored = [], set()
    with open(stream_path, encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                ev = json.loads(raw)
            except json.JSONDecodeError:
                continue
            content = (ev.get("message") or {}).get("content")
            if not isinstance(content, list):
                continue
            for item in content:
                if not isinstance(item, dict):
                    continue
                if ev.get("type") == "assistant" and item.get("type") == "tool_use" \
                        and item.get("name") in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
                    fp = (item.get("input") or {}).get("file_path") or (item.get("input") or {}).get("notebook_path") or ""
                    calls.append((len(calls), item["name"], fp, item.get("id")))
                if ev.get("type") == "user" and item.get("type") == "tool_result" and item.get("is_error"):
                    errored.add(item.get("tool_use_id"))
    return calls, errored


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("work_dir")
    ap.add_argument("before_dir")
    ap.add_argument("--stream")
    args = ap.parse_args()

    work = os.path.realpath(args.work_dir)
    before = os.path.realpath(args.before_dir)
    project = os.path.join(work, "project")
    record_path = os.path.join(work, RECORD_REL)
    results = []  # (ok, name, [offending lines])

    # 1. Record exists, parses, has the spec 05.2 fields.
    rec = None
    if not os.path.isfile(record_path):
        results.append((False, "record file exists, parses, and has the spec 05.2 fields", [f"not found: {RECORD_REL}"]))
    else:
        try:
            with open(record_path, encoding="utf-8") as f:
                rec = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            results.append((False, "record file exists, parses, and has the spec 05.2 fields", [f"does not parse: {e}"]))
        else:
            bad = check_schema(rec)
            results.append((not bad, "record file exists, parses, and has the spec 05.2 fields", bad))
            if not isinstance(rec, dict):
                rec = None

    units = [u for u in (rec or {}).get("units") or [] if isinstance(u, dict)]
    copy_lines = set()
    copies = []  # (unit id, note, line)
    edit_after, edit_before, reject_sources = set(), set(), set()
    for u in units:
        for c in u.get("copies") or []:
            if isinstance(c, dict):
                for ln in c.get("lines") or []:
                    if isinstance(ln, str):
                        copy_lines.add(ln)
                        copies.append((u.get("id"), c.get("note"), ln))
        for e in u.get("edits") or []:
            if isinstance(e, dict):
                if isinstance(e.get("after"), str):
                    edit_after.add(e["after"])
                if isinstance(e.get("before"), str):
                    edit_before.add(e["before"])
        if u.get("action") == "reject":
            for s in u.get("sources") or []:
                if isinstance(s, dict) and isinstance(s.get("text"), str):
                    reject_sources.add(s["text"])
    no_rec = [] if rec is not None else ["(no usable record, so nothing is accounted for)"]

    # 2 and 3. Diff the notes against the before copy.
    if not os.path.isdir(before):
        results.append((False, "every added line is in the record (copies[].lines or edits[].after)", [f"before-dir not found: {before}"]))
        results.append((False, "every removed or changed line is in the record (reject sources or edits[].before)", [f"before-dir not found: {before}"]))
    else:
        added, removed = diff_notes(before, project)
        bad = [f"{n}:{i}: {t}" for n, i, t in added if t not in copy_lines and t not in edit_after]
        results.append((not bad, "every added line is in the record (copies[].lines or edits[].after)", (no_rec if bad else []) + bad))
        bad = [f"{n}:{i} (before): {t}" for n, i, t in removed if t not in reject_sources and t not in edit_before]
        results.append((not bad, "every removed or changed line is in the record (reject sources or edits[].before)", (no_rec if bad else []) + bad))

    # 4. Every copies[].lines entry appears in the note it names.
    bad, cache = [], {}
    for uid, note, ln in copies:
        if not isinstance(note, str):
            bad.append(f"{uid}: copy has no note path: {ln}")
            continue
        path = os.path.join(project, note)
        if path not in cache:
            cache[path] = set(read_lines(path)) if os.path.isfile(path) else None
        if cache[path] is None:
            bad.append(f"{uid}: note not found: {note}")
        elif ln not in cache[path]:
            bad.append(f"{uid}: not in {note}: {ln}")
    if rec is None:
        bad = no_rec + bad
    results.append((not bad, "every copies[].lines entry appears in the note it names", bad))

    # 5. The record Write comes before the first Write/Edit under project/.
    name = "the record file is written before the first Write/Edit to project/"
    stream = args.stream
    if not stream:
        for cand in (os.path.join(work, "stream.jsonl"), os.path.join(os.path.dirname(work), "stream.jsonl")):
            if os.path.isfile(cand):
                stream = cand
                break
    if not stream or not os.path.isfile(stream):
        results.append((False, name, ["stream.jsonl not found"]))
    else:
        calls, errored = tool_calls(stream)

        def resolve(fp):
            return os.path.realpath(fp if os.path.isabs(fp) else os.path.join(work, fp))
        rec_real = os.path.realpath(record_path)
        first_rec = next((c for c in calls if c[1] == "Write" and resolve(c[2]) == rec_real and c[3] not in errored), None)
        first_proj = next((c for c in calls if resolve(c[2]).startswith(project + os.sep)), None)
        if first_rec is None:
            results.append((False, name, ["no successful Write of run/unit-records.json in the stream"]))
        elif first_proj is not None and first_proj[0] < first_rec[0]:
            results.append((False, name, [f"tool call {first_proj[0] + 1} ({first_proj[1]} {first_proj[2]}) "
                                          f"comes before the record Write (tool call {first_rec[0] + 1})"]))
        else:
            results.append((True, name, []))

    for ok, label, lines in results:
        print(f"{'PASS' if ok else 'FAIL'}  {label}")
        for ln in ([] if ok else lines):
            print(f"      {ln}")
    sys.exit(0 if all(ok for ok, _, _ in results) else 1)


if __name__ == "__main__":
    main()
