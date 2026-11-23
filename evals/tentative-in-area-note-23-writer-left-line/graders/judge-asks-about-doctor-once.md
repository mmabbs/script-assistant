---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The Area Note char-mara.md holds the line "- Mara is wary of the mainland doctor. #status/provisional", which the writer left there among plain lines.

The rule: the migrator leaves the line as it is and asks about it once, in `questions`.

This file is the migrator's unit record. Questions for the writer are entries in `questions`, each with an `ask`.

PASS if exactly one entry in `questions` asks the writer about the mainland-doctor line, such as whether it should stay, move, or change status.
FAIL if no entry in `questions` asks about the mainland-doctor line, or if more than one entry does.
