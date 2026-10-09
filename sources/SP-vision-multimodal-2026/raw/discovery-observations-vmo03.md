# Discovery observations — VM-O03 D03 dense perception / segmentation

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: Interactive-segmentation predecessors (DEXTR/RITM-class) as one-line context; OVS branch lives in D07B with cross-ref here; panoptic at definition depth.

## VM-D013 — Fully Convolutional Networks for Semantic Segmentation (Long et al.)
- Locator: https://arxiv.org/abs/1411.4038
- Source type: `arxiv_primary` | Published: `2014-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O03` | Modality: `image` | Role: `anchor`
- X axes: `X02`
- Claim notes: Dense-prediction origin: fully convolutional training with skip fusion for pixel labeling. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Coarse boundaries; successor refinement needed for later claims.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D014 — U-Net (Ronneberger et al.)
- Locator: https://arxiv.org/abs/1505.04597
- Source type: `arxiv_primary` | Published: `2015-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O03` | Modality: `image` | Role: `context-node`
- X axes: `X02`
- Claim notes: Encoder-decoder with skip connections for segmentation; vision role ONLY — TS-002 diffusion-backbone role explicitly excluded. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: One cross-reference sentence to the TS-002 role; no mechanism duplication.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial (backbone role, different question)

## VM-D015 — Mask R-CNN (He et al.)
- Locator: https://arxiv.org/abs/1703.06870
- Source type: `arxiv_primary` | Published: `2017-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O03` | Modality: `image` | Role: `anchor`
- X axes: `X02`
- Claim notes: Instance-segmentation bridge: parallel mask head on Faster R-CNN with RoIAlign. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Box-dependent; the box-free dense pole needs FCN/SAM-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D016 — Panoptic Segmentation (Kirillov et al.)
- Locator: https://arxiv.org/abs/1801.00868
- Source type: `arxiv_primary` | Published: `2018-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O03` | Modality: `image` | Role: `contract-node`
- X axes: `X02`
- Claim notes: Semantic-vs-instance unification contract (stuff+things, PQ metric). Definition + citation depth only. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Contract clarity, not mechanism; no depth beyond the task definition.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D017 — Segment Anything (Kirillov et al.)
- Locator: https://arxiv.org/abs/2304.02643
- Source type: `arxiv_primary` | Published: `2023-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O03` | Modality: `image` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Promptable task/model/SA-1B (>1B masks) system explicitly targeting zero-shot transfer; first vision-foundation-model event. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Carry BOTH readings (foundation model vs task-bounded annotation engine); downstream evals adjudicate per task.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/facebookresearch/segment-anything

## VM-D018 — SAM 2: Segment Anything in Images and Videos (Ravi et al.)
- Locator: https://arxiv.org/abs/2408.00714
- Source type: `arxiv_primary` | Published: `2024-08` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O03`, `VM-O12` | Modality: `video` | Role: `bridge-node`
- X axes: `X02`
- Claim notes: Streaming-memory architecture extending promptable segmentation to video; D03->D11 bridge pointer. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Architecture pointer, not a streaming-system case; system-case status decided by R5 anchors.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
