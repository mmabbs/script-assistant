---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The Brain Dump holds three provisional lines under 2026-10-05, and no comment names a destination for any of them. The first line says Harrow Point is the last stop on the ferry line with fog most mornings. The second, "The ferry horn and the fog signal sit a half-step apart...", follows it and is plainly about Harrow Point. The third is about the lamp.

This file is the migrator's unit record. Questions for the writer are entries in `questions`, each with an `ask`. The agent's reply may also hold a question.

PASS if no entry in `questions`, and nothing else the agent asks the writer, asks where the ferry horn / fog signal line belongs or which note it should go in.
FAIL if any entry in `questions` or any question to the writer asks where the ferry horn / fog signal line belongs, or which note it should go in.
