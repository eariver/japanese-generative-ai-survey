# TS-003 Vision & Multimodal AI — Sol pre-research skeleton

Status: `SOL_PRERESEARCH_SKELETON / PRE_DISCOVERY / NOT_PRODUCTION_AUTHORITY`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Planning branch: `planning/ts-003-vision-multimodal-preresearch-20260930`

Planning base: `d6381568cc897a47d6de992189e20339350342b7`

Planning identity: `TS-003`

Working title:

> **Vision & Multimodal AI — 検知・認識からVLM・World Modelへ**

This document is a Sol-authored **research skeleton** created before production initialization. It is intentionally lighter than a full Discovery run. It defines the questions, research lanes, cross-Special relationships, anti-thinness rules, candidate historical anchors, current-capstone directions, evaluation map, negative space, and the proposed Sol↔Worker rally process.

It is **not** Discovery, Evidence, Selection, Architecture, Human approval, or publication prose. All candidate papers/models/benchmarks below remain subject to normal source intake and authority validation.

---

## 1. Editorial role of TS-003

TS-003 should not be a generic history of computer vision and should not be a catalogue of famous multimodal models.

The intended role is to **complete and reconnect the technical space opened by TS-001 and TS-002**.

- **TS-001 Efficient Intelligence:** how intelligence is computed efficiently — compute, memory, attention, MoE, precision, decoding, serving, routing, deployment economics.
- **TS-002 Beyond Text:** how non-text media is represented and generated — representation, objective, conditioning, control, editing, temporal structure, runtime, evaluation.
- **TS-003 Vision & Multimodal AI:** how observed worlds become machine-usable representations — perception, recognition, localization, language alignment, grounding, multimodal fusion, reasoning, temporal/spatial understanding, action, and predictive world representation.

A compact three-Special framing is:

```text
TS-001: compute the intelligence
TS-002: generate the world
TS-003: perceive, ground, reason about, predict, and act in the world
```

TS-003 should therefore function as a **convergence volume**, not merely a sequel to classical computer vision.

---

## 2. Central technical question

Provisional Core Question:

> AIは、画像や映像を単に分類する段階から、対象の位置・構造・時間関係を認識し、言語概念へ接地し、複数modalを統合して推論し、予測や行動へ利用できる内部表現を形成する段階へ、どのように発展してきたのか。

A second question should run through the whole Special:

> **What representation of the world is sufficient for the next computation?**

That question changes by stage:

- classification needs category-discriminative representation;
- detection needs object identity + localization;
- segmentation needs dense region/pixel structure;
- OCR/document AI needs visual structure + symbolic content + layout;
- CLIP-like systems need language-addressable visual semantics;
- VLMs need representations usable by language reasoning;
- video models need temporal state;
- GUI agents need actionable visual grounding;
- VLA systems need perception linked to motor/action spaces;
- world models need state representations from which future observations or dynamics can be predicted.

The desired historical map is therefore not a single ladder such as:

```text
CNN -> YOLO -> ViT -> CLIP -> VLM -> VLA -> World Model
```

Instead, TS-003 should reconstruct a directed graph of partially independent lineages that later converge.

---

## 3. Working coordinate system

The current backlog uses:

```text
Perception -> Recognition -> Understanding -> Multimodal reasoning
```

This remains useful but is too linear for production. For pre-research, use the expanded coordinate system:

```text
Representation
  -> Recognition
  -> Localization / Structure
  -> Language Alignment
  -> Grounding
  -> Multimodal Fusion
  -> Temporal / Spatial State
  -> Reasoning
  -> Action and/or Prediction
```

These are **problem layers**, not eras. Multiple approaches can coexist, and later systems may retain older components.

---

## 4. Anti-thinness requirements

A TS-003 package is incomplete if it becomes any of the following:

- `AlexNet -> YOLO -> ViT -> CLIP -> GPT-like VLM -> World Model` as a model chronology;
- a leaderboard of current VLMs;
- a general robotics survey;
- a duplicate of TS-002 image/video generation history;
- a generic “multimodal AI can see images now” narrative;
- a list of benchmarks without analysis of what each benchmark actually measures;
- a vision-only survey that treats language, action, geometry, and temporal state as appendices.

At minimum the final research base should establish:

1. **Representation is first-class.** Track what visual information is preserved, compressed, discarded, localized, tokenized, or converted to language-addressable semantics.
2. **Task structure matters.** Classification, detection, segmentation, OCR, VQA, grounding, video understanding, GUI interaction and robot control are not interchangeable forms of “vision”.
3. **Closed-set to open-vocabulary transition is explicit.** Fixed label spaces and language-addressable concepts must be distinguished.
4. **Recognition and grounding are different.** Knowing “what” is present is not the same as identifying “where” or “which one”.
5. **Understanding and generation are different but increasingly coupled.** Reuse TS-002 where useful, but do not claim that generative capability automatically proves understanding.
6. **Visual backbone and multimodal fusion must be separated.** Vision encoder choice is not the same design axis as projector/Q-Former/cross-attention/native multimodal fusion.
7. **Token/context economics is first-class.** Image/video token count, dynamic resolution, resampling, pruning, memory and attention cost connect directly to TS-001.
8. **Spatial and temporal state must be explicit.** Multi-image, video, 3D, GUI and embodied tasks require more than single-image semantics.
9. **Action is not just another text output.** GUI and robotics require grounding into an executable action space and environment feedback.
10. **World model is a loaded term.** Do not collapse video generator, predictive representation, learned dynamics model, simulator, and action-conditioned world model into one category.
11. **Evaluation must preserve task identity.** OCR accuracy, detection mAP, segmentation IoU, VQA accuracy, multimodal reasoning benchmarks, GUI task success, robotics success and world-model fidelity are different authorities.
12. **Source-faithful claims are mandatory.** Apply the W39 CV2-DM-020 lesson: citation resolution alone does not prove the claim preserves novelty, scope, strength, conditions, or source role.
13. **Canonical terminology must survive.** Apply CV2-DM-006 before publication; no forced literal translation of model/task/metric names.
14. **Frontier vendor claims remain vendor claims unless independently reproduced.** Capability demonstrations do not automatically establish mechanism or generality.

---

## 5. Boundary and integration with TS-001 / TS-002

### 5.1 Reuse rather than duplicate

TS-003 may reuse the same technical object when the question changes.

Examples:

| Technical object | TS-001 angle | TS-002 angle | TS-003 angle |
| --- | --- | --- | --- |
| Transformer / attention | compute, memory, long context | media backbone where relevant | visual tokens, multimodal fusion, reasoning |
| ViT | attention/token efficiency when relevant | generation backbone only when load-bearing | visual representation and Transformerization of vision |
| CLIP | deployment/compute only if material | conditioning/alignment for generation | open-vocabulary visual-language alignment |
| VAE / tokenizer | memory/compute only if material | compress media for generation | perceptual/multimodal token budget only where used for understanding/fusion |
| video model | context/runtime | generation, motion, temporal consistency | recognition, temporal grounding, memory, reasoning |
| quantization / pruning | core subject | generation deployment where material | VLM/VLA deployment only where perception-token or edge constraints matter |
| world model | efficiency only if architecture/runtime material | generated/simulated world as media | predictive/action-conditioned state model and agent interaction |

### 5.2 TS-002 boundary

Default to TS-002 when the primary question is:

> What is generated, by what representation/objective/sampler/control/editing mechanism?

Default to TS-003 when the primary question is:

> What is perceived, represented, aligned, grounded, reasoned about, predicted, or acted upon?

Generation can appear in TS-003 when it is a component of reasoning, predictive simulation, environment modeling, or unified multimodal representation — but TS-003 should cross-reference rather than retell the full generative lineage.

### 5.3 TS-001 boundary

Default to TS-001 when the primary question is:

> How is compute/memory/latency/throughput/cost reduced or scheduled?

TS-003 should reuse that vocabulary when multimodality creates a new bottleneck:

- visual token explosion;
- high-resolution/dynamic-resolution input;
- long video context;
- multi-image context;
- KV-cache impact;
- resampler/projector bottlenecks;
- edge/on-device VLM/VLA deployment;
- real-time perception-action latency.

TS-003 should not retell generic quantization, MoE, serving, speculative decoding, or low-bit history unless a multimodal-specific consequence is load-bearing.

---

## 6. Mandatory research dimensions

### D01 — Visual representation before and through deep learning

Core questions:

- What changed when handcrafted visual features gave way to learned feature hierarchies?
- What information did classification-oriented representation preserve and discard?
- How much of later multimodal AI depends on reusable representation rather than task-specific prediction heads?

Candidate historical anchors:

- SIFT / HOG / bag-of-visual-words as concise context, not a full pre-deep-learning CV history.
- LeNet/CNN lineage where needed.
- AlexNet / ImageNet 2012 as large-scale supervised CNN + GPU scaling landmark.
- VGG / GoogLeNet / ResNet as representation-depth/scaling transitions.

Light read-back note:

- AlexNet's paper explicitly combined a large deep CNN with efficient GPU convolution and large-scale ImageNet classification.
- ResNet reframed deep-network optimization through residual functions and demonstrated transfer to detection/segmentation workloads.

### D02 — Classification to detection and structured localization

Core questions:

- Why is image-level classification insufficient for scene understanding?
- What changed between sliding-window / region-proposal pipelines, two-stage detectors and one-stage detectors?
- How did anchors, NMS and hand-designed detection machinery become architectural assumptions?
- What did DETR change by reformulating detection as set prediction?

Candidate anchors:

- R-CNN / Fast R-CNN / Faster R-CNN.
- YOLO family as real-time one-stage detection lineage; do not reduce the entire one-stage history to one product family.
- SSD / RetinaNet where necessary for lineage completeness.
- DETR.
- open-vocabulary detection/grounding later as a bridge into language alignment.

Light read-back note:

- DETR explicitly removes several hand-designed detection components such as anchor generation/NMS and casts detection as direct set prediction with a Transformer encoder-decoder.

### D03 — Dense perception: segmentation, promptable vision and pixel-level foundation models

Core questions:

- semantic vs instance vs panoptic segmentation;
- dense prediction vs object box prediction;
- what changed when segmentation became promptable and zero-shot transferable?

Candidate anchors:

- FCN.
- U-Net only where vision-segmentation history requires it; distinguish from its TS-002 diffusion-backbone role.
- Mask R-CNN.
- panoptic segmentation.
- Segment Anything / SAM-family.

Light read-back note:

- Segment Anything framed segmentation as a promptable task/model/data system and built SA-1B with over one billion masks, explicitly targeting zero-shot transfer.

### D04 — Geometry, depth, pose, 3D and spatial state

This is mandatory so that embodied/spatial reasoning does not appear from nowhere.

Research lanes:

- monocular/stereo depth;
- optical flow only where useful for temporal state;
- keypoints / pose;
- multi-view geometry and learned 3D representation;
- point clouds / voxel / implicit scene representation only as needed;
- spatial relations, camera coordinates and object-centric state;
- scene graphs where historically/materially important.

Questions:

- What spatial information is absent from category labels?
- How is metric/relative geometry represented?
- What survives when 3D or continuous space is compressed into language tokens?

Boundary:

Do not expand into a full SLAM/robotics textbook. Include geometry where it materially explains modern multimodal/spatial/embodied reasoning.

### D05 — OCR to Document Intelligence and visual knowledge work

Core questions:

- recognition of glyphs vs understanding document structure;
- OCR + layout + reading order + tables + charts + equations + figures;
- image-rendered text vs native text extraction;
- document VQA and multimodal knowledge work;
- screenshots/UI as structured visual documents.

Candidate lanes:

- OCR historical context only as needed.
- document layout models.
- LayoutLM/Donut/Pix2Struct-type transitions where supported.
- chart/table/document VLM benchmarks.
- multimodal PDF/document reasoning.

TS-003 should explicitly test whether “native multimodal” models truly remove OCR/layout bottlenecks or merely move them inside the model.

### D06 — Transformerization and self-supervised visual foundation models

Core questions:

- what did ViT change relative to convolutional inductive bias?
- why do large-scale pretraining and transfer matter?
- how did masked/self-distillation/self-supervised approaches reduce dependence on class labels?
- what is a reusable visual foundation representation before language alignment?

Candidate anchors:

- Vision Transformer (ViT).
- DeiT where data-efficient training matters.
- Swin / hierarchical vision Transformer where needed.
- MAE.
- DINO / DINOv2.

Light read-back notes:

- ViT treats an image as a sequence of patches and shows that a pure Transformer can compete strongly when pretrained at scale.
- DINOv2 explicitly targets all-purpose visual features and scales self-supervised pretraining with curated diverse data and large ViT models.

### D07 — Vision-language alignment and open-vocabulary semantics

This is a major bridge from classical vision to modern multimodal AI.

Core questions:

- fixed class ontology vs natural-language-addressable concepts;
- paired image-text pretraining;
- contrastive objectives vs generative captioning objectives;
- zero-shot transfer and open-vocabulary recognition;
- limitations of language supervision and dataset semantics.

Candidate anchors:

- early image-text embedding/captioning context where necessary.
- CLIP.
- ALIGN / SigLIP where materially distinct.
- open-vocabulary detection/segmentation descendants.

Light read-back note:

- CLIP explicitly contrasts fixed predetermined class supervision with learning from image-text pairs and uses natural language to reference learned visual concepts for zero-shot transfer.

TS-002 cross-reference:

CLIP appeared there as conditioning/alignment machinery for generation. TS-003 should instead treat it as a transition in **what visual concepts can be addressed by language**.

### D08 — Bridging pretrained vision and pretrained language models

Core questions:

- frozen vision encoder + frozen/mostly frozen LLM vs end-to-end joint training;
- projector vs resampler vs Q-Former vs cross-attention;
- why bridging pretrained unimodal systems can be compute-efficient;
- where modality mismatch remains.

Candidate anchors:

- Flamingo.
- BLIP-2.
- LLaVA.
- related bridge architectures only when they materially change the design space.

Light read-back notes:

- BLIP-2 bootstraps from frozen image encoders and frozen LLMs using a lightweight Querying Transformer.
- LLaVA connects a vision encoder and LLM and makes visual instruction tuning a central training step.

TS-001 cross-reference:

This is an explicit efficiency/design trade-off: bridge a frozen pretrained vision system and frozen/mostly-frozen LLM, or train a more deeply unified multimodal stack.

### D09 — Native multimodal fusion, tokenization and context economics

This lane should distinguish “VLM as connected modules” from more deeply integrated multimodal foundation models.

Questions:

- how are images converted to tokens/embeddings?
- fixed resolution vs dynamic resolution / tiling;
- token count per image/frame;
- resampling / token compression / token pruning;
- early vs late fusion;
- cross-attention vs unified sequence;
- modality-specific encoders vs shared/native multimodal backbone;
- multi-image and long-video context;
- visual token impact on attention cost and KV cache.

TS-001 integration is mandatory here.

Required measurement fields where sources allow:

- visual tokens / patches / frames;
- input resolution;
- context expansion;
- memory footprint;
- latency / throughput;
- training/fine-tuning cost;
- on-device/edge constraints.

### D10 — Multimodal reasoning and failure decomposition

Do not treat one “multimodal benchmark score” as general vision intelligence.

Separate at minimum:

- object/property recognition;
- OCR/text-in-image;
- counting;
- spatial relations;
- geometry;
- charts/tables/diagrams;
- scientific figures;
- multi-image comparison;
- visual commonsense;
- compositional reasoning;
- hallucination / unsupported visual claims;
- visual evidence localization/grounding.

Research should distinguish:

- language prior success;
- actual visual evidence use;
- benchmark contamination;
- chain-of-thought/reasoning scaffold effects;
- tool-assisted perception.

### D11 — Video understanding, temporal memory and event grounding

TS-002 generated video; TS-003 understands observed video.

Core questions:

- image recognition repeated over frames vs genuine temporal modeling;
- action recognition;
- event localization;
- temporal ordering;
- causal/physical reasoning;
- long-video memory and retrieval;
- audio-video integration where understanding requires both;
- online/streaming video understanding.

Research should ask what state is actually retained across time, and how context length/token budget constrains long-video reasoning.

### D12 — GUI / Computer Use as actionable visual grounding

This is the digital-world bridge from perception to action.

Core questions:

- screenshot parsing;
- element grounding;
- OCR/UI semantics;
- coordinate/action prediction;
- dynamic state after actions;
- visual vs accessibility-tree / DOM/tool use;
- multi-application task execution;
- error recovery and closed-loop observation.

Candidate anchor:

- OSWorld and later successors.

Light read-back note:

- OSWorld evaluates open-ended tasks in real operating-system environments and identifies GUI grounding and operational knowledge as major deficiencies in the evaluated multimodal agents.

TS-001 integration:

Computer use creates latency and interaction-cost requirements; token-heavy screenshot loops and repeated perception should be treated as systems costs, not just model capability.

### D13 — Vision-Language-Action and embodied multimodal systems

VLA is not simply a VLM with a robotics output head.

Questions:

- observation/action representation;
- action tokenization;
- policy learning vs language reasoning;
- web-scale vision-language pretraining transferred into robot control;
- embodiment-specific vs multi-embodiment generalization;
- closed-loop control and latency;
- on-device deployment;
- safety/uncertainty only insofar as technically load-bearing.

Candidate anchors:

- RT-1 where necessary.
- RT-2.
- OpenVLA / related open VLA work where authoritative.
- Gemini Robotics family as current vendor case, with mechanism/generalization claims treated according to source authority.

Light read-back notes:

- RT-2 co-fine-tunes vision-language models with robotic trajectory data and represents robotic actions as text tokens, explicitly defining a VLA formulation.
- Google DeepMind's Gemini Robotics line explicitly extends multimodal models into vision-language-action and embodied reasoning, including later on-device variants; vendor capability statements remain vendor evidence until independently reproduced.

### D14 — Predictive representations and World Models

This lane must be terminologically strict.

Do not treat these as synonyms:

- video prediction;
- latent dynamics model;
- predictive representation learning;
- learned simulator;
- generative interactive environment;
- action-conditioned world model;
- planning model.

Core questions:

- what state is represented?
- what is predicted: pixels, latents, rewards, actions, observations, object states?
- is the model conditioned on action?
- can trajectories branch under different actions?
- is the model used for planning/training/evaluation, or only generation?
- does generated video imply usable dynamics?

Candidate historical/context anchors:

- model-based RL / learned dynamics sufficient to establish terminology;
- World Models (Ha & Schmidhuber) where lineage is supported;
- Dreamer-family where relevant;
- Genie / Genie 2 as modern generative-interactive world-model cases.

Light read-back note:

- Genie 2 is explicitly presented as an action-controllable foundation world model: given actions and prior latent frames it autoregressively generates subsequent observations. This is a useful example of why “world model” should be tied to action-conditioned dynamics rather than generic video generation.

TS-002 cross-reference:

The same generative machinery may appear in video generation, but TS-003 asks whether the representation supports **state, counterfactual action and prediction**, not merely visual realism.

### D15 — Evaluation, robustness, provenance and convergence

This should be a full research lane.

Classical/task-specific metrics may include:

- ImageNet classification accuracy;
- detection mAP;
- segmentation IoU / mask quality;
- OCR/CER/WER where applicable;
- retrieval/alignment measures;
- VQA/task accuracy;
- grounding/localization accuracy;
- video temporal/event metrics;
- GUI task success;
- robot task success;
- world-model predictive/control-oriented measures.

Multimodal benchmark analysis must preserve:

- task identity;
- dataset version;
- image resolution/input policy;
- chain-of-thought/tool allowance;
- model/version identity;
- judge type;
- answer extraction;
- contamination risk;
- vendor vs independent measurement.

Final convergence questions:

- Will perception/generation/reasoning/action converge in a single native multimodal model?
- Or will specialized visual encoders, generators, planners, tools and action models remain modular?
- Does a unified token interface imply unified internal representation?
- Which bottlenecks remain stubbornly modality-specific?

The Special should end with evidence-backed open questions, not a predetermined “everything becomes one model” conclusion.

---

## 7. Provisional historical anchor map

This is only a starting map for Worker reconnaissance. It is **not an accepted source set**.

### Learned visual representation / recognition

- Krizhevsky, Sutskever, Hinton — *ImageNet Classification with Deep Convolutional Neural Networks* (2012).
- He et al. — *Deep Residual Learning for Image Recognition* (CVPR 2016).

### Detection / structured perception

- Girshick et al. — R-CNN lineage.
- Ren et al. — Faster R-CNN.
- Redmon et al. — YOLO lineage.
- Carion et al. — *End-to-End Object Detection with Transformers* / DETR (2020).

### Segmentation / promptable perception

- Long et al. — FCN.
- He et al. — Mask R-CNN.
- Kirillov et al. — *Segment Anything* (2023).

### Transformer / self-supervised visual foundation

- Dosovitskiy et al. — *An Image is Worth 16x16 Words* / ViT.
- He et al. — *Masked Autoencoders Are Scalable Vision Learners*.
- Oquab et al. — *DINOv2*.

### Vision-language alignment / VLM bridge

- Radford et al. — CLIP.
- Alayrac et al. — Flamingo.
- Li et al. — BLIP-2.
- Liu et al. — LLaVA.

### Action / interactive environments

- Brohan et al. — RT-2.
- Xie et al. — OSWorld.
- Bruce et al. — Genie.
- Google DeepMind — Genie 2 / Gemini Robotics family as current first-party cases, subject to normal evidence-strength boundaries.

A later reconnaissance pass should add missing predecessors, alternative lineages, negative results, and non-US/non-big-lab contributions rather than letting the source map become a famous-paper canon.

---

## 8. Provisional current-capstone directions

Do **not** lock these as the final current-model set yet. Worker reconnaissance should determine which cases are sufficiently source-rich and technically distinct.

Candidate capstone classes:

1. **Native multimodal foundation model** — text/image/audio/video integration, long multimodal context, reasoning.
2. **Open / inspectable VLM** — architecture, visual tokenization, fine-tuning, deployment and independent evaluation can be examined.
3. **Document/UI specialist or strong generalist** — OCR/layout/chart/UI grounding.
4. **Long-video / streaming multimodal system** — temporal memory and context economics.
5. **Computer-use agent stack** — visual grounding + action + environment feedback.
6. **VLA / embodied system** — visual-language representation connected to physical action.
7. **World-model system** — action-conditioned predictive environment rather than ordinary media generation.

Selection criteria:

- technical distinctiveness;
- accessible first-party/primary material;
- architecture/source transparency;
- independent evaluation availability;
- non-redundancy with TS-001/002;
- evidence sufficient to discuss limitations rather than only marketing claims.

---

## 9. Negative-space requirements

Worker reconnaissance must explicitly report areas where evidence is sparse or terminology is unstable.

At minimum check:

- non-Transformer visual representations that remain competitive/material;
- open-vocabulary perception outside CLIP-style contrastive alignment;
- 3D/spatial representations that do not fit VLM token narratives;
- multimodal models where visual capability may be largely OCR/language-prior driven;
- specialist document/UI models vs general VLMs;
- audio as an input-understanding modality, which TS-002 treated mainly from generation side;
- multimodal systems that are modular rather than native/unified;
- world-model work not based on photorealistic video generation;
- embodied systems where action representation/control, not perception, is the real bottleneck;
- edge/on-device multimodal systems where TS-001 efficiency becomes decisive.

A low-yield lane must not silently disappear. Report it as `LOW_YIELD`, `OUT_OF_SCOPE`, `EVIDENCE_GAP`, or `MERGE_CANDIDATE` with rationale.

---

## 10. Proposed Sol ↔ Worker rally before production Discovery

For large Specials, do **not** jump directly from this Sol memo to a one-shot exhaustive Worker Discovery.

Use an iterative pre-production loop:

### Round A — Sol skeleton

Current document.

Outputs:

- editorial thesis;
- mandatory dimensions;
- boundaries;
- initial anchor map;
- current-capstone classes;
- anti-thinness rules.

### Round B — Worker reconnaissance

Worker performs a **bounded reconnaissance**, not canonical Discovery.

For each D01–D15:

- candidate primary/official sources;
- missing predecessor/successor nodes;
- competing technical interpretations;
- likely source-access blockers;
- possible duplicated scope with TS-001/002;
- candidate current cases;
- initial evidence-density estimate;
- proposed split/merge of dimensions.

No production state mutation, no Screening/Evidence, no claim of completeness.

### Round C — Sol synthesis / gap review

Sol reviews Worker reconnaissance and decides:

- which lanes are mandatory;
- which are support/context only;
- which need another pass;
- which need broader/non-obvious sources;
- which current cases are redundant or marketing-heavy;
- whether the Core Question must change.

### Round D — Worker targeted follow-up

Only targeted unresolved lanes are researched further.

Examples:

- weak 3D/spatial lineage;
- missing OCR/document bridge;
- world-model terminology ambiguity;
- native multimodal architecture uncertainty;
- non-Western/open-source lineage gaps;
- evaluation benchmark gaps.

### Round E — Sol scope closure

Sol produces the **pre-Discovery production contract**:

- final mandatory research dimensions;
- accepted planning boundaries;
- Discovery minimum coverage requirements;
- initial obligation map;
- source authority policy;
- current-capstone requirements;
- TS-001/002 cross-reference policy;
- negative-space requirements;
- terminal stop for first production run.

Only after Round E should production initialization and canonical Discovery begin.

This rally is intended to prevent a Worker from compressing a broad Special into the first plausible taxonomy it finds.

---

## 11. Likely first production stop

If the rally converges, the first production run should likely mirror TS-002:

```text
INITIALIZE_THEMATIC
  -> canonical research scope / obligations
  -> primary-technical-first Discovery
  -> Discovery acceptance
  -> STOP at DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW
```

Do not authorize Screening or Evidence until Sol has independently reviewed Discovery completeness and cross-lane balance.

Because TS-003 spans classical CV, multimodal foundation models, agents and world models, one-shot Discovery completeness is unlikely to be trustworthy without this stop.

---

## 12. Planning-level page/depth expectation

No production page target is authoritative at this stage.

However, the topic is broader than a narrow VLM survey. If D01–D15 survive reconnaissance, a final LONGFORM_SPECIAL substantially below the TS-002 scale would be suspicious unless Architecture Review provides a strong reason.

Planning envelope:

- `80–120 pages` as a plausible normal range;
- larger is acceptable if Evidence density and non-duplication justify it;
- do not use a page cap to compress detection, document AI, video, spatial reasoning, VLA and world models into token paragraphs.

The production goal is **semantic coverage and technical lineage**, not page-count symmetry with TS-001/002.

---

## 13. Light pre-research conclusions

The limited primary/first-party read-back already supports several planning hypotheses:

1. **The important transition is not simply CNN -> Transformer.** AlexNet/ResNet establish scalable learned visual representations; DETR changes the structure of detection; ViT changes the visual backbone/token formulation; these are separate transitions.
2. **Language alignment is a distinct historical break.** CLIP explicitly replaces a fixed-category supervision framing with image-text supervision and natural-language-addressable concepts.
3. **Modern VLMs have at least two architectural phases worth distinguishing:** bridge/frozen-component designs such as BLIP-2 and instruction-tuned vision-encoder+LLM designs such as LLaVA, versus deeper/native multimodal systems to be mapped in reconnaissance.
4. **Promptable foundation perception deserves its own treatment.** SAM and DINOv2 show different ways “foundation model” entered vision before/alongside general VLMs: promptable dense segmentation and all-purpose self-supervised visual features.
5. **Action introduces a new contract.** RT-2 turns actions into model outputs within a VLA formulation; OSWorld shows that GUI action depends on grounding/operational knowledge, not merely descriptive vision-language competence.
6. **World-model scope must be action/dynamics-aware.** Genie/Genie 2 provide a concrete action-controllable predictive case; this helps prevent TS-003 from equating photorealistic video generation with world modeling.
7. **TS-001 integration is structural, not optional.** Visual token counts, long-video context, repeated screenshot loops and on-device VLA introduce compute/memory/latency questions that should reuse TS-001's measurement discipline.
8. **TS-002 integration is also structural.** Shared visual tokenizers, video models and generative objectives can appear in both Specials, but TS-003 must ask whether they provide state/grounding/prediction/action rather than retelling generation quality history.

---

## 14. Next action

The next step should be **Worker reconnaissance Round B**, not production Discovery.

A separate prompt should instruct Muse to return a structured reconnaissance package for D01–D15, with candidate primary sources, missing lanes, source-access risks, overlap with TS-001/002, capstone candidates, and recommended scope corrections.

Sol should then perform Round C before any production issue/branch/source root is initialized.
