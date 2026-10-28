# Shared release-workflow defect — `validate-state` subcommand does not exist (W43 observed, NOT repaired)

Status: `SHARED_WORKFLOW_DEFECT / EDITION_OBSERVED / PROVENANCE_RECOVERED_LOCALLLY`
Observed: 2026-10-28, release run #40610449934 (`survey-production-v2-release.yml` on main).
Edition: `2026-W43`, FROZEN State `72f9f511…`, manifest `bc1a1fdd…`, merged main `90b39359e`.

## Failure

Step "Build immutable Release Record and compact Release Stage Checkpoint",
final line:

```text
PYTHONPATH=. python scripts/survey_agent_control_v2.py --repo-root . validate-state --state "$STATE"
```

```text
survey_agent_control_v2.py: error: argument command: invalid choice: 'validate-state'
(choose from advance-stage, approve-architecture, approve-publication-preview, revalidate-publication-surface)
```

Exit code 2 → run conclusion FAILURE — AFTER the Release itself was created,
published, and exact-byte verified by the workflow's own publish step
(tag `weekly/2026-W43`, asset SHA `b09fd181…` == approved bytes).

Uncommitted runner-side outputs lost with the ephemeral checkout:
`merge-verification-v2.json`, `release-record-v2.json`, `FROZEN.json`
checkpoint, RELEASED State, and the provenance PR (never opened).

## Disposition (no shared-Core change during production)

- `.github/workflows/survey-production-v2-release.yml` is a protected shared
  root: read-only during edition production. NOT patched here.
- Provenance recovered with the exact frozen builders the workflow uses
  (`build_merge_verification`, `build_release_record`,
  `survey_release_checkpoint_v2.py`) plus the equivalent frozen
  `agent.validate_agent_state` (VALID), committed through the normal
  `release-record/2026-W43-40610449934` PR and merged to main.
- Resembles the W42 run `39523390651` failure-with-verified-asset pattern
  (CV2-DM-004 family). Shared-workflow repair belongs to a separate reviewed
  Core change; this file is the edition-local record.
