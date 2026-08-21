# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY INDEX`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`

## 1. Purpose

The improvement branch intentionally preserves earlier design documents for auditability. Two pre-implementation audits later corrected parts of those documents.

This index makes the live-tree authority unambiguous without deleting the historical reasoning that led to the correction.

A continuation session working on Survey Production Core v2 must read this index before treating any other improvement document as current implementation guidance.

Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and merged. This index is authoritative only for work on the improvement branch.

## 2. Authority responsibilities

Authority is split by responsibility. Do **not** interpret the work log as a higher semantic-policy authority than the contract documents.

### 2.1 Repository reality

Actual repository files, committed artifacts, hashes, tests, and branch state are the highest factual authority. If documentation disagrees with repository reality, correct the documentation first.

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
1. this authority index
2. second-audit amendments
3. first-audit amendments
4. base Phase 0/1/2/3 design documents
5. historical/current-main implementation docs used as source evidence
```

The work log may summarize these rules but may not override them.

## 3. Document status map

| Document | Current authority status | Notes |
|---|---|---|
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE BASE PLAN` | overall goal/phases remain valid; later amendments control where explicitly different |
| `docs/survey-production-core-v2-component-inventory.md` | `SUPERSEDED IN PART` | process archaeology remains useful; semantic-neutrality conclusions are corrected by the audit amendment |
| `docs/survey-production-core-v2-component-inventory-audit-amendment.md` | `AUTHORITATIVE FOR PHASE 0 CORRECTION` | controls profile-pollution classification through Synthesis |
| `docs/survey-production-core-v2-contract-normalization.md` | `ACTIVE BASE CONTRACT / SUPERSEDED IN PART` | two-gate/temporal/release model remains; implementation identity and taxonomy are amended below |
| `docs/survey-production-core-v2-contract-normalization-second-audit-amendment.md` | `AUTHORITATIVE PHASE 1 AMENDMENT` | implementation identity, Finding taxonomy, Pilot entry, optional W33 reuse, Thematic closure |
| `docs/survey-production-core-v2-historical-invariants.md` | `ACTIVE INVARIANT CATALOG` | failure-driven durable invariants |
| `docs/survey-production-core-v2-historical-production-pattern-matrix.md` | `SUPERSEDED AS PHASE 2 EXIT EVIDENCE` | useful first-pass pattern summary; insufficient edition-depth by itself |
| `docs/survey-production-core-v2-historical-production-deep-audit.md` | `AUTHORITATIVE PHASE 2 EXIT EVIDENCE` | all 15 Specials audited at final-state production-lineage depth; not a claim that every historical intermediate artifact was reread |
| `docs/survey-production-core-v2-minimum-vertical-slice.md` | `SUPERSEDED IN PART` | base Phase 3 reasoning retained, but not sufficient as current implementation contract |
| `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` | `SUPERSEDED IN PART BY SECOND AUDIT` | first correction remains valid except where second amendment conflicts; legacy W33 compatibility wording inside it is superseded |
| `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md` | `AUTHORITATIVE PHASE 3 IMPLEMENTATION AMENDMENT` | current Pilot/implementation boundary |
| `docs/survey-production-core-v2-w33-artifact-disposition.md` | `ACTIVE SUPPORTING POLICY` | optional legacy benchmark/reuse policy; not a W33 acceptance contract |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL WORK CHECKPOINT` | status/progress/next action only; does not override semantic contracts |

## 4. Critical corrected rules

A continuation session must not recover superseded conclusions from older documents.

Current rules are:

1. `shared file format != shared semantic Core`.
2. Weekly semantics currently pollute Screening through Synthesis and must move behind Profile contracts.
3. W33 is **Weekly Profile First Production Validation**.
4. The legacy W33 RC is an optional benchmark/provenance fixture; reuse is never a Pilot acceptance criterion.
5. SP001 must perform true Thematic Research Expansion and closure/saturation auditing.
6. A full production-capable v2 candidate is merged to `main` before external W33/SP001 production begins, even if an individual production session initially stops at Architecture Review.
7. Production provenance binds semantic contract identity **and** executable implementation identity **and** artifact byte identity.
8. Pilot Finding scope and regression requirement are orthogonal fields.
9. Candidate Selection is internal; normal Human Gates are Architecture Review and exact-byte Publication Preview.
10. Frozen historical releases remain unchanged.

## 5. Avoid amendment-chain growth

These amendments are temporary design-history scaffolding.

After W33/SP001 and second validation stabilize the design:
- consolidate the active Core/Profile contracts;
- mark base/amendment documents as historical design;
- point `AGENTS.md` and bootstrap docs to a small canonical contract set;
- do not create a permanent `v2/v3/...` documentation repair chain analogous to the old Special runtime repair chain.

## 6. Resume rule

Before starting or continuing a work unit:

```text
read current main
-> read worklog for status/next action
-> read this index for semantic authority
-> read authoritative documents for the active WU
-> verify repository reality
-> update worklog IN_PROGRESS
-> perform work
-> validate
-> record commit/next action
```
