# Session — W36 resume r2 via Issue #502 comment citation (suppression-free, STOP at Preview r2 PENDING)

- Issue: `2026-W36` (WEEKLY + WEEKLY_MAGAZINE)
- Branch: `weekly/2026-W36-v2-work`
- Execution contract: `execution/requests/sol-w36-resume-r2-with-issue-comment-citation-no-core-change-20260917.md`
- Human decisions (preserved): Architecture Review r2 `APPROVED`; Publication Preview r1 `REQUEST_CHANGES` (boundary `DRAFT_COMPLETE`)
- Started at Exact Starting SHA: `395fc3335e986c73c7313b9996f62a36489c4fe3` (tree `4662544f037e4eb2b7c35e4f68641b9db42dea99`, parent `9ee8ddc65d6ddd039bcdb2f6607662a5085458f6`)
- Starting Guard: all read-only checks PASS (remote W36 HEAD/tree/parent, main `5acbff85`/`451fd7c6`, Production Line `774dd39a`/`cd46a6f7a`, lifecycle `DRAFT_COMPLETE`, next `stage:reader-publication-validation`, Arch r2 APPROVED, Pub r1 REQUEST_CHANGES/DRAFT_COMPLETE, no r2 decision, Discovery 19 / Screening 19 KEEP / Evidence 13V+6P / Materiality 18+1 / Selection 18+1, repaired TeX present)
- Ended: `RELEASE_CANDIDATE` / `PUBLICATION_PREVIEW` / `HUMAN_GATE_REACHED`, Preview r2 PENDING
- Session status: `COMPLETE_AT_GATE` (no Freeze/Release; no r2 decision generated or inferred)

## Blocker-avoidance repair (no Core change)

- OLD blocked URL (`w36community`): `https://github.com/eariver/japanese-generative-ai-survey/blob/188f5acc0cfd97885e3b110b565a57d31e13ff3c/surveys/weekly/2026-W36/community-observation.md`
- NEW public citation URL: `https://github.com/eariver/japanese-generative-ai-survey/issues/502#issuecomment-5716020666`
- `surveys/weekly/2026-W36/community-observation.md` preserved as audit artifact.
- Removed active `sources/2026-W36/publication/v2/reader-surface-suppressions-v2.json` from publication input (history preserved).
- Core v2 untouched: no `RSG-LEX-INTERNAL-PATHS` change, no suppression plumbing fix, no exception, no validation bypass.

## Preservation (#434/#500/#501/#502)

- No reader-facing HOLD/PARTIAL/revision-ID/promotion language (lexical scan 11/11 PASS).
- GLM-5.3 medium-confidence boundary, no same-week assertion.
- Natural precise technical Japanese preserved.
- NVIDIA/Hugging Face agreed/announced, not closed.
- Community observation context-only, never technical authority.

## Regeneration (canonical tooling only)

1. `references.bib` URL swap + suppression removal.
2. Rebuilt `reader-manuscript-v2.json` via `build_manuscript_manifest` (suppressions=None): manifest SHA `199d450c...`, bib SHA `fe650393...`, `validate_manuscript_manifest` PASS.
3. Rebuilt `reader-surface-semantic-review-v2.json` (updated citation wording, same surface SHA `34328c08...`): validated PASS.
4. Rebuilt `reader-surface-gate-v2.json` via `build_reader_surface_gate` (no suppressions): PASSED, 0/0/0, `validate_reader_surface_gate` PASS.
5. Pushed intermediate commit `52bb2f6c9`; CI `build-weekly-survey` run `35294636439` success (artifact `10527815569`); pinned `main.pdf` 12p/359750B/`07defd59...` + `main.pdf.sha256`; PDF text verified (Issue URL present, no blob, no HOLD/PARTIAL).
6. Rebuilt 3 deterministic checks + `quality-regression-bundle-v2.json` via `build_bundle`: bundle SHA `702cd3b4...`, `validate_bundle` PASS.
7. Built `semantic-editorial-review-v2.json` (11 PASS) + `visual-review-v2.json` (2 PASS) via `build_review_record` on exact bytes: both validated.
8. `validate_stage` DRAFT_COMPLETE→VALIDATED_DRAFT PASS (`reader-publication-stage-validation-r2.json`); `advance-stage` to VALIDATED_DRAFT.
9. `build_candidate` fresh candidate SHA `8103f341...`; `validate_candidate` PASS.
10. `validate_stage` VALIDATED_DRAFT→RELEASE_CANDIDATE PASS (`publication-candidate-stage-validation-r2.json`); `advance-stage` to RELEASE_CANDIDATE (`PUBLICATION_PREVIEW`/`HUMAN_GATE_REACHED`).
11. Committed authority `315d72805`; authored Preview r2 shell/dossier (PENDING, reviewed `315d72805`).

## Commits pushed (normal, non-force)

1. `52bb2f6c9` — bib URL swap + suppression removal + manuscript/semantic/gate rebinding (suppression-free).
2. `315d72805` — r2 publication authority (new PDF, deterministics, bundle, semantic/visual reviews, candidate, validations, checkpoints, RELEASE_CANDIDATE).
3. Preview r2 shell/dossier commit (this run, PENDING).

## Exact stop reason

`HUMAN_GATE_REACHED`: fresh Human Publication Preview r2 PENDING at reviewed authority commit `315d72805`; no Freeze/Release; no Human decision generated.
