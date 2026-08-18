# Automotive E/E experiment: generalization findings

Status: **EXPERIMENTAL / production AI pipeline unchanged**

This note records what the Automotive E/E architecture experiment has demonstrated about the existing survey pipeline. It is intentionally not a migration plan for the production generative-AI survey. The AI survey remains the repository's primary product and its current contracts remain authoritative.

## 1. Experiment boundary

Branch: `experiment/automotive-ee-architecture-special`

Issue identity used only by the experiment: `SP-automotive-ee-architecture-2023-2026`

The experiment is designed to answer a narrow question:

> Which parts of the existing Special pipeline are genuinely survey-domain-neutral, and which parts only appear generic because the production domain is always generative AI?

No production AI collector config, prompt, schema or pipeline controller is modified by this experiment.

## 2. Empirical Source Intake result

The profiled Source Intake reuses `scripts/source_intake.py` without changing it and supplies an Automotive E/E profile/plan through an experiment-only adapter.

Observed intake from the current experiment run family:

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

### Finding S3 — Screening structure is reusable; editorial relevance is profile context

**Likely future abstraction:** parameterize Screening prompt/context and lane meanings. Do not widen or weaken the production Screening result schema.

## 5. Evidence task construction

`scripts/build_evidence_tasks.py` is largely domain-neutral. It converts retained Screening records into deterministic verification tasks and carries provenance, grouping hints and verification targets forward.

One behavior depends indirectly on the Source/Screening semantic leak described above: `official-index-snapshot` becomes `INSPECT_INDEX`. Once item-level HTML is represented correctly as `official-page-snapshot`, that behavior is no longer a problem.

### Finding E1 — task construction can remain shared

No Automotive-specific task-builder fork is currently justified.

## 6. Evidence contract

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

The Evidence prompt is also domain-specific because standards, consortium claims and retrospective relevance need different verification instructions from generative-AI model/release verification.

### Finding E2 — Evidence shape is reusable; artifact ontology and verification context are profile-owned

**Likely future abstraction:** generate the closed `artifact_type` enum from a domain profile at package-build time, while keeping a strict production AI ontology for AI editions.

This is preferable to replacing the enum globally with an unconstrained string.

## 7. Candidate comparison / later stages

Initial code inspection suggests `build_candidate_matrix.py` is structurally reusable: it compares timing, evidence status, recommendation, source/evidence-class depth and unresolved boundaries without ranking.

A small semantic leak remains: a boundary string refers to "Weekly why-now relevance". Retrospective timing semantics also depend on the surrounding pipeline state.

This stage has **not yet been exercised end-to-end with accepted Automotive Evidence**, so no production abstraction should be made from inspection alone.

## 8. Proposed abstraction shape — not yet a production change

The experiment currently supports the following layered model:

```text
shared deterministic machinery
  ├─ HTTP / arXiv / GitHub collectors
  ├─ Raw provenance and hashing
  ├─ Screening record/batch mechanics
  ├─ Screening result schema
  ├─ Evidence task mechanics
  ├─ Evidence provenance / claim / metric / limitation structure
  └─ Candidate comparison mechanics (provisional)

survey/domain profile
  ├─ issue/time-window semantics
  ├─ source queries/watchlists
  ├─ source page role: INDEX | ITEM
  ├─ transport policy
  ├─ Screening editorial relevance
  ├─ topic-lane meanings
  ├─ Evidence verification prompt/context
  └─ Evidence artifact-type ontology

production AI profile
  └─ remains the authoritative default and retains current strict contracts
```

A future generic profile could eventually gather these currently separate experiment files under one manifest, but doing that now would be premature. The current split is useful because it exposes exactly which stage needs which context.

## 9. Guardrails before any production refactor

Do not modify the production pipeline merely because Automotive can pass an adapter probe.

Before moving an abstraction into shared production code, require all of the following:

1. Existing AI weekly/monthly/half-year/annual contract tests remain byte/behavior compatible where intended.
2. The abstraction has been exercised by at least the Automotive experiment through the relevant downstream stage, not only inferred from code inspection.
3. The production AI profile preserves current defaults explicitly; there is no silent behavior change from missing profile fields.
4. Domain-specific prompt/schema changes remain fail-closed and pinned by SHA-256 in execution packages.
5. Retrieval failures remain visible coverage gaps; genericization must not introduce insecure transport fallbacks.

## 10. Current conclusion

The existing pipeline is more reusable than its naming suggests. The safe direction is **profile extraction around a stable AI pipeline core**, not conversion of the entire repository into a generic framework.

So far, the smallest useful abstraction boundary is:

1. collector provenance/config context;
2. source page role;
3. Screening relevance/lane context;
4. Evidence prompt and artifact ontology.

Everything else should remain unchanged until the Automotive experiment supplies contrary evidence.
