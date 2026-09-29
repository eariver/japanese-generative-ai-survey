# TS-003 Vision & Multimodal AI — Muse Round D targeted follow-up report

Status: `ROUND_D_TARGETED_FOLLOWUP / PRE_SOL_ROUND_E / NOT_PRODUCTION_AUTHORITY`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `planning/ts-003-vision-multimodal-preresearch-20260930` (no new branch created)

Starting guard (read-only, before any write): remote HEAD `06e431e07fbbf9fea578bc0ec3a93c17b2106fb5`
== Exact Starting SHA ✓; remote tree `a4ac28f2c16bcb803e44b28a7ead385781f75074`
== Expected Starting Tree ✓. Local was one commit behind and was advanced by fast-forward-only
merge to the exact guarded SHA; no other local state existed.

Scope authority: Round C (`2026-09-30_ts-003-sol-round-c-scope-review.md`). Round B proposals were
used only as overridden by Round C dispositions (D07 split accepted; D04 support-capped; Tier B
13–18%; Parts I–V; no new top-level D; no standalone data lane; no fixed capstones).

This report covers ONLY R1–R10. No broad lane was re-opened. No production Issue/branch/Profile/
State/Discovery/Screening/Evidence/Selection/Architecture/Draft/PDF/Freeze/Release was created or
mutated. Shared Core, `main`, backlog, TS-001/TS-002 bytes, and all existing Sol/Round B/Round C
files are untouched; all findings are additive.

Evidence discipline per finding: **source-supported fact** vs **Worker interpretation** vs
**unresolved uncertainty** vs **authority limitation** are separated inline. Vendor capability claims,
published mechanisms, and independently reproduced behavior are never conflated (CV2-DM-020).
Canonical names preserved untranslated (CV2-DM-006). Source publication/version/announcement dates
kept distinct (CV2-DM-013). Access honesty: every Round-D-checked source is recorded with its actual
read level in the companion source-resolution file; nothing checked is marked `NOT_ACCESSED`, and
nothing unchecked is listed there.

Companion: `docs/research-plans/2026-09-30_ts-003-muse-round-d-source-resolution.md`
(only sources actually checked in Round D, with exact access status).

---

## Executive Summary

All ten residual questions are resolved to a state sufficient for Sol Round E closure. Headline
verdicts:

- **R1 (D04 allow-list): RESOLVED — 4 nodes, cap met.** MiDaS (monocular/relative depth +
  zero-shot-transfer framing) → OpenPose (keypoint/object-centric state) → Visual Genome
  (relational scene structure + region–language grounding data) → DUSt3R (learned geometric state:
  camera-free pointmap regression unifying mono/binocular). NeRF/3DGS/SLAM/full-reconstruction
  refused with named rationale.
- **R2 (D07B minimum chain): RESOLVED — 11-node chain with redundancy calls.** Exact IDs fixed for
  OVR-CNN (`arXiv:2011.10678`), ViLD (`arXiv:2104.13921`), MDETR (`arXiv:2104.12763`), Detic
  (`arXiv:2201.02605` — corrects Round B's wrong guess `2201.12280`), RegionCLIP
  (`arXiv:2112.09106`), OWL-ST/OWLv2 (`arXiv:2306.09683`, NeurIPS 2023), Flickr30k Entities
  (ICCV 2015), LSeg (`arXiv:2201.03546`), X-Decoder (CVPR 2023), OpenSeg (named variant),
  ODISE (`arXiv:2303.04803`, diffusion-pole note).
- **R3 (second open VLM): RESOLVED POSITIVE — two qualifiers, no `NO_SECOND_OPEN_VLM_MEETS_BAR`.**
  InternVL3 (`arXiv:2504.10479`, primary: native joint-pretraining paradigm contrast vs Qwen staged
  bridge) + Molmo 2 (`arXiv:2601.10611`, Jan 2026, Apache 2.0, grounding/video specialist with
  fully-open Olmo variant).
- **R4 (doc specialist vs generalist): `NO_CROSS_MODEL_NUMERIC_COMPARISON` + qualitative contract.**
  Nougat (`arXiv:2308.13418`) and GOT (`arXiv:2409.01704`, 580M, OCR-2.0) evaluate on own
  markup/format suites vs pipeline baselines; generalists on DocVQA-ANLS / ChartQA-relaxed-accuracy /
  OCRBench-v2 — incommensurable protocols. Five-axis qualitative comparison contract proposed.
- **R5 (streaming): RESOLVED — no `LOW_YIELD`.** Flash-VStream (`arXiv:2406.08085`, memory-based
  real-time system + VStream-QA) + StreamingBench (`arXiv:2411.03628`, 18 tasks, timestamped queries,
  omni-source, proactive output).
- **R6 (audio-input chain): RESOLVED — 5-node minimum chain, generation fully excluded.**
  Whisper → BEATs (`arXiv:2212.09058`) → CLAP (`arXiv:2206.04769`, ICASSP 2023) →
  Qwen3-Omni audio encoder + TM-RoPE (absolute-time sync) → StreamingBench omni-source eval.
- **R7 (VLA chain): RESOLVED — 7-node minimum chain.** SayCan exact ID fixed (`arXiv:2204.01691`,
  CoRL 2022 proceedings PMLR v205) with a refined role: language-conditioned planning WITHOUT joint
  representation (frozen LLM × affordance value functions) — which sharpens, not duplicates, the
  PaLM-E → RT-2 succession. RT-1/PaLM-E/OpenX/RT-2/OpenVLA/Gemini-Robotics roles confirmed as
  Round-C-accepted anchors (re-binding at intake, not re-opened here).
- **R8 (world-model counterweights): RESOLVED.** V-JEPA exact ID fixed (`arXiv:2404.08471` —
  corrects Round B's wrong guess `2307.07420`); Genie 3 official page read and role-capped
  (CAPABILITY + DEPLOYMENT-pointer only; 5 stated limitations recorded). Four-pole comparison
  contract delivered (state / predicted target / action conditioning / pixel-latent-reward /
  planning-use / distinguishing evidence).
- **R9 (eval cleanup): RESOLVED — retain/drop list with distinct-contract rationale.**
  Retain: DocVQA, ChartQA, OCRBench v2 (drop v1), POPE + HallusionBench (`arXiv:2310.14566`, CVPR
  2024 — corrects Round B's wrong guess `2311.07312`), ScreenSpot (inside SeeClick,
  `arXiv:2401.10935`, ACL 2024), OSWorld 1.0 + 2.0, Video-MME (`arXiv:2405.21075`),
  LongVideoBench (`arXiv:2407.15754`), StreamingBench, VSI-Bench (CVPR 2025, + debiased subset).
  Drop as separate anchors: MLVU/LVBench/InfiniBench, VStream-QA (predecessor context),
  Mind2Web/AITW (downstream-validation context), TextVQA/ST-VQA (umbrella-covered), BLINK
  (image-only; subsumed for TS-003 purposes), OCRBench v1 (superseded).
- **R10 (capstone role matrix): DELIVERED** with †-marking for prior-round IDs requiring intake
  re-binding. No architecture inferred from product pages or demos anywhere.

**Round C reversal assessment: NO REVERSAL recommended.** Refinements only (allow-list, retain/drop
lists, role matrix). The 4-condition new-lane test admits no new top-level D/X (streaming stays a
D11 sub-lane + eval presence; retrieval stays a D05 sub-lane).

---

## R1 — D04 spatial/geometry exact allow-list: RESOLVED

**Allow-list (4 nodes = cap; order is explanatory, not chronological rank):**

1. **MiDaS — Ranftl et al., `arXiv:1907.01341` (TPAMI 2022); repo `isl-org/MiDaS`.**
   Contract contribution: monocular/relative geometry WITHOUT metric calibration (scale/shift-
   invariant losses) + **zero-shot cross-dataset transfer as the evaluation contract** for
   robustness. Answers Round C Q1 (what geometry is absent from labels: dense relative depth) and
   feeds X01 (multi-dataset mixing via Pareto-optimal multi-objective learning). [source-supported]
2. **OpenPose — Cao et al., `arXiv:1812.08008` (TPAMI 2019; CVPR 2017 precursor); PAFs.**
   Contract contribution: object-centric spatial state (135 body/foot/hand/face keypoints) via
   bottom-up part-affinity association — the canonical demonstration that *association*, not just
   detection, is a representation problem. Answers Round C Q2/Q4 (pose state; why classification
   features cannot drive action). [source-supported]
3. **Visual Genome — Krishna et al., `arXiv:1602.07332` (IJCV 2017); 108K images, ~21 objects /
   ~18 attributes / ~18 relations per image, WordNet-canonicalized scene graphs.**
   Contract contribution: relational scene structure as first-class annotation + region-description
   grounding data. Dual role: D04 relational-structure node AND D07B/MDETR-era grounding-data
   predecessor (GLIP GoldG practice descends from this data regime). [source-supported]
4. **DUSt3R — Wang et al., `arXiv:2312.14132` (CVPR 2024); repo `naver/dust3r`.**
   Contract contribution: learned geometric state WITHOUT camera priors — pointmap regression
   unifying monocular and binocular cases, cameras recoverable downstream. This is the D04→D09/D13
   bridge exhibit: geometry as network output state rather than calibrated pipeline input, built on
   pretrained Transformer init. [source-supported]

**Coverage check against Round C's four questions:** absent-from-labels geometry (MiDaS depth +
VG relations) ✓; assumed 2D/2.5D/3D state (OpenPose keypoints + DUSt3R pointmaps) ✓;
token/language conversion loss (framed as the D04→Part III handoff question; VG region–language
links are the concrete artifact) ✓; why classification cannot yield interaction (OpenPose
association + DUSt3R pose-free reconstruction as existence proofs) ✓. [Worker interpretation]

**Explicitly refused near-neighbours:** NeRF (explicit neural scene representation — Genie 3's own
vendor framing positions emergent consistency AGAINST explicit-3D methods, reducing TS-003 need);
3D Gaussian Splatting (same reason); classical SLAM/SfM pipelines (calibration-first paradigm that
DUSt3R explicitly supersedes for TS-003's purposes); full MVS survey; 3D object detection;
human-mesh recovery (SMPL-class — application-specific); depth-benchmark zoos (KITTI/NYU/ETH3D as
eval substrates only, no mechanism nodes). [Worker interpretation; Sol may grant named exceptions
only with a load-bearing justification at Round E]

**Uncertainty:** DUSt3R successors (MASt3R/Spann3R-class) exist but add no new contract → correctly
excluded by the minimum rule; note as intake-awareness only, not nodes.

## R2 — D07B grounding lineage exactness: RESOLVED

**Minimum non-redundant chain** (each node changes exactly one contract; drops noted):

| # | Node | Exact source | Contract changed |
|---|---|---|---|
| 1 | Phrase-localization task origin | Flickr30k Entities, Plummer et al., ICCV 2015 (ICCV open-access canonical) | Detection-with-fixed-classes → open-phrase-set localization (244k coreference chains, 276k boxes); task "akin to detection but phrases unseen at train time" |
| 2 | REC eval contract | RefCOCO/+/g, Yu et al., 2016 (`arXiv:1606.03825`, carried) | Single-referent disambiguation under relational/ambiguous description; precision metric home |
| 3 | OVD concept origin | OVR-CNN, Zareian et al., CVPR 2021 (`arXiv:2011.10678`) | Recognition/localization disentangled: captions teach recognition (V2L + grounding/MLM/ITM pretraining), boxes teach localization; coins "open-vocabulary detection" |
| 4 | CLIP-distillation transfer | ViLD, Gu et al., ICLR 2022 (`arXiv:2104.13921`) | Frozen open-vocabulary classifier (CLIP/ALIGN teacher) distilled into two-stage detector (ViLD-text + ViLD-image); LVIS-rare protocol entry (16.1→26.3 APr) |
| 5 | Region-pretraining pole | RegionCLIP, Zhong et al., CVPR 2022 (`arXiv:2112.09106`) | Image-level→region-level domain-shift diagnosis; pseudo region-text pairs + contrastive region pretraining (≠ ViLD's detector-distillation) |
| 6 | Vocabulary-scaling pole | Detic, Zhou et al., ECCV 2022 (`arXiv:2201.02605`) | Image-level labels (ImageNet-21K) train detector classifier via max-size-proposal assignment; localization/classification decoupling premise |
| 7 | Detection-as-grounding reformulation | GLIP, Li et al., CVPR 2022 (carried, Round-C-accepted) | Unification of detection + phrase grounding losses; GoldG grounding-data practice |
| 8 | Modulated-detection multi-tasker | MDETR, Kamath et al., ICCV 2021 (`arXiv:2104.12763`) | DETR conditioned on raw text queries; one model spans phrase grounding (Flickr30k) + REC (RefCOCO/+/g) + RES (PhraseCut) + VQA-adjacent (GQA); early-fusion pole |
| 9 | Minimal-head late-fusion pole | OWL-ViT, Minderer et al., ECCV 2022 (carried) | Frozen CLIP + per-token heads; architecture-minimal contrast to GLIP/MDETR early fusion |
| 10 | Tight-fusion unification | Grounding DINO, Liu et al., 2023 (carried) | Three-phase fusion + sub-sentence features; detection + REC in one framework; ODinW record context |
| 11 | Web-scale self-training scaling | OWL-ST/OWLv2, Minderer et al., NeurIPS 2023 (`arXiv:2306.09683`; NeurIPS proceedings canonical) | N-gram machine label space + weak filtering → 1B+ pseudo-annotated examples; LVIS-rare 31.2→44.6% (X01 exhibit). "Unseen" claim is label-space-sensitive — bind exactly (CV2-DM-020) |
| 12 | OVS origin → unification | LSeg (`arXiv:2201.03546`, ICLR 2022) → X-Decoder (Zou et al., CVPR 2023) | Pixel-text alignment origin → generic+referring segmentation + VL tasks in one decoder (no pseudo-labeling). OpenSeg (ECCV 2022, Ghiasi) named as scaling variant (not a separate node). ODISE (`arXiv:2303.04803`, CVPR 2023 Highlight) named as diffusion-backbone pole with TS-002-crossover flag |
| → | Actionable-grounding bridge (pointer, not a D07B node) | ScreenSpot/SeeClick (`arXiv:2401.10935`); OSWorld 1.0/2.0 (R9) | D07B→D12 handoff: coordinate prediction becomes task-state action |

**Redundancy calls executed:** ViLD vs RegionCLIP kept (distillation vs pretraining — different
mechanisms, and RegionCLIP's domain-shift diagnosis is itself load-bearing text); RegionCLIP vs
Detic kept (recognition-pretraining vs vocabulary-supervision — different X01 contracts); GLIP vs
MDETR kept (data-practice reformulation vs modulated multi-task architecture); GLIP vs Grounding
DINO kept (reformulation vs fusion design); MDETR fine-tuned REC vs zero-shot REC: note as protocol
difference, not a new node. OWOD (unknown-aware, Joseph 2021) stays a D07B footnote per Round B.
[source-supported facts for IDs/roles; keep/drop is Worker interpretation for Round E to ratify]

**D07A-vs-D07B metric split (for Round E contract):** D07A = zero-shot classification / Recall@K
retrieval on image-level pairs; D07B = LVIS-rare AP / ODinW / RefCOCO grounding accuracy /
phrase-localization Recall@K. No shared ranking table permitted.

**Uncertainty:** exact GLIP/OWL-ViT/Grounding-DINO/RefCOCO IDs carried from prior rounds (†, re-bind
at intake); GoldG composition details deferred to intake.

## R3 — Second open VLM family: RESOLVED POSITIVE

Two families meet the bar; no `NO_SECOND_OPEN_VLM_MEETS_BAR`.

**Primary recommendation — InternVL3 (`arXiv:2504.10479`, Apr 2025, Shanghai AI Lab + collaborators;
repo `OpenGVLab/InternVL`; weights + data released):**
- Primary technical report available ✓ (ABSTRACT_FETCH; "Technical Report" comment).
- Inspectable architecture ✓: InternViT-300M/6B-448px encoders × Qwen2.5/InternLM3 backbones
  (1B–78B table), open weights + `OpenGVLab/InternVL-Data`.
- Mechanism detail for comparison ✓: **native multimodal pre-training paradigm** (joint
  text+multimodal from stage one — the direct paradigm contrast to Qwen's staged bridge/extend
  recipe), V2PE (variable visual position encoding for extended multimodal context), SFT + MPO
  (mixed preference optimization) post-training, test-time scaling strategies.
- Current relevance ✓: 78B = 72.2 MMMU (open-SOTA claim at report date; vendor-measured);
  competitive-with-proprietary framing (4o/3.5 Sonnet/Gemini 2.5 Pro — vendor claims).
- Non-redundancy vs Qwen ✓: paradigm-level (native-joint vs staged-bridge), encoder-level
  (InternViT vs SigLIP2-continued), post-training-level (MPO vs bifurcated thinking SFT).
- Limitations ✓: vendor-measured evals only at this read level; independent reproduction to be
  bound at intake. [source-supported from abstract; full-recipe depth requires intake read]

**Comparator — Molmo 2 (`arXiv:2601.10611`, v4 Apr 2026, Ai2; Apache 2.0; repo `allenai/molmo2`;
code + weights + datasets):**
- Fully-open variant exists (Olmo-backed 7B: encoder→connector→LLM all open) alongside
  Qwen3-8B/SigLIP2 8B/4B variants — openness gradient itself is TS-003-relevant (X04/X01).
- Distinct contribution vs Qwen: data-first openness (no closed-VLM synthetic data), pointing as
  interface (PixMo-Points → video pointing/tracking), grounding-measured video evals (video
  counting 35.5 vs Qwen3-VL 29.6; pointing F1 38.4 vs Gemini 3 Pro 20.0; tracking J&F 56.2 vs 41.1
  — all author-measured, bind at intake).
- Role: grounding/video specialist comparator + D07B→D11 actionability exhibit; NOT the primary
  paradigm-contrast family (8B/4B reuse Qwen3 backbones — partial Qwen dependence, disclosed).
  [source-supported]

**Selection rationale for Round E:** InternVL3 = architecture-paradigm comparison (Part II/III);
Molmo 2 = openness + grounding-measurement comparison (Part II/V). Neither selected by popularity;
both by contract distinctness + source richness.

**Uncertainty:** InternVL3.5-series currency and Molmo-2 follow-ups must be re-checked at intake
(search noted InternVL3.5-8B as a live comparator name; not verified → not a source entry).

## R4 — Document specialist vs generalist: `NO_CROSS_MODEL_NUMERIC_COMPARISON` + qualitative contract

**Finding (source-supported):** the two poles report on incommensurable protocols.
- Specialist pole A — Nougat (`arXiv:2308.13418`, Meta): Donut-lineage Swin encoder-decoder,
  markup output (text + LaTeX math + tables), trained on arXiv/PMC/IDL-derived pairs (>91.5%
  arXiv); evaluates markup agreement vs GROBID/pdf-text baselines on own scientific-document test.
  Open code + models.
- Specialist pole B — GOT (`arXiv:2409.01704`, Sep 2024): 580M encoder-decoder (80M
  high-compression encoder: 1024²px → 256 tokens; 0.5B Qwen-based decoder, 8K context),
  OCR-2.0 theory (plain + formatted markdown/tikz/smiles/kern outputs, region-prompt, dynamic
  resolution, multi-page); evaluates on own OCR-2.0 suites vs OCR-1.0/LVLM-manner baselines.
- Generalist pole: DocVQA-ANLS (extractive answer tolerance), ChartQA relaxed-accuracy
  (visual+logical QA), OCRBench-v2 (23 tasks incl. localization/reasoning, 6 metric types, private
  test set). Different metrics × different test distributions × different resolution policies ×
  different output contracts (markup reconstruction vs answer extraction).
- Therefore any single numeric ranking would violate CV2-DM-020 (flattened conditions) and the
  Round C comparability rule. Verdict: `NO_CROSS_MODEL_NUMERIC_COMPARISON`. [Worker inference from
  source-supported protocol facts]

**Safe qualitative comparison contract (for Round E, five axes, no scores ranked):**
1. Output contract: faithfulিয reconstruction (markup/format) vs answer extraction (ANLS/accuracy).
2. Resolution/token policy: native-dynamic (GOT) vs tiling-dependent generalist (bind px + tokens).
3. OCR dependence: OCR-free end-to-end (Nougat/GOT/Donut-line) vs OCR-tool-assisted generalist paths.
4. Interactivity: region/coordinate-prompt recognition (GOT) vs whole-image QA.
5. Failure-mode profile: dense math/table scenes, handwriting, non-semantic text, layout parsing —
   reported per-axis with the source that measured it, never as a cross-model table.
   OCRBench-v2's capability-split findings (text recognition vs spotting vs element parsing vs
   reasoning) are the sanctioned vocabulary for axis 5.

**Uncertainty:** GOT/Nougat head-to-head on identical DocVQA/ChartQA splits was not found at this
read level; if Discovery finds a same-protocol comparison, Round E may admit that single table with
full condition binding — otherwise the contract above stands.

## R5 — Streaming / long-video: RESOLVED (no LOW_YIELD)

- **System anchor — Flash-VStream (`arXiv:2406.08085`, Jun 2024; code/models/datasets stated
  available):** memory-based real-time understanding for long video streams; human-memory-mechanism
  framing; reduced inference latency + VRAM; handles asynchronous user questions against continuous
  visual content (the online-arrival problem); SOTA-claim on offline benches too (author-measured).
  Covers: online input ✓, bounded memory ✓, persistent state ✓, latency/VRAM trade-off ✓.
  [ABSTRACT_FETCH]
- **Companion bench — VStream-QA (inside the same paper):** timestamped QA for online streaming;
  named predecessor context for StreamingBench. Retained as cited-predecessor, not a separate anchor.
- **Eval anchor — StreamingBench (`arXiv:2411.03628`, Nov 2024; repo `THUNLP-MT/StreamingBench`):**
  900 videos / 4,500 human QA / 18 tasks / 3 categories (real-time visual, omni-source incl. audio,
  contextual incl. streaming interaction + proactive output); timestamped mid-stream queries;
  best model (Gemini 1.5 Pro) 67.07% vs human 91.66% (author-measured). Covers incremental-update
  and continuous-perception-latency evaluation. [ABSTRACT_FETCH]
- **Boundary vs long-context:** Qwen3-VL-256K/Molmo-2-long-video = offline long-context (D09/D11
  core); Flash-VStream/StreamingBench = online streaming (D11 sub-lane + D15 eval). The two must
  not share a metric column. [Worker interpretation]

**Uncertainty:** real-deployment latency figures beyond author-reported; streaming-native open
system newer than Flash-VStream to be swept at intake (currency check, not a gap).

## R6 — Audio-input / omni predecessor chain: RESOLVED

**Minimum input-side chain (5 nodes; every generation node refused):**

1. **Whisper (`arXiv:2212.04356`, carried):** robust speech-input encoder precedent (multitask
   weakly-supervised speech). Role: speech→token input contract. Generation history stays TS-002.
2. **BEATs (`arXiv:2212.09058`, ICML 2023; code+models):** general-audio SSL via iterative
   acoustic-tokenizer + masked discrete-label prediction (NOT reconstruction); 50.6% mAP
   AudioSet-2M audio-only, 98.1% ESC-50 (author-measured). Role: non-speech-audio input
   representation contract (semantics-preserving discretization). [ABSTRACT_FETCH]
3. **CLAP (`arXiv:2206.04769`, ICASSP 2023):** contrastive language-audio pretraining, 128k pairs,
   16 tasks/8 domains zero-shot + 5 supervised SOTAs (author-measured). Role: the explicit
   CLIP-parallel — audio-side addressability, completing the D07A analogy for sound.
   [ABSTRACT_FETCH]
4. **Qwen3-Omni input/fusion (`arXiv:2509.17765`, Apache 2.0):** from-scratch audio encoder,
   TM-RoPE absolute-time 80ms alignment of audio+video streams, Thinker–Talker streaming
   (234ms first-packet, theoretical). Role: omni input fusion + modality-synchronization mechanism;
   output-generation (Talker/Code2Wav/speech synthesis) is TS-002-side and subordinated.
   [ABSTRACT_FETCH]
5. **StreamingBench omni-source category (`arXiv:2411.03628`):** synchronized visual+audio
   content + proactive output as an evaluated contract. Role: streaming-multimodal-input eval.
   [ABSTRACT_FETCH]

**Excluded with rationale:** TTS/voice-cloning/music-generation mechanisms (TS-002-owned);
AudioSet as mechanism node (named data context only — BEATs' 50.6% already situates it);
Wav2CLIP/AudioCLIP (CLIP-distillation variants — superseded by CLAP's native audio-text contrast
for TS-003's addressability question; named context at most). [Worker interpretation]

**Contract changed per step (for Part III prose):** speech-tokens (Whisper) → general-audio
semantics (BEATs) → language-addressable audio (CLAP) → time-aligned omni fusion (Qwen3-Omni) →
streaming-evaluated input (StreamingBench).

## R7 — VLA predecessor chain: RESOLVED

**Minimum chain (7 nodes; each changes one representation/interface contract):**

| Node | Source | New contract contributed |
|---|---|---|
| SayCan | `arXiv:2204.01691` (CoRL 2022; PMLR v205, 2023); site+code `say-can.github.io` | **Language-conditioned planning WITHOUT joint representation:** frozen LLM (Say, task-grounding) × learned affordance value functions (Can, world-grounding); 101 real kitchen tasks, 84% planning / 74% execution; grounding doubles non-grounded baseline. Refines Round B: SayCan is the *planner-side* predecessor, making PaLM-E's joint-embedding step the visible break |
| RT-1 | carried † | Large-scale real-robot demonstration-token corpus (kitchen tasks); the data-regime predecessor that makes trajectory-conditioning trainable |
| PaLM-E | `arXiv:2303.03378` † | Embodied joint representation: continuous sensor observations injected into the LM embedding space (the "VLM into body" break SayCan stops short of) |
| Open X-Embodiment | `arXiv:2310.08864` † | Cross-embodiment data contract (X01 exhibit): multi-robot skill transfer substrate |
| RT-2 | carried † (Round C §D13 fixes formulation) | **Action tokenization + co-fine-tuning:** actions as text tokens; web-scale VL transfer into control (VLA formulation origin) |
| OpenVLA | `arXiv:2406.09246` † | Open-weights VLA implementation (inspection/ARCHITECTURE pole) |
| Gemini Robotics 2 / On-Device 2 | model pages + On-Device 2 card (Jul 2026, read R10) | Planner–policy split in production form (ER 2 + VLA) + on-device/multi-embodiment deployment contract (<200-example adaptation claim; trusted-tester distribution; bi-arm-primary eval scope; high-DoF limits stated) |

† = ID/role from prior-round acceptance (Round B ledger / Round C §D13); exact re-binding required
at Discovery intake; NOT re-fetched in Round D per scope discipline (no re-opening settled lanes).

**Explicit exclusions (no change to Round C list):** kinematics/dynamics/gait/actuators/locomotion
content beyond embodiment-adaptation facts; manipulation-hardware surveys; general robotics
safety/policy (layered-safety noted as deployment fact only, per card).

**Uncertainty:** independent (non-vendor) VLA eval remains thin — partial EVIDENCE_GAP carried to
Round E (OpenVLA-community evals to be swept at intake).

## R8 — World-model terminology counterweights: RESOLVED

**Four-pole comparison contract** (not ancestry — separation):

| Pole | Representative source (status) | State represented | Predicted target | Action conditioning | Pixel / latent / reward | Planning/training/eval use | Distinguishing evidence |
|---|---|---|---|---|---|---|---|
| Terminological origin | Ha & Schmidhuber 2018 † | VAE latent + RNN hidden | Next latent + reward (MDN) | Yes (action-in) | Latent (+reward) | Planning (evolution in dream) | Historical term source; NOT Genie's technical ancestor (§G.5 carried) |
| Latent dynamics / model-based decision | DreamerV3 † | RSSM stochastic+deterministic latent | Latent trajectory + reward + discount | Yes | Latent (+reward) | Planning + training (Atari/DMC/Minecraft diamonds — task returns) | Task-return gains, not visual fidelity |
| Predictive representation, no generation | V-JEPA, Bardes et al. (`arXiv:2404.08471`; repo `facebookresearch/jepa`) — ABSTRACT_FETCH | Masked spatiotemporal features | Missing-region features (no pixels, no text, no negatives) | No | Latent only | Representation probe (frozen backbone: K400 81.9 / SSv2 72.2 / IN1K 77.9) | Frozen-eval transfer WITHOUT any generative decoder (diffusion-pixel decoder exists only as post-hoc grounding probe, encoder frozen) |
| Generative interactive environment | Genie 3 (DeepMind blog 2025-08-05 + model page, OFFICIAL_PAGE_READ) | Autoregressive frame trajectory + 1-min visual memory | Next frames under navigation + promptable events | Partial (navigation + text events; agent action space stated LIMITED) | Pixel | Agent training/eval substrate (SIMA goal rollouts; goal-agnostic simulation) | Minutes-scale consistency + SIMA-task executability, NOT photorealism scores |

**Genie 3 role cap enforced (source-supported):** real-time 24fps/720p ✓, minutes-scale consistency
✓, promptable world events ✓, SIMA use ✓ — all CAPABILITY_CASE; architecture undisclosed (no
paper/weights) → never ARCHITECTURE_CASE; DEPLOYMENT-pointer (research preview + prototype gating).
Five vendor-stated limitations recorded verbatim-class: limited agent action space; multi-agent
interaction unsolved; no georeferenced real locales; text rendering conditional; minutes-scale
duration. The blog's NeRF/3DGS contrast ("emergent consistency vs explicit 3D") is vendor framing —
attribute, don't adopt (feeds R1's NeRF exclusion rationale).

**Anti-collapse rule for Round E (carried + sharpened):** every D14 exhibit must fill the
state/target/conditioning/pixel-latent-reward/use row before any prose; exhibits that can only fill
the pixel column are TS-002 cross-references, not D14 cases.

**Uncertainty:** transferable control-oriented world-model benchmark — none found → EVIDENCE_GAP
(see R9).

## R9 — Evaluation authority cleanup: RESOLVED

**Retain list (distinct measurement contract each; versions/metrics binding specified):**

- **DocVQA** (`arXiv:2007.00398`, WACV 2021; docvqa.org leaderboard): structure-sensitive document
  QA; metric ANLS (+ accuracy); human 94.36%; 50K Q / 12.7K images; 80-10-10 split. Distinct:
  document-structure reading. Contamination MEDIUM (web documents); language-prior HIGH (extractive
  shortcuts) → report ANLS, never bare accuracy alone.
- **ChartQA** (`arXiv:2203.10244`, Findings ACL 2022; repo `vis-nlp/ChartQA`): human-written
  visual+logical chart QA (9.6K human + 23.1K generated); relaxed-accuracy metric. Distinct:
  visual-reference + arithmetic reasoning over charts. Prior synthetic sets (FigureQA/DVQA/PlotQA)
  named context only.
- **OCRBench v2** (`arXiv:2501.00321`, Jan 2025): 23 tasks / 31 scenarios / 10K human-verified QA /
  6 metric types + 1,500-image PRIVATE test set (contamination discipline); eight capabilities incl.
  text spotting / element parsing / reasoning. Distinct: localization + reasoning over visual text
  (v1's recognition-only scope superseded → DROP v1). Finding-2 (78.3% VQA-with-position vs 12.9%
  IoU localization, InternVL3-14B) is the sanctioned D07B→D15 exhibit.
- **POPE** (carried): object-existence polling; cheap hallucination screen. Distinct: polling
  protocol. Non-redundant with HallusionBench (polling vs control-pair diagnosis).
- **HallusionBench** (`arXiv:2310.14566`, CVPR 2024; repo `tianyi-lab/HallusionBench`): 346 images
  (165 original + 181 human-edited) / 1,129 questions / control-pair structure separating language
  hallucination vs visual illusion; GPT-4V 31.42% pair-accuracy (author-measured). Distinct:
  failure-attribution diagnosis. Contamination LOW-MEDIUM (handcrafted + edited images).
- **ScreenSpot** (inside SeeClick, `arXiv:2401.10935`, ACL 2024): 600+ screenshots / 1,200+
  instructions; mobile+desktop+web; text + icons/widgets; icon-grounding is the hard slice.
  Distinct: pure element-localization accuracy (vs OSWorld task success). Currency check at intake
  (v2/Pro-class successors named as check, not entries).
- **OSWorld 1.0** (carried): short-horizon task success (grounding/operational-knowledge thesis).
  **OSWorld 2.0** (`arXiv:2606.29537` v2 Jul 2026, ABSTRACT_FETCH): long-horizon state-management
  thesis + token-cost curves + safety-audit metadata; strictest binding in volume (model + thinking
  + tool setting + steps + release). Distinct: task-state persistence economics.
- **Video-MME** (`arXiv:2405.21075`, v3 May 2025): 900 videos / 254h / 2,700 QA; 11s–1h durations;
  subtitles + audio modalities. Distinct: full-spectrum duration × modality breadth.
  [ABSTRACT_FETCH]
- **LongVideoBench** (`arXiv:2407.15754`): 3,763 videos + subtitles; 6,678 QA; "referring
  reasoning" task (retrieve + reason over referred long context). Distinct: referred-context
  retrieval-reasoning; frame-count sensitivity finding (performance improves only with more frames).
  [ABSTRACT_FETCH]
- **StreamingBench** (above, R5): streaming-eval contract (timestamped + omni-source + proactive).
- **VSI-Bench** (CVPR 2025, Yang et al.; HF `nyu-visionx/VSI-Bench`; 5,131 examples + 2,363 debiased
  subset Nov 2025): video-based visual-spatial intelligence (configurational / measurement / 
...[truncated 3880 chars]