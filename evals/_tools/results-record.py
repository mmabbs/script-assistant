#!/usr/bin/env python3
"""Write a results record for a research-run.py --suite migrator run, so the run can be rebuilt if its folder is lost.

Usage: results-record.py <runs-folder> <out.md> <header.md>

<header.md> is the hand-written top of the record: what ran, the results table, and the findings. After it, for
each case and run in <runs-folder>, the record gets the run's grades.txt, a diff of the project before and after,
the unit record, and the final reply. First used for results/2026-10-13-migrator-all-cases-1-20-pieces.md.
"""
import json, os, subprocess, sys

runs, out_path, header_path = sys.argv[1], sys.argv[2], sys.argv[3]
parts = [open(header_path, encoding="utf-8").read().rstrip() + "\n"]
for case in sorted(os.listdir(runs)):
    for r in sorted(os.listdir(os.path.join(runs, case))):
        base = os.path.join(runs, case, r)
        work, before = os.path.join(base, "work"), os.path.join(base, "before")
        grades = open(os.path.join(base, "grades.txt"), encoding="utf-8").read().rstrip()
        n_fail = sum(1 for l in grades.splitlines() if l.startswith("FAIL"))
        n = len(grades.splitlines())
        diff = subprocess.run(["diff", "-ru", os.path.join(before, "project"), os.path.join(work, "project")],
                              capture_output=True, text=True).stdout.replace(base + "/", "")
        try:
            record = json.dumps(json.load(open(os.path.join(work, "run", "unit-records.json"))), indent=2,
                                ensure_ascii=False)
        except (OSError, ValueError) as e:
            record = f"(no readable record: {e})"
        reply = open(os.path.join(base, "reply.txt"), encoding="utf-8").read().strip()
        parts.append(f"\n## {case} {r}: {n - n_fail} of {n} checks\n\n### Grades\n\n```text\n{grades}\n```\n\n"
                     f"### Note changes\n\n```diff\n{diff.rstrip()}\n```\n\n### Unit record\n\n```json\n{record}\n```\n\n"
                     f"### Reply\n\n```text\n{reply}\n```\n")
open(out_path, "w", encoding="utf-8").write("".join(parts))
print(out_path, sum(len(p) for p in parts), "chars")
