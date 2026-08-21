# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`

## 1. Purpose

This file is the persistent work-status ledger for the Survey Production Core v2 improvement program. Progress must be reconstructable from repository state alone. Every substantive work unit must read this file before making changes and update it before the work unit is considered complete.

Edition-specific W33 / W34 / SP001 / SP002 / SP003 production state belongs in each edition's canonical artifacts. Only findings evaluated as Core / Profile / contract / regression work are recorded here.

## 2. Update contract

For every substantive work unit: re-read current `main` when relevant; read the improvement plan and this log; mark the unit `IN_PROGRESS`; perform work and validation; update this checkpoint before stopping; record concrete artifacts, unresolved findings, and the exact next action. A unit is not `COMPLETE` until its intended validation is complete.

Status values: `PLANNED`, `IN_PROGRESS`, `PAUSED`, `BLOCKED`, `COMPLETE`, `SUPERSEDED`.

## 3. Current snapshot

Last updated: **2026-08-22 JST**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Original and currently revalidated base `main`: `2086b396d2f30103d9292b722891be436cd28db5`
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 2 — Historical Knowledge Distillation**
- Current phase status: `IN_PROGRESS`
- Current active work unit: **WU-003 — reconstruct high-value repair/review lineage into invariants and regression candidates**
- Next work unit: to be assigned from WU-003 output.

### Pilot validation state

- W33 — future Weekly Profile first-production validation; legacy W33 work is comparison material, not a migration acceptance requirement.
- SP001 — future Thematic Profile first-production validation.
- W34 — second Weekly validation after W33 findings are evaluated and incorporated.
- SP002 / SP003 — Thematic generalization validation after SP001 findings are incorporated.

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `COMPLETE` | `docs/survey-production-core-v2-component-inventory.md` |
| 1 | Contract Normalization | `COMPLETE` | `docs/survey-production-core-v2-contract-normalization.md` |
| 2 | Historical Knowledge Distillation | `IN_PROGRESS` | planned repair-lineage / invariant catalog |
| 3 | Core v2 Candidate Design / Minimum Vertical Slice | `PLANNED` | W33/SP001-capable candidate merged-ready |
| 4 | First external production validation | `PLANNED` | W33 + SP001 findings |
| 5 | Cross-Pilot evaluation / first consolidation | `PLANNED` | classified fixes + regressions + revised contract |
| 6 | Second production validation | `PLANNED` | W34 + SP002 + SP003 findings |
| 7 | Stabilization / consolidation | `PLANNED` | stable Core/Profile contracts and simplified production path |

## 5. Work-unit index

| Work unit | Scope | Status | Primary artifacts |
|---|---|---|---|
| WU-000 | Establish direction, branch, plan, checkpoint | `COMPLETE` | improvement plan; this log |
| WU-001 | Phase 0 component inventory/classification | `COMPLETE` | component inventory |
| WU-002 | Phase 1 contract authority/drift normalization | `COMPLETE` | contract normalization |
| WU-003 | Phase 2 historical repair/review distillation | `IN_PROGRESS` | planned: `docs/survey-production-core-v2-historical-invariants.md` |

## 6. Completed work-unit records

### WU-000 — Program direction

Status: `COMPLETE`

Established `Survey Production Core v2 + Profiles + optional Series Research Layer`, kept `main` as production source of truth, rejected W33 legacy-state migration as an acceptance criterion, and separated improvement/evaluation sessions from Pilot production sessions.

Artifacts:
- `docs/survey-production-core-v2-improvement-plan.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`

### WU-001 — Component inventory

Status: `COMPLETE`

Key results:
- most Screening/Evidence/Draft semantic contracts are already shared and should be promoted, not rebuilt;
- main fragmentation is state/Human Gate/orchestration/publication/profile policy;
- long Special repair chains are eventual `LEGACY_REPLAY` hot-path removal candidates, but their invariants/tests must be extracted first;
- missing components include Materiality Ledger, profile completeness, temporal policy abstraction, advance-to-gate, subject/entity binding guard, structured findings, reusable Evidence corpus, and Series state.

Artifact: `docs/survey-production-core-v2-component-inventory.md`  
Commit: `a407606d704e7438eed32c0a0441a5cad74bcf2d`

### WU-002 — Contract normalization

Status: `COMPLETE`

Key decisions:
- target normal Human Gates are **Architecture Review** and **Publication Preview** for Weekly/Period/Thematic;
- Candidate Selection stays an internal auditable checkpoint;
- Visual Review/Freeze/Release are machine/provenance transitions under exact Publication Preview byte authority;
- Exception Gate is on demand only;
- current coarse lifecycle is retained initially while state ownership is normalized;
- research scope is separated from temporal policy (`ROLLING_WINDOW`, `BOUNDED_PERIOD`, `OPEN_HISTORY_AS_OF`, `CURRENT_STATE_AS_OF`);
- Core owns material traceability; Profiles own completeness semantics;
- editorial role vocabulary becomes Profile-supplied rather than permanently hard-coded as Core ontology;
- issue-only public release identity is canonical after named legacy releases;
- source commit vs release anchor distinction remains preserved;
- generic bootstrap/orchestration and hash-identifiable contract provenance are required;
- reusable Evidence facts are separated from edition-specific interpretation.

Validation:
- compared Special canonical Human Gate policy, Weekly legacy design/config, current release identity policy, Weekly release integrity design, AGENTS bootstrap policy, and Special edition/config contracts;
- contract artifact checked on the branch; branch remained based on unchanged current `main`.

Artifact: `docs/survey-production-core-v2-contract-normalization.md`  
Commit: `953002529bac3f0f4f9021fa1401df28012f1bc0`

Phase 1 exit condition: **satisfied**.

## 7. Active work-unit record

### WU-003 — Historical Knowledge Distillation

Status: `IN_PROGRESS`

Started: **2026-08-22 JST**

Scope:
- reconstruct high-value Human Review / defect / repair lineages from completed Specials and relevant Weekly evolution;
- map each defect to its durable invariant and appropriate owner (`CORE`, Profile, Publication, `LEGACY_REPLAY`);
- identify existing regression tests that already encode the invariant;
- distinguish edition-local repair from generic contract defect and post-release correction;
- identify invariants still trapped only in repair scripts/workflows and therefore at risk during consolidation.

Priority finding families include:
- broad Source Intake / silent material drop (#166);
- subject/entity binding (#191);
- period/chronology consistency;
- final retrospective synthesis preservation;
- Technical Notes generic/fallback/source-specific defects;
- References/source mapping and URL/path integrity;
- reader-facing taxonomy/internal jargon leakage;
- visual/layout/tail/reference pagination regressions;
- release/freeze exact-byte integrity;
- repair-chain side effects caused by successive fixes.

Primary planned artifact:
- `docs/survey-production-core-v2-historical-invariants.md`

Exit condition:
- high-value recurring repairs have a named durable invariant, owner, current implementation/test status, and regression/migration action;
- edition-specific or exact historical variance is explicitly separated from future Core requirements.

## 8. Finding handoff template

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

## 9. Resume rule

A continuation session must read current `main`, the improvement plan, and this log; verify the active/next unit against repository reality; and continue from repository-recorded state. If the log and repository disagree, repository reality wins and this file must be corrected first.
