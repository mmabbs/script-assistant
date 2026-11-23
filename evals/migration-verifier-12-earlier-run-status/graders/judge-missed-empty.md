---
type: llm
---

The batch is two pieces of brain-dump.md:
- under "### 2026-10-02", one line the writer re-tagged after an earlier run: "- Mara rows out to the wreck buoy every Sunday to leave flowers for Tobias. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]". Unit u1 graduated it to char-mara.
- under "### 2026-10-09": "- Mara has stopped answering letters from the mainland. #status/provisional" with its comment "Agent, idea-mara-habits." (unit u2)

Both have a unit. Nothing was left out. The earlier run's copy of the wreck-buoy line in Ideas/idea-mara-habits.md still carries #status/provisional, below the writer's new committed tag. That is not a missed line: a status that is lower because the writer changed the tag after an earlier run is not this run's business, and the re-tagged line was acted on (u1). The barometer line under "### 2026-10-02" didn't change since the earlier run and isn't in the batch.

PASS if the reply's `missed` list is empty.
FAIL if `missed` holds any entry, in particular one naming the wreck-buoy line or its provisional copy in idea-mara-habits, or the barometer line. Quote the `missed` list.
