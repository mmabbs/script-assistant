---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The Brain Dump bullet "The lamp room's north pane has a star-shaped crack, and Mara has never reported it to the lighthouse board." has the comment "Agent, tag this provisional." under it, which asks only for a status tag. The project has two Idea Notes: idea-lighthouse, with sections on the lamp room and the tower, and idea-tobias.

The rule: the migrator adds the tag, doesn't move the line, and asks in `questions` whether the line should move, naming the note it would fit. Here that note is idea-lighthouse.

This file is the migrator's unit record. Questions for the writer are entries in `questions`, each with an `ask`.

PASS if an entry in `questions` asks the writer whether the north-pane line should move (or be migrated), and names idea-lighthouse, or the lighthouse note, as where it would go.
FAIL if no entry in `questions` asks whether the north-pane line should move, or if the entry that asks names no note, or names a note other than idea-lighthouse.
