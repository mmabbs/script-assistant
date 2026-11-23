# Steps: the migration dry run

The session runs the real `/script-asst:run migration` on a fresh copy of the project. At each agent step it copies the prepared files below instead of calling the migrator or the migration-verifier. Everything else is the skill's own steps, unchanged.

## Placeholders

| Placeholder | Means |
| --- | --- |
| `DRY` | `/Users/mabbs/.claude/plugins/local/script-asst/lib/runmanager/tests/dryrun-migration` |
| `PREP` | `DRY/prepared` |
| `P` | the project folder `build.py` made: `{DEST}/Lighthouse`, as an absolute path |
| `{run-id}` | the id `start` prints on its `run_id:` line, such as `run-2026-10-13-1000-migration` |
| `R` | `P/.runs/{run-id}` |

`runmanager` and `editguard` are the plugin's launchers in `bin/`.

## Before the run

1. Run `python3 DRY/build.py {DEST}`, with `{DEST}` a new folder. It prints `built {DEST}/Lighthouse`.
2. Open the session in `P` (the skill needs the project folder as its working directory).
3. Type `/script-asst:run migration`, with no request. The skill runs `runmanager start --project P --kind migration`. It prints `run_id: {run-id}` and `batches: 2`.

## At each `next:` line

Run `runmanager status --project P` before each step, as the skill does. Do the step whose `next:` text matches, in this order. Each step is listed once; the order below is the order they come.

| # | `next:` says | Do this instead of the agent call | Then the skill runs | It prints |
| --- | --- | --- | --- | --- |
| 1 | run the migrator on batch 1, round 0, then record | `cp PREP/b1-r0/record.json P/.runs/units/{run-id}-b1.json` then `cp -R PREP/b1-r0/notes/. P/` | `runmanager record --project P` | exit 1, refusal line below (plant 1) |
| 2 | same as step 1 (the retry) | `cp PREP/b1-r0-retry/record.json P/.runs/units/{run-id}-b1.json` then `cp -R PREP/b1-r0-retry/notes/. P/` | `runmanager record --project P` | `checking 5 unit(s) of batch 1, round 0` |
| 3 | run the migration-verifier on batch 1, round 0, save its findings, then findings | `cp PREP/b1-r0/findings.json R/findings-b1-r0.json` | `runmanager findings --project P` | `to fix: u1; next: run the migrator on batch 1, round 1` |
| 4 | run the migrator on batch 1, round 1, then record | `cp PREP/b1-r1/record.json P/.runs/units/{run-id}-b1.json` then `cp -R PREP/b1-r1/notes/. P/` | `runmanager record --project P` | `checking 1 unit(s) of batch 1, round 1` |
| 5 | run the migration-verifier on batch 1, round 1, save its findings, then findings | `cp PREP/b1-r1/findings.json R/findings-b1-r1.json` | `runmanager findings --project P` | `to fix: u1; next: run the migrator on batch 1, round 2` |
| 6 | run the migrator on batch 1, round 2, then record | `cp PREP/b1-r2/record.json P/.runs/units/{run-id}-b1.json` then `cp -R PREP/b1-r2/notes/. P/` | `runmanager record --project P` | `checking 1 unit(s) of batch 1, round 2` |
| 7 | run the migration-verifier on batch 1, round 2, save its findings, then findings | `cp PREP/b1-r2/findings.json R/findings-b1-r2.json` | `runmanager findings --project P` | `undone: 1; step: migrating` |
| 8 | run the migrator on batch 2, round 0, then record | `cp PREP/b2-r0/record.json P/.runs/units/{run-id}-b2.json` then `cp -R PREP/b2-r0/notes/. P/` | `runmanager record --project P` | `checking 1 unit(s) of batch 2, round 0` |
| 9 | run the migration-verifier on batch 2, round 0, save its findings, then findings | `cp PREP/b2-r0/findings.json R/findings-b2-r0.json` | `runmanager findings --project P` | `undone: 0; step: batches-done` |
| 10 | pointers | nothing to copy | `runmanager pointers --project P` | `pointers written for 3 unit(s); undone: 0; next: run editguard check for flags-1.json, then act` |
| 11 | run editguard check for flags-1.json, then act | nothing to copy; run the Edit guard as the skill says (first form below) | `runmanager act --project P` | `step: judging; flags for the migration-verifier: 1` |
| 12 | run the migration-verifier on verify-flags.json, save its findings as findings-flags.json, then findings | `cp PREP/flags/findings-flags.json R/findings-flags.json` | `runmanager findings --project P` | `step: judged; next: act` |
| 13 | act | nothing to copy | `runmanager act --project P` | `step: acted; units undone: 0; lines not found: 0` |
| 14 | run editguard check for flags-2.json, then close | nothing to copy; run the Edit guard with `--judged` and `--findings` (second form below) | `runmanager close --project P` | `run log: Runs/{run-id}.md` |

Step 1's `record` exits 1 and prints this one line on stderr, with `P` and `{run-id}` filled in:

```
runmanager: The record file P/.runs/units/{run-id}-b1.json was refused: unit u3's copy `- The relief keeper could be someone from the mainland who has never seen the sea and is scared of the water.` isn't in Ideas/idea-relief-keeper.md as a line the run wrote.
```

The refusal changes nothing, so the run stays at `migrating`, batch 1, round 0, and `status` still says step 1's `next:` text. The skill calls the migrator again with the same prompt (its first of two retries); step 2 stands in for that call. It succeeds, so `record --failed` is never run.

`cp -R PREP/…/notes/. P/` copies the notes over the project's, keeping their folders. Each `notes/` folder holds only the notes that migrator call changed, each as the whole note. `b1-r0-retry/record.json` is the same as `b1-r0/record.json`: the retried migrator rewrites the note's line to match its record.

## The two Edit guard commands

Step 11, the first check (no `findings-flags.json` exists yet):

```
editguard check --kind migration --project P --snapshot R/snapshot \
  --records P/.runs/units/{run-id}-b*.json --run-state P/.runs/run-state.json \
  --run-id {run-id} --fingerprints R/fingerprints.json --out R/flags-1.json
```

It writes 3 flags, `f1` to `f3` (see `planted.md`). `f2` and `f3` stand, so `act` hands only `f1` to the migration-verifier.

Step 14, the second check (`first_check` is 1, and this is flags-2):

```
editguard check --kind migration --project P --snapshot R/snapshot \
  --records P/.runs/units/{run-id}-b*.json --run-state P/.runs/run-state.json \
  --run-id {run-id} --fingerprints R/fingerprints.json --out R/flags-2.json \
  --judged R/flags-1.json --findings R/findings-flags.json
```

It writes `[]`. `findings-flags.json` holds the migration-verifier's verdict on `f1` and the `asked` entries the Run manager added for `f2` and `f3` after `findings` (plan-run-manager.md 06 item 14, reading 2).

## If a line doesn't match

Stop at the first step whose output differs from the table, and report the step number, the command, and its output. Don't go on to the next step.
