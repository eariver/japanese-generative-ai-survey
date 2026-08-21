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

Last updated: **2026-08-22 JST — second audit correction in progress**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Original base `main`: `2086b396d2f30103d9292b722891be436cd28db5`
- Current `main` revalidated at second-audit correction start: `2086b396d2f30103d9292b722891be436cd28db5` — unchanged.
- Production source of truth remains current `main` after coherent candidate changes are reviewed and merged.
- No frozen historical release is being rewritten by this improvement work.

### Program state

- Overall status: `ACTIVE`
- Current phase: **Phase 2 deep audit + Phase 3 contract correction**
- Current phase status: `IN_PROGRESS`
- Active work: **WU-003C + WU-004B**
- WU-005 is **HOLD / not authorized** until both correction units close.

### Pilot state

- **W33 primary role:** `Weekly Profile First Production Validation`.
- The legacy `weekly/2026-W33-work` RC is an **optional benchmark/provenance fixture**, not a required migration or compatibility acceptance test.
- Safe legacy artifact reuse is permitted only when it reduces work without weakening v2 correctness. A W33 run may instead regenerate an artifact from verified inputs when that is simpler or clearer.
- SP001 — first Thematic Profile production validation. It requires true thematic research expansion and must not fabricate Weekly fields.
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

That correction produced the Phase 0 amendment, first 15-edition pattern matrix, W33 artifact-disposition document, and corrected vertical-slice amendment.

### 3.2 Second pre-implementation audit

A second audit deliberately challenged the corrected state before WU-005 and found additional issues:

A. W33 had drifted from `Weekly Profile First Production Validation` toward a compatibility-boundary test. Legacy reuse must be optional and must not become a Pilot acceptance criterion.
B. The first 15-edition matrix had explicit rows for all editions but did not inspect every edition at sufficient production-lineage depth. `row coverage != edition-level audit depth`.
C. If optional W33 reuse is implemented, compatibility work must follow stage ownership: Raw/provenance at discovery, factual Evidence at Evidence, semantic comparisons later. It must not be concentrated artificially in WU-008.
D. Base design documents remained visually canonical even where audit amendments superseded them. Live-tree authority labels must be explicit.
E. Pilot entry criteria were ambiguous between “Architecture Review capable” and “full production-capable candidate”. The program must choose one model.
F. Contract hashes alone do not bind implementation behavior. v2 provenance must include repository/control implementation identity.
G. Finding classification vocabulary had two shapes. Scope classification and regression requirement must be separate normalized axes.
H. Thematic completeness needs saturation/closure evidence rather than only recursively declared obligations.

These findings reopen Phase 2 and Phase 3 design. WU-005 remains on hold until the correction is committed and re-audited.

## 4. Phase checkpoint

| Phase | Description | Status | Exit evidence |
|---|---|---|---|
| 0 | Cross-Pipeline Process Archaeology | `COMPLETE` after audit amendment | original inventory + profile-pollution amendment through Synthesis |
| 1 | Contract Normalization | `COMPLETE / AMENDMENT PENDING` | canonical contract map + second-audit provenance/taxonomy clarifications |
| 2 | Historical Knowledge Distillation | `IN_PROGRESS` — Phase 2C | invariant catalog + edition-depth audit across all 15 frozen Specials |
| 3 | Core v2 Candidate Design / Implementation | `IN_PROGRESS / DESIGN HOLD` | WU-004B corrected Pilot contract, then WU-005–WU-011 implementation |
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
| WU-002 | Phase 1 contract normalization | `COMPLETE / AMENDMENT PENDING` | contract normalization |
| WU-003 | Initial failure/invariant distillation | `COMPLETE / EXTENDED` | historical invariant catalog |
| WU-003B | First all-15 positive/negative production-pattern matrix | `COMPLETE AS FIRST PASS / INSUFFICIENT DEPTH` | historical production pattern matrix |
| **WU-003C** | Edition-level production-lineage audit of all 15 Specials | **`IN_PROGRESS`** | deep historical production audit |
| WU-004 | First corrected minimum vertical slice | `COMPLETE AS FIRST PASS / REOPENED BY AUDIT` | base + first audit amendment |
| **WU-004B** | Correct Pilot role/authority/identity/taxonomy/closure contract | **`IN_PROGRESS`** | second-audit amendment + document status normalization |
| WU-005 | Foundation contracts, state and anti-divergence | `PLANNED / HOLD` | implementation after WU-003C/WU-004B |
| WU-006 | Research discovery expansion + Screening v2 | `PLANNED` | implementation |
| WU-007 | Factual Evidence + Edition View + Materiality + Completeness | `PLANNED` | implementation |
| WU-008 | Matrix + internal Selection + Architecture | `PLANNED` | implementation |
| WU-009 | Drafting + Synthesis semantic generalization | `PLANNED` | implementation |
| WU-010 | Executable orchestration + Finding/Repair Set | `PLANNED` | implementation |
| WU-011 | P0 quality integration + Pilot bootstrap | `PLANNED` | merge-ready candidate |

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
- Thematic research requires reference/lineage expansion and explicit closure evidence;
- Pilot findings return to this design/evaluation stream rather than becoming automatic edition-specific repair chains.

## 7. W33 role and legacy fixture policy

### 7.1 Primary acceptance objective

W33 succeeds as a Pilot when the v2 Weekly Profile can compile the real issue correctly and reach the requested Human Gate/publication path under the normalized Core contract.

Required W33 acceptance concerns include:
- correct rolling editorial-window/carry-over semantics;
- current/broad research with explicit completeness status;
- no silent material drop;
- internal Selection and Architecture Review compression visibility;
- correct factual/claim/attribution boundaries;
- valid downstream publication path without legacy Human Gate semantics.

### 7.2 Legacy W33 fixture

The existing RC remains useful as:
- benchmark for intake/Screening/Evidence/Selection/Architecture differences;
- immutable Raw/provenance source when independently revalidated;
- regression/comparison PDF;
- evidence for compatibility design if a repeated need emerges.

But:
- automatic migration is not required;
- artifact reuse is not required;
- proving compatibility-boundary reuse is not a W33 acceptance criterion;
- the implementation must not become more complex merely to preserve old intermediate work.

The disposition document therefore describes **safe choices if reuse is attempted**, not mandatory actions every W33 run must perform.

## 8. Phase 2C — edition-depth audit contract

WU-003C must inspect all 15 frozen Specials beyond a release-manifest row.

For every edition, inspect at minimum:
- final `pipeline-state.json` / lifecycle and Human Gate provenance;
- approved Architecture identity and role when available;
- final validated source revision and revision lineage signals;
- review/repair records referenced by the final state;
- explicit issue references where recorded;
- chronology/synthesis/layout/reference behavior relevant to that edition;
- final successful behavior that should be retained;
- failures/repair interactions that should become invariant/regression evidence;
- behavior that is merely legacy variance.

The audit may use representative records rather than rereading every historical intermediate file, but no edition may be represented only by page count/source version/general format assumptions.

Exit condition:
- every edition has explicit evidence references for its row;
- major final-state repair lineage is not silently omitted;
- positive and negative knowledge is both recorded;
- cross-edition pattern claims cite more than one supporting edition when appropriate.

## 9. WU-004B — second Pilot-contract correction

WU-004B must resolve all second-audit findings before implementation.

### 9.1 Pilot rollout model

Adopt a **full production-capable candidate before first external Pilot**.

Reason:
- W33/SP001 may initially be asked to stop at Architecture Review, but the merged candidate must already contain a valid downstream Draft/Synthesis/Publication semantic path so Architecture approval does not lead into a legacy-shaped dead end;
- this keeps the separate production sessions on one coherent `main` contract throughout the edition.

Therefore WU-005–WU-011 remain pre-Pilot implementation units. `Architecture Review capable` is a minimum semantic checkpoint, not the merge/Pilot entry boundary.

### 9.2 Implementation identity

Production State / Action provenance must bind both semantic contracts and the executable implementation basis.

Minimum target:

```yaml
contract:
  pipeline_contract_version:
  pipeline_contract_sha256:
  quality_contract_version:
  quality_contract_sha256:
  research_profile_version:
  research_profile_sha256:
  publication_profile_version:
  publication_profile_sha256:
implementation:
  repository_commit_sha:
  orchestrator_version:
```

Per-action results may add handler/module identity where useful. A contract SHA alone must not imply executable equivalence.

### 9.3 Finding taxonomy

Use orthogonal axes instead of mixing ownership and required action:

```yaml
classification:
  scope: EDITION_LOCAL | WEEKLY_PROFILE | PERIOD_PROFILE | THEMATIC_PROFILE | CORE | PUBLICATION_PROFILE | QUALITY_CONTRACT | SERIES_LAYER | UNCLASSIFIED
  defect_kind: CORRECTNESS | TRACEABILITY | COVERAGE | EDITORIAL | PUBLICATION | ORCHESTRATION | COMPATIBILITY | OTHER
  confidence: low | medium | high
requires_regression: true | false
```

`REGRESSION_REQUIRED` is therefore not a scope value.

### 9.4 Thematic closure evidence

Profile Completeness must retain explicit closure evidence. A thematic research pass may close when, at minimum:
- required named obligations have a disposition;
- no material branch/transition obligation remains `NEEDS_RESEARCH`;
- a targeted gap-fill pass has been performed for residual uncertainty;
- the latest expansion pass produced no new **material** branch/transition, or any new branch is explicitly classified non-material/out-of-scope/limitation;
- unresolved limitations remain explicit.

No fixed source count or citation depth proves completeness.

### 9.5 Optional W33 reuse ownership

If legacy W33 reuse is attempted:
- Raw/provenance import/revalidation belongs with WU-006 discovery/Screening inputs;
- factual Evidence revalidation belongs with WU-007;
- semantic comparison/disposition records belong with WU-008 or Pilot reporting;
- no WU may make reuse mandatory.

## 10. Live-document authority

During the correction period:

- `docs/survey-production-core-v2-component-inventory-audit-amendment.md` controls over the original component inventory where they conflict;
- `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` and the forthcoming second-audit amendment control over the original vertical-slice document where they conflict;
- base documents must be relabeled `SUPERSEDED IN PART` in the live tree so a continuation session cannot mistake them for unqualified canonical implementation contracts;
- after Pilot stabilization, consolidate rather than accumulate permanent amendment chains.

## 11. Resume rule

A continuation session must read current `main`, the improvement plan, this log, and the authoritative audit amendments; verify the active/next unit against repository reality; and continue from repository-recorded state. If the log and repository disagree, repository reality wins and this file must be corrected first.

**Next action: complete WU-003C and WU-004B. Do not begin WU-005 until both are formally closed and re-audited.**
