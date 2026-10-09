# Discovery observations — VM-O01 D01 learned visual representation (CONTEXT_CAPPED)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: SIFT/HOG/bag-of-words cited as named context only; VGG/GoogLeNet are depth-scaling footnotes at most; no further mechanism nodes.

## VM-D001 — Neocognitron (Fukushima)
- Locator: https://doi.org/10.1007/BF00344251
- Source type: `official_publisher_page` | Published: `1980` | Access: `PUBLISHER_OR_AUTHOR_PAGE_VERIFIED`
- Obligations: `VM-O01` | Modality: `image` | Role: `predecessor-context`
- X axes: `X01`
- Claim notes: Hierarchical shift-invariant feature extraction with S-/C-cells; the conceptual origin of convolutional feature hierarchies. [retrieval: PUBLISHER_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Paywalled journal page; mechanism detail stays at context level per D01 cap; no performance claims carried.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D002 — Gradient-Based Learning Applied to Document Recognition (LeCun et al.)
- Locator: http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf
- Source type: `official_publisher_page` | Published: `1998-11` | Access: `PUBLISHER_OR_AUTHOR_PAGE_VERIFIED`
- Obligations: `VM-O01` | Modality: `image` | Role: `predecessor-context`
- X axes: `X01`, `X02`
- Claim notes: LeNet CNN trained end-to-end with gradient backprop on document characters; establishes learned hierarchies over handcrafted features for a real task. [retrieval: AUTHOR_PDF_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Document-domain scope; later scaling claims need ImageNet-era sources, not this paper alone.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D003 — ImageNet Classification with Deep CNNs (Krizhevsky, Sutskever, Hinton)
- Locator: https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks
- Source type: `official_conference_paper` | Published: `2012-09` | Access: `PROCEEDINGS_OR_ANTHOLOGY_VERIFIED`
- Obligations: `VM-O01` | Modality: `image` | Role: `anchor`
- X axes: `X01`, `X03`
- Claim notes: Large deep CNN + efficient GPU convolution + 1.2M-image ImageNet classification; the large-scale supervised + compute-scaling break. [retrieval: PROCEEDINGS_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Recipe reading (data+GPU+depth) vs architectural novelty must be preserved; no transfer claims beyond what successors establish.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D004 — Deep Residual Learning for Image Recognition (He et al.)
- Locator: https://arxiv.org/abs/1512.03385
- Source type: `arxiv_primary` | Published: `2015-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O01` | Modality: `image` | Role: `anchor`
- X axes: `X01`
- Claim notes: Residual reframing of deep-network optimization enabling 100+ layer training; demonstrated transfer to detection/segmentation workloads. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Optimization-break reading; later pretraining-recipe debates (DeiT/Swin) qualify any architecture-triumphalism.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
