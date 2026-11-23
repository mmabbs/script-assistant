Judge every unit in the record, and list any line in the batch that was left out. Answer with JSON only, in this shape:

```json
{
  "batch": "b2",
  "round": 0,
  "units": [
    {
      "unit": "u3",
      "verdict": "fix",
      "problems": [
        {
          "check": "<check>",
          "note": "<note path>",
          "line": 0,
          "what": "<one or two sentences, in plain words, for the writer>"
        }
      ]
    },
    { "unit": "u4", "verdict": "approve", "problems": [] }
  ],
  "missed": [
    {
      "source": { "note": "<note path>", "line": 0, "text": "<the line>" },
      "what": "<one or two sentences, in plain words, for the writer>"
    }
  ]
}
```

Each problem's `check` is one of `lost-detail`, `status`, `scope`, `standalone`.
