#!/usr/bin/env python3
"""PostToolUse hook for the stop dry run (tests/dryrun-stop/).

Reads the hook's JSON on stdin. When the Bash call was a `runmanager start` with `--kind research`,
copies stand-in.js (beside this file) over $CLAUDE_PROJECT_DIR/.runs/research.js. Prints nothing and
always exits 0, so it never blocks a call. Any other call is left alone. Standard library only.
"""
import json
import os
import re
import shutil
import sys

START = re.compile(r"(^|[\s/])runmanager\s+start(\s|$)")
KIND = re.compile(r"--kind(\s+|=)research(\s|$)")


def main():
    try:
        event = json.load(sys.stdin)
        command = (event.get("tool_input") or {}).get("command") or ""
        if event.get("tool_name", "Bash") != "Bash":
            return
        if not (START.search(command) and KIND.search(command)):
            return
        project = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or ""
        target = os.path.join(project, ".runs", "research.js")
        if not project or not os.path.isfile(target):
            return
        shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stand-in.js"), target)
    except Exception:
        return


if __name__ == "__main__":
    main()
    sys.exit(0)
