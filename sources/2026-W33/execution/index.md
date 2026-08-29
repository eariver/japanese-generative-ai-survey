# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `EVIDENCE_REVIEWED`
- Current machine action: `stage:selection`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Core implementation authority recorded at initialization: `02ba8323c80ac52ab407ff3199ed344907a170b2`
- Orchestrator: `survey-production-core-v2/0.15-postintegration-transport-thematic`

Discovery, Screening, Evidence, Materiality, and Completeness are complete at their current lifecycle boundaries. The repaired E/M/C semantics are frozen, the deterministic transition to `EVIDENCE_REVIEWED` has passed Sol verification, and the next bounded task is Luna creation of the deterministic Candidate Matrix plus a complete Selection proposal under the current Sol rubric.

No Selection checkpoint or lifecycle advancement is authorized yet.

## Current Production State

Authoritative current State:

- SHA-256: `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`
- lifecycle: `EVIDENCE_REVIEWED`
- next action: `stage:selection`
- terminal reason: null
- Discovery: `passed`
- Screening: `passed`
- Evidence: `passed`
- Materiality: `passed`
- Completeness: `passed`
- Selection: `pending`
- Architecture: `pending`
- Architecture Review: `pending`

The current Luna Selection proposal task must leave Production State byte-identical.

## Discovery authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Discovery acceptance: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`
- canonical X manifest SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`

## Screening authority

Semantic seed:

`sources/2026-W33/screening/sol-screening-decisions-r1.json`

- semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4 / total 41

Accepted Screening:

`sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`

- result-set identity: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- acceptance SHA-256: `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b`
- package SHA-256: `186b2c0227af0faa405d0618c7fa5e0849075ec51d51d7da013f626801a10da7`

Sol Screening review:

`sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`

Decision:

`ACCEPT / APPROVED_FOR_CORE_ADVANCEMENT`

Screening advancement verification:

`sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`

Decision:

`ACCEPT / STATE_TRANSITION_VERIFIED / READY_FOR_EVIDENCE_POLICY`

## E/M/C semantic authority

Original policy/handoffs:

1. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
2. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r2.md` — wins on conflicts

First Sol E/M/C review:

`sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-review-20260830-r1.md`

Decision:

`REPAIR_REQUIRED / EVIDENCE_LAYER_ACCEPTED_AS_REPAIR_BASIS / EDITION_VIEW_SEMANTIC_REPAIR_REQUIRED / NO_UPSTREAM_SOURCE_EXPANSION`

Repair handoff:

`sources/2026-W33/execution/handoffs/w33-evidence-view-semantic-repair-luna-r1.md`

Repair canonical chain:

`f9b87c035d35bbe62e0ff03adc7d050b624311f2 -> 02c1029dcf09adc5486b0fc74098edd5e1d764ee -> cd73a7ebac64f31d15a49f20ac9dbc62217a76c5`

Luna repair session:

`sources/2026-W33/execution/sessions/w33-luna-evidence-view-semantic-repair-20260830-r1.md`

Final Sol semantic re-review:

`sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`

Decision:

`ACCEPT / REPAIR_VERIFIED / EVIDENCE_MATERIALITY_COMPLETENESS_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

### Frozen accepted Evidence

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/`

- result-set identity: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- package SHA-256: `2655553661ebb6c2b0d2710403d2f8d0492f2d3e248ad3f71ffd06a561b7f39d`
- acceptance SHA-256: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- 37 results: VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

### Frozen repaired Edition Views

`sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/`

- View-set identity: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- acceptance SHA-256: `6c94ede36420b1fe4b283481d141bb7dc8b6dcd1d7b5266060cebfd64e1a8632`
- 37 Views: MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0
- all rationale / `why_this_issue` fields are candidate-specific

### Materiality Ledger

`sources/2026-W33/materiality-ledger-v2.json`

- SHA-256: `cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`
- rows: 41

### Profile Completeness

`sources/2026-W33/profile-completeness-v2.json`

- SHA-256: `9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`
- overall: `INCOMPLETE`
- `weekly:current-relevance`: `LIMITATION`
- `weekly:technical-significance`: `LIMITATION`
- `weekly:carry-over`: `NEEDS_RESEARCH`

`INCOMPLETE` is an accepted explicit limitation. No upstream rewind or new source acquisition is authorized merely to force closure.

## E/M/C deterministic advancement

Advancement handoff:

`sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-advance-luna-r1.md`

Canonical advancement chain:

`0acce237691def3b1756eca59896d6b3c58a9faa -> e1aeec4cbbceaa8a17ddc6e0e6065c9dc7c7a179 -> 2cf55e9d0784512936f956630fc02f4537a776fa -> 399429681a6c3c27a294526f244a12fee72f791a`

- request commit: `e1aeec4cbbceaa8a17ddc6e0e6065c9dc7c7a179`
- result commit: `2cf55e9d0784512936f956630fc02f4537a776fa`
- final Luna head: `399429681a6c3c27a294526f244a12fee72f791a`
- Luna session: `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-advance-20260830-r1.md`
- checkpoint: `sources/2026-W33/orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json`
- checkpoint SHA-256: `6857d6f9e45b0356fd22ee29e46fb2e59aa283cf8f9cedd8d560312a65d3972f`
- resulting State SHA-256: `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`

Sol advancement verification:

`sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-advance-sol-review-20260830-r1.md`

Decision:

`ACCEPT / STATE_TRANSITION_VERIFIED / READY_FOR_SELECTION_POLICY`

## Current Selection authority

Selection base handoff:

`sources/2026-W33/execution/handoffs/w33-selection-luna-r1.md`

Corrective runtime overlay:

`sources/2026-W33/execution/handoffs/w33-selection-luna-r2.md`

**r2 wins on conflicts.** The correction is narrow: Candidate Matrix derivation must run through `scripts.survey_agent_tool_v2.current_stage_basis_override()` with the actual current work-branch implementation SHA. Do not use r1's direct Matrix CLI with reviewed-main SHA as runtime implementation identity.

Current combined status:

`READY_FOR_LUNA / SELECTION_PROPOSAL_ONLY / STOP_FOR_SOL_REVIEW`

Core Selection facts:

- Candidate Matrix is a deterministic 37-row derivation from the frozen E/M/C authority.
- Candidate Selection must assign every Matrix candidate exactly once.
- dispositions: `SELECTED`, `HOLD`, `REJECT`, `INSPECT`.
- SELECTED requires `PRIMARY` or `SUPPORTING` architecture usage and W33 Profile/Publication role authority.
- non-selected assignments must have `NONE` usage and null roles.
- Materiality `HOLD` / `NON_MATERIAL` cannot be SELECTED.
- Evidence `NEEDS_MORE` / `REJECTED` cannot be SELECTED.

Sol Selection rubric:

- MATERIAL is a selection pool, not automatic inclusion.
- technical significance and W33 reader value outrank source volume.
- duplicate/index/dedicated-page/event/community representations must be single-homed rather than double-counted.
- CONTEXT is normally SUPPORTING when selected, never PRIMARY without Sol inspection.
- all six current HOLD/NEEDS_MORE Matrix candidates remain Selection HOLD under frozen authority.
- REJECT means semantically understood but omitted for concrete redundancy/marginal-value/scope reasons.
- INSPECT is reserved for genuine editorial ambiguity that Sol must resolve.
- breadth is a sanity check, not a vendor/topic quota.
- source attribution and unresolved Evidence boundaries survive Selection.

Luna must write only:

1. `sources/2026-W33/candidate-matrix-v2.json`
2. `sources/2026-W33/candidate-selection-v2.json`
3. `sources/2026-W33/execution/sessions/w33-luna-selection-20260830-r1.md`

Luna must leave Production State unchanged and stop before a Selection checkpoint, `ADVANCE_STAGE`, or Architecture work.

## Current semantic status

`EVIDENCE_REVIEWED / SELECTION_POLICY_FROZEN / SELECTION_PROPOSAL_READY_FOR_LUNA / LIFECYCLE_ADVANCEMENT_BLOCKED`

The next valid sequence is:

1. Luna derives Candidate Matrix and commits a complete Selection proposal.
2. Sol reviews exact Selection semantics and resolves any INSPECT assignments.
3. If accepted, Sol creates a separate deterministic Selection advancement handoff.
4. Luna advances exactly `EVIDENCE_REVIEWED -> SELECTION_COMPLETE`.
5. Sol verifies the transition.
6. Only then does Sol define Architecture policy and Luna propose Architecture.
7. Human Architecture Review occurs only after `ARCHITECTURE_ESTABLISHED` and its required review artifacts exist.

## Unresolved boundaries carried forward

- MiniMax lacks a dated qualifying W33 event body -> HOLD / non-selectable.
- five active W32 carry-over rechecks lack a fresh W33 first-party delta -> HOLD / non-selectable.
- GLM-5.3 detailed coding/cyber/benchmark/local-weight claims remain bounded by direct-page/chronology limitations.
- vendor/project/author/RSS/index claims remain attributed, not independently reproduced.
- X remains discovery/community context only, never technical authority.
- Selection must resolve duplicate/single-home and editorial consolidation without new research.
- historical legacy State/Core checkpoint-layout mismatch remains a separate nonblocking maintenance concern; current agent-first stage validation passes.

No Human Exception Gate is active for these bounded limitations.

## Sol/Luna responsibility model

`Sol policy/rubric/constraints -> Luna analysis/proposal/materialization -> Sol semantic review -> Luna deterministic advancement`

Current ownership:

- Sol: Selection rubric and final semantic acceptance.
- Luna: deterministic Matrix derivation + full Selection proposal under that rubric.
- Human: no action until Architecture Review.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
4. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`
5. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-advance-luna-r1.md`
6. `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-advance-20260830-r1.md`
7. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-advance-sol-review-20260830-r1.md`
8. `sources/2026-W33/execution/handoffs/w33-selection-luna-r1.md`
9. `sources/2026-W33/execution/handoffs/w33-selection-luna-r2.md`
10. latest Luna Selection session, if any
11. latest Sol Selection review, if any

Resume from the first uncompleted Selection proposal/review/advancement step. Do not repeat Discovery, Screening, Evidence research, the Edition View repair, or E/M/C advancement merely because chat history was lost.