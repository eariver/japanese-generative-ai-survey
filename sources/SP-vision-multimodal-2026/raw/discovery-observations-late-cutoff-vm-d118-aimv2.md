# Discovery observation — VM-D118 AIMv2 (materialized 2026-10-05, cutoff-bound)

Primary: AIMv2 (Apple). arXiv:2411.14402 (2024-11-21). CVPR 2025 Highlight.
Cutoff 2026-09-30: PASS.

- Autoregressive prefix-ViT plus causal multimodal decoder generating raw patches
  then text tokens; dense per-token signal without large-batch contrastive.
- Objective family distinct from masked (MAE), contrastive (CLIP/SigLIP),
  self-distillation (DINO/DINOv2/DINOv3). Frozen-trunk transfer.
- Residual-sweep admission: criteria 1–5 met (new objective contract).
