# Discovery observation — VM-D121 V-JEPA 2 / V-JEPA 2-AC (materialized 2026-10-05, cutoff-bound)

Primary: V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and
Planning (Meta FAIR + Mila). arXiv:2506.09985v1 (2025-06-11). Blog + code
facebookresearch/vjepa2. Cutoff 2026-09-30: PASS.

- ONE two-stage contract (do not split): Stage-1 V-JEPA 2 action-free JEPA pretraining
  (mask-denoising in representation space, >1M hours video, ViT-L 300M → ViT-g 1B)
  plus Stage-2 V-JEPA 2-AC frozen-encoder latent action-conditioned predictor
  (~300M, block-causal, trained on 62h unlabeled DROID).
- Image-goal planning / action selection via MPC energy minimization (CEM,
  receding-horizon); zero-shot Franka deployment; LLM alignment for VideoQA.
- Inherits V-JEPA mask-predict/EMA/frozen-probe protocol; new: 3D-RoPE, data/model
  scale, AC post-training + planning use.
- No general robotics expansion.
