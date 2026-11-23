---
description: "Case for the missed-unit failure (scattered tags). Runs against the script-asst:migrator agent. The user has not reviewed the expected result."
tags: [missed-unit, migrator-agent]
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
      "heading": null,
      "lines": [
        {
          "line": 8,
          "text": "%% Agent, anything I tag provisional under these three dates goes in idea-harrow-point. Leave the untagged lines where they are. %%"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-09-28",
      "lines": [
        {
          "line": 30,
          "text": "- The council sold the fish market roof for scrap in 2011. #status/provisional"
        },
        {
          "line": 33,
          "text": "- The cliff path lost twelve metres to the sea last winter. #status/provisional"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-09-30",
      "lines": [
        {
          "line": 22,
          "text": "- The primary school has nine pupils, all cousins. #status/provisional"
        },
        {
          "line": 25,
          "text": "- A seal called Mister Hale comes into the harbour every October. #status/provisional"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-01",
      "lines": [
        {
          "line": 13,
          "text": "- The post office doubles as the undertaker's. #status/provisional"
        },
        {
          "line": 16,
          "text": "- The chemist, Ferris, fills prescriptions from memory. #status/provisional"
        }
      ]
    }
  ]
}
```
