# W37 Core-defect record — Freeze closure bounded compatibility (no Core change)

Status: `SHARED_CORE_DEFECT / EDITION_LOCAL_COMPATIBILITY / NO_CORE_CHANGE`
Date: `2026-09-19 JST`
Edition: `2026-W37`
Work branch: `weekly/2026-W37-v2-work`

## Defect 1 — profiled Freeze visual authority expects legacy record

`scripts/survey_profiled_freeze_v2.py::build_profiled_freeze` validates the
visual authority via `publication.validate_visual_review`, which requires the
legacy post-approval `visual-review-record-v2` schema (`pdf_path` top-level).

W37 (like W34/W35/W36) binds the candidate-bound pre-preview VISUAL review
(`sources/2026-W37/publication/v2/visual-review-v2.json`, reader review-record
schema with `pdf.path`), validated by
`survey_reader_publication_v2.validate_review_record`.

Reproduction (valid RELEASE_CANDIDATE after Publication Preview r4 APPROVED):

```text
PYTHONPATH=. python3 scripts/survey_profiled_freeze_v2.py \
  --state sources/2026-W37/production-state.json
```

fails with:

```text
Visual Review record fails schemas/visual-review-record-v2.schema.json:
$: 'pdf_path' is a required property
```

Precedent: `sources/2026-W36/execution/defects/w36-freeze-core-defects-20260918.md`.
W34/W35/W36 closed Freeze via the canonical compatibility path
`survey_publication_v2.build_freeze`, which binds the candidate-bound
pre-preview VISUAL review. W37 uses the same canonical compatibility path.
No shared-Core byte change.

## Defect 2 — Freeze stage validator misclassifies Human approval as checkpoint

`scripts/survey_stage_validation_v2.py::_prior_artifacts` iterates every
non-null `checkpoint_provenance` entry and validates each file against
`schemas/stage-checkpoint-v2.schema.json`.

After canonical Human Publication Preview approval,
`checkpoint_provenance.publication_preview` legitimately references the
Publication Preview approval JSON
(`sources/2026-W37/gates/publication-preview-approval.json`), not a Stage
Checkpoint. The validator misclassifies it and fails:

```text
prior Stage Checkpoint fails schemas/stage-checkpoint-v2.schema.json:
$: 'artifacts' is a required property
```

Precedent: `sources/2026-W35/execution/defects/w35-freeze-prior-checkpoint-provenance-core-defect-20260915.md`
(and W36 `survey_stage_validation_v2 with bounded Freeze/Human-Gate artifact
admission correction`).

## W37 bounded compatibility (edition-local, runtime-only)

- Freeze Record + Release Manifest built only via canonical
  `survey_publication_v2.build_freeze` (exact approved bytes preserved,
  release identity `weekly/2026-W37`).
- Stage validation report generated with the W34/W35/W36 bounded admission
  correction, runtime/in-memory only:
  - preserve and validate all true prior Stage Checkpoints;
  - exclude Human Gate approval provenance from Stage Checkpoint admission;
  - validate the Publication Preview approval through the dedicated
    Human-Gate authority path (`validate_preview_approval`);
  - bind the already candidate-bound pre-preview VISUAL review as
    `visual-review-record` (no post-approval review invented).
- Report + reviews + Stage Checkpoint follow the exact W34/W35/W36 authority shape
  (3 artifacts, 2 deterministic reviews).
- No shared-Core file changed. No approved content regenerated.

Approved bytes preserved:

- PDF SHA-256 `09dea4e7fe7eecc6c4dae39a308899849ac84e598f9251b3d415e24b7ee3e268`
- bytes `309187`, pages `11`
- Candidate internal `0f7c5af2dd069412b54aced39c43366975548ed50e2358bf3b7264775fb59f04`
- reviewed repository commit `07da54bfe3c1bc186abf7016486a4a6768f322c5`
