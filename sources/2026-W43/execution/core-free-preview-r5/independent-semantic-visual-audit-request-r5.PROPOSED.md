# W43 independent semantic + all-page visual audit request (r5 PROPOSED)

To: Independent Sol (read-only) + separate visual auditor. From: Muse Worker.
Basis: r5 `PRINT_SEMANTIC_PASS` (exit 0) + `NEGATIVES_PASS` 23/23 (exit 0); r3 print fixed at HEAD `3cdf2a01…` (PDF `d0fa8b56…` 483305B 22p).

## Pointers (verify after r5 push/readback)

- r5 validator + clean/negative JSONs (cause-coded), binding `row-cell-claim-binding-r5.md` (20/80/29), `input-identity-r5.json` (6/6 SHA match), span audit `citation-span-and-confidence-r5.md` (19/1/13/2/1/0, spans verified), key classifier script, readback/boundaries, visual request (this file), manifest, build notes.
- r3 print: PDF blob `4e016ab1…`, TeX blob `79a90d40…`, p-18 blob `22bfb2df…`, 22 PNGs + 3 sheets.

## Scope

1. Re-execute r5 clean + negatives; confirm same-entrypoint causes.
2. Semantic spot-check of anchored claims (COBOL 40%+ prevalence vs accuracy, GH vs npm clocks, MemT storage-only, Patch 5 stages, Voxtral units) in exact TeX rows.
3. All-page visual audit of r3 PDF with real binary/page access (tables, figures, code, URLs, bib, P8→recap→refs).
4. Confirm key accounting and GH≠npm / 404 / RAW guards.

If binary/page media inaccessible: report `PDF_VISUAL_AUDIT_BLOCKED`, not PASS. Human PDF review is a separate explicit decision. No Stage/Freeze/Release.
