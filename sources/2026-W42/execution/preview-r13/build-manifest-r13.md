# W42 r13 TeX/PDF build manifest (NONCANONICAL, NOT A PUBLICATION PREVIEW)

- Inputs: 7 r13 proposals v13.0 REVISED (frozen draft-check 7/7 PASS) + proposed synthesis (PASS) under `execution/editorial-revision-r13/`.
- TeX: `execution/preview-r13/main.tex` (820 lines; 7 tables; \cite keys [B01]–[B59]; thebibliography with category tags).
- Style: `preview.sty` = verbatim W41 `jgaisurvey.sty` except: `\ProvidesPackage` renamed + biblatex block removed (no biber in this transport; documented deviation). All other layout macros identical and read-only.
- Compiler: LuaLaTeX, TeX Live 2026 (TinyTeX), `jlreq` + `luatexja-preset` HaranoAji (fonts present). 4 runs to stable aux.
- Output: `main.pdf` — 465913 bytes — sha256 `84d07de08e738a72acda8a1dd743fd452dc35f401711d6be40848b95f10e7782` — 19 pages, A4 two-column + cover + bibliography.
- Log: `main.log` committed. Zero overfull/underfull hbox, zero missing CJK glyphs, zero undefined citations/refs after final runs; ONE overfull vbox (43.6pt, P7 table* float, p16) — visually verified whitespace-only, documented in review-pages.
- Renders: 19 page PNGs @150dpi + 2 contact sheets under `pages/`, all hashed in review-pages index.
- TeX↔proposal fidelity: TeX body text = preview JSON block text verbatim; ONLY delta is appended `\cite{...}` markers (documented here). Block→key crosswalk: `citation-repair-ledger-r13.json` (`direct_source_keys`) + `bibliography-map-r13.json`.
- Page verdict: 19 pages vs Architecture target 28 / max 30. Honest content at magazine density (W41 canonical: 17 pages). Gap is a Sol/Human planning decision (deepen vs amend plan), not padded.
- Markers: cover + footer carry `NONCANONICAL EDITORIAL PROOF / NOT A PUBLICATION PREVIEW`. No VALIDATED_DRAFT, no Publication Preview, no Freeze/Release, no main merge.

(End of manifest)
