# Discovery observations — VM-O08 D07B open-vocabulary perception and grounding (FULL_WEIGHT)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: GoldG grounding-data composition deferred to Evidence; MDETR fine-tuned vs zero-shot REC is a protocol note; OWOD footnote per above.

## VM-D041 — Flickr30k Entities (Plummer et al.)
- Locator: https://openaccess.thecvf.com/content_iccv_2015/html/Plummer_Flickr30k_Entities_Collecting_ICCV_2015_paper.html
- Source type: `official_conference_paper` | Published: `2015-12` | Access: `PROCEEDINGS_OR_ANTHOLOGY_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `task-origin`
- X axes: `X01`, `X02`
- Claim notes: 244k coreference chains / 276k boxes; phrase-localization task origin (open-phrase-set localization akin to detection). [retrieval: PROCEEDINGS_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: People/animal-heavy domain bias; later OVD protocols generalize beyond it.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D042 — Modeling Context in Referring Expressions / RefCOCO (Yu et al.)
- Locator: https://aclanthology.org/D16-1212/
- Source type: `official_conference_paper` | Published: `2016-09` | Access: `PROCEEDINGS_OR_ANTHOLOGY_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `task-anchor`
- X axes: `X02`
- Claim notes: RefCOCO/+/g REC contract: single-referent disambiguation under relational/ambiguous description; grounding-precision metric home. [retrieval: ANTHOLOGY_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID corrected at intake (1606.03825 is a physics paper); fine-tuned vs zero-shot REC is a protocol difference, not a new node.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D043 — Open-Vocabulary Object Detection Using Captions / OVR-CNN (Zareian et al.)
- Locator: https://arxiv.org/abs/2011.10678
- Source type: `arxiv_primary` | Published: `2020-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `concept-origin`
- X axes: `X01`, `X02`
- Claim notes: Coins OVD: captions teach recognition (V2L + grounding/MLM/ITM pretraining), boxes teach localization; recognition/localization disentanglement. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: 'Open' is embedding-bounded in practice; later scaling poles qualify the claim.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D044 — Open-vocabulary Object Detection via Vision and Language Knowledge Distillation / ViLD (Gu et al.)
- Locator: https://arxiv.org/abs/2104.13921
- Source type: `arxiv_primary` | Published: `2021-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `transition-node`
- X axes: `X01`
- Claim notes: CLIP/ALIGN teacher distilled into two-stage detector (ViLD-text + ViLD-image); LVIS-rare 16.1 to 26.3 APr; open code. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Teacher-bounded; region-pretraining pole (RegionCLIP) is a different mechanism, kept separately.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/tensorflow/tpu (vild project)

## VM-D045 — RegionCLIP (Zhong et al.)
- Locator: https://arxiv.org/abs/2112.09106
- Source type: `arxiv_primary` | Published: `2021-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `variant-node`
- X axes: `X01`
- Claim notes: CLIP image-to-region domain-shift diagnosis; pseudo region-text pairs + contrastive region pretraining; COCO-novel 31.4 vs OVR 22.8. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Pseudo-label noise bounds; distinct from ViLD distillation (kept, not merged).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/microsoft/RegionCLIP

## VM-D046 — Detecting Twenty-thousand Classes using Image-level Supervision / Detic (Zhou et al.)
- Locator: https://arxiv.org/abs/2201.02605
- Source type: `arxiv_primary` | Published: `2022-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `variant-node`
- X axes: `X01`
- Claim notes: Image-level (ImageNet-21K) classifier training via max-size-proposal assignment; vocabulary-scaling pole. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID corrected at intake (Round B guess 2201.12280 wrong); assignment heuristic is the load-bearing detail.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/facebookresearch/detic

## VM-D047 — Grounded Language-Image Pre-training / GLIP (Li et al.)
- Locator: https://arxiv.org/abs/2112.03857
- Source type: `arxiv_primary` | Published: `2021-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Detection reformulated as phrase grounding; unified detection+grounding losses; GoldG grounding-data practice. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); GoldG composition deferred to Evidence.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D048 — MDETR (Kamath et al.)
- Locator: https://arxiv.org/abs/2104.12763
- Source type: `arxiv_primary` | Published: `2021-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `transition-node`
- X axes: `X01`, `X02`
- Claim notes: DETR conditioned on raw text queries; spans phrase grounding + REC + RES(PhraseCut) + GQA-adjacent; early-fusion pole; 1.3M-pair pretraining. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Modulated multi-task architecture vs GLIP data-practice reformulation: different contracts, both kept.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/ashkamath/mdetr

## VM-D049 — Simple Open-Vocabulary Object Detection with Vision Transformers / OWL-ViT (Minderer et al.)
- Locator: https://arxiv.org/abs/2205.06230
- Source type: `arxiv_primary` | Published: `2022-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `transition-node`
- X axes: `X02`
- Claim notes: Frozen CLIP + per-token heads; architecture-minimal late-fusion pole contrasting GLIP/MDETR early fusion. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); minimalism is the exhibit, not the endpoint.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D050 — Grounding DINO (Liu et al.)
- Locator: https://arxiv.org/abs/2303.05499
- Source type: `arxiv_primary` | Published: `2023-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `anchor`
- X axes: `X02`
- Claim notes: Three-phase tight fusion + sub-sentence features; detection + REC in one framework; ODinW record context. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); REC zero-shot call is an explicit evaluation note.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D051 — Scaling Open-Vocabulary Object Detection / OWL-ST/OWLv2 (Minderer et al.)
- Locator: https://arxiv.org/abs/2306.09683
- Source type: `arxiv_primary` | Published: `2023-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `scaling-node`
- X axes: `X01`
- Claim notes: N-gram machine label space + weak filtering to 1B+ pseudo-annotated examples; LVIS-rare 31.2 to 44.6%; code+checkpoints. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: 'Unseen' claim is label-space-sensitive; bind exactly (CV2-DM-020). Proceedings canonical: NeurIPS 2023.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D052 — Language-driven Semantic Segmentation / LSeg (Li et al.)
- Locator: https://arxiv.org/abs/2201.03546
- Source type: `arxiv_primary` | Published: `2022-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `branch-origin`
- X axes: `X01`, `X02`
- Claim notes: Pixel-text contrastive alignment origin for open-vocabulary segmentation. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Origin node; unification needs X-Decoder-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D053 — Generalized Decoding for Pixel, Image, and Language / X-Decoder (Zou et al.)
- Locator: https://openaccess.thecvf.com/content/CVPR2023/papers/Zou_Generalized_Decoding_for_Pixel_Image_and_Language_CVPR_2023_paper.pdf
- Source type: `official_conference_paper` | Published: `2023-06` | Access: `PROCEEDINGS_OR_ANTHOLOGY_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `branch-unification`
- X axes: `X02`
- Claim notes: Unified generic + referring segmentation + VL tasks without pseudo-labeling; 7-dataset open-vocab SOTA. [retrieval: PROCEEDINGS_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: OpenSeg is a named scaling variant (separate record below), not merged here.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D054 — Scaling Open-vocabulary Image Segmentation with Image-level Labels / OpenSeg (Ghiasi et al.)
- Locator: https://arxiv.org/abs/2112.12143
- Source type: `arxiv_primary` | Published: `2021-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `branch-variant`
- X axes: `X01`
- Claim notes: Image-level-label scaling variant of OVS; bounded variant per Round E (not equal-depth node). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Variant status; arXiv locator preferred over proceedings deep-link.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D055 — Open-Vocabulary Panoptic Segmentation with Text-to-Image Diffusion Models / ODISE (Xu et al.)
- Locator: https://arxiv.org/abs/2303.04803
- Source type: `arxiv_primary` | Published: `2023-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08` | Modality: `image-text` | Role: `branch-variant`
- X axes: `X01`, `X02`
- Claim notes: Frozen diffusion + discriminative backbones for open-vocabulary panoptic segmentation; diffusion-backbone pole with TS-002-crossover flag. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: TS-002 crossover must be policed per-paragraph at later stages.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial (diffusion backbone)
- repo: https://github.com/NVlabs/ODISE

## VM-D056 — LVIS: A Dataset for Large Vocabulary Instance Segmentation (Gupta et al.)
- Locator: https://arxiv.org/abs/1908.03195
- Source type: `arxiv_primary` | Published: `2019-08` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O08`, `VM-O16` | Modality: `image` | Role: `eval-authority`
- X axes: `X01`, `X04`
- Claim notes: LVIS-rare AP is the OVD eval home (base/common/frequent vs rare split); ODinW named as in-the-wild complement (context, no separate record). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Rare-split protocol must be bound per use; web-pretraining adjacency affects 'unseen' readings.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
