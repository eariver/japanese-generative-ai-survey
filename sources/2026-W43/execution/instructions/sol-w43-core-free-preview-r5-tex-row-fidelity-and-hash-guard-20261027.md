# W43 Editorial Sol — r5 final bounded print-fidelity checker closure

Status: `SOL_R4_QUALIFIED_NOT_FULLY_CLOSED / NO_PDF_CONTENT_REPAIR_REQUESTED / NARROW_QA_INTEGRITY_ONLY / HUMAN_PREVIEW_PENDING`
Date: 2026-10-27 JST. Repo: `eariver/japanese-generative-ai-survey`. Execute ONLY on existing `weekly/2026-W43-v2-work`. Muse Worker performs bounded technical work; no independent reviewer decisions fabricated.

## 0. Fail-closed 6-way remote guard

First read remote branch HEAD and root Tree for all three refs, before any writes. The following WORK pair is the **pre-contract parent**, NOT Muse execution start. The separate Sol dispatch supplies the post-contract commit's exact starting HEAD/Tree. Its parent must be the pre-contract WORK pair; exactly one normal fast-forward commit added only this contract.

| Ref | HEAD | Root Tree |
|---|---|---|
| WORK pre-contract parent | `52224fa2acf83d2f482e207b7bceebda077ba221` | `970d348c4f6a144d08d990457f2f27511f1b4f4e` |
| main | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| production/survey-core-v2 | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

If ANY differs, ZERO WRITES and exact expected/actual STOP. No new/review/fallback/repair branch, no rebase/reset/force, PR or main/Core writes, no changed guarded originals. Clean local checkout may fetch+ff-only. Normal non-force push to existing WORK only; remote recheck before push and immutable full HEAD/Tree/file-diff readback after.

## 1. Facts, accepted accomplishments and remaining gaps

Muse r4 HEAD `52224fa2acf83d2f482e207b7bceebda077ba221`, root Tree `970d348c4f6a144d08d990457f2f27511f1b4f4e`. Compared with dispatch `e707379f7440d336b94908e7d56bffc6869d2f1e`: 1 FF commit, 13 changed W43 edition-local execution paths, no main/Frozen Core/State/Gate mutations.

r4's corrected checker `execution/core-free-preview-r4/print-semantic-fidelity-check-r4.py` genuinely removed r3's `or True` tautology and uses one `validate()` entrypoint for clean and 17 negative mutations (17 saved correct cause codes). r4 source-key classification corrected the false 18-key accounting and accurately discloses `19 EXACT_VISIBLE / 1 MACHINE_ONLY / 13 NATURAL / 2 FURTHER / 1 UNAVAILABLE / 0 ORPHAN` as a curated classification. Main r3 TeX's POST method/path, correct developer-guide URL, provider GH/npm split, 36 bibliography entry strings and all 20 table captions were directly checked by editorial Sol; fixed 22-page r3 PDF binary is present in GitHub and unchanged by r4.

**Remaining limits confirmed by static inspection**:

**R5-FID-01 — False scope claim for TeX table cells**. r4 `V03-rows-ordered-join` checks source-to-projection row identity, but `V04-tex-row-counts` checks TeX caption/number of rows only. `V05-claims-anchored` scans the **whole TeX table span** for values, variants and qualifiers rather than **the specific row/cell** of the given claim. Reordering two TeX rows within the same table, or replacing non-claim text in a TeX table cell while preserving row counts and words somewhere in the table, could pass. This does not establish `80-row bidirectional source→projection→TeX semantic join`; we must prove the **printed physical row position and cells**, not table presence/count. Do not claim old r4 result is a valid full TeX row-level proof.

**R5-FID-02 — V00 input hash not actually checked**. `V00-inputs-pinned` calls `rec(..., True, ...)` and says `SHAs verified by caller`; no read/hash comparison is performed inside r4 validator. Add real raw-byte SHA256 for (a) immutable r3.5 Reader `6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6`, (b) ledger `6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4`, (c) physical manifest `85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111`, (d) r3 print projection `63ad2617f663a01bd14a93b803a96272bf3cc72debbdf4817f81c6596eccbe80`, (e) r3 TeX `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed` and (f) original r3 PDF `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`. Clearly distinguish immutable disk files' expected hash vs ephemeral negative-mutant input strings. In a mutated-input validation, pin the true original baselines and validate the mutated text via semantic checks; no oracle/hardcoded `True` bypass for input hashes.

**R5-FID-03 — Evidence category scope**. r4's reader-visible-key arithmetic is more accurate than r3. Preserve 19/1/13/2/1/0 as an observed classification, but the 13 `EXPLICIT_NATURAL_REFERENCE` members in `source-key-classify-r4.py` are from a **curated literal evidence map**, not programmatically checked by source-span IDs. Never label those 13 as automatic positive proof or validate source claim URLs from their mere existence. Add a precise source-span/TeX-visible evidence extract or mark each class `CURATED_REVIEW_REQUIRED`; no invented link, raw source, independent truth or unverified evidence upgrade.

Other known limitations and nonclaims remain: r3.5 independent source audit `PASS_WITH_LIMITATIONS`, original P1 `R32-FULL-003=FIXED`; 31 Architecture must-cover were originally 20 SUBSTANTIVE_COMPLETE/11 PARTIAL; 22 printed pages vs 38 estimate (38 is a plan, not a required PDF padding count); binary existence, build log, and Muse pdftotext do not equal **independent 22-page visual audit**. Frozen Core v2 native Draft remains blocked; no formal publication preview or Human approval exists.

## 2. One narrow r5 QA unit, NOT another PDF rebuild

Read this contract, the full r4 checker and result JSON, r4 table/claim/keys audit and fixed r3 TeX/projection, plus the r3.5 exact Reader, strict original join checker and actual row manifest. All r1/r2/r3 PDFs/TeXs/projections, r4 QA files, r3.5 text/ledger/manifest and approved Architecture/Selection/Evidence/State/Human Gates must remain byte-for-byte unchanged.

Output only NEW versioned items under
`sources/2026-W43/execution/core-free-preview-r5/`,
plus `execution/SOL_W43_CORE_FREE_PREVIEW_R5_QA_HANDOFF.md`, one new session log under `execution/sessions/`, and append-only `execution/index.md`.

1. New r5 deterministic checker (Python or equivalent) using actual source→projection→TeX **20 tables/80 physical rows** 1:1. Parse each TeX `tabularx` body into **individual ordered rows and ordered cells**, correctly handling escaped TeX `\\&`, `\\%`, `\\_`, braces, `\\url`, and line wrapping. Map each printed row to exact table-id + row ordinal + manifest row-id and DATA/NOTE; show complete normalized source/projection/TeX per-cell comparison with a **bounded, explicit, reviewed allowlist** for operator-token rendering and print escaping only. Flag unrecognized changes, missing/extra/reordered rows or cells. For all 29 claims assert actual value/variant/qualifier in the **one target TeX row/cell**, with correct provider, unit, comparator and source provenance. The existing r4 V03 source→projection checker is a helpful input, not a substitute for true print mapping.
2. Make cryptographic input identity real (`hashlib.sha256(actual_file.read_bytes()) == expected`), exact six source+print inputs above, and make it visible in reported clean results with evaluated digest per file. A negative that intentionally corrupts a baseline original must fail `HASH_MISMATCH`, while projection/TeX text mutants go through the common semantic validator and fail their intended causes. If test harness overrides base bytes, be explicit and do NOT simply skip hash checking.
3. **True negative mutants run through same validator**, with cause checks: swap TeX row order in same table while holding 80 count; alter non-claim TeX cell text; swap two claim-bearing TeX rows while retaining table-level literal multiset; delete/replace TeX claim in its own row; shift a claim to the adjacent row; wrong provider clock/URL; alter a TeX row's DATA/NOTE; hash-mutated original. Existing r4 17 negatives may be reused but must stay real. Avoid `or True`, count-only, naive global keyword search, or `ANY_FAIL` acceptance.
4. A 36-key mapping with actual TeX-visible span references, distinguishing 19 reader-visible exact labels, 1 machine-only `recap` label, 13 curator-assessed natural references, 2 further-reading, 1 explicitly unavailable/404. For the 13 natural cases show exact quote/span and source support where available; label any that still require independent interpretation. Preserve GH/npm raw distinction and post-cutoff documentation restrictions.
5. Actual saved clean/negative test results, `row-cell-claim-binding-r5.md`, `input-identity-r5.json`, `citation-span-and-confidence-r5.md`, `r5-QA-limitations-and-independent-audit-handoff.md`, and **proposed** independent semantic+all-page visual audit request if and only if tests and static semantics genuinely pass. Use real command/exit outputs; do not invent tests or readbacks.

**Do not create any r5 PDF or modify fixed r3 PDF/TeX**; request Sol decision and STOP if actual reader-visible corruption is discovered. Existing print remains at fixed HEAD `3cdf2a01b810a972ecddfaa41c7dccded55c75f9` / tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73`, PDF SHA256 `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`. Do not move audit subject to r5 HEAD.

## 3. Terminal and governance

If complete, real 80-row TeX/claim binding + real input hash guards + same-entrypoint negatives pass, stop:
`MUSE_W43_R5_PRINT_FIDELITY_QA_READY_FOR_INDEPENDENT_AUDIT`.
This is only a **Muse technical handoff**; NOT independent audit PASS.

If parsing cannot prove full per-cell equality or constraints cannot be met honestly, stop:
`MUSE_W43_R5_PRINT_FIDELITY_QA_BLOCKED`
with exact row(s), claims, source/TeX discrepancy and limited proven scope. Do not turn partial confidence into full PASS.

Report actual start/final remote HEAD & root Tree and non-force FF, full changed-path list, unchanged main/Core/State/Gates, exact input digests and test logs/negative failure reasons, r3 PDF fixed object, credible coverage limitations, independent visual-audit dependency. Do not run Core native Stage or mutate shared/frozen scripts/configs, canonical `surveys/weekly/2026-W43/main.pdf`, official publication Preview/Human decision, Freeze, Release or main merge. After an honest r5 handoff, editorial Sol will open a separate read-only independent semantic and 22-page visual audit. On inaccessible PDF/PNG, that auditor MUST report `PDF_VISUAL_AUDIT_BLOCKED`, never PASS.
