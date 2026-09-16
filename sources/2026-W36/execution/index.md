# Survey Production execution index — 2026-W36

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W36/production-state.json`.

## Current authority

- Issue / edition: `2026-W36`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W36-v2-work`
- Start-of-run reviewed `main`: `5acbff8528890ed9fc324c0227e6c4e43067c438`
- Run started: `2026-09-16T14:04:14Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W36/production-profile.json`
- Production State: `sources/2026-W36/production-state.json`
- Current State SHA-256: `b7116d2aa904d5f71bf6ef9704cee3c5c3e24685132a3aaa0b69b82324c92ed9`
- Current lifecycle: `ISSUE_INITIALIZED`
- Current terminal reason: `AWAITING_GROK_BLOCKED`
- Current next action: `import Grok result -> record-result -> stage:discovery`
- Formal Discovery: `not accepted` (count = 0)
- Core changes: `0`
- Human decisions: `0`
- Pinned Production Line: `production/survey-core-v2 @ 774dd39a951c9ac3818e83dfffd4c7666efb0a20` (untouched)
- W36 branch basis: `weekly/2026-W36-v2-work` from exact main `5acbff85` (remote read-back verified)
- Canonical ordinary window: ET `[2026-08-28T18:00:00-04:00, 2026-09-04T18:00:00-04:00)` /
  UTC `[2026-08-28T22:00:00Z, 2026-09-04T22:00:00Z)` /
  JST `[2026-08-29T07:00:00+09:00, 2026-09-05T07:00:00+09:00)`, end-exclusive

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
- Grok run ID: `weekly-x-2026-W36`
- Repository task authority: `sources/2026-W36/external/x/weekly-x-2026-W36/grok-task.md`
- Latest Drive task-file path/reference: `Grok_X_SourseIntake/Weekly/2026-W36/weekly-x-2026-W36/grok-task.md`
- Intended Drive result folder: `Grok_X_SourseIntake/Weekly/2026-W36/weekly-x-2026-W36`
- Expected result filename: `grok-x-result.md`
- Latest result disposition: `AWAITING_GROK` (no Raw result yet; manifest
  `sources/2026-W36/external/x/x-source-intake-v2.json`)

## Deviations

- None. Contract-compliant `AWAITING_GROK_BLOCKED` stop (missing required X input), not an
  Exception Gate. Issue #497 + known release-workflow CLI defect intentionally untouched.

## Shared Core defects

- None discovered in this run. No repair branch or PR exists.

## Pre-Discovery research preparation

- `sessions/w36-pre-discovery-research-prep-20260916-r1.md` (non-authoritative input only):
  all 12 lanes breadth-scanned; lanes F/I `NONE_FOUND`/`UNCERTAIN` pending Grok + first-party
  recheck; post-cutoff Late Breaking separated (vLLM 0.29.0, AgentAudit, Anthropic 09-09
  assessment, Gloo Code GA).

## Sessions

- `sessions/w36-sol-initialize-through-architecture-review-20260916-r1.md`
- `sessions/w36-pre-discovery-research-prep-20260916-r1.md` (non-authoritative preparation input)

## Instruction authority

- `requests/w36-sol-initialize-through-architecture-review-20260916-r1.md`

## Final disposition

`AWAITING_GROK_BLOCKED`
