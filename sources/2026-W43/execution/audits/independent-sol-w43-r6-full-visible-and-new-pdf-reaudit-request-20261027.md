# J-GAS W43 r6 — independent Sol full-visible fidelity and new PDF visual re-audit

Status: `INDEPENDENT_READ_ONLY_REQUEST / R6_EDITORIAL_SOL_RECHECK_ACCEPTED_FOR_AUDIT / HUMAN_PDF_GATE_PENDING`
Date: 2026-10-27 JST.
Repository: `eariver/japanese-generative-ai-survey`.
Executor: separate independent Sol session, not Muse Worker or editorial Sol. **Completely read-only toward GitHub/repository, Stage/Gates, Main, Frozen Core.** External report to Google Drive `GPT-Sol_Review`, `yyyyMMddHHmmss_SolReview.md`.

## 0. Immutable pinning, including worker metadata-error warning

**FIXED audit subject = Muse r6 SHA (this audit contract is a later child commit, NOT a replacement subject):**
- Existing branch `weekly/2026-W43-v2-work`.
- **r6 QA/print HEAD `d8e21b8fe6513ff0592604292bdec034d2c3eeea`**.
- **r6 Root Tree `9ec7dd73d4acc50be48672fd3970af0e2b30925d`**.
- parent/dispatch `9f79ccb81b361e0bbc712a30d342833ba25ee2a9`; one FF commit, 47 changed paths restricted to `sources/2026-W43/execution/`.
- Reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
- Frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Previous independent r5 QA subject HEAD `fa1caaedb6f2b09a6d8e1f77a505d363ca6d0c31`, Tree `4576f190346da02c1937778e459eb0391fbf6430`.
- **CORRECT historical r3 print HEAD** `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`; **CORRECT r3 Tree** `17b0525fec79d5624a227f82bf7c5493dd1e5b73`.
- r3 print historical PDF raw SHA256 `d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca`, historical TeX `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`.

**CRITICAL worker metadata issue (to be assessed, not silently trusted):**
`core-free-preview-r6/build-manifest-r6.json` historical_subjects.r3_print_head is recorded incorrectly as `3cdf2a01b810a972ecddfaa41c3dccded55c75f9`; r3_print_tree is recorded incorrectly as `17b0525fec79d5624a227f82bf7dccded55c75f9`. The Muse `independent-sol-r6-print-semantic-visual-audit-request.PROPOSED.md` repeats those corrupted historical identifiers. Both **contradict live GitHub Git commit/tree readback**. Do not use them as audit subjects, do not assert valid historical commit hashes, and explicitly report this metadata P2-level defect/scope recommendation. The **current r6 HEAD/root Tree, new PDF and TeX hashes below are separate and not implicated by these historic pointer typos**; verify each object independently.

## 1. Actual new r6 print subject (NOT historical r3)

- PDF at r6 commit: `sources/2026-W43/execution/core-free-preview-r6/main.pdf`.
- **r6 PDF raw SHA256 `113b179a4fab82df28a5d9f1ac1ac6c588ce2a0a253b988ba590944057f76320`**, Git blob `0342d2b5b5b38d9bd5cbb9488cbe98519a6c2af1`, **482659 bytes, 22 A4 pages** (claimed; independently re-evaluate).
- r6 TeX: `sources/2026-W43/execution/core-free-preview-r6/main.tex`, raw SHA256 `7c052f05227228332fecec469b3b90e1b8952d4c3ab44ea65f180cecd4dd662b`, Git blob `38bbe745d21eb3558344bfe49b9a7c85dc060d24`, 90920 bytes (claimed).
- r6 reader print projection raw SHA256 `63ad2617f663a01bd14a93b803a96272bf3cc72debbdf4817f81c6596eccbe80` = old r3 projection unchanged.
- r6 style raw SHA256 `46326113e54479f2ae9c4bfd1e116552d4765fa5fbae83b6ddfcf89f57417183` = old r3 style unchanged.
- r6 `pages/p-01.png` through `p-22.png` and 3 contact sheets are committed, but the **independent auditor must actually open new r6 page image bytes / PDF and inspect all pages**. Neither Muse's report nor previous r3 22/22 page audit substitutes.

Editorial Sol directly compared entire textual contents of historical r3 TeX and new r6 TeX: **exactly ONE deletion** of old TeX line
`{\\small\\color{SurveyMuted}P8の後に置く独立した締めくくり（5段落）。新規のP9パッケージではない。\\par}`
after `\\label{sec:recap}`, 0 other textual differences. Confirm independently by full file diff, not just `print-only-diff-r6.md`. The five actual recap paragraphs must be preserved in printed PDF.

## 2. Previous independent r5 findings to close, not rename

Prior independent report `20261027011100_SolReview.md`: `INDEPENDENT_W43_R5_REQUEST_CHANGES` P0=0/P1=1/P2=3. The prior auditor independently read actual r3 PDF/22 page PNGs and recomputed 6 raw SHA256, independently compared 20 tables/80 physical rows/**307 nonempty cells**/29 claim anchors with 0 mismatches. Prior r5 Python clean and 23 negatives were **NOT independently rerun**, fixed absolute paths blocked them. The prior r3 PDF visually printed an internal process note on p20.

- **P1 `W43-R5-AUD-01`**: ordinary paragraphs, complete figures and recap TeX content were *not* covered by the older r5 source→projection→TeX checker; independent TeX-only recap semantic reversal counterexample. New r6 purports to close with structural ordered full-visible check 36/36 + 38 negatives.
- **P2 `W43-R5-AUD-02`**: portable independent execution + accurate count + nonduplicative negatives + real hash-mutant binding; r6 `--repo-root` and `--staged-dir` claims to close. Independently run actual code, record commands, 36/38 counts, exits and real failure reasons. If not runnable, mark `NOT_RERUN` and qualify.
- **P2 `W43-R5-AUD-03`**: 36 reference keys 19 exact-visible/1 machine label/13 natural/2 further/1 unavailable/0 orphan; 13+2 `CURATED_REVIEW_REQUIRED`, none is magically verified raw. Preserve evidence tiers, GH `15:18:14Z` versus npm `15:21:49.491Z RAW_NOT_ARCHIVED`, 404 non-evidence and post-cutoff caveats.
- **P2 `W43-R5-AUD-04`**: reader-facing process note on old r3 p20. New TeX omits exactly one note line. Verify actual r6 PDF page p20 and text extraction excludes it while five recap paragraphs survive, and no collateral visual/layout regression occurs.

Original independent r3.5 **source/content** audit `PASS_WITH_LIMITATIONS` is a separate authority and should not be called r6 approval. Core-native Draft BLOCKED, current noncanonical/unvalidated proof only.

## 3. Audit A — Independently challenge r6 Phase A evidence and code

Read the FULL `sources/2026-W43/execution/core-free-preview-r6/full-reader-visible-segment-join-r6.py` (1455 lines), `portable-runbook-r6.md`, `full-segment-join-clean-r6.json`, `full-segment-join-clean-r6-baseline-r3.json`, `full-segment-join-negatives-r6.json`, `source-to-projection-to-tex-segment-map-r6.md`, `six-input-identity-and-mutant-binding-r6.json`, `reference-claim-tier-curation-r6.md`, `architecture-11-partial-disposition-r6.md`; fetch immutable source reader, ledger, manifest, strict checker and r3 TeX at exact historical commit.

**Replay**, don't accept self-declared JSON: real raw hashes of source r3.5 Reader/ledger/manifest, projection, r3 TeX+PDF, plus new r6 TeX+PDF; run clean for `tex_role=r3` and `tex_role=r6` and all 38 r6 negatives through the same validator using a portable input layout (can assemble read-only staged directory). Return exact command + exit code and provide an independent **new** adversarial mutation, not one of 38 saved cases. Confirm specific rejection of N-AUD-RECAP-SEMANTIC-REVERSAL (TeX only), N-PRINT-NOTE-LEAK (r6), deletion/change in ordinary paragraphs, figure body/edges, five code blocks and 5 recap paragraphs; no global words-only proxy, oversanitization, skipped unmatched paragraphs, or tautological PAs.

Independent source r3.5→projection→r6 TeX full ordered semantic fidelity including 8 packages/28 subsections/71 ordinary prose paras + one structural split/8 reading quote boxes/3 complete figures/5 code blocks/5 recap paras/20 tables/80 physical rows 78+2/307 cells/29 claim anchors/36 bibliography items. Separate preservation of source claim values/provenance from externally verifying those primary sources; qualified claims should stay qualified.

For 36 key categories, independently judge the source-span and confidence map. `CURATED_REVIEW_REQUIRED` may remain without being a P1 provided the data is explicitly limited; use exact key→claim→visible span→URL→raw/derived tier and do not inflate to 36 verified raws.

## 4. Audit B — new r6 PDF actual visual and link-level verification

Independently obtain **actual r6 PDF bytes AND/OR all r6 22 page PNG bytes** from immutable r6 commit. Recompute PDF SHA-256 from the binary; if binary inaccessible but all page images are available, describe precisely what was and wasn't verified. Page-by-page matrix p01–p22 with actual inspected image IDs and content notes (not merely whole-page layout log). Confirm cover, TOC pages, P1–P8, table1–20 (especially p07/p14/p16/p19 print legibility), all code/3 figures, p18 `POST /v1/decisions`/official clean URL, GH/npm separation p19, page p20 process note **absent**, recap exactly 5 paragraphs, 36 bibliography items legible on p21–p22, footers and NONCANONICAL banner. Check actual `/Annots` destinations, especially guide and percent-encoded npm scoped URL, CJK glyphs/font embedding and text extraction if tool support; do not assert them solely because Muse says 44 links/15 fonts.

Check print reflow/pagination caused by deletion, and whether retained 22 pages vs 38-page Architecture estimate is honest; no automatic minimum or forced padding. Prior PDF r3 visual audit DOES NOT count as r6 PDF inspection. If media blocked, explicit `PDF_VISUAL_AUDIT_BLOCKED`, not PASS.

## 5. Architecture grading mismatch — editorial provenance, not silent promotion

**New information detected before this request**: r2 location diagnostic `core-free-preview-r2/architecture-coverage-and-volume-diagnosis-r2.md` has **31 individually coded requirement rows** whose arithmetic is **18 SUBSTANTIVE / 13 PARTIAL**, while that same document's header/footer claims **20 SUBSTANTIVE_COMPLETE / 11 PARTIAL**. r6 `architecture-11-partial-disposition-r6.md` accurately identifies 13 named partial IDs. r6 worker reports r3.2 external independent summary as 20/11 but does not possess complete approved per-row 20/11 composition; r3.1 showed 26/5 at a different point in workflow; Human-approved Architecture `architecture-v2.json` has requirement titles but no SUBSTANTIVE/PARTIAL tier by row. **Do not fabricate which 2 IDs differ or revise the approved Architecture**. Independently review actual relevant r3.2 independent report if available, otherwise categorize `ARCHITECTURE_REQUIREMENT_TIER_MAPPING_UNRESOLVED` for Sol editorial ruling; stage/human gate remain unchanged. This is a separate editorial-quality/governance finding, not a reason to change a scientifically qualified claim in print.

## 6. Report and terminal

Save an independent full Japanese Markdown report in Google Drive `GPT-Sol_Review` as `yyyyMMddHHmmss_SolReview.md` (never update repo or write an audit PASS to GitHub). If saving fails, do not claim completed. Include immutable HEAD+Tree, actual remote tip distinguished from subject (the r6 request commit may advance branch), original/printed hashes vs actual recalculated, code replay proof, novel adversarial test, full-page matrix and PDF link annotations, independent P0/P1/P2 findings with evidence and source line/row/page refs, historical-pointer typo separately, reference-tier and Architecture 18/13 vs 20/11 unresolved status, and exact remaining Human decisions.

Terminal choose only one, supporting actual evidence:
`INDEPENDENT_W43_R6_PDF_PASS` (print fidelity and actual full visual verified P0=P1=0, with explicit P2/limitations); 
`INDEPENDENT_W43_R6_SEMANTIC_PASS_VISUAL_BLOCKED`;
`INDEPENDENT_W43_R6_REQUEST_CHANGES`;
`INDEPENDENT_W43_R6_INCONCLUSIVE`.

No Human approval, no formal native Draft/Validation/Publication Preview completion, Freeze/Release or main merge. Keep State `ARCHITECTURE_ESTABLISHED`, Human PDF Preview Gate PENDING, Core native Draft BLOCKED, all Frozen Core v2 and shared files untouched. Report back to **editorial Sol** for adjudication.
