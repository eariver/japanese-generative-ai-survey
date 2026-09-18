# W37 execution instruction — Sol Architecture r1 REQUEST_CHANGES, regenerate from DISCOVERY_COLLECTED

Status: `EXECUTION_AUTHORITY / SOL_ARCHITECTURE_R1_REQUEST_CHANGES / OPERATOR_INVALIDATE_UNPRESENTED_GATE / REGENERATE_FROM_DISCOVERY_COLLECTED / BOUNDED_AT_FRESH_ARCHITECTURE_R2`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W37-v2-work`

## 1. Authority

This request imports the actual independent Sol review:

`sources/2026-W37/execution/reviews/sol-w37-architecture-r1-independent-review-20260919.md`

Sol verdict:

`REQUEST_CHANGES`

This is **not** a Human Architecture Review decision.

Human Architecture Review remains `PENDING`.

Do not record `APPROVED` or `REQUEST_CHANGES` as a Human decision.

The current r1 Human Gate surface was not accepted for Human presentation because Sol found blocking defects first. Treat it as an unpresented pending surface and invalidate it through the current canonical operator/stage invalidation mechanism.

Generic authority defect tracking:

Issue #506 — `Worker-generated Sol/Human review attribution must be prohibited`.

## 2. Invocation guard

The Muse invocation MUST supply the exact current remote HEAD/tree after this request commit is pushed.

Before any write, read-only verify:

- remote W37 HEAD == Exact Starting SHA from invocation;
- remote W37 tree == Exact Starting Tree from invocation;
- Exact Starting SHA parent == `3a7dae1942d4ba5522377d9d3a97fd12aa619ca2`;
- parent tree == `6f10819cbaead1f983bc99cd8be245379e9c7547`;
- remote `main` HEAD == `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`;
- remote main tree == `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

If any guard differs: zero repository/GitHub writes; report expected vs actual and STOP.

No alternate/fallback/repair/review/temp branch.

No force/reset/rebase/squash/history rewrite.

## 3. Reviewed r1 identity

Presented branch before Sol review:

- HEAD: `8fb3960f649249d60fc569e2d1dfc732ce382680`
- tree: `05e4e2e87ffada8ff567e95fcb32a542f7206a0f`

Architecture bytes reviewed at:

- commit: `1bef366ac8e21641027ddb9feda6263c0ed01aa4`
- tree: `6f86c640f844a14a1c0748f98db0a96d7d2bb14d`

Machine stage endpoint was valid:

`ARCHITECTURE_ESTABLISHED / HUMAN_GATE_REACHED`

but semantic/provenance Sol review failed.

## 4. Regeneration boundary

Earliest affected semantic stage:

`DISCOVERY_COLLECTED`

Reason:

The first false `Sol:` reviewer attribution appears in accepted Screening. Discovery itself is usable.

Preserve:

- Grok r3 Raw and X manifest;
- actual Sol Grok r3 correction review;
- 14-record accepted Discovery graph;
- all existing edition-local primary/secondary Raw captures;
- W36 carry-over source material.

Do **not** rerun Grok.

Do not repeat broad Discovery unless a narrowly bounded verification is needed for a blocking finding below.

Invalidate/regenerate:

`Screening -> Evidence -> Materiality -> Completeness -> Selection -> Architecture -> fresh r2 review surface`

Use current canonical invalidation/stage tooling. Inspect CLI/help before invocation.

Do not hand-edit production-state JSON.

## 5. RC-1 — reviewer provenance correction

Blocking defect:

Muse created files and semantic rationales claiming independent Sol authority despite the runner being Muse.

Historical worker files include:

- `sol-w37-discovery-completeness-20260918.md`
- `sol-w37-evidence-authority-consumption-20260918.md`
- `sol-w37-materiality-selection-20260918.md`
- `sol-w37-architecture-20260918.md`

Preserve them as historical r1 artifacts, but r2 must classify them as:

`WORKER_SELF_REVIEW / NON_AUTHORITATIVE_AS_SOL`

Do not delete/rewrite history merely to hide the defect.

### r2 requirements

Worker-generated Screening/Evidence/Materiality/Selection rationales must:

- use neutral wording, or
- identify Muse/worker provenance explicitly.

Forbidden unless supplied verbatim by a real Sol authority artifact:

- `Sol:`
- `Sol review`
- `Sol-owned`
- `Sol independent`
- `Sol supervisory`
- equivalent claims.

Do not generate a new file named or framed as independent Sol review.

Actual Sol review is performed after remote read-back by ChatGPT/Sol.

The r2 Human Gate shell/dossier must distinguish:

1. deterministic machine validation;
2. worker analysis;
3. prior actual Sol r1 REQUEST_CHANGES authority;
4. fresh r2 awaiting independent Sol review;
5. Human decision still pending.

## 6. RC-2 — Fusion exact time boundary

Canonical ordinary W37 UTC window:

`[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)`

Current stored Fusion capture establishes only:

`09.11.26`

not an hour.

The r1 worker statement:

`Fusion Sep 11 assumed ordinary daytime`

is prohibited.

### Required bounded verification

Attempt to establish an authoritative publication timestamp for:

`https://cognition.com/blog/local-fusion`

sufficient to compare against `2026-09-11T22:00:00Z`.

Acceptable authority may include first-party page metadata, first-party feed/API, repository/publication metadata, or another reliable first-party timestamp.

If exact/adequate time is established:

- preserve the authority in an edition-local Raw/verification record;
- classify by exact UTC boundary.

If it cannot be established:

- do not assume ordinary status;
- use current schema semantics to HOLD/bound/exclude Fusion from ordinary W37 selection/architecture;
- preserve the uncertainty explicitly.

Do not fabricate a timestamp.

Any Fusion disposition change must propagate downstream canonically.

## 7. RC-3 — resignation HOLD must not carry Architecture thesis

r1 Selection:

- resignation = `HOLD`
- architecture usage = `NONE`

but r1 thesis says the “100M-reach resignation” helped set the weekly safety bound.

Default r2 repair:

- keep resignation as CONTEXT/HOLD attention only;
- remove it from editorial thesis and package must-cover requirements;
- do not let it carry selected Architecture weight;
- use the selected Anthropic Sep 10 threat report as the technical safety package.

Do not promote the resignation merely to preserve r1 wording.

## 8. RC-4 — preserve OpenAI product/model boundaries

Do not repeat:

`OpenAI packaged Astra into Financial Services, voice, and harness APIs`

Evidence supports separate Sep 10 surfaces:

- Financial Services explicitly uses GPT-6 Astra reasoning;
- GPT-Live-1 is a separate full-duplex voice model/layer that can delegate to Astra or other backends;
- Agents API is a managed harness configurable with models; Astra may be an example/configuration.

r2 thesis/architecture must state these as distinct products/layers.

A safe conceptual structure is:

`OpenAI expanded its Sep 10 vertical/platform stack with Financial Services on Astra, a separate GPT-Live-1 voice API, and an Agents API harness.`

Exact wording is worker/editorial choice, but the semantic distinction is mandatory.

## 9. RC-5 — DeepSeek comparative/future boundary

Do not repeat an unqualified thesis claim equivalent to:

`V4.1 Flash beats its Pro at Flash rates`.

Evidence boundary:

- “ahead of V4-Pro” is vendor-reported; unnamed “multiple parties”; independent reproduction absent;
- API docs describe future Sep 14 routing from V4-Pro to V4.1-Flash, which is post-W37 occurrence even though the document is in-window.

r2 must:

- attribute comparative performance to DeepSeek/vendor reporting;
- keep independent-reproduction limitation;
- not describe Sep 14 routing as an event that occurred inside W37;
- separate in-window published pricing/economics from future routing.

## 10. Screening regeneration

Regenerate all 14 Screening decisions from the frozen Discovery set with correct runner provenance.

Expected substantive shape may remain 13 KEEP / 1 DROP if re-evaluation still supports it, except Fusion may change depending on timestamp verification.

Do not force previous counts.

The GLM rumor may remain DROP if current frozen authority still supports that disposition.

## 11. Evidence regeneration

Regenerate Evidence for all new non-DROP Screening candidates.

Existing primary Raw bodies may be reused and semantically consumed; do not re-fetch merely to create fresh timestamps.

Preserve:

- X as Raw Observation/community signal;
- vendor benchmark boundaries;
- independent reproduction gaps;
- source-authority distinctions;
- exact temporal classification.

If Fusion cannot be established ordinary, ensure Evidence does not label it `MAIN_EVENT` merely from calendar date.

No fake Sol materiality rationale.

## 12. Materiality / Completeness / Selection regeneration

Regenerate canonically from r2 Evidence.

Completeness may remain LIMITED if appropriate; do not force prior status/counts.

Selection rationale must be neutral/worker-attributed.

Do not copy r1 `Sol:` strings.

Resignation should remain HOLD/NONE unless new authority independently justifies a different decision; no such promotion is requested by Sol.

## 13. Architecture r2

Build fresh Architecture only after regenerated Selection.

Mandatory fixes:

- no false reviewer attribution;
- no date-only Fusion ordinary assumption;
- resignation HOLD not thesis-bearing;
- OpenAI Financial Services / Live / Agents boundaries distinct;
- DeepSeek comparative performance explicitly vendor-attributed;
- post-window future routing not represented as occurred W37 fact.

Preserve valid r1 strengths:

- seven-package shape may remain if still supported;
- all vendor benchmarks bounded;
- Fusion 39% max-not-uniform if Fusion remains selected;
- quiet image/video lanes remain quiet;
- Threat notable-examples/vendor-investigation bounds;
- North judge/license bounds;
- MiniCPM/Ling card-reported bounds.

## 14. Fresh r2 review surface and STOP

After Architecture r2 generation and deterministic validation:

- generate a fresh r2 Architecture Review shell/dossier;
- mark it `PENDING`;
- do **not** claim r2 was independently reviewed by Sol;
- cite the actual r1 Sol REQUEST_CHANGES as prior authority;
- STOP.

Normal endpoint:

`ARCHITECTURE_ESTABLISHED / fresh r2 Architecture Review pending independent Sol review`

No Human decision.

No Draft / Publication Preview / Freeze / Release.

## 15. Shared-Core freeze

Do not modify:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`
- `production/survey-core-v2`

Issue #506 is future Core hardening only.

Issue #505, #497, and release-workflow CLI defects remain out of scope.

If current Core cannot perform the bounded invalidation/regeneration without semantic workaround, record exact blocker and STOP. Do not patch Core.

## 16. Commit discipline

Stay on existing W37 branch.

Use meaningful normal commits, non-force push, remote read-back, and expected-prior-SHA checks.

No history rewrite.

## 17. Final report

Report:

- invocation Starting SHA/tree;
- operator invalidation boundary;
- Discovery preserved identity/count;
- Screening r2 distribution;
- Fusion timestamp verification result and resulting disposition;
- Evidence r2 status counts;
- Materiality/Completeness;
- Selection r2 distribution;
- confirmation no worker-generated false Sol authority remains in new r2 semantic artifacts;
- Architecture r2 thesis/packages;
- deterministic validation;
- r2 review path;
- ending HEAD/tree;
- main/Production Line unchanged;
- shared-Core changed paths = 0;
- stop reason.

Do not infer Human judgment.
