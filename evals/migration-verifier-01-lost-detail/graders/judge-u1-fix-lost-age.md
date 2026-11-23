---
type: llm
---

Unit u1 is a split. Its source line, in brain-dump.md, reads:
"- Mara's brother Tobias drowned off the north jetty when she was nine. She still sets a place for him at dinner."

Its two copies read:
- in Ideas/idea-tobias.md: "- Mara's brother Tobias drowned off the north jetty when she was a child."
- in Ideas/idea-mara-habits.md: "- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine."

The planted error: the idea-tobias copy lost Mara's age. The source says "nine"; the copy says "a child." The idea-mara-habits copy is correct.

PASS if u1's verdict is `fix` and one of its problems points at the idea-tobias copy and says the age, "nine," was lost or changed. The check name doesn't matter.
FAIL if u1 is approved, or if no problem names the lost age in the idea-tobias copy. Quote the verdict and the problems.
