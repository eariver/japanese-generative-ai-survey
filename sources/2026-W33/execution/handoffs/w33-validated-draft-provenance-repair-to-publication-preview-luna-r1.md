# 2026-W33 validated-draft provenance repair through Publication Preview — Luna handoff r1

## Purpose

Perform one exact mechanical repair to the already Sol-accepted layout-polished validation candidate, then use canonical Core to advance through `VALIDATED_DRAFT` and materialize the Publication Candidate, stopping at the `PUBLICATION_PREVIEW` Human Gate.

Normal completion status:

`PUBLICATION_PREVIEW_GATE_READY_FOR_OWNER_REVIEW`

## Repository authority

Repository:

`eariver/japanese-generative-ai-survey`

Branch:

`weekly/2026-W33-v2-work`

The caller provides the Exact Starting SHA. Before any write, verify remote branch HEAD exactly equals that SHA. If not, write nothing and stop with the actual remote HEAD.

Reviewed-main Core authority:

`6267de3f6876f491950139757bfdf1085fc07bdc`

Shared Core/config/schema/workflow authority is read-only.

## Mandatory read order

1. reviewed-main `config/survey-production-v2.json`
2. reviewed-main `scripts/survey_stage_validation_v2.py`
3. reviewed-main `scripts/survey_reader_publication_v2.py`
4. reviewed-main `scripts/survey_publication_v2.py`
5. reviewed-main `schemas/reader-manuscript-v2.schema.json`
6. reviewed-main `schemas/publication-review-record-v2.schema.json`
7. reviewed-main `schemas/quality-regression-bundle-v2.schema.json`
8. reviewed-main `schemas/publication-candidate-v2.schema.json`
9. current `sources/2026-W33/production-state.json`
10. current Draft checkpoint referenced by State
11. `sources/2026-W33/publication/v2/reader-manuscript-v2.json`
12. `surveys/weekly/2026-W33/main.tex`
13. `surveys/weekly/2026-W33/main.pdf`
14. `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json`
15. `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json`
16. `sources/2026-W33/publication/v2/visual-review-v2.json`
17. `sources/2026-W33/execution/sessions/w33-luna-reader-layout-polish-20260831-r1.md`
18. `sources/2026-W33/execution/reviews/w33-validated-draft-layout-polish-sol-review-20260831-r2.md`

## Required starting state

Verify before write:

- lifecycle `DRAFT_COMPLETE`
- `next_action = stage:reader-publication-validation`
- draft checkpoint `passed`
- validation checkpoint `pending`
- publication preview `pending`
- Architecture Review `approved`
- Exception Gate inactive
- reader source SHA-256 `b9f9dfa1e2639cedf66bf85b7ed5102c733c51ef5076882c78b5867c5b2e38f4`
- exact PDF SHA-256 `4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`
- PDF page count 11
- Quality Bundle SHA-256 `2e0cd1de4a61355c6f3e2d33eb47e8008346b27e994120546ebd38b6f785b9ca`
- Semantic Review SHA-256 `7685ee4b658ff5135ebea17e8f02a01a7c4e67756adad7ddd12753805c640b0c`
- Reader Manifest SHA-256 `516a6f3d1dfbb9d7a413914c27358f05d8fe447c438693dfe8cf7a374a411b59`

If any authority differs, stop `NEEDS_SOL_REVIEW` without repair or advancement.

## Phase 1 — exact visual-review provenance repair

Current `sources/2026-W33/publication/v2/visual-review-v2.json` has a Sol-identified stale human-readable provenance defect only.

Do not change the top-level reader-manuscript/source/PDF bindings or visual conclusions.

Perform these exact replacements wherever they occur in the visual review evidence locations:

1. `4f1028c221101cd21cf300a3916c9d4b7cf589b5f672a0f97f61aa6afc992243`
   -> `4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`

2. workflow run `33398104252`
   -> `33403175661`

3. artifact `9760255099`
   -> `9762175041`

4. repository PDF blob `9c0de61f6469e2f40ca81c293a541f4669f95bbc`
   -> `c17f1b77434351e49793b11f2ce82815ecb5693e`

Recompute `review_sha256` exactly according to current Core/schema semantics.

If any additional stale pre-polish identifier appears in the visual review, or if any other semantic change appears necessary, stop `NEEDS_SOL_REVIEW` rather than broadening repair.

After repair:

- schema-validate the visual review;
- current Core review validator must PASS;
- confirm source/PDF/Reader Manifest bindings remain unchanged;
- confirm all 11-page review conclusions remain unchanged;
- rerun the complete `DRAFT_COMPLETE` stage contract using the current reader-manuscript, source, exact PDF, Quality Bundle, semantic review, and repaired visual review.

The stage contract must PASS before any transition.

Do not rebuild the PDF and do not modify TeX/source/PDF unless a validator proves bytes have drifted. Byte drift is a stop condition, not repair permission.

## Phase 2 — deterministic validation advancement

Only after Phase 1 PASS, create one canonical trusted-operator `ADVANCE_STAGE` request from `DRAFT_COMPLETE` using exactly:

- reader-manuscript: `sources/2026-W33/publication/v2/reader-manuscript-v2.json`
- validated-source: `surveys/weekly/2026-W33/main.tex`
- publication-pdf: `surveys/weekly/2026-W33/main.pdf`
- quality-regression-bundle: `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json`
- semantic-review: `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json`
- repaired visual-review: `sources/2026-W33/publication/v2/visual-review-v2.json`

Bind the Sol review:

`sources/2026-W33/execution/reviews/w33-validated-draft-layout-polish-sol-review-20260831-r2.md`

Require Preflight PASS and Execute PASS.

Expected transition exactly once:

`DRAFT_COMPLETE -> VALIDATED_DRAFT`

Expected checkpoint:

- validation = `passed`
- other accepted checkpoint authority preserved

After transition, read back State and exact checkpoint provenance. If anything diverges, stop `NEEDS_SOL_REVIEW`.

## Phase 3 — deterministic Publication Candidate

Only from a successfully materialized `VALIDATED_DRAFT` state:

Use reviewed-main `scripts/survey_publication_v2.py` canonical helpers to build and validate exactly one:

`sources/2026-W33/publication/v2/publication-candidate-v2.json`

The candidate must be constructed only from the exact already-reviewed authorities:

- Reader Manuscript
- validated source `main.tex`
- exact repository PDF
- page count 11
- Quality Regression Bundle
- Semantic / Editorial Review
- repaired Exact-PDF Visual Review

Required candidate status:

`READY_FOR_PUBLICATION_PREVIEW`

No new prose, review conclusion, evidence, source, or PDF may be introduced at this phase.

Then create one canonical trusted-operator `ADVANCE_STAGE` request from `VALIDATED_DRAFT` using only that publication candidate.

Require Preflight PASS and Execute PASS.

Expected transition exactly once:

`VALIDATED_DRAFT -> RELEASE_CANDIDATE`

At `RELEASE_CANDIDATE`, canonical State must reach Human Gate:

- `next_action = PUBLICATION_PREVIEW`
- `terminal_reason = HUMAN_GATE_REACHED`
- `human_gates.publication_preview = pending`
- publication preview approval provenance remains null

## Human Gate ownership

STOP at Publication Preview.

Do NOT:

- approve or reject Publication Preview;
- create `publication-preview-approval-v2.json`;
- create a Human Gate decision on behalf of Owner;
- freeze;
- release;
- merge;
- alter reader prose/source/PDF;
- change Evidence/Selection/Architecture/Draft content;
- use Web, Google Drive, Raw source, or fresh research.

## Write allowlist

Only write paths required for:

1. repaired `sources/2026-W33/publication/v2/visual-review-v2.json`;
2. any hash-bound record that current canonical helper necessarily regenerates solely because visual-review bytes changed;
3. validation ADVANCE_STAGE request/bridge/checkpoint/Production State outputs;
4. `sources/2026-W33/publication/v2/publication-candidate-v2.json`;
5. publication-candidate ADVANCE_STAGE request/bridge/Production State outputs;
6. one Luna session record for this task.

Do not modify shared Core/config/schema/workflows or reader source/PDF.

## Stop conditions

Stop `NEEDS_SOL_REVIEW` without broader repair if:

- starting HEAD mismatch;
- current State/authority drift;
- repair requires anything beyond the four exact stale provenance replacements plus mechanically dependent hashes;
- exact reader source/PDF bytes drift;
- DRAFT_COMPLETE validation fails;
- a canonical transition preflight or execute fails;
- publication candidate cannot be generated solely from the accepted exact authorities;
- Publication Candidate validator fails;
- Human Gate fields differ from the expected pending state.

## Completion record

Create one session record:

`sources/2026-W33/execution/sessions/w33-luna-publication-preview-gate-20260831-r1.md`

Record at minimum:

- Exact Starting SHA
- Ending SHA
- repaired visual-review SHA-256
- proof of four exact replacements and no semantic change
- validation request/event/bridge IDs and SHAs
- Validation checkpoint SHA-256
- post-validation State SHA-256
- Publication Candidate path/SHA-256/candidate_sha256/PDF SHA/page count
- publication-candidate request/event/bridge IDs and SHAs
- final State SHA-256
- final lifecycle/next_action/terminal_reason
- publication preview = pending / provenance null
- changed path inventory

Normal successful stop:

`PUBLICATION_PREVIEW_GATE_READY_FOR_OWNER_REVIEW`
