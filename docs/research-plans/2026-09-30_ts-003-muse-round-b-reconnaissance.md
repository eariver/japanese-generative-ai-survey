# TS-003 Vision & Multimodal AI — Muse Round B bounded reconnaissance report

Status: `ROUND_B_RECONNAISSANCE / PRE_SOL_ROUND_C / NOT_PRODUCTION_AUTHORITY`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `planning/ts-003-vision-multimodal-preresearch-20260930` (no new branch created)

Starting authority verified read-only before any write:

- Exact Starting SHA: `def6829efdd29cbb825825c59060b17e09e2ebe7` — remote HEAD matched
- Expected Starting Tree: `ebb2fd528e7127ef9ac3aa4efac170340d2847c2` — remote tree matched

Companion authorities (read in mandatory order, challenged — not assumed correct):

- `docs/research-plans/2026-09-30_ts-003-vision-multimodal-sol-preresearch-skeleton.md` (Sol skeleton)
- `docs/research-plans/2026-09-30_ts-003-sol-scope-audit-before-worker.md` (Sol scope audit)
- `docs/thematic-special-backlog.md`, `surveys/special/efficient-llm-2026/main.tex` (TS-001 final),
  `surveys/special/beyond-text-2026/main.tex` (TS-002 final)
- `docs/research-plans/2026-09-24_ts-002-beyond-text-sol-preresearch.md`,
  `docs/research-plans/2026-09-24_ts-002-beyond-text-muse-discovery-contract-draft.md` (TS-002 precedent)
- `docs/core-v2-deferred-maintenance-summary.md` (CV2-DM-006, CV2-DM-013, CV2-DM-020 applied below)

This is **bounded reconnaissance, not production Discovery**. No Source Intake, Screening, Evidence,
Completeness, Materiality, Selection, Architecture, Draft, PDF, Freeze, or Release was performed.
All source candidates below are `NOT_ACCESSED` planning material for Sol Round C. No canonical
Discovery ledger was created. Existing Sol documents were left read-only; all findings are additive.

Method: per-lane representative primary/official sources sufficient to judge lineage, missing nodes,
competing interpretations, limitations, capstone candidacy, and access risk. Thin-source padding was
refused; low-yield lanes are reported as `LOW_YIELD` / `EVIDENCE_GAP` rather than filled.

Terminology discipline (CV2-DM-006): canonical model/task/metric/benchmark names are preserved in
English/katakana form. No forced literal Japanese translation of technical identities is introduced
in this report. Claim-strength discipline (CV2-DM-020): vendor capability claims, published
mechanisms, and independently reproduced behavior are kept distinct throughout; a resolved citation
is never treated as proof of claim semantics. Date discipline (CV2-DM-013): source publication,
version, and announcement dates are recorded as distinct events where they differ.

---

## A. Executive finding

### A.1 Is the current Sol structure broadly sound?

**Yes, with one structural split and three weight corrections.** The D01–D15 + X01–X04 map is
directionally correct and does not need wholesale expansion. The three-volume thesis
(compute → generate → perceive/ground/reason/predict/act) survives contact with evidence, and the
"directed graph of converging lineages, not a single ladder" framing is confirmed by every lane
examined: open-vocabulary detection, instruction-tuned VLMs, omni fusion, GUI agents, VLA, and world
models each have partially independent ancestries that meet late.

### A.2 Biggest gap

**D07 as a single lane collapses two different technical transitions.** Sol's scope audit already
flagged this ("make grounding/open-vocabulary perception explicit") and proposed refining D07's
title. Reconnaissance finds the title fix **insufficient**: image-level language alignment
(CLIP/ALIGN/SigLIP: image–text pairs → zero-shot classification/retrieval) and open-vocabulary
localization/grounding (OVR-CNN → ViLD → GLIP → OWL-ViT → Grounding DINO → OWLv2/OWL-ST;
referring-expression lineage RefCOCO/Flickr30k Entities → MDETR → REC evaluation) differ in
objective, training data, evaluation authority (zero-shot accuracy vs LVIS-rare AP / RefCOCO grounding
accuracy / ODinW), and downstream consumer (VLM conditioning vs GUI/VLA actionable coordinates).
Forcing them into one lane will reproduce exactly the "潰さない" failure the task brief prohibits.
**Recommendation: SPLIT D07 into D07A (image-level vision-language alignment) and D07B
(open-vocabulary perception and grounding).** Detail in §B-D07 and Challenge A verdict (§A.5).

### A.3 Biggest over-scope risk

**D04 (geometry/3D/spatial) and the Tier B endpoints (D12–D14) in that order.** D04 is one
NeRF/SLAM survey away from escaping the volume; its legitimate TS-003 content is narrow
(what spatial information survives into language-token and action representations). Among Tier B,
D13 (VLA) has the strongest ballooning gradient because whole-body humanoid control (Gemini
Robotics 2, 2026-07-30) invites control-theory and locomotion exposition that TS-003 must refuse.
None of these lanes should be dropped — each carries a load-bearing convergence argument — but all
three need explicit page/weight caps and refusal lists. Detail in §E and §K.

### A.4 Most important restructuring proposal

1. **SPLIT D07 → D07A + D07B** (above).
2. **Keep X01 cross-cutting; do NOT promote data/supervision to a D-lane** (Challenge B verdict).
   Add instead a mandatory per-lane data-contract block plus a Tier C supervision-timeline synthesis.
3. **Confirm the Challenge C boundary as drawn** (vision-centered; audio-input/fusion/reasoning only
   in TS-003, all generation history in TS-002) **but expand D09/D11 scope checklists** to explicitly
   own audio-input encoding, heterogeneous token/sample rates, absolute-time alignment, and streaming.
4. **Reframe D12 around the OSWorld 1.0 → 2.0 transition** (June 2026): the bottleneck moved from
   GUI grounding to long-horizon state management. D12's thesis must move with it.
5. **Rebalance D14 with a non-generative counterweight** (Dreamer-family latent dynamics, JEPA-type
   predictive representation) so it does not become a Genie chronology; Genie 3 is a
   `CAPABILITY_CASE`, not an `ARCHITECTURE_CASE` (no architecture paper; vendor blog + model page only).

### A.5 Round C re-examination list for Sol

Sol Round C must re-judge, with this report + original skeleton + scope audit + TS-001/TS-002 finals
open simultaneously: Core Question wording (§K.1); D07 split; X01 non-promotion; Tier A/B/C weights
(§K.4); TS-001 boundary (token/context economics reuse); TS-002 boundary (generation vs
understanding, audio split); vision-centrality; audio/omni scope checklist; grounding placement;
data/supervision axis shape; GUI/VLA/World-Model weights; evaluation chapter range (benchmark
methodology, not catalogue); page/depth expectation (80–120pp envelope, Tier-weighted).

### Challenge verdicts (summary; evidence in §§B–D)

- **Challenge A (grounding boundary): SEPARATE.** The six-stage boundary
  (closed-set → language-aligned → open-vocabulary recognition → open-vocabulary detection →
  referring-expression grounding → actionable grounding) is confirmed as six genuinely distinct
  technical contracts. D07 SPLIT required.
- **Challenge B (data/supervision history): X01 SUFFICES, strengthened.** Architecture-only history
  would indeed distort TS-003, but a standalone data lane would duplicate every lane's training
  section and decay into a dataset catalogue. Verdict: KEEP X01 cross-cutting + REWEIGHT upward.
- **Challenge C (beyond vision+text): CURRENT BOUNDARY VALID, checklist-expanded.** Qwen3-Omni
  (arXiv:2509.17765, Apache 2.0, Thinker–Talker MoE, TM-RoPE absolute-time alignment) and the Gemini 3
  native-audio/video family confirm omni convergence is 2026-material, but the TS-003/TS-002 split
  (input understanding/fusion/reasoning here; synthesis/generation history there) holds cleanly
  against that evidence.

---

## B. D01–D15 audit

Disposition vocabulary: `KEEP / MERGE / SPLIT / DROP / REWEIGHT / ADD` (combinations allowed).

### D01 — Visual representation / CNN / ImageNet — `KEEP + REWEIGHT (context weight, capped)`

- **Technical rationale.** The learned-feature-hierarchy break (handcrafted SIFT/HOG/bag-of-words →
  learned hierarchies) and the large-scale-supervised + GPU-scaling break (AlexNet/ImageNet 2012) plus
  the optimization break (ResNet residual framing, transfer to detection/segmentation) are genuine
  load-bearing predecessors: every later lane reuses "reusable representation vs task head" thinking.
  But D01's TS-003 function is *context*, not body: later lanes do not need CNN internals, only the
  representation-contract idea.
- **Candidate primary sources.** Krizhevsky et al., *ImageNet Classification with Deep CNNs* (2012,
  NIPS); He et al., *Deep Residual Learning* (arXiv:1512.03385, 2015); LeCun et al., LeNet
  (*Proc. IEEE* 1998) as concise predecessor context; Fukushima, Neocognitron (1980) one-paragraph
  context only.
- **Missing lineage nodes.** Neocognitron/LeNet pre-AlexNet context (anti-abrupt-start; see §G.1).
  SIFT/HOG cited as named context only — no papers needed.
- **Competing interpretation.** "AlexNet = big CNN + GPU + data" vs "AlexNet = ReLU/dropout/data
  augmentation engineering stack". Both reduce to: scaling recipe, not architectural novelty — which
  is precisely the TS-003-relevant reading (representation scaling precedent for later multimodal
  scaling). No conflict to resolve; record the recipe reading.
- **Evidence density.** HIGH for anchors; LOW for anything beyond ResNet that TS-003 would need —
  VGG/GoogLeNet add little TS-003-load-bearing content (depth-scaling footnotes at most).
- **Source-access risk.** LOW (all open).
- **TS-001/002 overlap.** TS-001: absent (CNN history not covered). TS-002: partial (VAE/tokenizer
  representation ideas adjacent, not duplicative). Disposition: full-new-treatment but **short**.
- **Current-case candidates.** None (historical lane by design).
- **Open questions.** How much expository weight does pre-2012 context deserve before it becomes a
  CV-textbook appendix? Proposed cap: ≤2 pages equivalent (see §K.5).

### D02 — Detection / structured localization — `KEEP`

- **Technical rationale.** Classification→localization is the first "representation insufficiency"
  transition in the volume's thesis: image-level labels cannot express object identity + location.
  The region-proposal → single-shot → set-prediction (DETR) arc, with anchors/NMS as fossilized
  machinery that DETR removed, is a clean mechanism story with no TS-001/002 duplication.
- **Candidate primary sources.** R-CNN (arXiv:1311.2524); Faster R-CNN (arXiv:1506.01497); YOLO
  (arXiv:1506.02640, lineage representative — not the whole one-stage history); SSD
  (arXiv:1512.02325) and RetinaNet (arXiv:1708.02002) as lineage-completeness nodes; DETR
  (arXiv:2005.12872, 2020); DINO detector (Zhang et al., arXiv:2203.03605) as DETR-successor node.
- **Missing lineage nodes.** DINO detector is absent from the Sol anchor map and should be added:
  it is the technical base of Grounding DINO (D07B) and the DETR-lineage capstone. **Terminology
  collision warning:** "DINO" = Caron et al. self-supervised vision (D06) AND Zhang et al. detector
  (D02/D07B). CV2-DM-006-adjacent identity hazard; the volume must disambiguate every occurrence.
- **Competing interpretation.** One-stage vs two-stage is largely a latency/accuracy operating-point
  debate, not a representation debate — say so explicitly to avoid over-philosophizing YOLO.
- **Evidence density.** HIGH.
- **Source-access risk.** LOW.
- **TS-001/002 overlap.** TS-001: absent. TS-002: partial (ControlNet consumes edge/depth/pose/
  segmentation signals as *generation controls* — explicitly not perception history; cross-reference
  only). Disposition: full-new-treatment.
- **Current-case candidates.** YOLO-World (open-vocabulary YOLO reformulation following GLIP) as
  D02→D07B bridge case (ARCHITECTURE_CASE candidate, open).
- **Open questions.** Whether OWOD (open-world detection, Joseph et al. 2021, unknown-aware) deserves
  a named node or a footnote inside D07B. Recommendation: footnote in D07B; OWOD's incremental
  TS-003 value over OVD is thin.

### D03 — Segmentation / promptable dense perception — `KEEP`

- **Technical rationale.** Dense prediction vs box prediction is a distinct task contract, and SAM's
  promptable/zero-shot-transfer reframing (task + model + SA-1B data system) is the first "vision
  foundation model" event in the volume — preceding general VLMs. DINOv2 vs SAM contrast
  (all-purpose features vs promptable interface) is the load-bearing comparison.
- **Candidate primary sources.** FCN (arXiv:1411.4038); U-Net (arXiv:1505.04597, vision-role only —
  must not import its TS-002 diffusion-backbone role); Mask R-CNN (arXiv:1703.06870); panoptic
  segmentation, Kirillov et al. (arXiv:1801.00868); SAM (arXiv:2304.02643); SAM 2
  (arXiv:2408.00714, 2024) as D11 bridge (video); DINOv2 comparison node (see D06).
- **Missing lineage nodes.** Interactive-segmentation predecessors (DEXTR, RITM-class) as one-line
  context so SAM's promptability does not appear ex nihilo; open-vocabulary segmentation family
  (LSeg, OpenSeg, ODISE, X-Decoder) — place in D07B, cross-referenced here, not duplicated.
- **Competing interpretation.** "SAM = segmentation foundation model" vs "SAM = promptable
  annotation engine whose zero-shot generality is task-bounded". Both readings are source-supported
  (SA-1B scale claim vs downstream evaluations); the volume should carry both with the evaluation
  evidence (D15) adjudicating per-task.
- **Evidence density.** HIGH.
- **Source-access risk.** LOW (SAM code/data cards open).
- **TS-001/002 overlap.** TS-001: absent. TS-002: partial (U-Net as diffusion backbone — explicitly
  different role; one cross-reference sentence). Disposition: full-new-treatment.
- **Current-case candidates.** SAM-family + specialist medical/remote-sensing segmenters as
  "generalist vs specialist" contrast — only if a generic mechanism point emerges; else negative
  space (§J).
- **Open questions.** Whether panoptic segmentation needs mechanism depth or a definition + citation.
  Recommendation: definition + citation (contract clarity, not mechanism).

### D04 — Geometry / depth / pose / 3D / spatial state — `KEEP + REWEIGHT (support weight, hard cap)`

- **Technical rationale.** Mandatory anti-abrupt-start function only: without it, spatial reasoning in
  D10, GUI coordinate prediction in D12, and VLA observation spaces in D13 lack ancestry. But its
  native content (multi-view geometry, SLAM, 3D reconstruction) is a separate discipline; every
  additional page beyond "what spatial information is absent from labels, and what survives
  tokenization" is over-scope.
- **Candidate primary sources (bounded).** A monocular-depth representative; a pose-estimation
  representative; scene-graph representative only if load-bearing for D10 spatial relations.
  Deliberately no full NeRF/3DGS/SLAM capture in Round B — the cap decision (below) makes most of
  that history out of scope by construction. Flag for Round C: Sol must name the 2–4 allowed
  mechanism nodes, else Worker will over-collect.
- **Missing lineage nodes.** None mandatory beyond the cap; the risk here is excess, not absence.
- **Competing interpretation.** "3D understanding via explicit geometry" vs "3D understanding via
  learned 2.5D/pattern shortcuts in VLMs" — this IS load-bearing (it determines how D10 spatial
  benchmarks are read). Keep the debate, cut the geometry textbook.
- **Evidence density.** MEDIUM for the narrow TS-003-relevant slice; HIGH for the excluded textbook
  (which must be refused).
- **Source-access risk.** LOW.
- **TS-001/002 overlap.** TS-001: absent. TS-002: partial (ControlNet depth/pose *controls*;
  camera/motion control signals — different question). Disposition: expand-from-new-angle, short.
- **Current-case candidates.** Spatial-VLM evaluations (as EVALUATION_CASE in D15 rather than D04
  mechanism cases).
- **Open questions.** Exact node allow-list and page cap (§K.5 proposes Tier A-floor weight).

### D05 — OCR → Document Intelligence — `KEEP`

- **Technical rationale.** Glyph recognition → layout-aware document understanding is one of the
  cleanest "representation insufficiency" arcs in the volume (pixels → symbols + layout + reading
  order + tables/charts/equations), and it directly feeds the "do native multimodal models really
  remove OCR bottlenecks or move them inside?" test — a first-class TS-003 question with no
  TS-001/002 home.
- **Candidate primary sources.** LayoutLM (arXiv:1912.13318); LayoutLMv3 (arXiv:2204.08387);
  Donut (arXiv:2111.15664, OCR-free); Pix2Struct (arXiv:2210.03347); Nougat (arXiv:2308.13418,
  academic-document specialist, MEDIUM confidence — verify role in Round C/D).
- **Missing lineage nodes.** Classical OCR history (one-line context only); chart/table specialist
  benchmarks (to be mapped in D15, not D05 mechanism); screenshot/UI-as-document bridge to D12
  (explicit handoff paragraph, not duplication).
- **Competing interpretation.** "Native VLMs obsolete OCR pipelines" vs "VLMs internalize OCR with
  resolution-dependent failure modes". Strongly source-testable (resolution ablations in Qwen3-VL-class
  reports); the volume must run this test, not assert either side.
- **Evidence density.** MEDIUM-HIGH (mechanism papers open; current specialist-vs-generalist
  comparison evidence thinner — partial EVIDENCE_GAP).
- **Source-access risk.** LOW.
- **TS-001/002 overlap.** TS-001: absent. TS-002: absent (text rendering *generation* is TS-002's;
  text *reading* is TS-003's — clean split). Disposition: full-new-treatment.
- **Current-case candidates.** A document/UI-strong generalist (Qwen3-VL-class doc/OCR eval section
  as EVALUATION_CASE) vs a specialist (Nougat-class as ARCHITECTURE_CASE if verified).
- **Open questions.** Whether multimodal retrieval/RAG-for-documents needs a named sub-lane here.
  Recommendation: bounded sub-lane under D05 (retrieval as document-work interface), not a new D.

### D06 — ViT / self-supervised visual foundation — `KEEP`

- **Technical rationale.** Two separable breaks: (1) ViT — convolution-to-sequence/token formulation
  of vision, the precondition for all later vision-language token fusion; (2) MAE/DINO/DINOv2 —
  label-free reusable visual features, the precondition for "foundation representation before language
  alignment". Collapsing them into "Transformer era" loses the volume's representation-first thesis.
- **Candidate primary sources.** ViT (arXiv:2010.11929); DeiT (arXiv:2012.12877, data-efficiency
  bridge); Swin (arXiv:2103.14030, hierarchy node — keep short); MAE (arXiv:2111.06377); DINO
  (arXiv:2104.14294); DINOv2 (arXiv:2304.07193); SigLIP (arXiv:2303.15343) as encoder-lineage node
  (Qwen3-VL builds on SigLIP2-So400m — encoder reuse is a 2026-load-bearing fact).
- **Missing lineage nodes.** Pre-ViT attention-in-vision context (non-local networks, one line);
  InstructBLIP-adjacent instruction-tuning is D08, not here. Self-supervised-video (V-JEPA-class)
  pointer to D14 counterweight.
- **Competing interpretation.** "ViT won by architecture" vs "ViT won by scale + pretraining recipe
  (DeiT/SWIN ablations cut both ways)". Record the recipe reading; it supports X01.
- **Evidence density.** HIGH.
- **Source-access risk.** LOW.
- **TS-001/002 overlap.** TS-001: partial (attention/KV/token-efficiency angle where material —
  reuse-by-reference; D06 must not retell FlashAttention). TS-002: partial (backbone role only where
  load-bearing). Disposition: expand-from-new-angle (representation/token-formulation angle is new).
- **Current-case candidates.** SigLIP2-family encoders inside 2026 VLMs as DEPLOYMENT_CASE
  (encoder reuse as deployment fact).
- **Open questions.** None structural.

### D07 — Vision-language alignment / open-vocabulary / grounding — `SPLIT → D07A + D07B`

This is the report's central structural recommendation. Evidence:

- **D07A — Image-level vision-language alignment (KEEP, narrowed).** Contract: fixed ontology →
  language-addressable image-level semantics via paired pretraining. Sources: DeViSE
  (arXiv:1312.5624, 2013, visual-semantic embedding predecessor); Show and Tell captioning
  (arXiv:1411.4555, 2014); VQA (arXiv:1505.00468, 2015) as task-predecessor; CLIP
  (arXiv:2103.00020); ALIGN (arXiv:2102.05918); SigLIP (arXiv:2303.15343, sigmoid-loss variant —
  materially distinct objective node). Evaluation: zero-shot classification/retrieval. Consumer:
  VLM conditioning (TS-002 cross-ref) and D08 bridges. TS-002 overlap: partial (CLIP-as-conditioning
  covered) → TS-003 reuses by reference, new angle is *addressability transition*.
- **D07B — Open-vocabulary perception and grounding (SPLIT-OUT, new lane).** Contract: arbitrary
  language-referred concept → localized prediction (box/mask/coordinates). Lineage, each step
  technically distinct: phrase grounding (Flickr30k Entities, 2015) → referring-expression
  comprehension (RefCOCO/+/g, 2016, arXiv:1606.03825) → OVR-CNN (first open-vocabulary detection
  concept) → ViLD (CLIP-distillation into detector) → RegionCLIP/Detic (pseudo-label/weak-supervision
  variants) → GLIP (arXiv:2112.03857, detection reformulated as phrase grounding, GoldG grounding
  data) → OWL-ViT (arXiv:2205.06230, minimal heads on frozen CLIP) → Grounding DINO
  (arXiv:2303.05499, tight fusion + detection/REC unification, 52.5 COCO zero-shot AP) → OWLv2/OWL-ST
  (NeurIPS 2023, web-scale self-training to 1B+ examples, LVIS-rare 44.6%) → YOLO-World (GLIP
  formulation in YOLO). Open-vocabulary segmentation branch: LSeg → OpenSeg → ODISE → X-Decoder →
  SAM+CLIP combinations (place here, cross-ref D03). Evaluation: LVIS-rare AP, ODinW, RefCOCO/+/g —
  none interchangeable with D07A metrics. Consumers: D10 visual-evidence attribution, D12 element
  grounding, D13 language-conditioned policies. **This is the actionable-grounding substrate of the
  entire Tier B; burying it inside D07A hides the volume's load path.**
- **Why a title patch is not enough (Sol skeleton says X, evidence suggests Y).** A shared title
  forces one evaluation section, one data section, one "limitation" section for two contracts whose
  metrics, data, and failure modes do not overlap (bag-of-words alignment limits vs region-word
  correspondence noise). The surveys found in reconnaissance (OVD/OVS survey arXiv:2307.09220;
  open-vocabulary learning survey arXiv:2306.15880; open-world detection survey arXiv:2508.16527)
  all treat these as a standalone research program — supporting, not proving, lane status.
  Secondary surveys are taxonomic witnesses only (CV2-DM-020: survey existence ≠ mechanism proof).
- **Evidence density.** HIGH for both halves.
- **Source-access risk.** LOW (all open; code for GLIP/Grounding DINO/OWL-ViT open).
- **TS-001/002 overlap.** D07A: TS-002 partial (conditioning angle) → reuse-by-reference. D07B:
  TS-002 absent; TS-001 absent → full-new-treatment.
- **Current-case candidates.** Qwen3-VL grounding evals (EVALUATION_CASE); YOLO-World / Grounding
  DINO checkpoints (ARCHITECTURE_CASE, open).
- **Open questions.** D-numbering: D07A/D07B sub-lettering (recommended — avoids renumbering churn)
  vs new D16. Sol Round C to decide; content identical either way.

### D08 — Bridging pretrained vision and language models — `KEEP`

- **Technical rationale.** Frozen-encoder + frozen-LLM bridging (projector/resampler/Q-Former/
  cross-attention) vs joint training is the volume's cleanest efficiency/design-tradeoff node and the
  direct ancestor of the D09 native-vs-modular debate. Flamingo (few-shot, gated cross-attention),
  BLIP-2 (frozen–frozen + Q-Former), LLaVA (vision encoder + LLM + visual instruction tuning) are
  three genuinely different answers, not a chronology.
- **Candidate primary sources.** Flamingo (arXiv:2204.14198); BLIP-2 (arXiv:2301.12597); LLaVA
  (arXiv:2304.08485); InstructBLIP (arXiv:2305.06500, **missing node in Sol map** — the
  instruction-tuning bridge between BLIP-2 and LLaVA); MiniGPT-4 (arXiv:2304.10592, same bridge
  function, open); Frozen (arXiv:2106.13884, 2021 precursor, one-line context).
- **Missing lineage nodes.** InstructBLIP + MiniGPT-4 (above) — without them LLaVA's instruction
  tuning appears abrupt. This is a genuine predecessor gap in the Sol anchor map.
- **Competing interpretation.** "Bridging is a stepping stone to native models" vs "bridging is a
  durable deployment optimum (frozen-component reuse)". Qwen3-VL's continued three-module
  vision-encoder + merger + LLM architecture (arXiv:2511.21631) is 2026 evidence that modular
  bridging persists at frontier scale — the volume must not narrate it as obsolete.
- **Evidence density.** HIGH.
- **Source-access risk.** LOW.
- **TS-001/002 overlap.** TS-001: partial (frozen-component compute tradeoff — reuse vocabulary by
  reference). TS-002: absent. Disposition: full-new-treatment.
- **Current-case candidates.** Qwen3-VL three-module stack as ARCHITECTURE_CASE for durable
  modularity (open weights + report).
- **Open questions.** None structural.

### D09 — Native/omni fusion, tokenization, context economics — `KEEP + REWEIGHT (upward) + ADD (audio-input sub-lane checklist)`

- **Technical rationale.** This lane carries the volume's second core question ("what representation
  suffices for the next computation?") in its most measurable form: tokens/image, resolution policy,
  resampling/pruning, fusion depth, KV/memory cost. 2026 evidence (Qwen3-VL DeepStack multi-level ViT
  features, interleaved-MRoPE, 256K interleaved context with staged S0–S3 recipe and token budgets;
  Qwen3-Omni TM-RoPE absolute-time 80ms alignment, Thinker–Talker MoE, 234ms first-packet latency)
  makes this the densest mechanism lane in Tier A. It also absorbs Challenge C's bounded audio scope.
- **Candidate primary sources.** Qwen2.5-VL (arXiv:2502.13923, M-RoPE/dynamic-resolution predecessor);
  Qwen3-VL (arXiv:2511.21631, DeepStack + interleaved-MRoPE + text-timestamp alignment + 4-stage
  recipe); Qwen3-Omni (arXiv:2509.17765, Thinker–Talker MoE + TM-RoPE + audio encoder from scratch on
  20M hours); Whisper (arXiv:2212.04356, audio-input encoder predecessor — understanding side only);
  CLAP (audio-language alignment parallel to CLIP — predecessor node, verify exact citation in
  Round D); Gemini 3.1 Pro model card (2026-02-19, closed native-multimodal CAPABILITY_CASE +
  1M-context DEPLOYMENT_CASE; no architecture authority).
- **Missing lineage nodes.** Audio-input encoder history (AudioSet 2017 as data predecessor; Whisper;
  CLAP) — bounded to input/fusion relevance; Flamingo Perceiver-Resampler as resampling predecessor
  (cross-ref D08, not duplicated).
- **Competing interpretation.** "Native unified backbone" vs "specialist encoders + merger" (Qwen3
  family demonstrates both coexisting: unified Omni vs modular VL). The volume's convergence chapter
  must present this as an open engineering tradeoff with 2026 evidence on both sides — not a march
  toward unity.
- **Evidence density.** HIGH (Qwen reports unusually mechanism-rich for 2026 first-party work).
- **Source-access risk.** MEDIUM: Qwen reports + Apache-2.0 weights are open; Gemini-side fusion
  details are undisclosed (CAPABILITY_CASE only — marketing pages must not source architecture
  claims, CV2-DM-020).
- **TS-001/002 overlap.** TS-001: partial-but-structural (token/memory/latency economics — reuse
  TS-001 measurement vocabulary, add multimodal-specific fields; do not retell MoE/quantization).
  TS-002: partial (shared tokenizers/codecs where load-bearing — cross-reference). Disposition:
  expand-from-new-angle (fusion/representation angle is TS-003-native).
- **Current-case candidates.** Qwen3-VL-235B-A22B (ARCHITECTURE_CASE + DEPLOYMENT_CASE, open);
  Qwen3-Omni-30B-A3B (ARCHITECTURE_CASE for omni fusion + streaming, Apache 2.0);
  Qwen3-VL-Embedding/Reranker (arXiv:2601.04720, retrieval-reuse case — supports D05 sub-lane);
  Gemini 3.x (CAPABILITY_CASE + EVALUATION_CASE only).
- **Open questions.** Exact visual-token accounting comparability across vendors (tokens/image claims
  are config-dependent — CV2-DM-020: never tabulate without config binding).

### D10 — Multimodal reasoning / failure decomposition — `KEEP`

- **Technical rationale.** The anti-leaderboard lane: per-capability decomposition (recognition, OCR,
  counting, spatial, charts, multi-image, compositional, hallucination, evidence localization) with
  language-prior vs visual-evidence-use separation is what makes D15 evaluation honest. Without D10's
  taxonomy, benchmark scores revert to "general vision intelligence" numerology.
- **Candidate primary sources.** MMMU (arXiv:2311.16502); MMMU-Pro (Gemini 3.1 Pro card context,
  80.5–81.0 range as vendor claim — EVALUATION_CASE only); MathVista/MathVision (visual-math;
  verify citations Round D); POPE (arXiv:2305.10355, hallucination polling); HallusionBench
  (verify citation Round D); MMBench (arXiv:2307.06281, verify).
- **Missing lineage nodes.** Chart/figure-specialist evals; multi-image-comparison evals; visual
  chain-of-thought/tool-use scaffolds (Gemini 3 "visual thinking via code execution" as 2026
  tool-assisted-perception case — CAPABILITY_CASE).
- **Competing interpretation.** "Reasoning elicitation (CoT/scaffold)" vs "perceptual grounding
  improvement" as rival explanations for benchmark gains — the volume must keep both explanations
  live per benchmark (X04 obligation).
- **Evidence density.** MEDIUM (benchmark papers open; contamination/language-prior analyses thinner
  and scattered — partial EVIDENCE_GAP, methodology-first collection needed in Discovery).
- **Source-access risk.** LOW for papers; MEDIUM for vendor eval methodology pages (version drift).
- **TS-001/002 overlap.** TS-001: absent. TS-002: absent (generation evals are a different contract).
  Disposition: full-new-treatment.
- **Current-case candidates.** Thinking-vs-non-thinking VLM variants (Qwen3-VL bifurcated
  post-training) as reasoning-scaffold ARCHITECTURE_CASE.
- **Open questions.** Contamination-honest reporting standard for 2026 closed-model scores (D15 owns).

### D11 — Video understanding / temporal memory / event grounding — `KEEP + ADD (audio-video joint checklist)`

- **Technical rationale.** Frame-repeat vs genuine temporal modeling (action recognition → event
  localization → ordering → causal/physical → long-video memory/retrieval → streaming) is the
  temporal half of the volume's state thesis; D09 handles fusion mechanics, D11 handles temporal
  semantics. TS-002 generated video; TS-003 asks what state persists across frames.
- **Candidate primary sources.** Kinetics (arXiv:1705.06950, action-recognition predecessor);
  Something-Something V2 (arXiv:1706.04261, temporal-ordering-sensitive predecessor); Ego4D
  (arXiv:2110.07058, egocentric + audio-visual + trajectory-adjacent data predecessor);
  Video-MME (arXiv:2405.21075, verify); LongVideoBench (arXiv:2407.15754, verify); SAM 2
  (arXiv:2408.00714, streaming-memory architecture bridge from D03); Qwen3-VL text-timestamp
  alignment (temporal-grounding mechanism, cross-ref D09).
- **Missing lineage nodes.** Online/streaming video understanding (low-density — LOW_YIELD risk;
  StreamChat-class systems to be scoped in Round D, not assumed); audio-video joint understanding
  where audio is load-bearing (Qwen3-Omni AV benchmarks as EVALUATION_CASE).
- **Competing interpretation.** "Longer context window = longer understanding" vs "retrieval +
  hierarchical memory = understanding" — Qwen3-VL's 256K-native vs agent-memory approaches; keep
  both, adjudicate via long-video evals (D15).
- **Evidence density.** MEDIUM (short-video HIGH; long-video/streaming MEDIUM-LOW).
- **Source-access risk.** LOW-MEDIUM.
- **TS-001/002 overlap.** TS-001: partial (long-context memory economics — reuse by reference).
  TS-002: partial (video generation lineage — clean question-split: generated vs observed; extensive
  cross-referencing, no retelling). Disposition: expand-from-new-angle.
- **Current-case candidates.** A long-video/streaming-capable open system (verify Round D);
  Video-MMMU (Gemini 3 context: 87.6% vendor claim) as EVALUATION_CASE with vendor attribution.
- **Open questions.** Whether streaming deserves a named sub-lane or a D15-future-work pointer.
  Recommendation: sub-lane stub + explicit LOW_YIELD-or-fill verdict in Round D.

### D12 — GUI / Computer Use — `KEEP + REWEIGHT (reframe around OSWorld 1.0 → 2.0)`

- **Technical rationale.** The digital-action bridge (screenshot parsing → element grounding →
  coordinate/action prediction → closed-loop state). **Reconnaissance finding that moves the thesis:**
  OSWorld 2.0 (arXiv:2606.29537, June 2026, 108 tasks, median 1.6 human-hours, ~318 tool calls vs
  ~30 in 1.0) shows frontier failure moved UP the stack: from GUI grounding/operational knowledge
  (OSWorld 1.0: best 12.24% vs human 72.36%) to constraint-tracking, mid-task information arrival,
  implicit-state inference, and verification skipping (2.0: best 20.6% binary / 54.8% partial).
  Basic GUI control is no longer the binding constraint; task-level state persistence is. D12's
  center of gravity must shift from "can it click?" to "can it hold a task model across 300 steps?".
- **Candidate primary sources.** OSWorld (arXiv:2404.07972, NeurIPS 2024); OSWorld 2.0
  (arXiv:2606.29537 — **new anchor absent from Sol map, add**); ScreenSpot-class element-grounding
  evals (verify Round D); Set-of-Mark prompting (as grounding-scaffold technique, verify);
  Gemini 2.5 Computer Use (via Gemini 3 launch blog 2025-11-18, DEPLOYMENT_CASE pointer only);
  Claude computer-use / Operator-class systems as DEPLOYMENT_CASE pointers (verify exact 2026
  authority in Round D — no architecture claims from product pages).
- **Missing lineage nodes.** Pre-OSWorld GUI grounding (SeeClick/Mind2Web-class web-agent lineage —
  verify and bound: web-phase vs OS-phase distinction matters); accessibility-tree/DOM vs pure-vision
  interface-contract debate (X02 content, surfaced here).
- **Competing interpretation.** "Pure-vision screenshots suffice" vs "a11y-tree/DOM/MCP tool
  invocation is the durable interface" (OSWorld-MCP exists; OSWorld 2.0 agents split programmatic vs
  GUI actions ~37/37). The volume must present the interface-contract fork, not pick a winner.
- **Evidence density.** HIGH for benchmarks; MEDIUM for vendor computer-use stacks (deployment facts
  open, mechanisms closed).
- **Source-access risk.** MEDIUM (vendor stacks: capability/deployment facts only).
- **TS-001/002 overlap.** TS-001: partial (screenshot-loop token/latency costs — reuse economics
  vocabulary). TS-002: absent. Disposition: full-new-treatment.
- **Current-case candidates.** OSWorld 2.0 leaderboard slice (EVALUATION_CASE with exact
  model/thinking-budget/step-budget binding); a computer-use deployment stack (DEPLOYMENT_CASE).
- **Open questions.** Safety/audit reporting (OSWorld 2.0 safety reports) — include only as
  evaluation-metadata, not a policy chapter (§J).

### D13 — VLA / embodied multimodal systems — `KEEP + REWEIGHT (endpoint cap, refusal list)`

- **Technical rationale.** Perception→motor representation transfer (action tokenization, policy-vs-
  reasoning split, web-scale VL pretraining transfer, multi-embodiment generalization, closed-loop
  latency) is the physical-action endpoint the volume promises. But the lane borders control theory,
  locomotion, and manipulation hardware — all out of scope. The lane's TS-003 content is the
  *representation contract across the vision-language-action boundary*, nothing deeper into physics.
- **Candidate primary sources.** RT-1 (arXiv:2212.06817, direct predecessor); RT-2
  (arXiv:2307.15818, VLA formulation: actions-as-text-tokens, co-fine-tuning); OpenVLA
  (arXiv:2406.09246, open ARCHITECTURE_CASE); Open X-Embodiment (arXiv:2310.08864, **data
  predecessor missing from Sol map — add**, supports X01); SayCan (2022, planning-grounding
  predecessor, verify citation Round D); PaLM-E (arXiv:2303.03378, **embodied-multimodal-LM
  predecessor missing from Sol map — add**); Gemini Robotics 2 + On-Device 2 (2026-07-30 model
  pages/cards: whole-body humanoid + <200-example adaptation + trusted-tester distribution —
  CAPABILITY_CASE + EVALUATION_CASE + DEPLOYMENT_CASE; NOT architecture authority); Gemini
  Robotics ER 2 (reasoning/policy split case, capability-level only).
- **Missing lineage nodes.** SayCan, PaLM-E, Open X-Embodiment (above) — without them RT-2 appears
  abrupt, which is exactly the "RT-2から突然始めない" failure the brief prohibits. Sol map has RT-1
  only; three additions required.
- **Competing interpretation.** "VLA = VLM + action head" (RT-2 framing) vs "VLA = policy with
  VL-initialized perception" (controls-side framing) vs "planner–policy split (ER + VLA)" (Gemini
  Robotics 2 stack framing). All three are live in 2026 sources; the volume must carry the
  three-way split — it determines what "multimodal understanding" even means for action.
- **Evidence density.** MEDIUM-HIGH (papers open; frontier vendor mechanisms closed; independent
  evals thin — partial EVIDENCE_GAP on independent VLA eval).
- **Source-access risk.** MEDIUM-HIGH (Gemini Robotics distribution is trusted-tester/private-preview;
  no downloadable checkpoints; latency/price/token facts unpublished).
- **TS-001/002 overlap.** TS-001: partial (edge latency/on-device constraints — On-Device 2 is the
  TS-001-vocabulary showcase; reuse by reference). TS-002: absent. Disposition: full-new-treatment
  within cap.
- **Current-case candidates.** OpenVLA (ARCHITECTURE_CASE); Gemini Robotics On-Device 2
  (DEPLOYMENT_CASE + EVALUATION_CASE with model-card scope limits quoted: bi-arm-primary,
  high-DoF limits); RT-2 (historical ARCHITECTURE_CASE).
- **Open questions.** Exact refusal list for Round E contract: no kinematics/dynamics expositions, no
  locomotion-gait content beyond embodiment-adaptation facts, no manipulation-hardware surveys.

### D14 — Predictive representations / World Models — `KEEP + REWEIGHT (terminology-split mandatory, non-generative counterweight)`

- **Technical rationale.** The term "world model" currently denotes at least four different objects
  (latent dynamics for planning; predictive representation learning; generative interactive
  environment; action-conditioned simulator for training/evaluation). Sol's seven-way non-synonym
  list is confirmed correct and must be enforced as lane structure, not preamble.
- **Candidate primary sources.** Ha & Schmidhuber, *World Models* (arXiv:1803.10122, terminological
  origin — NOT technical ancestor of Genie; see correction §G.5); PlaNet/Dreamer
  (arXiv:1912.01603) → DreamerV3 (arXiv:2301.04104, latent-dynamics planning line); I-JEPA
  (arXiv:2301.08243) / V-JEPA-class (predictive-representation competing interpretation — verify
  exact V-JEPA citation Round D); Genie (arXiv:2402.15391); Genie 2 (DeepMind page, vendor
  CAPABILITY_CASE); **Genie 3 (Aug 2025 blog + model page; Jan 2026 Project Genie prototype —
  new current anchor absent from Sol map in this form: real-time 24fps/720p, ~1-min visual memory,
  few-minutes consistency, promptable world events, SIMA-agent training use, limited action space,
  60s prototype cap)**; Waymo World Model (Genie-3-derived applied variant — DEPLOYMENT_CASE
  pointer, verify primary source Round D).
- **Missing lineage nodes.** Model-based-RL dynamics lineage (one-line context: PILCO/PlaNet minimum);
  JEPA line (above);-pane world-model-for-robotics evaluation uses (SIMA-in-Genie-3 as
  training/evaluation-use case — the "used for planning/training, not just generation" discriminator).
- **Competing interpretation.** "World model = interactive generative video" (Genie framing) vs
  "world model = latent dynamics for decision-making" (Dreamer framing) vs "world model =
  predictive representation without generation" (JEPA framing). The lane's central deliverable is
  keeping these three from collapsing — with the action-conditioning + planning-use test as the
  adjudicator (Sol's six questions, confirmed).
- **Evidence density.** MEDIUM (papers open; Genie-3 internals undisclosed; independent eval of
  "dynamics usability" vs "visual realism" thin — EVIDENCE_GAP on control-oriented world-model
  measures).
- **Source-access risk.** MEDIUM-HIGH (Genie 3: no paper, no weights; vendor blog + prototype only).
- **TS-001/002 overlap.** TS-001: absent (except autoregressive rollout compute — negligible).
  TS-002: partial-and-delicate (shared video-generation machinery; the question-split —
  state/counterfactual/action vs visual realism — must be enforced per-paragraph, else D14 dissolves
  into TS-002 retelling). Disposition: expand-from-new-angle with strict boundary policing.
- **Current-case candidates.** Genie 3 (CAPABILITY_CASE + DEPLOYMENT_CASE-pointer; explicitly NOT
  ARCHITECTURE_CASE); DreamerV3 (ARCHITECTURE_CASE, open); Waymo World Model (DEPLOYMENT_CASE);
  V-JEPA-class (ARCHITECTURE_CASE for the non-generative pole, pending verification).
- **Open questions.** Whether "planning-use" evaluations (SIMA success, rollout-based planning gains)
  can be sourced independently of vendor blogs — likely EVIDENCE_GAP; record as such rather than
  promoting vendor claims.

### D15 — Evaluation / robustness / provenance / convergence — `KEEP (full lane, methodology-first)`

- **Technical rationale.** Confirmed as full lane: without it, D10's decomposition has nowhere to
  land and Tier B endpoints get scored on borrowed metrics. The Sol authority list (classification
  accuracy → robot success → world-model control-oriented measures + multimodal benchmark metadata
  preservation) is the right shape; reconnaissance adds 2026 updates (below) and a structural demand:
  **no cross-task-family ranking tables** (brief §12 prohibition — enforce in Round E contract).
- **Candidate primary sources.** Per-family methodology papers (see evaluation map §I for the full
  matrix); OSWorld 2.0 (§D12 — includes cost-aware + safety-audit methodology, a 2026 evaluation
  practice worth generalizing); MMEB-V2 (retrieval-eval methodology via Qwen3-VL-Embedding report,
  arXiv:2601.04720); LVIS/ODinW/RefCOCO (D07B grounding evals); Video-MMMU/LongVideoBench/Video-MME
  (video evals, verify); POPE/HallusionBench (hallucination evals, verify HallusionBench).
- **Missing lineage nodes.** Classical metric papers where load-bearing (mAP/IoU definitions as cited
  context, not mechanism); human-preference-protocol methodology (TS-002-adjacent — cross-ref, and
  note TS-002's evaluator/judge-dependence lessons apply directly).
- **Competing interpretation.** "Benchmark score as capability measure" vs "benchmark score as
  scaffold+data+judge artifact" — D15 must institutionalize the second reading per score (X04).
- **Evidence density.** MEDIUM (methodology papers open; contamination analyses and judge-dependence
  studies scattered — targeted Discovery required).
- **Source-access risk.** LOW-MEDIUM (vendor eval pages drift; bind version+date per CV2-DM-013).
- **TS-001/002 overlap.** TS-001: partial (benchmark-methodology lane precedent — reuse the
  condition-binding discipline verbatim). TS-002: partial (eval-provenance norms: FID/MOS/VBench
  lessons transfer; media-fidelity metrics stay in TS-002). Disposition: expand-from-new-angle.
- **Current-case candidates.** OSWorld 2.0 cost/token-horizon analysis as cross-lane evaluation
  practice exemplar (EVALUATION_CASE).
- **Open questions.** Convergence-subsection placement: end-of-D15 synthesis (recommended) vs
  standalone closing chapter (Round C choice; content identical).

---

## C. X01–X04 audit

### X01 — Data / supervision / post-training — `KEEP cross-cutting + REWEIGHT (upward, with teeth)`

- **Verdict: cross-cutting axis suffices; lane promotion refused (Challenge B).** The supervision
  progression (hand-labelled → large supervised → self-supervised → image-text pairs → interleaved
  documents → visual instruction tuning → synthetic multimodal → preference/post-training → action
  trajectories) is confirmed load-bearing: Qwen3-VL's staged recipe (67B alignment → ~1T
  multimodal → ~1T long-context → 100B ultra-long-context, with sqrt-reweighting to protect text)
  and OWL-ST's 1B-example self-training scaling are 2026 demonstrations that data/supervision
  decisions move results as much as backbones. But a standalone data lane would (a) duplicate every
  D-lane's training subsection, (b) decay into the dataset catalogue Sol already prohibits, and
  (c) separate supervision from the objectives it co-defines (X02). The failure mode "architecture
 史だけで組む" is real, but the cure is mandatory per-lane data-contract blocks, not a new chapter.
- **Required shape (proposal for Round C/E contract).** Every D-lane reports, where applicable: data
  type/scale, supervision type, paired-vs-interleaved structure, human/web/synthetic provenance,
  pretrain/SFT/preference/action-trajectory stage, multilingual coverage when material, known
  authority limits. Plus ONE Tier C synthesis: a supervision-contract timeline figure/table
  (the eight-stage progression above with representative systems per stage) placed in D15/convergence
  or as an X-synthesis appendix — a single shared artifact instead of fifteen repeated histories.
- **Missing anchor to add:** interleaved-data representatives (OBELISC/MMC4-class — verify exact
  citations Round D); visual-instruction-tuning data (LLaVA-Instruct); synthetic-multimodal-data
  practice (ALLaVA-class — verify); preference/post-training for VLMs (RLHF-V/RLAIF-V-class —
  verify); action-trajectory data (Open X-Embodiment, Ego4D). These are currently the thinnest part
  of X01 — targeted Round D fill, not Round B scope failure.

### X02 — Objective / interface contract — `KEEP`

- Correctly scoped: architecture≠objective separation is the TS-002-proven discipline (backbone vs
  objective vs sampler) transplanted to understanding-side contracts (contrastive vs captioning vs
  next-token multimodal vs instruction-tuning vs preference/RL vs action-prediction vs predictive
  world-model objectives). No change proposed. One addition: D12's interface fork (screenshot-action
  vs a11y/DOM/MCP invocation) and D13's planner–policy split should be explicitly named as X02
  instances in the Round E contract so they are not treated as product trivia.

### X03 — Efficiency / token / memory / latency economics — `KEEP`

- Correctly scoped as TS-001-vocabulary reuse with multimodal-only fields (tokens/image-frame,
  resolution/tiling policy, resampler/pruning, long-video KV impact, screenshot-loop costs,
  on-device VLA latency, streaming constraints). Qwen3-Omni's 234ms first-packet latency, Genie 3's
  real-time rollout compute, and OSWorld 2.0's token-vs-completion cost curves are 2026-native X03
  exhibits. Warning (CV2-DM-020): vendor latency/token figures are config-bound claims — bind
  config or do not tabulate. No generic MoE/quantization retelling (TS-001 owns).

### X04 — Reliability / source fidelity / claim strength — `KEEP`

- Correctly scoped and load-bearing for the volume's credibility: hallucination/unsupported-claim
  tracking, language-prior-vs-evidence-use separation, modality-conflict, grounding correctness,
  contamination/judge-dependence, and per-claim source-role preservation (CV2-DM-020 as production
  QA, not just planning hygiene). One addition for Round E: the closed-model four-role tagging
  (CAPABILITY/ARCHITECTURE/DEPLOYMENT/EVALUATION) used in this report's capstone section should
  become the production tagging rule — §H demonstrates the practice.

### No mandatory X addition

- Considered and refused: X05 "modality-synchronization/streaming contract" (fold into D09/D11
  checklists — too narrow for an axis); X06 "multilingual/multi-domain" (per-lane field inside X01
  suffices); X07 "safety/policy" (out of scope per §J — technical safety only where load-bearing in
  D12/D13/D15). Verdict: **NO_MANDATORY_X_ADDITION**.

---

## D. Missing dimensions

No new top-level D-number beyond the D07 SPLIT is mandated. Bounded additions (sub-lane or checklist
level, not new lanes):

1. **[SPLIT, structural] D07B open-vocabulary perception & grounding** — §B-D07. The only
   taxonomy-level addition. Implement as D07A/D07B sub-lettering (recommended) or D16; Sol Round C
   decides numbering, content is fixed either way.
2. **[ADD, sub-lane] Multimodal retrieval & embedding reuse under D05** — Qwen3-VL-Embedding/
   Reranker (arXiv:2601.04720, MMEB-V2 77.8 SOTA Jan 2026) shows VLM-backbone retrieval is now a
   first-class interface (document RAG, video search, agent memory). Sol audit parked retrieval as
   "capability under D05/D07/D10". Reconnaissance upgrades the parking spot to an explicit named
   sub-lane (not a lane): retrieval objective, Matryoshka/quantization-aware deployment traits,
   cross-ref D09 encoder reuse. Low collection cost, real interface coverage.
3. **[ADD, checklist] Audio-input-understanding scope items in D09/D11** — §Challenge C verdict:
   audio-input encoder lineage (AudioSet → Whisper → CLAP → omni audio encoders), heterogeneous
   rate handling, absolute-time alignment (TM-RoPE-class), streaming interaction. Checklist-level;
   any full audio-history treatment is refused (§J).
4. **[ADD, nodes] Named predecessor insertions** — InstructBLIP/MiniGPT-4 (D08), SayCan/PaLM-E/
   Open X-Embodiment (D13), OVR-CNN/ViLD/Detic/RegionCLIP/OWL-ST (D07B), DeViSE/captioning/VQA
   predecessors (D07A), DINO detector (D02), SAM 2 video bridge (D03→D11), Genie 3 current anchor
   + JEPA/Dreamer counterweights (D14), OSWorld 2.0 (D12). All within existing lanes.

If Sol prefers a strict reading, items 2–4 are scope clarifications, and the verdict can be recorded
as: **one structural split (D07), zero additional top-level lanes.**

---

## E. Over-scoped dimensions (cap, don't cut)

1. **D04 geometry/3D** — highest escape gradient toward SLAM/NeRF/3DGS textbook. Cap: named node
   allow-list (2–4 mechanisms) + support weight (§K.5). Refuse: full reconstruction history,
   classical SLAM/control expositions.
2. **D13 VLA** — second-highest escape gradient (locomotion, control theory, manipulation hardware).
   Cap: representation-contract boundary (§B-D13 refusal list) + endpoint weight. Refuse: kinematics/
   dynamics, gait/locomotion content beyond embodiment-adaptation facts, hardware surveys.
3. **D14 world models** — escape gradient toward model-based-RL encyclopedia and video-generation
   retelling. Cap: terminology-split structure as the lane skeleton + TS-002 boundary policing
   per-paragraph. Refuse: full RL history, photorealism-chronology writing.
4. **D01 pre-deep history** — escape gradient toward CV textbook. Cap: ≤2-page-equivalent context
   weight. Refuse: handcrafted-feature mechanism expositions.
5. **D12 agent benchmarks** — catalogue gradient (every new computer-use benchmark is not a new
   finding). Cap: OSWorld-lineage spine + interface-contract debate; new benchmarks enter only via
   D15 methodology merit, not vendor novelty.
6. **D09 omni scope** — generation-side creep gradient (speech/music synthesis detail belongs to
   TS-002). Cap: Challenge C checklist (§B-D09); any synthesis-mechanism exposition is refused and
   referred to TS-002.

---

## F. TS-001 / TS-002 overlap matrix

Legend — TS-001/TS-002 status: `covered / partial / absent`. TS-003 disposition:
`reuse-by-reference / expand-from-new-angle / full-new-treatment`.

| # | Topic | TS-001 (Efficient LLM) | TS-002 (Beyond Text) | TS-003 disposition |
|---|---|---|---|---|
| 1 | Transformer / attention | covered (bottleneck contract, MHA→GQA/MLA/FlashAttention/linear hybrids) | partial (backbone where relevant) | reuse-by-reference; new only for visual-token fusion use (D06/D09) |
| 2 | ViT | partial (token-efficiency angle only) | partial (generation backbone where load-bearing) | expand-from-new-angle: visual representation/ token-formulation history (D06) |
| 3 | CLIP | partial (deployment/compute only if material) | partial (conditioning/alignment machinery) | expand-from-new-angle: addressability transition D07A; reuse conditioning angle by reference |
| 4 | VAE / tokenizer | partial (memory/compute only) | covered (representation-shortening spine: VAE→VQ→RVQ→semantic/acoustic→spatiotemporal) | reuse-by-reference; new only for understanding-side token budgets (D09) |
| 5 | Multimodal tokenization | partial (cost lens) | covered (compression lens for generation) | expand-from-new-angle: fusion/grounding/state lens (D09) — same objects, different question |
| 6 | Video | partial (context/runtime lens) | covered (generation, motion, temporal consistency) | expand-from-new-angle: observed-video understanding/memory/grounding (D11); strict generated-vs-observed split |
| 7 | Audio | absent (except runtime where material) | covered (speech/music generation history) | expand-from-new-angle, bounded: input-understanding/fusion/reasoning only (D09/D11 checklist); generation stays in TS-002 |
| 8 | Quantization | covered (core subject: PTQ/QAT, KV, GGUF-as-format discipline) | partial (deployment where material) | reuse-by-reference; new only for VLM/VLA edge-perception constraints (X03 fields) |
| 9 | Context length | covered (KV/efficiency lens) | partial (long-generation lens) | reuse-by-reference; new only for interleaved multimodal context + temporal memory (D09/D11) |
| 10 | Token compression | covered (pruning/sparse lens) | partial (codec/compression lens) | expand-from-new-angle: resampling/pruning for perception-fusion economics (D09) |
| 11 | Long-context memory | covered (cache/systems lens) | partial (state-across-chunks lens for generation) | expand-from-new-angle: temporal/event state across observed frames (D11) |
| 12 | Runtime / latency | covered (serving/decoding/inference lens) | covered (sampling-steps/realtime-factor lens) | reuse-by-reference both; new only for perception-action loops, screenshot-loop and on-device VLA costs (D12/D13 via X03) |
| 13 | Evaluation | covered (methodology lane precedent: condition-binding, no cross-condition ranking) | covered (fidelity/alignment/structure/temporality/preference + provenance mechanisms) | expand-from-new-angle: understanding-side task identities + grounding/spatial/agentic/robot/world-model measures (D15); import both volumes' condition-binding discipline verbatim |
| 14 | World model | partial (efficiency only if material) | partial (generated/simulated world as media) | expand-from-new-angle: predictive/action-conditioned state + planning-use test (D14); shared machinery cross-referenced, never retold |
| 15 | Agent / action | partial (routing/specialization-instead-of-generation: Jev-type; serving/scheduling) | partial (agentic workflows around generation/editing) | full-new-treatment of perception-grounded action: GUI grounding→action→state (D12), VL→motor transfer (D13); TS-001/002 agent content reused by reference only |

Boundary rules carried forward (Sol skeleton §5, confirmed): TS-002 owns "what is generated, by
what mechanism"; TS-003 owns "what is perceived, represented, aligned, grounded, reasoned about,
predicted, acted upon"; TS-001 owns "how compute/memory/latency/cost is reduced or scheduled".
Generation appears in TS-003 only as reasoning/prediction/simulation component with cross-reference;
efficiency appears only through multimodal-specific consequences with TS-001 vocabulary reuse.

---

## G. Historical lineage corrections

G.1 **Pre-AlexNet context (D01).** Sol skeleton/map is correct to start at AlexNet but abrupt without
one-paragraph Neocognitron/LeNet context. Correction: ADD concise predecessor context (no mechanism
depth). Risk if omitted: "CNN suddenly appeared in 2012" reading. Low cost, do it.

G.2 **Pre-CLIP vision-language (D07A).** Starting at CLIP repeats the abruptness error one level up.
Correction: ADD DeViSE (2013) → captioning (Show and Tell 2014) → VQA (2015) predecessor chain so
CLIP reads as the *web-scale + zero-shot-transfer* break, not the invention of image–text learning.
Sol audit §10 already orders this; reconnaissance confirms the exact nodes.

G.3 **DINO name collision (D02/D06/D07B).** "DINO" denotes Caron et al. self-supervised ViT (D06
predecessor of DINOv2) AND Zhang et al. DINO detector (D02 successor, Grounding DINO base). The Sol
map names neither explicitly enough to prevent confusion. Correction: always-qualified references
("DINO self-supervised" vs "DINO detector") as a production terminology rule (CV2-DM-006 class).

G.4 **BLIP-2 → LLaVA gap (D08).** Sol anchor map jumps bridge generations. Correction: INSERT
InstructBLIP + MiniGPT-4 as the instruction-tuning bridge nodes. Without them, visual instruction
tuning (an X01-stage in its own right) has no mechanism ancestry.

G.5 **Genie ≠ descendant of Ha & Schmidhuber (D14). FALSE-DIRECT-ANCESTRY RISK.** *World Models*
(2018) is the terminological origin but NOT the technical ancestor of the Genie line (video-diffusion
/ spatiotemporal-Transformer interactive generation). Presenting Genie as the culmination of the
Ha-lineage is historically misleading; the relationship is terminological convergence, and the
Dreamer line (latent dynamics for planning) is the actual technical continuation of model-based
prediction. Correction: D14 must narrate three poles (generative-interactive / latent-dynamics /
predictive-representation) with explicit non-ancestry statements, not a single chain.

G.6 **RT-2 abruptness (D13).** Sol map lists RT-1 → RT-2 only. Correction: ADD SayCan (grounding
language plans in affordances), PaLM-E (embodied multimodal LM — the direct "VLM into body"
predecessor), and Open X-Embodiment (the data contract that made transfer-scale possible). RT-2 then
reads as convergence, not miracle.

G.7 **Grounding lineage missing middle (D07B).** Sol audit names OWL-ViT + GLIP/Grounding-DINO-class
but the connective tissue (OVR-CNN concept origin → ViLD CLIP-distillation → RegionCLIP/Detic
weak-supervision variants → GoldG grounding-data practice → OWL-ST web-scale self-training) is what
makes the six-stage boundary (§A.5-Challenge A) explicable. Correction: adopt the full chain in §B-D07B.

G.8 **SAM promptability predecessors (D03).** Interactive segmentation (DEXTR/RITM-class) one-line
context so SAM's "promptable" framing reads as systematization-at-scale (task+model+SA-1B), not
invention. Minor; low cost.

G.9 **OSWorld 1.0 → 2.0 succession (D12).** Sol map predates OSWorld 2.0 (June 2026). Correction:
ADD 2.0 as the current anchor and reframe the lane thesis (grounding bottleneck → state-management
bottleneck, §B-D12). This is the largest *current-anchor* correction in the report.

G.10 **Encoder-reuse lineage (D06→D09).** SigLIP → SigLIP2-So400m → Qwen3-VL/Qwen3-Omni vision
encoder is a 2026-load-bearing reuse fact ("which encoder, frozen or continued-trained, inside which
frontier VLM"). Correction: name SigLIP as D06 output node with a forward pointer to D09; verify
SigLIP2 citation exactness in Round D (currently secondary-confirmed via Qwen reports citing
"Tschannen et al., 2025").

G.11 **M-RoPE lineage (D09).** Qwen2-VL M-RoPE → Qwen2.5-VL extensions → Qwen3-VL interleaved-MRoPE +
text-timestamp alignment → Qwen3-Omni TM-RoPE (absolute-time 80ms IDs). A clean fusion-position-
encoding thread Sol does not name. Correction: adopt as D09's running example of "fusion is a
representation decision".

---

## H. Current capstone candidates (role-tagged)

Role vocabulary (proposed production rule, cf. §C-X04): `ARCHITECTURE_CASE` (mechanism authority) /
`CAPABILITY_CASE` (what it can do) / `DEPLOYMENT_CASE` (availability/runtime/lifecycle facts) /
`EVALUATION_CASE` (measured results with bound conditions). Closed-vendor entries are NEVER
architecture authority (CV2-DM-020).

1. **Native multimodal foundation.**
   - Qwen3-VL-235B-A22B (+ 30B-A3B / dense 2B–32B; report arXiv:2511.21631, Nov 2025; code + Apache
     weights): ARCHITECTURE_CASE (DeepStack, interleaved-MRoPE, 4-stage recipe) + DEPLOYMENT_CASE
     (open weights, FP8 variants) + EVALUATION_CASE (MMMU/visual-math/doc, vendor-measured).
     Strongest open inspectable foundation in class. Non-redundant vs TS-001/002 (fusion/reasoning
     angle is new). Limitation: vendor-measured benchmarks; independent reproduction pending.
   - Gemini 3.1 Pro / 3.6 Flash (model cards 2026-02-19 / 2026-07-21; 1M context; text/image/audio/
     video-in): CAPABILITY_CASE + EVALUATION_CASE (MMMU-Pro 80.5–81.0, Video-MMMU 87.6 — vendor
     claims with methodology pages) + DEPLOYMENT_CASE (API IDs/pricing). NOT architecture authority.
2. **Open / inspectable VLM.**
   - Qwen3-VL-8B/4B/2B dense + Thinking/non-thinking variants: ARCHITECTURE_CASE (same report;
     inspectable at consumer scale) + DEPLOYMENT_CASE (local execution, vLLM/Transformers support).
     Thinking bifurcation is D10's scaffold-vs-grounding exhibit.
   - Second open family for non-single-vendor dependence: TO VERIFY in Round D (small-VLM class;
     do not freeze a name without source-richness check). Recorded as fill-task, not gap.
3. **Document / UI understanding.**
   - Qwen3-VL doc/OCR/chart eval sections: EVALUATION_CASE (generalist pole of the specialist test).
   - Nougat-class specialist (arXiv:2308.13418): ARCHITECTURE_CASE candidate, MEDIUM confidence —
     verify role/currentness Round D. The specialist-vs-generalist comparison is the lane's payoff;
     do not let the generalist pole stand alone.
4. **Long-video / streaming.**
   - Qwen3-VL 256K interleaved context + text-timestamp grounding: ARCHITECTURE_CASE (temporal
     mechanism) + EVALUATION_CASE (long-video/doc evals).
   - Streaming-native system: LOW_YIELD in Round B (no source-rich candidate confirmed; SAM 2 memory
     design is an architecture pointer, not a system case). Explicit Round D fill-or-declare task.
5. **GUI / computer-use stack.**
   - OSWorld 2.0 slice (Claude Opus 4.8 max-thinking batched: 20.6% binary / 54.8% partial at 500
     steps; GPT-5.5 token-efficiency plateau ~13–14%): EVALUATION_CASE with full condition binding
     (model + thinking level + tool setting + step budget + release v2026.06.24).
   - Vendor computer-use deployment (Gemini 2.5 Computer Use / Claude computer-use / Operator-class):
     DEPLOYMENT_CASE pointers; exact 2026 authority to be bound in Round D. No mechanism claims.
6. **VLA / embodied.**
   - OpenVLA (arXiv:2406.09246): ARCHITECTURE_CASE (open weights/policy formulation).
   - Gemini Robotics 2 + On-Device 2 (2026-07-30; whole-body humanoid / <200-example adaptation /
     trusted-tester + private-preview distribution; bi-arm-primary eval scope with stated high-DoF
     limits): CAPABILITY_CASE + EVALUATION_CASE (card-scoped) + DEPLOYMENT_CASE (access terms).
     TS-001-crossover exhibit (on-device latency/connectivity constraints).
   - RT-2: historical ARCHITECTURE_CASE (VLA formulation origin).
7. **Action-conditioned world model.**
   - Genie 3 (Aug 2025 blog + model page; Project Genie Jan 2026): CAPABILITY_CASE (real-time
     24fps/720p, ~1-min memory, minutes-scale consistency, promptable events, SIMA training use) +
     DEPLOYMENT_CASE-pointer (research preview / Ultra-gated prototype, 60s cap). Explicitly NOT
     ARCHITECTURE_CASE (no paper/weights). Known limitations on record (limited agent action space,
     minutes-scale duration, no multi-agent reliability, non-georeferenced locales).
   - DreamerV3 (arXiv:2301.04104): ARCHITECTURE_CASE for the latent-dynamics pole (open).
   - Waymo World Model (Genie-3-derived): DEPLOYMENT_CASE pointer (verify primary source Round D).
   - V-JEPA-class: ARCHITECTURE_CASE candidate for the non-generative pole (verify citation Round D).

Selection discipline reminder for Round C: newest/famous/benchmark-leader alone select nothing;
each case above carries its technical-distinctiveness + source-richness + limitation rationale.

---

## I. Evaluation map (task identity preserved; no cross-family ranking)

Per family: measures / does-not-measure / metric-evaluator / contamination risk / language-prior
shortcut / source-version dependence / current relevance.

- **Image classification (ImageNet-1k top-1).** Measures: closed-set discriminative quality of a
  frozen/learned representation. Misses: localization, grounding, reasoning. Metric: top-1 accuracy
  (exact). Contamination: LOW (old, saturated — DINOv2 86.5% zero-shot cited as transfer probe, not
  frontier claim). Language-prior: N/A. Version: stable. Relevance: transfer-probe only.
- **Object detection (COCO mAP; LVIS-rare for OVD; ODinW).** Measures: closed-set (COCO) vs
  open-vocabulary generalization (LVIS-rare) vs in-the-wild robustness (ODinW). Misses: referring
  precision (see grounding), reasoning. Contamination: MEDIUM (web-scale pretraining may include
  test-adjacent images; OWL-ST's N-gram pseudo-labeling makes "unseen" claims label-space-sensitive —
  bind the exact claim). Language-prior: LOW. Version: bind dataset split + vocab. Relevance: HIGH
  (D07B's home metric).
- **Segmentation (IoU variants; SA-1B zero-shot transfer protocols).** Measures: dense-region quality;
  promptable transfer. Misses: semantic openness (unless OVS protocol). Contamination: LOW-MEDIUM.
  Language-prior: N/A (vision-only) / MEDIUM under OVS prompts. Version: bind protocol. Relevance:
  MEDIUM-HIGH (D03).
- **OCR (CER/WER, parsing benchmarks).** Measures: glyph/layout transcription fidelity. Misses:
  document reasoning. Contamination: LOW. Language-prior: MEDIUM (LM post-correction inflates naive
  scores). Version: bind benchmark + resolution policy (resolution-dependence is the specialist-test
  variable). Relevance: HIGH (D05).
- **Document/chart (DocVQA-class, chart QA, layout parsing).** Measures: structure + symbolic-content
  understanding. Misses: open reasoning depth. Contamination: MEDIUM (documents on the web).
  Language-prior: HIGH (questions often answerable from extracted text without layout). Version: bind
  exactly. Relevance: HIGH (D05/D10).
- **Image-text retrieval/alignment (Recall@K, zero-shot transfer).** Measures: global cross-modal
  addressability. Misses: region precision, compositionality (CLIP bag-of-words limits — record the
  limitation, it motivates D07B). Contamination: MEDIUM. Language-prior: N/A-by-construction
  (it IS the language prior, measured). Version: bind pretraining-data disclosure. Relevance:
  MEDIUM (D07A).
- **VQA (accuracy, open/closed splits).** Measures: visually-conditioned answering. Misses:
  evidence-use honesty (language-prior-inflated). Contamination: MEDIUM-HIGH (VQA v2 widely trained
  on). Language-prior: HIGH (the canonical shortcut exhibit — D10's central control). Version: bind
  split + answer-extraction rule. Relevance: HIGH with controls, LOW without.
- **Grounding (RefCOCO/+/g accuracy; phrase-grounding Recall).** Measures: language→region precision
  incl. relational/ambiguous reference. Misses: open-vocabulary breadth (use LVIS-rare alongside).
  Contamination: LOW-MEDIUM. Language-prior: LOW (localization resists priors — the honest metric).
  Version: bind split. Relevance: HIGH (D07B/D10/D12).
- **Spatial reasoning (spatial-relation benchmarks; VLM spatial evals).** Measures: relations, depth/
  pose-adjacent judgments via language. Misses: metric geometry (2.5D-pattern vs true-3D ambiguity —
  record per result). Contamination: MEDIUM. Language-prior: MEDIUM-HIGH. Version: bind. Relevance:
  MEDIUM-HIGH (D04→D10 handoff).
- **Multimodal reasoning (MMMU/MMMU-Pro, MathVista/MathVision, MMBench-class).** Measures:
  knowledge + visual-math + compositional reasoning under scaffold. Misses: perception-vs-reasoning
  attribution (thinking-variant ablations required). Contamination: HIGH (frontier training-data
  opacity; closed-model scores vendor-measured). Language-prior: HIGH. Version: bind model version +
  thinking budget + tool allowance (Gemini 3 code-execution visual thinking changes the contract).
  Relevance: HIGH with bindings, LOW as bare leaderboard.
- **Hallucination (POPE, HallusionBench-class).** Measures: unsupported-visual-claim rate under
  controlled polling/adversarial visuals. Misses: open-ended generation faithfulness. Contamination:
  MEDIUM (polling sets leak into training). Language-prior: IS the measurand (inverted).
  Version: bind sampling + polling protocol. Relevance: HIGH (X04 instrument).
- **Video understanding (Kinetics-style action acc; event localization mAP; Video-MME/Video-MMMU).**
  Measures: action/event/ordering/causal/physical axes separately. Misses: long-horizon state (see
  next). Contamination: MEDIUM. Language-prior: MEDIUM (narrative priors). Version: bind clip
  length + frame sampling (sampling policy changes results). Relevance: HIGH (D11).
- **Long-video (LongVideoBench, MLVU-class, 256K-context evals).** Measures: retention/retrieval/
  cross-referencing over hour-scale inputs. Misses: streaming/online interaction. Contamination:
  MEDIUM. Language-prior: MEDIUM. Version: bind duration + sampling + context config. Relevance:
  HIGH and rising (D09/D11 convergence exhibit).
- **GUI/computer-use (OSWorld 1.0 success; OSWorld 2.0 binary/partial + cost + safety audits).**
  Measures: 1.0 grounding/operational knowledge; 2.0 long-horizon state management + token economics.
  Misses: production deployment robustness (sandbox ≠ workplace). Contamination: LOW (self-hosted
  stateful tasks) but version-fragile (bind release v2026.06.24 + step/thinking/tool budgets).
  Language-prior: LOW. Version: strictest binding in the volume. Relevance: HIGHEST in class (D12).
- **Robotics/VLA (task success under embodiment/instruction/action generalization; adaptation-sample
  counts).** Measures: policy generalization + adaptation efficiency (<200-example claims).
  Misses: safety certification (no benchmark certifies deployment — state explicitly). Contamination:
  LOW (embodied) but evaluator-subjective (bind protocol). Language-prior: LOW. Version: bind
  embodiment + demo count + eval scope (bi-arm vs whole-body). Relevance: HIGH within scope (D13).
- **World model (fidelity scores vs control-oriented measures: rollout usefulness, SIMA-task success,
  planning gains).** Measures: two different things under one name — keep separate columns always.
  Misses: each misses the other (the lane's central warning). Contamination: LOW. Language-prior:
  N/A. Version: bind simulator build + horizon. Relevance: MEDIUM, methodology-immature
  (EVIDENCE_GAP on control-oriented measures — §B-D14).

---

## J. Negative space (investigated, refused — with rationale)

- **Full classical-CV history (SIFT/HOG mechanism, pre-LeNet eras).** Out of scope: D01 context
  function needs names, not expositions.
- **NeRF / 3D Gaussian Splatting / 3D reconstruction full history.** Support/context only (D04 cap):
  no TS-003-load-bearing fusion/reasoning question requires their internals; Genie 3's explicit
  non-3D-representation stance (consistency as emergent property) further reduces the need.
- **Classical SLAM / control theory / robot kinematics / locomotion.** Out of scope (D13 refusal
  list): embodiment-adaptation facts only.
- **Medical / autonomous-driving / remote-sensing / scientific-imaging verticals.** Too
  application-specific unless a generic mechanism point is demonstrated at Discovery acceptance;
  default OUT_OF_SCOPE with named-exception rule for Round E.
- **Full speech-recognition / speech-LM / audio-generation history.** Duplicative of TS-002 (which
  owns WaveNet→codec-LM→native-audio *generation*); TS-003 takes input-side nodes only (§B-D09).
- **Music-generation / voice-cloning / TTS mechanism detail.** TS-002-owned; referenced, never
  retold.
- **Safety/policy as independent subject.** Technical safety only where load-bearing (OSWorld 2.0
  safety audits as eval metadata; VLA layered-safety architectures as deployment facts). No policy
  chapter.
- **Multimodal generation+editing convergence mechanics.** TS-002-owned (FLUX/Nano-Banana-class
  unified stacks appear in TS-003 only as boundary pointers, e.g. Project Genie's Nano-Banana-Pro
  world-sketching integration noted without mechanism claims).
- **Streaming video-understanding systems.** LOW_YIELD in Round B (no source-rich system candidate
  confirmed): Round D fill-or-declare task, not silent omission.
- **Second open-VLM family; document specialist; V-JEPA citation; chart-specialist evals;
  HallusionBench/MMBench/MathVista citations; SayCan citation; CLAP/AudioSet citations;
  ScreenSpot/Set-of-Mark citations.** INSUFFICIENT_AUTHORITY at reconnaissance level (names known,
  exact bytes/roles unverified): explicit Round D verification list, §D-item-4.
- **OWOD (open-world, unknown-aware) as separate node.** Too duplicative of OVD for TS-003 purposes:
  footnote inside D07B.
- **Panoptic-segmentation mechanism depth.** Contract-clarity only (definition + citation).

---

## K. Proposed revised research architecture (Muse final proposal)

### K.1 Revised Core Question

Keep the Sol question's substance; sharpen its testable edge:

> AIは、画像や映像を単に分類する段階から、対象の位置・構造・時間関係を認識し、言語概念へ接地し、
> 複数modalを統合して推論し、予測や行動へ利用できる内部表現を形成する段階へ、どのように発展して
> きたのか。各段階で「次の計算に十分な世界の表現」は何であり、何が失われ、何が言語・座標・行動へ
> 変換可能になったのか。

Revision notes: (a) appends the representation-sufficiency question INTO the Core Question so the
X02-flavored test ("what survives into the next computation?") is asked per lane, not only in
convergence; (b) "言語・座標・行動" names the three output contracts (language-addressable semantics /
actionable coordinates / motor trajectories) that separate D07A / D07B–D12 / D13 — the volume's
load path in one phrase. Cross-cutting question retained verbatim:
**What representation of the world is sufficient for the next computation?**

### K.2 Revised dimensions

- D01 context-capped KEEP; D02 KEEP (+DINO detector); D03 KEEP (+SAM 2 bridge); D04 KEEP hard-capped
  support; D05 KEEP (+retrieval sub-lane); D06 KEEP (+SigLIP encoder-output node);
  **D07A alignment + D07B grounding (SPLIT)**; D08 KEEP (+InstructBLIP/MiniGPT-4); D09 KEEP weighted-up
  (+audio-input checklist); D10 KEEP; D11 KEEP (+AV-joint checklist, streaming stub); D12 KEEP
  reframed (OSWorld 2.0 thesis); D13 KEEP capped (+SayCan/PaLM-E/OpenX predecessors); D14 KEEP
  terminology-split (+JEPA/Dreamer counterweights, Genie 3 capability-capped); D15 KEEP full
  methodology lane (+2026 updates, convergence synthesis).
- X01 KEEP strengthened (per-lane data-contract blocks + one Tier C supervision-timeline synthesis);
  X02/X03/X04 KEEP (X02 +interface-fork instances; X03 +2026 exhibits; X04 +four-role tagging rule).
- No new top-level D beyond the split; no new X. (§D)

### K.3 Revised boundaries (reaffirmed with teeth)

- TS-002: generation-mechanism ownership absolute; TS-003 cites generation only as
  reasoning/prediction/simulation component (D14 per-paragraph policing; D09 synthesis-mechanism
  refusal with TS-002 referral).
- TS-001: efficiency-vocabulary ownership absolute; TS-003 contributes only multimodal-specific
  fields and reuses bottleneck-contract language (X03).
- Vision-centered omni: audio-input/fusion/reasoning in, all audio-synthesis history out (checklist
  enforcement, §B-D09/D11).
- Robotics: representation-contract boundary at the VL→action interface (D13 refusal list).
- Closed-vendor material: four-role tagging mandatory per case (CAPABILITY/ARCHITECTURE/DEPLOYMENT/
  EVALUATION); marketing pages never source architecture (CV2-DM-020 production rule).

### K.4 Revised tier weights

- **Tier A — Core (D01–D11 incl. D07A/D07B): heaviest, ~55–60%.** Within Tier A: D07A/D07B, D08, D09,
  D10 at full weight (the volume's explanatory center); D02/D03/D06 at normal weight; D01/D04/D05 at
  context/support weight (D05 heavier than D01/D04 — the OCR-bottleneck test is frontier-live,
  geometry context is not). D11 normal weight (long-video/streaming is the rising edge).
- **Tier B — Convergence endpoints (D12–D14): bounded, ~20–25% combined.** D12 reframed heaviest of
  the three (OSWorld-2.0 state-management thesis is 2026's freshest actionability result); D13 capped
  (refusal list); D14 capped (terminology-split skeleton). Hard rule: Tier B must not exceed Tier A
  any-subsection without Round C re-approval and evidence-density justification.
- **Tier C — Synthesis (D15 + X-synthesis): ~15–20%.** D15 full lane incl. supervision-timeline
  synthesis (X01's single shared artifact) and convergence verdict (unified-vs-modular with 2026
  evidence both ways; no predetermined unity narrative).

### K.5 Proposed page/depth distribution (planning envelope, not production authority)

Sol's 80–120pp LONGFORM envelope is confirmed plausible; reconnaissance supports the upper half
(100–120pp) IF D07B/D09/D12/D15 evidence density materializes at Discovery, else 80–100pp with Tier B
caps absorbing the cut. Depth rule: mechanism depth follows the representation-contract test (does
this mechanism change what survives into the next computation?) — not fame, not recency. No lane may
spend pages on taxonomy that its evaluation section cannot adjudicate (D10/D15 gating rule).

### K.6 What "same as Sol" means here

Where this proposal matches the Sol skeleton/audit (thesis, D01–D06/D08–D15 shape, X01–X04 set, tier
labels, 80–120pp envelope), the match is **verification outcome, not deference**: each element above
carries its evidence hook (2026 capstone reports, OVD/grounding surveys, OSWorld 2.0, Genie 3 scope
limits, encoder-reuse facts). Where it differs (D07 split depth, X01 non-promotion rationale, D12
reframing, D14 counterweight requirement, refusal lists, four-role tagging, retrieval sub-lane), the
difference is the Round B deliverable for Sol Round C to adjudicate against the five simultaneous
inputs (this report + skeleton + scope audit + TS-001 final + TS-002 final).

---

## Terminal state

`TS-003 ROUND_B_RECONNAISSANCE_COMPLETE`
`AWAITING_SOL_ROUND_C_SCOPE_REVIEW`
`NO_PRODUCTION_INITIALIZATION`

Round C is Sol's. No production Issue/branch/Profile/State/Discovery/Screening/Evidence/Selection/
Architecture/Draft/PDF/Freeze/Release was created or mutated. Shared Core untouched. TS-001/TS-002
publication bytes untouched. Backlog status untouched.

Companion file: `docs/research-plans/2026-09-30_ts-003-muse-round-b-source-candidates.md`
(audited source-candidate ledger; planning material, not canonical Discovery).
