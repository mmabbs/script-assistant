---
type: llm
---

The writer's only rejection comment sits in Ideas/idea-mara-lighthouse.md, under the hotel-sale line there:
"%% Agent, the hotel sale is out for Mara's story only. The town can still have it. %%"

Unit u2 rejected a line in a different note, Ideas/idea-harrow-point.md, the town's note:
"- A hotel chain buys the old harbour cottages and the pier."
It is gone from that note's live part, and under "## Rejected" it now reads:
"- A hotel chain buys the old harbour cottages and the pier. #status/rejected"

The planted error: the rejection was read wider than the writer's scope. The writer said "for Mara's story only" and "The town can still have it." The town's hotel line should have stayed live.

PASS if u2's verdict is `fix` and a problem with the check `scope` says the town's hotel line in idea-harrow-point was rejected outside what the writer's comment covered.
FAIL if u2 is approved, or if no `scope` problem names the town line rejected beyond the writer's scope. Quote the verdict and the problems.
