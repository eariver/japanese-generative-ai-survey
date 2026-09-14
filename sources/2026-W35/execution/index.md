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
- Current State SHA-256: `fa82abcd52f9af71a01301ffbb7726b03654e4d0c2c39c05da084c751cfaed0b`
- Current lifecycle: `ISSUE_INITIALIZED`
- Current terminal reason: `AWAITING_GROK_BLOCKED`
- Current next action: `import Grok result -> record-result -> stage:discovery`
- Production Line authority: `production/survey-core-v2 @ 774dd39a951c9ac3818e83dfffd4c7666efb0a20` (created this session from reviewed main; unchanged since)
- W35 branch basis: `weekly/2026-W35-v2-work` from Production Line head (never branched directly from main)
- Main invariant: `main` remains review target only; no Core repair merged to main (none exists)

## Human Gates

- Architecture Review: `pending`
- Publication Preview: `pending`
- Detailed review records: none recorded yet

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Latest Drive task-file path/reference: `Grok_X_SourseIntake/Weekly/2026-W35/weekly-x-2026-W35/grok-task.md`
- Repository task authority: `sources/2026-W35/external/x/weekly-x-2026-W35/grok-task.md`
- Latest result disposition: `AWAITING_GROK` (manifest `sources/2026-W35/external/x/x-source-intake-v2.json`)

## Deviations

- Contract-compliant blocking stop at `ISSUE_INITIALIZED`: formal Discovery acceptance requires
  a COMPLETE X manifest; no Discovery/Evidence/Selection/Architecture artifacts materialized and
  no lifecycle transition attempted without the Grok result. Missing input, required collector,
  blocking stage, and continuation point are recorded in the session log and instruction record.

## Shared Core defects

- None discovered in this session. No repair branch or PR exists; `main` unmerged by design.

## Sessions

- `sessions/w35-sol-initialize-through-architecture-review-20260915-r1.md`
- `sessions/w35-pre-discovery-research-prep-20260915-r1.md` (non-authoritative preparation input)

## Instruction authority

- `requests/sol-w35-initialize-through-architecture-review-20260915-r1.md`

## Final disposition

`BLOCKED_ON_EXTERNAL_HANDOFF (AWAITING_GROK)`
