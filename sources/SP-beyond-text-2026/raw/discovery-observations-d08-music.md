# TS-002 Discovery observations — D08 music / general audio lineage

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`. Primary-technical first pass; full-body consumption at Evidence stage.

## BT-D063 — Jukebox: A Generative Model for Music (Dhariwal et al.)

- Locator: https://arxiv.org/abs/2005.00341
- Published: 2020-04
- Source class: PRIMARY_PAPER / role: anchor / modality: music
- Obligations: BT-O08, BT-O02, BT-O06
- Summary: VQ-VAE hierarchical autoregressive music with lyrics/genre conditioning; long-form raw-audio precedent. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Four-minute coherence ceiling needs MusicLM/MusicGen comparison.

## BT-D064 — DiffWave: A Versatile Diffusion Model for Audio Synthesis (Kong et al.)

- Locator: https://arxiv.org/abs/2009.09761
- Published: 2020-09
- Source class: PRIMARY_PAPER / role: anchor / modality: audio
- Obligations: BT-O08, BT-O07, BT-O02
- Summary: Waveform diffusion for vocoding/general audio; diffusion-in-audio transition shared with speech. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Step-cost needs DDIM/fast-sampler successors.

## BT-D065 — MusicLM: Generating Music From Text (Agostinelli et al.)

- Locator: https://arxiv.org/abs/2301.11325
- Published: 2023-01
- Source class: PRIMARY_PAPER / role: anchor / modality: music
- Obligations: BT-O08, BT-O06
- Summary: Semantic+acoustic staged generation with MuLan alignment; long-form text-music structure study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Structure evaluation needs long-form music metrics.

## BT-D066 — Simple and Controllable Music Generation (MusicGen) (Copet et al.)

- Locator: https://arxiv.org/abs/2306.05284
- Published: 2023-06
- Source class: PRIMARY_PAPER / role: anchor / modality: music
- Obligations: BT-O08, BT-O04
- Summary: Single-stage autoregressive codec music with melody conditioning; AudioCraft open controllable baseline. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Melody-control measurement needs Mustango comparison.

## BT-D067 — AudioLDM: Text-to-Audio Generation with Latent Diffusion (Liu et al.)

- Locator: https://arxiv.org/abs/2301.12503
- Published: 2023-01
- Source class: PRIMARY_PAPER / role: anchor / modality: audio
- Obligations: BT-O08, BT-O02
- Summary: CLAP-conditioned latent diffusion for general audio; the latent-diffusion-in-audio transition. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: CLAP-conditioning limits need AudioLDM-2 successor.

## BT-D068 — Stable Audio Open (Evans et al.)

- Locator: https://arxiv.org/abs/2402.10046
- Published: 2024-02
- Source class: PRIMARY_PAPER / role: anchor / modality: music
- Obligations: BT-O08, BT-O10
- Summary: Open-weight latent-diffusion audio with timing conditioning and local execution; open-mechanism anchor. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Stereo/long-form scope needs Stable Audio 3 successor.

## BT-D069 — MuSTANGO: Controllable Text-to-Music (Feijoo et al.)

- Locator: https://arxiv.org/abs/2308.02530
- Published: 2023-08
- Source class: PRIMARY_PAPER / role: anchor / modality: music
- Obligations: BT-O08, BT-O04
- Summary: Beat/chord/key control signals for music diffusion; fine-grained musical-control study. [retrieval: SUMMARY_CAPTURED; full-body consumption at Evidence stage]
- Limitation: Control-audio quality interaction needs MusicGen comparison.
