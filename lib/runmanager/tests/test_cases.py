"""The case runner (CONTRACT.md section 2). One pytest test per folder in tests/cases/.

A case copies `before/{Project}` to a temp folder of the same name, runs `steps.json` in order, then
compares the result with `expected/tree/{Project}` and, if present, `expected/log.json`.
`run_case` is public so the skeleton tests can run it on the self-test cases."""
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
RUNMANAGER = ROOT / "bin" / "runmanager"
EDITGUARD = ROOT / "bin" / "editguard"
CASES = Path(__file__).parent / "cases"
IGNORED = {".DS_Store"}
EXIT_WORDS = "Nothing needs you."


def case_names():
    if not CASES.is_dir():
        return []
    return sorted(p.name for p in CASES.iterdir() if p.is_dir() and not p.name.startswith("."))


@pytest.mark.parametrize(
    "name", case_names() or [pytest.param(None, marks=pytest.mark.skip(reason="tests/cases/ is empty"))])
def test_case(name, tmp_path):
    run_case(CASES / name, tmp_path)


# ---------------------------------------------------------------- running the steps

class Case:
    def __init__(self, case_dir, workdir):
        self.dir = Path(case_dir)
        before = self.dir / "before"
        tops = [p for p in before.iterdir() if p.is_dir()]
        if len(tops) != 1:
            raise AssertionError(f"{before} must hold exactly one project folder, found {len(tops)}")
        self.name = tops[0].name
        self.project = Path(workdir) / self.name
        shutil.copytree(tops[0], self.project)
        self.now = None
        self.last_run_id = None  # the id the last `start` printed

    def open_run(self):
        with open(self.project / ".runs" / "run-state.json", encoding="utf-8") as f:
            return json.load(f)["open_run"]

    def run_id(self):
        """The id the last `start` printed, else the open run's id (for cases that begin mid-run)."""
        if self.last_run_id:
            return self.last_run_id
        run = self.open_run()
        if not run:
            raise AssertionError("a step names {run_id}, but no start ran and no run is open")
        return run["id"]

    def env(self):
        env = dict(os.environ)
        env.pop("RUNMANAGER_NOW", None)
        if self.now:
            env["RUNMANAGER_NOW"] = self.now
        return env

    def execute(self, command, step):
        done = subprocess.run([str(c) for c in command], capture_output=True, text=True,
                              env=self.env(), timeout=120)
        want = step.get("exit", 0)
        if done.returncode != want:
            raise AssertionError(f"step {step}: exit {done.returncode}, wanted {want}\n"
                                 f"stdout: {done.stdout}\nstderr: {done.stderr}")
        if "stderr" in step and step["stderr"] not in done.stderr:
            raise AssertionError(f"step {step}: stderr should contain {step['stderr']!r}, got {done.stderr!r}")
        wanted = step.get("stdout", [])
        for needle in [wanted] if isinstance(wanted, str) else wanted:
            if needle not in done.stdout:
                raise AssertionError(f"step {step}: stdout should contain {needle!r}, got {done.stdout!r}")
        return done

    def sub_id(self, text):
        return text.replace("{run_id}", self.run_id()) if "{run_id}" in text else text


def second_pass_args(run, folder):
    """A migration run's second Edit guard check gets the judged flags file and the flag findings, when
    both exist (spec-edit-guard.md 02 item 6; CONTRACT.md 5.5 item 1)."""
    first = run.get("first_check")
    findings = folder / "findings-flags.json"
    if first is None or run["next_check"] == first or not findings.is_file():
        return []
    return ["--judged", folder / f"flags-{first}.json", "--findings", findings]


def run_step(case, step):
    if "now" in step:
        case.now = step["now"]
    if "run" in step:
        sub, *rest = step["run"]
        done = case.execute([RUNMANAGER, sub, "--project", case.project, *rest], step)
        if sub == "start":
            found = re.search(r"^run_id: (.+)$", done.stdout, re.M)
            if found:
                case.last_run_id = found.group(1).strip()
    elif "copy" in step:
        src = case.dir / step["copy"]
        dst = case.project / case.sub_id(step["to"])
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        elif src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        else:
            raise AssertionError(f"step {step}: {src} does not exist")
    elif "delete" in step:
        target = case.project / step["delete"]
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()
    elif step.get("editguard"):
        run = case.open_run()
        if not run or run.get("next_check") is None:
            raise AssertionError(f"step {step}: the open run has no next_check to name the flags file")
        folder = case.project / ".runs" / run["id"]
        out = folder / f"flags-{run['next_check']}.json"
        if run["kind"] == "migration":
            records = sorted((case.project / ".runs" / "units").glob(f"{run['id']}-b*.json"))
            case.execute([EDITGUARD, "check", "--kind", "migration", "--project", case.project,
                          "--snapshot", folder / "snapshot", "--records", *records,
                          "--run-state", case.project / ".runs" / "run-state.json", "--run-id", run["id"],
                          "--fingerprints", folder / "fingerprints.json", "--out", out,
                          *second_pass_args(run, folder)], step)
        else:
            case.execute([EDITGUARD, "check", "--kind", "research", "--project", case.project,
                          "--snapshot", folder / "snapshot", "--requests", folder / "requests.json",
                          "--outcomes", folder / "outcomes.json", "--fingerprints", folder / "fingerprints.json",
                          "--out", out], step)
    elif "chmod" in step:
        os.chmod(case.project / step["chmod"], int(step["mode"], 8))
    elif "flags" in step:
        run = case.open_run()
        if not run or run.get("next_check") is None:
            raise AssertionError(f"step {step}: the open run has no next_check to name the flags file")
        dst = case.project / ".runs" / run["id"] / f"flags-{run['next_check']}.json"
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(case.dir / step["flags"], dst)
    else:
        raise AssertionError(f"unknown step: {step}")


# ---------------------------------------------------------------- comparing

def files_under(root, skip_top=()):
    """Map each file's path (relative, with /) to its Path. Skips junk files and the named top-level names."""
    found = {}
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root)
        if rel_dir == Path("."):
            dirnames[:] = [d for d in dirnames if d not in skip_top]
            filenames = [f for f in filenames if f not in skip_top]
        for f in filenames:
            if f not in IGNORED:
                found[(rel_dir / f).as_posix()] = Path(dirpath) / f
    return found


def compare_trees(want_root, got_root, label, skip_top=()):
    problems = []
    want, got = files_under(want_root, skip_top), files_under(got_root, skip_top)
    for rel in sorted(want.keys() - got.keys()):
        problems.append(f"{label}: missing file {rel}")
    for rel in sorted(got.keys() - want.keys()):
        problems.append(f"{label}: extra file {rel}")
    for rel in sorted(want.keys() & got.keys()):
        if want[rel].read_bytes() != got[rel].read_bytes():
            problems.append(f"{label}: {rel} differs from the expected file")
    return problems


def compare_json(want_path, got_path, label):
    if not got_path.is_file():
        return [f"{label}: missing"]
    with open(want_path, encoding="utf-8") as f:
        want = json.load(f)
    try:
        with open(got_path, encoding="utf-8") as f:
            got = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        return [f"{label}: does not parse: {e}"]
    if want != got:
        return [f"{label}: differs\n  want: {json.dumps(want, sort_keys=True)}\n  got:  {json.dumps(got, sort_keys=True)}"]
    return []


def compare_project(case, want_project):
    problems = compare_trees(want_project, case.project, "tree", skip_top=(".runs", "Runs"))
    want_runs = want_project / ".runs"
    if not want_runs.is_dir():
        return problems
    state = want_runs / "run-state.json"
    if state.is_file():
        problems += compare_json(state, case.project / ".runs" / "run-state.json", ".runs/run-state.json")
    for folder in sorted(p for p in want_runs.iterdir() if p.is_dir()):
        got = case.project / ".runs" / folder.name
        label = f".runs/{folder.name}"
        if (folder / "NO-SNAPSHOT").exists():
            if (got / "snapshot").exists():
                problems.append(f"{label}: snapshot/ should be gone")
        elif (folder / "snapshot").is_dir():
            if not (got / "snapshot").is_dir():
                problems.append(f"{label}: snapshot/ is missing")
            else:
                problems += compare_trees(folder / "snapshot", got / "snapshot", f"{label}/snapshot")
        names = ["requests.json", "fingerprints.json", "batches.json", "undo-misses.json", "pointer-misses.json", "findings-flags.json", "restore-misses.json"]
        names += sorted(f.name for f in folder.glob("verify-*.json"))
        names += sorted(f.name for f in folder.glob("flags-*.json"))
        for name in names:
            if (folder / name).is_file():
                problems += compare_json(folder / name, got / name, f"{label}/{name}")
        if (folder / "removed").is_dir():
            problems += compare_trees(folder / "removed", got / "removed", f"{label}/removed")
    want_units = want_project / ".runs" / "units"
    if want_units.is_dir():
        for f in sorted(want_units.glob("*.json")):
            problems += compare_json(f, case.project / ".runs" / "units" / f.name, f".runs/units/{f.name}")
    return problems


# ---------------------------------------------------------------- log.json

def split_frontmatter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[1:i], lines[i + 1:]
    return None, lines


def first_type(frontmatter):
    """The first item of the frontmatter's `type` list (inline or block form)."""
    for i, line in enumerate(frontmatter):
        found = re.match(r"type:\s*(.*)$", line)
        if not found:
            continue
        rest = found.group(1).strip()
        if not rest:
            for nxt in frontmatter[i + 1:]:
                if nxt.strip():
                    rest = nxt.strip().lstrip("-").strip()
                    break
        rest = rest.lstrip("[").rstrip("]").split(",")[0].strip()
        return rest.strip("'\"")
    return None


def check_log(case, spec):
    label = spec["file"]
    path = case.project / label
    if not path.is_file():
        return [f"{label}: the run log is missing"]
    problems = []
    frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if frontmatter is None:
        return [f"{label}: no frontmatter"]
    if first_type(frontmatter) != "run-log":
        problems.append(f"{label}: frontmatter `type` must list run-log first, found {first_type(frontmatter)!r}")
    nonblank = [i for i, line in enumerate(body) if line.strip()]
    first = body[nonblank[0]].rstrip() if nonblank else None
    if "first_line" in spec and first != spec["first_line"]:
        problems.append(f"{label}: first line is {first!r}, wanted {spec['first_line']!r}")
    second = body[nonblank[1]].rstrip() if len(nonblank) > 1 else None
    if "second_line" in spec and second != spec["second_line"]:
        problems.append(f"{label}: second line is {second!r}, wanted {spec['second_line']!r}")
    headings = [(i, m.group(1).strip()) for i, line in enumerate(body) if (m := re.match(r"## (.+)$", line))]
    titles = [t for _, t in headings]
    at = 0
    for sec in spec.get("sections", []):
        pos = next((k for k in range(at, len(headings)) if headings[k][1] == sec["heading"]), None)
        if pos is None:
            where = "out of order" if sec["heading"] in titles else "missing"
            problems.append(f"{label}: section '{sec['heading']}' is {where}")
            continue
        at = pos + 1
        start = headings[pos][0] + 1
        end = next((i for i in range(start, len(body)) if re.match(r"#{1,2} ", body[i])), len(body))
        text = "\n".join(body[start:end])
        for needle in sec.get("contains", []):
            if needle not in text:
                problems.append(f"{label}: section '{sec['heading']}' lacks {needle!r}")
        if sec.get("ordered"):
            at_char = 0
            for needle in sec.get("contains", []):
                found = text.find(needle, at_char)
                if found < 0:
                    problems.append(f"{label}: section '{sec['heading']}' lacks {needle!r} after the strings before it")
                    break
                at_char = found + len(needle)
        for needle in sec.get("lacks", []):
            if needle in text:
                problems.append(f"{label}: section '{sec['heading']}' should not hold {needle!r}")
    for title in spec.get("absent", []):
        if title in titles:
            problems.append(f"{label}: section '{title}' should not appear")
    whole = "\n".join(body)
    for needle in spec.get("contains", []):
        if needle not in whole:
            problems.append(f"{label}: lacks {needle!r}")
    if "nothing_needs_you" in spec:
        after = next((body[i].rstrip() for i in nonblank[1:2]), None)
        said = after == EXIT_WORDS
        if said != spec["nothing_needs_you"]:
            problems.append(f"{label}: 'Nothing needs you.' should "
                            f"{'' if spec['nothing_needs_you'] else 'not '}follow the first line")
    return problems


# ---------------------------------------------------------------- one case

def restore_permissions(project):
    """Undo every `chmod` step, so pytest can delete the temp folder: owner read/write on every file,
    and read/write/search on every folder."""
    if not project.exists():
        return
    os.chmod(project, os.stat(project).st_mode | 0o700)
    for dirpath, dirnames, filenames in os.walk(project):
        for d in dirnames:
            p = os.path.join(dirpath, d)
            os.chmod(p, os.stat(p).st_mode | 0o700)
        for f in filenames:
            p = os.path.join(dirpath, f)
            if not os.path.islink(p):
                os.chmod(p, os.stat(p).st_mode | 0o600)


def run_case(case_dir, workdir):
    """Run one case folder in `workdir`. Raises AssertionError listing every difference."""
    case = Case(case_dir, workdir)
    with open(case.dir / "steps.json", encoding="utf-8") as f:
        steps = json.load(f)
    try:
        for step in steps:
            run_step(case, step)
        expected = case.dir / "expected"
        problems = compare_project(case, expected / "tree" / case.name)
        log_file = expected / "log.json"
        if log_file.is_file():
            with open(log_file, encoding="utf-8") as f:
                specs = json.load(f)
            for spec in specs if isinstance(specs, list) else [specs]:
                problems += check_log(case, spec)
    finally:
        restore_permissions(case.project)
    if problems:
        raise AssertionError(f"{case.dir.name}: {len(problems)} problem(s)\n" + "\n".join(problems))
