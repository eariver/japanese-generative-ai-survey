# Muse W43 Core-free Preview r4 worklog — 2026-10-27

Branch `weekly/2026-W43-v2-work`. Contract `sol-w43-core-free-preview-r4-print-checker-integrity-20261027.md`.
Worker claim: `MUSE_W43_R4_PRINT_QA_INTEGRITY_READY_FOR_SOL_RECHECK`.

## Guards

Remote 6-way PASS read-only (dispatch `e707379f…`/`08d6cfd0…` parent `3cdf2a01…`, diff contract only; main/frozen match). Local `3cdf2a01…` clean → ff-only → `e707379f…`.

## Validator integrity (defects A–D closed)

- A: `or True` removed; real ordered 80-row join (src→proj vs manifest, allowlisted subs, dup cleanup) + TeX caption/row identity + DATA/NOTE + uniqueness.
- B: 17 negatives via same `validate()` on ephemeral mutants with SPECIFIC causes (incl. single-side API deletion, count-held swap/dup, NOTE alter, model/metric/drop, bib URL). Old diff-only/BOTH-only gaps closed.
- C: programmatic 19/1/13/2/1/0 key audit (visible/machine/natural/further/unavailable/orphan); r3 18/15/2/1/0 corrected.
- D: honest names; global literals labeled supplement. Clean PASS (22, exit 0) + negatives PASS (17/17, exit 0).

## Print standing

r3 PDF/TeX/PNG bytes FIXED (no rebuild). Local SHA256 + pdftotext protected-string checks pass. Log/blob ≠ visual QA (boundaries doc). No new semantic loss found; else would have STOP-BLOCKED with discrepancy (none).

## Push/readback

Non-force commit + push + readback; scope = r4 namespace + handoff + session + index only.
Final HEAD: PENDING_AT_COMMIT; Tree: PENDING_AT_COMMIT.
r4 validator URL: PENDING_AT_COMMIT (`.../blob/<FINAL_HEAD>/sources/2026-W43/execution/core-free-preview-r4/print-semantic-fidelity-check-r4.py`).

No State/Core/Architecture/Selection/Evidence/Gates change. Stop at Sol recheck.
