# W43 Sol Evidence r2 independent audit — substantive improvement, factual/provenance REQUEST_CHANGES

Status: `SOL_EDITORIAL_EVIDENCE_R2_REQUEST_CHANGES / NO_STAGE_ADVANCE / FIVE_RECORD_REPAIR_ONLY`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Reviewed work branch `weekly/2026-W43-v2-work` HEAD `8aeafe90c43e44a96a1b181c0d3b685046e1433d`, Root Tree `a53b75069b8a72df092c84365822368690f14132`.
Actual parent `6a3898771038d64fc2cd6a911c4445177d43a8e2`.
Reviewed main HEAD/Tree `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core HEAD/Tree `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## Reviewed authority

- r2 handoff `execution/SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r2.md`, actual 152-path edition-local commit, r2 Evidence Card/Edition View acceptances, r1 historical acceptance and archive, r2 interactive source records, source-depth notes, four official primary attempts, six actual Evidence Authority Supplement entries, r2 seven-ID derived-only compatibility projection, Materiality/Completeness, frozen State.
- Exact accepted Evidence: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/evidence-accepted.json` (32 PARTIAL, no NEEDS_MORE). Views: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/edition-views-accepted.json` (20 MATERIAL / 11 CONTEXT / 1 NON_MATERIAL, 0 HOLD). Core-derived Materiality 51 rows: 20 / 11 / 1 / 19 EXCLUDED; Completeness `LIMITED` and original 12 W42 carry dispositions intact. Four former INSPECT/NEEDS_MORE source bodies addressed (3 MATERIAL, 1 CONTEXT); MemT 7,096,280-byte PDF genuinely archived and recognized as separate from AM-Bench 2,379,235-byte PDF.
- Exact 32 interactive-record r1→r2 comparison: only **five** discovery IDs substantively changed: `w43-primary-automode-20261021`, `w43-primary-decisions-api-20261022`, `w43-primary-patch-planet-20261021`, `w43-primary-openai-cloud-20261021`, `w43-r2-memt-20261019`. Other 27 records structurally unchanged, source identifiers stable. No manual changes to accepted Discovery/Screening or original r1 Evidence/Views.
- Genuine raw HTML three files archived (Anthropic 599,884B, OpenAI API changelog 553,250B, GCP announcement 224,991B), original HTML syntax present and document text visible. Original OpenAI Decisions API and Patch the Planet article pages were rendered-read only due to bot-wall; worker marks `RENDERED_BODY_READ_NOT_BYTE_ARCHIVED` honestly. Real MemT PDF 7,096,280B archived; source artifact supplement manifest can be counted directly. The r2 supplement manifest actually has **six** sources, not the handoff's claimed eight: 2 retained r1 paper PDFs plus 4 added (auto-mode HTML, Decisions changelog, GCP HTML, MemT PDF).
- Worker reports unchanged frozen Core-native agent-first Evidence/Views/Materiality/Completeness validation, Stage scratch precheck PASS, negative integrity tests PASS; Sol independently read back the records and files, not the complete worker-local CLI stdout. Legacy Core issues #568/#569 remain OPEN; no permission to edit frozen shared Core.

## Human decision

**NONE / NOT_APPLICABLE.** This is Sol's editorial/factual authority audit, NOT a Human Architecture Review or Publication Preview. Both real Human Gate values remain pending. **Do not run trusted `ADVANCE_STAGE` now.** Editorial result `REQUEST_CHANGES`, because publication-facing scientific/model attribution and exact provenance must be repaired before moving State.

## Requested changes

### CR-01 (mandatory factual correction): Patch the Planet model misattribution

The r2 accepted Patch Evidence Card `w43-primary-patch-planet-20261021` (result filename `task-5d21d93e7679f5441b8a.json`) claim-1 says **`Calif via GPT-6 Sol`**. Sol independently checked the **actual OpenAI official English source** `https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/` and official JP `https://openai.com/ja-JP/index/coordinated-disclosure-of-critical-vulnerabilities/`: the exact attributed model is **`GPT-5.6 Sol`** (Oct 21). This is a factual entity/model-version error in a MATERIAL security story, not a harmless notation. Correct all *new* interactive claim, accepted card, View rationale and any other derived narrative usages of the model name; preserve the original r2 accepted bytes for audit and do not invent a different model name.

Official source: `https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/` (October 21 2026). Primary page specifically says Calif used GPT-5.6 Sol to identify a critical PHP flaw and Wiz independently discovered/reported both flaws. No CVE ID need be guessed; preserve publisher attribution and vendor-claim class.

### CR-02 (mandatory provenance): Patch actual official URL is not attached to claim's source_id

The accepted Patch Card `sources[0].url` is `primary:openai.com/index/patch-the-planet` inherited from accepted Discovery, whereas the actual article consumed by r2 and relied on for new vulnerability, PHP, coordination and Daybreak claims is `https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/`. The Card currently has **no new supplement source** and every expanded factual claim refers only to `src-1` linked to that unrelated/inexact pseudo-URL. This defeats exact claim→source traceability, even if the publisher's article is genuine.

Preserve original accepted Discovery (do NOT rewrite it). Capture the true official English/JP article in an authentic task-bound derived rendered-document archive where bot-wall prevents raw HTML, explicitly labeling capture type, exact retrieval origin/time and SHA; use the **existing frozen Evidence Authority Supplement schema** if compatible with an honestly labeled rendered text source. If unable to create an authentic supplementary source through frozen validation, at minimum produce an edition-local exact original→canonical URL resolution ledger with genuine retrieved paragraph/section provenance and adjust Card citations only through the allowed Core APIs; **do not claim a false first-party raw HTML archive, invent a source ID, or invent a validator PASS**. If exact primary source binding remains unsound, stop BLOCKED and report the cause rather than promoting EVIDENCE_REVIEWED.

### CR-03 (mandatory provenance): MemT README-only license claims attributed to paper-only sources

The corrected r2 MemT Card `w43-r2-memt-20261019` has only two `sources`: `src-1` (arXiv abstract locator) and `supplement-src-927931f4a303eaa6` (authentic MemT paper PDF). Its claim-3 and verification reference a **repository README** for `CC BY-NC-SA / PolyForm Noncommercial / weight-licensing not covered`, while acknowledging that **the PDF has no such terms**. But there is no separate repo README source bound to those license assertions.

Identify the actually read upstream MemT repository README and anchor license/source-control claims to its *own genuine first-party source* and raw SHA/capture if retrievable; use exact task-bound authorized supplement source only for content genuinely consumed. Alternatively conservatively remove/downgrade unsupported precise license language and mark license verification unresolved. **Do not cite the PDF as proof of license terms it does not contain.** Retain actual MemT 7,096,280B PDF archive and mechanism/benchmark evidence as-is; distinguish training/equations/README terms and vendor unreproduced claims. Correct `tech-report-pdf` finding that currently calls nonexistent paper license sections "consumed" without a truthful qualification.

### CR-04 (execution metadata errata only, do not alter old handoff)

- r2 handoff/session starting work Tree is written `b8e1a207edb3cc92827284241e486ce4683612` (incorrect). The real Git Tree of exact Starting parent `6a3898771038d64fc2cd6a911c4445177d43a8e2` is `b8e1a207edb3cc82927284241e486ce468360642`. The actual parent of r2 commit is correct and independent HEAD matches; preserve original worker logs, file an exact SHA transcription erratum.
- r2 handoff says `8 entries` in Evidence Authority Supplement but the actual JSON has **6** (2 retained paper sources + 4 new), which is logically consistent with its narrative "2 carried + 4 new". Correct in an r3 erratum, not by rewriting historical r2 handoff.
- The r2 "VERIFIED" evidence-target findings reflect **publisher text/description read** rather than independent reproduced behavior; keep this distinction conspicuous.

## Regeneration boundary

**W43 edition-local Evidence r3 bounded factual and provenance correction only**. Keep old accepted r1 and r2 Evidence/Views immutable, as well as r1/r2 raw sources/PDFs, r2 materiality/completeness history snapshot, accepted Discovery/Screening, Grok Raw, Frozen Core/main, State/checkpoints and Human Gates. Reconstruct r3 Core-accepted 32 Evidence Cards and 32 Views from r2, showing explicit per-field changes limited to Patch source/model assertions, MemT README/license/provenance, bindings and downstream hashes; original 27 unaffected records must remain semantically the same. Materiality should reflect same evidence strength unless new facts warrant change; do not force selection. Generate new content-addressed Evidence and Views, and dependent Materiality/Completeness from exact frozen Core-native adapter; validate 32 IDs, seven derived-only source class projections, authority supplement, raw bytes/sha, negative tests and Stage scratch precheck. If all PASS, stop for Sol final readback. **No `ADVANCE_STAGE`, Selection, Architecture, manuscript/PDF or Human Gate**.

Stop `SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_READY_R3`; on failure `BLOCKED` honestly with no forged PASS. Shared Frozen Core v2 MUST remain untouched; Issues #568/#569 remain open.
