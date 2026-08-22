# Survey Production Core v2 — WU-008 / Whole-System Audit

Status: `ACTIVE AUDIT / remediation in progress`  
Audit date: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft PR: `#310`  
Pre-audit WU-008 head: `a2f723eea4d22ff14d43b7da7866dc5aed764ca4`  
Production `main` at audit start: `2086b396d2f30103d9292b722891be436cd28db5`

## 1. Purpose

This audit has two layers:

1. **WU-008 completion audit** — verify Candidate Matrix, internal Selection, generic Architecture, and Architecture Review Summary against the authoritative Phase 3 contracts.
2. **Whole-system audit** — re-read the implemented v2 path from WU-005 through WU-008 as one system rather than assuming green unit/workflow tests imply cross-contract correctness.

The audit intentionally distinguishes:
- a defect in already-implemented behavior;
- a Pilot-blocking capability intentionally assigned to a later work unit;
- a future/non-Pilot capability that is not yet required.

A later work unit does not excuse a defect in an earlier work unit's declared exit contract. Conversely, an unimplemented WU-009/WU-010/WU-011 responsibility is not retroactively classified as a WU-008 defect merely because the full Pilot is not yet production-capable.

## 2. Baseline verification

Before audit remediation, head `a2f723eea4d22ff14d43b7da7866dc5aed764ca4` passed all five cross-regression workflows:

- Survey Production Core v2 CI — SUCCESS;
- Evidence contract CI — SUCCESS;
- Screening contract CI — SUCCESS;
- repository-wide Pipeline contract tests — SUCCESS;
- Weekly pipeline spine — SUCCESS.

Draft PR #310 was mergeable and remained intentionally draft. Production `main` was unchanged.

Green CI is treated as necessary evidence, not sufficient audit proof.

## 3. WU-008 completion assessment

### 3.1 Satisfied

WU-008 establishes:

- Candidate Matrix derived from exact accepted Evidence, Edition Evidence View, Materiality Ledger and Profile Completeness;
- deterministic Candidate identity and no silent loss of accepted Evidence tasks before Matrix;
- one explicit Selection assignment per Matrix candidate;
- Selection dispositions `SELECTED | HOLD | REJECT | INSPECT` without Human approval fields;
- Profile/Publication-owned role namespaces rather than one global Weekly role enum;
- generic Architecture packages with primary/supporting assignment, must-cover requirements, boundaries and drafting order;
- selected PRIMARY destination exactly once, selected SUPPORTING at least once, or explicit structured selected exception;
- no generic `LATE_BREAKING`, `X_COMMUNITY`, `WATCHLIST_CHRONOLOGY`, or `this_week_summary_written_last` requirement;
- Weekly and Thematic fixtures through the same Core contract without dummy fields from the other Profile;
- Architecture Review Summary with exact basis hashes, discovery/screening/evidence/materiality/selection/completeness counts, material destinations, residual limitations, page plan, and research-expansion summary;
- WU-008 schema files included in `pipeline_contract_sha256` identity;
- regression proving Architecture schema drift invalidates initialized Production State.

### 3.2 Audit conclusion

WU-008's **pre-Human-Gate production of a reviewable Architecture proposal** satisfies its declared exit criteria.

One Gate-approval provenance issue is intentionally not counted as a failure of the pre-gate WU-008 path because execution of Human Gate state/approval belongs to WU-010. It is nevertheless a P0 requirement for WU-010 and must be resolved before the first external Pilot.

## 4. Whole-system findings

### AUD-001 — P0 / TRACEABILITY — Architecture approval must not self-mutate away from reviewed bytes

**Observed**

Current `survey_architecture_v2.py` can represent `status=APPROVED` by rewriting the same Architecture object with Human Review metadata.

**Problem**

The Human reviews a proposed Architecture/Review Summary whose SHA is known before approval. If the reviewed Architecture file is then rewritten from `PROPOSED` to `APPROVED`, the downstream Architecture SHA is different from the bytes the Human reviewed.

This violates the design principle that a Human Gate binds an exact review basis.

**Disposition**

- Scope: `CORE`
- Defect kind: `TRACEABILITY`
- Severity: `P0 before Pilot`
- Owner: **WU-010 Human Gate/orchestration**
- Required repair: an independent Architecture Approval Record (or equivalent immutable proposal binding) that records exact proposed Architecture SHA and exact Architecture Review Summary SHA. Gate state may advance only from that record. Do not rely on self-mutating approval bytes as the sole authority.
- WU-008 consequence: review-summary generation remains valid; direct `APPROVED` representation is not sufficient Gate authority.

### AUD-002 — P0 / COVERAGE — Thematic closure counters were self-reported rather than derived

**Observed**

The WU-007 base Completeness validator checked closure counters for type and internal arithmetic but did not prove that `expansion_passes`, `final_pass_new_sources`, or final-pass material-obligation counts matched Discovery provenance.

A result could therefore claim saturation counters inconsistent with the actual research graph.

**Disposition**

- Scope: `CORE`
- Defect kind: `COVERAGE`
- Severity: `P0`
- Owner: WU-007 post-audit hardening
- Status: **REPAIRED during this audit**

Repair:
- `survey_completeness_v2.py` now derives expansion-pass and final-pass counters from Discovery `research_pass` / `obligation_ids`;
- closure self-report must match the derived values;
- Completeness obligation rows now fail closed on extra/missing fields, invalid Profile dimensions, duplicate refs, unknown Discovery/Evidence refs, and missing required text;
- dedicated negative regressions added.

### AUD-003 — P1 / TRACEABILITY — Discovery expansion edges are syntactically present but not yet fully graph-resolved

**Observed**

For expansion origins, WU-006 requires non-empty `parent_refs`, but the current Discovery-set validator does not prove that every expansion parent resolves to an allowed in-run Discovery node/known external trigger, nor does the record have a first-class discovery-method/query/reference field separate from prose `reason`.

The authoritative first audit states that every non-base discovery must retain parent/trigger, discovery method/query/reference, retrieval provenance, accepted Raw identity, and downstream Screening disposition.

**Disposition**

- Scope: `CORE`
- Defect kind: `TRACEABILITY`
- Severity: `P1 now / P0 before SP001 Pilot`
- Owner: WU-006 + WU-011 bootstrap integration
- Required before Pilot:
  - define parent-reference namespaces or same-run edge resolution rules;
  - retain structured discovery method/trigger data;
  - bind accepted Raw identity structurally rather than relying only on path strings/opaque metadata;
  - add negative regression for dangling expansion edges and Raw identity drift.

This does not invalidate current Screening mechanics, but the research graph must be hardened before SP001 is authorized.

### AUD-004 — P1 / CORRECTNESS — Machine-readable schemas and hand-written validators are not uniformly equivalent

**Observed**

The repository commits strict JSON Schemas with `additionalProperties: false`, required nested fields and enum/type constraints, while runtime validators are hand-written. Some validators are exact and strong; others validate only the semantically critical subset.

Examples found during audit:
- Production Profile runtime validation does not fully mirror every schema structural restriction;
- Evidence Card semantic validation strongly checks basis/source/entity binding but does not independently mirror every nested schema constraint;
- before AUD-002 repair, Completeness obligation nested shape was more permissive than its schema.

**Risk**

A payload can be contract-schema-invalid yet pass a narrower runtime validator, undermining the meaning of including schema bytes in `pipeline_contract_sha256`.

**Disposition**

- Scope: `CORE`
- Defect kind: `CORRECTNESS`
- Severity: `P1 now / P0 before Pilot`
- Owner: WU-011 P0 quality integration, with earlier fixes when a concrete bypass is found
- Required repair: establish one fail-closed schema-conformance layer (library or maintained subset validator) and run it before semantic validators for model-produced/externally supplied artifacts. Add regression proving schema-invalid-but-semantically-plausible payloads cannot be accepted.

### AUD-005 — P1 / EDITORIAL TRACEABILITY — Architecture Review Summary should expose item-level non-selected/excluded rationale

**Observed**

The Review Summary exposes counts for Screening and Materiality plus detailed destinations for `MATERIAL`/`CONTEXT` Matrix candidates. Discovery rows dropped during Screening are preserved in the Materiality Ledger as `EXCLUDED`/`DUPLICATE`, but the Human Gate summary currently exposes those mostly as counts rather than a concise item-level exclusion/hold list.

**Risk**

Issue #166 was precisely a wide-intake compression failure. A reviewer should not need to manually open the full ledger merely to discover which potentially important intake items were excluded or held.

**Disposition**

- Scope: `CORE`
- Defect kind: `TRACEABILITY`
- Severity: `P1 before Pilot`
- Owner: WU-008 post-audit / WU-011 review-surface integration
- Required repair: add a bounded item-level Review Summary section for `DROP`, `INSPECT`, `MAYBE`, `HOLD`, `NON_MATERIAL`, `EXCLUDED`, and `DUPLICATE` dispositions with stable IDs and rationale, while keeping the full Ledger authoritative.

### AUD-006 — PLANNED, not an implemented-unit defect — Production State action/checkpoint advancement is still skeletal

`transition_state` currently establishes monotonic lifecycle mechanics and basis anti-divergence. It does not yet own the final action planner/executor semantics, checkpoint evidence application, terminal-reason computation, or Human Gate state transitions.

This is explicitly WU-010 scope. Do not treat the current skeleton as a production `advance-to-gate` implementation.

### AUD-007 — PLANNED, not a Pilot blocker at WU-008 — Retrospective Period constructor/path is not in the first vertical slice

The config/schema declare `RETROSPECTIVE_PERIOD`, but the current executable initializer focuses on W33 Weekly and SP001 Thematic validation. Period support remains a required eventual Profile capability, but absence of a Period Pilot initializer is not a failure of the W33/SP001-first WU-005–008 slice.

### AUD-008 — PASS — W33 legacy RC remains optional and non-authoritative

No W33-specific migration compatibility was introduced into WU-008. Fresh v2 Matrix/Selection/Architecture remains the canonical Pilot path; legacy W33 is only an optional comparison/provenance fixture.

## 5. Cross-cutting observations

### 5.1 Strongest current mechanics

The most mature cross-cutting properties now are:
- exact basis hashes at each semantic boundary;
- complete-only accepted result sets;
- content-addressed Screening/Evidence/View archives;
- explicit Discovery→Screening→Evidence→View→Materiality traceability;
- subject/entity role binding for comparator safety;
- internal Selection separated from Human Gate approval;
- Profile-neutral Matrix/Architecture envelope;
- deterministic regression fixtures for historical #166/#191 defect families.

### 5.2 Main residual risk before WU-009

WU-009 must not reintroduce Weekly semantics through Draft Package, Draft Result, or Profile Synthesis. The audit should be used as a negative-design checklist:
- no universal `late_breaking` field;
- no universal `this_week` synthesis payload;
- Draft must bind approved/review-authorized Architecture basis, not merely any Architecture file;
- Evidence/Matrix boundaries must survive into drafting;
- Profile extensions remain Profile-owned.

## 6. Audit gate before WU-009

Before WU-009 begins:

1. AUD-002 repair regressions must be green in dedicated Core v2 CI and all cross-regression workflows.
2. WU-008 must remain green after the WU-007 closure hardening.
3. this audit must be reflected in the work log.
4. AUD-001/AUD-003/AUD-004/AUD-005 must be carried as explicit Pilot-blocking requirements to their owner WUs rather than disappearing from chat context.
5. `main` must be rechecked for movement.

WU-009 may begin after those conditions if no new P0 defect in already-implemented WU-005–008 behavior is found.

## 7. Audit principle

> Green tests prove the tested contract. They do not prove that the contract itself contains every required invariant.

Whole-system audits therefore remain mandatory at coherent vertical-slice boundaries and before Pilot authorization.
