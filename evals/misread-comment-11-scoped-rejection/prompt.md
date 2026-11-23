---
description: "Case for the ignored-or-misread-comment failure (scoped rejection). Runs against the script-asst:migrator agent."
tags: [misread-comment, migrator-agent]
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
          "text": "%% Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear. %%"
        }
      ]
    }
  ]
}
```
