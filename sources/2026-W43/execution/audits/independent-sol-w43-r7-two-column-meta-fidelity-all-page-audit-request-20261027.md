# J-GAS W43 r7 — Independent Sol audit request: restored two-column layout, reader-meta closure, full print fidelity

Date: 2026-10-27 JST.
Status: `INDEPENDENT_SOL_READ_ONLY_R7_AUDIT_REQUEST / HUMAN_PUBLICATION_PREVIEW_PENDING`.
Repository: `eariver/japanese-generative-ai-survey`.
Executor: **independent Sol**, separate from editorial Sol and Muse Worker.
Submission: Google Drive folder `GPT-Sol_Review`, filename `yyyyMMddHHmmss_SolReview.md`.
Scope: **completely read-only repository/GitHub audit**. Do not mutate any branch, repository files, audit status, Human Gate, State, Core, Release or GitHub issue/PR. External Drive report may be written only to designated folder.

## 0. Exact immutable audit pin / no current-tip substitution

**Fixed r7 subject is the worker's r7 commit (not the later contract commit):**
- Branch name for ancestry: `weekly/2026-W43-v2-work`.
- **Audit HEAD: `3b1178ff5140ff03f4291701c346a6329a228a1b`.**
- **Audit Root Tree: `a196ebb56c19d12f805793330dfca9488b024f26`.**
- Exact parent: `794824f68e65e77f15b5280a8a1069bee05f03ee`.
- Relative r7 path: `sources/2026-W43/execution/core-free-preview-r7/`.
- Independent audit contract is committed AFTER fixed r7, so **current branch HEAD may differ**. Explicitly read the fixed r7 commit by SHA. Confirm the contract commit is one descendant adding ONLY this audit request.
- Protected reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
- Frozen production/survey-core-v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Correct historical r6 subject HEAD `d8e21b8fe6513ff0592604292bdec034d2c3eeea`, Tree `9ec7dd73d4acc50be48672fd3970af0e2b30925d`.
- Correct historical r3 print HEAD `3cdf2a01b810a972ecddfaa41c7dccded55c75f9`, Tree `17b0525fec79d5624a227f82bf7c5493dd1e5b73` (r6 build manifest had corrupted r3 SHA; r7 separate correction should be checked independently).

First independently read back every available fixed commit/tree, current remote tip and protected refs. Distinguish fixed subjects from current branch tip. If exact object cannot be verified, stop with `AUDIT_PIN_NOT_VERIFIED`; do not substitute a different SHA.

## 1. r7 PDF, source and worker claims to challenge

New fixed-r7 PDF:
`sources/2026-W43/execution/core-free-preview-r7/main.pdf`.

Muse-reported properties to verify with **actual binary bytes**, not mere JSON strings:
- raw PDF SHA-256 `5d01f49677c25e156da350c023ca5374cb72759b93eba21f049ea86d8dd9f93e`;
- Git blob SHA **`638fb602cee92ff18fac846aa805c7ae6b106b6b`** (independently read via GitHub content list);
- 487,514 bytes, 22 A4 pages.
- `main.tex`: raw SHA-256 `9791a545c1ed363f8abace62c90bdbfe15f31dac4017b80a5109907c35509ea0`, Git blob `d017dbefe9b5ad76616ece6c7cc16c414bde3b05`, 97,572 bytes.
- `preview.sty`: raw SHA-256 `0199d86d3553dbe731944999885830892203d0d2f1ff87eb96ad3d84e82b5a44`.
- r6 old-PDF SHA-256 `113b179a4fab82df28a5d9f1ac1ac6c588ce2a0a253b988ba590944057f76320` and old-TeX SHA-256 `7c052f05227228332fecec469b3b90e1b8952d4c3ab44ea65f180cecd4dd662b`. Never use r6 print visual QA as a substitute for r7.

The previous r6 independent report (Google Drive `https://drive.google.com/file/d/1TJwC41xoEteT3ZiS9AZ2iYJHWLFOkJo-/view?usp=drivesdk`) terminal was `INDEPENDENT_W43_R6_REQUEST_CHANGES`, P0=0/P1=2/P2=4:
- P1 `W43-R6-AUD-01` one-column main narrative vs established segmented two-column Weekly;
- P1 `W43-R6-AUD-02` reader-facing production/review/completeness metadata leaks;
- P2 `AUD-03` checker independent replay unexecuted;
- P2 `AUD-04` historical r3 SHA typos in r6 manifest;
- P2 `AUD-05` versioned Architecture 31-row totals 18/13 vs 20/11;
- P2 `AUD-06` bibliography 15 curated references remain not fully independently verified.

Muse r7 report claims `MUSE_W43_R7_TWO_COLUMN_READER_META_PDF_READY_FOR_INDEPENDENT_REAUDIT`; its saved r7 checks are `R7_READER_SURFACE_PASS` **18/18** and negative `NEGATIVES_PASS` **9/9**; r6 36/36 clean re-run witness, historical r6 38/38 NOT re-run. These are **Muse claims**, not independent PASS. Worker visually checked 22/22 contact-sheet or sheet-scale thumbnails but only **11/22 full-resolution pages**. This audit requires new full-resolution inspection of **EVERY page**.

## 2. Layout audit: real two columns, wide material, reading order (blocking Human P1)

- Read actual released reference at reviewed `main` SHA:
  `surveys/weekly/2026-W42/main.tex`,
  `surveys/weekly/2026-W42/preview.sty`. W42 uses **segmented `multicols}{2}` normal narrative + full-width tables outside column segments**, two-column bibliography and 7mm gutter.
- Read fixed r7 `main.tex` and style independently: editorial Sol has counted **32 `\\begin{multicols}{2}` and 32 `\\end{multicols}` plus 20 `\\captionof{table}` full-width tables**. This validates source structure only. **Visual image proof** must show normal prose truly in two columns across p03–the closing; bib columns readable, not mere macro existence.
- Check all 20 tables, 3 figure bodies, 5 code blocks (including long Decisions JSON), full-width boundaries and new page breaks for rows dropped/reordered/overlap/clipping, mislocated captions, fragmented footnotes, awkward empty pages, TOC page numbering, total reading order across columns and pages; identify exact physical page and issue ID.
- Verify no layout-induced truncation of 29 anchored claims (vendor and clock qualifiers), 80 ordered physical rows, 307 nonempty table cells, 36 bib keys, 5 final recap paragraphs. No false page-count 22 mandate; evaluate actual pagination and legibility relative to W42.
- Audit all new `pages/p-01.png` … `p-22.png` individually **at readable/full resolution** by actually opening/inspecting their image bytes; supply a per-page p01–p22 matrix with observed evidence and page image blob/hash identifier. Render r7 PDF yourself if environment permits; if you cannot prove PNGs were produced from exact PDF binary, distinguish that limit. Do **not** report full visual PASS from mere file presence, manifest, contact sheets or Muse's 11 full-res check.
- Audit all-cover / first-body / intermediate / recap / bib layout; final page blank tail need not automatically fail; missing or clipped content does.

If media inaccessible, `PDF_VISUAL_AUDIT_BLOCKED` (even if source TeX structural checks PASS). Explicitly separate PDF-byte hash from PNG-image validation, and source-visible prose from actual PDF visible text.

## 3. Reader-facing metadata audit: independently scan 100% of print surface (blocking Human P1)

- Full source and actual PDF page scan (article/cover/title/section head/captions/box titles/code headers/bib intro/footer); assess 23 exact old→new changes recorded by Muse in `meta-change-ledger-r7.json` against real r6 and r7 TeX, not just 23 count.
- Verify removal of reader-visible `印刷用原稿 r3`, `編集プレビュー・未承認` within normal title, `読者確認用プレビュー`, `本プレビューは非正準の編集 proof`, internal Core gate/QA/review status, `p1-f1`, `p8-f2`, `§…実物` operator location tags in captions, and eight `P1 ---` through `P8 ---` chapter prefixes. Machine `\\label{sec:P1}` metadata may remain invisible.
- Check scientific qualifiers remain: `未実行`, `原本未取得`, `発行元測定`, `独立再現なし`, `単位・比較対象未確定`, `POST_CUTOFF`, 404 unusable for proof, numerical denominators, rights/license boundary, GH source vs npm `RAW_NOT_ARCHIVED`.
- Proof watermark/status visible on cover and end footer and PDF metadata can remain **only in visually separated anti-mispublication safety layer** while Core-native Draft is BLOCKED. Do not mistake that controlled safety warning for magazine prose; do not silently delete it.
- Inspect any other remaining operator phrasing, e.g. source-record provenance expressed as a narrative production process; distinguish readers' genuine evidence scope from internal editorial milestones. Identify exact page/line and proposed replacement if meaningful.
- Check whether a blank cover line/table of contents/recap was accidentally dropped during normalization; not just grep-clean.
- Report closure separately for both `W43-R6-AUD-01` and `AUD-02`.

## 4. Semantic regression / replay and **novel** counterexample

At immutable r7 commit read all:
`meta-change-ledger-r7.json`, `meta-scan-r7.md`, `layout-design-vs-W42-r7.md`, `r7-reader-surface-semantic-join.py`, `r7-semantic-clean.json`, `r7-semantic-negatives.json`, `portable-independent-replay-r7.md`, r6 `full-reader-visible-segment-join-r6.py` and original 36/38 outputs, r6 baseline witness and available r3.5 source/projection/ledger/manifest.

- Independently recalc raw hashes for r7 PDF, r7 TeX, style and pinned predecessor inputs, and corroborate Git blob object IDs.
- **Where executable**, independently run r7 18 clean/9 negative cases with actual exit codes, and 36 clean r6 historical baseline separately. Reconstruct a read-only staged worktree using immutable downloaded files if needed, and **never let the validator write into committed source**. r6 utility defaults `--out` beside itself (a prior worker run accidentally overwrote two immutable JSON files, then restored); ALWAYS pass an isolated output dir. r6 `--tex-role r6` also requires explicit `--test-tex` + `--test-pdf` r6 paths to avoid false S07c blocker. The historical r6 38 negatives are explicitly **not** replayable in that role because their harness demands an old r3 production note; do not claim rerun or unconditional closure.
- Add **at least one newly designed adversarial mutation** not among r7 saved nine, with a material scientific/production distinction and explicit actual result of same checker; choose e.g. a claim qualifier within a two-column paragraph outside table, wrong numeric unit from full-width table, loss of bib-to-claim link, prose ordering near split segment. If execution unavailable, state static expected rejection != experimentally observed rejection.
- For new r7 source, compare `r6→r7` entire TeX and visual-rendered text using EXACT whitelist of 23 reader-meta changes + nonvisible segmented-layout markers, not bag-of-words or number-only checks. Confirm 71 original ordinary prose paras + one authorized split, 8 reading-note boxes, 3 full figure bodies, 5 code blocks, recap 5/5, 20×80 ordered rows/307 cells, 29 claim anchors, 36 distinct bibliography keys and 13+2 curated classification. Normalize only proven formatting operations; report all exceptions.
- Source claim truth, independent benchmarking, full archival provenance and license validity are **not proven by TeX joins**. Never promote `RAW_NOT_ARCHIVED`, vendor performance results, 404 or post-cutoff into independent evidence.

## 5. Exact build/reproduction and P2 artifact integrity

**Observed repository gap as of this request:** r7 `build-manifest-r7.json` declares `outputs.log.path` = `sources/2026-W43/execution/core-free-preview-r7/main.log`, with claimed SHA256 `eb9cf8ea167dd03957c033dbc1cc5c9729d2446074f570d4f4faea6172332a25`, **but the fixed r7 GitHub tree has NO `main.log` entry**. It must NOT be cited as a committed log. Determine whether the omission is documented/intentional or accidental, what claims cannot be verified, and severity. Original r7 PDF+TeX artifacts exist and are distinct; this omission does not by itself prove the PDF build failed.

If independently able to run LuaLaTeX: do so only in a **temporary isolated copy, without any GitHub/repository writes**, capture exit codes, actual compile log, errors/overfull/underfull, PDF bytes, text-layer/URI annotations/fonts. PDF may contain nondeterministic build metadata, so distinguish semantic/visual equivalence from byte-for-byte identical output; do not insist a regenerated PDF SHA match without first proving build reproducibility.

- Verify PDF binary reported 22 A4 pages using a PDF parser (or precisely state not independently parsed), and all 22 PNG object bytes when possible; recompute hashes per page, not truncated 16-char digest displayed in worker page QA.
- Verify actual PDF `/Annots` external URI values: r7 Muse report says **28 UNIQUE http targets**, not “only 28 bibliography items”; 36 bibliography keys can legitimately map to shared URLs. Evaluate each visible bibliography link/official guide/API and scoped npm `%2F` target rather than treating 28!=36 as a presumed failure. Check link action validity, CJK punctuation absence, in-PDF selections and embedded fonts where tools support.
- Check reason for missing log, whether `main.log` should be retained in subsequent edition and whether independent build reconstruction can close traceability; note that you are read-only and must only recommend an edition-local future correction.

## 6. Versioned Architecture / bibliography governance (P2, do not change authority)

- Architecture accepted 31 must-cover requirements P1–P8, 19 selected stories, 29 claims, 20 tables/80 rows. Previous 2026-10-26 r3.2 independent **then-current** grading 20 SUBSTANTIVE/11 PARTIAL with its own 11 IDs; later r2 coverage-diagnosis individual arithmetic 18/13 has **13 different PARTIAL IDs**, with **14 changed IDs** overall. Do not report it as two simple score changes or either as the authoritative final grade; do not silently promote a weak evidence-limited requirement. Look at `architecture-31-versioned-reconciliation-r7.md`; report current printed placement and whether a new Human/Editorial rating is required, without altering approved Architecture.
- Bibliography unique 36 keys: 19 EXACT_VISIBLE, 1 machine-only label, 13 natural mentions, 2 further-reading, 1 unavailable/404, 0 orphan. The 13+2 remain `CURATED_REVIEW_REQUIRED`. Assess how uncertainty is communicated; do not require unavailable originals to be manufactured or quietly upgrade evidence tiers.

## 7. Terminal, report and independent boundary

Issue independent finding IDs `W43-R7-AUD-01...` with P0/P1/P2, actual exact SHA/Tree readback, read-only command evidence, all-page visual matrix, two blocking Human Comment closures, all 23 metadata mappings, external replay result/limits, novel mutation, actual PDF link/font/build-log findings, quantitative 20/80/307/29/36 coverage, citation and architecture grading bounds. Explicitly distinguish **worker claim**, **auditor actually independently executed**, **auditor visually inspected**, and **not accessible/not independently verified**.

Choose terminal based only on evidence:
- `INDEPENDENT_W43_R7_PDF_PASS` (all-new full visual print + semantic pass, P0=P1=0, P2 limits listed);
- `INDEPENDENT_W43_R7_SEMANTIC_PASS_VISUAL_BLOCKED`;
- `INDEPENDENT_W43_R7_REQUEST_CHANGES`;
- `INDEPENDENT_W43_R7_INCONCLUSIVE`.

No audit report in repo. Save **external** final Markdown at Google Drive `GPT-Sol_Review/yyyyMMddHHmmss_SolReview.md`, verify Drive readback, provide exact file URL. If unable to write, don't claim saved; give report inline and identify blockers. Report is a recommendation to editorial Sol, not Human approval. No freeze/release/PR/merge, no change to `ARCHITECTURE_ESTABLISHED`, Human PDF Gate `PENDING`, Core native Draft `BLOCKED`, Frozen Core unchanged.
