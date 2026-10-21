# W42 r13 independent-review intake — Sol editorial disposition

Date: 2026-10-18 JST
Authority: `SOL_EDITORIAL_DISPOSITION / EXTERNAL_INDEPENDENT_REVIEW_ADOPTED / NOT_HUMAN_APPROVAL`
Source: `20261018040632_SolReview.md`, user-delivered original from a separate independent review session, saved on Google Drive / GPT-Sol_Review. This repository file is a **faithful operative findings/disposition**, NOT the raw complete external report, a second independent audit, or an approval. If the original cannot be accessed by Muse, use this record and the linked execution contract; do not assert original was read.

## 1. Identity and independent finding

Independent target branch: `weekly/2026-W42-v2-work`
Audited HEAD/Tree: `5520e8f5b1f3c07686873cdf75a7086761bdea14` / `a72302edbf2fbad6cf714e4db9dbdcec48519c2c`
r13 compare base: `8154e3865c365c6009e485fef527c6f3478e7210`
Reviewed main HEAD/Tree: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / `801de813319f08777ab1581a5e8875fc1ac5df19`
Frozen Core v2 HEAD/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Audit verdict **REQUEST_CHANGES / 19_OF_19_PNG_VISUALLY_AUDITED / MAIN_LOG_ABSENT / NO_PUBLICATION_AUTHORITY**.
Auditor opened both contact sheets and all nineteen individual page PNGs at fixed r13 SHA. GitHub PDF binary and an independent LuaLaTeX rebuild were not checked; visual conclusions apply to the committed page PNGs. Branch diff r13 vs r13 base: one normal commit, 47 changed files, all under `sources/2026-W42/execution/`. The auditor independently confirmed HEAD/Tree identities and canonical invariants.

Editor Sol re-read audit and read-only re-checked live branch HEAD `5520e8f5b1f3c07686873cdf75a7086761bdea14`, main/Core HEADs, State (`DRAFT_COMPLETE`, architecture `approved`, publication `pending`), 47-file execution-only diff, and fixed-HEAD missing `preview-r13/main.log` (404). This disposition **adopts REQUEST_CHANGES**; neither r13 proof nor formal Reader/Publication progression is authorized.

## 2. Accepted repairs — preserve / regression-test

- F01: LFM publisher terms vs individual weight-file LICENSE; Beam Apache-2.0/NOTICE/attribution/modified-file/patent/third-party obligations. Do not collapse them or imply full redistribution clearance.
- F02: old seven unrelated internal-source references did not re-enter r13; new 117 ledger rows have HTTP(S) references when required.
- M01: MTP 4.287 → 4.718 denotes **average speculative decoding acceptance length**, not acceptance rate. Do not reintroduce the mistranslation.
- M02: aptamer 131/311 (42.1%) is screening; eight clones are later titration/confirmation, not the same denominator.
- M06: r12 JST-as-Z issue is documented by a qualified correction; file mtime is not in Git; do not convert inference to certainty.
- r13 maintains seven approved Architecture chapters, SELECTED28 (16 PRIMARY/12 SUPPORTING), canonical Draft v10.0 unchanged, all Stage/Gates unchanged.

## 3. Findings adopted for r14

**P0 / MAJOR — mandatory independent-verifiability and page-quality repair**
- PDF-01: p16 P7 `table*` isolated amid an almost empty page; reported 43.6 pt overfull vbox cannot be excused as harmless. Address root cause, not a visual patch.
- PDF-02: p19 carries only bibliography [B58]/[B59] and a proof marker. Remove orphan bibliography tail while retaining all entries and readable URLs.
- PDF-03: `preview-r13/main.log` absent at fixed HEAD, despite build manifest/review index/change ledger claims that it was committed. Save actual complete log, build commands, toolchain/fonts, warnings and independently read back at new fixed HEAD; disclose any evidence limitations. Never fabricate historic r13 log.
- PDF-04 (MINOR): committed `main.tex` is 820 logical lines; validation report says 808, manifest says 820. Reconcile as provenance correction.

**P1 / MAJOR — substantive source-supported correction**
- TECH-02: P6 Earth AI GRA: ground 4 conditions × 2 models, 3 repetitions/variation, evaluator and saturation, model-dependent planning contribution, negative/failed cases, cost and caps in the original paper. r13 Flash-only 3→52→63 is insufficient to infer universal gains.
- CITE-02: isolate important numeric, license, benchmark and evaluation assertions to individual source section/table/method at block/claim level; broad paragraph-wide sets (P1 s1-02, P3, P6, P7) are not sufficient.
- EDIT-01: r12 92 paragraphs/18,165 paragraph characters → r13 103/19,193 is **+11 / +1,028**. `+21 / +2,189` is r11 82/17,004 → r13, not r12→r13. r13 all-block `block.text` count 22,446 vs r12 21,412; other 22,315 counter may be defined differently. Fix baselines and preserve separate measurement definitions.
- Technical depth/size gap: r13 PDF 19 pages (including cover, float-only p16 and bibliography p17–19) vs Architecture magazine 28-page target and 30-page cap, planned article body 26.5 pages. These metrics are not identical, so do not claim exactly nine pages of missing body. However research depth is materially insufficient, especially P1/P2/P4/P5/P7, where r12→r13 increments were small or negative.

**P2 / targeted improvements**
- TECH-01 (MINOR): verify original NVIDIA research and Training Recipe: SPEED-Bench split, draft length 7, temperature 0 greedy 4.287→4.718 and separate temperature 1 sampling 3.787→4.612; cite tables, recheck semantics. Do NOT assert conditions without actually reading these sources.
- TECH-03 (INFO): clarify aptamer stage populations, criteria, measurements, and distinct trajectories 0/167, 54/208, 131/311 without implying longitudinal identical denominator.
- CITE-03 (MINOR): redundant chapter-end URL/source boxes plus 59-key end bibliography; create one accurate reader bibliography and useful per-claim source path, preserve every source.
- EDIT-02 (MINOR): collapse P7 repeated OpenRouter/API caveat and other generic closings; replace only with grounded mechanism/method/failure analysis.
- EDIT-03 (MINOR): remove literal `accepted_context_notes` from p17 reader surface; retain metadata in sidecar.
- EDIT-04 (MINOR): naturalize p01 `専門身体` wording; fix cross-chapter floats seen p03→04, p05→06, p10→11; keep Japanese glyph and source-label legibility.

## 4. Scope / prioritization ruling

All independently evidenced P0/P1 repairs are adopted. F01/F02/M01/M02 repairs remain regression gates; TECH-04 (license conservative phrasing) is maintain-as-is, not a demand for unverified legal certification. Text expansion must prioritize technical mechanisms, inputs/outputs, measured denominators, comparison design, failure cases and source caveats, not decorative page padding or repeated boilerplate.

Further technical deepening on P1 Wonder/Gemini 4 Argon/Active Memory and agent evaluation; P2 Maia/NUMA/prefill-decode and LFM comparisons; P3 Nemotron acceptance conditions/LiLiCorr/QAD; P4 Codex/Scion/HydraFusion/AutoFix/AI Scan; P5 unexpected behavior/distillation/NIST/METR; P6 Earth GRA/aptamer/Deep Review; P7 Vals/GLM-Legal/ASPIRE/Glimpse, bounded to the already-approved 28 selections and seven chapters.

The independent audit found 19/19 PNGs visually accessible, **not** that it independently reconstructed the PDF bytes. r14 must produce an independently auditable updated full-page proof, manifest, PDF hash and logs. If credible primary sources cannot justify the target pagination, report evidence shortfall and stop for editorial disposition; do not silently change approved 28-page plan.

## 5. Protected authority / next step

Frozen Core v2, shared roots, accepted evidence/materiality/selection/architecture, canonical Draft v10.0, Synthesis, Production State, Gate, checkpoints and reviewed `main` remain read-only and immutable.

Human Architecture Review r1 = APPROVED and is not to be repeated for edition-local prose/visual revisions preserving approved selection/architecture. Human Publication Preview = PENDING. No validated publication or release.

Next authorized unit: edition-local, noncanonical Muse r14 implementation via
`sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r14-substantive-depth-source-traceability-and-pdf-repair.md`.
All Muse work must use an existing branch, strict exact starting remote HEAD+Tree check against dispatch, normal commits and non-force push, no fallback branches. Publication transitions/Human approval remain withheld.
