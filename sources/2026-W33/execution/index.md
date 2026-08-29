# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `DISCOVERY_COLLECTED`
- Current machine action: `stage:screening`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Core implementation authority recorded by Production State: `02ba8323c80ac52ab407ff3199ed344907a170b2`
- Orchestrator: `survey-production-core-v2/0.15-postintegration-transport-thematic`

The current lifecycle above remains authoritative until the separately authorized Screening advancement task commits a validated Core transition.

## Current Discovery authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- Record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Canonical X manifest: `sources/2026-W33/external/x/x-source-intake-v2.json`
- X manifest SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- Discovery acceptance: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- Acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`
- Graph SHA-256: `f7ba629fffb48921b139034c4d44941507b83594f76a59dd9151c5270a995eff`

## Current Screening authority

Semantic seed:

- Sol semantic seed: `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- Semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- Semantic-authority Git blob: `ba649d6e805bac5316b88a78d259a3de97f839b2`
- Decisions: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4 / total 41

Canonical current-Core materialization:

- accepted run: `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`
- acceptance: `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json`
- result-set SHA-256: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- acceptance SHA-256: `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b`
- package SHA-256: `186b2c0227af0faa405d0618c7fa5e0849075ec51d51d7da013f626801a10da7`
- batch count: 1
- record count: 41
- aggregate: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4

Sol review:

- `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
- decision: `ACCEPT / APPROVED_FOR_CORE_ADVANCEMENT`

The pre-Luna expected content-addressed result-set id calculated by Sol matched the Luna materialization exactly. Screening semantic/materialization review is complete; only deterministic Screening checkpoint / lifecycle advancement remains.

## Screening transport provenance

Luna Screening S1 began from:

`3efd960e06f731cae4e2e6d671f99aff88a58c19`

Canonical GitHub transport commits are:

- candidate materialization: `28d5a3d1cf9d0fc2ac1a46e1cf5b1341004d502a`
- final Luna S1 GitHub head: `06fbb821da523782266b2bd39ee04cc66ea637c8`
- final GitHub tree: `ee42701c20971e0d94fbcddea08e507efb0d629c`

The Luna worker record contains local Git commit identities produced before GitHub API reconstruction. Those local SHAs are historical worker transport provenance only. Repository recovery must use the canonical GitHub SHAs above and the Sol review's transport reconciliation note.

## Latest semantic/work records

Historical Discovery chain:

- Luna reconstruction handoff: `sources/2026-W33/execution/handoffs/w33-discovery-rebuild-luna-r1.md`
- Luna reconstruction session: `sources/2026-W33/execution/sessions/w33-luna-discovery-rebuild-20260829-r1.md`
- Sol Discovery review: `sources/2026-W33/execution/reviews/w33-discovery-sol-review-20260829-r4.md`
- Sol review session: `sources/2026-W33/execution/sessions/w33-sol-discovery-review-20260829-r4.md`
- Sol Discovery acceptance session: `sources/2026-W33/execution/sessions/w33-sol-discovery-acceptance-20260829-r5.md`

Current Screening chain:

- Sol Screening semantic pass: `sources/2026-W33/execution/sessions/w33-sol-screening-20260829-r6.md`
- Post-r6 recovery record: `sources/2026-W33/execution/sessions/w33-sol-screening-materialization-recovery-20260830-r7.md`
- Current Sol/Luna plan through Architecture Review: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
- Screening materialization handoff: `sources/2026-W33/execution/handoffs/w33-screening-materialization-luna-r1.md`
- Luna Screening materialization session: `sources/2026-W33/execution/sessions/w33-luna-screening-materialization-20260830-r1.md`
- Sol Screening materialization review: `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
- Current phase-specific Luna handoff: `sources/2026-W33/execution/handoffs/w33-screening-advance-luna-r1.md`
- Superseded historical plan: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r2.md`

## Current semantic status

`SCREENING_SOL_REVIEW_PASSED / DETERMINISTIC_ADVANCEMENT_READY_FOR_LUNA`

The 41-record Screening semantic seed and current-Core content-addressed materialization have passed Sol review. The next bounded task is **only** the deterministic Screening checkpoint / `ADVANCE_STAGE` operation authorized by:

`sources/2026-W33/execution/handoffs/w33-screening-advance-luna-r1.md`

Luna must start from the exact current branch SHA supplied by Sol/caller, create the immutable operator request, execute the canonical bridge, advance exactly once to `CANDIDATES_NORMALIZED`, commit the resulting checkpoint/state/bridge provenance, and stop for Sol verification.

Do not begin Evidence work until Production State actually records `CANDIDATES_NORMALIZED` and Sol has authored the Evidence / Materiality / Completeness policy.

## Current Sol/Luna responsibility model

The authoritative model is defined by r3:

`Sol policy/rubric/constraints -> Luna collection/analysis/proposal/materialization -> Sol semantic review -> Luna deterministic advancement`

- Sol: define scope, policy, rubrics, source/evidence authority, constraints, required proposal dimensions, and stop conditions; review and accept/revise/reject Luna's semantic proposals.
- Luna: perform bounded source-local collection, organize evidence, analyze under Sol-defined criteria, propose Materiality/INSPECT/MAYBE resolution/Selection/Architecture outcomes, materialize Core artifacts, run validators and approved Core/Git operations, and record exact execution provenance.
- Luna proposals are not authority until Sol review passes.
- Sol does not need to pre-decide every item-level Materiality, Selection, or Architecture choice when the evaluation policy is sufficiently explicit; Luna may generate the first proposal under that policy.
- Core v2: deterministic schema/invariant/provenance/checkpoint/lifecycle enforcement.
- Human: perform Architecture Review after Sol has reviewed the Architecture artifacts and Core has reached `ARCHITECTURE_ESTABLISHED` / `ARCHITECTURE_REVIEW`.

Luna must not invent scope, broaden allowed sources, change Sol rubrics, promote X/community material to technical authority, guess unresolved source conflicts, treat its own proposal as final authority, or infer Human Gate decisions.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
4. `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
5. `sources/2026-W33/execution/handoffs/w33-screening-advance-luna-r1.md`
6. latest Luna advancement session record, if any
7. latest later Sol review/policy record, if any

Then resume from the first uncompleted advancement/policy/candidate/review step. Do not repeat already committed Screening materialization merely because the prior chat session was lost.
