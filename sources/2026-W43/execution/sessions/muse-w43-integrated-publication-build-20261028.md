# Session — Muse W43 integrated publication build (canonical TeX/PDF + 7 authorities, 2026-10-28)

Contract §4–§5B. State at build: `DRAFT_COMPLETE` (trusted bridge run 40539057751, bot commit `ada687453`).

## 1. Reader-to-r8 mapping

`execution/reader-to-r8-content-mapping-w43-20261028.md` (scripted, `/tmp/opencode/w43_reader_map.py`):
8/8 headlines equal; deck key-phrases 4/4 (P1,P2,P3,P5,P8), 3/3 (P4), 4/4 P6; draft HEADING verbatim 4/4–5/5 except P7 2/3 (documented enrichment, not a gap claim);
distinctive terms 8/8–8/9; recap YES (5 paras); bibkeys 36/36; A/B/C caveats PRESENT;
native census 121 blocks (28H/62P/15T/8N/8CB) + synthesis ESTABLISHED v1.0.
Mapping is evidence of basis coverage, NOT a byte-equivalence claim.

## 2. Canonical TeX (faithful r8 rendering)

`surveys/weekly/2026-W43/main.tex` (97156B, SHA256 `3fa6ca3b…`) =
approved r8 TeX `4ed553e5…` with exactly 4 proof-mark line changes
(header comment, hypersetup subject/keywords, cover mark deleted, footer mark deleted);
verified `diff` shows only those 4 hunks. `preview.sty` byte-identical to r8 (`0199d86d…`).
W42 precedent followed (layout comments kept source-only; rendered PDF neutral).
Frozen surface scan `scan_tex_file`: 0 findings / 0 blocking.

## 3. Deterministic PDF

`surveys/weekly/2026-W43/main.pdf` (486967B, SHA256 `b09fd181…`, 22 A4 pages):
LuaHBTeX 1.24.0, `SOURCE_DATE_EPOCH=1793145600 FORCE_SOURCE_DATE=1`, 3 runs,
runs 2–3 byte-identical; 0 errors, 0 missing chars, 0 warnings, 2 benign
output-routine vbox pp14–15 (same locus as approved r8, visually clean).
Evidence `execution/publication-build-w43/`: 3 compiler stdouts, full TeX log,
22 r150 PNGs + 3 contact sheets, page ledger (all A4, chars 43128),
links/fonts (75 actions / 28 targets / 14 embedded / 0 malformed).

## 4. Seven formal authorities (all frozen builders/validators PASS)

- `publication/v2/reader-manuscript-v2.json` (`079e07ce…`, READER_FACING_AUTHORED):
  binds profile/architecture/Human-approval, primary source main.tex, sty +
  synthesis-result + mapping as supporting; 31/31 must-cover rows FULFILLED
  (author assertion per schema; versioned 20/11 grades NOT transplanted —
  judged by ARCHITECTURE_CONTENT_FIDELITY check); requirements
  FINAL_SYNTHESIS + WEEKLY_COMMUNITY_MOVEMENT.
- `publication/v2/deterministic/{pdf-preflight,subject-entity-property-binding,identifier-preservation}.json`
  (measured: 22p/486967B/b09fd181; 36/36 keys, 3 URL-less; 8/8 order).
- `publication/v2/quality-regression-bundle-v2.json` (PASS, 3 DETERMINISTIC).
- `publication/v2/semantic-editorial-review-v2.json` (11/11 PASS, worker-attributed,
  expected family asserted via frozen `_expected_review_checks`).
- `publication/v2/visual-review-v2.json` (2/2 PASS).
- `publication/v2/reader-surface-semantic-review-v2.json` (`0a584f2e…`,
  separate worker surface re-read pass, 4/4 incl. READER_PIPELINE_INDEPENDENCE).
- `publication/v2/reader-surface-gate-v2.json` (PASSED, 0 blocking).

Fixed r8 proof, accepted research, State, Gates, shared Core: untouched.
No Stage/Gate/Freeze/Release/merge. Next: commit+push, independent General
regression audit on exact bytes (PDF `b09fd181…`), then trusted ADVANCE #2.
