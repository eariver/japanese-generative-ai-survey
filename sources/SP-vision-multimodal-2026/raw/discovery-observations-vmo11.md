# Discovery observations — VM-O11 D10 reasoning/failure decomposition

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: MMMU-Pro and vendor thinking-budget contexts travel with condition binding; multi-image-comparison and chart-specialist evals are methodology-first collection targets at Evidence.

## VM-D078 — MMMU (Yue et al.)
- Locator: https://arxiv.org/abs/2311.16502
- Source type: `arxiv_primary` | Published: `2023-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O11` | Modality: `image-text` | Role: `eval-anchor`
- X axes: `X04`
- Claim notes: Comprehensive multimodal-reasoning eval home; thinking-vs-non-thinking ablations required for attribution. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Composite score must not stand as general intelligence; contamination opacity for closed models.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D079 — Evaluating Object Hallucination / POPE (Li et al.)
- Locator: https://arxiv.org/abs/2305.10355
- Source type: `arxiv_primary` | Published: `2023-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O11`, `VM-O16` | Modality: `image-text` | Role: `eval-anchor`
- X axes: `X04`
- Claim notes: Controlled object-existence polling; cheap hallucination screen complementary to control-pair diagnosis. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Polling scope only; open-ended faithfulness needs other instruments.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D080 — HallusionBench (Guan et al.)
- Locator: https://arxiv.org/abs/2310.14566
- Source type: `arxiv_primary` | Published: `2023-10` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O11`, `VM-O16` | Modality: `image-text` | Role: `eval-anchor`
- X axes: `X04`
- Claim notes: 346 images (165 + 181 human-edited) / 1,129 Q; control-pair language-vs-vision failure attribution; GPT-4V 31.42% pair-accuracy (author-measured); CVPR 2024. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID corrected at intake (Round B guess 2311.07312 wrong); small-scale handcrafted scope.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/tianyi-lab/HallusionBench

## VM-D081 — MMBench (Liu et al.)
- Locator: https://arxiv.org/abs/2307.06281
- Source type: `arxiv_primary` | Published: `2023-07` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O11` | Modality: `image-text` | Role: `eval-anchor`
- X axes: `X04`
- Claim notes: Bilingual 3,000-Q / 20-ability VLM eval with CircularEval + LLM choice extraction; v1.1 quality revision; ECCV 2024. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Judge/choice-extraction dependence (GPT-4 matching 91.5%) must travel with every score.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/open-compass/MMBench

## VM-D082 — MathVista (Lu et al.)
- Locator: https://arxiv.org/abs/2310.02255
- Source type: `arxiv_primary` | Published: `2023-10` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O11` | Modality: `image-text` | Role: `eval-node`
- X axes: `X04`
- Claim notes: Visual-math reasoning: 6,141 examples from 28 datasets + 3 new; GPT-4V 49.9% vs human 60.3% (author-measured); ICLR 2024. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match; not 2311.12505); perception-vs-reasoning attribution needs scaffold ablations.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
