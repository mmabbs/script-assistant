#!/usr/bin/env python3
"""Build the stop dry-run project (Run manager, "stop a research run").

Usage: python3 build.py DEST

Makes DEST/Lighthouse/: the research project before the run (copied from ../dryrun/source/project/Lighthouse/),
set up with `runmanager init`, plus a .claude/settings.json holding
  1. a PostToolUse hook that swaps .runs/research.js for the cheap stand-in right after `runmanager start`, and
  2. allow rules so the stand-in's two agents can write their notes and run their wait command.
The stand-in and the hook script go in DEST/Lighthouse/.claude/dryrun/.
Refuses if DEST/Lighthouse already exists. Standard library only. Steps for the human: steps.md.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLUGIN = HERE.parents[3]  # tests/dryrun-stop -> tests -> runmanager -> lib -> plugin root
SOURCE = HERE.parent / "dryrun" / "source" / "project" / "Lighthouse"
RUNMANAGER = PLUGIN / "bin" / "runmanager"
WAIT_COMMAND = "sleep 180"


def main(argv):
    if len(argv) != 2:
        print("usage: python3 build.py DEST", file=sys.stderr)
        return 2
    dest = Path(argv[1]).expanduser().resolve()
    project = dest / "Lighthouse"
    if project.exists():
        print(f"refused: {project} already exists", file=sys.stderr)
        return 1
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, project)

    init = subprocess.run([str(RUNMANAGER), "init", "--project", str(project)], capture_output=True, text=True)
    if init.returncode != 0:
        print(f"init failed: {init.stdout}{init.stderr}", file=sys.stderr)
        return 1

    dryrun = project / ".claude" / "dryrun"
    dryrun.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "stand-in.js", dryrun / "stand-in.js")
    shutil.copyfile(HERE / "swap-standin.py", dryrun / "swap-standin.py")

    # An absolute path in a rule starts with //. Agent 2 waits with a background `sleep 180`: a foreground
    # sleep is blocked for agents, and a background one under a Bash(sleep N) rule was tested 2026-10-26.
    settings_path = project / ".claude" / "settings.json"
    settings = json.loads(settings_path.read_text()) if settings_path.exists() else {}
    allow = settings.setdefault("permissions", {}).setdefault("allow", [])
    allow += [
        f"Edit(/{project}/Research/**)",
        f"Bash({WAIT_COMMAND})",
    ]
    settings.setdefault("hooks", {}).setdefault("PostToolUse", []).append({
        "matcher": "Bash",
        "hooks": [{
            "type": "command",
            "command": f'python3 "{dryrun / "swap-standin.py"}"',
            "timeout": 10,
        }],
    })
    settings_path.write_text(json.dumps(settings, indent=2) + "\n")

    print(f"built {project}")
    print(f"settings {settings_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
