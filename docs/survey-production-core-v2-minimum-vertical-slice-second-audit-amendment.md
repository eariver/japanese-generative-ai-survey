# Survey Production Core v2 — Minimum Vertical Slice Second-Audit Amendment

Status: `PHASE 3 SECOND CORRECTION / authoritative implementation amendment`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Base design: `docs/survey-production-core-v2-minimum-vertical-slice.md`  
First amendment: `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md`  
Companions:
- `docs/survey-production-core-v2-historical-production-deep-audit.md`
- `docs/survey-production-core-v2-contract-normalization-second-audit-amendment.md`
- `docs/survey-production-core-v2-w33-artifact-disposition.md`

## 1. Authority

This second amendment controls over both the base vertical-slice document and the first audit amendment where they conflict.

The first amendment remains valid for:
- profile-pollution correction through Draft/Synthesis;
- Thematic Research Expansion;
- Materiality/Completeness;
- Review Finding/Repair Set;
- one-way state compatibility;
- executable `advance-to-gate`.

This amendment corrects rollout semantics, provenance identity, Finding taxonomy, Thematic closure evidence, and W33 optional-reuse ownership.

## 2. W33 primary role

W33 is:

> **Weekly Profile First Production Validation**

The existing legacy RC is an optional comparison/provenance fixture.

Therefore W33 acceptance does **not** require:
- importing legacy state;
- reusing legacy Raw;
- revalidating legacy Evidence;
- proving an artifact compatibility matrix;
- preserving legacy Selection/Architecture;
- matching the legacy PDF.

If an existing immutable input is convenient and independently valid, v2 may reuse it. If clean regeneration is simpler, regenerate it.

The supporting policy `docs/survey-production-core-v2-w33-artifact-disposition.md` defines safe choices only when reuse is attempted.

## 3. Pilot entry boundary

The first external W33/SP001 sessions begin only after a **full production-capable v2 candidate** has been reviewed and merged to `main`.

The candidate must have a coherent semantic path through:

```text
Profile / State
-> Research Discovery / Expansion
-> Raw provenance
-> Screening
-> Factual Evidence
-> Edition Evidence View
-> Materiality
-> Completeness
-> Matrix
-> internal Selection
-> Architecture
-> Architecture Review
-> Draft Package / Draft Result
-> Profile Synthesis
-> semantic/publication validation
-> Publication Preview
-> exact-byte Visual Review/Freeze/Release path
```

A production session may still be requested to stop at Architecture Review. That is the requested terminal Human Gate for that session, not the implementation boundary merged to `main`.

This eliminates the ambiguity between:
- “Architecture Review capable” as a minimum semantic milestone; and
- “safe to start a real Pilot edition” as the rollout criterion.

## 4. Revised implementation sequence

```text
WU-005 Foundation contracts/state/implementation identity
  ↓
WU-006 Research expansion + Screening
  ↓
WU-007 Factual Evidence + Edition View + Materiality + Completeness
  ↓
WU-008 Matrix + internal Selection + Architecture
  ↓
WU-009 Drafting + Profile Synthesis
  ↓
WU-010 executable orchestration + Finding/Repair Set
  ↓
WU-011 P0 quality + full Pilot bootstrap
  ↓
review / merge coherent candidate to main
  ↓
separate W33 + SP001 production sessions
```

No external Pilot starts after WU-008 merely because Human Gate 1 can be rendered.

## 5. WU-005 correction — implementation identity

WU-005 must bind both semantic contract and executable basis.

Minimum Production State concepts:

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

Action/result provenance may add exact handler/workflow/module identity.

Validation principle:

```text
contract SHA = policy identity
implementation commit = executable identity
artifact SHA = byte identity
```

A change in one cannot be hidden by stability in another.

## 6. W33 optional-reuse work ownership

If the Pilot chooses to reuse legacy artifacts:

### WU-006
May support:
- Raw hash/path validation;
- collector provenance import/reference;
- carry-over/current-context input revalidation.

### WU-007
May support:
- factual Evidence revalidation;
- subject/entity/identifier validation;
- fresh Edition Evidence View.

### WU-008
May support:
- legacy-v2 semantic comparison records;
- fresh Matrix/Selection/Architecture only.

Rules:
- none of these compatibility features is mandatory;
- no WU contains `if W33` production semantics when a generic input/import mechanism is not otherwise useful;
- legacy `pipeline-state.json` never becomes v2 authority.

## 7. Thematic Research Expansion closure

The first amendment correctly added research expansion but its closure rule was still too recursive.

Thematic Completeness must record saturation evidence.

A result can be `COMPLETE` or `LIMITED` only when:

1. profile-required named obligations have explicit dispositions;
2. no material branch/transition obligation remains `NEEDS_RESEARCH`;
3. targeted residual gap-fill has been performed;
4. the latest expansion pass introduces zero new material obligations, or every new obligation from that pass is explicitly disposed as non-material/out-of-scope/limitation;
5. unresolved limitations remain visible.

Suggested result surface:

```yaml
closure:
  expansion_passes: <int>
  final_pass_new_sources: <int>
  final_pass_new_material_obligations: <int>
  targeted_gap_fill_completed: true | false
  open_material_obligations: <int>
  limitations: []
  status: COMPLETE | LIMITED | NEEDS_RESEARCH
```

Do not use a universal source-count threshold.

## 8. Finding / Repair Set taxonomy

WU-010 must use one normalized Finding model.

```yaml
classification:
  scope: EDITION_LOCAL | WEEKLY_PROFILE | PERIOD_PROFILE | THEMATIC_PROFILE | CORE | PUBLICATION_PROFILE | QUALITY_CONTRACT | SERIES_LAYER | UNCLASSIFIED
  defect_kind: CORRECTNESS | TRACEABILITY | COVERAGE | EDITORIAL | PUBLICATION | ORCHESTRATION | COMPATIBILITY | OTHER
  confidence: low | medium | high
requires_regression: true | false
```

This replaces mixed vocabulary such as `CORE_DEFECT` vs `CORE`, or treating `REGRESSION_REQUIRED` as an ownership class.

A Repair Set separately records:
- Findings addressed;
- actual layer changed;
- generic/profile/local disposition;
- implementation commits;
- regression fixtures;
- verification editions.

## 9. Additional Phase 2C-derived P0/P1 requirements

The deep historical audit strengthens these requirements:

### 9.1 Derived reader scope identity

M06 proved that copied reader labels can leak another edition's month.

Production Profile/State should be the authority for reader-facing period/profile identity. Validation should detect inconsistent month/year/window labels where feasible.

Ownership: `CORE structured identity + PUBLICATION_PROFILE rendering`.

### 9.2 Coupled long-form regression family

2022-Y and 2024-H1 show that the following interact:
- subject/entity/property binding;
- identifier preservation;
- source-specific fail-closed notes;
- bibliography metadata;
- chronology-source mapping;
- empty-wrapper suppression;
- TOC hierarchy;
- Technical Notes tails / Needspace;
- required synthesis survival.

WU-011 must treat these as a regression family. A local repair cannot be considered stable by testing only its symptom.

### 9.3 Post-transformation revalidation

2020-Y, 2024-H1 and 2023-Y demonstrate that an old defect can return after source enrichment, compaction, or later repair.

Quality checks must be rerunnable after material transformations, especially before Publication Preview.

## 10. Architecture Review remains the first Human Gate

The full pre-Pilot implementation requirement does not change normal interaction.

External W33/SP001 sessions still follow:

```text
start
-> autonomous deterministic/model-assisted work
-> HUMAN GATE 1 Architecture Review
-> continue when approved
-> autonomous downstream work
-> HUMAN GATE 2 Publication Preview
-> deterministic Freeze/Release for approved bytes
```

Candidate Selection remains internal.

## 11. Second-audit acceptance criteria

Before WU-005 begins:

- [x] W33 restored to Weekly Profile First Production Validation.
- [x] Legacy W33 reuse made optional, not an acceptance criterion.
- [x] 15 Special editions re-audited at final-state production-lineage depth.
- [x] implementation identity added to the target contract.
- [x] Finding taxonomy normalized into orthogonal axes.
- [x] Thematic closure/saturation evidence defined.
- [x] optional W33 reuse assigned to the correct stage ownership.
- [x] Pilot entry boundary fixed as full production-capable candidate merged to `main`.
- [x] coupled long-form regression and post-transformation revalidation added from Phase 2C.

## 12. Exit decision

With this amendment, the implementation plan no longer treats W33 migration/compatibility as a required validation goal and no longer allows an Architecture-only candidate to start real Pilot production.

WU-004B may close after the live-document authority index and worklog are updated to point to this amendment.
