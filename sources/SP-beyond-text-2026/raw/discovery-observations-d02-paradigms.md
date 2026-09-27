# TS-002 Discovery observations — D02 generative paradigms / objectives

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D013 — Generative Adversarial Networks (Goodfellow et al.)

- Locator: https://arxiv.org/abs/1406.2661
- Published: 2014-06
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Adversarial generator/discriminator formulation; the quality/diversity/stability axis origin for all later media paradigms. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Modern role is vocoder/autoencoder/post-training hybrid, not standalone SOTA.

## BT-D014 — Unsupervised Representation Learning with Deep Convolutional GANs (DCGAN) (Radford et al.)

- Locator: https://arxiv.org/abs/1511.06434
- Published: 2015-11
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Convolutional GAN stabilization recipe; the first broadly reproducible high-fidelity image GAN baseline. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Stability analysis superseded by StyleGAN-era engineering.

## BT-D015 — Progressive Growing / Style-Based Generator (StyleGAN) (Karras et al.)

- Locator: https://arxiv.org/abs/1812.04958
- Published: 2018-12
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O04
- Summary: Style-based generator with disentangled latent control; high-fidelity and controllability landmark before diffusion. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Latent-editability claims need StyleGAN2/alias-free successors.

## BT-D016 — Analyzing and Improving the Image Quality of StyleGAN (StyleGAN2) (Karras et al.)

- Locator: https://arxiv.org/abs/1912.04958
- Published: 2019-12
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Artifact removal and quality redesign of the style generator; the GAN quality ceiling diffusion had to beat. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Comparison with diffusion needs matched-resolution/budget discipline.

## BT-D017 — Pixel Recurrent Neural Networks (van den Oord et al.)

- Locator: https://arxiv.org/abs/1601.06759
- Published: 2016-01
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Fully autoregressive pixel generation; likelihood-tractable origin showing why raw-sequence modeling is expensive. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Sequential cost argument needs Image Transformer/diagonal-BiLSTM follow-ups.

## BT-D018 — Image Transformer (Parmar et al.)

- Locator: https://arxiv.org/abs/1802.05751
- Published: 2018-02
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Self-attention autoregressive image modeling; transformer-prior precedent for later DiT/denoiser backbones. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Local-attention limits need full-attention DiT comparison.

## BT-D019 — Denoising Diffusion Probabilistic Models (Ho et al.)

- Locator: https://arxiv.org/abs/2006.11239
- Published: 2020-06
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O10
- Summary: Fixed-forward diffusion with learned reverse denoising; the sampling-cost-vs-quality contract all accelerators renegotiate. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Step-cost claims need DDIM/distillation successors.

## BT-D020 — Denoising Diffusion Implicit Models (DDIM) (Song et al.)

- Locator: https://arxiv.org/abs/2010.02502
- Published: 2020-10
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O10
- Summary: Non-Markovian implicit sampling cutting DDPM steps; the first general sampling-efficiency transition. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Step/quality curve needs LCM/consistency successors.

## BT-D021 — Score-Based Generative Modeling through SDEs (Song et al.)

- Locator: https://arxiv.org/abs/2011.13456
- Published: 2020-11
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Continuous-time score-SDE unification of diffusion/score models; solver/predictor-corrector design space. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Solver claims need EDM successor comparison.

## BT-D022 — Elucidating the Design Space of Diffusion-Based Generative Models (EDM) (Karras et al.)

- Locator: https://arxiv.org/abs/2206.00364
- Published: 2022-06
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O10
- Summary: Modular diffusion design space with preconditioning/schedule/solver ablations; engineering reference for later denoisers. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Ablations are image-domain; audio/video transfer needs modality sources.

## BT-D023 — High-Resolution Image Synthesis with Latent Diffusion Models (Rombach et al.)

- Locator: https://arxiv.org/abs/2112.10752
- Published: 2021-12
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O01
- Summary: Perceptual-latent diffusion separating autoencoder compression from denoising prior; the latent-diffusion era transition. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Cross-attention conditioning role needs D03 sources.

## BT-D024 — Stable Diffusion public implementation (Stability-AI/stablediffusion)

- Locator: https://github.com/Stability-AI/stablediffusion
- Published: 2022-08
- Source class: PRIMARY_REPO / role: anchor / modality: image
- Obligations: BT-O02, BT-O10
- Summary: Reference open implementation/weights of latent diffusion; deployment/ecosystem anchor for local execution. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Repo is versioned; exact tag/commit must be bound at Evidence stage.

## BT-D025 — Scalable Diffusion Models with Transformers (DiT) (Peebles & Xie)

- Locator: https://arxiv.org/abs/2212.09748
- Published: 2022-12
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Transformer denoiser replacing U-Net with scaling laws; backbone-vs-objective separation landmark. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Scaling claims need SiT/flow successors.

## BT-D026 — Scalable Interpolant Transformers (SiT) (Ma et al.)

- Locator: https://arxiv.org/abs/2401.08740
- Published: 2024-01
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02
- Summary: Interpolant/flow objective on transformer backbone; diffusion-to-flow bridge evidence. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Flow-vs-diffusion gaps need rectified-flow comparison.

## BT-D027 — Flow Matching for Generative Modeling (Lipman et al.)

- Locator: https://arxiv.org/abs/2210.02747
- Published: 2022-10
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O10
- Summary: Simulation-free continuous normalizing flow training; straighter-trajectory sampling-efficiency thesis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Trajectory-straightness measurement needs rectified-flow reflow sources.

## BT-D028 — Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow (Liu et al.)

- Locator: https://arxiv.org/abs/2209.03003
- Published: 2022-09
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O10
- Summary: Rectified-flow straightening with reflow distillation; few-step lineage feeding current flow-era generators. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Reflow cost accounting needs LCM/consistency comparison.

## BT-D029 — Consistency Models (Song et al.)

- Locator: https://arxiv.org/abs/2303.01469
- Published: 2023-03
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O10
- Summary: Self-consistent few-step generation by direct trajectory mapping; distillation-free acceleration axis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Few-step quality needs LCM/ADD empirical comparison.

## BT-D030 — Diffusion Models Beat GANs on Image Synthesis (ADM) (Dhariwal & Nichol)

- Locator: https://arxiv.org/abs/2105.05233
- Published: 2021-05
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O02, BT-O03
- Summary: ADM with classifier guidance beating GANs on ImageNet; guidance-as-capability turning point. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Guidance mechanism needs classifier-free successor.
