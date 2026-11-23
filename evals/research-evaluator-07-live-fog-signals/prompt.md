---
description: "Case for F8, the research-evaluator misses a planted error. Built from the first live run (2026-10-12): the real plan, findings, and the note's first draft, a long note with three real 'matches findings' problems, two of them 'which…' clauses that add a conclusion the findings don't hold. The live research-evaluator reported only one. Every one must be reported in one answer. Runs against the script-asst:research-evaluator agent."
tags: [research-workflow, research-evaluator, f8-evaluator-miss]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read]
---

This is the research-evaluator's step of a research run.

- Project folder: project/
- The plan: project/llm-files/research-plans/research-plan-lighthouse-fog-signals.md
- The findings files, from every researcher that answered found:
  - project/llm-files/research-findings/run-2026-10-12-1649-research/lighthouse-fog-signals/topic-1.md
  - project/llm-files/research-findings/run-2026-10-12-1649-research/lighthouse-fog-signals/topic-2.md
- The note: project/Research/research-lighthouse-fog-signals.md

Check the note. Answer with JSON only, in this shape: {"verdict": "pass" or "fail", "problems": [{"check": "matches findings" | "coverage" | "nothing dropped", "where": "...", "detail": "..."}]}. On a pass, "problems" is empty.
