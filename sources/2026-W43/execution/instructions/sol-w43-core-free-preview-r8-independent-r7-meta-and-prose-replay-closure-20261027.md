# J-GAS W43 r8 — Editorial Sol bounded execution contract

Date: 2026-10-27 JST
Authority: independent r7 Sol audit adjudication / EDITORIAL_SOL_R8_BOUNDED_CORRECTION
Repository: eariver/japanese-generative-ai-survey
Executor: Muse Worker on EXISTING branch weekly/2026-W43-v2-work ONLY.
Subject stays NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF. Human PDF Gate PENDING / ARCHITECTURE_ESTABLISHED / Core-native Draft BLOCKED.

## 0. Mandatory exact read-only guard

The separate Sol dispatch identifies a NEW post-contract W43 HEAD/root Tree, the ONLY authorized Muse execution starting pair. The W43 pair here is pre-contract parent, not a fallback:

W43 pre-contract HEAD be17e9944818442181975fa66b51912d2e7db8d8 / Tree 2429f675db817cc38333182734ed6338f1eabc68
reviewed main HEAD 041a08dfef3112643cbf85b4a86a7b6f9128aed6 / Tree a134dc36a407d08ab1de416324229b3955e0325a
Frozen production/survey-core-v2 HEAD 774dd39a951c9ac3818e83dfffd4c7666efb0a20 / Tree cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481

Confirm ALL THREE remote HEAD/root Tree pairs, post-contract W43 parent==pre-contract HEAD, and the contract-only single-file diff before ANY writes. Mismatch => ZERO WRITES / report exact expected vs actual / STOP. Local clean checkout may only fetch and FF-only. No new/fallback/review/repair branch, reset, rebase, force, other branch writes, PR/merge, or shared Core edits. Recheck before push, use normal non-force FF, remote HEAD/Tree/diff readback.

## 1. Independent r7 audit accepted and immutable pins

Original independent report: 20261027035724_SolReview.md at https://drive.google.com/file/d/1G97p7LnH5R3qeHLFMnE5JMfYt7ZcUDBW/view?usp=drivesdk .
Terminal INDEPENDENT_W43_R7_REQUEST_CHANGES; P0=0 / P1=1 / P2=4. If the report is unavailable, this contract transcribes its substantive findings; never claim to read inaccessible documents.

Fixed r7 HEAD 3b1178ff5140ff03f4291701c346a6329a228a1b; Root Tree a196ebb56c19d12f805793330dfca9488b024f26.
Fixed r7 TeX at sources/2026-W43/execution/core-free-preview-r7/main.tex: 97572 bytes, raw SHA256 9791a545c1ed363f8abace62c90bdbfe15f31dac4017b80a5109907c35509ea0.
Fixed r7 PDF at sources/2026-W43/execution/core-free-preview-r7/main.pdf: 487514 bytes, raw SHA256 5d01f49677c25e156da350c023ca5374cb72759b93eba21f049ea86d8dd9f93e; 22 A4 pages. Fixed style SHA256 0199d86d3553dbe731944999885830892203d0d2f1ff87eb96ad3d84e82b5a44.
Fixed r7 follows W42 segmented two-column layout: 32 begin/end pairs, 20 full-width tables, 3 figures, 5 code blocks, 5 recap paragraphs, 36 bib keys. Independent r7 auditor inspected 22 separate PNGs and supports closure of prior R6-AUD-01 two-column defect; DO NOT redo layout without a proven print issue. The independent auditor did NOT independently rerender the PDF, execute the Python checker, parse fonts or hyperlinks, or rebuild LuaLaTeX: preserve these limits.
Other fixed r7 issues: archived main.log absent due root gitignore *.log; r7 negative check_mutation does not compare normal narrative; 15 curated bib items (13 natural + 2 further), and versioned Architecture 31-row evaluations unresolved; never promote scores/claim confidence.

## 2. P1 residual metadata: EXACT three authorised reader-visible repairs

Audit finding W43-R7-AUD-01: three additional editorial approval/operator wordings remain visibly printed although 23 old replacements passed.

A. r7 main.tex line ~81 / PDF p04 / Flint table 2 cell:
CURRENT: 計数規約は承認済みArchitecture境界注記
REPLACE with precise reader-facing technical qualification, e.g. totalとactive per tokenは計数規約が異なり、直接比較できない.
Preserve 39.8B total, 約2.5B active, experts/layers/SWA, 512K/256K/262144 conditions and Apache-2.0; preserve row position and 307-cell count. No automatic alteration of actual scientific data.

B. r7 main.tex line ~440 / PDF p11 / FLUX prose:
Contains 承認済みArchitectureの旧ラベルはraw検証待ちの legacy として保持 inside an internally repetitive and ungrammatical sentence about PR/blog vs claimed FAQ Two at launch. Replace the editorial process phrase AND its redundant neighboring sentence with ONE clear reader-facing epistemic distinction, without adding new facts:
The PR/blog presents availability claims but a text attributed to FAQ has no verified original URL, version or timestamp; a contradiction between authoritative primary sources is NOT established; keyframes/live/schema/GA cannot be confirmed from the unresolved attribution. Preserve all published modality, commercial/performance conditions and separate known vs unknown. Do NOT claim the FAQ was fetched or an official cross-source contradiction was proven. Limit replacement to this exact whole prose paragraph.

C. r7 main.tex line ~985 / PDF p22 / bibliography [recap]:
CURRENT: P1-P8横断の編集合成
REPLACE with 本号の各主題を整理した派生記述 or equivalent, preserving [派生・限定], URL未取得, 新規数値なし, 新規の一次主張を含まない. Preserve recap bib machine key.

Create meta-closure-and-semantic-diff-r8.json containing full exact A/B/C before/after, r7 source line and old PDF page, new PDF page, preserved scientific facets, and strict allowed-delta assertion. Entire r7→r8 TeX difference MUST be ONLY the three authorised replacements (B counts as one whole paragraph). r8 preview.sty MUST be byte-identical to fixed r7. All layouts, other article paragraphs, all 20 tables except one exact cell change, 3 figure bodies, 5 code, 5 recap paras, 36 bib keys, 29 claim anchors preserved.

Run a new SEMANTIC human-readable sweep of *entire* TeX comment-excluded visible region and actual r8 PDF text/images: article, table cells, source notes, bibliography and cover. Look for unfamiliar process/meta markers (approved Architecture, gate, editorial proof, QA, rev, internal IDs), not just old 23 replacements; distinguish genuine evidence caution (未実行, 独立再現なし, 発行元測定, 原表未取得, POST_CUTOFF, 404, licence, RAW_NOT_ARCHIVED and GH/npm clocks) from internal workflow language. Preserve separate protective NONCANONICAL proof mark and PDF metadata until Human approval. If finding additional unambiguous reader-facing metadata outside A/B/C requiring a change, STOP and report Sol authorization required; don't silently enlarge scope.

## 3. P2 strict prose preservation — independently discovered negative N10

Independent audit found a NEW N10 adversarial mutation affecting normal P1 two-column prose with unchanged tables/codes/bib and critical marker counts:
OLD: MoonshotのKimi K3.1 Proは10月23日の告知とAPI提供が先行し、重み配布は11月4日の将来予定である。
MUTANT: MoonshotのKimi K3.1 Proは10月23日の告知後、API提供も重み配布もすべて終了した。

The auditor did not run r7 Python and made only a static detection-gap conclusion. FIRST: reproduce N10 in isolated memory/temp with original r7 check_mutation; capture ACTUAL return/cause/exit. No r7 repository mutation.

Implement new r8 checker that first builds an exact expected TeX = immutable fixed r7 TeX with exactly A/B/C whitelisted substitutions, then asserts full byte/UTF-8 visible-body identity with actual r8 TeX; no global token bag, count-only oracle, missing-paragraph skip, or excessive normalization. Test ALL ordinary P1–P8 paragraphs, 20 table bodies/80 rows/307 cells except A, 3 full figure bodies, 5 code, 5 recap, 36 bib, 29 claim facets, TOC titles and all caveats. Reuse prior r6 source→projection→TeX evidence only with its actual limitations: strict r7→r8 delta is not independent r3.5 original truth.

Run negatives using THE SAME full r8 checker used for clean and record EXPECTED vs ACTUAL failure causes/exit codes on temp copies. Must include N10, semantic qualifier reversal in another ordinary paragraph, FLUX unverified FAQ→confirmed contradiction, numeric cell/clock change, adjacent ordinary-paragraph swap, figure body change, code token change, recap paragraph change, bibliography key deletion, unknown operator sentence insertion, and proof mark removed/approved. N10 MUST be detected even if all counts & keywords unchanged. Do not give PASS for a mutation which wasn't actually introduced or failed for unrelated malformed input or a stale/oracle hash. Include isolated portable repo-root and staged-dir runbook; ensure no output writes to r6/r7 namespace. Report pre-fix actual old checker blind spot vs post-fix actual same-checker N10 rejection.

## 4. New edition-local r8 PDF, complete build log, full PDF QA

From fixed r7 TeX with A/B/C substitutions ONLY, produce NEW r8 TeX, same layout/sty and NEW PDF under sources/2026-W43/execution/core-free-preview-r8/; never overwrite r7 artifacts, and never substitute old PDF bytes. Keep actual two-column normal story, 20 wide tables, figures/code full-width and readable two-column bibliography. Page count may change honestly; no 22-page obligation.

Build with lualatex two times and record both actual exit codes and full compiler output. Preserve complete .log contents as a NEW **tracked .txt** name, e.g. main-tex-log.txt plus compiler-pass1.stdout.txt and compiler-pass2.stdout.txt. Root gitignore excludes *.log; do not merely list a nonexistent main.log in manifest. Compute SHA256, sizes and Git tree presence for logs and PDF in build-manifest-r8.json; if logs cannot be committed or verified, report BUILD_TRACEABILITY_BLOCKED.

Recompute new PDF raw SHA256, size, A4 page boxes, actual page count; render every page as >=150dpi pNN.png and contact sheets. Muse must independently view EVERY NEW r8 page at readable/full resolution, identify no clipping/table corruption/URL wrapping/TOC mismatch and confirm A/B/C are corrected at actual NEW page numbers and absent from printed text. Check long Decisions JSON, all 5 recap paras, p22-ish bibliography and both anti-mispublication marks. Record every PNG full SHA256 and page-by-page observations.

Parse ACTUAL r8 PDF link annotation destinations, official Decisions Guide, encoded scoped npm %2F URL, page boxes, selectable Unicode and embedded fonts with available tools; compare 36 bibliography keys versus repeated/unique actual URI count (28 unique http in r7 worker QA != 36 bib keys). Don't claim any PDF internal property independently validated merely from TeX strings. Where unsupported state NOT_VERIFIED.

## 5. Editorial authority, allowed writes, and stop

P2 versioned Architecture grading stays distinct: r3.2 prior independent 20 SUBSTANTIVE/11 PARTIAL, later r2 diagnostic row count 18/13 (14 row categories differ), neither automatically grades current r8. 36 bibliography keys keep 19 exact-visible/1 machine-only/13 natural/2 further/1 unavailable/0 orphan; 15 CURATED_REVIEW_REQUIRED do not upgrade without raw independent evidence. No approved Architecture, Selection, Evidence, State, Human Gate changes. No official Draft/Freeze/Release/merge.

Allowed writes ONLY new files in sources/2026-W43/execution/core-free-preview-r8/, one new sources/2026-W43/execution/SOL_W43_CORE_FREE_PREVIEW_R8_HANDOFF.md, one new sources/2026-W43/execution/sessions/muse-w43-core-free-preview-r8-20261027.md, and append-only sources/2026-W43/execution/index.md. No write to any older r1–r7 files, no canonical PDF or Core/shared files.

Recommended r8 content: main.tex, preview.sty, main.pdf, main-tex-log.txt, two compiler stdout txt, meta-closure-and-semantic-diff-r8.json, reader-meta-full-sweep-r8.md, r8-exact-fidelity-check.py, r8-fidelity-clean.json, r8-fidelity-negatives.json, n10-old-vs-new-replay-r8.md, portable-independent-replay-r8.md, build-manifest-r8.json, pdf-page-qa-r8.md, pdf-links-fonts-r8.md, full-resolution pages/contact sheets, architecture-and-reference-carryover-r8.md, independent-sol-r8-reaudit-request.PROPOSED.md. Final normal FF non-force commit/push, read back remote SHA/root Tree/changed paths, and include actual PDF SHA, page count, log hash and all page checks. PROPOSED independent reviewer must re-inspect r8 PDF/new images and attempt portable independent script replay; worker results are not separate Sol PASS.

Terminal only with recorded evidence:
MUSE_W43_R8_META_P1_AND_PROSE_FIDELITY_READY_FOR_INDEPENDENT_REAUDIT if A/B/C exact diff + genuine N10 test + full build logs + new all-page PDF QA all pass.
MUSE_W43_R8_READER_META_OR_SEMANTIC_BLOCKED if unauthorized visible/scientific change discovered.
MUSE_W43_R8_BUILD_LOG_OR_PDF_QA_BLOCKED if build/log/PDF/visual/annotation evidence cannot honestly pass.
