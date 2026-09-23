# TS-002 Discovery observations — D07 speech / voice lineage

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D051 — WaveNet: A Generative Model for Raw Audio (van den Oord et al.)

- Locator: https://arxiv.org/abs/1609.03499
- Published: 2016-09
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O02
- Summary: Dilated-causal raw-waveform autoregression; the waveform-modeling origin for neural speech/audio. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Sequential-cost argument needs parallel-vocoder successors.

## BT-D052 — Tacotron: Towards End-to-End Speech Synthesis (Wang et al.)

- Locator: https://arxiv.org/abs/1703.10135
- Published: 2017-03
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07
- Summary: End-to-end text-to-spectrogram synthesis; decomposition change away from pipeline TTS. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Attention-robustness needs Tacotron 2 successor.

## BT-D053 — Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrograms (Tacotron 2) (Shen et al.)

- Locator: https://arxiv.org/abs/1712.05862
- Published: 2017-12
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07
- Summary: Tacotron-2 plus modified WaveNet vocoder reaching human-parity MOS claims; evaluation-protocol anchor. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: MOS comparability needs protocol/later-system discipline.

## BT-D054 — FastSpeech: Fast, Robust and Controllable Text to Speech (Ren et al.)

- Locator: https://arxiv.org/abs/1905.09263
- Published: 2019-05
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O10
- Summary: Non-autoregressive TTS with duration predictor; parallelization/latency transition. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Duration-model quality needs VITS comparison.

## BT-D055 — HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis (Kong et al.)

- Locator: https://arxiv.org/abs/2010.05646
- Published: 2020-10
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O10
- Summary: Efficient GAN vocoder with multi-period discriminators; adversarial vocoding standard. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: GAN-artifact analysis needs diffusion-vocoder comparison.

## BT-D056 — Conditional VAE with Adversarial Learning for End-to-End TTS (VITS) (Kim et al.)

- Locator: https://arxiv.org/abs/2106.06103
- Published: 2021-06
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07
- Summary: VAE plus flow plus adversarial end-to-end TTS; latent/flow/adversarial hybrid thesis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Stochastic-duration modeling needs codec-LM comparison.

## BT-D057 — Transfer Learning from Speaker Verification to Multispeaker TTS (YourTTS) (Casanova et al.)

- Locator: https://arxiv.org/abs/2112.02418
- Published: 2021-12
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O04
- Summary: Zero-shot multispeaker TTS with speaker embeddings; speaker-identity conditioning precedent for cloning. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Similarity measurement needs GE2E/eval successors.

## BT-D058 — Neural Codec Language Models are Zero-Shot TTS Synthesizers (VALL-E) (Wang et al.)

- Locator: https://arxiv.org/abs/2301.02111
- Published: 2023-01
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O01
- Summary: Codec-token language modeling for zero-shot voice cloning; the codec-LM speech transition. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Acoustic-vs-semantic token analysis needs AudioLM linkage.

## BT-D059 — VALL-E 2: Neural Codec Language Models are Human Parity Zero-Shot TTS (Chen et al.)

- Locator: https://arxiv.org/abs/2406.05358
- Published: 2024-06
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O11
- Summary: Repetition-aware sampling and grouped code modeling toward human-parity claims; decoding-stability study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Parity claims need independent listening-study reproduction.

## BT-D060 — Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale (Le et al.)

- Locator: https://arxiv.org/abs/2306.15687
- Published: 2023-06
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O05, BT-O02
- Summary: Flow-matching infilling speech model for generation/editing with cross-lingual ability; non-AR editing thesis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Infilling-vs-generation split needs continuation benchmarks.

## BT-D061 — Seed-TTS: Versatile and High-Fidelity Speech Generation (ByteDance)

- Locator: https://arxiv.org/abs/2406.02430
- Published: 2024-06
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O06
- Summary: Self-distilled versatile TTS with speaker-factorization and emotion control; in-the-wild speaker study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Vendor-authored evaluation needs independent reproduction.

## BT-D062 — Seamless Communication: Expressive Multilingual Speech (SeamlessM4T v2) (Meta)

- Locator: https://arxiv.org/abs/2308.11596
- Published: 2023-08
- Source class: PRIMARY_PAPER / role: anchor / modality: speech
- Obligations: BT-O07, BT-O06
- Summary: Expressive multilingual speech-to-speech translation with prosody preservation; streaming/expressive axis. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Expressivity measurement needs prosody-eval successors.
