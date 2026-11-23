---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The Brain Dump holds two bullets under 2026-10-14, each with a comment directly under it. The first bullet, "The lamp room's north pane has a star-shaped crack, and Mara has never reported it to the lighthouse board.", has the comment "Agent, tag this provisional." That comment asks only for a status tag. The second bullet, about Tobias's tally in the boathouse beam, has the comment "Agent, tag this provisional and put it in idea-tobias."

The rule: a comment that asks only for a status tag doesn't move the line. The migrator adds the tag to the Brain Dump line, as a unit whose `action` is `edit`, and copies the line nowhere.

This file is the migrator's unit record. Each unit has an `action`, its `copies` (lines added to notes), and its `edits` (changes to existing lines, each with `before` and `after`).

PASS if a unit with `action` `edit` changes the north-pane line in brain-dump.md so that it ends in `#status/provisional`, and no unit's `copies` holds a line about the north pane or its star-shaped crack.
FAIL if no `edit` unit adds the tag to the north-pane line, or if any `copies` entry holds a line about the north pane or its crack.
