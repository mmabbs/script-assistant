#!/usr/bin/env python3
"""Hand runner for the research-, migration-verifier-, and migrator eval cases. Not part of claude plugin eval.

Usage: research-run.py --out <dir> [--suite S] [--cases <name> ...] [--runs N] [--agent NAME | --bare-append FILE] [--keep-transcripts]
       research-run.py --out <dir> --regrade [--suite S] [--cases <name> ...] [--runs N]

With no --agent, each run is bare Claude: the case's prompt body, its allowed_tools, and no agent
instructions (eval-cases-research-workflow.md 01, eval-cases-migration-verifier.md 06). Every call passes --strict-mcp-config, because
headless runs otherwise load the account's claude.ai connectors, Exa web search among them. With --agent, the same prompt goes to that agent.
--bare-append adds FILE's text after the prompt body, on bare runs only: the migration-verifier's prompts carry no answer
shape, which its agent file holds, so bare runs get the shape from _fixtures/bare-shape-migration-verifier-batch.md
(plan-migration-verifier.md 05).

For each case and run it makes <dir>/<case>/r<n>/, with:
  work/          the fixture's folder, where Claude runs
  before/        a copy of work/ taken before Claude ran
  stream.jsonl   Claude's stream-json output
  stderr.txt     Claude's stderr
  reply.txt      Claude's final reply
  grades.txt     one PASS or FAIL line per grader, with its evidence
  judges/        each llm grader's prompt and the judge's full answer; --regrade reuses an
                 answer when its prompt is unchanged

Graders are the files in each case's graders/ folder:
  regex      checked in code against the target file, or the final reply when there is no target;
             match is contains (default), not_contains, or count:N for exactly N matches
  tool_used  counted in code from the stream's tool calls; input_match is matched against the
             call's file_path, relative to work/, when it has one, else against the whole input
  llm        sent to a judge (claude -p, no tools, no MCP servers) with the focus file, or the final reply when there
             is no focus; the judge answers PASS or FAIL on its first line. `also: [path, ...]` adds more
             files from work/ after the focus file, each under its own path line (P5 uses it for run/answer.json)
  same_as    checked in code: the target file in work/ holds the same text as the file at `before:` in
             before/, line for line, ignoring whitespace at line ends and blank lines at the end (the Write
             tool retypes a file, so those can differ). Used for the research-writer's draft-1.md copy.

A case whose prompt.md frontmatter sets `retired` is not run and can't be named with --cases.

When a grader's target note under Research/ is missing and the run wrote exactly one new note
there, the grader reads that note, and the extra check `file-name` fails. So a wrong file name
fails once instead of failing every check on the note.

--suite picks the case folders: research (the default), migration-verifier, or migrator (every other case
folder). --cases names folders from that suite. On the migrator suite, each run's grades also hold one
`record-check` line from record-check.py, which checks the unit record against the notes. Default: every case in the suite, 3 runs each, at most 5 runs at a time. See evals/README.md.
"""
import argparse, json, os, re, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

TOOLS = os.path.dirname(os.path.abspath(__file__))
EVALS = os.path.dirname(TOOLS)
PLUGIN = os.path.dirname(EVALS)
MODEL = "claude-opus-5-5"
JUDGE_MODEL = "claude-opus-5-5"
JUDGE_TIMEOUT = 300
MAX_PARALLEL = 5
ENV = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
JUDGE_FRAME = """You are grading one check in an eval suite. Judge only what the check asks.

The check:

{check}

The text under test ({what}):

<text>
{text}
</text>

Answer with PASS or FAIL alone on the first line. Then give your evidence, quoting the text."""


SUITES = {"research": "research-", "migration-verifier": "migration-verifier-", "migrator": None}
RECORD_CHECK = os.path.join(TOOLS, "record-check.py")
MIGRATOR_TIMEOUT = 900


def in_suite(d, suite):
    if SUITES[suite]:
        return d.startswith(SUITES[suite])
    return not d.startswith(("_", ".") + tuple(p for p in SUITES.values() if p))


def all_cases(suite="research"):
    return sorted(d for d in os.listdir(EVALS)
                  if in_suite(d, suite) and os.path.isfile(os.path.join(EVALS, d, "prompt.md")) and not retired(d))


def retired(case):
    """True when the case's prompt.md frontmatter sets `retired`. Its folder stays; it is just not run."""
    fm, _ = split_frontmatter(open(os.path.join(EVALS, case, "prompt.md"), encoding="utf-8").read())
    return bool(parse_frontmatter(fm).get("retired"))


def same_text(a, b):
    """Compare two files line for line, ignoring whitespace at line ends and blank lines at the end."""
    norm = lambda p: [l.rstrip() for l in open(p, encoding="utf-8").read().rstrip().splitlines()]
    la, lb = norm(a), norm(b)
    if la == lb:
        return True, "same text"
    for i, (x, y) in enumerate(zip(la, lb), 1):
        if x != y:
            return False, f"differs at line {i}: {x[:80]!r} vs {y[:80]!r}"
    return False, f"{len(la)} lines vs {len(lb)}"


def record_check(work, before, stream):
    """record-check.py on a migrator run: (passed, the first FAIL line and what's under it, or 'all checks pass')."""
    rc = subprocess.run([sys.executable, RECORD_CHECK, work, os.path.join(before, "project"), "--stream", stream],
                        capture_output=True, text=True)
    out = rc.stdout + rc.stderr
    fails = [l for l in out.splitlines() if not l.startswith("PASS")]
    return rc.returncode == 0, (" | ".join(fails)[:400] if fails else "all checks pass")


def split_frontmatter(text):
    if text.startswith("---\n"):
        end = text.index("\n---", 4)
        return text[4:end], text[end + 4:].lstrip("-").strip()
    return "", text.strip()


def parse_scalar(v):
    v = v.strip()
    if v.startswith('"'):
        return json.loads(v)
    if v.startswith("{") and v.endswith("}"):
        out = {}
        for part in v[1:-1].split(","):
            k, _, val = part.partition(":")
            out[k.strip()] = val.strip()
        return out
    if v.startswith("[") and v.endswith("]"):
        return [x.strip() for x in v[1:-1].split(",") if x.strip()]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def parse_frontmatter(fm):
    out = {}
    for line in fm.splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            out[k.strip()] = parse_scalar(v)
    return out


def read_case(case):
    fm, body = split_frontmatter(open(os.path.join(EVALS, case, "prompt.md"), encoding="utf-8").read())
    meta = parse_frontmatter(fm)
    graders = []
    gdir = os.path.join(EVALS, case, "graders")
    for name in sorted(os.listdir(gdir)):
        if name.endswith(".md"):
            gfm, gbody = split_frontmatter(open(os.path.join(gdir, name), encoding="utf-8").read())
            g = parse_frontmatter(gfm)
            g["name"], g["body"] = name[:-3], gbody
            graders.append(g)
    return body, meta, graders


def stream_events(path):
    try:
        with open(path, encoding="utf-8") as f:
            for raw in f:
                try:
                    yield json.loads(raw)
                except json.JSONDecodeError:
                    continue
    except OSError:
        return


def final_reply(stream):
    reply, cost = "", None
    for ev in stream_events(stream):
        if ev.get("type") == "result":
            reply = ev.get("result") or ""
            cost = ev.get("total_cost_usd")
    return reply, cost


def tool_calls(stream, work):
    root = os.path.realpath(work) + os.sep
    calls = []
    for ev in stream_events(stream):
        if ev.get("type") == "assistant":
            for item in ev.get("message", {}).get("content", []) or []:
                if item.get("type") == "tool_use":
                    inp = item.get("input", {}) or {}
                    # Match a file tool on its path alone: a note's content can name other folders.
                    path = inp.get("file_path")
                    if path and os.path.realpath(path).startswith(root):
                        path = os.path.realpath(path)[len(root):]
                    calls.append((item.get("name"), path or json.dumps(inp, ensure_ascii=False)))
    return calls


def new_research_notes(work, before):
    research = os.path.join(work, "project", "Research")
    if not os.path.isdir(research):
        return []
    return sorted(n for n in os.listdir(research) if n.endswith(".md")
                  and not os.path.exists(os.path.join(before, "project", "Research", n)))


def resolve(work, before, rel, notes):
    """Return (path or None, note about the substitution or '')."""
    path = os.path.join(work, rel)
    if os.path.isfile(path):
        return path, ""
    if rel.startswith("project/Research/") and len(notes) == 1:
        return os.path.join(work, "project", "Research", notes[0]), f"read {notes[0]} in its place"
    return None, f"{rel} not written"


def judge(g, text, what, jdir):
    prompt = JUDGE_FRAME.format(check=g["body"], what=what, text=text)
    os.makedirs(jdir, exist_ok=True)
    ppath, apath = (os.path.join(jdir, g["name"] + ext) for ext in (".prompt.txt", ".answer.txt"))
    if os.path.isfile(ppath) and os.path.isfile(apath) and open(ppath).read() == prompt:
        answer, cost = open(apath).read(), 0.0  # same prompt: keep the earlier answer
        return verdict_of(answer) + (cost,)
    with open(ppath, "w") as f:
        f.write(prompt)
    cmd = ["claude", "-p", "--model", JUDGE_MODEL, "--setting-sources", "project", "--tools", "",
           "--strict-mcp-config", "--output-format", "json", "--no-session-persistence"]
    try:
        p = subprocess.run(cmd, input=prompt, cwd=jdir, env=ENV, capture_output=True, text=True,
                           timeout=JUDGE_TIMEOUT)
        res = json.loads(p.stdout)
        answer, cost = res.get("result") or "", res.get("total_cost_usd") or 0.0
    except (subprocess.TimeoutExpired, json.JSONDecodeError) as e:
        answer, cost = f"JUDGE ERROR: {e!r}", 0.0
    with open(apath, "w") as f:
        f.write(answer)
    return verdict_of(answer) + (cost,)


def verdict_of(answer):
    first = answer.strip().splitlines()[0].strip(" *#").upper() if answer.strip() else ""
    verdict = "PASS" if first.startswith("PASS") else "FAIL"
    return verdict, " ".join(answer.strip().splitlines()[1:])[:400]


def grade(graders, work, before, stream, base, check_record=False):
    reply, _ = final_reply(stream)
    calls = tool_calls(stream, work)
    notes = new_research_notes(work, before)
    lines, judge_cost, substituted = [], 0.0, False
    for g in graders:
        kind, name = g.get("type"), g["name"]
        if kind == "tool_used":
            hits = [inp for tool, inp in calls if tool == g["tool"] and re.search(g.get("input_match", "."), inp)]
            ok = int(g.get("min", 0)) <= len(hits) <= int(g.get("max", 10**9))
            detail = f"{len(hits)} {g['tool']} call(s) matching /{g.get('input_match')}/"
            if hits:
                detail += ": " + hits[0][:200]
            lines.append((name, ok, detail))
            continue
        if kind == "same_as":
            path, ref = os.path.join(work, g["target"]["path"]), os.path.join(before, g["before"])
            if not os.path.isfile(path):
                lines.append((name, False, f"{g['target']['path']} not written"))
            elif not os.path.isfile(ref):
                lines.append((name, False, f"{g['before']} not in before/"))
            else:
                lines.append((name,) + same_text(path, ref))
            continue
        loc = g.get("target") if kind == "regex" else g.get("focus")
        if isinstance(loc, dict) and loc.get("source") == "file":
            path, note = resolve(work, before, loc["path"], notes)
            substituted = substituted or note.startswith("read ")
            if path is None:
                lines.append((name, False, note))
                continue
            text, what = open(path, encoding="utf-8").read(), os.path.relpath(path, work)
            for extra in (g.get("also") or []) if kind == "llm" else []:  # more files for the judge, after the focus
                xp = os.path.join(work, extra)
                text += f"\n\n----- {extra} -----\n" + (open(xp, encoding="utf-8").read() if os.path.isfile(xp)
                                                        else "(not written)")
                what += f", then {extra}"
        else:
            text, what, note = reply, "the final reply", ""
        if kind == "regex":
            flags = 0
            for ch in str(g.get("flags", "")):
                flags |= {"m": re.M, "i": re.I, "s": re.S}.get(ch, 0)
            m = re.search(g["pattern"], text, flags)
            mode = str(g.get("match", "contains"))
            if mode.startswith("count:"):  # exactly N matches
                n = len(re.findall(g["pattern"], text, flags))
                ok, detail = n == int(mode[6:]), f"{n} match(es), want {mode[6:]}" + (f"; {note}" if note else "")
            else:
                ok = bool(m) == (mode != "not_contains")
                detail = (f"found {m.group(0)[:120]!r}" if m else "no match") + (f"; {note}" if note else "")
            lines.append((name, ok, detail))
        elif kind == "llm":
            verdict, evidence, cost = judge(g, text, what, os.path.join(base, "judges"))
            judge_cost += cost
            lines.append((name, verdict == "PASS", evidence + (f" [{note}]" if note else "")))
        else:
            lines.append((name, False, f"unknown grader type {kind!r}"))
    if any(str((g.get("target") or g.get("focus") or {}).get("path", "")).startswith("project/Research/")
           for g in graders):
        lines.append(("file-name", not substituted, "expected name written" if not substituted
                      else f"wrote {', '.join(notes)} instead"))
    if check_record:
        lines.append(("record-check",) + record_check(work, before, stream))
    with open(os.path.join(base, "grades.txt"), "w") as f:
        for name, ok, detail in lines:
            f.write(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}\n")
    return sum(ok for _, ok, _ in lines), len(lines), judge_cost


def one(case, n, out, agent, keep, append="", suite="research"):
    body, meta, graders = read_case(case)
    if append:
        body = body.rstrip("\n") + "\n\n" + append
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
        return case, n, f"fixture failed (exit {fx.returncode})", 0, None, 0, 0, 0.0
    shutil.copytree(work, before)

    tools = ",".join(meta.get("allowed_tools") or ["Read", "Write", "Edit", "Glob", "Grep"])
    timeout = int(meta.get("timeout_seconds") or 600) * 2
    if suite == "migrator":
        timeout = max(timeout, MIGRATOR_TIMEOUT)
    cmd = ["claude", "-p", body, "--setting-sources", "project", "--tools", tools, "--strict-mcp-config",
           "--permission-mode", "acceptEdits", "--output-format", "stream-json", "--verbose"]
    cmd += ["--agent", agent, "--plugin-dir", PLUGIN] if agent else ["--model", MODEL]
    if not keep:
        cmd.append("--no-session-persistence")
    proc = None
    with open(stream, "w") as so, open(stderr_path, "w") as se:
        try:
            proc = subprocess.Popen(cmd, cwd=work, env=ENV, stdout=so, stderr=se, text=True)
            proc.wait(timeout=timeout)
            status = f"exit {proc.returncode}"
        except subprocess.TimeoutExpired:
            status = f"timeout after {timeout}s"
        finally:
            if proc and proc.poll() is None:
                proc.kill()
                proc.wait()

    reply, cost = final_reply(stream)
    with open(os.path.join(base, "reply.txt"), "w") as f:
        f.write(reply)
    passed, total, jcost = grade(graders, work, before, stream, base, suite == "migrator")
    return case, n, status, round(time.time() - t0), cost, passed, total, jcost


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="output folder; each run gets <out>/<case>/r<n>/")
    ap.add_argument("--suite", choices=sorted(SUITES), default="research")
    ap.add_argument("--cases", nargs="+", help="case folder names (default: every case in the suite)")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--agent", help="agent to run, such as script-asst:research-writer (default: bare Claude)")
    ap.add_argument("--regrade", action="store_true",
                    help="grade the runs already in --out again, with no new Claude runs")
    ap.add_argument("--bare-append", metavar="FILE",
                    help="on bare runs, add this file's text after the prompt body")
    ap.add_argument("--keep-transcripts", action="store_true",
                    help="save each run's session transcript (leave off for batches)")
    args = ap.parse_args()

    known = all_cases(args.suite)
    cases = args.cases or known
    unknown = [c for c in cases if c not in known]
    gone = [c for c in unknown if os.path.isfile(os.path.join(EVALS, c, "prompt.md")) and retired(c)]
    if gone:
        sys.exit(f"retired case(s), not run: {', '.join(gone)}")
    if unknown:
        sys.exit(f"unknown case(s): {', '.join(unknown)}")
    out = os.path.abspath(args.out)
    if args.bare_append and args.agent:
        sys.exit("--bare-append is for bare runs; leave it off with --agent")
    append = open(args.bare_append, encoding="utf-8").read() if args.bare_append else ""
    if args.regrade:
        for c in cases:
            for n in range(1, args.runs + 1):
                base = os.path.join(out, c, f"r{n}")
                if os.path.isdir(base):
                    p, t, _ = grade(read_case(c)[2], os.path.join(base, "work"), os.path.join(base, "before"),
                                    os.path.join(base, "stream.jsonl"), base, args.suite == "migrator")
                    print(f"{c} r{n}: {p}/{t} checks, {'PASS' if t and p == t else 'FAIL'}", flush=True)
        return
    jobs = [(c, n) for c in cases for n in range(1, args.runs + 1)]
    taken = [os.path.join(out, c, f"r{n}") for c, n in jobs if os.path.exists(os.path.join(out, c, f"r{n}"))]
    if taken:
        sys.exit(f"already exists, will not overwrite: {taken[0]}")

    print(f"{len(jobs)} run(s) into {out}, {args.agent or 'bare ' + MODEL}", flush=True)
    total = 0.0
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futs = {ex.submit(one, c, n, out, args.agent, args.keep_transcripts, append, args.suite): (c, n) for c, n in jobs}
        for fut in as_completed(futs):
            try:
                case, n, status, secs, cost, passed, count, jcost = fut.result()
            except Exception as e:
                c, n = futs[fut]
                print(f"{c} r{n}: runner error: {e!r}", flush=True)
                continue
            total += (cost or 0.0) + jcost
            cost_s = f"${cost:.2f}" if cost is not None else "cost n/a"
            verdict = "PASS" if count and passed == count else "FAIL"
            print(f"{case} r{n}: {status}, {secs}s, {cost_s} + judges ${jcost:.2f}, "
                  f"{passed}/{count} checks, {verdict}", flush=True)
    print(f"ALL DONE. Reported cost: ${total:.2f}", flush=True)


if __name__ == "__main__":
    main()
