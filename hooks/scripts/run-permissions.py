#!/usr/bin/env python3
"""PreToolUse hook: approve a run's own work so a run asks the writer nothing (spec-run-manager.md 02 item 7;
11 item 84).

It approves:
  1. the migrator's Edit and Write calls on a .md note outside the project's dot-folders, or a .json file
     in .runs/units/, inside the folder the session was opened in;
  2. Read calls by any script-asst: agent inside the plugin's folder or the project;
  3. a Bash command that is one runmanager or editguard call and nothing else;
  4. the main session's Write of a file the run skill tells it to save, inside a run's folder:
     .runs/run-*/findings-b{N}-r{K}.json, findings-flags.json, or outcomes.json;
  5. a research agent's Edit and Write calls in its own folder inside the project: the research-planner's .md
     plans in llm-files/research-plans/, a researcher's findings files in llm-files/research-findings/, and the
     research-writer's .md notes in Research/, and the research-writer's draft-1.md copy anywhere in
     llm-files/research-findings/ (spec-run-manager.md 11 items 89 and 91);
  6. the researcher's WebSearch and WebFetch calls, which a workflow agent can't ask the writer about
     (spec-run-manager.md 11 item 92).
For every other call it prints nothing, so Claude Code asks as usual. A deny rule still wins over it.
Standard library only. Never fails a call: any error means no answer.
"""
import json
import os
import re
import sys

PLUGIN = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
MIGRATOR = "script-asst:migrator"
RESEARCHER = "script-asst:researcher"
AGENT_PREFIX = "script-asst:"
COMMAND = re.compile(r"(runmanager|editguard)(\s|$)")
FORBIDDEN = set(";&|<>`$\n\r")
SAVED = re.compile(r"(findings-b\d+-r\d+|findings-flags|outcomes)\.json")
RUN_FOLDER = re.compile(r"run-[\w-]+")
# Each research agent's folder, and whether its files must be .md notes.
RESEARCH = {"script-asst:research-planner": (("llm-files", "research-plans"), True),
            "script-asst:researcher": (("llm-files", "research-findings"), False),
            "script-asst:research-writer": (("Research",), True)}
# The one file the research-writer may also write in the researcher's folder: its first-draft copy on a fix round.
DRAFT_COPY = ("script-asst:research-writer", ("llm-files", "research-findings"), "draft-1.md")


def inside(path, root):
    """True when path, after resolving links, is root or sits under it."""
    return path == root or path.startswith(root + os.sep)


def resolve(path, cwd):
    return os.path.realpath(path if os.path.isabs(path) else os.path.join(cwd, path))


def migrator_may_write(path, project):
    if not inside(path, project) or path == project:
        return False
    parts = os.path.relpath(path, project).split(os.sep)
    if parts[:2] == [".runs", "units"] and len(parts) == 3 and parts[2].endswith(".json"):
        return True
    return path.endswith(".md") and not any(p.startswith(".") for p in parts)


def session_may_save(path, project):
    if not inside(path, project):
        return False
    parts = os.path.relpath(path, project).split(os.sep)
    return (len(parts) == 3 and parts[0] == ".runs" and bool(RUN_FOLDER.fullmatch(parts[1]))
            and bool(SAVED.fullmatch(parts[2])))


def research_may_write(agent, path, project):
    if agent not in RESEARCH or not inside(path, project):
        return False
    folder, notes_only = RESEARCH[agent]
    parts = os.path.relpath(path, project).split(os.sep)
    who, where, name = DRAFT_COPY
    if (agent == who and len(parts) > len(where) and tuple(parts[:len(where)]) == where and parts[-1] == name
            and not any(p.startswith(".") for p in parts)):
        return True
    return (len(parts) > len(folder) and tuple(parts[:len(folder)]) == folder
            and not any(p.startswith(".") for p in parts) and (path.endswith(".md") or not notes_only))


def decide(d):
    """The reason to approve the call, or None to leave it to Claude Code."""
    tool, agent = d.get("tool_name"), str(d.get("agent_type") or "")
    inp = d.get("tool_input") or {}
    cwd = d.get("cwd") or os.getcwd()
    if tool == "Bash":
        cmd = str(inp.get("command", "")).strip()
        if COMMAND.match(cmd) and not FORBIDDEN & set(cmd):
            return "a script-asst run command"
        return None
    if tool in ("WebSearch", "WebFetch"):
        return "the researcher's web call" if agent == RESEARCHER else None
    path = inp.get("file_path")
    if not isinstance(path, str) or not path:
        return None
    path, project = resolve(path, cwd), os.path.realpath(cwd)
    if tool in ("Edit", "Write") and agent == MIGRATOR and migrator_may_write(path, project):
        return "the migrator's write inside the project"
    if tool in ("Edit", "Write") and research_may_write(agent, path, project):
        return "a research agent's write in its own folder"
    if tool == "Write" and not agent and session_may_save(path, project):
        return "a file the run skill saves"
    if tool == "Read" and agent.startswith(AGENT_PREFIX) and (inside(path, PLUGIN) or inside(path, project)):
        return "a script-asst agent's read"
    return None


def main():
    try:
        reason = decide(json.load(sys.stdin))
    except Exception:
        return 0
    if reason:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow",
                                                 "permissionDecisionReason": f"script-asst: {reason}"}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
