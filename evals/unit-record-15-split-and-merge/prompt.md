---
description: "Case for the bad-unit-record failure (split and merge). Runs against the script-asst:migrator agent. The user has not reviewed the expected result."
tags: [unit-record, migrator-agent]
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
          "line": 12,
          "text": "%% Agent, migrate this. The bell ringing goes in idea-harrow-point, the part about Tobias in idea-tobias. %%"
        },
        {
          "line": 17,
          "text": "%% Agent, these two are one idea. Merge them into one unit in idea-mara-lighthouse. %%"
        },
        {
          "line": 19,
          "text": "- The lamp room smells of paraffin and wet wool. #status/provisional"
        },
        {
          "line": 21,
          "text": "%% Agent, the paraffin line goes in idea-mara-lighthouse too. %%"
        }
      ]
    }
  ]
}
```
