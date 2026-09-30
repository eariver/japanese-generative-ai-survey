# TS-003 Materiality + Completeness audit — Sol review surface

Issue: `SP-vision-multimodal-2026` | Date: `2026-10-01 UTC` | Lifecycle at build: `CANDIDATES_NORMALIZED`

Authority: Sol r5 PASS (`sol-evidence-semantic-review-r5.md`) + execution request
(`sol-ts003-evidence-materiality-completeness-20261001.md`).
Evidence authority used (exactly): `evidence/v2/accepted/4182d7d5...` (111 Cards, 106/5).
Views authority used (exactly): `evidence/v2/views/accepted/e3d0b3b3...` (111 Views, 101/10).
r1–r4 resolved as history only, never as active authority.

## 1. Materiality disposition counts (canonical ledger `materiality-ledger-v2.json`)

- Rows: 111 (one per Discovery record; no silent drops — validator enforces).
- MATERIAL: 101. CONTEXT: 10. EXCLUDED/DUPLICATE: 0 (no DROP screening decisions; all 111 locators unique, no duplicate groups declared).
- Ledger SHA-256: `c9fc9750fe20cc1d2a1bd0daa58207d0eb8ead47301a7f8b8cf2676904fcf15b`
  (recomputed at read-back; Sol may re-hash the committed file).

## 2. VM-O01–VM-O16 materiality coverage (multi-obligation records counted per obligation)

| Obligation | Status | MATERIAL | CONTEXT | MATERIAL anchors (high level) |
|---|---|---|---|---|
| VM-O01 | SATISFIED | 2 | 2 | AlexNet (D003), ResNet (D004) |
| VM-O02 | SATISFIED | 6 | 2 | R-CNN, Faster R-CNN, YOLO, DETR, DINO detector, YOLO-World |
| VM-O03 | SATISFIED | 4 | 2 | FCN, Mask R-CNN, SAM, SAM 2 |
| VM-O04 | SATISFIED | 4 | 0 | MiDaS, OpenPose, Visual Genome, DUSt3R (cap exact) |
| VM-O05 | SATISFIED | 10 | 0 | LayoutLM/v3, Donut, Pix2Struct, Nougat, GOT, Qwen3-VL-Embedding + evals |
| VM-O06 | LIMITATION | 7 | 0 | ViT, DeiT, Swin, MAE, DINO, DINOv2, SigLIP (G06 residual) |
| VM-O07 | SATISFIED | 4 | 1 | Show and Tell, VQA, CLIP, ALIGN (+ shared SigLIP) |
| VM-O08 | SATISFIED | 18 | 1 | Full 12-step chain (Flickr30k→RefCOCO→OVR→ViLD→RegionCLIP→Detic→GLIP→MDETR→OWL-ViT→Grounding DINO→OWL-ST→LSeg→X-Decoder) + ODISE + LVIS |
| VM-O09 | SATISFIED | 5 | 2 | Flamingo, BLIP-2, InstructBLIP, LLaVA, Molmo v1 (+ Frozen/MiniGPT-4 context) |
| VM-O10 | SATISFIED | 17 | 0 | Qwen2.5-VL, Qwen3-VL(+repo), Qwen3-Omni(+repo), Whisper, BEATs, CLAP, InternVL3(+repo), Molmo 2(+repo), Gemini 3.x cards |
| VM-O11 | SATISFIED | 9 | 0 | MMMU, POPE, HallusionBench, MMBench, MathVista (+ VQA/OCRBench-v2 shared) |
| VM-O12 | SATISFIED | 9 | 0 | Kinetics, SSv2, Ego4D, Video-MME, LongVideoBench, StreamingBench, Flash-VStream (+ SAM2/VSI shared) |
| VM-O13 | SATISFIED | 3 | 0 | OSWorld, OSWorld 2.0, SeeClick/ScreenSpot (cap) |
| VM-O14 | SATISFIED→LIMITATION | 9 | 0 | SayCan, RT-1, PaLM-E, OpenX, RT-2, OpenVLA, Gemini Robotics 2 + On-Device 2 (G01 residual) |
| VM-O15 | LIMITATION | 7 | 0 | Ha/Schmidhuber, DreamerV3, I-JEPA, V-JEPA, Genie, Genie 3 blog+page (G02 residual) |
| VM-O16 | SATISFIED | 12 | 0 | Retain-set via shared records (distinct contracts only) |

## 3. CONTEXT rationale (10 records; important non-material cases)

- VM-D001 Neocognitron (INSPECT): paywalled context-only origin; load-bearing mechanism starts later.
- VM-D002 LeNet (KEEP): custom-font-encoded PDF barrier; predecessor-context scope only.
- VM-D008 SSD / VM-D009 RetinaNet (MAYBE): thin lineage-completeness nodes; short treatment.
- VM-D014 U-Net (KEEP): segmentation-role confinement; diffusion-backbone history excluded (TS-002).
- VM-D016 Panoptic (MAYBE): definition+citation contract depth.
- VM-D040 ALIGN (KEEP): noisy-scale variant; short treatment.
- VM-D054 OpenSeg (KEEP): bounded OVS scaling variant, not equal-depth node.
- VM-D057 Frozen (KEEP): precursor context for frozen-component design space.
- VM-D061 MiniGPT-4 (KEEP): bridge-function node, same instruction-tuning bridge as InstructBLIP.

## 4. Duplicate / source-role handling

- No duplicate groups: all 111 locators unique; Screening declared zero duplicate_group values.
- Same-system multiple authorities are NOT double-counted as transitions: Qwen3-VL paper+repo,
  Qwen3-Omni paper+repo, InternVL3 paper+repo, Molmo 2 paper+repo, Gemini Robotics page+card,
  Genie 3 blog+page each form one lineage thread (branch_ids shared, e.g. `d09-qwen-line`).
- Vendor/model-card/blog records carry role caps (CAPABILITY/EVALUATION/DEPLOYMENT only where
  bound); no architecture inferred from pages/demos; vendor numbers quarantined with attribution.

## 5. TS-001 / TS-002 overlap handling

Per the coverage matrix: Transformer/attention, ViT, CLIP, VAE/tokenizer, video, audio,
quantization/MoE/serving, world-model and agent/action objects appear ONLY through the TS-003
question (token formulation, addressability, observed-video state, input/fusion, perception-grounded
action, predictive state). Generic efficiency history reused as vocabulary (X03), never retold;
generation/control/editing history cross-referenced, never retold. No retelling detected in audit.

## 6. D04 cap read-back

4/4 allow-list nodes MATERIAL, 0 CONTEXT, 0 additions. Refusals (NeRF/3DGS/SLAM/MVS/3D-detection/
SMPL/benchmark-zoos) ledgered in negative space. Cap holds.

## 7. D12–D14 combined-weight read-back

MATERIAL records: O13 3 + O14 9 + O15 7 = 19 of 101 (19%). Bounded endpoints hold; perception/
grounding/multimodal-state lineages (O01–O12 minus caps ≈ 82%) dominate. No endpoint inflation.

## 8. Profile Completeness per-obligation status (`profile-completeness-v2.json`)

Overall: `LIMITED`. Closure: `LIMITED` (expansion_passes 1, final-pass new sources 0,
open obligations 0, targeted gap-fill completed true — the targeted process was the
pre-production rally + Discovery coverage design; G01–G06 are bounded residuals, not
un-attempted gap-fills).
- SATISFIED 13: O01, O02, O03, O04, O05, O07, O08, O09, O10, O11, O12, O13, O16.
- LIMITATION 3: O06 (G06 SigLIP2 citation unbound), O14 (G01 VLA independent eval),
  O15 (G02 control-oriented world-model measures). Each residual explicitly bounded in rationale.
- NEEDS_RESEARCH 0: no obligation requires new research before Sol review (honestly recorded;
  Sol may disagree and authorize targeted research).

## 9. X01–X04 coverage read-back

- X01 data/supervision/post-training: 60 tagged records + per-obligation supervision contracts
  (ImageNet-scale, caption/V2L, distillation, region-pseudo, image-level-label, grounding-data,
  N-gram self-training, instruction data, joint/native, MPO, trajectory/cross-embodiment,
  acoustic-tokenizer, markup pairs). Part V synthesis staged, not a standalone chapter.
- X02 objective/interface contract: 62 tagged records; every transition's in/out contract in claims.
- X03 efficiency/token/memory/latency: 15 tagged records (fusion/tokenizer/resampling/loop/on-device/
  streaming costs); TS-001 vocabulary reused, never retold.
- X04 reliability/source fidelity/claim strength: 32 tagged records (failure attribution, vendor-claim
  isolation, 4-role tagging, contamination/judge disciplines, CV2-DM-020 throughout).

## 10. G01–G06 disposition (preserved, not erased)

Carried as residual limitations in Completeness (all six verbatim) and in obligation rationales
(O06/O14/O15). No narrative-confidence upgrade. No weak-authority closure.

## 11. Residual limitations / access barriers / LOW_SIGNAL

- Access: LeNet PDF encoding, Neocognitron paywall (context-scope only); repo commit pinning,
  vendor page drift, InternVL3.5/ScreenSpot-successor currency deferred to later stages.
- LOW_SIGNAL areas: none remaining (streaming + second-VLM resolved in Discovery).
- No FULL_TEXT overclaim: abstract/page-level capture recorded per record with evidence boundaries.

## 12. Stage-validation receipt

`execution/materiality-completeness-20261001/validation/evidence-materiality-completeness-validation.json`
with CORE_STAGE_CONTRACT result for the CANDIDATES_NORMALIZED combined basis
(discovery + screening + r5 evidence + r5 views + ledger + completeness).

## 13. Checkpoint/state transition receipt

`orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json`; Production State advanced
`CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` with evidence/materiality/completeness passed.
Bridge run: `execution/bridge-runs/advance-evidence-20261001/receipt.json` (if bridge path used)
or local advance script receipt (exact mechanism recorded in session).
