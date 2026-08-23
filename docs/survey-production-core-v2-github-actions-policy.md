# Survey Production Core v2 — GitHub Actions Responsibility Policy

Status: `INTEGRATED REDESIGN INVARIANT / HUMAN-GATE ROUNDTRIP MAINTENANCE SYNCHRONIZED`  
Established: 2026-08-23 JST  
Human-Gate update: 2026-08-24 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`  
Related feedback: `PFB-006` and `PFB-014` in `docs/survey-production-core-v2-production-feedback-backlog.md`

## 1. Purpose

This memo defines the responsibility rule for GitHub Actions in Survey Production Core v2 after W33/SP001 production review, clean post-merge revalidation, and the later Human Gate round-trip audit.

The old production topology used Actions for Drafting/Synthesis, semantic/publication mutation, layout repair, stage/candidate mutation and bot-driven production chaining. W33/SP001 demonstrated that this made workflow topology itself part of the production problem.

The governing principle remains:

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, Human-decision, or publication-authoring agent.**

A task must not be placed in Actions merely because it can be scripted.

The post-merge revalidation adds one qualification: when the primary ChatGPT connector runtime can edit the exact repository branch but cannot mount that branch and invoke canonical local Core CLI, Actions may supply that **missing deterministic execution substrate** through one narrowly constrained operator bridge. This does not transfer editorial or Human authority to Actions.

## 2. Admission rule for GitHub Actions

Before retaining or adding any production-related Actions task, ask both:

1. **Does Actions provide a concrete execution/reproducibility/security advantage that the primary operator path lacks?**
2. **Is the task mechanical enough that no research/editorial/visual/Human judgment is transferred into CI?**

Useful Actions-specific advantages include reproducible build environments, independent CI, branch-protection integration, credential isolation, immutable artifacts, deterministic verification and an exact checked-out Core execution environment unavailable to a connector-only ChatGPT runtime.

`It is already a script`, `it can be automated`, or `we used a workflow before` are not sufficient reasons.

## 3. Appropriate Actions responsibilities

### CI and contract validation

Appropriate examples include unit/regression tests, schema/path/invariant checks, provenance/exact-byte integrity, identifier/reference integrity, deterministic stage-contract verification and reproducible compiler/preflight checks.

### Reproducible builds

Actions may compile already-authored Weekly/Special publication source in a controlled toolchain, report deterministic findings/hashes/page counts and expose independently reproducible artifacts. It must not design or repair the publication.

### Freeze / release integrity

Actions may perform exact-byte Candidate/Preview/Freeze/Release checks, release-manifest validation, credential-isolated publishing and idempotent release reconciliation.

### Optional operator execution bridge

When direct exact local Core CLI execution is unavailable to ChatGPT, Actions may:

- check out one exact immutable request commit;
- verify the work branch's protected shared Core/contract bytes against one reviewed `main` baseline before execution;
- execute only schema-enumerated existing deterministic Core operations;
- initialize canonical Weekly, configured Retrospective Period, or Thematic Profile/State through repository-owned builders;
- validate already-authored stage artifacts, generate deterministic Stage Checkpoint/result authority, and advance one lifecycle edge;
- after a Human has explicitly decided, record Architecture/Publication Preview approval or `REQUEST_CHANGES` and apply the deterministic validated lifecycle consequence;
- enforce Profile-bound edition-local write scope;
- commit exact deterministic outputs and receipts back to the same work branch.

Configured Retrospective initialization reuses the **existing `survey_period_v2` Core helper**. Monthly, half-year and annual semantics remain one generic Retrospective Period path; maintenance adds no second period builder, scope schema or cadence-specific workflow logic.

Human Gate recording reuses canonical `survey_human_gate_v2`. The Human supplies the decision, review provenance, requested changes and regeneration boundary. Actions/Core only validate and record that explicit decision and invalidate the dependency range defined by repository contract.

The bridge must not accept request-supplied shell, Python, module, script, workflow or arbitrary executable identifiers. Its authority is `docs/survey-production-core-v2-operator-execution-bridge.md`.

## 4. Work that remains with ChatGPT and Human

Tasks requiring interpretation, synthesis, prioritization, semantic judgment, visual taste or actual Human decision remain outside Actions.

ChatGPT owns Source Intake/search strategy, source-quality/materiality judgment, Screening/Evidence interpretation, Selection, Architecture, Drafting/Synthesis, reader-facing authorship, Grok/X disposition, retrospective trajectory/period interpretation, thematic lineage/historical attribution, semantic/editorial QA, exact-PDF visual QA, applying requested revisions, and deciding whether a true Exception Gate is needed.

The Human owns the actual normal Human Gate decision:

- `APPROVED`; or
- routine `REQUEST_CHANGES` with feedback and a regeneration boundary.

The bridge may persist that already explicit decision. It must never choose it.

## 5. Mechanical execution vs encoded editorial judgment

A process can be deterministic while still encode editorial policy that should not be delegated. Turning authored source into TeX or validating a schema can be mechanically appropriate. A generic script deciding how much prose survives, what information becomes reader-facing, where every chapter breaks, which material is selected, or what the Human “must have meant” is editorial.

Therefore distinguish **mechanically executable** from **mechanically appropriate to delegate**.

Human Gate recording is mechanically appropriate only because the decision and regeneration boundary arrive as explicit Human input. The mechanical layer may reject invalid/stale input; it may not reinterpret it.

## 6. Generality rule

Do not solve generality by creating separate authoring/mutation workflow families for Weekly, monthly/half-year/annual retrospectives, standalone Thematic, Foundations or other topic/cadence variants.

Preferred model:

```text
Profile/config/edition authority
-> ChatGPT reasoning and authorship
-> Human decision at the two normal Gates
-> narrow common deterministic helpers
-> direct local execution when available
-> optional shared operator bridge when local execution is unavailable
-> shared CI/build/preview/release verification
```

The operator bridge must be Profile/path driven and must not encode W33/SP001 topic names, fixed package taxonomies, fixed source-root depth, fixed branch-family names, Foundations volume structure, annual trajectory choices, or topic-specific Human revision logic.

## 7. Target responsibility model

```text
ChatGPT
  research / reasoning / editorial judgment
  architecture / drafting / synthesis
  publication-source authoring
  semantic and exact-PDF visual review/repair
          |
Human     |  APPROVED / REQUEST_CHANGES + feedback/boundary
          v
Canonical repository scripts
  narrow deterministic transformation/checking
  Profile/State/checkpoint mechanics
  Human-decision recording / selective invalidation
  existing Weekly / Period / Thematic profile builders
          |
          +----------------------------+
          |                            |
          v                            v
Direct exact local CLI          Operator bridge (fallback)
preferred when available        exact checked-out deterministic execution only
          |                            |
          +-------------+--------------+
                        v
GitHub Actions independent surfaces
  CI / reproducible build / Preview transport / Release integrity
```

## 8. Human Gate operator-boundary rule

The bridge's Human Gate surface is deliberately not a generic `decision` interpreter. Its request schema exposes four narrow operation kinds:

- `RECORD_ARCHITECTURE_APPROVAL`
- `REQUEST_ARCHITECTURE_REVISION`
- `RECORD_PUBLICATION_PREVIEW_APPROVAL`
- `REQUEST_PUBLICATION_PREVIEW_REVISION`

Every request requires exact current State, next contiguous review revision, Human identity/time/reference and—when revising—explicit requested changes plus an enum-constrained gate-specific regeneration boundary.

A generic `EXECUTE_HUMAN_DECISION`, arbitrary rejection operation, command string or free-form executable target is prohibited.

## 9. PDF / typesetting boundary

Preferred publication loop:

```text
ChatGPT authors/edits publication source
-> ChatGPT reviews rendered PDF and makes semantic/layout decisions
-> candidate source is committed
-> Actions independently rebuilds/verifies
-> deterministic build/preflight PASS or FAIL
```

Avoid the retired anti-pattern where Actions chooses layout repairs or becomes the publication authoring loop.

## 10. Exact-byte/candidate/revision/release guarantees

Reducing Actions-authored production logic does not weaken exact source/PDF/Candidate binding, invalidation on byte changes, reproducible build, Freeze/Release exact-byte identity, release credential isolation or idempotent Release reconciliation.

Normal Human revision must strengthen these guarantees:

- r1 reviewed bytes are recorded by SHA and reviewed repository commit;
- selected downstream checkpoint/gate authority becomes pending after `REQUEST_CHANGES`;
- superseded Stage Checkpoints are removed so regeneration cannot silently reuse old acceptance;
- r2 must be revalidated to the same gate;
- stale r1 approval fails;
- final approval binds only the current rN bytes.

## 11. Workflow review classification

Retained/introduced workflows should fit one of these justified classes:

- `KEEP_AS_CI`
- `KEEP_AS_REPRODUCIBLE_BUILD`
- `KEEP_AS_EXACT_BYTE_TRANSPORT_OR_RELEASE`
- `KEEP_AS_DETERMINISTIC_EXECUTION_SUBSTRATE`
- `RETURN_TO_CHATGPT`
- `LEGACY_REMOVE_CANDIDATE`

Every retained workflow must state the concrete Actions-specific benefit and remain narrow enough that no editorial/Human decision ownership is transferred.

## 12. Current Actions surface

The maintenance candidate keeps exactly seven workflows:

1. `pipeline-contract-tests.yml`
2. `survey-production-v2-ci.yml`
3. `build-weekly-survey.yml`
4. `build-special-pdf.yml`
5. `survey-production-v2-export-publication-preview.yml`
6. `survey-production-v2-release.yml`
7. `survey-production-v2-operator-bridge.yml`

Human Gate round-trip support extends the existing seventh bridge; it does not justify an eighth workflow.

## 13. Evidence and acceptance

Earlier bridge work proved immutable requests, reviewed-main preflight, Profile-bound writes, no arbitrary executable surface, configured Retrospective reuse and init -> Discovery execution. The later full-system audit found that approval/revision continuation was missing.

Current maintenance therefore requires fresh positive/negative Human Gate round-trip regressions, bridge-backed execution tests, exact-head CI/contract tests and the complete **seven-point** fixed-head audit. Historical six-point PASS evidence remains diagnostic only.

After Human-reviewed unchanged integration, clean Weekly, SP001/Thematic, representative Retrospective and Foundations-guided production validation is still required before PFB-013/PFB-014 can be closed.
