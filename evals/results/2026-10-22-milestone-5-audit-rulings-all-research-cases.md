# 2026-10-22 Milestone 5 Runs: Every Research Case on the Audit-Ruling Agents

Plan Milestone 5 builds the writer's rulings 03.1, 03.2, 03.5, and 03.13 (spec-research-workflow.md 11 items 103 to 106). These runs test the four updated agent files on every active research case, the four new ones included: P5, W10, W11, and E10. W8 is retired. The runner is `_tools/research-run.py`; raw runs sit in the session scratchpad under `m5-runs/`.

## What Was Run

- **Date:** 2026-10-22, 16:17 to 16:44 EDT.
- **Agents:** `script-asst:research-planner`, `script-asst:research-writer`, `script-asst:research-evaluator`, each three runs per case.
- **Cases:** W1 to W3, W6, W9 to W11; P1, P2, P5; E1 to E4, E6 to E10.
- **Rounds:** the first round found failures in P5, W1 to W3, and E4. The planner and writer files were fixed and their cases rerun; E4's fixture was fixed twice and E1 to E4, E6, E10, and W11 rerun on it. The table gives the final round on the final files.
- **Errors and timeouts:** none.
- **Cost:** about $34 reported across every round, judges included.

## Summary Table (final files)

| Case | Result |
| --- | --- |
| P1, P2 | 3 of 3 each |
| P5 Almond request | 3 of 3 (5, 6, and 5 topics; no waits) |
| W1 to W3, W6, W9 | 3 of 3 each |
| W10 judgment sentence | 2 of 3, then 3 of 3 after item 111 (see Formatting Rerun) |
| W11 fix-round copy | 3 of 3 |
| E1 to E4 | 12 of 12 |
| E6, E10 | 3 of 3 each |
| E7 to E9 | 3 of 3 each (first round; their fixtures and agent file didn't change after) |

## Findings

1. **P5 took three planner fixes.** With item 103's rule alone, the planner stopped drawing out questions and wrote one topic of one or two sentences, 3 of 3. Told to draw out the questions a request implies, it split Almond into 5 topics, but topic 1 still bundled questions. A self-check, then a line that topic 1 is no catch-all, brought it to 3 of 3. The Pass line was loosened twice by the writer along the way (plan-research-workflow.md 05 items 28 and 29). Spec 11 item 107 records the planner's readings.
2. **The writer dropped Disagreement / Uncertainty in 4 of 9 runs of W1 to W3** after the judgment-sentence rule went in. The file now keeps that heading, empty if nothing fits, and says the judgment rule covers the researcher's findings sentences only (spec 11 item 108). W1 to W3 then held 9 of 9.
3. **E4's "clean" note wasn't clean.** One sentence had no footnote, and the Summary said "by hand" where the findings say "grozing iron." The evaluator flagged each once. Both fixed in the shared stained-glass fixture, with E6's and W11's patterns (plan 05 item 30).
4. **W10 r1 failed on "It is disputed (see Disagreement / Uncertainty)."** The dispute is sourced, by the 2018 article the note cites under Disagreement / Uncertainty, so the researcher's judgment didn't leak. But the sentence carries no footnote, which the research-evaluator's rule 1 would fail in a live run. Left at 2 of 3 for the writer.
5. **E10, the scoped re-check, held 6 of 6** across two rounds: plants 2 to 4 reported every time, plant 1 never.

## Live Almond Runs

| Run | Researchers | Pages opened | Cited URLs never opened | Note words |
| --- | --- | --- | --- | --- |
| 1, 2026-10-18 | 1 | 0 | 35 of 35 | 3,714 |
| 2, `run-2026-10-22-1659-research` | 8 | 0 | 226 of 226 | 13,238 |
| 3, `run-2026-10-22-1905-research` | 7 | 50 to 82 each | 1 of 93 | 11,093 |

6. **Run 2 opened nothing because WebFetch was denied** in the writer's user settings, which removes the tool from every agent. The researchers worked from search results alone; the one transcript read says so outright. That deny, not the 30-turn limit, explains run 1 too. The deny is gone; the hook approves the researcher's web tools (spec-run-manager.md 11 item 92); a researcher with no page tool now fails (spec-research-workflow.md 11 item 110).
7. **Run 3's one miss:** a researcher listed a page it marked "not opened… seen only in search results," and it reached the note as a footnote. One other URL was a blocked page whose mirror the researcher opened and named.
8. **Run 3's fix round and scoped re-check ran live and passed.** The planner named the request `catching-anxiety`, since `anxiety-contagion` and `anxiety-spread` already had plan files (spec item 109).
9. **Word counts include frontmatter and the Sources list.** The note grows with the topic count: each findings file may run 2,500 words, and spec item 59 keeps every finding.

## Formatting Rerun

10. **After spec item 111 (`###` sub-headings, paragraphs of about 100 words at most), W1 to W3 and W9 to W11 held 18 of 18, W10 included.** Every note used `###` sub-headings and no bold lead-ins; the longest paragraph in any note ran 76 words. W11's notes have no `###` headings, since the fix round only fixes the note it's handed. W6 was not rerun. Cost $5.54.
11. **Run 3's Summary holds no sentence of a researcher's own judgment.** Each cross-source sentence reports what its cited sources say. Topic 1's findings carried one ranking, "(strongest direct human evidence found)," which the research-writer left out of the note.
