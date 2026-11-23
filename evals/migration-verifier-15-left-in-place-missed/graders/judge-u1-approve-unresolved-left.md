---
type: llm
---

Line B, in brain-dump.md (line 13), is one committed bullet with an unresolved detail, and no comment:
"- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed"

Unit u1 graduated only the settled part to char-mara.md, an Area Note, under "## General", as a plain statement:
"- Mara crosses the causeway on foot on the night of the storm."
The record gives u1 the status `committed`. A `left_in_place` entry in the record also names line B.

Nothing was planted here. An unresolved detail in a committed bullet stays at the source: "Not sure what forces her to cross yet" is not committed, so it stays out of the Area Note, and the migrator lists the line in `left_in_place`. It is not turned into a `- [?]` line either.

PASS if u1's verdict is `approve` with no problems.
FAIL if u1's verdict is `fix`, and especially if a problem says the copy lost "not sure what forces her to cross yet", that the unresolved part should have gone to char-mara, or that it should have become a `- [?]` line. Quote the verdict and the problems.
