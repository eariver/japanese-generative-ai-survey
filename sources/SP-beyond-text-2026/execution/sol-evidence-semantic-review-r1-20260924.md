# TS-002 Sol Evidence Semantic Review r1

Status:

`SOL_EVIDENCE_SEMANTIC_REVIEW_R1 / REQUEST_CHANGES / EVIDENCE_DEPTH_REPAIR_REQUIRED`

Date: `2026-09-24 JST`

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`

Reviewed branch state:

- work HEAD: `f26a4d5dedfafba482b406df90aa4a7683814328`
- work tree: `3c232473137b6c65dcfc9b68d550389d594358fb`
- main HEAD: `0bbb02b3c5963403860897daec2feaf61e82589a`
- main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`

## Decision

**REQUEST_CHANGES.**

The X import and Screening work are accepted for continuation, but the current Evidence package is **not accepted as semantically sufficient Evidence for TS-002**.

The blocking defect is not topic coverage. The blocking defect is that the accepted Evidence cards were generated primarily from canonical Discovery summaries plus edition Raw observation notes, while the execution authority explicitly required real Evidence-stage semantic consumption of the underlying source bodies.

No Materiality, Completeness, Selection, Architecture, Draft, or later stage is authorized from the current Evidence package.

## What passed

### 1. Start guards and branch discipline

The Muse execution correctly verified the supplied work/main HEAD and tree guards before writes. No new/fallback/repair/review branch was created. No force push, reset, rebase, or history rewrite was used.

### 2. X reception import

The accepted X reception pass was correctly imported as one X-bound Discovery record `BT-D139`, rather than 27 technical Discovery records.

The Sol-audited 27-observation ledger and the downstream normalization of `OBS-SPEECH-01 FIRST_HAND YES -> NO` were preserved. The Raw r3 artifact remained immutable.

### 3. Discovery and Screening

Canonical Discovery increased from 138 to 139 records and was rebuilt/validated.

Screening produced 139 explicit decisions:

- KEEP: 134
- MAYBE: 3
- INSPECT: 2
- DROP: 0

The Screening result appropriately retained historical anchors, representation-first sources, current capability cases, LOW_SIGNAL lanes, and the TS-002 / TS-003 boundary.

### 4. Shared-Core source-type defect handling

The execution correctly identified that the frozen shared Core source-class map does not cover several TS-002 source types and did not modify shared Core.

The edition-local compatibility adapter is acceptable as a bounded compatibility measure for this edition, subject to later clean-Core regeneration if/when the shared map is repaired.

### 5. Stop discipline

The execution did not enter Materiality, Completeness, Selection, Architecture, Draft, Publication Preview, Freeze, or Release.

This was correct.

---

# Blocking findings

## E1 — Evidence-stage source-body semantic consumption was not performed

The execution authority required:

> For sources promoted into Evidence, perform real semantic consumption rather than relying only on Discovery summaries.

The generated operator script states explicitly that it consumes:

- canonical Discovery summaries;
- edition Raw observation files;
- X Raw;

and that **full-text bodies are reserved**.

The generated Evidence Cards repeat this boundary. Representative cards for VAE (`BT-D001`), SoundStream (`BT-D006`), AudioLM (`BT-D009`), DDPM (`BT-D019`), and LDM (`BT-D023`) all contain a limitation substantially equivalent to:

`Summary-plus-Raw consumption ... full-text body verification reserved.`

Therefore the central requirement of the execution unit was not met.

### Required correction

Evidence repair must read the underlying source body or relevant official technical documentation for every retained Evidence authority that is used for technical claims.

For papers, this means consuming the relevant method / experiment / limitation sections from the paper body, not only title/abstract/Discovery summary.

For official technical docs/model cards/repos/specifications, this means consuming the relevant body sections that directly support the recorded claims.

If source-body access is genuinely unavailable, the result must remain `PARTIAL` or `UNRESOLVED`, with the exact access barrier stated. It must not be represented as full-body verified.

## E2 — Verification status is semantically contradictory

Many Evidence tasks have verification target:

`Evidence-stage full-body verification`

with status:

`VERIFIED`

while the finding itself says verification was performed only against Discovery summary and edition Raw observation material and that full-text body is reserved.

This is internally contradictory.

### Required correction

`VERIFIED` may be used for a verification target only when the evidence actually satisfies that target.

Where only summary/Raw material is available:

- use `PARTIAL` / unresolved semantics supported by the current schema;
- state what was and was not verified;
- never label a reserved full-body check as VERIFIED.

## E3 — Source-specific historical-transition depth is mostly boilerplate

The Evidence generation script constructs the first claim directly from `summary_text` and programmatically adds generic historical-role text from the obligation mapping.

As a result, many cards do not actually answer the required source-specific transition questions:

1. What bottleneck existed before this transition?
2. What mechanism/objective/representation changed?
3. Why did that change improve capability, stability, control, speed, or scale?
4. What trade-off or new failure mode appeared?
5. Which later system inherited, modified, or displaced the idea?

Representative examples:

- VAE card restates amortized VI/reparameterization and a generic representation thread, but does not source-consume the transition in sufficient technical depth.
- SoundStream card restates RVQ lineage but does not source-consume codec structure/rate-quality/streaming trade-offs in sufficient detail.
- AudioLM card restates semantic-plus-acoustic tokenization but does not source-consume the hierarchy and structural/fidelity decomposition in sufficient detail.
- DDPM card restates forward/reverse diffusion and generic runtime language but does not source-consume the objective/sampling/quality-cost transition in sufficient detail.
- LDM card restates latent diffusion but does not source-consume the compression-vs-fidelity-vs-compute transition in sufficient detail.

These are representative, not exhaustive.

### Required correction

Source-local Evidence cards must contain concrete source-supported mechanism, measurements/ablations where relevant, and source-supported limitations.

Cross-source inheritance/displacement conclusions must be built separately as synthesis, with explicit links to the source-local Evidence cards that support them.

## E4 — Factual Evidence and thematic lineage synthesis are incorrectly mixed

The accepted Evidence package declares the rule:

`Factual Evidence contains no ... Thematic lineage role ...`

However the generator inserts a claim of the form:

`Historical role (BT-Oxx): ...`

into source-local Factual Evidence cards.

This violates the package's own responsibility boundary.

### Required correction

Separate two layers:

### Layer A — source-local factual Evidence cards

Contain only source-bound facts, measurements, methods, limitations, events, and explicitly attributable author/vendor claims.

Do **not** place edition-level lineage judgments, selection recommendations, or cross-source historical conclusions into these cards.

### Layer B — TS-002 semantic transition ledger

Create an edition-local synthesis artifact that may reason across multiple accepted Evidence cards.

For each major transition, record:

- transition ID/name;
- predecessor bottleneck;
- changed representation / objective / architecture / sampling mechanism;
- source-supported improvement;
- trade-off / failure mode;
- successor / inheritance / displacement relation;
- supporting Evidence task IDs / Discovery IDs;
- confidence and unresolved questions;
- whether the relation is direct source statement or Sol/Muse synthesis.

This is the proper place for thematic historical synthesis.

## E5 — The current Evidence package is structurally complete but semantically shallow

`evidence-accepted.json` contains 139 accepted results, all marked `PARTIAL`.

The count completeness is useful, but the package is not sufficient merely because there is one JSON result per Screening decision.

For TS-002, semantic depth takes precedence over mechanical one-result-per-task completion.

Do not proceed merely because validators accept the current package shape.

---

# Required depth by technical lane

The repair must preserve the common coordinate system:

`media representation -> generative process -> conditioning/alignment -> control/reference -> editing -> temporal/long-horizon structure -> runtime/deployment -> evaluation -> multimodal convergence`

The following anchors are mandatory deep-consumption groups. This list is a minimum, not an excuse to leave other retained Evidence tasks summary-only.

## Representation / tokenization

Consume source-body semantics for at least:

- VAE
- VQ-VAE / VQ-VAE-2 / VQGAN
- dVAE
- SoundStream
- EnCodec
- DAC
- AudioLM token hierarchy
- MAGVIT / video tokenizer lineage
- current high-compression video/audio representation sources where retained

## Paradigms / objectives / samplers

Consume source-body semantics for at least:

- GAN / DCGAN / StyleGAN lineage
- PixelRNN / Image Transformer autoregression
- DDPM
- DDIM
- score-SDE
- EDM
- latent diffusion
- DiT
- flow matching / rectified flow
- consistency / distillation / few-step acceleration sources

Keep architecture, objective, and sampling procedure distinct.

## Conditioning / control / editing

Consume source-body semantics for the retained anchors covering:

- classifier-free guidance
- text conditioning / cross-attention
- ControlNet / structural control
- reference/identity conditioning
- inpainting / instruction editing / preservation
- current editing systems where technical disclosure exists

## Speech / voice / audio

Consume source-body semantics for:

- WaveNet / Tacotron / VITS lineage where retained
- codec-LM speech systems
- VALL-E / Voicebox-class transitions where retained
- F5-TTS / flow-matching TTS
- Moshi / full-duplex speech
- current realtime/audio capstones only to the level their sources disclose

Distinguish waveform generation, acoustic model, codec representation, LM/flow objective, streaming architecture, and inference latency.

## Music

Consume source-body semantics for:

- Jukebox
- MusicLM
- MusicGen / AudioCraft
- Stable Audio lineage / current technical sources
- evaluation/human-preference studies

Long-form structure, lyrics intelligibility/alignment, motif recurrence, controllability, and local fidelity must remain distinct dimensions.

## Video

Consume source-body semantics for:

- Video Diffusion Models
- Imagen Video
- Phenaki
- latent/video tokenizer transitions
- modern open video sources such as Wan lineage where retained
- editing / rectified-flow comparisons
- current closed capstones only within disclosed capability/evaluation boundaries

Separate short-range motion fidelity from identity/object permanence, long-horizon structure, AV synchronization, continuation, and editing preservation.

## Evaluation validity

Consume methodology/limitations for retained evaluation anchors such as:

- FID/image evaluation
- FAD/audio evaluation
- WER/speaker-similarity contexts
- human listening/preference protocols
- VBench/VBench 2.0
- lip-sync metrics and critiques
- physics/commonsense video evaluation
- preference-vs-automatic-metric studies

Do not turn heterogeneous scores into a leaderboard.

---

# Repair constraints

1. Do not rerun Discovery.
2. Do not rerun X collection.
3. Do not change accepted X Raw bytes.
4. Do not redo Screening unless a source becomes unusable/inaccessible and the current Core contract requires a bounded disposition update.
5. Do not modify shared Core.
6. Preserve the current accepted Evidence result-set as historical r1 output; do not rewrite history or delete it.
7. Generate a fresh Evidence result-set for the repaired cards.
8. Use append-only/current-Core acceptance semantics where supported.
9. Any edition-local compatibility adapter must remain narrowly source-type projection only; do not use it to change claim semantics.
10. Do not enter Materiality, Completeness, Selection, Architecture, Draft, or later stages.

# Required repair artifacts

At minimum produce:

1. fresh repaired Evidence task/results package;
2. fresh accepted Evidence result-set with a new result-set SHA;
3. `sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/transition-ledger.json` or equivalent structured artifact;
4. a readable Markdown companion explaining the major historical transitions and residual gaps;
5. session report with source-body access statistics and unresolved access barriers;
6. validator receipts;
7. explicit proof that no current `FULL_BODY`/`VERIFIED` claim is based only on Discovery summary/Raw material.

# Quantitative audit required in the repair session report

Report exact counts for:

- Evidence tasks attempted;
- source-body successfully accessed;
- official technical body accessed;
- paper body accessed;
- dynamic/blocked/inaccessible sources;
- VERIFIED results;
- PARTIAL results;
- UNRESOLVED results;
- results whose claims materially changed from Discovery summary after body consumption;
- transition-ledger entries;
- transitions with at least two supporting sources;
- remaining LOW_SIGNAL / negative-space lanes.

# Stop condition

After the repaired Evidence package and semantic transition ledger are built and validated, stop at:

`EVIDENCE_REBUILT / AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R2`

Do not perform Materiality, Completeness, Selection, Architecture, Draft, Publication Preview, Freeze, or Release.
