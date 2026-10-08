# Discovery observation — VM-D123 Deformable DETR (P02 bounded bridge intake)

- Locator: https://arxiv.org/abs/2010.04159 (v4, last revised 2021-03-18)
- Title: Deformable DETR: Deformable Transformers for End-to-End Object Detection
- Authors: Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang, Jifeng Dai
- Venue: ICLR 2021 Oral.
- Retrieved: arXiv abs page + experimental HTML full body (2026-10-08; abs verified,
  body consumed §§ Abstract/1/4-5 for the bounded bridge role).
- Observed technical role (DETR → efficient multi-scale sparse-attention bridge):
  DETR suffers slow convergence + limited feature spatial resolution from Transformer
  attention limits on image feature maps; deformable attention attends only a small
  set of key sampling points around a reference point; multi-scale features handled
  without FPN help (small objects from high-resolution maps); 10x fewer training
  epochs than DETR with better performance especially on small objects; code released.
- Obligation: VM-O02 (detection_structured_localization, lane d02).
- Boundary: source-local claims only until Evidence verification. No deformable-attention
  general survey; bridge role only.
