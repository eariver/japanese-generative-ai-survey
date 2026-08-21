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
- Current `main` revalidated before WU-001 inventory commit: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged from branch base.
- Improvement-plan commit: `9839bbe002dc49470a66156e23a28aba6489d921`
- Phase 0 inventory commit: `a407606d704e7438eed32c0a0441a5cad74bcf2d`
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 1 — Contract Normalization**
- Current phase status: `IN_PROGRESS`
- Current active work unit: **WU-002 — contract authority and drift normalization map**
- Next work unit: to be assigned from WU-002 exit findings.

### Pilot validation state

- W33 — future Weekly Profile first-production validation; legacy W33 work remains comparison material, not a migration acceptance requirement.
- SP001 — future Thematic Profile first-production validation.
- W34 — second Weekly validation after W33 findings are evaluated and incorporated.
- SP002 / SP003 — Thematic generalization validation after SP001 findings are evaluated and incorporated.

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `COMPLETE` | `docs/survey-production-core-v2-component-inventory.md` |
| 1 | Contract Normalization | `IN_PROGRESS` | authoritative Core/Profile/Publication/Series contract map |
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
| WU-001 | Phase 0 component inventory and classification | `COMPLETE` | `docs/survey-production-core-v2-component-inventory.md` |
| WU-002 | Phase 1 contract authority / drift normalization map | `IN_PROGRESS` | planned: `docs/survey-production-core-v2-contract-normalization.md` |

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

Status: `COMPLETE`

Started / completed: **2026-08-22 JST**

Result:

- inventoried current Weekly, Special, and shared production families across docs/config/schemas/scripts/workflows/tests/publication/release surfaces;
- classified ownership as `CORE`, `WEEKLY_PROFILE`, `PERIOD_PROFILE`, `THEMATIC_PROFILE`, `PUBLICATION_PROFILE`, `SERIES_LAYER`, or `LEGACY_REPLAY`;
- classified disposition as `RETAIN`, `GENERALIZE`, `MERGE`, `REMOVE/ARCHIVE`, or `ADD`;
- confirmed that most Screening/Evidence/Draft semantic schemas and primitives are already shared and should be promoted rather than rebuilt;
- identified state/Human Gate/orchestration/publication boundaries as the principal duplication/drift area;
- confirmed Period consistency is Profile behavior despite historical `core` naming;
- classified long Special repair chains as eventual `LEGACY_REPLAY` hot-path removal candidates while preserving their learned invariants/tests;
- listed missing v2 components including Materiality Ledger, profile-defined completeness, temporal policy abstraction, advance-to-gate, entity binding guard, review finding/repair set, reusable Evidence corpus, and Series layer state.

Validation:

- current `main` remained `2086b396...` during the inventory;
- representative generic/shared and Weekly/Special wrapper implementations were inspected directly;
- representative state schemas, finalizers, workflows, period guards, publication checks, and repair-chain dependencies/tests were inspected;
- branch compare after inventory contained only the improvement plan, worklog, and component inventory; no production code was modified in WU-001.

Artifact:

- `docs/survey-production-core-v2-component-inventory.md`
- commit: `a407606d704e7438eed32c0a0441a5cad74bcf2d`

Phase 0 exit condition: **satisfied**.

### WU-002 — Phase 1 contract authority and drift normalization map

Status: `IN_PROGRESS`

Started: **2026-08-22 JST**

Scope:

- identify current authoritative and conflicting contracts for Human Gates, release identity, state/lifecycle, temporal scope, completeness/materiality, publication/Visual QA, and production bootstrap;
- define the candidate canonical contract hierarchy for Core, Weekly Profile, Period Profile, Thematic Profile, Publication Profile, and Series Layer;
- explicitly decide which current rules are retained, superseded, generalized, or left as legacy compatibility;
- define contract provenance fields required in future artifacts (`quality_contract_version`, `pipeline_contract_sha` or equivalent);
- avoid implementation changes until authority/drift decisions are explicit enough to prevent refactoring against stale documentation.

Primary planned artifact:

- `docs/survey-production-core-v2-contract-normalization.md`

Initial drift set carried from Phase 0:

1. Weekly legacy Selection/Freeze Human Gates vs Special Architecture Review/Publication Preview.
2. Issue-only public release policy vs older revisioned release workflows/docs.
3. shared lifecycle/machine gates vs separate Weekly/Special state schemas.
4. bounded Special coverage contract incorrectly constraining Thematic research.
5. collector/stage completion vs profile-specific completeness + materiality traceability.
6. internal Candidate Selection approval metadata vs user-interaction gate semantics.
7. shared vs profile-specific Architecture role vocabulary.
8. shared synthesis contract vs profile-specific synthesis requirements.
9. common publication integrity vs Weekly/long-form layout policy.
10. Visual Review checkpoint name vs Human Gate semantics.
11. Freeze/Release authority after exact Publication Preview approval vs older standalone approvals.
12. Special-only bootstrap vs future generic profile bootstrap.
13. missing cross-artifact contract identity.

Exit condition:

- a new implementation can identify one authoritative owner for each major production rule and can distinguish current canonical rules from legacy compatibility without consulting chat history.

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
