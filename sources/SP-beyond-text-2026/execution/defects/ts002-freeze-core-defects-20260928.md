# TS-002 Core-defect record — Freeze closure bounded compatibility (no Core change)

Status: `SHARED_CORE_DEFECT RECURRENCE / EDITION_LOCAL_COMPATIBILITY / NO_CORE_CHANGE`
Date: `2026-09-28`
Edition: `SP-beyond-text-2026` (Thematic LONGFORM_SPECIAL, divergent public slug)
Work branch: `special/beyond-text-2026-work`
Approval basis: Human Publication Preview r12 APPROVED (Human Owner, 2026-09-27T16:31:47Z / 2026-09-28 JST),
  reviewed commit `046f1ddebaef2a82777bb0c428b50f57d6904861`,
  candidate-producing commit `f81694363a6d6fc3456c96d77e02ee8360728ef1`,
  exact PDF `4e2250677716fba5cbfe3ea0e57d9f2174e83a93a15a361d8fbae164bf45089d`
  (1106143 bytes, 78 pages), candidate file `4d2c01ab62c690c53897da476d84861fcb4c4c62144910d84bc57462cd55a8c2`, internal `79c3a4fd9a2e9b948920dcd85004f8c22108dfbd2ca7ee268e91a2186140ec9b`.

Precedent: TS-001 Freeze commit `fff682cb4b8071d275b3f72af2c70aa5450c7d5a`
(`sources/SP-efficient-llm-2026/execution/defects/ts001-reissue-freeze-core-defects-20260923.md`
+ `sources/SP-efficient-llm-2026/execution/ts001-freeze-compat-20260923.py`).
No shared-Core byte change. No new CV2-DM ID (all recurrences).

## Defect 1 — CV2-DM-001 recurrence (profiled Freeze visual authority mismatch)

`scripts/survey_profiled_freeze_v2.py::build_profiled_freeze` validates the
visual authority via `publication.validate_visual_review`, which requires the
legacy post-approval `visual-review-record-v2` schema (`pdf_path` top-level).

TS-002 binds the candidate-bound pre-preview VISUAL review
(`sources/SP-beyond-text-2026/publication/v2/visual-review-v2.json`, reader
review-record schema with `pdf.path`), validated by
`survey_reader_publication_v2.validate_review_record`.

Reproduction (valid RELEASE_CANDIDATE after Publication Preview r12 APPROVED):

```text
PYTHONPATH=. python3 scripts/survey_profiled_freeze_v2.py \
  --state sources/SP-beyond-text-2026/production-state.json
```

fails with:

```text
Visual Review record fails schemas/visual-review-record-v2.schema.json:
$: 'pdf_path' is a required property
```

Identical to TS-001. No shared-Core byte change. No new CV2-DM ID.

## Defect 2 — CV2-DM-002 recurrence (Human approval misclassified as Stage Checkpoint)

`scripts/survey_stage_validation_v2.py::_prior_artifacts` iterates every
non-null `checkpoint_provenance` entry and validates each file against
`schemas/stage-checkpoint-v2.schema.json`.

After canonical Human Publication Preview r12 approval,
`checkpoint_provenance.publication_preview` legitimately references the
Publication Preview approval JSON
(`sources/SP-beyond-text-2026/gates/publication-preview-approval.json`,
SHA `5e121516c2d71905e75cacfe47b5e97ef61019dc712377f19fe89d87bd80459e`), not a Stage Checkpoint.

Reproduction (in-memory, read-only): `sv._prior_artifacts(root, cfg, state)`
-> `prior Stage Checkpoint fails schemas/stage-checkpoint-v2.schema.json: $: 'artifacts' is a required property`.

Identical to TS-001. No shared-Core byte change. No new CV2-DM ID.

## Defect 3 — CV2-DM-003 recurrence (VALIDATED_DRAFT checkpoint provenance omission)

The real `VALIDATED_DRAFT → RELEASE_CANDIDATE` checkpoint
(`sources/SP-beyond-text-2026/orchestration/v2/checkpoints/VALIDATED_DRAFT.json`,
carrying the exact r12 `publication-candidate` artifact `4d2c01ab...`) exists on
disk but is not referenced by `checkpoint_provenance` (that stage declares
`checkpoints: []`; `validation` points at `DRAFT_COMPLETE.json`). Frozen
admission therefore loses the `publication-candidate` authority required by
RELEASE_CANDIDATE stage semantics.

Identical to TS-001. No shared-Core byte change. No new CV2-DM ID.

## Defect 4 — CV2-DM-019 recurrence (build_freeze release identity ignores profile public slug)

`scripts/survey_publication_v2.py::build_freeze` derives the release identity
via `release_identity(publication_profile, issue_id)`. For TS-002 this yields
`special/SP-beyond-text-2026` (reference build output, verified this run).

The frozen release workflow
(`.github/workflows/survey-production-v2-release.yml`, authority step) mandates:

```text
tag = manifest['release_identity']
expected_tag = profiled.release_identity(profile)  # survey_root slug
if tag != expected_tag: raise SystemExit('Release Manifest public identity mismatch')
```

i.e. `special/beyond-text-2026`. A bare-`build_freeze` manifest would
hard-fail the frozen release. TS-001 precedent `fff682cb...` already allocated
`CV2-DM-019` for this class. TS-002 recurs identically. No new ID.

## TS-002 bounded compatibility (edition-local, runtime-only)

Implemented in:
`sources/SP-beyond-text-2026/execution/ts002-freeze-compat-20260928.py`
(edition-local helper; shared Core untouched; modeled directly on
`ts001-freeze-compat-20260923.py`):

- Reference build via canonical `survey_publication_v2.build_freeze` into a
  repo-local scratch dir (same `frozen_at`) to prove Freeze Record equivalence.
  Reference identity observed: `special/SP-beyond-text-2026` (stale, CV2-DM-019 recurrence).
- Canonical `freeze-record-v2.json` written byte-identical to the reference.
- Canonical `release-manifest-v2.json` byte-identical to the reference EXCEPT:
  `release_identity` = `special/beyond-text-2026` (profile-derived, exactly
  the value the frozen release workflow enforces) and `freeze_record_path`
  rebound from the scratch path to the canonical Freeze path (same SHA).
  Re-validated via `publication.validate_release_manifest`.
- Profile/Bundle/identity parity checks mirroring the profiled helper, binding
  the candidate-bound pre-preview VISUAL review via the reader path (as the
  frozen RELEASE_CANDIDATE stage semantics already do).
- Stage validation report with the W34–W38 bounded admission correction,
  runtime/in-memory only:
  - preserve and validate all true prior Stage Checkpoints;
  - exclude Human Gate approval provenance from Stage Checkpoint admission;
  - validate the Publication Preview approval through `validate_preview_approval`;
  - admit the exact canonical `VALIDATED_DRAFT.json` (`publication-candidate`
    artifact bytes + binding verified; no synthetic history);
  - replicate the frozen RELEASE_CANDIDATE semantics verbatim
    (candidate/approval/visual/freeze/manifest binding + exact-PDF chain).
- Report + reviews + Stage Checkpoint follow the exact W38 authority shape
  (3 artifacts: `freeze-record`, `release-manifest`, `visual-review-record`;
  2 deterministic reviews: `CORE_STAGE_CONTRACT`, `stage:freeze`).
- Advance via the frozen `survey_agent_control_v2.py advance-stage`
  (`RELEASE_CANDIDATE → FROZEN`).

Approved bytes preserved (verified before and after):

- PDF SHA-256 `4e2250677716fba5cbfe3ea0e57d9f2174e83a93a15a361d8fbae164bf45089d`
- bytes `1106143`, pages `78`
- Candidate file `4d2c01ab62c690c53897da476d84861fcb4c4c62144910d84bc57462cd55a8c2`,
  internal `79c3a4fd9a2e9b948920dcd85004f8c22108dfbd2ca7ee268e91a2186140ec9b`
- Source `d3543075351e14aaf95c2ada8099ec8dd122fb01e879be236a5b6fa162672782`
- reviewed repository commit `046f1ddebaef2a82777bb0c428b50f57d6904861`
- candidate-producing commit `f81694363a6d6fc3456c96d77e02ee8360728ef1`
- Human Publication Preview r12 approval `5e121516c2d71905e75cacfe47b5e97ef61019dc712377f19fe89d87bd80459e`
