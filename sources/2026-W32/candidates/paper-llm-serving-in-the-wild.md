---
candidate_id: paper-llm-serving-in-the-wild
issue_id: "2026-W32"
title: "LLM Serving in the Wild: An Empirical Study of Frameworks, Methods, and System Designs"
record_type: paper-screening-record
status: candidate
discovered_via: [manual-paper-scan]
published_at: "2026-08-04"
verification_status: abstract-screened
---

# LLM Serving in the Wild — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.03036
- Authors: Forough Majidi, Mohammad Mehdi Morovati, Foutse Khomh, Heng Li

## Collected abstract-level information
The paper empirically studies adoption of five LLM-serving frameworks in open-source systems: vLLM, SGLang, TensorRT-LLM, LMDeploy and FlashInfer. It examines framework combinations, serving-method categories, model families, modalities, sizes, deployment settings and repository architectures.

## Author-reported findings
- vLLM is reported as the most visible framework by popularity and adoption.
- Parallel computation, memory management and network pruning are reported as common serving-method categories.
- Multi-framework usage is described as limited; most projects rely primarily on one serving framework.
- Serving frameworks appear across reasoning/RL workloads, multimodal generation and understanding, microservices and cloud infrastructure.

## Verification boundary
Abstract-screened only. Dataset construction, repository sampling, coding methodology and quantitative tables still require paper-level review.

## Screening note
Keep in the inference / serving paper inventory.