# 2026-W33 reader/publication validation candidate via canonical Weekly CI — Luna handoff r1

## Purpose

Resume W33 from the already checkpointed `DRAFT_COMPLETE` state after the prior Luna environment lacked the TeX packages required for local LuaLaTeX publication rendering.

Do **not** repeat Drafting and do **not** repeat the Draft advancement.

Use the repository's existing canonical Weekly PDF workflow as the TeX build environment, then produce a complete reader/publication validation candidate and stop for Sol review before `VALIDATED_DRAFT` advancement.

Normal completion status:

`VALIDATED_DRAFT_CANDIDATE_READY_FOR_SOL_REVIEW`

## Repository authority

Repository:

`eariver/japanese-generative-ai-survey`

Branch:

`weekly/2026-W33-v2-work`

The caller supplies an **Exact Starting SHA**.

Before any write, verify the remote branch HEAD exactly equals that SHA.

If it does not, write nothing and stop with the actual remote HEAD.

Reviewed-main Core authority:

`6267de3f6876f491950139757bfdf1085fc07bdc`

Shared Core/config/schema/workflow files are read-only.

## Mandatory starting state

Verify `sources/2026-W33/production-state.json` before any write.

Required:

- lifecycle: `DRAFT_COMPLETE`
- `next_action = stage:reader-publication-validation`
- Architecture Review: `approved`
- draft checkpoint: `passed`
- validation checkpoint: `pending`
- publication preview: `pending`
- Exception Gate: `inactive`

Verify the canonical Draft checkpoint:

`sources/2026-W33/orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`

It must bind the exact Sol-accepted:

- 7 Draft Packages
- 7 Draft Results
- Synthesis Input
- Synthesis Result

and contain:

- `CORE_STAGE_CONTRACT = PASS`
- `SOL_DRAFT_CANDIDATE_SET_SEMANTIC_REVIEW = PASS`

If this authority has drifted, stop `NEEDS_SOL_REVIEW`.

## Mandatory read order

Read in this order:

1. reviewed-main `config/survey-production-v2.json`
2. reviewed-main `scripts/survey_stage_validation_v2.py`
3. reviewed-main `scripts/survey_reader_publication_v2.py`
4. reviewed-main `scripts/survey_reader_fidelity_v2.py`
5. reviewed-main `scripts/survey_quality_v2.py`
6. reviewed-main `scripts/survey_publication_v2.py`
7. reviewed-main `schemas/reader-manuscript-v2.schema.json`
8. reviewed-main `schemas/publication-review-record-v2.schema.json`
9. reviewed-main `schemas/quality-regression-bundle-v2.schema.json`
10. reviewed-main `config/publication-review-v2.json`
11. reviewed-main `.github/workflows/build-weekly-survey.yml`
12. `sources/2026-W33/production-profile.json`
13. `sources/2026-W33/production-state.json`
14. `sources/2026-W33/orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`
15. `sources/2026-W33/gates/architecture-approval.json`
16. `sources/2026-W33/architecture-v2.json`
17. all 7 accepted Draft Results under `sources/2026-W33/drafting/v2/luna-r1/results/`
18. accepted Synthesis Result `sources/2026-W33/drafting/v2/luna-r1/synthesis-result.json`
19. `sources/2026-W33/execution/reviews/w33-draft-candidate-set-sol-review-20260831-r1.md`
20. `sources/2026-W33/execution/reviews/w33-draft-advance-environment-block-sol-review-20260831-r1.md`
21. W32 Weekly publication files **for structure/layout precedent only**, never as W33 factual authority

## Factual authority boundary

Reader-facing W33 substantive facts must come from the seven Sol-accepted Draft Results.

Draft Packages/Evidence may be consulted only to preserve:

- citation/source metadata;
- attribution identity;
- limitations;
- exact source mapping needed by bibliography and review authority.

Do not add a substantive fact that does not exist in the accepted Draft Results.

No Web, Google Drive, Raw source, fresh Evidence, or new candidate research is allowed.

Do not reintroduce rejected/HOLD carry-over as W33 developments.

## Phase A — author W33 reader source

Create the canonical survey root:

`surveys/weekly/2026-W33/`

Author a magazine-quality Weekly source using the established repository Weekly publication stack.

W32 may be used only for structural conventions such as:

- `jlreq`
- `jgaisurvey`
- `.latexmkrc`
- `main.tex`
- `sections/`
- `references.bib`
- bibliography/source-note layout

Do not copy W32 factual prose.

The W33 reader structure must visibly preserve the approved Architecture's seven-package editorial logic:

1. Frontier Models & Access
2. Cyber Access & Governance
3. Serving & Runtime
4. Inference Systems Deep Dive
5. Agent Reliability
6. Multimodal & Media
7. Week in Review / WEEKLY_SYNTHESIS

The final Week in Review must remain an independent reader-facing chapter and must answer:

- what changed;
- why the changes matter together;
- what to watch next.

It must not merely repeat the preceding chapter summaries.

Include a reader-facing Weekly Community Movement/context block as required by the Weekly reader contract. X/community material is context only and must not be used as technical authority.

Preserve all meaningful Draft limitations and attribution boundaries.

Page plan:

- target: 18 pages
- hard maximum: 24 pages

Do not pad merely to hit 18 pages.

## Phase B — source candidate commit and canonical CI build

The prior Luna environment is **not** an approved TeX build environment for this task.

Do not solve this by modifying shared Core/workflows or by ad-hoc repository-level dependency changes.

Use existing:

`.github/workflows/build-weekly-survey.yml`

That workflow is the canonical remote build environment for this recovery path.

After the initial W33 TeX/bibliography source is complete and internally checked:

1. recheck remote branch HEAD for drift;
2. make a normal non-force commit containing the W33 reader source candidate;
3. push to the existing branch;
4. identify the `Build weekly survey PDF` workflow run triggered for that exact source commit;
5. require the workflow to complete successfully.

The workflow's final log gate must PASS. It rejects at least:

- undefined references;
- undefined citations;
- biblatex rerun requirements;
- Overfull hbox;
- Underfull hbox;
- Missing character.

If the build fails due reader source/layout defects, inspect the exact workflow log, repair only W33 reader source/bibliography/layout, commit normally, and allow a new run.

A bounded repair loop of up to 3 source/layout correction iterations is allowed inside this Luna work unit.

If after 3 repair iterations the workflow is still not clean, or if failure is infrastructure/environmental and not repairable within W33 reader source, stop `NEEDS_SOL_REVIEW` without advancing State.

Do not modify `.github/workflows/build-weekly-survey.yml`.

## Phase C — select and freeze one exact CI PDF

For the successful source-build workflow run selected as authority:

1. record the exact workflow run ID;
2. record the source commit SHA built by that run;
3. retrieve its uploaded artifact;
4. verify artifact `main.pdf.sha256` against downloaded `main.pdf` bytes;
5. verify PDF is non-empty and page count is between 1 and 24;
6. copy the **exact artifact bytes**, without re-rendering or mutation, to:

`surveys/weekly/2026-W33/main.pdf`

Also retain the corresponding digest file if repository convention permits/uses it.

Commit the exact PDF bytes normally to the same branch.

Important: a commit that stores `main.pdf` may itself trigger another Weekly build because the workflow watches `surveys/weekly/**`. Such a later automatic run is not allowed to silently replace the selected PDF authority. The selected PDF remains the exact bytes from the explicitly recorded successful source-build run, and the committed PDF SHA-256 must equal that run's artifact digest.

## Phase D — exact-PDF visual review and repair loop

Perform a real page-by-page visual review of the **exact committed PDF bytes**, not a local approximation.

Inspect every page for at least:

- clipping/cropping;
- unreadable text;
- broken Japanese glyphs;
- missing glyphs;
- overflow;
- awkward whitespace;
- column imbalance;
- orphan/widow-like layout defects where materially distracting;
- broken tables/lists;
- headings separated unnaturally from content;
- bibliography/source-note breakage;
- cover/frontmatter defects;
- page-count compliance;
- overall Weekly magazine readability.

If visual defects require source changes:

1. edit W33 TeX/source only;
2. commit normally;
3. obtain a new clean CI build from the new source commit;
4. retrieve the new exact PDF artifact;
5. replace the repository PDF with those exact bytes;
6. repeat the full page-by-page review.

The same overall maximum of 3 W33 source/layout repair iterations applies unless a lower-level deterministic script itself requires a simple correction that does not consume an editorial iteration.

Do not claim `EXACT_PDF_VISUAL_REVIEW` PASS without inspecting all pages of the final exact PDF.

## Phase E — canonical reader/publication validation candidate

Once reader source and exact PDF are stable, use reviewed-main canonical helpers to create and validate the required `DRAFT_COMPLETE` current-stage artifact set.

The exact Core stage contract requires:

- `reader-manuscript`
- `validated-source`
- `publication-pdf`
- `quality-regression-bundle`
- `semantic-review`
- `visual-review`

Use canonical helpers/schemas to determine and create repository-local paths. Do not invent alternate semantic formats when the Core provides a builder/schema.

### Reader Manuscript

Create a canonical Reader Manuscript Manifest that binds exact repository bytes for:

- Production Profile;
- approved Architecture;
- Architecture Approval;
- primary reader source (`surveys/weekly/2026-W33/main.tex`);
- relevant supporting source files;
- complete Architecture must-cover coverage;
- required reader requirements.

Weekly reader requirements must include the canonical requirements expected by reviewed Core, including:

- `FINAL_SYNTHESIS`
- `WEEKLY_COMMUNITY_MOVEMENT`

Every claimed LONGFORM/reader coverage location must resolve to actual non-empty reader blocks.

### Quality Regression Bundle

Generate the canonical quality-regression bundle from exact source/PDF authority and run all deterministic checks required by current Core/Profile.

### Semantic / Editorial Review

Create a canonical review record against the exact reader source/manuscript authority.

At minimum, satisfy all required semantic checks for current WEEKLY/WEEKLY_MAGAZINE contract, including the publication-review contract's:

- `PUBLICATION_BOUNDARY`
- `ARCHITECTURE_CONTENT_FIDELITY`
- `FINAL_SYNTHESIS_QUALITY`
- `WEEKLY_COMMUNITY_MOVEMENT`

and all generic/Profile quality checks expected by current Core, including source-specific fail-closed behavior, bibliography metadata, post-transform semantic revalidation, W33 issue relevance, late-breaking single-home semantics, watchlist reader semantics, and carry-over disposition where applicable.

The semantic review must verify that the reader-facing transformation did not introduce facts beyond the accepted Draft Results.

### Exact-PDF Visual Review

Create a canonical visual review record against the exact committed PDF bytes.

It must satisfy all required visual checks, including:

- `EXACT_PDF_VISUAL_REVIEW`
- Weekly rendered-page review requirements from the active quality contract.

Review evidence must identify that all final PDF pages were inspected.

## Phase F — deterministic candidate validation

Run the current reviewed Core's deterministic `DRAFT_COMPLETE` stage contract locally against the exact candidate artifacts.

Require PASS.

If deterministic validation finds W33-local reader/source/review metadata defects, repair them within scope and rerun.

Do not weaken or modify Core/schema/workflow to obtain PASS.

## Required stop boundary

Production State must remain:

`DRAFT_COMPLETE`

with:

- draft checkpoint: `passed`
- validation checkpoint: `pending`
- publication preview: `pending`

Do **not**:

- execute `DRAFT_COMPLETE -> VALIDATED_DRAFT`;
- create the Validation Stage Checkpoint;
- create an ADVANCE_STAGE request for validation;
- create Publication Candidate;
- enter Publication Preview Human Gate;
- freeze;
- release.

## Session record

Write one Luna session record documenting at least:

- Starting SHA and exact branch-head guard;
- starting/final State SHA-256 and proof lifecycle stayed `DRAFT_COMPLETE`;
- source candidate commit(s);
- every Weekly PDF workflow run used during the bounded repair loop;
- selected authoritative source commit and workflow run;
- selected artifact ID/name;
- artifact `main.pdf.sha256` and independently recomputed committed PDF SHA-256 equality;
- final page count;
- confirmation all pages were visually inspected;
- final reader manifest / source / PDF / quality bundle / semantic review / visual review paths and SHA-256 values;
- deterministic DRAFT_COMPLETE stage validation result;
- changed-path inventory;
- confirmation no `ADVANCE_STAGE` after DRAFT_COMPLETE and no Publication Candidate.

## Stop conditions

Stop `NEEDS_SOL_REVIEW` without validation advancement if any of the following occurs:

- starting remote HEAD mismatch;
- State is not exact required `DRAFT_COMPLETE` state;
- Draft checkpoint or accepted Draft artifacts drift;
- W33 substantive reader content would require new research/Evidence;
- canonical Weekly workflow itself requires shared-workflow/Core modification;
- no clean Weekly build can be obtained within the bounded source/layout repair loop;
- selected artifact digest does not equal committed PDF bytes;
- PDF page count exceeds 24;
- exact-PDF visual review cannot inspect every page;
- a semantic/visual required check cannot honestly PASS;
- deterministic `DRAFT_COMPLETE` stage contract fails and cannot be repaired edition-locally;
- a change outside the permitted W33 reader/publication/session scope becomes necessary.

Normal successful stop:

`VALIDATED_DRAFT_CANDIDATE_READY_FOR_SOL_REVIEW`
