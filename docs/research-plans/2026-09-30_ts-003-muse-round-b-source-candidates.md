# TS-003 Vision & Multimodal AI — Muse Round B source-candidate ledger

Status: `ROUND_B_PLANNING_LEDGER / NOT_CANONICAL_DISCOVERY / NOT_ACCESSED`

Date: `2026-09-30 JST`

Branch: `planning/ts-003-vision-multimodal-preresearch-20260930`

Companion: `docs/research-plans/2026-09-30_ts-003-muse-round-b-reconnaissance.md` (rationale, dispositions,
overlap matrix, evaluation map, capstone roles).

Read this ledger as: **planning material for Sol Round C / Round D follow-up, not canonical Discovery.**
Every entry is `access: NOT_ACCESSED` — no bytes captured, no provenance normalized, no Screening,
no Evidence. URLs are candidate identifiers to resolve at production Source Intake; version/date drift
must be re-checked then (CV2-DM-013). Closed-vendor entries carry role caps per CV2-DM-020
(capability/deployment/evaluation only unless a mechanism paper exists).

Field key per entry: `[lane] Title — year — type — authority — role — confidence — overlap — access`.
`why` = materiality in one line. `notes` = risks/relations.

Source-type vocabulary: `PAPER` (peer-reviewed/proceedings), `PREPRINT` (arXiv technical report),
`OFFICIAL_REPORT` (vendor/lab technical report or model card), `OFFICIAL_PAGE` (vendor product/model
page, capability/deployment facts only), `OFFICIAL_REPO` (code/weights), `BENCHMARK` (benchmark paper +
repo), `SURVEY` (secondary taxonomic witness only — never mechanism authority), `DATASET` (data paper).

Confidence: `HIGH` (canonical ID, stable), `MEDIUM` (ID likely correct, re-verify at intake),
`LOW` (name known, exact bytes/citation unverified — Round D verification task).

---

## D01 — Visual representation / CNN / ImageNet

- [D01] Krizhevsky et al., *ImageNet Classification with Deep CNNs* — 2012 — PAPER — primary —
  role: historical-anchor — confidence: HIGH — overlap: TS-001 absent / TS-002 absent —
  access: NOT_ACCESSED — why: large-scale supervised CNN + GPU scaling landmark —
  URL: https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks —
  notes: NIPS (no arXiv original); cite proceedings version.
- [D01] He et al., *Deep Residual Learning for Image Recognition* — 2015 — PREPRINT/PAPER (CVPR 2016) —
  primary — role: historical-anchor — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: residual optimization break + transfer-to-detection lineage —
  URL: https://arxiv.org/abs/1512.03385 — notes: none.
- [D01] LeCun et al., *Gradient-Based Learning Applied to Document Recognition* — 1998 — PAPER —
  primary — role: predecessor-context — confidence: HIGH — overlap: absent/partial (TS-002 VAE-adjacent only) —
  access: NOT_ACCESSED — why: concise pre-AlexNet CNN context, anti-abrupt-start —
  URL: http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf — notes: context only, ≤1 paragraph equivalent.
- [D01] Fukushima, Neocognitron — 1980 — PAPER — primary — role: predecessor-context —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED — why: named origin context only —
  URL: (resolve at intake; Biol. Cybernetics 36(4)) — notes: name + year suffice; no mechanism depth.

## D02 — Detection / structured localization

- [D02] Girshick et al., *Rich feature hierarchies (R-CNN)* — 2013 — PREPRINT/PAPER (CVPR 2014) —
  primary — role: historical-anchor — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: region-proposal detection origin —
  URL: https://arxiv.org/abs/1311.2524 — notes: none.
- [D02] Ren et al., *Faster R-CNN* — 2015 — PREPRINT/PAPER (NIPS 2015) — primary —
  role: historical-anchor — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: RPN two-stage capstone — URL: https://arxiv.org/abs/1506.01497 — notes: none.
- [D02] Redmon et al., *You Only Look Once (YOLO)* — 2015 — PREPRINT/PAPER (CVPR 2016) — primary —
  role: historical-anchor (lineage representative) — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: one-stage operating-point origin; do not reduce one-stage history to it —
  URL: https://arxiv.org/abs/1506.02640 — notes: YOLO-family later versions are distinct products; bind version.
- [D02] Liu et al., *SSD: Single Shot MultiBox Detector* — 2015 — PREPRINT/PAPER (ECCV 2016) —
  primary — role: lineage-completeness — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: one-stage non-YOLO branch — URL: https://arxiv.org/abs/1512.02325 — notes: short.
- [D02] Lin et al., *Focal Loss / RetinaNet* — 2017 — PREPRINT/PAPER (ICCV 2017) — primary —
  role: lineage-completeness — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: dense-detection imbalance treatment — URL: https://arxiv.org/abs/1708.02002 — notes: short.
- [D02] Carion et al., *DETR* — 2020 — PREPRINT/PAPER (ECCV 2020) — primary —
  role: historical-anchor — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: set-prediction; removes anchors/NMS — URL: https://arxiv.org/abs/2005.12872 — notes: none.
- [D02] Zhang et al., *DINO detector* — 2022 — PREPRINT (ICLR 2023) — primary —
  role: successor-node (missing from Sol map; Grounding DINO base) — confidence: HIGH —
  overlap: absent/absent — access: NOT_ACCESSED — why: DETR-lineage capstone; D07B technical base —
  URL: https://arxiv.org/abs/2203.03605 —
  notes: TERMINOLOGY COLLISION with DINO self-supervised (D06) — always qualify (CV2-DM-006 rule).
- [D02] YOLO-World — 2024 — PREPRINT — primary — role: bridge-case D02→D07B —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: GLIP-formulation open-vocabulary YOLO; ARCHITECTURE_CASE candidate (open) —
  URL: (resolve at intake; verify exact arXiv ID Round D) — notes: do not confuse with YOLO product line.

## D03 — Segmentation / promptable dense perception

- [D03] Long et al., *FCN* — 2014 — PREPRINT/PAPER (CVPR 2015) — primary —
  role: historical-anchor — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: dense-prediction origin — URL: https://arxiv.org/abs/1411.4038 — notes: none.
- [D03] Ronneberger et al., *U-Net* — 2015 — PREPRINT/PAPER (MICCAI 2015) — primary —
  role: context-node (vision role ONLY) — confidence: HIGH — overlap: absent/TS-002-partial —
  access: NOT_ACCESSED — why: segmentation history requires it; TS-002 diffusion-backbone role excluded —
  URL: https://arxiv.org/abs/1505.04597 — notes: one cross-reference sentence to TS-002 role.
- [D03] He et al., *Mask R-CNN* — 2017 — PREPRINT/PAPER (ICCV 2017) — primary —
  role: historical-anchor — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: instance-segmentation bridge — URL: https://arxiv.org/abs/1703.06870 — notes: none.
- [D03] Kirillov et al., *Panoptic Segmentation* — 2018 — PREPRINT/PAPER (CVPR 2019) — primary —
  role: contract-node (definition + citation) — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: semantic-vs-instance unification contract — URL: https://arxiv.org/abs/1801.00868 —
  notes: definition-level depth only.
- [D03] Kirillov et al., *Segment Anything (SAM)* — 2023 — PREPRINT/PAPER (ICCV 2023) — primary —
  role: historical-anchor (promptable task/model/SA-1B system) — confidence: HIGH —
  overlap: absent/absent — access: NOT_ACCESSED — why: first vision-foundation-model event; zero-shot transfer —
  URL: https://arxiv.org/abs/2304.02643 — notes: carry BOTH readings (foundation vs bounded annotation engine).
- [D03→D11] SAM 2 — 2024 — PREPRINT — primary — role: bridge-node (video memory) —
  confidence: HIGH — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: streaming-memory architecture pointer to D11 — URL: https://arxiv.org/abs/2408.00714 —
  notes: architecture pointer, not a streaming-system case.
- [D03] Interactive-segmentation predecessors (DEXTR/RITM-class) — various — PAPER — primary —
  role: predecessor-context — confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: one-line context so SAM promptability is systematization-at-scale, not invention —
  URL: (resolve Round D) — notes: verify exact citation; single sentence max.

## D04 — Geometry / depth / pose / 3D / spatial state (capped support lane)

- [D04] Monocular-depth representative — TBD Round C/D — PAPER/PREPRINT — primary —
  role: support-node — confidence: LOW — overlap: absent/TS-002-partial (control signals) —
  access: NOT_ACCESSED — why: what metric/relative geometry representation exists before tokenization —
  URL: (Sol Round C allow-list decides 2–4 nodes; do not pre-collect) —
  notes: CAP ENFORCED — no NeRF/3DGS/SLAM capture in this lane.
- [D04] Pose/keypoint representative — TBD Round C/D — PAPER/PREPRINT — primary —
  role: support-node — confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: object-centric state ancestry for D10/D13 — URL: (allow-list) —
  notes: same cap.
- [D04] Scene-graph representative (if load-bearing) — TBD — PAPER — primary —
  role: conditional support-node — confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: ONLY if D10 spatial-relation reading requires it — URL: (allow-list) —
  notes: default EXCLUDE unless Sol Round C admits with reason.

## D05 — OCR → Document Intelligence (+ retrieval sub-lane)

- [D05] Li et al., *LayoutLM* — 2019 — PREPRINT — primary — role: historical-anchor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: text+layout+position pre-training origin — URL: https://arxiv.org/abs/1912.13318 — notes: none.
- [D05] Huang et al., *LayoutLMv3* — 2022 — PREPRINT — primary — role: successor-node —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: unified text-layout-image pre-training — URL: https://arxiv.org/abs/2204.08387 — notes: none.
- [D05] Kim et al., *Donut (OCR-free)* — 2021 — PREPRINT/PAPER (ECCV 2022) — primary —
  role: transition-node — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: OCR-free document understanding branch — URL: https://arxiv.org/abs/2111.15664 — notes: none.
- [D05] Lee et al., *Pix2Struct* — 2022 — PREPRINT — primary — role: transition-node —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: screenshot-parsing pre-training; UI-as-document bridge — URL: https://arxiv.org/abs/2210.03347 —
  notes: explicit handoff paragraph to D12, not duplication.
- [D05] Blecher et al., *Nougat* — 2023 — PREPRINT — primary —
  role: specialist-pole candidate (ARCHITECTURE_CASE if verified) — confidence: MEDIUM —
  overlap: absent/absent — access: NOT_ACCESSED — why: academic-document specialist vs generalist test —
  URL: https://arxiv.org/abs/2308.13418 — notes: verify role/currentness Round D.
- [D05-sub] Qwen3-VL-Embedding / Reranker — 2026 — PREPRINT (arXiv:2601.04720) — primary —
  role: retrieval-sub-lane anchor — confidence: MEDIUM (ID from secondary fetch; re-verify) —
  overlap: absent/absent — access: NOT_ACCESSED —
  why: VLM-backbone retrieval (MMEB-V2 77.8 SOTA Jan 2026); document-RAG interface —
  URL: https://arxiv.org/abs/2601.04720 —
  notes: retrieval objective + Matryoshka/quantization-aware traits; cross-ref D09 encoder reuse.

## D06 — ViT / self-supervised visual foundation

- [D06] Dosovitskiy et al., *ViT (16x16 Words)* — 2020 — PREPRINT/PAPER (ICLR 2021) — primary —
  role: historical-anchor — confidence: HIGH — overlap: TS-001-partial/TS-002-partial —
  access: NOT_ACCESSED — why: convolution-to-sequence formulation; precondition of all VL fusion —
  URL: https://arxiv.org/abs/2010.11929 — notes: new angle = token-formulation, not efficiency/backbone.
- [D06] Touvron et al., *DeiT* — 2020 — PREPRINT/PAPER (ICML 2021) — primary —
  role: bridge-node — confidence: HIGH — overlap: partial/partial — access: NOT_ACCESSED —
  why: data-efficiency/recipe reading (architecture-vs-scale debate) — URL: https://arxiv.org/abs/2012.12877 —
  notes: short.
- [D06] Liu et al., *Swin Transformer* — 2021 — PREPRINT/PAPER (ICCV 2021) — primary —
  role: hierarchy-node — confidence: HIGH — overlap: partial/partial — access: NOT_ACCESSED —
  why: hierarchical vision Transformer completeness — URL: https://arxiv.org/abs/2103.14030 — notes: short.
- [D06] He et al., *MAE* — 2021 — PREPRINT/PAPER (CVPR 2022) — primary — role: historical-anchor —
  confidence: HIGH — overlap: partial/partial — access: NOT_ACCESSED —
  why: masked label-free visual pretraining — URL: https://arxiv.org/abs/2111.06377 — notes: none.
- [D06] Caron et al., *DINO (self-supervised)* — 2021 — PREPRINT/PAPER (ICCV 2021) — primary —
  role: historical-anchor — confidence: HIGH — overlap: partial/partial — access: NOT_ACCESSED —
  why: self-distillation; emergent object boundaries (OVD pseudo-label use) —
  URL: https://arxiv.org/abs/2104.14294 —
  notes: ALWAYS qualify vs DINO detector (CV2-DM-006 rule).
- [D06] Oquab et al., *DINOv2* — 2023 — PREPRINT — primary — role: historical-anchor —
  confidence: HIGH — overlap: partial/partial — access: NOT_ACCESSED —
  why: all-purpose visual features at scale; SAM-contrast pole — URL: https://arxiv.org/abs/2304.07193 —
  notes: none.
- [D06→D09] Zhai/Tschannen et al., *SigLIP* — 2023 — PREPRINT/PAPER (ICCV 2023) — primary —
  role: encoder-lineage node — confidence: HIGH — overlap: partial/TS-002-partial —
  access: NOT_ACCESSED — why: sigmoid-loss alignment; SigLIP2-So400m inside Qwen3-VL/Omni (2026 reuse fact) —
  URL: https://arxiv.org/abs/2303.15343 — notes: verify SigLIP2 citation exactness Round D (Tschannen et al. 2025).

## D07A — Image-level vision-language alignment

- [D07A] Frome et al., *DeViSE* — 2013 — PREPRINT (NIPS 2013) — primary — role: predecessor-node —
  confidence: HIGH — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: visual-semantic embedding origin; anti-CLIP-abruptness — URL: https://arxiv.org/abs/1312.5624 —
  notes: short.
- [D07A] Vinyals et al., *Show and Tell* — 2014 — PREPRINT/PAPER (CVPR 2015) — primary —
  role: predecessor-node — confidence: HIGH — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: captioning predecessor — URL: https://arxiv.org/abs/1411.4555 — notes: short.
- [D07A] Antol et al., *VQA* — 2015 — PREPRINT/PAPER (ICCV 2015) — primary — role: task-predecessor —
  confidence: HIGH — overlap: absent/TS-002-absent — access: NOT_ACCESSED —
  why: task that exposed language-prior shortcut (D10 control origin) — URL: https://arxiv.org/abs/1505.00468 —
  notes: short.
- [D07A] Radford et al., *CLIP* — 2021 — PREPRINT/PAPER (ICML 2021) — primary —
  role: historical-anchor — confidence: HIGH — overlap: TS-001-partial/TS-002-partial —
  access: NOT_ACCESSED — why: fixed-ontology → language-addressable break; zero-shot transfer —
  URL: https://arxiv.org/abs/2103.00020 —
  notes: TS-002 conditioning angle reused by reference; new angle = addressability transition.
- [D07A] Jia et al., *ALIGN* — 2021 — PREPRINT/PAPER (ICML 2021) — primary — role: variant-node —
  confidence: HIGH — overlap: partial/partial — access: NOT_ACCESSED —
  why: noisy web-scale scaling point — URL: https://arxiv.org/abs/2102.05918 — notes: short.
- [D07A] SigLIP (see D06 entry) — cross-listed variant-node (sigmoid objective distinction).

## D07B — Open-vocabulary perception & grounding (SPLIT-OUT lane)

- [D07B] Plummer et al., *Flickr30k Entities (phrase grounding)* — 2015 — PAPER/DATASET — primary —
  role: task-origin — confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: region-word correspondence task origin — URL: (resolve Round D) — notes: verify citation.
- [D07B] Yu et al., *RefCOCO/+/g (Modelling Context in Referring Expressions)* — 2016 —
  PREPRINT/DATASET — primary — role: task-anchor (REC eval) — confidence: HIGH —
  overlap: absent/absent — access: NOT_ACCESSED — why: referring-expression grounding eval home —
  URL: https://arxiv.org/abs/1606.03825 — notes: eval authority for grounding precision.
- [D07B] Zareian et al., *OVR-CNN* — 2021 — PREPRINT — primary — role: concept-origin —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: first open-vocabulary detection concept (caption-grounded V2L) — URL: (resolve Round D) —
  notes: verify exact citation; surveys confirm existence (arXiv:2306.15880).
- [D07B] Gu et al., *ViLD* — 2021 — PREPRINT — primary — role: transition-node —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: first CLIP-knowledge open-vocabulary detector (distillation) — URL: (resolve Round D) —
  notes: verify exact citation.
- [D07B] Li et al., *GLIP* — 2021 — PREPRINT/PAPER (CVPR 2022) — primary — role: historical-anchor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: detection reformulated as phrase grounding; GoldG grounding-data practice —
  URL: https://arxiv.org/abs/2112.03857 — notes: open code; GoldG practice feeds X01.
- [D07B] Minderer et al., *OWL-ViT* — 2022 — PREPRINT/PAPER (ECCV 2022) — primary —
  role: transition-node — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: minimal detection heads on frozen CLIP (late-fusion pole) — URL: https://arxiv.org/abs/2205.06230 —
  notes: contrast pole vs GLIP early fusion.
- [D07B] Zhang et al., *Detic* — 2022 — PREPRINT — primary — role: variant-node —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: classification-data weak supervision variant — URL: (resolve Round D) — notes: short; verify ID.
- [D07B] Gu et al., *RegionCLIP* — 2021 — PREPRINT/PAPER (CVPR 2022) — primary —
  role: variant-node — confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: CLIP pseudo region-word pairs — URL: (resolve Round D) — notes: short; verify ID.
- [D07B] Liu et al., *Grounding DINO* — 2023 — PREPRINT — primary — role: historical-anchor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: tight fusion + detection/REC unification (52.5 COCO zero-shot AP; ODinW record) —
  URL: https://arxiv.org/abs/2303.05499 — notes: open checkpoints; REC zero-shot call explicitly noted.
- [D07B] Minderer et al., *OWL-ST / OWLv2* — 2023 — PAPER (NeurIPS 2023) + PREPRINT — primary —
  role: scaling-node — confidence: MEDIUM-HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: web-scale self-training to 1B+ examples; LVIS-rare 31.2→44.6% (X01 exhibit) —
  URL: (resolve Round D; NeurIPS 2023 proceedings) — notes: "unseen" claim is label-space-sensitive (CV2-DM-020).
- [D07B] Kamath et al., *MDETR* — 2021 — PREPRINT/PAPER (ICCV 2021) — primary —
  role: transition-node — confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: modulated detection + GoldG soft-token prediction — URL: (resolve Round D) — notes: verify ID.
- [D07B] Open-vocabulary segmentation branch (LSeg → OpenSeg → ODISE → X-Decoder) — various —
  PAPER/PREPRINT — primary — role: branch-nodes — confidence: LOW — overlap: absent/absent —
  access: NOT_ACCESSED — why: OVS program completeness; SAM+CLIP combination endpoint —
  URL: (resolve Round D) — notes: place here, cross-ref D03; do not duplicate.
- [D07B] OVD/OVS survey (arXiv:2307.09220) + open-vocabulary survey (arXiv:2306.15880) + OWD survey
  (arXiv:2508.16527) — 2023–2025 — SURVEY — secondary — role: taxonomic-witness ONLY —
  confidence: HIGH (IDs confirmed live) — overlap: absent/absent — access: NOT_ACCESSED —
  why: corroborate lane-level standaloneness; NEVER mechanism authority (CV2-DM-020) —
  URLs: https://arxiv.org/abs/2307.09220, https://arxiv.org/abs/2306.15880, https://arxiv.org/abs/2508.16527 —
  notes: surveys date quickly; use for taxonomy cross-check at intake.

## D08 — Bridging pretrained vision and language models

- [D08] Tsimpoukelli et al., *Frozen* — 2021 — PREPRINT — primary — role: precursor-context —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: frozen-LLM bridging precursor, one line — URL: https://arxiv.org/abs/2106.13884 — notes: short.
- [D08] Alayrac et al., *Flamingo* — 2022 — PREPRINT — primary — role: historical-anchor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: few-shot VL bridging via gated cross-attention — URL: https://arxiv.org/abs/2204.14198 — notes: none.
- [D08] Li et al., *BLIP-2* — 2023 — PREPRINT/PAPER (ICML 2023) — primary — role: historical-anchor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: frozen–frozen + Q-Former bridging — URL: https://arxiv.org/abs/2301.12597 — notes: none.
- [D08] Dai et al., *InstructBLIP* — 2023 — PREPRINT — primary —
  role: missing-bridge-node (absent from Sol map — ADD) — confidence: HIGH —
  overlap: absent/absent — access: NOT_ACCESSED — why: instruction-tuning bridge BLIP-2→LLaVA —
  URL: https://arxiv.org/abs/2305.06500 — notes: genuine predecessor gap fill.
- [D08] Zhu et al., *MiniGPT-4* — 2023 — PREPRINT — primary — role: bridge-node —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: same instruction-tuning bridge function, open — URL: https://arxiv.org/abs/2304.10592 — notes: short.
- [D08] Liu et al., *LLaVA (Visual Instruction Tuning)* — 2023 — PREPRINT (NeurIPS 2023) — primary —
  role: historical-anchor — confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: vision-encoder+LLM + visual instruction tuning as central training step —
  URL: https://arxiv.org/abs/2304.08485 — notes: X01-stage exhibit (instruction-tuning data).

## D09 — Native/omni fusion, tokenization, context economics (+ audio-input checklist)

- [D09] Bai et al., *Qwen2.5-VL Technical Report* — 2025 — PREPRINT — primary —
  role: predecessor-node — confidence: HIGH — overlap: partial/partial — access: NOT_ACCESSED —
  why: M-RoPE + dynamic resolution predecessor of Qwen3-VL — URL: https://arxiv.org/abs/2502.13923 —
  notes: none.
- [D09] Qwen Team, *Qwen3-VL Technical Report* — 2025 — PREPRINT (arXiv:2511.21631) — primary —
  role: ARCHITECTURE_CASE (open) — confidence: HIGH (abstract + repo verified live 2026-09-30) —
  overlap: TS-001-partial/TS-002-partial — access: NOT_ACCESSED —
  why: DeepStack multi-level ViT features; interleaved-MRoPE; text-timestamp video alignment;
  4-stage recipe (67B→~1T→~1T→100B) with sqrt-reweighting; 256K interleaved context; dense+MoE family —
  URL: https://arxiv.org/abs/2511.21631 ; repo: https://github.com/QwenLM/Qwen3-VL —
  notes: unusually mechanism-rich 2026 first-party source; token/config claims are config-bound (CV2-DM-020).
- [D09] Qwen Team, *Qwen3-Omni Technical Report* — 2025 — PREPRINT (arXiv:2509.17765) — primary —
  role: ARCHITECTURE_CASE omni fusion (Apache 2.0) — confidence: HIGH (report content verified live) —
  overlap: TS-001-partial/TS-002-partial — access: NOT_ACCESSED —
  why: Thinker–Talker MoE; TM-RoPE absolute-time 80ms alignment; audio encoder from scratch (20M hrs);
  234ms first-packet streaming; 36 audio/AV benchmarks; no-degradation-vs-single-modal claim —
  URL: https://arxiv.org/abs/2509.17765 ; repo: https://github.com/QwenLM/Qwen3-Omni —
  notes: no-degradation claim is vendor-measured (CV2-DM-020); TS-003 uses input/fusion side only.
- [D09] Radford et al., *Whisper* — 2022 — PREPRINT/PAPER (ICML 2023) — primary —
  role: audio-input predecessor (understanding side only) — confidence: HIGH —
  overlap: absent/TS-002-partial — access: NOT_ACCESSED — why: robust audio-input encoder precedent —
  URL: https://arxiv.org/abs/2212.04356 — notes: generation history stays in TS-002.
- [D09] CLAP (audio-language alignment) — 2022/2023 — PREPRINT — primary —
  role: predecessor-node (CLIP parallel for audio) — confidence: LOW — overlap: absent/TS-002-partial —
  access: NOT_ACCESSED — why: audio-side addressability predecessor — URL: (resolve Round D) —
  notes: verify exact citation (CLAP 2022 vs LAION-CLAP 2023).
- [D09] AudioSet (Gemmeke et al. 2017) — DATASET/PAPER — primary — role: data-predecessor —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: audio-event data contract predecessor (X01) — URL: (resolve Round D) — notes: short.
- [D09] DeepMind, *Gemini 3.1 Pro model card* — 2026-02-19 — OFFICIAL_REPORT — official —
  role: CAPABILITY_CASE + EVALUATION_CASE + DEPLOYMENT_CASE (NEVER architecture) —
  confidence: HIGH (card verified live) — overlap: partial/partial — access: NOT_ACCESSED —
  why: closed native-multimodal pole (1M context; text/image/audio/video-in; MMMU-Pro/Video-MMMU claims) —
  URL: https://deepmind.google/models/model-cards/gemini-3-1-pro/ —
  notes: scores are vendor claims with methodology pages; bind version+date (CV2-DM-013).
- [D09] DeepMind, *Gemini 3.6 Flash model card* — 2026-07-21 — OFFICIAL_REPORT — official —
  role: DEPLOYMENT_CASE (token-efficiency pole) — confidence: HIGH (verified live) —
  overlap: TS-001-partial/partial — access: NOT_ACCESSED —
  why: efficiency-positioned native multimodal; X03 exhibit — URL: (card URL; resolve at intake) —
  notes: capability facts only.

## D10 — Multimodal reasoning / failure decomposition

- [D10] Yue et al., *MMMU* — 2023 — PREPRINT — primary — role: eval-anchor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: comprehensive multimodal-reasoning eval home — URL: https://arxiv.org/abs/2311.16502 — notes: none.
- [D10] Li et al., *POPE (hallucination polling)* — 2023 — PREPRINT/PAPER (EMNLP 2023) — primary —
  role: eval-anchor (X04 instrument) — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: controlled hallucination measurement — URL: https://arxiv.org/abs/2305.10355 —
  notes: none.
- [D10] Liu et al., *MMBench* — 2023 — PREPRINT — primary — role: eval-anchor candidate —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: bilingual/multitask VLM eval — URL: https://arxiv.org/abs/2307.06281 — notes: verify citation Round D.
- [D10] MMMU-Pro — 2024/2025 — PREPRINT — primary — role: eval-anchor (harder reasoning) —
  confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: Gemini 3.1 Pro card context metric (80.5–81.0 vendor claim) — URL: (resolve Round D) —
  notes: verify citation; vendor score needs condition binding.
- [D10] MathVista / MathVision (visual math) — various — PREPRINT — primary — role: eval-nodes —
  confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: Qwen3-VL leading-claim evals; perception-vs-reasoning attribution testbed —
  URL: (resolve Round D) — notes: verify citations.
- [D10] HallusionBench — 2023 — PREPRINT — primary — role: eval-node candidate —
  confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: adversarial-visual hallucination eval — URL: (resolve Round D) — notes: verify citation.
- [D10] Gemini 3 "visual thinking via code execution" (dev guide, live 2026-09-30) — OFFICIAL_PAGE —
  official — role: CAPABILITY_CASE (tool-assisted perception) — confidence: MEDIUM —
  overlap: absent/absent — access: NOT_ACCESSED — why: scaffold-vs-grounding exhibit for D10/X04 —
  URL: https://ai.google.dev/gemini-api/docs/gemini-3 — notes: capability description only; no mechanism.

## D11 — Video understanding / temporal memory / event grounding

- [D11] Kay et al., *Kinetics* — 2017 — PREPRINT/PAPER (CVPR 2017) — primary —
  role: predecessor-node — confidence: HIGH — overlap: absent/TS-002-partial —
  access: NOT_ACCESSED — why: action-recognition predecessor — URL: https://arxiv.org/abs/1705.06950 —
  notes: short.
- [D11] Goyal et al., *Something-Something V2* — 2017 — PREPRINT/PAPER (ICCV 2017) — primary —
  role: predecessor-node — confidence: HIGH — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: temporal-ordering-sensitive predecessor — URL: https://arxiv.org/abs/1706.04261 — notes: short.
- [D11] Grauman et al., *Ego4D* — 2021 — PREPRINT/PAPER (CVPR 2022) — primary —
  role: data-predecessor (X01) — confidence: HIGH — overlap: absent/TS-002-partial —
  access: NOT_ACCESSED — why: egocentric + audio-visual + trajectory-adjacent data —
  URL: https://arxiv.org/abs/2110.07058 — notes: feeds D13 data ancestry too.
- [D11] Fu et al., *Video-MME* — 2024 — PREPRINT — primary — role: eval-anchor candidate —
  confidence: MEDIUM — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: full-spectrum video-analysis eval — URL: https://arxiv.org/abs/2405.21075 — notes: verify Round D.
- [D11] Xiao et al., *LongVideoBench* — 2024 — PREPRINT — primary — role: eval-anchor candidate —
  confidence: MEDIUM — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: long-video retention eval — URL: https://arxiv.org/abs/2407.15754 — notes: verify Round D.
- [D11] Video-MMMU — 2025 — PREPRINT — primary — role: eval-node —
  confidence: LOW — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: Gemini 3 context metric (87.6 vendor claim) — URL: (resolve Round D) — notes: verify citation.
- [D11] Streaming/online video understanding systems — TBD — various — role: conditional fill —
  confidence: LOW — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: LOW_YIELD in Round B; Round D fill-or-declare task — URL: (do not assume) —
  notes: record LOW_YIELD/EVIDENCE_GAP if unfilled; do not pad.

## D12 — GUI / Computer Use

- [D12] Xie et al., *OSWorld* — 2024 — PREPRINT/PAPER (NeurIPS 2024) + OFFICIAL_REPO — primary —
  role: historical-anchor ( grounding-bottleneck thesis: best 12.24% vs human 72.36%) —
  confidence: HIGH — overlap: TS-001-partial/TS-002-absent — access: NOT_ACCESSED —
  why: real-OS multimodal-agent environment + benchmark origin —
  URL: https://arxiv.org/abs/2404.07972 ; repo: https://github.com/xlang-ai/OSWorld —
  notes: none.
- [D12] Yuan et al., *OSWorld 2.0* — 2026 — PREPRINT (arXiv:2606.29537) + site — primary —
  role: current-anchor (NEW — absent from Sol map; state-management-bottleneck thesis) —
  confidence: HIGH (paper + site verified live 2026-09-30) — overlap: TS-001-partial/TS-002-absent —
  access: NOT_ACCESSED —
  why: 108 long-horizon tasks; median 1.6 human-hrs; ~318 vs ~30 tool calls; best 20.6% binary /
  54.8% partial; cost-aware + safety-audit methodology; reframes D12 thesis —
  URL: https://arxiv.org/abs/2606.29537 ; site: https://osworld-v2.xlang.ai/ —
  notes: strictest condition binding in volume (model+thinking+tool+steps+release v2026.06.24).
- [D12] ScreenSpot-class element-grounding evals — various — BENCHMARK — primary —
  role: eval-node — confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: pure grounding-accuracy substrate beneath agent success — URL: (resolve Round D) —
  notes: verify citation.
- [D12] Set-of-Mark prompting — 2023 — PREPRINT — primary — role: technique-node —
  confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: grounding-scaffold technique (scaffold-vs-grounding debate) — URL: (resolve Round D) —
  notes: verify citation.
- [D12] Pre-OSWorld web/OS agent lineage (Mind2Web-class; SeeClick-class) — various —
  PAPER/PREPRINT — primary — role: predecessor-nodes — confidence: LOW —
  overlap: absent/absent — access: NOT_ACCESSED — why: web-phase vs OS-phase distinction —
  URL: (resolve Round D) — notes: bound tightly; web-phase ≠ OS-phase.
- [D12] Vendor computer-use deployments (Gemini 2.5 Computer Use; Claude computer-use;
  Operator-class) — 2025–2026 — OFFICIAL_PAGE — official — role: DEPLOYMENT_CASE pointers —
  confidence: MEDIUM — overlap: partial/absent — access: NOT_ACCESSED —
  why: deployment facts only; Gemini 3 launch blog (2025-11-18) confirms 2.5 Computer Use existence —
  URL: https://blog.google/products-and-platforms/products/gemini/gemini-3/ (pointer; bind exact pages Round D) —
  notes: NO mechanism claims from product pages (CV2-DM-020).

## D13 — VLA / embodied multimodal systems

- [D13] Ahn et al., *SayCan* — 2022 — PREPRINT — primary —
  role: missing-predecessor (ADD) — confidence: MEDIUM — overlap: absent/absent —
  access: NOT_ACCESSED — why: grounding language plans in affordances; anti-RT-2-abruptness —
  URL: (resolve Round D) — notes: verify exact citation.
- [D13] Driess et al., *PaLM-E* — 2023 — PREPRINT/PAPER (ICML 2023) — primary —
  role: missing-predecessor (ADD) — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: direct embodied-multimodal-LM predecessor ("VLM into body") —
  URL: https://arxiv.org/abs/2303.03378 — notes: none.
- [D13] O'Neill et al., *Open X-Embodiment* — 2023 — PREPRINT/PAPER (ICRA 2024) — primary/DATASET —
  role: missing-data-predecessor (ADD; X01) — confidence: HIGH — overlap: absent/absent —
  access: NOT_ACCESSED — why: the data contract enabling transfer-scale —
  URL: https://arxiv.org/abs/2310.08864 — notes: none.
- [D13] Brohan et al., *RT-1* — 2022 — PREPRINT — primary — role: direct-predecessor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: large-scale real-robot kitchen-task policy base — URL: https://arxiv.org/abs/2212.06817 — notes: none.
- [D13] Brohan et al. / Zitkovich et al., *RT-2* — 2023 — PREPRINT — primary —
  role: historical-anchor (VLA formulation: actions-as-text-tokens; co-fine-tuning) —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: VLA formulation origin — URL: https://arxiv.org/abs/2307.15818 — notes: none.
- [D13] Kim et al., *OpenVLA* — 2024 — PREPRINT/PAPER (CoRL 2024) + OFFICIAL_REPO — primary —
  role: ARCHITECTURE_CASE (open) — confidence: HIGH — overlap: TS-001-partial/TS-002-absent —
  access: NOT_ACCESSED — why: open-weights VLA policy formulation; independent-inspection possible —
  URL: https://arxiv.org/abs/2406.09246 — notes: none.
- [D13] DeepMind, *Gemini Robotics 2 + On-Device 2* (blog + model pages + On-Device 2 model card) —
  2026-07-30 — OFFICIAL_PAGE/OFFICIAL_REPORT — official —
  role: CAPABILITY_CASE + EVALUATION_CASE (card-scoped) + DEPLOYMENT_CASE; NEVER architecture —
  confidence: HIGH (pages + card verified live 2026-09-30) — overlap: TS-001-partial/TS-002-absent —
  access: NOT_ACCESSED —
  why: whole-body humanoid VLA; natively multi-embodiment <200-example adaptation; trusted-tester /
  private-preview distribution; stated bi-arm-primary scope + high-DoF limits; TS-001-crossover exhibit —
  URLs: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/ ;
  https://deepmind.google/models/gemini-robotics/ ;
  https://deepmind.google/models/gemini-robotics/on-device/ ;
  https://deepmind.google/models/model-cards/gemini-robotics-on-device-2/ —
  notes: quote card scope limits verbatim; no latency/price/token facts published; planner–policy split
  (ER 2 + VLA) is the live three-way-framing exhibit (§B-D13).

## D14 — Predictive representations / World Models

- [D14] Ha & Schmidhuber, *World Models* — 2018 — PREPRINT — primary —
  role: terminological-origin (NOT technical ancestor of Genie — §G.5) — confidence: HIGH —
  overlap: absent/TS-002-partial — access: NOT_ACCESSED — why: term origin + VAE+RNN+controller formulation —
  URL: https://arxiv.org/abs/1803.10122 — notes: explicit non-ancestry statement required in prose.
- [D14] Hafner et al., *Dreamer (PlaNet lineage)* — 2019 — PREPRINT/PAPER — primary —
  role: dynamics-line — confidence: HIGH — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: latent-dynamics-for-planning pole origin — URL: https://arxiv.org/abs/1912.01603 — notes: none.
- [D14] Hafner et al., *DreamerV3* — 2023 — PREPRINT — primary — role: ARCHITECTURE_CASE (open) —
  confidence: HIGH — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: general latent-dynamics capstone; non-generative pole anchor —
  URL: https://arxiv.org/abs/2301.04104 — notes: none.
- [D14] LeCun et al., *I-JEPA* — 2023 — PREPRINT — primary — role: competing-interpretation anchor —
  confidence: HIGH — overlap: absent/absent — access: NOT_ACCESSED —
  why: predictive-representation-without-generation pole — URL: https://arxiv.org/abs/2301.08243 — notes: none.
- [D14] V-JEPA-class — 2024 — PREPRINT — primary — role: ARCHITECTURE_CASE candidate —
  confidence: LOW — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: video predictive-representation pole — URL: (resolve Round D) — notes: verify exact citation.
- [D14] Bruce et al., *Genie* — 2024 — PREPRINT (arXiv:2402.15391) — primary —
  role: interactive-generative pole origin — confidence: MEDIUM-HIGH — overlap: absent/TS-002-partial —
  access: NOT_ACCESSED — why: latent-action interactive environment from unlabelled video —
  URL: https://arxiv.org/abs/2402.15391 — notes: re-verify ID at intake.
- [D14] DeepMind, *Genie 2 page* — 2024/2025 — OFFICIAL_PAGE — official —
  role: CAPABILITY_CASE — confidence: MEDIUM — overlap: absent/TS-002-partial — access: NOT_ACCESSED —
  why: action-controllable generative-environment predecessor of Genie 3 —
  URL: (DeepMind Genie pages; resolve at intake) — notes: vendor facts only.
- [D14] DeepMind, *Genie 3* (blog 2025-08-05 + model page + Project Genie Jan 2026) — OFFICIAL_PAGE —
  official — role: CAPABILITY_CASE + DEPLOYMENT_CASE-pointer; explicitly NOT ARCHITECTURE_CASE —
  confidence: HIGH (blog + model page verified live 2026-09-30) — overlap: absent/TS-002-partial —
  access: NOT_ACCESSED —
  why: real-time 24fps/720p interactive worlds; ~1-min visual memory; minutes-scale consistency;
  promptable world events; SIMA-agent training use; limited action space; 60s prototype cap (Project Genie) —
  URLs: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ ;
  https://deepmind.google/models/genie/ ;
  https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/ —
  notes: no paper/weights; "emergent consistency vs NeRF/3DGS" is vendor framing — attribute, don't adopt.
- [D14] Waymo World Model (Genie-3-derived applied variant) — 2025/2026 — OFFICIAL_PAGE — official —
  role: DEPLOYMENT_CASE pointer — confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: applied branching (edge-case simulation; lidar/action/layout/language controls per secondary reports) —
  URL: (verify primary source Round D) — notes: currently secondary-confirmed only; do not cite until primary bound.

## D15 — Evaluation / robustness / provenance / convergence (+ X-synthesis)

- [D15] LVIS (Gupta et al. 2019) — DATASET/BENCHMARK — primary — role: OVD eval home (rare-AP) —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: D07B grounding-eval authority — URL: (resolve Round D) — notes: bind split + vocab.
- [D15] ODinW (Li et al. 2022) — BENCHMARK — primary — role: in-the-wild detection eval —
  confidence: MEDIUM — overlap: absent/absent — access: NOT_ACCESSED —
  why: Grounding DINO record context (26.1 mean AP zero-shot claim — vendor/author-measured) —
  URL: (resolve Round D) — notes: verify citation.
- [D15] MMEB-V2 (via Qwen3-VL-Embedding report arXiv:2601.04720) — BENCHMARK (secondary-bound) —
  primary-via-report — role: retrieval-eval methodology — confidence: MEDIUM —
  overlap: absent/absent — access: NOT_ACCESSED — why: multimodal-retrieval eval practice (77.8 SOTA claim) —
  URL: https://arxiv.org/abs/2601.04720 — notes: methodology via report; leaderboard claim vendor-measured.
- [D15] Interleaved-data representatives (OBELISC / MMC4-class) — DATASET — primary —
  role: X01-synthesis nodes — confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: supervision-timeline synthesis stages — URL: (resolve Round D) — notes: verify exact citations.
- [D15] Visual-instruction-tuning data (LLaVA-Instruct) + synthetic multimodal (ALLaVA-class) +
  preference/post-training for VLMs (RLHF-V/RLAIF-V-class) — DATASET/PREPRINT — primary —
  role: X01-synthesis nodes — confidence: LOW — overlap: absent/absent — access: NOT_ACCESSED —
  why: post-pretraining supervision stages; thinnest X01 part — URL: (resolve Round D) —
  notes: targeted Round D fill; verify each citation.
- [D15] Classical metric definitions (mAP / IoU / CER-WER where load-bearing) — references —
  role: cited-context — confidence: HIGH (concepts stable) — overlap: partial/partial —
  access: NOT_ACCESSED — why: definition-level authority only — URL: (bind at intake) —
  notes: no mechanism depth.

## X-axes (cross-cutting; collected through D-lane entries above, not separately)

- X01 surfaces in: ImageNet/LAION-class pairs (D07A), GoldG/GoldG-practice (D07B), OWL-ST 1B self-training
  (D07B), LLaVA-Instruct (D08), Qwen3-VL 4-stage recipe (D09), Open X-Embodiment + Ego4D (D13/D11),
  interleaved/synthetic/preference datasets (D15). No standalone X01 entries — by design (§C-X01).
- X02 surfaces in: contrastive-vs-captioning (D07A), detection-vs-grounding contracts (D07B),
  projector/Q-Former/cross-attention (D08), Thinker–Talker + TM-RoPE (D09), screenshot-vs-a11y/MCP (D12),
  planner–policy split (D13), four-way world-model split (D14).
- X03 surfaces in: Qwen3-VL token/config fields (D09), Qwen3-Omni 234ms latency (D09), Genie 3 rollout
  compute (D14), OSWorld 2.0 token-vs-completion curves (D12), On-Device 2 constraints (D13).
- X04 surfaces in: POPE/HallusionBench (D10), contamination/judge-dependence methodology (D15),
  four-role vendor tagging (H), condition-binding discipline (TS-001/TS-002 import, §F).

---

## Round D verification list (exact-citation or fill-or-declare tasks)

LOW-confidence items above requiring exact-ID verification before production intake: YOLO-World ID;
Flickr30k Entities citation; OVR-CNN citation; ViLD citation; Detic ID; RegionCLIP ID; MDETR ID;
OVS branch (LSeg/OpenSeg/ODISE/X-Decoder) citations; OWL-ST/OBELISC/MMC4/LLaVA-Instruct/ALLaVA/
RLHF-V/RLAIF-V/CLAP/AudioSet/ScreenSpot/Set-of-Mark/Mind2Web/SeeClick/SayCan/V-JEPA/LVIS/ODinW/
MMMU-Pro/MathVista/MathVision/HallusionBench/Video-MMMU citations; Waymo World Model primary source;
second open-VLM family; document specialist role; streaming-system fill-or-declare; vendor
computer-use exact 2026 pages. This list is the bounded Round D work order — not Round B scope failure.
