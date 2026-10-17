# W42 Sol Discovery Completeness Review r2 — REQUEST_CHANGES / temporal-boundary repair

Review date: 2026-10-17 JST
Reviewed HEAD: `4d8247aaf9f1999d15017e7d28bf18f5a03234a2`
Reviewed canonical main: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`
Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
Verdict: `SOL_DISCOVERY_COMPLETENESS_REQUEST_CHANGES__TEMPORAL_PROVENANCE`
Core Discovery Acceptance: NOT AUTHORIZED. State `ISSUE_INITIALIZED`; all Human Gates pending.

## 1. Review result

Muse r2 successfully addressed the Sol r1 discovery source-gap findings: 7 first-party missed events, six r1 SEARCH_CONFIRMED upgraded to body-consumed notes, 49 proposal records, source-lane sweeps, and 73 Daily X topics classified in disjoint categories (40 PROPOSED, 13 DUP, 4 OUT-BG, 16 OMITTED), preserving all seven raw originals. The new candidate content and source-body distinction are substantially improved. Scope was correctly bounded; no acceptance/Screening/Evidence or Gate was fabricated.

**Blocker:** independent temporal audit found two r2 misclassifications of source dates and one authority-label overstatement. These concern Daily X event vs. underlying-source time and therefore must be repaired before Sol approval.

## 2. Mandatory correction A — AgentHorizon (material)

Record `w42-dailyx-agenthorizon-20261010` in `discovery-v2-proposal-r2.jsonl` states `arXiv 2610.11050 submitted Oct 8 IN-window` (both summary and provenance reason). This is FALSE against current W42 UTC half-open window `[2026-10-09T22:00:00Z, 2026-10-16T22:00:00Z)`.

Primary arXiv: https://arxiv.org/abs/2610.11050 (v1: 2026-10-08 01:03:48 UTC). This is 44h 56m before W42 start, not inside the window. The 2026-10-10 X *discussion* is inside W42; the underlying paper is outside.

Required: update proposal and crosswalk (and any claims in supplementary reports): `UNDERLYING_PAPER_OUT_OF_WINDOW / X_POST_IN_WINDOW / BACKGROUND_OR_DISCUSSION_ONLY`, unless an independent *new* W42 event/benchmark publication is documented. Preserve original Daily X link and topic provenance. Underlying out-of-window arXiv cannot be used as a newly released W42 research result. If a source makes it technically important as a sidebar/comparator, justify separately at Screening/Selection and not as a W42 paper launch. Do not erase the lead silently.

## 3. Mandatory correction B — Qwen Image Turbo

Record `w42-lead-qwen-turbo-20261011` and r2 collector `papers-qwen-aws-deepseek-jp-serving-20261017.md` describe Oct 9 open weights as an `IN-window` trigger. A 2026-10-09 **day-only** model/weight release is insufficient, because W42 starts at 2026-10-09 22:00 UTC (2026-10-10 07:00 JST), and ordinary Oct 9 dates could fall outside. A Japanese contemporaneous report at 2026-10-09 23:59 JST already described downloadable weights; the launch predates W42's 2026-10-10 07:00 JST start. Cross-check original checkpoint creation and official announcement UTC time before a W42-IN claim.

- First-party listing: https://www.alibabacloud.com/help/en/model-studio/newly-released-models (2026-10-09 entry).
- First-party model: https://modelscope.cn/models/Qwen/Qwen-Image-2.1-Turbo (updated 2026-10-09).
- Japanese contemporary reporting: https://pc.watch.impress.co.jp/docs/news/2147316.html (2026-10-09 23:59 JST).
- The separate `Oct 14 hosted API event` must be proven from a dated *event* release entry, not a Model Studio page's later update timestamp. Treat `updated_at` as document timestamp, not proof of launch. If no distinct in-window API launch is corroborated, mark as W42 discussion/background, not an in-window release.

## 4. Source-body provenance correction

`w42-dailyx-grok-scale-20261015` uses `capture_class=CLAIM_LEVEL_DERIVED_NOTE__BODY_CONSUMED` while raw_paths cite only the Daily X report. This proves the Daily X markdown was read, not that the original X post was independently consumed. Mark `DAILYX_RAW_CONSUMED__ORIGINAL_X_UNVERIFIED` or whichever legal schema value preserves this distinction; do not invent core enum or unverifiable raw X evidence.

Independent Grok native X research has NOT been executed; `REQUIRED_BY_PROFILE` lane remains `AWAITING_GROK/PARTIAL`, and must be resolved through operator/appropriate exception before a final claim of full intake.

## 5. Narrow next action

One **bounded r3 temporal repair**, not new full collection. Use previously consumed original material, fix only affected edition-local proposal/crosswalk/reports plus validated derivative artifacts, annotate diff and preserve 49 candidate rows unless a formally justified disposition requires otherwise. No change to frozen Core, main, W41, or Human Gates. Keep W42 State `ISSUE_INITIALIZED`, no Discovery Acceptance/Screening/Evidence/Architecture/PDF. Stop for fresh Sol review with exact hashes, before/after datetime classification and source-level authoritative proof. Independently reconfirm r2 changes actually on remote and schema-valid.

## 6. Other limitations carried

Paper PDF full texts not parsed, licenses (Muse Model License, OpenMDW) and important benchmark denominators unconsumed, community performance sparse, and Grok independent X pass remains pending. Those are authority limitations rather than invented PASS status. r2 is a strong improvement, but cannot be signed as complete while hard factual cutoff misclassification persists.
