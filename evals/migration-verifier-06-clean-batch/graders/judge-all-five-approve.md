---
type: llm
---

Every unit in this batch is correct. Nothing was planted.

- u1. Source in brain-dump.md: "- Tobias wanted to be a lighthouse keeper too, before the accident." Comment: "Agent, idea-tobias." Copy in Ideas/idea-tobias.md: the same text.
- u2, a split. Source in brain-dump.md: "- The causeway floods twice a month, and Mara times her supply runs around the tide table." Comment: "Agent, the flooding goes in idea-harrow-point, the supply runs in idea-mara-lighthouse." Copies: in Ideas/idea-harrow-point.md, "- The causeway to Harrow Point floods twice a month."; in Ideas/idea-mara-lighthouse.md, "- Mara times her supply runs around the tide table, because the causeway floods twice a month." Each copy reads on its own and loses nothing.
- u3, a merge. Sources in brain-dump.md: "- The new keeper could be someone from the mainland who's never seen the sea." and "- What if the relief keeper is scared of the water?" One comment under both: "Agent, these two are the same idea. Merge them into idea-mara-lighthouse." Copy in Ideas/idea-mara-lighthouse.md: "- The relief keeper could be someone from the mainland who has never seen the sea and is scared of the water." It keeps "could," and the "what if" stays a possibility.
- u4, a rejection. In Ideas/idea-mara-lighthouse.md, the line "- Mara keeps a dog called Skipper." had the comment "%% Agent, reject the dog. It makes her too cosy. %%" under it. The line is gone from the live part. Under "## Rejected" the copy is two lines: "- Mara keeps a dog called Skipper. #status/rejected", then on the next line "%% It makes her too cosy. %%". The writer's comment stays where it was. A comment holding only the writer's reason, on the line below the rejected line, is the settled form for a reason on a Rejected line, so the reason comment is correct.
- u5. Source in brain-dump.md: "- Tobias kept a tin of sea glass under his bed." Comment: "Agent, migrate this." It names no destination. Copy in Ideas/idea-tobias.md: the same text. Where a unit went is not judged when the writer named no note.

PASS if all five units, u1 to u5, have the verdict `approve` with no problems.
FAIL if any unit's verdict is `fix`. A problem on u5 about where it went is the clearest fail. A problem on u4's reason comment, "%% It makes her too cosy. %%" (that it was added, that it isn't on the rejected line, or that it changes the writer's words), is a fail too. Quote the verdict and the problems.
