# TS-002 Muse execution — Evidence Semantic Depth Repair r2

Status:

`EXECUTION_AUTHORITY / EVIDENCE_ONLY_SEMANTIC_REPAIR / STOP_FOR_SOL_R2_REVIEW`

Date: `2026-09-24 JST`

Issue:

`SP-beyond-text-2026` / GitHub Issue `#526`

Branch:

`special/beyond-text-2026-work`

## 0. Start guard

Use the exact work/main HEAD and tree values supplied in the Sol launch message.

Before any write, read-only verify:

- remote work branch HEAD == supplied Exact Starting SHA
- remote work branch tree == supplied Expected Starting Tree
- remote main HEAD == supplied Reviewed main SHA
- remote main tree == supplied Expected main Tree

If any mismatch occurs:

- perform zero repository/GitHub writes;
- report expected and actual values;
- stop.

Do not create any new branch, fallback branch, repair branch, review branch, or iteration branch.

No force push, reset, rebase, history rewrite, branch recreation, or destructive cleanup.

## 1. Authorities to read

Read in this order:

1. `docs/research-plans/2026-09-24_ts-002-beyond-text-sol-preresearch.md`
2. `sources/SP-beyond-text-2026/execution/sol-discovery-completeness-review-r2.md`
3. `sources/SP-beyond-text-2026/execution/sol-x-reception-r3-review-20260924.md`
4. `docs/prompts/2026-09-24_muse-ts-002-x-import-screening-evidence.md`
5. `sources/SP-beyond-text-2026/execution/sessions/ts002-x-import-screening-evidence-20260924.md`
6. `sources/SP-beyond-text-2026/execution/sol-evidence-semantic-review-r1-20260924.md`
7. current `production-state.json`
8. current accepted Screening result-set
9. current r1 accepted Evidence result-set and Edition Views
10. current Evidence task package / interactive input / compatibility defect record

The Sol Evidence Semantic Review r1 is authoritative for this repair.

## 2. Mission

Repair **Evidence semantic depth only**.

Do not rerun or broaden:

- Discovery
- X collection
- X reconciliation
- normal Screening

Do not enter:

- Materiality
- Completeness
- Selection
- Architecture
- Draft
- Validation
- Publication Preview
- Freeze
- Release

Normal target stop:

`EVIDENCE_REBUILT / AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R2`

## 3. Preserve the current r1 Evidence result-set

The current accepted Evidence result-set is a historical r1 artifact.

Do not delete it.
Do not overwrite its files in place.
Do not rewrite acceptance history.

The repair must generate a **new Evidence result-set** with new content hashes.

Any downstream/current-edition pointer or acceptance surface updated by canonical Core acceptance must point to the fresh result-set after successful validation, while the old result-set remains preserved as prior output.

If the frozen Core does not provide a safe append-only/current-result acceptance path, stop and report the exact incompatibility rather than manually mutating protected acceptance semantics.

## 4. Source-body semantic consumption — mandatory

This repair exists because r1 relied on Discovery summaries + edition Raw notes and reserved source-body reading.

That is not sufficient.

For every retained Evidence authority used for a technical claim, access the **underlying source body or relevant official technical documentation** and consume the sections necessary to support the Evidence Card.

### 4.1 Papers

For `PRIMARY_PAPER` sources, consume at minimum the relevant:

- abstract/introduction for problem framing;
- method/model/objective/representation section;
- experiment/ablation/evaluation section where the source makes capability or efficiency claims;
- limitations/failure/trade-off discussion where available.

Do not claim that reading only an abstract or Discovery summary is full-body verification.

You do not need to reproduce an entire paper in the repository. Record concise source-bound facts with provenance and section/page/figure/table hints when available.

### 4.2 Repositories / model cards / specs / docs

For official repositories, model cards, specifications, and technical documentation, consume the relevant body sections that establish:

- architecture or representation if disclosed;
- objective / training or inference method if disclosed;
- supported capability surface;
- runtime/hardware/configuration details if disclosed;
- limitations / version boundaries / license only when directly supported.

Do not infer undisclosed mechanisms from product behavior.

### 4.3 Announcements / dynamic vendor pages

Use these only within their authority boundary:

- release/lifecycle;
- documented capability surface;
- workflow;
- vendor evaluation claim with attribution.

If technical internals are not disclosed, explicitly mark them undisclosed rather than filling them from adjacent models.

### 4.4 X/community

The one X-bound record `BT-D139` remains reception/deployment/counter-signal only.

Do not convert it into architecture/specification authority.

Any technical lead from X must be rebound to a non-X primary or independent technical source before becoming a technical Evidence claim.

## 5. Verification semantics

Never mark a target `VERIFIED` if the target itself has not been verified.

In particular, for a target named substantially:

`Evidence-stage full-body verification`

- `VERIFIED` requires actual source-body semantic consumption;
- summary + Raw only is not VERIFIED;
- inaccessible/dynamic/blocked sources must remain `PARTIAL` or unresolved, with the exact barrier.

Do not use a finding that says `full-text reserved` together with `status: VERIFIED`.

## 6. Factual Evidence Card responsibility boundary

The current Evidence package rule is authoritative:

`Factual Evidence contains no Weekly why_now, Thematic lineage role, or Candidate Selection recommendation.`

Therefore the repaired source-local Evidence Cards must contain only source-bound factual material such as:

- artifact/source identity;
- publication/release events;
- method / architecture / representation / objective actually disclosed by the source;
- measurements / ablations / benchmark results with exact conditions;
- explicitly stated limitations;
- vendor/author claims with attribution;
- source-access / verification boundary.

Do **not** insert generic edition-level text such as:

`Historical role (BT-Oxx): ...`

into Factual Evidence cards.

Do not insert selection recommendations or unsupported successor judgments.

## 7. Separate TS-002 semantic transition ledger

Historical synthesis belongs in a separate edition-local artifact.

Create:

`sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/transition-ledger.json`

and a readable companion:

`sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/transition-ledger.md`

Each transition entry must include at minimum:

- `transition_id`
- `name`
- `modality_or_crossmodal`
- `predecessor_bottleneck`
- `changed_representation`
- `changed_architecture`
- `changed_objective`
- `changed_sampling_or_inference`
- `conditioning_or_control_change`
- `source_supported_improvement`
- `tradeoff_or_new_failure_mode`
- `successor_inheritance_or_displacement`
- supporting `discovery_ids`
- supporting `evidence_task_ids`
- source locators or source IDs
- `synthesis_type`: `DIRECT_SOURCE_STATEMENT`, `MULTI_SOURCE_SYNTHESIS`, or `OPEN_QUESTION`
- confidence
- unresolved questions

Do not force every field to have a claim. Use `NOT_ESTABLISHED` where the sources do not establish it.

For `MULTI_SOURCE_SYNTHESIS`, cite at least two supporting Evidence tasks unless the relation is genuinely source-local.

## 8. Mandatory deep-transition coverage

The transition ledger must cover, at minimum where present in Screening:

### Representation / compression / tokenization

- continuous latent variable modeling (VAE)
- discrete latent/codebook modeling (VQ-VAE lineage)
- perceptual/adversarial image tokenizers (VQGAN lineage)
- text-conditioned discrete visual tokens (dVAE lineage)
- neural audio codec + RVQ transition (SoundStream -> EnCodec/DAC lineage)
- semantic vs acoustic token hierarchy (AudioLM lineage)
- spatiotemporal/video tokenizer transition (MAGVIT / retained successors)
- modern high-compression video/audio representation sources if retained

### Generative paradigms / objectives / sampling

- GAN transition and its stability/fidelity trade-offs
- raw autoregressive pixels / transformer autoregression
- DDPM diffusion transition
- DDIM / solver/sampling-efficiency transition
- score-SDE continuous-time framing
- EDM design-space engineering
- latent diffusion
- DiT / transformer denoiser architecture transition
- flow matching / rectified flow
- consistency/distillation/few-step acceleration

Keep distinct:

- representation
- architecture
- objective
- sampler / solver / inference procedure

### Conditioning / control / editing

- text conditioning and cross-attention where retained
- classifier-free guidance
- structural conditioning / ControlNet lineage
- reference / identity conditioning
- inpainting/local editing/instruction editing
- preservation vs de-novo generation

### Speech / voice / audio

- waveform autoregression (WaveNet lineage)
- acoustic-model / vocoder decomposition where retained
- end-to-end TTS (Tacotron/VITS lineage as applicable)
- codec-LM speech
- VALL-E / Voicebox-class transitions where retained
- flow-matching TTS / F5-TTS
- full-duplex speech / Moshi
- realtime closed capstones only within disclosed boundary

### Music

- Jukebox lineage
- MusicLM
- MusicGen / AudioCraft
- Stable Audio lineage / retained technical sources
- long-form structure vs local fidelity
- prompt/lyrics/reference/control distinctions

### Video

- early video diffusion
- Imagen Video
- Phenaki
- tokenizer/latent transitions
- current open video lineage such as Wan where retained
- video editing / rectified-flow comparison
- AV synchronization / long-horizon / identity / physics evaluation

### Evaluation

- FID/image metrics
- FAD/audio metrics
- WER/speaker-similarity use context
- human preference/listening protocols
- VBench / VBench 2.0
- lip-sync metrics and critiques
- physics/commonsense evaluation
- automatic metric vs human preference evidence

## 9. Source-specific minimum content for technical anchors

For each technical anchor Evidence Card, include source-supported detail sufficient to answer the following where applicable:

1. What exact technical problem does the source address?
2. What representation / architecture / objective / inference procedure does it introduce or analyze?
3. What source evidence supports the claimed improvement?
4. What source-supported limitation or trade-off exists?
5. What is **not** established by this source?

Do not fake successor/inheritance inside the factual card. Put cross-source relations in the transition ledger.

### 9.1 Measurements

Where a source reports numerical results, bind each metric to:

- exact subject/model/version;
- benchmark/dataset/protocol;
- resolution/duration/bitrate/rate if relevant;
- sampling steps/NFE if relevant;
- hardware/runtime if relevant;
- comparator ownership.

Do not compare numbers with incompatible conditions as a ranking.

## 10. Runtime / deployment depth

Where source-supported, extract and bind:

- sampling steps / NFE;
- latency / RTF / first-package latency;
- VRAM / memory;
- quantization/offload;
- hardware/configuration;
- open/closed execution boundary;
- streaming/chunking behavior.

For X/community runtime signals, preserve them as observations and do not elevate them above their authority class.

## 11. Temporal / long-horizon depth

For speech/music/video, keep separate:

- local fidelity;
- short-range coherence;
- long-range structure;
- identity/object permanence;
- AV synchronization;
- continuation consistency;
- edit preservation.

One good sample is not evidence of long-horizon competence.

## 12. Evaluation-validity depth

For benchmark/evaluation sources, consume methodology and limitation sections.

Record when a metric measures only a proxy.

Examples of distinctions that must remain visible:

- image distribution quality vs prompt compositionality;
- acoustic fidelity vs semantic alignment;
- WER vs speaker identity / prosody;
- video frame quality vs temporal consistency;
- lip-sync metric vs perceptual AV coherence;
- physics classifier/evaluator ceiling;
- automatic metric correlation vs human preference.

## 13. Current closed systems

Closed products may establish only what the source discloses.

Allowed:

- documented capability surface;
- workflow;
- release/lifecycle;
- vendor evaluation claim, attributed;
- disclosed architecture if actually published in a technical source.

Not allowed:

- inferred hidden architecture;
- inferred training recipe;
- inferred tokenizer/latent space;
- architecture copied from an older related model without source support.

## 14. Access failure policy

For every inaccessible source, record:

- Discovery ID / task ID;
- locator;
- attempted access method;
- failure mode;
- whether an authoritative alternate source was available;
- final status `PARTIAL` / `UNRESOLVED`.

Do not silently substitute a lower-authority secondary summary for a missing primary source.

## 15. Evidence package regeneration

Use current Core builders/validators wherever compatible.

Because the frozen Core source-class map defect was already reproduced, the previously created edition-local source-type projection adapter may be reused only if:

- it remains narrowly limited to source-type vocabulary compatibility;
- it does not alter claim text, metrics, limitations, or verification status;
- projection/passthrough counts are reported;
- unknown vocabulary still fails closed;
- shared Core remains untouched.

Do not use compatibility code to manufacture semantic depth.

Generate a fresh Evidence package and Edition Views from the repaired results.

Do not reuse r1 result JSON files as the new semantic output.

## 16. Required audit artifacts

Create under:

`sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/`

at minimum:

- `transition-ledger.json`
- `transition-ledger.md`
- `source-body-access-ledger.json`
- `semantic-delta-audit.md`
- validator/output receipts or references

### `source-body-access-ledger.json`

For each Evidence task, record:

- Discovery ID
- Evidence task ID
- source type
- locator
- access status
- body sections consumed
- source-body vs summary-only flag
- final verification status
- access barrier if any

### `semantic-delta-audit.md`

Explain representative ways the repaired Evidence differs from r1.

At minimum compare:

- VAE
- SoundStream
- AudioLM
- DDPM
- latent diffusion
- at least one conditioning/control anchor
- at least one speech anchor
- at least one music anchor
- at least two video anchors
- at least two evaluation sources
- one current closed-system case
- BT-D139 X-bound evidence

## 17. Validation requirements

Before finalizing, prove:

- every new result file matches one Evidence task;
- every task has exactly one result;
- source IDs and subject binding remain valid;
- no Factual Evidence card contains edition-level lineage/selection prose;
- no `FULL_BODY`/`VERIFIED` statement is backed only by Discovery summary/Raw;
- transition ledger references only existing Discovery/Evidence IDs;
- source-body access ledger covers every Evidence task;
- X remains non-technical authority;
- closed-system non-inference preserved;
- metrics remain condition-bound;
- shared Core unchanged;
- Materiality and later stages remain untouched.

## 18. Session report

Write a new session report under the edition sessions directory.

Report exact:

- starting work HEAD/tree;
- main HEAD/tree;
- r1 Evidence result-set SHA;
- new Evidence result-set SHA;
- Evidence tasks attempted;
- paper bodies accessed;
- official technical docs/model cards/spec bodies accessed;
- dynamic/vendor pages accessed;
- blocked/inaccessible sources;
- VERIFIED count;
- PARTIAL count;
- UNRESOLVED count;
- records whose substantive claims changed after body consumption;
- transition-ledger entry count;
- entries backed by >=2 Evidence tasks;
- remaining LOW_SIGNAL / negative-space lanes;
- compatibility projection/passthrough count if used;
- all validator results;
- final remote HEAD/tree after push;
- confirmation that Materiality and later stages were not entered.

## 19. Stop

Stop at:

`EVIDENCE_REBUILT / AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R2`

Do not proceed to Materiality, Completeness, Selection, Architecture, Draft, Validation, Publication Preview, Freeze, or Release.
