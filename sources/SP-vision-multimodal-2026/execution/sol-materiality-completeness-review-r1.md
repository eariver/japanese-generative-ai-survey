# TS-003 Vision & Multimodal AI — Sol Materiality / Completeness Review r1

Status: `SOL_MATERIALITY_COMPLETENESS_REVIEW_R1 / PASS / AUTHORIZE_SELECTION_THROUGH_ARCHITECTURE`

Date: `2026-10-01 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-vision-multimodal-2026`

Reviewed branch: `special/vision-multimodal-2026-work`

Reviewed HEAD: `dd15645683eeccd26f42dbe4e58d028a8cd415c0`

Reviewed tree: `fa74c88b86b3c4bade6e0eae400049fed5057b85`

Reviewed main: `d6381568cc897a47d6de992189e20339350342b7`

Reviewed main tree: `83ce3a216d852a1c32d0138f9c56fadefa800666`

Reviewed Production Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Reviewed Core tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Decision: **PASS**.

The Materiality Ledger and Profile Completeness are sufficiently faithful to the accepted TS-003 research scope and the r5 Evidence authority to authorize Selection and Architecture. The next Human boundary remains a fresh Architecture Review. No Draft or later stage is authorized by this review.

---

## 1. Canonical state and stage integrity

The canonical Production State is correctly advanced to:

`EVIDENCE_REVIEWED`

with:

- discovery = passed
- screening = passed
- evidence = passed
- materiality = passed
- completeness = passed
- selection = pending
- architecture = pending
- Human Architecture Review = pending
- Publication Preview = pending

The combined stage validation is bound to the exact r5 Evidence and Edition Views authorities approved in Sol Evidence Review r5. Earlier r1-r4 Evidence/Views remain history only.

The canonical checkpoint binds:

- r5 Evidence acceptance `4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34`
- r5 Edition Views `e3d0b3b33588b235e1c9be41259fb5bb5e07cbd1105ac0ff31a7bf7b34bfd0c5`
- Materiality Ledger SHA-256 `c9fc9750fe20cc1d2a1bd0daa58207d0eb8ead47301a7f8b8cf2676904fcf15b`
- Profile Completeness SHA-256 `db2111f02c87a8238d0a41d6dceca8cc7ec8911f0cadf43b1c3914d9fd05aa55`

No Selection or Architecture state was entered during the reviewed execution.

---

## 2. Materiality decision

Canonical ledger:

- rows: 111
- MATERIAL: 101
- CONTEXT: 10
- EXCLUDED / DUPLICATE: 0

The high MATERIAL ratio is acceptable in this edition because the 111 records are already a post-Screening, Evidence-deepened, scope-constrained corpus rather than an unfiltered Discovery pool. Materiality here therefore identifies load-bearing/supporting source authority for the edition, not final page-level inclusion.

The ten CONTEXT records are semantically appropriate short-treatment nodes:

- VM-D001 Neocognitron
- VM-D002 LeNet
- VM-D008 SSD
- VM-D009 RetinaNet
- VM-D014 U-Net
- VM-D016 Panoptic
- VM-D040 ALIGN
- VM-D054 OpenSeg
- VM-D057 Frozen
- VM-D061 MiniGPT-4

They preserve historical continuity without forcing equal-depth treatment.

### 2.1 D04 spatial / geometry cap

PASS.

Exactly the four allowed support-substrate nodes remain MATERIAL:

- MiDaS
- OpenPose
- Visual Genome
- DUSt3R

No NeRF / 3DGS / SLAM / MVS / general 3D-CV expansion was introduced. This preserves D04 as a support substrate for later spatial reasoning/action rather than a standalone 3D-vision survey.

### 2.2 D07A image-language alignment vs D07B grounding

PASS.

The Materiality/Completeness surfaces keep image-level semantic alignment distinct from localization / grounding contracts. CLIP-style addressability is not used as a substitute for region/box/mask grounding history.

### 2.3 Document intelligence

PASS.

O05 retains enough authority for layout-aware, OCR-free, specialist, generalist and retrieval/UI bridges while preserving the prohibition on unsupported cross-model numeric ranking. The absence of a same-protocol specialist-vs-generalist benchmark remains G03 rather than being silently converted into a positive comparison.

### 2.4 Current multimodal systems and source-role duplication

PASS with downstream discipline required.

Multiple authorities for one system remain role-distinct rather than being counted as separate technical transitions. Paper / repository / model-card / vendor page / independent evaluation may all be selected when they support different claims, but Architecture must not present them as independent lineage nodes.

### 2.5 D12-D14 endpoint weight

PASS.

Computer Use + VLA + World Model material records account for 19 of 101 MATERIAL records, about 19%. This is substantial enough for a modern convergence endpoint but not large enough to displace the perception / grounding / multimodal-state history that forms the edition's main body.

---

## 3. Profile Completeness decision

Overall status: `LIMITED`.

This is accepted as publication-quality research closure for the Architecture stage, not as a claim that all external uncertainty is resolved.

- SATISFIED: 13 obligations
- LIMITATION: 3 obligations
- NEEDS_RESEARCH: 0 obligations

Accepted LIMITATION obligations:

### VM-O06 — ViT / self-supervised foundation

The representation lineage is sufficiently established for Architecture. G06 remains: exact SigLIP2 primary citation binding is unresolved. This limits citation-level precision for that successor, not the core ViT / MAE / DINO / DINOv2 / encoder-reuse history.

### VM-O14 — VLA / embodied systems

The representation/action-interface lineage is sufficiently established. G01 remains: independent/non-vendor VLA evaluation is sparse. Architecture must therefore distinguish system/interface history from claims about independently reproduced policy quality.

### VM-O15 — predictive / world models

The four-pole terminology split is sufficiently established: historical formulation, latent dynamics, predictive representation, and interactive generative world model. G02 remains: no transferable control-oriented benchmark closes the question of dynamics usability across these families.

---

## 4. Residual gaps that remain binding

All of G01-G06 remain downstream constraints:

- G01 independent/non-vendor VLA evaluation scarcity
- G02 transferable control-oriented world-model benchmark absent
- G03 same-protocol document specialist vs generalist comparison absent
- G04 real-deployment latency / VRAM beyond author-reported values
- G05 independent reproduction of current vendor/model-report scores
- G06 SigLIP2 exact citation binding

G03-G05 do not force NEEDS_RESEARCH before Architecture because the edition can remain semantically honest by bounding the associated claims. They must not disappear during Selection, Architecture, Draft, or later reader-facing synthesis.

X01-X04 also remain required cross-cutting dimensions:

- X01 data / supervision / post-training
- X02 objective / interface contract
- X03 efficiency / token / memory / latency economics
- X04 reliability / source fidelity / claim strength

---

## 5. Selection requirements

Selection may now determine PRIMARY / SUPPORTING / HOLD / other schema-valid roles from the canonical Materiality and Completeness surfaces.

Do not optimize for a target count.

Selection must preserve enough authority to support the following technical arcs without collapsing them into a model chronology:

1. learned visual representation and transfer;
2. detection / localization;
3. dense perception;
4. bounded geometry / spatial substrate;
5. OCR -> document intelligence;
6. Transformer / self-supervised visual foundations;
7. image-language alignment;
8. open-vocabulary perception and grounding;
9. pretrained vision-language bridges;
10. native multimodal fusion and context economics;
11. multimodal reasoning and failure decomposition;
12. video / temporal memory / streaming;
13. Computer Use as actionable grounding;
14. VLA / embodied action interfaces;
15. predictive / world-model families;
16. evaluation / robustness / convergence.

Selection must preserve alternative lineages and negative-space evidence where those are necessary to avoid a retrospective single-ladder story.

No source may be promoted simply because it is famous, current, or vendor-promoted.

---

## 6. Architecture requirements

Architecture must remain problem- and mechanism-led, not a simple chronology such as:

`CNN -> YOLO -> ViT -> CLIP -> VLM -> VLA -> World Model`

The preferred conceptual coordinate system remains:

`Representation -> Recognition -> Localization / Structure -> Language Alignment -> Grounding -> Multimodal Fusion -> Temporal / Spatial State -> Reasoning -> Action and/or Prediction`

These are interacting problem layers, not eras.

The central question remains:

> AIは、画像や映像を単に分類する段階から、対象の位置・構造・時間関係を認識し、言語概念へ接地し、複数modalを統合して推論し、予測や行動へ利用できる内部表現を形成する段階へ、どのように発展してきたのか。

The cross-cutting question remains:

> What representation of the world is sufficient for the next computation?

### 6.1 TS-001 integration

Reuse TS-001 only where multimodality changes the efficiency problem: visual-token growth, dynamic/high resolution, multi-image and long-video context, resampling/compression, KV/memory pressure, streaming, edge/on-device VLM/VLA, and perception-action latency.

Do not retell generic quantization, MoE, serving or speculative decoding history.

### 6.2 TS-002 integration

Reuse TS-002 only where generation is load-bearing to understanding, prediction or action. Do not retell generic image/audio/video generation history.

World-model treatment must keep video generation, latent dynamics, predictive representation, simulator-like interactive generation and action-conditioned planning models distinct.

### 6.3 Depth / page budget

Do not force symmetry with TS-001/TS-002 or an arbitrary page cap. If the evidence density requires roughly 80-120 pages or somewhat more, preserve semantic depth rather than compressing entire lineages into token paragraphs.

Current endpoints must not consume disproportionate space merely because they are recent.

---

## 7. Human Architecture Review dossier

The next execution may build Selection and Architecture through the canonical Core and then stop at:

`ARCHITECTURE_ESTABLISHED / AWAITING_HUMAN_ARCHITECTURE_REVIEW`

The Human-facing review surface should make it possible to review at least:

- proposed title / subtitle if changed;
- part/package ordering;
- package-level purpose and mechanism thesis;
- source/obligation coverage by package;
- page-budget distribution;
- D04 cap preservation;
- D07A/D07B separation;
- D12-D14 endpoint weighting;
- TS-001/TS-002 cross-reference plan;
- X01-X04 synthesis placement;
- G01-G06 limitations and where they constrain wording;
- current-capstone placement and source-role boundaries;
- explicit anti-chronology / alternative-lineage handling.

The Worker may prepare the dossier, but may not infer or record a Human approval/rejection decision.

---

## 8. Authorization

Authorize:

`EVIDENCE_REVIEWED`
-> Selection
-> `SELECTION_COMPLETE`
-> Architecture
-> `ARCHITECTURE_ESTABLISHED`
-> fresh Human Architecture Review dossier
-> **STOP**

Do not enter Draft.
Do not generate a Human Architecture Review decision.
Do not perform Publication Preview / Freeze / Release.
Do not modify main or `production/survey-core-v2`.

If canonical Selection or Architecture validation fails, or if the architecture cannot preserve the accepted scope/boundaries without new research, fail closed and stop for Sol review rather than forcing stage advancement.
