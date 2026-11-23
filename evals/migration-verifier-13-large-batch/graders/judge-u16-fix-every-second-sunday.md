---
type: llm
---

Unit u16's source line, in brain-dump.md under "### 2026-10-09", reads:
"- Mara rows out to the seal rocks every second Sunday, the way Tobias did."
Its comment: "Agent, idea-mara-habits."

Its copy, in Ideas/idea-mara-habits.md (line 10), reads:
"- Mara rows out to the seal rocks every Sunday, the way Tobias did."

The planted error: "every second Sunday" became "every Sunday." The copy doubles how often Mara goes. The rest of the line is the same, which makes the change easy to read past.

PASS if u16's verdict is `fix` and a problem says "second" was lost, or that the frequency changed from every second Sunday to every Sunday. The check name doesn't matter.
FAIL if u16 is approved, or if no problem names the lost "second" or the changed frequency. Quote the verdict and the problems.
