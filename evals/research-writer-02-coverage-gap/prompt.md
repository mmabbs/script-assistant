---
description: "Case for F3, a coverage gap. One plan question has no findings; one answer sits in the other topic's file. Runs against the script-asst:research-writer agent."
tags: [research-workflow, research-writer, f3-coverage-gap]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Write, Edit]
---

This is the research-writer's step of a research run.

- Run date: 2026-10-08
- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-london-gas-lamps.md
- The project's copy of the note template: templates/research-template.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-08-1400-research/london-gas-lamps/topic-1.md
  - project/llm-files/research-findings/run-2026-10-08-1400-research/london-gas-lamps/topic-2.md

Write the research note in project/Research/. When you finish, reply with the note's path.
