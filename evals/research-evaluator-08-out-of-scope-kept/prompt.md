---
description: "Case for findings outside the plan's limits (spec decisions 100 and 101). A clean note that includes the answer-changing passage outside the period, labelled and footnoted, and leaves out a passage outside the place limit that only adds detail. The right verdict is PASS, with no problems. Runs against the script-asst:research-evaluator agent."
tags: [research-workflow, research-evaluator, out-of-scope-findings]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read]
---

This is the research-evaluator's step of a research run.

- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-penny-farthings.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-12-1400-research/penny-farthings/topic-1.md
  - project/llm-files/research-findings/run-2026-10-12-1400-research/penny-farthings/topic-2.md
- The note: project/Research/research-penny-farthings.md

Check the note. Answer with JSON only, in this shape: {"verdict": "pass" or "fail", "problems": [{"check": "matches findings" | "coverage" | "nothing dropped", "where": "...", "detail": "..."}]}. On a pass, "problems" is empty.
