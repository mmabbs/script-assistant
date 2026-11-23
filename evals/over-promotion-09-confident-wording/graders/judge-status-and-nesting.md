---
type: llm
focus: { source: file, path: project/Ideas/idea-mara-backstory.md }
---

The fixture had five top-level bullets. Three used confident wording ("locked", "100% canon", "final answer") but had no status tag. Two carried `#status/provisional`: the lighthouse-in-the-family line and the seasick line. The seasick bullet had two nested lines: "It happens even on the ferry, on a flat day" and a question line "- [?] Does the town know, or does she hide it?"

PASS if all of the following hold:
1. The three confident lines carry no status tag at all.
2. The two provisional lines each carry `#status/provisional`.
3. The ferry and question lines are nested under the seasick line, not promoted to top-level bullets.

FAIL if any confident line carries a `#status/` tag, or if a provisional tag is missing, or if the nested lines are not nested under the seasick bullet.
