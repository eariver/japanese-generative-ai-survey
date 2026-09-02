# W33 Luna Reader Validation / CI Build Session

- Issue: `2026-W33`
- Branch: `weekly/2026-W33-v2-work`
- Exact starting SHA: `c9d9b973b4fb830bafb7199b3f8ed9731db904d6`
- Start guard: remote branch HEAD matched the exact starting SHA before the first GitHub write.
- Reviewed-main Core authority: `6267de3f6876f491950139757bfdf1085fc07bdc`

## Scope and authority

This session produced the reader/publication validation candidate only. The
seven Sol-accepted Draft Package/Result identities and the reviewed Architecture
were retained. No Web, Google Drive, raw-source, fresh Evidence, candidate, or
Architecture placement was added. Reader-facing substantive claims were limited
to the accepted Draft Results; Draft/Evidence material was used only for source
metadata, attribution, limitations, and identity preservation.

The final `w33-week-in-review` chapter is an independent cross-package synthesis
of the six substantive chapters. It covers what changed, why the changes matter
together, and what to watch next. The Weekly Community Movement block is visibly
context-only and does not serve as technical authority.

## Source and CI build

- Reader source commit: `2409fba0b3a4f866ce7251b8f05f49da6ebf50e1` (normal non-force push).
- Workflow: `Build weekly survey PDF` from `.github/workflows/build-weekly-survey.yml`.
- Selected source-build run: `33398104252` (run number 176), head SHA exactly
  `2409fba0b3a4f866ce7251b8f05f49da6ebf50e1`.
- `resolve-issue` job `99507430652`: success.
- `build` job `99507608795`: success.
- Final TeX publication-warning gate: PASS. No final undefined
  references/citations, biblatex rerun warning, Overfull/Underfull box, or
  Missing character gate failure remained.
- Selected artifact: ID `9760255099`, name
  `japanese-generative-ai-survey-2026-W33`.
- Artifact ZIP digest reported by Actions:
  `sha256:907d1c54dfe089cd6466e405e474e5279ce09fbe4ec4fe8d47b252f4ad08094b`.
- Artifact `main.pdf.sha256` and an independent hash of artifact `main.pdf`
  both yielded `4f1028c221101cd21cf300a3916c9d4b7cf589b5f672a0f97f61aa6afc992243`.
- PDF size: 270201 bytes; strict PDF preflight page count: 11; encrypted: no.
- Exact PDF pin commit: `68b6da34700379b61d93421cf7c216d6296cb787` (normal
  non-force push, parent `2409fba0b3a4f866ce7251b8f05f49da6ebf50e1`).
- Repository PDF blob: `9c0de61f6469e2f40ca81c293a541f4669f95bbc`.
- The committed PDF was fetched again from that commit and its normalized
  base64 matched the local artifact bytes exactly before review. The PDF bytes
  were not re-rendered or mutated; single-page re-rendering was used only as a
  visual inspection aid for two PNG conversion read errors.

## Canonical validation candidate

The canonical Core helpers generated and validated the following artifacts:

| Artifact | Path | SHA-256 |
|---|---|---|
| Reader Manuscript Manifest | `sources/2026-W33/publication/v2/reader-manuscript-v2.json` | `4fc617a3179a01647fd0bff3411151cf3e7baf58bb38c04e1889a4789db7582e` |
| Validated reader source | `surveys/weekly/2026-W33/main.tex` | `d09a97a0bc8c54f6230235929ad351391e1e8662959a4a809fe6bba235cc4f4c` |
| Publication PDF | `surveys/weekly/2026-W33/main.pdf` | `4f1028c221101cd21cf300a3916c9d4b7cf589b5f672a0f97f61aa6afc992243` |
| PDF digest file | `surveys/weekly/2026-W33/main.pdf.sha256` | `2e8fddb242e0a7e205b5a41c83b194b3d1fdc868176d43a7a78e462f04dc1f49` |
| Quality Regression Bundle | `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json` | `1bd21cbcd1f97fd33a198b569eb87a298f94caed4b9a2373d596487dbaf8d266` |
| Semantic / Editorial Review | `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json` | `03deca95bc5d8de5bd755d6f27b2de1dbd97ac3ff6ca67a085d173b866342e6c` |
| Exact-PDF Visual Review | `sources/2026-W33/publication/v2/visual-review-v2.json` | `5f72e610cb43a0a911f93477f74818721d3781f2ba2b54020b89f1dbdbfc2b1f` |

Deterministic result authorities bound by the Quality Regression Bundle:

- `sources/2026-W33/publication/v2/deterministic/subject-entity-property-binding.json`
  — `c430c6e5f1c4e2a03f3bb26bf926e8264e1827ce9a2870370034126ec9cace2c`
- `sources/2026-W33/publication/v2/deterministic/identifier-preservation.json`
  — `1ec4f253c8ce388fcdcf1b7a6d9ab8c087a588ea7fce043028a3e4520d6ff1ae`
- `sources/2026-W33/publication/v2/deterministic/pdf-preflight.json`
  — `ca57851ff7d4cee05beec7391d8af1be1464a85b04e465462d21718f301b0867`

The three deterministic checks all PASS. Citation/entity binding found 28
cited keys, 28 bibliography keys, and no missing or unused key. Identifier
preservation found seven packages, seven results, zero synthetic candidates,
and zero new Architecture placements.

## Visual review

All 11 pages of the exact committed PDF were inspected: pages 1, 2, 3, 4, 5,
6, 7, 8, 9, 10, and 11. The review found no clipping, missing glyphs, blocking
overflow, broken box borders, or unreadable layout. The document remains below
the hard maximum of 24 pages (11 pages); no padding to the 18-page soft target
was introduced.

## Stage contract and stop boundary

Canonical deterministic `DRAFT_COMPLETE` stage-contract validation returned
`CORE_STAGE_CONTRACT = PASS` for the candidate artifact set:

- from-state: `DRAFT_COMPLETE`
- contract next-state reported by the validator: `VALIDATED_DRAFT`
- implementation commit used by the validator:
  `c9d9b973b4fb830bafb7199b3f8ed9731db904d6`
- validation report was kept outside the repository at
  `/workspace/scratch/w33-stage-contract-draft.json`;
  SHA-256 `ea2c13da40f2145ea76ff1967e25c9e781262cc3d3a5b44bce17986e568cf166`.

This report is validation evidence only. No `ADVANCE_STAGE` was executed after
`DRAFT_COMPLETE`; no Validation Stage Checkpoint, operator bridge request,
Publication Candidate, Publication Preview Human Gate, freeze, or release was
created.

Production State was not modified. Starting and final State SHA-256 is
`1f398179156c346ba80fdb07e767d4e6273bcfcb18a21b48b98dd93c077989fa`; lifecycle
remained `DRAFT_COMPLETE`, draft checkpoint remained `passed`, and validation
and publication-preview checkpoints remained `pending`.

Unchanged authority hashes checked at close:

- Production Profile: `19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`
- Architecture: `8bc68693e182dbda9d7067e9bc127bf69548aba87ccd3078cb744bd991c6b406`
- Architecture Review Summary: `88c029b4bdc7944e1b6f213f0e05c4a8a650cec229bfeafc14c3cc0272410ccb`
- Architecture Review Attention: `b3bd9ef809076bf22e08da89347028bdee620bf26f8dd08abdf025c5b75e489`
- Draft checkpoint: `1397cf83d6837b5770b8315c7b8fa5f4771ca363a35201be0c76b74e7dfb4db2`

## Changed-path inventory

- `surveys/weekly/2026-W33/.latexmkrc`
- `surveys/weekly/2026-W33/main.tex`
- `surveys/weekly/2026-W33/main.pdf`
- `surveys/weekly/2026-W33/main.pdf.sha256`
- `surveys/weekly/2026-W33/references.bib`
- `surveys/weekly/2026-W33/sections/00-frontmatter.tex`
- `surveys/weekly/2026-W33/sections/10-frontier-models-access.tex`
- `surveys/weekly/2026-W33/sections/20-cyber-access-governance.tex`
- `surveys/weekly/2026-W33/sections/30-serving-runtime.tex`
- `surveys/weekly/2026-W33/sections/40-memory-decoding-systems.tex`
- `surveys/weekly/2026-W33/sections/50-agent-evaluation-reliability.tex`
- `surveys/weekly/2026-W33/sections/60-multimodal-media.tex`
- `surveys/weekly/2026-W33/sections/70-week-in-review.tex`
- `surveys/weekly/2026-W33/sections/99-source-notes.tex`
- `sources/2026-W33/publication/v2/reader-manuscript-v2.json`
- `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json`
- `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json`
- `sources/2026-W33/publication/v2/visual-review-v2.json`
- `sources/2026-W33/publication/v2/deterministic/subject-entity-property-binding.json`
- `sources/2026-W33/publication/v2/deterministic/identifier-preservation.json`
- `sources/2026-W33/publication/v2/deterministic/pdf-preflight.json`
- `sources/2026-W33/execution/sessions/w33-luna-reader-validation-ci-build-20260831-r1.md`

Normal successful stop requested by the handoff:

`VALIDATED_DRAFT_CANDIDATE_READY_FOR_SOL_REVIEW`
