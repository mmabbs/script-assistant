---
description: "Case 5, V7 and V8: the migration-verifier misses a line the migrator should have acted on, or reports a line as missed that wasn't. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v7-v8-missed-line]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep]
---

This is the migration-verifier's batch check, batch b1, round 0, of migration run run-2026-10-09-2100-migration.

- Project folder: project/
- Rules file: rules/migrator-rules.md
- Cut-down record: project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json
- Typed request: none

Batch b1, its pieces as they are in project/.runs/run-2026-10-09-2100-migration/batches.json:

```json
{
  "batch": "b1",
  "pieces": [
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-09",
      "lines": [
        {
          "line": 10,
          "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"
        },
        {
          "line": 11,
          "text": "%% Agent, char-mara. %%"
        },
        {
          "line": 13,
          "text": "- Mara sleeps in the watch room in winter, the relief keeper might be a woman from Oban, and the light could be decommissioned by spring. #status/committed"
        },
        {
          "line": 16,
          "text": "%% Agent, add this to the paraffin section of research-light-lighthouse-lamps. %%"
        }
      ]
    }
  ]
}
```
