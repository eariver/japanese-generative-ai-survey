---
candidate_id: paper-sparseety
issue_id: "2026-W32"
title: "SparSEEty: Extracting Tokens from Sparsity-Exploiting LLM Serving Systems via Deterministic Side Channels"
record_type: paper-screening-record
status: candidate
discovered_via: [manual-paper-scan]
published_at: "2026-08-04"
verification_status: abstract-screened
---

# SparSEEty — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.02995
- Authors: Yongwan Jo, Jinyoung Park, Euihyun Lee, Dokyung Song

## Collected abstract-level information
The paper studies a side channel created when sparsity-exploiting LLM serving systems skip weight accesses for inactive neurons. `SparSEEty` constructs a neuron-activation oracle from weight-access side channels and attempts to invert activation traces back into input/output tokens.

The authors instantiate the attack against an LLM-serving system inside an Intel TDX confidential VM.

## Author-reported results
- Prompt and response reconstruction with BLEU scores above 0.95 across evaluated models/datasets.
- Monitoring overhead reported between 3.7% and 7.2%.

## Verification boundary
Abstract-screened only. Threat model, attacker prerequisites, exact hardware/serving implementation, leakage channel and robustness across workloads require full-paper review.

## Screening note
Keep in the inference / safety / side-channel paper inventory.