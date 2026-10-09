# Discovery observation — VM-D122 Planning Limits (materialized 2026-10-05, cutoff-bound)

Primary: The Planning Limits of Latent World Models (Alrasheed et al., Univ. Melbourne).
arXiv:2609.39235v1 (2026-09-30, cutoff day itself → admissible).
Cutoff 2026-09-30: PASS.

- Cross-backbone action-conditioned predictor evaluation (V-JEPA 2/2.1, VideoMAEv2,
  VideoPrism, DINOv2) with plannable-range metric P*.
- Rollout horizon K vs usable planning horizon L (reliable only 5–10 steps vs 16–53 needed).
- Predictor scaling: 81× larger predicts better but plans no further.
- Perfect-prediction limit (simulator reference 92%→41%): closeness-score weakness, not error.
- Pure imagination vs MPC vs longer imagination vs expert-subgoal matrix; VLA
  candidate-action ranking (π₀ 65%→77%).
- Simulation + BridgeData real-robot offline coverage (offline only, not control).
