# W43 Muse r3.2 — Independent r3.1 1×P1 / 3×P2 Core-free editorial correction

Status: `SOLE_MUSE_R3_2_EXECUTION_CONTRACT / INDEPENDENT_R3_1_REQUEST_CHANGES / NO_CORE_REPAIR / NO_NATIVE_STAGE_ADVANCE / NO_RENDER`
Date: 2026-10-26 JST.
Repo: `eariver/japanese-generative-ai-survey`. Existing branch ONLY `weekly/2026-W43-v2-work`.
**Exact starting work HEAD and root tree will be provided separately by editorial Sol after THIS file is committed.** Do not use r3.1 audit subject SHA or previous moving HEAD as execution start.
Reviewed main HEAD/tree fixed: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core branch `production/survey-core-v2` HEAD/tree fixed: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## 0. Required 6-way safety preflight

Before any repository writes independently verify REMOTE work/main/frozen exact HEAD+root Tree against all six Sol supplied values. Any mismatch = STOP `STOP_ZERO_WRITES`, report actual and expected. Existing branch only. Clean local checkout solely fast-forward behind expected work HEAD may be synchronized **after remote guard** via `git fetch` + `git merge --ff-only`; reverify local and remote exact SHA/tree. Divergence, dirty checkout or unexpected local SHA = STOP. No new/review/fallback branch, reset, rebase, force, merge commit, protected Core edits, or State/Gate changes.

## 1. Exact inputs/read order

1. Full independent Sol report `20261026005634_SolReview.md` (34,589 raw bytes, SHA256 `fbbc9cb3efb512dbb31c9e09af12b54469e178b593058cd2591b1cb439788fcf`; if not available in Muse environment, use full 4-point Sol ruling below + indexed audit receipt, disclose original attachment unread).
2. Binding editorial Sol adjudication `sources/2026-W43/execution/reviews/sol-w43-r31-independent-editorial-audit-adjudication-20261026.md` and audit provenance receipt `sources/2026-W43/execution/audits/independent-sol-w43-r31-editorial-differential-result-receipt-20261026.md`; prioritize the exact original residual issue IDs `P1-A01/P2-A02/P2-A03/P2-A04` over any old historical Muse self-PASS label.
3. **Immutable audit subject** `9d3a3de06dc4478411a68bc7817ce74431bff01e` root `5214ef2e0e932065769905127eee8078fe709119`. Existing source editor assets `sources/2026-W43/execution/editorial-bypass/w43-r3-1-reader-preview-UNVALIDATED-20261025.md`, `w43-r3-1-citation-confidence-ledger.json`, `w43-r3-1-source-crosswalk.md`, `w43-r3-1-editorial-qa.md`, source snapshot `execution/source-intake/w43-r31-decisions-guide-snapshot-20261025.md`. r1/r2/r3 remain immutable history.
4. Human approved Architecture r6, 31 must-cover sections, 19 selected, original five LIMITED and 68 Review Attention; approved Human gate record, real State `ARCHITECTURE_ESTABLISHED`, machine Draft checkpoint pending and Publication Preview pending. Original native Core defect remains blocked; do not invoke any frozen Core native drafting/validator in this task.
5. Accepted Evidence/Views and source archived raws for every affected claim, especially Voxtral `sources/2026-W43/evidence/v2/accepted/dbc27cd8d5323c802bfb77c6fb4d6c917ba745417191da945c5ae8dbbdbad900/results/task-18a859ebb1ef50040078.json` (claim2 WER/cpWER/recall, claim3 pricing; derived Evidence, NOT original source cells), OpenAI Low-resource task-160489b77720f40bd1e1 in same accepted collection, saved MemT README licence lines208–219, and TanStack release + npm independently verified timestamps. See r3.1 crosswalk for status of absent vendor source originals.

## 2. Four bounded corrections (no breadth expansion)

### P1-A01 / blocking — new five TABLE rows must be source-resolved
Fix the existing r3.1 ledger and reader by writing NEW r3.2 assets; old history unmodified. For **each of exactly five additional comparison tables** `p2-f2`, `p5-f1`, `p7-f1`, `p8-f2`, `p8-f3`, create a non-empty, complete `table_rows[]` matching every actual displayed row and its major claim. Keep the existing 15 tables' row arrays intact and preserve 96 distinct block IDs; 20/20 table objects should have `table_rows[]` **and** no unmatched body row; count row-level source quality separately from array presence.
- Each row must include at least stable `row`, `product`, `url` (or null with why), `clock` (exact/day-only/unknown), `source_class` and `note` compatible with existing row shape.
- **For every independent factual subclaim** include claim-level source anchor (e.g. `claims[]` objects or `claim_refs[]`) with `value`, `metric`, `unit`, `denominator/comparison`, `model/version/variant`, `evidence_task_id/claim_id` and `archive_path` when real. Do not force spurious units for licences; distinguish `not applicable`, `unknown`, `not independently verified`. A per-row URL cannot stand for every metric or for a different model.
- Table `p2-f2`: paper source CC BY-NC-SA 4.0, original software PolyForm Noncommercial 1.0.0, third-party MIT, weights/datasets excluded with explicit scope; correct archived README.
- `p5-f1`: STT/Realtime/TTS/LiveKit rows; apply P2-A03 granular numeric source requirements below.
- `p7-f1`: languages (COBOL72.1 exception to 19/20≥83%), compared model/effort/harness/hidden vs public and $0.77/$3.48 denominator; if row mixes series, split claim refs within it. All publisher reported, not external benchmarks.
- `p8-f2`: TanStack GH published_at Oct22 15:18:14Z, npm 1.0.0 Oct22 15:21:49Z, stable core1.0 vs experimental harness0.x, and separate out-of-window Metrics; **each independent source clock must have own citation ref**. Do not make GH API prove npm timestamp.
- `p8-f3`: weights vs API vs add-ons—licence per artifact, HF/ModelScope SHA NOT independently read, Search/Fetch fee/free period as publisher claim not tested, harness/version and benchmark not independently replicated.
- For absent publisher original **do not invent, fabricate, or elevate status**: `DERIVED_ONLY/SOURCE_REPORTED/UNRESOLVED/SOURCE_NOT_VERIFIED` with exact gap. If a row factual detail has no acceptable accepted Evidence trace, remove or explicitly qualify the claim in reader. Add reader `典拠キー` for rows/footnotes, and new table audit crosswalk including exact file and original clock. No changes to canonical Matrix/Selection/Evidence/Architecture.

### P2-A02 — FAQ source attribution, NOT approved Architecture recoding
Inspect all P4 reader occurrences of `UNRESOLVED_VENDOR_DOC_CONFLICT`, `公式資料間`, `FAQ`, `二様式` relating to FLUX keyframes and ledger `p4-p2,p4-p7`. As original FAQ URL, version and dated first-party bytes are UNKNOWN, **do NOT treat it as a verified official conflicting publication**. Use editorial status `UNRESOLVED_FAQ_ATTRIBUTION` / `UNVERIFIED_CONTRARY_DESCRIPTION`, explain whether source is unlocated. Fal PR/blog statements retain properly sourced first-party attribution only where verified; live/schema/GA remain UNKNOWN; 10.95 vs 12.45 arithmetic and Elo vendor contradictions unchanged. Canonical Architecture may still contain historical label; state expressly that label is a legacy candidate conflict awaiting raw source verification, not evidence to assert official-FAQ origin. No Architecture revision.

### P2-A03 — Voxtral evaluation/payments source-precise
For `p5-f1` and relevant P5 reader paragraphs, identify from directly obtainable frozen accepted sources exactly:
- FLEURS WER `4.1/4.0`, diarization cpWER `18.4/18.6`, keyphrase recall `94.6/81.4` — **which model/variant, baseline and sampled units** each value denotes. If accepted card or archived primary does NOT specify a comparator, split/qualify as `COMPARATOR_UNVERIFIED`, do not guess who the comparison is against. Preserve vendor evaluation vs independent experiment.
- agent API `$0.04/$0.08` pricing must carry actual invoice unit from primary source; if unlocatable, `UNIT_UNVERIFIED` or omit the values from reader; **no invented per-minute/per-token pricing**. Other Mini/Small/Realtime/Speech prices retain units only when confirmed.
- STT claimed 50+ languages vs 11-language benchmark sample vs Realtime 35+ supported languages and 40+ dialects, vs any marketing "40+" statement, each named model and source/clock. TTS 35+/9/35/18/22 conflict stays UNRESOLVED, no simplification.
- Re-evaluate §5.1 and §5.2 truth states and only upgrade from PARTIAL if concrete validated row attribution and comparative conditions now exist; original vendor archive gaps can still legitimately remain PARTIAL.

### P2-A04 — DeepInfer code identity; reader-facing hygiene
The P2 `SamplingParams(seq_seed=1234)` line is not independently executable without a source-verified import; label it explicitly `構成の抜粋／疑似使用例・NOT_EXECUTED・IMPORT_UNVERIFIED` if original archive cannot prove import. **Do not fabricate an import from a guessed library or run it**. The mutually exclusive env configuration and source-confirmed symbols stay correct. Do not present partial Python fragment as copy-paste complete program.
Remove W43 operator-only provenance/status and "UNVALIDATED" notice **from within the reader-facing Markdown body** in a NEW r3.2 reader-export; keep a truthful `UNVALIDATED` in the filename plus internal QA and metadata sidecars. Do not hide limitations from real human production approvals. Consolidate repeated warnings for P2/P3/P4/P5 into concise footnote or scoped condition table where possible, with no loss of necessary uncertainty.
Preserve **final title exactly「今週の総括」, five substantive paragraphs, directly after P8** and no final editor note. No P9.

## 3. Re-evaluate 31 requirements honestly (independent baseline 26/5)

Independent r3.1 audit grades `SUBSTANTIVE_COMPLETE=26 / PARTIAL=5` (§1.4 Kimi/Nemotron benchmark comparator, §2.2 illustrative non-runnable DeepInfer code, §4.1 missing FAQ official attribution, §5.1 unresolved Voxtral population, §5.2 numeric comparator/units). This independent basis supersedes Muse r3.1 self-report 29/2. Create explicit per-requirement r3.2 five-state matrix `NOT_ADDRESSED/MENTIONED_ONLY/PARTIAL/SUBSTANTIVE_COMPLETE/NOT_VERIFIABLE` with actual reader evidence and original source proof. Upgrade only if source-backed substantive repair, never because a row or label exists. `PARTIAL` may remain with truthful explicit limitation. Count `SOURCE_VERIFIED` separate from `EDIT_CLOSED`; 96 ledger rows and inherited 5 LIMITED/68 Attention remain traceable.

## 4. Required edition-local outputs and QA

Write **new files only**, preserving immutable r1/r2/r3/r3.1:
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-reader-preview-UNVALIDATED-20261026.md` (P1–P8 plus final five-paragraph summary; reader view without operator meta).
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-citation-confidence-ledger.json` (96 block IDs, 20 actual table_rows with value-level provenance).
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-source-crosswalk.md` (row/claim→publisher/archived direct sources, observed date and source tier; unknown explicit).
- `sources/2026-W43/execution/editorial-bypass/w43-r3-2-editorial-qa.md` (four-point closure; 20-table exact row counts, P5 numeric class, 31 5-state depth audit and source confidence breakdown, duplicated-warning reduction; reader length same-method).
- `sources/2026-W43/execution/SOL_W43_CORE_FREE_EDITORIAL_R3_2_INDEPENDENT_4POINT_HANDOFF.md`, session worklog and navigation index.
- Optional extra `execution/editorial-bypass/w43-r3-2-table-row-validation.json` with row-key mapping for independent checking; NOT a native Core artifact.

Test all 20 tables have row arrays and match displayed rows/claims, 96 IDs unique, no accidental claim substitution or cross-period releases, no invented numeric units, no renderer-layout PASS. Prepare precise r3.1→r3.2 text+ledger diff and exact SHA hashes / source anchors; report all P1/P2 `FIXED/PARTIAL/UNRESOLVED`. Actual post-edit independent audit has NOT yet happened.

## 5. Stop authority / protections

No modification to `scripts/`, `schemas/`, `config/`, `.github/`, frozen or main branch, accepted Evidence/Views, Candidate/Matrix, Selection, Architecture, Summary, Attention, production State, Machine checkpoints, Human Gate, old receipts, or earlier r1/r2/r3/r3.1 artifacts. NO native Draft runner, NO fake `DRAFT_COMPLETE`, `ADVANCE_STAGE`, PDF/TeX, Publication Preview, Freeze, Release. Human Architecture remains approved; publication authorization has NOT been granted.
If some P5 metric is impossible to source, mark `UNVERIFIED` and qualify/omit instead of making it up. If a P1 row cannot be sourced even to accepted Evidence so the prose would become misleading, stop `SOL_W43_R3_2_SOURCE_BLOCKED` with exact incomplete row and why. Otherwise new r3.2 normal commit, non-force push, fixed remote HEAD+Root Tree readback, report real lifecycle/gates unchanged. Stop `SOL_W43_CORE_FREE_EDITORIAL_R3_2_READY_FOR_SOL_SPOTCHECK`; later Sol independently spotchecks and arranges read-only fixed-subject narrow audit of four new issues before any publication discussions.
