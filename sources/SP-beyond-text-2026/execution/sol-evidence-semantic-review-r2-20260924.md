# TS-002 Sol Evidence Semantic Review r2

Status:

`SOL_EVIDENCE_SEMANTIC_REVIEW_R2 / SEMANTIC_DEPTH_PASS / REQUEST_CHANGES_PROVENANCE_REBIND_REQUIRED`

Date: `2026-09-24 JST`

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`

Reviewed branch state:

- work HEAD: `1e6679011bf33b0353bfae06cde8991415935abf`
- work tree: `8ba405cd6865c2d4062fe7160eb7473bf5236515`
- main HEAD: `0bbb02b3c5963403860897daec2feaf61e82589a`
- main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`

Reviewed Evidence: r2 result-set `048cbd0942f073ed6ba134c97a5691e9ea4eb1eb0db6fa1ed842abe5faf2810e`
(139 Cards: 125 VERIFIED / 9 PARTIAL / 5 NEEDS_MORE) + transition ledger (43 entries).

## Decision

**SEMANTIC_DEPTH_PASS / REQUEST_CHANGES_PROVENANCE_REBIND_REQUIRED.**

Evidence semantic depth r2 itself is approved:

- Layer A factual Evidence: semantic depth **PASS**
- Layer B transition ledger: **PASS**
- source-body consumption discipline: **PASS_WITH_DECLARED_PARTIAL_AND_BLOCKED**
- PARTIAL / NEEDS_MORE boundary treatment: **PASS**
- r1 preservation: **PASS**

## Remaining blocker

Canonical provenance locator rebinding. The r2 campaign consumed verified-correct
bodies for 21 transcribed arXiv locators (plus identified v2/IEEE/CompVis identity
repairs for BT-D062/BT-D089/BT-D024), but canonical Discovery still binds the
known-wrong locators. Repair scope is **provenance only**:

- rebind the verified locators (this repair);
- BT-D062 v2 identity + card update from the v2 body only;
- BT-D089 IEEE rebind, PARTIAL retained, no promotion;
- BT-D024 CompVis identity verification with historical consistency;
- no false promotion of other PARTIAL / NEEDS_MORE barriers;
- canonical propagation (Discovery → Screening → Evidence → Views → ledger) with
  unchanged decision semantics and unchanged semantic payload except BT-D062.

## Explicitly not requested

- No redo of the semantic Evidence campaign.
- No Discovery research, X collection, or Screening research rerun.
- Materiality advance: **NOT_YET_AUTHORIZED**. Materiality / Completeness /
  Selection / Architecture remain pending Sol provenance readback.

## Provenance note

This file transcribes the operator-supplied Sol/ChatGPT review decision for this
repair run. It is not generated as the executing operator's own approval judgment.
