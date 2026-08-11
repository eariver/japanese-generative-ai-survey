# SP-2026-M07 v0.5 Visual Review direction

This note records the human Visual Review request made on 2026-08-11 JST before the next immutable source revision is generated.

Requested changes:

1. Remove the text collision visible especially at the start of Chapter 2. The root cause is a long chapter heading being typeset inside a narrow two-column column.
2. Replace hard `twocolumn -> clearpage -> onecolumn` transitions. Narrative text should remain two-column, but the columns should be balanced at the end of the narrative so the following full-width synthesis can use the remaining page naturally when space permits.
3. Keep Theme Synthesis, Source-backed Technical Notes, wide tables, front matter, and references full-width.
4. Add a final reader-facing chapter that revisits all six chapters and discusses their structural relationships. This chapter may synthesize only Evidence already selected for the approved July Architecture; it must not introduce new external Evidence or imply unverified causality.
5. The final PDF remains subject to the existing 32-40 page budget, clean TeX-log gate, render-first Visual Review, Freeze gate, and explicit public Release approval.

The intended implementation is a balanced `multicols` narrative flow: each chapter heading is full-width, the narrative body is two-column, and the two columns are balanced before returning to full-width synthesis/notes. This preserves the Weekly-series visual identity without wasting a nearly empty page at each column-mode transition.
