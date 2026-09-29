# TS-003 Vision & Multimodal AI — Muse Round D targeted follow-up contract

Status: `ROUND_D_TARGETED_FOLLOWUP_CONTRACT / PRE_DISCOVERY / NOT_PRODUCTION_AUTHORITY`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `planning/ts-003-vision-multimodal-preresearch-20260930`

Authority chain:

1. `docs/research-plans/2026-09-30_ts-003-vision-multimodal-sol-preresearch-skeleton.md`
2. `docs/research-plans/2026-09-30_ts-003-sol-scope-audit-before-worker.md`
3. `docs/research-plans/2026-09-30_ts-003-muse-round-b-reconnaissance.md`
4. `docs/research-plans/2026-09-30_ts-003-muse-round-b-source-candidates.md`
5. `docs/research-plans/2026-09-30_ts-003-sol-round-c-scope-review.md`

This contract authorizes only a **targeted Round D follow-up**. It is not production Discovery and must not initialize or mutate any production state.

## Mission

Resolve only the ten Round C residual questions R1–R10 strongly enough for Sol Round E to close the pre-Discovery scope. Do not repeat the broad Round B reconnaissance and do not expand the topic because adjacent material is interesting.

For every finding, distinguish:

- source-supported fact;
- Worker interpretation;
- unresolved uncertainty;
- source-access or authority limitation.

Current/vendor sources must preserve role boundaries: `ARCHITECTURE_CASE`, `CAPABILITY_CASE`, `DEPLOYMENT_CASE`, `EVALUATION_CASE`. A source supporting one role does not automatically support another.

## R1 — D04 exact allow-list

Recommend **2–4 primary mechanism nodes maximum** that are sufficient to explain the spatial/geometry substrate needed by later TS-003 lanes.

The purpose is not to survey 3D vision. Select only nodes that explain at least one of:

- depth / metric or relative geometry;
- pose / keypoints / object-centric spatial state;
- relational scene structure;
- why classification-style representations are insufficient for spatial reasoning, GUI grounding or embodied action.

Explicitly refuse full SLAM, NeRF, 3D Gaussian Splatting, reconstruction or robotics-geometry histories unless one source proves a load-bearing TS-003 requirement.

Output: final allow-list + excluded near-neighbours + rationale.

## R2 — D07B lineage exactness

Verify exact primary-source roles and minimum non-redundant lineage for:

- phrase grounding;
- referring-expression comprehension;
- open-vocabulary detection;
- language-grounded detection;
- open-vocabulary segmentation;
- actionable grounding bridge.

Candidate families to verify rather than blindly include: Flickr30k Entities / RefCOCO, OVR-CNN, ViLD, GLIP, OWL-ViT, Grounding DINO, OWLv2/OWL-ST, relevant open-vocabulary segmentation nodes.

Return the **minimum explanatory chain**, not the longest bibliography. Identify where two candidates are redundant and which metrics/task contracts differ from D07A image-level alignment.

## R3 — Second open VLM family

Find one technically distinct, source-rich open/inspectable VLM family independent of Qwen that can serve as an architecture comparison case.

Selection criteria:

- primary technical report/paper available;
- inspectable architecture and/or weights/code;
- enough mechanism detail to compare vision encoder, fusion/connector, tokenization/resampling, post-training and deployment assumptions;
- current relevance;
- non-redundancy with Qwen3-VL/Qwen3-Omni;
- documented limitations or independent evaluation preferred.

Do not select on popularity or leaderboard rank alone. If no candidate meets the bar, return `NO_SECOND_OPEN_VLM_MEETS_BAR` with reasons.

## R4 — Document specialist vs generalist

Test whether a current document-specialist vs general-VLM comparison can be made without violating evaluation comparability.

Check:

- document OCR/layout/chart/table/equation tasks;
- exact benchmark/version/input-resolution policy;
- specialist vs generalist architecture role;
- whether the same metric/protocol exists;
- whether a qualitative mechanism comparison is valid even when numeric ranking is not.

Return either:

- a defensible comparison contract; or
- `NO_CROSS_MODEL_NUMERIC_COMPARISON` plus a safe qualitative structure.

## R5 — Streaming / long-video

Find one source-rich streaming/online video-understanding system or benchmark that represents a genuinely distinct mechanism/problem from merely supplying a longer offline context.

The candidate must materially address at least one of:

- online observation arrival;
- bounded/rolling memory;
- persistent state over time;
- event updates without full replay;
- latency/throughput trade-offs of continuous multimodal perception.

If no source-rich candidate exists, return exactly:

`LOW_YIELD_CONFIRMED — STREAMING_VIDEO_UNDERSTANDING`

and explain why D11 should remain a stub rather than be padded.

## R6 — Audio-input / omni predecessor chain

Resolve a **minimal input-side predecessor chain** sufficient to explain 2025–2026 omni multimodal fusion without retelling TS-002 audio-generation history.

Potential categories:

- speech/audio encoders;
- audio-language alignment;
- audiovisual representation/alignment;
- streaming multimodal input;
- absolute-time / synchronization representation.

The chain should explain what technical contract changed as models moved from text+image to audio/video-aware omni input. Audio synthesis, TTS, voice cloning and music generation remain TS-002-owned unless a mechanism is indispensable to input/fusion explanation.

## R7 — VLA predecessor chain

Verify exact source roles and minimum required chain among candidates such as:

- SayCan;
- RT-1;
- PaLM-E;
- Open X-Embodiment;
- RT-2;
- OpenVLA;
- current vendor cases such as Gemini Robotics / on-device variants.

The purpose is to avoid making RT-2 appear from nowhere while also refusing a full robotics history.

For each retained node, state exactly what new representation/interface contract it contributes:

- language-conditioned planning;
- action tokenization;
- embodied multimodal representation;
- cross-embodiment data;
- open VLA implementation;
- on-device deployment/capability.

Return the minimum chain and explicit exclusions.

## R8 — World-model terminology counterweights

Verify primary authority and exact contribution for at least:

- Dreamer-family latent dynamics / model-based decision-making;
- JEPA/V-JEPA-like predictive representation learning;
- Genie-style interactive generative environment models.

The goal is not ancestry but **terminological separation**.

For each pole answer:

- what state is represented?
- what is predicted?
- is action conditioning present?
- are pixels/latents/rewards/actions predicted?
- is the model used for planning/training/evaluation, or only generation?
- what evidence would distinguish useful dynamics from visual realism?

Return a compact comparison contract that prevents `world model = video generator` collapse.

## R9 — Evaluation authority cleanup

Resolve exact source/version/role for the currently lower-confidence evaluation candidates needed by D05/D07B/D10/D11/D12/D14.

Prioritize only metrics/benchmarks that fill a distinct measurement contract, including as relevant:

- document/chart understanding;
- hallucination / visual evidence use;
- GUI grounding / computer use;
- long-video / temporal reasoning;
- spatial reasoning;
- world-model control-oriented evaluation.

For every retained benchmark record:

- canonical source;
- task identity;
- version/split;
- metric/evaluator;
- what it does **not** measure;
- contamination or language-prior risk;
- configuration fields that must be bound in publication.

Delete redundant benchmark candidates from the recommendation rather than maximizing count.

## R10 — Current-capstone source-role binding

For each serious current candidate, build a four-role authority matrix:

| Candidate | ARCHITECTURE_CASE | CAPABILITY_CASE | DEPLOYMENT_CASE | EVALUATION_CASE |
| --- | --- | --- | --- | --- |

At minimum assess candidate classes represented by:

- Qwen3-VL / Qwen3-Omni;
- the second open VLM from R3, if any;
- a document/UI case;
- long-video/streaming candidate, if any;
- computer-use case;
- VLA case;
- world-model case.

Each non-empty cell must name the exact primary/official source supporting that role. Unsupported cells remain blank. Do not infer architecture from product pages or demos.

## Required outputs

Create exactly two new planning files unless a third small appendix is strictly necessary:

1. `docs/research-plans/2026-09-30_ts-003-muse-round-d-targeted-followup.md`
2. `docs/research-plans/2026-09-30_ts-003-muse-round-d-source-resolution.md`

The main follow-up report must contain:

- executive summary;
- R1–R10 result sections;
- explicit unresolved gaps;
- recommended changes to the Round C taxonomy/boundaries/weights;
- whether any Round C decision should be reversed;
- a proposed Round E closure checklist.

The source-resolution file must contain only sources actually checked during Round D, with:

- exact URL/canonical identifier;
- source type;
- authority role;
- access result;
- relevant claim/task;
- confidence;
- version/date notes;
- TS-001/TS-002 overlap notes.

Unlike the Round B candidate ledger, do not mark checked sources `NOT_ACCESSED`. Record the actual access/read-back status honestly. If only abstract/summary/official page was read, say so.

## Scope discipline

Do not re-open already settled broad lanes unless R1–R10 evidence directly invalidates a Round C decision.

Do not add new top-level D/X lanes merely because a new subtopic is interesting. Any proposed new top-level lane requires:

1. evidence it is technically distinct;
2. evidence it is load-bearing to the Core Question;
3. evidence it cannot fit an existing lane without semantic loss;
4. evidence it will have enough primary-source density for the final Special.

## Explicit prohibitions

Do not perform or create:

- production Issue;
- production branch;
- `sources/SP-*` initialization;
- Production Profile / State;
- canonical Discovery;
- Screening;
- Evidence;
- Completeness / Materiality / Selection;
- Architecture;
- Draft / PDF;
- Freeze / Release;
- Shared Core changes;
- `main` changes;
- backlog status changes;
- edits to TS-001/TS-002 publication bytes;
- edits to existing Sol/Round B/Round C planning files.

All Round D findings are additive planning material on the existing planning branch only.

## Git discipline

- normal commits only;
- non-force push only;
- no reset/rebase/force/history rewrite/cherry-pick;
- unrelated files unchanged;
- final remote read-back required.

Final report must include:

- starting guard result;
- final branch HEAD/tree;
- changed files;
- Round D report blob SHA;
- source-resolution blob SHA;
- unresolved gap list.

## Terminal state

Normal completion is:

`TS-003 ROUND_D_TARGETED_FOLLOWUP_COMPLETE`

`AWAITING_SOL_ROUND_E_SCOPE_CLOSURE`

`NO_PRODUCTION_INITIALIZATION`

Stop there. Round E belongs to Sol.