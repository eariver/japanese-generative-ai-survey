# Defect CV2-W42-001 — prepare_evidence_package rejects all bridge-advanced states (shared-Core, frozen)

Date: 2026-10-17 JST. Session: muse r7. Severity: BLOCKING (Unit B).

## Observation
`survey_evidence_v2.prepare_evidence_package` calls `core.verify_state_basis`, which runs `core.validate_state_semantics`. On W42 `CANDIDATES_NORMALIZED` state it fails with: checkpoint discovery/screening authority path-not-canonical + history[1]/[2] implementation SHA divergence.

## Reproduction boundary
- Same failure occurs on W41 `RELEASED` main state (11 checkpoint-path + 10 history-SHA errors) → NOT edition-local; affects every agent-first/bridge-advanced state by construction:
  1. Bridge writes checkpoint provenance to `orchestration/v2/checkpoints/` while core semantics demands `orchestration/v2/attestations/` (config has both dirs distinct).
  2. Bridge appends history rows with per-advance commit SHAs while core semantics demands every row equal the pinned init SHA.
- Operative validator `validate_agent_state` passes clean on W42 state → state itself is healthy; only the strict-core helper path is unusable.

## Impact
Canonical Evidence package/task generation via Core is unreachable in production; role previously filled by edition-local task execution (r4/r5/r6, unaccepted).

## Safe edition-local workaround
None without waiver: bypassing verify (pinned-SHA override still fails on semantics) or hand-rolling package bytes would fabricate Core authority. PROVEN stop; accepted stages preserved.

## Core-maintenance pointer (separate track, NOT production)
Candidate fix: `prepare_evidence_package` (and any stage helper) should validate via `verify_agent_state_basis` (operative agent validator) instead of `core.verify_state_basis`, mirroring the bridge's own checks. Shared roots read-only in production — recorded here, repaired separately.

## Production disposition
Unit B acceptance blocked (this defect + EVIDENCE-CARD-TYPE defect below); Unit A repairs + provisional sketch committed; dossier r7 records exact errors.
