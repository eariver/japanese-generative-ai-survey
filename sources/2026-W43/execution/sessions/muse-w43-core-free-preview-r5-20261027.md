# Muse W43 Core-free Preview r5 worklog — 2026-10-27

Branch `weekly/2026-W43-v2-work`. Contract `sol-w43-core-free-preview-r5-tex-row-fidelity-and-hash-guard-20261027.md`.
Worker claim: `MUSE_W43_R5_PRINT_FIDELITY_QA_READY_FOR_INDEPENDENT_AUDIT`.

## Guards

Remote 6-way PASS read-only (dispatch `6f79350a…`/`a6ac634a…` parent `52224fa2…`, diff contract only; main/frozen match). Local `52224fa2…` clean → ff-only → `6f79350a…`.

## Integrity repairs (validator + accounting; print fixed)

- FID-01: TeX cell-level join (ordered rows+cells, escapes/urls/wrapping), per-cell normalized src/proj/TeX, per-claim own-row value+variant+quals in correct TeX span + bib URL. 3 padding rows found+resolved during development.
- FID-02: real SHA256 of 6 inputs (6/6 match); disk vs ephemeral explicit; hash mutant → HASH_MISMATCH.
- FID-03: programmatic 19/1/13/2/1/0 with span evidence; natural+further flagged CURATED_REVIEW_REQUIRED.
- Clean PASS (24, exit 0); negatives PASS (23/23 same-entrypoint, exit 0).

## Print standing

r3 PDF/TeX/PNG bytes FIXED (no rebuild). Local SHA256 + pdftotext protected strings pass. Log/blob/text ≠ visual QA. No new print defect found; else would have STOP-BLOCKED.

## Push/readback

Non-force commit + push + readback; scope = r5 namespace + handoff + session + index only.
Final HEAD: PENDING_AT_COMMIT; Tree: PENDING_AT_COMMIT.
r5 validator URL: PENDING_AT_COMMIT (`.../blob/<FINAL_HEAD>/sources/2026-W43/execution/core-free-preview-r5/print-fidelity-check-r5.py`).

No State/Core/Architecture/Selection/Evidence/Gates change. Stop at independent audit.
