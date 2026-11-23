---
type: llm
---

Every unit in this batch is correct. Nothing was planted. Both edits sit in Ideas/idea-mara-lighthouse.md, each with the writer's comment on the line below it.

- u1, an edit. Comment: "%% Agent, please correct the spelling in that line. %%"
  - before: "- Mara repaints the gallery railing evrey spring, its the only job she enjoys."
  - after: "- Mara repaints the gallery railing every spring. It's the only job she enjoys."
  The spelling fixes ("evrey" to "every", "its" to "It's") also turn a comma splice into two sentences. That comes with the asked-for fix and keeps the line's meaning, so it is asked for. Asked for is judged by meaning.
- u2, an edit. Comment: "%% Agent, tidy the grammar here. %%"
  - before: "- the keeper before Mara were a drunk named Ollie Venn"
  - after: "- The keeper before Mara was a drunk named Ollie Venn."
  "were" to "was", the capital, and the full stop are all grammar tidying. The meaning is unchanged.
- u3, a migration. Source in brain-dump.md: "- Mara counts the steps on the way up: 114." Comment: "Agent, idea-mara-lighthouse." Copy in Ideas/idea-mara-lighthouse.md: the same text.

PASS if all three units, u1 to u3, have the verdict `approve` with no problems.
FAIL if any unit's verdict is `fix`, and especially if u1 is fixed for the comma splice or the capital, or u2 for the added full stop. Quote the verdict and the problems.
