---
type: llm
---

The batch is the three lines under "### 2026-10-09" in brain-dump.md, each with a comment under it:
- "- Mara learned to read the weather from her father's barometer notes. #status/provisional" (unit u1)
- "- Mara has never once left Harrow Point overnight. #status/committed" (unit u2)
- "- Mara keeps the light by hand when the power fails, winding the old clockwork. #status/committed" (unit u3)

Every line has a unit in the record. None was left out. A unit with a status error is a `fix`, not a `missed` entry.

PASS if the reply's `missed` list is empty.
FAIL if `missed` holds any entry. Quote the `missed` list.
