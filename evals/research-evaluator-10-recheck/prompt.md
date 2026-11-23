---
description: "Case for spec decision 106, the scoped re-check after the fix round. The research-evaluator gets the first draft (draft-1.md), the fixed note, and the first check's three problems. Plants: (1) a flaw in a sentence that didn't change; (2) a first problem left unfixed; (3) a changed sentence with a new error; (4) a deleted sentence that dropped a plan answer. Pass: plants 2, 3, and 4 are reported in 3 of 3 runs, and plant 1 never is. The body follows research.js recheckPrompt line for line, with this case's paths; the closing answer-shape line is test-only, since the workflow passes a schema instead. Runs against the script-asst:research-evaluator agent."
tags: [research-workflow, research-evaluator, f8-evaluator-miss, re-check]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read]
---

Re-check one research note after its fix round.
Judge only what the fix round changed, found by comparing the note with draft-1.md, plus whether each of the first check's problems below was fixed.

Plan: project/llm-files/research-plans/research-plan-stained-glass-windows.md
Findings files:
- project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-1.md
- project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-2.md
Note: project/Research/research-stained-glass-windows.md
draft-1.md, the note before the fix round: project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/draft-1.md

First check's problems:
1. [matches findings] Where: Disagreement / Uncertainty. What is wrong: The note says the piece count is about 600; topic-2.md says about 800.
2. [matches findings] Where: Making the coloured glass, paragraph 2. What is wrong: The note says the glazier scored the glass with a diamond; topic-1.md says a red-hot iron was drawn along a marked line, and that diamond cutters came into use much later.
3. [matches findings] Where: Building the window, paragraph 2. What is wrong: "a method copied from Byzantine mosaic workshops" is not in the findings; topic-2.md passage 2 says nothing about where the method came from.

Answer with JSON only, in this shape: {"verdict": "pass" or "fail", "problems": [{"check": "matches findings" | "coverage" | "nothing dropped", "where": "...", "detail": "..."}]}. On a pass, "problems" is empty.
