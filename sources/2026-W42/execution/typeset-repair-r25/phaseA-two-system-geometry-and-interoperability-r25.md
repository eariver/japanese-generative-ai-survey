# W42 r25 Phase A two-system geometry and interoperability

Date: 2026-10-18 JST. Status: Track A FAIL (caption orphan + missing rows, overfull 178pt); Track B PASS sample (atomic tables + tcolorbox, overfull 30pt minor, no splits). No Gate.

## Versions (actual, not assumed)

- LuaHBTeX 1.24.0 TeX Live 2026; multicol v2.0b preinstalled (tools); cuted v2.10 + capt-of v0.2 (installed r24 via tlmgr to local TinyTeX; shared preview.sty untouched).
- cuted source: full-width onecolumn inserts in twocolumn, spread/shrink options, stripsep; caveats floats/footnotes/right-column/output/multiple-strips. W42 zero `\footnote` (7 hits all `\footnotesize`) → footnote N/A; float caveat applicable.
- Logs/samples archived `diagnostic-r25/phaseA/` (TeX/PDF/log/7 PNGs total: Track A 4pp + Track B 3pp).

## Track A — measured page-aware strip (FAIL)

Content: verbatim P3 tail (MiniCPM/FLUX/Granite provision/`重みの公開…`) + Table3 (6 rows) + P4 heading + full P4 (Codex..Decider) + Table4 (Decider) + P5 heading/intro; twocolumn + `strip` + `\captionof` + needspace T3 24 / T4 26 baselines (caption ~2 + rows ~17-19 + safety; estimated from r24 rendered ~1/3 page heights).

Result: exit 0, 4pp, 2× Overfull `\vbox 178pt` (≈6cm). Table3 caption `表 1…重み…` alone at p02 bottom; rows Spark/Beam/Nemotron on p02 bottom (cut), Granite/MiniCPM/FLUX MISSING (neither p02 nor p03 — p03 top is P4 heading, no rows). Caption orphan + missing rows HARD FAIL (same class as r24 F24-02, despite measured needspace). needspace does NOT make strip atomic — output routine splits caption/grid regardless. Images `phaseA/trackA/pages/a-2.png` (caption + 3 rows, cut) vs `a-3.png` (P4 heading, no rows). Citations `[?]` undefined (no bib in sample; full resolves — artifact, not package FAIL). Conclusion: measured strip cannot keep 6-row tables indivisible near page bottom; Track A disqualified (geometry proof, not preference).

## Track B — multicol segmented (PASS sample)

Same verbatim content (P4 trimmed to Codex+Decider for brevity + tcolorbox note to prove compat; less bottom stress than Track A full P4 — noted, full-issue test stresses fully). Structure: NO `\twocolumn`; `\begin{multicols}{2}` segments separated by full-width `{\centering\footnotesize \captionof{table}… \begin{tabularx}…}` tables (no float, no strip); `\setlength{\columnsep}{7mm}` enforced same gutter; headings + tcolorbox INSIDE segments (12pt? Actually same sizes; headings in-column like twocolumn).

Result: exit 0, 3pp, 2× Overfull 30pt (minor, like r24 sample 25pt; no clipping observed). Table3 (`表 1…重み…`, 6 rows ALL present same b-2) + Table4 (`表 2…生産性…`, 6 rows incl Decider same b-3) atomic (caption+rows same page, no orphan, no footer collision). tcolorbox note renders inside multicols (compat proven for jlreq/luatexja/tabularx/tcolorbox/hyperref). Section headings render inside segments. Two-column preserved (not one-column fallback); column widths/gutter visually match twocolumn (same `\columnsep`, same fonts; full-issue QA confirms). Citations `[?]` sample-only (no bib). Images `phaseA/trackB/pages/b-2.png` (Table3 complete) vs `b-3.png` (Table4 complete + note + P5 heading). Conclusion: multicol architecture viable; proceed to Phase B full (which stresses full P4 + all 7 tables + bib + notes).

No third method needed (two genuine architectures compared; one passes sample). Never one-column fallback.

(End.)
