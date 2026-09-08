# W34 Luna/Work execution request — Screening and Evidence after Sol Discovery Review r2

Status: `EXECUTION_AUTHORITY / SOL_DISCOVERY_REVIEW_R2_PASS / SCREENING_AND_EVIDENCE / STOP_AT_SOL_EVIDENCE_REVIEW`

Date: `2026-09-08 JST`

## 1. Repository guard

Repository:

`eariver/japanese-generative-ai-survey`

Existing branch only:

`weekly/2026-W34-v2-work`

The exact Starting SHA and Expected Starting Tree are supplied externally by the Sol handoff that invokes this request. Do not infer them from a commit embedded in this file.

Reviewed Core main:

`0a47a9b85108c5a2e9644037e7c0fb48b5bd96dc`

Before any write, verify read-only that:

- remote W34 branch HEAD == externally supplied Exact Starting SHA;
- remote W34 branch tree == externally supplied Expected Starting Tree;
- remote main HEAD == `0a47a9b85108c5a2e9644037e7c0fb48b5bd96dc`.

If any guard differs, make zero writes, report expected/actual values, and stop.

Do not create a new/fallback/repair/review/iteration branch. No force push, reset, rebase, history rewrite, or branch replacement.

## 2. Mandatory read order

Read before execution:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/survey-production-core-v2-sol-luna-review-governance.md`
4. `docs/survey-production-core-v2-authority.md`
5. `docs/survey-production-core-v2-issue-prevention-checklist.md`
6. `sources/2026-W34/execution/reviews/sol-discovery-completeness-review-20260908-r1.md`
7. `sources/2026-W34/execution/reviews/sol-discovery-completeness-review-20260908-r2.md`
8. `sources/2026-W34/execution/luna/w34-discovery-gapfill-after-sol-review-r1/sol-discovery-review-handoff-r2.md`
9. current W34 Production Profile, State, canonical Discovery acceptance/JSONL, and reconciled event-level Discovery inventory
10. prior W34 Evidence Authority Expansion and r2 Evidence only as historical inputs/lessons, not as current active authority unless the fresh Core run explicitly rebinds them

Sol Review r2 is the supervisory authority for this bounded execution.

## 3. Mission and exact stop boundary

Discovery is now sufficient to authorize downstream research execution.

Execute only:

```text
DISCOVERY_COLLECTED
-> fresh Screening
-> CANDIDATES_NORMALIZED
-> Evidence + iterative authority gap fill
-> provisional Materiality + Completeness as required by the Core stage contract
-> EVIDENCE_REVIEWED
-> SOL_EVIDENCE_REVIEW_READY
-> STOP
```

Current Core combines Evidence, Materiality, and Completeness in the `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` stage. Those Materiality/Completeness outputs are provisional execution artifacts subject to Sol semantic review.

Do **not** execute:

- Candidate Selection;
- `EVIDENCE_REVIEWED -> SELECTION_COMPLETE`;
- Architecture;
- Drafting;
- Publication Preview;
- sidecar QA;
- PDF build;
- freeze/release.

## 4. Fresh Screening requirements

Run fresh canonical Screening from the current canonical Discovery authority.

Do not reuse the old W34 Screening acceptance merely because it previously validated.

Use the reconciled event-level Discovery inventory as a semantic cross-check for:

- split event identities;
- provider-distribution vs base-model distinctions;
- chronology refinements;
- existing/prior duplicate relationships;
- the expanded arXiv research surface.

Do not silently revert to the old 105-event research basis.

Screening must remain pre-Materiality. It may remove clear duplicates, irrelevant/off-profile items, or chronology-ineligible items according to Core/Profile authority, but must not optimize toward a desired article count.

For research papers, do not DROP merely because the item is a paper or because the arXiv shortlist is large. Use technical relevance and duplicate/event identity. Conversely, do not keep every score-based arXiv shortlist row merely because `semantic_shortlist=true`; that label is not Sol semantic approval.

Record a Screening reconciliation summary with counts and explicit treatment of:

- prior 105-event candidates;
- 15 previous refresh leads;
- Alibaba split/refinement events;
- new AWS AgentCore Memory event;
- new arXiv shortlist identities;
- duplicate/merged paper relationships;
- chronology-boundary candidates.

After Screening validation, commit/push/read-back before beginning Evidence.

## 5. Evidence execution principle — authority must be consumed, not merely bound

The central regression being repaired in W34 is `AUTHORITY_CAPTURED_BUT_UNCONSUMED`.

For every non-DROP Evidence task:

1. identify the task's concrete verification target;
2. retrieve/inspect appropriate first-party or primary technical authority;
3. preserve exact source/provenance according to repository authority;
4. extract candidate-local bounded claims from the source body;
5. make limitations source-specific;
6. ensure the Evidence status and verification target reflect what the captured authority actually supports.

A `PRIMARY_OFFICIAL` binding alone is not completion.

Do not leave generic placeholders such as:

- `a separately captured authoritative source is required`;
- `locator only`;
- `technical details remain unaccepted`;
- `pending authoritative verification`;

when the required primary body is already captured and readable.

If a source body is captured but not substantively read/used, classify that in the execution-side consumption ledger as `AUTHORITY_CAPTURED_BUT_UNCONSUMED`; do not represent it as completed verification.

## 6. Iterative authority gap fill

One retrieval attempt per candidate is not a stopping rule.

For material or plausibly material candidates, follow an appropriate authority ladder until the remaining limitation is defensible. Depending on the candidate, this can include:

- official announcement/article;
- official release notes/changelog;
- product/API documentation;
- model card/system card;
- repository release/tag/commit;
- paper body, not merely title/index metadata;
- security/advisory database;
- official provider/cloud distribution page.

A failed configured URL must trigger an alternate first-party route when one is reasonably available.

Do not substitute secondary press for accessible first-party authority.

Do not fabricate inaccessible content.

## 7. Evidence regression cases that must be explicitly rechecked

### ChatGPT for Teens

The prior W34 Evidence card was internally contradictory: it bound OpenAI first-party sources but still said a separately captured authoritative source was required.

Fresh Evidence must inspect the actual first-party body and reflect supported product facts such as age routing / teen experience / stronger safeguards where appropriate. Do not inherit the old generic unresolved wording.

### Mistral Agentic Search

The prior W34 Evidence card treated the source as locator-only even though a substantive Mistral first-party body had been captured.

Fresh Evidence must consume the first-party article and distinguish supported product architecture/capability claims from maker-reported benchmark claims.

### Amazon Bedrock AgentCore Payments

Consume the AWS first-party GA body. Distinguish actual payment/API/MCP capability, guardrails/observability facts, and any marketing framing.

### Claude Platform Computer Use / Skills API / Files API

Use first-party Anthropic product/documentation authority. Verify what became GA, what tool/API surfaces changed, and any browser/computer-use boundary. Do not collapse distinct availability claims.

### GPT-5.6 Sol pricing update

Use first-party OpenAI pricing/model authority and exact W34 chronology. Preserve the distinction between base model release and the Aug 21 price/access delta.

### Grok Bot chronology

`W34-C066` requires explicit chronology resolution.

Preserved DailyX records an official X observation on `2026-08-21T17:29:36Z` describing access expansion. The current xAI article with the same broad title is now dated Aug 26 and describes a broader expansion.

Evidence must determine whether:

- Aug 21 was a distinct earlier expansion later superseded by Aug 26;
- the page was materially edited/re-dated;
- or the event identity needs split/reclassification.

Do not cite the current Aug 26 article as if it were an Aug 21 exact-body authority.

## 8. Research-paper Evidence depth

For non-DROP arXiv/paper tasks, the Discovery Atom abstract is not a complete Evidence authority.

At minimum, inspect the paper body or an equivalent primary paper source before accepting substantive methodology/result claims.

Evidence claims must separate:

- what the authors built/proposed;
- evaluation design and benchmark scope;
- maker-reported results;
- reproducibility/artifact availability;
- limitations that matter to editorial significance.

Do not promote benchmark numbers merely because they appear in an abstract.

Do not attempt full deep review of papers that Screening legitimately DROPs.

## 9. Evidence Authority Supplement / source binding

Where fresh post-Screening primary authority needs formal binding, use the reviewed Core's Evidence Authority Supplement mechanism or other repository-owned authority mechanism.

Do not hand-edit accepted Evidence authority to bypass task/source-binding rules.

Preserve the previous W34 authority-expansion execution directory as historical evidence; do not overwrite it.

Fresh tasks must be bound to their fresh task identity. Old task bindings do not automatically authorize new Screening/Evidence tasks.

## 10. Authority-consumption ledger for Sol

Create an execution-side reviewable ledger for **every non-DROP Evidence task** with one of these supervisory states:

- `AUTHORITY_NOT_FOUND`
- `AUTHORITY_RETRIEVAL_FAILED`
- `AUTHORITY_CAPTURED_BUT_UNCONSUMED`
- `AUTHORITY_CONSUMED`

For each task record at minimum:

- task ID;
- event/candidate identity;
- Evidence status;
- verification target;
- primary authority locator(s);
- exact captured body/provenance path(s) where available;
- consumption state;
- concise reason;
- whether additional gap fill was attempted;
- number/type of meaningful retrieval attempts;
- whether the candidate appears high-signal enough for Sol exhaustive review.

This ledger is supervisory evidence, not a new Core schema and not a substitute for canonical Evidence.

## 11. Provisional Materiality and Completeness

Run only the Core-owned Materiality and Completeness work required to reach `EVIDENCE_REVIEWED`.

Treat those outputs as provisional.

Do not make or execute Candidate Selection.

The handoff must specifically flag:

- `VERIFIED + CONTEXT/HOLD` combinations;
- high-signal candidates with low materiality caused by Evidence gaps;
- candidates with rich primary bodies but sparse Evidence claims;
- generic limitation patterns repeated across many candidates;
- any extreme compression signal already visible before Selection.

Sol will independently review these before Selection is authorized.

## 12. New execution area

Create exactly one new execution area:

`sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2/`

Before creation verify it does not already exist.

If it exists, do not invent retry/r2/repair names; report and stop.

Do not modify prior Luna execution directories or Sol review records.

## 13. Commit discipline

Use forward-only normal commits and non-force pushes.

Use separate logical checkpoints at minimum for:

1. fresh Screening acceptance/validation;
2. Evidence authority capture/gap-fill and canonical Evidence/Materiality/Completeness regeneration;
3. final Sol Evidence Review handoff, if a distinct metadata commit is genuinely necessary.

Do not create a metadata-only descendant solely to record its own commit SHA.

After every push, fresh remote read-back is mandatory.

Before each write phase, recheck remote branch HEAD against the expected parent SHA. If drift occurs, stop without writing.

## 14. Required final State and stop

Normal final lifecycle:

`EVIDENCE_REVIEWED`

Expected semantic state:

- Discovery = passed;
- Screening = passed;
- Evidence = passed;
- Materiality = passed;
- Completeness = passed;
- Selection = pending;
- Architecture = pending;
- Architecture Review = pending;
- exception gate inactive unless a genuine non-derivable decision is encountered.

The exact State bytes must be generated/validated by Core rather than manually forced.

Then STOP.

Explicit markers:

`DISCOVERY_REVIEW_R2_PASS`

`SELECTION_NOT_AUTHORIZED`

`ARCHITECTURE_NOT_AUTHORIZED`

`SOL_EVIDENCE_REVIEW_REQUIRED`

`SOL_EVIDENCE_REVIEW_READY`

## 15. Required Sol Evidence Review handoff

The handoff must report at minimum:

- Starting SHA/tree and final SHA/tree;
- fresh Screening acceptance path/SHA and Screening counts;
- non-DROP Evidence task count;
- Evidence result counts;
- primary authority bodies attempted/captured;
- meaningful retrieval-attempt distribution, not only a total count;
- consumption-state counts for all non-DROP tasks;
- high-signal `AUTHORITY_NOT_FOUND`, `RETRIEVAL_FAILED`, or `CAPTURED_BUT_UNCONSUMED` rows;
- explicit regression results for ChatGPT for Teens and Mistral Agentic Search;
- results for AgentCore Payments, Claude Platform GA, GPT-5.6 pricing, and Grok Bot chronology;
- paper-level authority coverage for retained research candidates;
- provisional Materiality counts;
- Completeness result;
- major repeated limitation patterns;
- candidates that appear likely to change prior W34 editorial conclusions;
- proof Selection was not executed;
- final Production State path/SHA256;
- remote read-back result.

Normal completion status:

`SOL_EVIDENCE_REVIEW_READY`

## 16. Human and publication boundaries

No Human decision is required in this execution.

Do not:

- manufacture Human review records;
- request Architecture approval;
- run publication sidecars;
- draft reader-facing text;
- build publication PDF;
- freeze or release.

The next decision belongs to Sol's internal Evidence/Materiality review, not Human Architecture Review.
