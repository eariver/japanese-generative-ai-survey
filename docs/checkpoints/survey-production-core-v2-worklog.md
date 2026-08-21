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

Last updated: **2026-08-22 JST — post-audit correction**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Original base `main`: `2086b396d2f30103d9292b722891be436cd28db5`
- Current `main` revalidated during the audit: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged.
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.
- No frozen historical release is being rewritten by this improvement work.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 0/2 correction + Phase 3 design correction**
- Current phase status: `IN_PROGRESS`
- Current active work: **WU-001A + WU-003B + WU-004 correction**
- WU-005 implementation is explicitly **not authorized yet**; WU-004 must be closed after the correction set is complete.

### Pilot state

- W33 — first Weekly Profile production validation. Existing legacy W33 RC artifacts must be inventoried and individually classified `REUSE / REVALIDATE / REGENERATE / REJECT`; automatic legacy-state migration is not itself a required product capability.
- SP001 — first Thematic Profile production validation. It requires true thematic research expansion, not only generic collector execution plus Screening.
- W34 — Weekly fix verification/generalization after W33 findings are incorporated.
- SP002 / SP003 — Thematic fix verification/generalization after SP001 findings are incorporated.

## 3. Audit correction record

A self-audit performed before WU-005 identified material deficiencies in the prior completion claims.

1. WU-004 had been described conversationally as fixed/ready, but this ledger still correctly recorded it as `IN_PROGRESS`; no formal exit validation had been recorded.
2. Phase 0 overstated how profile-neutral the existing shared semantic path is. Weekly vocabulary persists through Screening, Evidence, Selection, Architecture, Draft Packages, Draft validation, and Issue Synthesis.
3. Phase 2 distilled high-value failure invariants but did not yet perform a corpus-wide edition-by-edition positive/negative-pattern review across all 15 completed Retrospective Specials.
4. The WU-004 implementation plan omitted a Pilot-critical Thematic Research Expansion mechanism.
5. The Pilot finding/repair-set mechanism was described but not scheduled as a machine-readable implementation deliverable.
6. The proposed v2/legacy dual-state transition lacked an explicit anti-divergence rule.
7. `advance-to-gate` was underspecified as a planner; Pilot liveness requires a planner plus an executable dispatch/control abstraction for deterministic actions.

These findings do not invalidate the target architecture (`Core + Profiles + Publication Profile + optional Series Layer`), but they do invalidate the prior claim that Phase 0–2 were fully closed.

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `IN_PROGRESS` (amendment) | component inventory + full profile-pollution map |
| 1 | Contract Normalization | `COMPLETE` as target contract map | canonical contract map; implementation still pending |
| 2 | Historical Knowledge Distillation | `IN_PROGRESS` (Phase 2B) | invariant catalog + 15-edition positive/negative pattern matrix |
| 3 | Core v2 Candidate Design / Minimum Vertical Slice | `IN_PROGRESS` | corrected W33/SP001-capable implementation contract |
| 4 | First external production validation | `PLANNED` | W33 + SP001 findings |
| 5 | Cross-Pilot evaluation / first consolidation | `PLANNED` | classified fixes + regressions + revised contract |
| 6 | Second production validation | `PLANNED` | W34 + SP002 + SP003 findings |
| 7 | Stabilization / consolidation | `PLANNED` | stable Core/Profile contracts and simplified hot path |

## 5. Work-unit index

| Work unit | Scope | Status | Primary artifact |
|---|---|---|---|
| WU-000 | Direction, branch, plan, checkpoint | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement plan / this log |
| WU-001 | Initial Phase 0 component inventory | `COMPLETE` but insufficient | component inventory |
| WU-001A | Expand profile-pollution/dependency inventory through Architecture/Draft/Synthesis | `IN_PROGRESS` | amended component inventory |
| WU-002 | Phase 1 contract normalization | `COMPLETE` | contract normalization |
| WU-003 | Initial historical issue/invariant distillation | `COMPLETE` but partial corpus coverage | historical invariant catalog |
| WU-003B | 15-Special corpus positive/negative-pattern audit | `IN_PROGRESS` | historical production pattern matrix |
| WU-004 | Minimum v2 vertical-slice architecture | `IN_PROGRESS` | minimum vertical slice, corrected after audit |
| WU-005 | Foundation contracts and resolver | `PLANNED / HOLD` | implementation only after WU-004 closes |

## 6. Existing completed artifacts retained

### WU-000 — Direction

Retain:
- `Survey Production Core v2 + Profiles + optional Series Research Layer`;
- current `main` as production source of truth;
- separate Pilot production sessions and this design/evaluation stream;
- historical releases as immutable regression/learning corpus.

Audit amendment:
- W33 must not be treated as a clean-slate issue by default. Existing RC-stage artifacts are valuable integration evidence and require artifact-level disposition. Automatic state migration remains non-goal unless Pilot evidence justifies it.

### WU-001 — Initial component inventory

Original commit: `a407606d704e7438eed32c0a0441a5cad74bcf2d`

Useful findings retained:
- substantial shared provenance/Evidence mechanics already exist;
- state/Human Gates/orchestration/publication/Profile policy are fragmented;
- legacy repair chains should yield invariants/tests rather than define the future hot path.

Audit correction:
- do not call the full semantic path already profile-neutral. Weekly vocabulary remains embedded beyond Screening/Evidence, including Architecture, Draft Packages, Draft validation, and Issue Synthesis.

### WU-002 — Contract normalization

Commit: `953002529bac3f0f4f9021fa1401df28012f1bc0`

Retain:
- Architecture Review + Publication Preview as normal Human Gates;
- Candidate Selection internal/auditable;
- temporal policy separate from research scope;
- Materiality mechanism in Core, completeness semantics in Profiles;
- issue-only public Release identity;
- exact-byte Publication Preview authority;
- reusable factual Evidence separated from edition-specific interpretation.

### WU-003 — Initial historical invariant catalog

Commit: `9f972ab35ce7590d043c36251c8bf5379fb9e546`

Retain the named invariants and regression priorities, including Source Intake/materiality, identifier preservation, entity binding, reader/internal separation, exact-byte publication authority, and repair-chain-to-regression discipline.

Audit correction:
- this is a high-value failure-driven catalog, not yet the complete 15-edition knowledge-distillation exit artifact. WU-003B must add successful stable patterns and edition-specific evolution.

## 7. Active correction work

### WU-001A — semantic/profile-pollution map expansion

Status: `IN_PROGRESS`

Must explicitly inspect/classify at least:
- Screening schema/prompt/runners;
- Evidence schema/prompt/runners;
- Candidate Matrix / Selection;
- Architecture Input / Architecture Plan;
- Draft Package / Draft Result / Draft validator/renderer;
- Issue Synthesis;
- finalization/publication boundary.

Exit condition:
- every Pilot-critical stage is classified as genuinely Core, generic primitive with Profile field pollution, Profile adapter, Publication Profile, or legacy compatibility;
- WU-004 implementation work accounts for each required semantic boundary.

### WU-003B — 15-Special corpus positive/negative-pattern audit

Status: `IN_PROGRESS`

Corpus:
- 2026-M01 through 2026-M07;
- 2024-H1, 2024-H2, 2025-H1, 2025-H2;
- 2020-Y, 2021-Y, 2022-Y, 2023-Y.

For each edition record:
- production/profile type;
- mechanisms/pipeline generation actually used;
- major Human Review or repair themes;
- stable successful patterns that should be retained;
- observed failure/repair lessons;
- reusable Core/Profile/Publication implications;
- whether the behavior is regression evidence or legacy-only variance.

Exit condition:
- the 15-edition corpus has explicit coverage; knowledge extraction is not limited to already-known Issues.

### WU-004 — corrected minimum W33/SP001-capable vertical slice

Status: `IN_PROGRESS`

The corrected slice must include or explicitly schedule before Pilot:

1. Foundation Profile/State/Contract identity;
2. profile-neutral Screening and factual Evidence boundary;
3. profile-aware Candidate Matrix/Selection;
4. profile-neutral Architecture contract plus Profile/Publication hooks;
5. profile-neutral Draft Package/Draft validation semantics; Weekly-only `late_breaking`/`this_week` vocabulary moved behind Weekly/Profile fields;
6. profile-aware post-draft Synthesis contract;
7. Materiality Ledger and Completeness Result;
8. **Thematic Research Expansion**: seed → backward/forward references → successor/parallel/competing/bridge discovery → gap-fill → closure/completeness audit;
9. Architecture Review Summary;
10. machine-readable Review Finding / Repair Set;
11. one-way v2-authoritative state compatibility rule and anti-divergence validation;
12. `advance-to-gate` planner **plus executable deterministic-action dispatcher/control abstraction**;
13. W33 artifact disposition inventory (`REUSE / REVALIDATE / REGENERATE / REJECT`);
14. P0 quality/regression promotion;
15. Pilot/bootstrap docs sufficient for a separate session to operate from current `main` without chat history.

WU-004 may split implementation work units after this correction, but Pilot acceptance criteria must cover the complete semantic path to Architecture Review for both W33 and SP001, and the planned publication path must not reintroduce Weekly vocabulary into Thematic production.

## 8. W33 compatibility principle

The target is not a general-purpose automatic v1→v2 state migrator.

For the already-developed W33 issue, however, the existing `weekly/2026-W33-work` RC is an explicit integration fixture. Before Pilot execution, every potentially reusable artifact class must receive one disposition:

- `REUSE` — bytes/contracts remain valid under v2 without semantic reinterpretation;
- `REVALIDATE` — artifact may be reused only after v2 provenance/semantic validation;
- `REGENERATE` — source facts/provenance may inform production, but the artifact contract must be regenerated under v2;
- `REJECT` — artifact is misleading/incompatible and must not enter v2 state.

This validates compatibility boundaries without making perfect automatic migration a Core design requirement.

## 9. Pilot finding handoff contract

The earlier YAML template remains useful as a human-readable view, but the first v2 candidate must implement a schema/validator for findings/repair sets before external Pilot findings are returned.

Minimum semantics:

```yaml
finding_id:
edition:
stage:
observed_problem:
expected_behavior:
actual_behavior:
production_workaround:
classification:
  scope: EDITION_LOCAL | WEEKLY_PROFILE | PERIOD_PROFILE | THEMATIC_PROFILE | CORE | PUBLICATION_PROFILE | QUALITY_CONTRACT | SERIES_LAYER | UNCLASSIFIED
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

## 10. Resume rule

A continuation session must read current `main`, the improvement plan, and this log; verify the active/next unit against repository reality; and continue from repository-recorded state. If the log and repository disagree, repository reality wins and this file must be corrected first.

**Next action:** complete WU-001A and WU-003B, amend WU-004 from their findings, then record a formal WU-004 exit decision. Do not begin WU-005 before that exit decision is committed.
