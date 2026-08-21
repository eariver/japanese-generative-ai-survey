# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY INDEX`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`

## 1. Purpose

The improvement branch intentionally preserves earlier design documents for auditability. Two pre-implementation audits later corrected parts of those documents.

This index makes the live-tree authority unambiguous without deleting the historical reasoning that led to the correction.

A continuation session working on Survey Production Core v2 must read this index before treating any other improvement document as current implementation guidance.

Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and merged. This index is authoritative only for work on the improvement branch.

## 2. Precedence

Use this order when documents conflict:

```text
1. docs/checkpoints/survey-production-core-v2-worklog.md
2. this authority index
3. second-audit amendments
4. first-audit amendments
5. base Phase 0/1/2/3 design documents
6. historical/current-main implementation docs used as source evidence
```

Repository reality still wins if any document disagrees with actual files/state.

## 3. Document status map

| Document | Current authority status | Notes |
|---|---|---|
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE BASE PLAN` | overall goal/phases remain valid; W33 section already states migration is not primary acceptance |
| `docs/survey-production-core-v2-component-inventory.md` | `SUPERSEDED IN PART` | process archaeology remains useful; semantic-neutrality conclusions are corrected by the audit amendment |
| `docs/survey-production-core-v2-component-inventory-audit-amendment.md` | `AUTHORITATIVE FOR PHASE 0 CORRECTION` | controls profile-pollution classification through Synthesis |
| `docs/survey-production-core-v2-contract-normalization.md` | `ACTIVE BASE CONTRACT / SUPERSEDED IN PART` | two-gate/temporal/release model remains; implementation identity and taxonomy are amended below |
| `docs/survey-production-core-v2-contract-normalization-second-audit-amendment.md` | `AUTHORITATIVE PHASE 1 AMENDMENT` | implementation identity, Finding taxonomy, Pilot entry, optional W33 reuse, Thematic closure |
| `docs/survey-production-core-v2-historical-invariants.md` | `ACTIVE INVARIANT CATALOG` | failure-driven durable invariants |
| `docs/survey-production-core-v2-historical-production-pattern-matrix.md` | `SUPERSEDED AS PHASE 2 EXIT EVIDENCE` | useful first-pass pattern summary; insufficient edition-depth by itself |
| `docs/survey-production-core-v2-historical-production-deep-audit.md` | `AUTHORITATIVE PHASE 2 EXIT EVIDENCE` | all 15 Specials audited at final-state production-lineage depth |
| `docs/survey-production-core-v2-minimum-vertical-slice.md` | `SUPERSEDED IN PART` | base Phase 3 reasoning retained, but not sufficient as current implementation contract |
| `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` | `SUPERSEDED IN PART BY SECOND AUDIT` | first correction remains valid except where second amendment conflicts |
| `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md` | `AUTHORITATIVE PHASE 3 IMPLEMENTATION AMENDMENT` | current Pilot/implementation boundary |
| `docs/survey-production-core-v2-w33-artifact-disposition.md` | `ACTIVE SUPPORTING POLICY` | optional legacy benchmark/reuse policy; not a W33 acceptance contract |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL WORK CHECKPOINT` | current status and next action |

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
-> read worklog
-> read this index
-> read the authoritative documents for the active WU
-> verify repository reality
-> update worklog IN_PROGRESS
-> perform work
-> validate
-> record commit/next action
```
