---
type: llm
---

The batch is four lines under "### 2026-10-09" in brain-dump.md:
- A: "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed", with the comment "Agent, char-mara." The record has no unit, question, or could_not entry for it. This is the planted miss: the writer's tag and comment asked for it, and nothing was done.
- B: "- Mara sleeps in the watch room in winter, the relief keeper might be a woman from Oban, and the light could be decommissioned by spring. #status/committed". Unit u1 graduated its first idea, and a `questions` entry covers the rest. Not missed.
- C: "- The old keepers logged every ship that passed.", with the comment "Agent, add this to the paraffin section of research-light-lighthouse-lamps." That note doesn't exist, and a `could_not` entry names line C. Not missed.
- D: "- What if the fog horn is broken all winter?". No tag and no comment, so nothing asked for anything. Not missed.

PASS if the reply's `missed` list holds exactly one entry, and that entry is line A, the oilskin coat line.
FAIL if line A is not in `missed`, or if `missed` holds line B, C, or D. Quote the `missed` list.
