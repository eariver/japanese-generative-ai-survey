---
candidate_id: paper-sparseety
issue_id: "2026-W32"
title: "SparSEEty: Extracting Tokens from Sparsity-Exploiting LLM Serving Systems via Deterministic Side Channels"
record_type: paper-screening-record
status: candidate-reviewed
discovered_via: [manual-paper-scan]
published_at: "2026-08-04"
verification_status: full-paper-reviewed
evidence_record: "../evidence/papers/sparseety.md"
---

# SparSEEty — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.02995
- Authors: Yongwan Jo, Jinyoung Park, Euihyun Lee, Dokyung Song

## Full-review resolution
Full-paper evidence is recorded in `../evidence/papers/sparseety.md`.

The paper demonstrates a concrete efficiency–confidentiality interaction: in the authors' PowerInfer/Intel-TDX-style setting, sparse input-dependent weight access can expose host-observable patterns that support token reconstruction.

Important boundaries established by review:
- this is architecture/threat-model specific, not a generic break of TDX or all sparse LLM serving;
- the strongest reconstruction results depend on the available observation channel;
- `100 monitored neurons` is a result of the primary tested setup, not a universal threshold;
- private-LoRA and CPU-offload-only variants show materially different attack quality;
- mitigation can trade away the sparsity/efficiency benefit or require costly access-pattern hiding.

## Screening state
Retain as a reviewed Serving/Safety candidate. Its significance is cross-layer: an inference optimization can create a confidentiality side channel.