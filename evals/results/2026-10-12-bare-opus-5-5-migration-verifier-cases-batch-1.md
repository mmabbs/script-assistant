# 2026-10-12 Bare Run: Migration-verifier Cases, Batch 1

This run was done by hand with `_tools/research-run.py --suite migration-verifier`, outside `claude plugin eval`. The runner ran every grader in each case's `graders/` folder: tool_used graders in code, llm graders through a Claude Opus 5.5 judge. Claude then checked every reply against its Pass line in eval-cases-migration-verifier.md 04 by parsing the JSON in code, not only through the judges. The session that ran the cases did not write them.

## What Was Run

- **Date:** 2026-10-12, 14:31 to 14:34 EDT.
- **Model:** bare `claude-opus-5-5`, with no agent. The migration-verifier isn't built.
- **Claude Code:** 2.1.296.
- **Runs:** 27. Nine cases, three runs each, at most five at a time.
- **Prompt:** each case's `prompt.md` body, word for word, as the agent would get it, starting "This is the migration-verifier's batch check" or the flags-call equivalent. No other instructions.
- **Tools:** Read, Glob, Grep, from every case's `allowed_tools`.
- **Rules given:** `rules/migrator-rules.md`, copied by each fixture from `_fixtures/rules/migrator-rules.md`, which is byte-identical to the plugin's `references/migrator-rules.md` (checked with `cmp` before the run).
- **Command:**

```bash
OUT=/var/folders/jp/t3th_wsd03xgpgdnsn9ys63w0000gn/T/tmp.f9Zbkrr1NK
python3 _tools/research-run.py --suite migration-verifier --out "$OUT/mv-bare" --runs 3
```

- **What the runner launches per run and per judge:** the same as in `results/2026-10-12-bare-opus-5-5-research-cases-batch-1.md`, What Was Run: `--strict-mcp-config` on every call, no CLAUDE.md, rules, or output style loaded.
- **Errors and timeouts:** none. Every run exited 0. No run was repeated.
- **Before the batch,** a smoke run of case 1, one run, passed every check. It isn't counted.

## Summary Table

"Pass line held" uses the approved Pass lines in eval-cases-migration-verifier.md 04, checked in code against each reply's JSON. "All checks" counts runs where every grader passed, the shape judge included. Cost is the three runs' model cost, judges not included.

| Case | Pass line held | All checks | Cost |
| --- | --- | --- | --- |
| 1 `migration-verifier-01-lost-detail` | 3 of 3 | 3 of 3 | $0.75 |
| 2 `migration-verifier-02-status` | 3 of 3 | 3 of 3 | $0.81 |
| 3 `migration-verifier-03-scope` | 3 of 3 | 3 of 3 | $0.83 |
| 4 `migration-verifier-04-standalone` | 3 of 3 | 3 of 3 | $0.77 |
| 5 `migration-verifier-05-missed-line` | 3 of 3 | 3 of 3 | $0.77 |
| 6 `migration-verifier-06-clean-batch` | 3 of 3 | 3 of 3 | $0.90 |
| 7 `migration-verifier-07-asked-by-meaning` | 3 of 3 | 3 of 3 | $0.74 |
| 8 `migration-verifier-08-flags-asked` | 3 of 3 | 3 of 3 | $0.88 |
| 9 `migration-verifier-09-flags-not-asked` | 3 of 3 | 3 of 3 | $0.81 |
| **Total** | **27 of 27** | **27 of 27** | **$7.26** |

## Findings

1. **Bare Claude passes every batch-1 case, in every run.** It catches each planted error, approves each correct unit, and gives the clean batch five approvals. Every verdict is the same across the three runs of a case. So batch 1 can't show what the migration-verifier's instructions add. The cases still catch an agent that does worse than bare Claude. Harder plants would be needed to tell the two apart.
2. **The cases bare Claude might have been expected to miss, it didn't.**
    - Case 3: all three runs approve u1 and fix u2 for reading the rejection wider than "for Mara's story only." Each fixes u3 for the unasked edit to the causeway line, not for the copy.
    - Case 4: all three fix u1, naming both `lost-detail` and `standalone`, and approve u2 with no problem on the Rationale line.
    - Case 5: `missed` holds line A only, in all three. None names the line with a `questions` entry, the `could_not` line, or the untagged line.
    - Case 9: all three call f3 `not-asked`, though a spelling comment sits on its line, because "may" became "will."
    - Case 2: no run asks to raise u1 to committed.
3. **Observed, not graded: a problem's `note` sometimes names the source, not the copy.** In case 1 runs 2 and 3, and case 4 runs 1 and 3, every problem's `note` is `brain-dump.md`, with the copy's note named only in `what`. spec-migration-verifier.md 05.1 says a problem's `note` and `line` are "where it shows," which reads as the copy. The other 23 runs name the copy's note. The shape judge doesn't check this field, and the prompt's example gives only `<note path>`.

## Caveats

1. **One judge call per check, not repeated.** The code check of every verdict against the Pass lines agrees with the judges in every run.
2. **The bare prompt names the agent's role** because it is the agent's prompt word for word. It carries none of the agent's instructions.
3. **Cost:** the runs cost $7.26, from their streams. The batch's printed total, judges included, was $9.24. The smoke run cost $0.33.
4. **The raw run folders are in a temp folder** (the path under Command) and go when the Mac restarts. Each run's reply and grades are copied below.

## Full Outputs

Each run shows its grades, then its final reply.

### Case 1: `migration-verifier-01-lost-detail`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three lines in the batch appear as units in the reply: - u1 is marked `"verdict": "fix"`. - u2 is marked `"verdict": "fix"`. - u3 is marked `"verdict": "approve"`.  The two wrong copies (u1 lost the age "nine", and u2 lost the hedge "Maybe") are correctly logged as `fix` entries, not as `missed` entries.
PASS  judge-shape   The reply is a single JSON object with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`. Each rule holds:  - **Units handed, once each, nothing extra:** the `units` array has exactly three entries, `"unit": "u1"`, `"unit": "u2"` and `"unit": "u3"`. - **Every verdict is `approve` or `fix`:**   - u1 → `"verdict": "fix"`   - u2 → `"verdict": "fix"`   - u3 → `"verdict": "approve"` - **Every
PASS  judge-u1-fix-lost-age   The verdict for u1 is `fix`: `"unit": "u1", "verdict": "fix"`.  It has one problem, and that problem is about the idea-tobias copy and the lost age: - `"check": "lost-detail"` - `"note": "Ideas/idea-tobias.md"` - `"line": 10` - `"what": "The source says Mara was nine when Tobias drowned, but this copy says only \"when she was a child.\" Put the age back: \"when she was nine.\""`  The problem poin
PASS  judge-u2-fix-lost-maybe   u2's verdict is `fix`: `"unit": "u2", "verdict": "fix"`.  It has one problem, with `"check": "lost-detail"`, and that problem names the lost hedge: "The source starts with \"Maybe,\" but the copy states the father hiding the logbook as a fact. Put the hedge back, for example: \"Maybe Mara's father hid the old keeper's logbook somewhere in the tower before he died.\""  That says the copy dropped t
PASS  judge-u3-approve   The final reply gives u3 the following entry:  `{ "unit": "u3", "verdict": "approve", "problems": [] }`  The verdict is `approve` and the problems list is empty. The reply does not flag the rewording from "even though" to "still ... though," so no problem is raised against u3.
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
          "check": "lost-detail",
          "note": "Ideas/idea-tobias.md",
          "line": 10,
          "what": "The source says Mara was nine when Tobias drowned, but this copy says only \"when she was a child.\" Put the age back: \"when she was nine.\""
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
          "what": "The source starts with \"Maybe,\" but the copy states the father hiding the logbook as a fact. Put the hedge back, for example: \"Maybe Mara's father hid the old keeper's logbook somewhere in the tower before he died.\""
        }
      ]
    },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units appear in the `units` array: - u1 is `"verdict": "fix"`, because the age "nine" was lost from the copy. - u2 is `"verdict": "fix"`, because the "Maybe" hedge was lost. - u3 is `"verdict": "approve"`.  The copy problems in u1 and u2 are reported as `fix` entries, not as `missed` entries. That matches the check's rule.
PASS  judge-shape   Evidence: the reply is a JSON findings object with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`.  - **Unit coverage:** `units` has exactly three entries, `"unit": "u1"`, `"unit": "u2"`, and `"unit": "u3"`. Each appears once, and no other unit is listed. - **u1:** `"verdict": "fix"` with one problem, `"check": "lost-detail"`. Its note reads "The copy in Ideas/idea-tobias.md says Tobi
PASS  judge-u1-fix-lost-age   Evidence: u1's verdict is `"verdict": "fix"`. Its single problem points at the idea-tobias copy and names the lost age:  > "The copy in Ideas/idea-tobias.md says Tobias drowned 'when she was a child', but the source says she was nine. Put the age back: 'when she was nine'."  The problem names the right file (Ideas/idea-tobias.md), quotes the changed wording ("a child"), and states that the source
PASS  judge-u2-fix-lost-maybe   u2's verdict is `fix`: `"unit": "u2", "verdict": "fix"`.  Its one problem has `"check": "lost-detail"` and names the lost hedge directly: "The source starts with 'Maybe', but the copy in Ideas/idea-mara-lighthouse.md states the hidden logbook as fact. Put the hedge back so the copy shows the writer is only floating the idea."  That names both the missing "Maybe" and the result, a possibility turn
PASS  judge-u3-approve   The check needs u3 to be `approve` with no problems. The final reply contains:  `{ "unit": "u3", "verdict": "approve", "problems": [] }`  The verdict is `approve` and the `problems` array is empty. The reply did not flag the rewording ("even though" to "still ... though"), and it raised nothing else against u3.
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
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 10,
          "what": "The copy in Ideas/idea-tobias.md says Tobias drowned 'when she was a child', but the source says she was nine. Put the age back: 'when she was nine'."
        }
      ]
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 13,
          "what": "The source starts with 'Maybe', but the copy in Ideas/idea-mara-lighthouse.md states the hidden logbook as fact. Put the hedge back so the copy shows the writer is only floating the idea."
        }
      ]
    },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units appear in `units`. u1 and u2 are marked `"verdict": "fix"`, which is the right category for a unit with a wrong copy rather than a `missed` entry. u3 is marked `"verdict": "approve"`. No source line was put in `missed`.
PASS  judge-shape   The reply is a JSON findings object with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed": []`. Each rule holds:  - **Units:** there is exactly one entry each for `"unit": "u1"`, `"unit": "u2"` and `"unit": "u3"`, and no other units appear. - **u1:** `"verdict": "fix"` with one problem: `"check": "lost-detail"`, `"what": "The copy in idea-tobias says Tobias drowned 'when she was a child', 
PASS  judge-u1-fix-lost-age   u1's verdict is `"verdict": "fix"`. It has one problem:  - `"check": "lost-detail"`, `"note": "brain-dump.md"`, `"line": 10`, `"what": "The copy in idea-tobias says Tobias drowned 'when she was a child', but the source says 'when she was nine'. Put the exact age back so the drowning copy keeps the writer's detail on its own."`  This problem names the idea-tobias copy. It says the age "nine" was r
PASS  judge-u2-fix-lost-maybe   u2's verdict is `fix`: `"unit": "u2", "verdict": "fix"`.  It has one problem, with `"check": "lost-detail"`, which is one of the two accepted checks. That problem names the lost hedge directly: "The source opens with 'Maybe', but the copy says flatly that Mara's father hid the logbook, so it reads as settled. Keep the writer's hedge, for example 'Maybe Mara's father hid the old keeper's logbook s
PASS  judge-u3-approve   The reply's entry for u3 reads:  `{ "unit": "u3", "verdict": "approve", "problems": [] }`  The verdict is `approve` and the problems list is empty. The rewording from "even though" to "still ... though" was not flagged.
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
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 10,
          "what": "The copy in idea-tobias says Tobias drowned 'when she was a child', but the source says 'when she was nine'. Put the exact age back so the drowning copy keeps the writer's detail on its own."
        }
      ]
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 13,
          "what": "The source opens with 'Maybe', but the copy says flatly that Mara's father hid the logbook, so it reads as settled. Keep the writer's hedge, for example 'Maybe Mara's father hid the old keeper's logbook somewhere in the tower before he died.'"
        }
      ]
    },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

### Case 2: `migration-verifier-02-status`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  The reply records all three units. It gives u1 and u2 `"verdict": "fix"` for status problems, and it gives u3 `"verdict": "approve"`. The check treats a status error as a `fix`, not a `missed` entry, so no unit was wrongly moved into `missed`.
PASS  judge-shape   The reply holds JSON findings with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed": []`. It meets every rule in the check:  - **Each unit appears exactly once, and no others appear.** `units` has three entries: `"unit": "u1"`, `"unit": "u2"`, and `"unit": "u3"`. - **Every verdict is valid.** u1 is `"verdict": "fix"`, u2 is `"verdict": "fix"`, and u3 is `"verdict": "approve"`. - **Each `fi
PASS  judge-u1-fix-provisional-in-area-note   Evidence:  - **Verdict:** u1 has `"verdict": "fix"`, so it is not approved. - **Status problem:** u1's only problem has `"check": "status"` and `"note": "char-mara.md"`. It reads: "The source line is tagged #status/provisional, but the copy went into char-mara, an Area Note, as an untagged line. That makes it read as committed. Provisional material never goes in an Area Note." This names provisio
PASS  judge-u2-fix-below-writer-tag   The u2 verdict is `"verdict": "fix"`, and its problem names the gap between the writer's tag and the copy's tag.  The problem has check `"status"`, note `"Ideas/idea-mara-lighthouse.md"`, line 10. Its text reads: "The writer tagged the source #status/committed, but the copy carries #status/provisional in an Idea Note, which lowers the writer's status. The writer's comment also routes it to char-m
PASS  judge-u3-approve   The text gives u3 the verdict `approve` with an empty problems list:  `{ "unit": "u3", "verdict": "approve", "problems": [] }`  This is the expected result. The source line is committed. Its copy went to char-mara as the comment directed, and it carries no status tag, which is correct for an Area Note. "clockwork mechanism" means the same as "clockwork." The text raises no problems for u3.
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
          "what": "The source line is tagged #status/provisional, but the copy went into char-mara, an Area Note, as an untagged line. That makes it read as committed. Provisional material never goes in an Area Note. Take it out of char-mara and migrate it to an Idea Note (for example idea-mara-lighthouse) with its #status/provisional tag."
        }
      ],
      "fix_hint": null
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The writer tagged the source #status/committed, but the copy carries #status/provisional in an Idea Note, which lowers the writer's status. The writer's comment also routes it to char-mara. Take the copy out of the Idea Note and add it to char-mara (for example under ## General) as an untagged committed line: \"Mara has never once left Harrow Point overnight.\""
        }
      ]
    },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units appear in `units`: - u1 is `"verdict": "fix"`, with a status problem. - u2 is `"verdict": "fix"`, with a status problem. - u3 is `"verdict": "approve"`.  The two status errors are reported as `fix` verdicts, not as `missed` entries, which is what the check asks for.
PASS  judge-shape   The reply is a JSON object with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`. Every shape rule holds:  - **Units:** there is exactly one entry each for `"unit": "u1"`, `"unit": "u2"` and `"unit": "u3"`. No unit appears twice, and there are no other units. - **Verdicts:** u1 is `"verdict": "fix"`, u2 is `"verdict": "fix"`, and u3 is `"verdict": "approve"`. All are allowed values. - *
PASS  judge-u1-fix-provisional-in-area-note   Evidence: - u1's verdict is `fix`: `"unit": "u1", "verdict": "fix"`. - It has a problem under `"check": "status"` that names `"note": "char-mara.md"`. That problem says provisional material is in an Area Note: "The source is tagged #status/provisional, but the copy went into an Area Note without its tag, where an untagged line counts as committed. That raises its status. Provisional material neve
PASS  judge-u2-fix-below-writer-tag   u2's verdict is `fix`: `"unit": "u2", "verdict": "fix"`.  Its problem uses `"check": "status"` (one of the allowed checks) and names the gap between the writer's committed tag and the provisional copy: "The writer tagged the source #status/committed, but the copy says #status/provisional, which lowers a status the writer set."  It also covers the comment and placement: "The writer's comment also 
PASS  judge-u3-approve   The reply gives u3 the verdict `approve` and an empty problem list:  `{ "unit": "u3", "verdict": "approve", "problems": [] }`  The reply does not mark u3 as `fix` and names no problems for it. That matches the expected result: the line is committed, it was placed in char-mara.md as the comment directed, and it correctly has no status tag in the Area Note.
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
          "what": "The source is tagged #status/provisional, but the copy went into an Area Note without its tag, where an untagged line counts as committed. That raises its status. Provisional material never goes in an Area Note, so move this line to an Idea Note and keep its #status/provisional tag."
        }
      ]
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The writer tagged the source #status/committed, but the copy says #status/provisional, which lowers a status the writer set. The writer's comment also sends it to char-mara. Move it to char-mara.md as a plain, untagged committed statement, and take it out of the Idea Note."
        }
      ]
    },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  All three units appear in the record. u1 and u2 have status errors and are filed as `fix` (`"unit": "u1", "verdict": "fix"` and `"unit": "u2", "verdict": "fix"`), not as `missed` entries. u3 is `"verdict": "approve"`. No unit was left out or wrongly moved into `missed`.
PASS  judge-shape   The reply is JSON findings with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`.  - **Units:** there is exactly one entry each for `"unit": "u1"`, `"unit": "u2"`, and `"unit": "u3"`. No other unit appears. - **u1:** `"verdict": "fix"` with one problem: `"check": "status"`, `"note": "char-mara.md"`, `"line": 20`, `"what": "The source line is tagged #status/provisional, but the copy went
PASS  judge-u1-fix-provisional-in-area-note   Evidence: - The verdict for u1 is a fix: `"unit": "u1", "verdict": "fix"`. - It has a problem under the check `status` that names provisional material in char-mara as an Area Note: `"check": "status", "note": "char-mara.md"`, with the text "The source line is tagged #status/provisional, but the copy went into char-mara, which is an Area Note. Provisional material never goes in an Area Note." - Th
PASS  judge-u2-fix-below-writer-tag   Evidence: u2's verdict is `"verdict": "fix"`, and it has one problem with `"check": "status"` (an accepted check type). The problem names the gap the check asks for, on both counts:  - **Status gap:** "The writer tagged this line #status/committed … The copy lowered it to #status/provisional" - **Placement gap:** "their comment sends it to char-mara … and put it in an Idea Note instead"  It also 
PASS  judge-u3-approve   The final reply gives u3 the verdict `approve` with an empty problems list:  `{ "unit": "u3", "verdict": "approve", "problems": [] }`  That is the expected outcome. The line is committed and went to char-mara as its comment named. It correctly has no status tag in the Area Note, and "clockwork mechanism" is a faithful paraphrase. No problems were raised against u3.
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
          "what": "The source line is tagged #status/provisional, but the copy went into char-mara, which is an Area Note. Provisional material never goes in an Area Note. Take it out of char-mara and migrate it to an Idea Note, such as Ideas/idea-mara-lighthouse.md, keeping its #status/provisional tag."
        }
      ]
    },
    {
      "unit": "u2",
      "verdict": "fix",
      "problems": [
        {
          "check": "status",
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "what": "The writer tagged this line #status/committed and their comment sends it to char-mara. The copy lowered it to #status/provisional and put it in an Idea Note instead. Remove it from the Idea Note. Then add it to char-mara (for example under ## General) as a plain committed statement with no status tag."
        }
      ]
    },
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

### Case 3: `migration-verifier-03-scope`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  The two batch items are covered by units in the reply. The Mara radio line from brain-dump.md is unit u3 (verdict `"fix"`). The hotel-sale comment is acted on by u1 (verdict `"approve"`). The too-wide reading of the hotel-sale rejection is reported as a `fix` on u2 (`"check": "scope"`, "The comment says the hotel sale is out for Mara's story on
PASS  judge-shape   The reply holds JSON findings with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`. Each rule in the check holds:  - **Units:** there is exactly one entry each for `"unit": "u1"`, `"unit": "u2"`, and `"unit": "u3"`. No other unit appears, and none appears twice. - **u1:** `"verdict": "approve"` with `"problems": []`. That is an approve with an empty problems list, which is correct. - *
PASS  judge-u1-approve   The reply gives u1 a clean approval:  ```json {   "unit": "u1",   "verdict": "approve",   "problems": [] } ```  The verdict is `approve` and the `problems` array is empty. That matches the expected result, because the rejection inside Mara's story was correct and was what the writer asked for. The verifier did not flag u1. It raised the "town can still have it" scope point under u2 instead, which
PASS  judge-u2-fix-scope-town   u2's verdict is `"verdict": "fix"`, and it carries a problem with `"check": "scope"` on `"note": "Ideas/idea-harrow-point.md"`. The problem says the rejection went past the writer's scope: "The comment says the hotel sale is out for Mara's story only and the town can still have it. This line is about the town, so it is still a live tentative idea." It also asks for the line to be restored: "Move 
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `"verdict": "fix"`, as the check requires.  It has one problem, and that problem's check is `scope`: - `"check": "scope"` - `"note": "Ideas/idea-mara-lighthouse.md"` - `"what": "The causeway line is the writer's existing line, and nothing in this batch asked for it to change. No comment allowed a grammar fix. Undo the edit so it reads \"- the causeway floods at spring tides, about
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
          "line": 9,
          "what": "The comment says the hotel sale is out for Mara's story only and the town can still have it. This line is about the town, so it is still a live tentative idea. Move it back to its place under the heading, without the #status/rejected tag, and take it out of the Rejected section."
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
          "what": "The causeway line is the writer's existing line, and nothing in this batch asked for it to change. No comment allowed a grammar fix. Undo the edit so it reads \"- the causeway floods at spring tides, about twice a month\" again. Keep the migrated radio line as it is."
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
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Both batch items have units in the record. u1 is approved (`{ "unit": "u1", "verdict": "approve", "problems": [] }`), and u3 is graded `fix`. The hotel-sale rejection that was read too wide shows up as a `fix` on u2, which is the correct place for it, not a `missed` entry: "The comment in idea-mara-lighthouse rejects the hotel sale for Mara's s
PASS  judge-shape   The reply is JSON with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed": []`. Each rule holds:  - **Each unit appears exactly once, with no extras.** `units` has three entries: `"unit": "u1"`, `"unit": "u2"`, `"unit": "u3"`. - **u1:** `"verdict": "approve"` with `"problems": []`. It is an approve with an empty problems list. - **u2:** `"verdict": "fix"` with one problem, `"check": "scope"`
PASS  judge-u1-approve   u1's entry in the final reply is: `{ "unit": "u1", "verdict": "approve", "problems": [] }`  The verdict is `approve` and the problems list is empty, which matches the check's PASS condition. The `fix` verdicts for u2 and u3 are outside this check.
PASS  judge-u2-fix-scope-town   The verdict for u2 is `fix`: `"unit": "u2", "verdict": "fix"`.  Its one problem has `"check": "scope"` and `"note": "Ideas/idea-harrow-point.md"`. It names the town's hotel line as rejected beyond what the writer's comment covered: "The comment in idea-mara-lighthouse rejects the hotel sale for Mara's story only and says 'The town can still have it.' The hotel chain buying the harbour cottages an
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `"verdict": "fix"`, and it carries one problem with `"check": "scope"`:  > "The causeway line isn't in this batch, and no comment asked for it to be changed. Put back the writer's original wording, '- the causeway floods at spring tides, about twice a month'. The migrated radio line itself is fine."  This problem names the unasked edit to the writer's causeway line. It says no com
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
          "check": "scope",
          "note": "Ideas/idea-harrow-point.md",
          "line": 9,
          "what": "The comment in idea-mara-lighthouse rejects the hotel sale for Mara's story only and says 'The town can still have it.' The hotel chain buying the harbour cottages and pier is part of the town's material, so it must not be rejected. Put the line back where it was, untagged, and remove it from the Rejected section."
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
          "what": "The causeway line isn't in this batch, and no comment asked for it to be changed. Put back the writer's original wording, '- the causeway floods at spring tides, about twice a month'. The migrated radio line itself is fine."
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
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Both batch items have units in the record: u3 covers the radio line ("The copy of the radio line is fine"), and u1 acts on the hotel-sale comment (`{ "unit": "u1", "verdict": "approve", "problems": [] }`). The rejection that was read too wide is filed as a `fix` on u2 ("The writer's comment rejects the hotel sale for Mara's story only... Take t
PASS  judge-shape   The reply is JSON with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed": []`.  - **Units:** There is exactly one entry each for `"unit": "u1"`, `"unit": "u2"`, and `"unit": "u3"`. No unit appears twice and no other unit appears. - **u1:** `"verdict": "approve", "problems": []`. It is an approve with an empty problems list. - **u2:** `"verdict": "fix"` with one problem: `"check": "scope"`, 
PASS  judge-u1-approve   The reply gives u1 a verdict of `approve` with an empty problems list:  `{ "unit": "u1", "verdict": "approve", "problems": [] }`  The check passes only when u1 is approved with no problems, and that is what the reply shows. The verdicts for u2 and u3 are outside this check.
PASS  judge-u2-fix-scope-town   u2's verdict is `fix`: `"unit": "u2", "verdict": "fix"`.  It has a problem with `"check": "scope"` on `"note": "Ideas/idea-harrow-point.md"`. That problem names the town's hotel line as rejected beyond the writer's scope: "The writer's comment rejects the hotel sale for Mara's story only and says \"The town can still have it.\" This line is the town's hotel-chain idea, so it isn't rejected." It a
PASS  judge-u3-fix-scope-unasked-edit   u3's verdict is `"verdict": "fix"`, and it has one problem with `"check": "scope"`, `"note": "Ideas/idea-mara-lighthouse.md"`, `"line": 10`:  > "The copy of the radio line is fine. The edit to the causeway line isn't: that line is outside this batch, has no tag, and no comment asked for it to be changed. Put it back exactly as the writer wrote it: \"- the causeway floods at spring tides, about tw
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
          "check": "scope",
          "note": "Ideas/idea-harrow-point.md",
          "line": 9,
          "what": "The writer's comment rejects the hotel sale for Mara's story only and says \"The town can still have it.\" This line is the town's hotel-chain idea, so it isn't rejected. Take the #status/rejected tag off, and move the line out of the Rejected section and back where it was in Harrow Point's live material."
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
          "what": "The copy of the radio line is fine. The edit to the causeway line isn't: that line is outside this batch, has no tag, and no comment asked for it to be changed. Put it back exactly as the writer wrote it: \"- the causeway floods at spring tides, about twice a month\"."
        }
      ]
    }
  ],
  "missed": []
}
```
````

### Case 4: `migration-verifier-04-standalone`

#### Run 1

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`. Both units are accounted for in `units`: u1 gets `"verdict": "fix"` (with "lost-detail" and "standalone" problems), and u2 gets `"verdict": "approve"`. Nothing was put in `missed`.
PASS  judge-shape   The reply is a JSON findings object with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed": []`.  - **Units:** `units` has exactly two entries, `"unit": "u1"` and `"unit": "u2"`. Neither is listed twice, and no other unit appears. - **Verdicts:** u1 has `"verdict": "fix"` and u2 has `"verdict": "approve"`. Both are allowed values. - **u1 (`fix`):** It has two problems, so it is non-empty:  
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict": "fix"`, and two problems name the missing event behind "what happened that winter."  - **lost-detail:** "The copy drops the committed story facts: Mara's mother sold the family's fishing licence to the cannery, and it happened the winter Tobias died." This names the licence sale, the cannery and the winter Tobias died. - **standalone:** "\"what happened that winter\" p
PASS  judge-u2-approve-rationale   The u2 entry in the reply reads: `{ "unit": "u2", "verdict": "approve", "problems": [] }`.  The verdict is `approve` and the problems list is empty. Nothing says the Rationale line ("I like that her discipline looks like penance.") should be rewritten, can't stand alone, or is in the wrong voice. All of the reply's problems are attached to u1, not u2.
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
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 10,
          "what": "The copy drops the committed story facts: Mara's mother sold the family's fishing licence to the cannery, and it happened the winter Tobias died. Keep every specific when you rewrite it for the Area Note, for example: \"Mara's mother sold the family's fishing licence to the cannery the winter Tobias died.\" followed by \"Mara has never forgiven her mother for it.\""
        },
        {
          "check": "standalone",
          "note": "brain-dump.md",
          "line": 10,
          "what": "\"what happened that winter\" points at an event and a winter that char-mara.md never names, so the line doesn't make sense on its own. Say what happened and which winter in the Area Note itself."
        }
      ]
    },
    { "unit": "u2", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  Both units are covered under `units` instead of being reported as missing: - u1 is `"verdict": "fix"`, with `lost-detail` and `standalone` problems. The check says a copy that can't stand alone is a `fix`, not a `missed` entry. - u2 is `"verdict": "approve"`.
PASS  judge-shape   The reply contains JSON findings with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`.  - **Units:** there is exactly one entry for each unit handed over, `"unit": "u1"` and `"unit": "u2"`. No other units appear. - **u1:** `"verdict": "fix"`. It has two problems:   - `"check": "lost-detail"`: "The copy leaves out the first committed idea: Mara's mother sold the family's fishing licence
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict": "fix"`, so it is not approved.  Both problems name the event that "what happened that winter" leaves out:  - **lost-detail problem:** "The copy leaves out the first committed idea: Mara's mother sold the family's fishing licence to the cannery, the winter Tobias died. The licence, the cannery and Tobias's death all need to be in char-mara.md as a plain statement…" - **
PASS  judge-u2-approve-rationale   The reply gives u2 the verdict `approve` with an empty problems list:  `{ "unit": "u2", "verdict": "approve", "problems": [] }`  No problem in the reply touches u2. Nothing says the Rationale line "I like that her discipline looks like penance." should be rewritten, can't stand alone, or is in the wrong voice. Both problems listed belong to u1 (`"unit": "u1"`, line 20 of char-mara.md), not to u2.
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
          "check": "lost-detail",
          "note": "char-mara.md",
          "line": 20,
          "what": "The copy leaves out the first committed idea: Mara's mother sold the family's fishing licence to the cannery, the winter Tobias died. The licence, the cannery and Tobias's death all need to be in char-mara.md as a plain statement, for example \"Mara's mother sold the family's fishing licence to the cannery the winter Tobias died.\""
        },
        {
          "check": "standalone",
          "note": "char-mara.md",
          "line": 20,
          "what": "\"For what happened that winter\" only makes sense if you have read the source. Nothing in the Area Note says which winter or what happened. Say what she has never forgiven, for example \"Mara has never forgiven her mother for selling the licence.\""
        }
      ]
    },
    { "unit": "u2", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`.  The gaps in u1 were reported as `fix` problems, not as `missed` entries. Both are under `"unit": "u1", "verdict": "fix"`: - `"check": "lost-detail"`, which says "The copy leaves out the committed first sentence". - `"check": "standalone"`, which says "\"what happened that winter\" points back to an event the Area Note never states".  Unit u2 is
PASS  judge-shape   The reply is JSON findings with `"batch": "b1"`, `"round": 0`, `"units": [...]` and `"missed": []`.  - **Units:** `units` holds exactly two entries, `"unit": "u1"` and `"unit": "u2"`. Neither is listed twice and no other unit appears. - **Verdicts:** u1 has `"verdict": "fix"` and u2 has `"verdict": "approve"`. Both are allowed values. - **The `fix` has problems:** u1 lists two:   - `"check": "los
PASS  judge-u1-fix-not-standalone   u1's verdict is `"verdict": "fix"`, so it is not approved.  Two problems name the missing event:  1. `"check": "lost-detail"` says: "The copy leaves out the committed first sentence. Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. That event is story substance and has to be in char-mara.md as a plain statement…" This names the licence sale, the cannery, and 
PASS  judge-u2-approve-rationale   The final reply gives u2 this entry:  `{ "unit": "u2", "verdict": "approve", "problems": [] }`  The verdict is `approve` and the problems list is empty. No problem says the Rationale line ("I like that her discipline looks like penance.") should be rewritten, can't stand alone, or is in the wrong voice. The reply's only problems belong to u1 and concern a different line (brain-dump.md line 10). T
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
          "check": "lost-detail",
          "note": "brain-dump.md",
          "line": 10,
          "what": "The copy leaves out the committed first sentence. Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. That event is story substance and has to be in char-mara.md as a plain statement, for example: \"Mara's mother sold the family's fishing licence to the cannery the winter Tobias died.\""
        },
        {
          "check": "standalone",
          "note": "brain-dump.md",
          "line": 10,
          "what": "\"what happened that winter\" points back to an event the Area Note never states, so the line doesn't make sense on its own. Name the event, for example: \"Mara has never forgiven her mother for selling the licence.\""
        }
      ]
    },
    { "unit": "u2", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

### Case 5: `migration-verifier-05-missed-line`

#### Run 1

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list contains exactly one entry, and that entry is line A, the oilskin coat line:  ```json "missed": [   {     "source": {       "note": "brain-dump.md",       "line": 10,       "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"     },     "what": "This line is tagged committed, and the comment under it sends it to char-mara, but the record doesn'
PASS  judge-shape   The reply is JSON findings with all four required keys: `"batch": "b1"`, `"round": 0`, `"units": [...]` and `"missed": [...]`.  - **Units:** `units` holds exactly one entry, for the handed unit: `{ "unit": "u1", "verdict": "approve", "problems": [] }`. No other unit is listed, and u1 is not listed twice. - **Verdict:** The only verdict is `"approve"`, which is one of the allowed values. - **Probl
PASS  judge-u1-approve   The verdict for u1 is an approval with no problems listed: `{ "unit": "u1", "verdict": "approve", "problems": [] }`.  Nothing in the reply says the relief keeper or the decommissioning was left behind or should have graduated. The only `missed` entry is about a different line (line 10, "Mara keeps Tobias's oilskin coat on the hook by the door."), which is not line B. This check doesn't ask about 
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
    { "unit": "u1", "verdict": "approve", "problems": [] }
  ],
  "missed": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"
      },
      "what": "This line is tagged committed, and the comment under it sends it to char-mara, but the record doesn't account for it anywhere: it isn't a unit, it isn't left in place, and it isn't under could_not. Graduate it into char-mara.md as a plain statement, for example \"Mara keeps Tobias's oilskin coat on the hook by the door.\""
    }
  ]
}
```
````

#### Run 2

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list contains exactly one entry, and that entry is line A, the oilskin coat line:  ```json "missed": [   {     "source": { "note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed" },     "what": "This line is tagged committed and the comment under it sends it to char-mara, but the record doesn't mention it anywhere. 
PASS  judge-shape   The reply contains JSON findings with all four required keys: `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed"`.  - **Units:** `units` has exactly one entry, for u1, and none for any other unit: `{ "unit": "u1", "verdict": "approve", "problems": [] }` - **Verdict:** `"approve"` is one of the two allowed values. - **Approve has no problems:** the `approve` verdict comes with an empty list, 
PASS  judge-u1-approve   u1's verdict is `approve` and its problems list is empty: `{ "unit": "u1", "verdict": "approve", "problems": [] }`.  No problem says the relief keeper ("might be a woman from Oban") or the decommissioning ("could be decommissioned by spring") was left behind or should have graduated. The only other finding is in `missed`, and it concerns a different line: "- Mara keeps Tobias's oilskin coat on th
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
    { "unit": "u1", "verdict": "approve", "problems": [] }
  ],
  "missed": [
    {
      "source": { "note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed" },
      "what": "This line is tagged committed and the comment under it sends it to char-mara, but the record doesn't mention it anywhere. Add it to char-mara.md as a plain statement, for example \"Mara keeps Tobias's oilskin coat on the hook by the door.\""
    }
  ]
}
```
````

#### Run 3

Grades:

````
PASS  judge-missed-line-a-only   The `missed` list contains exactly one entry, and that entry is line A, the oilskin coat line:  ```json "missed": [   {     "source": { "note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed" },     "what": "This line has the writer's committed tag, and the comment under it (line 11) sends it to char-mara, but it is missing from
PASS  judge-shape   The reply holds JSON findings with all four top-level keys: `"batch": "b1"`, `"round": 0`, `"units": [...]`, `"missed": [...]`.  - **One entry for u1, no others:** `units` contains a single entry, `{ "unit": "u1", "verdict": "approve", "problems": [] }`. No other unit is listed. - **Verdict is allowed:** the verdict is `"approve"`. - **Approve has an empty problems list:** `"problems": []`. - **F
PASS  judge-u1-approve   The check covers only u1's verdict. The text gives:  `{ "unit": "u1", "verdict": "approve", "problems": [] }`  The verdict is `approve` and the problems list is empty. Nothing says the relief keeper or the decommissioning was left behind or should have graduated. The `missed` entry is about a different line (line 10, "Mara keeps Tobias's oilskin coat on the hook by the door"). It has nothing to d
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
    { "unit": "u1", "verdict": "approve", "problems": [] }
  ],
  "missed": [
    {
      "source": { "note": "brain-dump.md", "line": 10, "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed" },
      "what": "This line has the writer's committed tag, and the comment under it (line 11) sends it to char-mara, but it is missing from the record. Rewrite it as a plain statement in char-mara.md, for example under ## General, with no status tag."
    }
  ]
}
```
````

### Case 6: `migration-verifier-06-clean-batch`

#### Run 1

Grades:

````
PASS  judge-all-five-approve   All five units have the verdict `approve` and no problems:  - `{ "unit": "u1", "verdict": "approve", "problems": [] }` - `{ "unit": "u2", "verdict": "approve", "problems": [] }` - `{ "unit": "u3", "verdict": "approve", "problems": [] }` - `{ "unit": "u4", "verdict": "approve", "problems": [] }` - `{ "unit": "u5", "verdict": "approve", "problems": [] }`  No unit has the verdict `fix`. u5 has no pr
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`. All five units (u1–u5) appear in the record, each with `"verdict": "approve"`.
PASS  judge-shape   The reply is valid JSON with the required top-level keys: `"batch": "b1"`, `"round": 0`, `"units": [...]` and `"missed": []`.  - **Unit coverage:** `units` has exactly five entries, one each for `"u1"`, `"u2"`, `"u3"`, `"u4"` and `"u5"`. No unit is missing, none is listed twice, and no other unit appears. - **Verdict values:** Every verdict is `"verdict": "approve"`, which is an allowed value. - 
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
    { "unit": "u5", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-all-five-approve   All five units have verdict `approve` with empty problem lists:  - `{ "unit": "u1", "verdict": "approve", "problems": [] }` - `{ "unit": "u2", "verdict": "approve", "problems": [] }` - `{ "unit": "u3", "verdict": "approve", "problems": [] }` - `{ "unit": "u4", "verdict": "approve", "problems": [] }` - `{ "unit": "u5", "verdict": "approve", "problems": [] }`  No unit has the verdict `fix`. There i
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`. All five units (u1–u5) are present in the record, so nothing in the batch went unaccounted for.
PASS  judge-shape   The reply is a JSON findings object with all four top-level keys: `"batch": "b1"`, `"round": 0`, `"units": [...]`, and `"missed": []`.  - **Unit coverage:** `units` has exactly five entries, one each for `"u1"`, `"u2"`, `"u3"`, `"u4"`, and `"u5"`. None is duplicated and no extra unit appears. - **Verdict values:** every verdict is `"verdict": "approve"`, which is an allowed value. - **Approve/pro
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
    { "unit": "u5", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-all-five-approve   All five units are approved, and none has a problem listed.  - u1: `{ "unit": "u1", "verdict": "approve", "problems": [] }` - u2: `{ "unit": "u2", "verdict": "approve", "problems": [] }` - u3: `{ "unit": "u3", "verdict": "approve", "problems": [] }` - u4: `{ "unit": "u4", "verdict": "approve", "problems": [] }`. Nothing is flagged on the reason comment "%% It makes her too cosy. %%". - u5: `{ "un
PASS  judge-missed-empty   The reply's `missed` list is empty: `"missed": []`. The record also carries all five units the check names, each with a verdict: `{ "unit": "u1", ... }` through `{ "unit": "u5", ... }`. This covers u1 (lighthouse-keeper), u2 (causeway/supply-runs), u3 (merged new-keeper/relief-keeper), u4 (the Ideas comment, "reject the dog") and u5 (sea-glass).
PASS  judge-shape   The reply contains JSON findings with all four top-level keys: `"batch": "b1"`, `"round": 0`, `"units": [...]`, and `"missed": []`.  **Unit coverage:** `units` has exactly five entries, one for each handed unit and no others: - `{ "unit": "u1", "verdict": "approve", "problems": [] }` - `{ "unit": "u2", "verdict": "approve", "problems": [] }` - `{ "unit": "u3", "verdict": "approve", "problems": []
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
    { "unit": "u5", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

### Case 7: `migration-verifier-07-asked-by-meaning`

#### Run 1

Grades:

````
PASS  judge-all-three-approve   All three units, u1 to u3, have the verdict `approve` with empty problem lists:  - `{ "unit": "u1", "verdict": "approve", "problems": [] }`: u1 was not fixed for the comma splice or the capital. - `{ "unit": "u2", "verdict": "approve", "problems": [] }`: u2 was not fixed for the added full stop. - `{ "unit": "u3", "verdict": "approve", "problems": [] }`  No unit has the verdict `fix`, and `"misse
PASS  judge-shape   The reply is JSON with `batch`, `round`, `units`, and `missed`. It meets every shape rule:  - **One entry per handed unit, nothing extra:** `units` has exactly three entries: `"unit": "u1"`, `"unit": "u2"`, `"unit": "u3"`. None repeats and no other unit appears. - **Allowed verdicts:** all three are `"verdict": "approve"`. - **Approve has empty problems:** each entry has `"problems": []`. - **Fix
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
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 2

Grades:

````
PASS  judge-all-three-approve   All three units, u1 to u3, have the verdict `approve` and an empty problems list, which is what the check requires:  - `{ "unit": "u1", "verdict": "approve", "problems": [] }`: u1 was not fixed for the comma splice or the capital. - `{ "unit": "u2", "verdict": "approve", "problems": [] }`: u2 was not fixed for the added full stop. - `{ "unit": "u3", "verdict": "approve", "problems": [] }`  No uni
PASS  judge-shape   The reply contains JSON findings with `"batch": "b1"`, `"round": 0`, `units`, and `"missed": []`.  - **Unit coverage:** `units` has exactly three entries, one each for u1, u2, and u3. None is duplicated and no other unit appears:   - `{ "unit": "u1", "verdict": "approve", "problems": [] }`   - `{ "unit": "u2", "verdict": "approve", "problems": [] }`   - `{ "unit": "u3", "verdict": "approve", "pro
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
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

#### Run 3

Grades:

````
PASS  judge-all-three-approve   All three units, u1 to u3, have the verdict `approve` with no problems:  - `{ "unit": "u1", "verdict": "approve", "problems": [] }`: the comma splice and capital that came with the spelling fix were not flagged. - `{ "unit": "u2", "verdict": "approve", "problems": [] }`: the added full stop and capital were not flagged. - `{ "unit": "u3", "verdict": "approve", "problems": [] }`  No unit has the v
PASS  judge-shape   The reply contains JSON findings with `batch`, `round`, `units`, and `missed`, and every shape rule holds:  - **Each handed unit appears exactly once, and no others:** `"unit": "u1"`, `"unit": "u2"`, `"unit": "u3"` are each listed once. - **Every verdict is valid:** all three are `"verdict": "approve"`. - **Every `approve` has an empty problems list:** each entry has `"problems": []`. - **The `fi
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
    { "unit": "u3", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
```
````

### Case 8: `migration-verifier-08-flags-asked`

#### Run 1

Grades:

````
PASS  judge-f1-to-f4-asked   The check covers f1 to f4 only. All four are `asked`, each of f1 to f3 names its matching comment, and f4 is credited to the request. The extra f5 entry is outside this check's scope.  - **f1**: `"verdict": "asked"`, `"asked_by": { "kind": "comment", "note": "Ideas/idea-mara-lighthouse.md", "line": 12, "text": "%% Agent, please correct the spelling in that line. %%" }`. This is the right comment,
PASS  judge-f5-not-asked   Evidence: the final reply records f5 as `{ "flag": "f5", "verdict": "not-asked", "asked_by": null }`.  The verdict is `"not-asked"` and `asked_by` is `null`. The reply does not credit the change to the typed request. That request ("In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias.") is attributed only to f4, not to f5.
PASS  judge-shape   Evidence: - The reply contains JSON with a `flags` list holding exactly five entries: `"flag": "f1"`, `"flag": "f2"`, `"flag": "f3"`, `"flag": "f4"`, `"flag": "f5"`. Each handed flag appears once, and no other flag appears. - Every verdict is one of the two allowed values:   - f1: `"verdict": "asked"`   - f2: `"verdict": "asked"`   - f3: `"verdict": "asked"`   - f4: `"verdict": "asked"`   - f5: `
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
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
      "asked_by": { "kind": "request", "note": "", "line": "", "text": "In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias." }
    },
    { "flag": "f5", "verdict": "not-asked", "asked_by": null }
  ]
}
```
````

#### Run 2

Grades:

````
PASS  judge-f1-to-f4-asked   The check covers only f1 to f4, and all four meet the PASS conditions.  - **f1**: `"verdict": "asked"`, `"asked_by": { "kind": "comment", "note": "Ideas/idea-mara-lighthouse.md", "line": 12, "text": "%% Agent, please correct the spelling in that line. %%" }`. The verdict is asked, the kind is comment, and the text matches the listed comment. - **f2**: `"verdict": "asked"`, `"asked_by": { "kind": 
PASS  judge-f5-not-asked   The reply's entry for f5 reads: `{ "flag": "f5", "verdict": "not-asked", "asked_by": null }`.  - The verdict is `"not-asked"`, as the check requires. - `asked_by` is `null`, as the check requires.  The reply did credit the typed request ("In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias.") to f4. It did not credit that request to f5, so the failu
PASS  judge-shape   The reply holds JSON with a `flags` list of exactly five entries, one each for f1–f5, with no extra or duplicate flags:  - f1: `"verdict": "asked"`, `"asked_by": { "kind": "comment", "note": "Ideas/idea-mara-lighthouse.md", "line": 12, "text": "%% Agent, please correct the spelling in that line. %%" }`, which is an object. - f2: `"verdict": "asked"`, `"asked_by": { "kind": "comment", "note": "bra
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
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
      "asked_by": { "kind": "request", "note": "", "line": "", "text": "In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias." }
    },
    { "flag": "f5", "verdict": "not-asked", "asked_by": null }
  ]
}
```
````

#### Run 3

Grades:

````
PASS  judge-f1-to-f4-asked   Evidence:  - **f1**: `"verdict": "asked"`, `"asked_by": { "kind": "comment", "note": "Ideas/idea-mara-lighthouse.md", "line": 12, "text": "%% Agent, please correct the spelling in that line. %%" }`. This is the right comment, quoted word for word. - **f2**: `"verdict": "asked"`, `"asked_by": { "kind": "comment", "note": "brain-dump.md", "line": 11, "text": "%% Agent, mark this one committed. %%" 
PASS  judge-f5-not-asked   f5 gets the verdict the check requires, with a null attribution:  `{ "flag": "f5", "verdict": "not-asked", "asked_by": null }`  - **Verdict:** `"not-asked"` - **`asked_by`:** `null`  The typed request appears only on f4 (`"text": "In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias."`). It is not credited to f5, so the failure the check describes di
PASS  judge-shape   The reply contains JSON findings with a `flags` list. Each of the five handed flags appears exactly once, and no other flags are listed:  - **f1:** `"verdict": "asked"`. Its `asked_by` is an object: `{ "kind": "comment", "note": "Ideas/idea-mara-lighthouse.md", "line": 12, "text": "%% Agent, please correct the spelling in that line. %%" }` - **f2:** `"verdict": "asked"`. Its `asked_by` is an obje
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
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
      "asked_by": { "kind": "request", "note": "", "line": "", "text": "In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias." }
    },
    { "flag": "f5", "verdict": "not-asked", "asked_by": null }
  ]
}
```
````

### Case 9: `migration-verifier-09-flags-not-asked`

#### Run 1

Grades:

````
PASS  judge-f1-f2-f3-not-asked   Evidence from the text under test:  - **f1:** `{ "flag": "f1", "verdict": "not-asked", "asked_by": null }`. The verdict is `not-asked` and `asked_by` is null. - **f2:** `{ "flag": "f2", "verdict": "not-asked", "asked_by": null }`. The verdict is `not-asked` and `asked_by` is null. - **f3:** `{ "flag": "f3", "verdict": "not-asked", "asked_by": null }`. The verdict is `not-asked` and `asked_by` is 
PASS  judge-f4-asked   Evidence: f4 is recorded with `"verdict": "asked"`. Its `asked_by` is `{ "kind": "comment", "note": "Ideas/idea-harrow-point.md", "line": 10, "text": "%% Agent, fix the typo. %%" }`.  - The kind is `comment`, which is what the check requires. - The `text` field quotes the right comment, "Agent, fix the typo." - The `note` field names Ideas/idea-harrow-point.md, the file that holds flag f4.  The v
PASS  judge-shape   The reply contains JSON findings with a `flags` list that has exactly four entries, one each for f1, f2, f3, and f4. No flag is duplicated and no other flag appears.  - f1: `"verdict": "not-asked", "asked_by": null`. The verdict is valid and `asked_by` is null. - f2: `"verdict": "not-asked", "asked_by": null`. The verdict is valid and `asked_by` is null. - f3: `"verdict": "not-asked", "asked_by":
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "flags": [
    { "flag": "f1", "verdict": "not-asked", "asked_by": null },
    { "flag": "f2", "verdict": "not-asked", "asked_by": null },
    { "flag": "f3", "verdict": "not-asked", "asked_by": null },
    {
      "flag": "f4",
      "verdict": "asked",
      "asked_by": { "kind": "comment", "note": "Ideas/idea-harrow-point.md", "line": 10, "text": "%% Agent, fix the typo. %%" }
    }
  ]
}
```
````

#### Run 2

Grades:

````
PASS  judge-f1-f2-f3-not-asked   All three flags in question carry `not-asked` with a null `asked_by`:  - **f1:** `{ "flag": "f1", "verdict": "not-asked", "asked_by": null }` - **f2:** `{ "flag": "f2", "verdict": "not-asked", "asked_by": null }` - **f3:** `{ "flag": "f3", "verdict": "not-asked", "asked_by": null }`  The reply avoided the main trap. It did not credit f3 to the spelling comment ("%% Agent, please correct the spell
PASS  judge-f4-asked   The reply gives f4 the `asked` verdict and attributes it to the expected comment:  - Verdict: `"verdict": "asked"` - asked_by: `{ "kind": "comment", "note": "Ideas/idea-harrow-point.md", "line": 10, "text": "%% Agent, fix the typo. %%" }`  The `asked_by` kind is `comment`. It names the note Ideas/idea-harrow-point.md, and its text is "Agent, fix the typo.", the same comment the check describes. T
PASS  judge-shape   The reply contains valid JSON with a `flags` list. It has exactly four entries, one each for f1, f2, f3, and f4, and no other flags.  - f1: `"verdict": "not-asked", "asked_by": null`. This is valid. - f2: `"verdict": "not-asked", "asked_by": null`. This is valid. - f3: `"verdict": "not-asked", "asked_by": null`. This is valid. - f4: `"verdict": "asked", "asked_by": { "kind": "comment", "note": "I
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "flags": [
    { "flag": "f1", "verdict": "not-asked", "asked_by": null },
    { "flag": "f2", "verdict": "not-asked", "asked_by": null },
    { "flag": "f3", "verdict": "not-asked", "asked_by": null },
    {
      "flag": "f4",
      "verdict": "asked",
      "asked_by": { "kind": "comment", "note": "Ideas/idea-harrow-point.md", "line": 10, "text": "%% Agent, fix the typo. %%" }
    }
  ]
}
```
````

#### Run 3

Grades:

````
PASS  judge-f1-f2-f3-not-asked   Evidence from the final reply:  - **f1**: `{ "flag": "f1", "verdict": "not-asked", "asked_by": null }`. The verdict is `not-asked` and `asked_by` is null. - **f2**: `{ "flag": "f2", "verdict": "not-asked", "asked_by": null }`. The verdict is `not-asked` and `asked_by` is null. - **f3**: `{ "flag": "f3", "verdict": "not-asked", "asked_by": null }`. The verdict is `not-asked` and `asked_by` is null
PASS  judge-f4-asked   The text gives f4 the following verdict and `asked_by`:  - verdict: `"verdict": "asked"` - asked_by: `{ "kind": "comment", "note": "Ideas/idea-harrow-point.md", "line": 10, "text": "%% Agent, fix the typo. %%" }`  The verdict is `asked`. The `asked_by` kind is `comment`. It names the correct note (`Ideas/idea-harrow-point.md`) and quotes the comment exactly ("Agent, fix the typo."). The check giv
PASS  judge-shape   The reply contains a JSON object with a `flags` list. Each of f1–f4 appears exactly once, and no other flags are present.  - f1: `"verdict": "not-asked", "asked_by": null` - f2: `"verdict": "not-asked", "asked_by": null` - f3: `"verdict": "not-asked", "asked_by": null` - f4: `"verdict": "asked", "asked_by": { "kind": "comment", "note": "Ideas/idea-harrow-point.md", "line": 10, "text": "%% Agent, 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{
  "flags": [
    { "flag": "f1", "verdict": "not-asked", "asked_by": null },
    { "flag": "f2", "verdict": "not-asked", "asked_by": null },
    { "flag": "f3", "verdict": "not-asked", "asked_by": null },
    {
      "flag": "f4",
      "verdict": "asked",
      "asked_by": { "kind": "comment", "note": "Ideas/idea-harrow-point.md", "line": 10, "text": "%% Agent, fix the typo. %%" }
    }
  ]
}
```
````
