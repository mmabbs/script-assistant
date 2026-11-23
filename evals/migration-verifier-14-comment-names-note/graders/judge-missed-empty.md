---
type: llm
---

The batch is the three lines under "### 2026-10-09" in brain-dump.md, each with a comment under it:
- "- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin, and it's the only shop in the village Mara will set foot in." with "Agent, the chandlery goes in idea-harrow-point, the only-shop habit in idea-mara-habits." (unit u1)
- "- Mara sweeps the lamp room every morning before she eats." with "Agent, migrate this." (unit u2)
- "- Tobias was afraid of the dark until he was ten." with "Agent, put this with the rest of Tobias's material." (unit u3)

Every line has a unit. Nothing was left out. The chandlery half going to the wrong note is a `fix` on u1, not a `missed` entry, even though nothing landed in idea-harrow-point.

PASS if the reply's `missed` list is empty.
FAIL if `missed` holds any entry. Quote the `missed` list.
