# 2026-10-13 Regrade: Bare Migration-verifier Batch 1, With the Note Check

The 27 bare replies of `2026-10-12-bare-opus-5-5-migration-verifier-cases-batch-1.md`, graded again after the shape judges of cases 1 to 4 gained the note check. No new Claude runs; judges only. This is plan-migration-verifier.md 03, Milestone 1, its second step.

## What Changed in the Judges

Each `judge-shape.md` in cases 1 to 4, the batch-1 cases with a `fix` verdict, now checks that every problem on a fix-expected unit has `note` and `line` pointing at the bad text (spec-migration-verifier.md 10 item 28). A Sonnet 5.5 worker wrote the edits and took the line numbers from each built fixture with `grep -n`, frontmatter counted.

| Case | Unit | Where its problems must point |
| --- | --- | --- |
| 1 | u1 | `Ideas/idea-tobias.md` line 10, the copy that lost "nine" |
| 1 | u2 | `Ideas/idea-mara-lighthouse.md` line 10, the copy that lost "Maybe" |
| 2 | u1 | `char-mara.md` line 20 |
| 2 | u2 | `Ideas/idea-mara-lighthouse.md` line 10 |
| 3 | u2 | `Ideas/idea-harrow-point.md` line 13, the rejected copy, or line 9, where the record puts its source |
| 3 | u3 | `Ideas/idea-mara-lighthouse.md` line 10, the edited causeway line |
| 4 | u1 | `char-mara.md` line 20 |

Case 3's u2 takes two lines because decision 28 counts "a rejected source line" as where a `scope` overreach can sit. All three bare runs used line 9.

## How the Runs Were Regraded

The 2026-10-12 run folders were in a temp folder that is gone. Each run's final reply is copied in full in that run's results file, Full Outputs. A script rebuilt each run folder from it: `reply.txt`, and a `stream.jsonl` holding one `result` event with the reply. Then:

```bash
python3 _tools/research-run.py --suite migration-verifier --out <rebuilt folder> --regrade --runs 3
```

1. **Every llm judge reads only the reply** (no batch-1 grader has a `focus` file), so the judges graded the same text as on 2026-10-12.
2. **The `no-edit` and `no-write` checks are not re-derived.** The rebuilt stream holds no tool calls, so they pass by construction. They passed in all 27 original runs.
3. **Every judge re-ran,** because the rebuilt folders held no saved judge answers. `--regrade` doesn't report judge cost.

## Result

| Case | 2026-10-12 | 2026-10-13 regrade | Failing check |
| --- | --- | --- | --- |
| 1 `migration-verifier-01-lost-detail` | 3 of 3 | 1 of 3 | r2, r3: `judge-shape`, both problems name `brain-dump.md` line 10 and 13 |
| 2 `migration-verifier-02-status` | 3 of 3 | 3 of 3 | |
| 3 `migration-verifier-03-scope` | 3 of 3 | 3 of 3 | |
| 4 `migration-verifier-04-standalone` | 3 of 3 | 1 of 3 | r1, r3: `judge-shape`, both u1 problems name `brain-dump.md` |
| 5 to 9 | 15 of 15 | 15 of 15 | |
| **Total** | **27 of 27** | **23 of 27** | |

1. **The four fails are the four slips the bare-run record named** (2026-10-12 record, Findings item 3). No other run fails the note check.
2. **Every other judge gave the same verdict as on 2026-10-12,** in all 27 runs. So the rebuilt folders grade like the originals.
3. **The baseline now shows a slip bare Claude makes:** in 4 of the 12 runs of cases 1 and 4, the problem names the source note, not the copy.

## Prompt Changes Made the Same Day

Milestone 1's third step changed every batch-1 `prompt.md` to match what `skills/run/SKILL.md` hands the agent. The bare replies above answered the old prompts. Agent runs from Milestone 2 on use the new ones.

1. **Cases 1 to 7:** the batch is handed as its pieces, as `batches.json` holds them (CONTRACT.md 5.2), in place of a line range in words. Each fixture now writes `batches.json`. The brain-dump pieces came from the Run manager's own `scan.note_pieces`; the idea-note pieces use each old prompt's line numbers, as the notes stood when the run started.
2. **Cases 8 and 9:** only `verify-flags.json` is handed, rewritten in CONTRACT.md's flags-section shape: `{"flags": [...], "units": {"b1-u1": {...}}}`. Before, it held a unit list and the flags were a second file. `flags-1.json` stays in the fixture.
3. **All nine:** the answer shape, the "Judge every unit…" or "Judge every flag…" line, and the list of checks are gone. The skill hands none of them, so the agent file carries them.
4. **`skills/run/SKILL.md`:** the migration-verifier's batch step now says "its pieces as they are," as the Migrator's step does.
5. **No spec gap:** the skill hands everything spec-migration-verifier.md 03.1 and 03.2 list.
