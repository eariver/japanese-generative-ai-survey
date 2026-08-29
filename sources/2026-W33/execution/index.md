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

## Current Discovery authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- Record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Canonical X manifest: `sources/2026-W33/external/x/x-source-intake-v2.json`
- X manifest SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- Discovery acceptance: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- Acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`
- Graph SHA-256: `f7ba629fffb48921b139034c4d44941507b83594f76a59dd9151c5270a995eff`

## Current Screening semantic authority

- Sol semantic seed: `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- Semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- Semantic-authority Git blob: `ba649d6e805bac5316b88a78d259a3de97f839b2`
- Decisions: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4 / total 41
- Canonical current-Core Screening materialization: **pending**
- Screening lifecycle advancement: **not yet authorized**

A session-local expected content-addressed Screening result-set id was calculated as:

`648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`

This is a validation expectation only, not acceptance authority. See r7 below.

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
- Sol/Luna plan through Architecture Review: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r2.md`

## Current semantic status

`SCREENING_SEMANTIC_AUTHORITY_READY / CORE_MATERIALIZATION_PENDING`

The 41-record Discovery package is Core-accepted and Production State is already `DISCOVERY_COLLECTED`. Sol has completed semantic Screening and committed the authoritative 41-decision seed. The next bounded production operation is Luna materialization of current-Core Screening artifacts from that exact seed. Luna must stop before lifecycle advancement so Sol can review the materialized result set.

Do not begin Evidence work until:

1. Screening materialization is committed;
2. Sol review passes;
3. deterministic Screening checkpoint/`ADVANCE_STAGE` completes; and
4. Production State records `CANDIDATES_NORMALIZED`.

## Role split through Architecture Review

- Sol: define each phase policy and exact Luna handoff; decide source/evidence boundaries, Materiality, Selection, carry-over/single-home treatment, and Architecture; review every Luna candidate before lifecycle advancement.
- Luna: perform bounded source-local collection, policy-driven organization, schema-conforming materialization, validators, deterministic Core/Git operations, and exact work recording.
- Core v2: deterministic schema/invariant/provenance/checkpoint/lifecycle enforcement.
- Human: perform Architecture Review after Sol has reviewed the Architecture artifacts and Core has reached `ARCHITECTURE_ESTABLISHED` / `ARCHITECTURE_REVIEW`.

Luna must not invent scope, add unapproved sources, promote X/community material to technical authority, make Selection/Architecture decisions, or infer Human Gate outcomes. Ambiguity is surfaced to Sol rather than guessed.

## Crash restart order

On a new session, read in order:

1. `sources/2026-W33/production-state.json`
2. this `sources/2026-W33/execution/index.md`
3. `sources/2026-W33/execution/sessions/w33-sol-screening-materialization-recovery-20260830-r7.md`
4. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r2.md`
5. latest Luna session record, if any
6. latest Sol review record, if any

Then resume from the first uncompleted candidate/review/advancement step. Do not repeat already committed collection merely because the prior chat session was lost.
