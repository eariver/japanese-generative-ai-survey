# W43 r3 physical page and table QA (22 pages)

PDF r3 `d0fa8b56…` 483305B 22p A4 LuaLaTeX 1.24.0, 0 Illegal/Overfull/Errors. Pages `p-01.png`..`p-22.png` (150dpi) + 3 contact sheets. Every page inspected; focus: POST restore (p-18), clean body URL (p-18), TanStack 典拠 line (p-19 table), bib completeness (p-21/22).

## Per-page

- p-01 cover, p-02 TOC: unchanged from r2 (neutral, no intrusive stamp). PASS.
- p-03..p-17 (P1–P7 + tables/figs/code): identical rendering to r2 (body changes outside this range except L480 dup cleanup on p-19-adjacent prose — verified no reflow defects via contact sheets 01-02). Tables full-width, fonts readable, glyphs correct, no clipping. PASS.
- p-18 (Decisions JSON + POST + URL): JSON verbatim intact; `読み方：POST /v1/decisions に…` restored in monospace (300dpi confirms); body URL blue link ends before `（観測…`; SHA wraps via nolinkurl; no overfull. PASS (F-R3-01/02 repaired).
- p-19 (TanStack tables + new 典拠 line): p8-f2 table now carries `典拠: 安定核=tanstack-gh…／npm=tanstack-npm…` in muted note, no row-count change, caption attached, no width overrun. Prose GH/npm separation intact. PASS.
- p-20 (recap): 5 paras after P8, not P9, mid-page continuity from P8 tables. PASS.
- p-21/22 (bib 36 complete): unchanged from r2 (transplanted block), dense but readable, URLs break, 0 truncation. p-22 tail sparse (expected). PASS.

## Tables/figures/code/URLs

- 20 tables / 3 figures / code blocks: same pagination as r2, no new splits. `\url` hygiene: 34 http links, 0 JP-in-URL. `\nolinkurl` SHA breaks, no false links.
- Cross-page: no orphan headings, P8→recap→refs order preserved.

No critical defects. Independent visual audit still required (worker does not claim it).
