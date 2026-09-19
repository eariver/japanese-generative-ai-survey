# W38 Core-defect record — Freeze closure bounded compatibility (no Core change)

Status: `SHARED_CORE_DEFECT / EDITION_LOCAL_COMPATIBILITY / NO_CORE_CHANGE`
Date: `2026-09-19 JST`
Edition: `2026-W38`
Work branch: `weekly/2026-W38-v2-work`

## Defect 1 — profiled Freeze visual authority expects legacy record

`scripts/survey_profiled_freeze_v2.py::build_profiled_freeze` validates the
visual authority via `publication.validate_visual_review`, which requires the
legacy post-approval `visual-review-record-v2` schema (`pdf_path` top-level).

W38 (like W34/W35/W36/W37) binds the candidate-bound pre-preview VISUAL review
(`sources/2026-W38/publication/v2/visual-review-v2.json`, reader review-record
schema with `pdf.path`), validated by
`survey_reader_publication_v2.validate_review_record`.

Reproduction (valid RELEASE_CANDIDATE after Publication Preview r2 APPROVED):

```text
PYTHONPATH=. python3 scripts/survey_profiled_freeze_v2.py \
  --state sources/2026-W38/production-state.json
```

fails with:

```text
Visual Review record fails schemas/visual-review-record-v2.schema.json:
$: 'pdf_path' is a required property
```

Precedent: `sources/2026-W37/execution/defects/w37-freeze-core-defects-20260919.md`.
W34/W35/W36/W37 closed Freeze via the canonical compatibility path
`survey_publication_v2.build_freeze`, which binds the candidate-bound
pre-preview VISUAL review. W38 uses the same canonical compatibility path.
No shared-Core byte change.

## Defect 2 — Freeze stage validator misclassifies Human approval as checkpoint

`scripts/survey_stage_validation_v2.py::_prior_artifacts` iterates every
non-null `checkpoint_provenance` entry and validates each file against
`schemas/stage-checkpoint-v2.schema.json`.

After canonical Human Publication Preview r2 approval,
`checkpoint_provenance.publication_preview` legitimately references the
Publication Preview approval JSON
(`sources/2026-W38/gates/publication-preview-approval.json`), not a Stage
Checkpoint. The validator misclassifies it and fails:

```text
prior Stage Checkpoint fails schemas/stage-checkpoint-v2.schema.json:
$: 'artifacts' is a required property
```

Reproduced unpatched in this run before applying the bounded correction.
Precedent: `sources/2026-W37/execution/defects/w37-freeze-core-defects-20260919.md`
(and W35/W36 bounded admission notes).

## W38 bounded compatibility (edition-local, runtime-only)

- Freeze Record + Release Manifest built only via canonical
  `survey_publication_v2.build_freeze` (exact approved bytes preserved,
  release identity `weekly/2026-W38`).
- Stage validation report generated with the W34/W35/W36/W37 bounded admission
  correction, runtime/in-memory only:
  - preserve and validate all true prior Stage Checkpoints;
  - exclude Human Gate approval provenance from Stage Checkpoint admission;
  - validate the Publication Preview approval through the dedicated
    Human-Gate authority path (`validate_preview_approval`);
  - additionally admit the true prior VALIDATED_DRAFT -> RELEASE_CANDIDATE
    checkpoint record's `publication-candidate` artifact (canonical path
    `sources/2026-W38/orchestration/v2/checkpoints/VALIDATED_DRAFT.json`,
    unreferenced in `checkpoint_provenance` only because that stage declares
    `checkpoints: []`; file bytes verified against the checkpoint row);
  - bind the already candidate-bound pre-preview VISUAL review as
    `visual-review-record` (no post-approval review invented).
- Report + reviews + Stage Checkpoint follow the exact W34/W35/W36/W37 authority shape
  (3 artifacts, 2 deterministic reviews).
- No shared-Core file changed. No approved content regenerated.

Approved bytes preserved:

- PDF SHA-256 `3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`
- bytes `347330`, pages `11`
- Candidate internal `8aeb4dc4f959096708186ee338e11f518dd5a2f8c31f7a7757ec9f0278bcbe3f`
  (candidate file `f3fadf14e76ee884a798e1e0e9e17fad3e69a1ea8d81636e20bff2b1f58d7ca0`)
- reviewed repository commit `a55ac5b929221bd133d8a4b819bf960d2104d6c7`
- Human Publication Preview r2 approval `d77231121a49b356f953989fcdd5199a5f0b34c7ec09d220ae96a01d85d87558`
