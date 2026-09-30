# Discovery observations — VM-O09 D08 bridging vision and language (FULL_WEIGHT)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: Qwen-side three-module stack (VM-D065) is the durable-modularity exhibit carried from D09; Flamingo Perceiver-Resampler is the resampling predecessor cross-ref.

## VM-D057 — Multimodal Few-Shot Learning with Frozen Language Models / Frozen (Tsimpoukelli et al.)
- Locator: https://arxiv.org/abs/2106.13884
- Source type: `arxiv_primary` | Published: `2021-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O09` | Modality: `image-text` | Role: `precursor-context`
- X axes: `X02`
- Claim notes: Frozen-LLM bridging precursor; one-line context for the frozen-component design space. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Precursor only; short treatment.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D058 — Flamingo (Alayrac et al.)
- Locator: https://arxiv.org/abs/2204.14198
- Source type: `arxiv_primary` | Published: `2022-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O09` | Modality: `image-text` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Few-shot VL bridging via gated cross-attention with frozen components. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Closed-training-data regime; resampling predecessor role for D09 noted, not duplicated.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D059 — BLIP-2 (Li et al.)
- Locator: https://arxiv.org/abs/2301.12597
- Source type: `arxiv_primary` | Published: `2023-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O09` | Modality: `image-text` | Role: `anchor`
- X axes: `X01`, `X02`, `X03`
- Claim notes: Frozen-frozen bridging (vision encoder + LLM) via lightweight Q-Former; compute-efficient bridge exhibit. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Two-stage pretraining cost/complexity needs instruction-tuning successors for context.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D060 — InstructBLIP (Dai et al.)
- Locator: https://arxiv.org/abs/2305.06500
- Source type: `arxiv_primary` | Published: `2023-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O09` | Modality: `image-text` | Role: `bridge-node`
- X axes: `X01`
- Claim notes: Instruction-tuning bridge BLIP-2 to LLaVA; fills the Sol-map predecessor gap. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D061 — MiniGPT-4 (Zhu et al.)
- Locator: https://arxiv.org/abs/2304.10592
- Source type: `arxiv_primary` | Published: `2023-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O09` | Modality: `image-text` | Role: `bridge-node`
- X axes: `X01`
- Claim notes: Same instruction-tuning bridge function, open; alignment-stage exhibit. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short treatment.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D062 — Visual Instruction Tuning / LLaVA (Liu et al.)
- Locator: https://arxiv.org/abs/2304.08485
- Source type: `arxiv_primary` | Published: `2023-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O09` | Modality: `image-text` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: Vision encoder + LLM with visual instruction tuning as the central training step; X01 instruction-stage exhibit. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Instruction-data composition claims need data-side sources at Evidence.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D063 — Molmo and PixMo (Deitke et al.)
- Locator: https://arxiv.org/abs/2409.17146
- Source type: `arxiv_primary` | Published: `2024-09` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O09`, `VM-O10` | Modality: `image-text` | Role: `predecessor-context`
- X axes: `X01`, `X04`
- Claim notes: Open-data thesis origin (no closed-VLM synthetic data); PixMo-Points 2D pointing to grounding/counting; fully-open MetaCLIP+OLMo variant. Molmo 2 predecessor. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: v1 scope is image-centric; video claims belong to the Molmo 2 record.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
