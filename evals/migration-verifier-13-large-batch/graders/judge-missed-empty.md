---
type: llm
---

The batch is three date headings in brain-dump.md, with twenty units in the record:
- "### 2026-10-07": seven bullets inside a range comment (u1 to u7) and one just outside it (u8, migrated without being asked, which is a `fix` on u8, not a `missed` entry).
- "### 2026-10-08": six tagged lines, each with a unit (u9 to u14), and three untagged lines with no comment: "- What if the lens is worth more than the lighthouse?", "- Something about the gulls nesting on the gallery.", "- Check how often relief keepers actually rotated." No tag or comment asked for anything on those three, so they are not missed.
- "### 2026-10-09": six lines, each with its own comment and a unit (u15 to u20).

Every line the writer's tags or comments asked about has a unit. Nothing was left out.

PASS if the reply's `missed` list is empty.
FAIL if `missed` holds any entry. Quote the `missed` list.
