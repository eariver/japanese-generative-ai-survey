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

Last updated: **2026-08-22 JST — audit correction set closed**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Original base `main`: `2086b396d2f30103d9292b722891be436cd28db5`
- Current `main` revalidated during the audit/correction cycle: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged.
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.
- No frozen historical release has been rewritten by this improvement work.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 3 — Core v2 Candidate Implementation**
- Current phase status: `IN_PROGRESS`
- Latest completed work: **WU-001A / WU-003B / WU-004 audit correction set**
- Next work unit: **WU-005 — Foundation contracts, state and anti-divergence**
- WU-005 has **not started** as of this checkpoint.

### Pilot state

- W33 — first Weekly Profile production validation and compatibility-boundary fixture. Existing legacy RC artifacts have a normative artifact-level `REUSE / REVALIDATE / REGENERATE / REJECT` policy. Automatic legacy-state migration is not a generic Core requirement.
- SP001 — first Thematic Profile production validation. It requires true thematic research expansion and must not fabricate Weekly fields.
- W34 — Weekly fix verification/generalization after W33 findings are incorporated.
- SP002 / SP003 — Thematic fix verification/generalization after SP001 findings are incorporated.

## 3. Audit correction record

A self-audit before WU-005 found seven material deficiencies in the first design pass:

1. WU-004 had been described conversationally as ready while this ledger still correctly showed `IN_PROGRESS`.
2. Phase 0 overstated semantic neutrality: Weekly vocabulary persists through Screening, Evidence, Selection, Architecture, Draft Packages, Draft validation and Issue Synthesis.
3. Phase 2 was failure-driven and lacked a corpus-wide positive/negative audit of all 15 completed Specials.
4. Pilot-critical Thematic Research Expansion was omitted.
5. Review Finding / Repair Set was described but not scheduled as a machine-readable deliverable.
6. v2/legacy state compatibility lacked an anti-divergence contract.
7. `advance-to-gate` was underspecified as a planner rather than planner + executable dispatch/control.

The correction cycle preserved the target architecture and fixed the implementation boundary.

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `COMPLETE` after audit amendment | original inventory + profile-pollution amendment through Synthesis |
| 1 | Contract Normalization | `COMPLETE` as target contract map | canonical contract map; implementation pending |
| 2 | Historical Knowledge Distillation | `COMPLETE` after Phase 2B | invariant catalog + all-15-edition positive/negative production pattern matrix |
| 3 | Core v2 Candidate Implementation | `IN_PROGRESS` | corrected vertical slice + WU-005–WU-011 implementation candidate |
| 4 | First external production validation | `PLANNED` | W33 + SP001 findings |
| 5 | Cross-Pilot evaluation / first consolidation | `PLANNED` | classified fixes + regressions + revised contract |
| 6 | Second production validation | `PLANNED` | W34 + SP002 + SP003 findings |
| 7 | Stabilization / consolidation | `PLANNED` | stable Core/Profile contracts and simplified hot path |

## 5. Work-unit index

| Work unit | Scope | Status | Primary artifact |
|---|---|---|---|
| WU-000 | Direction, branch, plan, checkpoint | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement plan / this log |
| WU-001 | Initial Phase 0 component inventory | `COMPLETE / AMENDED` | component inventory |
| WU-001A | Expand semantic/profile-pollution map through Architecture/Draft/Synthesis | `COMPLETE` | component inventory audit amendment |
| WU-002 | Phase 1 contract normalization | `COMPLETE` | contract normalization |
| WU-003 | Initial failure/invariant distillation | `COMPLETE / EXTENDED` | historical invariant catalog |
| WU-003B | 15-Special positive/negative production-pattern audit | `COMPLETE` | historical production pattern matrix |
| WU-004 | Corrected minimum W33/SP001-capable vertical-slice architecture | `COMPLETE` | base vertical slice + audit amendment + W33 disposition |
| WU-005 | Foundation contracts, state and anti-divergence | `PLANNED` | implementation next |
| WU-006 | Research discovery expansion + Screening v2 | `PLANNED` | implementation |
| WU-007 | Factual Evidence + Edition View + Materiality + Completeness | `PLANNED` | implementation |
| WU-008 | Matrix + internal Selection + Architecture + W33 disposition support | `PLANNED` | implementation |
| WU-009 | Drafting + Synthesis semantic generalization | `PLANNED` | implementation |
| WU-010 | Executable orchestration + Finding/Repair Set | `PLANNED` | implementation |
| WU-011 | P0 quality integration + Pilot bootstrap | `PLANNED` | merge-ready candidate |

## 6. Completed design/distillation work

### WU-000 — Direction

Retained architecture:

```text
Survey Production Core v2
  + Research / Editorial Profile
  + Publication Profile
  + optional Series Research Layer
```

Retained operational principles:
- current `main` is production source of truth;
- frozen historical releases are immutable learning/regression corpus;
- W33/SP001 production occurs in separate sessions after a coherent candidate reaches `main`;
- Pilot findings return to this design/evaluation stream.

Audit amendment:
- W33 is not clean-slate by default. Its existing RC is an integration fixture whose individual artifacts receive explicit compatibility dispositions.

### WU-001 / WU-001A — Component archaeology

Original inventory commit: `a407606d704e7438eed32c0a0441a5cad74bcf2d`  
Audit amendment commit: `b41d40da86c8335c07116bbedd20894045bf9491`

Artifacts:
- `docs/survey-production-core-v2-component-inventory.md`
- `docs/survey-production-core-v2-component-inventory-audit-amendment.md`

Corrected conclusion:
- substantial generic primitives already exist;
- `shared file format != shared semantic Core`;
- Weekly semantics currently pollute Screening → Evidence → Matrix/Selection → Architecture → Draft → Synthesis;
- v2 should decompose and retain generic hash/provenance/evidence-reference primitives while moving editorial semantics into Profiles.

### WU-002 — Contract normalization

Commit: `953002529bac3f0f4f9021fa1401df28012f1bc0`

Artifact:
- `docs/survey-production-core-v2-contract-normalization.md`

Retain:
- Architecture Review + Publication Preview as normal Human Gates;
- Candidate Selection internal/auditable;
- temporal policy separate from research scope;
- Materiality mechanism in Core, completeness semantics in Profiles;
- issue-only public Release identity;
- exact-byte Publication Preview authority;
- reusable factual Evidence separated from edition-specific interpretation.

### WU-003 / WU-003B — Historical knowledge distillation

Initial invariant commit: `9f972ab35ce7590d043c36251c8bf5379fb9e546`  
15-edition matrix commit: `ce53e172cebbee65fcb77f8bb6e4394be1aac3f1`

Artifacts:
- `docs/survey-production-core-v2-historical-invariants.md`
- `docs/survey-production-core-v2-historical-production-pattern-matrix.md`

Phase 2B explicitly covers:
- Monthly `2026-M01` … `2026-M07`;
- Half-year `2024-H1`, `2024-H2`, `2025-H1`, `2025-H2`;
- Annual `2020-Y`, `2021-Y`, `2022-Y`, `2023-Y`.

Durable positive patterns include:
- exact-hash immutable review/release provenance;
- empirical convergence from revisioned/post-Freeze gates to issue-only + exact-byte Publication Preview authority;
- factual Evidence separated from reader rendering;
- Period synthesis deepening from Monthly → Half-year → Annual;
- narrative compression plus separately preserved objective chronology;
- stable long-form mixed-layout behavior;
- render-first Visual QA;
- coupled regression testing rather than one-symptom repairs.

### WU-004 — Corrected minimum vertical slice

Original design commit: `8970111d9c9c12c1b1089a261872f184de892c6f`  
W33 disposition commit: `c41e16fb789f040b0fc3eb2aeb1477d5e2aca6a7`  
Audit amendment commit: `3a8bc11eb1b8ddeebcd25c0737a29089020a1e06`

Artifacts:
- `docs/survey-production-core-v2-minimum-vertical-slice.md`
- `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md`
- `docs/survey-production-core-v2-w33-artifact-disposition.md`

The audit amendment is authoritative when it conflicts with the original WU-004 document.

Corrected Pilot-critical capabilities:

1. Foundation Profile/State/Contract identity;
2. one-way v2-authoritative state compatibility + anti-divergence;
3. research discovery/expansion provenance;
4. Thematic seed → backward/forward → successor/parallel/competing/bridge → gap-fill closure;
5. profile-neutral Screening;
6. factual Evidence + subject/entity binding;
7. Edition Evidence View;
8. Materiality Ledger + Profile Completeness;
9. profile-aware Matrix/internal Selection;
10. profile-neutral Architecture + Architecture Review Summary;
11. generic Draft Package/Draft Result + Profile validators;
12. Profile Synthesis envelope rather than mandatory `this_week_signals`;
13. machine-readable Review Finding / Repair Set;
14. planner + executable `advance-to-gate` dispatcher;
15. W33 artifact-level compatibility policy;
16. P0 quality/regression + Pilot bootstrap.

WU-004 exit condition: **satisfied after audit correction**.

## 7. W33 compatibility contract

Normative artifact: `docs/survey-production-core-v2-w33-artifact-disposition.md`.

Default dispositions:
- accepted Raw/collector provenance → `REVALIDATE`;
- carry-over/current-context Raw → `REVALIDATE`;
- v1 Screening → `REGENERATE`;
- Evidence factual subset → `REVALIDATE`; Edition View regenerated;
- Candidate Matrix/Selection → `REGENERATE`;
- Architecture → `REGENERATE`;
- Draft/Synthesis/final claim review → `REGENERATE` as canonical v2 artifacts;
- legacy TeX/PDF/Visual Review → retained comparison fixture, not v2 release authority;
- legacy `pipeline-state.json` → immutable comparison provenance, never v2 authority.

This creates a real integration test without adding a universal automatic migration requirement.

## 8. Pilot finding handoff contract

WU-010 must implement machine-readable Finding and Repair Set schemas/validators before external Pilot findings are returned.

Minimum classification scope:

```text
EDITION_LOCAL
WEEKLY_PROFILE
PERIOD_PROFILE
THEMATIC_PROFILE
CORE
PUBLICATION_PROFILE
QUALITY_CONTRACT
SERIES_LAYER
UNCLASSIFIED
```

A local production workaround is evidence about a defect and does not automatically become the canonical Core fix.

## 9. Implementation sequence now authorized

The corrected implementation sequence is:

```text
WU-005 Foundation contracts/state/anti-divergence
  -> WU-006 Research expansion + Screening
  -> WU-007 Evidence/View/Materiality/Completeness
  -> WU-008 Matrix/Selection/Architecture
  -> WU-009 Draft/Synthesis
  -> WU-010 executable orchestration + findings/repair sets
  -> WU-011 P0 quality + Pilot bootstrap
  -> coherent review/merge to main
  -> separate W33 and SP001 production sessions
```

No implementation work unit may restore dummy Weekly fields merely to reuse a v1 schema for Thematic production.

## 10. Resume rule

A continuation session must read current `main`, the improvement plan, this log, and the authoritative audit amendments; verify the active/next unit against repository reality; and continue from repository-recorded state. If the log and repository disagree, repository reality wins and this file must be corrected first.

**Next action: WU-005 — Foundation contracts, state and anti-divergence.**
