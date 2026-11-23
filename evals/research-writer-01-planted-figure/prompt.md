---
description: "Case for F2, the note says something the findings don't. A planted repaint figure differs from common knowledge. Runs against the script-asst:research-writer agent."
tags: [research-workflow, research-writer, f2-changed-detail]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Write, Edit]
---

This is the research-writer's step of a research run.

- Run date: 2026-10-08
- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-eiffel-tower-upkeep.md
- The project's copy of the note template: templates/research-template.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-08-1400-research/eiffel-tower-upkeep/topic-1.md
  - project/llm-files/research-findings/run-2026-10-08-1400-research/eiffel-tower-upkeep/topic-2.md

Write the research note in project/Research/. When you finish, reply with the note's path.
