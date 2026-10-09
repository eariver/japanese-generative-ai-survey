# Discovery observation — VM-D113 DINOv3 (materialized 2026-10-05, cutoff-bound)

Primary: DINOv3, Meta AI Research. arXiv:2508.10104v1 (2025-08-13).
Meta pages 2025-08-14 (publication/blog). Code: facebookresearch/dinov3.
Cutoff 2026-09-30: PASS (~13.5mo pre-cutoff).

- 7B-parameter SSL on LVD-1689M (1,689M hierarchical k-means + balanced sampling).
- Objective L_Pre = L_DINO + L_iBOT + 0.1*L_DKoleo; centering replaced by Sinkhorn-Knopp;
  axial RoPE; constant schedule, 1M iters.
- Dense feature degradation under long training (VOC mIoU peaks ~200k then declines);
  fixed by Gram anchoring (L_Gram on L2-normed patch Gram matrices vs early Gram-teacher).
- Post-hoc: resolution scaling, multi-student distillation (ViT-S/B/L/H+, ConvNeXt),
  dino.txt LiT-style text alignment.
- Inherited from DINOv2: DINO+iBOT discriminative SSL, multi-crop, Koleo, registers.
  Changed: 6x params / 12x data, RoPE, Sinkhorn, Gram refinement, distillation family.
- Frozen reusable dense representation (linear/attentive probes, no fine-tune).
