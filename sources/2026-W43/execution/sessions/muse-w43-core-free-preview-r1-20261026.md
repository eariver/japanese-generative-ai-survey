# Muse W43 Core-free PDF Preview r1 worklog — 2026-10-26

Branch: `weekly/2026-W43-v2-work`. Contract: `sol-w43-core-free-preview-r1-tex-pdf-visual-qa-20261026.md`.
Terminal: `MUSE_W43_CORE_FREE_PDF_PREVIEW_R1_READY_FOR_SOL_VISUAL_REVIEW` (PDF + all-page images/contact sheets, 20/80/29 parity, bibliography/provenance real, committed + remote-verifiable, no critical defects).

## Guards

- Remote six-way PASS read-only before writes: work dispatch `fa4235…`/`bf5582b2…` (parent `8c61ecd…`, diff contract only), pre-parent `8c61ecd…`/`845f6cb…`, main `041a08df…`/`a134dc36…`, frozen `774dd39a…`/`cd46a6f7a…` (ls-remote + gh API + local objects).
- Local `bc6b1c…` (r3.5, 2-behind of dispatch, ancestor of `8c61ecd…`) → `fetch origin weekly/2026-W43-v2-work` + `merge --ff-only` → `fa4235…`. Clean, no reset/rebase/force.
- r3.5 SHAs pinned exact: `6f07cb49…` / `6fd9d6fe…` / `85d94d74…`. Checker rerun exit 0 PASS.

## Build

- Projection from exact r3.5 (title clean, 19 token classes → natural Japanese, internal paths → 保存済み一次資料). Diff auditable.
- TeX 897 lines from projection (20 tables `tabularx`, 3 figures `tcolorbox`, 2 bash/python + 2 JSON `verbatim`, 8 reading-note boxes, TOC, 36 bibitems). `preview.sty` from W42 r15 (version comment W43).
- lualatex ×4 (final 2 clean, exit 0): fixed figure `\\[` Illegal → `\par`, URL/SHA Overfull → trim + `\url`. Final 22 pages, 480229B, metadata `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` (detokenize), 0 warnings.
- pdftoppm 150dpi → 22 PNGs + PIL 3 contact sheets. Inspected all pages via PNGs/sheets: tables fit, fonts/glyphs OK, code/URLs break, order correct, P8→recap mid-page p-20, bib p-21/22, p-22 tail sparse (expected). No critical defects.
- Manifest/fidelity/QA/visual-request built with exact SHAs. Volume 22 vs 38 target noted (W42 final 21 precedent, no padding).

## Outputs (SHAs at build)

- projection `e1a49da9…`, tex `0d8a8a09…`, sty `28a663bc…`, pdf `fd88cb7c…` (22p), log `8e29b6e7…`, pages 22 PNGs + 3 sheets (see manifest map).
- No State/Core/Architecture/Selection/Evidence/Gates mutation; edition-local + handoff/session/index only; `.aux/.toc/.out` excluded.

## Push/read-back

- Non-force commit + push + remote readback HEAD/Tree; `git diff --name-only` confirms scope; PDF blob exists remotely; commit-pinned PDF URL recorded below after push.
- Final HEAD: PENDING_AT_COMMIT; Tree: PENDING_AT_COMMIT; remote read-back: PENDING_AT_COMMIT.
- PDF URL: PENDING_AT_COMMIT (format: `https://github.com/eariver/japanese-generative-ai-survey/blob/<FINAL_HEAD>/sources/2026-W43/execution/core-free-preview-r1/main.pdf`).

Stop at Sol visual review. No independent PASS / Human approval / Freeze/Release claimed.
