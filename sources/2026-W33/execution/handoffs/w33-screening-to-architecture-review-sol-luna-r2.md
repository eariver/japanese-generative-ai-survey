# 2026-W33 Sol/Luna production plan — Screening to Architecture Review r2

Status: `SOL_PLAN / PHASE-BOUND LUNA EXECUTION / STOP AT ARCHITECTURE_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at plan creation: `DISCOVERY_COLLECTED`  
Current machine next action: `stage:screening`  
Requested Human stop: `ARCHITECTURE_REVIEW`

This document defines the operating split between Sol and Luna from the current Screening stage through the Architecture Review Human Gate. It is deliberately crash-resilient: each phase is bounded, repository-recorded, reviewed before lifecycle advancement, and restartable from repository authority without chat history.

## 1. Role contract

### Sol owns

Sol is the semantic and editorial authority before the Human Gate. Sol must:

- define the research scope and stage-specific policy before each Luna run;
- freeze allowed sources, evidence hierarchy, duplicate/carry-over handling, and unresolved questions when those choices matter;
- define the exact Luna task, allowed writes, stopping condition, and review criteria;
- review Luna output against source meaning, issue materiality, weekly policy, and Core invariants;
- reject or request bounded repair when Luna output changes meaning, exceeds scope, loses provenance, or resolves ambiguity without authority;
- approve a candidate for deterministic lifecycle advancement only after semantic review passes;
- define Selection and Architecture decisions; these are not delegated editorial judgments.

Sol does not use Luna as a substitute decision-maker. Luna may organize and execute a policy, but Sol authors the policy and decides whether the result is acceptable.

### Luna owns

Luna is the bounded execution and collection worker. Luna may:

- perform source-local information collection from sources explicitly allowed by Sol;
- organize collected information according to Sol-defined categories and schemas;
- materialize schema-conforming Core packages/results/accepted artifacts from frozen Sol decisions;
- execute deterministic repository scripts, validators, checksums, Git operations, and Core lifecycle commands that Sol has explicitly authorized;
- create work records with exact starting/ending SHAs, changed paths, counts, hashes, validation results, and unresolved items.

Luna must not:

- broaden scope or add opportunistic topics/sources;
- convert community/X signals into technical authority;
- make cross-source editorial judgments not specified by Sol;
- independently decide Materiality, Selection, carry-over disposition, single-home policy, or issue Architecture;
- resolve ambiguous identity/date/source conflicts by guess;
- advance a lifecycle stage before the current Luna candidate has passed Sol review, unless a specific Sol handoff explicitly says that a previously reviewed candidate is approved for advancement.

### Human owns

The user is the Human Architecture Review authority. A Sol review pass means “ready for Human review,” not Human approval.

## 2. Global execution pattern

Every stage from Screening through Architecture uses the same two-step commit/review pattern.

### A. Candidate/materialization step

1. Sol reads current repository authority and writes a bounded phase handoff.
2. Luna starts from the exact named branch SHA.
3. Luna performs only the allowed collection/organization/tool execution.
4. Luna commits the candidate artifacts plus a Luna session record.
5. Luna stops before lifecycle advancement.

### B. Sol review and advancement step

6. Sol reviews exact committed bytes and writes a Sol review record.
7. If review fails, Sol writes a bounded repair delta; Luna repairs only the rejected scope and stops again for review.
8. If review passes, Sol marks the candidate `APPROVED_FOR_CORE_ADVANCEMENT` in the review record or next handoff.
9. Luna executes deterministic Core checkpoint/validation/`ADVANCE_STAGE` operations only for that reviewed candidate and records the resulting SHA/state.
10. Sol verifies the resulting Production State and starts policy preparation for the next stage.

Where the Core implementation itself creates accepted artifacts during the deterministic operation, the same principle applies: semantic bytes/inputs must already be frozen and Sol-reviewed before state advancement, and the resulting accepted artifacts are verified immediately afterward.

## 3. Crash-recovery discipline

At all times:

- `sources/2026-W33/execution/index.md` is the recovery entry point.
- Every Sol policy/handoff is committed under `sources/2026-W33/execution/handoffs/`.
- Every Luna run is committed under `sources/2026-W33/execution/sessions/` with starting SHA, ending SHA, exact changed paths, hashes/counts, validators, and stop reason.
- Every Sol semantic review is committed under `sources/2026-W33/execution/reviews/` and references the exact Luna commit reviewed.
- Candidate materialization and lifecycle advancement should be separate commits whenever repository tooling permits.
- A phase is never considered complete merely because chat says it is complete.
- On restart, read Production State, execution index, latest phase handoff, latest Luna session, and latest Sol review before doing any work.

If a session crashes after Luna commits a candidate but before Sol review, restart at Sol review. If it crashes after Sol review pass but before advancement, restart at deterministic advancement. Do not re-run collection unless the repository evidence shows the candidate is missing or invalid.

## 4. Phase S — Screening materialization

### Current frozen semantic authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- Discovery record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Sol Screening seed: `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- Semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- Semantic-authority Git blob: `ba649d6e805bac5316b88a78d259a3de97f839b2`
- Expected aggregate: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4
- Session-local expected result-set id for verification only: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`

### Luna task S1 — materialize only

Sol will provide an exact starting SHA. Luna must:

1. Read current reviewed-main Core instructions, Screening schemas, Screening runner, Production State, r6, r7, and this plan.
2. Adapt the exact Sol seed into the current runner wrapper without changing any decision, reason, duplicate group, or verification target.
3. Run the current Screening materialization path.
4. Produce the current-Core Screening package, batch input(s), batch result(s), accepted result-set artifact, interactive input, and audit artifacts at the canonical paths chosen by the current implementation.
5. Validate complete ID coverage and the 26/8/3/4 aggregate.
6. Verify the content-addressed identity against the expected r7 value; if it differs, do not force it. Record the exact generated identity and the deterministic reason for the difference, then stop for Sol review.
7. Commit only Screening materialization outputs and the Luna session record.
8. Do not modify Production State and do not run `ADVANCE_STAGE`.

### Sol review S2

Sol reviews:

- exact 41-ID correspondence to the semantic seed;
- decision/reason/verification-target bindings;
- duplicate-group fidelity;
- package/result/acceptance consistency;
- absence of unauthorized semantic transformation;
- accepted result-set identity and provenance;
- changed-path boundary.

If pass, Sol authorizes Luna to run Screening checkpoint/validation and advance from `DISCOVERY_COLLECTED` to `CANDIDATES_NORMALIZED`.

## 5. Phase E — Evidence / Materiality / Completeness

Core next handler after Screening is `stage:evidence-materiality-completeness` and the next lifecycle state is `EVIDENCE_REVIEWED`.

This phase combines collection work with semantic policy, so Sol must prepare the policy before Luna collects anything.

### Sol task E0 — evidence policy specification

After Screening advancement, Sol must inspect the reviewed Screening output and define:

- which KEEP items require full Evidence work;
- exact bounded verification questions for each MAYBE and INSPECT item;
- DROP items that are excluded from further Evidence work;
- duplicate-group handling and candidate identity boundaries;
- source authority hierarchy for each subject, preferring first-party/primary authority where available;
- how publication date, event date, model/release identity, and carry-over ambiguity must be resolved;
- weekly current-relevance and technical-significance criteria;
- X/community material as discovery/context only, never technical fact authority;
- source-specific attribution requirements and unresolved questions that must remain unresolved if evidence is insufficient;
- expected artifact classes and allowed write paths.

Sol then commits an Evidence-phase handoff with the exact approved sources or source classes and task matrix.

### Luna task E1 — bounded collection and organization

Luna may then:

- retrieve/read the exact allowed sources;
- capture source-local facts needed by the Evidence tasks;
- resolve factual identity/date questions only where the approved source directly supports the resolution;
- preserve conflicts/unknowns rather than infer across documents;
- materialize Evidence cards/tasks/results, edition evidence views, Materiality ledger, and Profile Completeness result under current schemas and Sol policy;
- run deterministic validators/checksums;
- commit candidate artifacts plus a Luna session record;
- stop before lifecycle advancement.

Luna must not decide final weekly materiality merely from the collected facts. The Materiality ledger may encode Sol-defined criteria and source-supported observations, but editorial disposition remains subject to Sol review.

### Sol review E2

Sol reviews:

- source-to-claim binding and provenance;
- whether first-party claims remain attributed where appropriate;
- whether X/community statements were prevented from becoming technical authority;
- INSPECT/MAYBE resolution quality and whether unresolved cases should remain unresolved;
- duplicate/carry-over treatment;
- weekly relevance/significance judgments;
- completeness coverage against the research profile;
- whether evidence is sufficient for Selection without overclaiming.

If pass, Sol authorizes Luna to execute the evidence/materiality/completeness checkpoint and advance to `EVIDENCE_REVIEWED`.

## 6. Phase L — Selection

Core next handler is `stage:selection`; next state is `SELECTION_COMPLETE`.

### Sol task L0 — selection policy and decisions

Using only Sol-reviewed Evidence, Sol decides:

- publication candidates versus watchlist/carry-over/exclusion;
- relative materiality and issue-level balance;
- duplicate collapse and canonical representative;
- late-breaking single-home handling;
- carry-over disposition;
- what is sufficiently established to appear in the weekly issue;
- any residual uncertainty that must be visible to Architecture rather than silently resolved.

Sol writes a bounded Selection handoff containing the frozen selection decisions and required matrix relationships.

### Luna task L1 — selection materialization

Luna:

- organizes the frozen Sol decisions into the current candidate matrix and candidate selection schemas;
- preserves exact Evidence references and provenance;
- runs deterministic Selection validation;
- records counts and changed paths;
- commits the candidate plus a Luna session record;
- stops before lifecycle advancement.

Luna does not change a Sol selection decision for balance, novelty, perceived importance, or convenience.

### Sol review L2

Sol checks:

- matrix-to-Evidence traceability;
- exact fidelity to frozen selection decisions;
- weekly materiality balance;
- duplicate/single-home/carry-over consistency;
- no selected candidate lacking adequate reviewed Evidence.

If pass, Sol authorizes Luna to execute the Selection checkpoint and advance to `SELECTION_COMPLETE`.

## 7. Phase A — Architecture

Core next handler is `stage:architecture`; successful advancement reaches `ARCHITECTURE_ESTABLISHED`, which triggers the `ARCHITECTURE_REVIEW` Human Gate.

Required gate inputs under current Core are:

- `sources/2026-W33/architecture-v2.json`
- `sources/2026-W33/architecture-review-summary-v2.json`
- `sources/2026-W33/architecture-review-attention-v2.json`

### Sol task A0 — architecture policy

Sol defines the issue architecture from the reviewed Selection, including:

- article/section grouping and hierarchy;
- lead versus secondary material;
- relationships between selected developments;
- reader-facing weekly narrative and “why this issue” logic;
- handling of watchlist/carry-over/residual uncertainty;
- placement rules that prevent duplicate coverage;
- source/evidence boundaries that the later drafting stage must preserve;
- review-attention items that the Human reviewer should explicitly inspect.

Architecture is an editorial decision and is not delegated to Luna.

Sol commits the frozen Architecture specification/handoff before Luna writes gate artifacts.

### Luna task A1 — architecture artifact materialization

Luna:

- translates the exact Sol architecture specification into the three current Core Architecture gate artifacts;
- preserves candidate/Evidence references and ordered structure;
- materializes review summary and review-attention data exactly from Sol policy plus repository facts;
- runs the current Architecture validator;
- commits the candidate gate artifacts and Luna session record;
- stops before lifecycle advancement.

### Sol review A2

Sol reviews all three gate artifacts for:

- fidelity to the frozen Architecture policy;
- coherent issue narrative and section hierarchy;
- complete mapping of selected candidates;
- absence of duplicate or unsupported placement;
- correct uncertainty/carry-over treatment;
- useful and complete Human review-attention notes;
- schema/validator cleanliness and exact changed-path boundary.

If any semantic issue exists, Sol issues a bounded repair handoff and Luna revises only the affected artifacts.

### Luna task A3 — gate advancement after Sol pass

Only after Sol has committed an Architecture review pass may Luna execute the deterministic Architecture checkpoint/`ADVANCE_STAGE` operation.

Expected resulting Production State:

- lifecycle: `ARCHITECTURE_ESTABLISHED`
- Human gate: `ARCHITECTURE_REVIEW`
- terminal/stop behavior: stop for Human review according to current Core

Luna records the resulting commit SHA, Production State, checkpoint provenance, and changed paths.

### Sol task A4 — final pre-Human verification

Sol performs one final read-only verification that:

- the branch contains the exact Sol-reviewed Architecture bytes;
- Core recorded the Architecture checkpoint and Human Gate correctly;
- no Draft-stage artifacts were created;
- no work proceeded beyond the requested Human stop.

Sol then presents the Architecture Review package to the user. The user performs the Human review.

## 8. Repair and Exception Gate policy

A Luna failure is not automatically an Exception Gate.

Use bounded repair when the problem is:

- schema formatting;
- missing allowed-source capture;
- deterministic validation failure;
- incorrect file path/provenance link;
- a semantic mismatch between frozen Sol instructions and Luna materialization.

Return to Sol policy work when:

- evidence exposes a materially different identity/date/relationship than assumed;
- an INSPECT/MAYBE question cannot be resolved under the allowed evidence;
- selection balance or Architecture must change because reviewed evidence changed.

Use the Human Exception Gate only when a genuine editorial/owner decision cannot safely be derived from repository authority. Do not use it to avoid routine research or repair.

## 9. Immediate next step

The next phase is **S1 Screening materialization**. Sol must first instantiate a bounded Luna handoff from this plan using the exact current branch SHA. Luna then materializes Screening outputs and stops for Sol review.

No Evidence collection should begin until Screening has passed Sol review and Core has recorded `CANDIDATES_NORMALIZED`.
