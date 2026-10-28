# J-GAS 2026-W43 — Independent Sol audit: r5 print fidelity + fixed r3 PDF all-page visual

Date: 2026-10-27 JST.
Status: `INDEPENDENT_SOL_READ_ONLY_AUDIT_REQUEST / INDEPENDENT_R35_SOURCE_CLOSED / R5_PRINT_PENDING / HUMAN_PDF_GATE_PENDING`.
Repository: `eariver/japanese-generative-ai-survey`.
Audience: **separate independent Sol audit session**, NOT editorial Sol, NOT Muse Worker.

## 0. Immutable targets and read-only boundary

Audit **fixed r5 QA commit** (this request is committed AFTER its subject):
- Existing work branch: `weekly/2026-W43-v2-work`.
- **Exact r5 subject HEAD**: `fa1caaedb6f2b09a6d8e1f77a505d363ca6d0c31`.
- **Exact r5 subject Root Tree**: `4576f190346da02c1937778e459eb0391fbf6430`.
- r5 parent/dispatch `6f79350af14574d6398943ce12ccf0897bd8a02d`; r5 diff = one normal FF commit, 15 paths all edition-local W43 execution.
- The remote W43 branch may point ONE COMMIT LATER because editorial Sol committed this audit request. The auditor must **fetch and audit the immutable subject commit above** and NOT silently substitute current tip or replay another revision. Record actual branch tip separately and verify exact commit/tree objects before analysis.
- Protected main: HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
- Protected Frozen `production/survey-core-v2`: HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- **Fixed print subject: r3 commit** `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`, Root Tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73`.
- PDF path at r3: `sources/2026-W43/execution/core-free-preview-r3/main.pdf`; **raw SHA-256** `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`; **Git blob SHA** `4e016ab1e2beec8b4063778226e0404184ffcbc3`; 483305 bytes, 22 A4 pages.
- Fixed r3 TeX raw SHA-256 `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`, Git blob `79a90d4098a4b87605588d6cc57c7e785062d6d9`.
- r3 PNG path prefix `sources/2026-W43/execution/core-free-preview-r3/pages/`, p-01.png…p-22.png plus three `contact-sheet-*.png` (p-18 known blob `22bfb2df64a574b8fcacf40fc992b2298af7b470`). Audit actual image **bytes**, not filename existence only.

**Completely read-only**: no GitHub commit/issue/PR, no file updates, no branch, no Core execution, no State/Gate mutation. Only write the external independent report to Google Drive folder `GPT-Sol_Review` using `yyyyMMddHHmmss_SolReview.md`; never write an audit "PASS" into repo. If unable to write Drive, return full report and honestly declare Drive failure, without claiming saved.

## 1. Prior decisions, which must NOT be inflated

- Independent r3.5 reader/content audit `20261026231458_SolReview.md` concluded `PASS_WITH_LIMITATIONS`, P0=0/P1=0, last original P1 `R32-FULL-003=FIXED`, with primary raw/nonarchived caveats. This is separate authority, not proof of r3 PDF or r5 checker.
- Editorial Sol accepted r3 print fixes: restored literal `POST /v1/decisions`, clean official guide `https://developers.openai.com/api/docs/guides/decisions` without Japanese parenthetical inside hyperlink, complete 36-item bibliography, separate GitHub release and scoped npm clocks, original 20 tables/80 physical rows/29 claims.
- Muse r4 had defects: r4 `V04` counted TeX rows but did not check each TeX cell; r4 `V05` looked for claims anywhere in a table not the own row; r4 `V00-inputs-pinned` unconditionally returned `True`. r5 purports to close these.
- Muse r5 reports clean `PRINT_SEMANTIC_PASS` 22 checks and `NEGATIVES_PASS` **23/23** from same entrypoint, true raw-byte SHA256 6/6 and 19/1/13/2/1/0 bibliography classifications. **These are claims to challenge independently**, not audit verdicts.
- r3 PDF unchanged by r4/r5. Core native Draft is BLOCKED and Frozen Core v2 immutable. W43 architecture accepted r6, 31 must-cover historically `20 SUBSTANTIVE_COMPLETE/11 PARTIAL`. Human asked five-paragraph `今週の総括` after P8; reader 8 packages P1–P8, 19 selected (12 primary + 7 supporting). Page plan target ~38, max 44, page-count estimate `NOT A GUARANTEE` and no padding. Actual PDF 22 (cover 1/TOC 1/body and recap 18/bibliography 2); this discrepancy requires **editorial reasoning**, not a forced 38 pages or automatic blocker based only on count.
- **No official Publication Preview Gate decision, no formal Draft validation, no Freeze or Release**, irrespective of findings.

## 2. Mandatory independent read order

1. This contract, verify **exact** r5 HEAD/root Tree and the **separate** r3 print subject HEAD/root Tree; check all 15 r5 changed paths and protected references with remote commit metadata. Document limits of remote fetch and PDF access.
2. Read complete `sources/2026-W43/execution/core-free-preview-r5/print-fidelity-check-r5.py` (not just self-reported PASS); `print-fidelity-check-r5.result.json`, `print-fidelity-check-r5.negatives.json`, `input-identity-r5.json`, `row-cell-claim-binding-r5.md`, `citation-span-and-confidence-r5.md`, `source-key-audit-r5.md`, `r5-QA-limitations-and-independent-audit-handoff.md`, and Muse handoff.
3. At immutable r3: exact `main.tex`, `main.pdf`, actual page PNGs and contact sheets, r3 print projection and original generator/visual QA reports; for correctness, compare against fixed r3.5 reader, ledger, physical-row manifest, `EXPECTED_CLAIMS` in original r3.5 strict checker, and r3.3 source crosswalk. Read W43 Architecture r6 `architecture-v2.json` and actual Human approval/Bypass governance records, State, and source tier caveats.
4. **Do not trust** r5 success text, PDF preview tooltip or git blob pointer as substitute for independent byte reading/test run. Never substitute a stale r3.4 or r3.5 audit report for THIS independent r5+PDF review.

## 3. Audit A — semantic correctness and QA implementation (independent adversarial)

- Recompute true raw SHA-256 from actual six file byte sequences: r3.5 reader `6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6`, ledger `6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4`, manifest `85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111`, r3 projection `63ad2617f663a01bd14a93b803a96272bf3cc72debbdf4817f81c6596eccbe80`, r3 TeX `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`, r3 PDF `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`. If a particular binary is inaccessible, say which checks cannot be performed, not PASS.
- **Independently invoke** r5 clean and negative modes with exact command/exit code/log (or reimplement checks without trusting saved JSON). Confirm 23 mutants each actually mutate intended input and fail for the expected specific reason, not arbitrary crash; same validation oracle used. Probe at least ONE adversarial case not covered by Muse's saved 23 mutations. Pin the 6 actual files separately from mutable ephemeral bytes and identify any unverified dependency on fixed local absolute path `/home/eariver/git/japanese-generative-ai-survey`.
- Examine TeX parser and normalized cell comparator: ensure `\tabularx` 20 tables, 80 ordered physical rows, 78 DATA + 2 NOTE, each exact cell and column semantics, TeX `&` escaping, `\%`, `\_`, malformed/nonparsed rows, honest padding normalization. A TeX statement outside parsed rows must not hide an omitted row; wrong within-row cell assignment and same-table swap must FAIL. Analyze whether current checker confirms exact row-level *source→projection→TeX* mapping vs only a subset.
- Test all 29 numerical/rights claims at anchored row/variant/value/unit/source tier, not anywhere in same table; especially COBOL 40%+ enterprise use **≠** hidden-test accuracy 10.9→72.1, TanStack `GH published_at` 15:18:14Z **≠** npm registry 15:21:49.491Z **RAW_NOT_ARCHIVED**, MemT 66x **storage not speed** and 1.86x unverified, Voxtral WER/price units unresolved, DeepInfer `PSEUDOCODE` not runnable, Patch stage 4 vs 5 / CVE unidentified not proven absent, DeepSeek MIT vendor-declared/not verified by artifact LICENSE SHA.
- Verify exact 36 bibliography keys: 19 exact reader-visible / 1 `recap` machine-only / 13 natural and CURATED_REVIEW_REQUIRED / 2 further / 1 unavailable / 0 orphan are **Muse classification**. Personally evaluate key claim-support links, especially the 13 natural references and 2 further, expose ambiguous/unsupported ones. A string present in body is not evidence that it supports the exact bibliography claim, and a source URL in print is not evidence that raw bytes were archived. Confirm GitHub/npm times and postcutoff Oct25 documentation are never falsely promoted.
- Check print projection from independent r3.5 reader preserves all 8 packages, 19 items, 20 headers, 80 rows, 3 figures, 29 claims, 5 recap paragraphs, protected technical names and API routes. Inspect prose transformations outside tables (the r1/r2 loss of `POST /v1/decisions` was in a paragraph and escaped table-centric QA); spot-check URL parsing and copy/paste use. Challenge any meaningful defect not included in the saved mutation suite.

Report semantic `PASS`, `PASS_WITH_LIMITATIONS`, or `REQUEST_CHANGES` with concrete P0/P1/P2 evidence. If source bytes or runtime unavailable, say `STATIC_CODE_REVIEW_ONLY` and qualify what was not independently rerun.

## 4. Audit B — actual PDF visual and read-back (cannot be faked)

**Independently read the actual fixed PDF binary and/or all actual 22 PNG page bytes** using a supported binary-access route. Optionally render all pages from confirmed PDF, compare PDF-derived page count to 22, and inspect each page at readable resolution, not merely contact-sheet thumbnails. Check page-by-page: P1–P8 pagination/31 requirement coverage, TOC vs pages, figure captions, 20 tables and cells, cross-page floats/splits, Japanese fonts/tofu, long URLs, code/technical line breaks, P8 `POST /v1/decisions`, clean body hyperlink target, GH/npm note, bibliography completeness and readable line wraps on p21–22, page fill and wide tables. Keep a **page-by-page matrix p01–p22** with actionable notes plus exact byte/hash provenance for the inspected PDF/pages.
- Actual reader-visible PDF selectable/extractable text and link annotations should agree with TeX and claimed click destination. A GitHub contents metadata query or `main.log` is not visual inspection.
- If no reliable PDF/PNG binary access: state **`PDF_VISUAL_AUDIT_BLOCKED`**, include precise access attempts and coverage boundaries, and **DO NOT** claim visual PASS or overall publication-paper PASS. A semantic-only result may still be given separately.
- Assess ~22 vs 38 target honestly: content coverage vs depth, bibliography share, sparse pages, source caveats, not padding; respect prior 20 SUBSTANTIVE/11 PARTIAL, and do not call 31/31 complete.

## 5. Audit report and decisions

Deliver to Google Drive folder `GPT-Sol_Review` as `yyyyMMddHHmmss_SolReview.md` with:
- Exact audit subject r5 HEAD/Tree, print subject r3 HEAD/Tree/PDF raw SHA, current remote refs, repo scope/integrity.
- Original independent r3.5 status referenced correctly; independent new semantic / visual / provenance verdicts **separate**.
- Check-by-check evidence: clean test and 23 negatives actually rerun or marked not rerun; independent novel adversarial test; 20/80/29 claim mapping; 36 key classification/curator caveats; 22-page actual images and their IDs or a frank visual BLOCKED state.
- P0/P1/P2 findings with ID `W43-R5-AUD-xx`, exact source paths, affected claims/table rows/PDF page(s), expected vs actual, remediation scope, independent limitations.
- Explicit terminal: `INDEPENDENT_W43_R5_PDF_PASS` only when semantic and full visual both checked/P0=P1=0; `INDEPENDENT_W43_R5_SEMANTIC_PASS_VISUAL_BLOCKED` if semantics actually passed but binary inaccessible; otherwise `INDEPENDENT_W43_R5_REQUEST_CHANGES` if material defect, or `INDEPENDENT_W43_R5_INCONCLUSIVE` if both portions unverified. Be truthful about partial qualifications; don't conflate r3.5 audit PASS with this audit.
- Stage remains `ARCHITECTURE_ESTABLISHED`/native Draft BLOCKED and Human PDF Gate PENDING. **No writing to repo**, no Human approval, no Freeze/Release, no main merge. Report for **editorial Sol adjudication**, not for Muse self-closure.
