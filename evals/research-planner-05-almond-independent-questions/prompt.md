---
description: "Case for spec decision 103, one topic per independent question. The Almond request of 2026-10-18, word for word, with no comment. In that run the research-planner put five questions into one topic, and its one researcher opened no pages. Pass: no topic holds more than two of the first run's five questions. A topic's own \"how strong is the evidence?\" for its own question counts as narrowing that question, not as question 5. No topic waits on another, except that the topic for question 5 (is \"contagious\" an accurate word, and where is the evidence strong or weak) may wait on the topic for the studies (question 3). Any other wait fails. Approved by the writer 2026-10-22, loosened twice. Runs against the script-asst:research-planner agent."
tags: [research-workflow, research-planner, f4-misread-request, independent-questions]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Write]
---

This is the research-planner's step of a research run.

- Run id: run-2026-10-18-1807-research
- Project folder: project/
- Your request, r1:
  - path: project/brain-dump.md
  - line: 14
  - text: - [r] Is anxiety "contagious"? #research/run-1
  - comment: none
- Research topics already taken in this run: none

Write this request's plan to project/llm-files/research-plans/research-plan-anxiety-contagion.md. Use `anxiety-contagion` as the research topic for this case.

Then answer with the schedule as JSON: the research topic, and one entry per topic with its number and the topics it waits on, if any. Also write the same JSON to run/answer.json.
