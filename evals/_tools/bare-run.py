# Hand runner used for the 2026-10-01 bare-Claude runs. Launches one isolated claude -p child per case folder
# (c15 to c19 as written; edit the root path, the jobs list, and the prompt before reuse). Not part of claude plugin eval.
# See evals/README.md and the "What was run" section of each results file.
import os, subprocess, json, time, sys
from concurrent.futures import ThreadPoolExecutor
root = os.path.dirname(os.path.abspath(__file__))
PROMPT = ("This folder holds a screenwriting project. The files in rules/ explain how the project's notes work. "
          "Read rules/terminology-script-asst.md first, then rules/corrections.md, which is newer and wins where "
          "they differ. Then do a migration run: read project/brain-dump.md and migrate what the writer's status "
          "tags and comments point at, following the rules. Edit the notes directly. When you finish, reply with a "
          "short run log: what you migrated, where it went, and why.")
env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
def one(job):
    c, r = job
    base = os.path.join(root, c, r)
    cmd = ["claude", "-p", PROMPT, "--model", "claude-opus-5-5", "--no-session-persistence",
           "--setting-sources", "project", "--tools", "Read,Write,Edit,Glob,Grep",
           "--permission-mode", "acceptEdits", "--output-format", "json"]
    t0 = time.time(); proc = None
    try:
        proc = subprocess.Popen(cmd, cwd=os.path.join(base, "work"), env=env,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, err = proc.communicate(timeout=900)
        status = f"exit {proc.returncode}"
    except subprocess.TimeoutExpired:
        out, err, status = "", "timeout", "timeout"
    finally:
        if proc and proc.poll() is None:
            proc.kill(); proc.wait()
    with open(os.path.join(base, "result.json"), "w") as f: f.write(out or "")
    with open(os.path.join(base, "stderr.txt"), "w") as f: f.write(err or "")
    return c, r, status, round(time.time() - t0)
jobs = [(c, r) for c in ("c15", "c16", "c17", "c18", "c19") for r in ("r1", "r2", "r3")]
with ThreadPoolExecutor(max_workers=5) as ex:
    for res in ex.map(one, jobs):
        print(*res, flush=True)
print("ALL DONE")
