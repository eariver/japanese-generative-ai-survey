# W41 publication preparation log r17 (editorial proof, not a Candidate)

Date: 2026-10-14 JST
Authority: `SOL_W41_R16_INDEPENDENT_AUDIT_ACCEPTED / BOUNDED_READER_ACCURACY_REPAIR`
Profile: `WEEKLY + WEEKLY_MAGAZINE` (generic path)
Primary source: `surveys/weekly/2026-W41/main.tex` (UNAPPROVED_EDITORIAL_PROOF)
State: `DRAFT_COMPLETE` (unchanged); Publication Preview: `pending` (unchanged)

## Inputs

- r17 proposals v17.0 (P1 prompt-length 4 blocks; P2–P6 carried) + synthesis
  input/output + preview (67p, 5 tables, fidelity 6/6).
- Architecture (27/42) + approval; Grok/X ledger (14/12/2 OFFICIAL), DailyX raw,
  accepted Evidence (36 tasks), S17 supplement (prompt-length/5m-1h + Gemini
  identity + locator checks; r16 supplement preserved).
- r16 proof (17 pp.) as layout baseline.

## Repairs applied (M-01/M-02/m-01/m-02/m-03)

- M-01: unified `Prompt ≤100k / >100k tokens` headings + per-request Japanese
  phrasing in P1/TeX/table/synthesis/bib-note; 5m vs 1h verified (1h excluded
  from prose); numbers unchanged; table-vs-bill distinct; no guessed examples.
- M-02: 6 official titles fixed (re-fetched) + Gemini URL replaced (old 404 →
  new verified Cloud article; separate-material ruling; P2 unchanged) +
  locator honesty (category/permalink, listing/fragment, novasonic fetch limit).
- m-01: communitynote冒頭 ledger-scoped (FULFILLED_WITH_SAMPLING_LIMIT in body+QA).
- m-02: permalink/fragment check (no inventions; see supplement S17-3).
- m-03: `main.tex` header comment → r17 provenance (no body revision numbers).

## Method

- r16 records preserved (no overwrite). No canonical overwrite; no checkpoint
  regen; no semantic-renderer forcing. Bib titles caused no body regeneration.
- Manifest regenerated in place (file `09dd6633…`→`87bf7055…`, digest
  `6e65d09a…`→`5f2286a8…`; Git-tracked) and revalidated (27/27, lint clean).
- PDF rebuilt from exact bound bytes (17 pp.; `d1d1ed5…`→`39beecfd…`).
- Visual proof: all pages rendered from same-SHA PDF into
  `publication/v2/visual-proof-r17/` with render-index (see Phase H).

## Outputs

- `sources/2026-W41/execution/editorial-revision-r17/` (8 files) + session/index.
- `sources/2026-W41/publication/v2/`: manifest, requirements/coverage r17,
  reader-qa/preflight/pdf-qa/prep-log r17, bib + community audits, visual proof.
- `surveys/weekly/2026-W41/`: revised TeX + bib (+ledger unchanged) + r17 PDF/SHA.
- No semantic/gate PASS, no Human decision, no Candidate, no Freeze/Release/merge.

(End of file)
