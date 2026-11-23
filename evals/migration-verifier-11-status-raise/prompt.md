---
description: "Case 11, V4: the migration-verifier asks for a status above the writer's own, for a provisional copy whose wording reads confidently. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v4-status-raise]
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
          "text": "- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional"
        },
        {
          "line": 11,
          "text": "%% Agent, idea-mara-lighthouse. %%"
        },
        {
          "line": 14,
          "text": "%% Agent, idea-mara-lighthouse. %%"
        }
      ]
    }
  ]
}
```
