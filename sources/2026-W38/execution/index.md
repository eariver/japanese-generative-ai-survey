# Survey Production execution index — 2026-W38

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W38/production-state.json`.

## Current authority

- Issue / edition: `2026-W38`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W38-v2-work`
- Start-of-run reviewed `main`: `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`
- Run started: `2026-09-19T03:34:37Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W38/production-profile.json`
- Production State: `sources/2026-W38/production-state.json`
- Current State SHA-256: `0542a1bfdcc83851da8d0c2e512065752faeeb78c25d5d3102c5a05f797b00ed`
- Current lifecycle: `ARCHITECTURE_ESTABLISHED`
- Current terminal reason: `HUMAN_GATE_REACHED`
- Current next action: `ARCHITECTURE_REVIEW`

## Human Gates

- Architecture Review: `pending` (r1 superseded for decision by timestamp-provenance repair — historical bytes retained; r2 is the current pending Human target)
- Publication Preview: `pending`
- Detailed review records: r1 shell/dossier (historical), r2 shell/dossier (current pending target)
- Timestamp correction ledger: `sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md` (r1 `NOT_PRESENTABLE_FOR_DECISION_DUE_TO_TIMESTAMP_PROVENANCE`; State/validation historical `recorded_at` values invalid as wall-clock times; lifecycle/state identities remain authoritative)

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Grok run ID: `weekly-x-2026-W38`
- Repository task authority: `sources/2026-W38/external/x/weekly-x-2026-W38/grok-task.md` (SHA-256 `e90966695dec041241124cb0d190496b8f4014323d9315e92ff4796b5cb62b4c`, edition-local W38 breadth hardening included)
- Latest Drive task-file path/reference: `Grok_X_SourseIntake/Weekly/2026-W38/weekly-x-2026-W38/grok-task.md`
- Intended Drive result folder: `Grok_X_SourseIntake/Weekly/2026-W38/weekly-x-2026-W38`
- Expected result filename: `grok-x-result.md`
- Accepted result: `grok-x-result-r2.md` (Drive file ID `19YOzmzkuGn8Elk23tsQH3V6eUM7Jayru`), imported exact repository Raw `sources/2026-W38/external/x/weekly-x-2026-W38/raw/grok-x-result-r2.md` (bytes `16022`, SHA-256 `dac7e19fefcd2760efe82e4e602c8faa0f819b39866c0cffca6f6f02cc9e2634`, revision `r2`)
- Sol review: `sources/2026-W38/execution/reviews/sol-grok-x-r2-review-20260919.md` (`PASS_WITH_DERIVED_COUNT_CORRECTIONS`; row-level 25-URL ledger accepted; corrected counts: 25 total / 23 ordinary / 2 late-breaking / 15 ordinary accounts [7 independent + 3 official + 5 community]; C1 ordinary URLs 7; C2 class `MULTI_ACCOUNT_X`; C3 `OFFICIAL_ONLY_X`)
- r1 disposition: historical failed Raw on Drive only (`REQUEST_CORRECTION`, never imported as canonical result)
- Manifest `sources/2026-W38/external/x/x-source-intake-v2.json` status `COMPLETE` (run `weekly-x-2026-W38`, `SUCCESS`, `DISCOVERY_RECORDED` -> `w38-grok-r2-25-url-ledger`); Raw front-matter `observed_at` preserved exactly but NOT used as machine execution provenance (Sol timestamp caveat recorded in record rationale)
- No Drive access attempted from Muse; no connector searched for or installed.

## Discovery

- Discovery JSONL: `sources/2026-W38/discovery/discovery-v2.jsonl` (13 records: 1 X seed + 10 fresh primaries + 2 W37 carry-over revalidations)
- Discovery acceptance: `sources/2026-W38/discovery/discovery-accepted-v2.json` (graph validated; X integration validated)
- Collector run: `w38-primary-20260919-r1` (10 webfetch-excerpt raws under `sources/2026-W38/collectors/primary/runs/20260919T000000Z/`) + `w38-carryover-20260919-r1` (carry-over verification note)
- Sol completeness review: `sources/2026-W38/execution/reviews/sol-w38-discovery-completeness-20260919.md` (`NON_BLOCKING_WITH_INDIVIDUAL_LIMITS`)
- Lane coverage: A/B/C/D/F/G/H/J/K/L covered; E partial (creator-tool video only); I quiet (legitimate after check)

## Deviations

- Timestamp provenance repair (Issue #507 recurrence): pre-Human-Gate metadata-only correction via `execution/provenance/w38-execution-time-correction-20260919.md`. r1 review surface preserved but not usable for decision; fresh r2 surface generated with actual wall-clock provenance. No semantic regeneration; no Human decision recorded. Historic note: the original run stopped contract-compliantly at `ISSUE_INITIALIZED / AWAITING_GROK` before Grok r2 return; formal Discovery and later stages have since completed (see Final disposition).

## Shared Core defects

- None discovered in this run. Shared-Core repair explicitly out of scope; Production Line pin untouched.

## Sessions

- `sessions/w38-sol-initialize-through-grok-handoff-20260919-r1.md`
- `sessions/w38-pre-discovery-research-prep-20260919-r1.md` (non-authoritative pre-Discovery input, NOT Discovery)
- `sessions/w38-sol-resume-grok-r2-through-architecture-review-20260919-r1.md` (sync + r2 intake + Discovery + Architecture pipeline)
- `sessions/w38-timestamp-provenance-repair-20260919-r1.md` (metadata-only timestamp repair + fresh r2 review surface; no semantic regeneration)

## Final disposition

`ARCHITECTURE_ESTABLISHED / fresh Human Architecture Review pending` (Discovery = 13, Screening = 12 KEEP / 1 DROP, Evidence = 9 VERIFIED + 3 PARTIAL, Selection = 11 SELECTED / 1 HOLD, Architecture = 7 packages READY_FOR_ARCHITECTURE_REVIEW, Human decisions = 0, shared-Core changed paths = 0)

## Gate

- Human Architecture Review r1: `execution/reviews/architecture-r1.md` + dossier `execution/reviews/architecture-r1-dossier.md` (historical bytes retained; superseded for Human decision by timestamp-provenance repair, no decision was recorded on r1)
- Human Architecture Review r2: `execution/reviews/architecture-r2.md` + dossier `execution/reviews/architecture-r2-dossier.md` (current PENDING Human target, same Architecture triple + correction ledger)
