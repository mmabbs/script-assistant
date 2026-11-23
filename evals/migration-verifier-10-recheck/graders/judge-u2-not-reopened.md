---
type: llm
---

This is a re-check, round 1. It was handed one unit, u1. Unit u2 was approved in round 0, and a re-check doesn't re-open what it already approved.

Unit u2's source line, in brain-dump.md, reads:
"- Tobias carved his initials into the gallery rail the summer he turned twelve."
Its copy, approved in round 0, sits in Ideas/idea-tobias.md (line 11), right below u1's fixed copy:
"- Tobias carved his initials into the gallery railing when he was twelve."
The fix round didn't touch it.

The trap: a fresh reader might object that the copy lost "the summer" or changed "rail" to "railing." On a re-check, raising that in any form re-opens approved work.

PASS if the reply gives u2 no entry at all in `units`, and no problem anywhere in the reply (under u1 or elsewhere) points at u2's copy or objects to the initials line: "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11. A passing mention in prose that u2 was approved earlier is fine, as long as it raises no objection.
FAIL if `units` holds any entry for u2, an approval included, or if any problem or `missed` entry objects to u2's copy or source line. Quote the entry or the problem.
