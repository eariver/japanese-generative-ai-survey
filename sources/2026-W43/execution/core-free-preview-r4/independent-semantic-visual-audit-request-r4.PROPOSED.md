# W43 independent semantic + visual audit request r4 (PROPOSED)

To: Independent Sol (read-only) + separate visual auditor. From: Muse Worker.
Worker verdict on checker integrity: honest PASS (clean `PRINT_SEMANTIC_PASS` exit 0; negatives `NEGATIVES_PASS` 17/17 exit 0). No r3 PDF/TeX content change by r4.

## Pointers (verify after r4 push/readback)

- r4 validator `print-semantic-fidelity-check-r4.py` + clean/negative result JSONs (exit codes recorded).
- r4 binding `claim-and-table-print-binding-r4.md` (20 tables / 80 rows / 29 anchored claims, failure cases).
- r4 key audit `source-key-audit-r4.md` (19/1/13/2/1/0, programmatic) + classifier script.
- r3 print artifacts (fixed): PDF `d0fa8b56…` 483305B 22p (blob `4e016ab1…`), TeX `bb0e7e1d…` (blob `79a90d40…`), 22 PNGs + 3 sheets (e.g., p-18 blob `22bfb2df…`), log 0 warnings.
- r3 fidelity/QA/carryover + r4 readback/boundaries doc (text-extraction checks vs visual-QA limits).

## Scope

1. Re-run r4 validator invocations; confirm same-entrypoint negatives fail for their stated causes.
2. Semantic spot-check of anchored claims (especially COBOL 40%+ prevalence vs accuracy, GH vs npm clocks, MemT storage-only, Patch 5 stages, Voxtral units) in print location.
3. All-page visual audit of r3 PDF with real binary/page access (tables, figures, code, URLs, bib, P8→recap→refs).
4. Confirm 19/1/13/2/1/0 key accounting and no orphan; GH≠npm and 404/RAW guards.

If binary/page media inaccessible: report `PDF_VISUAL_AUDIT_BLOCKED`, not PASS. Human PDF review remains a separate explicit decision; no Stage/Freeze/Release authorized.
