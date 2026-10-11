# W40 Muse r5 — bounded Evidence semantic gap-fill + source-type compatibility proposal

Authority: `sources/2026-W40/execution/reviews/sol-w40-evidence-authority-consumption-r1-20261010.md`  
Status: `SOL_BOUND_EXECUTION_AUTHORITY / SC-E01_E02_E03_E04_E05 / STOP_AT_SOL_EVIDENCE_REVIEW`
Repository: `eariver/japanese-generative-ai-survey`
**Existing branch only:** `weekly/2026-W40-v2-work`
Reviewed `main`: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Reviewed Muse r4 HEAD/Tree: `e81ab6e461ff0e58bd62c590a532a78ca80a7057` / `db7423d2b17947fd56a0af9455153f27ac33eb13`
**Exact r5 Starting HEAD/Tree:** provided in the outer Muse invocation, after this file is committed.

## Zero-write start guard

Before any write: remote W40 branch HEAD equals outer Starting SHA, commit Tree equals outer Starting Tree, remote main HEAD exactly `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, starting commit is directly descended from reviewed r4 `e81ab6e461ff0e58bd62c590a532a78ca80a7057` through this Sol review commit, canonical State `CANDIDATES_NORMALIZED`, `next_action=stage:evidence-materiality-completeness`, human gates pending/pending. Mismatch -> STOP, report expected vs actual, ZERO WRITES.

No new/fallback/review branch, no local/remote reset, no rebase/force, no stale-head push, no unauthorized Core scripts/schema/config/docs/other edition/main/CI edits. Normal commit + non-force push only to existing W40 branch.

## Mission: bounded Evidence repair without premature acceptance

### 1. Root-cause and compatibility projection (SC-E01)

- Read existing deferred issue **CV2-DM-016** and W40 `execution/defects/w40-core-evidence-sourcemap-20261010.md`, frozen `scripts/survey_evidence_v2.py` source map, Discovery schema, exact accepted 37 Discovery, accepted 37 Screening, 35 Evidence tasks.
- Reproduce failure on 3 tasks; record actual stack/error and affected IDs. No unsupported source class should silently map.
- Research a minimal **edition-local derived-Evidence-Task-only** projection analogous to the DM-016 precedent, without changing canonical Discovery or accepted Screening:
  - original `PRIMARY_RESEARCH_ABSTRACT` -> derived `PRIMARY_PAPER`, but note content depth remains **abstract only** until full paper consumed; label source role/arXiv-submission precisely;
  - original `EVALUATOR_PUBLISHER` -> derived `PRIMARY_OFFICIAL` only for the **evaluator's own original benchmark report**, with explicit role `first-party evaluator/publisher of the benchmark`, NOT vendor of evaluated models and NOT an independent reproduction by Muse.
- Create a machine-checkable source-type projection ledger mapping all original affected `source_records` paths/SHAs/source-type to projected derived task paths/SHAs and expected Core authority classes. Fail closed on any other unknown type; proof that all 35 bound tasks have a recognized source class. **Preserve original 35 task file bytes and accepted Source/Screening authorities**; produce separate r5 candidate package/task copies if necessary. Include exact immutable source identity/basis and test failure injection for unreviewed type.
- Because the existing inventory calls for *reviewed narrow projections*, treat this as **PROPOSED_NOT_ACCEPTED** in r5. Run frozen Core preliminary validation but do not create a canonical accepted Evidence or State advance until Sol authorizes the exact ledger after semantic review. If frozen Core would reject the projection, STOP as CORE_BLOCKED; no fake pass flags or hidden mapper patches.

### 2. ELYZA deep primary consumption (SC-E02)

Retrieve W40 release-pinned full README/model cards and benchmarks for:
- `https://huggingface.co/elyza/ELYZA-Thinking-1.0-llm-jp-4-33b/commit/6ca556b2ddc4642580752b3a1ae2d7e7681106fc`;
- `https://huggingface.co/elyza/ELYZA-Thinking-1.0-llm-jp-4-32b-a3b/commit/5260ecc249f32ef5005ef940c78f41f130d9c468`.

Source table contains `Average performance` and `Benchmark Results`. Consume version-pinned relevant model/data-card content, not just API metadata. Record dense vs MoE parameter-active and base-model distinctions, Japanese-localized math/coding/STEM data, Japanese knowledge and tools, mid-training/SFT/RLVR method, 7 capability-group evaluation, representative benchmarks, denominators, compared baselines, eval scripts where provided, access and license scope; publisher claims must remain attributed. Distinguish images/graphs from machine-readable evaluation tables and explicitly state unreadable portions. Cross-check Oct-2 release timestamps as first-publication evidence. Do not automatically promote score without verified tables; do not default to HOLD because material first-party evaluation was not fetched.

Recreate the ELYZA **draft** reviewer input/card candidates and Edition View with evidence-source hashes, status and provisional materiality genuinely reflecting consumed primary content. Screening MAYBE remains immutable. Provide Sol a specific positive-vs-HOLD reason and counterfactual comparison.

### 3. Paper and source specificity (SC-E03 / E05)

- Read `https://arxiv.org/pdf/2609.37725` Context Language Models **full paper**, or record real retrieval failure after meaningful retries, comparing abstract figures against methods/conditions/ablations. Fix false `VERIFIED:...-pdf` verification target if PDF not actually read; retain abstract-backed claims only with explicit limitations.
- Read Ai2 Olmo-core 3 linked technical report (from `https://allenai.org/blog/olmocore3`) and original arXiv ProvenanceGuard `https://arxiv.org/abs/2606.18037` full available paper, or document explicit source failure and bound claim level. Analyze reporter-vs-original quantitative provenance, evaluation conditions and ablation / generalization restrictions. Do not confuse ProvenanceGuard's Sep29 team-blog event with Aug27 paper.
- For every paper/technical report actually used, link to exact revision and corpus, and record which pages/figures/tables were consumed; avoid `PDF_VERIFIED` if only the abstract or blog summary was read. Bounded copyright excerpts and content-location breadcrumbs rather than copying whole papers where redistribution is restricted.

### 4. Gemini source precision (SC-E04)

Original Google Sep 30 announcement explicitly states `output token limit to an industry-leading 1M tokens, up from the previous 64K`. Revise draft evidence to `Google-announced 1M OUTPUT token limit`, vendor-attributed. Do not silently infer general input context, universal API availability or rollout from that phrase; separately check model docs if needed.

### 5. Full review-input update and preflight

- Preserve original `evidence/v2/results/r1/interactive-evidence.json` as history. Create r5 revision file with the 35-record coverage and changed candidate-local claims/statuses; explicit r4→r5 diff ledger for ELYZA/ContextLM/Olmo/ProvenanceGuard/Gemini and any affected source records.
- Re-run Core schema/runner validation **without** suppressing task-source binding for the derived projection; if unsupported, report blocked. Prepare task-local canonical Evidence Card candidates **only if** the full Core Card contract can be met; do not claim accepted.
- Views remain drafts and must bind exact eventual Evidence Card result SHA only after actual acceptance. Existing task-package SHA binding is not the result SHA. Avoid `VERIFIED` for merely located/unread original source content, source capture vs consumption must be explicit.
- Retain W39 Pixel Canary/TBC HOLD, pre-window LIFT, Grok Raw exact 20,477B + 4 URL vs Daily X 64 distinction, uncertain Oct2 AstaBrief/AutoSynthData release time, and Oct2 DGX 13:00:39Z ordinary-eligibility with Oct23 future shipping.

## Reporting and stop

Provide new `sources/2026-W40/execution/SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF-r5.md` with:
1. actual Starting/Final HEAD/Tree/readback/allowlist, unchanged main/Core/Human Gates;
2. SC-E01 mapping projection exact proofs, original and projected SHA graph, Core pass/fail and negative tests;
3. exact original sources and sha/date/version, ELYZA benchmark/training consumption and materiality alternatives;
4. actual CLM/Olmo/ProvenanceGuard paper-body read checks or documented failures;
5. Gemini 1M **output** source correction;
6. 35 reviewer records old→new, source-consumption states, unresolved genuine primary limitations;
7. actual schema/preflight outcomes; explicit no accepted Evidence Card/Edition View unless authorized;
8. `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` or `SOL_EVIDENCE_AUTHORITY_REVIEW_BLOCKED`.

Stay at `CANDIDATES_NORMALIZED`, Evidence/Materiality/Completeness checkpoints pending, Selection/Architecture/Human untouched. STOP for independent Sol review. Shared Core fix belongs to separate reviewed maintenance; DM-016 remains OPEN.
