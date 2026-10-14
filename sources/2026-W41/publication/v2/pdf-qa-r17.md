# W41 editorial-proof PDF QA r17 (technical + layout, all pages)

Date: 2026-10-14 JST
PDF: `surveys/weekly/2026-W41/main.pdf` (17 pages, 446795 bytes)
SHA-256: `39beecfd0ac098bd4e4d493b7e634f271290a06d30e1771c0182f2a7a48c5d02`
(r16 PDF `d1d1ed5d4f6…` remains in Git history; r17 is the new unapproved proof.)
Toolchain: LuaLaTeX (TeX Live 2026) + Biber 2.22
Status: `UNAPPROVED_EDITORIAL_PROOF` (independent semantic/visual audit required)

## Technical fidelity (r17 → PDF)

- Body loss: none (fragment check 6/6; 38065 extracted chars).
- 5 tables with captions verified (表1 frontier/pricing with Prompt ≤/>100k
  headings, 表2 7-item availability, 表3 synonym triple, 表4 Astra quality,
  表5 provenance scope).
- Numbers unchanged from S1 (Input $0.10/$0.50, Output $0.50/$2.50, Cache read
  $0.01/$0.05, 5m write $0.125/$0.625; Sonnet $0.20→$0.10); 1h values absent
  from prose; bill-vs-estimate distinct; no guessed examples.
- Section numbering: Sec7 Community + Sec8 Synthesis (TOC matches TeX order).
- Sampling limit present in reader note; fixed bib titles render ([2]–[20]
  spot-checked); Biber 20/20 resolved; no undefined citations.

## Visual QA (all 17 pages rendered as images + text)

- Tables: no boundary splits; prompt-length headings render (`≤`/`>` via math).
- Characters: no tofu/garbling (fonts embedded); `%`/`$`/math render correctly.
- Headings: no isolated lone headings; community/synthesis transitions carry text.
- Blank pages: none fully blank (p.14 end-of-articles whitespace retained,
  complete subsection, documented since r15).
- Footnotes/references: no overflow (pp.16–17 clean; URLs break via xurl).
- Cover/TOC/numbers: consistent (Contents 7 Community / 8 Week in Review).
- Log: no undefined refs; Biber clean; one 0.29pt overfull (negligible).

## Fixes vs r16

- M-01 prompt-length headings + per-request phrasing (numbers unchanged);
  m-01 ledger-scoped note; m-03 provenance comment; M-02 bib titles/URL +
  P2-untouched identity ruling; locator honesty kept. Manifest rebuilt +
  revalidated per change; PDF rebuilt from exact bound bytes; SHA regenerated.

## Remaining visual-review condition

- INDEPENDENT_VISUAL_PASS not claimed. Page renders committed under
  `publication/v2/visual-proof-r17/` (same-SHA source) for the auditor.

## Invariance

- No Architecture/Evidence/State/checkpoint/approval changes; no Candidate;
  no semantic/visual/gate PASS fabricated; Preview `pending`.

(End of file)
