---
candidate_id: paper-when-does-disaggregation-pay
issue_id: "2026-W32"
title: "When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference"
record_type: paper-screening-record
status: candidate
discovered_via: [manual-paper-scan]
published_at: "2026-08-04"
verification_status: abstract-screened
---

# When Does Disaggregation Pay? — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.03741
- Authors: Przemyslaw Forys, Haoran Wu, Can Xiao, Jiayi Nie, Tony Liu, Rika Antonova, Timothy Jones, Robert Mullins, Wayne Luk, Aaron Zhao, George A. Constantinides

## Collected abstract-level information
The paper studies heterogeneous and disaggregated serving for agentic LLM inference, separating prefill, decode, attention and FFN workloads. It introduces `HeteroPanacea`, a simulation framework spanning disaggregated quantization, intra/inter-device parallelization scheduling and PDAF NPU heterogeneity.

## Author-reported results
- The authors report up to 75% throughput improvement from prefill/decode disaggregation versus traditional serving with current GPUs in their simulations.
- They report four-way Prefill/Decode/Attention/FFN disaggregation as the most consistently throughput-improving configuration under custom-NPU assumptions.

## Verification boundary
These are simulation-based author claims from the abstract. Workload assumptions, hardware models, network costs and sensitivity analyses require full-paper review before editorial use.

## Screening note
Keep in the inference-systems paper inventory, especially for the agentic serving / heterogeneous hardware theme.