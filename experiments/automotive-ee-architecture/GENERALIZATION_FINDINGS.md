# Automotive E/E experiment: generalization findings

Status: **EXPERIMENTAL / production AI pipeline unchanged**

This note records what the Automotive E/E architecture experiment has demonstrated about the existing survey pipeline. It is intentionally not a migration plan for the production generative-AI survey. The AI survey remains the repository's primary product and its current contracts remain authoritative.

## 1. Experiment boundary

Branch: `experiment/automotive-ee-architecture-special`

Issue identity used only by the experiment: `SP-automotive-ee-architecture-2023-2026`

The experiment asks a narrow question:

> Which parts of the existing Special pipeline are genuinely survey-domain-neutral, and which parts only appear generic because the production domain is always generative AI?

No production AI collector config, prompt, schema, deterministic stage implementation, or pipeline controller has been modified by this experiment.

A `main...experiment/automotive-ee-architecture-special` comparison after the Candidate-matrix probe showed the branch ahead of `main` with **all diff entries added files**; there were no modified or deleted production files. This is the strongest current guardrail: the experiment is additive, not a refactor of the AI product.

## 2. Empirical Source Intake result

The profiled Source Intake reuses `scripts/source_intake.py` without changing it and supplies an Automotive E/E profile/plan through an experiment-only adapter.

Observed stable intake shape from the experiment run family:

- arXiv: 50 unique papers from 6 successful queries;
- GitHub Releases: 53 matching releases from 4 repositories;
- official pages: 9 successful snapshots;
- official-page acquisition gaps: 4 (AUTOSAR TLS chain validation on the hosted runner: 3; ISO HTTP 403: 1).

The combined Screening input contains 112 records.

The acquisition gaps are retained as gaps. The experiment does not disable TLS verification, bypass access controls or treat a failed fetch as evidence.

### Finding S1 — collector mechanics are mostly reusable

`source_intake.py` already separates arXiv, GitHub Releases and official HTTP pages from most editorial semantics. The main domain-specific inputs are therefore configuration data:

- query/watch lists;
- repository lists;
- official-page lists;
- collection window / issue plan;
- coverage policy;
- transport policy and explicit exceptions.

The first hard-coded assumption encountered was provenance text pointing to the production AI config/weekly plan. The experiment adapter replaces only those labels.

**Likely future abstraction:** make collector provenance inputs explicit parameters. Do not fork the collector per domain.

## 3. Screening normalization result

The production `scripts/build_screening_index.py` normalized all 112 Automotive records without modification.

However, ordinary non-feed HTML is classified as `official-index-snapshot`. That is appropriate for the production AI watchlist, where many official pages are newsroom/index surfaces, but not for standards/technical pages that are already item-level evidence.

The experiment introduced `official_pages.pages[].page_role = INDEX | ITEM` and an experiment-only `profiled_screening_index.py` adapter.

With identical Raw input:

- canonical normalizer: 112 records, including 9 `official-index-snapshot` records, 5 batches;
- profiled normalizer: 112 records, with those 9 item pages represented as `official-page-snapshot`, 6 batches because visible item text is carried into Screening.

### Finding S2 — page role belongs in source/profile semantics

`INDEX` versus `ITEM` is not an AI concept. It is a property of how a configured HTTP source should be interpreted.

**Likely future abstraction:** add a source-page role to a generic source profile, while preserving the production default as `INDEX` so existing AI behavior does not change.

## 4. Screening decision contract

The existing `schemas/screening-batch-result.schema.json` is reusable unchanged:

- `KEEP | MAYBE | DROP | INSPECT`;
- reasons and confidence;
- duplicate grouping;
- verification targets;
- topic-lane identifiers.

The production Screening prompt is not domain-neutral. It embeds:

- generative-AI editorial relevance;
- weekly `why_now` semantics;
- the production A-L lane meanings.

The experiment therefore keeps the schema and supplies an Automotive-specific prompt plus lane profile:

- A — physical/zonal topology;
- B — central/HPC compute and mixed criticality;
- C — in-vehicle networking;
- D — runtime/middleware/service/data contracts;
- E — cloud-to-edge development and validation lifecycle;
- F — safety/security/isolation boundaries;
- G-L — reserved.

The pinned Automotive selection over the 112-record profiled Screening index is:

- `KEEP`: 41;
- `MAYBE`: 19;
- `DROP`: 52;
- retained for Evidence: 60.

Retained source composition:

- papers: 33;
- GitHub releases: 18;
- official item pages: 9.

The selection file intentionally stores only retained decisions, lane context and duplicate grouping. Omitted records deterministically become `DROP` in the experiment bridge. This avoids accidentally promoting verbose Screening rationale into a new shared contract.

### Finding S3 — Screening structure is reusable; editorial relevance is profile context

**Likely future abstraction:** parameterize Screening prompt/context and lane meanings. Do not widen or weaken the production Screening result schema.

## 5. Evidence task construction

The experiment materializes a verification queue from the pinned Screening selection and then calls the production `scripts/build_evidence_tasks.py` unchanged.

Empirical result:

- retained Screening records: 60;
- Evidence Tasks: 45;
- `VERIFY_ITEM`: 42;
- `VERIFY_SERIES`: 3;
- `INSPECT_INDEX`: 0;
- missing Screening coverage: 0;
- duplicate Screening coverage: 0.

The reduction from 60 records to 45 tasks is explained by three coherent release series (VSS, vSomeIP, S-CORE), not by an arbitrary target count.

One original behavior depended indirectly on the Source/Screening semantic leak: `official-index-snapshot` becomes `INSPECT_INDEX`. Once item-level HTML is represented correctly as `official-page-snapshot`, the production task builder works without modification.

### Finding E1 — Evidence task construction is shared machinery

This is now empirically demonstrated rather than inferred from code inspection. No Automotive-specific Evidence-task-builder fork is justified.

## 6. Evidence execution contract

The production Evidence model contains a strong reusable core:

- runner provenance;
- source classes;
- evidence classes (`PRIMARY_FACT`, `VENDOR_CLAIM`, `PROJECT_CLAIM`, `AUTHOR_CLAIM`, `SOCIAL_OBSERVATION`, `INFERENCE`);
- temporal Events;
- claims, metrics and limitations with source IDs;
- verification-target resolution;
- editorial recommendation states.

The first schema-level AI assumption is `artifact.artifact_type`, whose closed enum is centered on models/APIs/agents/AI frameworks.

The experiment therefore adds `evidence-profile.json` and `profiled_evidence_contract.py`. The adapter does **not** edit `schemas/evidence-card.schema.json`; instead it deterministically generates an experiment contract from the production shape and replaces only `artifact_type` with the domain ontology.

Automotive E/E experimental artifact types:

- `STANDARD`
- `SPECIFICATION`
- `PLATFORM`
- `MIDDLEWARE`
- `REFERENCE_IMPLEMENTATION`
- `PROTOCOL`
- `ARCHITECTURE_PATTERN`
- `CONSORTIUM_INITIATIVE`
- `PAPER`
- `FRAMEWORK`
- `PRODUCT`
- `OTHER`

The Evidence prompt is domain-specific because standards, consortium claims and retrospective relevance need different verification instructions from generative-AI model/release verification.

A read-only profiled Evidence execution package was successfully generated for all 45 Tasks. It composes:

1. Tasks produced by `scripts/build_evidence_tasks.py` unchanged;
2. the Automotive-specific pinned Evidence prompt;
3. generated strict Evidence Run/Card schemas derived from the production schema shape.

Production `prepare_evidence_run.py`, production Evidence prompt/schema, and production lifecycle acceptance were intentionally bypassed rather than modified.

### Finding E2 — Evidence package mechanics can be separated from lifecycle binding

Execution-package mechanics are reusable, while edition/lifecycle binding and the chosen prompt/schema contract are context. This suggests a future package-builder interface with explicit `issue identity`, `prompt`, `run schema`, `card schema`, and `lifecycle binding` inputs rather than a parallel Automotive package implementation.

## 7. Evidence ontology vertical slice

Three representative real Evidence Runs were created and validated against the exact pinned 45-task package:

| Case | Domain artifact type | Status | Recommendation |
|---|---|---|---|
| IEEE Std 802.1DG-2025 | `STANDARD` | `VERIFIED` | `CANDIDATE` |
| Eclipse S-CORE release series | `PLATFORM` | `PARTIAL` | `CANDIDATE` |
| Centralization potential paper | `PAPER` | `VERIFIED` | `CANDIDATE` |

All three passed both:

- the **unchanged** production `scripts/validate_evidence_run.py` invariant validator (task/prompt SHA, identity, source/event references, verification target coverage, etc.);
- strict JSON Schema validation against the **generated Automotive domain Evidence schemas**.

The S-CORE series correctly remains `PARTIAL`: v0.1.0 establishes a release but its release page does not provide enough detailed change evidence to pretend that the technical baseline is fully verified.

### Finding E3 — provenance/evidence semantics are reusable across distinct artifact ontologies

The existing source classes and evidence classes survived a standard, an OSS platform series and a research paper without domain-specific widening. The closed artifact ontology is the part that needs profiling.

**Likely future abstraction:** generate a strict `artifact_type` enum from the selected domain profile at package-build time; do not replace the production enum globally with an unconstrained string.

## 8. Candidate comparison probe

The three validated Evidence Runs were then passed to the production `scripts/build_candidate_matrix.py` unchanged.

Result:

- rows: 3;
- artifact types: `STANDARD`, `PLATFORM`, `PAPER`;
- timing: `MAIN_EVENT=2`, `TIMING_UNRESOLVED=1`;
- recommendation: `CANDIDATE=3`;
- readiness: `READY_WITH_CAVEAT=3`.

The `TIMING_UNRESOLVED` row is expected: the paper card includes a month-precision journal-publication event (`2025-01`), and the production matrix correctly refuses to invent day precision.

A small editorial semantic leak remains in `build_candidate_matrix.py`: when `why_now_confirmed=false`, it can emit the boundary text `Weekly why-now relevance is not confirmed.` That string was not emitted by this slice because all three have retrospective relevance confirmed.

### Finding C1 — Candidate matrix structure is shared; a small wording/context seam remains

This stage is now empirically demonstrated with Automotive Evidence. The matrix mechanics do not need an Automotive fork. If generalized later, `why_now` label/semantics should come from edition context rather than hard-coded weekly wording.

## 9. Proven shared/core boundary so far

```text
shared deterministic machinery — empirically reusable
  ├─ HTTP / arXiv / GitHub collector mechanics
  ├─ Raw provenance and hashing
  ├─ Screening record/batch mechanics
  ├─ Screening result schema
  ├─ Evidence Task construction
  ├─ Evidence invariant validation
  ├─ Evidence source/evidence class structure
  └─ Candidate comparison mechanics

survey/domain profile — empirically domain-owned
  ├─ issue/time-window semantics
  ├─ source queries/watchlists
  ├─ source page role: INDEX | ITEM
  ├─ transport policy
  ├─ Screening editorial relevance
  ├─ topic-lane meanings
  ├─ Evidence verification prompt/context
  └─ Evidence artifact-type ontology

execution/lifecycle binding — not yet generalized
  ├─ accepted Screening persistence
  ├─ lifecycle-state transitions
  ├─ complete Evidence acceptance
  ├─ Candidate Selection persistence
  └─ Architecture Review gate integration

production AI profile
  └─ remains the authoritative default and retains current strict contracts
```

A future generic profile could eventually gather the current experiment files under one manifest, but doing that now would be premature. The current split exposes exactly which stage needs which context.

## 10. Guardrails before any production refactor

Do not modify the production pipeline merely because Automotive passes these probes.

Before moving an abstraction into shared production code, require all of the following:

1. Existing AI weekly/monthly/half-year/annual contract tests remain byte/behavior compatible where intended.
2. The abstraction has been exercised by Automotive through the relevant downstream stage, not only inferred from code inspection.
3. The production AI profile preserves current defaults explicitly; there is no silent behavior change from missing profile fields.
4. Domain-specific prompt/schema changes remain fail-closed and pinned by SHA-256 in execution packages.
5. Retrieval failures remain visible coverage gaps; genericization must not introduce insecure transport fallbacks.
6. Existing strict AI ontologies must not be weakened merely to accommodate another domain.
7. Production lifecycle/acceptance code must not be generalized until a full Automotive Evidence set has exercised the same semantics end to end.

## 11. Next experimental milestone

The abstraction probe has reached Candidate comparison, but the **Automotive survey itself has not completed Evidence**. Only 3 of 45 Evidence Tasks have real verified result cards in the vertical slice.

The next milestone is therefore deliberately not a production refactor. It is:

1. execute the remaining Automotive Evidence Tasks against primary sources;
2. preserve unresolved AUTOSAR/ISO acquisition gaps rather than bypassing them;
3. build a complete reviewed Evidence set;
4. run the shared Candidate matrix over the complete set;
5. only then test Candidate Selection and Architecture-input mechanics.

This keeps the experiment evidence-led: abstractions move into the proven column only after a real downstream workload exercises them.

## 12. Current conclusion

The existing pipeline is substantially more reusable than its AI-specific naming suggests. The safe direction is **profile extraction around a stable AI-first pipeline core**, not conversion of the repository into a generic survey framework.

The smallest useful abstraction boundary currently demonstrated is:

1. collector provenance/config context;
2. source page role;
3. Screening relevance/lane context;
4. Evidence prompt and artifact ontology;
5. edition-specific `why_now` wording/context.

Everything related to production acceptance, lifecycle transitions, Candidate Selection and Architecture gates remains intentionally untouched until the complete Automotive Evidence workload provides evidence that those layers should be generalized.
