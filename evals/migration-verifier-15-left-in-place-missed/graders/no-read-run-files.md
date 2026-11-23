---
type: tool_used
tool: Read
input_match: "(^|/)\\.runs/(units(/|$)|[^/]+/snapshot(/|$)|[^/]+/record-b\\d+-r\\d+\\.json$)"
min: 0
max: 0
arm: both
---

Ruling 03.10 test (audit-decisions-prewriting.md 03.10; spec-migration-verifier.md 10 Decisions Log item 29, third bullet). The agent reads only the files the prompt names in `.runs/`. Fails on any Read of the full record in `.runs/units/`, its saved copy `.runs/{run id}/record-b{N}-r{R}.json`, or a file in the before-snapshot `.runs/{run id}/snapshot/`. The runner matches a Read on its `file_path`, relative to `work/`.
