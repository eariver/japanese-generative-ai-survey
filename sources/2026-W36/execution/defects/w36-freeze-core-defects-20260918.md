# W36 Core-defect record — Freeze closure bounded compatibility (no Core change)

Status: `SHARED_CORE_DEFECT / EDITION_LOCAL_COMPATIBILITY / NO_CORE_CHANGE`
Date: `2026-09-18Z`
Edition: `2026-W36`
Work branch: `weekly/2026-W36-v2-work`

## Defect 1 — profiled Freeze visual authority expects legacy record

`scripts/survey_profiled_freeze_v2.py::build_profiled_freeze` validates the
visual authority via `publication.validate_visual_review`, which requires the
legacy post-approval `visual-review-record-v2` schema (`pdf_path` top-level).

W36 (like W34/W35) binds the candidate-bound pre-preview VISUAL review
(`sources/2026-W36/publication/v2/visual-review-v2.json`, reader review-record
schema with `pdf.path`), validated by
`survey_reader_publication_v2.validate_review_record`.

Reproduction (valid RELEASE_CANDIDATE after Publication Preview r2 APPROVED):

```text
PYTHONPATH=. python3 scripts/survey_profiled_freeze_v2.py \
  --state sources/2026-W36/production-state.json
```

fails with:

```text
Visual Review record fails schemas/visual-review-record-v2.schema.json:
$: 'pdf_path' is a required property
```

Precedent: `sources/2026-W35/execution/defects/w35-profiled-freeze-visual-authority-core-defect-20260915.md`.
W34/W35 closed Freeze via the canonical compatibility path
`survey_publication_v2.build_freeze`, which binds the candidate-bound
pre-preview VISUAL review. W36 uses the same canonical compatibility path.
No shared-Core byte change.

## Defect 2 — Freeze stage validator misclassifies Human approval as checkpoint

`scripts/survey_stage_validation_v2.py::_prior_artifacts` iterates every
non-null `checkpoint_provenance` entry and validates each file against
`schemas/stage-checkpoint-v2.schema.json`.

After canonical Human Publication Preview approval,
`checkpoint_provenance.publication_preview` legitimately references the
Publication Preview approval JSON
(`sources/2026-W36/gates/publication-preview-approval.json`), not a Stage
Checkpoint. The validator misclassifies it and fails:

```text
prior Stage Checkpoint fails schemas/stage-checkpoint-v2.schema.json:
$: 'artifacts' is a required property
```

Precedent: `sources/2026-W35/execution/defects/w35-freeze-prior-checkpoint-provenance-core-defect-20260915.md`
(and W34 `survey_stage_validation_v2 with bounded Freeze/Human-Gate artifact
admission correction`).

## W36 bounded compatibility (edition-local, runtime-only)

- Freeze Record + Release Manifest built only via canonical
  `survey_publication_v2.build_freeze` (exact approved bytes preserved,
  release identity `weekly/2026-W36`).
- Stage validation report generated with the W34/W35 bounded admission
  correction, runtime/in-memory only:
  - preserve and validate all true prior Stage Checkpoints;
  - exclude Human Gate approval provenance from Stage Checkpoint admission;
  - validate the Publication Preview approval through the dedicated
    Human-Gate authority path (`validate_preview_approval`);
  - bind the already candidate-bound pre-preview VISUAL review as
    `visual-review-record` (no post-approval review invented).
- Report + reviews + Stage Checkpoint follow the exact W34/W35 authority shape
  (3 artifacts, 2 deterministic reviews).
- No shared-Core file changed. No approved content regenerated.
