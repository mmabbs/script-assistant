---
description: "Case for a cut-short findings file. topic-2.md has no closing line. The reply must name topic 2 as cut short, and nothing from that file may reach the note. Runs against the script-asst:research-writer agent."
tags: [research-workflow, research-writer, cut-short]
retired: "2026-10-22: the cut-short rule it tests is dropped (spec-research-workflow.md 11 item 105; plan-research-workflow.md 05 item 24). research-run.py skips it. Kept for its past results."
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Write, Edit]
---

This is the research-writer's step of a research run.

- Run date: 2026-10-09
- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-bathing-machines.md
- The project's copy of the note template: templates/research-template.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-09-1400-research/bathing-machines/topic-1.md
  - project/llm-files/research-findings/run-2026-10-09-1400-research/bathing-machines/topic-2.md
  - project/llm-files/research-findings/run-2026-10-09-1400-research/bathing-machines/topic-3.md

Write the research note in project/Research/. When you finish, reply with the note's path and the topic number of any findings file that was cut short.
