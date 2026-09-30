# TS-003 Muse execution — Selection through Architecture Review stop

Status:

`EXECUTION_AUTHORITY / SOL_MATERIALITY_COMPLETENESS_PASS / SELECTION_THROUGH_ARCHITECTURE_ONLY / STOP_FOR_HUMAN_ARCHITECTURE_REVIEW`

Date: `2026-10-01 JST`

Issue:

`SP-vision-multimodal-2026`

Branch:

`special/vision-multimodal-2026-work`

## 0. Guard authority

Do not hardcode the work-branch SHA/tree in this file.

The exact work-branch HEAD/tree supplied in the Sol launch message are the sole work-branch start guard.

Before any write, read-only verify:

- remote work branch HEAD/tree against the launch message;
- remote main HEAD/tree;
- remote `production/survey-core-v2` HEAD/tree;
- issue = `SP-vision-multimodal-2026`;
- lifecycle = `EVIDENCE_REVIEWED`;
- discovery = passed;
- screening = passed;
- evidence = passed;
- materiality = passed;
- completeness = passed;
- selection = pending;
- architecture = pending;
- Human Architecture Review = pending;
- Publication Preview = pending.

If any guard differs, perform zero writes and report expected vs actual.

No new/fallback/repair/review/iteration branch. No reset, rebase, force push, history rewrite, branch recreation or cherry-pick.

## 1. Mandatory authority chain

Read in this order:

1. `sources/SP-vision-multimodal-2026/execution/sol-materiality-completeness-review-r1.md`
2. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r5.md`
3. `sources/SP-vision-multimodal-2026/materiality-ledger-v2.json`
4. `sources/SP-vision-multimodal-2026/profile-completeness-v2.json`
5. Round E scope closure / production contract material already present for TS-003.
6. current `production-profile.json`
7. current `production-state.json`
8. exact r5 Evidence / Edition Views through current checkpoint provenance.
9. current Core v2 CLI/help/schema/stage-validation surfaces.
10. `docs/core-v2-deferred-maintenance-summary.md`, especially CV2-DM-006, CV2-DM-013 and CV2-DM-020.
11. TS-001 Efficient Intelligence final source as cross-reference authority.
12. TS-002 Beyond Text final source as cross-reference authority.

Sol Materiality/Completeness Review r1 is the supervisory authority for this execution.

## 2. Mission and allowed stage range

Perform only:

`EVIDENCE_REVIEWED`
-> build canonical Candidate Matrix / Candidate Selection
-> deterministic Selection validation/checkpoint
-> `SELECTION_COMPLETE`
-> build canonical Architecture + Architecture Review surfaces
-> deterministic Architecture validation/checkpoint
-> `ARCHITECTURE_ESTABLISHED`
-> prepare fresh Human Architecture Review dossier/surface
-> **STOP**

Do not enter Draft.
Do not create or infer a Human Architecture Review decision.
Do not build PDF.
Do not run Publication Preview / Freeze / Release.

New research is not authorized in the normal path. If a genuine architecture-blocking evidence gap is discovered, record it and stop fail-closed for Sol review rather than silently researching around the gap.

## 3. Selection contract

Build Selection through current canonical Core tooling.

Do not optimize for a target number of PRIMARY, SUPPORTING, HOLD or other dispositions.

The purpose of Selection is to create a source/claim architecture that is deep enough for a long-form thematic history while avoiding redundant retelling.

### 3.1 Required technical arcs

Selection must preserve sufficient load-bearing authority for all accepted arcs:

1. learned visual representation and transfer;
2. detection / structured localization;
3. dense perception;
4. bounded spatial / geometry substrate;
5. OCR -> document intelligence;
6. Transformer / self-supervised visual foundations;
7. image-level vision-language alignment;
8. open-vocabulary perception and grounding;
9. pretrained vision-language bridges;
10. native multimodal fusion / tokenization / context economics;
11. multimodal reasoning and failure decomposition;
12. video understanding / temporal memory / streaming;
13. Computer Use / actionable visual grounding;
14. VLA / embodied action interfaces;
15. predictive / world-model families;
16. evaluation / robustness / convergence.

Do not compress these into a single famous-model ladder.

### 3.2 Materiality and CONTEXT

Materiality Ledger is the canonical basis:

- 101 MATERIAL
- 10 CONTEXT

Do not automatically SELECT every MATERIAL record as PRIMARY.

The ten CONTEXT records should remain short-treatment/background unless a canonical selection rule requires another schema-valid role. Do not promote them simply to increase lineage density.

### 3.3 Source-role discipline

Paper, repository, model card, vendor page and independent evaluation records that describe the same system are not independent technical transitions.

Use multiple authorities where different source roles are necessary, but keep one lineage/system node unless the evidence demonstrates a distinct technical transition.

Vendor/model-report performance remains attributed vendor evidence unless independently reproduced.

### 3.4 D04 hard cap

Keep the D04 support substrate bounded to the accepted four-node set:

- MiDaS
- OpenPose
- Visual Genome
- DUSt3R

Do not expand into NeRF, 3DGS, SLAM, MVS, general 3D detection or a standalone geometry survey.

### 3.5 D07A / D07B separation

Do not collapse image-level language alignment into grounding.

Selection must preserve distinct authorities/contracts for:

- image-text semantic alignment / retrieval / zero-shot classification;
- phrase/region/box/mask/coordinate grounding and open-vocabulary perception.

### 3.6 D12-D14 endpoint bounds

Computer Use, VLA and World Models are modern convergence endpoints, not the main historical spine.

Keep enough depth to explain the representation/interface transition, but do not let current endpoint source volume displace perception, grounding, multimodal fusion, reasoning and temporal-state history.

### 3.7 G01-G06

Carry all six gaps forward.

Selection may choose sources that bound or explain them, but must not mark them resolved without already-bound authority.

## 4. Architecture thesis

Architecture must be problem- and mechanism-led.

The edition must not read as:

`CNN -> YOLO -> ViT -> CLIP -> VLM -> VLA -> World Model`

Use the accepted conceptual coordinate system:

`Representation -> Recognition -> Localization / Structure -> Language Alignment -> Grounding -> Multimodal Fusion -> Temporal / Spatial State -> Reasoning -> Action and/or Prediction`

These are interacting technical problem layers, not eras.

Central question:

> AIは、画像や映像を単に分類する段階から、対象の位置・構造・時間関係を認識し、言語概念へ接地し、複数modalを統合して推論し、予測や行動へ利用できる内部表現を形成する段階へ、どのように発展してきたのか。

Cross-cutting question:

> What representation of the world is sufficient for the next computation?

Architecture must explicitly show inheritance, branching, convergence and abandoned/specialist paths rather than retrospective inevitability.

## 5. TS-001 / TS-002 integration

### 5.1 TS-001 Efficient Intelligence

Use TS-001 as cross-reference/extension for multimodal-specific compute effects only, including where supported:

- visual-token growth;
- high/dynamic resolution;
- multi-image context;
- long-video context;
- visual resampling/compression/pruning;
- KV/memory pressure;
- streaming state;
- edge/on-device VLM/VLA;
- perception-action loop latency.

Do not retell generic quantization, MoE, serving, speculative decoding or general LLM-efficiency history.

### 5.2 TS-002 Beyond Text

Use TS-002 as cross-reference where generation is load-bearing for multimodal understanding, prediction or action.

Do not retell generic image/audio/music/video generation history.

World-model architecture must distinguish at least:

- media/video generation;
- latent dynamics;
- predictive representation;
- simulator-like / interactive generative environment;
- action-conditioned model used for planning/control.

Do not infer direct ancestry among Ha/Schmidhuber, Dreamer, JEPA/V-JEPA and Genie families where Evidence does not support it.

## 6. Required cross-cutting synthesis

Architecture must make X01-X04 visible across packages rather than burying them in a final appendix:

- X01 data / supervision / post-training;
- X02 objective / interface contract;
- X03 efficiency / token / memory / latency economics;
- X04 reliability / source fidelity / claim strength.

A final convergence/evaluation section may synthesize them, but earlier packages should expose them where technically load-bearing.

## 7. Evaluation discipline

Preserve benchmark/task identity.

Do not create cross-task or cross-protocol rankings.

Where metrics appear, retain sufficient context for:

- dataset / benchmark version;
- input/resolution policy where material;
- tool/CoT allowance;
- judge/extraction method;
- model/version identity;
- source role;
- vendor vs independent status;
- contamination risk when known.

G03-G05 remain binding limits on stronger comparison/deployment claims.

## 8. Current systems / capstones

Current 2025-2026 systems may appear as capstones only when they close a technical lineage or expose a new design trade-off.

Do not build a current-model catalogue or leaderboard.

Current-system architecture should prefer technically distinct cases over many similar families.

Paper/repo/model-card/vendor/eval surfaces for one system may support one capstone from different authority roles; do not count them as multiple independent capstones.

## 9. Depth and page budget

User preference is depth over artificial brevity.

Do not force symmetry with TS-001/TS-002 or a fixed page count.

A long-form architecture in roughly the 80-120 page range, or somewhat more if evidence density justifies it, is acceptable. The important condition is semantic coverage and non-duplication, not page minimization.

Do not compress detection, document intelligence, grounding, video, spatial state, VLA or world models into token paragraphs merely to meet an arbitrary target.

Conversely, do not expand every source into equal-depth treatment.

## 10. Human Architecture Review surface

Produce the canonical architecture artifacts required by current Core, including Candidate Matrix / Selection and Architecture Review Summary / Attention surfaces as applicable.

Also produce an additive Human-facing Architecture Review dossier in Markdown if useful for review clarity.

The review surface must expose at minimum:

- proposed title / subtitle if changed;
- architecture status and lifecycle;
- part/package ordering;
- package-level purpose;
- technical transition / mechanism thesis per package;
- key PRIMARY and SUPPORTING source roles per package;
- obligation coverage by package;
- estimated page budget / relative weight;
- D04 cap read-back;
- D07A / D07B separation read-back;
- document intelligence treatment;
- native multimodal / token-economics treatment;
- offline video vs online/streaming treatment;
- D12-D14 endpoint weight;
- TS-001 cross-reference plan;
- TS-002 cross-reference plan;
- X01-X04 placement;
- G01-G06 limitations and the claims they constrain;
- current-capstone placement and authority-role limits;
- explicit negative space / omitted expansions;
- risks that Human should inspect before approving Draft.

Do not write an approval/rejection conclusion on behalf of Human.

## 11. Canonical validation and state advance

Use current canonical Core APIs/CLI/stage-validation machinery.

Do not hand-edit `production-state.json`.

Expected normal transitions under the current frozen Core are:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED`

Selection stage should validate canonical Candidate Matrix + Candidate Selection artifacts.

Architecture stage should validate canonical Architecture + Architecture Review Summary + Architecture Review Attention artifacts.

Expected normal final state:

- lifecycle = `ARCHITECTURE_ESTABLISHED`
- selection = passed
- architecture = passed
- Human Architecture Review = pending
- draft = pending
- Publication Preview = pending

If current canonical tooling behaves differently, follow current Core and report the exact behavior. Do not fabricate a state transition.

## 12. Prohibited

Do not:

- modify Discovery;
- modify Screening;
- modify accepted r1-r5 Evidence/Views;
- rewrite Materiality Ledger or Profile Completeness merely to make Selection easier;
- perform unrequested broad new research;
- infer Human approval;
- enter Draft;
- generate reader-facing final chapters;
- build PDF;
- run Publication Preview / Freeze / Release;
- modify main;
- modify `production/survey-core-v2`.

Normal commit + non-force push only.

## 13. Final report

Report at minimum:

- startup guards;
- exact Materiality / Completeness authority read-back;
- Candidate Matrix path/hash and candidate count;
- Candidate Selection path/hash and disposition counts;
- PRIMARY/SUPPORTING/HOLD rationale summary;
- VM-O01-VM-O16 Selection coverage;
- X01-X04 Selection coverage;
- G01-G06 carry-forward status;
- Selection validator result and checkpoint;
- Architecture path/hash;
- Architecture Review Summary/Attention paths/hashes;
- package/part count and page-budget summary;
- D04 cap read-back;
- D07A/D07B separation read-back;
- D12-D14 endpoint weight/read-back;
- TS-001/TS-002 cross-reference plan;
- Human-facing review dossier path;
- Architecture validator result and checkpoint;
- final lifecycle/checkpoints;
- final remote HEAD/tree;
- main unchanged;
- Core unchanged;
- Draft not entered;
- Human decision not created.

Normal completion:

`TS-003 SELECTION_ARCHITECTURE_COMPLETE`

`ARCHITECTURE_ESTABLISHED`

`AWAITING_HUMAN_ARCHITECTURE_REVIEW`

`NO_DRAFT`

`NO_HUMAN_DECISION`

Stop there.
