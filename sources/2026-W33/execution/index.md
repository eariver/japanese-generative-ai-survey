# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `CANDIDATES_NORMALIZED`
- Current machine action: `stage:evidence-materiality-completeness`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Core implementation authority recorded by Production State initialization: `02ba8323c80ac52ab407ff3199ed344907a170b2`
- Orchestrator: `survey-production-core-v2/0.15-postintegration-transport-thematic`

Screening is complete and advanced. Evidence / Materiality / Completeness has been materialized, received one bounded semantic repair, and passed Sol re-review. Its exact semantic artifacts are now frozen and **approved for deterministic Core advancement**. Production State itself has not yet advanced; the next bounded task is Luna execution of the dedicated E/M/C advancement handoff.

## Current Production State

Authoritative State remains unchanged from completed Screening advancement:

- SHA-256: `bc7d2cad5a2a53634b3eeaab12336dfd4a3c56e1db8677534c8dc5b03f60ba6f`
- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- Discovery checkpoint: `passed`
- Screening checkpoint: `passed`
- Evidence checkpoint: `pending`
- Materiality checkpoint: `pending`
- Completeness checkpoint: `pending`
- Selection / Architecture: `pending`
- Architecture Review: `pending`
- terminal reason: null

The next task is allowed to change State only through the canonical operator bridge and only to `EVIDENCE_REVIEWED`.

## Discovery authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Canonical X manifest: `sources/2026-W33/external/x/x-source-intake-v2.json`
- X manifest SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- Discovery acceptance: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`
- graph SHA-256: `f7ba629fffb48921b139034c4d44941507b83594f76a59dd9151c5270a995eff`

## Screening authority

Semantic seed:

- `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- decisions: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4 / total 41

Accepted current-Core run:

`sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`

- result-set SHA-256: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- acceptance SHA-256: `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b`
- package SHA-256: `186b2c0227af0faa405d0618c7fa5e0849075ec51d51d7da013f626801a10da7`

Sol Screening review:

- `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
- decision: `ACCEPT / APPROVED_FOR_CORE_ADVANCEMENT`

Screening advancement verification:

- `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`
- decision: `ACCEPT / STATE_TRANSITION_VERIFIED / READY_FOR_EVIDENCE_POLICY`

Canonical Screening advancement chain:

`0c4ac45a69279ed35dd0ef81f605649a23394dd2 -> fa83972e887d506d69b19a450a1f3858747c7db5 -> 5b433d494a46cba7fad2503b23b35372b3c3240b -> e9221c0915e2b0e79411903479a056699612062a`

## E/M/C policy authority

The original E/M/C candidate task used both of the following, with r2 winning on conflicts:

1. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
2. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r2.md`

Exact W33 Profile dimensions:

- `current relevance`
- `technical significance`
- `carry-over obligations`

Exact W33 initial obligations:

- `weekly:current-relevance`
- `weekly:technical-significance`
- `weekly:carry-over`

## First Luna E/M/C candidate and rejected View proposal

Canonical remote chain:

`75d4cd6d14a73eee548fc52d3a460a7887e9c855 -> 8734705209cc14f79cb09c2f016f421d44a1df17 -> 164e1f2bfbd33cbda8b5dd6f0a0d9a3c12129538`

- candidate-artifact commit: `8734705209cc14f79cb09c2f016f421d44a1df17`
- final Luna candidate head: `164e1f2bfbd33cbda8b5dd6f0a0d9a3c12129538`
- Luna session: `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-20260830-r1.md`
- first stop status: `COMPLETENESS_INCOMPLETE_NEEDS_SOL_REVIEW`

The first View run remains immutable historical provenance:

`sources/2026-W33/evidence/v2/views/accepted/b6c6057fe9237cf45cf3d7245c9a7c8eb0c6d56a885300e718ca8d9f43b6bea6/`

It is **not** semantic authority because Sol rejected its generic `materiality.rationale` / `why_this_issue` treatment.

Sol repair-required review:

- `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-review-20260830-r1.md`
- decision: `REPAIR_REQUIRED / EVIDENCE_LAYER_ACCEPTED_AS_REPAIR_BASIS / EDITION_VIEW_SEMANTIC_REPAIR_REQUIRED / NO_UPSTREAM_SOURCE_EXPANSION`

Repair handoff:

- `sources/2026-W33/execution/handoffs/w33-evidence-view-semantic-repair-luna-r1.md`

## Frozen accepted Evidence authority

Accepted Evidence root:

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/`

- result-set identity: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- package SHA-256: `2655553661ebb6c2b0d2710403d2f8d0492f2d3e248ad3f71ffd06a561b7f39d`
- Evidence acceptance SHA-256: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- task/result count: 37
- statuses: VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

This Evidence run is frozen byte-for-byte. No new Evidence acquisition is authorized for the current advancement.

## Accepted repaired Edition View authority

Luna repair canonical chain:

`f9b87c035d35bbe62e0ff03adc7d050b624311f2 -> 02c1029dcf09adc5486b0fc74098edd5e1d764ee -> cd73a7ebac64f31d15a49f20ac9dbc62217a76c5`

- repair artifact commit: `02c1029dcf09adc5486b0fc74098edd5e1d764ee`
- repair artifact tree: `b307b98d84f140e358e05bb460b126113d0ad2a8`
- final Luna repair head: `cd73a7ebac64f31d15a49f20ac9dbc62217a76c5`
- Luna repair session: `sources/2026-W33/execution/sessions/w33-luna-evidence-view-semantic-repair-20260830-r1.md`
- Luna stop status: `READY_FOR_SOL_REREVIEW`

Worker-local artifact commit `84e13cd2fec5fd606bb269b80da02d10c3e7f51b` has the same tree as canonical GitHub `02c1029...`; it is transport provenance only.

Accepted repaired View root:

`sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/`

- View-set identity: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- acceptance SHA-256: `6c94ede36420b1fe4b283481d141bb7dc8b6dcd1d7b5266060cebfd64e1a8632`
- View count: 37
- Materiality: MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0

All 37 repaired Views use candidate-specific rationale and `why_this_issue`; the prior generic boilerplate is absent. The 11 Sol-reviewed INSPECT/MAYBE defaults were retained, and no other materiality status changed.

## Accepted Materiality / Completeness authority

Materiality Ledger:

- path: `sources/2026-W33/materiality-ledger-v2.json`
- SHA-256: `cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`
- row count: 41
- deterministic current-Core derivation from frozen Evidence + repaired View authority

Profile Completeness:

- path: `sources/2026-W33/profile-completeness-v2.json`
- SHA-256: `9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`
- overall: `INCOMPLETE`
- `weekly:current-relevance`: `LIMITATION`
- `weekly:technical-significance`: `LIMITATION`
- `weekly:carry-over`: `NEEDS_RESEARCH`

`INCOMPLETE` is an accepted explicit limitation, not a failed candidate. Five active W32 carry-over rechecks and MiniMax remain non-selectable HOLD/NEEDS_MORE boundaries under current authority. No upstream rewind or source expansion is authorized merely to force completeness closure.

## Current Sol E/M/C semantic authority

Final Sol re-review:

`sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`

Decision:

`ACCEPT / REPAIR_VERIFIED / EVIDENCE_MATERIALITY_COMPLETENESS_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

This supersedes the r1 repair-required decision for advancement readiness while retaining r1 as provenance of the repair reason.

The accepted semantic package is exactly:

1. Evidence acceptance `c86f49...`;
2. repaired View acceptance `51f4dda...`;
3. Materiality Ledger SHA `cd29a1...`;
4. Profile Completeness SHA `9ac456...`.

## Current bounded Luna task

Current phase-specific handoff:

`sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-advance-luna-r1.md`

Status:

`READY_FOR_LUNA / EVIDENCE_MATERIALITY_COMPLETENESS_ADVANCEMENT_ONLY / STOP_AFTER_STATE_TRANSITION`

Luna must:

1. start from the exact branch SHA supplied by Sol/caller;
2. verify the exact four frozen E/M/C artifacts and Sol r2 review;
3. create/validate a request-only operator commit;
4. execute the canonical bridge from `CANDIDATES_NORMALIZED`;
5. create the canonical `CANDIDATES_NORMALIZED` Stage Checkpoint with checkpoint set `evidence`, `materiality`, `completeness`;
6. advance exactly once to `EVIDENCE_REVIEWED`;
7. verify `next_action=stage:selection`;
8. commit/push bridge/checkpoint/State/session provenance;
9. stop for Sol before any Selection reasoning or artifact creation.

## Current semantic status

`EVIDENCE_MATERIALITY_COMPLETENESS_SEMANTICS_FROZEN / CORE_ADVANCEMENT_READY`

Do **not** begin Selection yet. Selection begins only after:

1. Luna executes the E/M/C deterministic transition;
2. Production State reaches `EVIDENCE_REVIEWED`;
3. Sol verifies the exact checkpoint/State transition; and
4. Sol defines the Selection policy/rubric and bounded Luna proposal handoff.

## Unresolved boundaries carried forward

- MiniMax: no dated qualifying W33 event body -> HOLD.
- Five active W32 carry-over rechecks: no fresh W33 first-party delta in frozen authority -> HOLD.
- GLM-5.3: detailed coding/cyber/benchmark/local-weight claims remain constrained by direct-page/chronology limits.
- Vendor/project/author/RSS/index claims remain attributed, not independently reproduced.
- Duplicate single-home/carry-over resolution is Selection work.
- X remains discovery/community context only, never technical authority.
- Historical State/Core checkpoint-layout mismatch remains a separate nonblocking maintenance concern under the passing agent-first stage path.

No Human Exception Gate is active for these bounded limitations.

## Sol/Luna responsibility model

Authoritative model:

`Sol policy/rubric/constraints -> Luna collection/analysis/proposal/materialization -> Sol semantic review -> Luna deterministic advancement`

For the current step, semantics are frozen. Luna performs deterministic advancement only. After the transition, Sol owns Selection policy/rubric definition before Luna may propose Selection outcomes.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
4. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
5. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r2.md`
6. `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-20260830-r1.md`
7. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-review-20260830-r1.md`
8. `sources/2026-W33/execution/handoffs/w33-evidence-view-semantic-repair-luna-r1.md`
9. `sources/2026-W33/execution/sessions/w33-luna-evidence-view-semantic-repair-20260830-r1.md`
10. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`
11. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-advance-luna-r1.md`
12. latest Luna E/M/C advancement session, if any
13. latest Sol E/M/C advancement verification, if any

Resume from the first uncompleted advancement/review/Selection-policy step. Do not repeat Discovery, Screening, Evidence research, or the View repair merely because a prior chat session was lost.
