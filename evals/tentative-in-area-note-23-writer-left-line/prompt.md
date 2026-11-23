---
description: "Case for the tentative-in-area-note failure (a provisional line the writer left in an Area Note). Runs against the script-asst:migrator agent. The writer approved the Pass line on 2026-10-14."
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
      "heading": "### 2026-10-14",
      "lines": [
        {
          "line": 10,
          "text": "- Mara rows out to the bell buoy every Sunday to scrape the gull droppings off it. #status/provisional"
        },
        {
          "line": 11,
          "text": "%% Agent, this goes in idea-mara-habits. %%"
        }
      ]
    },
    {
      "note": "char-mara.md",
      "heading": null,
      "lines": [
        {
          "line": 26,
          "text": "- Mara is wary of the mainland doctor. #status/provisional"
        }
      ]
    }
  ]
}
```
