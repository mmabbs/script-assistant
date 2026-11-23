---
type: regex
pattern: "## Every topic(?:(?!\\n## )[\\s\\S])*(small[- ]town|picture palace)"
flags: i
match: not_contains
target: { source: file, path: project/llm-files/research-plans/research-plan-silent-film-cinemas.md }
---
