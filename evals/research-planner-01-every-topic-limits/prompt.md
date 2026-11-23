---
description: "Case for F4, a misread request or ignored comment. No dependencies; the comment sets a place and a period for every topic. Runs against the script-asst:research-planner agent."
tags: [research-workflow, research-planner, f4-misread-request]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Write]
---

This is the research-planner's step of a research run.

- Run id: run-2026-10-08-1400-research
- Project folder: project/
- Your request, r1:
  - path: project/Concepts/concept-pit-village.md
  - line: 9
  - text: - [r] What did a typical shift look like for a coal miner, and what were the main dangers underground? #research/run-4
  - comment: Wales, the Rhondda valley, 1900 to 1914.

Write this request's plan to project/llm-files/research-plans/research-plan-rhondda-mining-shift.md. Use `rhondda-mining-shift` as the research topic for this case.

Then answer with the schedule as JSON: the research topic, and one entry per topic with its number and the topics it waits on, if any. Also write the same JSON to run/answer.json.
