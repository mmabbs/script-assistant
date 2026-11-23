---
type: llm
---

The batch is the two lines under "### 2026-10-09" in brain-dump.md, each with a comment under it naming idea-mara-lighthouse:
- "- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional" (unit u1)
- "- Mara will definitely sell the lighthouse lens to pay off the harbour debt." (unit u2)

Both have a unit in the record. Nothing was left out. u1's line is provisional by the writer's tag, so nothing asked for it to graduate to an Area Note; a reply that lists it in `missed` as "should have gone to char-mara" or "should be committed" is wrong. A unit with a status error is a `fix`, not a `missed` entry.

PASS if the reply's `missed` list is empty.
FAIL if `missed` holds any entry. Quote the `missed` list.
