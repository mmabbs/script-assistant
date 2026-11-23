# Eval Suite: migrator Cases

This folder holds eval cases for the script-asst plugin, testing nine migrator failure modes from eval-cases-migrator.md: lost or changed detail, bad unit record, over-promotion, ignored or misread comment, tentative material in an Area Note, missed unit, unasked edit, unasked migration, and wrong destination.

## Cases

1. `lost-detail-01-plain-copy`. A Brain Dump bullet with planted specifics is copied to an Idea Note.
2. `lost-detail-02-split-across-notes`. One bullet is split across two destination notes, testing whether each piece carries enough context.
3. `lost-detail-03-area-note-rewrite`. A committed bullet is rewritten into an Area Note, testing whether story facts and rationale survive the rewrite.
4. `lost-detail-04-existing-text`. A new bullet is added to an Idea Note that already has content, testing whether existing text is left alone.
5. `lost-detail-05-dense-bullet`. One long bullet with many units, hedges, and questions lands in a populated Idea Note.
6. `lost-detail-06-area-note-populated`. A long committed bullet is rewritten into an Area Note that already has content under Bio and Rationale.
7. `lost-detail-07-batch-two-notes`. Fourteen bullets under two date headings, each batch sent to its own Idea Note by a range comment.
8. `lost-detail-08-merge-by-comment`. Three bullets that say the same idea three ways are merged into one unit by comment.
9. `over-promotion-09-confident-wording`. Seven lines with confident prose but no committed tag, testing whether the agent promotes them.
10. `over-promotion-10-partial-graduation`. One committed tag on a bullet with three ideas, testing whether only the first graduates.
11. `misread-comment-11-scoped-rejection`. A rejection scoped to one character with a carve-out, testing whether the scope holds and the carve-out stays live.
12. `misread-comment-12-unusual-comment`. An unusual but clear comment that names bullets by position and sets a tag on one, testing whether the agent follows it exactly.
13. `misread-comment-13-ambiguous-comment`. An ambiguous comment ("the good ones") that names no bullets, testing whether the agent asks instead of guessing.
14. `unasked-migration-14-outside-range`. A range comment that covers three bullets, with a fourth just outside it and a second date heading with no comment at all.
15. `unit-record-15-split-and-merge`. One bullet to split across two notes, two to merge into one, and one plain migration, testing whether the unit record accounts for every copy.
16. `tentative-in-area-note-16-tagged-child`. A committed parent bullet with a provisional child, testing whether the child's own tag keeps it out of the Area Note.
17. `missed-unit-17-scattered-tags`. Six tagged bullets scattered among twelve untagged ones across three date headings, testing whether all six are found and none of the twelve moves.
18. `unasked-edit-18-typos-and-contradiction`. An Idea Note with typos and a line the new bullet contradicts, testing whether both existing lines are left alone.
19. `wrong-destination-19-no-destination-named`. Four provisional bullets with no comment naming a destination, three Idea Notes to choose from, testing whether each lands in the right note.
20. `wrong-destination-20-placement-from-context`. A provisional line that names no place, under a line that does, testing whether the migrator places it from the line above instead of asking.
21. `retry-21-no-second-copy`. A piece handed back after a unit in it was undone. One line already carries a pointer to its note and its copy is there; the other was undone. Testing that the pointed line gets no second copy.
22. `misread-comment-22-tag-only-comment`. A Brain Dump comment that asks only for a provisional tag, beside one that asks for a tag and a move. The first line gets the tag and a question, and no copy.
23. `tentative-in-area-note-23-writer-left-line`. A provisional line the writer left in an Area Note. It stays there unchanged, and the migrator asks about it once.
24. `request-comment-24-carried-request`. An untagged line under an `[AGENT]` comment that carries the writer's typed request from an earlier run, beside a later untagged line the request's words would also cover. The first line migrates as a comment-triggered unit; the second is left alone.

## Status

The cases now target the `script-asst:migrator` agent. Since 2026-10-13 each prompt hands the agent what the `/script-asst:run` skill hands it: the project folder, the rules file, batch b1's pieces as the Run manager's own scan (`lib/runmanager/migration/scan.py`) returns them for the fixture, no typed request, and the path for the unit record, `run/unit-records.json`. Every fixture scans to one batch. Before 2026-10-13 the prompt handed "the whole of project/brain-dump.md" as the batch. The record path stays outside the project, where the real run writes `{Project}/.runs/units/{run id}-bN.json`, because `record-check.py` reads it there. If a fixture changes, rebuild its prompt's JSON from the scan.

The only rules file a run gets is `_fixtures/rules/migrator-rules.md`, a copy of the plugin's `references/migrator-rules.md`. Recopy it when that file changes. The two older rules files, `terminology-script-asst.md` and `corrections.md`, are retired. They stay in `_fixtures/rules/` because the bare runs in `results/` used them.

Graders that used to read the agent's final reply now read `run/unit-records.json`: questions are entries in `questions`, things left behind are in `left_in_place`.

The earlier bare-Claude runs (no agent) are on record in `results/`. `_tools/bare-run.py` is the runner they used.

## Running

```bash
python3 _tools/research-run.py --suite migrator --agent script-asst:migrator --out <folder> [--cases <case> ...] [--runs N]
```

Since 2026-10-13 this is the runner for these cases. It runs every grader in each case's `graders/` folder, as described under Research Workflow Cases, and adds one `record-check` line from `_tools/record-check.py` to each run's `grades.txt`. A run's `before/` holds the whole fixture folder, so `before/project/` is the project before the agent ran. The migrator suite is every case folder that doesn't start with `research-` or `migration-verifier-`.

The older runner, which runs only the record check:

```bash
python3 _tools/migrator-run.py --out <folder> [--cases <case> ...] [--runs N]
```

Its default is all the cases, 3 runs each, at most 5 at a time. Each run gets `<folder>/<case>/r<n>/`, holding `work/` (where the agent ran), `before/` (the project notes before the agent ran), `stream.jsonl`, `stderr.txt`, and `record-check.txt`.

The runner calls `_tools/record-check.py` after each run. To check a run again by hand:

```bash
python3 _tools/record-check.py <run>/work <run>/before
```

It checks the unit record against the notes (spec-migrator.md 05 and 11) and prints one PASS or FAIL line per check. `migrator-run.py` doesn't run the graders; `research-run.py --suite migrator` does.

To write a results record for `results/` from a run folder, with every grade, note change, unit record, and reply copied in: `python3 _tools/results-record.py <out-folder> results/<name>.md <header.md>`, where `<header.md>` holds the record's hand-written top.

`claude plugin eval` has not been used on this folder.

Each run is a real model call against the account.

## Research Workflow Cases

Batch 1 of the Research workflow's cases, written 2026-10-08. The design, the ranked failure list, and every Pass line are in the vault note `Projects/Script Asst/research-workflow/eval-cases-research-workflow.md`. The spec is `Projects/Script Asst/research-workflow/spec-research-workflow.md`, accepted 2026-10-08.

Every research case folder starts with `research-`. `_tools/migrator-run.py` skips them, and the `migration-verifier-` folders too.

1. `research-writer-01-planted-figure`. F2. The findings give a repaint cycle of 5 years, where common knowledge says 7, and leave out the well-known paint tonnage. The note must carry 5 and neither outside fact.
2. `research-writer-02-coverage-gap`. F3. The plan asks four questions and the findings answer three. The fourth, lamplighters' pay, must land in Open Research Questions. One answer, 70 lamps per round, sits in the other topic's file.
3. `research-writer-03-source-trail`. F1. Passages with two URLs, one passage with no URL whose detail may appear only as a question under Open Research Questions, and one URL shared by two topics. Every footnote URL must come from the findings.
4. `research-planner-01-every-topic-limits`. F4. No topic waits on another. The comment's place and period must land under `## Every topic`.
5. `research-planner-02-one-topic-instruction`. F4. The comment's limit applies to one topic only and must land under that topic alone.
6. `research-evaluator-01-changed-number`. F8. The note's piece count was changed. The right verdict is FAIL.
7. `research-evaluator-02-missing-question`. F8. The note drops a plan question's answer. The right verdict is FAIL.
8. `research-evaluator-03-foreign-url`. F8. A footnote points to a URL not in the findings. The right verdict is FAIL.
9. `research-evaluator-04-clean-note`. F8, the negative case. The note matches the findings. The right verdict is PASS.
10. `research-writer-06-eight-topics`. Batch 2, written 2026-10-12. Scale. Eight topics and about 19,500 words of findings, with 16 planted details spread across every file. None may be lost, and each one-URL detail must cite its own URL.
11. `research-writer-08-cut-short`. Batch 2, written 2026-10-12. One of three findings files has no closing line. The reply must name that topic, and nothing from its file may appear in the note. **Retired 2026-10-22,** with the cut-short rule (spec-research-workflow.md 11 item 105). Its `prompt.md` sets `retired`, so `research-run.py` skips it. The folder stays for its past results.
12. `research-evaluator-06-three-errors`. F8. Written 2026-10-12, after the first live run, where the research-evaluator reported only 1 of a note's 3 real problems. One note holds three planted errors, each in a different section: the piece count under Disagreement / Uncertainty changed to about 600; a "which…" clause in Building the window that adds a conclusion the findings don't hold to a footnoted sentence; and the answer to plan question 2 (how the pieces were cut) dropped, with the question not listed as open. The writer kept the strict rule on 2026-10-12, with no reasoning steps allowed, so the clause fails "matches findings." The right verdict is FAIL, naming all three planted errors in one answer.
13. `research-evaluator-07-live-fog-signals`. F8. Written 2026-10-12, because E6 passed on both the agent and bare Claude, while the live miss happened on a long note. Built from the first live run: its real plan, findings, and note, saved in the case's `live-run/` folder because the test project may be deleted. `fixture.sh` reverts one sentence so the note is the first draft the live research-evaluator checked, and stops if that sentence isn't found. The note has three real "matches findings" problems: the Souter Point sentence saying the diaphones replaced the 1919 units, and two "which…" clauses that add conclusions (the compressor plant tying diaphones to stations, and the 1972 withdrawal showing more stations). The right verdict is FAIL, naming all three in one answer. A problem about the bell finding the note left out is neither required nor penalized.
14. `research-writer-09-out-of-scope-findings`. W9, written 2026-10-12 for spec decisions 100 and 101. The shared `_fixtures/research/penny-farthings/` plan limits the request to England, 1905 to 1914. One passage outside the period (penny-farthings were everyday transport only from about 1875 to 1885) changes the answer to plan question 1, so the note must keep it, footnoted to its own URL, and say it lies outside what was asked. One passage outside the place (the Kellard Brothers, American trick riders) only adds detail, and is neither required nor penalized. All four questions must be answered from inside the limits.
15. `research-evaluator-08-out-of-scope-kept`. E8, written 2026-10-12. F8, the negative case. W9's findings and a clean note that keeps the 1875 to 1885 finding, labelled as outside the period asked about, and leaves out the Kellard Brothers. The right verdict is PASS. A "nothing dropped" problem about the Kellard Brothers, or any other invented problem, is a fail.
16. `research-evaluator-09-out-of-scope-dropped`. E9, written 2026-10-12. F8. E8's note with the 1875 to 1885 finding removed: its Summary sentence, its paragraph, and its footnote. The right verdict is FAIL, with a "nothing dropped" problem naming that passage and no other problem.
17. `research-planner-05-almond-independent-questions`. P5, written 2026-10-22 for spec decision 103. The Almond request of 2026-10-18, word for word, with no comment, at its line in a copy of Almond's `brain-dump.md`. No topic may hold more than two of the first run's five questions; a topic's own "how strong is the evidence?" for its own question counts as narrowing that question, not as question 5. No topic may wait on another, except that the topic on whether "contagious" is an accurate word may wait on the studies topic.
18. `research-writer-10-judgment-sentence`. W10, written 2026-10-22 for spec decision 104. A findings passage ends in two sentences of the researcher's own judgment ("Where evidence is stronger: … Where it is weaker or disputed: …") under its URL list, as in Almond, and plan question 4 asks for that judgment. The note must never state it as a claim; at most it asks about it under Open Research Questions.
19. `research-writer-11-fix-round-draft-copy`. W11, written 2026-10-22 for spec decision 106. A fix round: the stained-glass note with E6's three errors, those three as the research-evaluator's problems, and a `draft-1.md` path in the findings folder. `draft-1.md` must match the note as handed, checked by a `same_as` grader, and the note must carry the fixes.
20. `research-evaluator-10-recheck`. E10, written 2026-10-22 for spec decision 106. A re-check: the first draft as `draft-1.md`, the fixed note, and the first check's three problems. Plants: (1) a flaw in a sentence that didn't change, (2) a first problem left unfixed, (3) a changed sentence with a new error, (4) a deleted sentence that dropped a plan answer. 2, 3, and 4 must be reported; 1 never.

### Fixtures

Each case's `fixture.sh` builds `project/`, the stand-in for `{Project}`. Writer cases get the plan in `project/llm-files/research-plans/`, the findings files in `project/llm-files/research-findings/run-2026-10-08-1400-research/{research-topic}/`, the note holding the request, and `templates/research-template.md`, a copy of the note template. The four evaluator cases share one plan, two findings files, and one clean note in `_fixtures/research/stained-glass/`. Cases 6 to 8 each plant their error in the note with one `perl` edit.

Recopy `_fixtures/research/research-template.md` from the vault template when that template changes.

### Where the answer is graded

1. **research-planner:** the prompt asks it to write its schedule to `run/answer.json` as well as answering with it. Graders read that file. Writing `run/answer.json` is a test-only extra. The spec gives the planner no such file.
2. **research-evaluator:** it has the Read tool only, so it can't write `run/answer.json`. Its verdict is graded from its final reply, by `llm` graders with no `focus`. `_tools/research-run.py` gives such a grader's judge the final reply.
3. **research-writer:** graders read the note it writes. Its reply, the note's path, is not graded. W11 also grades the `draft-1.md` copy it writes. Before 2026-10-22 the prompts also asked for any cut-short topic; that ask is gone with the cut-short rule (spec-research-workflow.md 11 item 105). W6 still holds one reply judge from then, `judge-reply-no-cut-short`, which passes when the reply names no topic as cut short.

The planner cases name the research topic in the prompt, so graders can find the plan file. In a real run the research-planner picks the name.

### Running

```bash
python3 _tools/research-run.py --out <folder> [--cases <case> ...] [--runs N] [--agent <name>]
python3 _tools/research-run.py --out <folder> --regrade [--cases <case> ...] [--runs N]
```

With no `--agent`, each run is bare Claude Opus 5.5: the case's prompt body and its `allowed_tools`, nothing else. With `--agent`, such as `script-asst:research-writer`, the same prompt goes to that agent from the plugin. The default is every `research-` case, 3 runs each, at most 5 at a time. Each run gets `<folder>/<case>/r<n>/`, holding `work/`, `before/`, `stream.jsonl`, `stderr.txt`, `reply.txt`, `grades.txt`, and `judges/`.

The runner runs every grader in the case's `graders/` folder: `regex`, `tool_used`, and `same_as` in code, `llm` through a judge call to Claude Opus 5.5 with no tools. A `same_as` grader, added 2026-10-22 for W11, checks that its target file in `work/` holds the same text as the file named by `before:` in `before/`, ignoring whitespace at line ends and blank lines at the end, since the Write tool retypes a file. A case whose `prompt.md` sets `retired` is skipped, and naming it with `--cases` stops the runner. `grades.txt` holds one PASS or FAIL line per check. `--regrade` grades the saved runs again after a grader changes, with no new Claude runs. It reuses a judge's saved answer when the judge's prompt hasn't changed. Two readings the runner makes:

1. A `tool_used` grader's `input_match` is matched against the call's file path, relative to `work/`, not the whole input, so a note that names another folder doesn't count as a write there.
2. When a writer case's note is missing under its expected name and the run wrote exactly one new note in `Research/`, the graders read that note and the extra check `file-name` fails.

Every call passes `--strict-mcp-config`. Without it, headless runs load the account's claude.ai connectors, Exa web search among them.

The batch-1 bare runs are on record in `results/2026-10-12-bare-opus-5-5-research-cases-batch-1.md`. `claude plugin eval` has not been used on this folder.

## migration-verifier Cases

Seventeen cases: batch 1, written 2026-10-10; batch 2, cases 10 to 14, written 2026-10-13; and batch 3, cases 15 to 17, written 2026-10-23 from the decision audit's rulings 03.9 and 03.10 and a finding made while writing them. The design, the ranked failure list, and every Pass line are in the vault note `Projects/Script Asst/migration-verifier/eval-cases-migration-verifier.md`. The spec is `Projects/Script Asst/migration-verifier/spec-migration-verifier.md`. The agent is `agents/migration-verifier.md`.

Every case folder starts with `migration-verifier-`. Each fixture writes the project as it stands after the migrator's pass, with errors planted in the copies, and the cut-down record or the Edit guard's flags under `project/.runs/run-2026-10-09-2100-migration/`. Every case has at least one correct unit or flag beside the planted ones.

1. `migration-verifier-01-lost-detail`. V1. A split loses "nine," and a copy drops "maybe." One unit is correct.
2. `migration-verifier-02-status`. V2. A provisional line in an Area Note, and a committed line copied as provisional. One unit is correct.
3. `migration-verifier-03-scope`. V5. A rejection meant for Mara's story applied to the town too, and an unasked wording fix on a neighbouring line.
4. `migration-verifier-04-standalone`. An Area Note line that only reads with its source beside it. A Rationale line in the writer's words must not be flagged.
5. `migration-verifier-05-missed-line`. V7 and V8. One committed line with no unit is `missed`. A line the migrator asked about, a `could_not` line, and an untagged line are not.
6. `migration-verifier-06-clean-batch`. V4. Five correct units. Every verdict is approve.
7. `migration-verifier-07-asked-by-meaning`. V3. A spelling fix that also fixed a comma splice, and a grammar fix. Both approve.
8. `migration-verifier-08-flags-asked`. V3, flags call. Four asked-for flags, including a fact change a comment asked for and an `[AGENT]` line the typed request asked for, and one control.
9. `migration-verifier-09-flags-not-asked`. V6, flags call. Three not-asked flags, including a spelling comment whose edit also changed "may" to "will," and one control.
10. `migration-verifier-10-recheck`. V9. A round-1 re-check with its earlier findings. The fix landed; an approved unit beside it must get no verdict.
11. `migration-verifier-11-status-raise`. V4. A provisional line that reads confidently stays provisional. A copy carries a tag the writer never gave.
12. `migration-verifier-12-earlier-run-status`. V8. An earlier run's copy below the writer's newer tag is not this run's business. A copy from this run dropped its tag.
13. `migration-verifier-13-large-batch`. Scale. Twenty units under three date headings, three planted errors and a decoy.
14. `migration-verifier-14-comment-names-note`. V5. Half of a split went to a note other than the one its comment named.
15. `migration-verifier-15-left-in-place-missed`. V7 and V8. A committed line listed only in `left_in_place`, with no reason the rules allow, is `missed`; a line rightly left in place for an unresolved detail is not. The fixture also holds the full record in `.runs/units/`, its `record-b1-r0.json` copy, and the before-snapshot, and three `tool_used` graders fail any Read, Grep, or Glob of them.
16. `migration-verifier-16-retagged-ignored`. V7. A pointer line the writer re-tagged committed is in the batch, and the migrator only listed it in `left_in_place`. It is `missed`. One unit is correct.
17. `migration-verifier-17-comment-only-missed`. V7. An untagged line with a comment asking for a move, and nothing in the record names it. Code skips comment lines, and the comment goes on the handled list, so only the migration-verifier can call it `missed`. One unit is correct.

### Where the answer is graded

The migration-verifier has Read, Glob, and Grep only, so it can't write a file. Its findings are graded from its final reply, by `llm` graders with no `focus`, as with the research-evaluator cases. Every case also checks the reply's shape and that nothing was written or edited.

Since 2026-10-13 the prompts match what the `/script-asst:run` skill hands the agent: no findings shape and no instructions on how to judge, since the agent file carries both. Bare runs get batch 1's shape text added with `--bare-append _fixtures/bare-shape-migration-verifier-batch.md`, so a bare run isn't failed for not knowing the shape.

### Running

Run them with `_tools/research-run.py --suite migration-verifier`, with the same options as the research cases. The batch-1 bare runs are on record in `results/2026-10-12-bare-opus-5-5-migration-verifier-cases-batch-1.md`, regraded with the note check in `results/2026-10-13-regrade-bare-migration-verifier-batch-1-note-check.md`. The agent's batch-1 runs are in `results/2026-10-13-agent-migration-verifier-batch-1.md`. Batch 3, cases 15 to 17, ran on the agent only: `results/2026-10-23-agent-migration-verifier-batch-3.md`. `claude plugin eval` has not been used on this folder.
