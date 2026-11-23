---
type: llm
---

Unit u1's source line, in brain-dump.md, reads:
"- Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. Mara has never forgiven her. #status/committed"
Its comment: "Agent, char-mara."

Its copy sits in char-mara.md, an Area Note, under "## General":
"- Mara has never forgiven her mother for what happened that winter."

The planted error: the copy reads only with the source beside it. "What happened that winter" doesn't say what happened: the mother sold the family's fishing licence to the cannery, the winter Tobias died. Every Area Note line must read correctly with no other note beside it.

PASS if u1's verdict is `fix` and a problem says the char-mara line doesn't say what happened (the licence sale, the cannery, or the winter Tobias died), so it can't stand on its own. Its check may be `standalone` or `lost-detail`; either is correct.
FAIL if u1 is approved, or if no problem names the missing event behind "what happened that winter." Quote the verdict and the problems.
