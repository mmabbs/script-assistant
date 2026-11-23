---
description: "Case for F8, the research-evaluator misses a planted error. Three errors in one note, each in a different section: a changed piece count under Disagreement / Uncertainty, a which-clause adding an unsupported conclusion to a footnoted sentence in Building the window, and the answer to plan question 2 (how the pieces were cut) dropped and not listed as open. Every one must be reported in one answer. Runs against the script-asst:research-evaluator agent."
tags: [research-workflow, research-evaluator, f8-evaluator-miss]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read]
---

This is the research-evaluator's step of a research run.

- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-stained-glass-windows.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-1.md
  - project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-2.md
- The note: project/Research/research-stained-glass-windows.md

Check the note. Answer with JSON only, in this shape: {"verdict": "pass" or "fail", "problems": [{"check": "matches findings" | "coverage" | "nothing dropped", "where": "...", "detail": "..."}]}. On a pass, "problems" is empty.
