# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`

## 1. Purpose

This file is the persistent work-status ledger for the Survey Production Core v2 improvement program.

It exists so that progress can be reconstructed from repository state alone, without depending on chat history. Every substantive work session or work unit on `refactor/survey-production-core-v2` must read this file before making changes and update it before the work unit is considered complete.

This log records the state of the **compilation-system improvement effort**. Edition-specific W33 / W34 / SP001 / SP002 / SP003 production state belongs in each edition's own canonical production artifacts and must not be duplicated here. Findings returned from those production sessions are recorded here only when they are being evaluated as Core / Profile / contract / regression work.

---

## 2. Update contract

For every substantive work unit:

1. read current `main` when the work can be affected by repository changes since the previous unit;
2. read `docs/survey-production-core-v2-improvement-plan.md` and this work log;
3. record the work unit as `IN_PROGRESS` before or at the beginning of implementation when practical;
4. perform the work and validation;
5. update the current snapshot and work-unit record before stopping;
6. record concrete changed files, validation performed, unresolved findings, and the exact next action;
7. do not mark a work unit `COMPLETE` merely because code was written — required inspection/tests for that unit must also be complete;
8. if work stops because a decision or blocker is unresolved, record `BLOCKED` or `PAUSED`, the reason, and the resume condition;
9. if current `main` moved materially, record the revalidation result rather than silently assuming the original branch base remains authoritative.

The log should remain concise enough to serve as a checkpoint. Detailed design reasoning belongs in dedicated docs, Issues, tests, or code comments; this file points to those artifacts.

### Work-unit status values

- `PLANNED` — identified but not started;
- `IN_PROGRESS` — actively being worked;
- `PAUSED` — intentionally stopped with a known resume point;
- `BLOCKED` — cannot proceed without resolving a concrete blocker or decision;
- `COMPLETE` — intended scope and validation for the unit are complete;
- `SUPERSEDED` — replaced by a later work unit or design decision.

---

## 3. Current snapshot

Last updated: **2026-08-22 JST**

### Repository / branch

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Branch originally derived from `main` commit: `2086b396d2f30103d9292b722891be436cd28db5`
- Improvement-plan commit: `9839bbe002dc49470a66156e23a28aba6489d921`
- Production source of truth remains: current `main` after coherent candidate changes are reviewed and merged.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 0 — Cross-Pipeline Process Archaeology**
- Current phase status: `PLANNED`
- Current active work unit: none
- Next work unit: **WU-001 — inventory current Weekly / Special / shared production components and classify ownership / disposition**

### Pilot validation state

- W33 — future `Weekly Profile First Production Validation`; production is intentionally outside this branch/session. Existing legacy W33 work is comparison material, not a migration acceptance requirement.
- SP001 — future `Thematic Profile First Production Validation`; production is intentionally outside this branch/session.
- W34 — second Weekly validation after W33 findings are evaluated and incorporated.
- SP002 / SP003 — later Thematic generalization validation after SP001 findings are evaluated and incorporated.

### Important unresolved design questions carried into Phase 0/1

- exact shared Core/Profile boundary for existing Weekly and Special schemas/scripts/workflows;
- whether Weekly should adopt the same normal two-Human-Gate interaction model as Special;
- exact generalized temporal-policy schema for Thematic and Period research;
- shape and storage location of the Materiality Ledger / completeness contract;
- canonical shared Evidence corpus vs edition-specific Evidence View representation;
- Series Research Layer representation for Foundations-style multi-volume work;
- legacy repair scripts that must remain for replay/audit vs those that can leave the future hot path;
- exact contract-drift resolution for older Weekly revisioned Release documentation vs current issue-only Release identity.

---

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `PLANNED` | component inventory + ownership/disposition map |
| 1 | Contract Normalization | `PLANNED` | authoritative Core/Profile/Publication/Series contract map |
| 2 | Historical Knowledge Distillation | `PLANNED` | repair lineage + invariants + regression candidates |
| 3 | Core v2 Candidate Design / Minimum Vertical Slice | `PLANNED` | W33/SP001-capable candidate merged-ready |
| 4 | First external production validation | `PLANNED` | W33 + SP001 production findings |
| 5 | Cross-Pilot evaluation / first consolidation | `PLANNED` | classified fixes + regressions + revised contract |
| 6 | Second production validation | `PLANNED` | W34 + SP002 + SP003 findings |
| 7 | Stabilization / consolidation | `PLANNED` | stable Core/Profile contracts and simplified production path |

---

## 5. Work-unit index

| Work unit | Scope | Status | Primary artifacts |
|---|---|---|---|
| WU-000 | Establish improvement direction, branch, plan, and persistent checkpoint mechanism | `COMPLETE` | `docs/survey-production-core-v2-improvement-plan.md`, this file |
| WU-001 | Phase 0 component inventory and classification | `PLANNED` | TBD |

Add new work units here before or when they begin. Do not reuse an identifier after completion.

---

## 6. Work-unit records

### WU-000 — Establish program direction and checkpoint mechanism

Status: `COMPLETE`

#### Scope

- revalidate the proposed Survey Production Core v2 direction against current `main`;
- create an improvement branch from current `main`;
- write the implementation/validation plan;
- define W33/SP001 as external first-production validation rather than edition work performed in this improvement context;
- explicitly reject legacy W33 state migration as a primary v2 acceptance requirement;
- establish this repository-backed work log before Phase 0 implementation begins.

#### Result

The direction was accepted with these constraints:

- shared `Survey Production Core v2` is a convergence of Weekly and Special knowledge, not one pipeline consuming the other;
- common mechanisms live in Core, while research/completeness semantics remain profile-specific;
- Research / Editorial Profile is separated from Publication Profile where practical;
- Thematic scope must not be forced into a bounded-period temporal model;
- reusable source facts must be separated from edition-specific historical/editorial interpretation;
- Foundations-style multi-volume work requires an outer Series Research Layer;
- current `main` remains production source of truth;
- W33 legacy artifacts are optional comparison material, not mandatory migration inputs;
- W33 and SP001 are compiled in separate production sessions and their findings are returned to this improvement effort;
- W34 and SP002/SP003 validate the repaired/generalized flow after first-pilot evaluation.

#### Artifacts

- `docs/survey-production-core-v2-improvement-plan.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`

#### Validation / repository evidence inspected

- current `main` and `AGENTS.md`;
- Weekly pipeline design / implementation status / planner;
- Special pipeline config / planner / two-Human-Gate contract;
- issue-only public Release identity vs older Weekly Release documentation;
- Thematic Special backlog;
- Foundations series design;
- Issue #166 materiality / silent-drop defect;
- Issue #191 subject/entity-binding correctness defect;
- existing `weekly/2026-W33-work` state and divergence from current `main`.

#### Next action

Begin **WU-001** from current `main`: inventory Weekly, Special, and genuinely shared docs/config/schemas/scripts/workflows/tests; classify each relevant component by both ownership (`CORE`, `WEEKLY_PROFILE`, `PERIOD_PROFILE`, `THEMATIC_PROFILE`, `PUBLICATION_PROFILE`, `SERIES_LAYER`, `LEGACY_REPLAY`) and disposition (`RETAIN`, `GENERALIZE`, `MERGE`, `REMOVE/ARCHIVE`, `ADD`).

---

## 7. Finding handoff template

When W33, SP001, W34, SP002, SP003, or another production session returns a pipeline finding, record or link it using at least the following fields before classification is considered complete:

```yaml
finding_id:
edition:
stage:
observed_problem:
expected_behavior:
actual_behavior:
production_workaround:

classification:
  scope: UNCLASSIFIED # EDITION_LOCAL / PROFILE_DEFECT / CORE_DEFECT / CONTRACT_DEFECT / REGRESSION_REQUIRED / SERIES_LAYER
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

---

## 8. Resume rule

A future session continuing this improvement work should begin by:

1. reading current `main` and identifying whether it materially changed since the last recorded checkpoint;
2. reading `docs/survey-production-core-v2-improvement-plan.md`;
3. reading this file;
4. locating the first `IN_PROGRESS`, `PAUSED`, or next `PLANNED` work unit;
5. verifying the stated next action against repository reality;
6. continuing from repository-recorded state rather than reconstructing progress from previous chat messages.

If this file and repository reality disagree, repository reality wins and this log must be corrected before further design assumptions are built on it.
