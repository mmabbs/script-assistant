---
type: llm
---

Line A, in brain-dump.md under "### 2026-10-09" (line 10), is untagged:
"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."
The comment below it (line 11): "%% Agent, idea-tobias. %%"

The writer's comment asks for the line to go to idea-tobias. Nothing did: the record has no unit, `left_in_place`, `questions`, or `could_not` entry for the line or its comment, and Ideas/idea-tobias.md holds no line about the ribbon. So the comment asked for something the migrator didn't do, and no question covers it. That is a `missed` line. Only the comment is a batch line, because an untagged bullet is not a trigger line; the line the writer's words asked about is the bullet above it.

PASS if the reply's `missed` list holds an entry whose `source` is the ribbon line: brain-dump.md, line 10, or the ribbon line's text.
FAIL if no `missed` entry names the ribbon line. An entry whose `source` is only the comment (line 11, "%% Agent, idea-tobias. %%") is a FAIL. Quote the `missed` list.
