---
type: llm
---

Unit u11's source line, in brain-dump.md, reads:
"- The relief keeper, maybe called Ewan, arrives each March and lodges above the pub on the quay. #status/provisional"

The migrator split it into two copies:
- in Ideas/idea-mara-lighthouse.md (line 10): "- The relief keeper, maybe called Ewan, arrives each March. #status/provisional"
- in Ideas/idea-harrow-point.md (line 10): "- Ewan, the relief keeper, lodges above the pub on the quay. #status/provisional"

The planted error: the writer hedged the name ("maybe called Ewan"). The idea-harrow-point copy uses "Ewan" as settled, and nothing in that note says the name is only a maybe. The rules say a hedged name is stated with its hedge where it's introduced and isn't used as settled on other lines, which refer to the thing by its role. The idea-mara-lighthouse copy is correct.

PASS if u11's verdict is `fix` and a problem says the idea-harrow-point copy states the name Ewan as settled, or loses the "maybe" on the name. Its check may be `lost-detail` or `status`; either is correct.
FAIL if u11 is approved, or if no problem names the settled "Ewan" (the lost hedge on the name) in the idea-harrow-point copy. Quote the verdict and the problems.
