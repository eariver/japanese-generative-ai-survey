# TS-002 Discovery observations — D01 media representation / compression / tokenization

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D001 — Auto-Encoding Variational Bayes (VAE) (Kingma & Welling)

- Locator: https://arxiv.org/abs/1312.6114
- Published: 2013-12
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O01, BT-O02
- Summary: Amortized variational inference with the reparameterization trick; continuous latent spaces that later image/audio/video autoencoders inherit. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Foundational method; downstream compression/fidelity claims need first-stage autoencoder sources, not this paper alone.

## BT-D002 — Neural Discrete Representation Learning (VQ-VAE) (van den Oord et al.)

- Locator: https://arxiv.org/abs/1711.00937
- Published: 2017-11
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O01, BT-O02
- Summary: Discrete codebook latents via vector quantization; the discrete-representation origin for VQGAN, neural codecs and video tokenizers. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Codebook collapse/usage trade-offs need successor sources.

## BT-D003 — Generating Diverse High-Fidelity Images with VQ-VAE-2 (Razavi et al.)

- Locator: https://arxiv.org/abs/1906.00446
- Published: 2019-06
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O01, BT-O02
- Summary: Hierarchical discrete codes scaling VQ-VAE to high-fidelity image generation; multi-scale codebook precedent. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Hierarchical-code cost/coverage needs comparison with single-scale successors.

## BT-D004 — Taming Transformers for High-Resolution Image Synthesis (VQGAN) (Esser et al.)

- Locator: https://arxiv.org/abs/2012.09812
- Published: 2020-12
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O01, BT-O02
- Summary: Perceptual-adversarial discrete tokenizer plus autoregressive transformer prior; the tokenizer quality bar for latent image modeling. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Reconstruction-vs-generation split needs first-stage vs prior ablations.

## BT-D005 — Zero-Shot Text-to-Image Generation (dVAE) (Ramesh et al.)

- Locator: https://arxiv.org/abs/2102.12092
- Published: 2021-02
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O01, BT-O03
- Summary: Discrete dVAE visual tokens jointly modeled with text; text-conditioned discrete representation precedent. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: dVAE compression ceiling superseded by VQGAN/clip-latent successors.

## BT-D006 — SoundStream: An End-to-End Neural Audio Codec (Zeghidour et al.)

- Locator: https://arxiv.org/abs/2107.03312
- Published: 2021-07
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O01, BT-O07
- Summary: End-to-end neural codec with residual vector quantization; the RVQ design that EnCodec/DAC and codec-LM speech systems build on. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Rate/quality points need EnCodec/DAC successor comparison.

## BT-D007 — High Fidelity Neural Audio Compression (EnCodec) (Defossez et al.)

- Locator: https://arxiv.org/abs/2210.13438
- Published: 2022-10
- Source class: PRIMARY_PAPER / role: anchor / modality: audio
- Obligations: BT-O01, BT-O07, BT-O08
- Summary: Multistream RVQ codec with adversarial/perceptual losses; the standard token rate/quality reference for codec-language-model audio. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Semantic-vs-acoustic split needs AudioLM-style hybrid sources.

## BT-D008 — High-Fidelity Audio Compression with Improved RVQGAN (Descript Audio Codec, DAC) (Kumar et al.)

- Locator: https://arxiv.org/abs/2306.06546
- Published: 2023-06
- Source class: PRIMARY_PAPER / role: anchor / modality: audio
- Obligations: BT-O01, BT-O08
- Summary: Improved RVQGAN codec raising reconstruction fidelity; successor datapoint on the codec rate/quality frontier. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Generation-downstream effect needs AudioLM-successor adoption evidence.

## BT-D009 — AudioLM: a Language Modeling Approach to Audio Generation (Borsos et al.)

- Locator: https://arxiv.org/abs/2209.03143
- Published: 2022-09
- Source class: PRIMARY_PAPER / role: anchor / modality: audio
- Obligations: BT-O01, BT-O08, BT-O07
- Summary: Hybrid semantic-plus-acoustic tokenization for audio language modeling; the separation thesis for structure vs fidelity. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Long-form structure claims need MusicLM/MusicGen successors.

## BT-D010 — Language-Neutral VQ-VAE Video Tokenizer (MAGVIT) (Yu et al.)

- Locator: https://arxiv.org/abs/2212.05199
- Published: 2022-12
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O01, BT-O09, BT-O06
- Summary: 3D-VQ video tokenizer for masked generative video modeling; spatiotemporal compression precedent for video transformers. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Masked-prior vs diffusion-prior comparison needs successor coverage.

## BT-D012 — Wan2.2-VAE: high-compression video VAE (Wan-Video)

- Locator: https://github.com/Wan-Video/Wan2.2
- Published: 2025-07
- Source class: PRIMARY_REPO / role: anchor / modality: video
- Obligations: BT-O01, BT-O09, BT-O10
- Summary: Open-weight MoE video family with high-compression VAE (4x16x16, total 4x32x32 with patchification); TI2V-5B runs 5s 720P on a single consumer GPU. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Open line stops at 2.2; 2.5/2.6/2.7/3.0 are API-only (see lifecycle note).
