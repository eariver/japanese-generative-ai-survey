# W42 r29 canonical build provenance and diff (r18 → r26 → r29)

Status: `SOL_W42_R29_CANONICAL_BUILD_INDEPENDENT_AUDIT_READY / STAGE_DRAFT_COMPLETE / PUBLICATION_UNAPPROVED`
Date: 2026-10-20 JST
Branch: `weekly/2026-W42-v2-work` (normal fast-forward only; no reset/rebase/new branch/force)

## 1. Authorities

- r18 Reader master: `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`
  - 7 chapters P1–P7, 28 selected topics, 157 blocks = 136 paragraphs + 7 headings + 7 notes + 7 tables
  - 7 captions / 27 rows / 110 cells, 150 nonTABLE blocks, 90 B-keys / 19 aliases / 177 ledger rows
- r26 diagnostic (independently audited CONTENT=PASS / PRINT=PASS_WITH_LIMITATIONS, PROCESS deviation separately dispositioned):
  - TeX blob `ffdd45742c16fc2f19fd21805479ca9d8373f30b` (1005 lines, 96891 bytes, SHA256 `5bbdca1b5f2d9671e123aed2a4bc25f876fdef28027158e8cbb9fc960d158b73`)
  - PDF SHA256 `c76f4a6e975039ec813e17909bd62768303c48c2e7018588c07e6bab7fe780c0` (508624 bytes, 21 pages)
  - style SHA256 `f0492fb6b2b9085f282a12120885b20271ec11b0fab56d8848d6f0ee474d534d` (6132 bytes)
  - layout: MULTICOL-V2 inter-segment wide tables, 7mm gutter, needspace 18/18/30/30/22/22/20
- Human authorizations: r29 build-only (`human-w42-r29-canonical-reader-pdf-build-authorization-20261020.md`), Route A conditional (`human-w42-r27-conditional-route-a-approval-20261020.md`)
- State-pinned Core: `a4f25630270f029656f35771592f9ebda02fa5cc`; reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`; Frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

## 2. Canonical TeX diff (r26 → r29)

Exact `diff -u` (only cover/provenance, no Reader prose/cell/citation change):

- header comment: diagnostic stamp → canonical provenance (`r29: r26 MULTICOL-V2 geometry kept; cover production normalization only`)
- `\surveyeditiondescriptor{週刊Technical Survey（診断用・非正準・未承認）}` → `\surveyeditiondescriptor{週刊Technical Survey}`
- `\surveycoverstory{...}{...}{NONCANONICAL DIAGNOSTIC \\ NOT A PUBLICATION PREVIEW \\ NOT FOR HUMAN APPROVAL}` → third arg `{}` (no anchors printed; headline/deck preserved)
- all body prose, 7 tables, citations, geometry comments, needspace, gutter unchanged

Verification:

- `grep -c NONCANONICAL|NOT A PUBLICATION|NOT FOR HUMAN|診断用・非正準・未承認` in canonical TeX = 0
- restored cells present: `商用上限1000万米ドル（法主体の年商）` count 1; `Super VL` + `ファイル未確認` on p09 (split across PDF text lines, visually intact per PNG)
- old errors absent: `商用上限1000万ドル` (without 米ドル/年商) 0; `Super VL未開封` 0

## 3. Canonical outputs

- `surveys/weekly/2026-W42/main.tex`: 96790 bytes, SHA256 `2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3`
- `surveys/weekly/2026-W42/main.pdf`: 505102 bytes, 21 pages, SHA256 `8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9`
- `surveys/weekly/2026-W42/preview.sty`: 6132 bytes, SHA256 `f0492fb6b2b9085f282a12120885b20271ec11b0fab56d8848d6f0ee474d534d` (byte-identical to r26)
- build: `SOURCE_DATE_EPOCH=1792311600 FORCE_SOURCE_DATE=1 lualatex -interaction=nonstopmode -halt-on-error main.tex` ×3; runs 2–3 byte-identical; LuaHBTeX 1.24.0 (TeX Live 2026), jlreq, multicol + capt-of
- log: 0 errors, 0 Overfull/Underfull, 0 missing glyphs, 0 LaTeX warnings; `Output written on main.pdf (21 pages, 505102 bytes)`
- r26→r29 PDF delta: -3522 bytes, same 21 pages; page text chars identical except p01 (380 vs 467, stamp removed); p02–p21 char counts match r26 exactly

## 4. Exceptions / limits

- Cover stamp removal affects only p01 (isolated by `\clearpage`); body pagination unchanged (verified by per-page char counts and table page map).
- No content padding/shortening to force page count; ~21pp accepted per Route A.
- No semantic/visual PASS claimed; independent Sol audit required on exact new hashes + PNGs.
- No Stage/Gate/Candidate/Freeze/Release; `production-state.json` untouched (`DRAFT_COMPLETE / PUBLICATION_UNAPPROVED`).
