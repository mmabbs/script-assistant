---
type: llm
---

Unit u2's source line, in brain-dump.md under "### 2026-10-09", reads:
"- Mara has stopped answering letters from the mainland. #status/provisional"
Its comment: "Agent, idea-mara-habits."

Its copy, written in this run, sits in Ideas/idea-mara-habits.md (line 11):
"- Mara has stopped answering letters from the mainland."
The record gives u2 the status `tentative`.

The planted error: the writer tagged the line provisional, and the copy written in this run dropped the tag, so it sits at tentative, below the writer's own tag. A copy written in this run at a lower status than the writer's own tag is a `status` fix: the migrator puts the writer's status back.

PASS if u2's verdict is `fix` and a problem says the copy lost the writer's provisional status or tag (it reads as tentative, or untagged, where the writer said provisional). Its check may be `status` or `lost-detail`; either is correct.
FAIL if u2 is approved, or if no problem names the missing provisional status on this copy. Quote the verdict and the problems.
