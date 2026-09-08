# W34 Sol Evidence Authority-Consumption Review r1

Status: `SOL_EVIDENCE_REVIEW_R1 / PASS_FOR_SELECTION_EXECUTION / SELECTION_NOT_YET_EXECUTED`

Date: `2026-09-09 JST`

## Review basis

This is the mandatory Sol supervisory review after Muse Spark 1.3 completed the fresh W34 Evidence run and after shared-Core PR #486 was Human-approved, merged to `main`, passed post-integration CI, and was integrated into the existing W34 production branch.

Reviewed W34 integration head at review start:

`284e57d345b60665e110d29596306266816a2cc5`

Reviewed Core main:

`6d748a962d57beff89da7c1b20cb5a9a86c8e261`

The W34 `scripts/survey_evidence_v2.py` runtime blob used for the completed Evidence work is byte-identical to the Human-approved Core blob now present on reviewed `main`. The newly integrated Core regression test preserves fail-closed behavior for unknown source types.

The existing `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` Stage Checkpoint still records the historical execution implementation identity `f062a12386d20a96d91eebe4d2d9f083181cd644`. That historical checkpoint is therefore not treated by Sol as proof that reviewed Core had already authorized the run at execution time. Instead, the completed Evidence bytes are treated as immutable content-addressed inputs which must be revalidated under the current reviewed implementation when the Selection stage is materialized. Current `survey_stage_validation_v2.py` performs that upstream Evidence/View/Materiality/Completeness revalidation before accepting Selection.

## Evidence coverage

Fresh Screening basis:

- total candidates: 439
- non-DROP Evidence tasks: 409

Fresh Evidence result counts:

- `VERIFIED`: 49
- `PARTIAL`: 352
- `NEEDS_MORE`: 8

Authority-consumption ledger:

- `AUTHORITY_CONSUMED`: 401
- `AUTHORITY_CAPTURED_BUT_UNCONSUMED`: 2
- `AUTHORITY_NOT_FOUND`: 5
- `AUTHORITY_RETRIEVAL_FAILED`: 1

All eight non-consumed/unresolved rows are `NEEDS_MORE` and are isolated as `HOLD`; none is marked high-signal.

The two captured-but-unconsumed rows are the OpenRouter image-model ranking/methodology item and the Kling MCP/CLI chronology item. They remain explicitly bounded rather than being promoted by source presence alone.

## Regression audit

The systematic defect found in Architecture r2 — primary authority captured but not semantically consumed — is not reproduced in the mandatory high-signal regression cases.

### ChatGPT for Teens

PASS. The accepted Evidence card consumes the OpenAI first-party body and creates candidate-local claims for automatic teen routing, stronger safeguards, and Study Mode. The old contradictory generic limitation requiring an authoritative source is gone. Vendor-described safeguard effectiveness and uncaptured page dateline are retained as source-specific limitations.

### Mistral Agentic Search

PASS. The accepted Evidence card consumes the Mistral first-party body and records the multi-step find/inspect/verify loop, search/open/navigate/read/grep tools, source reading and search refinement. Maker-reported FinanceBench/OfficeQA Pro results are explicitly separated from independently established fact.

### AgentCore Payments

PASS. Multiple AWS first-party surfaces are consumed. Functional payment/API/MCP transaction capability, guardrails and observability are separated from vendor framing.

### Claude Platform Computer Use / Skills / Files

PASS. Anthropic first-party announcement/docs surfaces are consumed and the distinct Computer Use, Skills API, Files API and browser-use surfaces are represented as candidate-local Evidence.

### GPT-5.6 Sol pricing

PASS. The W34 pricing/access delta is distinguished from the base-model release and is backed by OpenAI pricing/changelog/model authority plus AWS distribution authority.

### Grok Bot chronology

PASS with bounded chronology note. The Evidence target distinguishes the Aug 11 base launch from the Aug 21 W34 expansion. The later/re-dated xAI page is not used to rewrite the base event as an Aug 21 launch.

## Materiality review

The provisional ledger contains:

- `MATERIAL`: 41
- `CONTEXT`: 358
- `HOLD`: 10
- `EXCLUDED`: 26
- `DUPLICATE`: 4

Sol independently reviewed the MATERIAL surface and the unresolved/HOLD boundary.

The previous pathological compression (`MATERIAL=1`) is no longer present. The 41 MATERIAL items form several coherent editorial clusters rather than one isolated story:

1. agent execution moves into production control planes — payments, computer use, policy/authorization, memory, long-running execution;
2. agent work becomes collaborative and embedded — Slack code channels, GitHub Copilot in Slack/Teams/JetBrains, enterprise Antigravity;
3. retrieval/tool orchestration becomes a product layer — Mistral Agentic Search, Runway MCP workflows and related MCP/Skills surfaces;
4. safety/security/governance changes — teen routing/safeguards, ZDR-compatible monitoring, cyber-capability pacing, exploited-vulnerability/security-chain events, watermarking;
5. model economics and distribution — GPT-5.6 pricing/cross-region access, Grok Bedrock distribution, Qwen/DeepSeek/provider availability deltas;
6. multimodal/creative distribution — Pika audio, Adobe Firefly audio, Wan provider availability and related workflow changes;
7. infrastructure and ecosystem economics — OpenRouter/Stripe and compute/infrastructure commitments.

Not every MATERIAL row should become a standalone article. Several AWS, GitHub and provider-distribution rows are natural supporting context for broader selected stories. Selection must therefore avoid both the old one-story compression and the opposite failure of converting all 41 MATERIAL rows into article quota.

## Paper audit

Research-paper candidates were not promoted wholesale merely because they appeared in the 314-item research shortlist. The large majority remain `PARTIAL` / `CONTEXT`; paper bodies were captured one at a time and used as bounded research Evidence. No paper-only quota is imposed.

## Limitations and non-blocking caveats

- Profile Completeness remains `LIMITED`; this is not equivalent to failed Evidence sufficiency, but must remain visible to Selection and Architecture.
- Eight Evidence tasks remain unresolved and must not be silently upgraded downstream.
- Some date-bound candidates retain boundary/chronology qualifiers.
- Several MATERIAL rows describe implementation/control-plane deltas rather than model launches; Architecture should group them by editorial significance rather than vendor count.
- The historical Evidence Stage Checkpoint retains the pre-review implementation SHA. It must not be rewritten. The next deterministic stage validation must revalidate the immutable upstream Evidence basis against the current reviewed repository implementation.

## Sol disposition

`PASS_FOR_SELECTION_EXECUTION`

This PASS means:

- Discovery research sufficiency has already passed Sol review;
- the fresh Evidence set demonstrates material semantic consumption of primary authority;
- unresolved authority gaps are explicitly isolated rather than disguised;
- provisional Materiality is sufficiently rich and coherent for Sol-owned Selection;
- Selection may now be materialized under current reviewed Core, but Selection has not yet been executed or approved by this record.

This is not Human Architecture approval and does not authorize drafting.

Mandatory next boundary:

`EVIDENCE_REVIEWED -> SOL-OWNED SELECTION -> CURRENT-CORE STAGE VALIDATION -> SELECTION_COMPLETE`

Architecture may be generated only after Sol has reviewed the Selection result. Human Architecture Review remains the next Human Gate.