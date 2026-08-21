# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`  
Authority index: `docs/survey-production-core-v2-authority.md`

## 1. Purpose and update contract

This is the persistent work-status ledger for the Survey Production Core v2 improvement program. Progress must be reconstructable from repository state alone. Every substantive work unit reads this file before changes and updates it before the unit is considered complete.

Edition-specific W33 / W34 / SP001 / SP002 / SP003 state stays in each edition's canonical production artifacts. This log records only compilation-system design, implementation, and returned findings evaluated as Core/Profile/Publication/regression work.

Status values: `PLANNED`, `IN_PROGRESS`, `PAUSED`, `BLOCKED`, `COMPLETE`, `SUPERSEDED`.

For each unit: revalidate current `main` when relevant; mark the unit `IN_PROGRESS`; perform work and validation; record artifacts/commits, unresolved findings, and exact next action; do not mark `COMPLETE` before its intended validation is done.

## 2. Current snapshot

Last updated: **2026-08-22 JST — second audit correction set closed**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Original base `main`: `2086b396d2f30103d9292b722891be436cd28db5`
- Current `main` revalidated at second-audit correction start: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged.
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.
- No frozen historical release has been rewritten by this improvement work.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 3 — Core v2 Candidate Implementation**
- Current phase status: `IN_PROGRESS`
- Latest completed work: **WU-003C / WU-004B second-audit correction set**
- Next work unit: **WU-005 — Foundation contracts, state, implementation identity and anti-divergence**
- WU-005 has **not started** as of this checkpoint.

### Pilot state

- **W33 primary role:** `Weekly Profile First Production Validation`.
- The legacy `weekly/2026-W33-work` RC is an **optional benchmark/provenance fixture**, not a required migration or compatibility acceptance test.
- Safe legacy artifact reuse is permitted only when it reduces work without weakening v2 correctness. A W33 run may regenerate artifacts from verified/fresh inputs when that is simpler or clearer.
- SP001 — first Thematic Profile production validation. It requires true thematic research expansion and closure/saturation evidence and must not fabricate Weekly fields.
- W34 — Weekly fix verification/generalization after W33 findings are incorporated.
- SP002 / SP003 — Thematic fix verification/generalization after SP001 findings are incorporated.

## 3. Audit history

### 3.1 First pre-implementation audit

The first self-audit found seven material deficiencies:

1. WU-004 had been described conversationally as ready while this ledger still correctly showed `IN_PROGRESS`.
2. Phase 0 overstated semantic neutrality: Weekly vocabulary persists through Screening, Evidence, Selection, Architecture, Draft Packages, Draft validation and Issue Synthesis.
3. Phase 2 was failure-driven and lacked a corpus-wide positive/negative audit of all 15 completed Specials.
4. Pilot-critical Thematic Research Expansion was omitted.
5. Review Finding / Repair Set was described but not scheduled as a machine-readable deliverable.
6. v2/legacy state compatibility lacked an anti-divergence contract.
7. `advance-to-gate` was underspecified as a planner rather than planner + executable dispatch/control.

That correction produced the Phase 0 amendment, first 15-edition pattern matrix, initial W33 artifact-disposition document, and corrected vertical-slice amendment.

### 3.2 Second pre-implementation audit

The second audit found eight additional issues:

A. W33 had drifted from `Weekly Profile First Production Validation` toward a compatibility-boundary test.
B. The first 15-edition matrix had explicit rows but insufficient production-lineage depth.
C. Optional W33 reuse work was assigned too late in the implementation sequence.
D. Base design documents remained visually canonical despite amendments.
E. Pilot entry was ambiguous between Architecture-only capability and a full production-capable candidate.
F. Contract SHA did not bind executable implementation identity.
G. Finding taxonomy mixed ownership with regression action.
H. Thematic completeness lacked explicit saturation/closure evidence.

Second-audit corrections:
- W33 restored to Weekly-first production validation; legacy reuse made optional;
- all 15 Specials re-audited from final `pipeline-state.json` production lineage;
- implementation identity added to target provenance;
- Finding taxonomy normalized into orthogonal axes;
- Thematic closure evidence defined;
- optional W33 reuse assigned to discovery/Evidence/semantic stages rather than one late compatibility block;
- first Pilot now requires a full production-capable v2 candidate merged to `main`;
- live document authority is centralized in `docs/survey-production-core-v2-authority.md`.

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `COMPLETE` after first audit amendment | original inventory + profile-pollution amendment through Synthesis |
| 1 | Contract Normalization | `COMPLETE` after second-audit amendment | base contract map + implementation identity/taxonomy/Pilot-entry/closure amendment |
| 2 | Historical Knowledge Distillation | `COMPLETE` after Phase 2C | invariant catalog + first matrix + all-15 edition-level production deep audit |
| 3 | Core v2 Candidate Implementation | `IN_PROGRESS` | authoritative second-audit vertical-slice contract + WU-005–WU-011 implementation candidate |
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
| WU-002 | Phase 1 contract normalization | `COMPLETE / AMENDED` | base contract + second-audit amendment |
| WU-003 | Initial failure/invariant distillation | `COMPLETE / EXTENDED` | historical invariant catalog |
| WU-003B | First all-15 positive/negative production-pattern matrix | `COMPLETE AS FIRST PASS / SUPERSEDED AS EXIT EVIDENCE` | historical production pattern matrix |
| WU-003C | Edition-level production-lineage audit of all 15 Specials | `COMPLETE` | historical production deep audit |
| WU-004 | First corrected minimum vertical slice | `COMPLETE AS FIRST PASS / SUPERSEDED IN PART` | base + first audit amendment |
| WU-004B | Correct Pilot role/authority/identity/taxonomy/closure contract | `COMPLETE` | second-audit amendment + authority index + revised W33 policy |
| WU-005 | Foundation contracts, state, implementation identity and anti-divergence | `PLANNED` | implementation next |
| WU-006 | Research discovery expansion + Screening v2 | `PLANNED` | implementation |
| WU-007 | Factual Evidence + Edition View + Materiality + Completeness | `PLANNED` | implementation |
| WU-008 | Matrix + internal Selection + Architecture | `PLANNED` | implementation |
| WU-009 | Drafting + Synthesis semantic generalization | `PLANNED` | implementation |
| WU-010 | Executable orchestration + Finding/Repair Set | `PLANNED` | implementation |
| WU-011 | P0 quality integration + full Pilot bootstrap | `PLANNED` | merge-ready candidate |

## 6. Durable design retained through both audits

The target remains:

```text
Survey Production Core v2
  + Research / Editorial Profile
  + Publication Profile
  + optional Series Research Layer
```

Retained invariants:
- current `main` is production source of truth;
- frozen historical releases remain immutable learning/regression corpus;
- `shared file format != shared semantic Core`;
- Weekly semantics must not be fabricated for Thematic production;
- Architecture Review + Publication Preview are the normal Human Gates;
- Candidate Selection is internal/auditable;
- temporal policy is separate from research scope;
- Materiality mechanism is Core while completeness meaning is Profile-owned;
- issue-only public Release identity;
- exact-byte Publication Preview authority;
- reusable factual Evidence is separated from edition-specific significance;
- Thematic research requires reference/lineage expansion plus explicit closure/saturation evidence;
- semantic contract identity, executable implementation identity and artifact byte identity are all provenance;
- Pilot Finding scope and regression need are orthogonal;
- Pilot findings return to this design/evaluation stream rather than becoming automatic edition-specific repair chains.

## 7. Completed correction artifacts

### Phase 0 correction

- `docs/survey-production-core-v2-component-inventory-audit-amendment.md`
- commit `b41d40da86c8335c07116bbedd20894045bf9491`

Key rule: `shared file format != shared semantic Core`.

### Phase 1 base + second amendment

- base: `docs/survey-production-core-v2-contract-normalization.md`
- second amendment: `docs/survey-production-core-v2-contract-normalization-second-audit-amendment.md`
- second-amendment commit: `db0bffc6d84c13ec49b7eb7e22d17e32c3d4a87b`

Added:
- `implementation.repository_commit_sha` / orchestrator identity;
- orthogonal Finding taxonomy;
- full-production-capable pre-Pilot boundary;
- optional W33 reuse rule;
- Thematic closure evidence.

### Phase 2 knowledge distillation

- `docs/survey-production-core-v2-historical-invariants.md`
- first matrix: `docs/survey-production-core-v2-historical-production-pattern-matrix.md`
- deep audit: `docs/survey-production-core-v2-historical-production-deep-audit.md`
- deep-audit commit: `29d8aceba064336a1fcf1cde4f4d48d4ca51dc5b`

Phase 2C explicitly rechecked all fifteen final `pipeline-state.json` records and retained edition-specific Gate, Architecture, revision/repair, chronology/synthesis, control-commit and publication provenance.

New/strengthened cross-edition findings include:
- M06 template semantic leakage proves reader scope labels must derive from canonical state/profile;
- 2020-Y proves content enrichment can reintroduce layout regressions;
- 2024-H1 proves a new entity repair can regress an earlier entity repair;
- 2022-Y demonstrates a coupled long-form regression family across taxonomy, references, TOC, fallback, entity binding, empty wrappers, chronology mapping and layout;
- 2025-H1 proves completeness and publication correctness are independent axes.

### Phase 3 second correction

- revised W33 policy: `docs/survey-production-core-v2-w33-artifact-disposition.md`
  - commit `ca84d76768d92ee0f775da81bd5c2940424255ce`
- second vertical-slice amendment: `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md`
  - commit `fd6bb0e061f571b55bb4ec11742bf514d15a14bc`
- authority index: `docs/survey-production-core-v2-authority.md`
  - commit `199a289052879857dbb63673502b0a43a1bb048e`

Authoritative W33 rule:

```text
W33 = Weekly Profile First Production Validation
legacy W33 RC = optional benchmark/provenance fixture
legacy reuse = permitted optimization, never acceptance criterion
```

## 8. Pilot rollout contract

A **full production-capable** candidate must be merged to `main` before external W33/SP001 sessions start.

This means the merged candidate must have one coherent path through Human Gate 2 / exact-byte release authorization even if a particular initial production request says “stop at Architecture Review”.

Normal interaction remains:

```text
start
-> autonomous work
-> HUMAN GATE 1 Architecture Review
-> autonomous downstream work after approval
-> HUMAN GATE 2 Publication Preview
-> deterministic Visual Review / Freeze / merge / Release for approved bytes
```

## 9. Finding handoff contract

WU-010 implements:

```yaml
classification:
  scope: EDITION_LOCAL | WEEKLY_PROFILE | PERIOD_PROFILE | THEMATIC_PROFILE | CORE | PUBLICATION_PROFILE | QUALITY_CONTRACT | SERIES_LAYER | UNCLASSIFIED
  defect_kind: CORRECTNESS | TRACEABILITY | COVERAGE | EDITORIAL | PUBLICATION | ORCHESTRATION | COMPATIBILITY | OTHER
  confidence: low | medium | high
requires_regression: true | false
```

A production workaround is evidence about a defect, not automatic authorization to promote it into Core.

## 10. Thematic closure contract

Thematic completeness is not source-count based.

Closure requires:
- all named obligations disposed;
- zero open material `NEEDS_RESEARCH` obligations;
- targeted residual gap-fill completed;
- latest expansion pass produces zero new material obligations, or all new obligations are explicitly disposed;
- unresolved limitations remain visible.

Exact schema is WU-007 work.

## 11. Resume rule

A continuation session must:

```text
read current main
-> read this worklog
-> read docs/survey-production-core-v2-authority.md
-> read authoritative documents for the active WU
-> verify repository reality
-> mark work unit IN_PROGRESS
-> perform work + validation
-> record commit and next action
```

If documentation and repository reality disagree, repository reality wins and this log is corrected first.

**Next action: WU-005 — Foundation contracts, state, implementation identity and anti-divergence.**
