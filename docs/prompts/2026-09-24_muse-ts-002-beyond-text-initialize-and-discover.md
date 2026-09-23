# TS-002 Beyond Text — Muse initialization + primary-technical Discovery execution request

Status: `EXECUTION_AUTHORITY / INITIALIZE_THEMATIC / DISCOVERY_ONLY / STOP_FOR_SOL_REVIEW`

Date: `2026-09-24 JST`

Repository: `eariver/japanese-generative-ai-survey`

GitHub production Issue: `#526`

Edition identity:

- Planning identity: `TS-002`
- Machine identity: `SP-beyond-text-2026`
- Stable slug: `beyond-text-2026`
- Reader-facing working title: `Beyond Text — 画像・音声・音楽・映像生成AIの技術史`
- Research profile: `THEMATIC`
- Publication profile: `LONGFORM_SPECIAL`
- Temporal mode: `OPEN_HISTORY_AS_OF`
- Work branch: `special/beyond-text-2026-work`
- Canonical source root after initialization: `sources/SP-beyond-text-2026/`
- Canonical survey root: `surveys/special/beyond-text-2026/`
- Eventual Human gate: `ARCHITECTURE_REVIEW`
- This run terminal stop: `DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW`

---

## 0. Exact start guards — mandatory zero-write gate

Before any repository mutation, fetch the remote refs read-only and verify all of the following exactly:

```text
remote special/beyond-text-2026-work HEAD
  == fc17a75f068edbf6080d3614ed60539a444286c7

remote special/beyond-text-2026-work tree
  == d6d54ba549c85d285b509e1b413613048bdc4a7b

remote main HEAD
  == 0bbb02b3c5963403860897daec2feaf61e82589a

remote main tree
  == e4ddde5ed5059d303b818f54e27204369b256bcb
```

If **any one** of these values differs:

1. perform **zero writes** to GitHub/repository;
2. do not create another branch;
3. do not reset, force-push, rebase, cherry-pick, or create a fallback/repair/review branch;
4. report expected vs actual HEAD/tree values and stop.

The current `main` HEAD contains two no-op connector-history commits after the prior clean authority, but its tree is intentionally identical to `9b635adf6f2be535009d17feb50dda4e520a49c2`. Do not rewrite or clean up `main`; merely use the exact guard above for this run.

All writes in this execution belong only on the existing branch:

`special/beyond-text-2026-work`

Pushes must be normal/non-force fast-forwards.

---

## 1. Mission

Initialize TS-002 through the repository's current generic Thematic Special production path, materialize the Sol-designed research scope into canonical Core-v2-compatible edition artifacts, perform a **primary-technical Discovery expansion**, validate the resulting Discovery state, and stop for a fresh Sol Discovery Completeness Review.

This is **not** a request to produce a draft Special.

The normal path for this run is:

```text
existing Sol pre-research scaffold
-> exact guard PASS
-> inspect current generic THEMATIC / LONGFORM_SPECIAL initialization authority
-> synchronize planning status metadata
-> INITIALIZE_THEMATIC for SP-beyond-text-2026
-> materialize canonical research-scope-v2 with all required obligations
-> prepare execution request/receipt/run identity under edition root
-> primary-technical Discovery collection
-> normalize / provenance-bind Discovery using the current pipeline
-> edition-level Discovery validation / completeness accounting
-> safe checkpoint commit(s)
-> DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW
-> STOP
```

Do not proceed beyond that stop.

---

## 2. Mandatory read order

After the guards pass and before initialization/collection, read the following in order.

### 2.1 Current production authority

Read the current repository documentation/scripts/configuration that define:

- generic `THEMATIC` initialization;
- `LONGFORM_SPECIAL` publication profile;
- `INITIALIZE_THEMATIC` or its current equivalent;
- production-state/profile schema `2.0-rc1` or the current frozen equivalent;
- Discovery stage lifecycle and exact validators;
- frozen-Core defect handling / edition-local compatibility rules.

Do not infer invocation syntax from this prompt if repository authority has changed; use the current checked-in generic initializer and validators.

### 2.2 TS-002 Sol research authority

Read in full:

1. `docs/research-plans/2026-09-24_ts-002-beyond-text-sol-preresearch.md`
2. `docs/research-plans/2026-09-24_ts-002-beyond-text-muse-discovery-contract-draft.md`
3. GitHub Issue `#526`
4. `docs/thematic-special-backlog.md` for editorial lineage/boundary only.

The two Sol documents are not Evidence and do not substitute for external sources. They are the **research map and anti-thinness contract** that Discovery must consume rather than silently compress.

### 2.3 Frozen-Core maintenance context

Read the current:

`docs/core-v2-deferred-maintenance-summary.md`

Shared Core v2 remains frozen. Known generic defects must not trigger ad hoc shared-Core edits during this edition.

---

## 3. Planning metadata synchronization

Before or as part of initialization, update `docs/thematic-special-backlog.md` on this branch only so repository planning metadata matches reality.

Required bounded changes:

- `TS-001-REISSUE-2026 — Efficient Intelligence`: `SELECTED` -> `RELEASED`.
- `TS-002 — Beyond Text: Generative Media`: advance from `SCOPED` to the status appropriate for active production (`ACTIVE` once initialization/Discovery work has actually begun).

Do not rename historical `TS-001` or rewrite unrelated backlog entries.

Preserve the existing TS-002 / TS-003 editorial boundary:

```text
TS-002: what AI can generate and by what representation/generation/control/editing mechanisms.
TS-003: how AI perceives, recognizes, understands, and reasons about the world across modalities.
```

---

## 4. Initialization requirements

Use the repository's current generic Thematic initialization path. Do not hand-invent a reduced production state if the initializer can produce the canonical artifacts.

The initialized edition must use:

```text
issue_id: SP-beyond-text-2026
research_profile: THEMATIC
publication_profile: LONGFORM_SPECIAL
source_root: sources/SP-beyond-text-2026
survey_root: surveys/special/beyond-text-2026
work_branch: special/beyond-text-2026-work
temporal_mode: OPEN_HISTORY_AS_OF
```

Bind GitHub production tracking to Issue `#526` where the current pipeline supports such metadata.

Use the actual initialization time for `as_of` / materialization timestamps rather than copying a TS-001 timestamp.

Do not copy final-state TS-001 production-state fields into the new edition. TS-001 may be used as a structural example only.

---

## 5. Canonical research question

Materialize a canonical question equivalent in meaning to:

> High-dimensional continuous media — pixels, waveforms, frames, motion, and synchronized sound — became tractable for generative modeling through changes in representation, generative objective, conditioning, control/editing, temporal structure, sampling/runtime, and evaluation. How did those choices evolve across image, speech/voice, music/general audio, and video; what bottleneck did each major transition solve; what trade-offs did it introduce; and how are formerly separate media-generation stacks converging in current multimodal systems?

Do not replace this with a product-list question such as “what are the major image/audio/video generators?”

---

## 6. Mandatory canonical scope dimensions

The canonical `research-scope-v2.json` must represent **all** of the following as first-class dimensions/obligations. Naming can follow current schema conventions, but semantic coverage must not be collapsed.

### D01 — Media representation / compression / tokenization

Mandatory lineage/questions include:

- VAE and learned continuous latent spaces;
- VQ-VAE / discrete codebooks;
- VQGAN / perceptual-adversarial tokenizers where material;
- image latent autoencoders used by latent diffusion;
- neural audio codecs such as SoundStream/EnCodec lineage;
- semantic vs acoustic token separation where material;
- video/spatiotemporal VAE/tokenizer design;
- compression ratio / token rate / latent rate as a systems variable;
- representation loss and how it bounds downstream generation fidelity/editability.

The edition must establish that media-generation history is partly a history of making pixels/waveforms/frames cheap enough to model.

### D02 — Generative paradigms / objectives

Distinguish architecture from objective.

Mandatory lineage/questions include:

- VAE-style likelihood/variational generation;
- autoregressive image/audio/media modeling;
- GANs and adversarial training;
- DDPM / diffusion probabilistic models;
- score-based generative modeling;
- latent diffusion;
- Diffusion Transformer (DiT) / transformer denoisers;
- flow matching / rectified-flow-related lineages where supported;
- hybrid or distillation objectives when current systems materially depend on them.

For each major transition ask: bottleneck, mechanism, quality/diversity/stability/control/compute effect, downside, inheritance.

### D03 — Conditioning / semantic alignment

Mandatory topics include:

- class conditioning and text conditioning;
- cross-attention-based conditioning;
- classifier guidance and classifier-free guidance;
- CLIP/T5/other text encoders where they are load-bearing for generation;
- multi-input/reference conditioning;
- prompt adherence and compositional binding;
- conditioning representations for speech/music/video.

Do not turn this lane into a general VLM history; generation relevance is required.

### D04 — Control / reference / identity

Mandatory topics include:

- spatial controls (edge/depth/pose/segmentation etc.) with ControlNet-style lineage;
- adapters/reference encoders where material;
- identity/character preservation;
- style vs content reference;
- multi-reference generation;
- camera/motion controls in video;
- melody/rhythm/lyrics/voice/speaker controls in audio/music/speech;
- failure modes when control conflicts with diversity or preservation.

### D05 — Editing / preservation

Treat editing as distinct from de-novo generation.

Mandatory topics include:

- image-to-image;
- inpainting/outpainting;
- local/region editing;
- instruction-based editing;
- reference editing;
- multi-turn iterative editing;
- preservation of untouched content;
- audio/speech continuation or infilling where material;
- video editing / transformation / reference-preserving modification.

### D06 — Temporal / long-horizon consistency

Mandatory modality-specific problems include:

Speech/voice:
- speaker identity;
- prosody;
- timing/rhythm;
- conversational continuity;
- streaming/realtime constraints.

Music/general audio:
- motif/theme persistence;
- verse/chorus/bridge or analogous long-form structure;
- lyrics/vocal coherence;
- multi-minute generation;
- continuation/editing consistency.

Video:
- motion coherence;
- object permanence / identity;
- camera continuity;
- scene/shot continuity;
- temporal flicker;
- physics/dynamics claims with appropriate caution;
- synchronized audio and audiovisual continuity;
- long-video / extension / multi-shot storytelling.

### D07 — Speech / voice lineage

Must establish a dedicated lineage, not bury speech under music.

At minimum investigate:

- WaveNet;
- Tacotron-family milestones;
- neural vocoder evolution sufficient to understand modern TTS;
- VITS and end-to-end generative TTS where material;
- neural audio codecs;
- codec-language-model approaches such as VALL-E lineage;
- zero/few-shot speaker cloning;
- flow-matching speech generation / editing such as Voicebox lineage;
- expressive multilingual/streaming systems such as Seamless lineage;
- 2025–2026 native realtime speech-to-speech / audio multimodal systems.

### D08 — Music / general audio lineage

At minimum investigate:

- early neural audio/music generation sufficient to establish continuity;
- Jukebox;
- AudioLM;
- MusicLM;
- MusicGen / AudioCraft;
- latent-diffusion / DiT audio systems such as Stable Audio lineage;
- long-form commercial music generation as capability/ecosystem cases;
- lyrics/vocal structure/control;
- editing/continuation;
- rights/training-data/provenance only where technically load-bearing, not as the main policy narrative.

### D09 — Video lineage

At minimum investigate:

- early learned video generation sufficient to contextualize diffusion-era work;
- Video Diffusion Models;
- Imagen Video;
- Phenaki;
- latent-video/spatiotemporal diffusion/transformer methods;
- image-to-video and reference-conditioned video;
- video personalization/editing;
- Movie Gen as a major technical anchor where supported;
- current audio-video joint generation;
- open-weight/current deployment cases such as Wan where material.

### D10 — Runtime / deployment / acceleration

Mandatory topics include:

- latent/token rate and its compute consequence;
- sampling steps / solver cost;
- distillation / consistency/few-step/adversarial post-training where material;
- resolution and duration scaling;
- VRAM / memory pressure where documented;
- time-to-first-output / generation latency / real-time factor;
- streaming generation;
- local/open-weight execution when materially documented;
- why a visually/audibly stronger model may still be impractical under a different sampling budget.

Do not collapse runtime into generic “faster generation”.

### D11 — Evaluation methodology / metric validity

Evaluation is a mandatory standalone research lane.

Image candidates include:
- FID and known interpretation limits;
- CLIP-based alignment where relevant;
- GenEval;
- T2I-CompBench or equivalent compositional diagnostics;
- human preference methodology.

Speech/audio/music candidates include:
- MOS/MUSHRA-style human evaluation where applicable;
- WER/content preservation for speech;
- speaker similarity;
- prosody/expressivity;
- Fréchet Audio Distance and its limitations;
- text-audio alignment;
- music structure / musicality / long-form evaluation and known weakness of simple metrics.

Video candidates include:
- VBench or equivalent multidimensional evaluation;
- temporal consistency/flicker;
- subject/background consistency;
- motion quality;
- prompt adherence;
- audiovisual synchronization for joint generators;
- human evaluation methodology.

For any reported score/value, capture enough context to prevent invalid ranking across different versions, resolutions, durations, sampling budgets, prompt sets, seeds, human-study populations, or evaluator models.

### D12 — Multimodal convergence / generation-understanding boundary

Investigate:

- transition from text encoder + separate media generator toward richer multimodal conditioning;
- unified/native multimodal token/latent approaches where primary evidence exists;
- generators that consume image/audio/video references as context;
- integration with LLM/agent systems where it materially changes generation/editing workflows;
- proximity of video generation to world-model language, with explicit evidence boundaries;
- cases where generation and understanding share a model surface.

Do not absorb general perception/VLM history from TS-003.

---

## 7. Historical anchor expectations

Discovery must deliberately seek primary/technical authority for the major historical anchors named in the Sol pre-research scaffold. The following are seed anchors, not an exhaustive whitelist:

```text
VAE
VQ-VAE
VQGAN / learned visual tokenizers
GAN / DCGAN / StyleGAN lineage where material
autoregressive image generation
DDPM
score-based generative modeling
classifier-free guidance
latent diffusion / Stable Diffusion technical lineage
DiT
flow matching / rectified-flow-related lineage
ControlNet
modern reference / identity / editing systems

WaveNet
Tacotron lineage
VITS
SoundStream
EnCodec
VALL-E lineage
Voicebox
Seamless expressive/streaming lineage

Jukebox
AudioLM
MusicLM
MusicGen / AudioCraft
Stable Audio technical lineage

Video Diffusion Models
Imagen Video
Phenaki
Movie Gen
current spatiotemporal transformer / latent video lineages
```

For priority/history claims, prefer original papers, official technical reports, project repositories/model cards, or authoritative release documentation. Do not establish historical priority from secondary summaries alone.

---

## 8. 2025–2026 current-capstone discovery lanes

Do not pre-rank products. Current-capstone collection should seek **mechanism diversity** and evidence authority.

At minimum investigate current or recently current primary sources for:

### Image / editing
- Black Forest Labs FLUX family, especially generation/editing/reference developments;
- ByteDance Seedream current generation/editing lineage;
- OpenAI current image-generation/editing models;
- Google current image-generation/editing models (Imagen / Gemini-native image surfaces as applicable);
- at least one meaningful open/open-weight current ecosystem case.

### Speech / native audio
- OpenAI current realtime/native speech/audio systems;
- Google/Gemini current native audio systems;
- Meta or other technical/open research lineage where useful;
- current speech generation/editing/cloning systems with actual technical authority.

### Music / audio
- Google DeepMind Lyria current lineage;
- Stability AI Stable Audio current lineage;
- Suno current generation as a closed commercial capability/workflow case;
- additional materially distinct technical/open systems if they improve mechanism coverage.

### Video
- Google DeepMind Veo current lineage;
- ByteDance Seedance current lineage;
- Runway current lineage as a production/workflow capability case;
- Wan/open-weight current video lineage;
- other materially distinct current systems (Kuaishou/Kling, Alibaba, Meta, Adobe, etc.) where primary evidence materially improves mechanism/system coverage.

### Sora lifecycle case
Sora remains historically important but must not automatically be treated as the single “current frontier” capstone. Verify its current 2026 product/API lifecycle through first-party sources and use it as a technical/lifecycle case with dates and availability boundaries.

All named current candidates must be refreshed at execution time. Do not assume the Sol pre-research snapshot is the latest release state.

---

## 9. Source authority policy

Use the strongest available source for each claim type.

Preferred technical authority hierarchy for load-bearing architecture/history/spec claims:

1. original peer-reviewed/preprint paper or official technical report;
2. official model/system card with architecture/evaluation detail;
3. official project repository/documentation;
4. official release post for availability/product behavior;
5. independent reproduction/evaluation where available;
6. secondary reporting for discovery leads/context only when stronger authority is unavailable.

Closed vendor pages may establish documented capability, availability, workflow, or vendor benchmark claims. They do **not** establish undisclosed architecture by inference.

Community/X material is **not part of this first run**. It may be designed later as a separate reception/deployment pass after primary Discovery completeness review.

---

## 10. Required source metadata / provenance quality

For each Discovery record, retain the current Core v2-required provenance and enough semantic metadata to support later Evidence consumption. At minimum, where applicable:

- canonical URL;
- source title;
- source owner/authors;
- publication/release date;
- accessed/retrieved date;
- source type/class;
- modality;
- mandatory dimension(s) served;
- model/system/version if applicable;
- primary vs secondary authority;
- vendor vs independent status;
- exact relevant section/claim target when identifiable;
- notes on scope limitations;
- lifecycle/availability date when relevant.

Avoid one-source-per-obligation bookkeeping if one authoritative technical report legitimately supports several obligations; however, do not let a few broad vendor pages masquerade as depth across the whole edition.

---

## 11. Discovery completeness requirements

A large count is not a PASS.

Before declaring `DISCOVERY_COLLECTED`, produce machine-readable or Markdown accounting that allows Sol to review at least:

### 11.1 Dimension coverage
For each D01–D12:
- number of candidate sources;
- number of primary/technical authorities;
- historical-anchor coverage;
- current-system coverage where applicable;
- unresolved gaps.

### 11.2 Modality coverage
Separate accounting for:
- image;
- speech/voice;
- music/general audio;
- video;
- cross-modal/unified systems.

Image source volume must not hide weak speech/music/video coverage.

### 11.3 Historical transition coverage
For each major transition expected by the scaffold, state whether Discovery currently contains enough authority to later answer:

```text
prior bottleneck
-> changed representation/objective/architecture/control mechanism
-> measured or documented benefit
-> trade-off / failure mode
-> later inheritance/adoption
```

### 11.4 Current capstone coverage
For each current-capstone lane:
- architecture/mechanism authority if public;
- capability/workflow authority;
- evaluation methodology;
- runtime/deployment information where public;
- open/closed status;
- availability/lifecycle;
- independent evidence if any;
- explicit unknowns where architecture is undisclosed.

### 11.5 Evaluation coverage
Show that evaluation sources are not merely benchmark leaderboards. Discovery must contain authority about what the metrics/benchmarks measure and their limitations.

### 11.6 Negative-space report
Explicitly report important expected topics for which strong authority was not found, architecture is closed, independent validation is absent, or historical linkage remains uncertain.

Do not silently fill those gaps later with inference.

---

## 12. Anti-thinness acceptance rules

Discovery is not ready for Sol review if any of the following is true:

- the history effectively starts at Stable Diffusion;
- GAN -> diffusion is presented as the only meaningful transition;
- representation/tokenization is under-sourced;
- speech is reduced to a few TTS product releases;
- music is mostly Suno/service news;
- video is mostly Sora/Veo/Runway marketing pages;
- editing/reference/identity lacks an independent historical lane;
- temporal/long-horizon consistency lacks modality-specific evidence;
- evaluation is only a collection of scores;
- runtime/sampling cost is absent;
- current closed products are treated as if architecture were known;
- TS-003 understanding/perception history has swallowed the generation focus;
- source quantity is high but one or more D01–D12 dimensions lack load-bearing primary authority.

When a lane truly lacks public primary authority, mark the limitation instead of fabricating completeness.

---

## 13. Core v2 freeze / defect policy

Shared Core v2 is frozen for this edition.

Do not modify generic shared:

- schemas;
- Core scripts;
- reusable workflows;
- Core production lifecycle docs;
- generic renderer/validator behavior;

merely to make TS-002 pass.

If a known frozen-Core problem recurs, identify it against the deferred-maintenance inventory and use an already-established safe edition-local workaround where possible.

If a genuinely new generic defect appears:

1. record it under the edition's execution/defects area or current equivalent;
2. identify impact and reproducibility;
3. use bounded edition-local compatibility only if semantically safe and reproducible;
4. do not silently alter canonical Discovery/Screening meaning to satisfy a validator;
5. if no safe compatibility exists, stop at the blocking state and report it.

---

## 14. Write discipline

Allowed writes are only those required for this authorized TS-002 initialization and Discovery run on the existing work branch.

Do not:

- create additional branches;
- modify `main`;
- force-push;
- reset or rewrite branch history;
- start Screening/Evidence/Selection/Architecture;
- generate reader-facing draft prose or PDF;
- create Human approval decisions;
- collect X/community material in this run;
- perform shared-Core maintenance.

Use normal commits at meaningful safe checkpoints. Avoid tiny commit spam, but do not hold all work in an uncommitted state until the end.

---

## 15. Required terminal state and report

Successful first-run terminal state:

`DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW`

At stop, report all of the following:

1. exact starting work-branch HEAD/tree and main HEAD/tree actually verified;
2. final remote work-branch HEAD/tree after read-back;
3. initialization method used and resulting production identity/profile paths;
4. canonical `research-scope-v2.json` path and obligation count;
5. Discovery record count and unique-source count;
6. counts by source authority/type;
7. counts by modality;
8. counts/coverage by D01–D12;
9. historical anchor coverage summary;
10. current-capstone coverage summary;
11. evaluation-methodology coverage summary;
12. negative-space/unresolved-gap summary;
13. any edition-local compatibility used;
14. any deferred-Core defect observed;
15. exact changed-path list;
16. validation commands/checks executed and their outcomes;
17. confirmation that Screening and later stages were not run;
18. confirmation that X/community pass was not run;
19. confirmation of non-force push and remote read-back.

Also leave enough durable repository state under `sources/SP-beyond-text-2026/execution/` (or current canonical equivalent) for a subsequent Sol session to reproduce what was executed without relying on chat history.

Then stop and wait for Sol Discovery Completeness Review.
