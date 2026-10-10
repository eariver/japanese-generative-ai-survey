# Muse W40 r17 — ONLY two minor r16 audit documentation repairs

Status: `BOUNDED_EDITION_LOCAL_EXECUTION / TWO_MINOR_FINDINGS_ONLY / ZERO_CORE_WRITES`
Date: 2026-10-10 JST
Repo: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W40-v2-work`
Exact starting SHA/Tree: PROVIDED BY OUTER SOL PROMPT AFTER THIS FILE COMMIT.
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Sol r16 audit adoption: `sources/2026-W40/execution/reviews/sol-w40-r16-independent-audit-disposition-20261010.md`

## 0. Preflight / restrictions

BEFORE ANY WRITE read-only verify remote W40 branch HEAD and Tree identical to outer Exact Starting SHA and Expected Tree; remote main HEAD == Reviewed main SHA `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (this does NOT mean W40 HEAD == main HEAD); state `EVIDENCE_REVIEWED`, next `stage:selection`, Selection+Architecture checkpoints pending, both Human Gates pending with null provenance, exception inactive.

Verify four source byte hashes directly (DO NOT regenerate sources):
- selection-preview-r13.json: `dc0247781b0401e62eb8b17980050769b743f2aa313ffda3f5b5704235db0cb1`
- candidate-matrix-r10-staging.json: `f07b1166eef02598a1d57ebd7d0068119678fcfc17f1d118ef2b582594a736f6`
- architecture-coverage-r14.json: `3de8bd56f71996e6c6ff075157967507a03650de3fd10c15b31e72faebc671cc`
- architecture-boundaries-r15.json: `1736737e9488e3a6e2a94471bfc506fdc43c9f18d5321bbc31b25bb99eb749c7`

Mismatch at ANY guard → ZERO WRITES; report actual vs expected and STOP.
No new branches, reset/rebase/force/history rewrite. Normal commit/non-force push existing W40 only.

BANNED modifications: `scripts/`, `schemas/`, `config/`, `.github/`, shared Core, other Editions, main, Issue, accepted Discovery/Evidence/Selection/Matrix/Coverage, `architecture-boundaries-r15.json`, all r15/r16 artifacts, state/checkpoints/Gates. NO rerun/regenerate of Selection, 113 Boundary data, technical drafts. NO Human approval, Architecture, freeze, release, or supplement.

## 1. R16-F01: record ACTUAL deterministic reconstruction digests

Inputs:
- `sources/2026-W40/execution/selection/selection-preview-r13.json`
- `sources/2026-W40/execution/selection/candidate-matrix-r10-staging.json`
- `sources/2026-W40/execution/architecture-coverage-r14.json`
- `sources/2026-W40/execution/architecture-boundaries-r15.json`
- `sources/2026-W40/execution/architecture-boundaries-validation-addendum-r16.json`

Create successor **`execution/architecture-boundaries-roundtrip-digests-r17.json`**, do not edit r16 addendum.

On EXACT original candidate-to-package mapping from SELECTED assignments and Coverage r14, for each of P1,P2,P3,P4,P5,P6a,P6b,P7,P8:

1. Retrieve verbatim `remaining_boundaries` strings for the assigned candidates directly from Matrix r10; Role/usage/membership verified against Selection/Coverage. Never edit text or normalize.
2. Independently repeat derivation TWICE from immutable source data: `canonical_array = sorted(set(all_original_boundary_strings_of_package))` with Python Unicode code-point ordering (not locale-dependent). Both passes must genuinely recompute the content (not reuse a stored checksum).
3. Canonical serialization for each array exactly `json.dumps(canonical_array, ensure_ascii=False, separators=(',', ':')).encode('utf-8')`, no BOM and no newline. SHA-256 of those UTF-8 bytes, **full 64 hex chars**, for each pass.
4. Serialize the unchanged stored r15 package `boundaries` array with the SAME serializer (but do not re-sort) and record its own 64-hex `stored_array_sha256`; `stored_array_order_equal` may be false, `semantic_set_equal` must be true. Distinguish algorithmic idempotence from ordering equality, and do not claim byte-identical when sorted vs insertion order differs.
5. Machine-readable per-package record: `raw_count`, `unique_count`, `removed_duplicates`, `pass1_sha256`, `pass2_sha256`, `stored_array_sha256`, `pass_digests_equal`, `stored_order_equal`, `semantic_set_equal`, `missing_count`, `extra_count`. On mismatch include offending exact string/ID.
6. Full comparison: 28 selected IDs, 20 PRIMARY/8 SUPPORTING, 113 raw relationships, 105 package-unique strings, 8 dedup, 0 missing/extra, 0 internal duplicates. Confirm per-package expected table (P1 14/12/2, P2 8/8/0, P3 13/13/0, P4 10/8/2, P5 18/17/1, P6a 10/10/0, P6b 15/15/0, P7 19/16/3, P8 6/6/0).
7. Store exact source paths/hash, serializer name, Python version, explicit algorithm, whether independent derivation was actually executed vs simulated, and 9/9 digest equality. `PASS` only when all recomputed objective checks are true. Never write fictitious hashes.

If needed, create a tiny W40-local reproducibility note describing the above method; do not modify shared Core scripts.

## 2. R16-F02: correct ambiguous historical Git description

Create **`execution/SOL_W40_R16_HANDOFF_GIT_IDENTITY_CORRECTION_R17.md`** (additive addendum; preserve historical r16 Handoff intact).

State explicitly:
- historical r16 Handoff §1 `HEAD == main` is inaccurate if read as SHA equality and is WITHDRAWN;
- exact r16 preflight W40 branch HEAD == `109ddbddd8c00f81f58302d261750cfd26e14f2e`, Tree == `13258c731f72f5b624c48ccb2953b77fcd6da596`;
- remote main HEAD == reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, separately (they are DIFFERENT SHAs);
- final r16 W40 HEAD `aad4b80e6b1c767671a5ecfe8c9d2e3166743bb7`, Tree `8f76727e1345dc5220714258ca09b2e7e6f7eb58`;
- no false branch-equality implication, no rewrites of original r16 Git evidence.

## 3. Minimal closeout

Create `execution/SOL_W40_R17_TWO_MINOR_DOCUMENTATION_HANDOFF.md` + actual-date session log under `execution/sessions/`; append to `execution/index.md`.

Findings `R16-F01` and `R16-F02`: evidence-graded `CORRECTED/PARTIAL/OPEN`, not unconditional. No other Work. All old r15/r16 files immutable. Expected changes: 4 new edition-local docs (digest JSON, Git correction MD, r17 Handoff, session log), plus append-only index; optional small algorithm note only if justified.

After normal non-force push: verify remote W40 HEAD/Tree, direct parent FF, only allowed files, remote main unchanged, production-state Git blob unchanged, accepted source SHAs unchanged, checkpoints/Gates untouched, Issue #562 remains separate. Report exact Final HEAD/Tree, per-package checksum table, 9/9 comparisons and outcomes, two findings, and residual constraints.

Terminal status: `SOL_W40_R17_TWO_MINOR_DOCUMENTATION_REVIEW_REQUIRED`. STOP. Do not stage Selection/Architecture, authorize publication, or claim official Edition release.
