---
description: "Case for the lost-or-changed-detail failure. Runs against the script-asst:migrator agent."
tags: [lost-detail, migrator-agent]
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
      "heading": "### 2026-09-30",
      "lines": [
        {
          "line": 32,
          "text": "%% migrate all the bullets between \"- The storm night\" to \"I keep coming back\" %%"
        },
        {
          "line": 34,
          "text": "%% Agent, these go in idea-storm-night. %%"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-01",
      "lines": [
        {
          "line": 18,
          "text": "%% migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" %%"
        },
        {
          "line": 20,
          "text": "%% Agent, these go in idea-harrow-point. %%"
        }
      ]
    }
  ]
}
```
