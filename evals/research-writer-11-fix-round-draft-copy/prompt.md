---
description: "Case for spec decision 106, the fix round's first-draft copy. The research-writer is handed the stained-glass note with three problems the research-evaluator reported, and a draft-1.md path in the request's findings folder. Pass: draft-1.md matches the note as handed, and the note carries the fixes. The body follows research.js fixPrompt line for line, with this case's paths; the closing reply line is test-only. Runs against the script-asst:research-writer agent."
tags: [research-workflow, research-writer, fix-round, draft-copy]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Write, Edit]
---

Fix round. The research-evaluator failed the note.
Before you change anything, copy the note unchanged to the draft-1.md path below. Then fix each problem below in the note, in place.

Note: project/Research/research-stained-glass-windows.md
Copy the note to: project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/draft-1.md
Run date: 2026-10-08
Project folder: project/
Plan: project/llm-files/research-plans/research-plan-stained-glass-windows.md
Template copy: templates/research-template.md
Findings files:
- project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-1.md
- project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-2.md

Problems:
1. [matches findings] Where: Disagreement / Uncertainty. What is wrong: The note says the piece count is about 600; topic-2.md says about 800.
2. [matches findings] Where: Building the window, paragraph 3. What is wrong: "which let the builders make the window openings far larger than before" is not in the findings; topic-2.md says only that the armatures carried the weight of the leaded panels.
3. [coverage] Where: Making the coloured glass. What is wrong: Plan question 2, "How were the pieces cut to shape?", is neither answered nor listed under Open Research Questions; topic-1.md passage 2 answers it.

When you finish, reply with the note's path.
