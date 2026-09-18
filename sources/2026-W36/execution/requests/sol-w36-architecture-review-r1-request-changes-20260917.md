# W36 execution instruction — Architecture Review r1 REQUEST_CHANGES, bounded Architecture regeneration

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_REVIEW_R1_REQUEST_CHANGES / BOUNDED_TO_SELECTION_COMPLETE`

Date: `2026-09-17 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W36-v2-work`

## 1. Human decision authority (imported)

Human/Sol review authority supplied by execution request. Muse did not independently produce this review.

Human Architecture Review r1 decision:

`REQUEST_CHANGES`

Reviewed production authority:

`0295bd08c6b46a5b1be3a10051970d9e749cc73b` (tree `c5111e91509d6b68a28be2b7520ab54acee43bdd`)

Presentation shell that exposed the pending Human gate:

`d30949b0ba9d892505d9f2c5100da57171e273f1`

Regeneration boundary:

`SELECTION_COMPLETE`

Independent review findings supplied by this instruction:

- Research sufficiency: PASS
- Evidence authority/consumption: PASS
- Materiality/Selection: PASS
- Package architecture: PASS except RC-1
- Shared-Core discipline: PASS
- Blocking finding: RC-1
- Provenance correction: RC-2
- Decision: `REQUEST_CHANGES`

## 2. RC-1 — NVIDIA/Hugging Face acquisition boundary (BLOCKING_ARCHITECTURE_EVIDENCE_BOUNDARY)

The r1 editorial thesis wording equivalent to `NVIDIA moved to own the open platform it pledges to keep neutral` exceeds consumed authority (agreement != completed ownership). Rewrite thesis and dependent surfaces with transaction-status-safe language, e.g. `NVIDIA agreed to acquire Hugging Face while pledging to preserve its open, compute-agnostic character`. Preserve package-level boundary `Deal announced, not closed`. Do not promote the openness pledge to observed fact. Remove stale `moved to own` / `owns Hugging Face` / `NVIDIA-owned` language.

## 3. RC-2 — review provenance / Sol attribution (REVIEW_PROVENANCE_CORRECTION)

The worker-generated `execution/decisions/sol-w36-supervisory-reviews-20260917-r1.md` is a worker pre-gate review/check, not independent Sol authority. Preserve it as historical evidence; classify it accordingly; do not cite it as independent Sol review in r2. Record this r1 REQUEST_CHANGES through proper Human Gate provenance. Never write a new file claiming independent Sol/Human review unless supplied by contract.

## 4. Boundary

`SELECTION_COMPLETE`. Upstream frozen: Grok/X, Raws, Discovery (19), Screening (19 KEEP / 0 DROP), Evidence (13 VERIFIED / 6 PARTIAL), views, Materiality (18 MATERIAL / 1 CONTEXT), Completeness, Selection (18 SELECTED / 1 HOLD). No new research. No candidate/disposition/status change.

## 5. Expected end

Fresh r2 Human Architecture Review PENDING at `ARCHITECTURE_ESTABLISHED`. No Draft. No r2 decision inferred.
