---
candidate_id: kimi-k3
issue_id: "2026-W32"
title: "Kimi K3"
record_type: screening-record
status: candidate
discovered_via: [grok-v0.4, primary-source-screening, reaction-pass]
event_date: "2026-07"
verification_status: primary-screened
---

# Kimi K3 — Screening Record

## Collected information
- Moonshot's official model card describes Kimi K3 as an open-weight native multimodal agentic model.
- The model card reports 2.8T total parameters, 104B activated parameters and a 1,048,576-token context length.
- The official repository documents native text/image/video understanding, MXFP4 weights / MXFP8 activations and deployment paths including vLLM, SGLang and TokenSpeed.
- The model artifacts are approximately 1.56 TB in the official Hugging Face repository.

## Primary sources
- https://huggingface.co/moonshotai/Kimi-K3/blob/main/README.md

## Existing evidence
- Technical: `sources/2026-W32/evidence/technical/verified-candidates-v0.1.md`
- Social: `sources/2026-W32/evidence/social/x-community-reaction-normalized-v0.1.md`

## Community reaction collected
- A pre-cutoff viral post claimed an experimental pure-C99 implementation could stream experts from disk and run with about 8.24 GB peak RAM.
- Post-cutoff discussion emphasized large disk requirements and extremely low throughput.

## Unverified / pending
- Reproduction of the pure-C implementation before treating the 8.24 GB RAM figure, correctness or token speed as technical facts.
- Exact release timestamp if chronology needs finer than month-level precision.

## Screening note
Keep as a candidate. Separate official model facts from the community low-resource-inference experiment.