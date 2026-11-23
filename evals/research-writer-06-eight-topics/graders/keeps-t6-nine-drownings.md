---
type: regex
pattern: "(?<![\\^\\d])(9|nine)\\b[^.\\n]{0,40}drown|drown[^.\\n]{0,40}(?<![\\^\\d])(9|nine)\\b"
flags: i
target: { source: file, path: project/Research/research-ice-trade.md }
---
