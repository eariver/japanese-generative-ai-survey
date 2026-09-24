# TS-002 — Materiality through fresh Human Architecture Review

Status: `EXECUTION_AUTHORITY / EVIDENCE_REBOUND_ACCEPTED / BOUNDED_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`

Date: 2026-09-25 JST

Repository: `eariver/japanese-generative-ai-survey`
Branch: `special/beyond-text-2026-work`

Exact Starting SHA:
`bab96d1ac0510cf5ac35d5376d2784b3d220b576`

Expected Starting Tree:
`3114924889c5830eff40a29b89e580c73ff0c4da`

Reviewed main SHA:
`0bbb02b3c5963403860897daec2feaf61e82589a`

Expected main Tree:
`e4ddde5ed5059d303b818f54e27204369b256bcb`

## 1. Mission

Continue `SP-beyond-text-2026` from the accepted/rebound Evidence authority through canonical:

`Evidence checkpoint -> Materiality -> Completeness -> Selection -> Architecture`

and stop at a **fresh Human Architecture Review**.

Do not enter Draft, Validation, Publication Preview, Freeze, or Release.

The purpose of this execution is not to make the edition shorter. It is to convert the deep Evidence package into a coherent long-form technical-history architecture without losing the semantic depth already established.

## 2. Mandatory start guard

Before any write, verify read-only:

- remote work branch HEAD == Exact Starting SHA
- remote work branch tree == Expected Starting Tree
- remote main HEAD == Reviewed main SHA
- remote main tree == Expected main Tree

If any check fails: zero writes, report expected vs actual, stop.

No new branch, fallback branch, repair branch, review branch, reset, rebase, force push, or history rewrite.

## 3. Required authority read order

Read and treat as authoritative, in this order:

1. `docs/research-plans/2026-09-24_ts-002-beyond-text-sol-preresearch.md`
2. `sources/SP-beyond-text-2026/execution/sol-discovery-completeness-review-r2.md`
3. `sources/SP-beyond-text-2026/execution/sol-x-reception-r3-review-20260924.md`
4. `sources/SP-beyond-text-2026/execution/sol-evidence-semantic-review-r1-20260924.md`
5. `sources/SP-beyond-text-2026/execution/sol-evidence-semantic-review-r2-20260924.md`
6. `sources/SP-beyond-text-2026/execution/sol-evidence-provenance-readback-r1-20260925.md`
7. `sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/transition-ledger.json`
8. `sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/transition-ledger.md`
9. `sources/SP-beyond-text-2026/execution/provenance-rebind-20260924/provenance-repair-manifest.json`
10. current canonical Discovery / Screening / Evidence / Edition Views
11. `sources/SP-beyond-text-2026/production-state.json`

Use the current rebound Evidence authority, not the old r1/r2 pre-rebind result set, as the active factual basis.

Current accepted factual package expectations:

- Discovery: 139
- Screening: KEEP 134 / MAYBE 3 / INSPECT 2 / DROP 0
- Evidence: 139
- Evidence status: 126 VERIFIED / 8 PARTIAL / 5 NEEDS_MORE
- Edition Views: 139
- transition ledger: 43 entries

## 4. Evidence checkpoint / state advance

The Sol provenance readback authorizes Evidence acceptance for pipeline advance.

Use the current Core canonical stage machinery to establish the Evidence checkpoint and advance state without inventing a Human decision.

Do not rewrite factual Evidence merely to satisfy stage advancement.

If the frozen Core cannot consume the rebound accepted Evidence without an edition-local compatibility adapter, preserve the existing narrowly-scoped compatibility precedent. Do not modify shared Core.

Any Core defect encountered must be recorded edition-locally and worked around only if the workaround is:

- deterministic,
- narrow,
- field-preserving,
- validator-backed,
- and does not change Evidence semantics.

Otherwise stop before write/advance and report the blocker.

## 5. Materiality requirements

Materiality is not a popularity filter and not a current-product ranking.

Assess materiality against TS-002's historical-technical thesis:

`media representation -> generative process/objective -> conditioning/alignment -> control/reference -> editing -> temporal/long-horizon structure -> runtime/deployment -> evaluation validity -> multimodal convergence`

A source/transition is materially important when it substantially explains one or more of:

- a bottleneck that constrained the prior generation,
- a change in representation/tokenization/compression,
- a change in generative objective or training formulation,
- a change in architecture that must remain distinct from objective,
- a change in inference/sampling/runtime feasibility,
- a new conditioning/control/editing mechanism,
- a change in temporal or long-horizon capability/failure mode,
- an evaluation methodology or validity boundary,
- a durable inheritance relationship into later systems,
- a deployment/reproduction constraint that materially changes practical use.

Do not demote foundational sources simply because they are old or numerically weaker than current systems.

Do not promote closed-product announcements above open technical sources merely because they are current.

X remains reception/deployment/counter-signal evidence only.

## 6. Completeness requirements

Completeness must explicitly test whether the edition can answer the following, with source-backed depth rather than name-dropping.

### 6.1 Representation

Across image, speech/audio, music, and video, explain how systems moved among:

- raw pixels/waveforms/frames,
- continuous latents,
- discrete VQ/codebook tokens,
- residual-vector-quantized neural codecs,
- semantic/acoustic token hierarchies,
- spatiotemporal video compression.

Representation is a first-class historical axis, not an introductory aside.

### 6.2 Paradigms and objectives

Keep separate:

- autoregressive modeling,
- adversarial generation,
- diffusion / score modeling,
- flow matching / rectified flow,
- consistency / distillation / few-step generation.

Also keep architecture distinct from objective:

- U-Net vs Transformer / DiT is architecture,
- diffusion vs flow is objective/process,
- solver / DDIM / distillation is inference/sampling.

### 6.3 Conditioning, control, and editing

Distinguish:

- text conditioning,
- classifier / classifier-free guidance,
- reference/image/audio conditioning,
- identity/personalization,
- structural control,
- generation from scratch,
- local editing/inpainting,
- instruction editing,
- preservation/edit-locality failures.

### 6.4 Temporal / long-horizon structure

Do not collapse all video/audio/music quality into sample fidelity.

Separate at least:

- local perceptual fidelity,
- short-range coherence,
- long-range structure,
- identity/object permanence,
- AV/lip synchronization,
- continuation consistency,
- edit consistency,
- multi-round/long-form behavior.

### 6.5 Runtime / deployment

Where evidence supports it, preserve:

- sampling steps / NFE,
- latency / RTF / first-package latency,
- memory / VRAM,
- quantization / offload,
- local/open vs closed deployment,
- hardware/configuration binding.

Never compare unbound runtime numbers as a leaderboard.

### 6.6 Evaluation validity

Preserve the fact that metrics are not interchangeable.

Cover modality-appropriate validity boundaries such as:

- FID / IS,
- FAD / CLAP-based audio metrics,
- WER / speaker similarity / human listening,
- music preference studies,
- VBench / VBench-like video dimensions,
- AV/lip-sync metrics,
- physics/common-sense evaluation,
- human preference vs automatic metrics.

### 6.7 Current capstones and closed systems

Current 2025-2026 systems are capability/workflow/lifecycle cases unless first-party technical authority discloses mechanism.

Do not infer undisclosed architecture from behavior.

Do not let current vendor systems crowd out the historical mechanisms that made them possible.

### 6.8 Residual unresolved evidence

Carry the 13 non-VERIFIED records and LOW_SIGNAL lanes explicitly through Completeness.

Do not turn PARTIAL/NEEDS_MORE into narrative certainty.

Completeness may conclude that an unresolved item is non-blocking if the historical claim is supported elsewhere, but must state why.

## 7. Anti-thinness Selection contract

Selection must optimize for explanatory coverage, not minimum record count.

The 43-entry semantic transition ledger is a principal architecture input. It must not be reduced to a small handful of headline systems.

For every major transition retained in the final architecture, preserve where source support exists:

`prior bottleneck -> changed representation/mechanism/objective -> improvement -> trade-off/new failure -> successor/inheritance`

Selection should preserve enough source authority that the future draft can explain mechanisms and trade-offs without returning to Discovery summaries.

### Mandatory historical anchor families

Unless Completeness produces a documented source-backed reason otherwise, architecture must retain substantive coverage of:

- VAE -> VQ-VAE / VQGAN / latent compression
- GAN -> StyleGAN lineage
- PixelRNN/PixelCNN / Image Transformer autoregressive lineage
- DDPM -> DDIM -> score-SDE / EDM design-space boundary
- latent diffusion
- DiT / scalable transformer denoisers
- flow matching / rectified flow
- classifier-free guidance
- ControlNet / reference / personalization / adapter control
- image generation -> editing transition
- WaveNet / Tacotron / neural-vocoder lineage
- SoundStream / EnCodec / DAC codec lineage
- AudioLM / VALL-E / Voicebox / modern streaming/realtime speech
- Jukebox -> MusicLM -> MusicGen / latent-diffusion music/audio
- Video Diffusion Models -> cascaded/latent/open video -> current video capstones
- temporal consistency / long-horizon / AV sync / physics evaluation
- runtime/sampling-efficiency transition
- evaluation-validity transition
- multimodal convergence as an evidence-bounded open question.

## 8. Modality balance guard

Image is historically important but must not dominate the edition to the point that speech/audio/music/video become appendices.

Architecture must allocate first-class treatment to:

- image,
- speech/voice,
- music/general audio,
- video,
- cross-modal/evaluation/runtime synthesis.

Do not enforce artificial equal page counts, but require each non-image modality to contain its own representation, mechanism, control/temporal, runtime/evaluation story rather than a product list.

## 9. Architecture design requirements

Build a coherent chapter architecture for a long-form technical history.

The architecture should be mechanism-led, not vendor-led and not simply chronological.

A viable high-level shape may combine chronology inside semantic chapters, for example:

1. Why continuous media generation is hard: representation and compression
2. Competing generative paradigms: AR, GAN, diffusion/score, flow
3. Conditioning and controllability
4. Generation becomes editing and preservation
5. Image lineage
6. Speech and voice lineage
7. Music and general audio lineage
8. Video and temporal generation lineage
9. Long-horizon consistency, synchronization, and editing
10. Runtime and deployment economics
11. How to evaluate generated media
12. 2025-2026 capstones and multimodal convergence
13. What remains unresolved

This is guidance, not a mandatory chapter list. Use the Evidence/Materiality/Completeness results to derive the strongest architecture.

### Page guidance

Maintain the planning expectation of approximately 64-96 pages for the eventual PDF.

This is not a hard cap.

If adequate technical treatment requires more pages, prefer justified depth over artificial compression.

Do not target a shorter edition merely because the pipeline can fit it.

Architecture Review should include a plausible page-budget allocation by chapter/section so Human can judge whether any lane is being underweighted before Draft.

## 10. Architecture Review package must expose

The fresh Human Architecture Review must make it possible to review editorial structure before prose drafting.

At minimum expose:

- proposed title/subtitle if changed,
- central thesis / reader promise,
- chapter and section outline,
- page-budget estimate by chapter,
- mapping from chapters/sections to transition-ledger entries / major Evidence families,
- representation coverage map,
- modality coverage map,
- architecture-vs-objective separation check,
- generation-vs-editing separation check,
- temporal/long-horizon coverage check,
- runtime/deployment coverage check,
- evaluation-validity coverage check,
- closed-system boundary check,
- TS-002 / TS-003 boundary check,
- unresolved/PARTIAL/NEEDS_MORE handling plan,
- LOW_SIGNAL handling plan,
- explicit anti-thinness check,
- expected bibliography/evidence density,
- any intentional omissions and reasons.

Architecture Review must not contain a fabricated Human approval decision.

## 11. Canonical pipeline discipline

Use current Core canonical builders/validators and append-only acceptors where applicable.

Do not hand-edit accepted artifacts to bypass validators.

Preserve prior accepted authorities and snapshots.

Shared Core remains frozen: no changes under shared Core paths.

If current Core has a known vocabulary/compat defect already documented for this edition, reuse only the minimal existing edition-local adapter. Do not broaden it.

## 12. Validation and session report

Record a detailed session report including:

- start guards and actual values,
- active Discovery/Screening/Evidence hashes,
- Materiality counts and major dispositions,
- Completeness decision and residual gaps,
- Selection counts and rationale,
- evidence retention by modality / semantic lane,
- transition-ledger retention/mapping,
- Architecture output paths/hashes,
- page-budget summary,
- anti-thinness checks,
- PARTIAL/NEEDS_MORE handling,
- validators and receipts,
- final lifecycle / checkpoint state,
- final HEAD/tree,
- confirmation that Draft and later stages were not entered.

## 13. Normal stop

Normal terminal state for this execution:

`ARCHITECTURE_REVIEW / AWAITING_HUMAN_ARCHITECTURE_DECISION`

or the exact current-Core equivalent representing a fresh unresolved Human Architecture Review.

Stop immediately there.

If an Exception Gate is required earlier, stop at that gate with no fabricated resolution.
