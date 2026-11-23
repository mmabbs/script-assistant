---
description: "Case 1, V1: the migration-verifier misses a lost hedge or a lost story detail. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v1-missed-lost-detail]
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
          "line": 11,
          "text": "%% Agent, the drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%"
        },
        {
          "line": 14,
          "text": "%% Agent, this goes in idea-mara-lighthouse. %%"
        },
        {
          "line": 17,
          "text": "%% Agent, idea-mara-lighthouse. %%"
        }
      ]
    }
  ]
}
```
