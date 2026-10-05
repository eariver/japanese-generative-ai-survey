# Discovery observation — VM-D115 SAM 3 (materialized 2026-10-05, cutoff-bound)

Primary: SAM 3: Segment Anything with Concepts (Meta Superintelligence Labs).
Meta page 2025-11-19; arXiv:2511.16719 (v1 2025-11-20). Code: facebookresearch/sam3.
Cutoff 2026-09-30: PASS. SAM 3D excluded; SAM 3.1 successor-context only.

- Promptable Concept Segmentation: detect/segment/track all instances of a visual
  concept in image or short video; masks + unique identities.
- Prompts: simple text noun phrases, image exemplars (positive/negative boxes),
  visual clicks (SAM 2-style refinement, propagated across video).
- Image-level DETR-paradigm detector; memory-based SAM 2-style video tracker;
  shared Perception Encoder backbone; recognition/localization decoupling
  (presence token × per-query match).
- Inherits SAM/SAM2 PVS machinery; novelty is the language-grounded concept interface.
