# Survey Production Core v2 — GitHub Actions Responsibility Policy

Status: `INTEGRATED REDESIGN INVARIANT / OPERATOR-BRIDGE MAINTENANCE SYNCHRONIZED`  
Established: 2026-08-23 JST  
Bridge-maintenance update: 2026-08-23 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`  
Related feedback: `PFB-006` and `PFB-014` in `docs/survey-production-core-v2-production-feedback-backlog.md`

## 1. Purpose

This memo defines the responsibility rule for GitHub Actions in Survey Production Core v2 after the W33/SP001 production review and the later clean post-merge revalidation.

The old production topology used Actions for Drafting/Synthesis, semantic/publication mutation, layout repair, stage/candidate mutation and bot-driven production chaining. W33/SP001 demonstrated that this made the workflow topology itself part of the production problem.

The redesign therefore keeps the governing principle:

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, or publication-authoring agent.**

A task must not be placed in Actions merely because it can be scripted.

The clean post-merge revalidation added one important qualification: when the primary ChatGPT connector runtime can edit the exact repository branch but cannot mount that branch and invoke the canonical local Core CLI, Actions may supply that **missing deterministic execution substrate** through a narrowly constrained operator bridge. This does not transfer editorial ownership to Actions.

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

When direct exact local Core CLI execution is unavailable to the ChatGPT runtime, Actions may:

- check out one exact immutable request commit;
- execute only a schema-enumerated allowlist of existing deterministic Core operations;
- initialize canonical Weekly, configured Retrospective Period, or Thematic Profile/State only through repository-owned builders/authority;
- generate deterministic checkpoint/result authority already defined by canonical Core code;
- enforce reviewed-main shared-Core equivalence before dependency installation/execution;
- enforce Profile-bound edition-local write scope;
- commit exact deterministic outputs and receipts back to the same work branch.

Configured Retrospective initialization reuses the **existing `survey_period_v2` Core helper**. The bridge passes the configured `special_slug` to `survey_period_v2.resolve_configured_period()` and then uses `survey_period_v2.period_profile()`. Monthly, half-year and annual semantics therefore remain the existing generic Retrospective Period path; the maintenance candidate adds no second period builder, scope schema or cadence-specific workflow logic.

The bridge must not accept request-supplied shell, Python, module, script, workflow or arbitrary executable identifiers. Its current authority is `docs/survey-production-core-v2-operator-execution-bridge.md`.

## 4. Work that remains with ChatGPT

Tasks requiring interpretation, synthesis, prioritization, semantic judgment, visual taste or Human decision remain owned by ChatGPT, including Source Intake/search strategy, source-quality/materiality judgment, Screening/Evidence interpretation, Selection, Architecture, Drafting/Synthesis, reader-facing authorship, Grok/X disposition, retrospective trajectory/period interpretation, thematic lineage/historical attribution, semantic/editorial QA, exact-PDF visual QA and actual Human Gate handling.

A deterministic helper or operator bridge may validate or advance already-authored artifacts; it must not silently become the editor.

## 5. Mechanical execution vs encoded editorial judgment

A process can be deterministic while still encoding editorial policy that should not be delegated. Turning authored source into TeX or validating a schema can be mechanically appropriate. A generic script deciding how much prose survives, what information becomes reader-facing, where every chapter breaks, or which material is selected is editorial even if deterministic.

Therefore distinguish **mechanically executable** from **mechanically appropriate to delegate**. The operator bridge is admitted because its allowlist is limited to Core mechanics whose semantics already exist independently of the workflow.

## 6. Generality rule

Do not solve generality by creating separate authoring/mutation workflow families for Weekly, monthly/half-year/annual retrospectives, standalone Thematic, Foundations or other topic/cadence variants.

Preferred model:

```text
Profile/config/edition authority
-> ChatGPT reasoning and authorship
-> narrow common deterministic helpers
-> direct local execution when available
-> optional shared operator bridge when local execution is unavailable
-> shared CI/build/preview/release verification
```

The operator bridge must be Profile/path driven and must not encode W33/SP001 topic names, fixed package taxonomies, fixed source-root depth, fixed branch-family names, Foundations volume structure, or annual trajectory choices.

For Retrospective work, existing `survey_period_v2` remains the generic Core builder. The bridge only makes that existing deterministic path executable from the connector-only runtime.

## 7. Target responsibility model

```text
ChatGPT
  research / reasoning / editorial judgment
  architecture / drafting / synthesis
  publication-source authoring
  semantic and exact-PDF visual review/repair
          |
          v
Canonical repository scripts
  narrow deterministic transformation/checking
  Profile/State/checkpoint mechanics
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

## 8. PDF / typesetting boundary

Preferred publication loop:

```text
ChatGPT authors/edits publication source
-> ChatGPT reviews rendered PDF and makes semantic/layout decisions
-> candidate source is committed
-> Actions independently rebuilds/verifies
-> deterministic build/preflight PASS or FAIL
```

Avoid the retired anti-pattern where Actions chooses layout repairs or becomes the publication authoring loop.

## 9. Exact-byte/candidate/release guarantees

Reducing Actions-authored production logic does not weaken exact source/PDF/Candidate binding, invalidation on byte changes, reproducible build, Freeze/Release exact-byte identity, release credential isolation or idempotent Release reconciliation.

The bridge likewise binds exact request/event/Profile/State authority and may not bypass these controls.

## 10. Workflow review classification

Retained/introduced workflows should fit one of these justified classes:

- `KEEP_AS_CI`
- `KEEP_AS_REPRODUCIBLE_BUILD`
- `KEEP_AS_EXACT_BYTE_TRANSPORT_OR_RELEASE`
- `KEEP_AS_DETERMINISTIC_EXECUTION_SUBSTRATE`
- `RETURN_TO_CHATGPT`
- `LEGACY_REMOVE_CANDIDATE`

Every retained workflow must state the concrete Actions-specific benefit and remain narrow enough that no editorial ownership is transferred.

## 11. Evidence from W33 / SP001 and fixed-head audit

The failed pre-redesign SP001/W33 runs showed that Actions-heavy authoring and mutation did not guarantee publication quality and created authority-rebinding/workflow-chaining problems.

The first clean post-redesign W33/SP001 attempts then showed the opposite operational edge: once authoring/mutation workflows were correctly removed, the normal connector-only ChatGPT runtime lacked a way to execute canonical deterministic local Core mechanics over the exact branch checkout. That evidence motivates the narrow fallback bridge, not restoration of the old production topology.

A fresh maintenance audit then showed that a bridge exposing only Weekly/Thematic could not execute the mandated connector-runtime Retrospective validation. Deeper pre-freeze inspection established that Core already contained the canonical generic Retrospective builder in `scripts/survey_period_v2.py`; the maintenance defect was **bridge exposure**, not missing Retrospective semantics. Temporary duplicate adapter work was removed before candidate freeze.

## 12. Relationship to publication quality

Machine checks are necessary but not sufficient. Keep separate deterministic QA proved by scripts/Actions, semantic/editorial QA performed by ChatGPT, and exact-PDF visual QA performed by ChatGPT.

Actions must never issue a semantic-quality PASS merely because schemas or known-token checks pass. Likewise the operator bridge may transport ChatGPT-authored agent review evidence but cannot create or reinterpret the underlying semantic/visual judgment.

## 13. Current implementation rule

The integrated redesign remains authoritative. The operator bridge is a shared-Core maintenance candidate and changes the audited Actions surface from six to seven workflows if accepted.

Therefore the prior six-workflow fixed-head audit is historical evidence only. The bridge candidate must receive fresh exact-head CI and the complete six-point fixed-head audit. If that audit requires any tree change, the entire fixed-head audit restarts from point 1.

After Human-reviewed unchanged integration, the clean post-integration matrix must include:

- Weekly cold start;
- standalone `THEMATIC + LONGFORM_SPECIAL` with SP001 as the required regression case;
- representative configured `RETROSPECTIVE_PERIOD` production/replay through existing `survey_period_v2` semantics;
- Foundations-guided Thematic/Longform scenario;
- structural monthly/half-year/annual and unplanned-Thematic compatibility.

Only after that real-production evidence may PFB-013/PFB-014 be closed.
