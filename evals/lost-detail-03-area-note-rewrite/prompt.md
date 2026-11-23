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
      "heading": "### 2026-10-01",
      "lines": [
        {
          "line": 10,
          "text": "- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed"
        },
        {
          "line": 12,
          "text": "%% Agent, this belongs in char-mara. %%"
        }
      ]
    }
  ]
}
```
