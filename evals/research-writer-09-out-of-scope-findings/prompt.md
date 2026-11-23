---
description: "Case for findings outside the plan's limits (spec decision 100). The plan limits the request to England, 1905 to 1914. One passage outside the period shows plan question 1 rests on the wrong period, so it must be in the note, footnoted and labelled as outside the scope asked about. One passage outside the place limit only adds detail, so it is neither required nor penalized. Runs against the script-asst:research-writer agent."
tags: [research-workflow, research-writer, out-of-scope-findings]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Write, Edit]
---

This is the research-writer's step of a research run.

- Run date: 2026-10-12
- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-penny-farthings.md
- The project's copy of the note template: templates/research-template.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-12-1400-research/penny-farthings/topic-1.md
  - project/llm-files/research-findings/run-2026-10-12-1400-research/penny-farthings/topic-2.md

Write the research note in project/Research/. When you finish, reply with the note's path.
