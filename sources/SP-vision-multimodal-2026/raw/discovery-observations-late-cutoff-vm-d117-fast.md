# Discovery observation — VM-D117 FAST (materialized 2026-10-05, cutoff-bound)

Primary: FAST: Efficient Action Tokenization for VLA Models (Pertsch et al.).
arXiv:2501.09747v1 (2025-01-16). Cutoff 2026-09-30: PASS.

- Failure mode of per-dimension/per-timestep discretization for high-frequency actions.
- DCT frequency-space representation; action chunk compression (up to 13.2x on 50Hz);
  FAST+ universal tokenizer; BPE vocab 1024.
- Relationship to pi-zero/OpenVLA backbones; autoregressive vs flow-based trade-off
  (5x fewer GPU-hours vs diffusion; slower inference).
- Action representation/tokenization transition, not a general VLA system.
  Kept separate from pi-zero.
