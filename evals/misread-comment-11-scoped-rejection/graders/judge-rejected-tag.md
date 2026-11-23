---
type: llm
focus: { source: file, path: project/Ideas/idea-mara-backstory.md }
---

The writer said: "Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear."

The rule: a rejected unit is tagged `#status/rejected`, then moved to the note's Rejected section.

PASS if the line about Mara being afraid of the sea sits in the Rejected section and carries the tag `#status/rejected`, and no other line in the note carries that tag.
FAIL if that line has no `#status/rejected` tag. Also FAIL if the tag is on any line outside the Rejected section, such as the seasickness line, Tobias's fear, or the town's superstition.
