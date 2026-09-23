# TS-002 Discovery observations — D09 video generation lineage

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D070 — Video Diffusion Models (Ho et al.)

- Locator: https://arxiv.org/abs/2204.03458
- Published: 2022-04
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O09, BT-O02, BT-O06
- Summary: Factorized space-time diffusion for video; the diffusion-in-video transition paper. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Short-clip scope needs Imagen Video/Phenaki comparison.

## BT-D071 — Imagen Video: High Definition Video Generation with Diffusion Models (Ho et al.)

- Locator: https://arxiv.org/abs/2210.02303
- Published: 2022-10
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O09, BT-O06
- Summary: Cascaded spatial+temporal super-resolution video diffusion; duration/resolution scaling design. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Cascade cost needs latent-video successors.

## BT-D072 — Phenaki: Variable Length Video Generation from Open Domain Text (Villegas et al.)

- Locator: https://openreview.net/forum?id=vOEXS39nOF
- Published: 2022-09
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O09, BT-O01, BT-O06
- Summary: Causal C-ViViT tokenizer with masked bidirectional video transformer; variable-length/compressed-video thesis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Masked-prior quality needs diffusion-compressor comparison.

## BT-D073 — Make-A-Video: Text-to-Video Generation without Text-Video Data (Singer et al.)

- Locator: https://arxiv.org/abs/2209.14755
- Published: 2022-09
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O09, BT-O03
- Summary: T2I-leveraged video generation with spatiotemporal inflation; data-efficiency parallel invention. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Motion priors need VDM/Imagen Video comparison.

## BT-D074 — AnimateDiff: Animate Your Personalized Text-to-Image Diffusion (Guo et al.)

- Locator: https://arxiv.org/abs/2307.04790
- Published: 2023-07
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O09, BT-O05
- Summary: Plug-in motion module turning personalized T2I into animation; open-ecosystem motion adapter. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Motion-module generality needs personalization-model matrix.

## BT-D075 — Stable Video Diffusion: Scaling Latent Video Diffusion (Blattmann et al.)

- Locator: https://arxiv.org/abs/2311.15127
- Published: 2023-11
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O09, BT-O10
- Summary: Staged latent image-to-video diffusion with open weights; image-to-video mechanism reference. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Camera-motion control needs MotionCtrl comparison.

## BT-D076 — Movie Gen: A Cast of Media Foundation Models (Meta)

- Locator: https://ai.meta.com/research/publications/movie-gen-a-cast-of-media-foundation-models/
- Published: 2024-10
- Source class: PRIMARY_DOC / role: anchor / modality: video
- Obligations: BT-O09, BT-O06
- Summary: 30B video + 13B audio joint media foundation models with personalization/editing; synchronized-AV anchor. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: No public weights; capability claims need independent verification.

## BT-D077 — Sora: Creating video from text (OpenAI, technical overview)

- Locator: https://openai.com/index/sora/
- Published: 2024-02
- Source class: PRIMARY_ANNOUNCEMENT / role: anchor / modality: video
- Obligations: BT-O09, BT-O06
- Summary: Diffusion-transformer video with duration/resolution/composition claims; historical turning point (lifecycle retired 2026). [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Architecture undisclosed; lifecycle needs deprecation sources.
