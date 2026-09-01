---
candidate_id: paper-llm-serving-in-the-wild
issue_id: "2026-W32"
title: "LLM Serving in the Wild: An Empirical Study of Frameworks, Methods, and System Designs"
record_type: paper-screening-record
status: candidate-reviewed
discovered_via: [manual-paper-scan]
published_at: "2026-08-04"
verification_status: targeted-full-paper-reviewed
evidence_record: "../evidence/papers/llm-serving-in-the-wild.md"
---

# LLM Serving in the Wild — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.03036
- Authors: Forough Majidi, Mohammad Mehdi Morovati, Foutse Khomh, Heng Li

## Full-review resolution
Targeted full-paper evidence is recorded in `../evidence/papers/llm-serving-in-the-wild.md`.

The study is best interpreted as a public-OSS adoption snapshot, not a serving-performance benchmark or market-share report.

Important boundaries established by review:
- analysis is restricted to Python and public GitHub repositories;
- framework use is inferred from official API/import usage and filtered repository mining;
- filtered unique-repository counts are not production market share;
- popularity by stars/forks and observed adoption differ materially in the sample;
- repositories often combine serving methods/frameworks rather than using isolated optimizations.

## Screening state
Retain as a reviewed Serving/Inference empirical candidate, likely valuable as context/synthesis evidence. Quantitative repository counts must retain the study's sampling/filtering scope.