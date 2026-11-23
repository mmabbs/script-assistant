---
description: "Case for the unasked-migration failure (lines outside the migrate range). Runs against the script-asst:migrator agent."
tags: [unasked-migration, migrator-agent]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Write, Edit]
---

This is a migration run: batch b1, round 0.

- Project folder: project/
- Rules file: rules/migrator-rules.md
- Typed request: none
- Unit record file: run/unit-records.json

Batch b1, its pieces as they are in batches.json:

```json
{
  "batch": "b1",
  "pieces": [
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-01",
      "lines": [
        {
          "line": 15,
          "text": "%% migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\" %%"
        },
        {
          "line": 17,
          "text": "%% Agent, these go in idea-harrow-point. %%"
        }
      ]
    }
  ]
}
```
