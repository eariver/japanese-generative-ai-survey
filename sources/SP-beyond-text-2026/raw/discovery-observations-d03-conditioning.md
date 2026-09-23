# TS-002 Discovery observations — D03 conditioning / semantic alignment

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D011 — Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding (Imagen) (Saharia et al.)

- Locator: https://arxiv.org/abs/2205.11487
- Published: 2022-05
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O03, BT-O01
- Summary: Cascaded diffusion with large frozen text encoders; T5-vs-CLIP encoder finding that anchors conditioning-encoder choices. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Encoder finding is era-specific; native-multimodal successors differ.

## BT-D031 — Learning Transferable Visual Models (CLIP) (Radford et al.)

- Locator: https://arxiv.org/abs/2103.00020
- Published: 2021-02
- Source class: PRIMARY_PAPER / role: anchor / modality: crossmodal
- Obligations: BT-O03, BT-O11
- Summary: Contrastive image-text pretraining; the semantic encoder behind conditioning and alignment metrics. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Generation-relevance only; perception history belongs to TS-003.

## BT-D032 — Classifier-Free Diffusion Guidance (Ho & Salimans)

- Locator: https://arxiv.org/abs/2207.12598
- Published: 2022-07
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O03
- Summary: Joint conditional/unconditional training with inference-time guidance scale; the dominant text-adherence control. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Guidance-scale/diversity trade-off needs GLIDE/eDiff-I comparison.

## BT-D033 — GLIDE: Text-Guided Diffusion (Nichol et al.)

- Locator: https://arxiv.org/abs/2112.02092
- Published: 2021-12
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O03, BT-O05
- Summary: Text-guided diffusion with CLIP-guidance vs classifier-free comparison plus inpainting/editing extension. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Guidance comparison is era-specific; inpainting role cross-tags O05.

## BT-D034 — eDiff-I: Ensemble of Expert Denoisers (Balaji et al.)

- Locator: https://arxiv.org/abs/2211.12572
- Published: 2022-11
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O03
- Summary: Ensemble of specialized denoisers with T5/CLIP/Imagen encoders; conditioning-encoder composition study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Expert-mixture cost needs efficiency accounting.

## BT-D035 — CLAP: Contrastive Language-Audio Pretraining (Elizalde et al.)

- Locator: https://arxiv.org/abs/2206.04769
- Published: 2022-06
- Source class: PRIMARY_PAPER / role: anchor / modality: audio
- Obligations: BT-O03, BT-O11, BT-O08
- Summary: Text-audio joint embedding for conditioning and text-audio alignment evaluation. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Alignment-metric validity needs FAD/human-study comparison.
