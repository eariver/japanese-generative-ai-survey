# Survey Production Core v2 — Minimum W33 / SP001 Vertical Slice

Status: `PHASE 3 DESIGN / implementation contract`  
Established: 2026-08-22 JST  
Improvement branch: `refactor/survey-production-core-v2`  
Inspected `main`: `2086b396d2f30103d9292b722891be436cd28db5`

## 1. Objective

This document defines the smallest coherent implementation slice that should be merged to `main` before separate W33 and SP001 production sessions begin.

The slice must prove that one production architecture can support:

- a rolling Weekly issue;
- a cross-temporal Thematic Special;
- shared provenance / Screening / Evidence / Selection / Architecture mechanics;
- profile-specific relevance and completeness semantics;
- the normalized two-Human-Gate model;
- end-to-end materiality traceability;
- autonomous progression toward a requested Human Gate.

It is deliberately **not** a complete removal of every legacy wrapper or repair script.

---

## 2. Key design correction discovered during Phase 3

Phase 0 correctly found that Weekly and Special already share many schemas and runners. Phase 3 inspection adds an important qualification:

> The existing shared layer is mechanically cross-edition in several places, but not yet semantically profile-neutral.

Examples:

- `screening-batch-result.schema.json` requires `why_now` and fixed topic lanes `A` through `L`;
- the Screening prompt explicitly asks for weekly `why-now` relevance;
- `evidence-card.schema.json` requires `why_now_confirmed` / `why_now_note`;
- the Evidence prompt explicitly distinguishes release date from weekly trend relevance;
- `build_candidate_matrix.py` requires an editorial window/cutoff and emits Weekly timing classes;
- `candidate-selection-decision.schema.json` is Weekly-only and hard-codes Weekly-derived editorial roles;
- Special compatibility currently widens Weekly regexes by process-local monkey-patching in some wrappers.

Therefore v2 must distinguish:

```text
shared file format
!=
shared semantic Core
```

The first vertical slice must remove enough profile pollution to make SP001 a genuine Thematic test rather than a Weekly pipeline with dates and lane fields artificially filled in.

---

## 3. Migration strategy for the first candidate

### 3.1 Do not mutate historical v1 artifacts

Existing frozen and active legacy artifacts remain readable under their current schemas.

The first v2 candidate introduces **new v2 contracts alongside v1 compatibility paths** rather than rewriting every historical file in place.

This parallelism is explicitly transitional. It does not authorize permanent `weekly-v1 + special-v1 + core-v2` duplication.

### 3.2 Reuse proven primitives below the semantic boundary

Continue to reuse where safe:

- Raw collector provenance;
- hash/digest utilities;
- source normalization;
- complete-one-decision-per-input checks;
- Evidence source-reference validation concepts;
- stable Event IDs;
- Draft Package / structured Article Draft concepts;
- bibliography and exact-byte publication primitives.

### 3.3 Add v2 semantic contracts above those primitives

The first v2 path introduces:

1. Edition/Profile Descriptor;
2. v2 Production State;
3. profile-neutral Screening decision contract;
4. profile-neutral factual Evidence contract or compatibility adapter with authoritative Profile View;
5. Edition Evidence View / Profile Relevance record;
6. Materiality Ledger;
7. Profile Completeness Result;
8. profile-aware Candidate Matrix;
9. profile-aware internal Selection record;
10. Architecture Review Summary;
11. orchestration planner / `advance-to-gate` decision engine;
12. contract identity/hash binding.

---

## 4. Canonical v2 Edition/Profile Descriptor

Proposed path per edition:

```text
sources/<issue-id>/production-profile.json
```

Schema:

```text
schemas/survey-production-profile.schema.json
```

Required concepts:

```yaml
schema_version: "2.0-rc1"
issue_id: ...
research_profile: WEEKLY | RETROSPECTIVE_PERIOD | THEMATIC
publication_profile: WEEKLY_MAGAZINE | LONGFORM_SPECIAL
research_scope:
  question: ...
  inclusion: []
  exclusion: []
  scope_dimensions: []
  temporal_policy:
    mode: ROLLING_WINDOW | BOUNDED_PERIOD | OPEN_HISTORY_AS_OF | CURRENT_STATE_AS_OF
    ...mode-specific fields...
paths:
  source_root: ...
  survey_root: ...
  work_branch: ...
editorial_roles:
  allowed: []
profile_contract:
  version: ...
  sha256: ...
publication_contract:
  version: ...
  sha256: ...
```

### Weekly descriptor

The Weekly resolver derives the rolling cutoff/window from the existing tested calendar logic and materializes it into the descriptor.

Weekly-only scope dimensions may include current technical lanes/carry-over obligations.

### Thematic descriptor

SP001 uses `THEMATIC + OPEN_HISTORY_AS_OF` or `CURRENT_STATE_AS_OF` depending on the final research framing fixed at initialization.

For TS/SP001 (Chinese Generative AI rise), descriptor-level scope can name dimensions such as:

- major model families/ecosystems;
- model/weights/inference/developer-distribution layers;
- reasoning/coding/long-context/agentic development where material;
- Open Weight distinction/licensing boundaries;
- competing/parallel strategies;
- explicit out-of-scope policy/geopolitical material except where technically necessary.

These are data in the descriptor, not hard-coded `if SP001` logic.

---

## 5. v2 Production State

Proposed path:

```text
sources/<issue-id>/production-state.json
```

The first candidate uses a v2 sibling state rather than rewriting legacy `pipeline-state.json` in place.

Rationale:

- existing v1 schemas use `additionalProperties: false` and encode incompatible Weekly/Special automation fields;
- Thematic open-history state cannot honestly populate bounded `collection_window_start/end` merely to satisfy v1;
- historical/legacy tooling must remain readable during Pilot development;
- v2 state should not inherit misleading v1 Human Gate semantics.

This is transitional dual-format support, **not dual authority**.

For an edition initialized under v2:

> `production-state.json` is the v2 state authority. A v1 `pipeline-state.json` exists only if a compatibility adapter for a reused primitive requires it, and such a view is derived/non-authoritative.

Schema:

```text
schemas/survey-production-state.schema.json
```

Required common fields:

- `schema_version`;
- `issue_id`;
- `research_profile`;
- `publication_profile`;
- `lifecycle_state`;
- machine checkpoints;
- Human Gate state;
- requested `target_gate`;
- `next_action`;
- `terminal_reason`;
- `exception_gate`;
- profile/state references;
- contract identity;
- provenance.

The existing coarse lifecycle is retained.

Human Gate state must encode:

```text
architecture_review: pending | approved | rejected
publication_preview: pending | approved | rejected
```

Candidate Selection is not a Human Gate field.

---

## 6. Contract identity

Introduce one repository contract manifest, for example:

```text
config/survey-production-v2.json
```

It identifies:

- pipeline contract version;
- quality contract version;
- profile contract documents/files;
- publication profile documents/files;
- schema versions.

Initialization computes/records SHA-256 of the exact relevant contract files in the production descriptor/state.

First candidate version:

```text
2.0-rc1
```

No public PDF branding is required.

---

## 7. Screening v2

### 7.1 Problem with v1

The v1 Screening result mixes generic triage with Weekly relevance:

- `why_now`;
- fixed A–L topic lanes.

That is not a valid universal Screening ontology.

### 7.2 v2 separation

Screening v2 remains generic triage.

Per input it records:

```yaml
screening_id:
decision: KEEP | MAYBE | DROP | INSPECT
reason:
scope_tags: []
duplicate_group:
verification_targets: []
confidence: low | medium | high
```

No `why_now` is required by Core.

`scope_tags` are unconstrained stable strings supplied by the Profile/Screening task context rather than A–L constants.

Weekly `why this issue` is later Profile relevance data.

### 7.3 Prompt contract

Add a profile-neutral Screening prompt that receives the Edition/Profile Descriptor or a bounded screening-context projection.

The prompt evaluates:

- technical relevance to the supplied research question/scope;
- whether more inspection is required;
- duplicate/series hints;
- verification targets.

It does not invent one universal set of technical lanes.

### 7.4 Compatibility

v1 Screening remains accepted for legacy production/replay.

A v2 issue uses v2 Screening as authoritative input to subsequent v2 stages.

---

## 8. Evidence v2 and Edition Evidence View

### 8.1 Desired long-term boundary

Factual Evidence should not own edition-specific editorial significance.

Target:

```text
Evidence Card
  = factual/source/temporal/claim/metric/limitation verification

Edition Evidence View
  = relevance/materiality/profile interpretation
```

### 8.2 First candidate implementation

The first candidate should introduce a profile-neutral v2 Evidence Card if implementation cost remains bounded. It should remove required Weekly fields:

- `why_now_confirmed`;
- `why_now_note`;
- final editorial recommendation.

Evidence readiness can remain factual:

```text
VERIFIED | PARTIAL | REJECTED | NEEDS_MORE
```

If a full Evidence v2 rewrite would unnecessarily duplicate mature validators, a temporary adapter may consume a v1 Evidence Card as factual input **only when**:

- Weekly editorial fields are explicitly non-authoritative for non-Weekly Profiles;
- Edition Evidence View is the sole v2 authority for relevance/materiality;
- the Evidence prompt used for Thematic production does not bias research around weekly `why_now`.

The preferred Phase 3 implementation is the clean v2 factual schema; compatibility adapter is fallback, not target.

### 8.3 Edition Evidence View

Schema:

```text
schemas/edition-evidence-view.schema.json
```

One record per Evidence Task / resolved Evidence unit:

```yaml
issue_id:
evidence_task_id:
evidence_sha256:
materiality:
  status: MATERIAL | CONTEXT | NON_MATERIAL | HOLD
  rationale: ...
scope_dimensions: []
profile_annotations: {...}
```

Profile annotations are validated by profile-specific logic.

Weekly annotations may include:

- `why_this_issue`;
- relation to rolling window/carry-over;
- Late Breaking/watchlist suitability.

Thematic annotations may include:

- lineage role: `CORE | BRIDGE | CONTEXT | PARALLEL | COMPETING | COUNTEREXAMPLE`;
- branch/transition identifiers;
- inheritance/abandonment relevance;
- historical-attribution caveats.

These are research roles, not publication placement roles.

---

## 9. Materiality Ledger

Proposed path:

```text
sources/<issue-id>/materiality/materiality-ledger.json
```

Schema:

```text
schemas/materiality-ledger.schema.json
```

The ledger should be **derived and validated**, not manually maintained as a second narrative database.

### 9.1 Row identity

Primary discovery row key:

```text
screening_id
```

Each row records:

- intake origin (`BASE`, `SUPPLEMENTAL`, `REFERENCE_EXPANSION`, `CARRY_OVER`, etc.);
- Screening disposition;
- duplicate/lifecycle target if any;
- Evidence Task IDs;
- Edition Evidence View materiality;
- Selection disposition/role where applicable;
- Architecture package/surface placement;
- final reader-facing surface or explicit omission rationale;
- unresolved/HOLD status.

Multiple Screening records may converge on one Evidence Task.

### 9.2 Validation

Hard failures include:

- accepted discovery with no Screening disposition;
- material discovery with neither Evidence/duplicate/HOLD/explicit exclusion;
- material Evidence absent from Selection disposition;
- selected material absent from Architecture or explicit exclusion;
- Architecture-required Evidence absent from Draft/chronology/synthesis or explicit reader-facing omission rationale.

The first Pilot need only enforce transitions available up to its requested Human Gate. The ledger evolves monotonically as later stages become available.

---

## 10. Profile Completeness Result

Proposed path:

```text
sources/<issue-id>/completeness/profile-completeness.json
```

Schema:

```text
schemas/profile-completeness-result.schema.json
```

Structure:

```yaml
issue_id:
research_profile:
basis:
  production_profile_sha256:
  materiality_ledger_sha256:
overall_status: READY | INCOMPLETE
obligations:
  - obligation_id:
    dimension:
    description:
    status: SATISFIED | LIMITATION | NEEDS_RESEARCH | NOT_APPLICABLE
    screening_ids: []
    evidence_task_ids: []
    rationale:
residual_limitations: []
```

No fixed minimum item count is used.

### Weekly completeness

Profile generator/checker considers:

- current editorial window;
- carry-over obligations;
- configured technical discovery lanes where still useful;
- unresolved material post-cutoff/current items.

### Thematic completeness

Profile generator/checker considers research-question obligations such as:

- named/required major branches or ecosystems;
- transition coverage;
- primary/canonical sources;
- competing/parallel approaches;
- material counterexamples;
- unresolved lineage questions.

SP001 may have descriptor-provided initial obligations, but the mechanism must accept discovered obligations without code changes.

---

## 11. Candidate Matrix v2

The current matrix is Weekly-specific because it requires a rolling window and `why_now`.

Add a profile-aware matrix builder whose common rows contain:

- Evidence Task ID;
- artifact/source identity;
- factual Evidence status;
- materiality/profile relevance status;
- source/evidence depth;
- unresolved questions/contradictions/limitations;
- profile-provided comparison annotations.

### Weekly timing adapter

May reuse current timing relation logic:

- `MAIN_EVENT`;
- `PRE_WINDOW_RELEVANCE`;
- `POST_CUTOFF`;
- etc.

### Thematic adapter

Does not fabricate a window relation.

It may expose:

- event date(s);
- lineage/branch annotations;
- research-role/materiality status;
- unresolved historical significance.

The Core matrix remains non-ranking.

---

## 12. Internal Selection v2

Add a generic selection record distinct from Human approval.

Proposed schema:

```text
schemas/survey-selection.schema.json
```

Required concepts:

```yaml
issue_id:
research_profile:
status: COMPLETE
basis:
  candidate_matrix_sha256:
  materiality_ledger_sha256:
assignments:
  - evidence_task_id:
    publication_role:
    rationale:
provenance:
```

No `approved_by` Human field is required.

Profile validator supplies the allowed publication-role set.

Common dispositions such as `HOLD_OUT` / `EXCLUDE` may remain widely available, but Weekly-only roles such as `LATE_BREAKING` are not Core enum constants.

Architecture Review approval later binds the exact Selection record SHA together with Architecture and review summary.

---

## 13. Architecture Review Summary

Proposed path:

```text
sources/<issue-id>/architecture/architecture-review-summary.json
sources/<issue-id>/architecture/architecture-review-summary.md
```

Schema:

```text
schemas/architecture-review-summary.schema.json
```

Required exact basis hashes:

- Production Profile;
- Materiality Ledger;
- Profile Completeness Result;
- Candidate Matrix;
- internal Selection;
- Architecture proposal.

Summary includes:

- intake/source counts by origin;
- Screening dispositions;
- Evidence/materiality counts;
- holds/exclusions;
- Selection role counts;
- profile completeness obligations/status;
- major material discoveries and destinations;
- residual limitations;
- issue thesis;
- proposed package architecture/page constraints.

Architecture Review cannot be reached with `overall_status=INCOMPLETE` unless an Exception Gate explicitly records the editorial decision to proceed despite the limitation.

---

## 14. Subject/entity binding and identifier safety in the first slice

### 14.1 Identifier safety

Promote canonical URL/path/ID preservation into a generic utility/test before first Pilot.

Do not attempt to refactor every historical Special renderer first.

The v2 structured drafting/rendering path must preserve structured identifier fields byte-for-byte.

### 14.2 Entity binding

Do not port the entire half-year Technical Notes repair checker as Core.

The first candidate should instead enforce at the structured Evidence boundary that a concrete metric/attribute carries enough subject context to distinguish:

- target artifact/entity;
- comparator/related entity where applicable.

If extending the existing Evidence schema directly is too disruptive, add a v2 bound-fact representation used by Edition Evidence View / drafting.

Historical Mistral/Jamba/Ministral cases become generic fixtures.

The goal is to prevent wrong attribution before reader-facing Technical Notes are generated, not detect it only after final TeX exists.

---

## 15. Orchestration / `advance-to-gate`

The first candidate does not need to replace every GitHub workflow with one controller.

It must provide a deterministic planner that reads:

- Production State;
- Production Profile;
- presence/validity of stage artifacts;
- requested target Human Gate.

It returns:

```yaml
current_stage:
next_action:
action_kind: LOCAL_SCRIPT | WORKFLOW | HUMAN_GATE | COMPLETE | EXCEPTION
required_inputs: []
terminal_reason: null | HUMAN_GATE_REACHED | EXCEPTION_GATE_REQUIRED | COMPLETE
```

A CLI such as:

```text
python scripts/survey_production.py advance-to-gate --issue-id ...
```

may initially output/validate the next action rather than dispatch every GitHub workflow automatically.

This is sufficient for Pilot liveness if the production session can repeatedly invoke deterministic next actions without rediscovering pipeline logic from chat.

Later consolidation may add workflow dispatch adapters.

---

## 16. W33 initialization under v2

W33 is treated as a fresh v2 production validation.

Rules:

- current `main` determines the W33 production profile/window;
- v2 initialization does not import legacy W33 lifecycle state by default;
- legacy `weekly/2026-W33-work` artifacts may be inspected/comparison-tested separately;
- any reused Raw/Evidence artifact must pass v2 provenance and semantic-contract validation independently;
- easiest safe implementation is to initialize a clean v2 W33 work state/path/branch strategy rather than infer migration equivalence.

The exact branch naming must avoid accidentally overwriting the legacy W33 branch. Phase 3 implementation should choose a deterministic v2 work branch, for example:

```text
weekly/2026-W33-v2-work
```

or another explicitly documented temporary Pilot name.

After Pilot stabilization, normal Weekly may return to the canonical `weekly/<issue>-work` naming convention.

This temporary branch naming is a production-safety measure, not public issue identity.

---

## 17. SP001 initialization under v2

SP001 is the first true Thematic production validation.

Before source collection it requires:

- selected backlog item / stable slug;
- Production Profile with Thematic research question, inclusion/exclusion, scope dimensions, and temporal mode;
- long-form Publication Profile;
- profile completeness initial obligations;
- source-intake plan capable of base discovery plus citation/reference expansion and supplemental gap fill.

No synthetic `coverage.start` date should be added merely to satisfy old Special schema.

SP001 may retain an `as_of` timestamp as part of `OPEN_HISTORY_AS_OF` / `CURRENT_STATE_AS_OF`.

---

## 18. What is explicitly deferred from the first vertical slice

The following are important but do not block W33/SP001 Architecture Review validation if mature current implementations can still safely handle the publication side:

- complete removal of all v1 workflow wrappers;
- retirement of all `revise_special_*` scripts;
- unified Weekly/long-form TeX template;
- shared Evidence corpus across multiple published series volumes;
- full Series Research Layer implementation;
- perfect active-legacy-state migration;
- all P1 visual-layout repair consolidation;
- elimination of every legacy public release/recovery workflow.

These remain Phase 5/7 consolidation work unless Pilot findings promote them.

---

## 19. Implementation work units

### WU-005 — Foundation contracts and resolver

Implement:

- v2 contract manifest;
- Production Profile schema/resolver;
- Production State schema/initializer;
- Weekly and Thematic profile validation;
- temporal-policy validation;
- contract SHA binding;
- tests.

Exit: W33 and a synthetic SP001 descriptor initialize without any bounded-window fiction for Thematic.

### WU-006 — Profile-neutral Screening / Evidence relevance boundary

Implement:

- Screening v2 schema/prompt/package path;
- Edition Evidence View;
- remove weekly semantic authority from Thematic path;
- compatibility adapters only where necessary;
- tests showing Weekly and Thematic can use different profile relevance without schema monkey-patching.

Exit: same raw-discovery shape can flow to profile-neutral triage and profile-specific materiality.

### WU-007 — Materiality / completeness

Implement:

- Materiality Ledger schema/builder/validator;
- Profile Completeness schema/validator;
- Weekly and Thematic initial completeness adapters;
- silent-drop regression fixtures.

Exit: Issue #166 regression is mechanically impossible at the covered stages without validation failure.

### WU-008 — Candidate Matrix / internal Selection / Architecture Review Summary

Implement:

- profile-aware matrix;
- internal Selection v2;
- Architecture Review Summary;
- bind exact hashes;
- Architecture Review readiness validator.

Exit: W33 and SP001 can reach Human Gate 1 under one Core contract with different Profile semantics.

### WU-009 — Orchestration and bootstrap

Implement:

- `survey_production.py` planner / `advance-to-gate`;
- target-gate/next-action/terminal-reason state;
- generic bootstrap/session docs;
- W33/SP001 Pilot startup instructions;
- required workflow/control integration for safe Pilot execution.

Exit: another session can start either Pilot from current `main` and advance without chat-history knowledge.

### WU-010 — P0 quality promotion and integration regression

Implement/verify:

- identifier-preservation generic guard;
- subject/entity binding at structured evidence/draft boundary;
- reader/internal prose guard;
- exact PDF approval/freeze/release integration remains intact;
- frozen historical fixtures untouched;
- full v2 contract suite.

Exit: candidate is merge-ready for external W33/SP001 validation.

Work units may be merged/split if implementation reality demands it, but the semantic exit criteria must remain traceable in the work log.

---

## 20. Pilot acceptance criteria

### W33 Architecture Review

Must demonstrate:

- correct Weekly rolling window;
- profile-specific current relevance/carry-over semantics;
- broad intake plus explicit completeness status;
- no silent material drop to Selection/Architecture;
- no standalone Candidate Selection Human Gate;
- Architecture Review Summary exposes compression/limitations;
- legacy W33 state migration was not required.

### SP001 Architecture Review

Must demonstrate:

- no fake bounded historical coverage requirement;
- explicit thematic question/inclusion/exclusion;
- lineage/ecosystem/competing-approach completeness obligations;
- materiality linked to thematic relevance, not Weekly `why_now`;
- common Core Evidence/Selection/Architecture traceability;
- same Human Gate mechanics as W33.

### Publication path later in each Pilot

Must preserve:

- structured drafting/evidence boundaries;
- reader/internal prose separation;
- exact Publication Preview PDF bytes;
- deterministic Visual Review/Freeze/Release authority;
- Publication Profile-specific layout quality.

---

## 21. WU-004 exit decision

The design is sufficiently bounded for implementation when:

- the profile pollution in v1 shared schemas is explicitly addressed rather than hidden;
- v2 state/profile authority is unambiguous;
- Materiality/Completeness/Architecture Review artifacts have defined responsibilities;
- W33 does not depend on legacy-state migration;
- SP001 does not depend on bounded-window fiction;
- implementation is divided into reviewable vertical work units;
- existing mature primitives are reused below their valid semantic boundary;
- deferred cleanup is clearly separated from Pilot-critical work.

The next unit is **WU-005 — Foundation contracts and resolver**.
