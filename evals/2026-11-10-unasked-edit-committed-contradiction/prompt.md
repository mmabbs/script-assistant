---
description: "Case for the unasked-edit failure (committed contradiction). A committed line clashes with a line already in the Area Note. Runs against the script-asst:migrator agent. The user has not reviewed the expected result."
tags: [unasked-edit, migrator-agent]
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
          "text": "- Tobias drowned last spring, and Mara still hasn't cleared out his room. #status/committed"
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
