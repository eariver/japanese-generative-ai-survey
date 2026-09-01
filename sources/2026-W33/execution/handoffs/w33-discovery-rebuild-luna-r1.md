# 2026-W33 Sol→Luna handoff — Discovery reconstruction r1

Status: `READY_FOR_LUNA / BOUNDED MATERIALIZATION ONLY`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at specification time: `ISSUE_INITIALIZED`  
Current machine next action: `stage:discovery`  
Requested Human stop: `ARCHITECTURE_REVIEW`

This file is the execution authority for the first Work/GPT-5.6 Luna task in the Sol/Luna production split. The caller supplies the exact commit SHA containing this file. Luna must start from that exact canonical-branch SHA and must not silently rebase onto later production changes.

## 1. Objective

Materialize a **Sol-defined candidate Discovery package** for 2026-W33 under current Core v2 0.15, including exact recovered X/Grok task/result provenance and the Raw dependencies required by the Discovery records.

The worker endpoint is **a committed candidate ready for Sol semantic review**.

Do **not** execute `ADVANCE_STAGE`, do not create/commit a canonical Discovery acceptance/checkpoint, and do not change `production-state.json`. Sol reviews the candidate commit first; deterministic Core advancement happens only after that review.

## 2. Role boundary

Luna may:

- read current reviewed-main Core instructions and schemas;
- recover exact historical repository bytes from the refs named below;
- recover exact Drive bytes named below;
- perform source-local collection only from the explicit first-party URLs named below;
- materialize schema-conforming repository artifacts;
- perform deterministic validation;
- commit only the bounded candidate/work-record outputs described here.

Luna must not:

- change the Discovery scope;
- add opportunistically discovered sources or topics;
- decide Materiality, Selection, Architecture, or Human Gate outcomes;
- promote X claims to technical fact;
- restore old Production State, accepted checkpoints, old Human Gate state, or old Core contracts;
- use the historical accepted Discovery artifact as current acceptance authority;
- advance the lifecycle.

If this specification conflicts with current reviewed-main Core syntax/schema, record the exact conflict as `NEEDS_SOL_REVIEW` and stop before changing lifecycle authority.

## 3. Required authority reads

Read before writing:

1. `AGENTS.md` from reviewed `main`.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed `main`.
3. `docs/survey-production-core-v2-x-source-intake.md` from reviewed `main`.
4. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed `main`.
5. `scripts/survey_x_intake_v2.py` from reviewed `main`.
6. `scripts/survey_discovery_v2.py` from reviewed `main`.
7. `sources/2026-W33/production-profile.json` and `production-state.json` on the canonical work branch.
8. `sources/2026-W33/execution/index.md` and the latest Sol session records.
9. `docs/checkpoints/2026-W33-core015-handoff-20260829.md`.
10. `sources/2026-W33/postmerge-research-intake.md` from `archive/pre-core015-2026-W33-v2-work-20260829` as Sol-reviewed editorial research input only, not acceptance authority.

## 4. Frozen Sol decisions

These decisions are not delegated to Luna.

### 4.1 Historical Discovery seed

Use exactly:

- ref: `temp/w33-discovery-stage`
- verified commit: `a52e95c42ee09d46b3b0c89f0dfb99ed2bc988c8`
- seed path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- seed record count: **37**

The 37 JSONL records are reusable semantic seed material. Do **not** copy:

- `discovery-accepted-v2.json` as current authority;
- old Production State;
- old checkpoint provenance;
- old Human Gate state.

For each preserved seed record, inspect `source.raw_paths`. Restore only the exact missing Raw files required by the final candidate records, at the same repository-relative paths, from the named historical refs. Do not copy historical trees wholesale when a smaller exact set suffices.

### 4.2 Canonical X run

The canonical reconstruction input is the later post-merge run:

- run id: `weekly-x-2026-W33-postmerge-r1`
- Drive task path: `Grok_X_SourseIntake/Weekly/2026-W33/weekly-x-2026-W33-postmerge-r1/grok-task.md`
- repository task path: `sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/grok-task.md`
- exact task byte count: **9612**
- exact task SHA-256: `c86a6124bb0ff32832995883d37b7f44e08da7142af4ac39032fb7436035b356`
- Drive result filename/title: `grok-x-result.md`
- repository Raw path: `sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md`
- exact result byte count: **12171**
- exact result SHA-256: `93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06`
- result frontmatter `observed_at`: `2026-08-23T12:48:54+00:00`
- canonical Weekly window: `[2026-08-07T18:00:00-04:00, 2026-08-14T18:00:00-04:00)`

Recover the exact Drive bytes. If the Drive download layer supplies a `.txt` filename for the result, keep the exact bytes but store them at the repository Raw path above. Do not normalize line endings or rewrite frontmatter.

The older `weekly-x-2026-W33-fresh-r1` run is historical/comparison material only for this reconstruction and must not become the canonical X manifest run.

Build/materialize current-schema `sources/2026-W33/external/x/x-source-intake-v2.json` around the recovered exact task/result bytes. The manifest must validate under current reviewed-main Core.

Use:

- Profile policy: `REQUIRED_BY_PROFILE`
- decision: `REQUIRED`
- series_context: `null`
- Drive category: `Weekly`
- edition folder: `2026-W33`
- result status: `SUCCESS`
- Discovery disposition: `DISCOVERY_RECORDED`
- Discovery id: `x-weekly-signal-wave`

Recover the run purpose, research questions, coverage focus, time scope, expected result filename and Drive path semantics from the exact task file; do not invent replacements. Set `imported_at` to the actual Luna import time in UTC.

### 4.3 X Discovery record

Preserve the existing seed discovery id:

`x-weekly-signal-wave`

but rebind its X provenance and `source.raw_paths` to the postmerge Raw above. The record must remain community/discovery signal, not publication-grade technical Evidence.

If its old summary cannot be supported by the postmerge Raw, replace only that summary with a neutral source-local synopsis limited to themes directly observed in the Raw, including the Aug. 12–14 release wave, coding/agentic emphasis, open/local adoption, price pressure, practical local-inference constraints, and counter-signals where present.

### 4.4 Exactly four missing model-release discoveries

The old 37-record package omitted four individually verified first-party W33 model-release records. Add exactly these four new Discovery records; do not add other new topics in this Luna task.

Use `origin = GAP_FILL`, `research_pass = 1`, no parent refs, and obligations including `weekly:current-relevance` and `weekly:technical-significance` unless current schema/authority requires an equivalent existing obligation form.

Use these stable ids unless they collide with an existing seed id:

1. `gapfill-model-grok-4_6`
2. `gapfill-model-qwen3_8-open-weight-expansion`
3. `gapfill-model-gemini-3_7-flash`
4. `gapfill-model-glm-5_3`

If any of these subjects is already represented by an individual event-level record in the 37-record seed, stop and report the exact collision to Sol instead of silently changing the expected count.

#### Grok 4.6

First-party URL only:

- `https://x.ai/news/grok-4-6`

Event date: `2026-08-12`.

Bounded framing: long-running agents, coding/knowledge work, ambitious interactive/visual tasks. Vendor benchmark claims remain vendor-attributed; do not synthesize cross-vendor ranking.

#### Qwen3.8 W33 open-weight expansion

First-party URL only:

- `https://github.com/QwenLM/Qwen3.8`

Relevant in-window chronology already fixed by Sol:

- `2026-08-12`: Qwen3.8-2.4T-A95B
- `2026-08-14`: Qwen3.8-27B

Bounded framing: W33 is the open-weight/deployment expansion of the Qwen3.8 family, not a claim that the family itself was first announced in W33. Do not import consumer-GPU parity/speed claims from X as technical fact.

#### Gemini 3.7 Flash

First-party URLs only:

- `https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/`
- `https://deepmind.google/models/model-cards/gemini-3-7-flash/`
- `https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash`

Event date: `2026-08-13` GA.

Bounded framing: workhorse model for coding/agents; native multimodal input, function calling, code execution, preview computer use, configurable thinking where directly supported by the first-party pages. Pricing/comparative claims remain Google-attributed.

#### GLM-5.3

First-party URL only:

- `https://z.ai/blog/glm-5.3`

Event date: `2026-08-14`.

Bounded framing: same base model as GLM-5.2; claimed gains from scaled post-training; complex coding/long-horizon emphasis and cybersecurity capability growth. Preserve the critical boundary that the page says local weights will become available later; W33 must not imply weights were already downloadable in-window. Vendor benchmark/vulnerability claims remain attributed.

### 4.5 New source-local Raw captures

For the four gap-fill records, create bounded source-local captures under:

`sources/2026-W33/collectors/sol-approved-primary-gapfill/runs/w33-model-wave-r1/raw/`

Use clear stable filenames. Each capture should include:

- source URL;
- page/repository title;
- retrieval timestamp;
- event date(s) when explicitly supported;
- concise source-local observations needed by the Discovery record;
- no long page mirror and no unsupported inference.

Use:

- `collector_id = sol-approved-primary-gapfill`
- `collector_run_id = w33-model-wave-r1`

The Google subject may bind multiple capture files to one Discovery record.

## 5. Expected candidate shape

Final candidate should contain **41 Discovery records**:

- 37 historical semantic seed records, with `x-weekly-signal-wave` provenance updated to postmerge X Raw;
- plus exactly 4 model-release gap-fill records above.

Expected final path:

`sources/2026-W33/discovery/discovery-v2.jsonl`

Do not commit `sources/2026-W33/discovery/discovery-accepted-v2.json` in this worker task.

## 6. Historical Raw recovery rule

For each final seed-derived Discovery record:

1. parse its `source.raw_paths`;
2. test whether the path exists on the canonical work branch;
3. if missing, recover the exact bytes from `temp/w33-discovery-stage@a52e95c42ee09d46b3b0c89f0dfb99ed2bc988c8` when present;
4. if a required path is not present there, inspect `temp/w33-x-import@85031fd91bad19ee093c7aa1730a7539878a265d` and `archive/pre-core015-2026-W33-v2-work-20260829` only to locate the exact historical Raw;
5. if still unresolved, stop with `NEEDS_SOL_REVIEW` and list the exact missing paths.

Do not rewrite historical Raw to make validation pass.

## 7. Validation before commit

Run all applicable current-Core deterministic checks without lifecycle advancement.

Minimum required:

1. JSONL parses successfully.
2. Exactly 41 unique `discovery_id` values.
3. Every final `source.raw_paths` file exists.
4. X task SHA/bytes exactly match the fixed values above.
5. X result SHA/bytes exactly match the fixed values above.
6. `scripts/survey_x_intake_v2.py validate` passes for the COMPLETE current manifest.
7. Exercise `scripts.survey_discovery_v2.build_acceptance(...)` only into a temporary, non-repository path or otherwise perform an equivalent no-write validation so the candidate Discovery graph/X integration is proven valid; do not commit the generated acceptance artifact.
8. `production-state.json` bytes are unchanged from task start.
9. No shared-Core path is modified.
10. Git diff is limited to the write allowlist below.

## 8. Write allowlist

Allowed candidate writes:

- `sources/2026-W33/discovery/discovery-v2.jsonl`
- exact Raw paths referenced by preserved seed records that are missing on the reset branch
- `sources/2026-W33/external/x/x-source-intake-v2.json`
- `sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/grok-task.md`
- `sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md`
- `sources/2026-W33/collectors/sol-approved-primary-gapfill/runs/w33-model-wave-r1/raw/**`
- `sources/2026-W33/execution/sessions/w33-luna-discovery-rebuild-20260829-r1.md`
- `sources/2026-W33/execution/index.md`
- optional Luna validation/report files under `sources/2026-W33/execution/luna/w33-discovery-rebuild-r1/**`

Forbidden writes include:

- `sources/2026-W33/production-state.json`
- canonical Discovery accepted/checkpoint artifacts
- operator requests/bridge runs for stage advancement
- shared Core roots (`AGENTS.md`, `config/`, `schemas/`, `scripts/`, `.github/workflows/`, `docs/survey-production-core-v2-*.md`)
- publication, gate approval, or Architecture artifacts

## 9. Work record / crash recovery

Create `sources/2026-W33/execution/sessions/w33-luna-discovery-rebuild-20260829-r1.md` using the execution-record policy headings and record material milestones, not tool-call transcripts.

Update `sources/2026-W33/execution/index.md` so it records:

- Luna task path;
- worker start SHA;
- worker output commit SHA when available;
- current lifecycle still `ISSUE_INITIALIZED`;
- status `AWAITING_SOL_REVIEW` after candidate commit;
- exact next action: Sol semantic review of the candidate before Core advancement.

## 10. Final report to Sol

Return:

- starting SHA;
- ending commit SHA;
- changed-file list/count;
- final Discovery count and unique-id count;
- restored historical Raw file count;
- new gap-fill Raw capture count;
- X task SHA/bytes;
- X result SHA/bytes;
- current manifest validation result;
- no-write Discovery acceptance/graph validation result;
- confirmation that Production State did not change;
- any `PARTIAL`, `UNRESOLVED`, or `NEEDS_SOL_REVIEW` item.

Do not continue into Screening. Sol reviews this commit first.
