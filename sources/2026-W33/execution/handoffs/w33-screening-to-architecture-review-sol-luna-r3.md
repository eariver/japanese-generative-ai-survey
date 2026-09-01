# 2026-W33 Sol/Luna production plan — Screening to Architecture Review r3

Status: `SOL_POLICY / LUNA_ANALYSIS_AND_PROPOSAL / SOL_SEMANTIC_ACCEPTANCE / STOP_AT_ARCHITECTURE_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Plan base commit: `df6a29bdd2354fa439a7a6c01fae14694fb62164`  
Current lifecycle at plan creation: `DISCOVERY_COLLECTED`  
Current machine next action: `stage:screening`  
Requested Human stop: `ARCHITECTURE_REVIEW`

This r3 plan supersedes r2 as the current Sol/Luna operating authority from Screening through Architecture Review. r2 remains immutable historical provenance. The main amendment is that Luna is not restricted to mechanical materialization for Materiality, Selection, or Architecture: once Sol has fixed the policy, rubric, constraints, allowed evidence, and required outputs, Luna may analyze the reviewed evidence and produce reasoned proposals. Sol remains the semantic acceptance authority before the Human Gate.

## 1. Governing division of responsibility

The operating model is:

`Sol policy/rubric/constraints -> Luna collection/analysis/proposal/materialization -> Sol semantic review -> Luna deterministic advancement -> next Sol policy`

### Sol owns

Sol is responsible for defining the decision space and accepting or rejecting Luna's proposed result. Sol must:

- define stage scope, research questions, policy, rubric, constraints, and stopping conditions before each Luna run;
- freeze source authority, allowed source classes, evidence hierarchy, attribution rules, duplicate/carry-over rules, and unresolved-question handling where relevant;
- define what Luna may infer from source-local facts and what must remain unresolved;
- define the expected proposal schema or decision dimensions for Materiality, Selection, and Architecture;
- review Luna proposals against source meaning, weekly editorial policy, Core invariants, and cross-candidate consistency;
- accept, modify, or reject Luna proposals and freeze the reviewed semantic result before lifecycle advancement;
- decide whether a genuine Exception Gate is required;
- present the final Sol-reviewed Architecture package to the Human reviewer.

Sol does not need to generate every item-level judgment from scratch when the decision criteria are already explicit. Luna may perform first-pass reasoning under the frozen criteria; Sol is responsible for semantic acceptance.

### Luna owns

Luna is the bounded research, analysis, proposal, materialization, and execution worker. Within an exact Sol handoff, Luna may:

- collect source-local information from the exact sources or source classes allowed by Sol;
- organize facts according to Sol-defined categories and current Core schemas;
- evaluate items against Sol-defined rubrics;
- propose Materiality ratings/dispositions, INSPECT/MAYBE resolutions, Selection outcomes, duplicate/carry-over handling, and Architecture structures when requested by Sol;
- provide reasoning, confidence, evidence references, unresolved questions, and alternative proposals where ambiguity remains;
- materialize schema-conforming Core packages/results/accepted artifacts after the semantic proposal is frozen or where the current runner itself is the prescribed representation;
- execute deterministic validators, checksums, Git operations, and Core lifecycle commands explicitly authorized by Sol;
- create exact work records with starting/ending SHAs, changed paths, hashes/counts, validation results, proposal summaries, unresolved items, and stop reason.

Luna must not:

- broaden scope or add opportunistic topics/sources outside Sol policy;
- silently change the rubric or invent new editorial criteria;
- convert X/community signals into technical authority;
- resolve unsupported identity/date/source conflicts by guess;
- treat its proposal as final authority before Sol review;
- advance lifecycle before Sol has accepted the semantic candidate, unless the handoff explicitly authorizes advancement of an already reviewed candidate;
- infer Human Gate approval.

### Human owns

The user is the Architecture Review authority. A Sol semantic review pass means `READY_FOR_HUMAN_REVIEW`, not Human approval.

## 2. Proposal contract

Whenever Luna is asked to make a semantic proposal, the proposal must be auditable rather than opaque. For each proposed judgment, Luna should provide, as applicable:

- subject/candidate identifier;
- proposed decision or rating;
- applicable Sol rubric criterion/criteria;
- evidence/source references supporting the proposal;
- concise reasoning;
- confidence;
- unresolved questions or conflicts;
- duplicate/carry-over/single-home relationship where relevant;
- alternative disposition if the evidence supports more than one reasonable outcome.

Luna should prefer `UNRESOLVED` or an explicit alternative over inventing certainty. Sol review may accept the proposal as-is, revise it, or return a bounded repair instruction.

## 3. Global execution pattern and crash discipline

Each phase uses a candidate/review/advancement pattern.

1. Sol reads current repository authority and commits a bounded phase handoff containing policy, rubric, allowed sources, proposal fields, allowed writes, and stop condition.
2. Luna starts from the exact named branch SHA.
3. Luna performs only the authorized collection, analysis, proposal, materialization, and deterministic tool work.
4. Luna commits candidate/proposal artifacts plus a Luna session record and stops before lifecycle advancement.
5. Sol reviews the exact committed bytes and writes a Sol review record.
6. If review fails, Sol writes a bounded repair delta; Luna repairs only the rejected scope and stops again.
7. If review passes, Sol freezes the accepted semantic result and authorizes deterministic Core advancement.
8. Luna executes validation/checkpoint/`ADVANCE_STAGE` for the reviewed candidate and records the resulting SHA/state.
9. Sol verifies Production State and writes the policy for the next phase.

Crash recovery rules:

- `sources/2026-W33/execution/index.md` is the recovery entry point.
- Sol policies/handoffs live under `sources/2026-W33/execution/handoffs/`.
- Luna runs live under `sources/2026-W33/execution/sessions/`.
- Sol semantic reviews live under `sources/2026-W33/execution/reviews/`.
- Candidate/proposal commits and lifecycle advancement should remain separate when tooling permits.
- If a session crashes after Luna candidate commit, restart at Sol review.
- If it crashes after Sol review pass, restart at deterministic advancement.
- Do not repeat already committed research merely because conversational state was lost.

## 4. Phase S — Screening materialization

Screening semantics are already frozen by Sol, so Luna's role here remains materialization rather than proposal.

### Frozen authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- Discovery record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Sol Screening seed: `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- Semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- Semantic-authority Git blob: `ba649d6e805bac5316b88a78d259a3de97f839b2`
- Expected aggregate: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4
- Session-local expected result-set id for verification only: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`

### Luna S1 — materialize current-Core Screening

Luna must:

- adapt the exact Sol seed to the current runner wrapper without changing decisions, reasons, duplicate groups, or verification targets;
- run the current Screening materialization path;
- produce canonical package/batch/result/acceptance/interactive artifacts;
- validate exact 41-ID coverage and 26/8/3/4 counts;
- compare the generated content-addressed identity with the r7 expectation, recording any deterministic difference instead of forcing the value;
- commit Screening materialization outputs plus session record;
- stop before Production State modification or `ADVANCE_STAGE`.

### Sol S2 — review

Sol verifies exact semantic-seed fidelity, package/result/acceptance consistency, duplicate groups, provenance, hashes, and changed-path boundaries. After pass, Sol authorizes Luna to checkpoint and advance to `CANDIDATES_NORMALIZED`.

## 5. Phase E — Evidence / Materiality / Completeness

Core handler: `stage:evidence-materiality-completeness`  
Next lifecycle: `EVIDENCE_REVIEWED`

### Sol E0 — define research and evaluation policy

Sol must define before Luna collection:

- which KEEP records require Evidence work;
- exact verification questions for every MAYBE and INSPECT record;
- excluded DROP scope;
- allowed sources/source classes and authority hierarchy per subject;
- date/identity/release/carry-over resolution rules;
- duplicate-group and canonical-subject boundaries;
- weekly current-relevance and technical-significance rubric;
- attribution requirements for vendor claims;
- X/community role as discovery/context only;
- required Evidence/Materiality/Completeness proposal fields and artifacts;
- unresolved conditions that Luna must surface instead of solving by inference.

### Luna E1 — collect, organize, and propose

Under the Sol policy, Luna may:

- retrieve/read the allowed sources and collect source-local facts;
- create Evidence cards/tasks/results and edition evidence views;
- resolve factual date/identity questions where approved evidence directly supports the resolution;
- propose disposition for INSPECT/MAYBE items;
- propose per-candidate Materiality assessment using Sol's rubric;
- propose duplicate/carry-over treatment where the rubric permits;
- record confidence and unresolved questions;
- populate candidate Materiality ledger and Profile Completeness candidate artifacts according to current schemas and Sol policy;
- run validators/checksums and commit the candidate plus session record;
- stop before lifecycle advancement.

Luna's Materiality ratings are proposals, not authority.

### Sol E2 — semantic review and freeze

Sol reviews:

- source-to-claim binding and attribution;
- whether evidence hierarchy was followed;
- whether X/community claims remained non-authoritative;
- INSPECT/MAYBE resolutions;
- proposed Materiality judgments against the frozen rubric;
- duplicate/carry-over proposals;
- completeness against WEEKLY profile obligations;
- unresolved cases and whether they can safely proceed to Selection.

Sol freezes accepted/revised Evidence, Materiality, and Completeness semantics. Only then may Luna run the deterministic checkpoint and advance to `EVIDENCE_REVIEWED`.

## 6. Phase L — Selection

Core handler: `stage:selection`  
Next lifecycle: `SELECTION_COMPLETE`

### Sol L0 — define Selection rubric and issue constraints

Sol defines:

- inclusion/exclusion/watchlist/carry-over criteria;
- issue-level balance goals and limits;
- minimum Evidence sufficiency for selection;
- duplicate canonicalization rules;
- late-breaking single-home policy;
- carry-over disposition rules;
- how uncertainty affects inclusion;
- required proposal dimensions for Luna.

Sol need not freeze every individual candidate disposition before Luna works.

### Luna L1 — propose Selection

Using only Sol-reviewed Evidence and the Sol Selection rubric, Luna may propose:

- selected publication candidates;
- watchlist/carry-over/excluded candidates;
- canonical representative for duplicate groups;
- late-breaking single-home placement;
- relative priority/materiality ordering;
- issue-balance rationale;
- residual uncertainty that should be visible in Architecture.

Luna materializes a candidate matrix/selection proposal with exact Evidence traceability, reasoning, confidence, and alternative choices where appropriate, validates it, commits it, and stops before lifecycle advancement.

### Sol L2 — review and freeze Selection

Sol reviews each proposal and the issue as a whole for Evidence sufficiency, materiality balance, duplicate/single-home/carry-over consistency, and weekly editorial coherence. Sol may accept, modify, or reject individual Luna proposals. The reviewed Selection becomes frozen authority. Luna may then checkpoint and advance to `SELECTION_COMPLETE`.

## 7. Phase A — Architecture

Core handler: `stage:architecture`  
Successful next lifecycle: `ARCHITECTURE_ESTABLISHED`, triggering `ARCHITECTURE_REVIEW`.

Required gate inputs:

- `sources/2026-W33/architecture-v2.json`
- `sources/2026-W33/architecture-review-summary-v2.json`
- `sources/2026-W33/architecture-review-attention-v2.json`

### Sol A0 — define Architecture design policy

Sol defines the architecture design space rather than necessarily writing the first full structure. Sol must specify:

- intended reader outcome and `why this issue` logic;
- acceptable article/section count or complexity envelope;
- principles for lead versus secondary material;
- grouping/splitting rules;
- relationship types worth surfacing between selected developments;
- duplicate-coverage avoidance and single-home constraints;
- watchlist/carry-over/residual-uncertainty treatment;
- source/evidence boundaries later drafting must preserve;
- Human review-attention categories;
- any required or prohibited narrative emphasis.

### Luna A1 — propose Architecture and materialize candidate gate artifacts

Using the frozen Selection and Sol Architecture policy, Luna may propose:

- lead story candidate(s);
- section grouping and hierarchy;
- ordering;
- relationships between selected developments;
- concise issue narrative / why-this-issue formulation;
- placement of secondary/watchlist/carry-over material where allowed;
- Human review-attention items;
- alternative architecture where two materially different structures are both plausible.

Luna then materializes the proposed architecture into the three current Core gate artifacts, preserving Selection/Evidence references, runs the Architecture validator, commits the candidate plus session record, and stops before lifecycle advancement.

### Sol A2 — semantic Architecture review and freeze

Sol reviews Luna's proposed architecture for:

- fidelity to Sol design policy;
- editorial coherence and appropriate lead weighting;
- complete mapping of selected candidates;
- unsupported or duplicate placement;
- source/evidence boundaries;
- treatment of uncertainty/carry-over/watchlist;
- Human review-attention usefulness;
- schema/validator cleanliness and changed-path boundary.

Sol may adopt Luna's proposal unchanged, revise specific architecture choices, or request bounded repair. The Sol-reviewed architecture is the semantic authority presented upstream to the Human Gate.

### Luna A3 — deterministic gate advancement

Only after a Sol review pass may Luna execute the Architecture checkpoint/`ADVANCE_STAGE` operation.

Expected result:

- lifecycle: `ARCHITECTURE_ESTABLISHED`
- Human gate: `ARCHITECTURE_REVIEW`
- no Draft-stage work

Luna records resulting commit SHA, Production State, checkpoint provenance, and changed paths.

### Sol A4 — final pre-Human verification

Sol performs read-only verification that the branch contains exactly the reviewed Architecture bytes, Core recorded the Architecture checkpoint and Human Gate correctly, no Draft artifacts were created, and work stopped at the requested gate. Sol then presents the package to the user for Human Architecture Review.

## 8. Repair and Exception Gate policy

Use bounded Luna repair for schema formatting, missing approved-source captures, deterministic validation failures, incorrect path/provenance links, or mismatches between Sol policy and Luna materialization/proposal.

Return to Sol policy work when new evidence changes the assumed identity/date/relationship, exposes a material new ambiguity, or requires a different Materiality/Selection/Architecture rubric application.

Use Human Exception Gate only when a genuine owner/editorial decision cannot safely be derived from repository authority. Routine research ambiguity, bounded re-collection, proposal disagreement, or validator failure is not itself an Exception Gate.

## 9. Immediate next step

The immediate next task remains Screening S1. Sol should instantiate an exact Luna Screening handoff from the current branch SHA. Screening does not need a new Luna semantic proposal because the 41 Screening decisions are already frozen. After Screening advancement, Evidence and later phases follow the r3 proposal model defined above.
