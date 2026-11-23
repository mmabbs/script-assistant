---
description: "Case for the tentative-in-area-note failure (tagged child). Runs against the script-asst:migrator agent. The user has not reviewed the expected result."
tags: [tentative-in-area-note, migrator-agent]
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
          "text": "- Mara keeps a logbook of every ship that passes. #status/committed"
        },
        {
          "line": 12,
          "text": "    - She has started leaving gaps in it on purpose. #status/provisional"
        },
        {
          "line": 14,
          "text": "%% Agent, the committed material belongs in char-mara. The provisional line goes in idea-mara-habits. %%"
        }
      ]
    }
  ]
}
```
