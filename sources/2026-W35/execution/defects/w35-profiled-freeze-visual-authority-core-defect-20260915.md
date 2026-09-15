# W35 Core-defect record — canonical Freeze blocked by visual-authority shape contradiction

Status: `BLOCKED / SHARED_CORE_DEFECT / STOPPED_BEFORE_FREEZE`
Date: `2026-09-15Z`
Edition: `2026-W35` (WEEKLY + WEEKLY_MAGAZINE)
Work branch: `weekly/2026-W35-v2-work`
Safe frontier commit: `2f61adda199ffe9a27c737568bf63a9c3dc28fcc` (canonical Human Publication Preview r1 APPROVED; lifecycle `RELEASE_CANDIDATE`, next `stage:freeze`)

No shared-Core file was modified. No workaround provenance was forged. `main` and `production/survey-core-v2` untouched (both still `774dd39a951c9ac3818e83dfffd4c7666efb0a20` at guard time). No Freeze/Release artifact was written.

## 1. Failing contract and command

Current canonical Freeze procedure (`scripts/survey_profiled_freeze_v2.py`, introduced in `981dc85bb`):

```text
python3 -m scripts.survey_profiled_freeze_v2 --state sources/2026-W35/production-state.json --frozen-at "2026-09-15T14:15:28Z"
```

Result: exit 2 —

```text
Visual Review record fails /home/eariver/git/japanese-generative-ai-survey/schemas/visual-review-record-v2.schema.json: $: 'pdf_path' is a required property
```

Raised by `build_profiled_freeze` → `publication.validate_visual_review(repo_root, publication/v2/visual-review-v2.json, approval_path)` (`scripts/survey_profiled_freeze_v2.py:87`, `scripts/survey_publication_v2.py:319-327`), which enforces the **legacy post-approval** visual schema (`schemas/visual-review-record-v2.schema.json`: top-level `pdf_path`, `publication_preview_approval_path`, `review_tool`, `additionalProperties: false`).

## 2. Edition authority (correct per current production)

`sources/2026-W35/publication/v2/visual-review-v2.json` is the candidate-bound **pre-preview** VISUAL record (`publication-review-record-v2` shape: nested `pdf: {path, sha256, byte_count}`, `review_kind: VISUAL`, checks with `evidence_locations`). It is byte-identical between reviewed production authority `d1d6bdc67` and the starting authority, bound by the Publication Candidate (`candidate_sha256 3195f74c…`), and it carried the edition through `RELEASE_CANDIDATE`. A pre-preview record cannot carry approval binding — the approval did not exist yet.

## 3. Internal Core contradiction (shared defect, not edition data)

Three current-contract components require the pre-preview authority; only the Freeze builder demands the legacy shape:

1. `survey_stage_validation_v2.py:541-551` (`validate:freeze`) — validates the candidate visual via `reader.validate_review_record(..., expected_kind="VISUAL")` and requires `freeze.visual_review == candidate.visual_review` ("Freeze record does not bind Candidate pre-preview Visual Review").
2. `survey_publication_v2.py:408-409` (`validate_release_manifest`, used by the default-branch release workflow) — requires `freeze.visual_review == candidate.visual_review`.
3. `survey_publication_v2.py:291-295` (`build_visual_review` docstring) — "New candidates already bind a pre-preview `publication-review-record-v2` VISUAL record. **New production must not require this function before Freeze.**"
4. Against all three, `survey_profiled_freeze_v2.py:79-87` requires the legacy post-approval record at the fixed `publication/v2/visual-review-v2.json` path.

Both closure paths are shut: the single file `publication/v2/visual-review-v2.json` cannot simultaneously satisfy two mutually exclusive schemas (`additionalProperties: false` on both shapes), and manufacturing a legacy post-approval record is exactly what Core forbids (see (3)) and what the W34 precedent explicitly refused ("no post-approval review was invented"; W34 froze via the superseded `publication.build_freeze`, which binds the pre-preview record).

The defect was introduced by `981dc85bb` ("Add Profile-aware freeze and release identity helper"), which migrated release-identity derivation to the Production Profile but regressed visual validation to the legacy schema. The legacy orchestrator handler `validate_freeze` (`scripts/survey_handlers_v2.py:404`) shares the same stale expectation, but it is outside the current agent-first local path.

## 4. Safe frontier preserved

- `2f61adda1` — canonical Human Publication Preview r1 APPROVED (5 helper-generated files only: `gates/publication-preview-approval.json`, `gates/reviews/publication-r1.json`, `gates/reviews/approvals/publication-r1.json`, `review-index.json`, `production-state.json`), pushed as normal fast-forward on `weekly/2026-W35-v2-work`.
- Approved bytes unchanged: PDF `6115f0a7…` (285365 bytes, 8 pages), candidate file `b2f7a3a0…` / `candidate_sha256 3195f74c…`, reviewed commit `d1d6bdc67`.
- Lifecycle `RELEASE_CANDIDATE`; `publication_preview: approved/passed`; `freeze/release: pending`.
- No force push, reset, rebase, squash, history rewrite, fallback branch, content regeneration, or Core edit occurred.

## 5. Required Sol ruling before resume

Reviewed shared-Core repair (outside edition production, per `AGENTS.md`) must reconcile `survey_profiled_freeze_v2.build_profiled_freeze` visual validation with the `validate:freeze` / `validate_release_manifest` pre-preview authority — then this edition must rerun the Freeze step cleanly from the preserved frontier. Suggested direction only (not applied): validate the candidate-bound pre-preview VISUAL record in the Freeze builder instead of the legacy schema. W36 not started.
