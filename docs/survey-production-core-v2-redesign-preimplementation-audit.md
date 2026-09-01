# Survey Production Core v2 — Redesign Pre-Implementation Audit

Status: `AUDIT COMPLETE / DESIGN REVISIONS REQUIRED BEFORE IMPLEMENTATION`  
Established: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Primary evidence: Issues #400, #433, #434; W33/SP001 execution records; existing Retrospective/Thematic/Foundations guidance

## 1. Audit question

Before implementing the post-W33/SP001 redesign, verify that the proposed direction:

1. actually addresses the failures observed in the two real production trials;
2. remains consistent with the Owner's GitHub Actions principle;
3. does not overfit the Core to `2026-W33` or `SP001`;
4. preserves or improves applicability to `RETROSPECTIVE_PERIOD`, standalone `THEMATIC`, and Generative AI Foundations guided-series work;
5. retains enough deterministic/provenance structure that moving more editorial work back to ChatGPT does not reduce auditability or reproducibility;
6. remains compatible with the two-Human-Gate and autonomous-progression model.

## 2. Overall verdict

The redesign direction is **substantively sound**, but the first draft of the redesign plan is **not yet sufficient as an implementation authority**.

The strongest parts are:

- moving reader-facing authorship and editorial/layout judgment back to ChatGPT;
- reducing GitHub Actions to deterministic/reproducible verification and controlled release work;
- creating an explicit internal-vs-reader-facing Publication Boundary;
- separating deterministic, semantic/editorial, and visual QA;
- making Publication Candidate revision atomic;
- separating edition production from shared-Core maintenance;
- standardizing edition-local execution records.

These changes should generally **increase**, not decrease, profile generality because fewer publication semantics are encoded in fixed Actions/workflow mutation paths. However, that improvement only holds if ChatGPT operates under stable Profile/edition authority rather than unconstrained free-form judgment.

Therefore the target architecture should be understood as:

```text
shared invariant Core
+ Research Profile constraints
+ Publication Profile constraints
+ edition/series planning authority
+ ChatGPT reasoning/editorial judgment
+ narrow deterministic helpers
+ independent CI/build/release verification
```

not simply:

```text
remove workflows
-> let the LLM decide everything
```

## 3. Finding RDA-001 — acceptance scope regressed from the original generality standard

Severity: `HIGH`  
Disposition: `REVISE DESIGN BEFORE IMPLEMENTATION`

The current redesign acceptance strategy names only:

- one clean Weekly trial;
- one clean `LONGFORM_SPECIAL` trial using SP001.

That is narrower than the pre-existing Core v2 final-audit requirement, which explicitly covered:

- future Weekly;
- Retrospective Period;
- standalone Thematic;
- SP-001–003 style work;
- Generative AI Foundations guided-series work;
- later unplanned Specials through generic Profile/planning authority.

A successful SP001 rerun proves the `THEMATIC + LONGFORM_SPECIAL` path, but it does not by itself prove:

- bounded-period coverage-audit semantics;
- annual/half-year chronology and cross-period synthesis;
- period-specific normalization and temporal-skew handling;
- Foundations series-level living-authority behavior.

### Required revision

The redesign acceptance strategy must restore the original generality bar.

At minimum:

1. real cold-start Weekly acceptance run;
2. real cold-start standalone Thematic/LONGFORM acceptance run using SP001;
3. one representative Retrospective Period production/replay through the requested Human Gate with no in-run Core repair, plus compatibility review against monthly/half-year/annual period guidance;
4. one Foundations-guided volume/scenario through at least Architecture Review to validate the living series authority and cross-volume planning boundary;
5. explicit no-overfit inspection confirming no W33/SP001/topic-specific behavior exists in shared Core.

Do not require an exhaustive synthetic future-edition matrix. Use a small representative set plus structural/Profile audits.

## 4. Finding RDA-002 — Research Profile and Publication Profile orthogonality must be explicit

Severity: `HIGH`  
Disposition: `REVISE DESIGN BEFORE IMPLEMENTATION`

The redesign correctly discusses `WEEKLY_MAGAZINE` and `LONGFORM_SPECIAL`, but its first draft could be read as if publication type were the primary semantic axis.

The current Core intentionally separates:

### Research Profiles

- `WEEKLY`
- `RETROSPECTIVE_PERIOD`
- `THEMATIC`

### Publication Profiles

- `WEEKLY_MAGAZINE`
- `LONGFORM_SPECIAL`

This separation must survive the redesign.

Examples:

- monthly, half-year and annual retrospectives share `RETROSPECTIVE_PERIOD` research semantics while varying edition-level editorial compression;
- standalone thematic and Foundations volumes may share `THEMATIC` research semantics while Foundations additionally uses living series authority;
- both Retrospective and Thematic publications may use `LONGFORM_SPECIAL`, but their research closure, chronology and synthesis requirements differ.

### Required revision

Shared Core should own only cross-profile invariants such as lifecycle, provenance, Publication Boundary, QA-class separation, candidate atomicity and execution records.

Research Profile guidance must continue to own research semantics. Publication Profile guidance must continue to own reader-format/layout semantics. Edition/series guidance must remain able to add narrower constraints without creating new generic workflows.

## 5. Finding RDA-003 — reduced Actions can improve generality, but only with policy-guided LLM reasoning

Severity: `MEDIUM`  
Disposition: `CLARIFY DESIGN`

The Owner's expectation is reasonable: removing fixed production-mutation workflows can make the pipeline more general because the same ChatGPT operator can reason over different edition types using the relevant policy rather than forcing every edition through a narrowly encoded execution graph.

This is especially useful for:

- evidence-derived retrospective trajectories;
- different chronology structures;
- thematic lineage work;
- Foundations volumes whose architecture can change as later research changes series understanding;
- future unplanned Specials.

However, unconstrained LLM reasoning would reduce reproducibility and make cross-session continuation fragile.

### Required balance

Retain stable constraints for:

- Profile identity and temporal semantics;
- source/evidence/provenance boundaries;
- Human Gates;
- required reader-facing components where genuinely universal/profile-specific;
- exact candidate byte identity;
- execution-record format;
- deterministic build/integrity checks.

Leave to ChatGPT:

- what the evidence means;
- how Architecture should organize it;
- how much depth each topic requires;
- how reader-facing prose should be composed;
- how a layout should be repaired when the correct repair depends on content.

Generality therefore comes from **fewer encoded editorial decisions**, not from fewer constraints overall.

## 6. Finding RDA-004 — Actions policy is compatible with the redesign and should remain a hard constraint

Severity: `PASS WITH GUARDRAIL`

The current Actions policy is consistent with the Owner's principle:

> GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, or publication-authoring agent.

Appropriate retained Actions work includes:

- regression/contract CI;
- schema/provenance/hash validation;
- pinned reproducible TeX/PDF build;
- deterministic compiler/preflight checks;
- exact-byte/freeze/release integrity;
- credential-isolated release publication.

Inappropriate Actions work includes:

- article drafting/synthesis;
- deciding reader-facing content survival;
- semantic publication reconstruction;
- layout correction chosen from document meaning;
- quality-state mutation that substitutes for ChatGPT editorial review;
- PR-as-execution-trigger chains used only to cause production mutation.

### Additional generality guardrail

Do not replace one set of W33/SP001-specific workflows with separate monthly/annual/Foundations workflows.

Where a crisp profile-specific CI check is justified, prefer a parameterized shared CI surface driven by Profile/config over a new authoring workflow.

## 7. Finding RDA-005 — Publication Boundary must be generic, not one fixed W33/SP001 payload schema

Severity: `MEDIUM`  
Disposition: `CLARIFY DESIGN`

Issue #434 suggests a non-empty `publication_payload` as one possible mechanism. The invariant that matters is broader:

> internal editorial/provenance fields are not legal publication prose inputs.

The redesign should not assume that every profile can or should be forced into one fixed `publication_payload` object with one article structure.

A reader-facing manuscript may be represented by Markdown, TeX, structured content, or another reviewed representation as long as:

- it is explicitly authored as reader-facing content;
- it is separate from internal rationale/state;
- publication assembly cannot fall back to internal fields;
- exact source-to-PDF provenance remains available.

This keeps the boundary generic enough for Weekly, period retrospectives, standalone Thematic work and Foundations.

## 8. Finding RDA-006 — Longform Evidence wording must not require every selected record to appear as prose

Severity: `MEDIUM`  
Disposition: `CLARIFY DESIGN`

The first redesign draft says selected Evidence must be developed into longform technical narrative. Read literally, this could encourage every selected/supporting record to become prose, which would be harmful for retrospective chronology and dense historical Specials.

The intended rule should be:

- every Architecture `must-cover` obligation and materially selected story/lineage must receive adequate reader-facing treatment;
- supporting Evidence may appear through notes, chronology, comparison, attribution or bibliography rather than one paragraph per record;
- publication depth is judged against the Architecture and research question, not Evidence-record count.

## 9. Finding RDA-007 — Retrospective Period semantics must be explicitly preserved

Severity: `HIGH`  
Disposition: `REVISE DESIGN BEFORE IMPLEMENTATION`

Existing half-year/annual guidance contains important semantics not exercised by W33/SP001:

- base Source Intake is a broad baseline, not a completeness proof;
- period-specific coverage audit and supplemental gap-fill;
- bounded-period chronology and lifecycle identity;
- annual within-year temporal-skew audit;
- Event -> Story unit -> Annual trajectory compression;
- cross-period/half-year synthesis;
- chronology resolution must survive narrative compression;
- later outcomes must not be back-projected into the historical period.

The redesign must state that these remain Profile/editorial authority and are not replaced by the W33/SP001-derived Publication changes.

## 10. Finding RDA-008 — Foundations series authority must remain living and outside a rigid machine series engine

Severity: `HIGH`  
Disposition: `REVISE DESIGN BEFORE IMPLEMENTATION`

The Foundations series intentionally allows later detailed research to revise the understanding and architecture of earlier/later volumes. Volume 1 is a living synopsis before it becomes final publication prose, and volume allocation can be split/merged/reordered.

The redesign should not introduce a fixed machine-level series graph or force all thematic work into SP001-style family packages.

Foundations should remain:

```text
living series authority
+ THEMATIC research profile
+ LONGFORM_SPECIAL publication profile
+ per-volume Architecture
```

with cross-volume planning/context supplied by the series memo.

## 11. Finding RDA-009 — execution-record path should bind to source root, not assume one issue-ID naming convention

Severity: `LOW`  
Disposition: `REVISE DOCUMENTATION`

The execution-record policy correctly says records live under the edition's existing source root, but examples/formal paths use `sources/<issue-id>/...`.

Existing Retrospective Specials may use internal source identities such as `sources/SP-<slug>/...`; therefore the contract should use:

```text
{source_root}/execution/
```

and treat the concrete source-root path as Profile/edition authority.

## 12. Finding RDA-010 — pre-existing authority/final-audit text conflicts with the new Production/Core boundary

Severity: `HIGH`  
Disposition: `NORMALIZE AUTHORITY BEFORE IMPLEMENTATION`

The old Core authority/final-audit rule still permits wording such as `generic repair`, `tool repair`, and integrating reviewed generic repairs into a running validation edition. It also describes Grok manual transport as passing instruction/prompt text rather than the newer exact Drive task-file path.

Those clauses were appropriate before the W33/SP001 evidence, but now conflict with the redesign.

Before implementation begins, the canonical authority and final-audit rule must be synchronized so that:

- production sessions do not author shared-Core repairs;
- a Core acceptance run that discovers a shared defect is failed/preserved and rerun cleanly after separate maintenance;
- ordinary edition-local/transient repair remains autonomous;
- Grok transport uses the exact Drive task-file path/reference;
- final generality audit again covers Weekly, Retrospective, Thematic and Foundations viability.

## 13. Finding RDA-011 — fewer Actions must not weaken deterministic exact-byte and release guarantees

Severity: `PASS WITH GUARDRAIL`

Reducing Actions should not remove controls that are genuinely strongest when independent of the authoring session.

Keep or replace equivalently:

- exact Source/PDF/Candidate binding;
- reproducible build;
- candidate invalidation on byte change;
- Freeze/Release exact-byte identity;
- Release credential isolation;
- idempotent release reconciliation.

The SP001 authority-drift defect is an argument for a smaller **more atomic** deterministic candidate-finalization mechanism, not for removing exact-byte authority.

## 14. Finding RDA-012 — two Human Gates and autonomous progression remain valid

Severity: `PASS`

Nothing in Issues #400/#433/#434 demonstrates a need for more routine Human Gates.

The failures occurred because the autonomous flow produced inadequate reader-facing artifacts, not because the user needed to approve more intermediate steps.

Keep:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Add stronger ChatGPT semantic/editorial/visual self-review before Publication Preview rather than creating a third Human checkpoint.

Manual Grok task-file path handoff remains transport, not approval.

## 15. Required design revisions before implementation

Before any scripts/schemas/workflows are changed:

1. add explicit Core / Research Profile / Publication Profile / edition-series authority layering to the redesign plan;
2. restore Retrospective Period and Foundations to the redesign acceptance matrix;
3. clarify that the reader-facing manuscript boundary is representation-agnostic and has no internal fallback;
4. clarify longform content fidelity around Architecture obligations rather than one-to-one Evidence rendering;
5. add the no-profile-specific-Actions-proliferation guardrail;
6. normalize execution-record paths around `{source_root}`;
7. synchronize the final-audit/authority rules with Production-vs-Core separation and exact Drive task-file Grok handoff;
8. preserve exact-byte/release guarantees explicitly;
9. only after these documentation/authority revisions are coherent should implementation begin.

## 16. Audit conclusion

The redesign should proceed **after the above design corrections are applied**.

The Owner's hypothesis is supported with an important qualification:

> Reducing Actions-authored production logic should improve Core generality because fewer edition semantics are frozen into workflows, **provided** Profile/edition authority remains explicit and ChatGPT's increased reasoning freedom is recorded and bounded by stable provenance, gate, and candidate-integrity contracts.

Under that model, the redesign is expected to improve applicability to future Weekly issues, Retrospective Period Specials, standalone Thematic Specials and Foundations volumes rather than narrowing the Core around W33/SP001.
