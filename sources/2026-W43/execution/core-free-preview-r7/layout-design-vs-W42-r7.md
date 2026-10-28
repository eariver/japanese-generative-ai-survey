# W43 r7 layout design vs released W42 (Phase B record)

Reference (read-only, reviewed main `041a08df`/`a134dc36`):
- `surveys/weekly/2026-W42/main.tex` (97647 B), `surveys/weekly/2026-W42/preview.sty` (6132 B).
- r6 style is W42 style + one version-string line (diff verified); geometry
  identical: jlreq + LuaLaTeX, A4/10pt, `margin=18mm`, `\columnsep=7mm`.

## W42 proven geometry (adopted, not improvised)

- NO `twocolumn` class option. Segmented `\begin{multicols}{2}` /
  `\end{multicols}` around wide material (7 segments in W42 body + bib
  segment); full-width tables as `\needspace{…}` +
  `{\centering\footnotesize \captionof{table}{…} \begin{tabularx}{0.96\linewidth}…}`
  OUTSIDE multicols; resume columns after. Bibliography in two-column
  `multicols`. Reading-note `tcolorbox`es (breakable) stay INSIDE columns.
- r6 defect: `preview.sty` loads `multicol` + sets 7mm gutter, but r6
  `main.tex` contains ZERO `\begin{multicols}` → single-column regression.
  r7 installs the actual environments (preamble `multicol` + `capt-of` +
  gutter, as W42 ll.9–10).

## r7 segmentation (this build)

- 32 balanced `multicols{2}` segments; 20/20 tables converted
  `table`-float+`\caption` → inter-segment `\captionof` (order kept, bodies
  byte-identical, 80 rows / 307 nonempty cells verified); 3/3 figure
  `figure`-floats → full-width bare accent `tcolorbox`es (bodies identical);
  5/5 verbatim code blocks full-width outside columns (first-line example
  header whitelisted, rest identical); 8× `\bigskip\hrule\bigskip` section
  dividers full-width; gray `SurveyRule` reading notes stay in-column
  (breakable, as W42); cover + TOC single-column (TOC regenerated);
  bibliography two-column multicols (36 keys, URLs intact).
- Narrative share: P1–P8 section/subsection prose + 5-para recap entirely in
  two columns (≈ p03–p21 body); exceptions are cover, TOC, 20 full-width
  tables, 5 full-width code blocks, 3 full-width figure boxes, 8 full-width
  hrules, bib (two-column, so not an exception to two-column policy).
  No page is single-column body prose. No `multicols` blanket: nothing wide
  was squeezed into a column (validator `L-two-column` asserts all 8
  sections inside columns AND ≥20 full-width tables outside).

## Documented exceptions vs W42

1. **Bibliography entry without forced `\clearpage`.** W42 uses `\clearpage`
   before bib (float flush). First r7 build kept it → p21 left half-blank
   after repagination (recap ends mid-page). Since r7 has NO floats (all
   inter-segment), the flush is unnecessary; removed the forced break so bib
   heading flows onto p21 (build 2). Final: 22 pages, no underfilled body
   page; only normal final-page tail (p22 lower half after bib end + proof
   footer). Done as reasoned bounded need, not padding.
2. **Code blocks:** W42 has none; r7 places 5 verbatims full-width
   (`\needspace{8\baselineskip}`, `\footnotesize` wrapper) — same mechanism
   as W42 tables. No overflow (0 overfull/underfull, visual check p08/p18).
3. **Cover proof mark:** W42 (canonical release) has none; r7 (Core-free
   proof) adds a muted cover safety line + end footer + PDF metadata
   (protection requirement; visually separate from article).

## Legibility

150dpi full-page PNGs p-01–p-22 + 3 contact sheets; inspected 22/22 (record:
`new-physical-page-qa-r7.md`). No blank body pages, no broken URLs
(`pdf-link-font-qa-r7.md`: 28 unique http, 0 malformed), CJK subsets
embedded (14/14). Build: lualatex ×2, exit 0/0, 0 errors, 0 overfull/
underfull (`main.log` kept).
