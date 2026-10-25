# W43 Muse r3 — POST independent audit binding executable instruction (11 findings)

Status: `SOLE_EXECUTION_CONTRACT / INDEPENDENT_R2_REQUEST_CHANGES / R3_BOUNDED_EDITORIAL_REPAIR / NO_CORE_REPAIR / NO_STAGE_ADVANCE`
Date: 2026-10-25 JST.
Repository: `eariver/japanese-generative-ai-survey`.
Existing branch ONLY: `weekly/2026-W43-v2-work`.
Exact starting work HEAD and root Tree are provided separately by Sol **AFTER THIS FILE IS COMMITTED**, not r2's audit subject or earlier planning HEAD.
Reviewed main HEAD / root Tree: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen production Core HEAD / root Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## 0. Mandatory preflight / safe local synchronization

First read-only verify ALL six remote HEAD+root tree expected values for work/main/frozen. Any mismatch: `STOP_ZERO_WRITES` with expected and actual, no GitHub write. Existing branch only; prohibit new branch, fallback, rebase, reset, force, history rewrite, merge commits, Core modifications. If local work branch is clean, behind exact work HEAD and strict ancestor, `git fetch` then `git merge --ff-only` and recheck exact local/remote HEAD+root Tree. Dirty/diverged local: stop, no workaround. No operation besides the permitted local ff or edition-local output commits/pushes.

## 1. Mandatory read order / exact authority

1. Original independent uploaded `20261025212008_SolReview.md` (SHA256 `fa0d8d7a63198d2d6d1db6d5ef693c8f2d43823a5a00036a200631b4ad329bb5`, 23,861 bytes; if the file is not available from Muse's session, read the full 11-finding editorial Sol adjudication and independent audit metadata receipt under `execution/reviews/` and `execution/audits/`; absence of original is a review limitation to disclose, never assert having read unseen file).
2. Binding Sol adjudication `sources/2026-W43/execution/reviews/sol-w43-r2-independent-manuscript-audit-adjudication-20261025.md` and independent provenance summary `sources/2026-W43/execution/audits/independent-sol-w43-r2-manuscript-audit-receipt-20261025.md`. Existing prior Sol r2 targeted adjudication `execution/reviews/sol-w43-core-free-editorial-r2-targeted-adjudication-20261025.md` is lower priority where different; existing r3 pre-independent instruction `execution/instructions/sol-w43-core-free-editorial-r3-depth-and-citation-repair-20261025.md` is **background**, NOT an additional competing executor mandate.
3. Fixed r2 original full reader `execution/editorial-bypass/w43-r2-reader-preview-UNVALIDATED-20261025.md`, exact r2 ledger 86 rows, r2 QA and original r1 unvalidated input. Original audited fixed commit `a74e0e9537813b12b803fc133a727b064876118c` / Tree `f60b35fb9a7c1500d3eb8dcf245ba1cafb51d0f1`.
4. Human-approved r6 Architecture, all 31 actual must-cover requirements and package page_plan, Selection 19, accepted Evidence Cards/Views, materiality/completeness/5 LIMITED, 68 Attention, source collector raws; reviewed Human Architecture APPROVED and mandatory P8-after `今週の総括`. Prior status `ARCHITECTURE_ESTABLISHED` and machine draft pending, publication_preview pending, non-null approval provenance.
5. Native Draft defect `execution/defects/w43-drafting-screening-basis-drift-20261025.md`: root is Core `validate_package_basis` stale Screening `state_sha256` vs bridge-updated legitimate State. Human explicitly prohibits Core repair; **do not rerun native Draft or fake validation**.

## 2. Mandatory 11-finding correction matrix

### P1-01 — Actual artifact coverage (CRITICAL)

For each Architecture requirement, produce the explicitly specified **actual item**, not a promised future diagram. Include in new complete reader preview:
- P1 §1.3 **three-layer context schematic** for Kimi API vs Flint published support512k/recommended256k/card config262144; do not combine into one universal maximum;
- P2 §2.2 **two genuinely source-derived, mutually exclusive** DeepInfer settings/code snippets (exact full env var names and source-checked `SamplingParams(seq_seed=...)` location; if only API usage is not in archived code, mark syntax `ILLUSTRATIVE_NOT_EXECUTED` and do not give an unverified executable snippet); §2.5 **MemT license matrix/schematic** clearly distinguishes paper-related README-4.0 / original software PolyForm NC-1.0.0 / third-party MIT component / weights+data not authorized by those licenses;
- P3 §3.2 **credential/human-confirmation flow diagram**, staging vs live availability; threat boundary and provenance anchored to approved Evidence;
- P6 §6.1 **five-step coordinated disclosure process** with roles, actor and state/provenance and rendered-only source caveat;
- P8 actual concise **Decisions API request/response example**, endpoint and field names verified against official developer docs / accepted original; `SAMPLE_ONLY` and NOT_RUN, no guessed schema or version. If source cannot be obtained, mark **P1-01 UNRESOLVED** and stop `SOL_W43_EDITORIAL_R3_SOURCE_BLOCKED`; never claim full completion.
A requirement's presence as a promise isn't SUBSTANTIVE_COMPLETE. Actual figures may be simple Markdown/Mermaid/ASCII concept diagrams with anchored claims, but placeholders do not count.

### P1-02 — Row-level citations (CRITICAL)

Keep existing 86 ledger block IDs; add `claims[]`, `table_rows[]`, or another documented edition-local sub-row provenance field for all mixed-product tables, at least `p1-t2,p1-t3,p1-t4,p5-t1,p7-t2,p8-t1,p8-t2`. Each row/claim records product/model/version, exact best primary URL, archived file path or Evidence claim pointer, publication-time precision, metric units and denominator, vendor/third-party source class, `SOURCE_REPORTED`/verified raw/limited/conflict. Attach useful citation key(s) in tables themselves. Never let Flint best_url stand in for Kimi+Nemotron.

### P1-03 — QA truth values (CRITICAL)

For 31 must-cover requirements distinguish `NOT_ADDRESSED`, `MENTIONED_ONLY`, `PARTIAL`, `SUBSTANTIVE_COMPLETE`, `NOT_VERIFIABLE`. Provide actual file/block/figure/code location and original source anchors for each. Correct r2 claim `31/31 all Y`; do not output 31/31 passed unless true. Track `EDIT_FIXED` separately from `SOURCE_VERIFIED`, `vendor-only` vs external reproduction; audit all 15 tables for *content*, per-row source and *layout* separately. Previously `VERIFIED_DIRECT=16 / SOURCE_REPORTED=56 / LIMITED=8 / UNRESOLVED=4 / SOURCE_NOT_VERIFIED=2` is pre-r3 starting tally, NOT an r3 verified claim.

### P1-04 — fal FAQ confidence and clock (CRITICAL)

Original Oct18 `Two at launch` FAQ not independently fetched in auditor's fixed r2; its URL/version/observation clock absent. Attempt locating only within accepted archived sources; if unavailable, lower language to "FAQ由来とされる未照合の記述との食い違い" with no exact Oct18 attributable official original claim. Do not turn it into a confirmed official contradiction unless real source bytes/locator/version exist. Other vendor PR/blog speed/Elo/keyframe statuses remain unresolved where appropriate, no actual schema/live/GA proof invented; the approved r6 Architecture itself remains unmodified.

### P2-01 — MemT license (exact saved primary)

`sources/2026-W43/collectors/primary/runs/20261025T044100Z-muse-r3-evidence/raw/memt-readme-e75c13d.md`, around lines 208–219 explicitly states paper-related/original paper materials `Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International`, repository original software incl SGLang integration `PolyForm Noncommercial License 1.0.0`, a third-party flash-linear-attention component MIT, weights/datasets/trademarks excluded. Use edition-local sourced license matrix, correct mistaken prior rejection, **do not claim paper's PDF contains terms merely because README declares them**.

### P2-02 — Flint 2.2B and contexts

Archived Flint model README explicitly states approximate **2.2B active body**, approximately 2.5B active incl output head/excl embedding, card config **262,144**; original Recursive announcement separately explicitly states supports **512k**, recommends **256k**. No claim of independent 512k test. Fix r2 `SOURCE_NOT_VERIFIED` label using actual archived original + URL at precise row and claim level.

### P2-03 — DeepInfer reproducible setup

Original saved DeepInfer README lines 24–28, `environ.py` 129–132 and 197. Use full `DEEPINFER_ENABLE_MTP_VARLEN=1`, `DEEPINFER_USE_NEXTN_DECODE` (default 5) in one settings example; separate `DEEPINFER_BATCH_INVARIANT=1 DEEPINFER_ENABLE_MTP_VARLEN=0` + fixed per-sequence `seq_seed` (NVIDIA only) for deterministic example; no implied compatible simultaneous sample. Validate snippet syntax/source; report `NOT_EXECUTED` if not actually run. Replace repeated restatement with explanations of what changes in path/results.

### P2-04 — Audio quantitative depth

From accepted Voxtral Evidence `task-18a859ebb1ef50040078.json` and Mistral original, reconstruct small STT/Realtime/TTS variant matrix with **real** FLEURS WER, cpWER, keyphrase recall, task sample conditions, prices/units/US/EU/self-host where original numerals present. Vendor-reported, not rerun; keep incompatible 9/35+/18/22 official conflicting counts distinct and AA raw missing. No hallucinated numbers.

### P2-05 — Low resource evaluation labels

From accepted `task-160489b77720f40bd1e1.json` and original OpenAI blog, distinguish **19/20 languages ≥83%** from exception **COBOL 72.1%**, separate public SQLite suite vs hidden COBOL byte parity, and annotate which GPT model and low/high effort, cost sample, Luna $0.77 vs Sol $3.48 denominator and vendor-only origin. Recheck 10.9 baseline, 40% and metrics before interpreting cross-bench; no false universal performance leap.

### P2-06 — Development API/SDK actual example

Include one source-aligned `/v1/decisions` JSON request+response example, bound to official guide and version; if not exactly source-supported mark `ILLUSTRATIVE_NOT_EXECUTED`, do not invent parameter names or example outputs. Distinguish 400 per request, cache writes billed separately, read/un-cached versions and TTL where verified (otherwise UNKNOWN), region/long-context conditions. TanStack AI stable-core vs experimental harness side-by-side table, DeepSeek model weights vs API vs extras: exact artifact-specific license and lifecycle.

### P2-07 — Natural Japanese + conclusion

Correct unidiomatic/false technical translations: speculative decoding "投機的／推測デコード" not "予定検証", `confidence-scheduled verification` properly sourced, agent translated by role as "エージェント" rather than vague "主体", catalogue "接続先一覧" vs live connectors, awkward security phrases. Remove repetitive paragraphs and add sourced mechanism. W43 closing five paragraphs exactly titled `今週の総括` **after P8, before bibliography**, say "性能・能力向上が報告された" rather than independently confirmed "向上した事実". Remove editor notes and pre-publication QA warnings from **reader-facing manuscript**; keep in separate QA file.

## 3. Deliverables and coverage closure

Create NEW edition-local `sources/2026-W43/execution/editorial-bypass/w43-r3-reader-preview-UNVALIDATED-20261025.md`, `w43-r3-citation-confidence-ledger.json`, `w43-r3-editorial-qa.md`, `w43-r3-source-crosswalk.md`, per-requirement artifact inventory with actual locations, explicit exception states, `sources/2026-W43/execution/SOL_W43_CORE_FREE_EDITORIAL_R3_POST_INDEPENDENT_AUDIT_HANDOFF.md` and session log/index. Keep original r1/r2 untouched. Give explicit 11-row findings closure matrix with `FIXED` vs `PARTIAL` vs `UNRESOLVED`, actual modified block IDs, trustworthy original archive pointers; report useful prose chars and deleted repetition, tables counted only when actual rows/columns valid.

TeX/PDF/Publication Preview still forbidden in this execution. Edition-local source QA is not Core Stage QA; do not manufacture any native receipt. Avoid new evidence selection/Architecture changes, W44 out-of-window promotion or false source verification. Source scarcity => **stop**, not invented summary or magic bypass.

## 4. Terminal stop conditions

Success only if no P1 in missing actual artifacts, no unsourced official FAQ certainty, transparent per-row source classes, truthful conditional 31 requirement coverage, valid conclusion placement, and all 11 findings closed/qualified. **Normal commit + nonforce push to the existing branch**, exact HEAD+Tree remote read-back. Stop: `SOL_W43_CORE_FREE_EDITORIAL_R3_POST_INDEPENDENT_AUDIT_REVIEW_READY`. This is NOT official `DRAFT_COMPLETE`; approved Human Architecture remains and later Publication Preview still pending. If unverified source prevents required actual artifact, stop with `SOL_W43_EDITORIAL_R3_SOURCE_BLOCKED` or `SOL_W43_EDITORIAL_R3_REQUEST_CHANGES` and precise evidence. Do not forge PASS.

Followup after r3: editorial Sol targeted closure of these 11, then separate independent read-only differential audit when warranted. No independent r2 audit result counts as r3 PASS.
