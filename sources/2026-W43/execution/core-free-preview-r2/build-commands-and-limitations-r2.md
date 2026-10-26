# W43 r2 build commands and limitations

Starting HEAD `192fbb14…` verified (parent `071016d0…`, diff contract only; main/frozen 6-way PASS).
r3.5 SHAs pinned exact; checker exit 0 PASS.

## Commands (exit 0)

- `lualatex …/core-free-preview-r2/main.tex` x2 → 22 pages, 0 Illegal/Overfull/Errors, 483473B.
- `pdftoppm -png -r 150 …/main.pdf …/pages/p` → 22 PNGs.
- PIL contact sheets x3 → batches 8/8/6.
- `pdfinfo` → Title neutral, Subject/Keywords `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`, LuaLaTeX 1.24.0, 22p A4.
- r3.5 checker → `EDITION_LOCAL_ROW_JOIN_PASS`, 24/24 negatives.

## r1 -> r2 fix

- Bibliography 36 entries rebuilt from crosswalk as complete sentences; r1 60-char cuts eliminated (`速度で]`, `Small/Re]`, `=IMP]`, `upstream validat]`, `別ソ]`, `no post-cutoff]` gone).
- TanStack GH proves GH only; npm separate RAW_NOT_ARCHIVED scoped; post-cutoff guides guarded.
- Body/projection identical to r1 (SHA `e1a49da9…`); TeX change is bib block + sty comment only (+3244B, pages unchanged 22).

## Limitations / volume

- 22p = cover1/TOC1/body18/bib2 honest. 38 target/44 max/37 estimate vs actual: concise 71KB approved prose, 62 paras, 20 tables; Architecture note says estimate not guarantee, padding forbidden. All 31 must-cover visible (20/11 preserved). Worker does NOT claim 31/31 re-audit; Sol adjudicates READY vs VOLUME_OR_LAYOUT_REVIEW_REQUIRED.
- Residuals unchanged from r1 (no independent rerun, raw snapshots unavailable, etc.).
- Edition-local only; State/Core/Architecture/Selection/Evidence/Gates/main/Frozen untouched; no Stage/Freeze/Release. `.aux/.toc/.out` excluded; `main.log` force-added (gitignore `*.log` overridden for required artifact, W42 precedent).
