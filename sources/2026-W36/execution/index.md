# Survey Production execution index — 2026-W36

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W36/production-state.json`.

## Current authority

- Issue / edition: `2026-W36`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W36-v2-work`
- Start-of-run reviewed `main`: `5acbff8528890ed9fc324c0227e6c4e43067c438`
- Run started: `2026-09-16T14:04:14Z`; resumed from accepted Grok r4: `2026-09-17T00:08:00+09:00 JST`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W36/production-profile.json`
- Production State: `sources/2026-W36/production-state.json`
- Current State SHA-256: see `production-state.json` (lifecycle `ARCHITECTURE_ESTABLISHED`)
- Current lifecycle: `ARCHITECTURE_ESTABLISHED`
- Current terminal reason: `HUMAN_GATE_REACHED`
- Current next action: `ARCHITECTURE_REVIEW` (Human decision only)
- Formal Discovery: `accepted` (count = 19; graph `9c55b223`)
- Core changes: `0`
- Human decisions: `0`
- Pinned Production Line: `production/survey-core-v2 @ 774dd39a951c9ac3818e83dfffd4c7666efb0a20` (untouched)
- W36 branch basis: `weekly/2026-W36-v2-work` from exact main `5acbff85` (remote read-back verified)
- Canonical ordinary window: ET `[2026-08-28T18:00:00-04:00, 2026-09-04T18:00:00-04:00)` /
  UTC `[2026-08-28T22:00:00Z, 2026-09-04T22:00:00Z)` /
  JST `[2026-08-29T07:00:00+09:00, 2026-09-05T07:00:00+09:00)`, end-exclusive

## Human Gates

- Architecture Review: `pending` (r1 `REQUEST_CHANGES` recorded canonically; fresh r2 shell + 12-element dossier presented; no r2 decision recorded or inferred)
- Publication Preview: `pending`
- Detailed review records: `execution/reviews/architecture-r1.md` (REQUEST_CHANGES r1), `execution/reviews/architecture-r1-dossier.md` (r1), `execution/reviews/architecture-r2.md` (PENDING r2), `execution/reviews/architecture-r2-dossier.md` (r2); canonical `gates/reviews/architecture-r1.json` + `gates/review-index.json`

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
- Accepted result: `grok-x-result-r4.md` (24219B / `a94f543d`; observed `2026-09-16T14:51:00Z`; manifest
  `sources/2026-W36/external/x/x-source-intake-v2.json` COMPLETE, SUCCESS / DISCOVERY_RECORDED)
- Canonical X accounting: 15 unique / 12 ordinary (3 official + 9 independent, 8 accounts) / 0 background / 3 late-breaking; 7 new r4 URLs

## Pipeline aggregates (r1)

- Discovery: 19 (BASE 19)
- Screening: 19 KEEP / 0 DROP (result set `f55a2285`)
- Evidence: 13 VERIFIED / 6 PARTIAL (set `1c0efd9f`); views `aab96ba6`
- Materiality: 18 MATERIAL / 1 CONTEXT; Completeness: LIMITED (3/3 SATISFIED)
- Selection: 18 SELECTED / 1 HOLD; Architecture r2: 6 packages, READY_FOR_ARCHITECTURE_REVIEW (RC-1 thesis corrected; packages/membership unchanged; matrix/selection byte-identical)
- Carry-over: zero formal inherited obligations (W35 RELEASED scanned; no carry roles); no W35 copy; Grok SELECTED never copied

## Deviations

- None blocking. Four issue-local vocabulary defects repaired edition-locally with full downstream regeneration (verification status enum, PROJECT entity/artifact types, missing closure, target-string mismatch, exception rules). No Core defect; no repair branch. Issue #497 + known release-workflow CLI defect intentionally untouched.

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
- `sessions/w36-sol-resume-grok-r4-through-architecture-review-20260917-r1.md` (r4 through Architecture Review; COMPLETE_AT_GATE)
- `sessions/w36-architecture-r1-request-changes-bounded-regen-20260917-r2.md` (r1 REQUEST_CHANGES bounded regen; COMPLETE_AT_GATE)

## Instruction authority

- `requests/w36-sol-initialize-through-architecture-review-20260916-r1.md`
- `requests/sol-w36-resume-from-grok-r4-through-architecture-review-20260917.md` (execution contract for the r1 run)
- `requests/sol-w36-architecture-review-r1-request-changes-20260917.md` (Human/Sol review authority supplied by execution request; r1 decision + RC-1/RC-2 + SELECTION_COMPLETE boundary)

## Provenance correction (RC-2)

- `execution/decisions/sol-w36-supervisory-reviews-20260917-r1.md` preserved byte-identical as worker-generated pre-gate check (not independent Sol authority)
- Classification: `execution/decisions/w36-worker-pregate-review-provenance-20260917-r2.md`; r2 dossier cites imported authority + Worker/Operator validation only

## Final disposition

`HUMAN_GATE_REACHED` (fresh Human Architecture Review r2 pending; no Draft; no Human r2 decision recorded or inferred)
