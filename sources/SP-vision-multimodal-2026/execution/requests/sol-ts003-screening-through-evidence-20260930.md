# TS-003 Muse execution — Screening through Evidence, then stop for Sol semantic review

Status:

`EXECUTION_AUTHORITY / DISCOVERY_PASS / SCREENING_EVIDENCE_ONLY / STOP_FOR_SOL_EVIDENCE_REVIEW`

Date: `2026-09-30 JST`

Issue:

`SP-vision-multimodal-2026`

Branch:

`special/vision-multimodal-2026-work`

## 0. Exact start guard

Before any write, read-only verify:

- remote work branch HEAD == `95cd2c363feab6dbda88f53ea36b1b125d4ba8c1`
- remote work branch tree == `c13b7ffd406c60f982b3f368f5b8c32e45bce49b`
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Also verify current canonical edition state:

- issue = `SP-vision-multimodal-2026`
- lifecycle = `DISCOVERY_COLLECTED`
- discovery checkpoint = `passed`
- screening/evidence/materiality/completeness/selection/architecture = `pending`
- Human Architecture Review = `pending`
- Human Publication Preview = `pending`
- Discovery acceptance record count = `111`
- Discovery unique locators = `111`

If any expected value differs, perform zero writes, report expected vs actual, and stop.

Do not create another branch. No fallback/repair/review/iteration branch.

No reset, rebase, force push, history rewrite, branch recreation or cherry-pick.

## 1. Mandatory authorities

Read in this order:

1. `sources/SP-vision-multimodal-2026/execution/sol-discovery-completeness-review-r1.md`
2. `sources/SP-vision-multimodal-2026/execution/discovery-coverage-20260930.md`
3. `sources/SP-vision-multimodal-2026/raw/discovery-negative-space-2026-09-30.md`
4. current `sources/SP-vision-multimodal-2026/production-profile.json`
5. current `sources/SP-vision-multimodal-2026/production-state.json`
6. current canonical Discovery artifacts and Raw observation lane files
7. `docs/research-plans/2026-09-30_ts-003-sol-round-e-scope-closure.md`
8. `docs/core-v2-deferred-maintenance-summary.md`, especially CV2-DM-006, CV2-DM-013 and CV2-DM-020
9. current CLI/help/schema for Screening and Evidence

The Sol Discovery Completeness Review is authoritative for whether Discovery may advance.

## 2. Mission

Perform exactly this bounded sequence:

1. canonical Screening over the accepted 111-record Discovery corpus;
2. preserve historically/load-bearing transition nodes and edition scope boundaries;
3. build Evidence with real semantic source consumption;
4. validate/checkpoint Screening and Evidence using current canonical Core v2 paths;
5. stop for fresh Sol Evidence Semantic Review.

Do **not** proceed into Materiality, Completeness, Selection, Architecture, Drafting or publication.

Target operational stop:

`EVIDENCE_BUILT / AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW`

Use the actual canonical lifecycle/state names emitted by current tooling; do not hand-invent state values.

## 3. Screening contract

Screening must not become a recency/popularity filter.

Preserve sources that are required to explain a transition even if they are old or no longer state of the art.

### 3.1 Mandatory lane integrity

The screened corpus must retain enough evidence to support all VM-O01..VM-O16 obligations.

In particular:

- VM-O01 may remain compact but must retain the pre-AlexNet context + AlexNet/ResNet transition.
- VM-O04 remains hard-capped/supporting; do not expand geometry/3D history.
- VM-O07 and VM-O08 remain separate.
- VM-O08 must retain a genuine grounding lineage rather than collapsing to a few famous endpoints.
- VM-O10 must include at least two technically distinct current open/inspectable VLM families; do not allow Qwen-only current architecture coverage.
- VM-O12 must preserve the distinction between offline long-context and online streaming.
- VM-O13/VM-O14/VM-O15 remain bounded endpoint lanes.
- VM-O15 must preserve latent dynamics and non-generative predictive representation counterweights to generative interactive environments.
- VM-O16 keeps evaluation contracts distinct and does not optimize for benchmark count.

### 3.2 No authority flattening

Do not promote:

- product/demo pages into architecture evidence;
- vendor benchmark claims into independent evaluation;
- repository existence into capability proof;
- benchmark score into general visual intelligence;
- current-system popularity into Selection materiality.

### 3.3 Negative space survives Screening

The six current gaps must remain visible unless actually resolved by authoritative evidence:

- G01 independent VLA evaluation scarcity;
- G02 transferable control-oriented world-model benchmark absent;
- G03 same-protocol document specialist/generalist comparison absent;
- G04 real-deployment latency/VRAM beyond author-reported values;
- G05 independent reproduction of 2026/current vendor/model-report scores;
- G06 SigLIP2 exact citation binding.

Screening is not allowed to hide gaps by dropping the lane that exposes them.

## 4. Evidence — required semantic depth

Evidence construction is the main purpose of this execution.

Discovery summaries are not sufficient Evidence.

For retained sources, perform real semantic consumption of the actual paper/report/card/repository/documentation required to support the claim.

### 4.1 Common analytical coordinate system

Every major transition should, where source-supported, capture:

1. prior representation/interface bottleneck;
2. input representation/state;
3. training target / supervision contract;
4. mechanism or interface change;
5. output contract;
6. what new operation becomes possible;
7. what information/capability remains missing;
8. compute/token/memory/latency consequence where material;
9. evaluation method and its limitations;
10. successor/inheritance relation;
11. exact source authority and claim-strength boundary.

The cross-cutting question remains:

`What representation of the world is sufficient for the next computation?`

Do not reduce Evidence to chronological summaries.

## 5. Lane-specific Evidence requirements

### VM-O01 — learned visual representation

Explain the transition from task/hand-engineered or shallow visual features to learned reusable representation without turning this into a full classical-CV history.

Evidence must make clear why AlexNet/ImageNet/GPU-scale supervised learning mattered and what ResNet changed for reusable deep representation/training depth.

### VM-O02 — detection

Keep distinct:

- image classification;
- two-stage region detection;
- one-stage operating point;
- anchor/NMS-heavy formulation;
- set prediction / DETR-style formulation;
- open-vocabulary bridge.

Do not use `DINO` without explicit disambiguation between detector and self-supervised model family.

### VM-O03 — segmentation

Preserve semantic/instance/panoptic/promptable distinctions.

U-Net may appear only in its segmentation lineage; do not re-teach diffusion U-Net history from TS-002.

### VM-O04 — spatial/geometry substrate

Evidence is bounded to the four-node support contract unless an exact same-contract substitution is necessary:

- MiDaS;
- OpenPose;
- Visual Genome;
- DUSt3R.

The purpose is to explain spatial state, not build a 3D reconstruction survey.

### VM-O05 — document intelligence

Treat OCR/layout/document structure as technical representation/interface problems.

Specialist vs generalist comparison must remain qualitative unless Evidence establishes identical protocol conditions.

If no same-protocol comparison exists, preserve `NO_CROSS_MODEL_NUMERIC_COMPARISON`.

### VM-O06 — ViT / self-supervised foundation vision

Separate:

- patch/token representation;
- architecture;
- pretraining objective;
- teacher/distillation/self-supervised mechanism;
- encoder reuse into VLMs.

Generic attention efficiency remains TS-001-owned.

### VM-O07 — image-level vision-language alignment

Evidence must establish the change from fixed class ontology to language-addressable image-level semantics.

Keep image-level zero-shot/retrieval evaluation identity separate from grounding/localization evaluation.

### VM-O08 — grounding

For each major retained transition, capture the changed contract rather than only model name:

- phrase localization / referring expression;
- open-vocabulary detection;
- distillation vs region pretraining vs vocabulary supervision;
- detection-as-grounding reformulation;
- early/tight/late fusion differences where supported;
- open-vocabulary segmentation branch;
- actionable grounding handoff.

Do not create one synthetic ranking table across LVIS-rare, RefCOCO, phrase localization and D07A retrieval metrics.

### VM-O09 — bridge VLMs

Explain the technical role of projector/resampler/Q-Former/cross-attention/frozen-component strategies and visual instruction tuning.

Flamingo, BLIP-2 and LLaVA-class systems should not be flattened into one generic `vision encoder + LLM` sentence.

### VM-O10 — native/omni multimodal fusion

Capture, where authoritative:

- visual/audio/video tokenization;
- dynamic resolution / tiling / resampling;
- position/time encoding;
- fusion location/interface;
- interleaved context handling;
- token/context cost;
- audio-video time alignment;
- current open implementation/repository constraints.

Qwen3-VL/Qwen3-Omni may be architecture cases only where technical reports/repositories actually support the claim.

InternVL/Molmo-class alternatives must be used to test whether the narrative is Qwen-specific.

Audio remains input/fusion/reasoning-only; speech/music generation mechanisms stay outside TS-003.

### VM-O11 — reasoning/failure decomposition

Separate:

- perception failure;
- OCR/text-recognition failure;
- grounding/localization failure;
- language-prior shortcut;
- reasoning failure;
- hallucination/evidence-use failure;
- scaffold/tool/test-time-compute effects.

Do not call one benchmark a measure of general multimodal intelligence.

### VM-O12 — video/temporal state

Distinguish frame sampling and offline long-context from online streaming state.

Where systems claim streaming, capture memory/update policy and latency constraints if source-supported.

Long-video benchmark numbers must bind frame/input policy, subtitle/audio use and model version.

### VM-O13 — Computer Use

Evidence should move beyond click accuracy:

`screenshot/document perception -> element grounding -> action interface -> persistent task state -> verification`

Distinguish pure-vision, accessibility/DOM, API/tool and mixed interfaces.

OSWorld 1.0 and 2.0 must not be treated as identical evaluation contracts.

### VM-O14 — VLA

Maintain the predecessor distinctions:

- SayCan: planner-side language × affordance, not joint representation;
- RT-1: trajectory/data regime;
- PaLM-E: embodied joint representation;
- Open X-Embodiment: cross-embodiment data contract;
- RT-2: action tokenization / VLA formulation;
- OpenVLA: inspectable open implementation;
- current Gemini Robotics-class endpoint: capability/deployment/card-scoped evaluation only where supported.

Do not fill independent-evaluation gaps using vendor pages.

### VM-O15 — predictive representations / World Models

Every retained case must explicitly bind:

- represented state;
- predicted target;
- action conditioning;
- pixel vs latent vs reward/action target;
- use for representation learning, planning, training or evaluation.

At minimum preserve distinct poles for:

- historical latent world-state formulation;
- Dreamer-family latent dynamics/model-based decision;
- JEPA/V-JEPA-family predictive representation without photorealistic generation;
- Genie-family interactive generative environment.

Do not imply direct ancestry where none is established.

Genie 3 official pages remain capability/deployment authority only unless a real architecture source exists.

### VM-O16 — evaluation/provenance/convergence

Evidence must bind exact evaluation conditions where relevant:

- benchmark version;
- dataset/subset;
- model version/date;
- image/video/audio input policy;
- frame count/resolution/context;
- tool access;
- thinking/scaffold/test-time compute;
- judge/answer extraction;
- metric semantics;
- vendor vs independent authority;
- contamination/version-drift limitations.

No bare-score leaderboard.

## 6. Current-system source-role discipline

For every current system, keep role tags separate:

- `ARCHITECTURE_CASE`
- `CAPABILITY_CASE`
- `DEPLOYMENT_CASE`
- `EVALUATION_CASE`

One source may fill only the roles it actually supports.

Dynamic repositories/pages must be rebound to exact commit/version/date where material.

Any current-family currency change discovered during Evidence should be recorded as provenance/version context, not silently substituted in a way that changes the historical Discovery corpus without explanation.

## 7. Date/provenance discipline

Apply CV2-DM-013 strictly.

Do not conflate:

- paper first submission;
- paper revision;
- conference publication;
- model announcement;
- product release;
- model-card publication/update;
- repository state;
- Evidence retrieval time.

If a source has ambiguous chronology, preserve the ambiguity explicitly.

## 8. Evidence artifact expectations

The resulting Evidence should be deep enough for later Materiality/Selection/Architecture without rediscovering source semantics.

For each evidence unit, capture as applicable:

- source identity;
- exact claim;
- mechanism;
- input/output representation;
- supervision/data contract;
- grounding/fusion/action interface;
- efficiency/runtime consequence;
- evaluation protocol;
- limitations/trade-offs;
- historical role;
- successor/inheritance/counterexample;
- source-role cap;
- provenance/version/date.

Do not optimize for brevity.

## 9. Validation and stop

Use current canonical Core CLI/helpers for Screening and Evidence.

Validate/checkpoint each stage according to the current schema.

At the end verify:

- Screening completed and passed;
- Evidence completed/built and passed according to current canonical state;
- Materiality remains pending;
- Completeness remains pending;
- Selection remains pending;
- Architecture remains pending;
- no Human Gate decision exists;
- main unchanged;
- Production Core unchanged;
- no new branch;
- no force/reset/rebase/rewrite;
- no X/community pass unless a deterministic current-Core requirement makes a zero-content manifest update necessary.

## 10. Required final report

Report:

- exact starting HEAD/tree;
- exact main/Core guards;
- Screening input count and dispositions;
- retained source count;
- Evidence unit count;
- per-VM-O01..VM-O16 Evidence coverage;
- X01..X04 semantic coverage;
- source-role binding summary;
- full-text vs abstract/page-only consumption accounting;
- resolved vs unresolved G01..G06;
- any source/date/version corrections found;
- validator/checkpoint results;
- final remote HEAD/tree;
- lifecycle state;
- explicit confirmation that Materiality/Completeness/Selection/Architecture were not run.

Terminal operational state:

`TS-003 SCREENING_EVIDENCE_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`
