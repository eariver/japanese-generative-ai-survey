# W35 temporary compatibility Freeze/Release execution request

Status: `EXECUTION_AUTHORITY / HUMAN_PREVIEW_APPROVED / TEMP_COMPAT_CLOSURE / NO_CORE_MUTATION`
Date: `2026-09-15 JST`
Edition: `2026-W35`
Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W35-v2-work`

## 1. Purpose

Complete W35 without modifying shared Core while a separately tracked Core defect remains open.

The current profile-aware Freeze helper is blocked by a shared-Core visual-authority contract contradiction. The defect is real, but the shared Core must remain frozen because another J-GAS refactor is analysing the W34-era Core baseline.

This request therefore authorizes a one-edition compatibility closure using the still-present canonical `scripts.survey_publication_v2.build_freeze()` primitive. That function is not a hand-written artifact workaround: it validates the exact Human-approved Publication Candidate and its already-bound pre-preview VISUAL authority and emits the same canonical Freeze/Release Manifest schemas expected by the current stage validator and release validator.

Do not modify any shared-Core source, schema, config, workflow, or test file.

## 2. Starting guard

Before any write, read-only verify all of the following:

- remote `weekly/2026-W35-v2-work` HEAD == Exact Starting SHA supplied by Sol invocation
- remote branch tree == Expected Starting Tree supplied by Sol invocation
- starting parent chain includes approved-preview frontier `2f61adda199ffe9a27c737568bf63a9c3dc28fcc`
- `main` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- W35 lifecycle == `RELEASE_CANDIDATE`
- `human_gates.architecture_review == approved`
- `human_gates.publication_preview == approved`
- `next_action == stage:freeze`
- Freeze/release artifacts do not yet exist
- public release/tag identity `weekly/2026-W35` does not yet exist
- approved PDF path `surveys/weekly/2026-W35/main.pdf`
- approved PDF SHA-256 == `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`
- approved PDF byte count == `285365`
- approved PDF page count == `8`
- Publication Candidate remains exact approved authority: candidate semantic hash `3195f74c89a3c8e163f0f29cc0123132ecedd287f84c1467d9110d40167e2e8d`

If any mismatch exists: zero further writes; report expected/actual and STOP.

## 3. Core defect boundary

Read and preserve:

`sources/2026-W35/execution/defects/w35-profiled-freeze-visual-authority-core-defect-20260915.md`

The defect is tracked separately as shared-Core maintenance debt. This execution MUST NOT repair it, cherry-pick a fix, modify Production Line, or change main before W35 closure.

Forbidden:

- editing `scripts/`, `schemas/`, `config/`, `.github/` or shared tests
- creating a Core fix/repair/fallback branch
- synthesizing a legacy post-approval Visual Review
- replacing or rewriting `publication/v2/visual-review-v2.json`
- changing Candidate, PDF, TeX, Architecture, Selection, Evidence, or Human approval bytes
- force push, reset, rebase, squash, history rewrite

## 4. Authorized temporary compatibility Freeze

Use the existing canonical function from the frozen Core baseline:

`scripts.survey_publication_v2.build_freeze()`

Its current contract explicitly says:

`Freeze the exact Human-approved candidate and its already-bound visual QA.`

It validates the Candidate-bound pre-preview `publication-review-record-v2` VISUAL authority and emits canonical `freeze-record-v2.json` and `release-manifest-v2.json`.

For W35, legacy `release_identity(publication_profile, issue_id)` and profile-aware identity are equivalent because:

- publication profile = `WEEKLY_MAGAZINE`
- issue id = `2026-W35`
- profile `paths.survey_root` basename = `2026-W35`

Both resolve to exactly `weekly/2026-W35`.

Invoke `build_freeze()` directly without modifying repository Core code. A one-shot Python invocation importing the existing function is permitted. Do not create a replacement helper under `scripts/`.

Exact inputs:

- candidate: `sources/2026-W35/publication/v2/publication-candidate-v2.json`
- approval: `sources/2026-W35/gates/publication-preview-approval.json`
- freeze output: `sources/2026-W35/publication/v2/freeze-record-v2.json`
- manifest output: `sources/2026-W35/publication/v2/release-manifest-v2.json`

Use a real current UTC timestamp for `frozen_at`.

Immediately validate the generated Release Manifest with the existing `publication.validate_release_manifest()`.

## 5. Canonical Freeze stage validation

After compatibility artifact generation, run the existing current stage validation for `RELEASE_CANDIDATE -> FROZEN` using the generated canonical artifacts.

The validation must demonstrate:

- Freeze binds exact Candidate file bytes
- Freeze binds exact Publication Preview approval
- Freeze binds Candidate pre-preview VISUAL path + SHA
- Candidate/PDF/Visual/approval/manifest exact PDF SHA all equal `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`
- Release Manifest identity == `weekly/2026-W35`

Advance canonical Production State to `FROZEN` only if the current stage validator PASSes.

Commit only edition-local Freeze/state/checkpoint/execution evidence and other artifacts normally required by the current contract. Push normally/non-force and remote read-back.

## 6. Main integration topology

W35 carries no Production-Line-only Core change: starting `main` and `production/survey-core-v2` are identical at `774dd39a951c9ac3818e83dfffd4c7666efb0a20`.

Therefore after successful W35 Freeze, follow the same canonical publication topology used by W34:

1. integrate the exact frozen W35 authority to `main` by the repository's normal reviewed merge mechanism;
2. no squash/rebase/content regeneration;
3. preserve exact frozen PDF/Candidate/Freeze/Manifest bytes;
4. obtain the actual main merge commit SHA by read-back;
5. use that exact merge SHA as release target authority.

If main changed unexpectedly from the guarded value before integration, STOP rather than guessing or rebasing.

Do not update `production/survey-core-v2` as part of W35 closure. This is intentionally preserving the refactor baseline and deferring the Core defect.

## 7. Public Release

After frozen authority is correctly integrated to main, run the current canonical release mechanism for release identity:

`weekly/2026-W35`

The released asset must be the exact approved/frozen PDF:

- SHA-256 `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`
- 285365 bytes
- 8 pages

Perform exact-byte release reconciliation against the public release/downloaded asset and record the current required release/merge verification authorities.

Advance `FROZEN -> RELEASED` only after all current release checkpoint contracts pass.

## 8. Terminal state

Normal completion requires all of:

- lifecycle `RELEASED`
- terminal_reason `COMPLETE`
- Publication Preview r1 approval preserved
- Freeze checkpoint passed
- Release checkpoint passed
- release identity `weekly/2026-W35`
- release target read back and recorded
- exact approved PDF SHA/bytes/pages preserved
- no content regeneration after Human approval
- shared Core files unchanged
- `production/survey-core-v2` remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- W36 not started

## 9. Stop conditions

STOP without improvisation if:

- direct canonical `publication.build_freeze()` itself fails on W35 exact authorities;
- current Freeze stage validation rejects the generated artifacts;
- release identity differs from `weekly/2026-W35`;
- main changes unexpectedly before merge;
- current release workflow/checkpoint reveals another shared-Core defect;
- exact approved PDF bytes drift at any point.

A STOP under this section is not authorization to repair Core.

## 10. Final report

Report:

- starting HEAD/tree
- compatibility Freeze invocation/result
- Freeze/Manifest SHA identities
- Freeze stage validation result
- frozen branch SHA/tree
- main merge PR/merge SHA or equivalent canonical integration evidence
- public release/tag identity and release target
- downloaded release asset exact-byte reconciliation
- final W35 branch HEAD/tree
- final `production-state` lifecycle/terminal reason
- final main HEAD
- final Production Line HEAD (must remain frozen baseline)
- changed paths after this request
- explicit confirmation: no shared-Core mutation, no force/history rewrite, no W36 work

Normal final status:

`W35 RELEASED / COMPLETE via temporary canonical compatibility Freeze; shared-Core repair deferred to tracked Issue.`
