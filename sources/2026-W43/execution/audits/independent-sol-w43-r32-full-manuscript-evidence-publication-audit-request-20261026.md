# J-GAS 2026-W43 — INDEPENDENT Sol complete manuscript/source/technical/preview-readiness audit

Date: 2026-10-26 JST.
Status: `REQUEST_FOR_NEW_INDEPENDENT_SOL_READ_ONLY_SESSION / FIXED_R3_2 / COMPREHENSIVE / NOT_MACHINE_STAGE_VALIDATION`.
Repository: `eariver/japanese-generative-ai-survey`. Work branch `weekly/2026-W43-v2-work` is for lookup ONLY.
**IMMUTABLE AUDIT SUBJECT HEAD**: `efac8324ff7a9f35ad34be391ba2ea328cfc1722`
**IMMUTABLE SUBJECT ROOT TREE**: `61e33ad8c9b8bb1a3a5e51dbc1d9d5b5b2222c43`.
Verify commit object's root tree and parents read-only; never switch to current remote HEAD, which has already advanced with Sol instructions. The review is of this content, not the later governance note.

## 0. Read only; independent standards

Act as **independent Sol in a separate session** from W43 editorial direction and Muse implementation. GitHub, files and source retrieval strictly READ-ONLY; DO NOT create issue/PR comments, commits, branches, pull requests, releases, or edit Drive/GitHub content other than saving *your audit report to the established Google Drive review folder* if available. Never run/repair frozen Survey Production Core v2 or invoke the blocked native Draft runner; never fabricate PASS, Human decision or Gate approvals. Avoid auditor dependence on Muse's 26/5 self-score, r3.2 QA "FIXED" claims, and editorial Sol's prior spotchecks.

Audit in two stages: (A) **blind-first independent full reading/technical and evidence challenge** of the r3.2 manuscript, accepted Evidence and primary archive, then (B) compare against historic audit chains, Muse QA, and recent editorial Sol three known regressions. Resist rubber-stamp checking; find genuinely new problems. If source original is unavailable, mark `UNVERIFIABLE` precisely, not fictitious corroboration.

Original W43 time window `[2026-10-16T22:00:00Z,2026-10-23T22:00:00Z)`, JST Saturday→Saturday. A vendor document viewed on Oct25 is NOT automatically a dated Oct22 source snapshot. Future weight releases and after-cutoff metrics are not W43 observed current releases.

## 1. Fixed corpus: read all, not just QA summaries

Core reader:
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-reader-preview-UNVALIDATED-20261026.md` (33,557 JS code units, 8 P1–P8 packages, five-paragraph final 「今週の総括」).
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-citation-confidence-ledger.json` (96 block objects, 20 TABLE objects, 79 `table_rows[]` records, 29 new top-level `claims[]` in five added tables; verify exact reality instead of accepting these counts).
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-source-crosswalk.md`, `w43-r3-2-editorial-qa.md`, `execution/SOL_W43_CORE_FREE_EDITORIAL_R3_2_INDEPENDENT_4POINT_HANDOFF.md`.
Architecture/scope: `sources/2026-W43/architecture-v2.json`, `architecture-review-summary-v2.json`, `architecture-review-attention-v2.json`; `candidate-matrix-v2.json`, `candidate-selection-v2.json`, accepted 32 Evidence cards/Views, 51 Materiality, Completeness LIMITED, evidence-risk ledger, 68/68 Attention and 19 SELECTED.
Trace to actual `sources/2026-W43/collectors/primary/runs/**` first-party saved raw bytes, accepted source references and literal publication clock; read relevant original public web source selectively when a high-impact missing raw can be independently verified. A source URL alone is not evidence that archive bytes were read. Archived README vs derived Evidence summary vs later live docs are different tiers.
Historical baseline: r2 independent full review `20261025212008_SolReview.md` (if accessible), r3.1 independent report `20261026005634_SolReview.md` (if accessible), previous r3.2 audit adjudication, Muse corrected versions r2, r3, r3.1 and r3.2. Audit does not claim those original files were read if unavailable.

## 2. Full independent technical/content audit P1–P8 + recap

Audit every article and every substantial factual assertion, not only the four recent fixes. For each chapter report: technical novelty and plausible mechanism; implementation/configuration and real execution prerequisites; source ownership and legal permissions; model/weights/API version, availability status and dates; exact numerical experiment population, apparatus, comparator, denominator, number units; conflicts, limitations and reader relevance; Japanese terminology and meaningful technical depth.

- **P1** Kimi API available vs Nov4 future weights; original clocks/cutoff, parameter total/active conventions for Flint and Nemotron; card's context config262144 vs announcement supports512K/recommends256K; weight licence vs paper/base licence; distinguish vendor claims from independently downloaded actual weights.
- **P2** DeepInfer DSpark MTP variable-length vs batch-invariant deterministic modes mutually exclusive, correct env variable names and exact code-derived provenance, `SamplingParams(seq_seed=1234)` import unavailable and snippet NOT_EXECUTED; MemT original 65pp paper partial validation, architecture and train stages, benchmark denominators1.86x/66x, source-specific CC BY-NC-SA 4.0, PolyForm NC 1.0.0, third-party MIT, unlicensed weights.
- **P3** Duet and 1Password agent credentials, permission grant flow, live vs coming-soon catalogue, prompt-injection defense limits, human in loop and vendor security claims; meaningful figure not a label.
- **P4** fal FLUX video speed: 277.80/10.95=25.37x, 277.80/12.45=22.31x and (277.80-12.45)/277.80=95.52% with clear denominator; vendor 26.5x/96.2% inconsistent, +47 vs +50 Elo vendor versions, AA original lacking; keyframes FAQ alleged `Two at launch` **original missing**, so no definite verified official-document contradiction or Oct18 source claim, live/schema/GA unresolved.
- **P5** Mistral Voxtral 3 STT/TTS/Realtime, Ming3.0-tts, Eleven Realtime: variant, model family, languages50+ vs35+/40+ vs benchmark11, official conflicts on TTS 9/35+/18/22, WER4.1/4.0 and cpWER18.4/18.6 vs Pyannote19.0 and recall94.6/81.4 with verified comparator or `COMPARATOR_UNVERIFIED`; pricing Mini $0.0035/min vs Small $0.004, Realtime $0.008 and agent $0.04/$0.08 `UNIT_UNVERIFIED`; raw chart absence must be visible. Check quoted per-sample eval and attribution of vendor benchmark.
- **P6** OpenAI Patch the Planet CVE not identified (not "zero"); rendered-only publisher extract, independently untested exploit/patch, five-step disclosure actors and chronology; frontier model training isolation threat model, in-vendor evidence vs outside repetition.
- **P7** biological research blind evaluation vs true independent wet-lab; low-resource coding public SQLite benchmark vs private/hidden COBOL migration; 19/20 ≥83% except COBOL72.1%, effort conditions, dollar costs $0.77 vs $3.48, benchmarking licenses.
- **P8** Decisions API `POST /v1/decisions` request JSON and separate *illustrative* response (not a run) from Oct25 observed docs, 400 questions **per request**, prices regional/long-context/write and access scopes; TanStack AI stable vs experimental, Github `@tanstack/ai@1.0.0` release 15:18:14Z vs npm **scoped package `@tanstack/ai`** timestamp 15:21:49Z, current r3.2 row link erroneously `https://registry.npmjs.org/ai` (unscoped), verify actual registry object/clock; DeepSeek V4.1 Flash 1017 model weights/API/harness, actual artifact-specific MIT/legal proofs, availability, vendor benchmarks and future billing.
- **Final 「今週の総括」** actually after P8, before references; full five paragraphs, accurate first-party vs reproduced distinctions and no new event/claim; not P9 and no editor-facing note.

Audit full 31 must-cover requirements independently with exact provenance & actual artifact location in manuscript; use `NOT_ADDRESSED / MENTIONED_ONLY / PARTIAL / SUBSTANTIVE_COMPLETE / NOT_VERIFIABLE`. Prior independent 26 COMPLETE / 5 PARTIAL (§1.4, §2.2, §4.1, §5.1, §5.2) is **a prior finding, not an automatic ground truth**. Distinguish partial because evidence missing from partial because author omitted valid content. Assess chapter density versus ~35pp planned body and reader value, no padding.

## 3. Every table, code and source link: 96 block ledger audit

- Verify all **96** ledger block IDs correspond to actual reader text, chapter/candidate and substantive claims; every **20 TABLE** object has correct actual text row-to-`table_rows[]` mapping; all **79 source subrows** and new 29 top-level `claims[]` support *the right metric/variant* (claims may be unlinked to actual row; do not accept count alone). Inspect all P1–P8 figures/code and citations; no invented numeric units, legal permissions or release clocks. If 96 full-source raw checks impossible, check every original in-repo raw available for high-impact claims and enumerate exact files not checked. Distinguish `source URL known`, `raw archived and read`, `publisher-reported`, `derived summary only`, `independent arithmetic rechecked`, `genuinely independently reproduced`.
- Test links plausibility and identity: **scope mismatch `https://registry.npmjs.org/ai` vs `@tanstack/ai` in `p8-f2`**; avoid a fabricated npm timestamp proof. For mixed tables link each **claim** to valid product+version+source, not a single block's `best_url`. Evaluate orderable timestamps vs day-only placeholders, DOI/license translations, source URLs that return moved/404. Inspect earlier accepted Evidence where original is missing, don't silently fill source gaps with web content out of issue cutoff.
- Unit checks: seconds, Elo difference, percentage vs percent-points, currency **per minute/per 1M chars/per 1k calls/per M tokens**, context size token vs support vs runtime config, language population, model/version. Verify technical code syntax against actual publisher source, label illustrative code honestly and distinguish imports not available.
- Reader-facing publication surface: validate Japanese readability, spelling, excessive kanji literal translation, copyeditor meta at **start of r3.2 reader** (`UNVALIDATED` status, `実行根拠と状態`, Stage checkpoints) and any tail/operator notes; trim redundant repeated caveats without losing unique relevant limits; flow, tables and figures currently fenced DRAFT_TEXT not layout tested. Check citation adequacy for public distribution, quote reproduction/language naturalness and license attribution.

## 4. Governance and Preview readiness

Assess whether content is ready for a **separately-governed noncanonical Core-free PDF prepublication preview**. This is NOT asking you to render a PDF or to approve a formal Production Human Preview Gate. Frozen Survey Production Core v2 `production/survey-core-v2` stays byte-identical `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Main remains reviewed `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`. State remains `ARCHITECTURE_ESTABLISHED`, Human Architecture approved, publication preview pending, native Draft checkpoint PENDING due Screening basis drift; this cannot be declared passed by an edition-local audit.

Find all publication-blocking P0/P1 and correctable P2 (or honest PARTIAL evidence gaps), distinguish from layout/preview-only blockers. No new branch/writes, no machine QA/TeX/PDF/Preview/Release, no exact Human Gate action, no Core repair.

## 5. Auditor deliverable (full, actionable, independent)

Produce:
1. **Editorial verdict** `PASS / PASS_WITH_LIMITATIONS / REQUEST_CHANGES`, distinct `NATIVE_DRAFT_VALIDATION = BLOCKED`; recommended whether a single consolidated Muse repair can reach a PDF preview.
2. P0/P1/P2 issue matrix with **stable IDs** (e.g. `R32-FULL-001`), severity, actual **file/block/table/row**, exact offending Japanese text or summary, first-party archived raw path/public URL/observed time, expected correction, `BLOCKS_PDF_PREVIEW=YES/NO`, potential impact on other sections, and clear acceptance test. No "fix X" without reproducible test.
3. 8-chapter editorial scorecard, separate 31-requirement **five-state** coverage and implementation strength, 96-block source coverage, 20-table row/claims validation, 5 LIMITED/68 attention status, reader-afterword and layout risk.
4. Check known 3 earlier Sol microissues **only AFTER blind phase**: wrongly unscoped npm registry ref; reader-facing header meta; P4 unsupported FAQ contradiction certainty. Report them in independent severity scheme and discover any others.
5. A **consolidated repair plan** grouped by same source or document root cause, avoiding sequential one-fix iterations; corrected wording/code/figures/table citations and sources for each; identify which limitations cannot be removed without original source and should stay labelled.
6. Exact SHA/tree audited and source fetch coverage / not-fetched disclosure. No claim all 96 URLs independently refetched when not true.
7. Terminal judgement `INDEPENDENT_FULL_R32_REVIEW_COMPLETE / READY_FOR_SOL_CONSOLIDATED_ADJUDICATION` with no GitHub mutations.

If possible, save full report to Google Drive `GPT-Sol_Review` following `YYYYMMDDHHMMSS_SolReview.md` and share link/filename. Otherwise provide complete Markdown in chat. The report must not fabricate content or be replaced by a short summary. Return to **editorial Sol**; no direct Muse writes. 
