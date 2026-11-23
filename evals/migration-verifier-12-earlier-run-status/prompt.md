---
description: "Case 12, V8: a copy from an earlier run sits below the writer's new, higher tag. The migration-verifier calls it a status fix or a missed line. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v8-earlier-run-status]
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
          "text": "- Mara rows out to the wreck buoy every Sunday to leave flowers for Tobias. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-09",
      "lines": [
        {
          "line": 15,
          "text": "- Mara has stopped answering letters from the mainland. #status/provisional"
        },
        {
          "line": 16,
          "text": "%% Agent, idea-mara-habits. %%"
        }
      ]
    }
  ]
}
```
