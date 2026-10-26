# W43 r5 build commands and integrity notes

Start `6f79350a…` verified (parent `52224fa2…`, diff contract only; main/frozen 6-way PASS).

## Commands (exit codes)

- `print-fidelity-check-r5.py --mode clean` → `PRINT_SEMANTIC_PASS`, 24 checks, exit 0.
- `print-fidelity-check-r5.py --mode negatives` → `NEGATIVES_PASS`, 23/23 same-entrypoint with specific causes, exit 0.
- `source-key-classify-r4.py` (copied as method reference) → 19/1/13/2/1/0, ORPHAN 0.
- `input-identity` recomputation → 6/6 SHA256 match (`input-identity-r5.json`).
- `pdftotext` protected-string verification on local r3 bytes → all present (POST, TanStack keys, qualifiers, clocks, recap).
- No TeX/PDF rebuild (r3 print intentionally fixed); `git status` clean except r5 namespace + handoff + session + index.

## Defects closed vs r4 (integrity, not print)

- R5-FID-01: TeX parsed to ordered rows AND cells (unescaped `&`, `\%`, `\_`, braces, `\url`); per-cell normalized src/proj/TeX comparison with explicit TOKEN_SUBS allowlist; trailing generator padding stripped + asserted empty; per-claim own-row value+variant+quals in correct TeX row visible span + per-claim bib URL. Clean run caught 3 padding rows during development (documented, resolved honestly).
- R5-FID-02: `hashlib.sha256(actual bytes)` for all 6 inputs; disk vs ephemeral distinguished; hash-corrupted baseline fails `HASH_MISMATCH`; text mutants go through common validator.
- R5-FID-03: programmatic visible-span key count; 13 natural + 2 further carry exact quote/span evidence and `CURATED_REVIEW_REQUIRED` flags; no invented links; 404/RAW never validate claims.
- Names match coverage; no `or True`, no count-only, no `ANY_FAIL`.

## Content changes: NONE to print

r1/r2/r3/r3.5, Architecture/Selection/Evidence/State/Gates/main/Frozen unchanged. A reader-visible print error would have STOP-BLOCKED with position/impact (none found). No new article, no canonical PDF, no Stage/Freeze/Release. `.aux`-type byproducts: none (validator-only run).
