---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The source bullet had three ideas in one line: (1) Mara is the only keeper since her father, (2) a second keeper arriving from the mainland, and (3) the lighthouse being sold to a hotel chain. Only the first should graduate to the Area Note. The unit record must show that the second-keeper and hotel-chain ideas were left out and ask the writer whether the committed tag covers them.

This file is the migrator's unit record. Questions for the writer are entries in `questions`, each with an `ask`. Things left behind are entries in `left_in_place`. What was migrated is in `units`, under each unit's `copies`.

PASS if the record shows that the second-keeper idea and the hotel-chain idea were not migrated (no `copies` entry holds them; a `left_in_place` entry or a question's `ask` may say so) and an entry in `questions` asks the writer whether they should be.
FAIL if no entry in `questions` asks about the two left-out ideas, or if the record's `copies` hold all three ideas without such a question.
