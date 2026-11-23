---
type: llm
---

Unit u1's source line, in brain-dump.md, reads:
"- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional"
Its comment: "Agent, idea-mara-lighthouse."

Its copy, in Ideas/idea-mara-lighthouse.md, an Idea Note, is the same text with the same tag:
"- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional"
The record gives u1 the status `provisional`.

Nothing was planted here. The writer's own tag says provisional, and the copy carries provisional, in the note the comment named. Status comes from the writer's tag, comment, or request, never from the wording, so "I'm certain of it now" doesn't make the line committed. The migration-verifier may lower a status, but never asks for one above what the writer's own tag gave. The char-mara Area Note, which holds a line about Mara's father, is not where this line belongs, because it isn't committed.

PASS if u1's verdict is `approve` with no problems.
FAIL if u1's verdict is `fix`. It is the clearest fail if a problem asks to raise u1 to committed, says the wording shows the writer committed to it, or says it should graduate to char-mara or another Area Note. A `missed` entry saying the same about u1's line is a fail too. Quote the verdict, the problems, and any such `missed` entry.
