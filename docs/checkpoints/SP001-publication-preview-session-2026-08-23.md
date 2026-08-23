# SP001 Publication Preview session — 2026-08-23

## Purpose

This checkpoint records the post-draft continuation of SP001 (`THEMATIC` / `LONGFORM_SPECIAL`) from `DRAFT_COMPLETE` through exact rendered-page validation, Quality Regression Bundle establishment, Publication Candidate construction, and arrival at the `PUBLICATION_PREVIEW` Human Gate.

Earlier discovery / evidence / architecture / drafting work is recorded in the existing SP001 checkpoint files under `docs/checkpoints/`, including `SP001-architecture-review-session-2026-08-23-core-v2-runtime.md` and `SP001-post-architecture-review-2026-08-23.md`.

## Starting authority

At the start of this continuation:

- Production State: `DRAFT_COMPLETE`
- next action: semantic publication validation
- Architecture Review: approved
- Publication Preview: pending
- publication source/PDF had already been assembled once from the approved seven Draft Results and issue-level synthesis

The semantic publication input remained unchanged throughout the typography repair and final rebuild.

## Exact rendered-page review and cover defect

The first exact 11-page publication PDF was exported from GitHub Actions for rendered-page inspection.

Visual review of all pages found no body clipping, overlap, broken glyphs, TOC defect, claim-boundary collision, summary-placement defect, or References defect. One publication-quality issue was found on the cover:

- the English word `Special` in the survey title was rendered as `Spe-` / `cial` across a discretionary hyphenation break.

This was treated as a generic survey-cover typography defect rather than a SP001 prose defect.

### Generic style repair

A minimal template repair was made to prevent discretionary word hyphenation inside the survey cover title group only.

- PR #385: `Survey style: prevent cover title word breaks`
- repair merged to `main` as commit `1419dacba9ee15ac48bb6d3bf92b99add48625fb`
- Core / pipeline contract checks passed
- Special post-draft contract passed
- real weekly LuaLaTeX build and TeX-log validation passed
- the reviewed repair was integrated into `special/SP001-v2-work` through PR #387

No SP001 Draft, Evidence, synthesis, or semantic publication prose changed in this repair.

## Exact semantic publication rebuild

SP001 was rebuilt from the byte-identical semantic publication input previously used for the first semantic-publication run.

- rebuild PR: #389 `SP001: regenerate preview after cover typography repair`
- semantic publication runner: `scripts/run_semantic_publication_v2_interactive.py`
- all seven established Draft Results and Profile Synthesis were revalidated before source rendering
- LuaLaTeX / biber build: PASS
- deterministic PDF/identifier preflight: PASS
- page count: `11`
- final PDF byte count: `285892`
- final PDF SHA-256: `8a363a33db80f55a047a8d6cdfecedb196f380939a3d40e68e3c3d21aded2764`
- validated-source manifest SHA-256: `48d9bcb924946a31dae87fd9a9510116743aedc591341bd76bf160061eb4ed88`
- log gate findings: none

Canonical publication paths:

- `sources/SP001/publication/v2/SP001-publication-preview.pdf`
- `sources/SP001/publication/v2/SP001-publication-preview.txt`
- `sources/SP001/publication/v2/validated-source-manifest.json`
- `surveys/special/SP001/main.pdf`
- `surveys/special/SP001/main.tex`
- `surveys/special/SP001/references.bib`
- `surveys/special/SP001/jgaisurvey.sty`

## Final exact-PDF visual QA

The rebuilt exact PDF was exported through a temporary SHA-verifying Actions transport and rendered at 170 DPI. The transport PR was closed without merge after inspection.

The final exact PDF SHA reviewed visually was:

`8a363a33db80f55a047a8d6cdfecedb196f380939a3d40e68e3c3d21aded2764`

All 11 pages were inspected:

1. cover — `Special` word break fixed; no clipping or collision
2. frontmatter / TOC — hierarchy and page references legible and aligned
3. foundations section — body and claim-boundary box intact
4. GLM section — body and claim-boundary box intact
5. Qwen section — body and claim-boundary box intact
6. DeepSeek section — body and claim-boundary box intact
7. Kimi section — body and claim-boundary box intact
8. runtime / Open Weight ecosystem section — body and claim-boundary box intact
9. parallel / boundary section — body and claim-boundary box intact
10. `この号の総括` — required issue-level synthesis present before end matter
11. References — starts cleanly and remains readable

No clipping, overlap, orphaned heading/tail, broken glyph, accidental blank wrapper, or pagination defect was found in the final exact PDF.

## Quality Regression Bundle

A complete Core + `THEMATIC` + `LONGFORM_SPECIAL` Quality Regression Bundle was built and validated in PR #392.

Canonical path:

`sources/SP001/publication/v2/quality-regression-bundle-v2.json`

The bundle binds:

- Production Profile SHA-256: `91836f2f255bec01887d85619da792c49a74bf9a7ccc1c861f81698e40642f44`
- validated source SHA-256: `48d9bcb924946a31dae87fd9a9510116743aedc591341bd76bf160061eb4ed88`
- final PDF SHA-256: `8a363a33db80f55a047a8d6cdfecedb196f380939a3d40e68e3c3d21aded2764`
- final PDF byte count: `285892`
- bundle content digest (`bundle_sha256`): `905cb9ea991ca264fe883a3b7ad6bf4b0bd0ff028033db6bbba15c73c5c90e3f`

All applicable quality checks passed:

### Core deterministic

- `SUBJECT_ENTITY_PROPERTY_BINDING`
- `IDENTIFIER_PRESERVATION`
- `PDF_PREFLIGHT`

### Core semantic

- `SOURCE_SPECIFIC_FAIL_CLOSED_NOTES`
- `BIBLIOGRAPHY_METADATA`
- `POST_TRANSFORM_SEMANTIC_REVALIDATION`

### THEMATIC semantic

- `THEMATIC_RESEARCH_CLOSURE`
- `THEMATIC_HISTORICAL_ATTRIBUTION`

### LONGFORM_SPECIAL deterministic / visual

- `EMPTY_WRAPPER_SUPPRESSION`
- `TOC_HIERARCHY`
- `TECHNICAL_NOTES_TAIL_NEEDSPACE`
- `LONGFORM_PAGE_BALANCE`

The bundle was also passed through the exact `DRAFT_COMPLETE -> VALIDATED_DRAFT` Core stage validator before being adopted.

## Production State transition: DRAFT_COMPLETE -> VALIDATED_DRAFT

The canonical work-branch control path was used with an exact-State-locked `control-request.json`.

The Core stage validator accepted:

- `validated-source`
- `publication-pdf`
- `quality-regression-bundle`

Production State then advanced:

- from: `DRAFT_COMPLETE`
- to: `VALIDATED_DRAFT`
- recorded at: `2026-08-23T01:19:41Z`
- transition basis commit recorded by State: `e05d7119ca153d7c596bbdc3895fbd5d7e6cec8f`
- validation checkpoint: `passed`
- next action became: `stage:publication-candidate`

## Publication Candidate

An immutable Publication Candidate was built and prevalidated in PR #394, then merged to the work branch.

Canonical path:

`sources/SP001/publication/v2/publication-candidate-v2.json`

Candidate authority:

- status: `READY_FOR_PUBLICATION_PREVIEW`
- publication profile: `LONGFORM_SPECIAL`
- source SHA-256: `48d9bcb924946a31dae87fd9a9510116743aedc591341bd76bf160061eb4ed88`
- PDF SHA-256: `8a363a33db80f55a047a8d6cdfecedb196f380939a3d40e68e3c3d21aded2764`
- PDF byte count: `285892`
- page count: `11`
- Quality Bundle SHA-256: `cf1d4f846a8a3ff2501ad445fb5e3430d58d787c47a624e6a777c3ec7a76ab74`
- candidate content digest (`candidate_sha256`): `87ce71f31c6ea880154b00a495f35adbc431f80091a61874f654eccc38c86e94`

The candidate passed `VALIDATED_DRAFT -> RELEASE_CANDIDATE` Core stage prevalidation before adoption.

## Production State transition: VALIDATED_DRAFT -> RELEASE_CANDIDATE

A second exact-State-locked canonical control request was adopted through the work-branch control workflow.

Production State advanced:

- from: `VALIDATED_DRAFT`
- to: `RELEASE_CANDIDATE`
- recorded at: `2026-08-23T01:25:09Z`
- transition basis commit recorded by State: `ee778b828826b9f3316e9c5072e2ef06da07bf10`
- `next_action`: `PUBLICATION_PREVIEW`
- `terminal_reason`: `HUMAN_GATE_REACHED`
- `human_gates.publication_preview`: `pending`
- exception gate: inactive

This is the intended stopping point for autonomous work.

## Current Human Gate input

The Publication Preview reviewer should evaluate the immutable Publication Candidate and exact PDF:

- Candidate: `sources/SP001/publication/v2/publication-candidate-v2.json`
- PDF: `sources/SP001/publication/v2/SP001-publication-preview.pdf`
- exact PDF SHA-256: `8a363a33db80f55a047a8d6cdfecedb196f380939a3d40e68e3c3d21aded2764`
- page count: `11`

The reviewer may approve this exact candidate/PDF or request publication changes. Any change that alters the PDF bytes requires a new validated candidate before approval.

## Explicitly not performed

Because `PUBLICATION_PREVIEW` is a normal Human Gate, this session did **not**:

- fabricate or infer Publication Preview approval
- create `publication-preview-approval-v2.json`
- perform post-approval Visual Review authority creation
- freeze the publication
- create a Release Manifest for publication
- merge/release SP001 to `main`
- create or reconcile a GitHub Release

Those steps are downstream of explicit Publication Preview approval.
