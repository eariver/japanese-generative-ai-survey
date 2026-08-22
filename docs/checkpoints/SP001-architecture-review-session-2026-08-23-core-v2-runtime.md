# SP001 Architecture Review session — Core v2 runtime follow-up — 2026-08-23

## Scope

This checkpoint records the actual Core v2 execution work performed after the Grok/X return was imported and Discovery was prepared for adoption. It is an operational record, not an Architecture Review approval.

## Reviewed generic Core v2 execution repairs

### PR #316 — work-branch local control request

- Added `.github/workflows/survey-production-v2-work-branch-control.yml` as a generic execution surface for Weekly/Special v2 local-stage adoption.
- The path invokes the exact work-branch `scripts/survey_stage_validation_v2.py` and then the existing `survey_agent_control_v2.py advance-stage` controller.
- The surface is `adopt-stage` only and cannot approve either Human Gate.
- Merged to `main` as `05b48e937f7f9e7eaaf2e9db83c1a248cbc5fcd6` and integrated into `special/SP001-v2-work` through PR #317.

### PR #319 — same-repository PR execution

- Connector-authored repository writes did not provide a reliable observable push-trigger path for this session.
- The generic work-branch controller was extended to same-repository pull requests targeting `weekly/*-v2-work` or `special/*-v2-work`.
- The controller validates the Production Profile against the PR base branch, executes the exact PR head bytes, rejects fork execution, writes generated control bytes back to the PR head, and consumes the request after successful execution.
- The path remains `adopt-stage` only and does not alter Human Gate authority.
- Merged to `main` as `4834507508126996295738cc9497e87faaad7d8d` and integrated into `special/SP001-v2-work` through PR #320.

## SP001 Discovery runtime validation

Execution PR: #321 (`trigger/sp001-discovery-control-v2` -> `special/SP001-v2-work`)

GitHub Actions run: `32583682703`

Job: `97056710761`

The request bound:

- current persisted Production State SHA-256: `f47b218ca6df23495ae08020df62f05dbf4766d6de9328018e9b78d8b9d0c076`
- Discovery acceptance: `sources/SP001/discovery/discovery-accepted-v2.json`
- stage review: `sources/SP001/orchestration/v2/reviews/ISSUE_INITIALIZED.json`

Observed execution result:

1. request / Production State / Production Profile identity validation: **PASS**
2. exact `survey_stage_validation_v2.py` execution: **PASS**
   - generated runner-local result path: `sources/SP001/orchestration/v2/validation/ISSUE_INITIALIZED.json`
3. `survey_agent_control_v2.py advance-stage`: **PASS**
   - generated lifecycle: `DISCOVERY_COLLECTED`
   - generated next action: `stage:screening`
   - generated terminal reason: `null`
   - generated checkpoint path: `sources/SP001/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`
4. post-transition resumable-State validation: **FAIL due to generic workflow command wiring**, not due to SP001 Discovery bytes

The failing workflow command attempted:

`survey_agent_control_v2.py validate-state --state ...`

but the agent-first controller does not expose a `validate-state` CLI subcommand. The authoritative resumability validator is `agent.validate_agent_state()`.

Because this failure occurred before the workflow commit step, none of the runner-local generated validation/checkpoint/transitioned-State bytes were persisted. The canonical SP001 Production State therefore correctly remains `ISSUE_INITIALIZED` until the repaired controller re-executes the same accepted Discovery boundary.

## Generic repair in progress

PR #323 repairs both Core v2 control workflows by replacing the nonexistent `validate-state` CLI invocation with a direct call to `agent.validate_agent_state()` against the resulting exact State bytes and current Core v2 config.

Affected workflows:

- `.github/workflows/survey-production-v2-control.yml`
- `.github/workflows/survey-production-v2-work-branch-control.yml`

No lifecycle, artifact, editorial, source-selection, or Human Gate semantics are changed by this repair.

## Current SP001 status at this checkpoint

- Grok/X intake: `COMPLETE`
- canonical Discovery set: 24 records
- Discovery acceptance artifact: prepared and successfully validated during run `32583682703`
- persisted Production State: `ISSUE_INITIALIZED`
- expected next persisted transition after generic repair: `DISCOVERY_COLLECTED`
- target Human Gate: `ARCHITECTURE_REVIEW`
- Exception Gate: not required by the SP001 content or Discovery boundary at this point
