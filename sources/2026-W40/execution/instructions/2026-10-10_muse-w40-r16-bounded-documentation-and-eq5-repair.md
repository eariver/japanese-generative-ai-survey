# Muse W40 r16 — Bounded r15 audit-document corrections and ContextLM Eq.5

Status: `SOL_EXECUTION_REQUEST / R16_EDITION_LOCAL_ONLY / STOP_AT_SOL_R16_REVIEW`
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Existing branch ONLY: `weekly/2026-W40-v2-work`  
Outer exact Starting HEAD/Tree: supplied by Sol after this instruction is committed.  
Reviewed main SHA: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Governing Sol independent-r15 audit adoption: `sources/2026-W40/execution/reviews/sol-w40-r15-independent-audit-disposition-20261010.md`.  
Independent verdict: `BOUNDED_REVISION_REQUIRED` with findings `R15-A01`–`A05`.

## 0. Strict identity, authority and no-change guards

Before any repository write read-only verify:
- remote W40 existing-branch HEAD/Tree == outer exact Starting HEAD/Tree (no branch creation);
- remote main == `afdb3df3faa20af3bb5798be429bba8dbd2100b1`;
- Production State `EVIDENCE_REVIEWED`, next `stage:selection`, Selection and Architecture machine checkpoints pending; Human Architecture and Publication Preview Gates pending and provenance null; exception gate inactive;
- existing accepted Discovery37 / Screening37 / Evidence Cards35 / Views35 / Materiality37 / Completeness and SHA-bound checkpoints unchanged;
- selection-preview-r13 SHA256 `dc0247781b0401e62eb8b17980050769b743f2aa313ffda3f5b5704235db0cb1`, candidate-matrix-r10 SHA256 `f07b1166eef02598a1d57ebd7d0068119678fcfc17f1d118ef2b582594a736f6`, coverage-r14 SHA256 `3de8bd56f71996e6c6ff075157967507a03650de3fd10c15b31e72faebc671cc`, and boundaries-r15 SHA256 `1736737e9488e3a6e2a94471bfc506fdc43c9f18d5321bbc31b25bb99eb749c7` **all match their actual bytes**.

If a guard fails: ZERO WRITES; report exact expected/actual and STOP. No new/fallback/review branches, no reset/rebase/force. Only normal commits, non-force push on the already-existing W40 branch, with remote readback.

DO NOT edit `.github/`, `config/`, `schemas/`, `scripts/`, Shared Core/docs, `main`, other Editions, accepted upstream, Selection/Matrix/Coverage/Boundary r15/validation r15, any previous review/handoff file, `production-state.json`, checkpoints, Issue #562 or Human Gates. All production/authority artifacts stay unchanged. No formal Selection Acceptance, Stage transition, canonical Architecture, Human Gate, Freeze or Release. No public supplement.

**Minimal-scope philosophy:** A01–A05 only. Do not re-run Discovery/Evidence/Materiality or regenerate the 113-Boundary source structure. Retain r15 P6a/P6b technical drafts as reviewed historical artifacts; no broad research restart.

## 1. A01/A05 — exact correction of package counts and dedup description

Inputs (unchanged):
- `execution/selection/selection-preview-r13.json`
- `execution/selection/candidate-matrix-r10-staging.json`
- `execution/architecture-coverage-r14.json`
- `execution/architecture-boundaries-r15.json`
- `execution/architecture-boundaries-validation-r15.json`
- `execution/architecture-staged-outline-r15.md`
- `execution/SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_HANDOFF.md`

From actual bytes rebuild an r16 **documentation-only** package count table. Required:

| Package | raw | unique | dedup |
|---|---:|---:|---:|
| P1 | 14 | 12 | 2 |
| P2 | 8 | 8 | 0 |
| P3 | 13 | 13 | 0 |
| P4 | 10 | 8 | 2 |
| P5 | 18 | 17 | 1 |
| P6a | 10 | 10 | 0 |
| P6b | 15 | 15 | 0 |
| P7 | 19 | 16 | 3 |
| P8 | 6 | 6 | 0 |
| TOTAL | 113 | 105 | 8 |

Correct r15 Outline's wrong raw values (P1 12→14, P4 11→10, P5 19→18, P7 16→19) as **new** `execution/architecture-staged-outline-r16.md` successor. Preserve every prior correct Candidate ID, usage, Role and editorial destination. New outline must bind the exact r15 Boundary JSON by SHA and must not duplicate or edit literal strings. Explicitly correct dedup internal breakdown P1−2/P4−2/P5−1/P7−3. Do not imply that r15 Boundary source JSON was defective.

## 2. A02 — candidate-level Boundary distribution correction

Independently compute from SELECTED Matrix rows, counting `len(remaining_boundaries)` per candidate. Correct r15 handoff distribution to:

- one selected candidate × 7 Boundaries;
- nine candidates × 5;
- seven candidates × 4;
- eleven candidates × 3;
- weighted sum `1*7+9*5+7*4+11*3=113`, candidate sum `1+9+7+11=28`.

Do not retain obsolete `9×5 + 17×4 + 9×3` or blame the r15 source JSON. Show both counts and independent computation in r16 Handoff addendum. Keep former r15 Handoff intact, marked superseded for affected explanations only.

## 3. A03 — independently executed, machine-readable verification addendum

Create `execution/architecture-boundaries-validation-addendum-r16.json`, **not a replacement for r15 validation**, with exact input paths+SHA256, algorithm/method, recomputed 28/28/20P/8S, raw113/unique105, per-package correct table and:
- `unexpected_package_boundary_strings_count:0`; enumerate any extras on mismatch;
- `missing_literal_memberships_count:0`; enumerate candidate + package + verbatim missing string on mismatch;
- `package_boundary_array_duplicates_count:0`;
- `candidate_boundary_arrays_exact_match:true` (strict ordered-string equality with Matrix, no normalization);
- `package_primary_supporting_membership_exact_match:true` (Selection + Coverage);
- `deterministic_aggregation_roundtrip_idempotent:true`, computed by **re-deriving each package sorted/dedup exact strings twice from immutable Matrix and mapping and comparing both reconstructed results byte-for-byte to the stored r15 arrays**. If stored r15 ordering is not the same deterministic algorithm, explicitly distinguish `semantic_set_equal` from `byte_identical`; do not force a false PASS or modify r15 arrays to satisfy ordering. Record hash/digests for the actual computation and state the sorted/identity comparison semantics.
- independently re-run and report the actual unchanged Core **Boundary membership rule equivalent**, not claim full formal Architecture passed; if a temporary in-memory PROPOSED validator is feasible, label it as only that.
- `status:PASS` ONLY when truly recomputed checks pass, otherwise `FAIL` with mismatch details, STOP at Sol.

Avoid merely copying r15 validation's self-asserted PASS. Include actual runnable script or clearly specified reproducible pseudocode/method as r16 W40-local documentation, without editing `scripts/`. No need to create a new Core validator feature.

## 4. A04 — ContextLM Eq.5 precise, bounded primary-source supplement

Create `execution/technical-prep-r16/contextlm-eq5-primary-note.md` as **focused noncanonical note**. Do not rewrite all r15 P6a/P6b.

- Read primary `https://arxiv.org/html/2609.37725v1` or same pinned v1 authoritative HTML (`ar5iv`) at §4.2; identify Eq.5 by text surrounding its actual equation number (not nearby Eq.6 or a generic skill-evolution formula).
- Transcribe actual Eq.5 symbols, optimization target, and variable definitions exactly; explain in natural Japanese what is optimized and where development/training and held-out test data enter. Explicitly distinguish **skill evolution (in-context learning)** vs subsequent **RL parameter training** described around Eq.6.
- Cite version, section, equation anchor and direct source URL; cite evidence for development/training/test split. Do not invent a split that the paper does not state. When terms `training / development / test` are not identical across an optimization loop, keep paper's own names and describe the actual assignment.
- Verify the relationship to r15 Eq.4 and Eq.6; no change to independently accepted r15 Eq.6 interpretation or other metrics. Mark only still-not-retrieved sections `UNVERIFIED`; if exact source Eq.5 cannot be retrieved, DO NOT fabricate; state explicit retrieval failure with `A04_PARTIAL`.
- Small patch to reader-oriented explanatory prose, not a massive redevelopment. This note is NOT a formal Architecture section.

## 5. Accurate r16 Handoff, integrity and stop

Create `execution/SOL_W40_R16_BOUNDED_DOCUMENTATION_REVIEW_HANDOFF.md` and session log `execution/sessions/muse-w40-r16-20261010.md` (actual execution date if different), append only `execution/index.md` navigation. Report findings A01–A05 one-by-one with status `CORRECTED / PARTIAL / STILL_OPEN`, exact file/anchor, and provenance of independently executed checks.

W40-local paths should be only new r16 successor outline, r16 validation addendum, focused Eq.5 note, Handoff, session log, and appended index (plus a tightly scoped algorithm note if needed). No other modifications without explicit approval.

Final read-only checks: work branch HEAD/Tree; compare to initial head with FF ancestry and allowed changed paths; reviewed main SHA; State blob identical; Source Matrix, Selection, Coverage r14, Boundaries r15 byte-identical; Human Gates and checkpoints unchanged; #562 still separately OPEN as of last check, do not edit it.

Terminal: `SOL_W40_R16_BOUNDED_DOCUMENTATION_REVIEW_REQUIRED`. Stop and report Final HEAD/Tree, changed files, A01–A05 dispositions, counts and whether Eq.5 independently verified. **NO SELECTION ACCEPTANCE, STAGE TRANSITION, CANONICAL ARCHITECTURE, HUMAN GATES OR PUBLICATION.**
