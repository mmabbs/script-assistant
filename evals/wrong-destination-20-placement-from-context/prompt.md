---
description: "Case for the wrong-destination failure (placement from the lines around it). Runs against the script-asst:migrator agent. The user has not reviewed the expected result."
tags: [wrong-destination, migrator-agent]
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
      "heading": "### 2026-10-05",
      "lines": [
        {
          "line": 10,
          "text": "- Harrow Point is the last stop on the ferry line, and fog sits on it most mornings. #status/provisional"
        },
        {
          "line": 11,
          "text": "- The ferry horn and the fog signal sit a half-step apart, so on foggy mornings nobody can tell which is which. #status/provisional"
        },
        {
          "line": 12,
          "text": "- The lamp has to be wound by hand every four hours. #status/provisional"
        }
      ]
    }
  ]
}
```
