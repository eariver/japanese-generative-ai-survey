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
- Current State SHA-256: `560f0fda6e17c45f94d2b31526c577c42b2e178f5eb048d651b6cfd7067f91dd`
- Current lifecycle: `ARCHITECTURE_ESTABLISHED`
- Current terminal reason: `HUMAN_GATE_REACHED`
- Current next action: `ARCHITECTURE_REVIEW` (Human decision only)
- Formal Discovery: `accepted` (count = 14: 1 Grok r3 X-ledger + 13 W37-window primaries/secondaries)
- Screening: `13 KEEP / 1 DROP` (rumor-only GLM-5.5)
- Evidence: `11 VERIFIED + 2 PARTIAL` (views + materiality + completeness LIMITED 3/3 SATISFIED)
- Selection: `12 SELECTED / 1 HOLD` (7 packages, READY_FOR_ARCHITECTURE_REVIEW)
- Architecture: `ESTABLISHED` (Sol-owned, 0 blocking)
- Human decisions: `0` (r1 PENDING, no decision inferred)
- Shared-Core changed paths: `0`
- Canonical ordinary window: ET `[2026-09-04T18:00:00-04:00, 2026-09-11T18:00:00-04:00)` / UTC `[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)` / JST `[2026-09-05T07:00:00+09:00, 2026-09-12T07:00:00+09:00)`, end-exclusive

## Human Gates

- Architecture Review: `pending` (r1 shell + 12-element dossier at `execution/reviews/architecture-r1.md`, reviewed commit `1bef366ac8e21641027ddb9feda6263c0ed01aa4`)
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
- `sessions/w37-sol-resume-grok-r3-through-architecture-review-20260918-r1.md` (COMPLETE_AT_GATE)

## Sol supervisory reviews (same run)

- `reviews/sol-w37-discovery-completeness-20260918.md` (NON_BLOCKING)
- `reviews/sol-w37-evidence-authority-consumption-20260918.md` (CLEAN)
- `reviews/sol-w37-materiality-selection-20260918.md` (CLEAN)
- `reviews/sol-w37-architecture-20260918.md` (OWNED, 0 blocking)
- `reviews/architecture-r1.md` (PENDING shell) + `reviews/architecture-r1-dossier.md` (12-element dossier)

## Final disposition

`ARCHITECTURE_ESTABLISHED / HUMAN_GATE_REACHED / fresh Human Architecture Review pending (r1)`
