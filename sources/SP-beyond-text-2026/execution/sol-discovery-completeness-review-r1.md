# TS-002 Beyond Text — Sol Discovery Completeness Review r1

Status: `SOL_DISCOVERY_COMPLETENESS_REVIEW_R1 / REQUEST_CHANGES / BOUNDED_DISCOVERY_REPAIR`

Date: `2026-09-24 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-beyond-text-2026`

Reviewed branch: `special/beyond-text-2026-work`

Reviewed HEAD: `f1cb5fb655cc7fbf02a537ffb2e25d1022aa74b3`

Reviewed tree: `43e2361f581d81d2623a107e0788b4b3c9d320bd`

Reviewed main HEAD: `0bbb02b3c5963403860897daec2feaf61e82589a`

Reviewed main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`

Decision: **REQUEST_CHANGES**. The first-run Discovery is structurally strong and should be preserved, but it is not yet ready to advance to Screening because current-capstone chronology/provenance contains a systematic date defect and several mandatory evaluation/runtime negative-space lanes deserve one bounded gap-fill pass.

---

## 1. What passed

The initial Discovery successfully avoided the main anti-thinness failure modes.

- 128 BASE Discovery records were materialized and accepted by the current Discovery graph validator.
- D01–D12 are all represented.
- Image is the largest single lane but not the whole edition: the coverage accounting reports image 55 records versus speech/audio/music/video combined 66 records.
- Representation/tokenization, generative paradigms, conditioning, control/reference, editing, temporal/long-horizon structure, speech, music/audio, video, runtime, evaluation, and convergence are all first-class.
- The historical map is not reduced to `GAN -> diffusion`. VAE/VQ/codec/tokenizer, AR, GAN, DDPM/score/LDM/DiT/flow, control/editing, codec-LM speech/audio, long-form music, video temporal modeling, distillation/runtime, and evaluation lineages are present.
- Current closed systems are generally labeled as capability/workflow cases rather than undisclosed architecture authority.
- Sora is treated as a lifecycle/historical case rather than a current frontier capstone.
- X/community collection was correctly deferred.
- The worker stopped at `DISCOVERY_COLLECTED`; Screening/Evidence/Selection/Architecture were not run.
- No shared Core-v2 files were modified in the execution commit.

This means the current 128-record map is a usable base. Do **not** discard it or restart Discovery from scratch.

---

## 2. Blocking finding F1 — systematic `published_at` corruption in current-capstone records

The current-capstone observation file and canonical Discovery records contain many `published_at` values set to generic placeholders such as `2026-01` rather than the source's actual publication/release month.

This is not a cosmetic metadata issue. TS-002 is explicitly a technical history, and the current-capstone layer is meant to establish the 2025–2026 endpoint of that history. Incorrect chronology can distort version order, lifecycle interpretation, and Evidence-stage source binding.

Independent source checks by Sol found, at minimum:

- BT-D102 Seedream 5.0 Pro: ByteDance first-party page dated **2026-07-08**, not `2026-01`.
  - https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro
- BT-D103 ChatGPT Images 2.5: OpenAI first-party page dated **2026-09-08**, not `2026-01`.
  - https://openai.com/index/introducing-chatgpt-images-2-5/
- BT-D107 GPT-Live: OpenAI first-party page dated **2026-07-08**, not `2026-01`.
  - https://openai.com/index/introducing-gpt-live/
- BT-D109 Gemini 3.8 Audio: Google DeepMind model card published **2026-09-15**, not `2026-01`.
  - https://deepmind.google/models/model-cards/gemini-3-8-audio/
- BT-D111 Lyria 3.5: Google DeepMind model card published **2026-07-29**, not `2026-01`.
  - https://deepmind.google/models/model-cards/lyria-3-5/
- BT-D117 Seedance 2.5: ByteDance first-party page dated **2026-07-31**, not `2026-01`.
  - https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- BT-D119 FLUX 3: Black Forest Labs first-party page dated **2026-07-23**, not `2026-01`.
  - https://bfl.ai/blog/flux-3
- BT-D113 Stable Audio 3 / SAME is more severe: the Discovery record says `2025-01`, while Stability AI's research index and article place the release on **2026-05-20**.
  - https://stability.ai/research/stable-audio-3

Therefore this is treated as a **systematic metadata defect**, not isolated typo repair.

### Required repair

Re-read every current-capstone source `BT-D100` through `BT-D128` from its first-party locator and bind the actual publication/release date at the best precision supported by the canonical schema. If the schema convention is month precision, normalize `2026-07-31` to `2026-07`; do not invent a day.

Where a dynamic documentation page has no stable publication date, record that explicitly instead of substituting January. Distinguish:

- source publication/release date;
- model/product release date mentioned inside the source;
- page update date;
- Discovery `observed_at` retrieval timestamp.

Do not overwrite one with another.

The repair must propagate consistently through:

1. raw capstone observations;
2. `discovery-v2.jsonl`;
3. regenerated `discovery-accepted-v2.json`;
4. coverage / chronology notes that depend on those dates.

---

## 3. Blocking finding F2 — one bounded mandatory gap-fill pass before Screening

The existing negative-space document is useful and should be retained. Several gaps are acceptable limitations of closed systems, but four lanes are sufficiently central to the Sol pre-research contract that Discovery should make one more bounded attempt before Screening.

### G08 — audio-video synchronization evaluation

The edition treats joint audio-video generation as a major 2026 transition. A mere statement that no widely adopted standalone metric was found is not yet sufficient. Search for:

- AV synchronization / audiovisual alignment metrics used by video-generation papers or technical reports;
- benchmark suites with explicit sound-event timing / semantic alignment dimensions;
- validation studies or documented limitations of those metrics.

If no stronger authority exists, keep G08 unresolved but record the exact search surface and why available metrics are insufficient.

### G09 — current open speech-generation / voice-cloning deployment evidence

The historical speech lineage is good, but the current open/deployable side is thin relative to the open-runtime treatment given to image/video/audio. Search for current open-weight/open-source speech generation or cloning systems with first-party technical reports/repositories and documented runtime/deployment properties.

Do not select projects merely because they are popular; require a technically useful authority surface.

### G10 — streaming speech-to-speech latency methodology

Because realtime/native speech is a current capstone, the edition needs more than incomparable vendor latency adjectives. Search for papers/specifications that define or measure some combination of:

- time to first audio;
- end-of-turn to first audio;
- real-time factor;
- streaming chunk latency;
- interruption / barge-in behavior;
- full-duplex conversational latency.

The goal is methodology/taxonomy, not a cross-vendor leaderboard.

### G11 — video physics / commonsense evaluation validity

The current video storyline explicitly invokes physics, motion, continuity, and long-horizon consistency. Search for independent or research-paper evidence evaluating the validity/reproducibility of physics-oriented video-generation metrics or benchmark dimensions. If evidence remains thin, preserve this as an explicit methodological limitation rather than treating vendor benchmark scores as comparable truth.

### Non-blocking / opportunistic gaps

G03 (independent Suno/ElevenLabs evaluation), G04 (independent FLUX.2-klein runtime), and G12 (flow-vs-diffusion ablations outside image) are worth searching **only if low-cost during the bounded pass**. Failure to fill them does not by itself block the next Sol review if the search is recorded honestly.

Closed architecture gaps G01/G02/G05/G06 are not to be “solved” by speculation.

---

## 4. Retrieval-depth disposition

The first run marks records as `SUMMARY_CAPTURED` and defers full-body semantic consumption to Evidence. For this Discovery gate, that is acceptable **provided that** locator identity, source class, publication chronology, scope role, and negative-space are correct.

Do not turn the bounded repair into a premature Evidence pass. Full claim extraction remains an Evidence-stage responsibility.

However, date repair requires actually reading the first-party source header/metadata rather than guessing from search snippets or model version names.

---

## 5. Source-count / breadth disposition

Do not chase a numerical target simply to exceed TS-001's source count. The 128-record base already has useful structural breadth.

The reason for this REQUEST_CHANGES is quality and completeness of specific mandatory lanes, not “128 is too small.” Add only sources that materially improve chronology, methodology, or one of the bounded gaps above.

At the second Sol review, the important question will be whether the source map can support an eventual deep Architecture without forcing speech, music, or video into compressed appendices.

---

## 6. Required terminal state after repair

The repair run must remain inside Discovery.

Expected state after a successful bounded refresh:

`DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW_R2`

Do not run:

- Screening;
- Evidence;
- Materiality;
- Completeness stage;
- Selection;
- Architecture;
- Drafting;
- Publication;
- Freeze/Release.

X/community remains deferred unless a new Sol instruction explicitly opens that pass.

---

## 7. Acceptance criteria for r2 review

- [ ] All `BT-D100`–`BT-D128` current-capstone source dates are re-read from first-party authority and no generic `2026-01` placeholder remains unless January is actually source-supported.
- [ ] Stable Audio 3 / SAME chronology is corrected from the erroneous `2025-01` value to the source-supported 2026 release date/precision.
- [ ] Raw observations, canonical Discovery JSONL, accepted Discovery artifact, and coverage notes are mutually consistent after date repair.
- [ ] G08, G09, G10, and G11 each receive one bounded gap-fill search with source additions where material authority is found.
- [ ] Unfilled gaps remain explicit negative space with search/disposition notes; no speculation is used to close them.
- [ ] Any added records are provenance-bound and mapped to existing BT-O obligations; do not invent new dimensions merely to accommodate sources.
- [ ] Core Discovery validation passes after regeneration.
- [ ] No shared Core-v2 source/schema/workflow files change.
- [ ] No X/community pass is run.
- [ ] Lifecycle remains `DISCOVERY_COLLECTED`; downstream stages remain pending.
- [ ] Final report provides previous/new record counts, added/modified IDs, date corrections, gap dispositions, final remote HEAD/tree, and validator result.

---

## 8. Sol review conclusion

The first run is a strong research skeleton and should be preserved. The main defect is not conceptual collapse but **chronology/provenance hygiene in the current-capstone layer**, plus a small number of methodologically important negative-space lanes.

Disposition:

`REQUEST_CHANGES -> bounded Discovery repair -> Sol Completeness Review r2`
