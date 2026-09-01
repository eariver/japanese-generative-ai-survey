# Survey Production Core v2 — Issue Prevention Checklist

Status: `CANONICAL AGENT/TOOL REVIEW PLAYBOOK`  
Established: 2026-08-22 JST

## 1. Contract

This checklist turns recurring Human Review findings and clarified production requirements into a compact production playbook for a **ChatGPT-operated** pipeline. Read it with the applicable Research/Profile guidance before advancing each stage.

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

A failed deterministic or ChatGPT review is repaired and re-run autonomously. It does **not** create a Human Gate. Stop only at Architecture Review, exact-byte Publication Preview, a genuine Owner-level Exception Gate, or unavoidable manual Grok instruction/result transport when external Grok execution cannot be performed directly.

**Stop-discipline invariant (AUD-047):** do not ask for routine confirmation between internal stages. Source Intake, Screening, Evidence, Completeness/materiality, Selection, Architecture preparation, drafting/synthesis, deterministic QA, semantic/visual repair, CI retry, tool repair, Drive result import, and continuation after a returned Grok result proceed autonomously toward the requested Gate.

## 2. Core checks

| Origin | Stage | Primary owner | Required inspection |
|---|---|---|---|
| #166 / broad intake | Source Intake → Completeness | `CHATGPT_RESEARCH_REVIEW` | Explain what search/intake surfaces were exercised, gap-fill performed, negative results, residual uncertainty, and why the issue is READY/LIMITED. Collector success or record count alone is not completeness. |
| AUD-046 / X applicability | Source Intake | `CHATGPT_RESEARCH_REVIEW` | Weekly must run Grok/X. Period/Thematic must record explicit REQUIRED/NOT_REQUIRED rationale. Foundations uses its dedicated Drive category when X is material. |
| AUD-046 / X evidence boundary | Source Intake → Evidence | `CHATGPT_RESEARCH_REVIEW` | Grok/X is community-signal/Discovery input. Specifications, benchmark values, dates, licenses, historical priority and similar technical claims require authoritative verification before Evidence acceptance. |
| AUD-046 / X result disposition | Source Intake → Discovery | `DETERMINISTIC_TOOL_CHECK` | Exact returned Drive bytes are imported to Raw and every required Grok result is either bound to Discovery or explicitly closed as `NO_MATERIAL_DISCOVERY`; no collected X run silently disappears. |
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
- material candidates have Architecture destinations or explicit omission/exception rationale;
- the Architecture Review Summary exposes enough materiality/completeness information for the Owner to review the proposed issue without replaying the entire pipeline.

Only the final exact Architecture package is a Human Gate input.

## 4. Weekly overlay

| Origin | Primary owner | Required inspection |
|---|---|---|
| Weekly #9 / `why this issue` | `CHATGPT_EDITORIAL_REVIEW` | Older/background/trend-driven material explains why it belongs in **this** Weekly issue. |
| Weekly #9 / Late Breaking | `CHATGPT_EDITORIAL_REVIEW` | Each Late Breaking event has one substantive home; other appearances are compact context/cross-reference. |
| Weekly #9 / Watchlist | `CHATGPT_EDITORIAL_REVIEW` | Watchlist states current observation, uncertainty, and what future evidence would change the assessment; it is not a production TODO list. |
| carry-over | `CHATGPT_RESEARCH_REVIEW` | Every inherited carry-over obligation receives an explicit current-issue disposition. |

A quiet week is valid. Do not manufacture story/source/page quotas.

## 5. Retrospective Period overlay

| Origin | Primary owner | Required inspection |
|---|---|---|
| #49 | `DETERMINISTIC_TOOL_CHECK` | Cover/scope/chronology/synthesis structural period labels derive from Profile authority; copied neighboring-period labels are rejected. |
| #272 | `DETERMINISTIC_TOOL_CHECK` + research review | Material chronology events retain compact source mapping and correct event type. |
| #95 | `CHATGPT_EDITORIAL_REVIEW` | Required cross-article retrospective synthesis exists, is Evidence-backed, and survives later transformations. |
| period coverage | `CHATGPT_RESEARCH_REVIEW` | Monthly/Half-year/Annual coverage is not accidentally dominated by one sub-period without an explicit evidence-based reason. |
| coherence | `CHATGPT_RESEARCH_REVIEW` | If one volume cannot responsibly contain the material, use Exception Gate rather than silently deleting/compressing it. |

## 6. Thematic / Foundations overlay

ChatGPT must:

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

Before presenting Publication Preview, ChatGPT performs a page-by-page rendered-PDF review. After any source enrichment, compaction or layout repair, repeat affected semantic and visual checks because previous defects can return.

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
6. re-run interacting checks, not only the newest symptom;
7. after repair, continue toward the requested Gate rather than turning the finding itself into a routine stop.

Frozen historical releases remain immutable. The full historical rationale remains in `docs/survey-production-core-v2-historical-invariants.md` and `docs/survey-production-core-v2-historical-production-deep-audit.md`.
