# Discovery observations — VM-O02 D02 detection / structured localization

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: One-stage history beyond YOLO (RetinaNet/SSD kept as nodes); OWOD (Joseph 2021, unknown-aware) stays a D07B footnote; anchors/NMS read as fossilized machinery.

## VM-D005 — Rich feature hierarchies (R-CNN) (Girshick et al.)
- Locator: https://arxiv.org/abs/1311.2524
- Source type: `arxiv_primary` | Published: `2013-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02` | Modality: `image` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Region proposals + CNN features + classifiers; the region-proposal detection origin. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Multi-stage pipeline slowness superseded; historical role only.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D006 — Faster R-CNN (Ren et al.)
- Locator: https://arxiv.org/abs/1506.01497
- Source type: `arxiv_primary` | Published: `2015-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02` | Modality: `image` | Role: `anchor`
- X axes: `X02`
- Claim notes: Region Proposal Network sharing convolution with the detector; two-stage capstone. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Anchor/NMS machinery becomes the fossilized assumption DETR later removes; record as mechanism, not endpoint.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D007 — You Only Look Once (Redmon et al.)
- Locator: https://arxiv.org/abs/1506.02640
- Source type: `arxiv_primary` | Published: `2015-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02` | Modality: `image` | Role: `anchor`
- X axes: `X02`, `X03`
- Claim notes: Single-shot regression framing of detection; the one-stage operating-point origin (not the whole one-stage history). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Later YOLO versions are distinct products; bind version for any performance claim; latency/accuracy trade-off reading required.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D008 — SSD: Single Shot MultiBox Detector (Liu et al.)
- Locator: https://arxiv.org/abs/1512.02325
- Source type: `arxiv_primary` | Published: `2015-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02` | Modality: `image` | Role: `lineage-completeness`
- X axes: `X02`
- Claim notes: Multi-scale default boxes in a single shot; the non-YOLO one-stage branch. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Completeness node; short treatment.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D009 — Focal Loss / RetinaNet (Lin et al.)
- Locator: https://arxiv.org/abs/1708.02002
- Source type: `arxiv_primary` | Published: `2017-08` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02` | Modality: `image` | Role: `lineage-completeness`
- X axes: `X02`
- Claim notes: Dense-detection foreground/background imbalance treatment via focal loss. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Completeness node; short treatment.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D010 — End-to-End Object Detection with Transformers / DETR (Carion et al.)
- Locator: https://arxiv.org/abs/2005.12872
- Source type: `arxiv_primary` | Published: `2020-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02` | Modality: `image` | Role: `anchor`
- X axes: `X02`
- Claim notes: Detection as direct set prediction with Transformer encoder-decoder; removes anchor generation/NMS hand-design. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Training-data hunger and small-object behavior need successor sources; not a standalone endpoint.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D011 — DINO: DETR with Improved DeNoising Anchor Boxes (Zhang et al.)
- Locator: https://arxiv.org/abs/2203.03605
- Source type: `arxiv_primary` | Published: `2022-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02`, `VM-O08` | Modality: `image` | Role: `successor-node`
- X axes: `X02`
- Claim notes: DETR-lineage capstone and the technical base of Grounding DINO. ALWAYS qualify vs DINO self-supervised (CV2-DM-006 rule). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Name collision hazard; every prose occurrence must carry the detector qualifier.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D012 — YOLO-World: Real-Time Open-Vocabulary Object Detection (Cheng et al.)
- Locator: https://arxiv.org/abs/2401.17270
- Source type: `arxiv_primary` | Published: `2024-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O02`, `VM-O08` | Modality: `image` | Role: `bridge-case`
- X axes: `X01`, `X02`
- Claim notes: GLIP-formulation open-vocabulary detection inside the YOLO operating point; D02->D07B bridge exhibit. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Do not confuse with the YOLO product line; version-bound claims only.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- arch_role: ARCHITECTURE_CASE candidate (open)
