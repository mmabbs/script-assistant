---
type: llm
---

The writer was handed three findings files. topic-1.md and topic-3.md end with the closing line <!-- end of findings -->. topic-2.md does not: it was cut short.

PASS if the reply names topic 2 as cut short and names no other topic as cut short.
FAIL if the reply does not name topic 2 as cut short, says no file was cut short, or names topic 1 or topic 3 as cut short. Quote the reply's words on it.
