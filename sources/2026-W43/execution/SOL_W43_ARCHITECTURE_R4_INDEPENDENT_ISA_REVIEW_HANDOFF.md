# SOL W43 Architecture r4 independent ISA review handoff (Muse → Sol)

Status: `SOL_W43_ARCHITECTURE_R4_INDEPENDENT_ISA_REVIEW_READY`
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. Starting HEAD `db78839bd7cb858a6cc5b1620bf6c574f064339f` / Tree `b1ee9c3e686e3f50cfabc9d679eff7e01937726e` (remote 6-way MATCH pre-write; local aligned).

## What Muse did (one integrated r4, no Stage)

- Archived exact r3 proposal surfaces (7 files + README + SHA256SUMS, cmp-verified) to `execution/history/selection-architecture-r3/`.
- Built `execution/compat/selection-architecture-input-r4.json` (`67d0f39f…`, assignments 32/32 identical r3) with all nine ISA editorial corrections (P1 source-separated, P2 bounded, Japanese/availability fixed).
- Regenerated in isolated detached scratch @db78839bd (no new branch) with unchanged frozen runner → 19/8/READY; Matrix/Selection byte-identical r3; Architecture `9ab37dd6…`, Summary `c8bb6e2e…`; rebuilt full attention limit=100 → 68/68 byte-identical `7c3e4deb…`; reconciled audit `ff2267e2…`; stage precheck EVIDENCE_REVIEWED→SELECTION_COMPLETE PASS (no writes); second bridge NOT run; nine edition-local negatives all fail-closed.
- Reflected exact tested bytes to the work branch (proposal surfaces + r3 archive + editorial pack only). No shared-Core, Evidence, State, Checkpoint, Gate, main, or Frozen mutation. No ADVANCE_STAGE / operator comment / Human decision / Draft / TeX / PDF.

## What Sol must independently re-audit (before any trusted Stage)

1. All nine ISA closures in `execution/reviews/muse-w43-independent-isa-closure-architecture-r4-20261025.md`, especially P1 source semantics (DeepInfer mode separation; Voxtral UNRESOLVED conflict with no unified number).
2. The 19-risk ledger `execution/reviews/w43-human-selected-19-risk-register-r4.md` and crosswalk `execution/source-intake/w43-independent-isa-primary-source-conflict-crosswalk-r4.md` (rendered reads 2026-10-25, no new canonical raw).
3. Frozen-native regeneration integrity (Matrix/Selection identical, 19/19 placements, 68/68, audit SHAs, stage precheck transcript).
4. Selection invariance: 19 SELECTED / 1 HOLD / 12 REJECT, 8 packages, 31 must-covers, 5 LIMITED carried.

Both trusted bridges remain NO/NO. Both Human Gates remain PENDING. This handoff confers no approval.
