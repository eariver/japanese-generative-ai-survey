# W33 Draft advancement / reader-build environment block — Sol review r1

## Decision

`ACCEPT / DRAFT_COMPLETE_TRANSITION_VERIFIED / READER_BUILD_BLOCK_IS_ENVIRONMENT_ONLY / RESUME_VIA_CANONICAL_WEEKLY_CI`

## Reviewed branch authority

- Repository: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W33-v2-work`
- Luna handoff starting SHA: `bbae857b774464052204b1d7569a39742b17427e`
- Luna reported remote ending SHA: `c1a5f7e2dc318c991ccc7040f437052217ea1d7c`
- Compare: ahead 2 / behind 0

## Draft advancement verification

The remote diff contains only the immutable Draft advancement request plus canonical bridge outputs:

- `sources/2026-W33/execution/requests/w33-draft-advance-20260831-r1.json`
- `sources/2026-W33/execution/bridge-runs/w33-draft-advance-20260831-r1/core-stage-contract.json`
- `sources/2026-W33/execution/bridge-runs/w33-draft-advance-20260831-r1/receipt.json`
- `sources/2026-W33/execution/bridge-runs/w33-draft-advance-20260831-r1/reviews.json`
- `sources/2026-W33/orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`
- `sources/2026-W33/production-state.json`

The bridge receipt is `PASS` and records exactly one transition:

`ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE`

The Draft checkpoint binds the exact seven Draft Packages, seven Draft Results, Synthesis Input, and Synthesis Result previously accepted by Sol. It records both:

- `CORE_STAGE_CONTRACT = PASS`
- `SOL_DRAFT_CANDIDATE_SET_SEMANTIC_REVIEW = PASS`

Current Production State is valid:

- lifecycle: `DRAFT_COMPLETE`
- next action: `stage:reader-publication-validation`
- draft checkpoint: `passed`
- validation checkpoint: `pending`
- publication preview: `pending`
- Architecture Review: `approved`
- Exception Gate: `inactive`

No Draft rollback is required.

## Environment-block assessment

Luna reported that its local runtime lacked the TeX components required by the approved Weekly publication stack, including `jlreq.cls`, LuaTeX-ja, biblatex/biber, and Japanese fonts. Consequently no publication PDF or exact-page visual review could be produced locally.

The repository already contains a canonical Weekly PDF build workflow:

`.github/workflows/build-weekly-survey.yml`

That workflow:

- uses `xu-cheng/latex-action@v4`;
- uses TeX Live 2026;
- compiles with LuaLaTeX;
- checks the final log for undefined references/citations, biblatex rerun requests, overfull/underfull boxes, and missing characters;
- records `main.pdf` SHA-256;
- uploads the exact PDF and digest as a workflow artifact.

Therefore the observed block is not a Draft/content failure and does not require shared-Core modification or local ad-hoc TeX installation. The correct recovery is to use the repository's existing Weekly CI build path.

## Recovery policy

Resume from `DRAFT_COMPLETE` without repeating Drafting or Draft advancement.

The next Luna unit should:

1. author the reader-facing W33 TeX source and bibliography from the Sol-accepted Draft authority;
2. commit the source to the existing branch, allowing the existing Weekly PDF workflow to build it;
3. inspect workflow logs and repair source/layout defects within a bounded loop;
4. retrieve one successful workflow artifact and verify its published SHA-256;
5. commit those exact PDF bytes into `surveys/weekly/2026-W33/main.pdf` together with build provenance;
6. perform exact-PDF page-by-page visual review on the committed bytes;
7. create the Reader Manuscript Manifest, Quality Regression Bundle, Semantic/Editorial Review, and Exact-PDF Visual Review;
8. run deterministic `DRAFT_COMPLETE` stage validation against those exact artifacts;
9. stop for Sol review while Production State remains `DRAFT_COMPLETE`.

No `DRAFT_COMPLETE -> VALIDATED_DRAFT` advancement is authorized before Sol reviews the exact reader source/PDF/review authority.

## Notes on CI-triggered rebuilds

A later commit that records the selected PDF may itself trigger another Weekly build because the workflow watches `surveys/weekly/**`. That automatic later run is not permitted to silently replace the selected PDF authority. The selected PDF must remain explicitly tied to the successful source-build workflow run from which its bytes were retrieved, and its repository SHA-256 must equal the artifact digest from that run.

## Stop status

`DRAFT_COMPLETE_READY_FOR_CI_READER_VALIDATION_CANDIDATE`
