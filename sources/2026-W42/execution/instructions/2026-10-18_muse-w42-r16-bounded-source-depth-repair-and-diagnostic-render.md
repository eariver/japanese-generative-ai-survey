# W42 Muse r16 — bounded source/depth repair and independently auditable diagnostic render

Date: 2026-10-18 JST
Authority: `EXECUTION_AUTHORITY / SOL_R15_INDEPENDENT_REQUEST_CHANGES_ADOPTED / CORE_V2_FROZEN / NONCANONICAL_ONLY`
Repo: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W42-v2-work` (EXISTING ONLY)

## 0. Required starting and immutable guard

At dispatch Sol provides **Exact Starting Remote HEAD** and **Expected Starting Tree**. Read **remote ref + Git commit object** read-only before any write, and require byte-for-byte exact equality. Also check reviewed main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19`, Frozen Core v2 `production/survey-core-v2` `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. For source baseline read fixed r15.1 `523dbf757d0168c98096947e861e28197dff73b0`, Tree `06663d373dd1af43a206850296220e729b86ffae`.

If ANY identity missing/mismatched, **ZERO WRITES / STOP** reporting expected+actual. Before push recheck the exact remote lease. No branch creation/fallback/review/repair branches, no reset/rebase/rewrite/force. Normal commits and non-force pushes ONLY to the same branch.

Fully protected and read-only: shared `.github/config/docs/schemas/scripts/templates/tests`, `main`, Frozen Core v2, W42 canonical Discovery/Screening/Evidence/Views/Materiality/Completeness/Selection/Architecture, canonical Draft v10.0/Synthesis, `production-state.json`, Gate/review-index/approval/checkpoints and pre-r16 `execution` bytes. Human Architecture r1 remains APPROVED; Human Publication Preview PENDING; lifecycle `DRAFT_COMPLETE`.

All new content must be edition-local `sources/2026-W42/execution/editorial-revision-r16/`, `execution/diagnostic-r16/`, `execution/sessions/`, and a truthful append-only execution index. No canonical acceptance, Stage Validator transition, or Human candidate.

## 1. Mandatory read order and authority

Read:
1. `execution/reviews/sol-w42-r15-external-architecture-depth-audit-disposition-20261018.md` (Sol ruling based on original Human-delivered `20261018134400_SolReview.md` and user-provided follow-up check; **neither raw audit nor follow-up is claimed to be in repo**).
2. `execution/reviews/sol-w42-r14-external-review-disposition-20261018.md`, earlier r13 finding/gates.
3. r15.1 session, `architecture-coverage-and-depth-gap-r15.md`, `architecture-content-readiness-r15.md`, source/claim matrix, S7–S10 readings, Earth paper/repo discrepancy audit, all seven r15.1 Draft proposal JSONs, reader JSON/MD, 177-row citation ledger, 88-key bibliography map, validation report, synthesis and block-diff.
4. Human r9 dossier, approved `architecture-v2.json` + immutable Human r1 basis/approval, all 28 selected roles and accepted Evidence authority. Apply Sol r9 claim provenance errata; no backdating/post-window event misclassification.
5. r14 17pp full proof and stale `execution/preview-r15/main.pdf` v15.0 18pp **only as historical layout references**; v15.1 has NO PDF.

Do not tell readers `preview-r15/main.pdf` demonstrates r15.1/r16 content. The separate independent audit verdict is `REQUEST_CHANGES`, not permission to amend Architecture.

## 2. Unit A — original-source corrections and verified addition ledger (P0)

Perform actual original-page/section/table reads, log URL, access date, title, original section/figure, passage scope and exact source-backed assertion. Store `editorial-revision-r16/primary-source-repair-ledger-r16.md` and `editorial-revision-r16/claim-locator-crosswalk-r16.json`. Do not substitute existing sidebar records as independently fetched sources unless re-read genuinely.

**A1 / P1 Argon, Minecraft.** Read https://arxiv.org/html/2610.22319 Methods/experiment setup. Correct `t1-11/t1-23`: randomly generated Easy world (check whether seeds were preselected; do not infer unreported protocol), distinct 27h14m, 2,783 program creations, 605 deaths, 229 inter-agent messages and restarts/failed attempts. Do not fabricate causality or many-trial success rates. Remove `固定種`, `程序`, `229通`, `605死` and related unnatural translations. Distinguish single run from controlled replication; vendor-origin context.

**A2 / P2 Maia 300.** Read https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/ Rack-scale architecture and HBM4/NUMA sections. Correct **24 four-accelerator trays = 96 accelerators per 167-kW rack** everywhere `t2-03/11/14/20`, in tables, summaries, source matrix, and all newly authored r16 documents. Audit terminology for power/density/disaggregated prefill/decode and phase/future schedules. Separate vendor unnamed baseline from actual comparable test. Do not touch historical r15.1 proposal bytes.

**A3 / P7 ASPIRE.** Actually read https://research.nvidia.com/labs/gear/aspire/ section "Real-Robot Cross-Embodiment Skill Transfer" plus https://github.com/NVlabs/ASPIRE/blob/main/README.md . Extract physical robot tasks, program-debugging with/without retrieved simulated skill, output/total tokens until first success, held-out success rates of the first-success program; capture exact numerical values/units/denominators **only if figure/README really supplies them**, otherwise explicitly `FIGURE_VALUES_UNRESOLVED`. Describe limits and difference between sim and real and why this is **publisher's** real-robot result, not third-party reproduction. Correct prior "no real robot results" suggestion in `t7-05/t7-09/t7-17`, add appropriate precise explanation and provenance.

**A4 / P6 Earth AI.** Re-read https://arxiv.org/html/2610.15750v1 Table 4/5, §Methods and https://github.com/google-research/geospatial-reasoning-benchmarks. Preserve full symmetric 4 configs × 2 Gemini model comparison: Pro tool-only 50.8±1.7 → GRA 47.6±2.7 (−3.2 pp), Flash 52.2±5.4 → 62.7±2.5 (+10.5 pp); 3 repetitions with SD. For Table 5's domain negatives, check precise original values and axis/bench first (e.g. Site Selection) before quoting. Correct old `t6-08` apples-to-oranges juxtaposition; tool access vs planning effect within SAME model/benchmark. Be explicit about evaluator (human-validated tool-agnostic autorater), golden workflow, caps, cost with failures and Univearth saturation. Keep paper/repo GeoKTools 85/220 vs 85/210, template differences, CBGB 44 scored vs 45 curated as **unresolved version/scope differences**, with exact reference URLs; no invented reconciliation, no test-publication claim.

**A5 / P6 Wet-lab.** Read original https://www.gstatic.com/science-ai/agentic_aptamer_sandbox.pdf Methods and related epitope/VERID reports if accessible. Extract definitions for screening hit, population of round denominators, selected eight clones, subsequent titer/binding measurements and repetitions. If full PDF retrieval or section extraction fails, mark `PRIMARY_PDF_METHODS_BLOCKED` and refrain from inventing thresholds. Retain correct 131/311 screening vs 8 later clones separation.

**A6 / P2 LFM licensing/model documentation.** Read https://www.liquid.ai/lfm-license full §§2–5 and §11, original model card/files at https://huggingface.co/LiquidAI/LFM2.5-24B-A2B; confirm entity-wide $10M ANNUAL REVENUE applicability and license per distribution artifact; distinguish 33T pre-training vs 36T total training token budget if original card confirms, and exact benchmark temperature/hardware. Don't generalize publisher license text to every weight file without direct evidence.

**A7 / P3/P4/P5 continued guards.** Preserve NVIDIA original MTP average acceptance length vs rate, SPEED-Bench draft length 7 and temperature split, MTP 4.287→4.718 greedy vs 3.787→4.612 sampled. Preserve genuine rights/NOTICE/vendor/independent distinctions. Fix repeated Codex cost/CI, Scion WAL/cache and distillation/METR/ECDSA story boundaries without deleting unique technical claims. METR has no disclosed outcomes merely because new evaluator access exists.

**A8 / source mapping integrity.** `bibliography-map-r15.json` B69/B73/B88 contains appended human-note text inside URL; rewrite ONLY NEW r16 bibliography as normalized URL separated from `locator_note`/`provenance_note`. Resolve aliases B62/B65/B86/B87 without dropping attribution; maintain r16 cite references; each high-signal block uses direct original `URL → section/table/fig/license clause → observed number / methodology / version → block ID → bib key / TeX cite`. Never use syntactically HTTP-prefixed but invalid string as proof. Live link resolution on important claims; log failures. Preserve historical map intact.

## 3. Unit B — substantive Japanese reader revision; regression and counts

Create seven **new** `editorial-revision-r16/proposals/P1...P7/draft-result-r16.PROPOSED.json`, reader `.PROPOSED.json/.md`, r15.1→r16 block-diff/change ledger, claim/section mapping, new bibliography and citation ledger, and proposed synthesis pair; do NOT rewrite r15/r14 original files. Keep 7 packages and PRIMARY16+SUPPORTING12; no new research-selected topics, no fake Human Architecture amendment. Revise technical exposition with clear `mechanism → controlled comparison → observation → counterexample → limit`, concrete source and readable Japanese; avoid generalized paragraph padding and excess Sino-Japanese phrases. Ensure no wrong-seed, 96-trays or sim-only-ASPIRE claims recur.

Text repetition scan by semantic content (same measurement/denominator with merely synonymous wording), not just duplicate strings. Audit P2 `t2-14/20, t2-10/17, t2-08/21`; P4 `t4-03/21,t4-06/07/23`; P5 `t5-06/08/19`; P7 `t7-02/18,t7-07/19`, P6 repeated Earth tool-vs-plan summaries. For every retained second mention, record its genuinely different causal or experimental purpose.

Recompute exact r15.1 baseline **136 PARAGRAPH / 24,162 paragraph-only chars**, 7 TABLE, 7 NOTE; reviewer plain sum P+T+N text = **27,284**, Muse body PTN = **27,415** (131 difference). Publish both definitions and independently reproducible counters, explain difference line-by-line (e.g. table formatting) rather than asserting one is erroneous. Record r16 new technical facts and removed repeats separately from mere char additions. Run **frozen** 7 Draft checks and Synthesis proposal check; record actual receipts; none imply canonical validation.

**Mandatory editorial pre-render gate:** `editorial-revision-r16/content-and-source-readiness-r16.md` documenting each chapter's quality: P1/P6/P7 former MAJOR depth gaps, P2/P3/P4/P5 former MINOR; named technical findings disposition and important inaccessible primaries. Critical false factual conditions cannot be left uncorrected for rendered "review-ready" proof; if unknown, state it and render with explicit limitations, not fake resolution.

## 4. Unit C — DIAGNOSTIC rendering from exact r16 content, NOT formal Reader

Always attempt a **diagnostic**, regardless of whether 28 pages appears reachable; this is to MEASURE pagination, not demonstrate meeting a quota. Build TeX/PDF in an isolated temporary directory from the current r16 proposal JSON and verified citation/bibliography files; verify fresh TeX content and sample block hashes match r16 (no v15.0/v15.1 stale content). If build requires a repository copy, treat the local copy as ephemeral and do not write to canonical publication paths.

Record:
- actual **total PDF page count** via parser/pdfinfo and log, actual PDF SHA256/bytes;
- per-page cover/real article body/bibliography/methodology split, chapter boundaries, tables/notes, the fraction of each page visibly occupied, flow and column allocation; do NOT treat PDF total minus cover as all body, and don't equate a table page with an entire chapter;
- original vs actual reader text, citations, URLs and footnotes; bibliography end-entry page breaks and long URLs; no p15/p17 orphan/stranded URL or interchapter floats; all refs, warnings, fonts and CJK missing glyphs;
- complete engine build command/version/fonts and full `main.log`, every individual page PNG and contact sheets; actually open/review each page (not just file-exists).
- a quantitative range for **effective technical-body area**, contrasted with Architecture's planned 26.5 body and magazine target 28/max30; **no false 9,400 characters or 6–7 pages as proven shortfall**.

To make subsequent *independent* remote visual audit possible, after building ONLY IN TEMP, copy an explicitly stamped immutable **NONCANONICAL DIAGNOSTIC / NOT PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL** source+PDF+log+all PNG/contact sheets+manifest/index into `sources/2026-W42/execution/diagnostic-r16/`. This is an edition-local audit artefact, NOT a canonical Reader/Publication output. Historical `execution/preview-r15/main.pdf` remains untouched and labeled STALE v15.0. If binary evidence cannot safely be preserved, record why and report DIAGNOSTIC_VISUAL_AUDIT_BLOCKED; never claim independent PASS.

Create `editorial-revision-r16/architecture-pagination-reconciliation-r16.md` explicitly separating:
(1) technical content sufficiency vs missing factual/method questions;
(2) measured article-body effective pages vs cover/bibliography and empty space;
(3) comparison to approved per-chapter plans (P1 4, P2 2.5, P3 5, P4 4, P5 3, P6 4.5, P7 3.5; target28/max30);
(4) missing reproducible content vs questionable planning assumptions: approved notes estimated only 1–2 front/method/bib whereas prior cover ~1 and bib ~2; `not a hard cap` ambiguous, **never interpret this as an authorized revision**.
Give options A further source-backed deepening, B bounded Human page-only revision, C structural rebuild only if evidence requires; report evidence for each. No anonymous word quota, line spacing, font/whitespace inflation or scope dilution.

## 5. Verification and terminal

Deliver:
- source repair ledger + source/claim/section matrix, independent source access outcomes;
- 7 proposal JSONs, reader previews, bibliography/citation mapping, actual frozen validator receipts and exact r15→r16 counts;
- corrected factual and Japanese change ledger with all F-01...F-10 dispositions and regressions;
- diagnostic TeX/PDF/log, every page PNG, contact sheets, fixed SHA and real visual QA in `diagnostic-r16/` (NOT canonical formal preview);
- `editorial-revision-r16/architecture-pagination-reconciliation-r16.md` and `content-and-source-readiness-r16.md`;
- `editorial-revision-r16/validation-report-r16.md`, `execution/sessions/muse-w42-r16-20261018.md`, and truthful append to `execution/index.md`.

Check remote lease immediately before commit/push; normal non-force only. Verify new remote HEAD+Tree, all target blobs including log/images, file scope and **no modifications to r11–r15 history or canonical assets**. If any critical source/block issue remains, report explicit blocker and do not self-certify publication-ready. Either way stop for Sol editorial review/independent focused audit at `SOL_W42_R16_DIAGNOSTIC_EDITORIAL_REVIEW_READY / NONCANONICAL` or specific BLOCKED code.

**Never** call formal Reader/Publication/Freeze/Release, never change Architecture/Gate/State/checkpoints/Core/main, never create Human approval, never describe diagnostic PDF as accepted publication artifact.
