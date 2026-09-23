# TS-002 Discovery observations — D11 evaluation methodology and metric validity

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D083 — GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium (FID) (Heusel et al.)

- Locator: https://arxiv.org/abs/1706.08500
- Published: 2017-08
- Source class: PRIMARY_PAPER / role: eval / modality: image
- Obligations: BT-O11
- Summary: Frechet Inception Distance as distribution metric; the interpretation-limits anchor for image evaluation. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: FID limits (resolution/sample-size/embedding dependence) need dedicated methodology sources.

## BT-D084 — An Improved Technique for Evaluating GANs: Inception Score (Salimans et al.)

- Locator: https://arxiv.org/abs/1606.03461
- Published: 2016-06
- Source class: PRIMARY_PAPER / role: eval / modality: image
- Obligations: BT-O11
- Summary: Inception Score precursor showing single-number metric failure modes before FID. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Superseded; kept as metric-validity caution only.

## BT-D085 — GenEval: An Object-Focused Alignment and Compositional Evaluation (Ghosh et al.)

- Locator: https://arxiv.org/abs/2310.11513
- Published: 2023-10
- Source class: PRIMARY_PAPER / role: eval / modality: image
- Obligations: BT-O11, BT-O03
- Summary: Object-focused compositional alignment benchmark; prompt-adherence measurement separate from fidelity. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Detector-based scoring limits need protocol detail.

## BT-D086 — T2I-CompBench: Compositional Text-to-Image Benchmark (Huang et al.)

- Locator: https://arxiv.org/abs/2307.06350
- Published: 2023-07
- Source class: PRIMARY_PAPER / role: eval / modality: image
- Obligations: BT-O11, BT-O03
- Summary: Attribute/binding compositional diagnostics; binding-failure measurement. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Automatic-metric alignment with human judgment needs validation sources.

## BT-D087 — Pick-a-Pic: Open Dataset of User Preferences (Kirstain et al.)

- Locator: https://arxiv.org/abs/2305.01569
- Published: 2023-05
- Source class: PRIMARY_PAPER / role: eval / modality: image
- Obligations: BT-O11
- Summary: Large-scale human-preference dataset for image generation; preference-methodology anchor. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Population/prompt bias needs protocol sources.

## BT-D088 — Fréchet Audio Distance (Kilgour et al.)

- Locator: https://arxiv.org/abs/1812.08466
- Published: 2018-12
- Source class: PRIMARY_PAPER / role: eval / modality: audio
- Obligations: BT-O11
- Summary: Embedding-based audio quality distance; the FAD-limits anchor for audio/music evaluation. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Embedding dependence needs CLAP/human comparison.

## BT-D089 — LibriSpeech: Large-Scale Read English Speech Corpus (Panayotov et al.)

- Locator: https://arxiv.org/abs/1507.08211
- Published: 2015-04
- Source class: PRIMARY_PAPER / role: eval / modality: speech
- Obligations: BT-O11, BT-O07
- Summary: Standard ASR corpus behind WER/intelligibility measurement for speech generation. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Read-speech bias; expressive/streaming needs other protocols.

## BT-D090 — Generalized End-to-End Loss for Speaker Verification (GE2E) (Wan et al.)

- Locator: https://arxiv.org/abs/1710.10467
- Published: 2017-10
- Source class: PRIMARY_PAPER / role: eval / modality: speech
- Obligations: BT-O11, BT-O07
- Summary: Speaker-embedding similarity loss behind speaker-similarity evaluation. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Similarity-vs-naturalness split needs listening-study sources.

## BT-D091 — MUSHRA method (ITU-R BS.1534) reference

- Locator: https://www.itu.int/rec/R-REC-BS.1534
- Published: 2015-10
- Source class: PRIMARY_SPEC / role: eval / modality: audio
- Obligations: BT-O11
- Summary: Standardized multi-stimulus listening-test method behind MOS/MUSHRA-style audio claims. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Recommendation text; study-level protocol needs per-paper binding.

## BT-D092 — VBench: Comprehensive Benchmark Suite for Video Generative Models (Huang et al.)

- Locator: https://arxiv.org/abs/2311.17982
- Published: 2023-11
- Source class: PRIMARY_PAPER / role: eval / modality: video
- Obligations: BT-O11, BT-O09
- Summary: Decomposed video-quality dimensions (subject/background consistency, flicker, motion); the video-eval anchor. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Dimension-weighting choices need VBench-2.0 comparison.

## BT-D093 — VBench-2.0: Advancing Intrinsic Faithfulness (Zheng et al.)

- Locator: https://arxiv.org/abs/2503.21755
- Published: 2025-03
- Source class: PRIMARY_PAPER / role: eval / modality: video
- Obligations: BT-O11, BT-O09
- Summary: Intrinsic faithfulness (physics, commonsense, human fidelity, controllability, creativity) extension. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Model-version binding needs per-evaluation snapshots.
