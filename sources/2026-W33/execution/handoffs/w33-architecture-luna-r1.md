# 2026-W33 Sol→Luna handoff — Architecture proposal r1

Status: `READY_FOR_LUNA / ARCHITECTURE_PROPOSAL_ONLY / EXPECTED_COMPLETENESS_BLOCKER / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical branch: `weekly/2026-W33-v2-work`  
Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle: `SELECTION_COMPLETE`  
Current action: `stage:architecture`  
Target Human Gate: `ARCHITECTURE_REVIEW`  
Selection advancement verification: `sources/2026-W33/execution/reviews/w33-selection-advance-sol-review-20260830-r1.md`

The caller must supply the exact current branch HEAD containing this handoff and the updated recovery index. Luna must clone/check out that exact branch state and verify remote HEAD equality before any write. If it differs, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 1. Objective

Materialize only the W33 proposed Architecture and its deterministic Human-review surfaces:

1. create `sources/2026-W33/architecture-v2.json` as a `PROPOSED` Issue Architecture;
2. derive `sources/2026-W33/architecture-review-summary-v2.json` from current Core;
3. derive `sources/2026-W33/architecture-review-attention-v2.json` from current Core with limit 50;
4. validate the Architecture against exact upstream Selection authority;
5. validate the Review Summary as exact deterministic derivation;
6. validate Review Attention;
7. run the current-stage validator at `SELECTION_COMPLETE` with exactly those three current artifacts;
8. record one Luna session file;
9. commit/push only those four paths;
10. stop for Sol semantic review.

Do **not** run `ADVANCE_STAGE` in this task. Do not create a Stage Checkpoint, Architecture approval/revision record, Draft package, Draft result, synthesis artifact, manuscript, PDF, or publication artifact.

Successful endpoint:

`ARCHITECTURE_PROPOSAL_READY_FOR_SOL_REVIEW`

The deterministic Architecture Review Summary is expected to be `BLOCKED` only because accepted Profile Completeness is currently `INCOMPLETE`. That expected blocker is not permission to ignore any other error.

## 2. Frozen authority

### Production State

At start verify exact current State:

- path: `sources/2026-W33/production-state.json`
- SHA-256: `15be77ab1902510131b3ffb765b2c1c13f86800cf0dadd07a7d03a5c5cdb8c9d`
- lifecycle: `SELECTION_COMPLETE`
- next action: `stage:architecture`
- Selection: `passed`
- Architecture: `pending`
- Architecture Review: `pending`
- terminal reason: null

Production State must remain byte-identical during this proposal task.

### Candidate Matrix

- path: `sources/2026-W33/candidate-matrix-v2.json`
- SHA-256: `1b660291564bda5f30debd86bb6911eb53edf06e8f735710f84652d972c4d198`
- candidates: 37

### Candidate Selection

- path: `sources/2026-W33/candidate-selection-v2.json`
- SHA-256: `9c6997d2ed3921a847db5e001ec9377189bb25d5475454593f23016308557005`
- SELECTED 28 = PRIMARY 21 / SUPPORTING 7
- HOLD 6 / REJECT 3 / INSPECT 0

Sol semantic authority:

`sources/2026-W33/execution/reviews/w33-selection-sol-review-20260830-r1.md`

Decision:

`ACCEPT / SELECTION_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

### E/M/C authority

- Profile: `sources/2026-W33/production-profile.json`, SHA-256 `19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`
- Materiality Ledger: `sources/2026-W33/materiality-ledger-v2.json`, SHA-256 `cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`
- Profile Completeness: `sources/2026-W33/profile-completeness-v2.json`, SHA-256 `9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`
- Evidence acceptance: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- repaired Edition View set: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`

Completeness is frozen for this task:

- overall: `INCOMPLETE`
- current relevance: `LIMITATION`
- technical significance: `LIMITATION`
- carry-over obligations: `NEEDS_RESEARCH`

Do not rewrite any upstream authority.

## 3. Required read order

Before any write, read:

1. `AGENTS.md` at reviewed main.
2. `docs/survey-production-core-v2-session-bootstrap.md` at reviewed main.
3. `docs/survey-production-core-v2-execution-record-policy.md` at reviewed main.
4. `config/survey-production-v2.json` at reviewed main, especially `SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED` and `ARCHITECTURE_REVIEW` gate inputs.
5. `schemas/issue-architecture-v2.schema.json`.
6. `schemas/architecture-review-summary-v2.schema.json`.
7. `schemas/architecture-review-attention-v2.schema.json`.
8. `scripts/survey_architecture_v2.py` and `scripts/survey_architecture_v2_base.py`.
9. `scripts/survey_review_attention_v2.py`.
10. `scripts/survey_stage_validation_v2.py`.
11. `scripts/survey_agent_tool_v2.py` for current-stage historical package handling.
12. current `production-profile.json`, `production-state.json`, Candidate Matrix, Candidate Selection, Completeness, Materiality Ledger.
13. `sources/2026-W33/execution/reviews/w33-selection-sol-review-20260830-r1.md`.
14. `sources/2026-W33/execution/sessions/w33-luna-selection-advance-20260830-r1.md`.
15. `sources/2026-W33/execution/reviews/w33-selection-advance-sol-review-20260830-r1.md`.
16. this handoff.

For editorial precedent only, Luna may read:

`sources/2026-W32/issue-architecture-v0.1.md`

W32 is not W33 factual authority.

## 4. Architecture thesis

Use an editorial thesis equivalent in substance to:

> W33の生成AIは、単発のモデル性能競争だけでなく、モデル/APIの利用形態、実運用を支えるserving/runtime、そしてagent systemの評価・信頼性設計が同時に前進した週として読む。モデル発表を羅列せず、「何が使えるようになったか」「どう運用するか」「どう測り、壊れ方を捉えるか」を一つの技術潮流として構成する。

The exact Japanese prose may be polished, but do not change the substance into a generic “many models were released” thesis.

Architecture goals must include all of the following concepts:

1. compress 28 selected candidates into coherent editorial packages rather than 28 article slots;
2. preserve single-home semantics for dedicated event vs index/access/support records;
3. give serving/runtime and agent evaluation/reliability real structural weight rather than treating them as release-note sidebars;
4. keep research papers grouped by technical question where possible rather than one-paper-one-article;
5. preserve every Evidence limitation and attribution boundary in the package that consumes the candidate;
6. keep X/community evidence contextual only;
7. expose unresolved carry-over as a Human-review blocker rather than silently dropping or promoting it.

## 5. Page plan

Use:

```json
{
  "target_pages": 18,
  "max_pages": 24,
  "notes": "W32's approximately 18-page weekly-magazine architecture is used only as editorial precedent. W33 should fit six substantive packages plus cover/contents/synthesis/source notes; selected-candidate count must not determine page count."
}
```

The 18/24 values are editorial planning numbers, not factual claims.

## 6. Exact six-package structure

Use exactly these six package IDs and drafting order. Titles may receive minor Japanese editorial polishing but package purpose and candidate placement must remain equivalent.

### 1. `w33-frontier-models-access`

Working title: `Frontier Models & Access — 性能競争から「どう使えるか」へ`

Purpose: compare the strongest W33 model/API/open-weight developments by access mode, controllability, deployment surface, and bounded technical positioning rather than six isolated release notes.

PRIMARY candidates:

- `candidate:2026-W33:8f686c0ca43adb04` — GPT-5.6 Sol Ultrafast API preview
- `candidate:2026-W33:02186efabc1adee3` — Qwen3.8 open-weight series
- `candidate:2026-W33:a7382c928aaf7a34` — Gemini 3.7 Flash
- `candidate:2026-W33:ca6a8ccdef944c08` — Grok 4.6
- `candidate:2026-W33:e7efd5ec0f61a3f8` — DeepSeek-V4-Pro API update
- `candidate:2026-W33:a4c3f4c1d7da594d` — GLM-5.3

SUPPORTING candidates:

- `candidate:2026-W33:51d2b6df5349ba4f` — Gemini API chronology
- `candidate:2026-W33:cbb5d5b272ed68b6` — Grok index chronology
- `candidate:2026-W33:c756cddb93a383a1` — W33 X community signal wave

Must cover:

- availability/access surface differences: API preview, GA API/app/web, open weights, partner channels where actually evidenced;
- exact chronology and post-cutoff boundaries;
- vendor claims remain attributed;
- GLM direct-page/benchmark/cyber/local-weight limitations remain explicit;
- GPT Ultrafast preview-vs-GA and performance-measurement uncertainty remains explicit;
- X is reader/context signal only, never technical authority.

Publication planning target: roughly 3 substantive pages.

### 2. `w33-cyber-access-governance`

Working title: `Cyber Access & Governance — 高能力モデルを誰に、どの境界で開くか`

PRIMARY:

- `candidate:2026-W33:6118ffacbd5f2ab4` — GPT-5.6-Cyber / Daybreak Red

SUPPORTING:

- `candidate:2026-W33:ed6c8786bd01008d` — Daybreak on Amazon Bedrock
- `candidate:2026-W33:b585d075aee90b44` — Daybreak partner/governance access context

Must cover:

- authorized vulnerability-research/security-testing context;
- distinguish program access from general model/API availability;
- model/access scope and safeguard boundaries;
- Bedrock/partner records are distribution/governance support, not duplicate launches.

Publication planning target: roughly 2 pages.

### 3. `w33-serving-runtime`

Working title: `Serving & Runtime — 新モデルを「使える」に変える実装層`

PRIMARY:

- `candidate:2026-W33:5c01e3060037bcb5` — vLLM v0.27.0
- `candidate:2026-W33:e2d4c5e6687a1d91` — llama.cpp b10369

SUPPORTING:

- `candidate:2026-W33:4dbf548aae8b62fd` — SGLang v0.5.17
- `candidate:2026-W33:cff4fbabb60c45ab` — FlashInfer v0.6.17

Must cover:

- model availability depends on serving/runtime support;
- distinguish full serving framework, local inference runtime, front-end/cache behavior, and low-level kernels;
- do not turn every project release into a standalone launch article;
- preserve project-reported performance/timing attribution if mentioned.

Publication planning target: roughly 2 pages.

### 4. `w33-memory-decoding-systems`

Working title: `Inference Systems Deep Dive — KVメモリとdecodingをどう組み替えるか`

PRIMARY:

- `candidate:2026-W33:7fd5c6c0b34e96c6` — vToken
- `candidate:2026-W33:88728dc06945dd90` — OasisKV
- `candidate:2026-W33:a1f086cab5a80708` — Ripple-Pivot Search

SUPPORTING: none.

Must cover:

- vToken: logical/physical token indirection, reclamation/repacking, compatibility claims only as evidenced;
- OasisKV: tiered-memory/lookahead sparse prefetch and author-reported trade-offs;
- Ripple-Pivot: training-free decoding change for diffusion LLMs;
- frame all reported evaluations as paper-author results, not independent reproduction;
- compare problems and mechanisms; do not present three disconnected abstracts.

Publication planning target: roughly 2 pages.

### 5. `w33-agent-evaluation-reliability`

Working title: `Agent Reliability — interfaceよりscaffolding、成功率より失敗の構造`

PRIMARY:

- `candidate:2026-W33:14aade682991a3e4` — controlled MCP/CLI scaffolding comparison
- `candidate:2026-W33:1bd2bbd1244b55bb` — unified issue-resolution benchmark
- `candidate:2026-W33:e821e85cf1f9eb00` — Agentic Transaction
- `candidate:2026-W33:1d2206529402becc` — PluginEval
- `candidate:2026-W33:9821c729d7b65c2e` — REDAgentBench
- `candidate:2026-W33:2680059eda6bb020` — Agent Skills Can Be Harmful

SUPPORTING: none.

Must cover:

- distinguish scaffolding/interface effects, requirements/planning, function-call diagnosis, executable red teaming, transaction semantics, and skill-induced regressions;
- synthesize around how an agent system is evaluated and where failure originates;
- preserve benchmark/environment scope and author-report attribution;
- avoid a six-paper summary list.

Publication planning target: roughly 3 pages.

### 6. `w33-multimodal-media`

Working title: `Multimodal & Media — 生成・編集・理解をworkflowでつなぐ`

PRIMARY:

- `candidate:2026-W33:a2c7d35f90da3ed9` — VideoGAIA
- `candidate:2026-W33:4b0d709fe4bde8ee` — VoiceDesigner
- `candidate:2026-W33:495c437f7961dcef` — ComfyUI v0.31.0

SUPPORTING: none.

Must cover:

- VideoGAIA as multi-turn/tool-augmented video understanding evaluation, not a model ranking claim;
- VoiceDesigner as unified generation/editing research with baseline/novelty/evaluation questions preserved;
- ComfyUI as implementation-facing workflow/runtime change;
- connect research capability to practical media workflow without implying direct interoperability unless Evidence says so.

Publication planning target: roughly 2 pages.

## 7. Placement invariants

Core requires:

- every SELECTED PRIMARY candidate has **exactly one** Architecture destination unless a declared selected exception is used;
- every SELECTED SUPPORTING candidate has at least one Architecture destination;
- placement kind must exactly match Selection `architecture_usage`;
- no HOLD/REJECT candidate may appear in package candidate arrays;
- no candidate may be both primary and supporting in one package;
- every `remaining_boundaries` string from Candidate Matrix for every placed candidate must be present exactly in that package's `boundaries` array.

For this r1 proposal, use **no `selected_exceptions`** unless Core reveals a direct impossibility. Expected value is `[]`.

Do not place a PRIMARY in more than one package. Cross-package narrative references are drafting/synthesis work and do not require duplicate Architecture destinations.

## 8. `must_cover_requirements`

Each package must include concise unique strings that state the actual editorial obligations above. Requirements must be drafting-actionable, not generic placeholders such as “cover candidate facts.”

At minimum each package must specify:

- what factual distinction the section must explain;
- what attribution/uncertainty boundary must survive;
- what duplicate/single-home error must be avoided where relevant;
- what reader-facing synthesis question links the candidate set.

## 9. Extensions

Use package `profile_extensions` to preserve Weekly editorial directives. Recommended stable keys:

```json
{
  "weekly_angle": "<candidate-specific package synthesis angle>",
  "window_policy": "Preserve Candidate Matrix window_relation and carry-over semantics; do not backdate post-cutoff/context records.",
  "attribution_policy": "Preserve Evidence attribution and unresolved boundaries exactly."
}
```

Use package `publication_extensions` with:

```json
{
  "section_kind": "FEATURE|DEEP_DIVE|SYSTEMS|PAPER_SYNTHESIS",
  "target_pages": 2,
  "layout_note": "<brief magazine-layout intent>"
}
```

For package 1 and package 5 use target_pages 3; all other substantive packages use 2.

Architecture-level `profile_extensions` should record:

- `weekly_thesis`: the package-level synthesis thesis;
- `carry_over_gate_status`: `BLOCKED_BY_ACCEPTED_INCOMPLETE_COMPLETENESS`;
- `community_signal_policy`: X/community is context only.

Architecture-level `publication_extensions` should record:

- `planned_substantive_pages`: 14;
- `planned_total_pages`: 18;
- `hard_max_pages`: 24;
- `editorial_precedent`: W32 approximately 18-page weekly architecture, structure only.

These extensions are directives, not factual claims.

## 10. Issue Architecture envelope

Write:

`sources/2026-W33/architecture-v2.json`

Requirements:

- schema version `2.0-rc1`;
- issue/profile identities exact;
- `status="PROPOSED"`;
- exact basis hashes from current upstream artifacts;
- six packages above;
- `selected_exceptions=[]` expected;
- `human_review.reviewed_by=null`;
- `human_review.reviewed_at=null`;
- `human_review.review_reference=null`.

Do not set `APPROVED` and do not invent Human review metadata.

## 11. Deterministic Architecture Review Summary

Write:

`sources/2026-W33/architecture-review-summary-v2.json`

Derive it with current Core `build_architecture_review_summary()` under the current agent-first runtime basis override required by historical accepted Screening/Evidence package State hashes.

Do not hand-edit the summary.

Expected readiness:

```text
BLOCKED
```

Expected blocker set after Architecture semantic validity is achieved:

```text
Profile Completeness is INCOMPLETE; Architecture Review is not ready
```

The exact deterministic wording is authoritative.

If `readiness.errors` contains **anything else**, do not normalize it away. Stop with:

`ARCHITECTURE_PROPOSAL_HAS_ADDITIONAL_CORE_ERRORS_NEEDS_SOL_REVIEW`

This includes package-placement errors, missing Evidence boundaries, invalid Selection basis, artifact drift, or architecture schema errors.

## 12. Deterministic Review Attention

Write:

`sources/2026-W33/architecture-review-attention-v2.json`

Use `scripts/survey_review_attention_v2.py` / `build_attention()` with limit `50`, exact current:

- Screening acceptance;
- Materiality Ledger;
- Candidate Selection.

Do not hand-edit it.

At the current W33 decision volume it is expected not to truncate; verify rather than assume.

## 13. Current-stage validation

Run the canonical `SELECTION_COMPLETE` stage validator with exactly:

- `issue-architecture=sources/2026-W33/architecture-v2.json`
- `architecture-review-summary=sources/2026-W33/architecture-review-summary-v2.json`
- `architecture-review-attention=sources/2026-W33/architecture-review-attention-v2.json`

The stage contract may PASS even though the Review Summary reports `BLOCKED`, because the summary is required to be the exact deterministic derivation. Record both facts distinctly in the Luna session.

Do not interpret stage-contract PASS as Human-gate readiness.

## 14. Allowed writes

This task may create only:

1. `sources/2026-W33/architecture-v2.json`
2. `sources/2026-W33/architecture-review-summary-v2.json`
3. `sources/2026-W33/architecture-review-attention-v2.json`
4. `sources/2026-W33/execution/sessions/w33-luna-architecture-20260830-r1.md`

No other repository path may change.

Production State, all prior checkpoints, Profile, Discovery, Screening, Evidence, Views, Ledger, Completeness, Matrix, and Selection must remain byte-identical.

## 15. Luna session record

Record at minimum:

- exact starting SHA;
- reviewed main SHA;
- all frozen upstream hashes;
- six package IDs and candidate placement counts;
- architecture SHA-256;
- deterministic Review Summary SHA-256 and readiness/errors;
- deterministic Review Attention SHA-256, total/shown/overflow/truncated counts;
- current-stage validation result;
- explicit statement that no State advancement or Human gate operation occurred;
- exact changed paths;
- local/GitHub transport identity distinctions, if any;
- final status.

Successful stop status:

`ARCHITECTURE_PROPOSAL_READY_FOR_SOL_REVIEW_WITH_EXPECTED_COMPLETENESS_BLOCKER`

## 16. Stop conditions

Stop for Sol without advancing if any of the following occurs:

- branch HEAD drift;
- current State differs from frozen `SELECTION_COMPLETE` basis;
- Candidate Matrix/Selection bytes drift;
- any upstream artifact drift;
- package placement cannot satisfy current Core;
- any selected candidate cannot preserve its exact Matrix boundaries;
- Review Summary has any error other than the known `INCOMPLETE` Completeness blocker;
- Review Attention cannot be deterministically validated;
- shared Core/config/schema changes appear necessary;
- an actual editorial choice outside this handoff becomes unavoidable.

Do not create a Human Exception Gate merely because the known Completeness blocker exists. It is expected to surface at Architecture Review through the ordinary Human Gate/revision contract.
