---
name: run
description: "Start a pre-writing run on the writer's project: init, a migration run, a research run, recover after a crash, abandon a run recover couldn't clear, or stop a research run. The Run manager's front door."
argument-hint: init|migration ["request"]|research N|recover|abandon
when_to_use: "Invoke when the writer types /script-asst:run, or asks to start a migration run or a research run, set up a project for runs, recover a crashed run, abandon a stuck run, or stop or cancel a research run."
---

# run

The front door for every pre-writing run. You run the steps. The `runmanager` and `editguard` commands make every exact edit and every check. One run does one job.

## Rules

1. **Run every step through the shell, in order.** Don't skip a step. Don't reorder steps.
2. **Never edit the writer's notes or any file in `.runs/` yourself.** The exceptions are saving what a workflow or agent returns, where a step says to: the outcomes in research step 4, and the migration-verifier's findings in the migration steps.
3. **If a command exits non-zero, stop.** The exceptions are `runmanager record` and `runmanager findings` on a migration run, where the migration steps say what to do. Otherwise, show the writer its one line. Run `runmanager status --project P` and show that line too. Don't retry, and don't work around it. A refusal means a step is missing or a run is open.
4. **When unsure where a run stands, run `runmanager status --project P` and do what its `next:` says.**
5. **Never act as the migrator or the migration-verifier yourself.** Their work comes only from the Agent tool calls the migration steps name.
6. **Tell the writer one short line at each stage:** the run started with how many requests or batches, the workflow or each batch started, the workflow or each batch finished, the check ran, the run closed. The workflow can take a while, so never leave the writer with a silent gap.
7. **Run each `runmanager` and `editguard` command as its own shell call, with `P` and every other path written out in full.** No shell variables, no `cd`, and nothing joined on with `&&`, `;`, a pipe, or a redirect. The plugin's permission hook lets a command through without asking only when it is one call and nothing else; anything more asks the writer. Read a file, such as `batches.json`, with the Read tool, and check whether one exists with the Glob tool, not the shell.
8. **When the writer wants a run to end, pick the path by the run's state, never by the writer's word.** "Abandon," "stop," and "cancel" all mean the writer wants the run to end, and "abandon" never means a crash on its own.
    - A research run this session started, whose workflow hasn't returned: follow **stop**.
    - A research run whose workflow has already returned: there's no stop. Tell the writer in one line, and finish the research steps.
    - A migration run: tell the writer to type `/script-asst:run recover`. A migration run has no stop.
    - A run already open when the session began: follow **recover** first, then **abandon** only if recover fails.

## Find the project

**Every run uses the session's working directory as the project folder, `P`, as an absolute path.** Runs never work on another folder. If the working directory holds no `.runs/run-state.json` and the writer didn't ask for `init`, stop before any command and tell the writer: "Runs need Claude Code opened in the project folder, so the agents can save their files. Open Claude Code in the project folder and run this again. If the project is new, run `/script-asst:run init` there first." The plugin approves the agents' writes only inside the folder the session was opened in.

## init

1. Run `runmanager init --project P`. It creates the run state and nothing else.
2. Tell the writer the result in one line.

## migration

The writer may type a request after `migration`, in quotes. It goes to the migrator and the migration-verifier as is. Below, `R` is `P/.runs/{run id}`, and the rules path is the plugin's `references/migrator-rules.md`: from this skill's base directory, `../../references/migrator-rules.md`, given to the agents as an absolute path.

1. Run `runmanager start --project P --kind migration`, adding `--request "{request}"` when the writer typed one. Read the run id from its `run_id:` line and the batch count from `batches:`. If it says there is no new work, tell the writer and stop.
2. Run `runmanager status --project P`, and do what its `next:` says, from the list below. Then run `status` again. Repeat until `next:` is `close`.
    - **"run the migrator on batch N, round K, then record":** call the Agent tool with `subagent_type` `script-asst:migrator`. The prompt gives: the project folder `P`; the rules path; batch `bN` from `R/batches.json`, its pieces as they are; the writer's request, or "none"; the record path `P/.runs/units/{run id}-bN.json`; and on round 1 or 2, the findings to fix, `R/findings-bN-r{K-1}.json`, naming the units it must fix and saying it touches no other unit. Wait for it. Then run `runmanager record --project P`.
        - If `record` refuses, or the migrator failed, call the migrator again with the same prompt, adding `record`'s refusal line when there is one, so it can make its record and the notes agree. After 2 such retries, run `runmanager record --project P --failed`.
    - **"run the migration-verifier on batch N, round K, save its findings, then findings":** call the Agent tool with `subagent_type` `script-asst:migration-verifier`. The prompt gives: the cut-down record `R/verify-bN-rK.json`; batch `bN` from `R/batches.json`, its pieces as they are; the writer's request, or "none"; the project folder; the rules path; and on round 1 or 2, its own earlier findings, `R/findings-bN-r{K-1}.json`. Save the JSON it returns, exactly as returned, to `R/findings-bN-rK.json`. Run `runmanager findings --project P`.
        - If `findings` refuses, or the migration-verifier failed, call it again. After 2 such retries, run `runmanager findings --project P --failed`.
    - **"pointers":** run `runmanager pointers --project P`.
    - **"run editguard check for flags-n.json, then act":** run the Edit guard, then `runmanager act --project P`:

        ```
        editguard check --kind migration --project P --snapshot R/snapshot \
          --records P/.runs/units/{run id}-b*.json --run-state P/.runs/run-state.json \
          --run-id {run id} --fingerprints R/fingerprints.json --out R/flags-n.json
        ```

        If `R/findings-flags.json` exists and `n` isn't the open run's `first_check` in `P/.runs/run-state.json`, add `--judged R/flags-{first_check}.json --findings R/findings-flags.json`.
    - **"run the migration-verifier on verify-flags.json, save its findings as findings-flags.json, then findings":** call the migration-verifier with `R/verify-flags.json`, the writer's request, the project folder, and the rules path. Save what it returns to `R/findings-flags.json`, then run `runmanager findings --project P`. Retry as for a batch; after 2 retries, `runmanager findings --project P --failed`.
    - **"act":** run `runmanager act --project P`.
    - **"run editguard check for flags-n.json, then close":** run the Edit guard as above, with the `--judged` and `--findings` rule.
3. Run `runmanager close --project P`. It prints the run log's path.
4. Tell the writer as in research step 10.

## research N

`N` is the run number, the number in the writer's `#research/run-N` tag.

1. Run `runmanager start --project P --kind research --run-number N`. Read the run id from its `run_id:` line and the workflow script's path from its `workflow:` line. Below, `R` is `P/.runs/{run id}`.
2. Read `R/requests.json`.
3. Call the Workflow tool with `scriptPath` set to the path from the `workflow:` line. Never call it by name. Pass `args` as an object: `{"project": "P", "run_id": "{run id}", "requests": [every entry of requests.json, as is]}`, with `P` as the project folder's absolute path. The workflow runs in the background. Keep the task id the Workflow tool returns; **stop** needs it. Wait for its completion notice. Run no command while it runs. If the writer asks to end the run while it runs, follow **stop**.
4. Save the list the workflow returns, exactly as returned, to `R/outcomes.json`. If the workflow failed or returned no list, save nothing and go on. `mark` handles a missing file.
5. Run `runmanager mark --project P`.
6. Run the Edit guard, with the flags file `runmanager` waits for. The first time, that's `flags-1.json`:

    ```
    editguard check --kind research --project P --snapshot R/snapshot \
      --requests R/requests.json --outcomes R/outcomes.json \
      --fingerprints R/fingerprints.json --out R/flags-1.json
    ```

7. Run `runmanager act --project P`.
8. Run `runmanager status --project P`. If its `next:` names a flags file, run step 6 again with `--out R/{that file}`.
9. Run `runmanager close --project P`. It prints the run log's path.
10. Tell the writer where the log is, as a wikilink in the form the run log uses for its own links: `[[Projects/{project folder name}/Runs/{run id}|{run id}]]`. Don't look for the vault folder. Then give the log's first section heading and its first entry, or "Nothing needs you." Don't summarize the rest. The writer reads the log.

## stop

Use this when the writer wants to end a research run this session started, and its workflow hasn't returned. Never ask the writer why, and record no reason.

1. Call the TaskStop tool with the task id from research step 3.
    - If it reports success, the workflow is stopped. Go on to step 2.
    - If it says the task is not running with status `killed`, treat the workflow as already stopped. Go on to step 2.
    - If it says the task is not running with any other status, the workflow already returned, so there's no stop. Tell the writer in one line, and go on from research step 4.
    - If the session no longer has the task id, tell the writer to open `/workflows`, stop the research run if it's listed, and say yes. Wait for the yes. Then go on to step 2.
2. Save no outcomes. Run `runmanager mark --project P --stopped`.
3. Do research steps 6 to 10.

## recover

Use this when a run stopped partway, or when `start` says a run is still open.

0. Run `runmanager status --project P`. If the open run is a research run at step `started`, its workflow may still be running in the background. Tell the writer to open `/workflows`, stop the research run if it's listed, and say yes. Wait for the yes before step 1. At any other step, go straight to step 1.
1. Run `runmanager recover --project P`. It picks the crashed run up from the step it reached.
2. Run `runmanager status --project P` and do what `next:` says: for a research run, research steps 6 to 9; for a migration run, migration steps 2 and 3. `close` writes the recover run's own log.
3. Tell the writer as in research step 10.

## abandon

Use this when the writer types `/script-asst:run abandon`, after a recover that failed. `runmanager abandon` refuses until recover has had its one try, and edits no note.

1. Run `runmanager abandon --project P`.
2. If it printed the log's whole text, because the log couldn't be written, show that text to the writer whole. Otherwise tell the writer as in research step 10.
