# TS-002 Discovery observations — D05 editing and preservation

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D044 — SDEdit: Guided Image Synthesis and Editing with SDEs (Meng et al.)

- Locator: https://arxiv.org/abs/2108.01049
- Published: 2021-08
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O05
- Summary: Noise-then-denoise stroke/image-guided editing; the editing-as-partial-diffusion formulation. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Stroke-fidelity limits need inpainting successors.

## BT-D045 — RePaint: Inpainting using Denoising Diffusion Probabilistic Models (Lugmayr et al.)

- Locator: https://arxiv.org/abs/2201.09865
- Published: 2022-01
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O05
- Summary: Mask-conditioned resampling inpainting; preservation-of-unmasked-content mechanism. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Sampling cost needs blended-latent successors.

## BT-D046 — Blended Latent Diffusion (Avrahami et al.)

- Locator: https://arxiv.org/abs/2206.02779
- Published: 2022-06
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O05
- Summary: Latent-space local editing with mask blending; resolution/speed improvement over pixel-space inpainting. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Region-boundary quality needs instruction-editing comparison.

## BT-D047 — Prompt-to-Prompt Image Editing with Cross-Attention Control (Hertz et al.)

- Locator: https://arxiv.org/abs/2208.01626
- Published: 2022-08
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O05, BT-O03
- Summary: Cross-attention map injection for prompt-driven local edits; attention-as-editing-interface thesis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Structure-preservation scope needs Imagic comparison.

## BT-D048 — Imagic: Text-Based Real Image Editing (Kawar et al.)

- Locator: https://arxiv.org/abs/2209.15146
- Published: 2022-09
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O05
- Summary: Optimization-based text editing of real images with interpolation control; edit-strength dial study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Optimization cost needs InstructPix2Pix comparison.

## BT-D049 — InstructPix2Pix: Learning to Follow Image Editing Instructions (Brooks et al.)

- Locator: https://arxiv.org/abs/2301.01780
- Published: 2023-01
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O05
- Summary: Instruction-following editing from synthetic paired data; multi-turn editing workflow origin. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Synthetic-pair bias needs reference-editing successors.

## BT-D050 — Tune-A-Video: One-Shot Tuning of Image Diffusion for Text-Driven Video Editing (Wu et al.)

- Locator: https://arxiv.org/abs/2212.11565
- Published: 2022-12
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O05, BT-O09, BT-O06
- Summary: One-shot T2I inflation for video editing; temporal-attention extension mechanism. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Consistency horizon needs long-video successors.
