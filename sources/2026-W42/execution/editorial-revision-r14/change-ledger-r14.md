# W42 r14 change ledger (external audit M01–M06/m01–m05 + P0–P2 findings closure)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-18 JST. Old: r13 v13.0 (103 paras / 19,193 paragraph-only chars). New: r14 v14.0 (112 paras / 20,479 paragraph-only chars; body 23,601). Deltas r13→r14: **+9 paras / +1,286 paragraph chars** (r12→r13 was +11/+1,028; r11→r13 +21/+2,189 — definitions reconciled in validation report).

## P0 — layout/artifact repairs
- PDF-01 (p16 float-only page): root-cause fix — all 7 comparison tables moved to in-flow position right after each chapter's 2nd paragraph (no new float package available in this transport; placement strategy instead); chapter-end URL boxes removed entirely (CITE-03), reducing float pressure. P7 table now lands on p15 with its closing paragraph. No stranded float-only page remains (p15 carries table + closing + cites; flagged as chapter-end partial, not a defect).
- PDF-02 (p19 2-entry orphan bib tail): bibliography tightened (`\footnotesize`, `\itemsep 2pt`, `\parsep 0pt`); all 59 unique-URL entries kept (no entry discarded). Tail now carries the marker + closing entries on a shared page; documented as normal bibliography tail.
- PDF-03 (main.log absent): root cause = repo `.gitignore` excludes `*.log`; r13 never force-added it. Fix: `git add -f` the actual complete log + remote blob read-back verification in this unit. Historic r13 log is NOT fabricated.
- PDF-04 (808 vs 820 lines): reconciled — `wc -l main.tex` counts physical lines (744 for r14; r13 file recounts to its own value in report); "logical lines" was an undefined informal count. Procedure documented; no content claim rests on it.

## P1 — substantive repairs
- TECH-02 (Earth 4×2): three new P6 blocks from S2 live paper read (4 configs × 2 models + cost; tool-vs-plan split with search/EE behavior; golden workflows + autorater validation + unreconciled + saturation + releases). Flash-vs-Pro confound, 3-repeat mean±std, failure-inclusive cost all stated.
- CITE-02: P1 s1-02 (15 refs) split into Wonder/Argon blocks; all 7 tables get per-row ledger entries with row→discovery→URL mapping; TeX tables carry per-row `\cite` in last cell; chapter boxes removed (were redundant with inline cites + one bibliography).
- EDIT-01: counter definitions fixed and scripted — paragraph-only / body(PTN) / all-text reported separately per revision (see validation report). No quota claimed.
- Depth gap: +9 paras net (P1 +1 ray-tracer, P2 +1 sealed-eval, P3 +2 Table-8/MOPD, P4 +2 Codex/Max-gates, P5 +1 durability, P6 +3 config/split/rounds minus 2 merged/dropped, P7 +1 Vals-design minus 1 dup). Shortfall vs 28pp reported honestly (17 pages; see manifest).

## P2 — targeted
- TECH-01: SPEED-Bench split + draft length 7 + greedy 4.287→4.718 + sampled 3.787→4.612 ALL verified from S3a/S3b first-party pages (sidecar recorded); cross-model honesty kept (sampled best vs greedy others); MOPD shares + dashed agentic edge marked unconfirmed.
- TECH-03: aptamer rounds vs 8-clone confirmation kept separated; round populations/criteria stated from card + excerpt limits.
- CITE-03: chapter-end URL boxes removed; one end bibliography (59 unique URLs, category-tagged) + inline per-row cites.
- EDIT-02: OpenRouter/API dup (P7 s7-08) merged away; Rosalind dup (P6 s6-12) removed (coverage via table row); generic closings (P1/P2/P5/P7) rewritten grounded.
- EDIT-03: `accepted_context_notes` literal removed from reader surface (rephrased); metadata stays in ledger sidecar.
- EDIT-04: cover deck `専門身体` → `専門・身体の各分野`; tables land in-chapter (verified p3–p15, no wrong-chapter floats observed).

## Held gates (no regression)
F01 (LFM publisher-terms level; Beam Apache full conditions), F02 (100% http URLs, bundle refs excluded), M01 (acceptance length), M02 (denominator separation), M06 (timestamp notice stands). MarkTechPost/OpenRouter/HF-API/X remain SECONDARY, never primary. No EXO scores, no AA ranks, no X-only allegations.
