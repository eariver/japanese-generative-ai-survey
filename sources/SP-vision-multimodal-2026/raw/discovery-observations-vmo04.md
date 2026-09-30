# Discovery observations — VM-O04 D04 spatial/geometry substrate (HARD CAP)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: REFUSED: NeRF, 3DGS, classical SLAM/SfM, full MVS survey, 3D object detection, SMPL-class human mesh, depth-benchmark zoos (KITTI/NYU/ETH3D are eval substrates only). DUSt3R successors add no new contract.

## VM-D019 — Towards Robust Monocular Depth Estimation / MiDaS (Ranftl et al.)
- Locator: https://arxiv.org/abs/1907.01341
- Source type: `arxiv_primary` | Published: `2019-07` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O04` | Modality: `image` | Role: `support-node`
- X axes: `X01`
- Claim notes: Scale/shift-invariant monocular/relative depth WITHOUT metric calibration; multi-dataset Pareto-mixing; zero-shot cross-dataset transfer as the robustness contract. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Relative depth only; metric claims need other sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial (control signals)
- repo: https://github.com/isl-org/MiDaS

## VM-D020 — OpenPose: Realtime Multi-Person 2D Pose (Cao et al.)
- Locator: https://arxiv.org/abs/1812.08008
- Source type: `arxiv_primary` | Published: `2018-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O04` | Modality: `image` | Role: `support-node`
- X axes: `X02`
- Claim notes: Part Affinity Fields bottom-up multi-person 2D pose (135 body/foot/hand/face keypoints); association-as-representation demonstration. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: 2D pose only; 3D lifting claims excluded by the cap.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D021 — Visual Genome (Krishna et al.)
- Locator: https://arxiv.org/abs/1602.07332
- Source type: `arxiv_primary` | Published: `2016-02` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O04`, `VM-O08` | Modality: `image` | Role: `support-node`
- X axes: `X01`, `X02`
- Claim notes: 108K images with dense objects/attributes/relations and WordNet-canonicalized scene graphs; region-description grounding data. Dual role: relational-structure node + grounding-data predecessor. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Annotation density claims are version-bound; GoldG-descent claims need GLIP-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D022 — DUSt3R: Geometric 3D Vision Made Easy (Wang et al.)
- Locator: https://arxiv.org/abs/2312.14132
- Source type: `arxiv_primary` | Published: `2023-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O04` | Modality: `image` | Role: `support-node`
- X axes: `X02`
- Claim notes: Camera-free pointmap regression unifying monocular/binocular reconstruction; geometry as network output state on pretrained Transformer init. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Successor variants (MASt3R-class) add no new contract; excluded by the minimum rule.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- repo: https://github.com/naver/dust3r
