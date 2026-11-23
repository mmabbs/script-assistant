---
description: "Case 7, V3: the migration-verifier says an asked-for change wasn't asked for, at the batch check. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v3-asked-judged-unasked]
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
          "text": "%% Agent, idea-mara-lighthouse. %%"
        }
      ]
    },
    {
      "note": "Ideas/idea-mara-lighthouse.md",
      "heading": null,
      "lines": [
        {
          "line": 12,
          "text": "%% Agent, please correct the spelling in that line. %%"
        },
        {
          "line": 15,
          "text": "%% Agent, tidy the grammar here. %%"
        }
      ]
    }
  ]
}
```
