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

Screening advancement has been executed and Sol-verified. Evidence / Materiality / Completeness is now the active candidate phase, but lifecycle advancement to `EVIDENCE_REVIEWED` is **not authorized** until the Luna candidate passes Sol review.

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

Sol Screening materialization review:

- `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
- decision: `ACCEPT / APPROVED_FOR_CORE_ADVANCEMENT`

## Screening advancement authority

Canonical remote advancement chain:

- exact start: `0c4ac45a69279ed35dd0ef81f605649a23394dd2`
- request commit: `fa83972e887d506d69b19a450a1f3858747c7db5`
- deterministic execution commit: `5b433d494a46cba7fad2503b23b35372b3c3240b`
- final Luna remote head: `e9221c0915e2b0e79411903479a056699612062a`

Worker-local transport identities retained in the Luna session:

- local request commit: `0e93d080257389b57e160be0fffb4bda6311e13e`
- local execution-result commit: `fa8018c00c6ab44dd19bed6caeffa866fe886cc7`

The local/GitHub commit-object SHAs differ because the worker reconstructed commits through the authenticated GitHub API after ordinary shell Git credentials were unavailable. Request tree `67b78089278f039647d91079acb2e21dc81f65ca` and execution-result tree `991b6d399a84c30331d2cb248e282d07f9279258` were preserved across transport.

The deterministic Core artifacts correctly bind the **GitHub canonical request/event SHA** `fa83972e887d506d69b19a450a1f3858747c7db5`. This exact SHA appears in bridge receipt, Stage Checkpoint implementation provenance, and Production State history. No internal Core provenance repair is required.

Canonical advancement artifacts:

- request: `sources/2026-W33/execution/requests/w33-screening-advance-20260830-r1.json`
- request SHA-256: `cdd19b25fab78af7a3795c66d199b943b75fd900b139bdb99753d7e69d5b6d17`
- bridge run: `sources/2026-W33/execution/bridge-runs/w33-screening-advance-20260830-r1/`
- Core stage contract SHA-256: `1cca146b694554114f653e43073f4bd90687a49ef10b89f8982b01bdba60fdca`
- bridge reviews SHA-256: `1c275e653aba13b48830ec3141ccf2882cc83d6a0b53f2b4fe6a66952f9f16cb`
- bridge receipt SHA-256: `8f77838a7d37cac942ecfe918dab03bb2234d19fe871b42d2ae0a8e2e31c06e6`
- Screening checkpoint: `sources/2026-W33/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`
- Screening checkpoint SHA-256: `4d0939a6352786787e01b05881b540aa259640e67d7a0e20429db6aa17cf1ec0`
- Luna advancement session: `sources/2026-W33/execution/sessions/w33-luna-screening-advance-20260830-r1.md`
- Sol advancement verification: `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`
- Sol decision: `ACCEPT / STATE_TRANSITION_VERIFIED / READY_FOR_EVIDENCE_POLICY`

The authoritative Production State after advancement is:

- SHA-256: `bc7d2cad5a2a53634b3eeaab12336dfd4a3c56e1db8677534c8dc5b03f60ba6f`
- lifecycle `CANDIDATES_NORMALIZED`
- next action `stage:evidence-materiality-completeness`
- Screening checkpoint `passed`
- Evidence / Materiality / Completeness checkpoints `pending`

## Evidence / Materiality / Completeness policy

Current phase-specific Sol handoff:

`sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`

The current Core phase structure is:

`37 active Screening records -> Evidence Tasks -> factual Evidence Cards -> Weekly Edition Evidence Views -> deterministic 41-row Materiality Ledger -> Profile Completeness`

Key policy:

- exact active Evidence task count: 37 = KEEP 26 + INSPECT 8 + MAYBE 3;
- the four DROP records receive no Evidence task;
- Evidence Card sources must remain within each task's accepted Discovery source record;
- a better/new URL discovered during research is a `SOURCE_GAP`, not automatic new Evidence authority;
- X/community is discovery/context only and cannot support technical claims;
- Luna may propose Edition View Materiality under the frozen Sol rubric: `MATERIAL`, `CONTEXT`, `NON_MATERIAL`, `HOLD`;
- KEEP does not imply MATERIAL;
- INSPECT/MAYBE and carry-over records should be resolved as far as the bound source permits;
- duplicate groups are not collapsed during Evidence;
- the Materiality Ledger must be current-Core deterministic derivation, not hand-edited;
- Profile Completeness status must be preserved as Core derives it; do not force `READY`;
- Luna must stop before checkpoint/`ADVANCE_STAGE` for Sol semantic review.

## Latest semantic/work records

Historical Discovery chain:

- Luna reconstruction handoff: `sources/2026-W33/execution/handoffs/w33-discovery-rebuild-luna-r1.md`
- Luna reconstruction session: `sources/2026-W33/execution/sessions/w33-luna-discovery-rebuild-20260829-r1.md`
- Sol Discovery review: `sources/2026-W33/execution/reviews/w33-discovery-sol-review-20260829-r4.md`
- Sol review session: `sources/2026-W33/execution/sessions/w33-sol-discovery-review-20260829-r4.md`
- Sol Discovery acceptance session: `sources/2026-W33/execution/sessions/w33-sol-discovery-acceptance-20260829-r5.md`

Screening chain:

- Sol Screening semantic pass: `sources/2026-W33/execution/sessions/w33-sol-screening-20260829-r6.md`
- Post-r6 recovery record: `sources/2026-W33/execution/sessions/w33-sol-screening-materialization-recovery-20260830-r7.md`
- Current Sol/Luna plan through Architecture Review: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
- Screening materialization handoff: `sources/2026-W33/execution/handoffs/w33-screening-materialization-luna-r1.md`
- Luna Screening materialization session: `sources/2026-W33/execution/sessions/w33-luna-screening-materialization-20260830-r1.md`
- Sol Screening materialization review: `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`
- Screening advancement handoff: `sources/2026-W33/execution/handoffs/w33-screening-advance-luna-r1.md`
- Luna Screening advancement session: `sources/2026-W33/execution/sessions/w33-luna-screening-advance-20260830-r1.md`
- Sol Screening advancement verification: `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`

Current phase:

- current E/M/C Luna handoff: `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`

Historical superseded operating plan:

- `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r2.md`

## Current semantic status

`EVIDENCE_MATERIALITY_COMPLETENESS_HANDOFF_READY / CANDIDATE_PENDING`

Screening is complete through deterministic lifecycle advancement and has passed Sol verification. The next bounded operation is Luna creation of the Evidence / Materiality / Completeness **candidate** under the current phase-specific Sol handoff.

Luna must:

1. start from the exact current branch SHA supplied by Sol/caller;
2. generate exactly 37 current-Core Evidence tasks from the accepted 41-record Screening set;
3. perform bounded source-local factual research under the frozen source authority;
4. materialize complete Evidence results;
5. propose Weekly Edition Evidence Views / Materiality under the Sol rubric;
6. accept the View set using current Core;
7. deterministically derive the 41-row Materiality Ledger;
8. build/validate Profile Completeness;
9. commit candidate artifacts plus its Luna session record;
10. stop for Sol review with Production State still `CANDIDATES_NORMALIZED`.

Do not begin Selection until:

1. the E/M/C candidate is committed;
2. Sol semantic review passes;
3. a separate deterministic E/M/C checkpoint/`ADVANCE_STAGE` task completes; and
4. Production State records `EVIDENCE_REVIEWED`.

## Current Sol/Luna responsibility model

The authoritative model is defined by r3:

`Sol policy/rubric/constraints -> Luna collection/analysis/proposal/materialization -> Sol semantic review -> Luna deterministic advancement`

- Sol: define scope, policy, rubrics, source/evidence authority, constraints, required proposal dimensions, and stop conditions; review and accept/revise/reject Luna's semantic proposals.
- Luna: perform bounded source-local collection, organize evidence, analyze under Sol-defined criteria, propose Materiality/INSPECT/MAYBE resolution/Selection/Architecture outcomes where authorized, materialize Core artifacts, run validators and approved Git/Core operations, and record exact execution provenance.
- Luna proposals are not authority until Sol review passes.
- Core v2 owns deterministic schema/invariant/provenance/checkpoint/lifecycle enforcement.
- Human performs Architecture Review after Sol has reviewed Architecture artifacts and Core reaches `ARCHITECTURE_ESTABLISHED` / `ARCHITECTURE_REVIEW`.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`
4. `sources/2026-W33/execution/reviews/w33-screening-advance-sol-review-20260830-r1.md`
5. `sources/2026-W33/execution/handoffs/w33-evidence-materiality-completeness-luna-r1.md`
6. latest Luna E/M/C session record, if any
7. latest Sol E/M/C review record, if any

Then resume from the first uncompleted candidate/review/advancement step. Do not repeat already committed Screening work merely because the prior chat session was lost.
