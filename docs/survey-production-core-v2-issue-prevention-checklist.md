# Survey Production Core v2 — Issue Prevention Checklist

Status: `CANONICAL AGENT/TOOL REVIEW PLAYBOOK`  
Established: 2026-08-22 JST

## 1. Contract

This checklist turns recurring Human Review findings into a compact production playbook for a **ChatGPT-operated** pipeline. Read it with the applicable Research/Profile guidance before advancing each stage.

Ownership vocabulary:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

A failed deterministic or ChatGPT review is repaired and re-run autonomously. It does **not** create a Human Gate. Stop only at Architecture Review, exact-byte Publication Preview, or a genuine Exception Gate where repository authority is insufficient for a safe Owner-level decision.

## 2. Core checks

| Origin | Stage | Primary owner | Required inspection |
|---|---|---|---|
| #166 / broad intake | Source Intake → Completeness | `CHATGPT_RESEARCH_REVIEW` | Explain what search/intake surfaces were exercised, gap-fill performed, negative results, residual uncertainty, and why the issue is READY/LIMITED. Collector success or record count alone is not completeness. |
| AUD-046 / X applicability | Source Intake | `CHATGPT_RESEARCH_REVIEW` + `DETERMINISTIC_TOOL_CHECK` | Weekly must run Grok/X intake. Retrospective/Thematic/Foundations must explicitly decide REQUIRED/NOT_REQUIRED with a substantive rationale. A missing decision is not equivalent to NOT_REQUIRED. |
| AUD-046 / X evidence boundary | Source Intake → Evidence | `CHATGPT_RESEARCH_REVIEW` | Treat Grok/X as Discovery/community-signal input. Do not promote X claims about specifications, benchmark values, dates, licenses or other technical facts directly into publication Evidence without appropriate authoritative verification. |
| AUD-046 / X result disposition | Source Intake → Discovery | `DETERMINISTIC_TOOL_CHECK` + research review | Every required Grok run is imported from its exact Google Drive result into immutable repository Raw, then either bound to named Discovery records or closed as `NO_MATERIAL_DISCOVERY` with rationale. Collected X output may not silently disappear. |
| #166 / silent drop | Materiality → Architecture | `DETERMINISTIC_TOOL_CHECK` | Every material Discovery has a downstream disposition and no selected/material item silently disappears. |
| #191 | Evidence + post-transform | `DETERMINISTIC_TOOL_CHECK` + source reading | Bind technical values/features to the intended subject/component/variant/property; comparator/neighbor values cannot become target facts. Re-run after enrichment/compaction. |
| #139 | Evidence → Draft | `CHATGPT_EDITORIAL_REVIEW` | No generic contentless fallback is presented as a source-backed technical fact. Reduce/omit/HOLD when Evidence is insufficient. |
| #172 | Transform/render | `DETERMINISTIC_TOOL_CHECK` | Preserve canonical URL/path/filename/model/API/command/citation identifiers byte-for-byte. |
| #78 | References | `CHATGPT_EDITORIAL_REVIEW` | Known title/author/date/URL metadata is not degraded to generic placeholder references. |
| #272 | Chronology | `CHATGPT_RESEARCH_REVIEW` | Event type/date is source-backed; unresolved date precision remains unresolved instead of being guessed. |
| #40 / reader boundary | Draft/publication | `CHATGPT_EDITORIAL_REVIEW` | Reader prose may show useful uncertainty/claim boundaries but not internal Candidate/Selection/status/TODO vocabulary. |

## 3. Architecture Review preparation

Before Human Gate 1, ChatGPT must confirm:

- broad research has been compressed visibly into kept/held/excluded/merged material;
- all Profile completeness obligations have a reasoned disposition and residual limitations are explicit;
- X/Grok applicability was explicitly resolved and every required X run has an imported/dispositioned result;
- X-origin leads that became technical claims were primary-source verified under the normal Evidence boundary;
- material candidates have Architecture destinations or explicit omission/exception rationale;
- the Architecture Review Summary exposes enough materiality/completeness information for the Owner to review the proposed issue without replaying the entire pipeline.

Only the final exact Architecture package is a Human Gate input.

## 4. Weekly overlay

| Origin | Primary owner | Required inspection |
|---|---|---|
| AUD-046 / Weekly X lane | `CHATGPT_RESEARCH_REVIEW` | Perform the required Grok/X coverage scan, including targeted media second-pass behavior when needed. A quiet X week is valid; skipping the scan is not. |
| Weekly #9 / `why this issue` | `CHATGPT_EDITORIAL_REVIEW` | Older/background/trend-driven material explains why it belongs in **this** Weekly issue. X momentum may be the current trigger, but the underlying technical event/date remains separately verified. |
| Weekly #9 / Late Breaking | `CHATGPT_EDITORIAL_REVIEW` | Each Late Breaking event has one substantive home; other appearances are compact context/cross-reference. |
| Weekly #9 / Watchlist | `CHATGPT_EDITORIAL_REVIEW` | Watchlist states current observation, uncertainty, and what future evidence would change the assessment; it is not a production TODO list. |
| carry-over | `CHATGPT_RESEARCH_REVIEW` | Every inherited carry-over obligation receives an explicit current-issue disposition. |

A quiet week is valid. Do not manufacture story/source/page quotas.

## 5. Retrospective Period overlay

| Origin | Primary owner | Required inspection |
|---|---|---|
| AUD-046 / Period X decision | `CHATGPT_RESEARCH_REVIEW` | Decide whether community adoption/reproduction/integration signal from X materially helps the bounded retrospective. If not, record why authoritative/historical sources are sufficient for the question. |
| #49 | `DETERMINISTIC_TOOL_CHECK` | Cover/scope/chronology/synthesis structural period labels derive from Profile authority; copied neighboring-period labels are rejected. |
| #272 | `DETERMINISTIC_TOOL_CHECK` + research review | Material chronology events retain compact source mapping and correct event type. |
| #95 | `CHATGPT_EDITORIAL_REVIEW` | Required cross-article retrospective synthesis exists, is Evidence-backed, and survives later transformations. |
| period coverage | `CHATGPT_RESEARCH_REVIEW` | Monthly/Half-year/Annual coverage is not accidentally dominated by one sub-period without an explicit evidence-based reason. |
| coherence | `CHATGPT_RESEARCH_REVIEW` | If one volume cannot responsibly contain the material, use Exception Gate rather than silently deleting/compressing it. |

## 6. Thematic / Foundations overlay

ChatGPT must:

- explicitly decide whether X is material to the current thematic/series-volume research question; do not use X merely to inflate source count;
- when X is required, use question-specific Special runs rather than a generic Weekly Top-10 scan;
- for Foundations, use X only where it materially helps contemporary reception/implementation/frontier questions and never use X to establish historical priority or ancestry;
- expand Source Intake along discovered lineages, actors, competing approaches and counterexamples rather than stopping after the seed query;
- stop expansion by reasoned saturation/closure, not a fixed source count;
- make residual lineage questions explicit;
- distinguish hindsight from unsupported retroactive credit, terminology or ancestry;
- for Foundations volumes, re-read the living series memo and update lineage/volume dependencies/open questions when primary-source work changes the series architecture.

The Foundations series does not gain a routine third Human Gate.

## 7. Publication and visual checks

| Origin | Primary owner | Required inspection |
|---|---|---|
| #50/#54 | `CHATGPT_EDITORIAL_REVIEW` | Internal taxonomy/provenance labels become natural reader-facing labels without mutating underlying identifiers. |
| #140 | `CHATGPT_EDITORIAL_REVIEW` | Repeated boilerplate/low-information notes or references do not dominate pages; compactness must preserve attribution. |
| #271 | `DETERMINISTIC_TOOL_CHECK` | Zero-content optional wrappers/headings/tables are suppressed as a unit. |
| #55 | `CHATGPT_VISUAL_REVIEW` | No URL-only/source-heading-only/final-line-only low-information continuation at the next page top. |
| #40/#55 | `CHATGPT_VISUAL_REVIEW` | No repair-created blank page, isolated whole-page box, or large unnatural whitespace. |
| #122 family | `CHATGPT_VISUAL_REVIEW` | TOC/navigation hierarchy is readable and not dominated by low-value depth. |
| exact-byte release | `DETERMINISTIC_TOOL_CHECK` | Publication Preview approval → Visual Review → Freeze → merge verification → Release preserve identical PDF SHA-256/byte count. |

Before presenting Publication Preview, ChatGPT performs a page-by-page rendered-PDF review. After any source enrichment, compaction or layout repair, repeat the affected semantic and visual checks because previous defects can return.

## 8. Quality tiers

Final quality review rows are classified as:

```text
DETERMINISTIC
AGENT_SEMANTIC
AGENT_VISUAL
```

`DETERMINISTIC` requires an executable result artifact/digest. `AGENT_SEMANTIC` and `AGENT_VISUAL` require concise reasoned evidence tied to the exact source/PDF revision. Required rows are derived from Core + Research Profile + Publication Profile; inapplicable checks are not ceremonial PASS rows.

## 9. When a new finding appears

1. repair the current edition safely;
2. classify whether it is edition-local or reusable;
3. repair the narrowest correct shared layer when reusable;
4. add a deterministic regression only if the failure has crisp deterministic semantics;
5. otherwise update this checklist/Profile guidance so future ChatGPT sessions explicitly inspect it;
6. re-run interacting checks, not only the newest symptom.

Frozen historical releases remain immutable. The full historical rationale remains in `docs/survey-production-core-v2-historical-invariants.md` and `docs/survey-production-core-v2-historical-production-deep-audit.md`.
