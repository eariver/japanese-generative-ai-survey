# Discovery observation — VM-D124 DAB-DETR (P02 bounded bridge intake)

- Locator: https://arxiv.org/abs/2201.12329 (v4, last revised 2022-03-30)
- Title: "DAB-DETR: Dynamic Anchor Boxes are Better Queries for DETR"
- Authors: Shilong Liu, Feng Li, Hao Zhang, Xiao Yang, Xianbiao Qi, Hang Su, Jun Zhu, Lei Zhang
- Venue: ICLR 2022.
- Retrieved: arXiv abs page (2026-10-08; verified) + abstract/body claims consumed for
  the bounded bridge role (query formulation, dynamic updates, COCO result).
- Observed technical role (query representation / dynamic-anchor bridge):
  decoder queries directly formulated as 4D box coordinates (x, y, w, h) and
  dynamically updated layer-by-layer; explicit positional priors improve
  query-to-feature similarity and convergence; width/height modulate positional
  attention; queries read as layer-by-layer cascade soft ROI pooling; 45.7 AP on
  COCO with ResNet50-DC5 at 50 epochs (best among DETR-like under same setting);
  code released.
- Obligation: VM-O02 (detection_structured_localization, lane d02).
- Boundary: source-local claims only until Evidence verification. No Anchor DETR /
  Conditional DETR / full-successor-taxonomy expansion; included only because
  detector-DINO explicitly uses this branch.
