# r13 Selection Core validation output (unmodified Core, read-only run)

Date: 2026-10-10
Core implementation: reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (working-tree
scripts unmodified; `git status` shows no `scripts/`/`config/`/`schemas/` changes —
only pre-existing untracked `scripts/__pycache__/`).
State: `EVIDENCE_REVIEWED` (no transition attempted or performed).

## Command (equivalent)

`validate_selection(repo, selection-preview-r13.json, production-profile.json,
candidate-matrix-r10-staging.json, profile-completeness-v2.json, materiality-ledger-v2.json)`
via `scripts/survey_architecture_v2_base.py::validate_selection` (imported, NOT edited).

## Change vs r12 (authorized single-disposition edit only)

`selection-preview-r12.json` → `selection-preview-r13.json` diff (exact):
- `selection_version`: `r12-preview-1` → `r13-preview-1`;
- `candidate:2026-W40:071ac2e6d62319fd` (DGX Spark): `INSPECT` → `REJECT` + Sol-worded
  rationale (standalone-item editorial exclusion; in-window status and facts preserved);
- `summary`: `{35, {HOLD:4, SELECTED:28, INSPECT:1, REJECT:2}, 28}` →
  `{35, {HOLD:4, SELECTED:28, REJECT:3}, 28}` (recomputed from actual bytes).
- No Candidate ID, basis, assignment-field, or upstream-byte changes.

## Result

`PASS` — 0 errors.

## Basis binding (exact bytes verified)

- preview-r13 SHA-256: `dc0247781b0401e62eb8b17980050769b743f2aa313ffda3f5b5704235db0cb1`
- production_profile_sha256: `c921bd14…` (unchanged)
- candidate_matrix_sha256: `f07b1166…` (UNCHANGED)
- profile_completeness_sha256: `f83b2d94…` (UNCHANGED)
- materiality_ledger_sha256: `ce63f3a9…` (UNCHANGED)

## Semantic-conflict disclosure (validator-clean but editorially material)

The validator checks FORMAL consistency (IDs/coverage/roles/basis/summary). It passes
because the amended DGX REJECT carries usage NONE and no roles, like the other
non-selected assignments. It does NOT certify editorial completeness: the two
AstaBrief/AutoSynthData HOLDs remain an acknowledged, documented gap
(CORE_REENTRY_CONTRACT_GAP, Issue #562) staged noncanonically in
`execution/editorial-supplement/r13/` — NOT bypassed. This preview is review-only and
is still NOT authorized as full editorially sufficient Selection (per r13 instruction
§2: AstaBrief/AutoSynthData retain canonical HOLD). No acceptance masquerade, no
State/checkpoint change.
