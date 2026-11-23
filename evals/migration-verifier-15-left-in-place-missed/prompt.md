---
description: "Case 15, V7 and V8: a committed line the migrator listed in left_in_place with no reason the rules allow, beside a line rightly left in place. Also checks that the agent never reads the full record in .runs/units/, its saved copy, or the before-snapshot. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, v7-v8-left-in-place-missed, blind-to-reasons]
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
          "text": "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"
        },
        {
          "line": 11,
          "text": "%% Agent, char-mara. %%"
        },
        {
          "line": 13,
          "text": "- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed"
        },
        {
          "line": 16,
          "text": "%% Agent, idea-tobias. %%"
        }
      ]
    }
  ]
}
```
