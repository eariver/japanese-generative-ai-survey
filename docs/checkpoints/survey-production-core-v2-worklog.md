# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`

## 1. Purpose

This file is the persistent work-status ledger for the Survey Production Core v2 improvement program. Progress must be reconstructable from repository state alone. Every substantive work unit must read this file before making changes and update it before the work unit is considered complete.

Edition-specific W33 / W34 / SP001 / SP002 / SP003 production state belongs in each edition's canonical artifacts. Only findings evaluated as Core / Profile / contract / regression work are recorded here.

## 2. Update contract

For every substantive work unit:

1. re-read current `main` when repository changes can affect the work;
2. read the improvement plan and this log;
3. mark the work unit `IN_PROGRESS` before or at the beginning of implementation when practical;
4. perform the work and validation;
5. update the snapshot and work-unit record before stopping;
6. record changed files, validation, unresolved findings, and the exact next action;
7. do not mark a work unit `COMPLETE` until its intended inspection/tests are complete;
8. use `PAUSED` / `BLOCKED` with a concrete resume condition when appropriate;
9. record material movement of `main` rather than assuming the original branch base remains current.

Status values: `PLANNED`, `IN_PROGRESS`, `PAUSED`, `BLOCKED`, `COMPLETE`, `SUPERSEDED`.

## 3. Current snapshot

Last updated: **2026-08-22 JST**

### Repository / branch

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Original base `main`: `2086b396d2f30103d9292b722891be436cd28db5`
- Current `main` revalidated at WU-001 start: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged from branch base.
- Improvement-plan commit: `9839bbe002dc49470a66156e23a28aba6489d921`
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 0 — Cross-Pipeline Process Archaeology**
- Current phase status: `IN_PROGRESS`
- Current active work unit: **WU-001 — component inventory and classification**
- Next work unit: to be assigned after WU-001 exit findings are recorded.

### Pilot validation state

- W33 — future Weekly Profile first-production validation; legacy W33 work remains comparison material, not a migration acceptance requirement.
- SP001 — future Thematic Profile first-production validation.
- W34 — second Weekly validation after W33 findings are evaluated and incorporated.
- SP002 / SP003 — Thematic generalization validation after SP001 findings are evaluated and incorporated.

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `IN_PROGRESS` | component inventory + ownership/disposition map |
| 1 | Contract Normalization | `PLANNED` | authoritative Core/Profile/Publication/Series contract map |
| 2 | Historical Knowledge Distillation | `PLANNED` | repair lineage + invariants + regression candidates |
| 3 | Core v2 Candidate Design / Minimum Vertical Slice | `PLANNED` | W33/SP001-capable candidate merged-ready |
| 4 | First external production validation | `PLANNED` | W33 + SP001 production findings |
| 5 | Cross-Pilot evaluation / first consolidation | `PLANNED` | classified fixes + regressions + revised contract |
| 6 | Second production validation | `PLANNED` | W34 + SP002 + SP003 findings |
| 7 | Stabilization / consolidation | `PLANNED` | stable Core/Profile contracts and simplified production path |

## 5. Work-unit index

| Work unit | Scope | Status | Primary artifacts |
|---|---|---|---|
| WU-000 | Establish direction, branch, plan, and checkpoint mechanism | `COMPLETE` | improvement plan; this log |
| WU-001 | Phase 0 component inventory and classification | `IN_PROGRESS` | planned: `docs/survey-production-core-v2-component-inventory.md` |

## 6. Work-unit records

### WU-000 — Establish program direction and checkpoint mechanism

Status: `COMPLETE`

Result:

- established `Survey Production Core v2 + Profiles + optional Series Research Layer` as the target;
- kept current `main` as production source of truth;
- rejected legacy W33 state migration as a primary acceptance requirement;
- separated improvement/evaluation work from W33/SP001 production sessions;
- defined W33/SP001 as first production validations and W34/SP002/SP003 as post-repair generalization validations.

Artifacts:

- `docs/survey-production-core-v2-improvement-plan.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`

### WU-001 — Phase 0 component inventory and classification

Status: `IN_PROGRESS`

Started: **2026-08-22 JST**

Scope:

- inventory current `main` Weekly, Special, and genuinely shared production components across docs, config, schemas, scripts, workflows, tests, publication/release surfaces, and orchestration controls;
- classify relevant components by ownership: `CORE`, `WEEKLY_PROFILE`, `PERIOD_PROFILE`, `THEMATIC_PROFILE`, `PUBLICATION_PROFILE`, `SERIES_LAYER`, `LEGACY_REPLAY`;
- classify disposition: `RETAIN`, `GENERALIZE`, `MERGE`, `REMOVE/ARCHIVE`, `ADD`;
- identify duplicated mechanisms, stale contracts, hot-path repair chains, missing shared abstractions, and caller/workflow dependencies that constrain later consolidation.

Start validation:

- current `main` is unchanged from the improvement branch base (`2086b396...`);
- current workflow and script directories have begun to be inspected from `main`;
- no edition-production branch is being treated as the v2 source of truth.

Planned primary artifact:

- `docs/survey-production-core-v2-component-inventory.md`

Exit condition:

- the inventory is sufficiently complete to support Phase 1 contract normalization without guessing component ownership;
- major remove/archive candidates have dependency/replay caveats recorded rather than being proposed for deletion solely from filename/version age.

## 7. Finding handoff template

```yaml
finding_id:
edition:
stage:
observed_problem:
expected_behavior:
actual_behavior:
production_workaround:
classification:
  scope: UNCLASSIFIED
  confidence:
provenance:
  source_commit:
  relevant_artifacts: []
  human_review_reference:
improvement_action:
regression_fixture:
status:
```

A production workaround does not automatically become the canonical Core fix.

## 8. Resume rule

A continuation session must: read current `main`; read the improvement plan and this log; locate the active/paused/next planned work unit; verify its stated next action against repository reality; and continue from repository-recorded state. If the log and repository disagree, repository reality wins and this file must be corrected first.
