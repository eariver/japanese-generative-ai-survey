# W34 Luna/Work execution request — Discovery gap-fill after Sol Review r1

Status: `EXECUTION_AUTHORITY / SOL_DISCOVERY_REVIEW_R1_REQUEST_GAP_FILL / DISCOVERY_ONLY / STOP_AT_SOL_DISCOVERY_REVIEW_R2`

Date: `2026-09-08 JST`

## 1. Repository guard

Repository:

`eariver/japanese-generative-ai-survey`

Existing branch only:

`weekly/2026-W34-v2-work`

The exact W34 Starting SHA and tree are intentionally **not self-anchored in this committed instruction file**. Committing this instruction necessarily advances the branch, so a SHA embedded here would immediately become stale.

Before any write, Luna/Work must receive the current exact W34 branch SHA/tree from the external Sol handoff message and verify read-only that:

```text
origin/weekly/2026-W34-v2-work == externally supplied exact Starting SHA
```

The reviewed Core authority remains:

`origin/main == 0a47a9b85108c5a2e9644037e7c0fb48b5bd96dc`

If the external exact W34 SHA/tree is absent, or either remote ref differs, make zero writes, report the actual refs, and stop.

The externally supplied SHA/tree overrides any historical parent SHA mentioned in earlier handoffs. Do not infer the starting SHA from timestamps, local checkout state, or this file's parent.

Do not create a new/fallback/repair/review/iteration branch. No force push, reset, rebase, or history rewrite.

## 2. Mandatory read order

Read from current reviewed main and W34 branch:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/survey-production-core-v2-sol-luna-review-governance.md`
4. `docs/survey-production-core-v2-authority.md`
5. `sources/2026-W34/execution/reviews/sol-discovery-completeness-review-20260908-r1.md`
6. `sources/2026-W34/execution/luna/w34-architecture-r2-research-sufficiency-revision-r1/discovery-research-dossier.md`
7. `sources/2026-W34/execution/luna/w34-architecture-r2-research-sufficiency-revision-r1/sol-discovery-review-handoff.md`
8. current canonical Discovery, State, Production Profile, and event-level inventory

The Sol review is authoritative for this bounded gap-fill execution.

## 3. Mission

Do not proceed to Screening.

Repair Discovery completeness only, addressing every blocking finding in:

`sources/2026-W34/execution/reviews/sol-discovery-completeness-review-20260908-r1.md`

The intended flow is:

```text
DISCOVERY_COLLECTED
-> official-channel fallback gap fill
-> full collected-arXiv relevance triage
-> fresh event-level Discovery reconciliation
-> canonical Discovery regeneration/validation
-> DISCOVERY_COLLECTED
-> SOL_DISCOVERY_REVIEW_R2_READY
-> STOP
```

This is an internal Sol supervisory loop, not a new Human Gate.

## 4. Official-channel fallback gap fill

A configured collector failure is not a negative result.

For each failed or weak official lane, use alternate first-party official surfaces before declaring the lane unresolved.

At minimum explicitly recheck:

- Alibaba Cloud / Model Studio / Qwen ecosystem
- xAI official news/product pages
- AWS official Bedrock/AgentCore/What's New/blog surfaces
- Microsoft/Azure/GitHub official AI surfaces
- IBM official AI/model/platform announcement surfaces

Also recheck any other major lane where the prior fresh collector reported only a timeout, HTTP error, index-only snapshot, or unstable chronology.

Do not rely on secondary press when a first-party official page is accessible.

### Mandatory Alibaba reconciliation

Sol independently found the official Alibaba Model Studio lifecycle page:

`https://www.alibabacloud.com/help/en/model-studio/newly-released-models`

At minimum inspect and reconcile the in-window entries currently showing:

- `wan3.0-video-prime` — 2026-08-20
- `kimi-k3` — 2026-08-19
- `qwen3.8-27b` — 2026-08-17
- `ZHIPU/GLM-5.3` — 2026-08-17

Do not blindly create four stories. Determine event identity at Discovery level only.

Required identity handling includes:

- split Alibaba Model Studio `wan3.0-video-prime` in-window service availability from later Runway Wan 3.0 availability currently grouped in `W34-C072`;
- distinguish base model release from provider/service distribution availability;
- refine/split Qwen3.8-27B and GLM-5.3 chronology only where first-party source supports a distinct W34 delta;
- represent Kimi K3 service/distribution availability if it is not already covered by an event-equivalent row.

Preserve exact source/provenance and chronology precision.

## 5. arXiv triage repair

The prior refresh collected 2,296 unique arXiv entries but the materializer used eight hard-coded `wanted_arxiv` IDs. That is not sufficient negative-space evidence.

Perform a transparent relevance triage over the full already-collected arXiv set.

Requirements:

1. Do not recollect arXiv unless the existing Raw is corrupt or incomplete.
2. Do not use a fixed hand-selected ID list as the sole extraction mechanism.
3. Build a broad reviewable shortlist from the collected entries.
4. Preserve at least arXiv ID, title, published timestamp, categories, candidate technical lane, concise relevance rationale, and duplicate/merge relationship when applicable.
5. Record the triage method and counts at each step.
6. A broad deterministic title/abstract keyword prefilter is permitted only as an assistive high-recall pass; document its vocabulary and do not treat it as semantic truth.
7. Do not impose a target paper count or story quota.
8. Do not make Materiality/Selection decisions.
9. Keep plausible research candidates even if later Evidence may reject them.

Create a durable arXiv triage artifact under the new bounded execution directory so Sol can inspect the shortlist and rejected/merged rationale.

## 6. Fresh event-level Discovery inventory

The old event-level inventory contains 105 events, while the prior refresh added 15 Discovery leads to the canonical graph.

Before Screening can ever resume, create a new event-level inventory revision that reconciles:

- the prior 105 event rows;
- the 15 prior refresh leads;
- the official-channel fallback findings from this run;
- the arXiv triage findings from this run.

For every event-level row preserve traceability to source/Discovery authority.

Explicitly record:

- unchanged event
- new event
- merged duplicate
- split event identity
- chronology correction/refinement
- pre-window / in-window / post-cutoff boundary where known
- unresolved chronology where exact time remains unavailable

Do not attach Screening, Materiality, Selection, or Architecture dispositions beyond Discovery-boundary vocabulary.

## 7. Canonical Discovery regeneration

Use reviewed repository-owned Core mechanisms to regenerate and validate canonical Discovery from the corrected research basis.

Do not hand-edit accepted authority merely to make validation pass.

The run must end again at:

`DISCOVERY_COLLECTED`

with Screening and every downstream checkpoint still pending.

## 8. New execution area

Create one new execution area:

`sources/2026-W34/execution/luna/w34-discovery-gapfill-after-sol-review-r1/`

Before creation verify it does not already exist.

If it exists, do not invent retry/r2/repair names; report and stop.

Do not edit the prior Luna execution directory or Sol review record.

## 9. Required Sol handoff r2

Create a new Sol Discovery Review r2 handoff that includes:

- starting SHA/tree;
- final SHA/tree;
- official channels exercised and exact fallback surfaces used;
- official retrieval failures that remain after alternate-surface attempts;
- prior event count;
- revised event-level inventory count;
- added/merged/split/chronology-corrected counts;
- Alibaba reconciliation result for each of the four named entries;
- arXiv full-set triage method;
- total collected arXiv entries;
- deterministic-prefilter count if used;
- semantic shortlist count;
- duplicate/irrelevant/boundary counts where available;
- high-signal papers needing later Evidence depth;
- remaining negative-space concerns;
- canonical Discovery acceptance path/SHA256;
- Production State path/SHA256;
- proof that Screening was not executed.

Explicit final markers:

`SCREENING_NOT_AUTHORIZED_BY_SOL_REVIEW_R1`

`SCREENING_NOT_EXECUTED`

`SOL_DISCOVERY_REVIEW_R2_REQUIRED`

`SOL_DISCOVERY_REVIEW_R2_READY`

## 10. Stop discipline

Do not execute:

- Screening
- Evidence
- Evidence Authority Supplement regeneration
- Materiality
- Completeness
- Candidate Matrix
- Selection
- Architecture
- Drafting
- Publication Preview
- sidecar QA
- PDF build
- freeze/release

Stop after fresh Discovery validation and remote read-back.

Normal completion status:

`SOL_DISCOVERY_REVIEW_R2_READY`
