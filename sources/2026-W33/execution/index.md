# 2026-W33 execution recovery index

This file is the crash-recovery entry point for the current W33 production run. Repository state is authoritative over chat history.

## Canonical production authority

- Work branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Production State: `sources/2026-W33/production-state.json`
- Lifecycle before Core Discovery advancement: `ISSUE_INITIALIZED`
- Current machine action: `stage:discovery`
- Target Human Gate: `ARCHITECTURE_REVIEW`

## Current Discovery authority

- Discovery: `sources/2026-W33/discovery/discovery-v2.jsonl`
- Record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Canonical X manifest: `sources/2026-W33/external/x/x-source-intake-v2.json`
- X manifest SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- Discovery acceptance: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- Acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`
- Graph SHA-256: `f7ba629fffb48921b139034c4d44941507b83594f76a59dd9151c5270a995eff`

## Semantic authority / work records

- Luna reconstruction handoff: `sources/2026-W33/execution/handoffs/w33-discovery-rebuild-luna-r1.md`
- Luna reconstruction session: `sources/2026-W33/execution/sessions/w33-luna-discovery-rebuild-20260829-r1.md`
- Sol Discovery review: `sources/2026-W33/execution/reviews/w33-discovery-sol-review-20260829-r4.md`
- Sol review session: `sources/2026-W33/execution/sessions/w33-sol-discovery-review-20260829-r4.md`
- Sol acceptance session: `sources/2026-W33/execution/sessions/w33-sol-discovery-acceptance-20260829-r5.md`

## Current semantic status

`DISCOVERY_ACCEPTANCE_READY_FOR_CORE`

The 41-record Discovery candidate has passed Sol semantic review. The canonical Core Discovery acceptance has been reconstructed from current Discovery/Raw/X bytes. The next repository operation must be a request-only `ADVANCE_STAGE` commit followed by trusted Core execution. Do not begin Screening until Production State records `DISCOVERY_COLLECTED`.

## Role split

- Sol: scope, research strategy, cross-source interpretation, Screening/Evidence/Materiality/Completeness/Selection/Architecture/editorial judgment, semantic review of Luna output.
- Luna: bounded source-local collection, exact-byte recovery, schema-conforming materialization, prescribed validation/Git work under explicit handoff.
- Core v2: deterministic schema/invariant/provenance/checkpoint/lifecycle enforcement.
- Human: Architecture Review, Publication Preview, genuine exceptions.

Luna must not invent scope, add unapproved sources, perform cross-document interpretation, decide Selection/Architecture, or infer Human Gate decisions. Ambiguity is surfaced rather than guessed.
