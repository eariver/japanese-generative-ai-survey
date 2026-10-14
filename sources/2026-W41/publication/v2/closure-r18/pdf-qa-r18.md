# r18 PDF QA record (bounded: references page + pagination integrity)

Date: 2026-10-14 JST
Starting SHA: `8f02b42ec0a6dc793633d82dab38935807bdf732`
r17 PDF SHA (in history): `39beecfd0ac098bd4e4d493b7e634f271290a06d30e1771c0182f2a7a48c5d02`
PDF: `surveys/weekly/2026-W41/main.pdf` (17 pages, 446781 bytes)
SHA-256: `4fd1958ce7dea3b2c257c5abe1de96e14c7e66cfe0d9c35e884ae596819750ce`
Toolchain: LuaLaTeX (TeX Live 2026) + Biber 2.22
Status: `UNAPPROVED_EDITORIAL_PROOF`

## Build checks (all PASS)

1. 20/20 citation keys resolved (Biber clean; no undefined citations/refs).
2. Gemini Reference [7] shows the new title
   (`Google Cloud introduces the Gemini agent.`).
3. Gemini access date renders 10/14/2026.
4. Reader bibliography note carries no internal Evidence-management terms
   (`Evidence-bound`, `NOT_CANONICAL`, `Card claims` absent from PDF text).
5. P1–P6 body + 5 comparison tables byte-unchanged vs r17
   (working-tree TeX identical except `references.bib`; body text extraction
   spot-checked: prompt-length headings, sampling-limit note, synthesis).
6. `FINAL_SYNTHESIS` (Sec.8) + `WEEKLY_COMMUNITY_MOVEMENT` (Sec.7) unchanged.
7. Page count 17 (not forced), SHA-256 recomputed from exact bytes above.
8. Visual proof regenerated from these exact bytes
   (`visual-proof-r18/`, 17 PNGs + index + README; index SHA matches this SHA).

## Bounded visual check (r17 17/17 already independently PASSED)

- Focus pages re-rendered and inspected: references (new [7] title/date),
  pricing table (unchanged), community/synthesis transitions (unchanged),
  final bibliography page (no dropped entries, no URL overflow).
- Before/after page mapping: identical pagination (17 pp.); the bib change
  alters only reference [7]'s text block. No table/heading/body displacement,
  no new orphans, no missing final-page entries.
- Full re-render + byte/text consistency done; body re-evaluation not repeated
  (content declared unchanged and verified identical).

## Unresolved

- Independent visual review of THESE r18 bytes still required
  (`INDEPENDENT_VISUAL_PASS` not claimed).
