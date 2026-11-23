---
description: "Case for a retried piece (no second copy of a line whose pointer already names its note). Runs against the script-asst:migrator agent. The writer approved the Pass line on 2026-10-13."
tags: [retry, migrator-agent]
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
      "heading": "### 2026-10-07",
      "lines": [
        {
          "line": 13,
          "text": "%% Agent, both of these belong in idea-lighthouse. %%"
        }
      ]
    }
  ]
}
```
