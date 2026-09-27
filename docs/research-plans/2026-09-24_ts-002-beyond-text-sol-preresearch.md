# TS-002 Beyond Text — Sol independent pre-research skeleton

Status: `SOL_INDEPENDENT_PRERESEARCH / PRE_DISCOVERY / NOT_YET_PRODUCTION_AUTHORITY`

Date: `2026-09-24 JST`

Repository: `eariver/japanese-generative-ai-survey`

Planning branch: `planning/ts-002-beyond-text-preresearch-20260924`

Clean planning base: `9b635adf6f2be535009d17feb50dda4e520a49c2`

Reader-facing working title:

> **Beyond Text — 画像・音声・音楽・映像生成AIの技術史**

This document is a Sol-authored research scaffold created **before Muse Discovery** so that the worker is not asked to invent the technical map from scratch and so that breadth/depth is not silently lost during large-scale collection. It is not Evidence, Selection, Architecture, or Human approval. Exact-byte capture, provenance normalization, source acceptance, and stage validation remain production-pipeline responsibilities.

---

## 1. Editorial thesis

TS-002 should not be a catalogue of Stable Diffusion, Midjourney, Suno, Sora, Veo, or other well-known products. The central technical question is:

> High-dimensional continuous media — pixels, waveforms, frames, motion, and synchronized sound — were made tractable for generative modeling by changing **representation**, **prediction/generation objective**, **conditioning**, **control/editing**, **temporal structure**, **sampling/runtime**, and **evaluation**. How did those choices evolve across image, speech, music, and video, what bottleneck did each transition solve, and what trade-offs did it introduce?

The desired reader model is therefore not:

`famous model -> next famous model -> current product`

but approximately:

`media representation -> generative process -> conditioning/alignment -> control/reference -> editing -> temporal/long-horizon structure -> runtime/deployment -> evaluation -> multimodal convergence`.

The same coordinate system should be used across modalities wherever technically honest, while preserving modality-specific problems that cannot be flattened into a generic diffusion story.

---

## 2. Anti-thinness requirements

A TS-002 research package is incomplete if it only establishes that GANs were followed by diffusion models or if it gives each modality a small list of popular products.

At minimum, the final research/evidence base must support all of the following:

1. **Representation is first-class.** Explain why generation moved from raw pixels/waveforms/frames toward continuous latents, discrete codebooks, neural codecs, spatiotemporal tokenizers, or hybrid semantic/acoustic representations.
2. **Architecture and objective must be separated.** U-Net vs Transformer is not the same axis as autoregressive vs diffusion vs flow matching.
3. **Image must not dominate the Special.** Speech/voice, music/general audio, and video each require their own historical lineage and modality-specific failure modes.
4. **Generation and editing are distinct technical problems.** Inpainting, continuation, instruction editing, local editing, reference editing, and preservation of untouched content need explicit treatment.
5. **Single-sample fidelity is not enough.** Identity, composition, lyrics, speaker consistency, temporal consistency, physics, camera control, and long-form structure require separate treatment.
6. **Current closed products are capability cases, not automatic architecture authority.** When architecture is undisclosed, do not reverse-engineer it from marketing prose.
7. **Benchmarks are not interchangeable.** Do not rank models across incompatible prompt sets, duration, resolution, sampling budgets, human-study populations, versions, or metric definitions.
8. **Runtime matters.** Resolution, latent/token rate, sampling steps, solver/distillation, time-to-first-output, real-time factor, VRAM, duration, and local/open-weight execution can materially change what is deployable.
9. **TS-002/TS-003 boundary must remain explicit.** A model's understanding/reasoning is covered only insofar as it changes generation, editing, control, or media consistency.
10. **Historical transitions require causality questions.** For each major transition ask: What bottleneck existed? What mechanism changed? What improved? What became worse or more expensive? What later systems inherited the idea?

A page target is not authoritative before Evidence/Architecture Review, but a **64–96 page design envelope should be treated as a floor/normal range rather than a hard cap** if source density justifies it. The topic is broader than TS-001 Efficient Intelligence; forcing it into a short model catalogue would defeat the purpose of the Special.

---

## 3. Boundary with TS-003 Vision & Multimodal AI

Normative editorial split:

- **TS-002:** What can AI generate, and by what representation / generative / control / editing mechanism?
- **TS-003:** How does AI perceive, recognize, understand, and reason about the world across modalities?

Allowed in TS-002 when load-bearing for generation:

- CLIP/T5/VLM encoders as conditioning or evaluation machinery.
- Multimodal reasoning when it materially changes generation/editing behavior.
- World-model language only where video generation and simulated dynamics genuinely intersect.
- Reference-image/video/audio understanding required for preservation, editing, or control.

Default to TS-003:

- object detection history;
- segmentation history as a perception task;
- OCR/general visual recognition;
- general VLM benchmark history;
- visual question answering;
- perception-centric spatial/embodied reasoning.

ControlNet may use edge/depth/pose/segmentation signals, but TS-002 should discuss those signals as **generation controls**, not retell the perception history of producing them.

---

## 4. Mandatory research dimensions

### D01 — Media representation, compression, and tokenization

Questions:

- Why are raw pixels, waveform samples, and dense video frames expensive sequences for generative models?
- Continuous latent vs discrete token: what information is intentionally discarded or preserved?
- What are the roles of VAE, VQ-VAE/VQGAN-style discrete latents, residual vector quantization, neural audio codecs, video VAEs/tokenizers?
- How do compression ratio / token rate / reconstruction quality constrain downstream generation?
- Why can semantic structure and acoustic/perceptual fidelity pull representation design in different directions?

Mandatory anchors/candidates:

- Auto-Encoding Variational Bayes (VAE), 2013.
- Neural Discrete Representation Learning (VQ-VAE), 2017.
- latent image autoencoders used by Latent Diffusion.
- SoundStream, 2021.
- EnCodec / High Fidelity Neural Audio Compression, 2022.
- AudioLM hybrid semantic + acoustic tokenization, 2022.
- Phenaki causal video tokenizer, 2022/2023.
- modern temporal video/audio autoencoders where technically documented.

Key thesis to test: **the history of media generation is partly a history of making the object to be generated dramatically shorter.**

### D02 — Generative paradigms and training objectives

Keep these axes distinct:

- latent-variable generative models / VAE;
- autoregressive generation;
- GAN/adversarial generation;
- diffusion/DDPM;
- score-based generative modeling;
- latent diffusion;
- Diffusion Transformer (DiT);
- continuous normalizing flow / flow matching;
- rectified-flow family where relevant;
- hybrid objectives and adversarial post-training/distillation.

Mandatory questions:

- sample quality vs diversity / mode coverage;
- tractable likelihood vs implicit models;
- training stability;
- sequential sampling cost;
- ability to condition/control/edit;
- scalability with Transformer backbones;
- sampling trajectory and solver implications.

Do not write the transition as simply `GAN -> diffusion`. GANs remain important for adversarial reconstruction, vocoders, autoencoders, post-training, and hybrid media systems even after diffusion became dominant in major image/video generators.

### D03 — Conditioning, alignment, and guidance

Research lanes:

- class conditioning;
- text embeddings / cross-attention;
- classifier guidance;
- classifier-free guidance;
- CLIP/T5-like semantic conditioning;
- text + image / text + audio / text + video conditions;
- melody/chroma/lyrics conditions;
- multi-reference conditioning;
- reference style/content separation.

For each mechanism distinguish:

- training-time conditioning;
- inference-time guidance;
- separately trained control/adapters;
- in-context reference conditioning.

Prompt adherence is not equivalent to perceptual quality or distribution quality.

### D04 — Control, reference, identity, and preservation

Mandatory subjects:

- ControlNet as an important spatial-control transition.
- adapter/reference mechanisms where historically/materially important.
- subject/character/speaker identity preservation.
- style vs content reference.
- multi-reference generation.
- camera / motion / keyframe / first-last-frame control in video.
- lyric, section, tempo, melody, stem, or timing control in music/audio where supported.

Research must separate **control signal fidelity** from generic sample quality.

### D05 — Generation to editing

Editing must be treated as a different problem from unconditional or text-to-X generation.

Mandatory lanes:

- image-to-image;
- inpainting/outpainting;
- instruction-based image editing;
- local/region editing;
- reference editing;
- iterative/multi-turn editing;
- video-to-video transformation and instruction editing;
- audio/music continuation and inpainting;
- speech content editing while preserving speaker/prosody;
- preservation of non-target regions/segments.

A major current trend to test is the convergence of formerly separate generation and editing stacks into one multimodal model or endpoint.

### D06 — Image generation lineage

Minimum historical path:

- VAE / early latent-variable models;
- autoregressive pixels (PixelRNN/PixelCNN; Image Transformer where useful);
- GAN -> StyleGAN family as high-fidelity/control landmark;
- DDPM and score-based modeling;
- classifier-free guidance;
- latent diffusion / Stable Diffusion lineage;
- DiT;
- ControlNet/reference/editing systems;
- flow-matching / rectified-flow era;
- unified generation + editing and multimodal reasoning-assisted image creation.

Current capability cases should include technically distinct/open-vs-closed examples, not a popularity ranking.

### D07 — Speech and voice lineage

Speech must not be collapsed into the music chapter.

Minimum historical path:

- WaveNet raw-waveform autoregression;
- Tacotron/end-to-end TTS decomposition change;
- neural vocoders and parallelization where load-bearing;
- VITS / end-to-end latent + flow + adversarial synthesis;
- SoundStream/EnCodec neural codec transition;
- codec language models / VALL-E zero-shot TTS;
- Voicebox non-autoregressive flow-matching speech generation/editing;
- zero/few-shot voice cloning;
- multilingual/expressive speech;
- streaming and full-duplex speech-to-speech;
- current native-audio multimodal systems.

Required dimensions:

- intelligibility / WER;
- naturalness / MOS or listening study;
- speaker similarity;
- prosody/emotion;
- latency and streaming;
- speaker/voice consent and provenance as a technical boundary.

### D08 — Music and general-audio lineage

Minimum historical path:

- raw/discrete autoregressive audio and Jukebox;
- neural audio codecs;
- AudioLM;
- MusicLM;
- MusicGen/AudioCraft;
- latent-diffusion/DiT audio systems such as Stable Audio lineage;
- long-form song models and editing/control workflows;
- scene-level audio generation (speech + ambience + effects) where current systems make this distinction material.

Required dimensions:

- acoustic fidelity;
- text/music alignment;
- long-horizon musical form;
- verse/chorus/bridge or comparable section structure;
- vocals and lyrics coherence;
- melody/rhythm/tempo control;
- continuation/inpainting/remix;
- stems / source separation interaction if generation workflows depend on them;
- duration and real-time factor.

### D09 — Video generation lineage

Minimum historical path:

- early video prediction/generative approaches only as much as needed to establish the temporal problem;
- Video Diffusion Models (2022);
- Imagen Video / cascaded spatial+temporal super-resolution;
- Phenaki / compressed discrete variable-length video representation;
- latent video diffusion / spatiotemporal attention;
- video Transformer / media foundation model scaling;
- personalization/reference/video editing;
- native synchronized audio-video generation;
- longer single-pass generation and continuation;
- multi-shot/narrative control;
- current open-weight ecosystem and runtime constraints.

Mandatory failure dimensions:

- identity/object permanence;
- temporal flicker;
- motion quality;
- camera consistency;
- scene continuity;
- multi-shot continuity;
- prompt timing;
- physics/commonsense fidelity;
- lip/audio synchronization.

### D10 — Temporal and long-horizon structure across modalities

Do not treat duration as a marketing field. Research how models preserve structure as generated sequence length increases.

Cross-modal questions:

- What is the effective generation sequence length after compression/tokenization?
- Is generation autoregressive, masked-token, iterative denoising, flow-based, chunked, hierarchical, or continuation-based?
- What state is preserved between chunks/extensions?
- Does a longer duration actually preserve global structure, or merely continue local texture?
- How is identity/speaker/motif/scene state represented?

Image has spatial compositional consistency; speech, music, and video add genuine temporal dependency and should therefore be compared carefully rather than forced into the same metric vocabulary.

### D11 — Runtime, sampling efficiency, and deployment

Mandatory fields where available:

- resolution/sample rate/frame rate;
- maximum or evaluated duration;
- latent/token rate or compression ratio;
- number of denoising/sampling steps;
- distillation/adversarial post-training/few-step generation;
- time-to-first-frame/audio where material;
- real-time factor;
- VRAM/accelerator requirements;
- batch vs interactive latency;
- local/open-weight execution;
- quantization/offload/runtime support for large open media models.

Important distinction: a model can have excellent sample quality but be operationally unsuitable for interactive editing, realtime speech, local creation, or long video because its runtime path is too expensive.

### D12 — Evaluation, benchmark validity, provenance, and convergence

Evaluation is a full package, not a footnote.

Image candidates:

- FID as distribution metric and its limitations;
- CLIP-like alignment metrics;
- GenEval;
- T2I-CompBench;
- human preference and editing-preservation evaluations.

Audio/speech/music candidates:

- MOS/MUSHRA and listening protocols;
- WER/intelligibility;
- speaker similarity;
- Fréchet Audio Distance and embedding dependence;
- CLAP/text-audio alignment;
- structural/long-form music evaluation and the limits of automatic metrics.

Video candidates:

- VBench;
- VBench-2.0 intrinsic faithfulness (physics, commonsense, human fidelity, controllability, creativity);
- human preference protocols;
- task-specific editing/reference/identity measures;
- audio-video synchronization measures.

Provenance/rights should not become the political/legal center of the Special, but technical mechanisms are in scope when they affect deployment and trust: watermarking, C2PA/content credentials, generated-media detectors/verification, authorized voice/reference inputs, declared training-data boundaries, and open-weight/license constraints.

The final convergence question is whether media generation is moving toward one unified representation/model or toward tightly connected modality-specialized generators orchestrated by multimodal reasoning/agents. This should remain an evidence-backed question, not a predetermined conclusion.

---

## 5. Historical anchor source map — primary/near-primary starting points

This is a **pre-Discovery source map**, not an accepted Evidence set. Muse must capture canonical source bytes/metadata under the normal pipeline and may add predecessors/successors required by citation graphs.

### General / image representation and generation

- Kingma & Welling, **Auto-Encoding Variational Bayes** — https://arxiv.org/abs/1312.6114
- Goodfellow et al., **Generative Adversarial Networks** — https://arxiv.org/abs/1406.2661
- van den Oord et al., **Pixel Recurrent Neural Networks** — https://arxiv.org/abs/1601.06759
- van den Oord et al., **Neural Discrete Representation Learning (VQ-VAE)** — https://arxiv.org/abs/1711.00937
- Parmar et al., **Image Transformer** — https://arxiv.org/abs/1802.05751
- Karras et al., **Analyzing and Improving the Image Quality of StyleGAN** — https://arxiv.org/abs/1912.04958
- Ho et al., **Denoising Diffusion Probabilistic Models** — https://arxiv.org/abs/2006.11239
- Song et al., **Score-Based Generative Modeling through Stochastic Differential Equations** — https://arxiv.org/abs/2011.13456
- Rombach et al., **High-Resolution Image Synthesis with Latent Diffusion Models** — https://arxiv.org/abs/2112.10752
- Ho & Salimans, **Classifier-Free Diffusion Guidance** — https://arxiv.org/abs/2207.12598
- Peebles & Xie, **Scalable Diffusion Models with Transformers (DiT)** — https://arxiv.org/abs/2212.09748
- Lipman et al., **Flow Matching for Generative Modeling** — https://arxiv.org/abs/2210.02747
- Zhang et al., **Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet)** — https://arxiv.org/abs/2302.05543

### Speech / audio representation and generation

- van den Oord et al., **WaveNet: A Generative Model for Raw Audio** — https://arxiv.org/abs/1609.03499
- Wang et al., **Tacotron: Towards End-to-End Speech Synthesis** — https://arxiv.org/abs/1703.10135
- Kim et al., **Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech (VITS)** — https://proceedings.mlr.press/v139/kim21f.html
- Zeghidour et al., **SoundStream: An End-to-End Neural Audio Codec** — https://arxiv.org/abs/2107.03312
- Défossez et al., **High Fidelity Neural Audio Compression (EnCodec)** — https://arxiv.org/abs/2210.13438
- Borsos et al., **AudioLM: a Language Modeling Approach to Audio Generation** — https://arxiv.org/abs/2209.03143
- Wang et al., **Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers (VALL-E)** — https://arxiv.org/abs/2301.02111
- Le et al., **Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale** — https://arxiv.org/abs/2306.15687

### Music / general audio

- Dhariwal et al., **Jukebox: A Generative Model for Music** — https://arxiv.org/abs/2005.00341
- Agostinelli et al., **MusicLM: Generating Music From Text** — https://arxiv.org/abs/2301.11325
- Copet et al., **Simple and Controllable Music Generation (MusicGen)** — https://arxiv.org/abs/2306.05284
- Stability AI, **Stable Audio 3 / SAME** — https://stability.ai/research/stable-audio-3

### Video

- Ho et al., **Video Diffusion Models** — https://arxiv.org/abs/2204.03458
- Ho et al., **Imagen Video: High Definition Video Generation with Diffusion Models** — https://arxiv.org/abs/2210.02303
- Villegas et al., **Phenaki: Variable Length Video Generation from Open Domain Textual Descriptions** — https://openreview.net/forum?id=vOEXS39nOF
- Meta, **Movie Gen: A Cast of Media Foundation Models** — https://ai.meta.com/research/publications/movie-gen-a-cast-of-media-foundation-models/
- OpenAI, **Sora: Creating video from text** — https://openai.com/index/sora/

### Evaluation

- Heusel et al., **FID / TTUR** — https://arxiv.org/abs/1706.08500
- Kilgour et al., **Fréchet Audio Distance** — https://arxiv.org/abs/1812.08466
- Ghosh et al., **GenEval** — https://arxiv.org/abs/2310.11513
- Huang et al., **T2I-CompBench** — https://arxiv.org/abs/2307.06350
- Huang et al., **VBench** — https://arxiv.org/abs/2311.17982
- Zheng et al., **VBench-2.0** — https://arxiv.org/abs/2503.21755

---

## 6. 2025–2026 current capstone candidate map

These are **candidates to investigate**, not a ranking and not yet Selection. A candidate may be retained as a closed capability/workflow case even if it lacks enough architecture disclosure to be a mechanism anchor.

### Image / image editing

1. **Black Forest Labs FLUX.2 family**
   - unified image generation + editing;
   - multi-reference workflows;
   - open/local variants available in the family;
   - FLUX.2 [klein] explicitly targets sub-second/consumer-hardware generation in documented configurations;
   - useful for runtime/open-vs-closed comparison.
   - Primary starting points: https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence and https://help.bfl.ai/articles/4292391522-what-is-flux-2

2. **ByteDance Seedream 5.0 Pro**
   - current multimodal image creation/editing case;
   - spatially grounded professional editing and information/design tasks are material current directions;
   - treat vendor evaluations as vendor claims until independently supported.
   - Primary: https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro

3. **OpenAI ChatGPT Images / GPT Image 2.5**
   - current generation + iterative editing capability case;
   - architecture disclosure may be limited, therefore do not use it to infer mechanism without technical authority.
   - Primary: https://openai.com/index/introducing-chatgpt-images-2-5/

4. **Google Nano Banana 2 / Gemini 3.1 Flash Image**
   - native multimodal reasoning + image generation/editing case;
   - particularly relevant to TS-002/TS-003 boundary because world knowledge/reasoning is used in a generator/editor.
   - Primary: https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/ and https://deepmind.google/models/model-cards/gemini-3-1-flash-image/

5. **Imagen 4**
   - historically/currently relevant dedicated diffusion image generator, but Google developer guidance states Imagen models were deprecated/shut down in favor of Nano Banana in 2026; treat this lifecycle transition as evidence for dedicated-generator -> native-multimodal convergence, not as proof of architectural inevitability.
   - Primary: https://deepmind.google/models/imagen/

### Speech / native audio

1. **OpenAI GPT-Live / GPT-Realtime-2 family**
   - native realtime conversational speech case;
   - reasoning + speech interaction + latency/streaming make it a current capstone candidate rather than a conventional offline TTS case.
   - Primary: https://openai.com/index/introducing-gpt-live/ and https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/

2. **Google Gemini 3.8 Audio / Live**
   - native audio input/output in a multimodal reasoning model;
   - current model card provides limitations/evaluation authority.
   - Primary: https://deepmind.google/models/model-cards/gemini-3-8-audio/

3. **ByteDance SeedRealtime / Seed Audio 1.0**
   - separate but related current directions: full-duplex multimodal interaction and scene-level audio generation;
   - Seed Audio 1.0 explicitly combines speech, effects, ambience and timing under shared scene context, useful for testing whether 'speech', 'SFX', and 'audio scene' are converging.
   - Primary: https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model

### Music / general audio

1. **Google Lyria 3.5**
   - model card states latent diffusion over temporal audio latents;
   - supports long-form/structured composition and gives unusually useful architecture/evaluation authority for a current closed frontier music model.
   - Primary: https://deepmind.google/models/model-cards/lyria-3-5/ and https://deepmind.google/models/lyria/

2. **Stability AI Stable Audio 3**
   - open-weight/current mechanism anchor;
   - semantic-acoustic autoencoder + latent diffusion + adversarial post-training;
   - variable-length generation, editing/inpainting, local execution are all relevant.
   - Primary: https://stability.ai/research/stable-audio-3

3. **Suno v6 family**
   - current closed commercial capability/workflow case;
   - local editing, multi-source mashup, multimodal creative inputs, and product-level long-form song workflow are material;
   - architecture authority appears weaker than Lyria/Stable Audio, so default role is capability/ecosystem evidence unless stronger technical sources are found.
   - Primary: https://suno.com/release-notes and https://www.suno.com/blog/introducing-v6

4. **ElevenLabs Music v2/v2.5**
   - candidate secondary closed workflow comparator for composition plans, audio reference, long-form composition and inpainting.
   - Primary: https://elevenlabs.io/docs/overview/capabilities/music

### Video

1. **ByteDance Seedance 2.5**
   - unified audio-video joint generation;
   - up to 30-second single-pass creation plus continuation;
   - multimodal reference and editing;
   - strong capstone candidate for 'clip -> creative work / storytelling' transition.
   - Primary: https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5

2. **Google Veo 3.1**
   - native audio, reference ingredients/style, prompt adherence and physics evaluation;
   - good closed current comparator with model-card/benchmark authority.
   - Primary: https://deepmind.google/models/veo/

3. **Black Forest Labs FLUX 3**
   - 2026 early-access multimodal image/video/audio joint model;
   - useful as a convergence case and for examining shared media foundation models.
   - Primary: https://bfl.ai/blog/flux-3

4. **Kuaishou Kling AI 3.0 / Omni**
   - native multimodal video architecture claim; generation + editing + audio; up to 15-second generation in the launch authority;
   - investigate technical disclosure depth before assigning a mechanism role.
   - Primary: https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be

5. **Runway Gen-4.5 / Aleph 2.0 workflow**
   - Gen-4.5 is current high-end T2V/I2V production case; Aleph is relevant to editing separation;
   - useful for production workflow/control/runtime comparison, likely weaker as architecture authority.
   - Primary: https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5

6. **Luma Ray3.x**
   - professional/HDR/keyframe/reference/control direction;
   - current status must be rechecked at Discovery because Ray3 subversions changed during 2026.
   - Primary: https://lumalabs.ai/ray3 and https://lumalabs.ai/news/introducing-ray-3-2

7. **Wan open video lineage**
   - mandatory open-weight/runtime lane even if a later Wan release supersedes Wan2.2;
   - Wan2.2 is historically useful for open MoE video diffusion and local runtime ecosystem, but Discovery must identify the current official Wan release and not freeze on the 2025 version.
   - Starting point: https://github.com/Wan-Video/Wan2.2

8. **OpenAI Sora / Sora 2**
   - mandatory historical turning point, but **not a current 2026 product capstone**: Sora web/app ended 2026-04-26 and the Sora 2 Videos API shutdown date is 2026-09-24.
   - This lifecycle is editorially useful: frontier research impact, product longevity, and ecosystem authority are different dimensions.
   - Primary: https://openai.com/index/sora/ and https://developers.openai.com/api/docs/deprecations

---

## 7. Source-authority policy for Muse Discovery

Preferred authority order depends on claim type; there is no single universal ordering.

### Architecture / method claims

Prefer:

1. peer-reviewed paper / author-hosted technical report;
2. official model technical report/model card;
3. official implementation / weights repository;
4. official research blog with concrete technical detail;
5. vendor product documentation for product capabilities;
6. independent reproduction/measurement for deployment behavior;
7. press/community material only for reception/adoption context.

### Current product/capability claims

Official release notes/product docs can be primary authority for availability, supported inputs/outputs, duration, API IDs, deprecation dates, and documented feature surface. They are **not automatically sufficient** for architecture or comparative superiority.

### Benchmark claims

Capture at minimum:

- exact model/version;
- benchmark version;
- prompt/sample count;
- resolution/duration/sample rate;
- sampling/inference budget when disclosed;
- human evaluator population/protocol when disclosed;
- baseline versions;
- whether the source is model-vendor-authored;
- whether generated samples/settings are available for reproduction.

A vendor leaderboard is a vendor claim until independently reproduced. Do not normalize incompatible benchmark scores into a single ranking.

### Community/X evidence

As with TS-001, community evidence may be valuable for:

- deployment friction;
- open-weight/local execution;
- reproducibility;
- workflow adoption;
- visible failure modes;
- product reception.

It is not technical authority for architecture unless it directly points to primary code/report evidence.

---

## 8. Muse Discovery completeness obligations

The first Muse run should stop at **fresh Discovery completeness review**, not Screening, unless a later execution contract explicitly changes the stop point.

Discovery is incomplete if any of the following remains unrepresented by credible source targets:

- VAE/VQ-style representation lineage;
- GAN/StyleGAN lineage;
- autoregressive image/audio lineage;
- DDPM + score-based lineage;
- latent diffusion;
- DiT;
- flow matching / rectified-flow lineage;
- classifier-free guidance;
- spatial/reference control and ControlNet lineage;
- image editing lineage;
- WaveNet/Tacotron/VITS or equivalent speech-history anchors;
- SoundStream/EnCodec neural codec lineage;
- codec language model / VALL-E lineage;
- flow-based modern speech generation/editing;
- AudioLM/MusicLM/MusicGen;
- diffusion/flow music/audio lane;
- long-form music structure/control;
- Video Diffusion / Imagen Video / Phenaki historical lane;
- modern video foundation/Transformer lane;
- reference/identity/video editing;
- native audio-video generation;
- long-duration/continuation/storytelling;
- open-weight/local video execution;
- image/audio/video evaluation methodology;
- runtime/few-step/distillation or other generation-efficiency evidence;
- current 2025–2026 image capstones;
- current speech/native-audio capstones;
- current music capstones;
- current video capstones;
- TS-002/TS-003 boundary cases;
- technical provenance/watermark/content-credential mechanisms where material.

The completeness review should explicitly report negative space: important lanes searched but lacking adequate technical authority, especially for closed commercial systems.

---

## 9. Expected research shape before Architecture

A plausible evidence-backed architecture may eventually resemble:

1. Why media generation is not just 'LLM beyond text'
2. Representing media: continuous latent, discrete token, neural codec, spatiotemporal compression
3. Generative paradigms: autoregression, adversarial learning, diffusion/score, flow
4. Conditioning, guidance, reference, and control
5. Image generation and the transition to editing
6. Speech and voice: waveform -> end-to-end -> codec LM -> native realtime audio
7. Music/general audio: codec LM vs latent diffusion and long-form structure
8. Video: temporal coherence -> media foundation models -> synchronized audiovisual storytelling
9. Runtime and deployment: sampling steps, latency, local/open execution, streaming
10. Evaluation: fidelity, alignment, identity, structure, temporality, physics, human preference
11. Convergence: unified multimodal media models vs specialized generators + reasoning/agents

This is **not** the Architecture Review and must not be treated as a frozen chapter plan. Evidence density and Selection negative-space review may split or merge these packages.

---

## 10. Explicit research cautions

- Do not infer unpublished architecture from UI behavior.
- Do not use a product family name without exact version/date where versions materially differ.
- Do not confuse maximum supported duration with demonstrated long-horizon coherence.
- Do not compare 720p 5-second video with 1080p 30-second video by a single quality score without controlling conditions.
- Do not equate native audio output with a single jointly generated audiovisual latent unless technical authority supports that mechanism.
- Do not equate 'reasoning image/video model' marketing language with a specific reasoning architecture.
- Do not treat open weights, open source, reproducible training, and permissive license as synonyms.
- Do not make copyright/policy disputes the narrative spine. Capture training-data/license/consent/provenance facts only where technically or operationally material.
- Do not let image-generation evidence stand in for audio/video evidence merely because diffusion terminology is shared.

---

## 11. Next handoff state

Before Muse is given a production Discovery instruction:

1. Human/Sol review this scaffold for scope direction.
2. Synchronize the stale `TS-001-REISSUE-2026` backlog state from `SELECTED` to its actual `RELEASED` state.
3. Deepen the TS-002 backlog entry using this scaffold without turning the lightweight backlog into a full evidence ledger.
4. Create TS-002 production identity / issue / branch / Profile according to the current Special pipeline.
5. Freeze an exact starting SHA and reviewed `main` SHA for Muse.
6. Give Muse a **bounded primary-technical Discovery request** that consumes this scaffold as mandatory research obligations.
7. Keep X/community collection as a separate pass after primary technical completeness is demonstrated, unless production-core rules require a different ordering.

Until those steps occur, this document remains a planning/research authority only.
