# SOL W43 Architecture r6 post-audit repair handoff (Muse → Sol)

Status: `SOL_W43_ARCHITECTURE_R6_CORRECTION_READY_FOR_SOL_REVIEW`
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. Starting HEAD `b7445700dd852024ac27f1feaed58a61de9a9a42` / Tree `e5cd33332af5aa52ba6358d3296510ee2ac44d6b` (remote 6-way MATCH pre-write).

## What Muse did (one governed r6, no Stage, no Human operation)

- Preserved exact r5 established proposal in NEW immutable `execution/history/selection-architecture-r5-established/` (7 files + README + SHA256SUMS, cmp-verified); r3/r4 unchanged.
- Ran frozen `invalidate-pending-gate` (ARCHITECTURE_REVIEW → EVIDENCE_REVIEWED, R5-N01/02/03 reason, adjudication+audit refs, HEAD locks b7445700…) → exit 0, record `architecture-invalidation-0001.json` (`human_decision=false`), frozen validation PASS. No Human REQUEST_CHANGES or approval generated.
- Fixed R5-N01 (separate ratio/percent denominators), R5-N02 (uninverted GH 15:18:14Z/npm 15:21:49Z with independent publisher fetches), R5-N03 (CVE qualified wording) — Architecture wording/provenance only.
- Regenerated in isolated detached scratch (invalidated EVIDENCE_REVIEWED bytes, no branch) with unchanged frozen runner → 19/8/READY; Matrix/Selection byte-identical r3/r4/r5; Architecture `7d8f0ea5…`, Summary `38c17ecc…`; full attention limit=100 → 68/68 identical `7c3e4deb…`; audit `d27adb84…`; stage precheck EVIDENCE_REVIEWED→SELECTION_COMPLETE PASS (no writes); second bridge NOT run; 9+3 prior + 3 new negatives all fail-closed.
- Reflected exact tested bytes to the work branch (invalidation record + r5 archive + r6 surfaces + editorial pack). No shared-Core, Evidence, Gate, main, or Frozen mutation. No ADVANCE / operator bridge / Human decision / Draft / TeX / PDF.

## What Sol must independently check (targeted, before any re-bridging)

1. Invalidation legitimacy: pending unpresented Gate, EVIDENCE_REVIEWED boundary, `human_decision=false`, record validity, State resumable with both checkpoints pending.
2. R5-N01/02/03 textual fixes + TanStack publisher fetches + arithmetic (25.37x/22.31x/95.52%, 1139−1089=50).
3. Frozen-native regen integrity (Matrix/Selection identical, 19/19 placements, 8 packages/31 must-covers, 68/68, audit SHAs, precheck transcript).
4. Selection invariance 19/1/12 + 5 LIMITED; no upstream Evidence invalidation.

Next (Sol-owned): TWO SEPARATE NEW trusted ADVANCE requests (Selection unchanged, then Architecture r6) with real receipts, then the first authentic Human Architecture Review. This handoff confers no approval.
