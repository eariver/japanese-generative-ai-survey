# W42 r13 validation report (frozen validators + TeX proof + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition.

## Frozen CLI validations (all PASS, real receipts)
- `survey_drafting_v2_base.py draft-check` (canonical package × r13 proposal): P1–P7 all `{"passed": true, "errors": []}`.
- Proposal SHAs v13.0 REVISED (recorded at commit; 103 paras / 19,193 paragraph-only chars / 22,315 body chars / 7 tables / 7 notes):
  P1 d7887f24…(r12 base, kept+1), P2, P3, P4, P5, P6, P7 — exact SHAs in commit; per-chapter paragraph chars P1 2,925 / P2 2,628 / P3 3,732 / P4 2,835 / P5 2,292 / P6 2,722 / P7 2,059.
- `synthesis-input` built via frozen CLI from the 7 proposal pairs; proposed synthesis result written with verified-UTC `generated_at` (2026-10-17T18:2x:xxZ, cross-checked against `date -u` at build); `synthesis-check` `passed: true`.
- `validate_agent_state`: PASS (State untouched at DRAFT_COMPLETE).

## F01/F02 gates
- F01 RESOLVED: LFM publisher-terms level; Beam Apache full conditions (Built-with vs NOTICE/attribution/modified-file/patent/third-party); programmatic scan clean.
- F02 RESOLVED: 0 non-http URLs in 117 ledger rows; 4 bundle-sourced refs excluded from all proposal blocks; q5-08 editorial framing; Nipah non-use stance; accepted-context annotation split recorded, accepted bytes untouched.

## Reader preview fidelity
- `reader-preview-r13.PROPOSED.json/.md`: 103 paragraphs / 7 tables / 7 notes; zero CLAIM_BOUNDARY; zero machine-trace/Hangul/simplified ghosts; single documented exception (none remaining; SRFT retained as named method with ledger note).
- TeX body = preview block text verbatim; ONLY documented delta is appended `\cite{..}` markers + bibliography. Block→key crosswalk: ledger `direct_source_keys` + `bibliography-map-r13.json` (59 unique keys: 45 primary-vendor / 9 secondary / 4 paper / 1 independent).

## TeX/PDF proof (non-canonical, edition-local)
- `preview-r13/main.tex` (808 lines; 7 tables; 59-key bibliography with category tags) + `preview.sty` (verbatim W41 layout minus biblatex; documented).
- LuaLaTeX/TexLive2026, 4 runs to stable aux: `main.pdf` 19 pages, A4. Log: zero overfull/underfull hbox, zero missing CJK glyphs, zero undefined citations/refs after final runs; ONE overfull vbox (43.6pt, P7 `table*` float, p16) — visually verified whitespace-only placement artifact, flagged not hidden.
- 19 page PNGs @150dpi + 2 contact sheets committed with hashes; `review-pages-r13.md` renderable index with per-page density/cite/table checklist.
- Page verdict: 19 pages vs Architecture target 28 / max 30. Honest content at magazine density (W41 canonical: 17 pages; r12 proof: 16 pages). Gap is a Sol/Human planning decision (deepen vs amend plan), not padded. Partial pages p16 (table float gap) and p19 (bib tail) flagged.

## Canonical invariants (all preserved)
- `production-state.json`: DRAFT_COMPLETE, architecture approved, publication pending (SHA unchanged).
- Draft checkpoint `ARCHITECTURE_ESTABLISHED.json`, approval, review index, r1 record/snapshot: unchanged.
- Canonical Draft Results/Packages/Synthesis (v10.0): SHAs unchanged (read-only validator inputs).
- Accepted Evidence/Views/Materiality/Selection/Architecture: untouched. r11/r12 proposals preserved as history. No TeX in canonical paths; Publication Preview not started.

## Remaining explicit unknowns (not hidden)
- Nemotron draft length / greedy decoding condition: NOT in retained sources; no live report-PDF read performed — qualified, not asserted.
- METR three-tier internal structure beyond announcement text: not detailed.
- Independent reproduction of all vendor benchmarks: absent by design (LIMITED completeness stands).
