# Muse W40 r10 — bounded independent Selection-audit remediation

Status: `SOL_BOUNDED_AUTHORITY / SELECTION_REVISION_REQUIRED / STOP_AT_SOL_SELECTION_REVIEW`
Repository: `eariver/japanese-generative-ai-survey`
Existing and ONLY work branch: `weekly/2026-W40-v2-work`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Reviewed Muse r9 HEAD: `e2940790ede6f29796f3b9885e7262fd3c086622`; Tree: `36881abe1aeebf742d1e5af15fd9c9d92cf59652`
Independent full audit: `sources/2026-W40/execution/reviews/independent-selection-audit-w40-r9-20261010.md`
Sol adjudication: `sources/2026-W40/execution/reviews/sol-w40-selection-adjudication-r1-20261010.md`
**Actual r10 starting HEAD/Tree must be given by the outer invocation, after this contract is committed.**

## 0. Zero-write admission guard

Read-only check remote W40 HEAD == outer Starting SHA, commit Tree == outer Starting Tree, remote main HEAD == reviewed `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, starting commit descends from r9 `e2940790ede6f29796f3b9885e7262fd3c086622`, `production-state.json.lifecycle_state=EVIDENCE_REVIEWED` and next `stage:selection`, Selection/Architecture/Human Gates all pending. Mismatch => STOP expected/actual, **ZERO WRITES**.

ONLY W40 edition-local writes; existing branch, normal commits and non-force push/readback. No new/fallback/review branch, reset, rebase, history rewrite, force push, shared Core/schema/config/workflows/main/W39/other editions/Human Gate edits. Preserve canonical Discovery37, Screening37, Evidence35, Views35, Materiality37, Completeness, official Core Stage checkpoint and State.

## 1. Read contract and auditor source

Read independent full audit and Sol adjudication above, r9 handoff, `execution/selection/selection-proposal-r9.json`, `selection-dossier-r9.md`, Canonical Stage authority, accepted Evidence/Views, reviewed `main` `schemas/candidate-matrix-v2.schema.json`, `schemas/candidate-selection-v2.schema.json`, `scripts/survey_architecture_v2_base.py::validate_selection`, `scripts/survey_completeness_v2.py::validate_profile_completeness` and Sol/Luna governance. No automatic acceptance of earlier Muse PASS as semantic proof.

## 2. Selection semantic/count corrections (S01, S02)

Preserve r9 inputs as historical. Create distinct `execution/selection/selection-proposal-r10.json`, `selection-dossier-r10.md`, and a machine-recomputable count report:
**35 assigned = 28 SELECTED (20 PRIMARY, 8 SUPPORTING) + 1 INSPECT (DGX) + 4 HOLD + 2 REJECT**. Two separate negative-space log records EXCLUDED from 37 Discovery are not extra assignments. Do not re-invent 23/5.

Produce **Core Candidate Matrix staging** with actual frozen-Core operations/accepted upstream SHA, and an exact old r9 human candidate→Core task-derived candidate mapping for all 35. Prepare Core-compatible Selection **review-only preview** from those 35 rows: candidate IDs and sha basis genuine; summary numeric object; schema fields exact; `status=ESTABLISHED` only as required for the **isolated noncanonical validator preview**, not as Core Stage approval. `dgx` INSPECT and all HOLD/REJECT use `architecture_usage=NONE` and roles null; SELECTED use valid PRIMARY/SUPPORTING, role namespace and exact matrix/materiality checks. Keep explanatory `PROPOSED_NOT_ACCEPTED` in separate review metadata and file path. If Core cannot form preview, return genuine validator failures; do NOT fabricate canonical Acceptance or Selection Complete.

## 3. Four bounded October 2 time investigations (T01/N01)

Fixed W40 UTC half-open `[2026-09-25T22:00:00Z,2026-10-02T22:00:00Z)`.

Check first-party original **first-publication instant**, original artifact/event availability, and later update vs feed ingestion (UTC/timezone, source anchor, hash, archive):
- Ai2 AstaBrief 8B: `https://allenai.org/blog/astabrief`;
- ServiceNow AutoSynthData: `https://huggingface.co/blog/ServiceNow-AI/autosynthdata` (secondary external RSS `04:01:31Z` is a lead, NOT issuer-proof);
- Cloudflare Web Search API: `https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/`;
- Cloudflare Pi Durable Harness: `https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/`.

Search publisher RSS/Atom, API changelog sources, initial git tag/commit/release, first archive/publication metadata; record attempts, exact first-party evidence or unresolved. Day-only `2026-10-02` is NOT enough to assign an hour or prove the 22:00Z cutoff. If proven in-window and materially changes candidacy (including adding either Cloudflare technical event not in 37 accepted Discovery), write `execution/selection/selection-scope-delta-r10.md` with evidence, expected Core change chain, and **STOP for Sol upstream-scope approval**; do not silently reclassify accepted HOLDs or add Discovery rows. Otherwise preserve HOLD/unadmitted; do not manufacture completeness.

## 4. Focused primary-authority consumption (E01), not broad reintake

Actually read source content for:
- Ai2 Olmo-core 3 full technical report as first priority (try legal official HTML/text, PDF segment/paginated extract and commit-pinned source alternatives after >5 MB failures; never claim full report consumed if not);
- Context Language Models important appendices, figures and/or code needed for method/bench;
- ProvenanceGuard **official v2** later sections/appendix, avoid invented v3 dates;
- FLUX 3 Image original model/product/repo release and licenses, separated from July FLUX 3;
- Cloudflare MCP Auth release and protocol specifications and threat boundaries.

For each source record original URL/revision/date, actually consumed section/table/figure, method, baselines and denominators, limitations, publisher-vs-independent claims, and exact candidate/local Card impact. Keep accepted Evidence immutable. If new technical facts contradict its claims or materially alter Selection, create a **separate Evidence delta proposal** for Sol; don't patch accepted Cards, Stage or checkpoint.

## 5. High-information-density editorial plan (A01/A02)

Create a revised package/relative-depth proposal. Prefer dividing P6 into **training-methods-and-systems** (ContextLM, Olmo-core 3; AutoSynthData only if first-party timestamp proven and canonicalized later) and **evaluation-and-execution-infra** (AgentPerf, Open TTS, RL Env), or demonstrate separate substantial chapters within one P6 with individual mechanisms/metrics/method conditions/repro limits. Rename P2 separating Holo4 general GUI/agent weights and ELYZA Japanese reasoning release. P5 distinct runtime controls, safety-case guidance, biological watermark, source attribution and MCP authorization; P7 FLUX image/VSS reference-video/ASR + agent observability; P8 PRIMARY=0 should generally be enterprise/industry digest. Include 35-candidate relation map, source↔claim anchors, overlap/DevDay count exclusions, recommended comparison tables, actual depth per theme and strong unselected counterfactuals. Do not force an arbitrary short issue; 29 MATERIAL leads do not require 29 separate articles.

For DGX INSPECT propose include or exclude with actual technical merit, Oct 2 official time and Oct 23 planned availability; this is a **proposal to Sol**, not a silent status/authority change.

## 6. Prior-record interpretation and terminal stop

Record a non-mutating erratum: Core checkpoint free-text says MATERIAL30, actual authority MATERIAL29. Do NOT rewrite immutable checkpoint/State/old SHA. Completeness `discovery_ids` all37 because frozen Core provenance obligations; substantive Evidence task scopes 31/29/2 (W39 carry-over only two). Retain user-critical HOLD/technical caveats and CV2-DM-016 OPEN_CORE.

Generate `sources/2026-W40/execution/SOL_SELECTION_SEMANTIC_REVIEW_HANDOFF-r10.md` reporting:
1. Starting/Final HEAD/Tree, reviewed main, fast-forward, changed-file allowlist, nonforce push/readback;
2. actual 35 counts 28=20/8 and all Core Candidate Matrix/candidate-ID/basis-sha crosswalk and validator output, no false PASS;
3. four release-time verification outcomes with dates/timezones/boundary and source authorship;
4. five original-authority deeper readings with locations and actual claim delta versus accepted Evidence;
5. revised package/depth and P6 alternative, duplication/negative-candidate counterfactual;
6. prior Stage authority intact and erratum;
7. terminal `SOL_SELECTION_SEMANTIC_REVIEW_READY` if no upstream shift needed, else `SOL_SELECTION_SCOPE_CHANGE_REVIEW_REQUIRED` with precise source/effect and no unauthorized changes; or `SOL_SELECTION_SEMANTIC_REVIEW_BLOCKED` with true blockers.

**STOP before actual Core Selection Acceptance/`SELECTION_COMPLETE`, Architecture, Draft, Publication or Human Gate.** Only Sol next independent Selection review can authorize these.
