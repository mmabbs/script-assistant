---
type: regex
pattern: "seaside-trades-history\\.example|yorkshire-coast-archive\\.example|east-sussex-records\\.example"
flags: i
match: not_contains
target: { source: file, path: project/Research/research-bathing-machines.md }
---
