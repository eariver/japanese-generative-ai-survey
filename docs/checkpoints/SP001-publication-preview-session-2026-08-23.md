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

This was the first arrival at the intended stopping point for autonomous work. The 11-page candidate was subsequently rejected by Human Publication Preview and is superseded by the Issue #400 revision recorded below.

## Issue #400 Publication Preview revision trial

Human Publication Preview of the 11-page candidate opened Issue #400: `[Publication][SP001] Previewがmixed layoutから回帰し、LONGFORM_SPECIALとして著しく内容不足`.

The requested correction had four independent dimensions:

1. restore the Special mixed-layout contract: full-width headings/standfirsts, balanced two-column narrative, full-width synthesis/comparisons and Claim Boundary/Technical Notes, one-column References;
2. restore LONGFORM_SPECIAL technical depth from already accepted Evidence rather than mechanically padding to the architecture page target;
3. restore reader-facing synthesis / source-backed Technical Notes / chronology and comparison layers;
4. remove internal Core v2 / Evidence / materiality / verification-task language from the reader-facing PDF.

The revision explicitly preserved accepted Architecture, Draft Results, Profile Synthesis and Evidence authority. No new external Evidence was admitted.

### Generic renderer hardening before the rerun

Issue #400 exposed generic LONGFORM_SPECIAL renderer gaps rather than only SP001-local prose defects.

- PR #431 `Core v2: finalize longform Publication Preview revisions` merged to `main` as `891091ed1446ef614f1c8b7775e64368dee40498`.
  - reader-facing longform prose is assembled from reviewed Evidence-backed publication content rather than raw production Draft blocks;
  - cross-family comparison returns to normal full-width layout;
  - internal review/Evidence-pass wording is rejected from reader-facing output;
  - pending, unapproved Publication Preview revisions may replace renderer-owned generated source without editing accepted Draft/Evidence bytes.
- PR #432 integrated the reviewed renderer into `special/SP001-v2-work` as `284d1b19e6e00b262445ea010238a40f2b35a3c8`.

The reconstructed semantic-publication request was separately checked before execution:

- byte count: `49038`
- SHA-256: `dcb2e6138e0ac3c9a69f4894b7886e07b655c2076fe145b068b487e007027896`
- all seven publication packages present exactly once;
- accepted Evidence only; HOLD / NEEDS_MORE records not used as factual authority;
- Technical Notes covered assigned Evidence and canonical URLs;
- cross-family comparison remained non-ranking and architecture-consistent;
- no new external Evidence was introduced.

### Workflow-chain failure and rerun route

PR #437 `SP001: regenerate longform Publication Preview for Issue #400` was the first revision execution route. Its semantic-publication workflow reached `action_required` because an earlier commit in the chain was authored by `github-actions[bot]`; GitHub would not use that bot-generated commit to trigger the next write-capable workflow.

This was treated as an execution-chain limitation, not a semantic or Evidence failure. PR #437 was therefore not used as the final execution route.

A fresh human-authored execution branch was opened as PR #440 `SP001: rerun Issue #400 Publication Preview`. This successfully triggered the existing semantic-publication workflow without changing Architecture, Draft or Evidence authority.

### Layout/style defects found during the rerun

The rerun exposed further generic style assumptions:

- generated `main.tex` used `wideflow`, but the shared style did not yet define the environment;
- initial repair experiments used a review-branch-only `wideflow` wrapper;
- deterministic preflight then exposed loose-line / overfull behavior in dense mixed Japanese/English longform material and full-width tables;
- a temporary review-only `\hbadness=10000` was used only during diagnosis and was intentionally excluded from the final shared style; Overfull diagnostics were never intentionally suppressed in the final generic repair;
- the exact 1em full-width table overflow was traced to paragraph indentation interacting with `tabularx{\linewidth}` inside the full-width wrapper.

The durable generic fix was extracted from the SP001 branch rather than left as a review-only patch:

- PR #441 `Core v2: harden LONGFORM_SPECIAL full-width style` merged to `main` as `198c69703dba7b4f2f7b1d914d88f72bf7d7d887`;
- it defines `wideflow` as a normal full-page-measure wrapper while renderer-owned `multicols` handles narrative columns;
- it zeroes paragraph indent inside `wideflow` and adds conservative table/URL line-breaking behavior;
- it does not include the temporary `\hbadness` suppression;
- PR #442 integrated exactly this one-file shared-style change into `special/SP001-v2-work` as `91fdf25711775ab02524c542462afb441546807e`.

During PR #441/#442 validation, the repository's `Pipeline contract tests` workflow failed because `config/survey-production-v2-requirements.txt` installed `jsonschema` but an existing test module directly imported `pytest`. The Special post-draft contract and real weekly LuaLaTeX build passed. This dependency mismatch was observed but deliberately not repaired as part of SP001 publication work.

## Revised 19-page Publication Preview

PR #440 ultimately persisted and merged the Issue #400 publication artifacts to `special/SP001-v2-work` as merge commit `b3bc51fc1ba6439dde9ee0d2c44a7828e920c88f`.

Final revised publication bytes:

- PDF path: `sources/SP001/publication/v2/SP001-publication-preview.pdf`
- page count: `19`
- PDF byte count: `390572`
- PDF SHA-256: `305ced9bba08604bff52a85b3fd223bf0a32e60b5ec0c14126bd39debc069a90`
- validated-source manifest SHA-256: `06e2588672742a3bca317a0605f93de10ee793bc621cea98e585b96b5ebaa6c4`

The LONGFORM_SPECIAL deterministic layout preflight reported:

- package count: `7`
- `multicol` flow count: `15`
- `wideflow` count: `15`
- Technical Note count: `22`
- `clearpage` count: `2`
- findings: none

The exact revised PDF was inspected across all 19 pages. The review confirmed:

- normal narrative body uses balanced two-column flow;
- timeline, synthesis and wide comparison layers are full-width;
- Claim Boundary and Source-backed Technical Note blocks are full-width and visually attached to their sections;
- References remain one-column;
- no clipping, overlap, broken glyphs, abnormal page holes or unusable URL wrapping;
- all required family/model identifiers survive PDF extraction;
- forbidden reader-facing production metadata patterns are absent;
- the seven package families have materially greater version-specific lineage / architecture / post-training / serving / distribution / license depth than the rejected 11-page candidate.

The deterministic PDF preflight for these bytes is PASS and records no log-gate or reader-surface leakage findings.

## Authority drift found after successful PDF regeneration

After the 19-page PDF/source artifacts had been merged, a final authority check found a critical post-revision inconsistency:

- `production-state.json` correctly remained `RELEASE_CANDIDATE` with `PUBLICATION_PREVIEW` pending;
- the repository PDF and deterministic preflight described the new 19-page SHA `305ced9b...`;
- however `quality-regression-bundle-v2.json` and `publication-candidate-v2.json` still bound the superseded 11-page SHA `8a363a33...`.

Therefore the repository had a valid revised PDF but **did not yet have a valid Human Gate input for that revised PDF**. The semantic-publication revision workflow regenerated source/PDF/preflight bytes but did not automatically rebuild the immutable Quality Regression Bundle and Publication Candidate authority.

This was corrected without changing Production State or Human Gate approval:

- PR #444 `SP001: bind revised Publication Candidate to 19-page preview` changed only:
  - `sources/SP001/publication/v2/quality-regression-bundle-v2.json`
  - `sources/SP001/publication/v2/publication-candidate-v2.json`
- PR #444 merged to `special/SP001-v2-work` as `6d019ec552ebb1977092fb7093d8982a09c76767`.

Final candidate authority:

- status: `READY_FOR_PUBLICATION_PREVIEW`
- source SHA-256: `06e2588672742a3bca317a0605f93de10ee793bc621cea98e585b96b5ebaa6c4`
- PDF SHA-256: `305ced9bba08604bff52a85b3fd223bf0a32e60b5ec0c14126bd39debc069a90`
- PDF byte count: `390572`
- page count: `19`
- Quality Bundle file SHA-256: `24889dbe7d35b89701c0b4b0b58454115b881d15606e38e3da2155fdc9595c12`
- Quality Bundle content digest (`bundle_sha256`): `a772a4f92f2d86e460f45d9b29fdeabf685dde740d032ef9d3e32eee17ebce0b`
- Candidate content digest (`candidate_sha256`): `12cc2e574916919c78dcdf17bcac0881bc002480f5e603d57703853bdbbfe3cf`

All twelve applicable Core + THEMATIC + LONGFORM_SPECIAL quality checks were re-bound or re-reviewed for the exact 19-page bytes.

One accidental draft PR (#443) was created while preparing the short-lived authority-rebind branch and was immediately closed without making or merging changes.

## Final Human Gate state at trial termination

At the end of the SP001 trial:

- branch: `special/SP001-v2-work`
- lifecycle state: `RELEASE_CANDIDATE`
- `next_action`: `PUBLICATION_PREVIEW`
- `terminal_reason`: `HUMAN_GATE_REACHED`
- Architecture Review: approved
- Publication Preview: pending
- `human_gate_provenance.publication_preview`: `null`
- exception gate: inactive
- Publication Preview approval record: absent
- Freeze: not performed
- Release: not performed

The canonical Human Preview input at termination is therefore:

- Candidate: `sources/SP001/publication/v2/publication-candidate-v2.json`
- PDF: `sources/SP001/publication/v2/SP001-publication-preview.pdf`
- exact PDF SHA-256: `305ced9bba08604bff52a85b3fd223bf0a32e60b5ec0c14126bd39debc069a90`
- page count: `19`

## Observations retained for later flow review

These are recorded as SP001 trial facts only. No flow/pipeline redesign is performed by this checkpoint update.

- write-capable workflow chaining through `github-actions[bot]` commits can stop with `action_required`, even when the semantic payload is valid;
- Publication Preview revision currently has a split authority lifecycle: source/PDF/preflight regeneration can succeed without refreshing the Quality Regression Bundle and Publication Candidate, so exact-byte Human Gate authority must be checked explicitly after revision;
- LONGFORM_SPECIAL renderer assumptions and shared style capabilities must evolve together (`multicols`, `wideflow`, table measure, URL/token breaking); otherwise semantic generation can be correct while publication compilation/preflight fails;
- review-only diagnostic suppression must not leak into durable shared style; the temporary `\hbadness` setting was successfully excluded before integration;
- the existing Pipeline contract test environment has a `pytest` dependency mismatch independent of SP001 content and should be handled in the separate flow-maintenance effort.

## Trial termination decision

On 2026-08-23, the owner decided to stop SP001 compilation at this point and return to the separate survey-production flow review.

Accordingly, this session updates only this SP001-specific checkpoint. It intentionally does **not** update:

- the survey-production flow/design documents;
- `docs/checkpoints/survey-production-core-v2-worklog.md`;
- any other flow-review work record.

SP001 remains an unapproved 19-page `RELEASE_CANDIDATE` retained as a concrete trial artifact and regression case for that later review.

## Explicitly not performed

Because `PUBLICATION_PREVIEW` is a normal Human Gate and the trial is terminated here, this session did **not**:

- fabricate or infer Publication Preview approval
- create `publication-preview-approval-v2.json`
- perform post-approval Visual Review authority creation
- freeze the publication
- create a Release Manifest for publication
- merge/release SP001 to `main`
- create or reconcile a GitHub Release

Those steps remain downstream of an explicit future Publication Preview approval if SP001 compilation is ever resumed.
