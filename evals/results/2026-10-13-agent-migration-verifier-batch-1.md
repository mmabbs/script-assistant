# 2026-10-13 Agent Run: Migration-verifier Batch 1

The first run of the `script-asst:migration-verifier` agent file on batch 1. Run by hand with `_tools/research-run.py --suite migration-verifier --agent script-asst:migration-verifier`, outside `claude plugin eval`. This is plan-migration-verifier.md 03, Milestone 2, its third step. The worker that wrote the agent file never saw the cases.

## What Was Run

- **Date:** 2026-10-13, 16:53 to 16:57 EDT.
- **Agent:** `agents/migration-verifier.md`, 163 lines, as written by its worker, with no fix: `model: claude-opus-5-5`, `effort: high`, `tools: Read, Glob, Grep`.
- **Claude Code:** 2.1.296.
- **Runs:** 27. Nine cases, three runs each, at most five at a time.
- **Prompt:** each case's `prompt.md` body as changed on 2026-10-13 to match the skill's hand-off (`results/2026-10-13-regrade-bare-migration-verifier-batch-1-note-check.md`, Prompt Changes). It carries no answer shape and no instructions on how to judge.
- **Rules given:** `rules/migrator-rules.md`, byte-identical to the plugin's `references/migrator-rules.md` (checked with `cmp`).
- **Judges:** every grader in each case's `graders/`, the shape judges of cases 1 to 4 with the note check.
- **Command:**

```bash
python3 _tools/research-run.py --suite migration-verifier --agent script-asst:migration-verifier \
  --out <session scratchpad>/mv-agent-1 --runs 3
```

- **Errors and timeouts:** none. Every run exited 0. No run was repeated.
- **Cost:** $6.86 for the runs, from their streams. The runner's printed total, judges included, was $8.81.

## Summary Table

| Case | All checks | Bare, regraded | Cost |
| --- | --- | --- | --- |
| 1 `migration-verifier-01-lost-detail` | 3 of 3 | 1 of 3 | $0.90 |
| 2 `migration-verifier-02-status` | 3 of 3 | 3 of 3 | $0.83 |
| 3 `migration-verifier-03-scope` | 3 of 3 | 3 of 3 | $0.74 |
| 4 `migration-verifier-04-standalone` | 3 of 3 | 1 of 3 | $0.71 |
| 5 `migration-verifier-05-missed-line` | 3 of 3 | 3 of 3 | $0.71 |
| 6 `migration-verifier-06-clean-batch` | 3 of 3 | 3 of 3 | $0.77 |
| 7 `migration-verifier-07-asked-by-meaning` | 3 of 3 | 3 of 3 | $0.67 |
| 8 `migration-verifier-08-flags-asked` | 3 of 3 | 3 of 3 | $0.76 |
| 9 `migration-verifier-09-flags-not-asked` | 3 of 3 | 3 of 3 | $0.77 |
| **Total** | **27 of 27** | **23 of 27** | **$6.86** |

"Bare, regraded" is the 2026-10-12 bare runs with the note check (`results/2026-10-13-regrade-bare-migration-verifier-batch-1-note-check.md`). The bare runs answered the older prompts, which gave the answer shape; these agent runs got no shape from the prompt.

## Code Checks

Made in code on every reply, beyond the judges:

1. **Every reply is bare JSON.** `json.loads` reads all 27 as they are: no code fence, no prose.
2. **`runmanager findings` would accept every reply.** Each passed the code's own `shape_problem`, the batch one in `migration/findings.py` or the flags one in `migration/flags.py`, with the units or flags its fixture handed.
3. **The runs used the agent.** The runner passed `--agent` and `--plugin-dir`, and each run's start event lists `script-asst:migration-verifier`. The start event doesn't name the agent in use. The replies show it: the prompts hold no answer shape, and all 27 answer in the agent file's shape.
4. **Tools:** Read in every run, Glob in three, Grep in the three runs of case 9. No other tool, and no write.

## Findings

1. **The agent passes every batch-1 check in all 27 runs, the note check included.** Every verdict and every problem's `note` is the same across a case's three runs.
2. **Every problem names the note that holds the bad text.** Cases 1 and 4, where bare Claude named `brain-dump.md` in 4 of 6 runs, name the copy's note in all six.
3. **Case 3's u2 points at the rejected copy, `Ideas/idea-harrow-point.md` line 13,** in all three runs. All three bare runs used line 9, where the record puts the source. Both pass.
4. **Case 2's u2 gets a second problem in all three runs, a `scope` fix:** the comment named char-mara and the copy went to an Idea Note. The judge's own text names this as a second error. Bare Claude raised only the `status` half.
5. **Observed, not graded: `what` speaks to the writer as "you" in some runs and as "the writer" in others.** In case 2, runs 1 and 3 say "You tagged this line committed"; run 2 says "The writer tagged this line committed." Both are plain words for the writer.
6. **Batch 1 still can't be the gate on its own** (plan-migration-verifier.md 01 item 7). Cases 10 to 14 are.

## Full Outputs

Each run shows its grades, then its final reply.

### Case 1: `migration-verifier-01-lost-detail`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units have entries in `units`: - `"unit": "u1"` with `"verdict": "fix"` - `"unit": "u2"` with `"verdict": "fix"` - `"unit": "u3"` with `"verdict": "approve"`  The bad copies for u1 ("only says 'when she was a child', so her exact age is lost") and u2 ("states it as fact") are reported as `fix` verdicts, not as `missed` entries. That m
PASS  judge-shape   Evidence: - JSON findings are present with all required keys: `"batch": "b1"`, `"round": 0`, `"units": [...]`, `"missed": []`. - `units` has exactly one entry each for u1, u2, and u3. No other unit appears. - u1: `"verdict": "fix"`, with one problem: `"check": "lost-detail"`, `"note": "Ideas/idea-tobias.md"`, `"line": 10`. The note and line match the expected copy and line, and the problem does n
PASS  judge-u1-fix-lost-age   u1's verdict is `"verdict": "fix"`, and it lists one problem, which points at the idea-tobias copy:  - `"note": "Ideas/idea-tobias.md"`, `"line": 10` - `"what": "The source says Tobias drowned when Mara was nine, but this copy only says 'when she was a child', so her exact age is lost."`  The problem names the right file and says the age "nine" was lost and replaced by "a child." No problem is ra
PASS  judge-u2-fix-lost-maybe   u2's verdict is `fix`: `"unit": "u2", "verdict": "fix"`.  Its one problem names the lost hedge directly: - `"check": "lost-detail"` - `"what": "The source says her father 'maybe' hid the logbook in the tower, but the copy states it as fact."`  The check is `lost-detail`, which the rubric accepts. The note text says the "maybe" in the source became a statement of fact in the copy. That is the plan
PASS  judge-u3-approve   The reply gives unit u3 the verdict `approve` and lists no problems:  ``` "unit": "u3", "verdict": "approve", "problems": [] ```  The reply does not flag u3 as `fix`, either for the rewording ("even though" → "still ... though") or for any other reason. That matches the expected outcome, since the copy keeps the paraffin smell and the year 1962.
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
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "Ideas/idea-tobias.md",
          "line": 10,
          "what": "The source says Tobias drowned when Mara was nine, but this copy only says 'when she was a child', so her exact age is lost."
        }
      ]
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The source says her father 'maybe' hid the logbook in the tower, but the copy states it as fact."
        }
      ]
    },
    {
      "unit": "u3",
      "verdict": "approve",
      "problems": []
    }
  ],
  "missed": []
}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units are covered in `units`: - u1: `"verdict":"fix"` - u2: `"verdict":"fix"` - u3: `"verdict":"approve"`  The wrong copies in u1 and u2 are correctly recorded as `fix` verdicts, not as `missed` entries.
PASS  judge-shape   The reply is valid JSON and has the required keys: `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`.  **Units:** There is exactly one entry each for u1, u2 and u3, and no other units appear.  **Verdicts:** Every verdict is allowed. - u1: `"verdict":"fix"` - u2: `"verdict":"fix"` - u3: `"verdict":"approve"`  **Problems and approve:** - u1 has one problem. - u2 has one problem. - u3 h
PASS  judge-u1-fix-lost-age   Evidence: - u1's verdict is `"verdict":"fix"`. - One problem points at the idea-tobias copy: `"note":"Ideas/idea-tobias.md"`. - That problem names the lost age: `"what":"The source says Tobias drowned when Mara was nine. The copy says 'when she was a child', so her exact age is lost."` - u1 has only this one problem. It does not wrongly flag the idea-mara-habits copy.
PASS  judge-u2-fix-lost-maybe   Evidence: u2's verdict is `"verdict":"fix"`, and its single problem names the lost hedge:  - check: `"lost-detail"` - note: `"Ideas/idea-mara-lighthouse.md"`, line 10 - what: `"The source says her father 'maybe' hid the logbook in the tower. The copy states it as fact and drops the 'maybe'."`  This finds the planted error: the copy dropped "Maybe," so a possibility now reads as fact. The check ty
PASS  judge-u3-approve   The final reply gives u3 an approval with no problems: `{"unit":"u3","verdict":"approve","problems":[]}`.  The rewording ("even though" became "still ... though") was not flagged. No problem is listed against u3, and the `"missed":[]` field adds nothing about it. The `fix` verdicts in the reply belong only to u1 and u2.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,"what":"The source says Tobias drowned when Mara was nine. The copy says 'when she was a child', so her exact age is lost."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the logbook in the tower. The copy states it as fact and drops the 'maybe'."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units appear in the record with verdicts: - `"unit":"u1","verdict":"fix"` - `"unit":"u2","verdict":"fix"` - `"unit":"u3","verdict":"approve"`  The two copies with lost details (Mara's age for u1, the dropped "maybe" for u2) are filed as `fix`, not as `missed` entries, as the check requires.
PASS  judge-shape   Evidence: - **Top-level shape:** The reply is JSON with `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`. - **Units:** There is exactly one entry each for u1, u2 and u3, and no other units. - **u1:** `"verdict":"fix"` with one problem: `{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,...}`.   - The note and line match the expected `Ideas/idea-tobias.md` line 10.   - T
PASS  judge-u1-fix-lost-age   Unit u1 has the verdict `"verdict":"fix"`.  Its one problem points at the idea-tobias copy and names the lost age: `{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,"what":"The source says Mara was nine when Tobias drowned; the copy only says she was 'a child', so her exact age is lost."}`  The `note` field targets `Ideas/idea-tobias.md`. The `what` field says "nine" was replaced by
PASS  judge-u2-fix-lost-maybe   u2's verdict is `fix`: `"unit":"u2","verdict":"fix"`.  Its one problem names the lost hedge: `{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the logbook in the tower; the copy states it as fact."}`  The check is `lost-detail`, which is allowed. The note says the source's "maybe" was dropped and the copy now states it as fact.
PASS  judge-u3-approve   The u3 entry in the reply reads: `{"unit":"u3","verdict":"approve","problems":[]}`. The verdict is `approve` and the problems list is empty. The reply did not flag the "even though" → "still ... though" rewording, and it raised nothing else for u3.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-tobias.md","line":10,"what":"The source says Mara was nine when Tobias drowned; the copy only says she was 'a child', so her exact age is lost."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"lost-detail","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The source says her father 'maybe' hid the logbook in the tower; the copy states it as fact."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 2: `migration-verifier-02-status`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units are covered in `units`: - u1: `"verdict":"fix"`, a status problem. - u2: `"verdict":"fix"`, with status and scope problems. - u3: `"verdict":"approve"`.  The status errors on u1 and u2 are reported as `fix` verdicts, not as `missed` entries. That matches what the check requires.
PASS  judge-shape   The JSON has `batch`, `round`, `units`, and `missed`. Each rule holds:  - **Units:** there is exactly one entry each for `"unit":"u1"`, `"unit":"u2"` and `"unit":"u3"`, and no other units. - **Verdicts:** all are `fix` or `approve`. u1 is `"verdict":"fix"`, u2 is `"verdict":"fix"`, and u3 is `"verdict":"approve"`. - **Problems on fixes:** u1 has one problem and u2 has two. - **Approve has none:**
PASS  judge-u1-fix-provisional-in-area-note   u1's verdict is `fix`: `{"unit":"u1","verdict":"fix",...}`  It has one problem, and it uses the check `status`: `{"check":"status","note":"char-mara.md","line":20,"what":"You tagged this line provisional, but it was copied into Mara's character note, which can only hold committed material. It belongs in an Idea Note at provisional."}`  - The problem names provisional material in char-mara.md and 
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `"verdict":"fix"`, and both of its problems name the gap between the writer's committed tag or comment and the provisional copy:  - **Status:** `{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"You tagged this line committed, but the copy was written as provisional in an Idea Note, which is lower than the status you gave it."}` This says the copy is provi
PASS  judge-u3-approve   The reply gives u3 the verdict `approve` with no problems: `{"unit":"u3","verdict":"approve","problems":[]}`. It doesn't flag the status, scope, or the "clockwork mechanism" wording.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"status","note":"char-mara.md","line":20,"what":"You tagged this line provisional, but it was copied into Mara's character note, which can only hold committed material. It belongs in an Idea Note at provisional."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"You tagged this line committed, but the copy was written as provisional in an Idea Note, which is lower than the status you gave it."},{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says this goes in char-mara, but it was put in the Mara Lighthouse Idea Note instead of Mara's character note."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units appear in the record: - `"unit":"u1","verdict":"fix"` - `"unit":"u2","verdict":"fix"` - `"unit":"u3","verdict":"approve"`  The two status problems (u1 and u2) are recorded as `fix` verdicts. They are not listed as `missed` entries, which is what the check requires.
PASS  judge-shape   **Units:** exactly three entries, one each for `"unit":"u1"`, `"unit":"u2"`, and `"unit":"u3"`. No other units appear, and none is listed twice. `"missed":[]` is present, along with `"batch":"b1"` and `"round":0`.  **Verdicts:** all are valid. They are `"verdict":"fix"` for u1, `"verdict":"fix"` for u2, and `"verdict":"approve"` for u3.  **Fix and approve rules:** - u1 (`fix`) has 1 problem. - u2
PASS  judge-u1-fix-provisional-in-area-note   Evidence:  - **Verdict:** u1's verdict is `"verdict":"fix"`, not approve. - **Status problem:** u1 has a problem with `"check":"status"` on `"note":"char-mara.md"`. It reads: *"The writer tagged this line provisional, but the copy sits in Mara's Area Note, which holds only committed material. Provisional material belongs in an Idea Note, not an Area Note."* This says that provisional, uncommitted
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `"verdict":"fix"`.  Its problems name the gap between the writer's committed tag and the provisional copy: - `{"check":"status", ... "what":"The writer tagged this line committed, but the copy is tagged provisional and sits in an Idea Note. It should be committed, as the writer tagged it."}` - `{"check":"scope", ... "what":"The writer's comment says this line goes in char-mara, bu
PASS  judge-u3-approve   The reply gives u3 the verdict `approve` with no problems: `{"unit":"u3","verdict":"approve","problems":[]}`. That matches the expected result. The line is committed, it went to char-mara.md as the comment named, and "clockwork mechanism" says the same thing as "clockwork."
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"status","note":"char-mara.md","line":20,"what":"The writer tagged this line provisional, but the copy sits in Mara's Area Note, which holds only committed material. Provisional material belongs in an Idea Note, not an Area Note."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer tagged this line committed, but the copy is tagged provisional and sits in an Idea Note. It should be committed, as the writer tagged it."},{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The writer's comment says this line goes in char-mara, but the copy went to the Mara Lighthouse Idea Note instead."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All three units appear in the record: - `"unit":"u1","verdict":"fix"` - `"unit":"u2","verdict":"fix"` - `"unit":"u3","verdict":"approve"`  The status errors on u1 and u2 are recorded as `fix` verdicts, not as `missed` entries, which is what the check requires.
PASS  judge-shape   Evidence: - `units` has exactly u1, u2, u3, each once, and no other units. - Every verdict is `approve` or `fix`: u1 `"verdict":"fix"`, u2 `"verdict":"fix"`, u3 `"verdict":"approve"`. - Each `fix` has problems, and the `approve` has an empty list: u3 `"problems":[]`. - Every check is in the allowed set: `"status"` on u1, and `"status"` and `"scope"` on u2. - u1's problem points to the expected no
PASS  judge-u1-fix-provisional-in-area-note   **Verdict:** u1 is marked `"verdict":"fix"`, not approved.  **Problem:** It has exactly one problem, with `"check":"status"` and `"note":"char-mara.md"`: > "You tagged this line provisional, but it was copied into Mara's character note, which holds only committed material. Provisional material belongs in an Idea Note, so it shouldn't sit here."  **Why this passes:** - It says the material is prov
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `"verdict":"fix"`, and both of its problems name the gap the check asks for.  - **Status problem:** `{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"You tagged this line committed, but the copy is tagged provisional, which is lower than the status you gave it."}`. This says the copy is provisional where the writer said committed. - **Scope problem:** `{"
PASS  judge-u3-approve   The final reply gives u3 the verdict `approve` with an empty problems list:  `{"unit":"u3","verdict":"approve","problems":[]}`  No problems are raised against u3 anywhere else in the reply. The flagged problems belong only to u1 (`"line":20` in char-mara.md) and u2 (`Ideas/idea-mara-lighthouse.md`). The `"missed":[]` field is also empty, so nothing about u3 is reported there.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"status","note":"char-mara.md","line":20,"what":"You tagged this line provisional, but it was copied into Mara's character note, which holds only committed material. Provisional material belongs in an Idea Note, so it shouldn't sit here."}]},{"unit":"u2","verdict":"fix","problems":[{"check":"status","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"You tagged this line committed, but the copy is tagged provisional, which is lower than the status you gave it."},{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"Your comment says this goes in char-mara, but the copy went into the Mara Lighthouse Idea Note and nothing was added to char-mara."}]},{"unit":"u3","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 3: `migration-verifier-03-scope`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`. Both batch items are covered by units in the record (u3 for the brain-dump radio line, u1 for the hotel-sale comment). The over-wide reading of the rejection appears as a `fix` on unit u2 (`"This rejects the town's hotel sale of the harbour cottages and pier, which the writer kept open."`), not as a `missed` entry.
PASS  judge-shape   Evidence: - **Shape:** The reply is JSON with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed": []`. - **Units:** There is exactly one entry each for u1, u2 and u3, and none for any other unit. - **u1:** `"verdict": "approve"` with `"problems": []`. This is an approve with an empty problems list. - **u2:** `"verdict": "fix"` with one problem: `"check": "scope"`, `"note": "Ideas/idea-harrow
PASS  judge-u1-approve   u1's verdict is `approve` and it lists no problems: `"unit": "u1", "verdict": "approve", "problems": []`. The problems the reviewer flagged are all on other units. u2 is marked fix for the harbour cottages rejection in idea-harrow-point.md, and u3 is marked fix for the causeway line edit. Neither one touches u1's rejection of the Mara hotel-sale line.
PASS  judge-u2-fix-scope-town   u2's verdict is `"verdict": "fix"`, and it has a single problem:  - `"check": "scope"` - `"note": "Ideas/idea-harrow-point.md"` - `"line": 13` - `"what": "The comment ruled out the hotel sale for Mara's story only and said the town can still have it. This rejects the town's hotel sale of the harbour cottages and pier, which the writer kept open."`  This problem has the check `scope` and is in the
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `"verdict": "fix"`, so the unit was not approved.  It has one problem, and its check is scope: - `"check": "scope"`, `"note": "Ideas/idea-mara-lighthouse.md"`, `"line": 10` - `"what": "The causeway line was capitalised and given a full stop, but no comment asked for that. The comment only asked to migrate the radio line into this note."`  This problem names the unasked edit to the
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
          "check": "scope",
          "note": "Ideas/idea-harrow-point.md",
          "line": 13,
          "what": "The comment ruled out the hotel sale for Mara's story only and said the town can still have it. This rejects the town's hotel sale of the harbour cottages and pier, which the writer kept open."
        }
      ]
    },
    {
      "unit": "u3",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The causeway line was capitalised and given a full stop, but no comment asked for that. The comment only asked to migrate the radio line into this note."
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
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  The scope problems it raises are filed as `fix` verdicts on units, not as `missed` entries. One is on u2 (`"verdict":"fix"`, "the rejection reaches wider than you asked") and one is on u3 (`"verdict":"fix"`, "The causeway line ... was capitalised and given a full stop"). The check expects exactly this.
PASS  judge-shape   Evidence: - The reply is JSON with `"batch":"b1"`, `"round":0`, `"units"`, and `"missed":[]`. - `units` has exactly one entry each for u1, u2, and u3. It has no other units. - u1: `"verdict":"approve","problems":[]`. The verdict is approve and the problems list is empty. - u2: `"verdict":"fix"`, with one problem: `{"check":"scope","note":"Ideas/idea-harrow-point.md","line":13,...}`. The check `sc
PASS  judge-u1-approve   u1's verdict in the final reply is `approve` with an empty problems list:  `{"unit":"u1","verdict":"approve","problems":[]}`  That matches the PASS condition. The scope problems the reply raises belong to other units (u2 for `Ideas/idea-harrow-point.md` line 13, u3 for the causeway line in `Ideas/idea-mara-lighthouse.md` line 10), not to u1.
PASS  judge-u2-fix-scope-town   The verdict for u2 is `fix`: `{"unit":"u2","verdict":"fix", ...}`.  It has one problem, and its check is `scope`. It names the town's note: `"note":"Ideas/idea-harrow-point.md"`. It says the rejection went wider than the writer's comment allowed: "Your comment rejects the hotel sale only for Mara's story and says the town can still have it. This town-level hotel idea was rejected anyway, so the r
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `fix`: `{"unit":"u3","verdict":"fix",...}`  Its one problem uses check `scope` and names the unasked edit to the causeway line, both the capital and the full stop: `{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line next to the migrated radio line was capitalised and given a full stop, though no comment asked for it to be edited."}`  The pr
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-harrow-point.md","line":13,"what":"Your comment rejects the hotel sale only for Mara's story and says the town can still have it. This town-level hotel idea was rejected anyway, so the rejection reaches wider than you asked."}]},{"unit":"u3","verdict":"fix","problems":[{"check":"scope","note":"Ideas/idea-mara-lighthouse.md","line":10,"what":"The causeway line next to the migrated radio line was capitalised and given a full stop, though no comment asked for it to be edited."}]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Both batch items have units in the record, and neither shows up as missed: - u1 (the hotel-sale comment in Ideas/idea-mara-lighthouse.md): `{ "unit": "u1", "verdict": "approve", "problems": [] }` - u3 (the radio line from brain-dump.md): `"unit": "u3", "verdict": "fix"`  The over-wide rejection is filed as a `fix` on u2, not as a `missed` entry
PASS  judge-shape   The reply is valid JSON with `batch` ("b1"), `round` (0), `units`, and `missed` ([]).  **Units:** There is exactly one entry each for u1, u2, and u3, and no other units appear.  **u1:** `{ "unit": "u1", "verdict": "approve", "problems": [] }`. The verdict is approve and the problems list is empty, as required.  **u2:** `"verdict": "fix"`, with one problem: - `"check": "scope"` is one of the allow
PASS  judge-u1-approve   u1's entry in the final reply is:  `{ "unit": "u1", "verdict": "approve", "problems": [] }`  The verdict is `approve` and the problems list is empty, which is what the check requires. The `fix` verdicts in the reply belong to u2 and u3, which this check does not cover.
PASS  judge-u2-fix-scope-town   Evidence:  - **u2's verdict is `fix`:** `"unit": "u2", "verdict": "fix"` - **The problem uses the `scope` check:** `"check": "scope"` - **It names the town's note:** `"note": "Ideas/idea-harrow-point.md"` - **It says the rejection went past the writer's scope:** "The comment rejects the hotel sale for Mara's story only and says the town can still have it. Rejecting the hotel chain buying the harb
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `"verdict": "fix"`, so the unit was not approved.  u3 has one problem, and it has `"check": "scope"`. It names the unasked edit to the causeway line:  > "The causeway line was recapitalised and given a full stop. No comment asked for that edit. The comment only asked to move the radio line into this note."  That names both parts of the change, the capital ("recapitalised") and the
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
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
          "check": "scope",
          "note": "Ideas/idea-harrow-point.md",
          "line": 13,
          "what": "The comment rejects the hotel sale for Mara's story only and says the town can still have it. Rejecting the hotel chain buying the harbour cottages and pier in the Harrow Point note makes the rejection wider than the writer asked."
        }
      ]
    },
    {
      "unit": "u3",
      "verdict": "fix",
      "problems": [
        {
          "check": "scope",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The causeway line was recapitalised and given a full stop. No comment asked for that edit. The comment only asked to move the radio line into this note."
        }
      ]
    }
  ],
  "missed": []
}
````

### Case 4: `migration-verifier-04-standalone`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units in the batch are accounted for under `units`: - `{"unit":"u1","verdict":"fix",...}`. The standalone problem with u1 is recorded as a `fix`, not as a `missed` entry. The reply says: "'What happened that winter' points to something the Area Note never says." - `{"unit":"u2","verdict":"approve","problems":[]}`
PASS  judge-shape   The reply is valid JSON with `batch` ("b1"), `round` (0), `units`, and `missed` ([]).  **Units:** there is exactly one entry for u1 and one for u2, and no other units appear.  **u1:** `"verdict":"fix"` with two problems: - `{"check":"lost-detail","note":"char-mara.md","line":20,...}` - `{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' points to something t
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict":"fix"`, and two problems name the missing event:  - **lost-detail** on char-mara.md line 20: "The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy leaves out the sale, the licence, the cannery and Tobias's death, and keeps only the grudge." - **standalone** on char-mara.md line 20: "'What happened that winter' p
PASS  judge-u2-approve-rationale   u2's entry in the reply is `{"unit":"u2","verdict":"approve","problems":[]}`. The verdict is `approve` and the problems list is empty. No problem says the Rationale line ("I like that her discipline looks like penance.") should be rewritten, can't stand alone, or is in the wrong voice. Both problems in the reply belong to u1, not u2.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"char-mara.md","line":20,"what":"The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy leaves out the sale, the licence, the cannery and Tobias's death, and keeps only the grudge."},{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' points to something the Area Note never says. With no Idea Note beside it, a reader can't tell which winter is meant or what Mara's mother did."}]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units are accounted for in `units`: - u1 has verdict `"fix"`, with `lost-detail` and `standalone` problems. The check says a copy that can't stand alone belongs under `fix`, not `missed`, and that is how the reply handles it. - u2 has verdict `"approve"`.
PASS  judge-shape   The reply is valid JSON with all four top-level keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, `"missed":[]`.  **Units:** there is exactly one entry for each unit handed over, and no others: - `"unit":"u1","verdict":"fix"` - `"unit":"u2","verdict":"approve"`  **Verdicts:** both verdicts are allowed values (`fix` and `approve`).  **u1 (`fix`) has two problems:** 1. `{"check":"lost-detail","no
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict":"fix"`.  Two problems name the missing event: - **lost-detail:** "The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy leaves out the sale, the licence, the cannery and Tobias's death, and keeps only the grudge." - **standalone:** "'What happened that winter' points to nothing in the Area Note. Without the sourc
PASS  judge-u2-approve-rationale   The reply gives u2 this verdict:  `{"unit":"u2","verdict":"approve","problems":[]}`  The verdict is `approve` and the problems list is empty. Nothing says the Rationale line ("I like that her discipline looks like penance.") should be rewritten, can't stand alone, or is in the wrong voice. The only problems in the reply belong to u1, which is not what this check covers.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"char-mara.md","line":20,"text_ignored":null,"what":"The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy leaves out the sale, the licence, the cannery and Tobias's death, and keeps only the grudge."},{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' points to nothing in the Area Note. Without the source, a reader can't tell which winter it means or what her mother did."}]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[]}
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  Both units are accounted for in `units`: - u1 got `"verdict":"fix"`, with problems including `"check":"standalone"` ("'What happened that winter' points at nothing in the Area Note"). The check says a copy that can't stand alone belongs under `fix`, not `missed`, and that is how it was recorded. - u2 got `"verdict":"approve"`.
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[]`.  - **Units:** There is exactly one entry for each unit handed over, `"unit":"u1"` and `"unit":"u2"`, and no other units appear. - **Verdicts:** u1 is `"verdict":"fix"` and u2 is `"verdict":"approve"`. Both are allowed values. - **Fix has problems:** u1 lists two problems. - **Appro
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict":"fix"`, and both of its problems name the event the copy leaves out:  - **lost-detail**, char-mara.md line 20: "The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy leaves out the sale, the licence, the cannery and Tobias's death, and keeps only that Mara never forgave her." - **standalone**, char-mara.md line 2
PASS  judge-u2-approve-rationale   The reply gives u2 the verdict `approve` with no problems: `{"unit":"u2","verdict":"approve","problems":[]}`.  It doesn't flag the Rationale line ("I like that her discipline looks like penance.") for rewriting, for failing to stand alone, or for being in the wrong voice. Both problems in the reply belong to u1, not u2.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"fix","problems":[{"check":"lost-detail","note":"char-mara.md","line":20,"what":"The source says Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. The copy leaves out the sale, the licence, the cannery and Tobias's death, and keeps only that Mara never forgave her."},{"check":"standalone","note":"char-mara.md","line":20,"what":"'What happened that winter' points at nothing in the Area Note. Read alone, the line doesn't say which winter or what her mother did."}]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[]}
````

### Case 5: `migration-verifier-05-missed-line`

#### Run 1

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list has exactly one entry, and it is line A:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara, but it was never copied to char-mara and no question asks about it."}] ```  The quoted text matches line A
PASS  judge-shape   The reply is valid JSON with all four top-level keys: `"batch":"b1"`, `"round":0`, `"units"`, and `"missed"`.  - **Units:** there is exactly one entry, for u1, and none for any other unit: `{"unit":"u1","verdict":"approve","problems":[]}` - **Verdict:** `"approve"` is one of the allowed values. - **Approve has no problems:** the `problems` list is empty (`[]`), as required. - **Fix rule:** no `fi
PASS  judge-u1-approve   The check covers only u1. The reply gives u1 this verdict: `{"unit":"u1","verdict":"approve","problems":[]}`.  The verdict is `approve` and the `problems` array is empty. No problem says the relief keeper or the decommissioning was left behind or should have graduated. The reply's `missed` entry is about a different line (line 10, Tobias's oilskin coat), not line B. It falls outside this check an
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara, but it was never copied to char-mara and no question asks about it."}]}
````

#### Run 2

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list holds exactly one entry, and it is line A:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment below it sends it to char-mara, but it was never added to char-mara and no question asks about it."}] ```  Lines B (watch room / Oban / 
PASS  judge-shape   The reply is valid JSON and has all four required keys: `"batch":"b1"`, `"round":0`, `units`, and `missed`.  - **Units:** `units` holds exactly one entry, for the handed unit u1: `{"unit":"u1","verdict":"approve","problems":[]}`. It lists no other unit and does not repeat u1. - **Verdict:** The verdict is `"approve"`, which is an allowed value. - **Problems:** The `approve` has an empty problems 
PASS  judge-u1-approve   The check asks only about unit u1's verdict. The text gives:  `{"unit":"u1","verdict":"approve","problems":[]}`  The verdict is `approve` and the `problems` list is empty. No problem says the relief keeper or the decommissioning was left behind or should have graduated. The separate `missed` entry is about line 10, the oilskin coat, not line B, so it does not affect this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment below it sends it to char-mara, but it was never added to char-mara and no question asks about it."}]}
````

#### Run 3

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list has exactly one entry, and it is line A, the oilskin coat line:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara, but it was never copied there."}] ```  - The quoted text matches line A word for wo
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[...]`.  - **Units:** `units` has exactly one entry, `{"unit":"u1","verdict":"approve","problems":[]}`. It covers u1 and no other unit. - **Verdict:** `"approve"` is one of the allowed values. - **Approve rule:** the `approve` verdict has an empty `problems` list (`"problems":[]`), as 
PASS  judge-u1-approve   The check asks only about u1's verdict. The text gives `{"unit":"u1","verdict":"approve","problems":[]}`. The verdict is `approve` and the problems list is empty. There is no complaint that the relief keeper or the decommissioning was left behind.  The reply also has a separate `missed` entry for line 10, about Tobias's oilskin coat. That is not about u1 or line B, so this check does not cover it
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara, but it was never copied there."}]}
````

### Case 6: `migration-verifier-06-clean-batch`

#### Run 1

Grades:

````
PASS  judge-all-five-approve   All five units are approved, and none has a problem:  - `{"unit":"u1","verdict":"approve","problems":[]}` - `{"unit":"u2","verdict":"approve","problems":[]}` - `{"unit":"u3","verdict":"approve","problems":[]}` - `{"unit":"u4","verdict":"approve","problems":[]}`: nothing is raised about the reason comment "%% It makes her too cosy. %%". - `{"unit":"u5","verdict":"approve","problems":[]}`: nothing 
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All five units have a record entry: - `{"unit":"u1","verdict":"approve","problems":[]}` - `{"unit":"u2","verdict":"approve","problems":[]}` - `{"unit":"u3","verdict":"approve","problems":[]}` - `{"unit":"u4","verdict":"approve","problems":[]}` - `{"unit":"u5","verdict":"approve","problems":[]}`
PASS  judge-shape   The reply is valid JSON with the required top-level keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  - **Units:** There is exactly one entry for each handed unit and no others: `{"unit":"u1",...}`, `{"unit":"u2",...}`, `{"unit":"u3",...}`, `{"unit":"u4",...}`, `{"unit":"u5",...}`. Nothing is duplicated and nothing extra appears. - **Verdicts:** All five are `"verdict":"appr
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
PASS  judge-all-five-approve   All five units have the verdict `approve`, and every `problems` list is empty:  - `{"unit":"u1","verdict":"approve","problems":[]}` - `{"unit":"u2","verdict":"approve","problems":[]}` - `{"unit":"u3","verdict":"approve","problems":[]}` - `{"unit":"u4","verdict":"approve","problems":[]}`: nothing is raised about the reason comment "%% It makes her too cosy. %%". - `{"unit":"u5","verdict":"approve"
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed":[]`.  All five expected units are present in the record: `{"unit":"u1",...}`, `{"unit":"u2",...}`, `{"unit":"u3",...}`, `{"unit":"u4",...}`, `{"unit":"u5",...}`. These cover the four brain-dump units (u1, u2, u3 merged, u5) and the idea-file comment (u4).
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  **One entry per handed unit, and nothing else:** `units` contains exactly five entries: - `{"unit":"u1","verdict":"approve","problems":[]}` - `{"unit":"u2","verdict":"approve","problems":[]}` - `{"unit":"u3","verdict":"approve","problems":[]}` - `{"unit":"u4","verdict":"approve",
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
PASS  judge-all-five-approve   All five units, u1 to u5, have the verdict `approve` and an empty problems list. No unit is marked `fix`.  - u1: `{"unit": "u1", "verdict": "approve", "problems": []}` - u2: `{"unit": "u2", "verdict": "approve", "problems": []}` - u3: `{"unit": "u3", "verdict": "approve", "problems": []}` - u4: `{"unit": "u4", "verdict": "approve", "problems": []}`. No problem is raised on the reason comment "%% 
PASS  judge-missed-empty   The check passes when the reply's `missed` list is empty. The reply contains `"missed": []`, so nothing is listed as missed.  The record also has a unit for every expected item in the batch: `"unit": "u1"`, `"unit": "u2"`, `"unit": "u3"`, `"unit": "u4"`, and `"unit": "u5"`. These cover the four brain-dump units (u1, u2, u3 merged, and u5) and the idea-file comment (u4).
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch": "b1"`, `"round": 0`, `"units": [...]`, `"missed": []`.  - **Units:** `units` has exactly five entries, one each for `"unit": "u1"`, `"u2"`, `"u3"`, `"u4"` and `"u5"`. None is duplicated, and no unit appears that wasn't handed over. - **Verdicts:** every entry has `"verdict": "approve"`, which is an allowed value. No `fix` verdicts app
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch": "b1", "round": 0, "units": [{"unit": "u1", "verdict": "approve", "problems": []}, {"unit": "u2", "verdict": "approve", "problems": []}, {"unit": "u3", "verdict": "approve", "problems": []}, {"unit": "u4", "verdict": "approve", "problems": []}, {"unit": "u5", "verdict": "approve", "problems": []}], "missed": []}
````

### Case 7: `migration-verifier-07-asked-by-meaning`

#### Run 1

Grades:

````
PASS  judge-all-three-approve   All three units have the verdict `approve` and an empty problems list:  - u1: `{"unit":"u1","verdict":"approve","problems":[]}`. It was not fixed for the comma splice or the capital. - u2: `{"unit":"u2","verdict":"approve","problems":[]}`. It was not fixed for the added full stop. - u3: `{"unit":"u3","verdict":"approve","problems":[]}`  No unit has the verdict `fix`. The reply also has `"missed":
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[]`.  - **Units:** `units` has exactly three entries, one each for u1, u2, and u3. None is repeated and no other unit appears: `{"unit":"u1",...}`, `{"unit":"u2",...}`, `{"unit":"u3",...}`. - **Verdicts:** every verdict is allowed. All three are `"verdict":"approve"`. - **Problems:** e
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
PASS  judge-all-three-approve   Evidence: all three units are approved and none lists a problem. - u1: `{"unit": "u1", "verdict": "approve", "problems": []}`. It was not fixed for the comma splice or the capital. - u2: `{"unit": "u2", "verdict": "approve", "problems": []}`. It was not fixed for the added full stop. - u3: `{"unit": "u3", "verdict": "approve", "problems": []}`  No unit has the verdict `fix`, and `"missed": []` is
PASS  judge-shape   The reply is valid JSON with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed": []`.  - **Units:** There is exactly one entry each for u1, u2 and u3, and no other units appear.   - `{"unit": "u1", "verdict": "approve", "problems": []}`   - `{"unit": "u2", "verdict": "approve", "problems": []}`   - `{"unit": "u3", "verdict": "approve", "problems": []}` - **Verdicts:** All three are `approve`
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"batch": "b1", "round": 0, "units": [{"unit": "u1", "verdict": "approve", "problems": []}, {"unit": "u2", "verdict": "approve", "problems": []}, {"unit": "u3", "verdict": "approve", "problems": []}], "missed": []}
````

#### Run 3

Grades:

````
PASS  judge-all-three-approve   All three units were approved and none of them lists a problem: - `{"unit":"u1","verdict":"approve","problems":[]}`: the spelling fix, which also splits the comma splice and adds the capital, is approved. It is not flagged as out of scope. - `{"unit":"u2","verdict":"approve","problems":[]}`: the grammar tidy, including the added full stop, is approved. - `{"unit":"u3","verdict":"approve","problem
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, `"missed":[]`.  - **Unit coverage:** `units` has exactly three entries, one each for `"unit":"u1"`, `"unit":"u2"` and `"unit":"u3"`. None is duplicated and no other unit appears. - **Verdicts:** All three are `"verdict":"approve"`, which is an allowed value. - **Approve/problems rule:** Each approve
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
PASS  judge-f1-to-f4-asked   Evidence for each flag:  - **f1:** `"verdict":"asked"`, with `"asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}`. The kind is comment, and it names the listed comment by its text and note. - **f2:** `"verdict":"asked"`, with `"asked_by":{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% Agent, 
PASS  judge-f5-not-asked   The check requires f5 to have the verdict `not-asked` with `asked_by` set to null. The text under test contains this entry for f5:  `{"flag":"f5","verdict":"not-asked","asked_by":null}`  The verdict is `"not-asked"` and `asked_by` is `null`. f5 is not credited to the typed request, which is the failure case the check describes. That request is instead attached to f4 (`"kind":"request"`), and that
PASS  judge-shape   The reply is valid JSON with a `flags` list. It has exactly one entry for each of f1–f5 and no entries for any other flag:  - f1: `"verdict":"asked"`, `asked_by`: `{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}` - f2: `"verdict":"asked"`, `asked_by`: `{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% 
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
PASS  judge-f1-to-f4-asked   Evidence, flag by flag:  - **f1**: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"}`. The kind is comment and the text matches the listed comment exactly. - **f2**: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"brain-dump.md","line":11,"text":"%% Agent, mark this one co
PASS  judge-f5-not-asked   The final reply records f5 as `{"flag":"f5","verdict":"not-asked","asked_by":null}`.  - **Verdict:** `"not-asked"` - **`asked_by`:** `null`  The typed request was used only for f4 (`"kind":"request"`), not for f5. So the reply did not credit the Tobias edit to the request just because the request mentions Tobias.
PASS  judge-shape   The reply is valid JSON with a `flags` list. It has exactly one entry for each of f1–f5 and no others.  - **f1**: `"verdict":"asked"`, `asked_by` is an object (`"kind":"comment","note":"Ideas/idea-mara-lighthouse.md","line":12,"text":"%% Agent, please correct the spelling in that line. %%"`) - **f2**: `"verdict":"asked"`, `asked_by` is an object (`"kind":"comment","note":"brain-dump.md","line":11
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
PASS  judge-f1-to-f4-asked   All four checked flags have the verdict `asked` and the right `asked_by` kind and source.  - **f1**: `"verdict": "asked"`, `"asked_by": { "kind": "comment", "note": "Ideas/idea-mara-lighthouse.md", "line": 12, "text": "%% Agent, please correct the spelling in that line. %%" }`. The kind is comment, and the text matches the listed comment exactly. - **f2**: `"verdict": "asked"`, `"asked_by": { "ki
PASS  judge-f5-not-asked   The f5 entry reads `"flag": "f5", "verdict": "not-asked", "asked_by": null`.  The verdict is `not-asked` and `asked_by` is `null`, which is what the check requires. The reply does not credit the typed request ("In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias.") for f5. It uses that request only for f4.
PASS  judge-shape   The reply is valid JSON with a `flags` list, and it meets every rule:  - **One entry per handed flag, no extras:** the entries are `"flag": "f1"`, `"f2"`, `"f3"`, `"f4"` and `"f5"`. Each appears once, and no other flag is listed. - **Verdicts are allowed values:**   - f1, f2, f3 and f4 are `"verdict": "asked"`.   - f5 is `"verdict": "not-asked"`. - **Every `asked` verdict has an `asked_by` object
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{
  "flags": [
    {
      "flag": "f1",
      "verdict": "asked",
      "asked_by": { "kind": "comment", "note": "Ideas/idea-mara-lighthouse.md", "line": 12, "text": "%% Agent, please correct the spelling in that line. %%" }
    },
    {
      "flag": "f2",
      "verdict": "asked",
      "asked_by": { "kind": "comment", "note": "brain-dump.md", "line": 11, "text": "%% Agent, mark this one committed. %%" }
    },
    {
      "flag": "f3",
      "verdict": "asked",
      "asked_by": { "kind": "comment", "note": "char-mara.md", "line": 13, "text": "%% Agent, Mara is thirty-four now, not thirty-two. Update this. %%" }
    },
    {
      "flag": "f4",
      "verdict": "asked",
      "asked_by": { "kind": "request", "note": "", "line": null, "text": "In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias." }
    },
    {
      "flag": "f5",
      "verdict": "not-asked",
      "asked_by": null
    }
  ]
}
````

### Case 9: `migration-verifier-09-flags-not-asked`

#### Run 1

Grades:

````
PASS  judge-f1-f2-f3-not-asked   All three flags are `not-asked` with `asked_by` set to null:  - **f1:** `{"flag":"f1","verdict":"not-asked","asked_by":null}` - **f2:** `{"flag":"f2","verdict":"not-asked","asked_by":null}` - **f3:** `{"flag":"f3","verdict":"not-asked","asked_by":null}`  The reply avoided the main trap. It did not credit f3 to the spelling comment ("%% Agent, please correct the spelling in that line. %%"). It cor
PASS  judge-f4-asked   Evidence: The reply gives f4 the verdict `"verdict":"asked"`. Its `asked_by` is `{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}`. That is kind `comment`, and it names the right comment by its text ("Agent, fix the typo.") and by its note (idea-harrow-point). Since the verdict is `asked` and the attribution points to the comment that requested 
PASS  judge-shape   The reply is valid JSON with a `flags` list holding exactly one entry for each handed flag (f1, f2, f3, f4) and no others:  - f1: `"verdict":"not-asked","asked_by":null`, a valid pairing. - f2: `"verdict":"not-asked","asked_by":null`, a valid pairing. - f3: `"verdict":"not-asked","asked_by":null`, a valid pairing. - f4: `"verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-poi
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
PASS  judge-f1-f2-f3-not-asked   All three flags carry the required verdict, and each has a null `asked_by`:  - **f1**: `{"flag":"f1","verdict":"not-asked","asked_by":null}` - **f2**: `{"flag":"f2","verdict":"not-asked","asked_by":null}` - **f3**: `{"flag":"f3","verdict":"not-asked","asked_by":null}`  The reply avoided the main trap. It did not credit f3 to the spelling comment.  f4 was marked `asked`, but the check covers only 
PASS  judge-f4-asked   Evidence: the reply's f4 entry reads `{"flag":"f4","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}}`.  - The verdict is `"asked"`, as required. - `asked_by.kind` is `"comment"`. - The comment it names is in the right note (`"note":"Ideas/idea-harrow-point.md"`) and has the right text (`"text":"%% Agent, fix the typo
PASS  judge-shape   The reply is valid JSON with a `flags` list. It has exactly four entries, one each for f1, f2, f3, and f4, and no other flags:  - `{"flag":"f1","verdict":"not-asked","asked_by":null}`: not-asked, and `asked_by` is null ✓ - `{"flag":"f2","verdict":"not-asked","asked_by":null}`: not-asked, and `asked_by` is null ✓ - `{"flag":"f3","verdict":"not-asked","asked_by":null}`: not-asked, and `asked_by` is
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
PASS  judge-f1-f2-f3-not-asked   The check requires f1, f2, and f3 to each have verdict `not-asked` with `asked_by` null. The reply meets that for all three:  - **f1:** `{"flag":"f1","verdict":"not-asked","asked_by":null}` - **f2:** `{"flag":"f2","verdict":"not-asked","asked_by":null}` - **f3:** `{"flag":"f3","verdict":"not-asked","asked_by":null}`. The reply avoided the main trap. It did not credit the "may" → "will" change to 
PASS  judge-f4-asked   The verdict for f4 is `asked`: `{"flag":"f4","verdict":"asked",...}`.  Its `asked_by` is of kind `comment` and names the right comment in the right note: `"asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}`.  The quoted text matches "Agent, fix the typo." and the note is idea-harrow-point. Both PASS conditions are met.
PASS  judge-shape   The reply is valid JSON with a `flags` list. It has exactly one entry each for f1, f2, f3, and f4, and no entry for any other flag.  - f1: `"verdict":"not-asked"`, `"asked_by":null` - f2: `"verdict":"not-asked"`, `"asked_by":null` - f3: `"verdict":"not-asked"`, `"asked_by":null` - f4: `"verdict":"asked"`, `"asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"flags":[{"flag":"f1","verdict":"not-asked","asked_by":null},{"flag":"f2","verdict":"not-asked","asked_by":null},{"flag":"f3","verdict":"not-asked","asked_by":null},{"flag":"f4","verdict":"asked","asked_by":{"kind":"comment","note":"Ideas/idea-harrow-point.md","line":10,"text":"%% Agent, fix the typo. %%"}}]}
````

