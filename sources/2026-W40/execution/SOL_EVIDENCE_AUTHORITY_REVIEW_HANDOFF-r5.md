# SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF-r5 — 2026-W40 (Muse r5, 2026-10-10Z)

Status: `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` candidate — Sol independently re-audits and decides Evidence Acceptance vs further gap-fill. **REVIEW_PENDING; no Sol PASS forged; NO formal Evidence Acceptance; NO Core State transition.** Canonical state stays `CANDIDATES_NORMALIZED`.

## 1. Identity, ancestry, allowlist, readback, invariants

- Starting HEAD `266ae7d4e7091b848443d3c46a26edc25c2ba300` / Tree `e8ee3918c285bed8de4328bb7e90ac0a1e44c98b` (remote read-only match; local ff-only sync, NO reset). Reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (match). R4 ancestor PASS.
- Final HEAD / Tree: filled at commit (normal commit, non-force ff push, remote read-back verified).
- Changed-file allowlist (all `sources/2026-W40/`, NO Core/branch/Gate/State-transition writes):
  - `execution/compat/evidence-source-class-projection-r5/` (build script + 35-task compat-package `0be7e105…` + ledger + validation report)
  - `collectors/primary/runs/20261010T060000Z-muse-r5/` (5 md: 2 ELYZA excerpts + CLM excerpt + Guard excerpt + Olmo failure log; run/index json, schema PASS)
  - `evidence/v2/results/r5/interactive-evidence-r5.json` (35 records) + `r4-r5-diff-ledger.json` + `card-candidates/` (5 PROPOSED cards)
  - `evidence/v2/views/draft-r1/views/` (5 views updated, bindings unchanged)
  - `execution/sessions/muse-w40-r5-20261010.md` (NEW) + this handoff + `execution/index.md`
- Preserved byte-identical: 37 Discovery, 37 Screening acceptance, 35 package tasks, r1 evidence file (history), Grok Raw 20477B, DailyX 64, W39 HOLDs.
- State: `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; evidence/materiality/completeness pending; gates pending/pending. No `evidence-accepted.json`, no checkpoint, no transition.

## 2. SC-E01 projection proofs (original/projected SHA graph, Core pass/fail, negative tests)

- Failure reproduced on exactly 3 tasks with verbatim frozen-Core errors (ledger `reproduced_failures`): contextlms + lift (`PRIMARY_RESEARCH_ABSTRACT`), agentperf (`EVALUATOR_PUBLISHER`).
- Reviewed narrow map: `PRIMARY_RESEARCH_ABSTRACT→PRIMARY_PAPER` (abstract-only depth noted; arXiv-submission role), `EVALUATOR_PUBLISHER→PRIMARY_OFFICIAL` (evaluator-own-report ONLY; not vendor; not independent reproduction).
- Projected SHAs: lift `9276f5a3…→0e157574…`, agentperf `52585ecd…→c8299fc8…`, contextlms `c1d1027c…→07091638…`; 32 passthrough byte-identical (only-source_type-drift invariant enforced per task). Compat package `0be7e105fa7d57cf4345969881dbde3f8762f5b72dfb6714be22af2379557c76`.
- Frozen Core: `validate_evidence_package_basis` PASS; `task_authority_sources` 35/35 PASS; negative injection (`BOGUS_UNREVIEWED_TYPE`) FAIL_CLOSED_PASS; double-build identical. Full r5 doc validates WITH task-source bindings against projected package (35/35).
- PROPOSED_NOT_ACCEPTED: originals preserved; canonical source_type strings untouched; acceptance use requires Sol authorization of this exact ledger. Core diff empty (no patch).

## 3. ELYZA deep consumption + provisional materiality (SC-E02)

- Sources (exact): 33b pinned README @`6ca556b` (33.6 kB) + 32b-a3b @`5260ecc` (36.5 kB), full bodies read; bounded excerpts archived with SHAs.
- Consumed: frontmatter (Apache-2.0/JA-EN/bases), Highlights (domestic foundation, JA-localized reasoning/SFT data, Wiki/Wikidata knowledge), Average-performance method (7 groups), FULL Benchmark Results (33B 61.69/JA62.18/EN59.72 vs base 51.50; MoE 58.46/JA59.61/EN55.94 vs base 46.38; JA deltas M-IFEval-ja +18.36/+18.70, Nejumi +34.95/+30.31, LiveCodeBench +24.63/+26.80; trails Qwen3.5-27B 68.18/Gemma4-31B 70.54 and MoE peers), footnotes (parallel-call floor, temp/effort/max-output), 3-stage method (mid-training/SFT-millions/RLVR-loopholes-closed), quickstart/cites. Chart images explicitly unread; quickstart unexecuted.
- Dense vs MoE + base distinctions consumed (names/tags/backends; active counts beyond names unstated). Oct-2 first-publication cross-checked (createdAt day). No score promoted without tables.
- Provisional materiality: MATERIAL (reviewer input) — in-window Japanese-vendor open-weight release with complete JA method + tables, directly material to a Japanese survey. Counterfactual HOLD: global-frontier-rank lens (trails Qwen3.5/Gemma4) could HOLD as non-frontier. Screening MAYBE immutable. Sol decides.
- Status VERIFIED; targets elyza-dated-pin + license-file VERIFIED (+ benchmark consumption folded into dated-pin finding for exact card-contract coverage).

## 4. Paper-body read checks / failures (SC-E03/E05)

- CLM: full text §§1–6 + refs + App.A READ via ar5iv (Eq.1–6, ContextBench, zero-shot deltas, RL Table 2, SCR 65%, §6 injection persistence, code URL, authors/funding); bounded excerpts archived. Direct PDF fetch returned BINARY (metadata only) → pdf-bytes UNRESOLVED; target renamed (r1 FALSE pdf-VERIFIED withdrawn). Figures garbled, Appendices B–F unread, code unopened — all explicit.
- ProvenanceGuard: original paper §§I–V READ via ar5iv (trace Eq, routing/NLI/RF Table 1, 281-trace corpus, 361 held-out, Tables 3–6 incl. 0.802/0.858/0.681 and multi-source 0.846/0.503/0.229, baselines, repair, RQ2); reporter corrections applied (0.681 omission, unit distinction 0.503/0.229, LLM-assisted adjudication scope, 256-historical labeling). Tail §§/appendices unread; PDF bytes not consumed; code/poster/PR unopened.
- Olmo-core 3 report: RETRIEVAL_FAILED after 2 meaningful retries (markdown + text, both >5MB; no URL guessing). Fallback: blog (fully read, claims stay reporter-level VERIFIED) + repo page read (1.7k stars/Apache-2.0/PyPI/scripts — existence only). Failure logged with retry avenue (paginated/docs/clone at Selection depth).
- Abstract/blog-only claims retained ONLY with explicit limitations; no PDF_VERIFIED without bytes.

## 5. Gemini 1M OUTPUT correction (SC-E04)

- Record corrected to `Google-announced 1M OUTPUT token limit (from 64K)`, vendor-attributed, model/version/rollout-qualified (Fairwind staged rollout, Sep 30 announcement). R1 broad-limit wording WITHDRAWN (noted in limitations). Input-context/API/rollout breadth still NOT inferred; model-docs pending. Status VERIFIED; other targets unchanged.

## 6. 35 reviewer records old→new, consumption states, genuine limitations

- Changed (5): elyza PARTIAL+HOLD→VERIFIED+MATERIAL(provisional) (12 claims); contextlm abstract→fulltext (5 claims; pdf target honest-UNRESOLVED); olmocore3 blog + failure-bound (4 claims); guard team-blog→paper-backed (5 claims); gemini corrected (3 claims). Other 30 byte-identical to r1.
- Consumption states: CONSUMED 29 full bodies + 7 delegated pins (r4, Sol-reverifiable) + 5 r5 reads (2 cards, 2 papers, 1 repo/failure); CAPTURED_BUT_UNCONSUMED enumerated per record (cards, repos, weights, scripts, replays, rate pages, paper tails, code); RETRIEVAL_FAILED (AutoSynthData standalone, ELYZA eval void, /pricing banner direct, Olmo report body, PDF bytes); NOT_FOUND (Pixel Canary card/outage, TBC bench/paper).
- Genuine primary limitations carried: no independent benchmark reproduction; 0 byte-identical captures; AstaBrief/AutoSynthData times unresolved (out of r5 scope, preserved); Oct 8/9 post-window guarded; Oct 2 Cloudflare day-only items unclassified.
- Views: 5 updated (materiality/rationale), 30 untouched; all still draft (package-task-SHA binding, NO result-SHA until acceptance).

## 7. Schema/preflight outcomes; no accepted cards/views

- Runner field validation r5 file: 35/35 PASS (29 VERIFIED / 6 PARTIAL; 29 MATERIAL / 5 HOLD / 1 CONTEXT); completeness 3 SATISFIED + 11 residuals + closure null PASS.
- Projected-bindings validation: 35/35 PASS (no suppression). Views: 35/35 schema PASS (5 rewritten). Collector run/index: schema PASS. Compat: frozen PASS ×3 + negative + reproducibility.
- Card candidates: 5/5 built + `validate_evidence_card` PASS (contextlm vs projected task) — kept as `card-<did>.PROPOSED.json`, explicitly NOT accepted; no Edition View binds them; no `evidence-accepted.json`.
- State/gates/Core: unchanged except edition files (see §1); no Selection/Architecture/Human action.

## 8. Terminal + residual

- Terminal: `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` candidate (REVIEW_PENDING).
- Residual for Sol: (a) authorize/reject exact projection ledger (acceptance blocked until then + Core repair rerun); (b) ELYZA MATERIAL-vs-HOLD adjudication; (c) paper-tail/appendix depth sufficiency (CLM B–F, Guard VI+/schema, Olmo report retry avenue); (d) AstaBrief/AutoSynthData times + AutoSynthData standalone (unchanged); (e) Selection-depth pins (cards, repos, weights, scripts, replays, rates) enumerated per record.
