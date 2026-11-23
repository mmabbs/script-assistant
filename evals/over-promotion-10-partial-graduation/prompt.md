---
description: "Case for the over-promotion failure (partial graduation). Runs against the script-asst:migrator agent."
tags: [over-promotion, migrator-agent]
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
          "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
        },
        {
          "line": 13,
          "text": "%% Agent, this belongs in char-mara. %%"
        }
      ]
    }
  ]
}
```
