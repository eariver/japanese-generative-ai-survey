---
candidate_id: paper-prweaver
issue_id: "2026-W32"
title: "PRWeaver: Evaluating LLM-Based Code Auditors against Long-Horizon Malicious Pull Requests"
record_type: paper-screening-record
status: candidate-reviewed
discovered_via: [manual-paper-scan]
published_at: "2026-08-03"
verification_status: full-paper-reviewed
evidence_record: "../evidence/papers/prweaver.md"
---

# PRWeaver — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.02693
- Authors: Yuekun Wang, Mingfei Cheng, Xiaofei Xie

## Full-review resolution
Full-paper evidence is recorded in `../evidence/papers/prweaver.md`.

Review materially sharpens the abstract claim:
- simple decomposition across PRs has only a small reported effect;
- benign interleaving and semantically coherent carrier fusion degrade detection more;
- the steepest degradation appears when benign and malicious changes jointly occupy the active review window;
- hiding repository history has a smaller effect, so the paper is better read as a review-context/workflow boundary than as evidence that history access is useless.

The benchmark contains 208 execution-validated attacks / 832 renderings across 10 repositories and is heavily Python-skewed. All detection rates remain benchmark-specific author-reported results.

## Screening state
Retain as a reviewed Coding-Agent / Security candidate. The strongest editorial angle is that review-window composition and harness behavior are security properties of LLM code auditors.