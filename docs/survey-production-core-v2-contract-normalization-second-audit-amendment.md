# Survey Production Core v2 — Contract Normalization Second-Audit Amendment

Status: `PHASE 1 AMENDMENT / authoritative where conflicting`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Base contract map: `docs/survey-production-core-v2-contract-normalization.md`

## 1. Purpose

A second pre-implementation audit found that the Phase 1 contract map remained directionally correct but left three implementation-critical points underspecified:

1. semantic contract hashes do not bind the executable implementation;
2. Pilot Finding classification mixed ownership with regression action in different documents;
3. Pilot entry timing was ambiguous between Architecture-only capability and a fully coherent downstream path.

This amendment resolves those points before WU-005 begins.

Where this document conflicts with the base contract normalization, this amendment controls.

## 2. Contract identity is necessary but not sufficient

The existing target fields remain mandatory:

```yaml
contract:
  pipeline_contract_version:
  pipeline_contract_sha256:
  quality_contract_version:
  quality_contract_sha256:
  research_profile:
  research_profile_version:
  research_profile_sha256:
  publication_profile:
  publication_profile_version:
  publication_profile_sha256:
```

However, two runs can use identical contract files while different executable code produces different behavior.

Historical Special build states already preserve `control_commit_sha` and style SHA. v2 generalizes that provenance principle.

### New invariant C-25 — executable implementation identity is explicit

Owner: `CORE`

Every authoritative v2 Production State records at minimum:

```yaml
implementation:
  repository_commit_sha: <40-hex commit>
  orchestrator_version: <stable identifier>
```

Every material deterministic/model-assisted action records or inherits enough information to determine which repository implementation executed it.

An Action Result may additionally record:

```yaml
handler:
  name:
  module_or_workflow:
  version_or_sha:
```

Rules:
- contract SHA proves semantic policy identity;
- repository/control identity proves implementation basis;
- artifact SHA proves exact input/output identity;
- none substitutes for the others.

A state transition must not claim equivalence merely because contract files are unchanged when implementation commit changed.

## 3. Finding classification is orthogonal

The program previously used both:

```text
CORE_DEFECT
WEEKLY_PROFILE_DEFECT
REGRESSION_REQUIRED
```

and a separate `classification.scope` model.

These mix different dimensions. v2 adopts orthogonal fields.

### New invariant C-26 — Finding scope is not repair action

Machine-readable Finding records use:

```yaml
classification:
  scope: EDITION_LOCAL | WEEKLY_PROFILE | PERIOD_PROFILE | THEMATIC_PROFILE | CORE | PUBLICATION_PROFILE | QUALITY_CONTRACT | SERIES_LAYER | UNCLASSIFIED
  defect_kind: CORRECTNESS | TRACEABILITY | COVERAGE | EDITORIAL | PUBLICATION | ORCHESTRATION | COMPATIBILITY | OTHER
  confidence: low | medium | high
requires_regression: true | false
```

Optional fields may add severity/priority, but:
- `REGRESSION_REQUIRED` is not a scope;
- a `CORE` finding does not automatically mean a generic repair is already known;
- an edition-local workaround does not determine final scope;
- regression need is an independent decision.

Repair Set records group Findings and state which layer is actually changed.

## 4. Pilot entry uses one coherent merged contract

The base plan says the minimum semantic test is reaching Architecture Review. The corrected vertical-slice plan also covers Draft/Synthesis/Publication to avoid a dead end.

These are reconciled as follows.

### New invariant C-27 — first external Pilot starts only after a full production-capable candidate is merged

Before W33/SP001 external production sessions begin, `main` must contain a coherent v2 path through:

```text
Discovery
-> Screening
-> Evidence/View
-> Materiality/Completeness
-> Matrix/Selection
-> Architecture Review
-> Draft/Synthesis
-> semantic/publication validation
-> Publication Preview
-> Freeze/Release authorization path
```

The production session may be instructed initially to stop at Architecture Review. That is a **requested gate target**, not a reason to merge an Architecture-only implementation.

Reason:
- Architecture approval must not strand the same edition on legacy-shaped downstream contracts;
- the same current `main` contract should remain valid when the user continues from Human Gate 1 to Human Gate 2;
- W33 and SP001 remain real production validations rather than isolated schema demos.

## 5. W33 compatibility is explicitly non-normative

### New invariant C-28 — legacy artifact reuse is optional optimization

The W33 Pilot is not required to exercise legacy migration or artifact reuse.

The existing legacy RC:
- remains immutable benchmark/provenance evidence;
- may provide independently revalidated Raw/factual inputs;
- may be compared against v2 results;
- does not alter W33 pass/fail criteria.

No Core implementation feature may be justified solely by a desire to preserve one legacy intermediate artifact unless the feature has independent generic value.

## 6. Thematic completeness requires closure evidence

Thematic research expansion creates obligations dynamically. A recursively expanding obligation list is not itself a stop condition.

### New invariant C-29 — Thematic completeness records saturation/closure evidence

A Thematic Profile may report research completeness only when:

1. all required named obligations have explicit status;
2. no material branch/transition remains `NEEDS_RESEARCH`;
3. targeted residual gap-fill has been performed where uncertainty remained;
4. the latest expansion pass produced no new **material** branch/transition, or each newly discovered branch is explicitly disposed as non-material/out-of-scope/limitation;
5. unresolved limitations are retained explicitly.

This is a qualitative saturation condition, not a fixed source-count or citation-depth threshold.

The Completeness Result should retain at least:

```yaml
closure:
  expansion_passes:
  final_pass_new_sources:
  final_pass_new_material_obligations:
  targeted_gap_fill_completed:
  open_material_obligations:
  limitations: []
  status: COMPLETE | LIMITED | NEEDS_RESEARCH
```

Exact schema is WU-007 work.

## 7. Consequences for implementation work units

### WU-005

Must include:
- contract identity;
- implementation `repository_commit_sha` / orchestrator identity;
- authoritative state transition basis validation.

### WU-006

Owns optional legacy Raw/provenance reuse if any is implemented. W33-specific import is not required.

### WU-007

Owns optional factual Evidence revalidation if any is implemented and Thematic closure-result semantics.

### WU-008

Owns fresh Matrix/Selection/Architecture and optional legacy-v2 semantic comparison reporting, not Raw/Evidence migration.

### WU-010

Finding schema must use the orthogonal taxonomy in this amendment.

### WU-011

External Pilot bootstrap is permitted only after the coherent full path is validated and merged to `main`.

## 8. Exit decision

Phase 1 contract normalization remains valid after this amendment and is considered complete for implementation planning when this amendment is committed.

The target contract now binds:
- semantic policy identity;
- executable implementation identity;
- exact artifact identity;
- orthogonal Finding classification;
- one coherent pre-Pilot production path;
- optional, non-normative W33 legacy reuse;
- explicit Thematic closure evidence.
