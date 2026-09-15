# W35 execution instruction — Architecture Review r1 REQUEST_CHANGES, bounded Architecture regeneration

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_REVIEW_R1_REQUEST_CHANGES / BOUNDED_TO_SELECTION_COMPLETE`

Date: `2026-09-15 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W35-v2-work`

## 1. Human decision authority

Human Architecture Review r1 decision:

`REQUEST_CHANGES`

Reviewed production authority:

`676160e325db35840af1f36b8cac8c3dad54beb4`

Presentation shell that exposed the pending Human gate:

`a5ab5113ce3d3ab41cdbd1a8121d534c4c5fd455`

Regeneration boundary:

`SELECTION_COMPLETE`

This is a bounded Architecture-only correction. The Human is **not** requesting new Discovery, Screening, Evidence, Materiality, Completeness, or Selection work.

The current Selection is accepted as the upstream basis for the repair. Do not reinterpret this REQUEST_CHANGES decision as permission to alter candidate dispositions or rerun research.

## 2. Starting guard

The Muse invocation will provide an Exact Starting SHA equal to the GitHub commit that contains this execution request.

Before any repository/GitHub write, read-only verify all of the following:

- remote `weekly/2026-W35-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- that Exact Starting SHA has parent `a5ab5113ce3d3ab41cdbd1a8121d534c4c5fd455`;
- remote `main` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote `main` tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- `sources/2026-W35/production-state.json` at the starting branch reports `ARCHITECTURE_ESTABLISHED`, `next_action = ARCHITECTURE_REVIEW`, `terminal_reason = HUMAN_GATE_REACHED`, and Architecture Review still pending before this Human decision is recorded;
- `sources/2026-W35/candidate-selection-v2.json` is the r1 Selection authority with `17 SELECTED / 2 HOLD` and is unchanged from the reviewed r1 gate.

If any guard differs, perform no repository/GitHub write, report expected versus actual, and STOP.

No force push, reset, history rewrite, fallback branch, alternate W35 branch, or Core repair branch is authorized by this instruction.

## 3. Mandatory read order

After the guard passes, read at minimum:

1. `sources/2026-W35/execution/reviews/architecture-r1.md`
2. `sources/2026-W35/execution/reviews/architecture-r1-dossier.md`
3. this execution request
4. `sources/2026-W35/candidate-selection-v2.json`
5. `sources/2026-W35/architecture-v2.json`
6. `sources/2026-W35/architecture-review-summary-v2.json`
7. `sources/2026-W35/architecture-review-attention-v2.json`
8. the accepted Evidence cards for the three P1 anchors:
   - GLM-5.3-Flash: candidate `candidate:2026-W35:be4a33f4e49afd7a`
   - Qwen3.8-Flash-Next: candidate `candidate:2026-W35:16371443ec36c482`
   - Hy4 preview: candidate `candidate:2026-W35:b52eeb85a267ab91`
9. current canonical Core commands/contracts for recording a Human Architecture Review REQUEST_CHANGES and regenerating from `SELECTION_COMPLETE`.

Do not rely on the machine `READY_FOR_ARCHITECTURE_REVIEW` status as a substitute for this Human decision.

## 4. Review finding that must be corrected

The r1 Architecture structure is broadly accepted: five packages, current candidate membership, package order, HOLD handling, negative-space accounting, and evidence boundaries are not being rejected.

The blocking defect is narrower:

The r1 editorial thesis aggregates model-specific properties into a cluster-wide factual statement:

> `sub-5%-activation MoEs with offloadable memory shipped under MIT and permissive licenses`

That formulation exceeds the accepted Evidence boundary.

### 4.1 Active-ratio problem

The accepted Evidence cards report approximately:

- GLM-5.3-Flash: `18B active / 320B total` = `5.625%`
- Qwen3.8-Flash-Next: `~6B active / 125B total` ≈ `4.8%`
- Hy4 preview: `~49B active / 770B total` ≈ `6.36%`

Therefore `sub-5%-activation MoEs` is **not** a valid common property of the three P1 anchors. It is, at most, a Qwen-specific characterization under the current Evidence.

Do not preserve an aggregate threshold claim merely because all three are sparse/MoE systems.

### 4.2 License-authority problem

The accepted Evidence does not support presenting `MIT and permissive licenses` as a settled cluster-wide common property.

In particular:

- GLM MIT weight availability remains explicitly `UNRESOLVED` pending Z.ai/HF primary verification;
- Qwen `qwen-community-1.0` license terms remain explicitly `UNRESOLVED` pending primary verification;
- Hy4's accepted card is secondary/relayed and does not establish a common license framing for the cluster.

License statements must remain per-model and bounded by the relevant Evidence status. Do not convert unresolved license targets into a thesis-level common fact.

### 4.3 Offload / serving characterization

Do not attribute an offloadable-memory or other architecture mechanism to the entire three-model cluster unless the accepted Evidence establishes it for each relevant model.

Model-specific architecture/serving properties may remain in P1, but they must be attached to the correct model and inherit its Evidence boundary.

## 5. Required correction

Regenerate Architecture from the unchanged `SELECTION_COMPLETE` authority so that the top-level thesis and P1 framing use only properties supported at the common-cluster level.

A suitable semantic direction is:

> In 2026-W35, open-weight competition centered on architectural efficiency: large MoE releases and previews paired relatively low active-parameter counts with increasingly explicit serving-efficiency goals, while the agent coding plane reorganized around portable sessions, agent-native forges, and deterministic guardrails; flagship claims and governance moves remain inside explicit evidence bounds.

This wording is **guidance, not mandatory literal text**. Use the strongest formulation that is actually supported by the accepted Evidence.

The corrected Architecture must satisfy all of the following:

1. No cluster-wide `sub-5%` claim unless every model in the scope actually satisfies and supports it.
2. No cluster-wide license claim that promotes unresolved per-model license assertions.
3. No cluster-wide offload/memory mechanism unless common support exists.
4. Qwen-specific ~4.8% active ratio may be described as Qwen-specific and bounded as relayed/unresolved where appropriate.
5. GLM 18B/320B and Hy4 49B/770B may be described model-specifically only with their current PARTIAL/relayed boundaries.
6. License details, if retained, must be model-specific and reflect VERIFIED/PARTIAL/UNRESOLVED authority precisely.
7. The `preview` status of Qwen3.8-Flash-Next relative to Qwen 4 and Hy4 preview must remain explicit.
8. Existing benchmark/vendor-claim boundaries must not be weakened.
9. X remains community-signal authority only, never technical verification.

## 6. Upstream immutability for this bounded run

Do **not** rerun or change:

- Grok/X Source Intake;
- Discovery;
- Screening;
- Evidence;
- Evidence Edition Views;
- Materiality;
- Completeness;
- candidate matrix;
- candidate Selection dispositions;
- the `17 SELECTED / 2 HOLD` decision set;
- Raw source bytes;
- current `main` or `production/survey-core-v2`.

The existing upstream artifacts must remain byte-identical unless the canonical Human-decision machinery itself writes required provenance/state metadata outside those substantive artifacts.

If the current Core requires invalidation metadata or review provenance to be written, that is allowed. Substantive upstream research/selection content is not.

## 7. Human decision recording

Record the r1 Human Architecture Review decision through the repository's canonical Human-gate mechanism, not by manually pretending the old r1 Architecture was approved.

The recorded decision must express:

- decision: `REQUEST_CHANGES`;
- reviewed revision: Architecture Review `r1`;
- reviewed production authority: `676160e325db35840af1f36b8cac8c3dad54beb4`;
- presentation shell: `a5ab5113ce3d3ab41cdbd1a8121d534c4c5fd455` where supported by the review surface;
- regeneration boundary: `SELECTION_COMPLETE`;
- requested change: remove/repair thesis-level aggregation of unsupported `sub-5%`, common-license, and common-offload claims while preserving the accepted Selection and five-package structure.

Do not invent additional Human requested changes.

## 8. Architecture regeneration

After recording REQUEST_CHANGES, use the canonical regeneration/invalidation flow from `SELECTION_COMPLETE`.

Regenerate all Architecture-stage artifacts that the current Core requires, including fresh machine review/attention surfaces and stage validation as appropriate.

Expected substantive scope:

- `architecture-v2.json` thesis/P1 framing and any directly dependent architecture fields;
- Architecture review summary/attention surfaces;
- Architecture-stage validation/checkpoint/provenance that must change because Architecture bytes changed;
- execution/review/session records required for r2 presentation.

Preserve the five-package architecture unless the canonical generator requires a mechanically equivalent reserialization:

1. `w35-open-efficient-turn`
2. `w35-agent-coding-plane`
3. `w35-flagship-receipts`
4. `w35-infra-regional`
5. `w35-safety-governance`

Candidate membership and PRIMARY/SUPPORTING roles are accepted and should not change in this run.

## 9. Fresh Architecture Review r2

After regeneration and validation, create/present a **fresh Human Architecture Review r2**.

The r2 review dossier must make the correction auditable by explicitly showing:

- the r1 Human `REQUEST_CHANGES` decision;
- regeneration boundary `SELECTION_COMPLETE`;
- the old thesis/problematic formulation;
- the new thesis;
- confirmation that Selection membership/dispositions are unchanged;
- confirmation that Discovery/Evidence/Selection were not rerun;
- confirmation that P1 model-specific ratios/license states remain bounded correctly;
- exact reviewed production HEAD for r2;
- machine validation result;
- Human decision remains `PENDING` for r2.

Do not reuse the r1 Human decision as approval of r2.

## 10. Stop condition

Normal stopping point:

`fresh Human Architecture Review r2 pending`

At that point:

- lifecycle should again be `ARCHITECTURE_ESTABLISHED`;
- `next_action` should be `ARCHITECTURE_REVIEW`;
- `terminal_reason` should be `HUMAN_GATE_REACHED`;
- r2 Human decision must be `PENDING`;
- Draft generation must not start.

STOP and report:

- starting SHA;
- Human REQUEST_CHANGES decision record/provenance;
- regeneration boundary used;
- ending production commit and presentation-shell commit if distinct;
- ending branch HEAD/tree;
- changed paths;
- old vs new editorial thesis;
- confirmation of byte-identical substantive upstream Selection/Evidence authority;
- fresh r2 Architecture Review path;
- whether any unexpected Core defect was encountered.

## 11. Core repair policy

No Core defect is currently identified. This request is an edition-local Architecture correction.

If a genuine generic Core defect is discovered while executing the canonical REQUEST_CHANGES/regeneration mechanism, STOP before ad-hoc repair and report it. Do not merge any Core repair to `main` under this instruction.
