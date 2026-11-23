---
type: llm
---

Unit u1's source line, in brain-dump.md, reads:
"- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin, and it's the only shop in the village Mara will set foot in."
Its comment names a note for each half:
"%% Agent, the chandlery goes in idea-harrow-point, the only-shop habit in idea-mara-habits. %%"

The migrator split it into two copies:
- in Ideas/idea-mara-habits.md (line 9): "- The only shop in the village Mara will set foot in is Fenwick's chandlery on the quay." This went where the comment said. It is correct.
- in Ideas/idea-mara-lighthouse.md (line 10): "- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin." This is the chandlery half. The comment named idea-harrow-point, and it went to idea-mara-lighthouse instead.

The planted error: the writer's comment named a note for the chandlery, and the copy went elsewhere. Its wording is faithful, word for word the source. Only where it went is wrong. A comment that names a note and was not followed is a `scope` problem.

PASS if u1's verdict is `fix` and a problem with the check `scope` says the chandlery copy went to idea-mara-lighthouse when the comment named idea-harrow-point.
FAIL if u1 is approved; if no `scope` problem names the chandlery copy going to the wrong note; or if u1's only problems are about wording, or about the idea-mara-habits copy. Quote the verdict and the problems.
