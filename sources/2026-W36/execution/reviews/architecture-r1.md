# Human Architecture Review — 2026-W36 r1 (REQUEST_CHANGES recorded)

## Reviewed authority

- Edition: `2026-W36` (WEEKLY + WEEKLY_MAGAZINE), target gate `ARCHITECTURE_REVIEW`
- Reviewed repository commit SHA: `0295bd08c6b46a5b1be3a10051970d9e749cc73b` (tree `c5111e91509d6b68a28be2b7520ab54acee43bdd`; production HEAD under review)
- Lifecycle at review: `ARCHITECTURE_ESTABLISHED`; terminal `HUMAN_GATE_REACHED`; next action `ARCHITECTURE_REVIEW`
- Gate inputs reviewed (r1 bytes):
  - `sources/2026-W36/architecture-v2.json`
  - `sources/2026-W36/architecture-review-summary-v2.json`
  - `sources/2026-W36/architecture-review-attention-v2.json`
- Full r1 dossier: `sources/2026-W36/execution/reviews/architecture-r1-dossier.md`
- Sol supervisory reviews: `sources/2026-W36/execution/decisions/sol-w36-supervisory-reviews-20260917-r1.md` (worker-generated pre-gate check per RC-2 provenance note; not independent Sol authority)
- Machine validation: `sources/2026-W36/execution/validation/architecture-stage-validation-r1.json` (CORE_STAGE_CONTRACT PASS)
- Canonical review record: `sources/2026-W36/gates/reviews/architecture-r1.json` (decision `REQUEST_CHANGES`, boundary `SELECTION_COMPLETE`); index `sources/2026-W36/gates/review-index.json`
- Execution instruction: `sources/2026-W36/execution/requests/sol-w36-architecture-review-r1-request-changes-20260917.md` (Human/Sol review authority supplied by execution request)

## Human decision

`REQUEST_CHANGES` (revision 1).

Recorded via canonical `survey_human_gate_v2.py request-architecture-revision` against the exact reviewed bytes above; reviewed-by `Human Owner`; reviewed-at `2026-09-16T15:51:32Z`; reviewed commit `0295bd08c6b46a5b1be3a10051970d9e749cc73b`.

## Requested changes

- RC-1 (`BLOCKING_ARCHITECTURE_EVIDENCE_BOUNDARY`): r1 thesis wording equivalent to `NVIDIA moved to own the open platform it pledges to keep neutral` exceeds authority (agreement != completed ownership). Corrected to transaction-status-safe language in r2, preserving package boundary `Deal announced, not closed` and pledge-as-pledge semantics.
- RC-2 (`REVIEW_PROVENANCE_CORRECTION`): worker-generated pre-gate review classified as such (see provenance note `execution/decisions/w36-worker-pregate-review-provenance-20260917-r2.md`); r2 dossier does not cite it as independent Sol authority.

## Regeneration boundary

`SELECTION_COMPLETE` (bounded Architecture-only correction; no Discovery/Screening/Evidence/Materiality/Completeness/Selection rerun; dispositions unchanged).

## Shared-Core implication

None. Edition-local Architecture correction; no Core defect discovered; no repair branch or PR; `main` and Production Line untouched and unmerged by design.

## Supersession note

r1 Architecture artifacts were invalidated by the canonical machinery (removed paths recorded in the gate run); r2 was regenerated from the unchanged Selection and is presented separately in `architecture-r2.md`. This r1 record is preserved as immutable review history.
