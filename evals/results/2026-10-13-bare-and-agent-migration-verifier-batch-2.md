# 2026-10-13 Bare and Agent Runs: Migration-verifier Batch 2

Cases 10 to 14, run three times bare and three times on the `script-asst:migration-verifier` agent. This is plan-migration-verifier.md 03, Milestone 3, its third step. A worker who never saw the agent file wrote the cases, and the writer approved their Pass lines first. Run by hand with `_tools/research-run.py --suite migration-verifier`, outside `claude plugin eval`.

## What Was Run

- **Date:** 2026-10-13, 17:44 to 17:58 EDT. The bare set and the agent set ran side by side, each at most five at a time.
- **Agent:** `agents/migration-verifier.md` as it passed batch 1, 163 lines, before the change for spec-migration-verifier.md 10 item 30.
- **Bare:** `claude-opus-5-5` with no agent, and with `--bare-append _fixtures/bare-shape-migration-verifier-batch.md`: batch 1's old answer-shape text after the prompt (plan-migration-verifier.md 05 item 8). The agent runs got the prompt alone.
- **Claude Code:** 2.1.296.
- **Commands:**

```bash
CASES="migration-verifier-10-recheck migration-verifier-11-status-raise migration-verifier-12-earlier-run-status \
  migration-verifier-13-large-batch migration-verifier-14-comment-names-note"
python3 _tools/research-run.py --suite migration-verifier --cases $CASES \
  --bare-append _fixtures/bare-shape-migration-verifier-batch.md --out <scratchpad>/mv-bare-2 --runs 3
python3 _tools/research-run.py --suite migration-verifier --cases $CASES \
  --agent script-asst:migration-verifier --out <scratchpad>/mv-agent-2 --runs 3
```

- **Errors and timeouts:** none. Every run exited 0. No run was repeated.
- **Cost:** bare $4.49 and agent $3.95 for the runs, from their streams. With judges, the runner printed $5.93 and $5.27.

## Summary Table

| Case | Agent | Bare | Agent cost | Bare cost |
| --- | --- | --- | --- | --- |
| 10 `migration-verifier-10-recheck` | 3 of 3 | 2 of 3 | $0.75 | $0.90 |
| 11 `migration-verifier-11-status-raise` | 3 of 3 | 2 of 3 | $0.69 | $0.78 |
| 12 `migration-verifier-12-earlier-run-status` | 3 of 3 | 1 of 3 | $0.72 | $0.92 |
| 13 `migration-verifier-13-large-batch` | 3 of 3 | 0 of 3 | $1.00 | $1.07 |
| 14 `migration-verifier-14-comment-names-note` | 3 of 3 | 2 of 3 | $0.79 | $0.82 |
| **Total** | **15 of 15** | **7 of 15** | **$3.95** | **$4.49** |

A run counts only when every grader passed.

## Code Checks

1. **Every agent reply is bare JSON that `runmanager findings` accepts:** `shape_problem` in `migration/findings.py`, with round 1 and unit u1 for case 10.
2. **Every bare reply is wrapped in a ```` ```json ```` fence,** all 15, though the added text says "Answer with JSON only." `runmanager findings` would refuse each one, which in a live run costs a retry. The judges read past the fence, so this isn't in the table.
3. **Tools:** Read, Glob, and Grep only, in both sets. No write.
4. **No agent run read the before-snapshot or `.runs/units/`.** The fixtures hold neither, so the agent file's rule against reading them is not tested by any case.

## Findings

1. **The agent passes every check of cases 10 to 14 in all 15 runs. Bare Claude passes 7 of 15.** Batch 2's plants tell the two apart, where batch 1's didn't.
2. **Case 10, bare run 1, re-opens the approved unit through `missed`.** Its `units` holds only u1, but its `missed` entry objects to u2's copy: "This line's unit (u2) isn't in this round's record because I approved it in round 0, but that approval was wrong." It fails the u2 judge, the `missed` judge, and the shape judge.
3. **Case 12, bare runs 1 and 3, fix u1 over the earlier run's copy.** Each raises a `status` problem on char-mara.md line 20 because an earlier run's copy in idea-mara-habits is provisional. Spec-migration-verifier.md 04.2 item 3 and 10 item 30 rule that copy out.
4. **Case 13, all three bare runs catch the three planted errors and approve the seventeen correct units,** but point u8's `scope` problem at `brain-dump.md` line 17, the source, not the copy. All three fail only the shape judge.
5. **Cases 11 and 14, one bare run each, fail only the shape judge for where a problem points.** Case 14 run 2 names `brain-dump.md` line 11 for the misplaced copy; case 11 run 2 names the wrong line for u2.
6. **The agent's every problem points at the bad text,** in all 15 runs.

## Full Outputs: Agent

Each run shows its grades, then its final reply.

### Case 1: `migration-verifier-10-recheck`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply includes a `missed` list, and it is empty: `"missed":[]`. Both lines under "### 2026-10-09" already have units (u1 and u2), so nothing should be listed. That matches the rule that a re-check never lists missed lines. The full reply is `{"batch":"b1","round":1,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[]}`.
PASS  judge-shape   Evidence: - `batch` is `"b1"` and `round` is `1`. Both are as required. - `units` has exactly one entry: `{"unit":"u1","verdict":"approve","problems":[]}`. It is for u1 only. There is no entry for u2 or any other unit. - The `verdict` is `"approve"`, which is a valid value. Its `problems` list is empty (`[]`), as an approve requires. - No problems are present, so there are no `check` values to va
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` with no problems:  `{"unit":"u1","verdict":"approve","problems":[]}`  The `problems` array is empty. So nothing objects to the idea-mara-lighthouse copy ("after Tobias drowned", "the next morning", the oars line). Nothing objects to "that night" in the idea-tobias copy. Nothing claims the "Maybe" is still missing. The verdict is not `fix`. The reply meets 
PASS  judge-u2-not-reopened   The `units` array has exactly one entry, for u1: `{"unit":"u1","verdict":"approve","problems":[]}`. There is no entry for u2, not even an approval.  No objection to u2 appears anywhere: - u1's problems list is empty: `"problems":[]`. - The missed list is empty: `"missed":[]`. - The reply has no other prose, so nothing mentions "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md
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
PASS  judge-missed-empty   The reply contains a `missed` list, and that list is empty: `"missed":[]`. The full reply is `{"batch":"b1","round":1,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[]}`. That matches the rule that a re-check reports no missed lines. Both 2026-10-09 lines already have units, u1 and u2, so there was nothing to report.
PASS  judge-shape   Evidence: - `batch` is right: `"batch":"b1"`. - `round` is 1: `"round":1`. - `units` has exactly one entry, for u1, and nothing for u2 or any other unit: `{"unit":"u1","verdict":"approve","problems":[]}`. - The verdict is `approve`, which is an allowed value, and its `problems` list is empty: `"problems":[]`. Since there are no problems, no `check` values need validating. - `missed` is empty: `"m
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` with an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`.  It raises no objection to the idea-mara-lighthouse copy ("The morning after Tobias drowned"). It also raises none to "that night" in the idea-tobias copy, and doesn't claim "Maybe" is still missing. The `missed` array is empty too (`"missed":[]`), so nothing new was raised.
PASS  judge-u2-not-reopened   The reply gives u2 no entry. `units` has a single entry, for u1 only: `{"unit":"u1","verdict":"approve","problems":[]}`.  No problem points at u2's copy. u1's `problems` is empty (`[]`), and `"missed":[]` is also empty. Nowhere does the reply mention "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":1,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is present and empty: `"missed": []`. The check passes when that list is empty, so the reply meets it.
PASS  judge-shape   Evidence: - The reply is JSON findings: `{"batch": "b1", "round": 1, "units": [...], "missed": []}`. - `batch` is `"b1"` and `round` is `1`, as required. - `units` has exactly one entry, `{"unit": "u1", "verdict": "approve", "problems": []}`. There is no entry for u2 or any other unit. - The `verdict` is `"approve"`, which is a valid value. It has an empty `problems` list (`"problems": []`), whic
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` and an empty problem list: `{"unit": "u1", "verdict": "approve", "problems": []}`. It raises nothing about the idea-mara-lighthouse copy ("after Tobias drowned", "the next morning", or the oars line). It doesn't object to "that night", and it doesn't say "Maybe" is still missing. That is the passing condition: `approve` with no problems.
PASS  judge-u2-not-reopened   The reply's `units` array holds a single entry, for u1 only: `{"unit": "u1", "verdict": "approve", "problems": []}`. There is no u2 entry, approval or otherwise.  No problem anywhere objects to u2's copy. u1's `problems` is empty (`[]`), and `"missed": []` is also empty. Nothing mentions "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch": "b1", "round": 1, "units": [{"unit": "u1", "verdict": "approve", "problems": []}], "missed": []}
````

### Case 2: `migration-verifier-11-status-raise`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units are covered in `units`: u1 is `"verdict":"approve"` and u2 is `"verdict":"fix"` with a status problem. The reply does not list u1 as something that should have gone to char-mara or been committed. It treats u2's status error as a `fix`, not a `missed` entry, which is what the check expects.
PASS  judge-shape   The reply is valid JSON findings with `"batch":"b1"`, `"round":0`, `units`, and `"missed":[]`.  - **Units:** There is exactly one entry for each handed unit, `"unit":"u1"` and `"unit":"u2"`. No other units appear. - **u1:** `"verdict":"approve","problems":[]`. The verdict is valid and the problems list is empty. - **u2:** `"verdict":"fix"` with one problem: `{"check":"status","note":"Ideas/idea-m
PASS  judge-u1-approve-not-raised   u1's entry reads `{"unit":"u1","verdict":"approve","problems":[]}`. The verdict is `approve` and the problems list is empty.  The `missed` list is `"missed":[]`, so it has no entry about u1's line. Nothing in the reply asks to raise u1 to committed, treats "I'm certain of it now" as a commitment, or says the line should move to char-mara or another Area Note.  The only problem in the reply belong
PASS  judge-u2-fix-tag-writer-never-gave   Evidence: - u2's verdict is `fix`: `{"unit":"u2","verdict":"fix",...}` - The problem uses check `"status"`, which is one of the two accepted values. - The problem names the provisional tag the writer never gave and says the copy should be untagged: "The source line has no status tag, and its comment only says which note it goes to, so the idea is still tentative. The copy adds #status/provisional
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":11,"what":"The source line has no status tag, and its comment only says which note it goes to, so the idea is still tentative. The copy adds #status/provisional, which raises it above what the writer gave; the copy should have no tag."}]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units have a verdict in the reply: u1 is `"verdict":"approve"` and u2 is `"verdict":"fix"`. u2's status problem appears as a `fix` (`"check":"status"`), not as a `missed` entry. Nothing claims u1 should have gone to char-mara or been committed.
PASS  judge-shape   The reply is valid JSON with `batch` ("b1"), `round` (0), `units`, and `missed` ([]).  - **Units:** there is exactly one entry each for u1 and u2, and no other units. - **u1:** `"verdict":"approve"` with `"problems":[]`. That is an approve with an empty problems list. - **u2:** `"verdict":"fix"` with one problem:   - `"check":"status"` is one of the four allowed checks.   - `"note":"Ideas/idea-ma
PASS  judge-u1-approve-not-raised   u1's verdict is `{"unit":"u1","verdict":"approve","problems":[]}`. It is approved with an empty problems list.  No problem asks to raise u1 to committed. None says its wording shows the writer committed, and none says it should graduate to char-mara or another Area Note. The `missed` array is empty (`"missed":[]`), so there is no such entry about u1's line either.  The only `fix` is for u2, which
PASS  judge-u2-fix-tag-writer-never-gave   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`.  The problem has `"check":"status"`, which the check allows. It names the provisional tag the writer never gave: "The source line has no status tag, so it is tentative by the Brain Dump's default... The copy is tagged #status/provisional, which raises it above what the writer gave."  It rejects "definitely" as a source of status: "The word 'de
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":11,"what":"The source line has no status tag, so it is tentative by the Brain Dump's default. The comment under it only says where the line goes. The copy is tagged #status/provisional, which raises it above what the writer gave. The word 'definitely' doesn't set status. The copy should carry no status tag."}]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The `missed` list is empty: `"missed":[]`. Both units appear in the record: u1 has the verdict `"approve"` and u2 has the verdict `"fix"`. The reply does not list either one as missed. u2's status problem is reported as a `fix` (`"check":"status"`) and not as a `missed` entry, which matches what the check expects.
PASS  judge-shape   Evidence: - The reply is JSON findings with all four keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, `"missed":[]`. - `units` has exactly two entries, one each for u1 and u2, and no other units. - u1: `{"unit":"u1","verdict":"approve","problems":[]}`. It is an approve with an empty problems list. - u2: `{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lightho
PASS  judge-u1-approve-not-raised   u1's verdict is `approve` with no problems: `{"unit":"u1","verdict":"approve","problems":[]}`.  No problem asks to raise u1 to committed, says the wording ("I'm certain of it now") shows commitment, or says the line should graduate to char-mara or another Area Note. The `missed` list is empty: `"missed":[]`.  The u2 `fix` entry is about a different unit, so it does not bear on this check.
PASS  judge-u2-fix-tag-writer-never-gave   Evidence: - u2's verdict is fix: `"unit":"u2","verdict":"fix"` - The problem's check is `"check":"status"`, which is one of the accepted values. - The problem names the provisional tag that the writer never gave: "The copy adds #status/provisional, a status you never gave it." - It finds the source tentative: "The source line has no status tag, and its comment only says where the line goes, so it
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":11,"what":"The source line has no status tag, and its comment only says where the line goes, so it is tentative. The copy adds #status/provisional, a status you never gave it. It should carry no tag."}]}],"missed":[]}
````

### Case 3: `migration-verifier-12-earlier-run-status`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The check asks only whether the reply's `missed` list is empty, and it is: `"missed": []`.  There is no entry naming the wreck-buoy line, its provisional copy in idea-mara-habits, or the barometer line. The reply accounts for both batch lines through units: `"unit": "u1", "verdict": "approve"` and `"unit": "u2", "verdict": "fix"`. Whether u2's status problem is correct is outside this check.
PASS  judge-shape   Evidence: - **Top-level shape:** The reply is JSON with all four required keys: `"batch": "b1"`, `"round": 0`, `"units": [...]` and `"missed": []`. - **Units handed:** `units` has exactly one entry for `"unit": "u1"` and one for `"unit": "u2"`. No other unit appears, and neither is listed twice. - **u1:** `"verdict": "approve"` with `"problems": []`. That is a valid verdict, and the approve has a
PASS  judge-u1-approve-earlier-copy-left   u1's verdict is `approve` with no problems. The reply reads:  ``` "unit": "u1", "verdict": "approve", "problems": [] ```  No problem anywhere in the reply says the earlier run's idea-mara-habits copy (line 10) should be updated to committed, re-tagged, or removed. None says it contradicts or duplicates the char-mara line. The only `fix` is for u2, a different unit, and it points at line 11 rather
PASS  judge-u2-fix-below-writer-tag   The u2 verdict is `"verdict": "fix"`, not approve.  Its one problem has `"check": "status"`, which the check allows. The problem names the lost provisional tag on this exact copy (`"note": "Ideas/idea-mara-habits.md"`, `"line": 11`):  > "You tagged this line #status/provisional in the brain dump, but the copy has no tag and the record calls it tentative. The copy should keep #status/provisional."
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{
  "batch": "b1",
  "round": 0,
  "units": [
    {
      "unit": "u1",
      "verdict": "approve",
      "problems": []
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-habits.md",
          "line": 11,
          "what": "You tagged this line #status/provisional in the brain dump, but the copy has no tag and the record calls it tentative. The copy should keep #status/provisional."
        }
      ]
    }
  ],
  "missed": []
}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  It names nothing as missed. The wreck-buoy line, its provisional copy in idea-mara-habits, and the barometer line are all absent from it. The u2 "fix" verdict about `Ideas/idea-mara-habits.md` line 11 sits in the `problems` list for unit u2, not in `missed`. It is outside this check.
PASS  judge-shape   Evidence: - The reply is JSON findings with `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`. - `units` has exactly one entry each for u1 and u2, and no other unit. - u1: `{"unit":"u1","verdict":"approve","problems":[]}`. This is an approve with an empty problems list. - u2: `{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-habits.md","line":11,...
PASS  judge-u1-approve-earlier-copy-left   u1 received `approve` with no problems: `{"unit":"u1","verdict":"approve","problems":[]}`.  No problem under u1 says the earlier run's provisional copy in idea-mara-habits should be updated to committed, re-tagged, or removed. None says it contradicts or duplicates the char-mara line.  The reply's only problem belongs to u2: `"note":"Ideas/idea-mara-habits.md","line":11`. It concerns a different 
PASS  judge-u2-fix-below-writer-tag   Evidence: - The verdict for u2 is `fix`: `{"unit":"u2","verdict":"fix",...}` - One problem names the missing provisional status on this copy, with `"check":"status"`, `"note":"Ideas/idea-mara-habits.md"`, `"line":11`. Its text: "You tagged this line #status/provisional, but the copy has no tag and the record calls it tentative. An untagged line in an Idea Note counts as tentative, so the copy sit
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-habits.md","line":11,"what":"You tagged this line #status/provisional, but the copy has no tag and the record calls it tentative. An untagged line in an Idea Note counts as tentative, so the copy sits below your status. It needs your #status/provisional tag."}]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The check asks only whether the reply's `missed` list is empty. The reply ends with:  `"missed":[]`  The list is empty. It does not name the wreck-buoy line, its provisional copy in idea-mara-habits, or the barometer line. The u2 "fix" verdict in `units` is outside this check's scope.
PASS  judge-shape   Evidence: - The reply is JSON with all four keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`. - `units` has exactly two entries, one for each unit handed: `{"unit":"u1",...}` and `{"unit":"u2",...}`. No unit is listed twice and no other unit appears. - u1: `"verdict":"approve","problems":[]`. The approve has an empty problems list. - u2: `"verdict":"fix"` with one problem, so
PASS  judge-u1-approve-earlier-copy-left   u1's verdict is `approve` and it has no problems: `{"unit":"u1","verdict":"approve","problems":[]}`.  The only `fix` verdict is for u2. Its problem is about line 11 of Ideas/idea-mara-habits.md: "You tagged this line provisional in the brain dump, but the copy has no tag and the record gives it as tentative." This check covers u1 only, and that problem does not mention u1's char-mara line or the 
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `fix`: `{"unit":"u2","verdict":"fix",...}`.  It has one problem, with check `status` on `Ideas/idea-mara-habits.md` line 11. The problem says: "You tagged this line provisional in the brain dump, but the copy has no tag and the record gives it as tentative. The copy should keep your #status/provisional tag."  That problem names the lost provisional status. It says the copy has no 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-habits.md","line":11,"what":"You tagged this line provisional in the brain dump, but the copy has no tag and the record gives it as tentative. The copy should keep your #status/provisional tag."}]}],"missed":[]}
````

### Case 4: `migration-verifier-13-large-batch`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All twenty units, u1 through u20, are listed in `units`. u8 shows up as a `fix` with a scope problem ("The line about Mara blaming herself comes after that range and has no tag, so nothing asked for it to be migrated"), not as a `missed` entry. That matches what the check expects. None of the three untagged 2026-10-08 lines appear in `missed`.
PASS  judge-others-approve   All seventeen correct units have the verdict `approve` with an empty problems list:  - u1 to u7: `{"unit":"u1","verdict":"approve","problems":[]}` through `{"unit":"u7","verdict":"approve","problems":[]}` - u9: `{"unit":"u9","verdict":"approve","problems":[]}` - u10: `{"unit":"u10","verdict":"approve","problems":[]}`. There is no problem about dropping "I think". - u12: `{"unit":"u12","verdict":"
PASS  judge-shape   Evidence:  - **`units` count:** there are 20 entries, u1 through u20, each listed once in order. No other unit appears. - **Verdicts:** every verdict is `approve` or `fix`. The three `fix` units are u8, u11 and u16. Every `approve` has `"problems":[]`. - **Each `fix` has at least one problem, and every `check` is allowed:**   - u8: `"check":"scope"`   - u11: `"check":"lost-detail"`   - u16: `"che
PASS  judge-u11-fix-hedged-name   u11's verdict is `fix`: `{"unit":"u11","verdict":"fix",...}`  Its one problem names the idea-harrow-point copy and says the name is stated as settled: - check: `"lost-detail"` (one of the two accepted checks) - note: `"Ideas/idea-harrow-point.md"`, line: `10` - what: `"The source says the relief keeper is 'maybe called Ewan'. This copy uses Ewan as if the name were settled. It should call him the
PASS  judge-u16-fix-every-second-sunday   u16's verdict is `fix`: `{"unit":"u16","verdict":"fix",...}`.  Its one problem names the changed frequency: `{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday'. The copy says 'every Sunday', which changes how often she goes."}`  This quotes the source "every second Sunday" next to the copy's "every Sunday" and says the c
PASS  judge-u8-fix-scope-outside-range   u8's verdict is `fix`: `{"unit":"u8","verdict":"fix",...}`  It has one problem, with `"check":"scope"`, pointing at `Ideas/idea-tobias.md` line 17: > "Your comment asked to migrate the bullets from \"- Tobias taught Mara\" to \"- Tobias wanted to leave\". The line about Mara blaming herself comes after that range and has no tag, so nothing asked for it to be migrated."  This names the migration t
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]},{"unit":"u6","verdict":"approve","problems":[]},{"unit":"u7","verdict":"approve","problems":[]},{"unit":"u8","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"Your comment asked to migrate the bullets from \"- Tobias taught Mara\" to \"- Tobias wanted to leave\". The line about Mara blaming herself comes after that range and has no tag, so nothing asked for it to be migrated."}]},{"unit":"u9","verdict":"approve","problems":[]},{"unit":"u10","verdict":"approve","problems":[]},{"unit":"u11","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source says the relief keeper is 'maybe called Ewan'. This copy uses Ewan as if the name were settled. It should call him the relief keeper, without the name."}]},{"unit":"u12","verdict":"approve","problems":[]},{"unit":"u13","verdict":"approve","problems":[]},{"unit":"u14","verdict":"approve","problems":[]},{"unit":"u15","verdict":"approve","problems":[]},{"unit":"u16","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday'. The copy says 'every Sunday', which changes how often she goes."}]},{"unit":"u17","verdict":"approve","problems":[]},{"unit":"u18","verdict":"approve","problems":[]},{"unit":"u19","verdict":"approve","problems":[]},{"unit":"u20","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The out-of-range bullet is treated as the check expects: u8 gets `"verdict":"fix"` with a scope problem, not a `missed` entry. The three untagged 2026-10-08 lines also do not appear in `missed`.
PASS  judge-others-approve   All seventeen correct units are `"verdict":"approve"` with `"problems":[]`:  - u1–u7: `{"unit":"u1","verdict":"approve","problems":[]}` through `{"unit":"u7","verdict":"approve","problems":[]}` - u9: `{"unit":"u9","verdict":"approve","problems":[]}`. There is no problem about which note it went to. - u10: `{"unit":"u10","verdict":"approve","problems":[]}`. There is no problem about dropping "I th
PASS  judge-shape   **Unit count:** `units` has 20 entries, one each for `"u1"` through `"u20"`, in order. No unit appears twice and none falls outside u1–u20. Top-level keys are `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`.  **Verdicts:** every entry is `"approve"` or `"fix"`. The fixes are u8, u11 and u16; the other 17 are approve.  **Problems lists:** each approve has `"problems":[]`, and each fix ha
PASS  judge-u11-fix-hedged-name   u11 has the verdict `"verdict":"fix"`. It lists one problem, and that problem targets the idea-harrow-point copy:  > `{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source says the relief keeper is 'maybe called Ewan'. This copy treats Ewan as his settled name. It should say 'maybe called Ewan' or just call him the relief keeper."}`  - The check is `lost-detail`,
PASS  judge-u16-fix-every-second-sunday   The u16 verdict is `fix`: `"unit":"u16","verdict":"fix"`.  Its one problem names the frequency change. It is `{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday', but the copy says 'every Sunday'. That changes how often she goes."}`. It quotes "every second Sunday" against "every Sunday" and says how often she goes has ch
PASS  judge-u8-fix-scope-outside-range   u8's verdict is `fix`, and its only problem has check `scope` and names the unasked migration as out of range:  - `"unit":"u8","verdict":"fix"` - `"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"The comment asks to migrate only the bullets from \"Tobias taught Mara\" to \"Tobias wanted to leave\". The bullet about Mara blaming herself comes after that range, and nothing asked for 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]},{"unit":"u6","verdict":"approve","problems":[]},{"unit":"u7","verdict":"approve","problems":[]},{"unit":"u8","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"The comment asks to migrate only the bullets from \"Tobias taught Mara\" to \"Tobias wanted to leave\". The bullet about Mara blaming herself comes after that range, and nothing asked for it to be migrated."}]},{"unit":"u9","verdict":"approve","problems":[]},{"unit":"u10","verdict":"approve","problems":[]},{"unit":"u11","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source says the relief keeper is 'maybe called Ewan'. This copy treats Ewan as his settled name. It should say 'maybe called Ewan' or just call him the relief keeper."}]},{"unit":"u12","verdict":"approve","problems":[]},{"unit":"u13","verdict":"approve","problems":[]},{"unit":"u14","verdict":"approve","problems":[]},{"unit":"u15","verdict":"approve","problems":[]},{"unit":"u16","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday', but the copy says 'every Sunday'. That changes how often she goes."}]},{"unit":"u17","verdict":"approve","problems":[]},{"unit":"u18","verdict":"approve","problems":[]},{"unit":"u19","verdict":"approve","problems":[]},{"unit":"u20","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  It covers all twenty units (u1–u20). It handles u8 as the check expects, as a `fix` with a scope note ("It has no tag and no comment of its own, so nothing asked for it to be migrated") rather than as a `missed` entry. The three untagged 2026-10-08 lines do not appear in `missed` either.
PASS  judge-others-approve   All seventeen correct units are `approve` with empty problem lists: - u1–u7: each `"verdict":"approve","problems":[]` (e.g. `{"unit":"u5","verdict":"approve","problems":[]}`). - u9: `{"unit":"u9","verdict":"approve","problems":[]}`. - u10: `{"unit":"u10","verdict":"approve","problems":[]}`, so there is no problem for dropping "I think". - u12: `{"unit":"u12","verdict":"approve","problems":[]}`. -
PASS  judge-shape   **Units:** 20 entries, u1 through u20, each appearing exactly once and no others.  **Verdicts:** Every verdict is `"approve"` or `"fix"`. The three `fix` entries (u8, u11, u16) each have one problem. All 17 `approve` entries have `"problems":[]`.  **Check values:** `"scope"` on u8 and `"lost-detail"` on u11 and u16. All are in the allowed set.  **Pointing:** - **u8:** `"note":"Ideas/idea-tobias.m
PASS  judge-u11-fix-hedged-name   u11's verdict is `fix`: `{"unit":"u11","verdict":"fix",...}`  Its single problem names the idea-harrow-point copy and says the hedge on the name was dropped: - `"check":"lost-detail"` - `"note":"Ideas/idea-harrow-point.md"` - `"line":10` - `"what":"The source says the relief keeper is 'maybe called Ewan', but this copy uses Ewan as his settled name. In this note the name has no hedge, so the line
PASS  judge-u16-fix-every-second-sunday   u16's verdict is `fix`: `{"unit":"u16","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday', but the copy says 'every Sunday', which changes how often she goes."}]}`  The problem names the frequency change directly. It contrasts "every second Sunday" in the source with "every Sunday" in the copy
PASS  judge-u8-fix-scope-outside-range   Evidence: u8's verdict is `fix`, and it has a `scope` problem that names the unasked migration.  - Verdict: `"unit":"u8","verdict":"fix"` - Problem: `{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"The comment asks to migrate the bullets from \"- Tobias taught Mara\" to \"- Tobias wanted to leave\", and this line comes after that range. It has no tag and no comment of its own, so
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]},{"unit":"u4","verdict":"approve","problems":[]},{"unit":"u5","verdict":"approve","problems":[]},{"unit":"u6","verdict":"approve","problems":[]},{"unit":"u7","verdict":"approve","problems":[]},{"unit":"u8","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-tobias.md","line":17,"what":"The comment asks to migrate the bullets from \"- Tobias taught Mara\" to \"- Tobias wanted to leave\", and this line comes after that range. It has no tag and no comment of its own, so nothing asked for it to be migrated."}]},{"unit":"u9","verdict":"approve","problems":[]},{"unit":"u10","verdict":"approve","problems":[]},{"unit":"u11","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-harrow-point.md","line":10,"what":"The source says the relief keeper is 'maybe called Ewan', but this copy uses Ewan as his settled name. In this note the name has no hedge, so the line should keep the hedge or refer to him only as the relief keeper."}]},{"unit":"u12","verdict":"approve","problems":[]},{"unit":"u13","verdict":"approve","problems":[]},{"unit":"u14","verdict":"approve","problems":[]},{"unit":"u15","verdict":"approve","problems":[]},{"unit":"u16","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-habits.md","line":10,"what":"The source says Mara rows out 'every second Sunday', but the copy says 'every Sunday', which changes how often she goes."}]},{"unit":"u17","verdict":"approve","problems":[]},{"unit":"u18","verdict":"approve","problems":[]},{"unit":"u19","verdict":"approve","problems":[]},{"unit":"u20","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 5: `migration-verifier-14-comment-names-note`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units are accounted for: `"unit":"u1","verdict":"fix"`, `"unit":"u2","verdict":"approve"`, and `"unit":"u3","verdict":"approve"`. The chandlery misrouting is handled as a `fix` on u1, as the check expects, not as a missed entry: "Your comment says the chandlery goes in idea-harrow-point, but the copy went into idea-mara-lighthouse inst
PASS  judge-shape   Evidence: - The reply is JSON findings with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, `"missed":[]`. - `units` has exactly one entry each for u1, u2, and u3, and no other units. - Every verdict is valid:   - u1 is `"verdict":"fix"` and has one problem.   - u2 and u3 are each `"verdict":"approve"` with `"problems":[]`. - The only problem's check, `"check":"scope"`, is o
PASS  judge-u1-fix-scope-wrong-note   The verdict for u1 is `fix`: `"unit":"u1","verdict":"fix"`.  It has one problem, and that problem's check is `scope`: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went into idea-mara-lighthouse instead. Nothing was added to idea-harrow-point."}`  This problem names the chandlery copy (idea-mara-l
PASS  judge-u2-u3-approve   Both units have the verdict `approve` and no problems.  - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. It has no problem about which note it went to, which is correct because the comment "Agent, migrate this." names no destination. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`. This is correct because the copy went to Tobias's note, as the comment asked.  The only `fix` is on 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went into idea-mara-lighthouse instead. Nothing was added to idea-harrow-point."}]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units appear in the reply: u1 (`"verdict":"fix"`), u2 (`"verdict":"approve"`) and u3 (`"verdict":"approve"`). The chandlery going to the wrong note is filed as a `fix` problem on u1, not as a `missed` entry: "the chandlery line was put in idea-mara-lighthouse, and nothing about it went to idea-harrow-point."
PASS  judge-shape   The reply is JSON findings with `batch` ("b1"), `round` (0), `units`, and `missed` ([]).  - **Units:** `units` has exactly one entry each for u1, u2, and u3, and no others. - **Verdicts:** all are `approve` or `fix`. u1 is `"verdict":"fix"`, and u2 and u3 are `"verdict":"approve"`. - **Problems match verdicts:** u1 (`fix`) has one problem. u2 and u3 (`approve`) each have `"problems":[]`. - **Chec
PASS  judge-u1-fix-scope-wrong-note   The reply gives u1 `"verdict":"fix"`. It has one problem, with `"check":"scope"`, `"note":"Ideas/idea-mara-lighthouse.md"`, `"line":10`, and `"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and nothing about it went to idea-harrow-point."`  That problem names the chandlery copy. It says the copy went to idea-mara-lighthous
PASS  judge-u2-u3-approve   Both units the check covers are approved, and neither has any problems listed.  - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. The verdict is approve and the problems list is empty. Nothing questions which note the line went to (idea-mara-lighthouse vs. idea-mara-habits), so the clearest fail case does not occur. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`. The verdict is ap
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the chandlery line was put in idea-mara-lighthouse, and nothing about it went to idea-harrow-point."}]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units are accounted for: u1 is `"verdict":"fix"` (the chandlery copy went to idea-mara-lighthouse instead of idea-harrow-point, which the check says is a fix, not a missed entry), and u2 and u3 are `"verdict":"approve"`.
PASS  judge-shape   The reply is valid JSON with `batch` ("b1"), `round` (0), `units`, and `missed` ([]).  **Units:** there is exactly one entry each for u1, u2 and u3, and no other units. - u1: `"verdict":"fix"` with one problem: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went to idea-mara-lighthouse instead, and
PASS  judge-u1-fix-scope-wrong-note   u1's verdict is `"verdict":"fix"`. It has one problem, and it is a scope problem: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went to idea-mara-lighthouse instead, and idea-harrow-point got nothing."}`  This names the chandlery copy (idea-mara-lighthouse.md, line 10), says it went to idea-mara-l
PASS  judge-u2-u3-approve   Both units come back `approve` with empty problem lists:  - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. It is not a `fix`, and no problem is raised about which note it went to. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`. It is not a `fix`, and no problems are listed.  The only `fix` is on u1, which this check doesn't judge.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says the chandlery goes in idea-harrow-point, but the copy went to idea-mara-lighthouse instead, and idea-harrow-point got nothing."}]},{"unit":"u2","verdict":"approve","problems":[]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

## Full Outputs: Bare

Each run shows its grades, then its final reply.

### Bare Case 1: `migration-verifier-10-recheck`

#### Run 1

Grades:

````
FAIL  judge-missed-empty   The reply's `missed` list is not empty. It holds one entry:  ```json "missed": [   {     "source": { "note": "brain-dump.md", "line": 13, "text": "- Tobias carved his initials into the gallery rail the summer he turned twelve." },     "what": "This line's unit (u2) isn't in this round's record because I approved it in round 0, but that approval was wrong. The copy in Ideas/idea-tobias.md line 11 
FAIL  judge-shape   The reply has JSON findings. `batch` and `round` are correct, and `units` is correct. The `missed` list is not empty, which breaks the rule that a re-check never lists missed lines.  - `"batch": "b1"`: correct. - `"round": 1`: correct. - `units`: one entry, `{ "unit": "u1", "verdict": "approve", "problems": [] }`. The verdict is `approve` and the `problems` list is empty, which is correct. There 
PASS  judge-u1-approve-fix-landed   u1's verdict is `approve` and its problem list is empty: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. Nothing objects to the idea-mara-lighthouse copy ("after Tobias drowned", "the next morning", the oars line) or to "that night". Nothing says "Maybe" is still missing.  The reply also has a `missed` entry about a different unit (u2, brain-dump.md line 13, "the summer he turned twelve
FAIL  judge-u2-not-reopened   The `units` array is fine: it holds only u1 (`{ "unit": "u1", "verdict": "approve", "problems": [] }`), with no entry for u2. The failure is in `missed`, which re-opens u2's approved copy.  - **It objects to u2's source line.** The `missed` entry cites `"brain-dump.md", "line": 13, "text": "- Tobias carved his initials into the gallery rail the summer he turned twelve."`, which is u2's source. - 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 1,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] }
  ],
  "missed": [
    {
      "source": { "note": "brain-dump.md", "line": 13, "text": "- Tobias carved his initials into the gallery rail the summer he turned twelve." },
      "what": "This line's unit (u2) isn't in this round's record because I approved it in round 0, but that approval was wrong. The copy in Ideas/idea-tobias.md line 11 says \"when he was twelve\" and drops \"the summer he turned twelve\". Fix that existing line so it keeps \"the summer\". Don't add a second copy."
    }
  ]
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply includes a `missed` list, and that list is empty: `"missed": []`. The check requires an empty `missed` list on a re-check, and both lines under "### 2026-10-09" already have units (u1 and u2), so nothing should be listed as missed.
PASS  judge-shape   Evidence: - `batch` is `"batch": "b1"` and `round` is `"round": 1`. Both match. - `units` has exactly one entry: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. There is no entry for u2 or any other unit. - The verdict is `approve`, which is an allowed value. Its `problems` list is empty, which is what an approve requires. - No problems are listed, so no `check` values need validating. 
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` with an empty problems list: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. It raises nothing about the idea-mara-lighthouse copy ("after Tobias drowned" / "the next morning"), nothing about "that night", and does not claim "Maybe" is still missing. `"missed": []` is also empty, so no new objections were introduced.
PASS  judge-u2-not-reopened   The `units` array has a single entry, and it is for u1: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. There is no entry for u2, not even an approval.  No problem points at u2's copy. u1's `problems` is empty (`[]`), and `"missed": []` is empty too. The reply never mentions "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11. The approved u2 work is left clos
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 1,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply includes a `missed` list, and it is empty: `"missed": []`. That matches the re-check rule, which says `missed` is always empty on a re-check. Both lines under "### 2026-10-09" already have units (u1 and u2), so nothing is missing.
PASS  judge-shape   Evidence: - `"batch": "b1"` and `"round": 1`: both match. - `"units"` has exactly one entry, `{ "unit": "u1", "verdict": "approve", "problems": [] }`. There is no entry for u2 or any other unit. - The verdict is `"approve"`, a permitted value, and the `"problems"` list is empty, as an approval requires. Because no problems are listed, the `check` values have nothing to validate. - `"missed": []` 
PASS  judge-u1-approve-fix-landed   The reply gives u1 the verdict `approve` with an empty problem list: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. Because there are no problems, nothing objects to the idea-mara-lighthouse copy ("after Tobias drowned", "the next morning", the oars line). Nothing objects to "that night" either, and nothing claims "Maybe" is still missing. The `"missed": []` field is also empty, so the
PASS  judge-u2-not-reopened   The reply's `units` array contains only one entry, and it is for u1: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. There is no entry for u2, not even an approval.  No problem anywhere objects to u2's copy. u1's `problems` list is empty (`"problems": []`), and so is `"missed": []`. Nothing mentions "when he was twelve," "the summer," "railing," or Ideas/idea-tobias.md line 11.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 1,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

### Bare Case 2: `migration-verifier-11-status-raise`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Both units appear in the record: `{ "unit": "u1", "verdict": "approve", "problems": [] }` and `{ "unit": "u2", "verdict": "fix", ... }`. The status problem on u2 is filed as a `fix` under `"check": "status"`, not as a `missed` entry. The reply does not list u1 as something that should have gone to char-mara or been committed.
PASS  judge-shape   The reply is a JSON object with `batch` set to `"b1"`, `round` set to `0`, a `units` array, and `"missed": []`.  - **Units:** There is exactly one entry for u1 and one for u2, and no other units appear. - **u1:** It has `"verdict": "approve"` with `"problems": []`. The approve has an empty problems list. - **u2:** It has `"verdict": "fix"` with one problem. The fix has at least one problem:   - `
PASS  judge-u1-approve-not-raised   u1's verdict is `approve` with no problems: `{ "unit": "u1", "verdict": "approve", "problems": [] }`.  The `missed` list is empty (`"missed": []`), so no entry asks to raise u1 to committed or move it to char-mara or any other Area Note.  The only problem in the reply is about u2, not u1. It concerns a different source line (brain-dump.md line 13) and asks to lower or remove a tag, not raise one.
PASS  judge-u2-fix-tag-writer-never-gave   The verdict for u2 is `fix`: `"unit": "u2", "verdict": "fix"`  The problem uses check `"status"`, which the rubric accepts. It names the provisional tag the writer never gave: "The source line (brain-dump.md line 13) has no status tag, and the comment under it only says where the line goes, so the line is tentative. The copy adds #status/provisional, which raises a status the writer never gave." 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 11,
          "what": "The source line (brain-dump.md line 13) has no status tag, and the comment under it only says where the line goes, so the line is tentative. The copy adds #status/provisional, which raises a status the writer never gave. \"Definitely\" in the wording doesn't change that. Remove the tag so the copy has no tag, like its source."
        }
      ]
    }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Both units appear in the `units` array (`"unit": "u1"` with verdict `"approve"`, and `"unit": "u2"` with verdict `"fix"`). The status problem on u2 is recorded as a `fix` with `"check": "status"`, not as a `missed` entry. Nothing in the reply says u1 should have gone to char-mara or should have been committed.
FAIL  judge-shape   The u2 problem points to the wrong line. The shape is otherwise fine, but the location rule is broken.  - **Units:** there is exactly one entry each for u1 and u2, and nothing else. This holds. - **u1:** `{ "unit": "u1", "verdict": "approve", "problems": [] }`. It is an approve with an empty problems list. This holds. - **u2:** `"verdict": "fix"` with one problem, and `"check": "status"` is one o
PASS  judge-u1-approve-not-raised   u1's verdict is `approve` with an empty problems list:  `{ "unit": "u1", "verdict": "approve", "problems": [] }`  The `missed` array is empty (`"missed": []`), so there is no entry about u1's line. Nothing in the reply asks to raise u1 to committed or says the wording ("I'm certain of it now") shows commitment. Nothing says the line should move to char-mara or another Area Note.  The only problem
PASS  judge-u2-fix-tag-writer-never-gave   The verdict for u2 is `fix`: `"unit": "u2", "verdict": "fix"`.  One problem, with check `status`, names the provisional tag that the writer never gave and asks for it to be removed: - "The source line has no status tag, and the comment on line 14 only says where the line goes, so the line stays tentative." - "Remove the `#status/provisional` tag the copy added." - "The word \"definitely\" doesn't
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 13,
          "what": "The source line has no status tag, and the comment on line 14 only says where the line goes, so the line stays tentative. Remove the `#status/provisional` tag the copy added. The word \"definitely\" doesn't raise the status, and the copy should have no tag at all."
        }
      ]
    }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Both units appear in the record: `{ "unit": "u1", "verdict": "approve", "problems": [] }` and `{ "unit": "u2", "verdict": "fix", ... }`. Nothing about u1 is flagged as needing to go to char-mara or be committed. The only status issue, on u2, is handled as a `fix` with `"check": "status"`, not as a `missed` entry. That matches what the check exp
PASS  judge-shape   Evidence: - The reply is JSON with all four required keys: `"batch": "b1"`, `"round": 0`, `"units": [...]`, `"missed": []`. - `units` has exactly one entry for u1 and one for u2, and no other units. - u1: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. The verdict is approve and the problems list is empty, as required. - u2: `"verdict": "fix"` with one problem. That meets the rule that 
PASS  judge-u1-approve-not-raised   u1's verdict is `approve` with no problems: `{ "unit": "u1", "verdict": "approve", "problems": [] }`.  No problem asks to raise u1 to committed, cites "I'm certain of it now" as evidence of commitment, or suggests moving it to char-mara or another Area Note. The `missed` array is empty (`"missed": []`), so it has no entry about u1's line either.  The only problem in the reply concerns u2, which i
PASS  judge-u2-fix-tag-writer-never-gave   The verdict for u2 is `"verdict": "fix"`, and the problem uses `"check": "status"`, which the check accepts.  The problem names the provisional tag the writer never gave and asks for an untagged copy: - "The source line (brain-dump.md line 13) has no status tag, and the comment under it only says where the line goes. It doesn't set a status, so the line is still tentative." - "Remove the #status/
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 11,
          "what": "The source line (brain-dump.md line 13) has no status tag, and the comment under it only says where the line goes. It doesn't set a status, so the line is still tentative. Remove the #status/provisional tag from the copy so it has no tag, like its source. The word 'definitely' doesn't set a status."
        }
      ]
    }
  ],
  "missed": []
}
```
````

### Bare Case 3: `migration-verifier-12-earlier-run-status`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The check only asks whether the reply's `missed` list is empty. It is: `"missed": []`.  The reply has no `missed` entry naming the wreck-buoy line, its provisional copy in `Ideas/idea-mara-habits.md`, or the barometer line.  The reply does raise the provisional copy in idea-mara-habits under u1's `problems` ("its current standing is on that copy (line 10), which is tagged #status/provisional... T
PASS  judge-shape   **Units:** `units` has exactly two entries, `"unit": "u1"` and `"unit": "u2"`. Each appears once, and no other unit is listed. `missed` is present as `[]`, alongside `"batch": "b1"` and `"round": 0`.  **Verdicts:** both are allowed values: u1 is `"verdict": "fix"` and u2 is `"verdict": "fix"`.  **Every `fix` has a problem:** u1 has one problem and u2 has one problem. There are no `approve` verdic
FAIL  judge-u1-approve-earlier-copy-left   The check requires u1's verdict to be `approve` with no problems. The text gives u1 `"verdict": "fix"` with one problem:  > "check": "status", "note": "char-mara.md", "line": 20, "what": "An earlier run already migrated this unit into Ideas/idea-mara-habits.md, and its current standing is on that copy (line 10), which is tagged #status/provisional. The Brain Dump line is history. The writer has n
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `"verdict": "fix"`, as the check requires.  Its single problem has `"check": "status"`, which is one of the accepted check types. It points at `"note": "Ideas/idea-mara-habits.md"`, `"line": 11`. It says the copy lost the writer's provisional tag:  > "The source line has the writer's #status/provisional tag, but the copy has no tag, so it reads as tentative and the record says \"t
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    {
      "unit": "u1",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "char-mara.md",
          "line": 20,
          "what": "An earlier run already migrated this unit into Ideas/idea-mara-habits.md, and its current standing is on that copy (line 10), which is tagged #status/provisional. The Brain Dump line is history. The writer has not committed the Idea Note copy, so this provisional material must not graduate into the Area Note. Take the line out of char-mara.md and leave the unit in the Idea Note."
        }
      ]
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-habits.md",
          "line": 11,
          "what": "The source line has the writer's #status/provisional tag, but the copy has no tag, so it reads as tentative and the record says \"tentative\". Migrating never changes status: put #status/provisional on the copy and record the status as provisional."
        }
      ]
    }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  It names nothing as missed: not the wreck-buoy line, not its provisional copy in idea-mara-habits, and not the barometer line. Both units appear in the reply (`"unit": "u1"` with `"verdict": "approve"`, and `"unit": "u2"` with `"verdict": "fix"`). Whether u2's status problem is correct falls outside this check.
PASS  judge-shape   Evidence: - **JSON findings present.** The keys are `"batch": "b1"`, `"round": 0`, `"units"` and `"missed": []`. - **Units are exactly u1 and u2.** Each appears once, and no other unit is listed. - **u1 is approved with no problems.** It reads `{ "unit": "u1", "verdict": "approve", "problems": [] }`, so the empty problems list is correct. - **u2 is a fix with one problem.** It reads `"verdict": "
PASS  judge-u1-approve-earlier-copy-left   u1's verdict is approve and it lists no problems: `{ "unit": "u1", "verdict": "approve", "problems": [] }`.  Nothing in u1's entry asks for the idea-mara-habits copy to be updated to committed, re-tagged or removed. It also does not say that copy contradicts or duplicates the char-mara line.  The reply does contain a `status` problem on `Ideas/idea-mara-habits.md` line 11. That problem belongs to
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `fix`: `"unit": "u2", "verdict": "fix"`.  Its problem has check `"status"`, which the check accepts. It names the lost provisional status on this copy: "The writer tagged the source line #status/provisional, but the copy has no tag, and the record calls it tentative. That lowers the status the writer gave. Keep #status/provisional on the copy and record the status as provisional."
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-habits.md",
          "line": 11,
          "what": "The writer tagged the source line #status/provisional, but the copy has no tag, and the record calls it tentative. That lowers the status the writer gave. Keep #status/provisional on the copy and record the status as provisional."
        }
      ]
    }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The check asks only whether the `missed` list is empty. The reply has:  ```json "missed": [] ```  The list contains no entries. It does not name the wreck-buoy line, its provisional copy in Ideas/idea-mara-habits.md, or the barometer line.  Note (outside this check's scope): the reply does bring up the earlier run's provisional copy, but as a `fix` problem under u1 ("its copy there is tagged #sta
PASS  judge-shape   The reply holds JSON findings with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`.  - **Units:** There is exactly one entry for `"unit": "u1"` and one for `"unit": "u2"`, and no other units. - **Verdicts:** Both are `"verdict": "fix"`, which is an allowed value. - **Each `fix` has at least one problem:**   - u1 has one problem: `"check": "status", "note": "char-mara.md", "line": 20`. 
FAIL  judge-u1-approve-earlier-copy-left   u1's verdict is `fix`, not `approve`:  > "unit": "u1", > "verdict": "fix",  It raises a `status` problem against char-mara.md line 20. That problem rests on the earlier run's provisional copy in idea-mara-habits:  > "check": "status", "note": "char-mara.md", "line": 20, "what": "An earlier run already moved this line into Ideas/idea-mara-habits.md (it has a migrated-to pointer), and its copy ther
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `"verdict": "fix"`, and it has a single problem with `"check": "status"`, aimed at `"note": "Ideas/idea-mara-habits.md"`, `"line": 11`.  That problem names the lost provisional status on this copy: "The source line is tagged #status/provisional, so the copy has to keep that tag. Without it the line reads as tentative in an Idea Note."  The fix restores the writer's status: "Write 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    {
      "unit": "u1",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "char-mara.md",
          "line": 20,
          "what": "An earlier run already moved this line into Ideas/idea-mara-habits.md (it has a migrated-to pointer), and its copy there is tagged #status/provisional. The Brain Dump is only history, so the line's current standing is that provisional copy, and provisional material can't go into an Area Note. Take the line out of char-mara.md and leave the Idea Note copy as it is. Then ask the writer in the run log whether they meant to commit it. If they did, they can tag the Idea Note line #status/committed."
        }
      ]
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-habits.md",
          "line": 11,
          "what": "The source line is tagged #status/provisional, so the copy has to keep that tag. Without it the line reads as tentative in an Idea Note. Write it as '- Mara has stopped answering letters from the mainland. #status/provisional' and set the unit's status to provisional, not tentative."
        }
      ]
    }
  ],
  "missed": []
}
```
````

### Bare Case 4: `migration-verifier-13-large-batch`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  The unit-level verdicts are consistent with the check's record. u8 is handled as a `fix` with check `"scope"`, noting that the bullet "comes after that range, has no tag and no comment of its own, so it should not migrate". It is not filed under `missed`. The three untagged 2026-10-08 lines do not appear anywhere as missed entries.
PASS  judge-others-approve   All seventeen correct units have `"verdict": "approve"` and `"problems": []`.  - **u1 to u7:** each is `{ "unit": "uN", "verdict": "approve", "problems": [] }`. - **u9 and u10:** `{ "unit": "u9", "verdict": "approve", "problems": [] }` and `{ "unit": "u10", "verdict": "approve", "problems": [] }`. Nothing is flagged on u10 for dropping "I think". - **u12, u13 and u14:** each is `"verdict": "appro
FAIL  judge-shape   There are 20 entries in `units`, u1 through u20, each listed once, with no extra units. Every verdict is `approve` or `fix`. Each `fix` has a problem, and each `approve` has `"problems": []`. All checks used are `scope` or `lost-detail`, which are allowed.  The pointer rule fails on all three graded units:  - **u8**: the problem has `"note": "brain-dump.md"` and `"line": 17`. It should point to `
PASS  judge-u11-fix-hedged-name   u11's verdict is `fix`, and its problem identifies the settled "Ewan" in the idea-harrow-point copy:  - Verdict: `"unit": "u11", "verdict": "fix"` - Problem: `"check": "lost-detail"`, `"note": "Ideas/idea-harrow-point.md"`, with the text: "The writer hedged the name (\"maybe called Ewan\"), but the idea-harrow-point copy treats \"Ewan\" as settled. That note introduces the relief keeper, so it sh
PASS  judge-u16-fix-every-second-sunday   Evidence: u16 has the verdict `fix`: `"unit": "u16", "verdict": "fix"`  Its problem names the changed frequency directly: > "The source says Mara rows out \"every second Sunday\", but the copy says \"every Sunday\", which changes how often she goes. Put \"every second Sunday\" back."  That meets the PASS condition: the problem says the frequency changed from "every second Sunday" to "every Sunday
PASS  judge-u8-fix-scope-outside-range   u8's verdict is `fix`, and its problem uses the check `scope` to say the bullet was migrated without being asked:  - `"unit": "u8", "verdict": "fix"` - `"check": "scope"` - `"what": "The comment on line 19 migrates the bullets from \"- Tobias taught Mara\" through \"- Tobias wanted to leave\". This bullet comes after that range, has no tag and no comment of its own, so it should not migrate. Remo
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] },
    { "unit": "u2", "verdict": "approve", "problems": [] },
    { "unit": "u3", "verdict": "approve", "problems": [] },
    { "unit": "u4", "verdict": "approve", "problems": [] },
    { "unit": "u5", "verdict": "approve", "problems": [] },
    { "unit": "u6", "verdict": "approve", "problems": [] },
    { "unit": "u7", "verdict": "approve", "problems": [] },
    {
      "unit": "u8",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "brain-dump.md",
          "line": 17,
          "what": "The comment on line 19 migrates the bullets from \"- Tobias taught Mara\" through \"- Tobias wanted to leave\". This bullet comes after that range, has no tag and no comment of its own, so it should not migrate. Remove the copy from idea-tobias."
        }
      ]
    },
    { "unit": "u9", "verdict": "approve", "problems": [] },
    { "unit": "u10", "verdict": "approve", "problems": [] },
    {
      "unit": "u11",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "Ideas/idea-harrow-point.md",
          "line": 26,
          "what": "The writer hedged the name (\"maybe called Ewan\"), but the idea-harrow-point copy treats \"Ewan\" as settled. That note introduces the relief keeper, so it should either state the hedge where the name first appears or call him by his role, e.g. \"The relief keeper lodges above the pub on the quay.\""
        }
      ]
    },
    { "unit": "u12", "verdict": "approve", "problems": [] },
    { "unit": "u13", "verdict": "approve", "problems": [] },
    { "unit": "u14", "verdict": "approve", "problems": [] },
    { "unit": "u15", "verdict": "approve", "problems": [] },
    {
      "unit": "u16",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "Ideas/idea-mara-habits.md",
          "line": 38,
          "what": "The source says Mara rows out \"every second Sunday\", but the copy says \"every Sunday\", which changes how often she goes. Put \"every second Sunday\" back."
        }
      ]
    },
    { "unit": "u17", "verdict": "approve", "problems": [] },
    { "unit": "u18", "verdict": "approve", "problems": [] },
    { "unit": "u19", "verdict": "approve", "problems": [] },
    { "unit": "u20", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  The out-of-range bullet is handled as the check expects. It appears as a `fix` on u8 (`"unit": "u8", "verdict": "fix"`, check `"scope"`, line 17 "comes after that range... so it shouldn't migrate"), not as a `missed` entry. None of the three untagged 2026-10-08 lines appear in `missed`.
PASS  judge-others-approve   All seventeen correct units have `"verdict": "approve"` and `"problems": []`:  - u1–u7: each is `{ "unit": "uN", "verdict": "approve", "problems": [] }` - u9: `{ "unit": "u9", "verdict": "approve", "problems": [] }` - u10: `{ "unit": "u10", "verdict": "approve", "problems": [] }`. It was not flagged for dropping "I think". - u12: `{ "unit": "u12", "verdict": "approve", "problems": [] }` - u13: `{
FAIL  judge-shape   There are 20 entries in `units`, one for each of u1 to u20, with no duplicates and no extra units. Every verdict is `approve` or `fix`. Each `approve` has `"problems": []`, each `fix` has one problem, and every `check` is one of the allowed values (`scope`, `lost-detail`). So the shape passes. The failure is in where the problems point.  - **u8:** The problem is `"note": "brain-dump.md", "line": 
PASS  judge-u11-fix-hedged-name   u11's verdict is `"verdict": "fix"`, and it has one problem with `"check": "lost-detail"` (which the check accepts), `"note": "brain-dump.md"`, `"line": 26`:  > "The writer only said the relief keeper is \"maybe called Ewan\", but the idea-harrow-point copy uses Ewan as if the name were settled. In that note, either keep the hedge where the keeper first appears (\"The relief keeper, maybe called 
PASS  judge-u16-fix-every-second-sunday   u16's verdict is `fix`: `"unit": "u16", "verdict": "fix"`. Its single problem, check `"lost-detail"`, says the frequency changed:  > "The source says Mara rows out \"every second Sunday\", but the copy says \"every Sunday\", which changes how often she goes. Put \"every second Sunday\" back."  This names both the missing "second" and the change in frequency, which is what the check requires.
PASS  judge-u8-fix-scope-outside-range   Evidence: u8's verdict is `"verdict": "fix"`. Its one problem has `"check": "scope"` and says the bullet was migrated without being asked:  > "The comment on line 19 covers the bullets from \"- Tobias taught Mara\" through \"- Tobias wanted to leave\" (lines 10–16). Line 17 comes after that range, has no tag, and no comment points to it, so it shouldn't migrate. Remove this copy from idea-tobias.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] },
    { "unit": "u2", "verdict": "approve", "problems": [] },
    { "unit": "u3", "verdict": "approve", "problems": [] },
    { "unit": "u4", "verdict": "approve", "problems": [] },
    { "unit": "u5", "verdict": "approve", "problems": [] },
    { "unit": "u6", "verdict": "approve", "problems": [] },
    { "unit": "u7", "verdict": "approve", "problems": [] },
    {
      "unit": "u8",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "brain-dump.md",
          "line": 17,
          "what": "The comment on line 19 covers the bullets from \"- Tobias taught Mara\" through \"- Tobias wanted to leave\" (lines 10–16). Line 17 comes after that range, has no tag, and no comment points to it, so it shouldn't migrate. Remove this copy from idea-tobias."
        }
      ]
    },
    { "unit": "u9", "verdict": "approve", "problems": [] },
    { "unit": "u10", "verdict": "approve", "problems": [] },
    {
      "unit": "u11",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 26,
          "what": "The writer only said the relief keeper is \"maybe called Ewan\", but the idea-harrow-point copy uses Ewan as if the name were settled. In that note, either keep the hedge where the keeper first appears (\"The relief keeper, maybe called Ewan, lodges above the pub on the quay.\") or call them \"the relief keeper\"."
        }
      ]
    },
    { "unit": "u12", "verdict": "approve", "problems": [] },
    { "unit": "u13", "verdict": "approve", "problems": [] },
    { "unit": "u14", "verdict": "approve", "problems": [] },
    { "unit": "u15", "verdict": "approve", "problems": [] },
    {
      "unit": "u16",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 38,
          "what": "The source says Mara rows out \"every second Sunday\", but the copy says \"every Sunday\", which changes how often she goes. Put \"every second Sunday\" back."
        }
      ]
    },
    { "unit": "u17", "verdict": "approve", "problems": [] },
    { "unit": "u18", "verdict": "approve", "problems": [] },
    { "unit": "u19", "verdict": "approve", "problems": [] },
    { "unit": "u20", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Every unit is accounted for. u1 through u20 all appear in `units`. The out-of-range u8 is handled as a `fix` with `"check": "scope"` rather than as a missed entry. The three untagged lines under "### 2026-10-08" are not listed anywhere, which is correct.
PASS  judge-others-approve   All seventeen correct units are approved with empty problem lists:  - **u1 to u7:** each is `{ "unit": "uN", "verdict": "approve", "problems": [] }`. That includes u5, so its "Maybe" was not flagged. - **u9:** `{ "unit": "u9", "verdict": "approve", "problems": [] }`. It was not flagged for which note it went to. - **u10:** `{ "unit": "u10", "verdict": "approve", "problems": [] }`. It was not flag
FAIL  judge-shape   **Count:** `units` has 20 entries, u1 through u20, each once, with no extra units. Every `verdict` is `approve` or `fix`. Each `approve` has `"problems": []`, and each `fix` has at least one problem. Every `check` is one of the four allowed values: `scope`, `lost-detail`, `lost-detail`. Those rules hold.  **u8 is broken.** The problem points at the source note instead of the copy: ``` "check": "s
PASS  judge-u11-fix-hedged-name   u11's verdict is `fix`: `"unit": "u11", "verdict": "fix"`.  Its single problem has `"check": "lost-detail"`, `"note": "Ideas/idea-harrow-point.md"`, `"line": 10`. It names the settled "Ewan" in the idea-harrow-point copy: "The writer hedged the name (\"maybe called Ewan\"), but this copy treats Ewan as a settled name." It also gives the fix of referring to the keeper by role: "this line should re
PASS  judge-u16-fix-every-second-sunday   u16's verdict is `fix`: `"unit": "u16", "verdict": "fix"`.  Its one problem names the changed frequency directly: "The source says Mara rows out \"every second Sunday\", but the copy says \"every Sunday\", which changes how often she goes. Put \"every second Sunday\" back."  That problem says the copy changed "every second Sunday" to "every Sunday" and that this changes how often Mara goes, which
PASS  judge-u8-fix-scope-outside-range   u8's verdict is `fix`: `"unit": "u8", "verdict": "fix"`.  It has a `scope` problem that names the migration nobody asked for: `"check": "scope"`, with `"what": "The writer's comment on line 19 asks only for the bullets from \"- Tobias taught Mara\" through \"- Tobias wanted to leave\" (lines 10–16) to be migrated. Line 17 comes after that range and has no tag or comment of its own, so it doesn't 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    { "unit": "u1", "verdict": "approve", "problems": [] },
    { "unit": "u2", "verdict": "approve", "problems": [] },
    { "unit": "u3", "verdict": "approve", "problems": [] },
    { "unit": "u4", "verdict": "approve", "problems": [] },
    { "unit": "u5", "verdict": "approve", "problems": [] },
    { "unit": "u6", "verdict": "approve", "problems": [] },
    { "unit": "u7", "verdict": "approve", "problems": [] },
    {
      "unit": "u8",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "brain-dump.md",
          "line": 17,
          "what": "The writer's comment on line 19 asks only for the bullets from \"- Tobias taught Mara\" through \"- Tobias wanted to leave\" (lines 10–16) to be migrated. Line 17 comes after that range and has no tag or comment of its own, so it doesn't migrate. Remove this copy from Ideas/idea-tobias.md."
        }
      ]
    },
    { "unit": "u9", "verdict": "approve", "problems": [] },
    { "unit": "u10", "verdict": "approve", "problems": [] },
    {
      "unit": "u11",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "Ideas/idea-harrow-point.md",
          "line": 10,
          "what": "The writer hedged the name (\"maybe called Ewan\"), but this copy treats Ewan as a settled name. The hedge is already stated where the name first appears, in idea-mara-lighthouse, so this line should refer to him by his role: \"The relief keeper lodges above the pub on the quay. #status/provisional\""
        }
      ]
    },
    { "unit": "u12", "verdict": "approve", "problems": [] },
    { "unit": "u13", "verdict": "approve", "problems": [] },
    { "unit": "u14", "verdict": "approve", "problems": [] },
    { "unit": "u15", "verdict": "approve", "problems": [] },
    {
      "unit": "u16",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "Ideas/idea-mara-habits.md",
          "line": 0,
          "what": "The source says Mara rows out \"every second Sunday\", but the copy says \"every Sunday\", which changes how often she goes. Put \"every second Sunday\" back."
        }
      ]
    },
    { "unit": "u17", "verdict": "approve", "problems": [] },
    { "unit": "u18", "verdict": "approve", "problems": [] },
    { "unit": "u19", "verdict": "approve", "problems": [] },
    { "unit": "u20", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

### Bare Case 5: `migration-verifier-14-comment-names-note`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units appear in `units` (`"unit": "u1"`, `"unit": "u2"`, `"unit": "u3"`). The chandlery routing problem is handled as the check expects, as a `fix` on u1 rather than a `missed` entry: `"unit": "u1", "verdict": "fix"`, with the note "the chandlery goes in idea-harrow-point, but this copy was put in idea-mara-lighthouse."
PASS  judge-shape   The reply is well-formed JSON findings with `batch` ("b1"), `round` (0), `units`, and `missed` ([]).  **Units:** There is exactly one entry each for u1, u2, and u3. No other units appear.  **Verdicts:** - u1: `"verdict": "fix"`. It has one problem, so it is not empty. - u2: `"verdict": "approve", "problems": []` - u3: `"verdict": "approve", "problems": []`  Every verdict is either `approve` or `f
PASS  judge-u1-fix-scope-wrong-note   The verdict for u1 is `fix`: `"unit": "u1", "verdict": "fix"`.  It has one problem, and that problem's check is `scope`: - `"check": "scope", "note": "Ideas/idea-mara-lighthouse.md", "line": 10` - `"what": "The writer's comment on brain-dump.md line 11 says the chandlery goes in idea-harrow-point, but this copy was put in idea-mara-lighthouse. Move the paraffin sentence into Ideas/idea-harrow-poi
PASS  judge-u2-u3-approve   Both units the check covers got `approve` and have no problems:  - u2: `{ "unit": "u2", "verdict": "approve", "problems": [] }`. Nothing was raised about which note it went to, so it doesn't hit the clearest fail condition (a problem on u2 about destination). - u3: `{ "unit": "u3", "verdict": "approve", "problems": [] }`. Nothing was raised here either.  The only `fix` is on u1 (`"verdict": "fix"
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    {
      "unit": "u1",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The writer's comment on brain-dump.md line 11 says the chandlery goes in idea-harrow-point, but this copy was put in idea-mara-lighthouse. Move the paraffin sentence into Ideas/idea-harrow-point.md and take it out of idea-mara-lighthouse. The writer's routing comment wins."
        }
      ]
    },
    { "unit": "u2", "verdict": "approve", "problems": [] },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units are covered in `units` (u1 `"verdict": "fix"`, u2 `"verdict": "approve"`, u3 `"verdict": "approve"`). The chandlery misrouting is reported as a `fix` on u1 (`"Move that copy to Ideas/idea-harrow-point.md"`), not as a `missed` entry, which is what the check requires.
FAIL  judge-shape   The u1 problem points to the wrong note and line. The check requires every u1 problem to have `note` set to `Ideas/idea-mara-lighthouse.md` and `line` set to 10. The reply gives:  ```json {   "check": "scope",   "note": "brain-dump.md",   "line": 11,   "what": "The writer's comment sends the chandlery material to idea-harrow-point, but the copy about Fenwick's chandlery selling lamp paraffin went
PASS  judge-u1-fix-scope-wrong-note   Evidence:  - **u1's verdict is `fix`:** `"unit": "u1", "verdict": "fix"` - **There is a `scope` problem:** `"check": "scope"` - **It names the chandlery copy going to the wrong note.** The `what` field says: "The writer's comment sends the chandlery material to idea-harrow-point, but the copy about Fenwick's chandlery selling lamp paraffin went to Ideas/idea-mara-lighthouse.md. Move that copy to 
PASS  judge-u2-u3-approve   Both units under check are approved with empty problem lists:  - u2: `{ "unit": "u2", "verdict": "approve", "problems": [] }`. It has no `fix` and no problem about which note the copy went to, even though u1's problem mentions Ideas/idea-mara-lighthouse.md, where u2's copy also sits. - u3: `{ "unit": "u3", "verdict": "approve", "problems": [] }`. This is also clean.  The only `fix` in the reply i
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    {
      "unit": "u1",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "brain-dump.md",
          "line": 11,
          "what": "The writer's comment sends the chandlery material to idea-harrow-point, but the copy about Fenwick's chandlery selling lamp paraffin went to Ideas/idea-mara-lighthouse.md. Move that copy to Ideas/idea-harrow-point.md. The only-shop copy in idea-mara-habits is correct."
        }
      ]
    },
    { "unit": "u2", "verdict": "approve", "problems": [] },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units are accounted for. The chandlery routing error is handled as a `fix` on u1 (`"unit": "u1", "verdict": "fix"`), which is what the check expects. It is not listed as a missed entry.
PASS  judge-shape   The reply is valid JSON findings with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`.  **Units:** There is exactly one entry each for u1, u2, and u3, and no other units appear. - u1: `"verdict": "fix"` with one problem. - u2: `{ "unit": "u2", "verdict": "approve", "problems": [] }` - u3: `{ "unit": "u3", "verdict": "approve", "problems": [] }`  **Verdicts:** All are `approve` or `fix`
PASS  judge-u1-fix-scope-wrong-note   The u1 verdict is `fix`: `"unit": "u1", "verdict": "fix"`.  There is a `scope` problem about the chandlery copy: - `"check": "scope"` - `"note": "Ideas/idea-mara-lighthouse.md"` - `"line": 10` - `"what": "The writer's comment says the chandlery goes in idea-harrow-point, but this copy went to idea-mara-lighthouse. Move the paraffin line to Ideas/idea-harrow-point.md, because the writer's routing 
PASS  judge-u2-u3-approve   Both units in scope come back as clean approvals:  - u2: `{ "unit": "u2", "verdict": "approve", "problems": [] }`. Its verdict is `approve` and its problems list is empty. Nothing is raised about which note the copy landed in (Ideas/idea-mara-lighthouse.md). That is the case the check names as the clearest fail, and it does not occur. - u3: `{ "unit": "u3", "verdict": "approve", "problems": [] }`
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "batch": "b1",
  "round": 0,
  "units": [
    {
      "unit": "u1",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The writer's comment says the chandlery goes in idea-harrow-point, but this copy went to idea-mara-lighthouse. Move the paraffin line to Ideas/idea-harrow-point.md, because the writer's routing comment wins. The only-shop copy in idea-mara-habits is correct as it is."
        }
      ]
    },
    { "unit": "u2", "verdict": "approve", "problems": [] },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

