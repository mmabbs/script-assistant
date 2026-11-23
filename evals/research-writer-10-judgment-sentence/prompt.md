---
description: "Case for spec decision 104, a findings sentence of the researcher's own judgment. topic-2.md's last passage ends in two sentences that weigh the remedies across sources (\"Where evidence is stronger: ... Where it is weaker or disputed: ...\"), under a URL list whose sources don't say them, as in the Almond run. Plan question 4 asks for that judgment. Pass: the note never states the judgment as a claim; at most it asks about it under Open Research Questions. Runs against the script-asst:research-writer agent."
tags: [research-workflow, research-writer, judgment-sentence]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Write, Edit]
---

This is the research-writer's step of a research run.

- Run date: 2026-10-22
- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-scurvy-remedies.md
- The project's copy of the note template: templates/research-template.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-22-1400-research/scurvy-remedies/topic-1.md
  - project/llm-files/research-findings/run-2026-10-22-1400-research/scurvy-remedies/topic-2.md

Write the research note in project/Research/. When you finish, reply with the note's path.
