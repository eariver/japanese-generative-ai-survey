# Discovery observations — VM-O07 D07A image-level alignment

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: DeViSE (Frome et al., NIPS 2013, visual-semantic embedding origin) is NAMED PREDECESSOR CONTEXT without a standalone record: its joint-space contract is covered by the VQA-era discussion and the CLIP break narrative; no separate locator bound at intake.

## VM-D037 — Show and Tell (Vinyals et al.)
- Locator: https://arxiv.org/abs/1411.4555
- Source type: `arxiv_primary` | Published: `2014-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O07` | Modality: `image-text` | Role: `predecessor-node`
- X axes: `X01`
- Claim notes: Captioning predecessor: CNN encoder to RNN decoder generation; anti-CLIP-abruptness context. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short treatment; generation-side detail stays out (TS-002 owns synthesis).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D038 — VQA: Visual Question Answering (Antol et al.)
- Locator: https://arxiv.org/abs/1505.00468
- Source type: `arxiv_primary` | Published: `2015-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O07`, `VM-O11` | Modality: `image-text` | Role: `task-predecessor`
- X axes: `X02`, `X04`
- Claim notes: Task that exposed the language-prior shortcut; D10 control origin. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: VQA-v2 training contamination is the canonical shortcut exhibit; bind split + extraction rule.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D039 — Learning Transferable Visual Models / CLIP (Radford et al.)
- Locator: https://arxiv.org/abs/2103.00020
- Source type: `arxiv_primary` | Published: `2021-02` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O07` | Modality: `image-text` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Fixed-ontology to language-addressable break via web-scale pairs; zero-shot transfer. TS-002 conditioning angle reused by reference; TS-003 angle is the addressability transition. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Bag-of-words alignment limits motivate D07B; record the limitation, do not smooth it.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D040 — Scaling Up Visual and Vision-Language Representation Learning / ALIGN (Jia et al.)
- Locator: https://arxiv.org/abs/2102.05918
- Source type: `arxiv_primary` | Published: `2021-02` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O07` | Modality: `image-text` | Role: `variant-node`
- X axes: `X01`
- Claim notes: Noisy web-scale scaling point for image-text pretraining. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short treatment.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
