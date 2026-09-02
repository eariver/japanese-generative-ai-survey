# 2026-W33 reader layout polish — Luna handoff r1

## Purpose

Perform one bounded edition-local layout repair on the already validated W33
reader/publication candidate, rebuild the exact PDF through the canonical Weekly
GitHub Actions workflow, regenerate all hash-bound validation/review artifacts,
and stop for Sol review while Production State remains `DRAFT_COMPLETE`.

Normal completion status:

`VALIDATED_DRAFT_LAYOUT_POLISH_READY_FOR_SOL_REVIEW`

## Repository authority

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W33-v2-work`

The caller supplies an Exact Starting SHA. Before any write, verify remote branch
HEAD exactly equals that SHA. On mismatch, perform no writes and stop with the
actual remote HEAD.

Reviewed-main Core authority remains:

`6267de3f6876f491950139757bfdf1085fc07bdc`

Shared Core/config/schema/workflows are read-only.

## Mandatory current state

Verify before editing:

- lifecycle `DRAFT_COMPLETE`;
- draft checkpoint `passed`;
- validation checkpoint `pending`;
- Publication Preview `pending`;
- Architecture Review `approved`;
- Exception Gate inactive;
- seven Draft Package/Result pairs and Synthesis authority unchanged;
- current candidate artifacts from `sources/2026-W33/publication/v2/**` exist;
- current exact PDF SHA-256 is `4f1028c221101cd21cf300a3916c9d4b7cf589b5f672a0f97f61aa6afc992243` before repair.

Read the Sol review before editing:

`sources/2026-W33/execution/reviews/w33-validated-draft-candidate-sol-review-20260831-r1.md`

## Sole repair finding

On the exact 11-page candidate PDF, page 8 is the final page of the two-column
reader section. Its entire right column is blank while the left column contains
the tail of `Week in Review`. This is a page-balance defect, not missing content.

Repair this layout so the final two-column reader page is visually balanced.

The preferred outcome is that already-authored Week in Review material is
balanced across the final two columns rather than leaving a wholly empty right
column. Use the smallest W33 edition-local TeX/layout change that works reliably
under the existing canonical Weekly build environment.

Do not modify shared `templates/survey/jgaisurvey.sty` or any shared workflow.

## Semantic freeze

The substantive reader text is frozen by Sol review.

Do not add facts, sources, candidates, claims, examples, comparisons, or new
watchpoints.

Do not change the meaning of:

- the seven chapter narratives;
- evidence attribution or limitations;
- Weekly Community Movement context-only status;
- Week in Review what-changed / why-it-matters / what-to-watch synthesis;
- Source Notes evidence classes;
- bibliography records except deterministic formatting/layout necessities.

If balancing cannot be achieved without substantive prose changes, stop
`NEEDS_SOL_REVIEW` instead of rewriting content.

## Required execution loop

1. Verify Exact Starting SHA and mandatory current state.
2. Apply a minimal W33-only layout repair.
3. Commit/push the source change normally, non-force.
4. Use the existing `.github/workflows/build-weekly-survey.yml` push-triggered
   canonical build for that exact source commit.
5. Require workflow success and final TeX publication-warning gate PASS.
6. Download the selected workflow artifact.
7. Independently recompute `main.pdf` SHA-256 and compare with
   `main.pdf.sha256`.
8. Pin the exact successful CI `main.pdf` bytes and digest file into
   `surveys/weekly/2026-W33/` without mutation.
9. Render and visually inspect **every page** of that exact PDF.
10. Confirm the page-8/right-column defect is resolved and no new visual defect
    was introduced.
11. Regenerate/replace the exact hash-bound candidate artifacts:
    - `sources/2026-W33/publication/v2/reader-manuscript-v2.json`
    - `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json`
    - `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json`
    - `sources/2026-W33/publication/v2/visual-review-v2.json`
    - deterministic result authorities under
      `sources/2026-W33/publication/v2/deterministic/` as required by their exact source/PDF bindings.
12. Run canonical current-Core `DRAFT_COMPLETE` stage-contract validation with
    the repaired exact artifact set and require PASS.
13. Verify Production State bytes remain unchanged.
14. Write one session record:
    `sources/2026-W33/execution/sessions/w33-luna-reader-layout-polish-20260831-r1.md`.
15. Stop `VALIDATED_DRAFT_LAYOUT_POLISH_READY_FOR_SOL_REVIEW`.

## Visual acceptance criteria

At minimum:

- page 8 no longer has a wholly unused right column caused by the section-ending
  page break;
- no clipping/overlap;
- no broken callout/table borders;
- no missing glyphs/black squares;
- no unreadable column balancing;
- headings remain with sensible following content;
- citations remain legible;
- Source Notes/References remain readable;
- page count stays <= 24;
- no artificial padding toward the 18-page soft target.

The final page may naturally contain trailing whitespace after the bibliography;
that is not the defect being repaired.

## Write boundary

Allowed writes are only W33 reader/publication/session files necessary for this
repair and regenerated exact bindings.

Do not modify:

- Production State;
- any checkpoint;
- Draft Package/Result/Synthesis authority;
- Architecture/Selection/Evidence/Discovery authority;
- Human Gate records;
- shared Core/config/schema/workflows/templates.

## Forbidden operations

Do not execute:

- `ADVANCE_STAGE`;
- `DRAFT_COMPLETE -> VALIDATED_DRAFT`;
- Validation Stage Checkpoint creation;
- Publication Candidate creation;
- Publication Preview Human Gate;
- freeze;
- release.

## Stop conditions

Stop `NEEDS_SOL_REVIEW` without further semantic edits if:

- Starting SHA mismatches;
- mandatory State/authority drift exists;
- the layout repair would require changing substantive prose;
- canonical CI build cannot pass;
- exact PDF identity cannot be proven;
- page 8 remains unbalanced after reasonable edition-local attempts;
- a new blocking visual defect appears;
- current-Core DRAFT_COMPLETE validation fails.
