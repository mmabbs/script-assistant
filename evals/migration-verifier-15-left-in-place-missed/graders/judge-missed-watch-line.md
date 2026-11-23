---
type: llm
---

Line A, in brain-dump.md (line 10), is tagged committed, and the comment on the line below it names a note:
"- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"
"%% Agent, char-mara. %%"

The writer's tag and comment ask for it to graduate to char-mara. The migrator made no unit for it and asked no question about it. Its only entry in the record is in `left_in_place`. No reason the rules allow fits: nothing in the line is unresolved, hedged, or a question, and it holds one idea. So the tag and comment asked for something the migrator didn't do, and no question covers it. That is a `missed` line. Code counts any line named in `left_in_place` as handled, so only the migration-verifier can catch it.

PASS if the reply's `missed` list holds an entry for line A, the wristwatch line: its `source` names brain-dump.md and the wristwatch line, by its text or by line 10.
FAIL if no `missed` entry names the wristwatch line. An entry that names only the comment (line 11) and not the wristwatch line is a FAIL. Quote the `missed` list.
