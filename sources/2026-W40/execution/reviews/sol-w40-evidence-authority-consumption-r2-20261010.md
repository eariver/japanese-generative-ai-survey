# Sol W40 Evidence Authority-Consumption Review r2 — bounded source-binding correction required

Decision: **SOL_EVIDENCE_SUBSTANCE_PARTIAL_PASS / FORMAL_AUTHORITY_BINDING_REVISION_REQUIRED**  
Review date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Existing work branch: `weekly/2026-W40-v2-work`  
Reviewed Muse r5 HEAD: `8afb94c5ae93f016e4dd0228f66c142a842cafbe`  
Reviewed Muse r5 Tree: `b3e75757e7528cab3fb9b30f58a7f283b8dcb81a`  
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Current canonical State: `CANDIDATES_NORMALIZED`, next `stage:evidence-materiality-completeness`; Evidence/Materiality/Completeness pending; Human gates pending/pending.

## 1. Execution integrity — PASS

- Muse r5 started at Sol-approved `266ae7d4e7091b848443d3c46a26edc25c2ba300`, tree `e8ee3918c285bed8de4328bb7e90ac0a1e44c98b`, and finished at the reviewed HEAD/Tree above. One direct fast-forward commit, **61 files**, all within `sources/2026-W40/`. No Shared Core v2, main, other edition, Git history rewrite, or Human Gate edit.
- Canonical Discovery 37 and Screening 37 remain intact; existing 35 canonical Evidence Tasks and r1 reviewer inputs retained. r5 materialized 35-record **revised reviewer inputs** (29 VERIFIED, 6 PARTIAL; 29 provisional MATERIAL, 5 HOLD, 1 CONTEXT) and **five PROPOSED Card candidates**, not yet 35 canonical Cards/Acceptance.
- No Evidence Acceptance, no `EVIDENCE_REVIEWED`, no Selection/Architecture/Human approval asserted.

## 2. SC-E01 frozen-Core compatibility projection — Sol approves the bounded **mapping semantics**, not automatic Evidence Acceptance

Independent reading of frozen `scripts/survey_evidence_v2.py`, r5 `build_projection_r5.py`, ledger and validator report:

- `PRIMARY_RESEARCH_ABSTRACT` → `PRIMARY_PAPER` for the exact two arXiv source records (Context Language Models and pre-window LIFT), preserving **abstract versus full-paper consumption** in explicit claim and source notes.
- `EVALUATOR_PUBLISHER` → `PRIMARY_OFFICIAL` for the **evaluator's own published benchmark report**, AA-AgentPerf-Local, not as a frontier model vendor or independent re-run.
- Exactly 3/35 derived task source-type fields projected; 32 passthrough; original tasks plus canonical Discovery/Screening source types not changed; old/new task SHA per row, `SOURCE_CLASS_MAP` failure reproduction, unknown-type FAIL_CLOSED, double-build deterministic, frozen `validate_evidence_package_basis` and `task_authority_sources` 35/35 PASS in r5.
- Sol review accepts this **edition-local narrow interpretation for W40**, exact mapping identity from `execution/compat/evidence-source-class-projection-r5/projection-ledger.json` (35 rows, 3 changes, compat package SHA-256 `0be7e105fa7d57cf4345969881dbde3f8762f5b72dfb6714be22af2379557c76`). This is NOT a patch or a generic resolution to existing CV2-DM-016, which remains OPEN_CORE.
- Formal acceptance MUST use a full frozen-Core package/Card pipeline with provenance-correct primary sources and obey actual validator failure/success, without manual "PASS" patching. Extending the derived package for supplement bindings necessarily changes its hashes; record a new r6 ledger and full r5→r6 lineage.

## 3. SC-E02 through E05 content review — bounded PASS / disclosed limitations

- **ELYZA:** First-release 33B Dense / 32B-A3B MoE exact pinned model cards read, official numerical tables separately checked by Sol against first-party Hugging Face: Overall **61.69** and **58.46**, Japanese **62.18** and **59.61**, along with M-IFEval-ja, Nejumi BFCL, LiveCodeBench, training recipe and evaluation footnotes. Benchmarks are **publisher-measured**, not independent reproduction. ELYZA should be a **MATERIAL Selection candidate** for the Japanese Weekly Survey (open weights, domestic foundation, JP data/reasoning/tool evaluation), despite trailing some global frontier peers; preserve countervailing per-task rows (JMMLU slight decreases vs specific base) rather than blanket "all scores improved." Screening MAYBE historic record untouched.
- **Context Language Models:** r1 false PDF-VERIFIED label withdrawn; r5 consumes author paper text via ar5iv §§1–6 plus partial App.A, not original PDF bytes. Metrics are author claims with explicit evaluation conditions; figures/Appendices B–F and code remain unconsumed. Sufficient for bounded preliminary Evidence on methods, not paper-wide reproducibility.
- **ProvenanceGuard:** Original paper substantive text + tables/evaluation reviewed via ar5iv; author-reported source-owner and source+relation accuracy distinguished; no independent reproduction. The claim-to-primary-paper Card binding must still be repaired (below).
- **Gemini Argon:** Corrected to publisher-announced **1M OUTPUT token limit** with rollout constraints, no inference of input-context or general availability.
- **Olmo-core 3:** original report `https://allenai.org/papers/olmocore3` exceeded Muse fetch limit >5 MB twice (markdown/text). Blog and repo existence consumed; quantitative figures remain Ai2-announced, report-body and code-level ablation verification **UNRESOLVED**. This is a bounded limitation, not automatic cancellation of the infrastructure candidate. Do not assert an independent technical reproduction.

## 4. SC-E07 — PRIMARY Card source-binding gap [FORMAL ACCEPTANCE BLOCKER]

Independent read of five r5 `card-candidates/*.PROPOSED.json` reveals:

**ELYZA** `card-w40-weak-elyza-20261002.PROPOSED.json` is `status=VERIFIED`, claims first-party model-card benchmark / Apache-2.0 / launch facts, but its **only** bound `src-1` remains `source_class=SECONDARY`, locator `secondary:huggingface.co/elyza/ELYZA-Thinking-1.0-llm-jp-4-32b-a3b`, title `(Oct 2, UNVERIFIED)`. Six `PRIMARY_FACT`/`PROJECT_CLAIM` lines all bind that SECONDARY source. This formally passes source-ID/legacy-class structural checks but **misstates the actually consumed issuer authority**. The historical Discovery SECONDARY record must NOT be overwritten or mislabeled. Bind the two pinned original model-card excerpts as new authoritative source entries via frozen Core's `Evidence Authority Supplement` with `PRIMARY_REPOSITORY` mapped source types/classes, exact source URL, content hash, dates/reader rights, and explicit task assignment; cite corresponding source IDs on claims.

**ProvenanceGuard** Card `w40-primary-provenanceguard-20260929` includes detailed original-paper Eq/Tables claims but its sole source is the **Sep 29 team blog**. The core-authored paper source is not an explicit bound source. Bind the manuscript excerpt separately via the canonical Evidence Authority Supplement (`PRIMARY_PAPER`, exact revision and content path/SHA); blog remains source of W40 in-window announcement, paper is pre-window research mechanism/evaluation authority.

**Context Language Models** card's `src-1` arXiv abstract is a valid first-party paper-identity link but the detailed equations/tables were read through ar5iv full text. For semantic source-role precision, an additional exact-version paper HTML/excerpt authority entry is recommended/expected in the same supplement, with distinction from PDF bytes not read. Do not pretend citation to the abstract alone proves specific Table/Eq or appendices.

Frozen Core actually provides `schemas/evidence-authority-supplement-v2.schema.json` and `survey_evidence_v2.build_evidence_authority_supplement()`; its validator checks specific task/Discovery IDs, the canonical Screening non-DROP decision, SHA/byte-count of Raw, exact source type → allowed source class, publication/access instants and binding uniqueness. Supplement source_type **must itself be in frozen `SOURCE_CLASS_MAP`**: for model-card repository use `PRIMARY_REPOSITORY`, for paper use `PRIMARY_PAPER` (do not use unmapped `PRIMARY_MODEL_CARD`). Supplemental sources do not erase the original Discovery-bound source and must be cited claim-by-claim.

The r5 report of `5/5 validate_evidence_card PASS` demonstrates **structural correctness only**, not claim-to-source provenance fidelity. Do not promote to formal accepted Evidence with a `VERIFIED` Card whose only authority is secondary/old `UNVERIFIED` when issuer primary was actually available and consumed.

## 5. SC-E08 — ProvenanceGuard arXiv version/date error [CORRECTION REQUIRED]

First-party arXiv `https://arxiv.org/abs/2606.18037` records **v1 June 16, 2026 15:10:29 UTC** and **v2 July 26, 2026 10:47:53 UTC**. Muse r5 and earlier Evidence repeatedly say paper `Aug 27` as publication or pre-window background. **That precise Aug 27 assertion is unsupported**. Correct all r6 reader-input/Card chronology to `paper v1 Jun 16 / v2 Jul 26, pre-window; Sep 29 team-blog exposition is the W40 event`. Identify which manuscript revision ar5iv rendered, and version-pin paper numbers to that revision. This does not turn the paper into a new W40 research publication.

## 6. Conclusion / next boundary

**Decision:** `SOL_EVIDENCE_SUBSTANCE_PARTIAL_PASS / FORMAL_AUTHORITY_BINDING_REVISION_REQUIRED`. The r5 science/method gap-fill and narrowly mapped Core compatibility are sufficient to authorize a **bounded r6 corrective Evidence Authority Supplement and 35-card PROPOSAL**, not a transition to accepted Evidence or Materiality/Selection.

What remains: create a truthful original-source binding for ELYZA/ProvenanceGuard/CLM using the official supplement mechanism, correct paper-version dates, generate all 35 task-complete factual Card candidates (including 5 revised records) under the exact new combined compat/supplement basis, and run **full Core Card validation with binding enabled**, handling any further source-role mismatch as a fail-closed finding. STOP for Sol final Evidence review. Sol will then authorize the actual Core Evidence acceptance/state/checkpoint with preserved audits or require a specific further repair.

W39 carryovers remain HOLD; Oct2 AstaBrief/AutoSynthData time uncertainty and Olmo report depth remain item-level limitations. Shared Core CV2-DM-016 remains OPEN; W40 recurrence logged on Issue #515, deferred Summary update due at edition closure. No Human Gate action.
