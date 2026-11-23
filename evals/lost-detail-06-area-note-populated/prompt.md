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
          "text": "- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed"
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
