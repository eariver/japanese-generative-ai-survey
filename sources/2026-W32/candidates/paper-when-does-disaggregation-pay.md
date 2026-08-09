---
candidate_id: paper-when-does-disaggregation-pay
issue_id: "2026-W32"
title: "When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference"
record_type: paper-screening-record
status: candidate-reviewed
discovered_via: [manual-paper-scan]
published_at: "2026-08-04"
verification_status: full-paper-reviewed
evidence_record: "../evidence/papers/when-does-disaggregation-pay.md"
---

# When Does Disaggregation Pay? — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.03741
- Authors: Przemyslaw Forys, Haoran Wu, Can Xiao, Jiayi Nie, Tony Liu, Rika Antonova, Timothy Jones, Robert Mullins, Wayne Luk, Aaron Zhao, George A. Constantinides

## Full-review resolution
Full-paper evidence is recorded in `../evidence/papers/when-does-disaggregation-pay.md`.

The full paper materially qualifies the abstract-level throughput headline:
- the results are simulation-based;
- simulator validation is component-level on an 8×B200 system, not end-to-end serving validation;
- disaggregation can lose to unified serving for decode-heavy or balanced workloads;
- the strongest four-way PDAF gains rely on hardware specialization not generally available in current GPU catalogues;
- stage-wise quantization sensitivity changes by task in the paper's limited one-model/two-task study.

## Screening state
Retain as a reviewed Inference/Serving systems candidate. Its editorial value is the conditional design rule—**when disaggregation pays**—rather than a universal throughput-improvement number.