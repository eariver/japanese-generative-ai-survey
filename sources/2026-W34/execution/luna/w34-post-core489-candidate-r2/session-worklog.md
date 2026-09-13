# W34 post-Core-#489 candidate run r2 — Luna/Work execution worklog

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
Date: 2026-09-13 JST
Starting W34: `39ced1de...` (reviewed Core #489 integrated: parents `f50d2291...` + `658ae823...`)

## Authority

- Reviewed main `14781409...` (PR #489 merge; parents `005e5984...` + `f3203f4e...`) integrated via normal merge, no conflicts (W34 production paths untouched by merge).
- Phase-B inspection: VALIDATED_DRAFT / stage:publication-candidate, arch approved, preview pending, DRAFT_COMPLETE.json immutable, publication bytes = post-#488 regenerated (bib `1d3fecf3...`, tex `2c41cc6f...`, pdf `f7403b0a...` 12 pages), expected 5-drift defect shape confirmed.

## Phase C — sanctioned revalidation

- `revalidate-publication-surface --reason-class REVIEWED_CORE_CHANGE` (post-#489 authority revalidation for the existing regenerated surface).
- Established `publication/v2/publication-surface-revalidation-r1.json` + State-bound `publication_revalidation_provenance` (pointer-only state change).
- Postconditions verified: DRAFT_COMPLETE/approval/evidence/selection/architecture/draft/prose unchanged; gates unchanged; preview pending; state validation PASS; record ACTIVE.

## Phase D — candidate validation

- Existing candidate `dbd4c783...` (`READY_FOR_PUBLICATION_PREVIEW`) validates as-is against the revalidated surface (manuscript `4fb0830b...`, PDF `f7403b0a...` 12p, bundle/semantic/visual SHAs match). No rebuild performed.
- Canonical stage validation `VALIDATED_DRAFT -> RELEASE_CANDIDATE`: PASS (`publication-candidate-stage-validation-r2.json`).

## Phase E — advance

- `advance-stage` with the fresh CORE_STAGE_CONTRACT review → checkpoint `orchestration/v2/checkpoints/VALIDATED_DRAFT.json`.
- Final: `RELEASE_CANDIDATE`, `next_action PUBLICATION_PREVIEW`, `terminal_reason HUMAN_GATE_REACHED`, preview pending with no provenance, revalidation still ACTIVE, final state PASS.

## Sidecar A Sol disposition (carried)

`SOL_SEMANTIC_PASS / KNOWN_VALIDATOR_LANGUAGE_COVERAGE_FALSE_POSITIVE` for the section-20 framing residual; prose untouched. No new Sidecar A run (reader bytes verified identical to the rerun surface).

## Markers

`W34_POST_CORE489_CANDIDATE_R2_COMPLETE`, `PUBLICATION_PREVIEW_HUMAN_DECISION_NOT_GENERATED`.
Terminal: `W34_READY_FOR_PUBLICATION_PREVIEW_HUMAN_REVIEW`.
