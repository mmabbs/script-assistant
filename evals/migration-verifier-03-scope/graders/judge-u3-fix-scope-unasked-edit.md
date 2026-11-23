---
type: llm
---

Unit u3 migrates this line from brain-dump.md, whose comment says "Agent, idea-mara-lighthouse.":
"- Mara's radio is the only link to the mainland when the causeway floods."
Its copy, in Ideas/idea-mara-lighthouse.md, is the same text. The copy is correct.

u3 also holds an edit to the writer's existing line just above the copy, in the same note. No comment sits on or near that line:
- before: "- the causeway floods at spring tides, about twice a month"
- after: "- The causeway floods at spring tides, about twice a month."

The planted error: a wording fix on a neighbouring line that nobody asked for. The writer's words stay untouched unless a comment asks.

PASS if u3's verdict is `fix` and a problem with the check `scope` names the unasked edit to the causeway line (the capital and the full stop, or the change to the writer's line).
FAIL if u3 is approved, if no `scope` problem names the causeway edit, or if u3's problems name only the radio copy and not the edit. Quote the verdict and the problems.
