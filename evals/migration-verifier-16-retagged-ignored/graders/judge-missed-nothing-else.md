---
type: llm
---

The batch is two pieces of brain-dump.md:
- under "### 2026-10-02": "- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]" (line 11), re-tagged committed since an earlier run. This one is expected in `missed`; this check doesn't grade it.
- under "### 2026-10-09": the comment "%% Agent, idea-tobias. %%" (line 16), under "- Tobias once rowed to the mainland and back in a single night to win a bet." (line 15). Unit u1 copied that line to idea-tobias. Not missed.

The other line under "### 2026-10-02", "- Mara mends her own nets rather than buy new ones. #status/provisional [migrated-to:: …]" (line 10), didn't change since the earlier run and is not in the batch. Not missed.

PASS if the reply's `missed` list holds no entry other than the notebook line. An empty `missed` list also passes this check.
FAIL if `missed` holds the Tobias rowing line, its comment, or the nets line, or an entry about the earlier run's copies in idea-mara-habits. Quote the `missed` list.
