# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY INDEX`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`

## 1. Purpose

The improvement branch intentionally preserves earlier design documents for auditability. Subsequent audits corrected parts of those documents, and later implementation audits added cross-cutting constraints that must survive Pilot integration.

This index makes the live-tree authority unambiguous without deleting the historical reasoning that led to each correction.

A continuation session working on Survey Production Core v2 must read this index before treating any other improvement document as current implementation guidance.

Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and merged. This index is authoritative only for work on the improvement branch.

## 2. Authority responsibilities

Authority is split by responsibility. Do **not** interpret the work log as a higher semantic-policy authority than the contract documents.

### 2.1 Repository reality

Actual repository files, committed artifacts, hashes, tests, and branch state are the highest factual authority. If documentation disagrees with repository reality, correct the documentation before relying on the stale statement.

### 2.2 Work-status authority

`docs/checkpoints/survey-production-core-v2-worklog.md` is authoritative only for:

- current phase / work-unit status;
- start/stop state;
- completed commits and validation notes;
- unresolved work;
- exact next action.

It is a checkpoint ledger, not the normative semantic contract.

### 2.3 Semantic/design authority

For architecture, contracts, Pilot semantics, Profile/Core ownership, Human Gates, provenance requirements, and acceptance criteria, use this precedence:

```text
1. repository reality
2. this authority index
3. whole-system audit + explicit remediation status recorded here
4. second-audit amendments
5. first-audit amendments
6. base Phase 0/1/2/3 design documents
7. historical/current-main implementation docs used as source evidence
```

A remediation status can change a finding from open to repaired only when implementation and regression evidence exist. It does not erase unrepaired requirements from the originating audit.

## 3. Document status map

| Document | Current authority status | Notes |
|---|---|---|
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE BASE PLAN` | overall goal/phases remain valid; later authorities control where explicitly different |
| `docs/survey-production-core-v2-component-inventory.md` | `SUPERSEDED IN PART` | process archaeology remains useful; semantic-neutrality conclusions corrected by audit amendment |
| `docs/survey-production-core-v2-component-inventory-audit-amendment.md` | `AUTHORITATIVE FOR PHASE 0 CORRECTION` | controls profile-pollution classification through Synthesis |
| `docs/survey-production-core-v2-contract-normalization.md` | `ACTIVE BASE CONTRACT / SUPERSEDED IN PART` | two-gate/temporal/release model remains; later amendments control identity/taxonomy |
| `docs/survey-production-core-v2-contract-normalization-second-audit-amendment.md` | `AUTHORITATIVE PHASE 1 AMENDMENT` | implementation identity, Finding taxonomy, Pilot entry, optional W33 reuse, Thematic closure |
| `docs/survey-production-core-v2-historical-invariants.md` | `ACTIVE INVARIANT CATALOG` | failure-driven durable invariants |
| `docs/survey-production-core-v2-historical-production-pattern-matrix.md` | `SUPERSEDED AS PHASE 2 EXIT EVIDENCE` | useful first-pass pattern summary; insufficient edition-depth by itself |
| `docs/survey-production-core-v2-historical-production-deep-audit.md` | `AUTHORITATIVE PHASE 2 EXIT EVIDENCE` | all 15 Specials audited at final-state production-lineage depth |
| `docs/survey-production-core-v2-minimum-vertical-slice.md` | `SUPERSEDED IN PART` | base Phase 3 reasoning retained, but not sufficient as current implementation contract |
| `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` | `SUPERSEDED IN PART BY SECOND AUDIT` | first correction remains valid except where later authorities conflict |
| `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md` | `AUTHORITATIVE PHASE 3 IMPLEMENTATION AMENDMENT` | current W33/SP001 Pilot implementation boundary |
| `docs/survey-production-core-v2-whole-system-audit-2026-08-22.md` | `AUTHORITATIVE CROSS-CUTTING AUDIT` | originating integrated-audit requirements; finding status is normalized in this index |
| `docs/survey-production-core-v2-whole-system-audit-remediation-closure.md` | `AUTHORITATIVE HISTORICAL REMEDIATION EVIDENCE` | records WU-008A remediation and WU-009 entry; later WU-010 re-audit status is controlled here |
| `docs/survey-production-core-v2-w33-artifact-disposition.md` | `ACTIVE SUPPORTING POLICY` | optional legacy benchmark/reuse policy; not a W33 acceptance contract |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL WORK CHECKPOINT` | status/progress/next action only; does not override semantic contracts |

## 4. Critical corrected rules

A continuation session must not recover superseded conclusions from older documents.

Current rules are:

1. `shared file format != shared semantic Core`.
2. Weekly semantics remain behind Weekly/Profile contracts rather than polluting generic Screening, Evidence, Matrix, Drafting, or Synthesis.
3. W33 is **Weekly Profile First Production Validation**.
4. The legacy W33 RC is an optional benchmark/provenance fixture; reuse is never a Pilot acceptance criterion.
5. A named completed Weekly issue remains deterministically initializable after a newer cutoff; W33 must not depend on legacy state merely because W34 is now eligible.
6. SP001 must perform true Thematic Research Expansion and closure/saturation auditing.
7. Profile-defined initial research obligations are first-class identity-bearing obligations and cannot be replaced by generic dimension-only completion rows.
8. A full production-capable v2 candidate is merged to `main` before external W33/SP001 production begins, even if an individual production session initially stops at Architecture Review.
9. Production provenance binds semantic contract identity **and** executable implementation identity **and** artifact byte identity.
10. Human Gate approval binds exact reviewed bytes. Architecture remains immutable `PROPOSED`; approval is an independent record.
11. A machine checkpoint may become `passed` only when implementation-controlled semantic validation produced an exact-byte Validation Attestation and Production State pins that attestation by path + SHA-256.
12. Production State is the sole lifecycle/gate authority and must itself be semantically reconstructable: lifecycle/history/checkpoints/gates/controller fields and their provenance must agree.
13. Action execution binds State/Profile plus transitive State-pinned checkpoint/gate authorities; changing authoritative stage input bytes invalidates the plan rather than silently changing execution basis.
14. `WORKFLOW_DISPATCH` is non-retryable by default. Retry requires explicit idempotency/reconciliation authority.
15. Pilot Finding scope and regression requirement are orthogonal fields; a Finding cannot become `CLOSED` without a closed Repair Set authority.
16. Candidate Selection is internal; normal Human Gates are Architecture Review and exact-byte Publication Preview.
17. Repository-owned production paths are repository-confined; absolute/traversal escape is invalid.
18. Frozen historical releases remain unchanged.

## 5. Cross-cutting finding status

### 5.1 Repaired before the WU-010 Human re-audit

- **AUD-001 / WU-010 — REPAIRED, then strengthened by WU-010R.** Architecture Review uses immutable proposed Architecture bytes plus independent Approval Record. WU-010R additionally requires semantic checkpoint attestation and State-pinned gate provenance so exact-byte approval cannot bless semantically unvalidated bytes.
- **AUD-011 / WU-010 — REPAIRED.** State-pinned implementation identity survives artifact-only commits while committed/staged/unstaged/untracked implementation-control drift fails closed.

### 5.2 Human re-audit remediation — WU-010R

These findings were opened by the Human re-audit after the first WU-010 closure. They are mandatory before WU-011 starts. Work-status completion is recorded only in the worklog after focused and cross-regression validation.

- **AUD-013 / P0** — semantic checkpoint / Human Gate attestation. Required outcome: handler success alone never advances a checkpoint; exact semantic Validation Attestation is required and Gate approval consumes the attested/reviewed bytes.
- **AUD-014 / P0** — Production State self-consistency/provenance. Required outcome: lifecycle/history/checkpoint/gate/controller semantics are fail-closed and State pins exact checkpoint/gate authority bytes.
- **AUD-015 / P1, P0 before autonomous provenance reliance** — Action Spec stage-input provenance. Required outcome: the action basis includes State/Profile plus transitive exact State-pinned stage authorities so stage-input drift invalidates the action identity/plan.
- **AUD-016 / P1, P0 before external dispatch wiring** — retry/idempotency. Required outcome: retry is action-kind/stage-specific; external dispatch is not blindly repeated after ambiguous failure.
- **AUD-017 / P1 — REPAIRED BY THIS AUTHORITY UPDATE.** This index, not the worklog, now normalizes AUD-001/AUD-011 as repaired and records AUD-013–AUD-018 explicitly.
- **AUD-018 / P2, P1 before Pilot feedback loop** — Finding/Repair closure governance. Required outcome: standalone Finding closure is invalid; a closed Repair Set with validation authority is required.

### 5.3 Still open for WU-011 / pre-Pilot integration

- **AUD-003 / WU-011 with WU-006 hardening** — Discovery graph resolution, structured discovery trigger/method provenance, accepted Raw byte identity.
- **AUD-004 / WU-011** — common fail-closed JSON Schema conformance before semantic validators/model or external artifact acceptance.
- **AUD-005 / before Pilot** — bounded item-level review-attention surface for excluded/held/non-material/duplicate decisions with explicit overflow.
- **Publication Preview exact-byte authority / WU-011** — exact publication-candidate PDF bytes must remain bound through Publication Preview, Visual Review, Freeze, merge verification and Release.
- **Pilot handler/bootstrap wiring / WU-011** — settled W33/SP001 stage handlers, workflow dispatches and assistant-control/allowlist integration.

WU-011 must not start until WU-010R is marked complete after the required regression and re-audit sequence.

## 6. Negative-design rules that remain active

Drafting, Synthesis and orchestration must preserve the corrected architecture:

- no generic `late_breaking` field;
- no generic `this_week` synthesis payload;
- Draft basis binds independently authorized Architecture bytes; do not depend on self-mutated `APPROVED` Architecture semantics;
- Evidence refs, attribution/subject boundaries, must-cover requirements and explicit limitations survive into Draft validation;
- Profile semantics remain Profile-owned;
- Publication semantics remain Publication Profile-owned;
- handler success is not validation authority;
- worklog status is not semantic authority;
- artifact-only HEAD movement never silently changes the State-pinned implementation authority.

## 7. Avoid amendment-chain growth

These amendments/audits are temporary design-history scaffolding.

After W33/SP001 and second validation stabilize the design:
- consolidate the active Core/Profile contracts;
- mark base/amendment/audit documents as historical design evidence where appropriate;
- point `AGENTS.md` and bootstrap docs to a small canonical contract set;
- do not create a permanent `v2/v3/...` documentation repair chain analogous to the old Special runtime repair chain.

## 8. Resume rule

Before starting or continuing a work unit:

```text
read current main
-> read worklog for status/next action
-> read this index for semantic authority
-> read authoritative documents/audit constraints for the active WU
-> verify repository reality
-> update worklog IN_PROGRESS
-> perform work
-> validate
-> record commit/next action
```
