# TS-002 Beyond Text — Muse Discovery execution contract draft

Status: `DRAFT / NOT_EXECUTABLE / SOL_PRERESEARCH_HANDOFF`

Date: `2026-09-24 JST`

Companion authority:

- `docs/research-plans/2026-09-24_ts-002-beyond-text-sol-preresearch.md`

This document exists to preserve the research intent when TS-002 is handed from Sol to Muse Spark 1.3 / OpenCode. It is deliberately **not executable yet**: production identity, production Issue, work branch, exact starting SHA, reviewed main SHA, Profile, and canonical source root must be created/frozen under the then-current Special pipeline before this draft can be promoted to an execution request.

No worker should infer missing production identifiers from this draft.

---

## 1. Mission

Perform a **primary-technical Discovery expansion** for TS-002 Beyond Text sufficient for a fresh Sol Discovery Completeness Review.

The worker's task is not to decide the final narrative, not to rank current products, and not to compress the subject into a model catalogue. The worker must materialize a provenance-rich source map that allows later Screening/Evidence/Selection/Architecture to reconstruct the technical history of image, speech/voice, music/general audio, and video generation across common system dimensions.

Expected stop point:

`DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW`

Unless a later Human/Sol instruction explicitly changes this boundary:

- do **not** run Screening;
- do **not** generate Evidence;
- do **not** perform Selection;
- do **not** produce Architecture;
- do **not** draft publication prose;
- do **not** generate a Human decision;
- do **not** begin the X/community pass merely because primary Discovery appears large.

A large source count is not itself completeness.

---

## 2. Mandatory read order before any collection

At execution time, Muse must read in this order:

1. the current Special production pipeline/profile authority designated by the eventual execution request;
2. the canonical TS-002 production Profile and state files created for the edition;
3. `docs/research-plans/2026-09-24_ts-002-beyond-text-sol-preresearch.md` in full;
4. this execution-contract draft as promoted/finalized for the production run;
5. `docs/thematic-special-backlog.md` only for editorial lineage/boundary, not as a substitute for the deeper Sol scaffold;
6. current Core v2 deferred-maintenance inventory so known frozen-Core defects are not rediscovered as ad hoc production changes.

The Sol pre-research file is a **mandatory research-obligation input**, not optional background reading.

Muse must not summarize it into a shorter checklist and then discard the original dimensions. Every D01–D12 lane must remain traceable in Discovery coverage reporting.

---

## 3. Production guard placeholders

Before this draft is made executable, replace the following placeholders with exact values:

```text
Repository: eariver/japanese-generative-ai-survey
Production work branch: <TO_BE_CREATED>
Exact Starting SHA: <TO_BE_FROZEN>
Expected Starting Tree: <OPTIONAL_IF_PIPELINE_REQUIRES>
Reviewed main SHA: <TO_BE_FROZEN>
Production Issue: <TO_BE_CREATED>
Edition identity: <TO_BE_CREATED>
Canonical source root: <TO_BE_CREATED>
Canonical Profile: <TO_BE_CREATED>
```

Execution guard must require read-only confirmation that all supplied branch/main/tree values match exactly. On any mismatch: **zero repository/GitHub writes and stop with expected vs actual values**.

No fallback branch, repair branch, review branch, or alternate edition identity may be invented by the worker.

All pushes must be normal non-force updates.

---

## 4. Research question to preserve verbatim in substance

> High-dimensional continuous media — pixels, waveforms, frames, motion, and synchronized sound — became tractable for generative modeling through changes in representation, generation objective, conditioning, control/editing, temporal structure, sampling/runtime, and evaluation. How did those choices evolve across image, speech, music, and video; what bottleneck did each transition address; what trade-offs did it introduce; and how are formerly separate media-generation stacks converging in 2025–2026?

Discovery must collect sources that allow later stages to answer the **mechanism and transition questions**, not only describe what a product can generate.

---

## 5. Mandatory research lanes — D01 through D12

Muse must maintain a coverage ledger keyed to all twelve dimensions from the companion Sol scaffold.

### D01 Representation / compression / tokenization

Required source families include:

- VAE;
- VQ-VAE / discrete latent representations;
- latent image autoencoders;
- neural audio codecs (SoundStream/EnCodec lineage);
- semantic + acoustic token representations (AudioLM and successors where material);
- spatiotemporal/video tokenizers or VAEs;
- current media autoencoders where they materially change runtime, quality, or long-horizon modeling.

Discovery must seek quantitative representation facts where primary sources disclose them: compression ratio, token/frame rate, codebook structure, latent dimensionality, reconstruction quality, sample/frame rate, or equivalent.

### D02 Generative paradigm / objective

Required source families:

- autoregressive image/audio/media generation;
- GAN/adversarial lineage;
- DDPM;
- score-based SDE lineage;
- latent diffusion;
- DiT;
- flow matching;
- rectified-flow or closely related current flow formulations where materially adopted;
- hybrid/adversarial post-training or few-step generation when current systems use it.

Keep **backbone architecture** (for example U-Net vs Transformer) separate from **generative objective/process** (AR vs adversarial vs diffusion vs flow).

### D03 Conditioning / alignment / guidance

Required topics:

- class and text conditioning;
- cross-attention / text encoder roles;
- classifier guidance and classifier-free guidance;
- multimodal/reference conditioning;
- melody/lyrics/timing conditions where relevant;
- multi-reference inputs;
- training-time conditioning vs inference-time guidance vs adapters vs in-context references.

### D04 Control / reference / identity / preservation

Required topics:

- ControlNet or equivalent historical control transition;
- subject/character identity;
- speaker identity;
- style vs content reference;
- camera/motion/keyframe control;
- first/last-frame or temporal reference control;
- music/audio structural/reference control;
- preservation metrics or evaluations where available.

### D05 Editing

Required topics:

- image-to-image;
- inpainting/outpainting;
- instruction-based editing;
- local/region editing;
- multi-turn/reference editing;
- video editing/video-to-video;
- speech content editing while preserving voice identity;
- audio/music continuation/inpainting/remix;
- preservation of non-target content.

### D06 Image lineage

At minimum Discovery must cover the historical chain needed to explain:

`latent-variable / autoregressive -> GAN/StyleGAN -> DDPM/score -> latent diffusion -> DiT -> controllable/reference/editing -> flow-era / multimodal generator-editor`.

Do not use current product pages as substitutes for the historical primary papers.

### D07 Speech / voice lineage

At minimum:

`WaveNet -> Tacotron/end-to-end TTS -> neural vocoder/end-to-end synthesis -> VITS -> neural codecs -> codec LM/VALL-E -> flow-based universal speech generation/editing -> zero-shot cloning -> expressive/multilingual -> streaming/full-duplex/native speech-to-speech`.

Preserve modality-specific evaluation: intelligibility/WER, naturalness/listening studies, speaker similarity, prosody/emotion, latency/streaming.

### D08 Music / general audio lineage

At minimum:

`Jukebox/raw or discrete AR -> neural codec -> AudioLM -> MusicLM -> MusicGen/AudioCraft -> latent diffusion/DiT audio -> long-form/current controllable music and scene-audio systems`.

Discovery must find sources capable of discussing structure, not just acoustic fidelity: sections, motif/repetition, lyrics/vocals, duration, continuation, inpainting, reference audio, stems where material.

### D09 Video lineage

At minimum:

`early temporal-generation context -> Video Diffusion Models -> Imagen Video -> Phenaki/compressed variable-length generation -> latent/spatiotemporal diffusion -> scaled video/media Transformers -> personalization/reference/editing -> native synchronized audio-video -> continuation/longer generation -> multi-shot/storytelling -> current open-weight runtime`.

Preserve failure/evaluation dimensions: identity, object permanence, temporal flicker, motion, camera, scene continuity, multi-shot continuity, prompt timing, physics/commonsense, human fidelity, lip/audio synchronization.

### D10 Long-horizon / temporal structure

Discovery must look beyond advertised maximum duration.

For speech/music/video sources, seek answers to:

- effective post-compression sequence length;
- generation process over time/chunks;
- state/cache/reference carried across continuation;
- global structure vs local texture continuity;
- identity/speaker/motif/scene state preservation;
- extension vs single-pass generation distinctions.

### D11 Runtime / deployment

When disclosed, capture:

- resolution;
- sample rate;
- frame rate;
- duration;
- latent/token rate;
- denoising/sampling steps;
- solver/distillation/few-step mechanism;
- time-to-first-output;
- real-time factor;
- VRAM/accelerator requirement;
- local/open-weight execution;
- quantization/offload/runtime support.

Do not convert absent runtime data into estimates unless an independent measurement source clearly supplies the methodology.

### D12 Evaluation / provenance / convergence

Discovery must include primary methodology sources for:

- FID and limitations;
- GenEval/T2I-CompBench or comparable compositional image evaluation;
- MOS/MUSHRA/listening protocols where material;
- WER/speaker similarity;
- Fréchet Audio Distance and text-audio alignment measures;
- long-form music structure evaluation where credible methods exist;
- VBench and VBench-2.0 or comparable decomposed video evaluation;
- current human preference methodology;
- identity/reference/editing preservation;
- audio-video synchronization.

Technical provenance mechanisms (watermark/content credentials/C2PA or comparable mechanisms) are in scope only where technically or operationally material. They must not displace the architecture/history focus.

---

## 6. Mandatory historical anchor seed list

The companion Sol scaffold contains canonical starting URLs. Muse must independently resolve canonical metadata and capture according to the production provenance rules.

These are **minimum seed anchors, not a whitelist**:

- Auto-Encoding Variational Bayes;
- Generative Adversarial Networks;
- PixelRNN/PixelCNN lineage;
- VQ-VAE;
- Image Transformer where useful;
- StyleGAN2 or the StyleGAN paper most appropriate for the historical claim;
- DDPM;
- score-based SDE generative modeling;
- Latent Diffusion Models;
- Classifier-Free Guidance;
- DiT;
- Flow Matching;
- ControlNet;
- WaveNet;
- Tacotron;
- VITS;
- SoundStream;
- EnCodec;
- AudioLM;
- VALL-E;
- Voicebox;
- Jukebox;
- MusicLM;
- MusicGen;
- Video Diffusion Models;
- Imagen Video;
- Phenaki;
- Movie Gen;
- FID;
- Fréchet Audio Distance;
- GenEval;
- T2I-CompBench;
- VBench;
- VBench-2.0.

Muse should follow citation graphs backward/forward where needed to establish missing predecessors, parallel inventions, or successors. It must not force a linear ancestry where the papers do not support one.

---

## 7. Mandatory current-capstone investigation

This is a **candidate set**, not Selection and not a ranking.

The worker must investigate enough current first-party authority to decide later whether each candidate is:

- a mechanism/architecture anchor;
- a capability/workflow case;
- an open-weight/deployment case;
- a lifecycle/ecosystem case;
- or insufficiently documented and therefore negative space.

### Image / editing candidates

- Black Forest Labs FLUX.2 family, including interactive/local variants where material;
- ByteDance Seedream 5.x current lineage;
- OpenAI GPT Image 2.5 / current ChatGPT Images generation-editing stack as capability case;
- Google Nano Banana 2 / Gemini image generation-editing as native-multimodal convergence case;
- Imagen lineage as historical/dedicated-generator comparator and lifecycle transition.

### Speech / native-audio candidates

- OpenAI GPT-Live / GPT-Realtime-2 current native realtime voice family;
- Google Gemini 3.8 Audio / Live;
- ByteDance SeedRealtime / Seed Audio current speech/scene-audio directions;
- any current open or research system required to prevent the lane becoming exclusively closed-vendor evidence.

### Music / general-audio candidates

- Google Lyria 3.5;
- Stability AI Stable Audio 3;
- Suno v6 current commercial workflow/capability case;
- ElevenLabs Music current lineage as secondary comparator where useful;
- other technically disclosed current model only if it adds a mechanism not already represented.

### Video candidates

- ByteDance Seedance 2.5;
- Google Veo 3.1;
- Black Forest Labs FLUX 3 convergence case;
- Kling AI 3.x / Omni current lineage;
- Runway Gen-4.5 and editing workflow where technically useful;
- Luma Ray current lineage;
- **current official Wan open-video lineage** — do not stop at Wan2.2 merely because it is a known historical open model; identify the current first-party release at execution time;
- OpenAI Sora/Sora 2 as a historical/lifecycle turning point, with the 2026 product/API retirement chronology verified from current primary authority.

Current means **current at the execution date**, not current as of this 2026-09-24 planning note. Version/deprecation status must therefore be refreshed when Muse actually runs.

---

## 8. Source-class and claim-authority rules

### Architecture claims

Prefer primary technical papers/reports/model cards/code. A product release page cannot establish an unpublished architecture merely because it uses architecture-like terminology.

### Capability/availability claims

Official release notes/product documentation are valid primary sources for documented feature surfaces, model IDs, limits, release/deprecation dates, supported inputs/outputs, and availability.

### Comparative claims

Capture the exact conditions and preserve vendor attribution. Do not rewrite a vendor comparison as an independent conclusion.

### Independent evidence

Seek independent evidence particularly for:

- local/open-weight deployability;
- VRAM/runtime claims;
- reproducibility;
- workflow friction;
- failure modes;
- version regressions/improvements.

Independent community material is not a substitute for technical architecture authority.

---

## 9. Discovery record minimum fields

Use the production schema as authoritative. In addition, the resulting corpus must make the following concepts recoverable either in structured fields or notes/coverage artifacts:

- canonical title;
- author/organization;
- publication/release date;
- source class;
- canonical URL/identifier;
- exact model/version/product where applicable;
- modality;
- D01–D12 research dimension tags;
- historical anchor vs current capstone vs evaluation/runtime/supporting role;
- architecture authority strength;
- capability authority strength;
- whether comparative numbers are vendor-authored;
- open-weight/open-source/closed distinction where applicable;
- supersession/deprecation/lifecycle notes;
- key predecessor/successor relations only when source-supported.

Do not silently overwrite canonical schema fields if these concepts require a sidecar coverage artifact under frozen Core v2.

---

## 10. Discovery completeness report required at stop point

Before stopping, Muse must produce a machine-readable or Markdown coverage report permitted by the production pipeline that reports at least:

1. source count by modality: image / speech / music-general-audio / video / cross-modal-evaluation-runtime;
2. source count and representative anchors for D01–D12;
3. current-capstone coverage by candidate family;
4. number of primary technical vs official product/model-card vs independent/community sources;
5. historical gaps;
6. current first-party documentation gaps;
7. benchmark/evaluation methodology gaps;
8. open-weight/runtime gaps;
9. TS-002/TS-003 boundary ambiguities;
10. **negative space** — searched topics/candidates for which adequate authority was not found.

A lane must not be marked complete merely because one source nominally mentions it. Completeness means later Evidence could make a technically substantive claim about mechanism, evolution, or limitation with traceable authority.

---

## 11. Anti-collapse checks before Muse reports completion

Muse must explicitly answer PASS/FAIL/UNKNOWN for the following:

- [ ] Image sources do not exceed the research design to the point that speech/music/video become token appendices.
- [ ] Representation/tokenization has multiple modalities represented.
- [ ] GAN/adversarial lineage remains represented after diffusion sources are collected.
- [ ] Diffusion, DiT, and flow matching are not collapsed into one undifferentiated category.
- [ ] Speech has a real lineage, not only current voice products.
- [ ] Music has long-horizon/structural evidence, not only text-audio fidelity.
- [ ] Video has temporal/identity/physics/multi-shot evidence, not only headline model releases.
- [ ] Editing exists as a first-class lane across at least image plus one temporal modality.
- [ ] Runtime/deployment has actual technical sources rather than marketing speed adjectives.
- [ ] Evaluation has methodology sources for image, audio/speech/music, and video.
- [ ] Current capstones include both closed frontier capability cases and at least one meaningful open/open-weight deployment lane where the ecosystem supports it.
- [ ] Sora is not incorrectly described as a current active product if the verified execution-date status remains retired.
- [ ] No product demo is used as general proof of physical realism, coherence, or benchmark superiority.
- [ ] TS-003 perception/understanding history has not leaked into TS-002 except where load-bearing for generation/control/editing.

Any FAIL must be reported to Sol rather than hidden by increasing total source count elsewhere.

---

## 12. Memory-safe execution guidance for Muse/OpenCode

The production worker may operate on constrained hardware. Therefore:

- prefer incremental source capture and deterministic append/merge operations;
- avoid loading the entire corpus into model context when a bounded lane can be processed independently;
- checkpoint after coherent modality/dimension batches;
- preserve exact provenance even when notes are produced in small batches;
- run validators at the stage boundaries required by the current pipeline rather than repeatedly reparsing all sources without need;
- do not sacrifice Discovery breadth merely to fit one LLM context window.

A suitable collection order is:

1. cross-modal foundations: D01/D02/D03;
2. image historical + control/editing;
3. speech/voice;
4. music/general audio;
5. video;
6. evaluation/runtime;
7. 2025–2026 current capstone refresh;
8. cross-lane citation-graph gap fill;
9. completeness/negative-space report.

This order is advisory for memory safety; completeness obligations are normative.

---

## 13. Explicitly deferred pass: community / X

Primary technical Discovery must first demonstrate coverage. After Sol reviews completeness, a separate X/community pass may be authorized to collect:

- local/open model deployment experience;
- independent sample/workflow observations;
- reproducibility;
- performance/VRAM measurements;
- adoption/reception;
- recurring failure patterns.

As in TS-001, this material should normally be labeled reception/deployment evidence rather than technical architecture authority.

---

## 14. Promotion checklist — required before this draft becomes executable

Sol/Human owner should not hand this directly to Muse until all are true:

- [ ] TS-002 production identity and slug are fixed.
- [ ] production Issue exists.
- [ ] production work branch exists.
- [ ] exact starting SHA is frozen.
- [ ] reviewed main SHA is frozen.
- [ ] Profile/canonical source root exists.
- [ ] current Special pipeline stop point is verified.
- [ ] Core v2 remains frozen unless Human Owner separately authorizes maintenance.
- [ ] current model/version/deprecation status has been refreshed where the 2026-09-24 planning snapshot may have aged.
- [ ] this draft has been copied/promoted into the canonical execution-request location with placeholders removed.

Until then: `NOT_EXECUTABLE`.
