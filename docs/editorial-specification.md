# Weekly Generative AI Technical Survey — Editorial Specification

Version: v0.1  
Status: Initial authority for Phase 0–1  
Established: 2026-08-09

## 1. Purpose

This project produces a Japanese weekly technical survey / magazine for following current developments in LLMs, generative AI, agents, multimodal systems, inference, open-weight models, local AI, evaluation, and AI safety.

The publication is not intended to be a generic AI-news digest. It is an evidence-first technical review whose claims remain traceable to primary or otherwise clearly classified sources.

Core priority:

```text
Correctness > Traceability > Coverage > Speed
```

The publication should remain readable as a weekend technical magazine while preserving enough provenance to reconstruct where each factual statement originated.

## 2. Weekly editorial cycle

### 2.1 Editorial cutoff

The standard editorial cutoff is:

```text
Friday 18:00 America/New_York
```

`America/New_York` is used instead of a fixed EST offset so daylight-saving time is handled correctly.

Typical conversion to Japan time:

- EDT period: Saturday 07:00 JST
- EST period: Saturday 08:00 JST

Compilation is normally performed on Saturday in Japan after the cutoff so the finished issue can be read over the weekend.

### 2.2 Collection window

The source-collection window is intentionally not defined as an exact 168-hour period.

Operationally, the preferred window is:

```text
previous successful collection time
    -> current collection time
```

This avoids losing information when compilation is delayed or performed earlier/later than usual.

The editorial cutoff and the collection window therefore serve different purposes:

- **Editorial cutoff** determines the normal boundary of the issue.
- **Collection window** prevents missed observations between runs.

### 2.3 Issue identifier

Weekly issues may use identifiers such as:

```text
2026-W32
```

The identifier is an edition label. It does not imply that the contents are restricted to an exact ISO Monday-to-Sunday interval.

## 3. Time model

The project must distinguish at least the following time concepts.

### 3.1 Artifact / source event time

Examples:

- model announcement
- model release
- API preview / GA
- weights release
- paper publication
- GitHub release
- product integration
- deprecation / retirement

Representative fields:

```yaml
event_type:
event_date:
source_published_at:
observed_at:
```

### 3.2 X trend time

The date of a release and the date on which the technical community begins discussing it are not the same thing.

For X-derived trend candidates, keep separate fields such as:

```yaml
x_momentum_started_at:
x_peak_at:
x_activity_persistence:
x_observed_at:
why_now:
```

A topic may belong in the current weekly issue even when its underlying release occurred before the current editorial period, if meaningful technical attention emerged during the current observation window.

Conversely, a product released inside the period does not automatically deserve prominent coverage if there is little technical significance or community engagement.

## 4. Late Breaking

Information that becomes significant after the Friday 18:00 America/New_York cutoff may be listed in a small **Late Breaking** section when omission would make the issue misleading or immediately stale.

Late Breaking items should normally receive only brief treatment. Full verification and analysis should roll into the following issue when appropriate.

## 5. Page budget

Initial target:

```text
approximately 16 pages
maximum approximately 24 pages
```

This is provisional until one or more real issues are compiled.

References, source notes, or appendices may cause minor variation. The magazine should not inflate weak weeks merely to fill pages.

## 6. Initial magazine structure

The v0.1 structure is:

1. Cover
2. Contents
3. This Week in AI
4. Lead Stories
5. Model & Reasoning
6. Agent & Coding
7. Multimodal
8. Inference / Serving
9. Open Weight / Local AI
10. Research Paper Watch
11. OSS & GitHub Watch
12. X Community Watch
13. Deep Dive
14. Watchlist
15. References / Source Notes

Sections are optional when there is insufficient material. Editorial balance should reflect the week rather than artificially equalize categories.

## 7. Article types

Candidate article types include:

```text
LEAD
NEWS
PAPER_REVIEW
DEEP_DIVE
RELEASE
OSS
X_COMMUNITY
WATCHLIST
LATE_BREAKING
```

These are editorial classifications and are distinct from source classifications.

## 8. Source hierarchy and evidence-first policy

Preferred source classes include:

```text
PAPER
PREPRINT
OFFICIAL_MODEL_ANNOUNCEMENT
OFFICIAL_DOCUMENTATION
OFFICIAL_GITHUB
GITHUB_RELEASE
COMPANY_BLOG
INDEPENDENT_BENCHMARK
NEWS
SOCIAL_MEDIA
UNVERIFIED
```

Primary sources and credible independent evaluations should be preferred for factual claims.

The pipeline is conceptually:

```text
Source Collection
    -> Screening
    -> Source Manifest
    -> Evidence Extraction
    -> Evidence Store
    -> Topic Classification
    -> Cross-source Comparison
    -> Japanese Drafting
    -> Claim / Citation Validation
    -> LaTeX
    -> PDF
```

The survey should not introduce specific numerical or technical claims that are absent from the verified evidence layer unless they are explicitly marked as editorial interpretation or inference.

## 9. X / Grok policy

Grok is used as an **X trend sensor**, not as a factual authority.

Its purpose is to answer questions such as:

- What became technically important on X during the observation window?
- When did attention begin to build?
- When did it peak?
- Why did the topic become important at that particular time?
- What were practitioners testing, disputing, reproducing, or integrating?

Grok output is treated as a **Trend Candidate List**.

Conceptual flow:

```text
Grok / X raw observation
    -> Trend Candidate
    -> Primary-source verification
    -> Evidence Card
    -> Article Candidate
```

Raw Grok responses should be preserved for provenance when used in an issue, but should not be cited as sole support for important technical facts.

Representative X posts may be used to characterize community reaction, provided that community reaction is clearly distinguished from verified model capability or benchmark evidence.

## 10. Chronology

The project should maintain a reusable model / AI-event chronology alongside the weekly publication.

The chronology and the weekly magazine serve different purposes:

- **Chronology:** objective artifact and event history.
- **Weekly magazine:** what became technically important during a particular observation period.

The same artifact may therefore have multiple events, for example:

```yaml
artifact_id: example-model

events:
  - type: MODEL_ANNOUNCEMENT
    date: ...
  - type: MODEL_RELEASE
    date: ...
  - type: WEIGHTS_RELEASE
    date: ...
  - type: API_GA
    date: ...
  - type: MODEL_RETIREMENT
    date: ...
```

Initial event types include:

```text
MODEL_ANNOUNCEMENT
MODEL_RELEASE
MODEL_UPDATE
API_PREVIEW
API_GA
OPEN_WEIGHT
WEIGHTS_RELEASE
PRODUCT_INTEGRATION
INTEGRATION_GA
AGENT_RELEASE
FRAMEWORK_RELEASE
BENCHMARK_PUBLICATION
PAPER_PUBLICATION
MODEL_RETIREMENT
DEFAULT_ALIAS_SWITCH
PRODUCT_DEPRECATION
SECURITY_POLICY_CHANGE
```

X momentum timestamps are generally not chronology events; they belong to trend observation data.

## 11. Citation and attribution principles

1. Concrete numerical claims require a supporting source.
2. Performance comparisons require source and evaluation context.
3. Author / vendor claims must be distinguished from independent evaluation.
4. Terms such as “SOTA”, “best”, or “world-leading” require attribution.
5. Primary sources are preferred.
6. Secondary-only sourcing must be labeled when unavoidable.
7. A citation must actually support the claim it is attached to.
8. Unknown details must not be filled in by an LLM as if known.
9. Benchmark comparisons must account for differences in harness, prompt, generation settings, backend, benchmark version, and other material conditions.

## 12. Human review

Initial workflow:

```text
LLM-assisted collection / drafting
    -> human / independent review
    -> validation
    -> merge
    -> PDF
```

The initial phases intentionally avoid unattended automatic public release.

## 13. Current project phase

Current scope is Phase 0–1:

- repository and policy establishment
- editorial specification
- Grok X trend sensor prompt development
- manual source collection
- evidence-card PoC
- Japanese weekly survey PoC
- later: LuaLaTeX template and reproducible GitHub Actions PDF build

Automated arXiv / OpenReview collection, API-driven evidence extraction, fully automatic weekly PR generation, and monthly / annual synthesis remain later phases.

## 14. Design principle

The project is not primarily a system for making an AI write prose.

It is a system for making AI help construct a **traceable, evidence-backed Japanese technical survey** whose source history, editorial decisions, and generation process can be inspected and reproduced.
