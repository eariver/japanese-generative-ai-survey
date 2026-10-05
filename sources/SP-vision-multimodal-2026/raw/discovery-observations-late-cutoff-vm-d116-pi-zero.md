# Discovery observation — VM-D116 pi-zero (materialized 2026-10-05, cutoff-bound)

Primary: pi-zero: A Vision-Language-Action Flow Model (Physical Intelligence).
arXiv:2410.24164v1 (2024-10-31). PI official blog/pi0.pdf. Cutoff 2026-09-30: PASS.

- Pretrained PaliGemma VLM backbone (3B) plus 300M flow-matching action expert.
- Flow-matching continuous action generation (50-step chunks, up to 50Hz);
  vs RT-2/OpenVLA autoregressive discrete action-token contracts.
- Multi-robot dexterous data regime (10,000+ hrs, 903M timesteps, 7 configs/68 tasks).
- Discrete language-like action token vs continuous flow-matching interface transition.
- No robotics control/hardware survey expansion.
