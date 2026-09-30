# Discovery observations — VM-O05 D05 OCR/Document Intelligence (NORMAL_WEIGHT)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: Classical OCR history is one-line context; chart/table specialist benchmarks map in D15; screenshot/UI-as-document hands off to D12 by paragraph, not duplication.

## VM-D023 — LayoutLM (Xu et al.)
- Locator: https://arxiv.org/abs/1912.13318
- Source type: `arxiv_primary` | Published: `2019-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05` | Modality: `document` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Text+layout+position pre-training origin for document understanding. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Base-version scope; unified successors need v3-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D024 — LayoutLMv3 (Huang et al.)
- Locator: https://arxiv.org/abs/2204.08387
- Source type: `arxiv_primary` | Published: `2022-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05` | Modality: `document` | Role: `successor-node`
- X axes: `X01`
- Claim notes: Unified text-layout-image pre-training with word-patch alignment. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Generalist-pole-adjacent; specialist contrast needs Nougat/GOT-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D025 — Donut: OCR-free Document Understanding Transformer (Kim et al.)
- Locator: https://arxiv.org/abs/2111.15664
- Source type: `arxiv_primary` | Published: `2021-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05` | Modality: `document` | Role: `transition-node`
- X axes: `X01`, `X02`
- Claim notes: OCR-free end-to-end document understanding branch; Nougat/GOT lineage predecessor. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Synthetic-training dependence; domain-transfer limits need specialist sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D026 — Pix2Struct (Lee et al.)
- Locator: https://arxiv.org/abs/2210.03347
- Source type: `arxiv_primary` | Published: `2022-10` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05` | Modality: `document` | Role: `transition-node`
- X axes: `X01`
- Claim notes: Screenshot-parsing pretraining; UI-as-document bridge with explicit D12 handoff (not duplication). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Screenshot-domain scope; general-document claims need other sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D027 — Nougat: Neural Optical Understanding for Academic Documents (Blecher et al.)
- Locator: https://arxiv.org/abs/2308.13418
- Source type: `arxiv_primary` | Published: `2023-08` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05` | Modality: `document` | Role: `specialist-pole`
- X axes: `X01`, `X02`
- Claim notes: Donut-lineage Swin encoder-decoder producing markup (text+LaTeX math+tables) from arXiv/PMC/IDL-derived pairs; own-test markup agreement vs GROBID/pdf-text. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Own-suite evaluation only; cross-model numeric ranking prohibited (NO_CROSS_MODEL_NUMERIC_COMPARISON).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- Current-case role: `ARCHITECTURE_CASE (open)`
- repo: https://github.com/facebookresearch/nougat

## VM-D028 — General OCR Theory / GOT (Wei et al.)
- Locator: https://arxiv.org/abs/2409.01704
- Source type: `arxiv_primary` | Published: `2024-09` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05` | Modality: `document` | Role: `specialist-pole`
- X axes: `X01`, `X02`, `X03`
- Claim notes: 580M OCR-2.0 model: 80M high-compression encoder (1024px to 256 tokens) + 8K-context decoder; formatted outputs, region-prompt, dynamic resolution, multi-page; own OCR-2.0 suites. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Own-suite evaluation only; same-protocol head-to-head with generalists not found at intake.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- Current-case role: `ARCHITECTURE_CASE (open)`

## VM-D029 — Qwen3-VL-Embedding and Qwen3-VL-Reranker
- Locator: https://arxiv.org/abs/2601.04720
- Source type: `arxiv_primary` | Published: `2026-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05`, `VM-O10` | Modality: `multimodal` | Role: `retrieval-sub-lane`
- X axes: `X01`, `X02`
- Claim notes: VLM-backbone retrieval: MMEB-V2 77.8 (author-measured, Jan 2026); Matryoshka + quantization-aware deployment traits; D05 retrieval sub-lane + D09 encoder-reuse cross-ref. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID re-verified at intake (API title match); leaderboard claim is author-measured.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- Current-case role: `ARCHITECTURE_CASE + EVALUATION_CASE (author-measured)`

## VM-D108 — DocVQA (Mathew et al.)
- Locator: https://arxiv.org/abs/2007.00398
- Source type: `arxiv_primary` | Published: `2020-07` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05`, `VM-O16` | Modality: `document` | Role: `eval-authority`
- X axes: `X04`
- Claim notes: 50K Q / 12.7K images; ANLS metric; human 94.36%; structure-sensitivity gap. Distinct: document-structure reading. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Report ANLS, never bare accuracy alone; contamination MEDIUM; language-prior HIGH.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D109 — ChartQA (Masry et al.)
- Locator: https://arxiv.org/abs/2203.10244
- Source type: `arxiv_primary` | Published: `2022-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05`, `VM-O16` | Modality: `document` | Role: `eval-authority`
- X axes: `X04`
- Claim notes: 9.6K human + 23.1K generated visual+logical QA; relaxed-accuracy; real-world charts. Distinct: visual-reference + arithmetic reasoning. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Prior synthetic sets (FigureQA/DVQA/PlotQA) are named context only.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/vis-nlp/ChartQA

## VM-D110 — OCRBench v2 (Fu et al.)
- Locator: https://arxiv.org/abs/2501.00321
- Source type: `arxiv_primary` | Published: `2024-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O05`, `VM-O11`, `VM-O16` | Modality: `document` | Role: `eval-authority`
- X axes: `X04`
- Claim notes: 23 tasks / 31 scenarios / 10K verified QA / 6 metric types + 1,500-image private set; five limitation classes; spotting/localization gaps. v1 SUPERSEDED. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: v1 (2305.07895) dropped; private-set discipline is the contamination exhibit.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/Yuliang-Liu/MultimodalOCR
