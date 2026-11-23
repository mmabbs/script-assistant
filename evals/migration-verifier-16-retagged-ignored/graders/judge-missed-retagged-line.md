---
type: llm
---

An earlier migration run, on 2026-10-02, copied this provisional line from brain-dump.md to Ideas/idea-mara-habits.md and wrote a pointer on the source line. Since then the writer changed its tag to committed. It now reads (brain-dump.md, line 11, under "### 2026-10-02"):
"- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"

The changed tag made the line new work in this run, so it is in the batch. A committed tag asks for the line to graduate to an Area Note, such as char-mara.md. Nothing did: no unit has it as a source, no question asks about it, and char-mara.md holds no line about the notebook. Its only entry in the record is in `left_in_place`. The pointer naming idea-mara-habits is not a reason: it says the line was copied to that Idea Note before, not that it graduated. A re-tagged line the migrator ignores is `missed`.

PASS if the reply's `missed` list holds an entry for the notebook line: its `source` names brain-dump.md and the notebook line, by its text or by line 11.
FAIL if no `missed` entry names the notebook line, for example because the reply treats the line as handled, already migrated, or the earlier run's business. Quote the `missed` list.
