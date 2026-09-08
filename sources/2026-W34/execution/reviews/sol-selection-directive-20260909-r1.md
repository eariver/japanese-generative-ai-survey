# W34 Sol Selection Directive r1

Status: `SOL_SELECTION_DIRECTIVE_R1 / EXECUTION_MATERIALIZATION_AUTHORIZED / ARCHITECTURE_NOT_AUTHORIZED`

Date: `2026-09-09 JST`

## Authority and basis

This directive is the Sol-owned semantic Selection decision following:

- Sol Discovery Review r2 PASS;
- Muse Spark 1.3 fresh Screening and 409-task Evidence execution;
- Human-approved shared-Core PR #486 and post-integration CI;
- formal integration of reviewed `main@6d748a962d57beff89da7c1b20cb5a9a86c8e261` into W34;
- Sol Evidence Authority-Consumption Review r1 PASS.

The executor may materialize this directive into deterministic Candidate Matrix / Candidate Selection artifacts. The executor must not change the semantic decisions below.

Architecture is not authorized by this directive.

## Selection principle

The fresh Evidence surface contains 41 `MATERIAL` Evidence candidates, 358 `CONTEXT` candidates and 10 `HOLD` candidates among the 409 non-DROP Evidence tasks.

Sol's decision is:

- select **all 41 MATERIAL candidates** for Architecture consideration;
- designate **10** of those as `PRIMARY` story anchors;
- designate the remaining **31** as `SUPPORTING` evidence/context within seven editorial clusters;
- assign every `CONTEXT` candidate to Selection `HOLD`;
- assign every materiality `HOLD` candidate to Selection `HOLD`;
- no `REJECT` or `INSPECT` disposition is required in this Selection revision.

This does **not** mean 41 standalone articles. The selected supporting candidates exist so Architecture can combine fine-grained product/provider deltas into a smaller number of coherent packages without losing material factual coverage.

Expected Selection summary:

- candidate_count: 409
- SELECTED: 41
- HOLD: 368
- REJECT: 0
- INSPECT: 0
- selected_count: 41

## Required assignment conventions

For every Candidate Matrix row:

- preserve the matrix row `profile_extensions` exactly in Selection `profile_extensions`;
- use the exact deterministic Matrix `candidate_id`;
- every Matrix candidate must be assigned exactly once.

For PRIMARY selected rows:

- `disposition = SELECTED`
- `architecture_usage = PRIMARY`
- `publication_role = WEEKLY_MAGAZINE:primary-story-anchor`
- `architecture_role` = the cluster role specified below.

For SUPPORTING selected rows:

- `disposition = SELECTED`
- `architecture_usage = SUPPORTING`
- `publication_role = WEEKLY_MAGAZINE:supporting-evidence`
- `architecture_role` = the cluster role specified below.

For non-selected rows:

- `disposition = HOLD`
- `architecture_usage = NONE`
- `publication_role = null`
- `architecture_role = null`

Non-selected `CONTEXT` rationale must state that the candidate remains researched context/negative space but is not selected into W34 Architecture because the current Evidence/View does not establish `MATERIAL` status.

Non-selected materiality `HOLD` rationale must state that the candidate remains withheld because of an unresolved Evidence/materiality/chronology boundary and must not be silently upgraded downstream.

## Editorial clusters and exact selected Discovery identities

### A. `WEEKLY:agent-control-plane`

Editorial meaning: agents are moving from model/tool demos into governed production execution surfaces: transactions, computer use, policy, authorization, memory and durable execution.

PRIMARY:

- `w34-event-c010` — Amazon Bedrock AgentCore Payments GA
- `w34-event-c011` — Claude Platform Computer Use / Skills API / Files API

SUPPORTING:

- `w34-event-c007`
- `w34-event-c031`
- `w34-event-c087`
- `w34-event-c104`
- `w34-event-c105`
- `w34-event-gap-aws-agentcore-memory-json`

### B. `WEEKLY:collaborative-agent-workflows`

Editorial meaning: agent execution is becoming embedded in shared software-development and communication surfaces rather than remaining an isolated one-user chat/session.

PRIMARY:

- `w34-event-c012` — Slack code channels for agents

SUPPORTING:

- `w34-event-c052`
- `w34-event-c066`
- `w34-event-c096`
- `w34-event-c099`
- `w34-event-c100`
- `w34-event-c101`
- `w34-event-c102`
- `w34-event-refresh-kimi-code-cli-v038-v037`
- `w34-event-refresh-openai-replit-gpt56-luna`

### C. `WEEKLY:retrieval-tool-orchestration`

Editorial meaning: retrieval, navigation, MCP/tool invocation and workflow execution are increasingly productized as agent orchestration layers.

PRIMARY:

- `w34-event-c019` — Mistral Agentic Search

SUPPORTING:

- `w34-event-c045`
- `w34-event-c047`

### D. `WEEKLY:safety-security-governance`

Editorial meaning: this week materially changes how frontier products route users, monitor risk, pace dangerous capability, expose security failure modes, and satisfy provenance/compliance expectations.

PRIMARY:

- `w34-event-c004` — ChatGPT for Teens
- `w34-event-c055` — CoSnitch / Copilot security chain

SUPPORTING:

- `w34-event-c002`
- `w34-event-c005`
- `w34-event-c006`
- `w34-event-c008`
- `w34-event-refresh-openai-defenders-window`

### E. `WEEKLY:model-economics-distribution`

Editorial meaning: material change is not only a new base model; price, provider availability, region coverage and open/local accessibility change what can actually be deployed this week.

PRIMARY:

- `w34-event-c017` — GPT-5.6 Sol W34 pricing/access delta
- `w34-event-c039` — Qwen3.8 W34 availability/local adoption

SUPPORTING:

- `w34-event-c023`
- `w34-event-c030`
- `w34-event-c040`
- `w34-event-gap-alibaba-kimi-k3-model-studio`

### F. `WEEKLY:creative-multimodal-production`

Editorial meaning: multimodal/creative AI continues shifting from individual model releases toward production availability across image, video and audio workflows.

PRIMARY:

- `w34-event-c091` — Adobe Firefly music/speech/sound-effects availability

SUPPORTING:

- `w34-event-c018`
- `w34-event-c020`
- `w34-event-c022`
- `w34-event-gap-alibaba-wan30-model-studio`

### G. `WEEKLY:ecosystem-infrastructure-economics`

Editorial meaning: the AI stack is also changing structurally through gateway consolidation and large compute/infrastructure commitments, affecting routing and deployment economics beyond individual models.

PRIMARY:

- `w34-event-c003` — OpenRouter joining Stripe

SUPPORTING:

- `w34-event-c026`

## Exact count guard

Before writing Candidate Selection, the executor must verify that the deterministic current-Core Candidate Matrix contains exactly one Evidence candidate whose `discovery_ids` contains each of the 41 identities listed above, and that all 41 of those Matrix rows have `materiality == MATERIAL`.

Expected counts from this directive:

- PRIMARY identities: 10
- SUPPORTING identities: 31
- selected identities total: 41

If any listed identity is missing, appears more than once across Matrix candidates, has materiality other than `MATERIAL`, or if an additional Matrix row is `MATERIAL` but not listed here, the executor must not improvise. Stop and return the exact discrepancy to Sol.

## Rationale policy

The executor may render concise assignment rationales from the exact cluster semantics in this directive, but must not invent a new editorial reason, promote a CONTEXT/HOLD candidate, demote a listed MATERIAL candidate, or move a candidate to another cluster.

Suggested PRIMARY rationale template:

`Sol Selection r1 primary anchor for <cluster>: <candidate title> is a materially verified/qualified W34 change that anchors this cluster; finer-grained related deltas remain supporting evidence rather than standalone story quota.`

Suggested SUPPORTING rationale template:

`Sol Selection r1 supporting evidence for <cluster>: material W34 delta retained to support the cluster without requiring a standalone article.`

## Negative space

The 368 non-selected Matrix candidates remain part of the reviewed research record. They are not deleted or treated as failed research.

- `CONTEXT` means useful researched context that did not cross the current W34 materiality threshold.
- materiality `HOLD` means unresolved Evidence/materiality/chronology prevents selection.

Architecture Review must later expose the major negative-space and omission rationale rather than presenting only the selected set.

## Mandatory executor boundary

Authorized next machine path:

`EVIDENCE_REVIEWED -> deterministic Candidate Matrix -> Candidate Selection materialization -> current-Core stage validation -> SELECTION_COMPLETE`

The stage validation must run under the **current reviewed W34 repository implementation** and therefore revalidate the immutable upstream Screening/Evidence/View/Materiality/Completeness basis.

The historical Evidence checkpoint at implementation `f062a12386d20a96d91eebe4d2d9f083181cd644` must not be rewritten.

After `SELECTION_COMPLETE`, stop at:

`SOL_SELECTION_REVIEW_READY`

Do not generate Architecture, Architecture Review Summary, Architecture Review Attention, Drafting, Publication Preview, sidecar QA, PDF, freeze or release.
