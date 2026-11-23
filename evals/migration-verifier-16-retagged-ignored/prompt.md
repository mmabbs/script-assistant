---
description: "Case 16, V7: a pointer line the writer re-tagged committed after an earlier run is in the batch, and the migrator only listed it in left_in_place. The migration-verifier must report it as missed. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v7-retagged-ignored]
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
      "heading": "### 2026-10-02",
      "lines": [
        {
          "line": 11,
          "text": "- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-09",
      "lines": [
        {
          "line": 16,
          "text": "%% Agent, idea-tobias. %%"
        }
      ]
    }
  ]
}
```
