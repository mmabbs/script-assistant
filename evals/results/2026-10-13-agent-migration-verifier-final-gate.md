# 2026-10-13 Final Gate: Migration-verifier, All Fourteen Cases

All fourteen migration-verifier cases, three runs each, on the final agent file. This is the last step of plan-migration-verifier.md 03, Milestone 3, and its done check: every Pass line of all fourteen cases holds in 3 of 3 runs on the final agent file.

## What Was Run

- **Date:** 2026-10-13, 18:00 to 18:04 EDT.
- **Agent:** `agents/migration-verifier.md`, 163 lines, `model: claude-opus-5-5`, `effort: high`, `tools: Read, Glob, Grep`. The only change since batch 2's runs: "The Batch Check: What Was Left Out" item 3 now follows spec-migration-verifier.md 10 item 30. The earlier run's copy is not this run's business; a re-tagged line the Migrator ignored is `missed`.
- **Claude Code:** 2.1.296.
- **Runs:** 42. Fourteen cases, three runs each, at most five at a time.
- **Command:**

```bash
python3 _tools/research-run.py --suite migration-verifier --agent script-asst:migration-verifier \
  --out <session scratchpad>/mv-agent-final --runs 3
```

- **Errors and timeouts:** none. Every run exited 0. No run was repeated.
- **Cost:** $10.63 for the runs, from their streams. With judges, the runner printed $13.91.

## Result

| Case | All checks | Cost |
| --- | --- | --- |
| 1 `migration-verifier-01-lost-detail` | 3 of 3 | $0.84 |
| 2 `migration-verifier-02-status` | 3 of 3 | $0.80 |
| 3 `migration-verifier-03-scope` | 3 of 3 | $0.73 |
| 4 `migration-verifier-04-standalone` | 3 of 3 | $0.70 |
| 5 `migration-verifier-05-missed-line` | 3 of 3 | $0.72 |
| 6 `migration-verifier-06-clean-batch` | 3 of 3 | $0.77 |
| 7 `migration-verifier-07-asked-by-meaning` | 3 of 3 | $0.66 |
| 8 `migration-verifier-08-flags-asked` | 3 of 3 | $0.77 |
| 9 `migration-verifier-09-flags-not-asked` | 3 of 3 | $0.74 |
| 10 `migration-verifier-10-recheck` | 3 of 3 | $0.74 |
| 11 `migration-verifier-11-status-raise` | 3 of 3 | $0.69 |
| 12 `migration-verifier-12-earlier-run-status` | 3 of 3 | $0.71 |
| 13 `migration-verifier-13-large-batch` | 3 of 3 | $0.99 |
| 14 `migration-verifier-14-comment-names-note` | 3 of 3 | $0.77 |
| **Total** | **42 of 42** | **$10.63** |

## Code Checks

1. **Every reply is bare JSON that `runmanager findings` would accept,** by the code's own `shape_problem` in `migration/findings.py` or `migration/flags.py`.
2. **Every case gives the same verdicts, checks, and pointers in all three runs.**
3. **Tools:** Read, Glob, and Grep only. No write.

## Findings

1. **The gate holds: 42 of 42 on the final agent file.** Milestone 3 is done.
2. **Effort `high` passed the gate,** so effort stays `high` (plan-migration-verifier.md 05 item 4).
3. **Both duties pass in one file.** The flags cases, 8 and 9, pass in all six runs beside the twelve batch-check cases. The duties don't overload one agent.
4. **Across the day, the agent passed 84 of 84 runs:** batch 1 (27), batch 2 (15), and this gate (42), with one agent-file change, from a spec ruling, not a fail.

## Full Outputs

Each run shows its grades, then its final reply.

### Case 1: `migration-verifier-01-lost-detail`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units appear in the reply with a verdict: - u1: `"verdict":"fix"` - u2: `"verdict":"fix"` - u3: `"verdict":"approve"`  The two units with lost detail are marked `fix`, not `missed`. For u1 the reply notes "the copy says only 'when she was a child', so her age is lost." For u2 it notes "the copy drops 'maybe' and states it as fact." Tha
PASS  judge-shape   Evidence: - The reply is JSON findings with `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`. - `units` has exactly one entry each for u1, u2, and u3, with no other units. - **u1**: `"verdict":"fix"`, with one problem: `{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,...}`. The check is valid, the note is the expected copy (not `brain-dump.md`), and the line is 10. - **u2*
PASS  judge-u1-fix-lost-age   The reply gives u1 a verdict of `"verdict":"fix"`. That unit has one problem, and it points at the idea-tobias copy:  - `"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,"what":"The source says Tobias drowned when Mara was nine, but the copy says only 'when she was a child', so her age is lost."`  This problem names the right file (`Ideas/idea-tobias.md`). It also says the age "nine"
PASS  judge-u2-fix-lost-maybe   u2 is marked `fix`, and its single problem names the lost hedge:  - Verdict: `"unit":"u2","verdict":"fix"` - Problem: `{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the logbook, but the copy drops 'maybe' and states it as fact."}`  The check is `lost-detail`, which is one of the two accepted values. The note says plainly tha
PASS  judge-u3-approve   The final reply gives u3 the verdict `approve` with an empty problems list:  `{"unit":"u3","verdict":"approve","problems":[]}`  It does not flag the rewording ("even though" → "still ... though") or anything else for u3. The problems in the reply belong only to u1 and u2. That matches the PASS condition.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,"what":"The source says Tobias drowned when Mara was nine, but the copy says only 'when she was a child', so her age is lost."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the logbook, but the copy drops 'maybe' and states it as fact."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units in the batch have entries in `units`: - `"unit":"u1","verdict":"fix"` - `"unit":"u2","verdict":"fix"` - `"unit":"u3","verdict":"approve"`  The units with flawed copies (u1 losing "nine", u2 dropping "maybe") are correctly recorded as `fix`, not as `missed` entries.
PASS  judge-shape   The reply is valid JSON with `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`.  - **Units:** There is exactly one entry each for `u1`, `u2`, and `u3`, and none for any other unit. - **u1:**   - Verdict: `"verdict":"fix"`   - Problem: `{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,...}`   - It has one problem, the check is allowed, the note is the expected copy, and the l
PASS  judge-u1-fix-lost-age   Unit u1 got the verdict `"verdict":"fix"`.  It has one problem, and that problem points at the idea-tobias copy and names the lost age: - `"note":"Ideas/idea-tobias.md"` - `"what":"The source says Tobias drowned when Mara was nine. The copy only says she was 'a child', so her exact age is lost."`  This is the planted error. The source said "nine," and the idea-tobias copy changed it to "a child."
PASS  judge-u2-fix-lost-maybe   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`.  Its one problem names the lost hedge directly. It is filed under `"check":"lost-detail"` and reads: "The source says her father 'maybe' hid the keeper's logbook in the tower. The copy states it as fact and drops the 'maybe'."  That matches the planted error. The copy dropped "Maybe" and turned a possibility into a fact. `lost-detail` is one o
PASS  judge-u3-approve   The reply gives u3 the verdict `approve` with no problems: `{"unit":"u3","verdict":"approve","problems":[]}`. It does not flag the rewording ("even though" → "still ... though") or anything else, so the check's PASS condition is met.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,"what":"The source says Tobias drowned when Mara was nine. The copy only says she was 'a child', so her exact age is lost."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the keeper's logbook in the tower. The copy states it as fact and drops the 'maybe'."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`. All three units are covered in the record: `"unit":"u1","verdict":"fix"`, `"unit":"u2","verdict":"fix"`, `"unit":"u3","verdict":"approve"`. The wrong copies for u1 and u2 are recorded as `fix` verdicts, not as `missed` entries.
PASS  judge-shape   Evidence: - **Shape:** The reply is JSON with `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`. - **Units:** There is exactly one entry each for u1, u2, and u3, and none for any other unit. - **u1:** `"verdict":"fix"` with one problem:   - `"check":"lost-detail"`, `"note":"Ideas/idea-tobias.md"`, `"line":10`   - This matches the expected copy and line, not `brain-dump.md`. - **u2:** `"ve
PASS  judge-u1-fix-lost-age   u1's verdict is `fix`: `{"unit":"u1","verdict":"fix",...}`  Its one problem points at the idea-tobias copy and names the lost age: - `"note":"Ideas/idea-tobias.md"` - `"what":"The source says Tobias drowned when Mara was nine; the copy says only 'when she was a child', so the exact age is lost."`  This is the planted error. The problem is on the correct copy (idea-tobias, not idea-mara-habits), a
PASS  judge-u2-fix-lost-maybe   u2's verdict is `fix`: `{"unit":"u2","verdict":"fix",...}`  It has one problem, and that problem names the lost hedge: `{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the keeper's logbook in the tower; the copy states it as fact."}`  The note quotes "maybe" from the source and says the copy "states it as fact," so it identifi
PASS  judge-u3-approve   The final reply gives u3 this verdict: `{"unit":"u3","verdict":"approve","problems":[]}`.  The verdict is `approve` and the problems list is empty. The reworded line ("still smells of paraffin, though") was not flagged. The `fix` verdicts in the reply belong only to u1 and u2, which this check does not cover.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,"what":"The source says Tobias drowned when Mara was nine; the copy says only 'when she was a child', so the exact age is lost."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the keeper's logbook in the tower; the copy states it as fact."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 2: `migration-verifier-02-status`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units appear in `units`: - `"unit":"u1","verdict":"fix"` - `"unit":"u2","verdict":"fix"` - `"unit":"u3","verdict":"approve"`  The status problems on u1 and u2 are reported as `fix` verdicts, not as `missed` entries, which is what the check requires.
PASS  judge-shape   Evidence: - **Shape:** The reply is JSON with `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`. - **Units:** There is exactly one entry each for `"unit":"u1"`, `"unit":"u2"` and `"unit":"u3"`, and no others. - **Verdicts:** All are valid: u1 `"verdict":"fix"`, u2 `"verdict":"fix"`, u3 `"verdict":"approve"`. - **u1:** It is a `fix` with one problem: `{"check":"status","note":"char-ma
PASS  judge-u1-fix-provisional-in-area-note   Evidence: - The verdict for u1 is fix: `"unit":"u1","verdict":"fix"` - It has a `status` problem that names provisional material in char-mara, the Area Note: `"check":"status","note":"char-mara.md","line":20,"what":"The writer tagged this line provisional, but the copy was placed in Mara's character note, which is only for committed material. Provisional material belongs in an Idea Note."` - The 
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`.  Both of its problems name the gap between what the writer said and the provisional copy: - On the tag: `{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer tagged this line committed, but the copy is tagged provisional, which is lower than the status the writer gave it."}` - On the comment: `{"check":"scope",
PASS  judge-u3-approve   The reply gives u3 the verdict `approve` and lists no problems: `{"unit":"u3","verdict":"approve","problems":[]}`. That is what the check requires for a correct line with nothing planted.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"status","note":"char-mara.md","line":20,"what":"The writer tagged this line provisional, but the copy was placed in Mara's character note, which is only for committed material. Provisional material belongs in an Idea Note."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer tagged this line committed, but the copy is tagged provisional, which is lower than the status the writer gave it."},{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer's comment says this line goes in char-mara, but the copy went to the Mara Lighthouse Idea Note."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units appear in the record: - `"unit":"u1","verdict":"fix"` - `"unit":"u2","verdict":"fix"` - `"unit":"u3","verdict":"approve"`  The status errors on u1 and u2 are recorded as `fix` verdicts, not as `missed` entries, which is what the check expects.
PASS  judge-shape   The reply is JSON with all four keys: `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`.  **Units:** There is exactly one entry each for u1, u2 and u3, and no other units.  **u1:** - Verdict: `"verdict":"fix"` - One problem: `{"check":"status","note":"char-mara.md","line":20,...}` - `check` is one of the four allowed values. - `note` and `line` match the expected `char-mara.md` line 
PASS  judge-u1-fix-provisional-in-area-note   The verdict is a fix, and the `status` problem names provisional material in char-mara, the Area Note.  - Verdict for u1: `"unit":"u1","verdict":"fix"` - Its only problem: `{"check":"status","note":"char-mara.md","line":20,"what":"The writer tagged this line provisional, but the copy went into Mara's Area Note, which holds only committed material. It belongs in an Idea Note, at provisional, until
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`. Both of its problems name the gap the check asks for.  - **Status problem:** `{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer tagged this line committed, but the copy is tagged provisional. That is lower than the writer gave it."}` This states that the copy is provisional where the writer tagged it committ
PASS  judge-u3-approve   The text gives u3 the verdict `approve` with an empty problems list: `{"unit":"u3","verdict":"approve","problems":[]}`. It raises no `fix` and no problems for u3, which is what the check expects for this correct, unplanted line.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"status","note":"char-mara.md","line":20,"what":"The writer tagged this line provisional, but the copy went into Mara's Area Note, which holds only committed material. It belongs in an Idea Note, at provisional, until the writer commits it."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer tagged this line committed, but the copy is tagged provisional. That is lower than the writer gave it."},{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer's comment says this goes in char-mara, but the copy went into the Mara Lighthouse Idea Note instead."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units are covered in `units`. Two are `fix` and one is `approve`: - `{"unit":"u1","verdict":"fix",...}` - `{"unit":"u2","verdict":"fix",...}` - `{"unit":"u3","verdict":"approve","problems":[]}`  The status errors on u1 and u2 are reported as `fix` verdicts, not as `missed` entries, which is what the check requires.
PASS  judge-shape   **Units:** There is exactly one entry each for `"unit":"u1"`, `"unit":"u2"` and `"unit":"u3"`, and no other units. `"missed":[]` is present, along with `"batch":"b1"` and `"round":0`.  **u1:** `"verdict":"fix"`, with one problem: - `{"check":"status","note":"char-mara.md","line":20, ...}` - The check is valid, and the note and line match the expected `char-mara.md` line 20. - The extra `"text_unu
PASS  judge-u1-fix-provisional-in-area-note   Evidence: - The verdict for u1 is fix: `"unit":"u1","verdict":"fix"` - It has a `status` problem that names provisional material in char-mara, the Area Note: `"check":"status","note":"char-mara.md","line":20,...,"what":"The writer tagged this line provisional, but the copy sits in Mara's Area Note, which holds only committed material. A provisional idea belongs in an Idea Note."` - The fix does n
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`.  Two problems name the gap between the writer's committed tag (and comment) and the provisional copy:  1. Status check: `{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer tagged this line committed, but the copy was written as provisional in an Idea Note, which is lower than the status the writer gave it."}`
PASS  judge-u3-approve   The reply gives u3 an approval with an empty problem list: `{"unit":"u3","verdict":"approve","problems":[]}`. The verdict is `approve` and there are no problems, so it meets the PASS condition.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"status","note":"char-mara.md","line":20,"text_unused":null,"what":"The writer tagged this line provisional, but the copy sits in Mara's Area Note, which holds only committed material. A provisional idea belongs in an Idea Note."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer tagged this line committed, but the copy was written as provisional in an Idea Note, which is lower than the status the writer gave it."},{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer's comment says this goes in char-mara, but the copy went to the Mara Lighthouse Idea Note instead."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 3: `migration-verifier-03-scope`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both batch items have a unit in the record, and no entry was added to `missed`. The too-wide reading of the hotel-sale rejection was raised as a `fix` on u2, which is the right channel under the check's rule. Its note reads: "Your comment ruled out the hotel sale for Mara's story only and said the town can still have it. This town line ... was r
PASS  judge-shape   Evidence: - **JSON shape:** The reply is JSON with `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`. - **Units:** There is exactly one entry each for u1, u2, and u3, and no other units appear. - **u1:** `{"unit":"u1","verdict":"approve","problems":[]}` approves the unit with an empty problems list. - **u2:** `"verdict":"fix"` has one problem: `{"check":"scope","note":"Ideas/idea-harrow-p
PASS  judge-u1-approve   u1's verdict in the text is `approve`, and its problem list is empty: `{"unit":"u1","verdict":"approve","problems":[]}`.  The scope problems in the reply belong to other units. u2 widened the hotel-sale rejection to the town line in `Ideas/idea-harrow-point.md`. u3 made an unrequested capitalisation and punctuation edit to the causeway line. Neither is about u1. The check asks only for u1's verdi
PASS  judge-u2-fix-scope-town   u2's verdict is `fix`: `{"unit":"u2","verdict":"fix",...}`  It has one problem, and that problem uses the check `scope`. It names the town note, `"note":"Ideas/idea-harrow-point.md","line":13`, and says: "Your comment ruled out the hotel sale for Mara's story only and said the town can still have it. This town line about the hotel chain buying the harbour cottages and pier was rejected anyway, wh
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `fix`: `"unit":"u3","verdict":"fix"`.  It has one problem, and it is under the `scope` check: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line was rewritten with a capital letter and a full stop. No comment asked for that edit, and the line was not part of the migration."}`  This problem names the causeway edit directly. It mentions "a c
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-harrow-point.md","line":13,"what":"Your comment ruled out the hotel sale for Mara's story only and said the town can still have it. This town line about the hotel chain buying the harbour cottages and pier was rejected anyway, which reads the rejection wider than you meant it."}]},{"unit":"u3","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line was rewritten with a capital letter and a full stop. No comment asked for that edit, and the line was not part of the migration."}]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The overreach on the hotel-sale rejection is recorded as a `fix` on a unit (`"unit":"u2","verdict":"fix"` with `"what":"Your comment ruled out the hotel sale for Mara's story only and said the town can still have it. Rejecting the town's hotel chain buying the harbour cottages and pier stretches the rejection past what you asked."`). It is not l
PASS  judge-shape   Evidence: - **Top-level shape:** The reply is JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, `"missed":[]`. - **Unit coverage:** `units` has exactly three entries, `"unit":"u1"`, `"unit":"u2"` and `"unit":"u3"`. No unit is duplicated and none is extra. - **u1:** `"verdict":"approve","problems":[]` is an approve with an empty problems list, as required. - **u2:** `
PASS  judge-u1-approve   The check asks only about u1. The final reply has: `{"unit":"u1","verdict":"approve","problems":[]}`.  The verdict is `approve` and the problems list is empty, which meets the PASS condition. The `fix` verdicts for u2 and u3 are outside this check.
PASS  judge-u2-fix-scope-town   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`.  It has one problem, and that problem's check is `scope`. The problem sits on the town's note: `"check":"scope","note":"Ideas/idea-harrow-point.md","line":13`.  The problem says the rejection was applied to the town's hotel line beyond what the writer's comment covered: "Your comment ruled out the hotel sale for Mara's story only and said the 
PASS  judge-u3-fix-scope-unasked-edit   Evidence: - u3's verdict is fix: `"unit":"u3","verdict":"fix"` - u3 has one problem, under the check `scope`, and it names the unasked causeway edit along with the capital and the full stop: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line was reworded (capital letter and full stop added), but no comment or request asked for that line to be edited."}` -
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-harrow-point.md","line":13,"text_ignored":null,"what":"Your comment ruled out the hotel sale for Mara's story only and said the town can still have it. Rejecting the town's hotel chain buying the harbour cottages and pier stretches the rejection past what you asked."}]},{"unit":"u3","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line was reworded (capital letter and full stop added), but no comment or request asked for that line to be edited."}]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The over-wide rejection is reported as a `fix` on a unit, as the check expects. It appears under u2: `"verdict":"fix"` ... "This line about the town's harbour cottages and pier was rejected anyway, which takes the rejection further than you asked." Nothing is in `missed`.
PASS  judge-shape   The reply is valid JSON with `batch` ("b1"), `round` (0), `units` and `missed` ([]).  - **Units:** There is exactly one entry each for u1, u2 and u3, and no other units. - **u1:** `"verdict":"approve","problems":[]`. The verdict is valid and the problems list is empty, as an approve requires. - **u2:** `"verdict":"fix"` has one problem: `{"check":"scope","note":"Ideas/idea-harrow-point.md","line"
PASS  judge-u1-approve   The verdict for u1 is `approve`, and its problems list is empty: `{"unit":"u1","verdict":"approve","problems":[]}`.  That fits the check. The rejection the writer asked for was done correctly, so it should be approved with no problems.
PASS  judge-u2-fix-scope-town   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`.  It has one problem, and that problem has `"check":"scope"` and `"note":"Ideas/idea-harrow-point.md"`. It reads:  > "Your comment rules out the hotel sale for Mara's story only and says the town can still have it. This line about the town's harbour cottages and pier was rejected anyway, which takes the rejection further than you asked."  This 
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `fix`: `{"unit":"u3","verdict":"fix", ...}`  Its only problem has the check `scope` and names the unasked edit to the causeway line, including both the capital letter and the full stop: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line was reworded, with a capital letter and a full stop added, but no comment asked for that. Your comment o
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-harrow-point.md","line":13,"what":"Your comment rules out the hotel sale for Mara's story only and says the town can still have it. This line about the town's harbour cottages and pier was rejected anyway, which takes the rejection further than you asked."}]},{"unit":"u3","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line was reworded, with a capital letter and a full stop added, but no comment asked for that. Your comment only said where the radio line should go."}]}],"missed":[]}
````

### Case 4: `migration-verifier-04-standalone`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units have a verdict in the record, `"unit":"u1","verdict":"fix"` and `"unit":"u2","verdict":"approve"`. The standalone problem with u1 was reported as a `fix` (`"check":"standalone"... "'What happened that winter' doesn't make sense on its own."`) and not as a `missed` entry, which is what the check expects.
PASS  judge-shape   Evidence: - The reply is JSON with all four fields: `"batch":"b1","round":0,"units":[...],"missed":[]`. - `units` holds exactly one entry for u1 and one for u2, and no other units. - u1 has `"verdict":"fix"` and two problems:   - `{"check":"lost-detail","note":"char-mara.md","line":20,...}`   - `{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' doesn't make
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict":"fix"`, and both of its problems name the missing event.  - **lost-detail problem:** "The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy drops all of that and keeps only that Mara never forgave her." This names the licence sale, the cannery, and the winter Tobias died. - **standalone problem:** "'What happened
PASS  judge-u2-approve-rationale   The verdict for u2 is `approve` with an empty problems list: `{"unit":"u2","verdict":"approve","problems":[]}`.  Nothing flags the Rationale line ("I like that her discipline looks like penance.") for a rewrite, for failing to stand alone, or for being in the wrong voice. The only problems in the reply are under u1 ("lost-detail" and "standalone" on char-mara.md line 20), and they are about a dif
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"char-mara.md","line":20,"what":"The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy drops all of that and keeps only that Mara never forgave her."},{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' doesn't make sense on its own. Nothing in the note says which winter it was or what her mother did."}]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The problems that were found sit at the unit level, not in `missed`. Unit u1 has `"verdict":"fix"` with `lost-detail` and `standalone` problems. Unit u2 has `"verdict":"approve"`. This follows the rule that a copy that can't stand alone is a `fix`, not a `missed` entry.
PASS  judge-shape   The reply is a single JSON object with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  **`units` lists exactly u1 and u2, once each, and nothing else.**  **u1:** `"verdict":"fix"` with two problems. - Problem 1: `{"check":"lost-detail","note":"char-mara.md","line":20,...}`. The check is allowed, the note is `char-mara.md`, and the line is 20. - Problem 2:
PASS  judge-u1-fix-not-standalone   The reply gives u1 the verdict `"verdict":"fix"`. It does not approve it.  Both problems name the missing event behind "what happened that winter": - **lost-detail**: "The copy drops the main event: Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. Only Mara's grudge was kept, and the reason for it was cut." This names the licence sale, the cannery, and the wi
PASS  judge-u2-approve-rationale   The final reply gives u2 the verdict `approve` and lists no problems:  > `{"unit":"u2","verdict":"approve","problems":[]}`  Both problems in the reply belong to u1 ("lost-detail" and "standalone"). Neither mentions u2's Rationale line, so nothing asks to rewrite it, calls it unable to stand alone, or says it is in the wrong voice. The `missed` array is also empty (`"missed":[]`), so u2 is not fla
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"char-mara.md","line":20,"text_hint":null,"what":"The copy drops the main event: Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. Only Mara's grudge was kept, and the reason for it was cut."},{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' doesn't make sense on its own. Nothing in the Area Note says which winter it was or what happened."}]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units are accounted for in `units`: u1 has `"verdict":"fix"` (for lost detail and failing the standalone check), and u2 has `"verdict":"approve"`. Neither appears as a `missed` entry. That matches the check's expectation that every line has a unit and a copy that can't stand alone is a `fix`, not `missed`.
PASS  judge-shape   The reply is valid JSON. It has `"batch":"b1"`, `"round":0`, `units`, and `"missed":[]`.  - **Units:** There is exactly one entry for each unit handed, and no other units appear:   - `{"unit":"u1","verdict":"fix",...}`   - `{"unit":"u2","verdict":"approve","problems":[]}` - **Verdicts:** Both are allowed values (`fix` and `approve`). - **u1 (`fix`):** It has two problems, so it is not empty.   - 
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict":"fix"`, so it is not approved.  Two problems name the missing event behind "what happened that winter":  - **lost-detail** (char-mara.md, line 20): "The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy drops the sale, the cannery and Tobias's death, and keeps only that Mara never forgave her." This names all thr
PASS  judge-u2-approve-rationale   The final reply gives u2 the verdict `approve` with an empty problems list:  `{"unit":"u2","verdict":"approve","problems":[]}`  No problem is raised about the Rationale line "- I like that her discipline looks like penance." The reply does not say it should be rewritten, can't stand alone, or is in the wrong voice. All the problems in the reply (`lost-detail` and `standalone` at char-mara.md line
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"char-mara.md","line":20,"what":"The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy drops the sale, the cannery and Tobias's death, and keeps only that Mara never forgave her."},{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' points at nothing in the Area Note. A reader can't tell what happened or which winter is meant."}]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 5: `migration-verifier-05-missed-line`

#### Run 1

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list holds exactly one entry, and it is line A:  ``` "missed": [{"source": {"note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"}, "what": "This line is tagged committed, and the comment under it sends it to char-mara. Nothing was migrated, and char-mara has no line about the oilskin coat."}] ```  Lines B ("Mara 
PASS  judge-shape   The reply is JSON with all four required keys: `"batch": "b1"`, `"round": 0`, `units`, and `missed`.  - **One entry for u1, and no other unit:** `"units": [{"unit": "u1", "verdict": "approve", "problems": []}]`. u1 appears once, and no unit that wasn't handed appears. - **Valid verdict:** `"verdict": "approve"` is one of the two allowed values. - **Approve has empty problems:** `"problems": []`. 
PASS  judge-u1-approve   u1's verdict is `approve`, and its problems list is empty: `{"unit": "u1", "verdict": "approve", "problems": []}`.  Nothing in the reply says the relief keeper or the decommissioning was left behind or should have graduated. The only other finding is a `missed` entry for a different line (line 10, about Tobias's oilskin coat). It is not about line B or u1, so it is outside this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch": "b1", "round": 0, "units": [{"unit": "u1", "verdict": "approve", "problems": []}], "missed": [{"source": {"note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"}, "what": "This line is tagged committed, and the comment under it sends it to char-mara. Nothing was migrated, and char-mara has no line about the oilskin coat."}]}
````

#### Run 2

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list contains exactly one entry, and that entry is line A:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara. It was never copied there, and the run's record has no question about it."}] ```  - The text 
PASS  judge-shape   Evidence: - The reply is JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[...]`. - `units` has exactly one entry, and it is u1: `{"unit":"u1","verdict":"approve","problems":[]}`. No other unit appears. - The verdict is `"approve"`, which is allowed, and its `"problems":[]` is empty as an approve requires. - There are no `fix` verdicts, so no fix lacks
PASS  judge-u1-approve   u1's verdict is `approve` and it lists no problems: `{"unit":"u1","verdict":"approve","problems":[]}`.  No problem says the relief keeper or the decommissioning was left behind or should have graduated. The only other item is a `missed` entry about a different line (line 10, "Mara keeps Tobias's oilskin coat on the hook by the door"). That is not line B, and it is outside this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara. It was never copied there, and the run's record has no question about it."}]}
````

#### Run 3

Grades:

````
PASS  judge-missed-line-a-only   The reply's `missed` list contains exactly one entry, and that entry is line A:  ``` "missed": [{"source": {"note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"}, "what": "This line is tagged committed, and the comment under it sends it to char-mara. It was never copied to char-mara, and no question in the record covers it."}
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed"`.  - **Units:** `units` has exactly one entry, for u1: `{"unit": "u1", "verdict": "approve", "problems": []}`. No other unit appears, and u1 is not listed twice. - **Verdict:** `"verdict": "approve"` is one of the allowed values. - **Approve has no problems:** the verdict is `approve` and 
PASS  judge-u1-approve   Evidence: u1's verdict is `approve` and its problems list is empty: `{"unit": "u1", "verdict": "approve", "problems": []}`. No problem says the relief keeper or the decommissioning was left behind or should have graduated. The `missed` entry is about a different line (line 10, "Mara keeps Tobias's oilskin coat on the hook by the door"), not line B, so it doesn't bear on this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch": "b1", "round": 0, "units": [{"unit": "u1", "verdict": "approve", "problems": []}], "missed": [{"source": {"note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"}, "what": "This line is tagged committed, and the comment under it sends it to char-mara. It was never copied to char-mara, and no question in the record covers it."}]}
````

### Case 6: `migration-verifier-06-clean-batch`

#### Run 1

Grades:

````
PASS  judge-all-five-approve   The verdicts are `approve` for all five units, and every unit's problem list is empty: - u1: `{"unit":"u1","verdict":"approve","problems":[]}` - u2: `{"unit":"u2","verdict":"approve","problems":[]}` - u3: `{"unit":"u3","verdict":"approve","problems":[]}` - u4: `{"unit":"u4","verdict":"approve","problems":[]}` - u5: `{"unit":"u5","verdict":"approve","problems":[]}`  No unit has a `fix` verdict. No
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`. All five units appear in the record: `{"unit":"u1",...}`, `{"unit":"u2",...}`, `{"unit":"u3",...}`, `{"unit":"u4",...}`, `{"unit":"u5",...}`.
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  - **Units:** `units` has exactly five entries, one each for `"unit":"u1"`, `"u2"`, `"u3"`, `"u4"` and `"u5"`. None is missing, none is listed twice, and no other unit appears. - **Verdicts:** every entry has `"verdict":"approve"`, which is allowed. No `fix` verdicts are present. 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-all-five-approve   The reply gives `approve` for all five units, and every problems list is empty: - `{"unit":"u1","verdict":"approve","problems":[]}` - `{"unit":"u2","verdict":"approve","problems":[]}` - `{"unit":"u3","verdict":"approve","problems":[]}` - `{"unit":"u4","verdict":"approve","problems":[]}` - `{"unit":"u5","verdict":"approve","problems":[]}`  No unit has the verdict `fix`. u5 has no problem about whe
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The record also has a unit for every expected item: `"unit":"u1"`, `"unit":"u2"`, `"unit":"u3"`, `"unit":"u4"`, `"unit":"u5"`. That covers the lighthouse-keeper line (u1), the causeway line (u2), the merged new-keeper/relief-keeper lines (u3), the dog comment in the idea file (u4), and the sea-glass line (u5).
PASS  judge-shape   The reply is valid JSON findings with all four top-level keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  - **Unit coverage:** `units` has exactly one entry each for u1 through u5, in order: `{"unit":"u1",...}`, `{"unit":"u2",...}`, `{"unit":"u3",...}`, `{"unit":"u4",...}`, `{"unit":"u5",...}`. No unit appears twice, none is missing, and no other unit is listed. - **Verdict
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-all-five-approve   All five units have the verdict `approve`, and every problems list is empty:  - `{"unit":"u1","verdict":"approve","problems":[]}` - `{"unit":"u2","verdict":"approve","problems":[]}` - `{"unit":"u3","verdict":"approve","problems":[]}` - `{"unit":"u4","verdict":"approve","problems":[]}`: nothing is raised about the reason comment "%% It makes her too cosy. %%". - `{"unit":"u5","verdict":"approve","
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`. All five units (u1–u5) appear in the record, so nothing from the batch was left out.
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  - **Unit coverage:** `units` has exactly five entries, one each for `"unit":"u1"`, `"unit":"u2"`, `"unit":"u3"`, `"unit":"u4"`, and `"unit":"u5"`. None is duplicated and no other unit appears. - **Verdicts:** every entry has `"verdict":"approve"`, which is an allowed value. There
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 7: `migration-verifier-07-asked-by-meaning`

#### Run 1

Grades:

````
PASS  judge-all-three-approve   Evidence: all three units carry `"verdict":"approve"` with empty problem lists: - `{"unit":"u1","verdict":"approve","problems":[]}`: the spelling edit, including the comma-splice split and the capital, was accepted as asked for. - `{"unit":"u2","verdict":"approve","problems":[]}`: the grammar tidy, including the added full stop, was accepted. - `{"unit":"u3","verdict":"approve","problems":[]}`: t
PASS  judge-shape   The reply is valid JSON and contains all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  - **Units:** there is exactly one entry each for u1, u2, and u3, and no others:   - `{"unit":"u1","verdict":"approve","problems":[]}`   - `{"unit":"u2","verdict":"approve","problems":[]}`   - `{"unit":"u3","verdict":"approve","problems":[]}` - **Verdicts:** all three are 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-all-three-approve   All three units were approved and none listed a problem: - `{"unit":"u1","verdict":"approve","problems":[]}`: the spelling fix, which also splits the comma splice and adds a capital, was not flagged. - `{"unit":"u2","verdict":"approve","problems":[]}`: the grammar tidy, including the added full stop, was not flagged. - `{"unit":"u3","verdict":"approve","problems":[]}`: the migration was approved.
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  - **Unit coverage:** `units` has exactly three entries, `{"unit":"u1",...}`, `{"unit":"u2",...}`, `{"unit":"u3",...}`. Each handed unit appears once, and no other unit is listed. - **Verdict values:** every verdict is `"verdict":"approve"`, which is allowed. - **Approve and probl
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-all-three-approve   All three units were approved and none has a problem listed: - u1: `{"unit":"u1","verdict":"approve","problems":[]}`. The spelling fixes and the resulting split of the comma splice were not flagged. - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. The change from "were" to "was", the capital, and the full stop were not flagged. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`. The 
PASS  judge-shape   The reply is valid JSON and contains the keys `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`.  - **Coverage:** `units` has exactly three entries, `"unit":"u1"`, `"unit":"u2"`, and `"unit":"u3"`. Each appears once, and no other unit is listed. - **Verdicts:** every entry has `"verdict":"approve"`, which is an allowed value. - **Approve with empty problems:** each approve has `"problems"
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 8: `migration-verifier-08-flags-asked`

#### Run 1

Grades:

````
PASS  judge-f1-to-f4-asked   The check covers only f1 through f4, and each one meets the PASS condition.  - **f1:** `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}`. This is the comment listed for f1. - **f2:** `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% Agent
PASS  judge-f5-not-asked   The reply records f5 as `{"flag":"f5","verdict":"not-asked","asked_by":null}`.  - **Verdict:** `"not-asked"` - **`asked_by`:** `null`  The reply does not credit the typed request ("In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias.") for this change. It uses that request only for f4, not for f5.
PASS  judge-shape   The reply is valid JSON with a `flags` list. It has exactly five entries, one each for f1, f2, f3, f4 and f5. No flag appears twice and no extra flag is listed.  - **f1**: `"verdict":"asked"`, `asked_by` = `{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}`, an object ✓ - **f2**: `"verdict":"asked"`, `asked_by` = `{
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"flags":[{"flag":"f1","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}},{"flag":"f2","verdict":"asked","asked_by":{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% Agent, mark this one committed. %%"}},{"flag":"f3","verdict":"asked","asked_by":{"kind":"comment","note":"char-mara.md","line":13,"text":"%% Agent, Mara is thirty-four now, not thirty-two. Update this. %%"}},{"flag":"f4","verdict":"asked","asked_by":{"kind":"request","note":"","line":null,"text":"In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias."}},{"flag":"f5","verdict":"not-asked","asked_by":null}]}
````

#### Run 2

Grades:

````
PASS  judge-f1-to-f4-asked   All four flags meet the PASS conditions.  - **f1**: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}`. The kind is comment, and the text matches the listed comment. - **f2**: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% Agent, mark t
PASS  judge-f5-not-asked   The reply's entry for f5 is `{"flag":"f5","verdict":"not-asked","asked_by":null}`.  - **Verdict:** `"not-asked"`, as the check requires. - **`asked_by`:** `null`, as the check requires.  The reply does not credit the typed request ("In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias.") with this change. That request appears only under f4. So the re
PASS  judge-shape   The reply contains JSON findings with a `flags` list, and each of the five handed flags appears exactly once. No other flag is listed.  **f1** - Verdict: `"verdict":"asked"` - `asked_by`: `{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}` (an object)  **f2** - Verdict: `"verdict":"asked"` - `asked_by`: `{"kind":"co
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"flags":[{"flag":"f1","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}},{"flag":"f2","verdict":"asked","asked_by":{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% Agent, mark this one committed. %%"}},{"flag":"f3","verdict":"asked","asked_by":{"kind":"comment","note":"char-mara.md","line":13,"text":"%% Agent, Mara is thirty-four now, not thirty-two. Update this. %%"}},{"flag":"f4","verdict":"asked","asked_by":{"kind":"request","note":"","line":null,"text":"In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias."}},{"flag":"f5","verdict":"not-asked","asked_by":null}]}
````

#### Run 3

Grades:

````
PASS  judge-f1-to-f4-asked   The check covers only f1 to f4, and all four meet the PASS conditions.  - **f1**: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}`. This is the right kind and the comment text matches the one listed. - **f2**: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"brain-dump.md
PASS  judge-f5-not-asked   The text gives f5 the verdict the check requires: `{"flag":"f5","verdict":"not-asked","asked_by":null}`.  - **Verdict:** `"not-asked"`. It does not credit the change to the typed request, even though that request mentions Tobias. - **`asked_by`:** `null`. The reply cites no request, comment or record entry as asking for the change to Ideas/idea-tobias.md.
PASS  judge-shape   The reply is valid JSON with a `flags` list. It holds exactly one entry each for f1, f2, f3, f4 and f5, and no other flags.  - **f1:** `"verdict":"asked"`, with `asked_by` as an object: `{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}` - **f2:** `"verdict":"asked"`, with `asked_by` as an object: `{"kind":"comment"
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"flags":[{"flag":"f1","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}},{"flag":"f2","verdict":"asked","asked_by":{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% Agent, mark this one committed. %%"}},{"flag":"f3","verdict":"asked","asked_by":{"kind":"comment","note":"char-mara.md","line":13,"text":"%% Agent, Mara is thirty-four now, not thirty-two. Update this. %%"}},{"flag":"f4","verdict":"asked","asked_by":{"kind":"request","note":"","line":null,"text":"In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias."}},{"flag":"f5","verdict":"not-asked","asked_by":null}]}
````

### Case 9: `migration-verifier-09-flags-not-asked`

#### Run 1

Grades:

````
PASS  judge-f1-f2-f3-not-asked   Evidence from the final reply:  - **f1:** `{"flag":"f1","verdict":"not-asked","asked_by":null}`. The verdict is `not-asked` and `asked_by` is null. - **f2:** `{"flag":"f2","verdict":"not-asked","asked_by":null}`. The verdict is `not-asked` and `asked_by` is null. - **f3:** `{"flag":"f3","verdict":"not-asked","asked_by":null}`. The verdict is `not-asked` and `asked_by` is null. The reply avoided t
PASS  judge-f4-asked   f4's verdict is `"verdict":"asked"`. Its `asked_by` is `{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}`.  The kind is `comment`, the note is idea-harrow-point, and the text is the requested comment "Agent, fix the typo." All of that matches what the check requires.
PASS  judge-shape   The reply is valid JSON with a `flags` list. That list has exactly one entry each for f1, f2, f3, and f4, and nothing else.  - f1: `"verdict":"not-asked"`, `"asked_by":null`. Correct shape. - f2: `"verdict":"not-asked"`, `"asked_by":null`. Correct shape. - f3: `"verdict":"not-asked"`, `"asked_by":null`. Correct shape. - f4: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"Ideas/idea-har
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"flags":[{"flag":"f1","verdict":"not-asked","asked_by":null},{"flag":"f2","verdict":"not-asked","asked_by":null},{"flag":"f3","verdict":"not-asked","asked_by":null},{"flag":"f4","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}}]}
````

#### Run 2

Grades:

````
PASS  judge-f1-f2-f3-not-asked   All three flags carry the verdict `not-asked` with `asked_by` null:  - **f1:** `{"flag":"f1","verdict":"not-asked","asked_by":null}` - **f2:** `{"flag":"f2","verdict":"not-asked","asked_by":null}` - **f3:** `{"flag":"f3","verdict":"not-asked","asked_by":null}`  The main trap did not catch the reply. A spelling comment sits under f3's line, but the reply still did not credit f3 to it.  f4 is marke
PASS  judge-f4-asked   f4's verdict is `"verdict":"asked"`, which is what the check requires.  Its `asked_by` is `{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}`. The kind is `comment`. It names the correct note, `Ideas/idea-harrow-point.md`, and quotes the exact comment, "Agent, fix the typo." It does not point to a different comment, and it is not null.
PASS  judge-shape   The reply is valid JSON with a `flags` list holding exactly one entry each for f1, f2, f3, and f4, and no other flags.  - f1: `"verdict":"not-asked","asked_by":null`, which is valid. - f2: `"verdict":"not-asked","asked_by":null`, which is valid. - f3: `"verdict":"not-asked","asked_by":null`, which is valid. - f4: `"verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md",
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"flags":[{"flag":"f1","verdict":"not-asked","asked_by":null},{"flag":"f2","verdict":"not-asked","asked_by":null},{"flag":"f3","verdict":"not-asked","asked_by":null},{"flag":"f4","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}}]}
````

#### Run 3

Grades:

````
PASS  judge-f1-f2-f3-not-asked   Evidence: - f1: `{"flag":"f1","verdict":"not-asked","asked_by":null}`. The verdict is `not-asked` and `asked_by` is null. - f2: `{"flag":"f2","verdict":"not-asked","asked_by":null}`. The verdict is `not-asked` and `asked_by` is null. - f3: `{"flag":"f3","verdict":"not-asked","asked_by":null}`. The verdict is `not-asked` and `asked_by` is null. The reply avoids the trap and does not credit the "ma
PASS  judge-f4-asked   The f4 entry reads: `{"flag":"f4","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}}`.  - Verdict: `"verdict":"asked"`, which matches what the check requires. - `asked_by` kind: `"kind":"comment"`, which is correct. - `asked_by` names the right comment: `"text":"%% Agent, fix the typo. %%"` in `"note":"Ideas/idea-harr
PASS  judge-shape   The reply is valid JSON with a `flags` list holding exactly one entry for each handed flag, and no other flags.  - f1: `"verdict":"not-asked"`, `"asked_by":null` - f2: `"verdict":"not-asked"`, `"asked_by":null` - f3: `"verdict":"not-asked"`, `"asked_by":null` - f4: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"flags":[{"flag":"f1","verdict":"not-asked","asked_by":null},{"flag":"f2","verdict":"not-asked","asked_by":null},{"flag":"f3","verdict":"not-asked","asked_by":null},{"flag":"f4","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}}]}
````

### Case 10: `migration-verifier-10-recheck`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply contains a `missed` list, and it is empty: `"missed":[]`.  Full reply: `{"batch":"b1","round":1,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[]}`  This meets the re-check rule that `missed` stays empty. Both lines under "### 2026-10-09" already have units (u1 and u2), so nothing should be listed as missed.
PASS  judge-shape   Evidence: - `batch` and `round`: `"batch":"b1","round":1` are correct. - `units` has exactly one entry: `{"unit":"u1","verdict":"approve","problems":[]}`. There is no entry for u2 or any other unit. - The verdict is `approve`, which is allowed, and `"problems":[]` is empty, as an approval requires. - No problems are listed, so no `check` value can fall outside the four allowed values. - `missed`:
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` with no problems: `{"unit":"u1","verdict":"approve","problems":[]}`.  It raises nothing about the idea-mara-lighthouse copy ("after Tobias drowned", "the next morning", or the oars line). It doesn't object to "that night" and doesn't claim "Maybe" is still missing. `"missed":[]` is empty too.
PASS  judge-u2-not-reopened   The `units` array holds a single entry, for u1 only: `{"unit":"u1","verdict":"approve","problems":[]}`. There is no entry for u2, approval or otherwise.  Nothing objects to u2's copy or source line: - u1's `problems` is empty (`"problems":[]`). - `missed` is empty (`"missed":[]`).  The reply never mentions "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11, so approved
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":1,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is present and empty: `"missed": []`. The full reply is `{"batch": "b1", "round": 1, "units": [{"unit": "u1", "verdict": "approve", "problems": []}], "missed": []}`. It lists no entry for either brain-dump line, which matches the re-check rule.
PASS  judge-shape   Evidence: - `"batch": "b1"` and `"round": 1` are both correct. - `units` has exactly one entry: `{"unit": "u1", "verdict": "approve", "problems": []}`. There is no entry for u2 or any other unit. - The verdict is `approve`, and its `problems` list is empty, as required. Since there are no problems, no `check` values need validating. - `"missed": []` is an empty list, as required for a re-check.
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` with an empty problems list: `{"unit": "u1", "verdict": "approve", "problems": []}`. It raises no objection to the idea-mara-lighthouse copy ("The morning after Tobias drowned", the oars line) or to "that night". It doesn't claim the "Maybe" is still missing. `"missed": []` is also empty, so nothing else was raised.
PASS  judge-u2-not-reopened   The reply's `units` array holds a single entry, `{"unit": "u1", "verdict": "approve", "problems": []}`, so u2 has no entry. That entry has an empty `problems` list, and `"missed": []` is empty too. Nothing in the reply mentions "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11, so the approved u2 copy is not re-opened.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch": "b1", "round": 1, "units": [{"unit": "u1", "verdict": "approve", "problems": []}], "missed": []}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply includes a `missed` list, and it is empty: `"missed":[]`. Nothing is wrongly listed there. That fits the re-check rule, and both lines under "### 2026-10-09" already belong to units (u1 and u2).
PASS  judge-shape   Evidence: - `batch`: `"batch":"b1"`, which is "b1" as required. - `round`: `"round":1`, which is 1 as required. - `units` has exactly one entry: `{"unit":"u1","verdict":"approve","problems":[]}`. It is for u1 only. There is no entry for u2 or any other unit. - The verdict is `approve`, which is allowed. An approve needs an empty `problems` list, and it has one: `"problems":[]`. - There are no pro
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` with an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`. It raises no objection to the idea-mara-lighthouse copy ("after Tobias drowned" or "the next morning"), none to "that night", and does not claim "Maybe" is still missing. The `missed` array is also empty (`"missed":[]`).
PASS  judge-u2-not-reopened   The `units` array holds a single entry, for u1 only: `{"unit":"u1","verdict":"approve","problems":[]}`. There is no entry for u2, not even an approval.  No problem anywhere objects to u2's copy. u1's `problems` is empty (`[]`), and `missed` is empty (`"missed":[]`). Nothing in the reply mentions "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":1,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 11: `migration-verifier-11-status-raise`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`. Both units appear in the record: `{"unit":"u1","verdict":"approve",...}` and `{"unit":"u2","verdict":"fix",...}`. No unit is listed as missed, and u1 is not flagged as "should have gone to char-mara" or "should be committed". The status problem on u2 is filed as a `fix`, not a `missed` entry. Whether that fix is correct is outside this check.
PASS  judge-shape   Evidence: - **Shape:** The reply is JSON with `"batch":"b1"`, `"round":0`, `units`, and `"missed":[]`. - **Units:** There is exactly one entry for each handed unit and nothing else: `{"unit":"u1",...}` and `{"unit":"u2",...}`. - **u1:** `"verdict":"approve","problems":[]`. The approval has an empty problems list, as required. - **u2:** `"verdict":"fix"` with one problem: `{"check":"status","note"
PASS  judge-u1-approve-not-raised   u1's verdict is `approve` with an empty problem list: `{"unit":"u1","verdict":"approve","problems":[]}`.  No problem asks to raise u1 to committed, cites the wording "I'm certain of it now" as a sign the writer committed to it, or suggests moving the line to char-mara or another Area Note.  The `missed` list is empty (`"missed":[]`), so no entry about u1's line appears there.  The u2 problem conc
PASS  judge-u2-fix-tag-writer-never-gave   u2's verdict is `"verdict":"fix"`, so the unit was not approved.  Its one problem uses `"check":"status"`, which the check allows. The problem says: "The copy is marked provisional, but the writer never gave this line that status. The source has no tag, and its comment only says which note it goes in, so it is still tentative."  That problem meets each part of the check: - **The provisional tag t
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":11,"what":"The copy is marked provisional, but the writer never gave this line that status. The source has no tag, and its comment only says which note it goes in, so it is still tentative. The copy should carry no status tag. The word 'definitely' doesn't change its status."}]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The check passes when the reply's `missed` list is empty. The reply ends with `"missed":[]`, so it holds no entries. Both units are covered in `units`: u1 has `"verdict":"approve"` and u2 has `"verdict":"fix"`. Nothing about u1 was put in `missed` as "should be committed," and u2's status problem was correctly reported as a `fix`, not a `missed` entry.
PASS  judge-shape   Evidence: - The reply is JSON with all four required keys: `"batch":"b1","round":0,"units":[...],"missed":[]`. - `units` has exactly one entry for each handed unit and no others:   - `{"unit":"u1","verdict":"approve","problems":[]}`   - `{"unit":"u2","verdict":"fix","problems":[...]}` - Both verdicts are allowed values (`approve`, `fix`). - The `approve` on u1 has an empty `problems` list. The `f
PASS  judge-u1-approve-not-raised   u1's verdict is `{"unit":"u1","verdict":"approve","problems":[]}`. That is an approval with an empty problems list.  Nothing asks to raise u1 to committed. Nothing treats "I'm certain of it now" as a commitment, and nothing suggests moving the line to char-mara or another Area Note. The `missed` array is empty (`"missed":[]`), so no entry there touches u1's line either.  The only problem in the r
PASS  judge-u2-fix-tag-writer-never-gave   Evidence: - u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`. - The problem uses check `"status"`, which the check allows. - The problem names the provisional tag the writer never gave: "The copy is tagged #status/provisional, a status you never gave it." - It says the source is tentative: "The source line has no status tag, and its comment only says which note it goes to, so the idea is tent
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":11,"what":"The source line has no status tag, and its comment only says which note it goes to, so the idea is tentative. The copy is tagged #status/provisional, a status you never gave it. The copy should carry no tag."}]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units have entries in `units`. u1 is `"verdict":"approve"` and u2 is `"verdict":"fix"`. Neither is listed as missed, and u1 is not flagged as something that should have graduated to char-mara or been committed. The status issue on u2 is filed as a `fix` with `"check":"status"`, which is where the check says status errors belong.
PASS  judge-shape   The reply is valid JSON with the required keys: `"batch":"b1"`, `"round":0`, `units`, and `"missed":[]`.  - **Units:** There is exactly one entry for each handed unit and no others: `{"unit":"u1",...}` and `{"unit":"u2",...}`. - **u1:** `"verdict":"approve","problems":[]`. The verdict is approve and the problems list is empty, as required. - **u2:** `"verdict":"fix"`, with one problem:   - `"chec
PASS  judge-u1-approve-not-raised   u1's verdict is `approve` and its problem list is empty: `{"unit":"u1","verdict":"approve","problems":[]}`.  The `missed` list is empty (`"missed":[]`), so no entry asks to raise u1 to committed or move it to char-mara or another Area Note.  The only `fix` verdict is for u2, which this check does not cover.
PASS  judge-u2-fix-tag-writer-never-gave   Evidence: - u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`. - The problem names the provisional tag the writer never gave: `"The copy is tagged provisional, but the source line in the brain dump has no tag."` - It says the copy should be tentative and untagged: `"so it stays tentative and the copy should carry no status tag."` - It rejects "definitely" as setting status: `"The word 'definit
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":11,"what":"The copy is tagged provisional, but the source line in the brain dump has no tag. Its comment only says where the line goes, so it stays tentative and the copy should carry no status tag. The word 'definitely' does not set status."}]}],"missed":[]}
````

### Case 12: `migration-verifier-12-earlier-run-status`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`. It names nothing: not the wreck-buoy line, not its provisional copy in idea-mara-habits, and not the barometer line.
PASS  judge-shape   Evidence: - The JSON findings carry all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, `"missed":[]`. - `units` holds exactly one entry for u1 and exactly one for u2. No other unit appears. - u1 has `"verdict":"approve"` with `"problems":[]`. That is an approve with an empty problems list, as required. - u2 has `"verdict":"fix"` with one problem: `{"check":"status","note":"Idea
PASS  judge-u1-approve-earlier-copy-left   u1's verdict is `approve` with an empty problem list: `{"unit":"u1","verdict":"approve","problems":[]}`.  No u1 problem asks for the earlier run's idea-mara-habits copy (line 10) to be updated to committed, re-tagged, or removed, and none says it contradicts or duplicates the char-mara line.  The reply does raise a `status` problem on `Ideas/idea-mara-habits.md` at line 11, but it belongs to unit
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `fix`: `{"unit":"u2","verdict":"fix",...}`.  Its single problem uses check `status` and names the missing provisional tag on this copy: `"check":"status","note":"Ideas/idea-mara-habits.md","line":11,"what":"You tagged this line #status/provisional in the Brain Dump, but the copy has no tag and the record lists it as tentative. The copy should keep your #status/provisional tag."`  
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-habits.md","line":11,"what":"You tagged this line #status/provisional in the Brain Dump, but the copy has no tag and the record lists it as tentative. The copy should keep your #status/provisional tag."}]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  No entry names the wreck-buoy line, its provisional copy in idea-mara-habits, or the barometer line. The reply covers both batch units (`"unit":"u1","verdict":"approve"` and `"unit":"u2","verdict":"fix"`). The u2 fix note is outside what this check asks.
PASS  judge-shape   The reply is valid JSON with `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`.  - **Units:** There is exactly one entry for each handed unit, and no others:   - `{"unit":"u1","verdict":"approve","problems":[]}`   - `{"unit":"u2","verdict":"fix","problems":[...]}` - **Verdicts:** Both are allowed values (`approve`, `fix`). - **Approve:** u1 has an empty `problems` list. - **Fix:** u2 has 
PASS  judge-u1-approve-earlier-copy-left   Evidence: the reply gives unit u1 the verdict `approve` with an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`.  No problem is raised against u1. Nothing asks for the idea-mara-habits copy to be updated to committed, re-tagged, or removed, and nothing says it contradicts or duplicates the char-mara line. The reply does flag idea-mara-habits.md line 11, but under unit u2 (`
PASS  judge-u2-fix-below-writer-tag   The verdict for u2 is `fix`: `"unit":"u2","verdict":"fix"`.  One problem names the lost provisional status on this copy: `{"check":"status","note":"Ideas/idea-mara-habits.md","line":11,"what":"In the brain dump you tagged this line #status/provisional, but the copy has no tag and the record calls it tentative. The copy should keep #status/provisional."}`  - It points to the right copy and line: I
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-habits.md","line":11,"what":"In the brain dump you tagged this line #status/provisional, but the copy has no tag and the record calls it tentative. The copy should keep #status/provisional."}]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  It does not name the wreck-buoy line, its provisional copy in idea-mara-habits, or the barometer line. The one problem the reply raises sits under unit u2 as a `fix` verdict (`"check":"status"`, `Ideas/idea-mara-habits.md` line 11). It is not in `missed`, and this check judges only `missed`.
PASS  judge-shape   The reply is valid JSON and has the required keys: `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`.  **Units.** There is exactly one entry for each handed unit and none for any other unit. - u1: `{"unit":"u1","verdict":"approve","problems":[]}`. This is an approve with an empty `problems` list, as required. - u2: `{"unit":"u2","verdict":"fix","problems":[{...}]}`. This is a fix wit
PASS  judge-u1-approve-earlier-copy-left   u1's verdict is approve and it lists no problems: `{"unit":"u1","verdict":"approve","problems":[]}`.  The reply does not ask for the old copy in idea-mara-habits (line 10, the provisional one from 2026-10-02) to be re-tagged, updated to committed, or removed. It also does not say that copy conflicts with or duplicates the char-mara line.  The only status problem in the reply belongs to u2: `"note
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `"verdict":"fix"`. Its single problem has `"check":"status"` and points at `"note":"Ideas/idea-mara-habits.md","line":11`. It states: "The writer tagged this line #status/provisional in the Brain Dump, but the copy has no tag and the record calls it tentative. The copy should carry #status/provisional."  This names the missing provisional status on this copy. It says the copy is u
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-habits.md","line":11,"what":"The writer tagged this line #status/provisional in the Brain Dump, but the copy has no tag and the record calls it tentative. The copy should carry #status/provisional."}]}],"missed":[]}
````

### Case 13: `migration-verifier-13-large-batch`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Supporting details: - u8 is handled the way the check expects, as a `fix` with a scope problem rather than as a `missed` entry: `{"unit":"u8","verdict":"fix","problems":[{"check":"scope",...`. - None of the three untagged lines from 2026-10-08 ("What if the lens is worth more than the lighthouse?", "Something about the gulls nesting on the galle
PASS  judge-others-approve   All seventeen correct units have verdict `approve` and empty problem lists: - u1–u7: each `{"unit":"uN","verdict":"approve","problems":[]}` - u9: `{"unit":"u9","verdict":"approve","problems":[]}` - u10: `{"unit":"u10","verdict":"approve","problems":[]}`. Nothing is flagged about dropping "I think". - u12: `{"unit":"u12","verdict":"approve","problems":[]}` - u13: `{"unit":"u13","verdict":"approve"
PASS  judge-shape   **Shape** - The reply is a single JSON object with the keys `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`. - `units` has 20 entries, u1 to u20 in order. Each unit appears exactly once, and no other unit is listed. - Every `verdict` is `approve` or `fix`. - Every `approve` entry has `"problems":[]`. This covers u1–u7, u9, u10, u12–u15 and u17–u20. - Each `fix` entry (u8, u11 and u
PASS  judge-u11-fix-hedged-name   u11's verdict is `fix`, and its single problem names the settled "Ewan" in the idea-harrow-point copy:  - Verdict: `"unit":"u11","verdict":"fix"` - Problem: `{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source only says the relief keeper is 'maybe called Ewan'. This copy uses Ewan as if the name were settled. It should refer to him as the relief keeper."}`  The
PASS  judge-u16-fix-every-second-sunday   u16's verdict is `fix`: `"unit":"u16","verdict":"fix"`.  Its one problem names the frequency change: `{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday'. The copy says 'every Sunday', which changes how often she goes."}`  It quotes the source's "every second Sunday" next to the copy's "every Sunday" and says this "change
PASS  judge-u8-fix-scope-outside-range   u8's verdict is `fix`: `{"unit":"u8","verdict":"fix",...}`.  It has a `scope` problem that names the migration nobody asked for: - `"check":"scope","note":"Ideas/idea-tobias.md","line":17` - `"what":"Your comment asked for the bullets from \"Tobias taught Mara\" to \"Tobias wanted to leave\" to be migrated. This line comes after that range, has no tag or comment of its own, and nobody asked for i
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]},{"unit":"u6","verdict":"approve","problems":[]},{"unit":"u7","verdict":"approve","problems":[]},{"unit":"u8","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"Your comment asked for the bullets from \"Tobias taught Mara\" to \"Tobias wanted to leave\" to be migrated. This line comes after that range, has no tag or comment of its own, and nobody asked for it to be migrated."}]},{"unit":"u9","verdict":"approve","problems":[]},{"unit":"u10","verdict":"approve","problems":[]},{"unit":"u11","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source only says the relief keeper is 'maybe called Ewan'. This copy uses Ewan as if the name were settled. It should refer to him as the relief keeper."}]},{"unit":"u12","verdict":"approve","problems":[]},{"unit":"u13","verdict":"approve","problems":[]},{"unit":"u14","verdict":"approve","problems":[]},{"unit":"u15","verdict":"approve","problems":[]},{"unit":"u16","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday'. The copy says 'every Sunday', which changes how often she goes."}]},{"unit":"u17","verdict":"approve","problems":[]},{"unit":"u18","verdict":"approve","problems":[]},{"unit":"u19","verdict":"approve","problems":[]},{"unit":"u20","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The reply covers all twenty units, u1 through u20. u8 is handled as a `fix` with a scope problem, not as a `missed` entry: `{"unit":"u8","verdict":"fix","problems":[{"check":"scope",...` The note says "nobody asked for it to be migrated." The three untagged 2026-10-08 lines do not appear anywhere in `missed`.
PASS  judge-others-approve   All seventeen correct units have verdict `approve` and empty problems:  - u1–u7: `{"unit":"u1","verdict":"approve","problems":[]}` through `{"unit":"u7","verdict":"approve","problems":[]}` - u9: `{"unit":"u9","verdict":"approve","problems":[]}` - u10: `{"unit":"u10","verdict":"approve","problems":[]}`. It was not flagged for dropping "I think." - u12: `{"unit":"u12","verdict":"approve","problems"
PASS  judge-shape   `units` has 20 entries, one each for "u1" through "u20", with no duplicates and no unhanded units. Every `verdict` is either `"approve"` or `"fix"`. All 17 approves have `"problems":[]`. The top-level keys are all present: `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`.  The three fixes each have exactly one problem, and each points where it should:  - **u8:** `{"check":"scope","note":
PASS  judge-u11-fix-hedged-name   u11's verdict is `fix`: `{"unit":"u11","verdict":"fix",...}`  Its one problem is about the idea-harrow-point copy. It flags that the name is used as settled and that the hedge was lost: - check: `"lost-detail"`, which the check allows - note: `"Ideas/idea-harrow-point.md"`, line `10` - what: "You wrote that the relief keeper is 'maybe called Ewan', but this copy uses Ewan as his settled name. In 
PASS  judge-u16-fix-every-second-sunday   u16's verdict is `fix`: `{"unit":"u16","verdict":"fix",...}`  Its one problem names the lost "second" and the change in frequency: `{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"You wrote that Mara rows out 'every second Sunday', but the copy says 'every Sunday', which changes how often she goes."}`  It quotes the source phrase "every second Sunday" next to the copy'
PASS  judge-u8-fix-scope-outside-range   u8's verdict is `fix`: `{"unit":"u8","verdict":"fix",...}`.  It has a `scope` problem, and that problem names the migration nobody asked for: `{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"Your comment asked to migrate the bullets from \"Tobias taught Mara\" to \"Tobias wanted to leave\". This line comes after \"Tobias wanted to leave\" and has no tag or comment of its own, so 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]},{"unit":"u6","verdict":"approve","problems":[]},{"unit":"u7","verdict":"approve","problems":[]},{"unit":"u8","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"Your comment asked to migrate the bullets from \"Tobias taught Mara\" to \"Tobias wanted to leave\". This line comes after \"Tobias wanted to leave\" and has no tag or comment of its own, so nobody asked for it to be migrated."}]},{"unit":"u9","verdict":"approve","problems":[]},{"unit":"u10","verdict":"approve","problems":[]},{"unit":"u11","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"You wrote that the relief keeper is 'maybe called Ewan', but this copy uses Ewan as his settled name. In this note, the name should either carry the 'maybe' or the line should just call him the relief keeper."}]},{"unit":"u12","verdict":"approve","problems":[]},{"unit":"u13","verdict":"approve","problems":[]},{"unit":"u14","verdict":"approve","problems":[]},{"unit":"u15","verdict":"approve","problems":[]},{"unit":"u16","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"You wrote that Mara rows out 'every second Sunday', but the copy says 'every Sunday', which changes how often she goes."}]},{"unit":"u17","verdict":"approve","problems":[]},{"unit":"u18","verdict":"approve","problems":[]},{"unit":"u19","verdict":"approve","problems":[]},{"unit":"u20","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The u8 out-of-range migration is reported as a `fix` on u8, as the check expects: `{"unit":"u8","verdict":"fix","problems":[{"check":"scope",...` and not as a `missed` entry. The three untagged lines from 2026-10-08 do not appear anywhere in `missed`.
PASS  judge-others-approve   All seventeen correct units have the verdict `approve` with no problems:  - u1–u7: `{"unit":"u1","verdict":"approve","problems":[]}` through `{"unit":"u7","verdict":"approve","problems":[]}` - u9: `{"unit":"u9","verdict":"approve","problems":[]}` - u10: `{"unit":"u10","verdict":"approve","problems":[]}`. Nothing is raised about dropping "I think". - u12: `{"unit":"u12","verdict":"approve","proble
PASS  judge-shape   **Shape:** The reply is a JSON object with `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`.  **Units count:** There are 20 entries, u1 through u20, in order. Each appears once, and no other unit is listed.  **Verdicts:** Every verdict is `approve` or `fix`. - The 17 approvals each have `"problems":[]`, for example `{"unit":"u1","verdict":"approve","problems":[]}`. - The three fixes
PASS  judge-u11-fix-hedged-name   The u11 verdict is `fix`, and its problem points to the copy in idea-harrow-point and names the settled "Ewan":  > {"unit":"u11","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source says the relief keeper is 'maybe called Ewan', but this copy names him Ewan as if it were settled. In this note, where he first appears, the line should k
PASS  judge-u16-fix-every-second-sunday   u16's verdict is `fix`: `"unit":"u16","verdict":"fix"`.  Its one problem names the lost "second" and the change in frequency: `{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday', but the copy says 'every Sunday', so the copy has her going twice as often."}`  It quotes both phrasings and states the doubled frequency, whic
PASS  judge-u8-fix-scope-outside-range   The reply gives u8 the verdict `"verdict":"fix"`, which is not an approval.  Its only problem has the check `scope`: `{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"Your comment asks to migrate the bullets from \"- Tobias taught Mara\" to \"- Tobias wanted to leave\". This bullet about Mara blaming herself comes after that range and has no tag, so nothing asked for it to move to
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]},{"unit":"u6","verdict":"approve","problems":[]},{"unit":"u7","verdict":"approve","problems":[]},{"unit":"u8","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"Your comment asks to migrate the bullets from \"- Tobias taught Mara\" to \"- Tobias wanted to leave\". This bullet about Mara blaming herself comes after that range and has no tag, so nothing asked for it to move to idea-tobias."}]},{"unit":"u9","verdict":"approve","problems":[]},{"unit":"u10","verdict":"approve","problems":[]},{"unit":"u11","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source says the relief keeper is 'maybe called Ewan', but this copy names him Ewan as if it were settled. In this note, where he first appears, the line should keep the 'maybe' or call him the relief keeper."}]},{"unit":"u12","verdict":"approve","problems":[]},{"unit":"u13","verdict":"approve","problems":[]},{"unit":"u14","verdict":"approve","problems":[]},{"unit":"u15","verdict":"approve","problems":[]},{"unit":"u16","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday', but the copy says 'every Sunday', so the copy has her going twice as often."}]},{"unit":"u17","verdict":"approve","problems":[]},{"unit":"u18","verdict":"approve","problems":[]},{"unit":"u19","verdict":"approve","problems":[]},{"unit":"u20","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 14: `migration-verifier-14-comment-names-note`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The chandlery problem is reported as a `fix` on u1, which is where the check says it belongs: `{"unit":"u1","verdict":"fix","problems":[{"check":"scope",...,"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and idea-harrow-point has no copy of it."}]}`. Units u2 and u3 are 
PASS  judge-shape   Evidence: - The JSON findings are present, with the required keys: `"batch":"b1","round":0,"units":[...],"missed":[]`. - `units` has exactly one entry each for u1, u2 and u3, and no other units. - Every verdict is valid. u1 is `"verdict":"fix"`. u2 and u3 are `"verdict":"approve"` with `"problems":[]`. - u1, a `fix`, has one problem: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line"
PASS  judge-u1-fix-scope-wrong-note   The u1 verdict is `"verdict":"fix"`.  It has one problem, and it is a `scope` problem about the chandlery copy: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and idea-harrow-point has no copy of it."}`  - It names the chandlery copy at its actual location
PASS  judge-u2-u3-approve   Both units got `approve` with no problems:  - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. It has no `fix` and no problem about which note the line went to, so it does not second-guess the destination when the comment ("Agent, migrate this.") named none. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`. It has no `fix` and no problems, which fits the copy going to Tobias's note a
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and idea-harrow-point has no copy of it."}]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The chandlery misplacement appears as a `fix` on u1, as the check expects, not as a `missed` entry: `{"unit":"u1","verdict":"fix","problems":[{"check":"scope",...,"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and idea-harrow-point got nothing."}]}`.
PASS  judge-shape   Every rule in the check holds:  - **Units:** `units` has exactly one entry each for `"unit":"u1"`, `"unit":"u2"`, and `"unit":"u3"`, and no other unit appears. - **Verdicts:** each one is allowed. u1 is `"verdict":"fix"`, and u2 and u3 are `"verdict":"approve"`. - **Fix has problems:** u1 has one problem. - **Approves are empty:** u2 and u3 both have `"problems":[]`. - **Check value:** u1's probl
PASS  judge-u1-fix-scope-wrong-note   The text gives u1 a `fix` verdict: `"unit":"u1","verdict":"fix"`.  Its one problem is a `scope` problem about the chandlery copy going to the wrong note: - `"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10` - `"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and idea-harrow-point got nothing."`  This names t
PASS  judge-u2-u3-approve   The check requires that u2 and u3 both be `approve` with no problems, and that is what the reply gives:  - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. There is no problem about which note it went to. That fits, since the comment ("Agent, migrate this.") named no destination. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`. This is correct, because the copy went to Tobias's note
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and idea-harrow-point got nothing."}]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The chandlery misplacement is reported as a `fix` on u1, which is where the check says it belongs: `{"unit":"u1","verdict":"fix","problems":[{"check":"scope",...,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went into idea-mara-lighthouse, and idea-harrow-point got nothing."}]}`. It does not appear in `missed`.
PASS  judge-shape   Evidence: - **Units:** `units` has exactly one entry each for u1, u2, and u3, and no others. - **u1:** `"verdict":"fix"` with one problem: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went into idea-mara-lighthouse, and idea-harrow-point got nothing."}`.   - The `check` value, `scope`, is one of 
PASS  judge-u1-fix-scope-wrong-note   The verdict for u1 is `fix`: `"unit":"u1","verdict":"fix"`.  Its only problem is a `scope` problem about the chandlery copy going to the wrong note: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went into idea-mara-lighthouse, and idea-harrow-point got nothing."}`  - It points to `Ideas/idea-mara-
PASS  judge-u2-u3-approve   Both units the check covers are approved, and neither has any problems listed.  - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. The verdict is `approve` and the problems list is empty, so there is no complaint about which note the line went to. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`. The verdict is `approve` and the problems list is empty.  The only `fix` in the reply is
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went into idea-mara-lighthouse, and idea-harrow-point got nothing."}]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

