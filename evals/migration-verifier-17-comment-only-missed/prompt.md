---
description: "Case 17, V7: an untagged line only a comment triggered, and the migrator did nothing with it. Nothing in the record names it, and code can't see it. The migration-verifier must report the line as missed. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v7-comment-only-missed]
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
          "text": "%% Agent, idea-tobias. %%"
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
