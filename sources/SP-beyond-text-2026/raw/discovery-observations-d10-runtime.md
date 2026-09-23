# TS-002 Discovery observations — D10 runtime / deployment / acceleration

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D078 — Progressive Distillation for Fast Sampling of Diffusion Models (Salimans & Ho)

- Locator: https://arxiv.org/abs/2202.00512
- Published: 2022-02
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O10, BT-O02
- Summary: Iterative halving distillation of sampling steps; the distillation-for-few-step origin. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Distillation drift needs consistency/LCM comparison.

## BT-D079 — Latent Consistency Models (Luo et al.)

- Locator: https://arxiv.org/abs/2310.04378
- Published: 2023-10
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O10, BT-O02
- Summary: Consistency distillation in latent space for few-step inference; open few-step recipe. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Few-step quality needs ADD comparison.

## BT-D080 — LCM-LoRA: A Universal Stable-Diffusion Acceleration Module (Luo et al.)

- Locator: https://arxiv.org/abs/2311.05556
- Published: 2023-11
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O10, BT-O04
- Summary: LoRA-parameterized consistency acceleration; portable few-step module for the open ecosystem. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Module generality needs per-model validation.

## BT-D081 — SDXL-Turbo / Adversarial Diffusion Distillation (Sauer et al.)

- Locator: https://arxiv.org/abs/2311.17049
- Published: 2023-11
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O10, BT-O02
- Summary: Adversarial post-training for 1-4 step synthesis; hybrid adversarial-distillation thesis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Mode-coverage cost needs consistency comparison.

## BT-D082 — MobileDiffusion: Subsecond Text-to-Image on Mobile (Zhao et al.)

- Locator: https://arxiv.org/abs/2311.16567
- Published: 2023-11
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O10
- Summary: On-device diffusion with architectural/compression co-design; deployment-envelope study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Device-specific numbers need hardware binding at Evidence stage.
