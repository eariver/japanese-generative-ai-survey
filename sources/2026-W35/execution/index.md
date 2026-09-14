# Survey Production execution index — 2026-W35

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W35/production-state.json`.

## Current authority

- Issue / edition: `2026-W35`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W35-v2-work`
- Start-of-run reviewed `main`: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- Run started: `2026-09-14T15:00:00Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W35/production-profile.json`
- Production State: `sources/2026-W35/production-state.json`
- Current State SHA-256: `7eba58b385166a980e18c3d28291824158c6547227ba8c210060432310c9f331`
- Current lifecycle: `ARCHITECTURE_ESTABLISHED`
- Current terminal reason: `HUMAN_GATE_REACHED`
- Current next action: `ARCHITECTURE_REVIEW` (Human decision only; no further autonomous advancement)
- Production Line authority: `production/survey-core-v2 @ 774dd39a951c9ac3818e83dfffd4c7666efb0a20` (created this session from reviewed main; unchanged since)
- W35 branch basis: `weekly/2026-W35-v2-work` from Production Line head (never branched directly from main)
- Main invariant: `main` remains review target only; no Core repair merged to main (none exists)

## Human Gates

- Architecture Review: `pending` (r1; dossier + shell under `execution/reviews/`; reviewed commit recorded in `architecture-r1.md`)
- Publication Preview: `pending`
- Detailed review records: `execution/reviews/architecture-r1.md` (shell), `architecture-r1-dossier.md` (mandatory dossier); no decision recorded

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Latest Drive task-file path/reference: `Grok_X_SourseIntake/Weekly/2026-W35/weekly-x-2026-W35/grok-task.md`
- Repository task authority: `sources/2026-W35/external/x/weekly-x-2026-W35/grok-task.md`
- Latest result disposition: `COMPLETE` (`SUCCESS` / `DISCOVERY_RECORDED`; r3 Sol-reviewed correction, 35/25/0/10; manifest `sources/2026-W35/external/x/x-source-intake-v2.json`)
- Accepted Grok Raw: `sources/2026-W35/external/x/weekly-x-2026-W35/raw/grok-x-result-r3.md` (`5d1ee181…`, 21589 bytes, r2 GitHub-byte authority)

## Stage aggregates

- Discovery: 20 accepted (graph `fbab63dd`) | Screening: 19 KEEP / 1 DROP (result set `a04c2e0f`) | Evidence: 8 VERIFIED + 11 PARTIAL (result set `deae874c`) | Selection: 17 SELECTED / 2 HOLD | Architecture: 5 packages, review summary READY_FOR_ARCHITECTURE_REVIEW

## Deviations

- r1-guard Raw mismatch led to a contract-compliant no-write STOP; resolved by r2 override (one-space transfer normalization, ledger-unaffecting). No writes occurred under the failed guard.
- One issue-local source_type vocabulary defect self-caught pre-commit and repaired edition-locally with full downstream regeneration (canonical PRIMARY_OFFICIAL/PRIMARY_PAPER/SECONDARY/SOCIAL classes). No generic Core defect; no repair branch; Production Line untouched.

## Shared Core defects

- None discovered across both sessions. No repair branch or PR exists; `main` unmerged by design.

## Sessions

- `sessions/w35-sol-initialize-through-architecture-review-20260915-r1.md`
- `sessions/w35-pre-discovery-research-prep-20260915-r1.md` (non-authoritative preparation input)
- `sessions/w35-sol-resume-grok-r3-through-architecture-review-20260915-r1.md` (this resume run)

## Sol supervisory reviews

- `decisions/sol-w35-supervisory-reviews-20260915-r1.md` (completeness, authority-consumption, materiality/selection, architecture; 0 blocking findings)

## Instruction authority

- `requests/sol-w35-initialize-through-architecture-review-20260915-r1.md`
- `requests/sol-w35-resume-from-grok-r3-through-architecture-review-20260915-r1.md` (r1)
- `requests/sol-w35-resume-from-grok-r3-through-architecture-review-20260915-r2.md` (r2 override, top authority)

## Final disposition

`FRESH_HUMAN_ARCHITECTURE_REVIEW_REQUIRED`
