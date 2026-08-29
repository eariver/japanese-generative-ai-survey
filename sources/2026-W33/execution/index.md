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

Screening is complete and advanced. The first Evidence / Materiality / Completeness candidate has been materialized and Sol-reviewed. The factual Evidence layer is frozen as the basis for a bounded **Edition Evidence View semantic repair**. Lifecycle advancement to `EVIDENCE_REVIEWED` is not authorized until that repair passes Sol re-review.

## Current Production State

Authoritative State remains unchanged from the completed Screening advancement:

- SHA-256: `bc7d2cad5a2a53634b3eeaab12336dfd4a3c56e1db8677534c8dc5b03f60ba6f`
- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- Discovery checkpoint: `passed`
- Screening checkpoint: `passed`
- Evidence / Materiality / Completeness: `pending`
- Selection / Architecture: `pending`
- Architecture Review: `pending`
- terminal reason: null

The current repair task must leave these bytes unchanged.

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

Canonical advancement chain:

`0c4ac45a69279ed35dd0ef81f605649a23394dd2 -> fa83972e887d506d69b19a450a1f3858747c7db5 -> 5b433d494a46cba7fad2503b23b35372b3c3240b -> e9221c0915e2b0e79411903479a056699612062a`

## E/M/C policy authority

The original candidate task used both of the following, with r2 winning on conflicts:

1. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
2. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r2.md`

Exact W33 Profile dimensions remain:

- `current relevance`
- `technical significance`
- `carry-over obligations`

Exact W33 initial obligations remain:

- `weekly:current-relevance`
- `weekly:technical-significance`
- `weekly:carry-over`

## First Luna E/M/C candidate

Canonical remote chain:

`75d4cd6d14a73eee548fc52d3a460a7887e9c855 -> 8734705209cc14f79cb09c2f016f421d44a1df17 -> 164e1f2bfbd33cbda8b5dd6f0a0d9a3c12129538`

- candidate-artifact commit: `8734705209cc14f79cb09c2f016f421d44a1df17`
- candidate-artifact tree: `03db1583cd8532bdc2a7fee09e11fdb6fa14e6d2`
- final Luna remote head: `164e1f2bfbd33cbda8b5dd6f0a0d9a3c12129538`
- final Luna remote tree: `d80c198323801102cb2bc72ec5d334fb9c052e2c`
- Luna session: `sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-20260830-r1.md`
- Luna stop status: `COMPLETENESS_INCOMPLETE_NEEDS_SOL_REVIEW`

The reported local commit identities (`3bb7eb09...`, `ee332534...`) are worker transport provenance only; GitHub SHAs above are canonical for repository recovery.

### Frozen accepted Evidence repair basis

Accepted Evidence root:

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/`

- result-set identity: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- package SHA-256: `2655553661ebb6c2b0d2710403d2f8d0492f2d3e248ad3f71ffd06a561b7f39d`
- acceptance SHA-256: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- exact task count: 37
- Evidence statuses: VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

Sol review freezes this Evidence accepted run byte-for-byte as the repair input. Do not redo factual research or add sources in the current repair.

### Rejected historical View candidate

Historical View run:

`sources/2026-W33/evidence/v2/views/accepted/b6c6057fe9237cf45cf3d7245c9a7c8eb0c6d56a885300e718ca8d9f43b6bea6/`

- view-set identity: `b6c6057fe9237cf45cf3d7245c9a7c8eb0c6d56a885300e718ca8d9f43b6bea6`
- proposal distribution: MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0

This run is immutable historical candidate provenance, but it is **not accepted semantic authority**. Sol found systemic generic boilerplate in `materiality.rationale` and Weekly `profile_annotations.why_this_issue` across heterogeneous candidates.

### Candidate derived artifacts

The current root files are derived from the rejected View candidate and must be regenerated after repair:

- `sources/2026-W33/materiality-ledger-v2.json`
  - candidate SHA-256: `1e092842633c90f3f2d1d1a9fd0fc3e497f2aea300b41bd63ec419ee0cad0a0b`
- `sources/2026-W33/profile-completeness-v2.json`
  - candidate SHA-256: `4f670dbc75997084826f6a1cd6851a9afcb53bb2a4d2aa86e394c9d289c95463`
  - status: `INCOMPLETE`

Current `INCOMPLETE` status is a legitimate explicit limitation, not a deterministic failure. It is driven primarily by five active W32 carry-over rechecks that remain NEEDS_MORE/HOLD under frozen source authority. Sol does not authorize an upstream rewind or source expansion merely to force closure.

## Current Sol E/M/C review authority

Review:

`sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-review-20260830-r1.md`

Decision:

`REPAIR_REQUIRED / EVIDENCE_LAYER_ACCEPTED_AS_REPAIR_BASIS / EDITION_VIEW_SEMANTIC_REPAIR_REQUIRED / NO_UPSTREAM_SOURCE_EXPANSION`

Key decision:

- Evidence bytes remain frozen;
- six NEEDS_MORE items remain unresolved/HOLD under current authority;
- no Discovery/Screening rewind;
- no source expansion;
- `INCOMPLETE` Completeness may remain after repair;
- all 37 Edition Views require item-specific rationale and `why_this_issue`;
- the 11 INSPECT/MAYBE dispositions listed in the Sol review are frozen defaults unless existing Evidence reveals a contradiction;
- the other 26 statuses must be re-evaluated from existing Evidence while writing item-specific reasoning;
- new View acceptance, Ledger, and Completeness must be regenerated and returned for Sol re-review.

## Current bounded Luna repair handoff

Current phase-specific execution authority:

`sources/2026-W33/execution/handoffs/w33-evidence-view-semantic-repair-luna-r1.md`

Status:

`READY_FOR_LUNA / EDITION_VIEW_SEMANTIC_REPAIR_ONLY / STOP_FOR_SOL_REREVIEW`

Luna must:

1. start from the exact current branch SHA supplied by Sol/caller;
2. preserve Production State byte-for-byte;
3. preserve accepted Evidence result-set `c86f49...` byte-for-byte;
4. create a new complete 37-View content-addressed accepted set using only the existing Evidence bytes;
5. make every rationale and `why_this_issue` candidate-specific and decision-useful;
6. retain the 11 Sol-reviewed INSPECT/MAYBE defaults absent an exact Evidence contradiction;
7. explicitly report every status change among the other 26 candidates;
8. regenerate the 41-row Materiality Ledger deterministically from the new View acceptance;
9. regenerate/revalidate Profile Completeness without forcing a desired status;
10. commit the bounded repair plus one Luna repair session;
11. stop before any checkpoint/`ADVANCE_STAGE`.

## Current semantic status

`EVIDENCE_FROZEN / EDITION_VIEW_SEMANTIC_REPAIR_READY_FOR_LUNA / LIFECYCLE_ADVANCEMENT_BLOCKED`

Do not begin Selection and do not advance to `EVIDENCE_REVIEWED` until:

1. Luna commits the repaired View set and regenerated derived artifacts;
2. Sol re-reviews the exact repaired bytes and passes them;
3. Sol creates a separate deterministic advancement handoff;
4. the Core transition to `EVIDENCE_REVIEWED` completes.

## Sol/Luna responsibility model

Authoritative model:

`Sol policy/rubric/constraints -> Luna collection/analysis/proposal/materialization -> Sol semantic review -> Luna deterministic advancement`

In the current repair, factual collection is already frozen. Luna's job is semantic proposal repair/materialization under the existing rubric; Sol will accept/revise/reject the repaired View authority.

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
9. latest Luna View-repair session, if any
10. latest later Sol re-review, if any

Resume from the first uncompleted repair/re-review/advancement step. Do not repeat Discovery, Screening, or Evidence research merely because the previous chat session was lost.
