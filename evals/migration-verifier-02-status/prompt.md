---
description: "Case 2, V2: the migration-verifier misses a status error. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v2-missed-status]
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
          "text": "- Mara learned to read the weather from her father's barometer notes. #status/provisional"
        },
        {
          "line": 11,
          "text": "%% Agent, migrate this. %%"
        },
        {
          "line": 13,
          "text": "- Mara has never once left Harrow Point overnight. #status/committed"
        },
        {
          "line": 14,
          "text": "%% Agent, this goes in char-mara. %%"
        },
        {
          "line": 16,
          "text": "- Mara keeps the light by hand when the power fails, winding the old clockwork. #status/committed"
        },
        {
          "line": 17,
          "text": "%% Agent, char-mara. %%"
        }
      ]
    }
  ]
}
```
