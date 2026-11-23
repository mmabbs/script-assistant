---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The Brain Dump holds two bullets under 2026-10-07 and a comment below them: "Agent, both of these belong in idea-lighthouse." The first bullet, "The last keeper logged 38 nights of fog in her final winter, every one in green ink.", already ends in a `[migrated-to:: …]` pointer naming idea-lighthouse, and its copy already sits in idea-lighthouse from an earlier run. The second bullet, about Mara finding the last keeper's spare key under the third stair, has no pointer and no copy yet.

This file is the migrator's unit record. Each unit's `copies` lists the lines it adds to a note.

PASS if no `copies` entry in any unit holds a line about the last keeper's 38 nights of fog or her green ink. Naming that bullet elsewhere, such as in `left_in_place` or in a `why`, is fine.
FAIL if any `copies` entry holds a line about the last keeper's 38 nights of fog or her green ink.
