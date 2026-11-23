---
description: "Case for the over-promotion failure. Runs against the script-asst:migrator agent."
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
          "line": 13,
          "text": "- The lighthouse stays in the family, that's decided. #status/provisional"
        },
        {
          "line": 14,
          "text": "- Mara gets seasick, badly. #status/provisional"
        },
        {
          "line": 18,
          "text": "%% migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\" %%"
        },
        {
          "line": 20,
          "text": "%% Agent, these go in idea-mara-backstory. %%"
        }
      ]
    }
  ]
}
```
