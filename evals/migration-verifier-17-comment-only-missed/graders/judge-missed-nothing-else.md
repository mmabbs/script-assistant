---
type: llm
---

The batch is two comments under "### 2026-10-09" in brain-dump.md, each under an untagged line:
- "%% Agent, idea-tobias. %%" (line 11), under "- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone." (line 10). Nothing in the record names it. This one is expected in `missed`; this check doesn't grade it.
- "%% Agent, idea-mara-lighthouse. %%" (line 14), under "- Mara leaves the lamp-room door open so she can hear the foghorn from the kitchen." (line 13). Unit u1 copied that line to idea-mara-lighthouse. Not missed.

PASS if the reply's `missed` list holds no entry other than the ribbon line (or its comment). An empty `missed` list also passes this check.
FAIL if `missed` holds the lamp-room line or its comment. Quote the `missed` list.
