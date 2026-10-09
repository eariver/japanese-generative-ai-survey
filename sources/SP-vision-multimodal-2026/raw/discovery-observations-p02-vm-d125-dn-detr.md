# Discovery observation — VM-D125 DN-DETR (P02 bounded bridge intake)

- Locator: https://arxiv.org/abs/2203.01305 (CVPR 2022 Oral; TPAMI 2024 extended version)
- Title: "DN-DETR: Accelerate DETR Training by Introducing Query DeNoising"
- Authors: Feng Li, Hao Zhang, Shilong Liu, Jian Guo, Lionel M. Ni, Lei Zhang
- Retrieved: arXiv abs identity verified (2026-10-08; note: 2206.03627 is NOT this
  paper — verified by retrieval, correct ID is 2203.01305) + CVPR open-access body
  consumed for the bounded bridge role (matching-instability diagnosis, denoising
  mechanism, DAB-DETR-based evaluation, Deformable-DETR generality result).
- Observed technical role (denoising-training bridge):
  slow convergence diagnosed as bipartite-graph-matching instability (inconsistent
  early optimization goals); noised GT boxes + labels fed to the Transformer decoder
  as a denoising part alongside the matching part; reconstruction of original targets;
  reduced matching difficulty / faster convergence; built on DAB-DETR 4D-anchor
  formulation (decoder embedding as label embedding); attention mask blocks leakage;
  +1.9 AP over DAB-DETR same setting (43.4/48.6 AP R50 at 12/50 epochs); parity at
  ~50% epochs; also applied to Deformable DETR (DN-Deformable-DETR), Anchor DETR,
  Faster R-CNN, Mask2Former.
- Obligation: VM-O02 (detection_structured_localization, lane d02).
- Boundary: source-local claims only until Evidence verification. Denoising here is
  query-denoising training, NOT diffusion-model denoising.
