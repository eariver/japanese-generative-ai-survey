# TS-003 Vision & Multimodal AI — Sol Round E scope closure

Status: `SOL_ROUND_E_SCOPE_CLOSURE / PRE_PRODUCTION / DISCOVERY_AUTHORITY_READY`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `planning/ts-003-vision-multimodal-preresearch-20260930`

Reviewed Round D authority: `420064a2a553112d9ce37d5ba272e2736a5f9be5`

This document closes the iterative Sol↔Worker pre-research cycle for TS-003. It integrates the Sol skeleton, Sol scope audit, Muse Round B reconnaissance, Sol Round C review, Muse Round D targeted follow-up, TS-001/TS-002 final publications, and light current-source verification.

It is not canonical Discovery, Evidence, Selection, Architecture, or Human approval. It is the **pre-production scope authority** that production initialization and canonical Discovery must materialize faithfully.

---

## 1. Round E verdict

`PRE_DISCOVERY_SCOPE_CLOSED`

The current scope is sufficiently complete and bounded to begin production initialization and canonical Discovery.

No further pre-production reconnaissance round is required before initialization.

Round D did not overturn Round C. It resolved all ten targeted residuals to a planning-sufficient state. Remaining uncertainties are normal Discovery/Evidence obligations: exact source rebinding, current-version checks, full-text consumption, independent-reproduction scarcity, and benchmark-condition binding.

The central three-Special relationship is retained:

```text
TS-001: compute the intelligence
TS-002: generate the world
TS-003: perceive, ground, reason about, predict, and act in the world
```

TS-003 is therefore a **convergence volume** joining classical/perceptual vision, language grounding, multimodal representation, reasoning, digital/physical action, and predictive world representation without becoming a generic CV, robotics, or world-model encyclopedia.

---

## 2. Final provisional Core Question

Production Discovery must preserve the following Core Question unless new Evidence forces a later Architecture Review revision:

> **AIは、画像・映像を中心とする現実世界の信号を単に分類する段階から、対象・領域・構造・時間・空間状態を表現し、それらを言語や座標へ接地し、複数modalを統合して推論し、予測や行動へ変換できる段階へ、どのように発展してきたのか。各段階で「次の計算に十分な世界表現」は何であり、何が失われ、何が新たに操作可能になったのか。**

Mandatory cross-cutting test:

> **What representation of the world is sufficient for the next computation?**

This is the primary anti-catalogue rule. Every historical/current node should be interpreted through the contract it changes, not merely its publication date or benchmark position.

---

## 3. Final mandatory coverage taxonomy

The D-lanes below are **research coverage obligations**, not one-lane-per-chapter publication requirements.

### D01 — Learned visual representation / CNN / ImageNet

Status: `MANDATORY / CONTEXT_CAPPED`

Purpose:
- handcrafted/task-specific features -> learned reusable visual representation;
- large-scale supervised learning + GPU scaling;
- transfer to later perception tasks.

Minimum anchors: concise Neocognitron/LeNet context; AlexNet; ResNet.

Do not expand into a full pre-deep-learning CV history.

### D02 — Detection / structured localization

Status: `MANDATORY`

Purpose:
- image-level classification -> object identity + location;
- region/two-stage -> one-stage operating points;
- anchor/NMS-heavy machinery -> set prediction / DETR lineage;
- bridge toward language-grounded detection.

Required terminology discipline: always disambiguate DINO detector from DINO self-supervised representation.

### D03 — Dense perception / segmentation / promptable vision

Status: `MANDATORY`

Purpose:
- boxes -> dense region/pixel structure;
- semantic / instance / panoptic distinction;
- promptable segmentation/foundation perception;
- SAM/SAM2-class transition.

U-Net may appear only in its segmentation role; do not retell the TS-002 diffusion-backbone story.

### D04 — Spatial / geometry substrate

Status: `MANDATORY_SUPPORT / HARD_CAP`

This is not a full publication lane.

Round E accepts the four-node planning allow-list:
1. MiDaS — dense relative/monocular depth;
2. OpenPose — keypoint/object-centric spatial state and association;
3. Visual Genome — relational scene structure + region-language linkage;
4. DUSt3R — learned geometric pointmap state without a calibration-first pipeline assumption.

Purpose:
- establish what geometry/spatial state is absent from category labels;
- show what 2D/2.5D/3D state later reasoning/action assumes;
- provide ancestry for spatial reasoning, GUI grounding, VLA and world interaction.

Default exclusions: full SLAM/SfM history, NeRF history, 3D Gaussian Splatting history, full MVS/3D reconstruction survey, robot kinematics/dynamics.

Discovery may replace one allow-list node only if a demonstrably better primary-source node serves the same contract without expanding scope.

### D05 — OCR -> Document Intelligence / visual knowledge work

Status: `MANDATORY / NORMAL_WEIGHT`

Purpose:
- glyph recognition -> layout/structure/symbolic understanding;
- document, table, chart, equation, PDF, screenshot understanding;
- specialist pipeline/model vs general VLM interface;
- test whether "native multimodal" removes OCR/layout bottlenecks or internalizes them.

Round E adopts `NO_CROSS_MODEL_NUMERIC_COMPARISON` by default for specialist-vs-generalist comparisons unless Discovery finds identical datasets, resolution policy, output contract and metrics.

Safe comparison axes:
- output contract;
- resolution/token policy;
- OCR dependence;
- interactivity/region prompting;
- failure-mode profile.

Multimodal retrieval/RAG may remain a bounded D05 sub-lane when it changes the document interface; it is not a new top-level lane.

### D06 — ViT / self-supervised visual foundation representation

Status: `MANDATORY`

Purpose:
- convolutional inductive bias -> image patch/token formulation;
- scale and pretraining recipe;
- label-free reusable visual representation;
- ViT / MAE / DINO / DINOv2-class transitions;
- encoder reuse into later VLMs.

TS-001 owns generic attention efficiency; TS-003 owns the visual representation/tokenization contract.

### D07A — Image-level vision-language alignment

Status: `MANDATORY / FULL_WEIGHT`

Purpose:
- fixed class ontology -> natural-language-addressable visual semantics;
- visual-semantic embedding / captioning / VQA predecessor context;
- CLIP/ALIGN/SigLIP-class alignment and zero-shot transfer.

Evaluation identity:
- image-level zero-shot classification;
- image-text retrieval / Recall@K;
- alignment measures.

Do not merge these metrics with D07B localization metrics.

### D07B — Open-vocabulary perception and grounding

Status: `MANDATORY / FULL_WEIGHT`

Purpose:
- arbitrary language concept -> box/mask/region/coordinate/evidence;
- phrase grounding / referring expression / OVD / grounded detection / OVS;
- bridge from semantic addressability to actionable grounding.

Round E accepts the following **minimum transition set**, while not requiring equal publication depth for every item:
- Flickr30k Entities / phrase-localization task;
- RefCOCO-family REC contract;
- OVR-CNN / OVD formulation;
- ViLD / CLIP-to-detector distillation;
- RegionCLIP and/or Detic as region/vocabulary scaling poles;
- GLIP / detection-as-grounding reformulation;
- MDETR / text-modulated multi-task detector;
- OWL-ViT / minimal-head late-fusion pole;
- Grounding DINO / tight-fusion unification;
- OWL-ST/OWLv2 / web-scale self-training;
- LSeg -> X-Decoder-class open-vocabulary segmentation path.

OpenSeg and ODISE may appear as bounded variants/crossovers; they are not mandatory equal-depth nodes.

Evaluation identity:
- LVIS-rare/open-vocabulary AP;
- ODinW where appropriate;
- RefCOCO-family grounding accuracy;
- phrase-localization Recall@K.

No shared ranking table with D07A.

### D08 — Bridging pretrained vision and language systems

Status: `MANDATORY / FULL_WEIGHT`

Purpose:
- separately pretrained vision + LLM systems -> usable VLM;
- projector / resampler / Q-Former / cross-attention;
- frozen/mostly-frozen components vs deeper joint training;
- visual instruction tuning;
- compute-efficient bridge strategy vs deeper multimodal integration.

Historical anchors should include Flamingo/BLIP-2/LLaVA-class systems as source coverage permits.

### D09 — Native/omni multimodal fusion, tokenization and context economics

Status: `MANDATORY / FULL_WEIGHT`

Purpose:
- how image/video/audio become model-consumable state/token sequences;
- fixed vs dynamic resolution, tiling, resampling, token compression/pruning;
- early/late fusion, cross-attention vs unified sequence;
- multi-image, long-video and audio/video time alignment;
- context/KV/memory/latency implications.

TS-001 integration is mandatory through shared measurement vocabulary, but generic quantization/MoE/serving history must not be retold.

Bounded audio-input scope:
- speech/audio understanding: IN;
- audiovisual fusion: IN;
- language-addressable audio: IN;
- absolute-time / synchronization / streaming input: IN;
- TTS / voice cloning / music/audio generation history: OUT, TS-002-owned.

Minimum input-side chain accepted for Discovery obligations:
Whisper -> BEATs -> CLAP -> current omni-fusion system (e.g. Qwen3-Omni-class) -> streaming multimodal evaluation.

### D10 — Multimodal reasoning / perceptual failure decomposition

Status: `MANDATORY / FULL_WEIGHT`

Purpose:
- separate visual evidence use from language priors and reasoning scaffolds;
- recognition, OCR, counting, spatial, geometry, chart/table/diagram, scientific visual reasoning, multi-image, compositional reasoning, hallucination, localization/evidence-use;
- distinguish perceptual improvement from better reasoning elicitation/tool use.

No single composite multimodal benchmark is accepted as general visual intelligence.

### D11 — Video understanding / temporal state / long-horizon memory

Status: `MANDATORY / NORMAL_WEIGHT`

Purpose:
- repeated per-frame recognition -> genuine temporal state;
- action recognition, event localization, temporal ordering, causal/physical reasoning;
- long-video retrieval/memory;
- online/streaming video understanding;
- audiovisual understanding where audio is load-bearing.

Round E accepts Flash-VStream as a planning streaming-system anchor and StreamingBench as a planning streaming-evaluation anchor. Canonical Discovery must re-bind both.

Offline long-context and online streaming are different contracts and must not share an undifferentiated metric table.

### D12 — Computer Use / actionable digital grounding

Status: `MANDATORY_ENDPOINT / BOUNDED`

Purpose:
- screenshot/document perception -> element grounding -> coordinate/tool action -> persistent task state;
- compare pure-vision, accessibility-tree/DOM, API/tool and mixed interfaces as action contracts;
- emphasize long-horizon state and verification, not merely clicking accuracy.

OSWorld 1.0 / 2.0 are planning evaluation anchors; current vendor computer-use systems may appear as deployment/capability cases only where exact authority exists.

Do not expand into a generic agent architecture survey.

### D13 — Vision-Language-Action / embodied multimodal systems

Status: `MANDATORY_ENDPOINT / HARD_CAP`

Purpose:
- vision/language representations -> executable physical action interface;
- planner-side grounding vs embodied joint representation vs action tokenization vs open VLA implementation vs current deployment.

Round E accepts the minimum predecessor chain:
- SayCan — language planning × affordance values, explicitly not a joint representation;
- RT-1 — scaled real-robot trajectory/data regime;
- PaLM-E — embodied multimodal representation;
- Open X-Embodiment — multi-robot/cross-embodiment data contract;
- RT-2 — action tokens + VL co-fine-tuning / VLA formulation;
- OpenVLA — inspectable/open architecture pole;
- current Gemini Robotics-class capability/deployment endpoint where source role supports it.

Explicit exclusions: kinematics, dynamics, gait, actuator/hardware survey, locomotion theory, general robotics safety/policy.

Independent VLA evaluation scarcity must be preserved as an evidence limitation rather than repaired by vendor claims.

### D14 — Predictive representations / World Models

Status: `MANDATORY_ENDPOINT / HARD_CAP / TERMINOLOGY_SPLIT`

Do not use `world model` as one category.

Minimum four-pole comparison contract:
1. historical/latent world-state formulation;
2. latent dynamics / model-based decision-making (Dreamer-family);
3. predictive representation without photorealistic generation (V-JEPA/JEPA-class);
4. generative interactive environment / action-conditioned simulation (Genie-class).

Every D14 candidate must explicitly bind:
- represented state;
- predicted target;
- action conditioning;
- pixel vs latent vs reward/action target;
- planning/training/evaluation use.

Cases that can only establish photorealistic media generation belong primarily to TS-002, not D14.

Genie 3-class first-party pages are capability/deployment authority only unless an architecture source exists.

### D15 — Evaluation / robustness / provenance / convergence

Status: `MANDATORY / METHODOLOGY_FIRST`

Purpose:
- preserve task identity;
- compare evaluation contracts, not bare scores;
- bind dataset/version, input policy, tool allowance, thinking/scaffold budget, judge, answer extraction, contamination risk, and model version;
- separate provider measurement from independent reproduction;
- synthesize limits of cross-task comparability and convergence claims.

Round E retain-set for targeted evaluation coverage:
- DocVQA;
- ChartQA;
- OCRBench v2 (not v1);
- POPE + HallusionBench as complementary hallucination/failure-attribution instruments;
- ScreenSpot-class GUI grounding;
- OSWorld 1.0 + 2.0;
- Video-MME;
- LongVideoBench;
- StreamingBench;
- VSI-Bench-class spatial reasoning.

This is not a requirement to print all benchmark results; it is a minimum Discovery/evaluation map.

---

## 4. Cross-cutting axes

### X01 — Data / supervision / instruction tuning / post-training

Status: `MANDATORY_CROSS_CUTTING`

Do not create a standalone dataset-history chapter by default.

Every major D-lane must capture:
- input data type;
- supervision/target type;
- scale/source where authoritative;
- synthetic/pseudo-labelled/preference/action-trajectory data where material;
- what transfer/generalization the supervision enables;
- known data/authority limitations.

Part V may synthesize the progression:
hand-labelled tasks -> large supervised datasets -> self-supervision -> image-text pairs -> interleaved multimodal data -> instruction tuning -> synthetic/preference/post-training -> action trajectories.

### X02 — Objective / interface contract

Status: `MANDATORY_CROSS_CUTTING`

For each transition record what enters and what leaves the system:
class label / box / mask / text / region / coordinate / action / latent next-state / rendered frame / etc.

This is the main semantic guard against conflating systems that all appear to "understand vision".

### X03 — Efficiency / token / memory / latency economics

Status: `MANDATORY_CROSS_CUTTING`

Reuse TS-001 terminology and measurement discipline.

TS-003-specific fields include:
- image/video/audio tokenization;
- dynamic resolution;
- frame sampling;
- repeated perception loops;
- long-video memory;
- GUI screenshot-loop cost;
- edge/on-device perception-action latency.

### X04 — Reliability / source fidelity / claim strength

Status: `MANDATORY_CROSS_CUTTING`

Apply CV2-DM-020 throughout.

Every current system must be role-tagged separately:
- `ARCHITECTURE_CASE`
- `CAPABILITY_CASE`
- `DEPLOYMENT_CASE`
- `EVALUATION_CASE`

A source supporting one role does not automatically support another.

Vendor/product/demo pages must never become architecture authority without explicit technical material.

---

## 5. Final TS-001 / TS-002 boundary contract

### TS-001 ownership

TS-001 owns generic:
- attention/memory efficiency;
- MoE;
- quantization;
- decoding acceleration;
- serving/scheduling;
- generic local inference and cost/throughput theory.

TS-003 may reuse that language only where multimodality changes the bottleneck: visual token explosion, high-resolution input, multi-image/video context, resampling, streaming, repeated observation loops, on-device VLA latency.

### TS-002 ownership

TS-002 owns generic:
- image/audio/music/video generation lineage;
- generative objectives and samplers;
- control/editing and media consistency;
- speech/music/video synthesis.

TS-003 may revisit shared models/components only when the question becomes perception, representation, alignment, grounding, temporal state, prediction or action.

Critical examples:
- CLIP: TS-002 conditioning vs TS-003 language-addressable visual semantics;
- video: TS-002 generation/consistency vs TS-003 observation/temporal reasoning;
- audio: TS-002 synthesis vs TS-003 input/fusion/reasoning;
- World Models: TS-002 generated media vs TS-003 action-conditioned predictive state.

Cross-reference rather than re-teach prior Special content whenever possible.

---

## 6. Negative space / refusal list

Default OUT unless Discovery establishes a load-bearing generic mechanism point:
- full handcrafted/pre-deep-learning CV history;
- full SLAM/SfM/NeRF/3DGS/3D reconstruction history;
- full speech recognition history;
- TTS/voice cloning/music/audio generation history;
- generic robotics/control/kinematics/locomotion;
- medical vision / autonomous-driving / remote-sensing vertical surveys;
- AI policy/safety as standalone subject;
- generic multimodal RAG survey;
- generic agent architecture survey;
- every current VLM leaderboard.

A low-yield area must be recorded explicitly as `LOW_YIELD`, `OUT_OF_SCOPE`, `EVIDENCE_GAP`, or `CONTEXT_ONLY`; it must not silently vanish.

---

## 7. Current-system / capstone policy

No final capstone set is frozen pre-Discovery.

Production Discovery must seek source-rich candidates for at least these roles:
1. inspectable open VLM architecture;
2. second technically distinct open/inspectable VLM family;
3. native/omni multimodal architecture;
4. document/UI understanding case;
5. long-video/streaming case;
6. computer-use evaluation/deployment case;
7. VLA case;
8. predictive/world-model cases from at least two different poles.

Planning candidates currently include Qwen3-VL/Qwen3-Omni, InternVL3, Molmo 2, OSWorld 2.0, OpenVLA/Gemini Robotics-class endpoints, Dreamer/V-JEPA and Genie-class systems.

These are **candidate identities, not publication commitments**.

Discovery must re-check model/version currency and exact primary-source authority.

Current system selection criteria:
- technical distinctiveness;
- source richness;
- architecture transparency when used as architecture case;
- independent evaluation availability;
- documented limitations;
- non-redundancy with TS-001/002;
- current relevance.

Newest/famous/highest-score alone is never sufficient.

---

## 8. Provisional reader architecture

Research taxonomy must not become 16+ reader chapters.

Use the following five-Part structure as the default Architecture Review starting point:

### Part I — From visual signals to reusable structure

Coverage: D01-D06, with D04 support-capped.

Question:
> What visual representation did the next task require?

### Part II — Making vision language-addressable and grounded

Coverage: D07A + D07B + D08.

Question:
> How did category labels become language-addressable semantics, regions, coordinates and VLM interfaces?

### Part III — Multimodal state and reasoning

Coverage: D09-D11, with D04/D05 cross-links.

Question:
> How are heterogeneous signals fused, synchronized, retained and used as evidence for reasoning?

### Part IV — From understanding to action and prediction

Coverage: D12-D14.

Question:
> When does multimodal understanding become an actionable task state, physical policy or predictive world state?

This Part must remain bounded; it is not the majority of the book.

### Part V — Measurement, limits, and convergence

Coverage: D15 + X01-X04 synthesis.

Question:
> What do current systems actually establish, under which measurement and source conditions, and where does unification remain unresolved?

This Part structure is provisional until Human Architecture Review.

---

## 9. Weight / depth contract

Planning weight, not page quota:
- Parts I-III: `65–72%`;
- Part IV / D12-D14 combined: `13–18%`;
- Part V / evaluation+synthesis: `15–20%`.

No D12/D13/D14 topic earns large depth merely because it is current or dramatic.

D04 remains a support substrate.

Planning page envelope remains `80–120 pages`, with the upper half acceptable if primary-source/evidence density supports it.

Do not compress load-bearing lineages to meet a page cap.

---

## 10. Title disposition

Current backlog title:

`Vision & Multimodal AI — 検知・認識からVLM・World Modelへ`

Round E does **not** freeze this subtitle.

The phrase `VLM・World Modelへ` is too linear and may bias the narrative toward a predetermined endpoint.

Preferred current working-title direction for Discovery:

> **Vision & Multimodal AI — 視覚表現から接地・推論・行動へ**

Alternative:

> **Vision & Multimodal AI — 世界を読むAIの技術史**

Final title is deferred to Architecture Review, after Evidence density reveals the actual narrative center.

---

## 11. Discovery minimum-completeness contract

Canonical production Discovery is incomplete unless it can account for every mandatory D/X obligation above.

At minimum, Discovery must provide:
- primary/official source candidates for each D lane;
- historical predecessor/successor sufficient to prevent abrupt lineage jumps;
- current source-rich cases for major 2025–2026 transitions;
- TS-001/002 cross-reference mapping;
- per-lane supervision/data contract;
- per-lane input/output/interface contract;
- per-lane evaluation authority and limitations;
- current-case source-role classification;
- negative-space / low-yield accounting;
- access status and version/date provenance;
- unresolved evidence gaps rather than fabricated closure.

Specific obligations from Round D:
- D04 stays within the four-node/support contract unless explicitly justified;
- D07A/D07B remain separate;
- D07B carried source IDs (GLIP/OWL-ViT/Grounding DINO/RefCOCO etc.) must be re-bound exactly;
- second open VLM family must be captured (InternVL3 and/or Molmo 2-class, subject to current verification);
- document specialist/generalist numeric comparison remains prohibited unless same-protocol evidence exists;
- streaming is a D11 sub-lane, not a new top-level lane;
- audio-input chain stays input-side only;
- independent VLA evaluation remains an explicit gap if still thin;
- D14 must retain at least one latent-dynamics and one non-generative predictive counterweight to generative world models;
- evaluation benchmark count should be minimized to distinct contracts, not maximized.

---

## 12. Production initialization recommendation

Round E authorizes proceeding to **production initialization + canonical Discovery only**.

Recommended machine identity (provisional until initialization checks current naming conventions):

`SP-vision-multimodal-2026`

Recommended stable slug:

`vision-multimodal-2026`

Recommended work branch:

`special/vision-multimodal-2026-work`

Temporal mode:

`OPEN_HISTORY_AS_OF`

Eventual target Human gate:

`ARCHITECTURE_REVIEW`

First production execution must stop at:

`DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW`

Do not authorize Screening or later stages in the initial production run.

Production initialization should:
1. use the current generic THEMATIC + LONGFORM_SPECIAL Core v2 path;
2. materialize a canonical research-scope/obligation surface preserving this Round E contract;
3. synchronize backlog status only through the proper initialization path;
4. record exact main/Core authority and source provenance;
5. perform primary-technical-first Discovery;
6. stop for Sol completeness review before Screening.

Shared Core remains frozen unless separately authorized by the Human Owner.

---

## 13. Pre-research rally closure

The iterative pre-production process is complete:

```text
Round A  Sol skeleton
Round B  Muse bounded reconnaissance
Round C  Sol scope re-review
Round D  Muse targeted residual follow-up
Round E  Sol scope closure
```

This process materially improved the initial plan by:
- splitting image-level alignment from region/action grounding;
- strengthening supervision/data as a cross-cutting contract;
- adding bounded omni/audio-input coverage;
- capping geometry/3D and embodied/world-model scope;
- reframing Computer Use around persistent task state;
- establishing a four-pole world-model terminology contract;
- adding a second open-VLM comparison axis;
- resolving streaming as a genuine sub-lane rather than a speculative gap;
- cleaning benchmark and source-role boundaries;
- separating research taxonomy from reader-facing chapter structure.

This is sufficient planning maturity for production Discovery.

Terminal state:

`TS-003 ROUND_E_SCOPE_CLOSURE_COMPLETE`

`PRE_DISCOVERY_SCOPE_CLOSED`

`PRODUCTION_INITIALIZATION_AUTHORIZED`

`FIRST_PRODUCTION_STOP = DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW`
