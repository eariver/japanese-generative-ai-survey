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

## X / Grok trend sensing

Grok is used as an **X trend sensor**, not as factual evidence by itself.

The important distinction is between:

- when an underlying model / paper / OSS release occurred, and
- when the technical community on X actually began discussing, testing, reproducing, disputing, or integrating it.

Current prompts:

- [X Trend Sensor v0.1](config/prompts/grok/x-trend-sensor-v0.1.md)
- [X Trend Sensor v0.2](config/prompts/grok/x-trend-sensor-v0.2.md)

v0.2 explicitly separates release / publication dates from `X Momentum Started`, `X Peak`, and `Why Now`.

Grok output is treated as a **Trend Candidate List** and must be verified against primary or otherwise clearly classified sources before important technical claims are published.

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
│     ├─ screening.md
│     ├─ evidence.md
│     ├─ synthesis.md
│     └─ citation-review.md
├─ sources/
│  └─ <issue>/
│     ├─ manifest.yaml
│     ├─ grok/raw/
│     └─ evidence/
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

Directories will be added when they acquire real files; empty placeholder trees are intentionally avoided.

## Current phase

Current work is Phase 0–1:

- establish repository and editorial policy
- refine X / Grok trend collection
- manually collect candidate sources
- build Evidence Cards
- compile the first Japanese weekly survey PoC
- then introduce LuaLaTeX / LuaTeX-ja and a reproducible GitHub Actions PDF build

Later phases will add automated source collection, schema-constrained evidence extraction, scheduled weekly PR generation, and monthly / annual synthesis.

## Design principle

> AI に「文章を書かせる」システムではなく、AI に「根拠を追跡可能な Technical Survey を構築させる」システムにする。
