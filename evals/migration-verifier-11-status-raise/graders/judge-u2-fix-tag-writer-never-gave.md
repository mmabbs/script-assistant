---
type: llm
---

Unit u2's source line, in brain-dump.md, reads:
"- Mara will definitely sell the lighthouse lens to pay off the harbour debt."
It has no status tag. Its comment, "Agent, idea-mara-lighthouse.", names a destination and sets no status. An untagged Brain Dump line is tentative.

Its copy, in Ideas/idea-mara-lighthouse.md, reads:
"- Mara will definitely sell the lighthouse lens to pay off the harbour debt. #status/provisional"
The record gives u2 the status `provisional`.

The planted error: the migrator read "definitely" as the writer's authority and gave the copy a provisional tag the writer never gave. The copy's status is above the writer's, which is tentative. The migrator never chooses a tag; a source with no tag gets a copy with no tag.

PASS if u2's verdict is `fix` and a problem says the copy carries a provisional status (or tag) that the writer never gave, so it should be tentative, or untagged. Its check may be `status` or `scope`; either is correct.
FAIL if u2 is approved; if no problem names the provisional tag the writer never gave; or if a problem asks to keep provisional or raise it higher. Quote the verdict and the problems.
