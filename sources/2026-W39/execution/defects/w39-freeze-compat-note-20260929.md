# W39 Freeze compatibility note (edition-local, no shared-Core change)

Status: `EDITION_LOCAL_COMPATIBILITY / DOCUMENTED`
Date: `2026-09-29`

## Observation

Current frozen Core carries the known W34–W38 Freeze compatibility defects, both reproduced verbatim in the W39 `RELEASE_CANDIDATE -> FROZEN` transition:

1. `survey_profiled_freeze_v2.py` rejects the candidate-bound modern visual-review shape
   (expects legacy `pdf_path` field). Canonical publication freeze helper
   `survey_publication_v2.build_freeze` used instead (W38-compatible path).
2. Frozen stage validation misclassifies Human approval provenance
   (`checkpoint_provenance.publication_preview` → `gates/publication-preview-approval.json`)
   as a Stage Checkpoint, failing checkpoint-schema admission.

## Reproduction boundary

- `survey_stage_validation_v2._prior_artifacts` iterates all provenance values as checkpoints.
- `survey_stage_validation_v2._current_artifacts` rejects the schema-required
  `visual-review-record` extra for non-draft lifecycles, while the checkpoint schema's
  `freezeArtifacts` rule requires it alongside `freeze-record`/`release-manifest`.

## Safe edition-local handling (runtime/in-memory only)

- True checkpoints remained byte-validated; Human-gate approval validated through
  Human-gate authority (file presence + state-pinned SHA) rather than checkpoint admission.
- Canonical sibling `VALIDATED_DRAFT` checkpoint admitted for the publication-candidate
  authority it pins (byte-validated like every true checkpoint).
- `visual-review-record` admitted as the single extra current artifact exactly as the
  checkpoint schema's `freezeArtifacts` rule requires.
- Driver: `/tmp/opencode/freeze_validate_compat.py` (transient; not committed).
  No committed shared-Core file modified.

## Production disposition

- Freeze validation PASS (`RELEASE_CANDIDATE -> FROZEN`); advance PASS; state `FROZEN`.
- Freeze record + release manifest bind exact approved r6 Candidate/PDF bytes.
- Core-maintenance pointer: same defect class as W34–W38; shared-Core repair out of scope.

## Production disposition (post-release note)

- See release workflow section of the r6-approved session record for the known
  post-release `validate-state` CLI defect handling, if reproduced.
