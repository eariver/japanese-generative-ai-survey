# TS-003 Vision & Multimodal AI — Sol scope sufficiency audit before Worker reconnaissance

Status: `SOL_SCOPE_AUDIT / PRE_WORKER / NOT_PRODUCTION_AUTHORITY`

Date: `2026-09-30 JST`

Planning branch: `planning/ts-003-vision-multimodal-preresearch-20260930`

Companion skeleton:

`docs/research-plans/2026-09-30_ts-003-vision-multimodal-sol-preresearch-skeleton.md`

## 1. Audit purpose

Before asking Muse/Worker to perform reconnaissance, independently test whether the Sol skeleton is already broad enough to represent the intended TS-003 question, while still narrow enough to avoid becoming a generic survey of all computer vision, multimodal AI, robotics and world models.

The audit specifically asks:

1. Does TS-003 genuinely complement and reconnect TS-001 and TS-002?
2. Are any indispensable technical transitions missing?
3. Are any lanes over-expanded relative to the central question?
4. Is `Vision & Multimodal AI` broader than the current mostly vision-language skeleton actually supports?
5. Can the scope be stabilized before Worker reconnaissance so Muse is asked to challenge/refine a coherent map rather than invent one?

This document refines the planning skeleton. It is not Discovery, Evidence, Selection, Architecture or Human approval.

---

## 2. Overall disposition

`CONDITIONALLY SUFFICIENT AFTER THREE STRUCTURAL CORRECTIONS`

The existing D01-D15 map is directionally sound and does **not** require wholesale expansion. It already covers the major three-part flow:

1. learned/structured perception;
2. language-grounded multimodal representation and reasoning;
3. action/prediction endpoints.

However, three gaps are too important to leave implicit before Worker reconnaissance:

1. **open-vocabulary perception / language grounding** must become an explicit bridge, not a side note between detection and CLIP;
2. **data, supervision and post-training regimes** must become a mandatory cross-cutting axis, because the shift from class labels to image-text pairs, interleaved multimodal data, instruction data and synthetic/preference data is itself a major part of the technical history;
3. **audio/speech as an understanding input modality** must enter the multimodal convergence scope in a bounded way, otherwise `Multimodal AI` risks meaning only `vision + text` despite current native/omni systems spanning text, image, audio and video.

These corrections should be made without turning TS-003 into an audio-history volume or a robotics/world-model encyclopedia.

---

## 3. What is already necessary and should remain mandatory

The following existing lanes are justified and should remain mandatory unless Worker reconnaissance produces strong contrary evidence.

### A. Perception foundations

- D01 visual representation / CNN / ImageNet-scale learning;
- D02 detection / localization;
- D03 segmentation / dense perception / promptable perception;
- D04 geometry / depth / pose / spatial state;
- D05 OCR / document intelligence;
- D06 ViT / self-supervised visual foundation representations.

These lanes prevent modern VLM capability from appearing without the task-specific visual lineages it inherited or absorbed.

### B. Multimodal transition

- D07 vision-language alignment;
- D08 bridge architectures between pretrained vision and language models;
- D09 multimodal fusion/tokenization/context economics;
- D10 multimodal reasoning and failure decomposition;
- D11 video understanding / temporal state.

These are the core of the TS-003 identity and should receive more publication weight than the endpoint action/world-model lanes.

### C. Action and predictive endpoints

- D12 GUI / Computer Use;
- D13 VLA / embodied multimodal systems;
- D14 predictive representations / world models;
- D15 evaluation / robustness / convergence.

These remain mandatory as **convergence/end-point lanes**, not as permission to turn the Special into a complete robotics or model-based-RL history.

---

## 4. Structural correction 1 — make grounding/open-vocabulary perception explicit

### Problem

The skeleton currently contains:

- classical/closed-set detection in D02;
- image-level language alignment in D07;
- grounding again in reasoning/GUI/VLA downstream.

But the technical transition from `recognize a fixed class` to `localize an arbitrary language-referred concept` is central enough that it must not be left as a minor bridge sentence.

### Required revision

Refine D07 from:

`Vision-language alignment and open-vocabulary semantics`

into approximately:

`Vision-language alignment, open-vocabulary perception and grounding`

Mandatory questions:

- image-level alignment vs region/object grounding;
- fixed category ontology vs language-specified concept;
- zero-shot/open-vocabulary recognition vs open-vocabulary detection;
- referring-expression comprehension;
- phrase/region grounding;
- how language-conditioned detectors/segmenters connect CLIP-like semantics to actionable localization;
- how grounding quality propagates into GUI agents, VLA systems and visual evidence attribution.

Candidate anchors for reconnaissance:

- CLIP / ALIGN / SigLIP for image-level alignment;
- OWL-ViT or equivalent open-vocabulary detection transition;
- GLIP / Grounding DINO class of language-grounded detectors;
- referring-expression datasets/methods only as needed to establish the task distinction.

This is a true missing bridge, not merely another model family.

---

## 5. Structural correction 2 — data/supervision/post-training must be a mandatory cross-cutting axis

### Problem

The skeleton discusses architecture well, but the historical progression can be distorted if data and supervision are treated as background.

The field did not move only through backbone changes. It also moved through different supervision contracts:

```text
hand-labelled class/detection/segmentation targets
-> large supervised visual datasets
-> self-supervised visual pretraining
-> paired image-text web supervision
-> interleaved image-text documents
-> multimodal instruction tuning
-> synthetic multimodal instruction/reasoning data
-> preference/post-training and agent/action trajectories
```

This progression affects what concepts can be learned, what interfaces emerge, and what failures are inherited from the data.

### Required cross-cutting axis X01 — Data / supervision / post-training

Every relevant research lane should report, where applicable:

- data type and scale;
- label/supervision type;
- paired vs interleaved multimodal structure;
- human vs web-derived vs synthetic data;
- pretraining vs supervised/instruction fine-tuning vs preference/RL/post-training;
- presence of action trajectories or environment interaction data;
- multilingual/multi-domain coverage when technically material;
- known data authority limitations.

Important planning anchors include ImageNet, web-scale image-text pretraining, visual instruction tuning, and interleaved multimodal pretraining recipes.

Do **not** create a generic dataset catalogue. The question is how the supervision/data regime changed the model's usable representation and interface.

---

## 6. Structural correction 3 — broaden multimodality beyond vision+text, but only at convergence

### Problem

The Special is titled `Vision & Multimodal AI`, yet audio/speech currently appears mainly in D11 video and in negative space. That was acceptable for a VLM-only survey, but not sufficient for a convergence volume in 2026.

Modern native/omni systems increasingly accept combinations of:

- text;
- images;
- video;
- audio/speech;
- documents/screens;
- and, in embodied systems, proprioception/action state.

The key TS-003 question is not to retell audio-generation history from TS-002. It is to ask how heterogeneous observations are represented, temporally aligned, fused and reasoned over.

### Required revision to D09/D11

Expand D09 into approximately:

`Native/omni multimodal fusion, tokenization and context economics`

and require a bounded sub-lane for:

- audio/speech **understanding input**, not full speech-generation history;
- audio-video temporal alignment;
- different sampling/token rates across modalities;
- streaming multimodal interaction;
- whether modalities share one sequence/backbone or retain specialist encoders/components;
- modality-specific token compression and compute costs.

D11 video understanding should explicitly preserve audio-video joint understanding when audio is load-bearing.

Current open/first-party systems such as Qwen3-Omni and Gemini-family native multimodal models are suitable reconnaissance candidates because they expose the convergence problem across text/image/audio/video. They are **capstone candidates**, not automatic architecture authority for undisclosed details.

TS-002 remains the authority for the historical generation side of speech/audio/music/video.

---

## 7. Mandatory cross-cutting axes after the audit

The final TS-003 scope should keep D01-D15 but add explicit cross-cutting obligations rather than proliferating D-numbers.

### X01 — Data / supervision / post-training

As defined above.

### X02 — Objective and interface contract

For each major transition distinguish where applicable:

- classification/detection/segmentation loss;
- self-supervised/masked/distillation objective;
- contrastive image-text learning;
- captioning/generative language objective;
- next-token multimodal modeling;
- instruction tuning;
- preference/RL/post-training;
- action prediction / policy learning;
- predictive world-model objective.

Do not conflate architecture with training objective.

### X03 — TS-001 efficiency/context economics

Track only multimodal-specific consequences:

- image/video/audio token volume;
- resolution/frame/sample-rate effects;
- dynamic resolution / tiling;
- token pruning/resampling/compression;
- long multimodal context;
- KV-cache/memory impact;
- repeated screenshot/video observation loops;
- edge/on-device VLA latency;
- real-time/streaming constraints.

Generic MoE/quantization/serving history remains in TS-001.

### X04 — Reliability / evidence-use contract

Across reasoning/evaluation lanes track:

- visual hallucination / unsupported claims;
- language-prior success without visual evidence use;
- modality conflict;
- grounding/localization correctness;
- calibration/uncertainty where authoritative;
- tool-assisted perception;
- benchmark contamination and judge dependence;
- exact source-role and claim-strength preservation per CV2-DM-020.

---

## 8. Scope that should NOT become a new mandatory lane

The audit considered the following but does not recommend making them standalone mandatory dimensions before Worker reconnaissance:

### Multimodal retrieval / RAG

Relevant as a capability and interface under D05/D07/D10, especially document/video retrieval and multimodal embeddings, but not yet a separate historical lane.

### Medical / autonomous-driving / remote-sensing / scientific-imaging verticals

Use only when they reveal a generic architecture/evaluation issue. Otherwise they would turn TS-003 into an application-domain survey.

### NeRF / 3D Gaussian Splatting / full 3D reconstruction history

Potential support material for D04/world representation, but not automatically central to multimodal reasoning.

### Classical SLAM / control theory / robot kinematics

Include only the minimum context needed to explain D13. Do not expand into robotics fundamentals.

### Full speech recognition / speech-language-model history

TS-003 needs audio/speech understanding at the multimodal convergence layer, but a full audio lineage would duplicate/expand beyond TS-002 and distort the vision-centered Special.

### Safety/policy as an independent chapter

Include technical safety/reliability only where it materially affects multimodal perception/action/evaluation. Do not turn the Special into a policy survey.

---

## 9. Reweighting recommendation

The audit recommends a publication-weight hierarchy, subject to later Evidence/Architecture Review:

### Tier A — Core body

D01-D11.

This is where most of the technical history and explanatory depth should live.

### Tier B — Convergence endpoints

D12 GUI/Computer Use, D13 VLA, D14 World Models.

These should demonstrate where perception/grounding/reasoning becomes action/prediction, but should not consume more space than the multimodal core unless evidence density justifies it.

### Tier C — Cross-cutting synthesis

D15 + X01-X04.

Evaluation/data/efficiency/source-fidelity should be threaded through the volume and synthesized explicitly at the end.

This reweighting prevents the attractive current topics (robotics/world models) from crowding out the technical lineage that makes them understandable.

---

## 10. Historical sufficiency check

The current source skeleton is broadly adequate as a seed but must be expanded during Worker reconnaissance in four places:

1. **pre-deep visual representation:** add concise predecessor context such as Neocognitron/early CNN where it is needed to avoid starting history abruptly at AlexNet; do not build a full classical-CV chapter;
2. **vision-language before CLIP:** ensure captioning/VQA/visual-semantic embedding precedents are represented so CLIP does not appear ex nihilo;
3. **open-vocabulary grounding:** add explicit detection/grounding lineage as described above;
4. **multimodal data/training:** include representative primary work that exposes data mixture and instruction-tuning design, not only architecture papers.

Self-supervised vision, promptable segmentation, document intelligence, temporal video, GUI, VLA and world-model anchors are already sufficiently represented for a reconnaissance starting map.

---

## 11. 2026 capstone freshness correction

Do not freeze the current-case set to the older planning examples.

At Worker reconnaissance time, current capstone candidates should be refreshed against 2026 first-party/primary authority. The light audit found at least these useful *classes/examples*:

- an inspectable current VLM with explicit spatial/temporal/token architecture (e.g. Qwen3-VL class);
- an omni model spanning text/image/audio/video (e.g. Qwen3-Omni class);
- a current closed native multimodal reasoning model with first-party model card/eval material (Gemini 3.x class; exact version to be selected at source intake time);
- a current computer-use system/benchmark pair;
- a current VLA/embodied system, including on-device/latency-constrained cases (Gemini Robotics 2 / On-Device 2 class as one vendor case, plus open/independent authority where available);
- an interactive/action-controllable world model (Genie 3 class as a current first-party case, plus independent/academic alternatives where evidence permits).

These names are reconnaissance seeds only. Final case selection must be based on source richness, technical distinctiveness, independence, and non-redundancy with TS-001/002.

---

## 12. Final scope verdict before Muse

After this audit, the desired TS-003 research map is judged **necessary and sufficiently bounded for Worker reconnaissance** under the following conditions:

1. D01-D15 remain the base map;
2. D07 explicitly includes open-vocabulary perception and grounding;
3. D09/D11 explicitly include bounded audio/speech understanding and time-aligned multimodality;
4. X01-X04 are mandatory cross-cutting obligations;
5. D12-D14 are treated as convergence endpoints, not co-equal permission to survey all agents/robotics/world models;
6. vertical applications and classical robotics/3D histories remain support/context unless they reveal a general mechanism;
7. current capstones are refreshed from 2026 authority at reconnaissance time;
8. Muse is asked to challenge this map and identify omissions/redundancies, not to assume the Sol taxonomy is complete.

Under those constraints, further Sol-only broad research before Round B is unlikely to improve scope proportionally to its execution cost. The next useful information gain should come from a bounded Worker reconnaissance followed by Sol gap review.
