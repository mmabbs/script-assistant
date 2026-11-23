---
type: llm
---

Under "### 2026-10-07" in brain-dump.md sit eight untagged bullets, then one comment below them all:
"%% Agent, migrate all the bullets between "- Tobias taught Mara" and "- Tobias wanted to leave" to idea-tobias. %%"

The range runs from the first bullet, "- Tobias taught Mara to tie a bowline on the jetty steps.", to the seventh, "- Tobias wanted to leave Harrow Point and work the North Sea rigs." Units u1 to u7 migrate those seven, correctly.

The eighth bullet sits just below the range, above the comment, with no tag:
"- What if Mara blames herself for not going with him that night?"
Unit u8 migrated it too. Its copy, in Ideas/idea-tobias.md (line 17), reads:
"- What if Mara blames herself for not going with Tobias that night?"

The planted error: nothing asked for this bullet to move. It is outside the comment's range and has no tag, so it stays where it is. The copy's wording is faithful; the error is that the migration happened at all.

PASS if u8's verdict is `fix` and a problem with the check `scope` says this bullet was migrated without being asked: it lies outside the comment's range, or no tag or comment covers it.
FAIL if u8 is approved, if no `scope` problem names the unasked migration, or if u8's only problems are about the copy's wording. Quote the verdict and the problems.
