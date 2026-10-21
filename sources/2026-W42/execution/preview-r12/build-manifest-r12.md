# W42 r12 preview build manifest (NONCANONICAL, NOT A PUBLICATION PREVIEW)

Status: `EDITION_LOCAL / PREVIEW_PROOF / NO_STAGE_TRANSITION`
Date: 2026-10-18 JST. Branch: `weekly/2026-W42-v2-work`.

## Inputs (all edition-local proposals; canonical bytes untouched)
- 7 r12 proposals v12.0 REVISED, frozen draft-check 7/7 PASS, synthesis-check PASS (see `../editorial-revision-r12/validation-report-r12.md`).
- Reader preview JSON/MD r12 (filtered, CLAIM_BOUNDARY excluded).
- `main.tex` sha256 `b4f4b380cb7502fce0067ce1df91f6ef9a9fa060e84ad5da822d9820d334324e`.
- `preview.sty` sha256 `3954d6bfc879a42b325c81dd336c967eb88f9266901fab4f6157e87735323736` (= W41 `jgaisurvey.sty` verbatim EXCEPT: `\ProvidesPackage` renamed + biblatex block removed with comment; biber unavailable in this transport; citations rendered as chapter source boxes + URL lists).

## Build
- Compiler: LuaLaTeX, TeX Live 2026 (TinyTeX), `jlreq` + `luatexja-preset` HaranoAji (fonts present), 3 runs to stable `.aux`.
- Log: zero `Overfull/Underfull`, zero `Missing character`, zero LaTeX warnings (excluding package-load info lines). `main.log` retained beside the PDF for audit.
- Output: `main.pdf` sha256 `aa1cc1800a128d26233cf66a6c6b8b12a07ce7f4caa49449936501756c983f12`, 419,471 bytes.

## Page report (16 pages, A4 two-column + cover + closing)
- p1 cover (title, deck, NONCANONICAL marker, cutoff/repo/build lines). p2–p15: seven chapters with 7 comparison tables (table* spans), 7 caution notes (tcolorbox), 7 chapter source boxes ([Px-n] http(s) URLs only).
- p16: closing `出典一覧と確認水準` pointer section + NONCANONICAL marker only — intentionally partial (~15% full). No padding added per contract; flagged, not filled.
- Density: 92 paragraphs / ~21.3k body chars / 7 tables over 16 pages. Reference: W41 canonical PDF is 17 pages for 66 paragraphs / 14.6k chars + frontmatter extras. Architecture target 28 / max 30 is NOT met by honest content at this density; the gap is a Sol/Human planning decision (deepen content vs amend plan), not a layout defect to pad over.

## Layout QA (every page rendered at 110dpi and visually inspected)
- Cover: title/deck/marker legible; cutoff line wraps correctly.
- Chapters: no clipped text, no tiny type, no broken tables; table* spans stay within margins; tcolorbox notes unbroken across columns except where TeX naturally splits (none observed overflowing).
- CJK: no tofu/mojibake on any page; mixed Latin/Japanese line-breaking clean; URLs break via xurl without overflows.
- Source display: every chapter ends with a numbered http(s) URL box; no internal paths; end section points back to chapter boxes (no duplication).
- Known non-blockers: (1) section titles follow canonical Architecture wording (e.g. P5 `開示・蒸留・検証アクセス`) while in-chapter headings carry the revised taxonomy — intentional, canonical fidelity preserved; (2) final page partial (see above).

## Non-approval marker
THIS PDF IS `NONCANONICAL_EDITORIAL_PROOF`. It is NOT a validated release, NOT a Publication Preview, and carries NO Human approval. Generic Core Reader/Publication stages were NOT run. No `VALIDATED_DRAFT` transition, no Publication Preview record, no Freeze/Release, no main merge.
