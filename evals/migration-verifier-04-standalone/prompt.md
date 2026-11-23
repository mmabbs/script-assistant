---
description: "Case 4, the standalone check (no V number in the ranked list): the migration-verifier misses an Area Note line that can't stand alone, or flags the writer's Rationale line. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, standalone-check]
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
          "text": "- Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. Mara has never forgiven her. #status/committed"
        },
        {
          "line": 11,
          "text": "%% Agent, char-mara. %%"
        },
        {
          "line": 13,
          "text": "- Mara swims in the harbour every morning at six, even in January. #status/committed"
        },
        {
          "line": 15,
          "text": "%% Agent, char-mara. %%"
        }
      ]
    }
  ]
}
```
