---
candidate_id: paper-prweaver
issue_id: "2026-W32"
title: "PRWeaver: Evaluating LLM-Based Code Auditors against Long-Horizon Malicious Pull Requests"
record_type: paper-screening-record
status: candidate
discovered_via: [manual-paper-scan]
published_at: "2026-08-03"
verification_status: abstract-screened
---

# PRWeaver — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.02693
- Authors: Yuekun Wang, Mingfei Cheng, Xiaofei Xie

## Collected abstract-level information
PRWeaver is a benchmark for LLM-based pull-request auditors under malicious changes spread across repository evolution. The paper reports 208 execution-validated attacks from ten real-world repositories, rendered under four matched review settings for 832 total renderings.

## Author-reported results
- Attack decomposition alone changes detection by at most five percentage points across evaluated systems.
- Per-PR interleaving at N=16 and coherent carrier fusion reduce detection by 5–13 and 10–18 points respectively.
- Whole-window review at N=24 is reported at 16–22% detection versus 50–60% under per-PR review.

## Verification boundary
Abstract-screened only. Benchmark construction, attack validity, auditor configurations, model versions and statistical treatment require full-paper review.

## Screening note
Keep in coding-agent / security / evaluation paper inventory.