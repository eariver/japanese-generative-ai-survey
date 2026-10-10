# r12 Selection Core validation output (unmodified Core, read-only run)

Date: 2026-10-10Z
Core implementation: reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (working-tree
scripts unmodified; `git status` shows no `scripts/`/`config/`/`schemas/` changes).
State: `EVIDENCE_REVIEWED` (no transition attempted or performed).

## Command (equivalent)

`validate_selection(repo, selection-preview-r12.json, production-profile.json,
candidate-matrix-r10-staging.json, profile-completeness-v2.json, materiality-ledger-v2.json)`
via `scripts/survey_architecture_v2_base.py::validate_selection` (imported, NOT edited).

## Result

`PASS` — 0 errors.

## Basis binding (exact bytes verified)

- production_profile_sha256: `c921bd14…` (sources/2026-W40/production-profile.json)
- candidate_matrix_sha256: `f07b1166…` (candidate-matrix-r10-staging.json, UNCHANGED)
- profile_completeness_sha256: `f83b2d94…` (profile-completeness-v2.json, UNCHANGED)
- materiality_ledger_sha256: `ce63f3a9…` (materiality-ledger-v2.json, UNCHANGED)

## Semantic-conflict disclosure (validator-clean but editorially material)

The validator checks FORMAL consistency (IDs/coverage/roles/basis/summary). It passes
because the two corrected HOLD assignments carry usage NONE and no roles. It does NOT
certify editorial completeness: source truth (both IN-WINDOW + MATERIAL per Sol r11) vs
canonical HOLD is an acknowledged, documented gap (CORE_REENTRY_CONTRACT_GAP) carried in
the corrected rationales — NOT bypassed. No fake override, no recalculated SHA, no
acceptance masquerade.

## Tighter-than-expected constraints encountered

None blocked this unit: the compat route (28 SELECTED + corrected HOLD rationales +
separate NON_CANONICAL supplement) fits entirely within existing Core contracts.
Formal promotion of either item remains impossible without the Issue #562 Core
supersession path — as designed, not as a surprise.
