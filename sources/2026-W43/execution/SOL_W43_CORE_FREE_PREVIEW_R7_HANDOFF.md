# SOL_W43_CORE_FREE_PREVIEW_R7_HANDOFF (Muse worker → editorial Sol)

Terminal: `MUSE_W43_R7_TWO_COLUMN_READER_META_PDF_READY_FOR_INDEPENDENT_REAUDIT`
Date: 2026-10-27 JST. Branch: existing ONLY `weekly/2026-W43-v2-work`
(no new branch/Stage/Freeze/Release/merge; commit left for Human Commit Point).

## Start guard (exact, fail-closed)

- Post-contract HEAD/Tree at start: `794824f68…` / `a0b43a8d…` (FF-only from
  local `d8e21b8fe…`; remote re-verified: W43 `794824f68`/`a0b43a8d`,
  main `041a08df`/`a134dc36`, frozen `774dd39a`/`cd46a6f7a` — 6-way PASS,
  Drive report unreachable 401 → contract transcription applied, never
  claimed as read).

## P1 fixes delivered

1. **Two-column restored**: W42 segmented multicols adopted (32 segments,
   7mm gutter, A4/10pt/18mm unchanged); 20 tables + 5 code + 3 figures
   full-width outside columns; bib two-column; TOC regenerated sans P-prefix.
   New PDF 22p (repagination honest, NOT fixed at 22).
2. **Reader meta closed**: 23-pair whitelist, 0 visible leaks (TeX parse +
   PDF readback, all pages); scientific qualifiers kept (counts recorded);
   proof layer separate (cover mark p01 + footer p22 + PDF metadata).

## Evidence (all under `sources/2026-W43/execution/core-free-preview-r7/`)

`main.tex` (`9791a545…`, 97572 B), `preview.sty` (`0199d86d…`),
`main.pdf` (`5d01f496…`, 487514 B, 22p), `main.log`, `pages/` (22 PNG +
3 sheets), `meta-scan-r7.md`, `meta-change-ledger-r7.json` (23),
`layout-design-vs-W42-r7.md`, `new-physical-page-qa-r7.md` (22/22 sheets +
11/22 full-res + text layer), `pdf-link-font-qa-r7.md` (+raw JSON: 28 http,
0 malformed, 14 fonts), `r7-reader-surface-semantic-join.py`
(R7_READER_SURFACE_PASS 18/18 + NEGATIVES_PASS 9/9),
`portable-independent-replay-r7.md`, r6 replay witnesses (clean CONFIRMED;
38-negatives not re-runnable — harness asserts r3 note),
`historical-pin-correction-r7.md` (r6 manifest typos superseded),
`architecture-31-versioned-reconciliation-r7.md` (no re-grade),
`reference-tier-status-r7.md` (15 stay CURATED), `build-manifest-r7.json`
(all SHA pre-commit audited), re-audit request PROPOSED (this handoff's
§“next”).

## Method incidents (repaired + documented, not hidden)

- r6 validator default `--out` overwrote 2 immutable r6 JSONs → restored
  (`git checkout --`, tree verified clean); re-ran isolated.
- r6 validator default `--test-tex` = r3 file → first replay falsely
  BLOCKED on S07c; re-ran with explicit r6 paths → CONFIRMED.

## Next

Independent Sol executes the PROPOSED re-audit (new full-page inspection +
replay + novel mutation) → Drive report → editorial Sol adjudication →
Human PDF Gate (PENDING). Native Draft stays BLOCKED. Architecture/
Selection/Evidence/State/Gates/main/Frozen Core/r1–r6 untouched.
