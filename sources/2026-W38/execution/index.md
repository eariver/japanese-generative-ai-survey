# Survey Production execution index — 2026-W38

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W38/production-state.json`.

## Current authority

- Issue / edition: `2026-W38`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W38-v2-work`
- Start-of-run reviewed `main`: `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`
- Run started: `2026-09-19T03:34:37Z`
- Requested stop: `PUBLICATION_PREVIEW` (via `sol-w38-architecture-r2-approved-through-publication-preview-20260919.md`)
- Production Profile: `sources/2026-W38/production-profile.json`
- Production State: `sources/2026-W38/production-state.json`
- Current State SHA-256: `2372b415f8382f084d763f91bf71aad8c41f2ab8d7e4bcee7f7bfe963327ddbe`
- Current lifecycle: `RELEASE_CANDIDATE`
- Current terminal reason: `HUMAN_GATE_REACHED`
- Current next action: `PUBLICATION_PREVIEW`

## Human Gates

- Architecture Review: `APPROVED` (canonical revision 1 for Human-facing r2 content; reviewed `56b6d3d65c5b4105a410e61a22eb083e66fa344c`, reviewed_at `2026-09-19T05:46:14Z`; record `gates/reviews/architecture-r1.json`, immutable snapshot `gates/reviews/approvals/architecture-r1.json`; r1 surface superseded for decision, historical bytes retained, no decision ever recorded on r1)
- Publication Preview: `pending` (fresh r1 shell/dossier is the current Human target; no decision recorded)
- Detailed review records: architecture r1 shell/dossier (historical), architecture r2 shell/dossier (approved content), publication-preview r1 shell/dossier (current pending target)
- Timestamp correction ledger: `sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md` (r1 `NOT_PRESENTABLE_FOR_DECISION_DUE_TO_TIMESTAMP_PROVENANCE`; State/validation historical `recorded_at` values invalid as wall-clock times; lifecycle/state identities remain authoritative)
- Downstream monotonicity note: `sources/2026-W38/execution/provenance/w38-downstream-monotonicity-note-20260919.md` (Stage history `06:47/06:48/06:49Z` monotonicity-preserving, not wall-clock)
- Validation-report recovery note: `sources/2026-W38/execution/provenance/w38-validation-report-recovery-20260919.md` (deleted deterministic report recovered byte-identical, verified against sealed checkpoint SHA)

## Publication Candidate

- Current Human review target: `f2306ce407a6dc5c79e0125e3c5e8f49f04bba61` (exact branch commit with State + Candidate + Candidate-bound PDF)
- Candidate SHA-256: `43c7d33a457d74b04cbba571e006453f8cea27f4dab134e6265bb55f115ce409`
- PDF: `surveys/weekly/2026-W38/main.pdf` (11 pages, 344241 bytes, SHA-256 `767f4d98c366ae3c7247da635a6ea0b68753f58327104287ab4fb9d8ec9a2543`, CI run `35425249262`, artifact `10577998030`)
- Preview shell: `execution/reviews/publication-preview-r1.md` (SHA-256 `39d1dca71ae498002e041398c57e28d074642301fffcc5a5838ddc8a83fdc8de`)
- Preview dossier: `execution/reviews/publication-preview-r1-dossier.md` (SHA-256 `1664442719a550d6cf8741fc7d30200a86022fa37f41a0c537934b893ff2bf2a`)
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

- Timestamp provenance repair (Issue #507 recurrence): pre-Human-Gate metadata-only correction via `execution/provenance/w38-execution-time-correction-20260919.md`. r1 review surface preserved but not usable for decision; fresh r2 surface generated with actual wall-clock provenance. No semantic regeneration. Historic note: the original run stopped contract-compliantly at `ISSUE_INITIALIZED / AWAITING_GROK` before Grok r2 return; formal Discovery and later stages have since completed.
- Downstream run: Human Architecture r2 `APPROVED` canonically recorded (revision 1, reviewed `56b6d3d65`, `2026-09-19T05:46:14Z` actual wall clock); frozen upstream carried through Draft → TeX → CI PDF → manuscript/bundle/reviews → Candidate → `RELEASE_CANDIDATE`. Stage history `06:47/06:48/06:49Z` values are monotonicity-preserving per `w38-downstream-monotonicity-note-20260919.md`. One worker incident (deleted deterministic validation report) recovered byte-identical with sealed-SHA verification per `w38-validation-report-recovery-20260919.md`; no semantic impact. One pre-commit TeX typo repaired; no semantic change.

## Shared Core defects

- None discovered in this run. Shared-Core repair explicitly out of scope; Production Line pin untouched.

## Sessions

- `sessions/w38-sol-initialize-through-grok-handoff-20260919-r1.md`
- `sessions/w38-pre-discovery-research-prep-20260919-r1.md` (non-authoritative pre-Discovery input, NOT Discovery)
- `sessions/w38-sol-resume-grok-r2-through-architecture-review-20260919-r1.md` (sync + r2 intake + Discovery + Architecture pipeline)
- `sessions/w38-timestamp-provenance-repair-20260919-r1.md` (metadata-only timestamp repair + fresh r2 review surface; no semantic regeneration)
- `sessions/w38-r2-approved-through-publication-preview-20260919.md` (r2 APPROVED through Publication Preview r1 PENDING; Draft/TeX/CI-PDF/manuscript/bundle/reviews/candidate pipeline)

## Final disposition

`RELEASE_CANDIDATE / fresh Human Publication Preview r1 pending` (Discovery = 13, Screening = 12 KEEP / 1 DROP, Evidence = 9 VERIFIED + 3 PARTIAL, Selection = 11 SELECTED / 1 HOLD, Architecture = 7 packages, Draft = 7/7, PDF = 11 pages, Candidate READY_FOR_PUBLICATION_PREVIEW, Human decisions = 1 Architecture APPROVED + 0 Preview, shared-Core changed paths = 0)

## Gate

- Human Architecture Review r1: `execution/reviews/architecture-r1.md` + dossier `execution/reviews/architecture-r1-dossier.md` (historical bytes retained; superseded for Human decision by timestamp-provenance repair, no decision was recorded on r1)
- Human Architecture Review r2: `execution/reviews/architecture-r2.md` + dossier `execution/reviews/architecture-r2-dossier.md` (approved content; canonical decision record `gates/reviews/architecture-r1.json` revision 1 + immutable snapshot `gates/reviews/approvals/architecture-r1.json`)
- Human Publication Preview r1: `execution/reviews/publication-preview-r1.md` + dossier `execution/reviews/publication-preview-r1-dossier.md` (current PENDING Human target bound to reviewed commit `f2306ce4`; no decision recorded)
