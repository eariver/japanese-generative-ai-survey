# Shared-Core defect record — W41 release blocked pre-freeze (fail-closed stop)

Date: 2026-10-15 JST
Reporter: Muse (HUMAN_PUBLICATION_GO execution)
Severity: RELEASE-BLOCKING (shared Core, not edition content)
Status: RECORDED — shared-Core repair required before resume

## Defect location (frozen Core bytes, read-only)

- File: `scripts/survey_stage_validation_v2.py`, function `_prior_artifacts`
  (frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20`; work-branch
  `scripts/` verified byte-identical to frozen Core — defect is IN frozen Core).
- Interacts with: `scripts/survey_agent_control_v2.py::approve_publication_preview`
  (writes `checkpoint_provenance.publication_preview` = approval-record authority).

## Symptom (exact, reproduced)

Running the mission-mandated Phase D validation for lifecycle `RELEASE_CANDIDATE`
(`survey_stage_validation_v2 --state ... --artifact freeze-record=... --artifact
release-manifest=...`) fails inside `_prior_artifacts`:

```text
prior Stage Checkpoint fails .../schemas/stage-checkpoint-v2.schema.json: $: 'artifacts' is a required property
review result CORE_STAGE_CONTRACT missing or unsafe: sources/2026-W41/execution/validation/freeze-validation-r18.json
```

Cause: `_prior_artifacts` loads EVERY non-null `checkpoint_provenance` ref as a
Stage Checkpoint, including `publication_preview`, which (since the mandated
Phase C approval) points to `gates/publication-preview-approval.json` — an
approval record, not a checkpoint. Schema validation of that file fails.

## Reverse order also fails (no valid sequencing)

- WITHOUT recorded approval: `_validate_stage_semantics` for `RELEASE_CANDIDATE`
  fails at the approval authority (`_authority_ref_path(None)` → authority
  fields invalid), because freeze semantics require the recorded approval.
- WITH recorded approval: `_prior_artifacts` fails as above.
- Therefore the mandated freeze validation + `advance-stage` transition is
  unexecutable under frozen Core in either order. No workaround exists without a
  shared-Core change (prohibited during production) or a Gate bypass (prohibited).

## Impact and safe resting state

- Release BLOCKED pre-freeze. Lifecycle rests at `RELEASE_CANDIDATE` with the
  Human `APPROVED` preview recorded — a clean, meaningful, safe state.
- Completed and formally validated (all Core validators PASS): reader-surface
  gate, quality bundle, semantic (11/11) + visual (2/2) reviews, publication
  candidate (`READY_FOR_PUBLICATION_PREVIEW`, exact approved PDF), Human preview
  approval, freeze record + release manifest (built, individually validated).
- NOT done: `RELEASE_CANDIDATE` stage-level validation, advance to `FROZEN`,
  main merge, release workflow, publication. NOTHING published; `main` untouched;
  approved PDF bytes untouched (SHA `4fd1958c…` re-verified).

## Recovery (for Core maintenance, separate from production)

1. Reviewed shared-Core repair (e.g. `_prior_artifacts` loads only
   checkpoint-shaped provenances, or equivalent reviewed fix) through the Core
   change-management audit.
2. Clean rerun of the freeze validation + advance from THIS exact resting state
   (this failed run is failed evidence and must be rerun, not carried forward).
3. Then continue the authorized mission phases (merge → workflow → closure).

## Evidence pointers

- Failing command + output quoted above (this turn's execution log).
- State at stop: `sources/2026-W41/production-state.json` (`RELEASE_CANDIDATE`,
  preview approved). Artifacts: `publication/v2/` (gate, bundle, reviews,
  candidate, approval, freeze, manifest), `orchestration/v2/checkpoints/`
  (`DRAFT_COMPLETE`, `VALIDATED_DRAFT`), `execution/validation/` reports.
