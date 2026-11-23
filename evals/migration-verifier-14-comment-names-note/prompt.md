---
description: "Case 14, V5: the writer's comment names a note, and the copy went elsewhere. The migration-verifier misses the scope error. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v5-comment-names-note]
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
          "text": "%% Agent, the chandlery goes in idea-harrow-point, the only-shop habit in idea-mara-habits. %%"
        },
        {
          "line": 14,
          "text": "%% Agent, migrate this. %%"
        },
        {
          "line": 17,
          "text": "%% Agent, put this with the rest of Tobias's material. %%"
        }
      ]
    }
  ]
}
```
