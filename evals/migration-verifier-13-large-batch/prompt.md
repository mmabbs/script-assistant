---
description: "Case 13, scale: twenty units over three date headings, with three planted errors a careful reader could pass over. Runs against the script-asst:migration-verifier agent."
tags: [migration-verifier, scale-large-batch]
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep]
---

This is the migration-verifier's batch check, batch b1, round 0, of migration run run-2026-10-09-2100-migration.

- Project folder: project/
- Rules file: rules/migrator-rules.md
- Cut-down record: project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json
- Typed request: none

Batch b1, its pieces as they are in project/.runs/run-2026-10-09-2100-migration/batches.json:

```json
{
  "batch": "b1",
  "pieces": [
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-07",
      "lines": [
        {
          "line": 19,
          "text": "%% Agent, migrate all the bullets between \"- Tobias taught Mara\" and \"- Tobias wanted to leave\" to idea-tobias. %%"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-08",
      "lines": [
        {
          "line": 23,
          "text": "- Mara keeps the lamp lens polished with her mother's old silk scarf. #status/committed"
        },
        {
          "line": 24,
          "text": "- I think Mara only ever drinks tea, never coffee, since Tobias died. #status/committed"
        },
        {
          "line": 26,
          "text": "- The relief keeper, maybe called Ewan, arrives each March and lodges above the pub on the quay. #status/provisional"
        },
        {
          "line": 27,
          "text": "- Mara won't let anyone else wind the clockwork. #status/committed"
        },
        {
          "line": 29,
          "text": "- The harbour freezes over in hard winters. #status/provisional"
        },
        {
          "line": 30,
          "text": "- Mara reads the shipping forecast aloud to an empty room every night. #status/provisional"
        }
      ]
    },
    {
      "note": "brain-dump.md",
      "heading": "### 2026-10-09",
      "lines": [
        {
          "line": 36,
          "text": "%% Agent, idea-tobias. %%"
        },
        {
          "line": 39,
          "text": "%% Agent, idea-mara-habits. %%"
        },
        {
          "line": 42,
          "text": "%% Agent, idea-harrow-point. %%"
        },
        {
          "line": 45,
          "text": "%% Agent, idea-mara-lighthouse. %%"
        },
        {
          "line": 48,
          "text": "%% Agent, idea-mara-lighthouse. %%"
        },
        {
          "line": 50,
          "text": "- Mara's hands shake when she climbs the last flight of stairs. #status/committed"
        },
        {
          "line": 51,
          "text": "%% Agent, char-mara. %%"
        }
      ]
    }
  ]
}
```
