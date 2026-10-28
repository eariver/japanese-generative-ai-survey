# W43 r5 QA limitations and independent audit handoff

Validator: `print-fidelity-check-r5.py` — clean `PRINT_SEMANTIC_PASS` (exit 0), negatives `NEGATIVES_PASS` 23/23 via same entrypoint (exit 0). Results saved with cause codes; no `or True`, no count-only, no `ANY_FAIL`.

## What r5 proves (bounded)

- Real SHA256 identity of 6 inputs (`input-identity-r5.json`: all match).
- 80-row ordered src→proj→manifest join with explicit TOKEN_SUBS allowlist; TeX caption/row-count/cell-position identity (trailing generator padding stripped + verified empty); DATA 78 / NOTE 2; 80 unique row_ids.
- 29 claims anchored in own proj row AND correct TeX row visible cells (value+variant+qualifiers) with per-claim bib URL mapping.
- 3 figures identical; 5 recap paras identical; POST route in both artifacts; TanStack keys in print; URL hygiene (34 http, 0 malformed); qualifiers in both artifacts; 36 bibitems complete.
- 19/1/13/2/1/0 key accounting (programmatic visible-span count; 13 natural + 2 further marked CURATED_REVIEW_REQUIRED with span evidence).

## What r5 does NOT prove (limitations)

- No independent semantic re-audit of r3.5 source truth (r3.5 `PASS_WITH_LIMITATIONS` stands; R32-FULL-003 FIXED not reopened).
- No independent all-page visual QA: log/blob/`pdftotext`/PNG-readback existence ≠ visual inspection for layout defects. Muse inspected r3 PNGs locally (contact sheets + p-18/p-21 300dpi), but Sol must commission a **separate independent semantic + 22-page visual audit with real binary/page access**. On inaccessible media that auditor MUST report `PDF_VISUAL_AUDIT_BLOCKED`, never PASS.
- 22 pages vs 38 estimate carried over from r2 (Architecture notes: estimate not promise; no padding). 31 Architecture obligations remain at prior 20/11 baseline (worker-observed, not re-audited here).
- r3 print bytes intentionally FIXED by this contract; any newly discovered reader-visible corruption requires STOP + separate repair proposal (none found).

## Handoff

Independent Sol: re-run r5 invocations, spot-check anchored claims and key spans, then open the separate audits above. Human PDF review remains a separate explicit decision. No Stage/Freeze/Release/merge authorized.
