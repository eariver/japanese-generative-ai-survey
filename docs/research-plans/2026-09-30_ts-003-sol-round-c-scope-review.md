# TS-003 Vision & Multimodal AI — Sol Round C scope review

Status: `SOL_ROUND_C_SCOPE_REVIEW / PRE_DISCOVERY / NOT_PRODUCTION_AUTHORITY`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `planning/ts-003-vision-multimodal-preresearch-20260930`

Reviewed Round B authority: `160989357eb628ac84960ec28bd15fdb1efe4169`

This document is Sol's Round C re-review after Muse Round B. It deliberately re-evaluates **both** the new reconnaissance material and the original Sol organization. It is not a rubber-stamp of Muse's proposal and is not canonical Discovery, Evidence, Architecture, or Human approval.

---

## 1. Inputs re-evaluated together

Round C re-opened all of the following simultaneously:

1. `docs/research-plans/2026-09-30_ts-003-vision-multimodal-sol-preresearch-skeleton.md`
2. `docs/research-plans/2026-09-30_ts-003-sol-scope-audit-before-worker.md`
3. `docs/research-plans/2026-09-30_ts-003-muse-round-b-reconnaissance.md`
4. `docs/research-plans/2026-09-30_ts-003-muse-round-b-source-candidates.md`
5. final reader-facing TS-001 Efficient Intelligence
6. final reader-facing TS-002 Beyond Text
7. current external/primary spot-checks for key 2026 capstones and structural claims

Round B execution discipline is accepted: the branch advanced by one normal commit from the exact guarded starting authority and added only the two requested planning files. No production initialization or Core mutation occurred.

Important evidence boundary: the Muse source-candidate ledger intentionally marks every row `NOT_ACCESSED` in canonical-production terms. Therefore Round C treats the ledger as a **planning/source-resolution map**, not accepted Evidence. Detailed factual claims that matter to final production must still receive source read-back during targeted follow-up and canonical Discovery/Evidence.

---

## 2. Round C overall verdict

`ROUND_B_ACCEPTED_WITH_SOL_RESTRUCTURE`

The original three-Special thesis survives:

```text
TS-001: compute the intelligence
TS-002: generate the world
TS-003: perceive, ground, reason about, predict, and act in the world
```

However, the original D01-D15 list must be understood as a **coverage taxonomy**, not the final publication chapter architecture.

Muse's strongest correction is accepted:

> image-level language alignment and open-vocabulary localization/grounding are different technical contracts and should not share one undifferentiated D07 lane.

Round C also makes two additional Sol corrections that go beyond Muse's proposed K section:

1. D04 geometry/3D/spatial is retained only as a **bounded support substrate**, not as an equal-weight core narrative lane.
2. D12-D14 are retained as **convergence endpoints**, but their combined weight is reduced relative to Muse's proposal so that Computer Use / robotics / world models cannot turn TS-003 into an agent/robotics survey.

No new mandatory top-level research domain is added beyond the D07 split.

---

## 3. Revised Core Question

The Muse revision improves the representation-sufficiency thesis, but the phrase `画像や映像` is too narrow for a Special explicitly named `Vision & Multimodal AI`, because the volume must cover bounded audio-input / audiovisual fusion without becoming an audio-generation history.

Round C adopts the following provisional Core Question:

> **AIは、画像・映像を中心とする現実世界の信号を単に分類する段階から、対象・領域・構造・時間・空間状態を表現し、それらを言語や座標へ接地し、複数modalを統合して推論し、予測や行動へ変換できる段階へ、どのように発展してきたのか。各段階で「次の計算に十分な世界表現」は何であり、何が失われ、何が新たに操作可能になったのか。**

The cross-cutting test remains:

> **What representation of the world is sufficient for the next computation?**

This question is the primary anti-catalogue mechanism for the whole Special.

---

## 4. Coverage taxonomy after Round C

### D01 — Learned visual representation / CNN / ImageNet

Disposition: `KEEP / CONTEXT-CAPPED`

Purpose: establish learned reusable representation, large-scale supervision, transfer, and the precondition for later vision foundation models.

Do not write a complete classical-CV history. Neocognitron/LeNet may appear as concise anti-abrupt-start context; AlexNet/ResNet are sufficient major anchors unless Discovery shows a missing load-bearing node.

### D02 — Detection / structured localization

Disposition: `KEEP`

Purpose: classification is insufficient when object identity must be paired with location. Preserve region/two-stage, one-stage operating point, set prediction/DETR, and the bridge toward language-grounded detection.

DINO detector vs DINO self-supervised naming collision must be explicitly disambiguated.

### D03 — Dense perception / segmentation / promptable vision

Disposition: `KEEP`

Purpose: boxes are insufficient for dense region/pixel structure; SAM-family provides a distinct promptable-foundation transition.

Do not retell U-Net's TS-002 diffusion-backbone history.

### D04 — Spatial/geometry substrate

Disposition: `KEEP_AS_SUPPORT / HARD_CAP`

This is not a normal full-weight D lane for publication planning.

Required only to answer:

- what geometry/spatial state is absent from category labels;
- what 2D/2.5D/3D state modern multimodal reasoning assumes;
- what spatial information is lost or preserved when converted into token/language representations;
- why GUI/VLA/world interaction cannot emerge from image classification alone.

Round D must choose **2-4 representative mechanism nodes maximum**. Default exclusions: full SLAM history, NeRF history, Gaussian Splatting history, robot kinematics, full 3D reconstruction survey.

### D05 — OCR -> Document Intelligence / visual knowledge work

Disposition: `KEEP / NORMAL_WEIGHT`

Purpose: visual recognition becomes structured symbolic/layout understanding. This remains highly relevant because document, chart, table, equation, PDF and screenshot understanding are frontier workloads, not historical side topics.

Multimodal retrieval/RAG may appear as a bounded sub-lane only when it materially changes the document interface.

### D06 — ViT / self-supervised visual foundation representation

Disposition: `KEEP`

Purpose: distinguish Transformerization/token formulation from label-free reusable visual representation. ViT, MAE, DINO/DINOv2 and related nodes must not be collapsed into one generic `Transformer era`.

TS-001 overlap is limited to compute/token economics; TS-003 owns the representation-contract angle.

### D07A — Image-level vision-language alignment

Disposition: `SPLIT_ACCEPTED / KEEP`

Purpose: fixed ontology -> natural-language-addressable image-level semantics.

CLIP is a central anchor, but predecessor context from visual-semantic embedding / captioning / VQA is required so CLIP does not appear ex nihilo.

Evaluation identity: zero-shot classification/retrieval and related image-level alignment measures.

### D07B — Open-vocabulary perception and grounding

Disposition: `SPLIT_ACCEPTED / KEEP / FULL_WEIGHT`

Purpose: natural-language concept -> localized box/mask/coordinate/evidence.

This is distinct from D07A in objective, data, evaluation, and downstream use. It provides the substrate for actionable GUI grounding, region-level evidence attribution, and language-conditioned embodied action.

Grounding DINO / OWL-ViT-class evidence confirms that language-grounded detection is not simply CLIP classification with boxes attached; the detection/grounding contract deserves independent treatment.

### D08 — Bridging pretrained vision and language systems

Disposition: `KEEP / FULL_WEIGHT`

Purpose: projector/resampler/Q-Former/cross-attention and visual instruction tuning as the transition from separately pretrained components into usable VLMs.

Preserve the architectural distinction between bridging/frozen-component systems and more deeply integrated multimodal systems.

### D09 — Native/omni multimodal fusion, tokenization and context economics

Disposition: `KEEP / FULL_WEIGHT`

Purpose: how multimodal signals become model-consumable token/state sequences; how resolution, frames, audio/video time, resampling and fusion affect context/memory/latency.

TS-001 integration is structural here, but generic MoE/quantization/serving history must not be retold.

Bounded audio-input scope is mandatory:

- audio understanding / audiovisual fusion / temporal alignment / streaming input: IN
- TTS/music/audio generation history: TS-002, OUT here

Qwen3-Omni is a valid 2025-2026 planning candidate because a public technical report explicitly covers text/image/audio/video integration and streaming speech; production must still bind exact mechanism claims to the report and keep output-generation detail subordinate to the TS-003 input/fusion question.

### D10 — Multimodal reasoning / perceptual failure decomposition

Disposition: `KEEP / FULL_WEIGHT`

Purpose: separate perception, grounding, language prior, scaffold/tool use and reasoning rather than treating a composite benchmark score as general visual intelligence.

Mandatory decomposition includes OCR, counting, spatial, chart/table/diagram, multi-image, compositional reasoning, hallucination, visual evidence use, and tool-assisted perception where material.

### D11 — Video understanding / temporal state / long-horizon memory

Disposition: `KEEP / NORMAL_WEIGHT`

Purpose: distinguish repeated frame recognition from genuine temporal state, event grounding, ordering, memory/retrieval and audiovisual understanding.

TS-002 owns video generation mechanics; TS-003 owns observed-video state and temporal reasoning.

Streaming remains a targeted evidence gap, not a mandatory separate D lane unless Round D finds a source-rich distinct mechanism.

### D12 — Computer Use / actionable digital grounding

Disposition: `KEEP_AS_ENDPOINT / BOUNDED`

Muse's OSWorld 2.0 reframing is accepted after external spot-check. OSWorld 2.0 explicitly moves evaluation toward 108 long-horizon workflows with hidden/dynamic state and reports that frontier agents fail on constraint/state tracking rather than only basic GUI operation.

Therefore D12 must not be merely `can the model click the right pixel?`.

The TS-003 question is:

> how does multimodal perception become an actionable, persistent task state in a changing digital environment?

Do not expand into a general agent architecture survey. Tool/API/DOM/accessibility-tree interfaces are included only as competing grounding/action contracts.

### D13 — Vision-Language-Action / embodied multimodal systems

Disposition: `KEEP_AS_ENDPOINT / HARD_CAP`

RT-2 is a valid historical anchor: its paper explicitly formulates VLA by co-fine-tuning vision-language and robot trajectory data and expressing actions as tokens.

Gemini Robotics 2 / On-Device 2 are valid current capability/deployment cases; Google first-party material confirms a VLA/on-device framing, but vendor model pages must not be elevated into undocumented architecture authority.

Scope ends at the **representation/action interface**. Explicit exclusions: kinematics, dynamics, gait, actuator hardware, manipulation hardware survey, general robotics safety/policy.

### D14 — Predictive representations / World Models

Disposition: `KEEP_AS_ENDPOINT / HARD_CAP / TERMINOLOGY_SPLIT`

This lane survives, but `world model` must never be one undifferentiated category.

Minimum poles:

1. latent dynamics / model-based decision-making;
2. predictive representation learning without photorealistic generation;
3. generative interactive environment models;
4. action-conditioned simulation for agent training/evaluation/planning.

Genie 3 is a valid current **capability/deployment case**: DeepMind publicly describes a real-time interactive 720p world model with minutes-scale consistency and agent interaction. It is not, by that public page alone, architecture authority.

This lane must always cross-reference TS-002's video-generation history and ask the differentiating question:

> does this representation support state/action/counterfactual prediction, or only convincing media generation?

### D15 — Evaluation / robustness / provenance / convergence

Disposition: `KEEP / METHODOLOGY-FIRST`

Do not make D15 a benchmark catalogue. It should define why task-specific authorities cannot be collapsed into a single multimodal score and should carry version/config/judge/tool/thinking-budget/contamination/source-role discipline.

Per-lane evaluation obligations remain primary; D15 synthesizes their comparability limits and convergence claims.

---

## 5. Cross-cutting axes after Round C

### X01 — Data / supervision / instruction tuning / post-training

Disposition: `KEEP / STRENGTHEN / DO_NOT_PROMOTE_TO_STANDALONE_D`

Muse's recommendation is accepted.

Architecture-only history would be misleading, but a standalone dataset chapter risks becoming a catalogue and repeating every lane. Instead every D lane must include a compact `supervision contract` block:

- input data type;
- target/supervision type;
- scale/source where authoritative;
- synthetic/pseudo-labelled/preference/action-trajectory use;
- what new transfer/generalization the supervision makes possible;
- known dataset/authority limitations.

D15/Tier C may synthesize the transition from hand-labelled tasks to self-supervision, web-scale pairs, interleaved multimodal data, instruction tuning, synthetic/post-training and action trajectories.

### X02 — Objective / interface contract

Disposition: `KEEP`

For each transition identify what the system consumes and emits: class label, box, mask, text, coordinate, action, latent next-state, rendered frame, etc. This is the strongest guard against conflating visually similar systems.

### X03 — Efficiency / token / memory / latency economics

Disposition: `KEEP`

Reuse TS-001 terminology and measurement discipline. Add only multimodal-specific fields: visual/audio/video tokenization, dynamic resolution, frame sampling, repeated perception loops, long-video memory, edge/on-device action latency.

### X04 — Reliability / source fidelity / claim strength

Disposition: `KEEP`

Apply CV2-DM-020. Every current capstone must be role-tagged separately as applicable:

- `ARCHITECTURE_CASE`
- `CAPABILITY_CASE`
- `DEPLOYMENT_CASE`
- `EVALUATION_CASE`

One source may support one role without supporting the others.

---

## 6. Research taxonomy is not publication architecture

Round C explicitly rejects a one-D-per-chapter manuscript plan.

A better provisional reader architecture is:

### Part I — From visual signals to reusable structure

D01-D06, but compressed around the question:

> what visual representation did the next task require?

This part should move from learned representation -> localization -> dense structure -> document/spatial structure -> visual tokens/foundation features without becoming a CV textbook.

### Part II — Making vision language-addressable and grounded

D07A + D07B + D08.

This is a central part of the Special:

> image-level semantics -> region-level grounding -> VLM bridge.

### Part III — Multimodal state and reasoning

D09-D11 plus D05/D04 cross-links where needed.

This part asks:

> how are heterogeneous signals fused, retained over time, and used as evidence for reasoning?

### Part IV — From understanding to action and prediction

D12-D14.

This is a convergence endpoint, not the majority of the book.

### Part V — Measurement, limits, and convergence

D15 + X01-X04 synthesis.

This structure is provisional and remains subject to Discovery/Architecture Review.

---

## 7. Weight correction relative to Muse proposal

Muse proposed roughly:

- Tier A 55-60%
- Tier B D12-D14 20-25%
- Tier C 15-20%

Round C reduces Tier B to avoid topic drift.

Provisional planning weight:

- **Core representation/grounding/reasoning (Parts I-III): 65-72%**
- **Convergence endpoints D12-D14: 13-18% combined**
- **Evaluation/synthesis/cross-cutting: 15-20%**

D12, D13, D14 should each earn depth from evidence; none receives a guaranteed equal chapter size.

D04 support material is counted inside Parts I/III and must not independently consume a major share.

---

## 8. Title review

Current working title:

> `Vision & Multimodal AI — 検知・認識からVLM・World Modelへ`

Round C flags the subtitle as **potentially too linear and too World-Model-weighted**.

Do not rename yet, but Round D / Round E should compare alternatives such as:

- `Vision & Multimodal AI — 認識・接地・推論から行動するAIへ`
- `Vision & Multimodal AI — 世界を読むAIの技術史`
- `Vision & Multimodal AI — 視覚表現から接地・推論・行動へ`

The final title should follow the evidence architecture rather than pre-commit the conclusion that World Models are the inevitable endpoint.

---

## 9. Current-capstone policy after Round C

No fixed capstone list yet.

Validated planning classes:

1. inspectable/open VLM architecture;
2. native/omni multimodal system;
3. document/UI understanding case;
4. long-video/streaming case;
5. computer-use benchmark/deployment case;
6. VLA case;
7. world-model case.

Round C external spot-check confirms that Qwen3-VL and Qwen3-Omni have public technical reports with architecture-relevant material; OSWorld 2.0 has a public benchmark paper; Gemini Robotics 2/On-Device 2 and Genie 3 have current first-party material. These sources justify **candidate status only**, not automatic selection.

A second open VLM family should be sought so the current architecture story does not collapse into a Qwen-only narrative.

---

## 10. Targeted Round D gaps

Round D should be targeted, not another full reconnaissance.

### R1 — D04 exact allow-list

Find and recommend 2-4 representative primary nodes maximum for spatial/geometry substrate. The goal is conceptual ancestry for spatial reasoning/embodied grounding, not field coverage.

### R2 — D07B lineage exactness

Verify exact primary sources/roles for referring expression, phrase grounding, OVR-CNN/ViLD/GLIP/OWL-ViT/Grounding DINO and open-vocabulary segmentation. Identify the minimum non-redundant chain.

### R3 — Second open VLM family

Find one technically distinct, source-rich family independent of Qwen for architecture comparison. Do not select by popularity alone.

### R4 — Document specialist vs generalist

Verify whether a current specialist/generalist comparison can be made without incompatible evaluation conditions. If not, retain the conceptual contrast without a synthetic ranking.

### R5 — Streaming / long-video

Find one source-rich streaming/online video-understanding system or explicitly return `LOW_YIELD_CONFIRMED`. Do not fill the lane with weak secondary material.

### R6 — Audio-input / omni predecessor chain

Resolve a minimal input-side predecessor set (e.g. audio-language alignment / speech encoder / audiovisual representation) sufficient to explain omni fusion without retelling audio generation.

### R7 — VLA predecessor chain

Verify exact roles for RT-1, SayCan, PaLM-E, Open X-Embodiment, RT-2, OpenVLA. Determine the minimum chain required to avoid abrupt RT-2 entry.

### R8 — World-model terminology counterweights

Verify exact primary authority for Dreamer-family and JEPA/V-JEPA-like predictive representation, and define what they contribute that Genie-style interactive generation does not.

### R9 — Evaluation authority cleanup

Resolve exact source/version/role for currently low-confidence benchmark candidates (document/chart, hallucination, GUI grounding, long-video, spatial reasoning). Remove redundant metrics rather than maximize benchmark count.

### R10 — Current capstone source-role binding

For each candidate 2026 system, produce a four-role matrix showing which first-party/primary source can actually support architecture, capability, deployment and evaluation. Any unsupported role remains blank.

---

## 11. Round C disposition of Muse findings

Accepted:

- D07 split into D07A/D07B;
- X01 remains cross-cutting but strengthened;
- vision-centered omni boundary;
- D12 long-horizon state-management reframing;
- D13 hard boundary at representation/action interface;
- D14 non-generative counterweight requirement;
- source-role tagging for closed/current systems;
- 80-120pp as a non-authoritative planning envelope;
- negative-space/refusal lists;
- no one-shot production Discovery.

Modified by Sol:

- D04 demoted to support substrate/hard cap;
- Tier B weight reduced from 20-25% to 13-18%;
- Core Question widened slightly beyond `画像や映像` to bounded real-world multimodal signals;
- final publication structure reduced to five Parts rather than mirroring D01-D15;
- title marked for later re-evaluation because `World Model` in the subtitle may bias the endpoint;
- source ledger remains planning-only because canonical access/evidence was not performed.

Rejected/deferred:

- no additional mandatory top-level D beyond D07 split at this time;
- no standalone data/supervision D lane;
- no full 3D/SLAM/robotics/audio-generation expansion;
- no fixed 2026 capstone selection yet;
- no production initialization yet.

---

## 12. Next state

Round C is complete.

Next recommended step:

```text
TS-003 ROUND_D_TARGETED_FOLLOWUP
  -> only R1-R10 unresolved scope/source questions
  -> Sol Round E scope closure
  -> then production initialization / canonical Discovery
```

Do not initialize TS-003 production before Round E.

Terminal state:

`TS-003 ROUND_C_SCOPE_REVIEW_COMPLETE`
`TARGETED_ROUND_D_REQUIRED`
`NO_PRODUCTION_INITIALIZATION`
