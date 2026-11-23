# workflowtests: build contract

The shared contract for the fake-agent tests of `lib/research.js` (plan-research-workflow.md, Milestone 3). Three workers build against it: one writes `harness.mjs`, one writes the cases in `cases/`, one writes `research.js`. The spec owns the design: `~/Documents/obsidian/cerebral-swamp-vault/Projects/Script Asst/research-workflow/spec-research-workflow.md`. Where this file and the spec disagree, the spec wins. Report the disagreement.

## 1. What the harness runs

1. **Command:** `node lib/workflowtests/harness.mjs [case-name ...]`, run from the plugin root `~/.claude/plugins/local/script-asst/`. With no names it runs every folder in `cases/`. It prints one line per case, `PASS {case}` or `FAIL {case}: {first reason}`, then every reason for each failed case, and exits 0 only when every case passes. Node v26, standard library only. Nothing to install.
2. **The script under test is `lib/research.js`,** a Claude Code workflow script: plain JavaScript that starts with `export const meta = {...}`, then a body that uses top-level `await` and ends with `return`. It may use only these globals: `agent`, `parallel`, `pipeline`, `phase`, `log`, `args`. It can't read files or import anything.
3. **How the harness loads it:** read the file as text, drop the `export` keyword in front of `const meta`, and run the rest as the body of an `AsyncFunction` whose parameters are the six globals. The value the body returns is the workflow's result.
4. **The harness refuses a script that uses `Date.now()`, `Math.random()`, `new Date()` with no argument, `import`, or `require`.** The Workflow tool throws on the first three, and the script has no file access. The case fails with the name of what was found.

## 2. The stand-in globals

1. **`agent(prompt, opts)`:** looks up the call's `opts.label` in the case's `answers` (section 3), records the call (section 4), waits `delay_ms` (default 0, through `setTimeout`), then returns the next set answer for that label. A set answer of `null` returns `null`, as a real agent that died after the Workflow tool's own retries does. An answer `{"$throw": "message"}` throws an Error with that message. A label with no set answer left fails the case: "unexpected call {label}".
2. **`parallel(thunks)`:** runs every thunk at once and waits for all. A thunk that throws resolves to `null`. It never rejects.
3. **`pipeline(items, ...stages)`:** runs each item through every stage in order, with no barrier between items. Each stage gets `(previousResult, item, index)`. The first stage gets the item as `previousResult`. A stage that throws turns that item into `null` and skips its later stages. Returns the list of final results, in item order.
4. **`phase(title)` and `log(message)`:** record the text and return nothing.
5. **`args`:** the case's `args`, as given.

## 3. The labels and answers

The script must give every `agent()` call a `label` and an `agentType` in exactly this form. `{r}` is the request id, such as `r1`. `{n}` is the topic number.

| Call | `label` | `agentType` |
| --- | --- | --- |
| research-planner | `plan {r}` | `script-asst:research-planner` |
| researcher | `topic {r} {n}` | `script-asst:researcher` |
| research-writer, first draft | `write {r}` | `script-asst:research-writer` |
| research-evaluator, first check | `check {r}` | `script-asst:research-evaluator` |
| research-writer, fix round | `fix {r}` | `script-asst:research-writer` |
| research-evaluator, second check | `recheck {r}` | `script-asst:research-evaluator` |

1. **A retry reuses its label.** The harness hands out the label's answers in order, one per call.
2. **Every call passes `opts.schema`,** and it must equal that agent's schema in `references/research-answer-shapes.json`, with every key that starts with `_` removed, at any depth. The harness compares them by deep equality and fails the case on a mismatch, naming the label. Each set answer must also match the schema the call passed. The harness checks this with a small validator that covers what the four schemas use: `type` (one type or a list, `null` included), `properties`, `required`, `additionalProperties: false`, `items`, `enum`, `minItems`, `minimum`, and `pattern`. A set answer that fails it is a broken case, reported as such.

## 4. What the harness records

For every `agent()` call, in the order calls start: `label`, `agentType`, `prompt`, the full `opts`, a start sequence number, an end sequence number, and the labels of every call that had ended before this one started. `phase()` and `log()` texts are recorded in order too.

## 5. The case format

Each case is a folder `cases/{NN-short-name}/` holding one `case.json`:

```json
{
  "about": "what the case tests, in plain words",
  "spec": ["spec-research-workflow.md 04 item 10", "..."],
  "args": { "project": "/abs/Copper Coast", "run_id": "run-2026-10-08-1400-research", "requests": [ ... ] },
  "answers": {
    "plan r1": [ { "research_topic": "x", "topics": [ { "n": 1, "waits_on": [] } ] } ],
    "topic r1 1": [ { "result": "found" } ],
    "topic r1 2": [ null, null, null ]
  },
  "delay_ms": { "topic r1 1": 30 },
  "expect": {
    "result": [ { "request": "r1", "outcome": "passed", "note": "Research/research-x.md", "reason": null, "failed_topics": [] } ],
    "calls": {
      "topic r1 2": { "count": 3, "prompt_includes": ["/abs/Copper Coast/llm-files/research-plans/research-plan-x.md"], "prompt_excludes": ["topic-1.md"] }
    },
    "not_called": ["write r1"],
    "after": [ ["topic r1 2", "topic r1 1"] ],
    "together": [ ["topic r1 2", "topic r1 3"] ]
  }
}
```

1. **`args.requests`** holds entries in the shape `runmanager start` writes to `requests.json`: `id`, `note` (the request's note, a path inside the project folder), `line`, `text` (the whole request line), `comment` (the `%%` comment as written, markers included, or `null` when there is none). Example: `{"id": "r1", "note": "Ideas/idea-harrow-point.md", "line": 15, "text": "- [r] How did printed tide tables reach small villages in the 1950s? #research/run-2", "comment": "%% Look for printed almanacs. %%"}`.
2. **`expect.result`** is compared with the returned value by deep equality, after both lists are sorted by `request`. A `reason` is compared only as present or `null` unless the case gives `reason_includes` on that entry: `{ "request": "r1", ..., "reason_includes": ["second check"] }`.
3. **`expect.calls`** checks, per label: `count` (how many calls, retries included), `prompt_includes` and `prompt_excludes` (substrings of every call's prompt with that label).
4. **`expect.not_called`:** labels that must never be called.
5. **`expect.after`:** each pair `[A, B]` means every call labelled A started after every call labelled B ended.
6. **`expect.together`:** each list of labels must all have started before any of them ended, so they ran side by side. Give those calls a `delay_ms` long enough to overlap.
7. **The case writer works from the spec alone,** never from `research.js`. If a case needs a reading the spec doesn't settle, the case writer lists it in its report as a reading for the writer to approve. It never settles one silently.

## 6. Fixed facts the script and cases share

1. **Paths are absolute,** built from `args.project`: the plan at `{project}/llm-files/research-plans/research-plan-{research_topic}.md`, findings at `{project}/llm-files/research-findings/{run_id}/{research_topic}/topic-{n}.md`, the template copy at `{project}/Research/research-{research-topic}.md` (that literal file name, braces included), the request's note at `{project}/{request.note}`.
2. **The run date** is read from the run id: `run-2026-10-08-1400-research` gives `2026-10-08`.
3. **The outcome entry** is the shape in spec-run-manager.md 06 item 5: `request`, `outcome` (`passed`, `failed`, or `no findings`), `note` (the path inside the project folder, or `null`), `reason` (a string when `failed`, else `null`), `failed_topics` (a list). What one `failed_topics` entry holds is open: plan-research-workflow.md 05 item 19. The case writer proposes a reading.
4. **The cap is 15 researchers per request** (spec 09).

## 7. Self-test

The harness tests itself with a stand-in script and its own cases. Run it from the plugin root: `node lib/workflowtests/harness.mjs --script lib/workflowtests/selftest/script.js --cases lib/workflowtests/selftest/cases`. With no flags the harness runs `lib/research.js` and `lib/workflowtests/cases/`.

1. **`--script FILE` and `--cases DIR`** replace the defaults. Relative paths resolve from the folder you run in.
2. **`"expect_harness_fail": true` in a `case.json`** marks a case that is meant to fail. The harness prints `PASS {case} (failed as expected: ...)` when the case fails, and `FAIL {case}: expected the harness to fail this case, but it passed` when it doesn't. Real cases never use it.
3. **`"expect_fail_includes": "text"`** (optional, with the key above) also requires some failure reason to contain that text, so a case can't pass by failing for the wrong reason.
4. **`"script": "path"`** (optional, self-test only) runs that script for this case instead of the run's script. The path resolves from the case folder. The forbidden-call case needs it, because the scan reads the whole file.
