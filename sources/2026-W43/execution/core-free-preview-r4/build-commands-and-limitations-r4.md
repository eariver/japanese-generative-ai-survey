# W43 r4 build commands and integrity notes

Start `e707379f…` verified (parent `3cdf2a01…`, diff contract only; main/frozen 6-way PASS).

## Toolchain (exit codes)

- `print-semantic-fidelity-check-r4.py --mode clean` → `PRINT_SEMANTIC_PASS`, 22 checks, exit 0.
- `print-semantic-fidelity-check-r4.py --mode negatives` → `NEGATIVES_PASS`, 17/17 true negatives via SAME `validate()`, exit 0.
- `source-key-classify-r4.py` → 19/1/13/2/1/0, ORPHAN 0 (programmatic; r3 18/15/2/1/0 corrected: tanstack-gh/npm now EXACT, recap MACHINE_ONLY).
- `pdftotext` extraction on local r3 PDF bytes → protected strings present (POST x1, tanstack keys x2/x2, qualifiers, clocks, recap).
- No TeX rebuild (r3 PDF/TeX intentionally fixed); `git status` clean except r4 namespace + handoff + session + index.

## Defects fixed in the validator (not in print)

- A: removed `or True` tautology; real 80-row ordered join src→proj→manifest with allowlisted TOKEN_SUBS + path rule + dup cleanup, plus per-table TeX caption/row-count identity and row-anchored claim checks.
- B: all 17 negatives execute the same `validate()` on ephemeral mutants and assert the SPECIFIC cause (API_MISSING_PROJ/TEX, ROW_ALTERED, HEADER_ORDER, CLAIM_ANCHOR, URL_*, QUAL_*, TEX_ROW_COUNT, BIB_*); single-side deletions now caught (r3 `neg()` required BOTH).
- C: key audit recomputed from reader-visible spans (comments/labels stripped); one exclusive class per key; no double counting.
- D: check names match actual coverage (literals kept as explicitly-labeled global supplement, not anchoring proof).

## Content changes: NONE to print

r1/r2/r3 preview bytes, r3.5 reader/ledger/manifest/checker, Architecture/Selection/Evidence/State/Gates/main/Frozen untouched. No new article, no canonical PDF, no Stage/Freeze/Release. A reader-visible print error found by the strengthened checks would STOP with discrepancy (none found; clean PASS).
