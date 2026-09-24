# TS-002 Discovery observations — Sol r1 bounded gap-fill (r2 pass)

Collector run `beyond-text-discovery-r2` observed `2026-09-24T09:43:32Z`. Bounded primary-technical gap-fill only (G08/G09/G10/G11 mandatory; G03/G04/G12 opportunistic low-cost). Full-body consumption remains at Evidence stage.

## BT-D129 — Wav2Lip: A Lip Sync Expert Is All You Need for Speech to Lip Generation In The Wild (Prajwal et al., ACM MM 2020)

- Locator: https://arxiv.org/abs/2008.10010
- Published: 2020-08 (arXiv 2008.10010, first submitted 2020-08-23; ACM MM 2020)
- Source class: PRIMARY_PAPER / role: evaluation-method anchor / modality: video
- Obligations: BT-O11, BT-O09
- Summary: SyncNet-based lip-sync evaluation methodology for generated talking-face video: LSE-D (Lip-Sync Error Distance, lower is better) and LSE-C (Lip-Sync Error Confidence, higher is better), requiring no ground-truth reference pair; plus ReSyncED consistent benchmark construction (LRS2/LRW/LRS3-derived AV pairs) and human evaluation protocol (sync accuracy, visual quality, overall experience, preference). Gold-standard lip-sync metric family for G08. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Metric inherits SyncNet instabilities (see BT-D130); talking-face scope, not general sound-event timing.

## BT-D130 — Audio-Visual Speech Representation Expert for Enhanced Talking Face Video Generation and Evaluation (Yaman et al., CVPRW 2024)

- Locator: https://arxiv.org/abs/2405.04327
- Published: 2024-05 (arXiv 2405.04327, first submitted 2024-05-07; CVPRW 2024 NTIRE)
- Source class: PRIMARY_PAPER / role: evaluation-method anchor / modality: video
- Obligations: BT-O11
- Summary: Validity critique of the SyncNet/LSE family (GT-score fluctuation, poor shift-invariance, affine sensitivity, margin dependence) with documented user-study disagreement (Wav2Lip preferred by LSE on HDTF but far behind on human sync judgment); proposes three AV-HuBERT lip-reading-expert metrics (AVSu unsupervised AV, AVSm multimodal, AVSv visual-only) with stability evidence. Methodological-limitation authority for G08: do not treat LSE scores as comparable truth across conditions. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Talking-face scope; proposed metrics need independent adoption before they displace LSE.

## BT-D131 — VideoPhy: Evaluating Physical Commonsense for Video Generation (Bansal et al., ICLR 2025)

- Locator: https://arxiv.org/abs/2406.03520
- Published: 2024-06 (arXiv 2406.03520, first submitted 2024-06-05; ICLR 2025; code https://github.com/Hritikbansal/videophy)
- Source class: PRIMARY_PAPER / role: evaluation-method anchor / modality: video
- Obligations: BT-O11, BT-O09
- Summary: Independent physics-commonsense benchmark for text-to-video: 688 human-verified captions over solid-solid/solid-fluid/fluid-fluid interactions; binary Semantic Adherence (SA) and Physical Commonsense (PC) human judgments; best model (CogVideoX-5B) reaches only 39.6% joint SA+PC; plus VideoCon-Physics auto-evaluator (finetuned VideoCon; +17/+19 over zero-shot on SA/PC; GPT-4-Vision near-random on this task). Directly grounds G11 with a validity-quantified limitation: current video models are far from world-simulator physics. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: 2024 model set; newer 2025-2026 systems unevaluated on this protocol (Evidence-stage note).

## BT-D132 — F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching (Chen et al., ACL 2025)

- Locator: https://arxiv.org/abs/2410.06885
- Published: 2024-10 (arXiv 2410.06885, first submitted 2024-10-09; ACL 2025 long; code/checkpoints https://github.com/SWivid/F5-TTS)
- Source class: PRIMARY_PAPER / role: open-deployable anchor / modality: speech
- Obligations: BT-O07, BT-O10
- Summary: Fully non-autoregressive flow-matching DiT TTS without duration model/phoneme alignment (ConvNeXt text refinement + inference-time Sway Sampling); zero-shot voice cloning with WER 2.42/SIM-o 0.66 on LibriSpeech-PC at 32 NFE and RTF 0.15 at 16 NFE (PyTorch) / 0.04 (TRT-LLM server); trained on public 100K-hour multilingual data; all code and checkpoints released. Open-weight/runtime lane for G09 balancing the closed native-speech capstones. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Offline (non-streaming) synthesis; streaming counterpart is BT-D133.

## BT-D133 — CosyVoice 2: Scalable Streaming Speech Synthesis with Large Language Models (Du et al., 2024)

- Locator: https://arxiv.org/abs/2412.10117
- Published: 2024-12 (arXiv 2412.10117, first submitted 2024-12-13; code https://github.com/FunAudioLLM/CosyVoice)
- Source class: PRIMARY_PAPER / role: open-deployable + streaming-method anchor / modality: speech
- Obligations: BT-O07, BT-O10
- Summary: Streaming zero-shot TTS unifying streaming/non-streaming in one model: finite-scalar-quantized supervised semantic tokens, unified text-speech LM, chunk-aware causal flow matching; defines first-package latency L_TTS (token generation + mel reconstruction + vocoding) as the streaming UX metric; near-lossless streaming vs offline with human-parity naturalness claims. Serves G09 (open streaming TTS) and G10 (first-package-latency methodology). [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Latency figures are configuration-bound; vendor-family benchmark comparisons need Evidence-stage binding.

## BT-D134 — Moshi: a speech-text foundation model for real-time dialogue (Defossez et al., 2024)

- Locator: https://arxiv.org/abs/2410.00037
- Published: 2024-09 (arXiv 2410.00037, first submitted 2024-09-17; weights https://github.com/kyutai-labs/moshi)
- Source class: PRIMARY_PAPER / role: streaming-method anchor / modality: speech
- Obligations: BT-O07, BT-O10
- Summary: First real-time full-duplex speech-text LLM: parallel user/system audio token streams (no speaker-turn segmentation; overlap/interruption modeled), Mimi streaming neural codec (24kHz to 12.5Hz, 80ms frame latency), Inner Monologue time-aligned text prefix; theoretical latency 160ms (below the 230ms cross-linguistic natural-turn average), ~200ms in practice on L4. Foundational latency/architecture methodology for G10; open weights. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Research system; production deployment/runtime figures need independent measurement (Evidence-stage note).

## BT-D135 — MTR-DuplexBench: Towards a Comprehensive Evaluation of Multi-Round Conversations for Full-Duplex Speech Language Models (Zhang et al., 2025)

- Locator: https://arxiv.org/abs/2511.10262
- Published: 2025-11 (arXiv 2511.10262, first submitted 2025-11-13)
- Source class: PRIMARY_PAPER / role: evaluation-method anchor / modality: speech
- Obligations: BT-O11, BT-O07
- Summary: Full-duplex conversation evaluation methodology: smooth turn-taking, user interruption + resumption, pause handling, background-speech robustness as separate success criteria; per-round response latency (seconds) measured alongside success rate. Gives G10 a vendor-neutral measurement vocabulary (stop latency vs response latency) instead of incomparable vendor adjectives. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Recent protocol (2025-11); adoption across labs unverified.

## BT-D136 — Benchmarking Music Generation Models and Metrics via Human Preference Study (arXiv 2506.19085)

- Locator: https://arxiv.org/abs/2506.19085
- Published: 2025-06 (arXiv 2506.19085, first submitted 2025-06-23)
- Source class: PRIMARY_PAPER / role: evaluation-method anchor / modality: music
- Obligations: BT-O11, BT-O08
- Summary: Independent listening-study authority covering commercial models: 12 models including Suno v3/v3.5 and Udio, 6,000 generated songs, 15,600 pairwise comparisons by 2,500+ participants on music preference and text-audio alignment; Suno v3.5 top Elo on both axes; metric-correlation analysis (FAD-CLAP-MA best perception correlation; music-trained CLAP best for alignment). Partially fills G03 for Suno; dataset + human judgments openly released. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Suno v3/v3.5-era (not v5/v6); ElevenLabs independent evaluation still thin (negative space retained).

## BT-D137 — FLUX.2-klein-4B on H100: Image Generation Benchmark (Inference Bench, 2026-04-12)

- Locator: https://inferencebench.io/blog/flux2-klein-4b-image-generation-benchmark/
- Published: 2026-04 (article dated 2026-04-12)
- Source class: PRIMARY_DOC / role: independent-measurement anchor / modality: image
- Obligations: BT-O10
- Summary: Independent FLUX.2-klein-4B measurement with documented methodology (H100 SXM, Diffusers FluxPipeline bf16, flow-matching scheduler): 1024x1024 4-step 0.57s (1.77 img/s), 512x512 4-step 0.19s, VRAM 16-18GB by resolution, 5-10x faster than SDXL on equivalent hardware; explicit statement that diffusion metrics are images/sec, latency/image, VRAM, CLIP alignment (no KV-cache/TTFT). Partially fills G04; vendor sub-second claim now has an independent anchor. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Single-vendor-lab source (not peer-reviewed); consumer-GPU replication and A100 community figures remain for Evidence/X passes.

## BT-D138 — FiVE: A Fine-grained Video Editing Benchmark for Evaluating Emerging Diffusion and Rectified Flow Models (Wang, arXiv 2503.13684)

- Locator: https://arxiv.org/abs/2503.13684
- Published: 2025-03 (arXiv 2503.13684, first submitted 2025-03-17)
- Source class: PRIMARY_PAPER / role: evaluation-method anchor / modality: video
- Obligations: BT-O05, BT-O09, BT-O02
- Summary: First benchmark comparing diffusion-based vs rectified-flow video editing methods head-to-head (TokenFlow/DMT/VidToMe/AnyV2V/VideoGrain vs Pyramid-Edit/Wan-Edit via FlowEdit adaptation of Pyramid-Flow/Wan2.1): 100 videos, 420 object-level prompt pairs, 15 metrics; RF methods 10-15x faster per frame (Pyramid-Edit 1.44s/frame vs DMT 25.98s/frame) with competitive quality; new FiVE-Acc VLM metric. Partially fills G12 in the video-editing domain. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Editing-domain comparison; pure-generation flow-vs-diffusion ablations remain thin (negative space retained).
