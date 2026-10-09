# TS-003 Muse execution — Evidence checkpoint + Materiality + Completeness

Status:

`EXECUTION_AUTHORITY / SOL_EVIDENCE_R5_PASS / EVIDENCE_MATERIALITY_COMPLETENESS_ONLY / STOP_FOR_SOL_REVIEW`

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
- lifecycle = `CANDIDATES_NORMALIZED`;
- discovery checkpoint = `passed`;
- screening checkpoint = `passed`;
- evidence checkpoint = `pending`;
- materiality checkpoint = `pending`;
- completeness checkpoint = `pending`;
- selection / architecture = `pending`;
- Human Architecture Review and Publication Preview = `pending`.

If any guard differs, perform zero writes and report expected vs actual.

No new/fallback/repair/review/iteration branch. No reset, rebase, force push, history rewrite, branch recreation or cherry-pick.

## 1. Mandatory authority chain

Read in this order:

1. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r5.md`
2. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r4.md`
3. `sources/SP-vision-multimodal-2026/execution/evidence-coverage-r5-20260930.md`
4. Round E scope closure and production contract material already present in the edition.
5. current `production-profile.json`
6. current `production-state.json`
7. current Core v2 CLI/help/schema/stage-validation surfaces.
8. `docs/core-v2-deferred-maintenance-summary.md`, especially CV2-DM-006, CV2-DM-013 and CV2-DM-020.

Sol r5 PASS is authoritative over earlier Evidence acceptances and Worker reports.

## 2. Exact downstream Evidence authority

Use only this accepted Evidence set:

`4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34`

Path:

`sources/SP-vision-multimodal-2026/evidence/v2/accepted/4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34/evidence-accepted.json`

Use only this Edition Views set:

`e3d0b3b33588b235e1c9be41259fb5bb5e07cbd1105ac0ff31a7bf7b34bfd0c5`

Path:

`sources/SP-vision-multimodal-2026/evidence/v2/views/accepted/e3d0b3b33588b235e1c9be41259fb5bb5e07cbd1105ac0ff31a7bf7b34bfd0c5/edition-views-accepted.json`

Validate both exact acceptances before use.

Do not resolve an earlier r1/r2/r3/r4 acceptance as active merely because of directory ordering or timestamp.

The r5 authority contains 111 Cards with expected statuses:

- VERIFIED 106
- PARTIAL 5

Any mismatch must fail closed.

## 3. Mission and allowed stage range

Perform only:

`CANDIDATES_NORMALIZED`
→ exact r5 Evidence/View binding
→ Materiality Ledger construction
→ Profile Completeness construction
→ deterministic Evidence/Materiality/Completeness stage validation
→ canonical checkpoint/state advance
→ `EVIDENCE_REVIEWED`
→ **STOP**

TS-002 precedent under the same current Core shows Evidence, Materiality and Completeness sharing the `CANDIDATES_NORMALIZED` checkpoint and advancing together to `EVIDENCE_REVIEWED` after validation.

Do not run Selection.
Do not run Architecture.
Do not create or infer a Human Architecture Review decision.

## 4. Materiality construction

Build `materiality-ledger-v2.json` through current canonical Core tooling from the exact r5 Evidence/View authority.

Do not hand-edit the ledger to obtain desired counts.

Materiality must express editorial load-bearing value for **TS-003 specifically**, not general fame or current benchmark strength.

Preserve these scope constraints:

### 4.1 D04 support cap

Spatial/geometry records exist to make later spatial reasoning/action intelligible. They must not expand TS-003 into a general 3D reconstruction, SLAM or graphics history.

### 4.2 D07A / D07B separation

Image-level language alignment and localization/grounding are distinct contracts. Do not collapse their materiality rationale into one CLIP-to-VLM line.

### 4.3 Current-system role separation

Paper, repository, model-card, vendor capability and independent evaluation records may refer to the same system but have different source roles. Do not double-count a model as multiple independent technical transitions merely because multiple authorities exist.

### 4.4 TS-001 / TS-002 overlap

Generic attention, quantization, serving, generation, diffusion/video-generation and audio-generation history must not become MATERIAL in TS-003 merely because it appears in a multimodal source.

Where appropriate, retain as CONTEXT/cross-reference rather than retell.

### 4.5 D12–D14 bounded endpoints

Computer Use, VLA and World Models remain convergence endpoints. Their combined editorial weight must not dominate the earlier perception/grounding/multimodal-state lineages simply because they are recent.

### 4.6 Evaluation authorities

Benchmark records are MATERIAL only where their measurement contract is load-bearing to claims TS-003 intends to make. Do not convert the edition into a benchmark catalogue.

No cross-task score ranking.

## 5. Profile Completeness

Build canonical `profile-completeness-v2.json` using current schema/tooling over VM-O01–VM-O16.

For each obligation, assign only a schema-valid evidence-grounded status such as SATISFIED / LIMITATION / NEEDS_RESEARCH as current Core defines.

Do not optimize for SATISFIED count.

An obligation may be `LIMITATION` and still be sufficiently researched for this edition if the residual is explicitly bounded and does not prevent the intended claim.

If an obligation genuinely requires new research before publication-quality closure, record `NEEDS_RESEARCH` honestly. **Do not perform that new research in this execution.** Stop for Sol review after producing/validating the completeness surface to the extent current Core permits.

At minimum, carry forward G01–G06 explicitly:

- G01 independent/non-vendor VLA evaluation scarcity
- G02 transferable control-oriented world-model benchmark absent
- G03 same-protocol document specialist vs generalist comparison absent
- G04 real-deployment latency / VRAM beyond author-reported values
- G05 independent reproduction of current vendor/model-report scores
- G06 SigLIP2 exact citation binding

Do not silently transform source scarcity into a positive finding.

The Completeness rationale must also preserve X01–X04:

- X01 data/supervision/post-training
- X02 objective/interface contract
- X03 efficiency/token/memory/latency economics
- X04 reliability/source-fidelity/claim strength

These are cross-cutting dimensions, not optional decorations.

## 6. Required audit surfaces

Create additive execution artifacts sufficient for Sol read-back, including at minimum:

- exact r5 Evidence/View identity used;
- materiality disposition counts;
- VM-O01–VM-O16 materiality coverage;
- high-level list of MATERIAL anchors per obligation;
- CONTEXT/EXCLUDED or equivalent rationale for important non-material records;
- duplicate/source-role handling summary;
- TS-001/TS-002 overlap handling summary;
- D04 cap read-back;
- D12–D14 combined-weight read-back;
- Profile Completeness per-obligation status/rationale;
- X01–X04 coverage read-back;
- G01–G06 disposition;
- residual limitations / access barriers / LOW_SIGNAL areas;
- stage-validation receipt;
- canonical checkpoint/state transition receipt.

Counts are diagnostic, not quality targets.

## 7. Canonical state advance

Use current canonical Core APIs/CLI/stage-validation machinery. Do not hand-edit `production-state.json`.

TS-002 precedent shows the valid transition:

`CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED`

with Evidence / Materiality / Completeness all marked passed from the `CANDIDATES_NORMALIZED` checkpoint when the combined stage contract validates.

Expected successful state after this execution:

- lifecycle = `EVIDENCE_REVIEWED`
- evidence checkpoint = `passed`
- materiality checkpoint = `passed`
- completeness checkpoint = `passed`
- selection = `pending`
- architecture = `pending`
- Human Architecture Review = `pending`

If current Core behavior differs, follow current Core rather than fabricating state. Report the exact canonical behavior.

If stage validation fails, or Completeness has a blocking contract that prevents valid advancement, stop fail-closed and report it. Do not bypass validation.

## 8. Prohibited

Do not:

- modify Discovery;
- modify Screening;
- modify r1–r5 accepted Evidence/Views;
- perform new source research;
- build Selection;
- build Architecture;
- produce Architecture Review dossier or Human decision;
- draft reader-facing chapters;
- build PDF;
- run Publication Preview / Freeze / Release;
- modify main;
- modify `production/survey-core-v2`.

Normal commit + non-force push only.

## 9. Final report

Report at minimum:

- startup guards;
- exact r5 Evidence/View validation;
- Materiality Ledger path/hash and disposition counts;
- Profile Completeness path/hash and overall/per-obligation status;
- VM-O01–VM-O16 summary;
- X01–X04 summary;
- G01–G06 status;
- residual limitations;
- stage validator result;
- final lifecycle/checkpoints;
- final remote HEAD/tree;
- main unchanged;
- Core unchanged;
- Selection not run;
- Architecture not run;
- Human decision not created.

Normal completion:

`TS-003 EVIDENCE_MATERIALITY_COMPLETENESS_COMPLETE`

`EVIDENCE_REVIEWED`

`AWAITING_SOL_MATERIALITY_COMPLETENESS_REVIEW`

`NO_SELECTION`

`NO_ARCHITECTURE`

Stop there.
