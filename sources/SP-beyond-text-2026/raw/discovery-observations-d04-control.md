# TS-002 Discovery observations — D04 controllability / reference / identity

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D036 — Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet) (Zhang et al.)

- Locator: https://arxiv.org/abs/2302.05543
- Published: 2023-02
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O04
- Summary: Zero-convolution spatial-control adapter over frozen diffusion; the control-signal-fidelity transition. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Single-control framing; multi-reference needs IP-Adapter successors.

## BT-D037 — T2I-Adapter: Learning Adapters to Dig Out More Controllable Ability (Mou et al.)

- Locator: https://arxiv.org/abs/2302.08453
- Published: 2023-02
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O04
- Summary: Lightweight adapter alternative for spatial control; adapter-vs-finetune cost comparison point. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Adapter-capacity limits need ControlNet comparison.

## BT-D038 — IP-Adapter: Text-Compatible Image Prompt Adapter (Ye et al.)

- Locator: https://arxiv.org/abs/2308.06721
- Published: 2023-08
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O04, BT-O05
- Summary: Decoupled image-prompt adapter for reference/style/content control; reference-conditioning mechanism. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Identity-preservation measurement needs DreamBooth/eval successors.

## BT-D039 — DreamBooth: Personalization of Text-to-Image Diffusion (Ruiz et al.)

- Locator: https://arxiv.org/abs/2208.04111
- Published: 2022-08
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O04, BT-O05
- Summary: Few-shot subject personalization with prior-preservation loss; identity-preservation origin. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Overfitting/preservation trade-off needs LoRA comparison.

## BT-D040 — LoRA: Low-Rank Adaptation of Large Language Models (Hu et al.)

- Locator: https://arxiv.org/abs/2106.09685
- Published: 2021-06
- Source class: PRIMARY_PAPER / role: anchor / modality: crossmodal
- Obligations: BT-O04
- Summary: Low-rank adapter method widely adopted for media personalization/control; parameter-efficient control surface. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Media-specific behavior needs diffusion-LoRA adoption sources.

## BT-D041 — Semantic Image Synthesis with Spatially-Adaptive Normalization (SPADE/GauGAN) (Park et al.)

- Locator: https://arxiv.org/abs/1903.07291
- Published: 2019-03
- Source class: PRIMARY_PAPER / role: anchor / modality: image
- Obligations: BT-O04
- Summary: Spatially-adaptive normalization for layout-to-image control; pre-diffusion spatial-control precursor. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Precursor status; diffusion-era transfer needs ControlNet linkage.

## BT-D042 — MotionCtrl: Controllable Camera and Object Motion (Wang et al.)

- Locator: https://arxiv.org/abs/2311.17058
- Published: 2023-11
- Source class: PRIMARY_PAPER / role: anchor / modality: video
- Obligations: BT-O04, BT-O09, BT-O06
- Summary: Decoupled camera/object motion control for video diffusion; temporal-control mechanism with trajectory conditioning. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Camera-pose evaluation needs video-eval successors.

## BT-D043 — Music ControlNet (Wu et al.)

- Locator: https://arxiv.org/abs/2311.15049
- Published: 2023-11
- Source class: PRIMARY_PAPER / role: anchor / modality: music
- Obligations: BT-O04, BT-O08
- Summary: Time-varying melody/dynamics/rhythm control for music diffusion; audio-domain control-signal study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Control disentanglement needs Mustango comparison.
