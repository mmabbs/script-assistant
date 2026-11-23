---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The Brain Dump holds two untagged bullets under 2026-10-20. Under the first, "The fog bell rings on its own the night before every drowning.", sits a comment the Run manager wrote to carry the writer's typed request from an earlier run: `%% [AGENT] Your request from the migration run of 2026-10-21, for this line: "everything about the fog bell goes into idea-lighthouse, tagged or not" %%`. It counts as the writer's comment, for the line above it only. The second bullet, "The fog bell was cast from melted wedding rings.", has no tag and no comment of its own.

This file is the migrator's unit record. Each unit has a `trigger` with a `kind` and `text`, and `copies` lists the lines it adds to a note.

PASS if all three hold:
1. One unit copies the drowning line into idea-lighthouse.
2. That unit's `trigger` `kind` is `comment`, and its `text` holds the request comment's words.
3. No unit's `copies` holds a line about the bell being cast from wedding rings. Naming that bullet in `left_in_place` or in a `questions` entry is fine.
FAIL if any of the three doesn't hold.
