# W36 resume — avoid #502 Core false-positive via Issue comment citation; no Core changes

Status: `EXECUTION_AUTHORITY / RESUME_FROM_DRAFT_COMPLETE / NO_CORE_CHANGE / FRESH_PUBLICATION_PREVIEW_R2`

Date: `2026-09-17 JST`

## 1. Mission

Resume W36 from the safe blocked state at `DRAFT_COMPLETE` and complete canonical regeneration through a fresh Human Publication Preview r2, while **not modifying Core v2**.

The previous blocker was caused solely by the reader-facing bibliography URL for `w36community` using a GitHub blob permalink containing the substring `surveys/weekly/...`, which frozen Core rule `RSG-LEX-INTERNAL-PATHS` falsely classified as an internal path. File-based suppression cannot pass through the canonical review/stage-validation path in the pinned Core.

Do not fix or bypass Core. Remove the trigger instead.

The Human-authorized replacement reader-facing citation target is the public Issue #502 comment:

`https://github.com/eariver/japanese-generative-ai-survey/issues/502#issuecomment-5716020666`

That comment contains the accepted 15 public X URLs and the context-only/non-technical-authority boundary, without internal production paths or workflow state.

## 2. Frozen upstream authority

Blocked W36 state reviewed immediately before this request:

- branch: `weekly/2026-W36-v2-work`
- blocked HEAD: `9ee8ddc65d6ddd039bcdb2f6607662a5085458f6`
- blocked tree: `214fe962aa7302d447c72acc84a7822ca14b8c8e`
- lifecycle: `DRAFT_COMPLETE`
- next action: `stage:reader-publication-validation`
- Architecture Review r2: `APPROVED`
- Publication Preview r1: `REQUEST_CHANGES`
- regeneration boundary: `DRAFT_COMPLETE`

Reviewed `main` remains:

- HEAD `5acbff8528890ed9fc324c0227e6c4e43067c438`
- tree `451fd7c6c6a9fcda59daa81fe484c62291e7d018`

Pinned Production Line remains:

- branch `production/survey-core-v2`
- HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

The current Muse starting commit will be the commit that adds this execution request; the invoking prompt must provide its exact SHA/tree and parent.

## 3. Mandatory starting guards

Before any write, verify read-only:

1. remote W36 HEAD/tree exactly equal the invoking prompt values;
2. parent of the invoking starting SHA equals `9ee8ddc65d6ddd039bcdb2f6607662a5085458f6`;
3. `main` HEAD/tree equal the fixed values above;
4. `production/survey-core-v2` HEAD/tree equal the fixed values above;
5. current W36 lifecycle is still `DRAFT_COMPLETE` with `stage:reader-publication-validation`;
6. Architecture Review r2 remains approved;
7. Publication Preview r1 remains `REQUEST_CHANGES` with boundary `DRAFT_COMPLETE`;
8. no newer Human Publication Preview decision exists;
9. accepted upstream research authority remains unchanged: Discovery 19, Screening 19 KEEP / 0 DROP, Evidence 13 VERIFIED / 6 PARTIAL, Materiality 18 MATERIAL / 1 CONTEXT, Selection 18 SELECTED / 1 HOLD;
10. repaired TeX/source state from the blocked run remains present.

Any mismatch: perform no repository/GitHub write and STOP with expected vs actual.

## 4. Exact blocker-avoidance repair

Replace only the reader-facing `w36community` bibliography URL:

OLD blocked URL:

`https://github.com/eariver/japanese-generative-ai-survey/blob/188f5acc0cfd97885e3b110b565a57d31e13ff3c/surveys/weekly/2026-W36/community-observation.md`

NEW public citation URL:

`https://github.com/eariver/japanese-generative-ai-survey/issues/502#issuecomment-5716020666`

The new comment is the publication-facing citation target for W36 community observation.

Preserve the repository-local `surveys/weekly/2026-W36/community-observation.md` as audit/supporting material. Do not delete it merely because the bibliography now points to Issue #502.

Do not modify the 15 accepted X URLs or their context-only boundary.

## 5. Suppression cleanup

The prior edition-local suppression existed only to work around the blocked blob permalink.

For the resumed canonical run:

- do **not** use any suppression to pass `RSG-LEX-INTERNAL-PATHS`;
- remove the active `sources/2026-W36/publication/v2/reader-surface-suppressions-v2.json` from the current publication input if canonical tooling auto-loads it or otherwise treats it as active state;
- preserve the historical blocker/defect record and prior commits; do not rewrite history;
- regenerated `reader-surface-gate-v2.json` must pass with **zero unresolved blocking findings and zero suppressions required for the Issue-comment citation**.

If some unrelated legitimate finding appears, handle it honestly edition-locally if allowed; do not suppress merely to force PASS.

## 6. Preserve completed r1 repair

Do not undo the already-completed fixes for #434, #500, #501, #502.

Specifically preserve:

- no reader-facing `HOLD`, `PARTIAL`, raw revision IDs, promotion/demotion language, or equivalent internal workflow semantics;
- GLM-5.3 remains a medium-confidence W36 boundary item, not a definite same-week event;
- natural and technically precise Japanese terminology from the full reader-facing language pass;
- NVIDIA/Hugging Face remains agreed/announced, not closed;
- the community record remains context-only and non-authoritative for technical facts.

Do not rerun research and do not alter accepted Evidence/Selection/Architecture/Draft authority.

## 7. Regeneration scope

The allowed regeneration boundary remains `DRAFT_COMPLETE`.

After changing the bibliography citation target:

1. rebuild/rebind the reader manuscript as canonical tooling requires;
2. rerun deterministic checks and quality bundle;
3. rebuild reader-surface input;
4. rerun lexical + semantic reader-surface gate **without suppression**;
5. regenerate semantic/editorial review through the canonical binder;
6. rebuild the exact PDF through the normal CI/publication path;
7. run exact-PDF visual review;
8. validate `DRAFT_COMPLETE -> VALIDATED_DRAFT` canonically;
9. advance canonically to `VALIDATED_DRAFT`;
10. build a fresh publication candidate binding the new source/PDF/reviews;
11. validate and advance canonically to `RELEASE_CANDIDATE`;
12. create fresh Human Publication Preview r2 shell/dossier with decision `PENDING`;
13. STOP.

Do not reuse old candidate/PDF hashes after the bibliography change.

## 8. Core freeze — mandatory

No changes are authorized under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

Do not modify `main`.
Do not modify `production/survey-core-v2`.
Do not fix suppression plumbing.
Do not change `RSG-LEX-INTERNAL-PATHS`.
Do not add a Core exception for Issue comments.
Do not bypass canonical stage validation.
Do not hand-assemble PASS records around a failing canonical validator.

If the Issue-comment URL still fails frozen Core for another reason, record the exact new blocker and STOP. Do not repair Core.

## 9. Git discipline

Use only existing branch `weekly/2026-W36-v2-work`.

No new/fallback/repair/review branch.
No force push.
No reset/rebase/squash/history rewrite.
Normal commits and non-force push only.
Re-read remote HEAD before each write boundary; if moved unexpectedly, STOP.

## 10. Required final state

Success requires:

- lifecycle `RELEASE_CANDIDATE`;
- next action `PUBLICATION_PREVIEW`;
- terminal reason `HUMAN_GATE_REACHED`;
- Publication Preview r2 exists and is `PENDING`;
- Publication Preview r1 remains auditable as `REQUEST_CHANGES`;
- Architecture r2 remains `APPROVED`;
- no Freeze/Release;
- shared-Core changed paths = 0;
- `main` and Production Line unchanged;
- reader-surface gate passes without the prior path suppression;
- fresh PDF/candidate identity reported.

STOP at fresh Human Publication Preview r2.

## 11. Final report

Report:

- starting and ending W36 HEAD/tree;
- main and Production Line guard results;
- old blocked blob permalink and new Issue-comment permalink;
- confirmation that suppression is no longer required;
- #434/#500/#501/#502 artifact-repair preservation results;
- new PDF SHA-256 / bytes / pages;
- new candidate SHA-256;
- lexical/semantic/visual validation results;
- changed paths, explicitly proving zero shared-Core changes;
- lifecycle / next action / terminal reason;
- Publication Preview r2 decision status (`PENDING`);
- exact stop reason.
