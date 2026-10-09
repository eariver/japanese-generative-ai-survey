# Discovery observations — VM-O10 D09 native/omni fusion (FULL_WEIGHT)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: AudioSet named data context only (BEATs 50.6% situates it); Wav2CLIP/AudioCLIP superseded by CLAP for the addressability question; InternVL3.5-series currency re-check at Evidence; vendor latency/token figures are config-bound claims.

## VM-D064 — Qwen2.5-VL Technical Report (Bai et al.)
- Locator: https://arxiv.org/abs/2502.13923
- Source type: `arxiv_primary` | Published: `2025-02` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `predecessor-node`
- X axes: `X01`, `X02`, `X03`
- Claim notes: M-RoPE + dynamic resolution predecessor of Qwen3-VL; fusion position-encoding thread origin. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); superseded claims need Qwen3-side sources.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial

## VM-D065 — Qwen3-VL Technical Report (Bai et al.)
- Locator: https://arxiv.org/abs/2511.21631
- Source type: `arxiv_primary` | Published: `2025-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `current-case`
- X axes: `X01`, `X02`, `X03`, `X04`
- Claim notes: DeepStack multi-level ViT features; interleaved-MRoPE; text-timestamp video alignment; 4-stage recipe (67B to ~1T to ~1T to 100B) with sqrt-reweighting; 256K interleaved context; dense+MoE family. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Vendor-measured benchmarks; token/config claims are config-bound (CV2-DM-020); independent reproduction pending.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open) + DEPLOYMENT_CASE + EVALUATION_CASE (vendor-measured)`
- repo: https://github.com/QwenLM/Qwen3-VL

## VM-D066 — Qwen3-Omni Technical Report (Xu et al.)
- Locator: https://arxiv.org/abs/2509.17765
- Source type: `arxiv_primary` | Published: `2025-09` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `current-case`
- X axes: `X01`, `X02`, `X03`, `X04`
- Claim notes: Thinker-Talker MoE; TM-RoPE absolute-time 80ms audio-video alignment; from-scratch audio encoder; 234ms first-packet (theoretical); 36 audio/AV benches; Apache 2.0. Input/fusion side is TS-003; Talker/Code2Wav synthesis subordinated to TS-002. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: No-degradation claim is vendor-measured; generation-side detail excluded by boundary.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open, input/fusion) + EVALUATION_CASE (vendor-measured)`
- repo: https://github.com/QwenLM/Qwen3-Omni

## VM-D067 — Robust Speech Recognition via Large-Scale Weak Supervision / Whisper (Radford et al.)
- Locator: https://arxiv.org/abs/2212.04356
- Source type: `arxiv_primary` | Published: `2022-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10` | Modality: `audio` | Role: `predecessor-node`
- X axes: `X01`
- Claim notes: Robust speech-input encoder precedent (multitask weakly-supervised speech); speech-to-token input contract. Generation history stays TS-002. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Input-side role only.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D068 — BEATs: Audio Pre-Training with Acoustic Tokenizers (Chen et al.)
- Locator: https://arxiv.org/abs/2212.09058
- Source type: `arxiv_primary` | Published: `2022-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10` | Modality: `audio` | Role: `predecessor-node`
- X axes: `X01`
- Claim notes: Iterative acoustic-tokenizer SSL with discrete-label prediction (not reconstruction); AudioSet-2M 50.6% mAP audio-only, ESC-50 98.1% (author-measured). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Classification-benchmark scope; fusion behavior needs omni-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D069 — CLAP: Learning Audio Concepts From Natural Language Supervision (Elizalde et al.)
- Locator: https://arxiv.org/abs/2206.04769
- Source type: `arxiv_primary` | Published: `2022-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10` | Modality: `audio-text` | Role: `predecessor-node`
- X axes: `X01`, `X02`
- Claim notes: Contrastive language-audio pretraining, 128k pairs, 16 tasks/8 domains zero-shot + 5 supervised SOTAs (author-measured); explicit CLIP-parallel for audio addressability. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Pair-scale limits vs CLIP; later omni encoders qualify the comparison.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D070 — InternVL3 (Zhu et al.)
- Locator: https://arxiv.org/abs/2504.10479
- Source type: `arxiv_primary` | Published: `2025-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `current-case`
- X axes: `X01`, `X02`, `X03`, `X04`
- Claim notes: Native joint multimodal+text pretraining (paradigm contrast to Qwen staged bridge); V2PE extended context; SFT+MPO; 1B-78B family; 78B 72.2 MMMU (vendor-measured); weights+data released. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Vendor-measured evals at this read level; 3.5-series currency re-check at Evidence.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open) + EVALUATION_CASE (vendor-measured)`
- repo: https://github.com/OpenGVLab/InternVL

## VM-D071 — Molmo2 (Clark et al.)
- Locator: https://arxiv.org/abs/2601.10611
- Source type: `arxiv_primary` | Published: `2026-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O10`, `VM-O11` | Modality: `multimodal` | Role: `current-case`
- X axes: `X01`, `X02`, `X04`
- Claim notes: Open weights+data (Apache 2.0); no closed-VLM synthetic data; video pointing/tracking; 8B counting 35.5 vs Qwen3-VL 29.6, pointing F1 38.4 vs Gemini 3 Pro 20.0 (author-measured); fully-open Olmo variant. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: 8B/4B reuse Qwen3 backbones (partial Qwen dependence, disclosed); comparator role, not paradigm pole.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open) + EVALUATION_CASE (author-measured)`
- repo: https://github.com/allenai/molmo2
- blog: https://allenai.org/blog/molmo2

## VM-D072 — Gemini 3.1 Pro model card (DeepMind)
- Locator: https://deepmind.google/models/model-cards/gemini-3-1-pro/
- Source type: `first_party_release_or_docs` | Published: `2026-02` | Access: `MODEL_CARD_OR_PAGE_VERIFIED`
- Obligations: `VM-O10`, `VM-O11` | Modality: `multimodal` | Role: `current-case`
- X axes: `X03`, `X04`
- Claim notes: Closed native-multimodal pole: 1M context; text/image/audio/video-in; MMMU-Pro/Video-MMMU vendor claims with methodology pages. [retrieval: MODEL_CARD_VERIFIED; full-body consumption at Evidence stage]
- Limitation: NEVER architecture authority; scores are vendor claims; bind version+date (CV2-DM-013).
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `CAPABILITY_CASE + EVALUATION_CASE (vendor) + DEPLOYMENT_CASE`

## VM-D073 — Gemini 3.6 Flash model card (DeepMind)
- Locator: https://deepmind.google/models/model-cards/gemini-3-6-flash/
- Source type: `first_party_release_or_docs` | Published: `2026-07` | Access: `MODEL_CARD_OR_PAGE_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `current-case`
- X axes: `X03`, `X04`
- Claim notes: Token-efficiency-positioned native multimodal; X03 exhibit for the efficiency pole. [retrieval: MODEL_CARD_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Capability/deployment facts only; no mechanism.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `CAPABILITY_CASE + DEPLOYMENT_CASE`

## VM-D074 — QwenLM/Qwen3-VL repository (code + weights)
- Locator: https://github.com/QwenLM/Qwen3-VL
- Source type: `official_project_repo` | Published: `n/a (living repo/card)` | Access: `REPOSITORY_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `deployment-transparency`
- X axes: `X03`, `X04`
- Claim notes: Open weights (incl. FP8 variants), Transformers/vLLM support; the inspectability exhibit for the modular three-module stack. [retrieval: REPOSITORY_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Repo state drifts; bind commit/version at Evidence; weights do not self-establish eval claims.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `DEPLOYMENT_CASE + ARCHITECTURE_CASE (inspectable)`

## VM-D075 — QwenLM/Qwen3-Omni repository (code + weights)
- Locator: https://github.com/QwenLM/Qwen3-Omni
- Source type: `official_project_repo` | Published: `n/a (living repo/card)` | Access: `REPOSITORY_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `deployment-transparency`
- X axes: `X03`, `X04`
- Claim notes: Apache 2.0 omni weights incl. talker-disablable thinker-only mode; streaming omni deployment exhibit. [retrieval: REPOSITORY_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Same drift/version binding caveats as VM-D074.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `DEPLOYMENT_CASE + ARCHITECTURE_CASE (inspectable)`

## VM-D076 — OpenGVLab/InternVL repository (code + weights + data)
- Locator: https://github.com/OpenGVLab/InternVL
- Source type: `official_project_repo` | Published: `n/a (living repo/card)` | Access: `REPOSITORY_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `deployment-transparency`
- X axes: `X01`, `X04`
- Claim notes: Second-family openness exhibit: weights plus training-data release (InternVL-Data). [retrieval: REPOSITORY_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Data-release scope to be verified file-level at Evidence.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `DEPLOYMENT_CASE`

## VM-D077 — allenai/molmo2 repository (training + eval code)
- Locator: https://github.com/allenai/molmo2
- Source type: `official_project_repo` | Published: `n/a (living repo/card)` | Access: `REPOSITORY_VERIFIED`
- Obligations: `VM-O10` | Modality: `multimodal` | Role: `deployment-transparency`
- X axes: `X04`
- Claim notes: Full-stack openness exhibit (data prep, training, eval, vLLM inference); grounding-measurement tooling. [retrieval: REPOSITORY_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Training-data license mix (academic/non-commercial third-party sources) must be bound at Evidence.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 partial
- Current-case role: `DEPLOYMENT_CASE`
