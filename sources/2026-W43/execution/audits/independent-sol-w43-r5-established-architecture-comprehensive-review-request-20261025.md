# J-GAS W43 — Independent Sol full Architecture audit AFTER trusted Stage establishment

Status: `READ_ONLY_INDEPENDENT_SOL_COMPREHENSIVE_AUDIT / POST_TRUSTED_ARCHITECTURE / PRE_HUMAN_APPROVAL`
Date: 2026-10-25 JST. This instruction is intended for a **new, separate Sol audit chat**; the editorial Sol and Muse are NOT the independent auditor.

## 0. Exact immutable audit subject (not latest branch)

Repository: `eariver/japanese-generative-ai-survey`.
Existing work branch: `weekly/2026-W43-v2-work`.
**Fixed independently audited subject commit**: `6f961295c6743248c2bccb34e15cb84116bf4de7`.
**Fixed subject Root Tree**: `6a1f716b024cf742162a95dfb0bace227ee29f5e`.
Reviewed `main`: `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen `production/survey-core-v2`: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
The branch may have moved after this request file was added. Always audit the fixed subject commit. Independently verify all three remote HEAD/Tree pairs where possible; mark unavailable as NOT_VERIFIED rather than copying expected values into PASS.

## 1. Actual Trusted Operator receipts, not just editorial approval

Selection separate operator request `sources/2026-W43/execution/requests/sol-w43-selection-r5-advance-20261025.json`, immutable request commit `f0b82346a16cac0eea091c39e1d6b8a786ca99ee`; operator-generated commit `bd381bb83d46a65eeaf92cfa8d5d9205723fd4b2`; Actions `https://github.com/eariver/japanese-generative-ai-survey/actions/runs/40180961257`; receipt `execution/bridge-runs/sol-w43-selection-r5-advance-20261025/receipt.json`, stage contract PASS, `EVIDENCE_REVIEWED→SELECTION_COMPLETE`, Selection checkpoint passed.

Architecture separate request `sources/2026-W43/execution/requests/sol-w43-architecture-r5-advance-20261025.json`, immutable request commit `bf5d8d14897c14d42931de0604df64df9255643e`; operator-generated audit target commit `6f961295c6743248c2bccb34e15cb84116bf4de7`; Actions `https://github.com/eariver/japanese-generative-ai-survey/actions/runs/40181179121`; receipt `execution/bridge-runs/sol-w43-architecture-r5-advance-20261025/receipt.json`, contract PASS, `SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED`, Architecture checkpoint passed. Final `production-state.json`: `ARCHITECTURE_ESTABLISHED`, `terminal_reason=HUMAN_GATE_REACHED`, `human_gates.architecture_review=pending`, `human_gates.publication_preview=pending`. These are claims to independently re-read, not assumed.

**CRITICAL HUMAN BOUNDARY:** machine Stage established does NOT mean independent technical/editorial PASS or Human approval. The user specifically chose one full independent audit AFTER this trusted Architecture Stage, replacing the earlier proposed r5 pre-Stage spot re-audit. Absolutely no Human Gate approval, Draft, TeX, PDF, publication or Core mutation.

## 2. Blind-first independent content audit (full breadth, explicit depth)

First inspect **actual** `sources/2026-W43`:
- `candidate-matrix-v2.json` 32 rows; `candidate-selection-v2.json` 32 assignments; `architecture-v2.json` all 8 packages and all 31 `must_cover_requirements`, purposes, boundaries, page estimates, publication availability, source claims and MUST-NOT; `architecture-review-summary-v2.json`; `architecture-review-attention-v2.json` all 68; the separate `execution/reviews/w43-human-selected-19-risk-register-r4.md` selected-19 risks; orchestration `selection-architecture-input.json` and `-audit.json`.
- Accepted r4 Evidence 32 Cards (manifest `evidence/v2/accepted/fb6e5900b09ee77453aeaaf904d76fb56091fc977d61f82e4154e6f3787cf72b/evidence-accepted.json`); accepted r4 Views 32 (manifest `evidence/v2/views/accepted/482a084e172d20450afe45c84933f69a0074a8244f823ae8b2589279d7d3858e/edition-views-accepted.json`); 51 Materiality rows, LIMITED Completeness, source supplement IDs and raw bytes where available. Inspect claim-to-source identity and actual first-party passages. Distinguish `RENDERED_ONLY` from archived actual raw and independently verified benchmark.
- Validate exact 32 decisions 19 SELECTED/1 HOLD/12 REJECT, 19 unique placements/0 missing/0 nonselected, 8 packages/31 cover entries, Attention 68/68 unique limit100 truncated=false, 5 standing LIMITED; selected-19 separate risk ledger completeness. Verify reference hashes and r4/r5 history snapshot SHA256 plus Core-validator receipts. If Core-native validation cannot be executed, mark NOT_EXECUTED.
- W43 cutoff exact `[2026-10-16T22:00:00Z,2026-10-23T22:00:00Z)`, issue-specific IN/OUT/FUTURE and publisher dates; 9 placeholder-midnight origins are NOT exact clocks; Kimi API early vs Nov4 weights future, GitHub Metrics 23:42:03Z postcutoff OUT, Grok audit binder NEVER_STORY.

**Independent investigation goals:** Examine deep technical mechanisms and verifiable source claim in *every* article group P1–P8, not just the 3 latest repairs; interrogate model/weight availability, licensing and param conventions, benchmarks and apparatus, default flags and implementation environment, cost and rate limits, scientific evaluation design, language/translation accuracy, page density versus source support. Avoid false comprehensive claims for long MemT paper math/ablation and Artificial Analysis original data you did not actually review.

## 3. Known issues to test without being anchored by Muse PASS

(1) DeepInfer deterministic sampling uses `DEEPINFER_ENABLE_MTP_VARLEN=0` + `DEEPINFER_BATCH_INVARIANT=1` + fixed `seq_seed` NVIDIA; separate DSpark variable MTP `MTP_VARLEN=1`, version pinned `9bd9cf24`; no simultaneous use. (2) Voxtral Mini TTS announcement 35+ languages/50+ dialects versus Mistral model card 9 languages versus language matrix 35/50+; presets 18/22 conflicting, 11-language evaluation not coverage; `UNRESOLVED_VENDOR_DOC_CONFLICT`, never invent reconciliation. (3) Nemotron 8B total/4B effective vs Flint 39.8B total/~2.5B active counting non-equivalent; OpenMDW-1.1 weights versus Gemma-4 base license. (4) FLUX speed actual vendor sources, PR 10.95 seconds vs blog/product 12.45 seconds compared to 277.80: 25.37x versus 22.31x, 95.52% decrease for latter; blog 26.5x/96.2% incompatible with shown inputs; vendor Elo delta +47 (blog) versus +50 (fal product/Oct19 publisher PR), 1139−1089=50; keyframes PR "available" versus Oct18 product FAQ only text/image launch, no proven W43 live schema/GA; original AA historical snapshot absent. (5) Decisions 400 questions PER REQUEST; cache writes billed, long-context/regional premiums, output tokens not charged does not mean free requests. (6) Review Attention 68 is exceptions only; separate selected-19 ledger. (7) P8 3.5pp/total 37pp are estimates, not guaranteed filler; must-cover depth. (8) Natural Japanese for algorithms/context biasing/cpWER, no spurious absolute "best". (9) Published/preview/GA/weights/reproduced statuses distinct. (10) R4-010 fixed r5 real `runner.generated_at=2026-10-25T09:22:08Z` before final r5 commit `fbe2f9b0da0932bc41df5a4365ea6c2ed58def13` at `2026-10-25T09:25:44Z`; old anomalous r4 12:00Z kept in r4 history, do not silently rewrite. (11) R4-011/012 as FLUX conflicts above. (12) Five Evidence limitations retained, not manufactured as fully reproduced.

After blind-first inspection, read independent r3 and r4 reports:
`execution/audits/independent-sol-w43-selection-architecture-r3-comprehensive-audit-result-20261025.md`,
`execution/audits/independent-sol-w43-architecture-r4-postfix-review-result-20261025.md` (normalized, not raw byte-identical),
`execution/reviews/sol-w43-architecture-r4-postfix-independent-adjudication-20261025.md`;
Muse r5 closure `execution/reviews/muse-w43-architecture-r5-postfix-3p2-closure-20261025.md` and fal source crosswalk `execution/source-intake/w43-r5-fal-official-source-conflict-crosswalk.md`; editorial Sol's user-directed stage authorization `execution/reviews/sol-w43-architecture-r5-stage-advance-editorial-acceptance-20261025.md`. Challenge them; search for NEW P0/P1/P2, not just repeat old claims.

## 4. Verdict/output and hard stop

Produce one detailed **Japanese** independent audit Markdown with exact fixed HEAD/Tree and remote check; methodology and independently executed versus reported/NOT_EXECUTED; full selected candidate/source coverage table; 8-package/31-section assessment, source-to-claim concrete citations, time/math/evaluation/license/availability/Japanese checks, Stage/receipt correctness; P0/P1/P2 findings with IDs, source URLs and precise JSON pointers, fix plan and remaining review scope. Return explicit **Selection and Architecture independent** `PASS` / `PASS_WITH_LIMITATIONS` / `REQUEST_CHANGES` and **whether it is appropriate to present the Human Owner with an Architecture Review** (independent auditor must NOT approve gate). Any critical unsupported upstream Evidence/Selection assertion -> `SELECTION_REVIEW_REQUIRED`, not a stealth rewrite.

Save the original to Google Drive folder `GPT-Sol_Review` as `YYYYMMDDHHMMSS_SolReview.md` if available; only report SHA256 of genuinely computed original raw bytes. If Drive write unavailable, provide full Markdown so Human Owner/editorial Sol can save. Do NOT mutate GitHub, issue/comments, source, operator requests, Stage, State, Core, human gate or publication.

Stop after read-only audit report and return result for editorial Sol adjudication. Human Architecture Review **remains pending**, no Draft/TeX/PDF.
