---
type: llm
---

The batch is three lines under "### 2026-10-09" in brain-dump.md, each with what the record holds for it:
- A (line 10): "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed", with the comment "Agent, char-mara." Only a `left_in_place` entry. This one is expected in `missed`; this check doesn't grade it.
- B (line 13): "- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed". Unit u1 graduated the settled part to char-mara, and a `left_in_place` entry names the line. The unresolved part, "Not sure what forces her to cross yet", rightly stays at the source: an unresolved detail in a committed bullet is not committed. Not missed.
- C (line 15): "- Tobias always whistled the same three notes when he rowed.", with the comment "Agent, idea-tobias." Unit u2 copied it. Not missed.

PASS if the reply's `missed` list holds no entry other than line A (or its comment, line 11). An empty `missed` list also passes this check.
FAIL if `missed` holds line B or its unresolved part ("what forces her to cross"), or line C. Quote the `missed` list.
