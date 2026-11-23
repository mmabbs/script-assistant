---
description: "Case for the wrong-destination failure (no destination named). Runs against the script-asst:migrator agent. The user has not reviewed the expected result."
tags: [wrong-destination, migrator-agent]
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
          "line": 10,
          "text": "- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"
        },
        {
          "line": 11,
          "text": "- On the storm night the foghorn was already broken. #status/provisional"
        },
        {
          "line": 12,
          "text": "- The lamp's lens was cracked by a gull in 2003. #status/provisional"
        },
        {
          "line": 13,
          "text": "- Coyle closed the pub early that night, which he never does. #status/provisional"
        }
      ]
    }
  ]
}
```
