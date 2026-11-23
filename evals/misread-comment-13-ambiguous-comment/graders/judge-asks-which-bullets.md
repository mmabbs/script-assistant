---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The writer's comment said "move the good ones to idea-harrow-point" without naming any of the four bullets.

This file is the migrator's unit record. Questions for the writer are entries in `questions`, each with an `ask`. What was migrated is in `units`, under each unit's `copies`.

PASS if the record shows nothing was migrated (no unit has a `copies` entry holding any of the four bullets) and an entry in `questions` asks the writer which bullets are meant.
FAIL if any unit's `copies` hold one of the bullets, or if no entry in `questions` asks the writer to clarify.
