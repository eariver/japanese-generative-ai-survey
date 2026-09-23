# TS-001 reissue Core-defect record — Freeze closure bounded compatibility (no Core change)

Status: `SHARED_CORE_DEFECT / EDITION_LOCAL_COMPATIBILITY / NO_CORE_CHANGE`
Date: `2026-09-23`
Edition: `SP-efficient-llm-2026` (Thematic LONGFORM_SPECIAL, divergent public slug)
Work branch: `special/efficient-llm-2026-work`
Approval basis: Human Publication Preview r2 APPROVED (Human Owner, 2026-09-23T20:45:00+09:00),
  reviewed commit `82126c77f00889d98da43279079f034b52f6848b`,
  exact PDF `8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1`
  (850785 bytes, 66 pages), candidate file `adf22516...`, internal `6b9fd905...`.

## Defect 1 — CV2-DM-001 recurrence (profiled Freeze visual authority mismatch)

`scripts/survey_profiled_freeze_v2.py::build_profiled_freeze` validates the
visual authority via `publication.validate_visual_review`, which requires the
legacy post-approval `visual-review-record-v2` schema (`pdf_path` top-level).

TS-001 binds the candidate-bound pre-preview VISUAL review
(`sources/SP-efficient-llm-2026/publication/v2/visual-review-v2.json`, reader
review-record schema with `pdf.path`, SHA `fae79e67...`), validated by
`survey_reader_publication_v2.validate_review_record`.

Reproduction (valid RELEASE_CANDIDATE after Publication Preview r2 APPROVED):

```text
PYTHONPATH=. python3 scripts/survey_profiled_freeze_v2.py \
  --state sources/SP-efficient-llm-2026/production-state.json
```

fails with:

```text
Visual Review record fails schemas/visual-review-record-v2.schema.json:
$: 'pdf_path' is a required property
```

Precedent: `sources/2026-W38/execution/defects/w38-freeze-core-defects-20260919.md`
(and W34–W37). No shared-Core byte change. No new CV2-DM ID (recurrence only).

## Defect 2 — CV2-DM-002 recurrence (Human approval misclassified as Stage Checkpoint)

`scripts/survey_stage_validation_v2.py::_prior_artifacts` iterates every
non-null `checkpoint_provenance` entry and validates each file against
`schemas/stage-checkpoint-v2.schema.json`.

After canonical Human Publication Preview r2 approval,
`checkpoint_provenance.publication_preview` legitimately references the
Publication Preview approval JSON
(`sources/SP-efficient-llm-2026/gates/publication-preview-approval.json`,
SHA `15b88fb2...`), not a Stage Checkpoint.

Reproduction (in-memory, read-only):

```text
sv._prior_artifacts(root, cfg, state)
-> prior Stage Checkpoint fails schemas/stage-checkpoint-v2.schema.json:
   $: 'artifacts' is a required property
```

Precedent: W37/W38 bounded admission notes. No shared-Core byte change.
No new CV2-DM ID (recurrence only).

## Defect 3 — CV2-DM-003 recurrence (VALIDATED_DRAFT checkpoint provenance omission)

The real `VALIDATED_DRAFT → RELEASE_CANDIDATE` checkpoint
(`sources/SP-efficient-llm-2026/orchestration/v2/checkpoints/VALIDATED_DRAFT.json`,
carrying the exact r2 `publication-candidate` artifact `adf22516...`) exists on
disk but is not referenced by `checkpoint_provenance` (that stage declares
`checkpoints: []`; `validation` points at `DRAFT_COMPLETE.json`). Frozen
admission therefore loses the `publication-candidate` authority required by
RELEASE_CANDIDATE stage semantics.

Precedent: W38 bounded admission. No shared-Core byte change.
No new CV2-DM ID (recurrence only).

## Defect 4 — CV2-DM-019 NEW (build_freeze release identity ignores profile public slug)

`scripts/survey_publication_v2.py::build_freeze` derives the release identity
via `release_identity(publication_profile, issue_id)`. For TS-001 this yields
`special/SP-efficient-llm-2026` (reference build output, verified this run).

The frozen release workflow
(`.github/workflows/survey-production-v2-release.yml`, authority step) mandates:

```text
tag = manifest['release_identity']
expected_tag = profiled.release_identity(profile)  # survey_root slug
if tag != expected_tag: raise SystemExit('Release Manifest public identity mismatch')
```

i.e. `special/efficient-llm-2026`. A bare-`build_freeze` manifest would
hard-fail the frozen release. SP001 never exposed this (slug `SP001` ==
issue_id `SP001`, convergent). TS-001 is the first divergent-slug
LONGFORM_SPECIAL freeze under Core v2. Retrospective divergent-slug editions
froze under the pre-v2 flow.

This is a genuinely new generic Core defect, allocated `CV2-DM-019`
(per-edition closure review will carry it into
`docs/core-v2-deferred-maintenance-summary.md` on the separate docs-only
branch). Core left unrepaired per freeze policy.

## TS-001 bounded compatibility (edition-local, runtime-only)

Implemented in:
`sources/SP-efficient-llm-2026/execution/ts001-freeze-compat-20260923.py`
(edition-local helper; shared Core untouched):

- Reference build via canonical `survey_publication_v2.build_freeze` into a
  repo-local scratch dir (same `frozen_at`) to prove Freeze Record equivalence.
  Reference identity observed: `special/SP-efficient-llm-2026` (stale, CV2-DM-019).
- Canonical `freeze-record-v2.json` written byte-identical to the reference
  (SHA `142846f3b6580447e7ccb0c5c9b34ffc953d3cdff58cba453ed7b871630c35bd`).
- Canonical `release-manifest-v2.json` byte-identical to the reference EXCEPT:
  `release_identity` = `special/efficient-llm-2026` (profile-derived, exactly
  the value the frozen release workflow enforces) and `freeze_record_path`
  rebound from the scratch path to the canonical Freeze path (same SHA).
  Re-validated via `publication.validate_release_manifest`
  (SHA `302926da3fa119d7c5112625f444beb781958757516a7333fb9462a0c48e0748`).
- Profile/Bundle/identity parity checks mirroring the profiled helper, binding
  the candidate-bound pre-preview VISUAL review via the reader path (as the
  frozen RELEASE_CANDIDATE stage semantics already do).
- Stage validation report with the W34–W38 bounded admission correction,
  runtime/in-memory only:
  - preserve and validate all true prior Stage Checkpoints (with active
    publication-revalidation superseding for `DRAFT_COMPLETE.json`);
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
  (`RELEASE_CANDIDATE → FROZEN`, checkpoint `8cf74c5a...`).

Approved bytes preserved (verified before and after):

- PDF SHA-256 `8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1`
- bytes `850785`, pages `66`
- Candidate file `adf22516235c5a5db2a89f9a3facd6d5af559eac0ad564d373fd1b1a7a5e9638`,
  internal `6b9fd9059fc068674e63ec1f7e987fa1c2a9e7f4e008f96033909b463bcb62c4`
- Source `87bcb707e13cfde7e3d589271415b66e42385d4c7359f3bb492e9adf2d09fabe`
- reviewed repository commit `82126c77f00889d98da43279079f034b52f6848b`
- Human Publication Preview r2 approval `15b88fb22d96e146cb8b2f38e0dd38d0f61645f673e9f84aa99909d4881654e5`
