# Survey Production execution index — 2026-W37

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W37/production-state.json`.

## Current authority

- Issue / edition: `2026-W37`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W37-v2-work`
- Start-of-run reviewed `main`: `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`
- Run started: `2026-09-18T12:54:05Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W37/production-profile.json`
- Production State: `sources/2026-W37/production-state.json`
- Current State SHA-256: `edcd51daf03a8b1050d7ddfe30f1b26753dfa896a0d492329f01023d6d42f192`
- Current lifecycle: `ARCHITECTURE_ESTABLISHED`
- Current terminal reason: `HUMAN_GATE_REACHED`
- Current next action: `ARCHITECTURE_REVIEW` (independent review first, then Human decision)
- Formal Discovery: `accepted, preserved` (count = 14: 1 Grok r3 X-ledger + 13 W37-window primaries/secondaries)
- Screening r2: `13 KEEP / 1 DROP` (neutral worker provenance; Fusion KEEP on verified 17:00Z ordinary)
- Evidence r2: `11 VERIFIED + 2 PARTIAL` (views + materiality + completeness LIMITED 3/3 SATISFIED)
- Selection r2: `12 SELECTED / 1 HOLD` (7 packages, READY_FOR_ARCHITECTURE_REVIEW)
- Architecture r2: `ESTABLISHED` (deterministic PASS; RC-1..RC-5 repairs; independent review pending, 0 worker authority claims)
- Human decisions: `0` (r2 PENDING; prior r1 `REQUEST_CHANGES` was independent-review verdict, not a Human decision)
- Shared-Core changed paths: `0`
- Canonical ordinary window: ET `[2026-09-04T18:00:00-04:00, 2026-09-11T18:00:00-04:00)` / UTC `[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)` / JST `[2026-09-05T07:00:00+09:00, 2026-09-12T07:00:00+09:00)`, end-exclusive

## Human Gates

- Architecture Review: `pending` (r2 shell + worker dossier at `execution/reviews/architecture-r2.md`, reviewed commit `55e700a34765654cd2ced0c2a454d4fb3433dd4f`; r1 shell/dossier preserved as invalidated history)
- Publication Preview: `pending`
- Detailed review records: no Human decision recorded (APPROVED/REQUEST_CHANGES not invented)

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Grok run ID: `weekly-x-2026-W37`
- Repository task authority: `sources/2026-W37/external/x/weekly-x-2026-W37/grok-task.md`
- Latest Drive task-file path/reference: `Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37/grok-task.md`
- Intended Drive result folder: `Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37`
- Expected result filename: `grok-x-result.md`
- Latest result disposition: `SUCCESS` (r3 `grok-x-result-r3.md`, 14803B/`318ed342`, observed 2026-09-18T13:55:00Z; manifest `COMPLETE`, DISCOVERY_RECORDED `w37-grok-r3-45-url-ledger`; Sol review PASS_WITH_DERIVED_COUNT_CORRECTIONS, 45/24/1/20, 12 ordinary INDEPENDENT)
- No Drive access attempted from Muse; no connector searched for or installed.

## Deviations

- Partial-matrix overwrite guard hit twice during Selection runner (worker-side file handling, not Core defect); resolved by removing uncommitted partial matrix and rerunning cleanly.
- Image (D) / video (E) lanes legitimately quiet after examination; not an Exception Gate.

## Shared Core defects

- None discovered in this run. Issue #497, release `validate-state` defect, and reader-surface Core defects intentionally untouched (separate Core maintenance owns shared-Core repair).

## Sessions

- `sessions/w37-sol-initialize-through-grok-handoff-20260918-r1.md`
- `sessions/w37-pre-discovery-research-prep-20260918-r1.md` (non-authoritative pre-Discovery input, NOT Discovery)
- `sessions/w37-sol-resume-grok-r3-through-architecture-review-20260918-r1.md` (superseded r1 run; worker files retained as `WORKER_SELF_REVIEW / NON_AUTHORITATIVE_AS_SOL`)
- `sessions/w37-sol-r1-request-changes-regenerate-r2-20260919.md` (COMPLETE_AT_GATE)

## Review provenance in this run

- Prior independent authority: `reviews/sol-w37-architecture-r1-independent-review-20260919.md` (`REQUEST_CHANGES`, not a Human decision); r1 surface invalidated as unpresented (`execution/operator-invalidations/architecture-invalidation-0001.json`, boundary `DISCOVERY_COLLECTED`)
- Historical r1 worker files (`sol-w37-discovery-completeness-20260918.md`, `sol-w37-evidence-authority-consumption-20260918.md`, `sol-w37-materiality-selection-20260918.md`, `sol-w37-architecture-20260918.md`): preserved, classified `WORKER_SELF_REVIEW / NON_AUTHORITATIVE_AS_SOL`
- r2 worker dossier (`reviews/architecture-r2-dossier.md`) claims no independent review; r2 awaits independent review
- No new file framed as an independent review was generated in this run

## Historical r1 worker files (superseded, preserved)

- `reviews/sol-w37-discovery-completeness-20260918.md`, `reviews/sol-w37-evidence-authority-consumption-20260918.md`, `reviews/sol-w37-materiality-selection-20260918.md`, `reviews/sol-w37-architecture-20260918.md`: `WORKER_SELF_REVIEW / NON_AUTHORITATIVE_AS_SOL`
- `reviews/architecture-r1.md` (invalidated unpresented shell) + `reviews/architecture-r1-dossier.md`

## Final disposition

`ARCHITECTURE_ESTABLISHED / HUMAN_GATE_REACHED / fresh r2 Architecture Review pending independent review`
