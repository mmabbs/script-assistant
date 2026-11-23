---
description: "Case 6, V4: the migration-verifier invents a problem in a correct unit. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v4-invented-problem]
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
          "text": "%% Agent, the flooding goes in idea-harrow-point, the supply runs in idea-mara-lighthouse. %%"
        },
        {
          "line": 18,
          "text": "%% Agent, these two are the same idea. Merge them into idea-mara-lighthouse. %%"
        },
        {
          "line": 21,
          "text": "%% Agent, migrate this. %%"
        }
      ]
    },
    {
      "note": "Ideas/idea-mara-lighthouse.md",
      "heading": null,
      "lines": [
        {
          "line": 12,
          "text": "%% Agent, reject the dog. It makes her too cosy. %%"
        }
      ]
    }
  ]
}
```
