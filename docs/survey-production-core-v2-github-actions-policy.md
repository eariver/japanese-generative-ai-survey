# Survey Production Core v2 — GitHub Actions Responsibility Policy

Status: `FOLLOW-UP REVIEW TRUST-BOOTSTRAP REPAIR / DEFAULT-BRANCH ISSUE-COMMENT AUTHORITY / REAUDIT PENDING`  
Established: 2026-08-23 JST  
Updated: 2026-08-24 JST

## 1. Governing principle

> **GitHub Actions is a deterministic executor/verifier, not a research, editorial, visual, or Human-decision agent.**

Actions is justified only where it supplies concrete mechanical value unavailable or better isolated there: independent CI, reproducible build, exact-byte transport, credential-isolated release, or a trusted exact-checkout Core execution substrate.

## 2. Trust-root requirement

A work branch is untrusted until admitted. Therefore no workflow definition supplied by that work branch may decide that the same branch's Core/workflow/config bytes are acceptable or acquire write authority as part of that decision.

For operator execution the trusted initiation path is:

```text
ChatGPT pushes one request-only commit as exact work-branch head
-> ChatGPT comments on operator queue Issue #448:
     /survey-core-execute <exact-request-commit-sha>
-> survey-production-v2-operator-bridge.yml loaded from default-branch issue_comment authority
   -> read-only trusted operator-preflight treats request SHA/branch as data
   -> dependent write-capable operator-execute only after PASS
```

There is no work-branch signal workflow and no `workflow_run` trust hop. `pipeline-contract-tests.yml` remains independent CI only.

Trusted preflight obtains the protected-path authority from the named `reviewed_main_sha` config, never from the untrusted branch config being admitted. It also requires the supplied SHA to be the exact current canonical work-branch head and rechecks that head before execution; output push uses `force-with-lease` against the admitted SHA.

Issue #448 is deterministic transport only. It is not a Human Gate and free-form issue comments are not executable authority. Only the exact machine trigger syntax is recognized; the immutable request JSON remains the operation authority.

## 3. Appropriate Actions responsibilities

Actions may perform:

- Core/schema/regression CI;
- reproducible Weekly/Special build;
- exact Candidate PDF Preview transport;
- frozen-byte release and reconciliation;
- trusted execution of one schema-enumerated deterministic operator request after default-branch preflight.

Operator execution may initialize generic Weekly/configured Retrospective/Thematic State, adopt one validated lifecycle stage, or record an already explicit Human Gate decision and its deterministic lifecycle consequence.

Configured Retrospective initialization reuses the **existing `survey_period_v2`** builder. It does not create cadence-specific engines.

## 4. Work that remains outside Actions

ChatGPT owns research strategy, source quality/materiality judgment, Evidence interpretation, Selection, Architecture, drafting/synthesis, reader-facing authorship, semantic/editorial QA, exact-PDF visual QA, requested repair implementation, and Exception-Gate judgment.

The Human owns `APPROVED` vs `REQUEST_CHANGES`, requested changes, and regeneration boundary.

Actions/Core may validate and record that explicit input. They may not choose or reinterpret it.

## 5. Operator request surface

Exactly eight operation kinds are allowed:

- `INITIALIZE_WEEKLY`
- `INITIALIZE_RETROSPECTIVE`
- `INITIALIZE_THEMATIC`
- `ADVANCE_STAGE`
- `RECORD_ARCHITECTURE_APPROVAL`
- `REQUEST_ARCHITECTURE_REVISION`
- `RECORD_PUBLICATION_PREVIEW_APPROVAL`
- `REQUEST_PUBLICATION_PREVIEW_REVISION`

Arbitrary command, script, module, workflow, generic decision, or rejection surfaces are prohibited.

## 6. Human review provenance

Before either normal Human Gate is presented, the exact review surface must be committed **and retained on the canonical Profile work branch**.

Canonical Human Gate Core requires the reviewed commit to:

- exist;
- remain reachable from the canonical work branch;
- exact-bind current reviewed State and Gate inputs;
- for Publication Preview, exact-bind the Candidate-bound PDF.

Connector-safe execution additionally requires the reviewed commit to equal the request-only commit parent.

Every approval writes an immutable rN approval snapshot under `gates/reviews/approvals/`, so later dependency-aware reopening can supersede active canonical approval without destroying historical decision evidence.

## 7. Dependency-aware Human revision

Architecture Review may return to any allowed pre-Architecture boundary.

Publication Preview may return to:

- publication-local boundaries while preserving active Architecture approval; or
- an upstream Evidence/Selection/etc. boundary when Human feedback reveals an upstream defect.

If Publication Preview returns before `ARCHITECTURE_ESTABLISHED`, Core must supersede the active canonical Architecture approval after verifying its provenance, keep the immutable historical approval snapshot, mark Architecture Review pending, and require a new Architecture revision before publication continues.

Routine cross-gate correction is not a third Human Gate and not an Owner Exception Gate.

## 8. Current seven-workflow surface

1. `pipeline-contract-tests.yml` — read-only full repository regression CI.
2. `survey-production-v2-ci.yml` — focused Core regression.
3. `build-weekly-survey.yml` — read-only reproducible build.
4. `build-special-pdf.yml` — read-only reproducible build.
5. `survey-production-v2-export-publication-preview.yml` — exact Preview transport.
6. `survey-production-v2-release.yml` — exact-byte Release.
7. `survey-production-v2-operator-bridge.yml` — trusted default-branch `issue_comment` operator preflight/execution.

No eighth workflow is introduced by the trust fix.

## 9. Lifecycle boundary

Ordinary lifecycle stages remain local deterministic Core mechanics. `FROZEN -> RELEASED` remains the only lifecycle `WORKFLOW_DISPATCH` edge.

The trusted operator executor is an execution substrate for local mechanics, not a new lifecycle handler.

## 10. Acceptance

The earlier candidate `9932c8b7a14f1c3bdcc775df88056681b2841514` and its 7/7 audit are invalidated by follow-up review.

An intermediate read-only work-branch signal + default-branch `workflow_run` design is also superseded historical diagnosis, not current authority.

The repaired candidate must pass exact-head Core CI + pipeline contracts and a fresh seven-point audit from Point 1. That audit must explicitly inspect:

- default-branch `issue_comment` trust bootstrap and Issue #448 trigger scope;
- exact current work-branch-head/race fail-closed behavior;
- reviewed-commit branch reachability/durability;
- Publication Preview upstream revision reopening Architecture;
- preservation of immutable historical approval evidence.

Only a fresh 7/7 fixed-head PASS may return PR #447 to Human full-candidate review.
