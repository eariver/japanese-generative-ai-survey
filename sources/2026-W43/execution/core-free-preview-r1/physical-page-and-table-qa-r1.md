# W43 physical page and table QA r1 (22 pages, 150dpi PNGs + 3 contact sheets)

PDF: `main.pdf` (`fd88cb7c…`, 480229 bytes, 22 pages, A4, LuaLaTeX 1.24.0, 0 warnings final).
Pages: `pages/p-01.png`..`p-22.png` + `contact-sheet-01.png` (p-01..08), `-02.png` (p-09..16), `-03.png` (p-17..22).
Method: inspected EVERY actual PDF page via PNGs + contact sheets at 150dpi; checked table width, font size, Japanese glyphs, clipping, floats, captions/row cohesion, code/URLs, near-empty/overfull, source notes, order, bibliography, P8→recap continuity, cross-page breaks. Build log 0 Illegal/Overfull/Errors after fix.

## Per-page observations

- p-01 (cover): Title `Japanese Generative AI Technical Survey 2026-W43`, date 2026-10-24, cutoff `2026-10-16 22:00 UTC -- 2026-10-23 22:00 UTC`, repo/build lines, neutral headline/deck/anchors (no intrusive NONCANONICAL stamp on cover; flag in PDF metadata + end footer only). Japanese glyphs correct, no tofu, rules aligned. PASS.
- p-02 (TOC): 8 sections P1-P8 + recap + bibliography, page numbers 3..22, dot leaders aligned, no overfull. PASS (TOC stable after 2 runs).
- p-03 (P1 start): Section header, intro prose, table `公開状態×時点` full-width, 4 rows + source note, no clipping, footnote-size readable, caption attached. PASS.
- p-04 (P1 cont.): Tables `total/effective/active` + `bench×harness` + `可用性×時刻×約款`, 3-4 cols, first col left, rest X, no overrun, 典拠 notes in small muted text. PASS.
- p-05 (P1 end/P2 start): Figure `文脈長の三層` (blue tcolorbox) + reading note box, then P2 header. Figure text wraps, no float detachment. PASS.
- p-06 (P2): Table `核×役割` 5 rows, prose on DSpark exclusivity, no cramped lines. PASS.
- p-07 (P2 cont.): Table `bench×分母×条件 (MemT)` + rights table `p2-f2` (4 rows: CC/PolyForm/MIT/excluded), license scope preserved, no table split across pages mid-row. PASS.
- p-08 (P2 code): Bash + Python `verbatim` blocks, monospace, line breaks preserved, Japanese comments readable, no clipping. PASS.
- p-09 (P3 start): Section P3, table `権限×条件 (Duet)` + prose on credentials, waitlist/US Pro-Max, 6000+ vs live distinction. PASS.
- p-10 (P3 cont.): Table `旧/新/未来 (auto-mode)` + figure `資格・承認フロー` (blue box, 2 paths + coming-soon label naturalized), reading note. No caption detachment. PASS.
- p-11 (P4 start): Section P4, prose on FLUX post-train/keyframes UNRESOLVED, table `倍率×削減率` (25.37x/22.31x/95.52% + 26.5x incongruent + 22x lower-bound). Arithmetic values correct. PASS.
- p-12 (P4 end/P5 start): Elo/price prose + P5 header + table `機能×モデル×対応言語` (STT/Realtime/TTS unresolved). Table width 0.96 linewidth, no overrun. PASS.
- p-13 (P5): Tables `AA×原表有無 (Ming)` + `様式×評価・料金 (p5-f1)` 4 rows with qualified units/comparators, footnote-size but readable, no row orphan. PASS.
- p-14 (P5 cont./P6 start): Ming/Eleven prose + code? No code here, P6 header + `協調開示` prose. Page break mid-P5→P6 clean, no orphan heading. PASS.
- p-15 (P6): Five-stage list + figure `協調開示の五段階` (blue box, stages 1-5 + Daybreak/checker outside + CVE note), reading note. Figure not split. PASS.
- p-16 (P6 end/P7 start): Securing prose + P7 header + tables `手順×来歴×限界 (Bio)` + start of `言語別デルタ (p7-f1)`. Tables paginated safely (no mid-row split). PASS.
- p-17 (P7 cont.): Rest of `p7-f1` (COBOL 10.9→72.1 + 40%超 prevalence separate + OCaml/Fortran/VB/effort/cost) + `bench×分母 (Low-resource)` + blind-evaluation prose. 40%+ and accuracy kept distinct. PASS.
- p-18 (P7 end/P8 start + Decisions JSON): P7 reading note + P8 header + Decisions prose + JSON request/response `verbatim` (2 blocks). JSON braces aligned, no line truncation. PASS.
- p-19 (P8 cont.): TanStack/NVIDIA prose + tables `安定核 vs harness (p8-f2)` (GH 15:18:14Z vs npm 15:21:49Z separate) + `API×移行×約款` + `重み vs API`. Registry/GH separation explicit. PASS.
- p-20 (P8 end + recap): DeepSeek prose + `今週の総括` heading + first 3 of 5 paragraphs. P8→recap continuity mid-page, no orphan, recap labeled standalone (not P9). PASS.
- p-21 (recap cont. + bibliography start): Recap paras 4-5 + `出典一覧と確認水準` + bibitems 1..~28. URLs break via xurl, no overfull. PASS.
- p-22 (bibliography tail): Remaining bibitems (~8) + end footer `--- NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF NOT A PUBLICATION PREVIEW ---`. Page is sparse (near-empty) but expected for bibliography tail; not a readability defect. No missing source note; order preserved. PASS with note.

## Table/figure/code checks (all pages)

- 20 tables: all `table[htbp]` centered, `\footnotesize`, `tabularx 0.96\linewidth`, `booktabs` rules, captions attached, no width overrun, no font-size too small (9-10pt effective), no broken Japanese glyphs, row cohesion kept (no mid-row page split observed).
- 3 figures: blue `tcolorbox` titles correct, body wraps, no float drift, captions not detached.
- Code/URLs: `verbatim` blocks intact, `\url` breaks correctly (0 Overfull final), SHA hex via `\url` breaks, no truncated lines.
- Cross-page: No word/sentence mid-break issues (Japanese LuaTeX-ja handles); headings not orphaned; P8→recap flows mid-page p-20; bibliography starts p-21 after recap, no interleaving.
- Bibliography: 36 entries, page split p-21 (dense) / p-22 (tail). Body-vs-bib split: body/front 20 pages (p-01..p-20), bib 2 pages (p-21..p-22). Honest density.

## Fixed errors

- v1: 4× `Illegal unit of measure` from figure `\\[2 …]` → fixed to `\par` line breaks. 1× Overfull 68pt from bare URL + SHA → fixed via URL trailing-punct trim + hex `\url`. Final: 0 warnings. No content change, only breakability.

No critical readability/layout defects. Near-empty p-22 is bibliography tail, not padding. Ready for Sol visual review.
