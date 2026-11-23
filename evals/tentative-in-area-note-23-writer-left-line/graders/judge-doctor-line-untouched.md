---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The Area Note char-mara.md holds, among plain lines under Psychology, the line "- Mara is wary of the mainland doctor. #status/provisional". The writer left it there. The batch hands it to the migrator as a trigger line, because it carries a status tag.

The rule: a provisional line the writer left in an Area Note stays there. The migrator doesn't move, retag, or rewrite it. It asks about it once, in `questions`.

This file is the migrator's unit record. Each unit lists its `sources`, its `copies` (lines added to notes), and its `edits` (changes to existing lines).

PASS if no unit holds the mainland-doctor line in its `sources`, `copies`, or `edits`. Naming it in `questions` or `left_in_place` is fine.
FAIL if any unit's `sources`, `copies`, or `edits` holds the mainland-doctor line, in any wording, or a changed form of it, such as one without its tag or with a different tag.
