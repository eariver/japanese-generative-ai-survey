# japanese-generative-ai-survey

Evidence-first Japanese weekly technical survey for generative AI, built with LLMs, LaTeX, and reproducible source tracking.

## Overview

This repository is the Source of Truth for a Japanese-language weekly technical survey / magazine covering current developments in:

- Large Language Models
- Reasoning Models
- AI Agents / Coding Agents / Agent Harness
- Inference / Serving
- Multimodal AI
- Image / Video / Audio Generation
- Open Weight Models / Local AI
- Long-term Memory / Multi-Agent Systems
- Evaluation / Benchmarks
- AI Safety / Agent Security

The project does **not** aim to have an LLM write an unchecked AI-news digest.

Its core approach is:

```text
Source Collection
    -> Screening
    -> Evidence
    -> Cross-source Synthesis
    -> Japanese Drafting
    -> Claim / Citation Validation
    -> LaTeX
    -> Reproducible PDF
```

Core priority:

```text
Correctness > Traceability > Coverage > Speed
```

## Weekly cycle

The standard editorial cutoff is:

```text
Friday 18:00 America/New_York
```

Compilation is normally performed in Japan on Saturday after that cutoff, so the finished issue can be read over the weekend.

The collection window is not forced to an exact seven-day / 168-hour interval. Operationally it should cover:

```text
previous successful collection time
    -> current collection time
```

This prevents missed items when compilation timing shifts.

See [Editorial Specification](docs/editorial-specification.md) for the authoritative v0.1 rules.

## X / Grok sensing

Grok is used as an **X sensor**, not as factual evidence by itself.

The workflow separates two different Grok passes:

1. **Trend discovery** — detect what became technically important on X and when momentum arose.
2. **Community reaction evidence** — for selected topics, collect representative X posts with auditable URLs showing what researchers, engineers, OSS developers, local-AI users, and other technical actors actually tested, praised, questioned, reproduced, or criticized.

The important distinction is between:

- when an underlying model / paper / OSS release occurred,
- when the technical community on X actually began discussing, testing, reproducing, disputing, or integrating it, and
- what concrete community reactions can be traced to actual X posts.

### Trend prompt history

- [X Trend Sensor v0.1](config/prompts/grok/x-trend-sensor-v0.1.md)
- [X Trend Sensor v0.2](config/prompts/grok/x-trend-sensor-v0.2.md) — first live observation prompt; separates release / publication dates from `X Momentum Started`, `X Peak`, and `Why Now`
- [X Trend Sensor v0.3](config/prompts/grok/x-trend-sensor-v0.3.md) — requires the final Raw Observation to be delivered as an actual Markdown file rather than pasted into chat
- [X Trend Sensor v0.4](config/prompts/grok/x-trend-sensor-v0.4.md) — **current trend-discovery prompt**; adds `Coverage Scan -> Candidate Pool -> Global Ranking -> Coverage Audit`, including mandatory second-pass checks for multimodal / image / video / audio topics before final ranking

### Community reaction prompt

- [X Community Reaction Evidence Collector v0.1](config/prompts/grok/x-community-reaction-evidence-v0.1.md) — **current reaction-evidence prompt**; requires real X post URLs, independent-post checks, active search for skepticism / limitations, and explicit `INSUFFICIENT_X_EVIDENCE` when community reaction cannot be substantiated.

Because the standard Grok GitHub connector is treated as read-only for this workflow, Grok should not attempt to push observations itself. It should generate and present a `.md` file; that file is then transferred unchanged into the appropriate `sources/<issue>/grok/` path by a write-capable tool or agent.

Trend output is treated as a **Trend Candidate List** and must be verified against primary or otherwise clearly classified sources before important technical claims are published.

Reaction output is treated as **Social Observation Evidence**. It may support statements such as "X上ではこの観点が議論された" but must not be used by itself to establish technical facts such as benchmark scores, release dates, model sizes, licenses, or hardware requirements.

Run-specific instructions may be placed under `config/prompts/grok/runs/`. They can override observation windows, target topics, or output filenames without changing the normal filename convention in the main prompts.

## Planned weekly magazine structure

Initial structure:

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

Initial page budget is approximately **16 pages**, with a provisional maximum of approximately **24 pages**. Weak weeks should not be padded merely to fill the target.

## Chronology

The project also intends to maintain an AI / model chronology generated from the same underlying event data used by the survey.

The chronology and weekly survey have different roles:

- **Chronology:** objective artifact / event history.
- **Weekly survey:** what became technically important during a given observation period.

For example, a model may be released on one date but become a major weekly topic several days later when weights, quantizations, serving support, benchmarks, or integrations appear.

## Repository direction

Planned structure as the project develops:

```text
japanese-generative-ai-survey/
├─ README.md
├─ docs/
│  └─ editorial-specification.md
├─ config/
│  ├─ topics.yaml
│  ├─ source_policy.yaml
│  ├─ survey_policy.md
│  └─ prompts/
│     ├─ grok/
│     │  └─ runs/
│     ├─ screening.md
│     ├─ evidence.md
│     ├─ synthesis.md
│     └─ citation-review.md
├─ sources/
│  └─ <issue>/
│     ├─ manifest.yaml
│     ├─ grok/
│     │  ├─ raw/                  # trend-discovery Raw Observations
│     │  └─ reactions/
│     │     └─ raw/               # focused X Community Reaction collections
│     └─ evidence/                # verified technical Evidence Cards
├─ chronology/
│  └─ events.yaml
├─ surveys/
│  ├─ weekly/
│  ├─ monthly/
│  └─ annual/
├─ schemas/
├─ scripts/
├─ templates/
│  └─ survey/
└─ .github/workflows/
```

Existing trend Raw files remain in `sources/<issue>/grok/raw/` to preserve provenance. They are not moved merely to make the tree more symmetrical.

Directories will be added when they acquire real files; empty placeholder trees are intentionally avoided.

## Current phase

Current work is Phase 0–1:

- establish repository and editorial policy
- refine X / Grok trend collection
- collect auditable X community reaction evidence
- manually collect and verify candidate sources
- build Evidence Cards
- compile the first Japanese weekly survey PoC
- then introduce LuaLaTeX / LuaTeX-ja and a reproducible GitHub Actions PDF build

Later phases will add automated source collection, schema-constrained evidence extraction, scheduled weekly PR generation, and monthly / annual synthesis.

## Design principle

> AI に「文章を書かせる」システムではなく、AI に「根拠を追跡可能な Technical Survey を構築させる」システムにする。
