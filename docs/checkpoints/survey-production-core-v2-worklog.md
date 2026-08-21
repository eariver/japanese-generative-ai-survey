# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`

## 1. Purpose and update contract

This is the persistent work-status ledger for the Survey Production Core v2 improvement program. Progress must be reconstructable from repository state alone. Every substantive work unit reads this file before changes and updates it before the unit is considered complete.

Edition-specific W33 / W34 / SP001 / SP002 / SP003 state stays in each edition's canonical production artifacts. This log records only compilation-system design, implementation, and returned findings evaluated as Core/Profile/Publication/regression work.

Status values: `PLANNED`, `IN_PROGRESS`, `PAUSED`, `BLOCKED`, `COMPLETE`, `SUPERSEDED`.

For each unit: revalidate current `main` when relevant; mark the unit `IN_PROGRESS`; perform work and validation; record artifacts/commits, unresolved findings, and exact next action; do not mark `COMPLETE` before its intended validation is done.

## 2. Current snapshot

Last updated: **2026-08-22 JST**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Original base `main`: `2086b396d2f30103d9292b722891be436cd28db5`
- Current `main` revalidated at WU-003 close: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged.
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 3 — Core v2 Candidate Design / Minimum Vertical Slice**
- Current phase status: `IN_PROGRESS`
- Current active work unit: **WU-004 — design the minimum W33/SP001-capable vertical slice**
- Next expected work unit: WU-005 implementation of the approved WU-004 slice, unless WU-004 discovers a blocking architecture issue.

### Pilot state

- W33 — future Weekly Profile first-production validation; legacy W33 work is comparison material, not a migration requirement.
- SP001 — future Thematic Profile first-production validation.
- W34 — second Weekly validation after W33 findings are evaluated and incorporated.
- SP002 / SP003 — Thematic generalization validation after SP001 findings are incorporated.

## 3. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `COMPLETE` | component inventory |
| 1 | Contract Normalization | `COMPLETE` | canonical contract map |
| 2 | Historical Knowledge Distillation | `COMPLETE` | historical invariant/regression catalog |
| 3 | Core v2 Candidate Design / Minimum Vertical Slice | `IN_PROGRESS` | W33/SP001-capable implementation candidate |
| 4 | First external production validation | `PLANNED` | W33 + SP001 findings |
| 5 | Cross-Pilot evaluation / first consolidation | `PLANNED` | classified fixes + regressions + revised contract |
| 6 | Second production validation | `PLANNED` | W34 + SP002 + SP003 findings |
| 7 | Stabilization / consolidation | `PLANNED` | stable Core/Profile contracts and simplified hot path |

## 4. Work-unit index

| Work unit | Scope | Status | Primary artifact |
|---|---|---|---|
| WU-000 | Direction, branch, plan, checkpoint | `COMPLETE` | improvement plan / this log |
| WU-001 | Phase 0 component inventory | `COMPLETE` | `docs/survey-production-core-v2-component-inventory.md` |
| WU-002 | Phase 1 contract normalization | `COMPLETE` | `docs/survey-production-core-v2-contract-normalization.md` |
| WU-003 | Phase 2 historical repair/review distillation | `COMPLETE` | `docs/survey-production-core-v2-historical-invariants.md` |
| WU-004 | Minimum v2 vertical-slice architecture | `IN_PROGRESS` | planned: `docs/survey-production-core-v2-minimum-vertical-slice.md` |

## 5. Completed work units

### WU-000 — Direction

Established `Survey Production Core v2 + Profiles + optional Series Research Layer`, kept `main` as production source of truth, rejected legacy W33 migration as a primary acceptance criterion, and separated this improvement/evaluation stream from Pilot production sessions.

Artifacts:
- `docs/survey-production-core-v2-improvement-plan.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`

### WU-001 — Component inventory

Status: `COMPLETE`  
Commit: `a407606d704e7438eed32c0a0441a5cad74bcf2d`

Results:
- shared Screening/Evidence/Draft semantic Core already exists and should be promoted rather than rebuilt;
- primary fragmentation is state/Human Gates/orchestration/publication/Profile policy;
- long Special repair chains are eventual `LEGACY_REPLAY` hot-path removal candidates after invariant extraction;
- missing Core/Profile capabilities were enumerated.

Artifact: `docs/survey-production-core-v2-component-inventory.md`

### WU-002 — Contract normalization

Status: `COMPLETE`  
Commit: `953002529bac3f0f4f9021fa1401df28012f1bc0`

Results:
- target normal Human Gates: Architecture Review + Publication Preview;
- Candidate Selection internal; Visual Review/Freeze/Release machine/provenance transitions;
- temporal policy separated from research scope;
- Core material traceability separated from Profile completeness semantics;
- issue-only Release identity retained; source commit/release anchor distinction preserved;
- generic bootstrap/advance-to-gate and hash-identifiable contract provenance required;
- reusable Evidence facts separated from edition-specific interpretation.

Artifact: `docs/survey-production-core-v2-contract-normalization.md`

### WU-003 — Historical Knowledge Distillation

Status: `COMPLETE`  
Commit: `9f972ab35ce7590d043c36251c8bf5379fb9e546`

Results:
- converted high-value Weekly/Special Human Review findings into named durable invariants;
- classified each invariant by Core/Profile/Publication owner and current implementation maturity;
- defined P0 vs P1 quality set for first W33/SP001 validation;
- captured cross-repair side effects such as `generic fallback fix -> entity-binding defect` and `break repair -> blank-page/orphan regression` as coupled regression requirements;
- identified existing generic and Special-derived tests to preserve/promote;
- retained historical editions as regression/learning corpus, not an implicit reissue backlog.

Priority P0 invariants include:
- broad intake is not completeness;
- no silent material drop;
- supplemental research enters the same trace;
- identifier preservation;
- subject/entity binding;
- Architecture Review materiality/completeness summary;
- reader/internal prose separation;
- exact PDF byte authority;
- generic fix -> stable regression discipline;
- frozen historical immutability.

Artifact: `docs/survey-production-core-v2-historical-invariants.md`

Phase 2 exit condition: **satisfied**.

## 6. Active work unit

### WU-004 — Minimum W33/SP001-capable vertical slice

Status: `IN_PROGRESS`

Started: **2026-08-22 JST**

Objective:

Design the smallest coherent implementation slice that can be merged to `main` and then exercised by separate W33 and SP001 production sessions, while reusing the mature existing shared Screening/Evidence/Draft machinery.

The slice must not become a cosmetic v2 namespace or a big-bang rewrite.

Candidate mandatory capabilities to evaluate:

1. generic Edition/Profile descriptor and temporal policy;
2. v2 contract identity attached to edition state/artifacts;
3. normalized Human Gate/state semantics compatible with two-Gate production;
4. Materiality Ledger + Profile Completeness Result;
5. Architecture Review Summary binding materiality/completeness to Selection/Architecture;
6. true Thematic Profile scope/temporal representation sufficient for SP001;
7. generic orchestration/liveness planner sufficient to support `advance-to-gate` behavior;
8. generic promotion/reuse of identifier and entity-binding safety without preserving repair-script ancestry;
9. bootstrap/session docs sufficient for W33/SP001 sessions to discover the new path from current `main`;
10. tests proving old frozen artifacts are not rewritten and existing shared Core remains compatible.

Design questions to resolve in WU-004:

- which existing schema/state files can be extended compatibly vs need v2 sibling schemas;
- how W33 initializes under v2 without depending on legacy `weekly/2026-W33-work` state;
- stable IDs for Materiality Ledger rows across collector/Screening/Evidence/Selection;
- minimum Thematic completeness model that is general enough for TS/SP001 but not topic-specific;
- how much of `advance-to-gate` can be safely executable before all GitHub workflow wrappers are consolidated;
- which P1 publication invariants can rely on proven current implementations for Pilot 1 instead of being rewritten now.

Planned artifact:
- `docs/survey-production-core-v2-minimum-vertical-slice.md`

Exit condition:
- implementation tasks have explicit inputs/outputs/schemas, compatibility boundaries, tests, and Pilot acceptance criteria;
- no design decision depends on automatic migration of the legacy W33 work branch;
- the slice is small enough to implement/review coherently before W33/SP001 production.

## 7. Pilot finding handoff template

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

A continuation session must read current `main`, the improvement plan, and this log; verify the active/next unit against repository reality; and continue from repository-recorded state. If the log and repository disagree, repository reality wins and this file must be corrected first.
