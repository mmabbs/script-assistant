#!/usr/bin/env python3
"""Hand runner for the migrator eval cases. Not part of claude plugin eval.

Usage: migrator-run.py --out <dir> [--cases <name> ...] [--runs N]

For each case and run it makes <dir>/<case>/r<n>/, with:
  work/              the fixture's folder, where the agent runs (rules/, project/, run/unit-records.json)
  before/            a copy of work/project taken before the agent ran
  stream.jsonl       the agent's stream-json output
  stderr.txt         the agent's stderr
  record-check.txt   the output of record-check.py
Default: every migrator case, 3 runs each, at most 5 runs at a time. See evals/README.md.
"""
import argparse, json, os, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

TOOLS = os.path.dirname(os.path.abspath(__file__))
EVALS = os.path.dirname(TOOLS)
PLUGIN = os.path.dirname(EVALS)
RECORD_CHECK = os.path.join(TOOLS, "record-check.py")
TIMEOUT = 900
MAX_PARALLEL = 5
ENV = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}


def all_cases():
    return sorted(d for d in os.listdir(EVALS)
                  if not d.startswith(("_", ".", "research-", "migration-verifier-")) and os.path.isfile(os.path.join(EVALS, d, "prompt.md")))


def prompt_body(case):
    text = open(os.path.join(EVALS, case, "prompt.md"), encoding="utf-8").read()
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        text = text[end + len("\n---\n"):]
    return text.strip()


def cost_from_stream(path):
    cost = None
    try:
        with open(path, encoding="utf-8") as f:
            for raw in f:
                try:
                    ev = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                if ev.get("type") == "result" and ev.get("total_cost_usd") is not None:
                    cost = ev["total_cost_usd"]
    except OSError:
        pass
    return cost


def one(case, n, out):
    base = os.path.join(out, case, f"r{n}")
    work, before = os.path.join(base, "work"), os.path.join(base, "before")
    stream, stderr_path = os.path.join(base, "stream.jsonl"), os.path.join(base, "stderr.txt")
    os.makedirs(work)
    t0 = time.time()

    fx = subprocess.run(["bash", os.path.join(EVALS, case, "fixture.sh")], cwd=work, env=ENV,
                        capture_output=True, text=True)
    if fx.returncode != 0:
        with open(stderr_path, "w") as f:
            f.write("fixture.sh failed\n" + fx.stdout + fx.stderr)
        return case, n, f"fixture failed (exit {fx.returncode})", round(time.time() - t0), None, "not run"
    shutil.copytree(os.path.join(work, "project"), before)

    cmd = ["claude", "-p", prompt_body(case), "--agent", "script-asst:migrator", "--plugin-dir", PLUGIN,
           "--setting-sources", "project", "--tools", "Read,Write,Edit,Glob,Grep", "--strict-mcp-config",
           "--permission-mode", "acceptEdits", "--output-format", "stream-json", "--verbose",
           "--no-session-persistence"]
    proc = None
    with open(stream, "w") as so, open(stderr_path, "w") as se:
        try:
            proc = subprocess.Popen(cmd, cwd=work, env=ENV, stdout=so, stderr=se, text=True)
            proc.wait(timeout=TIMEOUT)
            status = f"exit {proc.returncode}"
        except subprocess.TimeoutExpired:
            status = f"timeout after {TIMEOUT}s"
        finally:
            if proc and proc.poll() is None:
                proc.kill()
                proc.wait()

    rc = subprocess.run([sys.executable, RECORD_CHECK, work, before, "--stream", stream],
                        capture_output=True, text=True)
    with open(os.path.join(base, "record-check.txt"), "w") as f:
        f.write(rc.stdout + rc.stderr)
    check = "record-check PASS" if rc.returncode == 0 else "record-check FAIL"
    return case, n, status, round(time.time() - t0), cost_from_stream(stream), check


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="output folder; each run gets <out>/<case>/r<n>/")
    ap.add_argument("--cases", nargs="+", help="case folder names (default: all)")
    ap.add_argument("--runs", type=int, default=3)
    args = ap.parse_args()

    known = all_cases()
    cases = args.cases or known
    unknown = [c for c in cases if c not in known]
    if unknown:
        sys.exit(f"unknown case(s): {', '.join(unknown)}")
    out = os.path.abspath(args.out)
    jobs = [(c, n) for c in cases for n in range(1, args.runs + 1)]
    taken = [os.path.join(out, c, f"r{n}") for c, n in jobs if os.path.exists(os.path.join(out, c, f"r{n}"))]
    if taken:
        sys.exit(f"already exists, will not overwrite: {taken[0]}")

    print(f"{len(jobs)} run(s) into {out}", flush=True)
    total = 0.0
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futs = {ex.submit(one, c, n, out): (c, n) for c, n in jobs}
        for fut in as_completed(futs):
            try:
                case, n, status, secs, cost, check = fut.result()
            except Exception as e:
                c, n = futs[fut]
                print(f"{c} r{n}: runner error: {e!r}", flush=True)
                continue
            cost_s = f"${cost:.2f}" if cost is not None else "cost n/a"
            total += cost or 0.0
            print(f"{case} r{n}: {status}, {secs}s, {cost_s}, {check}", flush=True)
    print(f"ALL DONE. Reported cost: ${total:.2f}", flush=True)


if __name__ == "__main__":
    main()
