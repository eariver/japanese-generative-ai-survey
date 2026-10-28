# SOL_W43_CORE_FREE_PREVIEW_R5_QA_HANDOFF

Status: `MUSE_W43_R5_PRINT_FIDELITY_QA_READY_FOR_INDEPENDENT_AUDIT`
Date: 2026-10-27. Branch: `weekly/2026-W43-v2-work` (existing only).
Sole contract: `sol-w43-core-free-preview-r5-tex-row-fidelity-and-hash-guard-20261027.md`

## 0. Guards (read-only PASS, ff-only)

- Dispatch `6f79350af14574d6398943ce12ccf0897bd8a02d` / `a6ac634aeffcf101d7284b17ce13edb03a33e86e` == origin; parent `52224fa2acf83d2f482e207b7bceebda077ba221` / `970d348c4f6a144d08d990457f2f27511f1b4f4e` (r4 per §0); diff = contract file only.
- main `041a08df…`/`a134dc36…`, frozen `774dd39a…`/`cd46a6f7a…` verified via API+ls-remote.
- Local `52224fa2…` clean → fetch + ff-only → `6f79350a…`. No reset/rebase/force/branch/PR/main/Core writes.

## 1. r4 gaps closed (QA integrity; print bytes fixed)

- R5-FID-01: r5 validator parses TeX `tabularx` bodies to ordered rows AND cells (unescaped `&`, `\%`, `\_`, braces, `\url`/wrapping), maps each printed row to table-id+ordinal+manifest row-id+DATA/NOTE, and compares NORMALIZED per-cell src/proj/TeX with bounded TOKEN_SUBS allowlist (trailing generator padding stripped + asserted empty). All 29 claims asserted in their ONE target TeX row/cell (value+variant+qualifier facets + provider/unit/comparator + per-claim bib URL). Development run caught 3 padding rows; resolved honestly with explicit normalization (no silent pass).
- R5-FID-02: real `hashlib.sha256(actual bytes)` for 6 pinned inputs (`input-identity-r5.json` 6/6 match). Disk files vs ephemeral mutants distinguished explicitly; hash-corrupted baseline fails `HASH_MISMATCH`; text mutants run the common validator and fail their intended causes.
- R5-FID-03: programmatic visible-span key classification 19/1/13/2/1/0 (ORPHAN 0); r3 18/15/2/1/0 corrected. 13 natural + 2 further carry exact quote/span evidence with `CURATED_REVIEW_REQUIRED`; 404/RAW never validate claims; GH proves GH only.
- Clean `PRINT_SEMANTIC_PASS` (24 checks, exit 0); negatives `NEGATIVES_PASS` 23/23 same-entrypoint with specific causes (single-side API, TeX row swap/alter/claim-shift, count-held dup/swap, header/NOTE/model/metric/drop, bib URL, JP-URL, qualifiers, hash), exit 0. No `or True`, no count-only, no `ANY_FAIL`.

## 2. Outputs (NEW r5 namespace only; NO PDF rebuild)

`core-free-preview-r5/` (validator + clean/negative JSONs, classifier copy, row-cell-claim binding, input-identity, span audit, readback/boundaries, visual request, manifest, build notes) + this handoff + session + index append. r1/r2/r3, r3.5, Architecture/Selection/Evidence/State/Gates/main/Frozen unchanged. No canonical PDF, no Stage/Freeze/Release. No `.aux`-type byproducts.

## 3. Standing print + boundaries

r3 PDF `d0fa8b56…` 483305B 22p (blob `4e016ab1…`), TeX `bb0e7e1d…` (blob `79a90d40…`), 22 PNGs + 3 sheets; local SHA256 + `pdftotext` protected-string checks pass. Log/blob/text ≠ all-page visual QA (boundaries doc). Separate independent semantic + 22-page visual audit still required; on inaccessible media report `PDF_VISUAL_AUDIT_BLOCKED`.

Final HEAD/Tree via push/readback (handoff cannot self-contain hash). Commit-pinned file URLs in session/final report post-push.

`MUSE_W43_R5_PRINT_FIDELITY_QA_READY_FOR_INDEPENDENT_AUDIT`
