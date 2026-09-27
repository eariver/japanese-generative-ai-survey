# Sol review — TS-002 Issue #543 r7 final independent full-text scan

Date: 2026-09-27 JST  
Disposition: `REQUEST_CHANGES / INDEPENDENT_FULLSCAN_RESIDUALS_FOUND / HUMAN_R10_REQUIRED`

## Reviewed candidate

- branch lineage: `special/beyond-text-2026-work`
- worker candidate commit: `8a9460fb19b87ca3eb8ae246de6253b89a09fb73`
- PDF: `surveys/special/beyond-text-2026/main.pdf`
- pages: 78
- PDF SHA-256: `0797c38a533a5b90ae089f8f9006b5ba6ea17ed4ae28c2460f0f0bb7e429aa5d`
- Candidate SHA-256: `4580b9a0220e836dbe8980ae02c0d67d791b0e61cefe7658c4a4b1ab4f4a6121`
- lifecycle at reviewed candidate: `RELEASE_CANDIDATE`
- Publication Preview: pending

## Mechanical pipeline audit

PASS.

The r9/r6 worker execution reached a fresh 78-page Release Candidate. Frozen Core identities remained unchanged, validation passed, bibliography coverage remained 139/139, and the worker's semantic/visual review surfaces reported PASS.

Sol additionally obtained the exact generated PDF from the successful GitHub Actions artifact, verified the PDF hash against the publication candidate, rendered all 78 pages, and visually inspected the complete document. No clipping, overflow, broken glyph, blank-page defect, or table-layout blocker was found. The sparse final bibliography page is a normal terminal page.

Therefore the current blocker is **not** layout, build, Core behavior, or page generation.

## Why Issue #543 still cannot close

Issue #543's acceptance criterion is seed-independent reader-facing terminology closure. Sol therefore performed a separate full-text/source readback instead of treating the worker zero-count dictionary as the editorial ground truth.

That independent scan found additional residual literalizations outside the r2-r6 mappings, including:

- technical text-modality compounds such as `文条件づけ`, `文整合`, `文符号器`, `文枝`, `文類似`, `文品質`;
- prompt-template `集成`, `尺度掃引`, reader-facing `jointly`, `joint 空間`, `baseline`, and `framing`;
- adapter/adaptation concepts incorrectly written with `適合`, colliding with the edition's own glossary meaning of distributional fit;
- `背骨` for model/evaluation backbone;
- MusicGen tokenizer literalization, Music ControlNet `拍弦予測`, MuSTANGO `対照音楽ネットワーク`, Imagen Video `回転整合`, Unified-IO `金字塔`, and other source-specific terms.

These are now fully adjudicated by Sol in:

`sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r7-final-independent-fullscan-20260927.md`

Muse must not independently reinterpret those decisions.

## Source-binding defect found by Sol

A separate citation-binding defect was found in Section 4.

`references.bib` establishes:

- `btd037` = T2I-Adapter
- `btd041` = SPADE/GauGAN

The current manuscript binds SPADE/GauGAN claims to `btd037` and T2I-Adapter claims to `btd041`. These are reversed.

r7 therefore authorizes exactly two new bounded citation corrections:

- `SOL-CIT-003`: SPADE/GauGAN-bound Section 4 claims -> `btd041`
- `SOL-CIT-004`: T2I-Adapter-bound Section 4 claims -> `btd037`

These corrections must be source/context-bound, not a blind repository-wide key swap.

Existing authorized exceptions `SOL-CIT-001` and `SOL-CIT-002` remain frozen.

## Core boundary

Frozen Core v2 remains immutable.

No Core repair, schema change, transition change, compatibility change, template change, or shared configuration change is authorized or necessary. All remaining work is TS-002 edition-local.

## Gate consequence

The reviewed edition is already at `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending`.

Under the frozen Core, applying r7 requires a new explicit Human Publication Preview `REQUEST_CHANGES` revision returning the edition to `DRAFT_COMPLETE`. Sol does **not** synthesize that Human decision.

Required next Human decision:

`Publication Preview r10 / REQUEST_CHANGES / regeneration_boundary=DRAFT_COMPLETE`

narrowly for applying the Sol r7 authority and SOL-CIT-003/004.

Architecture approval remains preserved. Freeze/Release remain unauthorized.

## Current post-review authority

This review is recorded after the r7 authority map. The branch HEAD created by this review record becomes the exact launch authority for any later r10 worker execution and must be read back before issuing that execution.

Issue #543 remains OPEN.
