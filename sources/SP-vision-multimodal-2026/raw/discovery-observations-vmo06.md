# Discovery observations — VM-O06 D06 ViT/self-supervised foundation

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: Pre-ViT attention-in-vision (non-local networks) one line; instruction-tuning bridges live in D08; self-supervised-video pointer (V-JEPA) to D14 counterweight.

## VM-D030 — An Image is Worth 16x16 Words / ViT (Dosovitskiy et al.)
- Locator: https://arxiv.org/abs/2010.11929
- Source type: `arxiv_primary` | Published: `2020-10` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O06` | Modality: `image` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Convolution-to-sequence formulation of vision; precondition of all later vision-language token fusion. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Scale-dependent claims; data-efficiency debate needs DeiT-side sources.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D031 — DeiT (Touvron et al.)
- Locator: https://arxiv.org/abs/2012.12877
- Source type: `arxiv_primary` | Published: `2020-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O06` | Modality: `image` | Role: `bridge-node`
- X axes: `X01`
- Claim notes: Data-efficient training via distillation; architecture-vs-recipe debate exhibit. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short treatment; recipe reading supports X01.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D032 — Swin Transformer (Liu et al.)
- Locator: https://arxiv.org/abs/2103.14030
- Source type: `arxiv_primary` | Published: `2021-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O06` | Modality: `image` | Role: `hierarchy-node`
- X axes: `X02`
- Claim notes: Hierarchical vision Transformer with shifted windows; completeness node. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short treatment.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D033 — Masked Autoencoders / MAE (He et al.)
- Locator: https://arxiv.org/abs/2111.06377
- Source type: `arxiv_primary` | Published: `2021-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O06` | Modality: `image` | Role: `anchor`
- X axes: `X01`
- Claim notes: Masked label-free visual pretraining at scale. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Reconstruction-vs-representation reading; downstream transfer needs probe sources.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D034 — Emerging Properties in Self-Supervised Vision Transformers / DINO (Caron et al.)
- Locator: https://arxiv.org/abs/2104.14294
- Source type: `arxiv_primary` | Published: `2021-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O06` | Modality: `image` | Role: `anchor`
- X axes: `X01`
- Claim notes: Self-distillation with emergent object boundaries; OVD pseudo-label use downstream. ALWAYS qualify vs DINO detector. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Name collision hazard (CV2-DM-006 rule).
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D035 — DINOv2 (Oquab et al.)
- Locator: https://arxiv.org/abs/2304.07193
- Source type: `arxiv_primary` | Published: `2023-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O06` | Modality: `image` | Role: `anchor`
- X axes: `X01`
- Claim notes: All-purpose visual features at scale with curated data; SAM-contrast pole (features vs promptable interface). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Frozen-eval transfer claims are probe-bound; task-specific limits need eval sources.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D036 — Sigmoid Loss for Language Image Pre-Training / SigLIP (Zhai et al.)
- Locator: https://arxiv.org/abs/2303.15343
- Source type: `arxiv_primary` | Published: `2023-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O06`, `VM-O07` | Modality: `image` | Role: `encoder-lineage-node`
- X axes: `X01`
- Claim notes: Sigmoid-loss alignment; SigLIP2-So400m continued inside Qwen3-VL/Omni encoders (2026 reuse fact). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: SigLIP2 exact citation to be bound from Qwen-report references at Evidence.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
