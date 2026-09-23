# TS-002 Beyond Text — Muse bounded Discovery repair after Sol r1

Status: `EXECUTION_AUTHORITY / DISCOVERY_REPAIR_ONLY / SOL_R1_REQUEST_CHANGES / STOP_FOR_SOL_R2`

Date: `2026-09-24 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-beyond-text-2026`

Existing branch only: `special/beyond-text-2026-work`

GitHub production Issue: `#526`

Reviewed Discovery HEAD: `f1cb5fb655cc7fbf02a537ffb2e25d1022aa74b3`

Sol r1 review commit: `cb03b40b55ba14a3f14a727688b892c6a32d683a`

Sol r1 review:

`sources/SP-beyond-text-2026/execution/sol-discovery-completeness-review-r1.md`

Target stop:

`DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW_R2`

---

## 0. Launch guard contract

The exact remote branch HEAD/tree for this execution is supplied by the outer launch instruction after this prompt is committed. Treat that launch guard as authoritative.

Before any mutation, verify read-only:

- remote `special/beyond-text-2026-work` HEAD/tree exactly match the launch values;
- remote `main` HEAD/tree exactly match the launch values.

If any value differs, perform **zero writes**, report expected vs actual, and stop.

Do not create a new branch, fallback branch, repair branch, review branch, or iteration branch.

Do not reset, rebase, cherry-pick, force-push, rewrite history, or modify `main`.

All writes belong only on the existing `special/beyond-text-2026-work` branch and must be normal non-force fast-forwards.

---

## 1. Mandatory read order

After guards pass, read in full:

1. `sources/SP-beyond-text-2026/execution/sol-discovery-completeness-review-r1.md`
2. `docs/research-plans/2026-09-24_ts-002-beyond-text-sol-preresearch.md`
3. `docs/research-plans/2026-09-24_ts-002-beyond-text-muse-discovery-contract-draft.md`
4. `sources/SP-beyond-text-2026/research-scope-v2.json`
5. `sources/SP-beyond-text-2026/production-profile.json`
6. `sources/SP-beyond-text-2026/production-state.json`
7. current `sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl`
8. current `sources/SP-beyond-text-2026/raw/discovery-negative-space-2026-09-24.md`
9. current Discovery validators / generic pipeline authority needed to rebuild accepted Discovery safely.

The Sol r1 review is the controlling delta for this run.

Do not reinterpret the request as a full Discovery restart.

---

## 2. Mission

Preserve the existing 128-record Discovery base and perform only the bounded repairs required by Sol r1:

1. repair current-capstone chronology/provenance for `BT-D100`–`BT-D128` by re-reading first-party source metadata;
2. run one bounded primary/technical gap-fill pass for G08, G09, G10, and G11;
3. optionally fill G03/G04/G12 only if a material authority is found with low additional search cost;
4. regenerate canonical Discovery acceptance/coverage artifacts consistently;
5. validate Discovery;
6. stop for Sol completeness review r2.

Do **not** run Screening or any later stage.

---

## 3. Chronology/provenance repair — mandatory

### 3.1 Re-read all current capstones

For every record `BT-D100` through `BT-D128`, open the first-party locator and determine the source's actual publication/release date at the best precision supported by repository conventions.

Do not derive publication date from:

- model name;
- URL slug;
- search-result year alone;
- Discovery observed time;
- another article describing the same model;
- a generic `2026-01` placeholder.

If the source itself exposes only year/month, use year/month. If it exposes day but canonical `published_at` is month precision, normalize to month while preserving exact source date in raw notes when useful.

If a dynamic documentation page has no defensible publication date, record it as unknown/undated according to schema convention and preserve the observed-at timestamp separately. Do not invent January.

### 3.2 Known Sol-verified corrections

At minimum, confirm and repair these first-party values rather than blindly copying them:

- BT-D102 Seedream 5.0 Pro — source date 2026-07-08.
- BT-D103 ChatGPT Images 2.5 — source date 2026-09-08.
- BT-D107 GPT-Live — source date 2026-07-08.
- BT-D109 Gemini 3.8 Audio model card — published 2026-09-15.
- BT-D111 Lyria 3.5 model card — published 2026-07-29.
- BT-D113 Stable Audio 3 / SAME — Stability AI research publication 2026-05-20; current `2025-01` is wrong.
- BT-D117 Seedance 2.5 — source date 2026-07-31.
- BT-D119 FLUX 3 — source date 2026-07-23.

The final values must come from the first-party sources during this run.

### 3.3 Propagation

Update consistently:

- `sources/SP-beyond-text-2026/raw/discovery-observations-capstones-2026.md`;
- the corresponding records in `sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl`;
- any negative-space/coverage chronology statements affected by the repairs.

Then rebuild `discovery-accepted-v2.json` using the repository's current canonical Discovery path rather than hand-editing the accepted artifact.

Do not change historical records merely to create churn; only fix independently verified metadata defects.

---

## 4. Mandatory bounded gap-fill

New material records must continue the existing ID sequence from `BT-D129` upward. Map each new record to existing BT-O obligations. Do not create new scope dimensions.

### 4.1 G08 — audiovisual synchronization evaluation

Search primary papers/specifications/technical reports for technically meaningful AV-sync or audiovisual-alignment evaluation used in generated video/audio-video systems.

Seek evidence for one or more of:

- sound-event timing alignment;
- audiovisual semantic alignment;
- lip/speech synchronization where relevant;
- benchmark dimensions designed specifically for generated audiovisual content;
- published validity/limitations of those metrics.

If material authority is found, add it to Discovery and update G08.

If not, preserve G08 as unresolved and record what was searched and why the available metrics are insufficient.

### 4.2 G09 — current open/deployable speech generation / voice cloning

Search for current first-party technical reports, model cards, repositories, or papers for open-weight/open-source speech generation, TTS, voice cloning, or speech-to-speech systems with useful deployment/runtime information.

The purpose is to balance the current closed native-speech capstones with at least one technically grounded open/deployable lane if such authority exists.

Do not use popularity as authority. Do not add thin model-list entries.

### 4.3 G10 — streaming speech-to-speech latency methodology

Search papers/specifications/technical reports defining or measuring concepts such as:

- time to first audio;
- end-of-turn to first audio;
- real-time factor;
- streaming chunk latency;
- barge-in / interruption latency;
- full-duplex conversational latency.

Prefer methodology/taxonomy authority over vendor leaderboard numbers.

Do not normalize incompatible vendor figures into a ranking.

### 4.4 G11 — video physics / commonsense evaluator validity

Search for research evidence on the validity, reproducibility, or limitations of physics-oriented / commonsense / intrinsic-faithfulness evaluation for generated video.

Seek independent benchmark papers or evaluator-validation work where available.

If evidence remains thin, keep G11 unresolved and state the limitation explicitly. Do not promote vendor scores to comparable truth.

---

## 5. Opportunistic gaps only

G03, G04, and G12 may be explored only if they do not materially expand the run.

- G03: independent Suno / ElevenLabs listening/evaluation evidence.
- G04: independent FLUX.2-klein runtime/VRAM/latency measurement.
- G12: rectified-flow / flow-matching versus diffusion ablations in audio/video.

Do not delay completion merely to force these gaps closed.

G01/G02/G05/G06 are legitimate closed-system negative space. Do not infer undisclosed architecture.

---

## 6. Discovery quality rules

Maintain the original anti-thinness contract.

- Do not convert the corpus into a current-model catalogue.
- Do not delete foundational historical anchors to keep record count small.
- Do not add duplicate sources for count inflation.
- Do not create cross-model rankings from incompatible evaluation settings.
- Preserve vendor attribution for vendor claims.
- Keep source publication/release date distinct from observed/retrieval time.
- Preserve TS-002 / TS-003 boundary.
- Keep representation, editing, long-horizon structure, runtime, and evaluation first-class.
- X/community remains deferred.

This is still Discovery. Do not perform full Evidence claim extraction except as minimally needed to verify source identity/date/technical relevance.

---

## 7. Regeneration and validation

After bounded repairs/gap-fill:

1. validate every added/modified JSONL record against current schema/graph requirements;
2. rebuild canonical accepted Discovery with the current pipeline;
3. regenerate/update Discovery coverage accounting;
4. update negative-space with G08/G09/G10/G11 disposition and any opportunistic gap results;
5. ensure all source IDs and obligation references are internally consistent;
6. run the exact Discovery validator(s) required by current Core-v2 authority;
7. verify `production-state.json` remains at `DISCOVERY_COLLECTED` and all downstream machine checkpoints remain pending;
8. do not advance lifecycle to Screening.

If the current pipeline requires a receipt/run/checkpoint artifact for a Discovery refresh, create it under the edition's existing execution root using normal conventions.

Shared Core remains frozen; if an edition-local compatibility issue appears, record it rather than modifying shared Core.

---

## 8. Required final report

Before stopping, report and persist a concise r2 refresh summary containing:

- exact starting remote branch HEAD/tree;
- exact reviewed main HEAD/tree;
- final remote branch HEAD/tree;
- previous Discovery record count: 128;
- new Discovery record count;
- IDs modified for chronology repair;
- IDs added by gap-fill and their obligation mappings;
- a date-correction table for `BT-D100`–`BT-D128` showing previous -> verified canonical date/unknown disposition;
- G08/G09/G10/G11 result: FILLED / PARTIALLY_FILLED / UNRESOLVED, with supporting IDs or negative-space rationale;
- opportunistic G03/G04/G12 result if searched;
- Discovery validator result;
- confirmation that no Screening/Evidence/later stage ran;
- confirmation that no shared Core file changed;
- confirmation that X/community was not run.

Expected stop:

`DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW_R2`

Then stop and return control to Sol/Human Owner.
