# Discovery observation — VM-D114 SigLIP 2 (materialized 2026-10-05, cutoff-bound)

Primary: SigLIP 2 (Zhai et al., Google DeepMind). arXiv:2502.14786v1 (2025-02-20).
Big Vision release/checkpoints. Cutoff 2026-09-30: PASS.

- Keeps SigLIP sigmoid per-pair loss; staged combination with captioning (LocCa decoder),
  self-distillation (SILC local-to-global), masked prediction (TIPS/DINO-line).
- Online/active data curation (ACID implicit distillation for small models).
- Multilingual WebLI mixture (109 langs) with de-bias filtering; Gemma tokenizer.
- Native aspect ratio + multi-resolution (NaFlex); localization/detection transfer
  (RefCOCO grounding, OWL-ViT open-vocab detection, dense probes).
- VLM visual-encoder transfer (PaliGemma-style frozen-encoder gains over SigLIP).
- Gains attributed to recipe combination, not a new loss.
