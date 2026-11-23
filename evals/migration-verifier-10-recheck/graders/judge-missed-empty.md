---
type: llm
---

This is a re-check, round 1. A re-check never lists missed lines: `missed` is empty on a re-check. The batch's two lines under "### 2026-10-09" in brain-dump.md both have units anyway:
- "- Maybe Tobias rowed out that night to meet someone. Mara found his oars still in the shed the next morning." (unit u1)
- "- Tobias carved his initials into the gallery rail the summer he turned twelve." (unit u2, approved in round 0)

PASS if the reply's `missed` list is empty.
FAIL if `missed` holds any entry, or the reply has no `missed` list. Quote the `missed` list.
