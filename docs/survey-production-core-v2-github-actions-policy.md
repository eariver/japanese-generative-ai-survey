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

Useful Actions-specific advantages include:

- reproducible controlled build environments;
- independent CI verification of committed artifacts;
- branch-protection integration;
- isolated release credentials / permissions;
- immutable or independently generated build artifacts;
- repeatable cross-regression execution;
- deterministic verification on relevant commits/PRs;
- release/freeze independence from the authoring session;
- an exact checked-out deterministic execution environment unavailable to a connector-only ChatGPT runtime.

`It is already a script`, `it can be automated`, or `we used a workflow before` are not sufficient reasons.

## 3. Appropriate Actions responsibilities

### CI and contract validation

Appropriate examples:

- unit/regression tests;
- schema/path/invariant checks;
- raw/provenance and exact-byte integrity;
- identifier/reference integrity;
- deterministic stage-contract verification;
- reproducible compiler/preflight checks.

### Reproducible builds

Actions may compile already-authored Weekly/Special publication source in a controlled toolchain, report deterministic findings/hashes/page counts and expose independently reproducible artifacts. It must not design or repair the publication.

### Freeze / release integrity

Actions may perform exact-byte Candidate/Preview/Freeze/Release checks, release-manifest validation, credential-isolated publishing and idempotent release reconciliation.

### Optional operator execution bridge

When direct exact local Core CLI execution is unavailable to the ChatGPT runtime, Actions may:

- check out one exact immutable request commit;
- execute only a schema-enumerated allowlist of existing deterministic Core operations;
- generate deterministic Profile/State/checkpoint/result authority already defined by canonical Core code;
- enforce Profile-bound edition-local write scope;
- commit exact deterministic outputs and receipts back to the same work branch.

The bridge must not accept request-supplied shell, Python, module, script, workflow or arbitrary executable identifiers. Its current authority is `docs/survey-production-core-v2-operator-execution-bridge.md`.

## 4. Work that remains with ChatGPT

Tasks requiring interpretation, synthesis, prioritization, semantic judgment, visual taste or Human decision remain owned by ChatGPT:

- Source Intake/search strategy;
- source-quality/materiality judgment;
- Screening/Evidence interpretation;
- Candidate Selection;
- Architecture;
- Drafting/Synthesis and `総括`;
- reader-facing manuscript/source authorship;
- Claim Boundary wording;
- Grok/X community disposition;
- retrospective trajectory/period interpretation;
- thematic lineage/historical attribution;
- semantic/editorial QA;
- exact-PDF visual QA;
- layout/content repair;
- preparation and recording of actual Human Gate decisions.

A deterministic helper or operator bridge may validate or advance already-authored artifacts; it must not silently become the editor.

## 5. Mechanical execution vs encoded editorial judgment

A process can be deterministic while still encoding editorial policy that should not be delegated.

Turning authored source into TeX or validating a schema can be mechanically appropriate. A generic script deciding how much prose survives, what information becomes reader-facing, where every chapter breaks, or which material is selected is editorial even if deterministic.

Therefore distinguish:

> **mechanically executable**

from

> **mechanically appropriate to delegate**.

The operator bridge is admitted because its allowlist is limited to Core mechanics whose semantics already exist independently of the workflow.

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

The operator bridge must be Profile/path driven and must not encode W33/SP001 topic names, fixed package taxonomies, fixed source-root depth, fixed `weekly/**` / `special/**` branch naming, Foundations volume structure, or annual trajectory choices.

Profile-specific Actions checks are acceptable only for crisp invariants and should prefer parameterized/shared verification over separate mutation workflows.

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
  schemas / hashes / provenance / references / preflight
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

Actions should answer crisp questions such as whether committed bytes reproduce and satisfy machine-verifiable invariants. They should not answer what the next article, paragraph, synthesis, Architecture choice, layout revision or Human decision should be.

## 8. PDF / typesetting boundary

Preferred publication loop:

```text
ChatGPT authors/edits publication source
-> ChatGPT reviews rendered PDF and makes semantic/layout decisions
-> candidate source is committed
-> Actions independently rebuilds/verifies
-> deterministic build/preflight PASS or FAIL
```

Avoid the retired anti-pattern where Actions builds, chooses a layout repair, mutates publication source, mutates quality state, and bot commits become the authoring loop.

## 9. Exact-byte/candidate/release guarantees

Reducing Actions-authored production logic does not weaken:

- exact source/PDF/Candidate binding;
- invalidation when source/PDF bytes change;
- reproducible build;
- Freeze/Release exact-byte identity;
- release credential isolation;
- idempotent Release reconciliation.

The bridge likewise must bind exact request/event/Profile/State authority and may not bypass these controls.

## 10. Workflow review classification

Retained/introduced workflows should fit one of these justified classes:

- `KEEP_AS_CI` — independent mechanical verification;
- `KEEP_AS_REPRODUCIBLE_BUILD` — controlled read-only build;
- `KEEP_AS_EXACT_BYTE_TRANSPORT_OR_RELEASE` — Preview/release integrity;
- `KEEP_AS_DETERMINISTIC_EXECUTION_SUBSTRATE` — exact checked-out Core mechanics unavailable to the primary runtime;
- `RETURN_TO_CHATGPT` — research/editorial/publication generation/correction;
- `LEGACY_REMOVE_CANDIDATE` — obsolete, one-off, edition-specific or superseded topology.

Every retained workflow must state the concrete Actions-specific benefit and remain narrow enough that no editorial ownership is transferred.

## 11. Evidence from W33 / SP001

The failed pre-redesign SP001/W33 runs showed that Actions-heavy authoring and mutation did not guarantee publication quality and created authority-rebinding/workflow-chaining problems.

The first clean post-redesign W33/SP001 attempts then showed the opposite operational edge: once authoring/mutation workflows were correctly removed, the normal connector-only ChatGPT runtime lacked a way to execute canonical deterministic local Core mechanics over the exact branch checkout. That evidence motivates the narrow fallback bridge, not restoration of the old production topology.

## 12. Relationship to publication quality

Machine checks are necessary but not sufficient. Keep separate:

- deterministic QA proved by scripts/Actions;
- semantic/editorial QA performed by ChatGPT;
- exact-PDF visual QA performed by ChatGPT.

Actions must never issue a semantic-quality PASS merely because schemas or known-token checks pass. Likewise the operator bridge may transport ChatGPT-authored agent review evidence but cannot create or reinterpret the underlying semantic/visual judgment.

## 13. Current implementation rule

The integrated redesign remains authoritative. The operator bridge is a shared-Core maintenance candidate and changes the audited Actions surface from six to seven workflows if accepted.

Therefore the prior six-workflow fixed-head audit is historical evidence only. The bridge candidate must receive fresh exact-head CI and the full changed-scope six-point fixed-head audit. If that audit requires any tree change, the entire fixed-head audit restarts from point 1.

After Human-reviewed integration, clean W33 and SP001 validation must restart from reviewed `main` and prove the bridge in real production before PFB-013/PFB-014 can close.
