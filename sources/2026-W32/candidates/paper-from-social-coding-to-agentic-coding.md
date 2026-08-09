---
candidate_id: paper-from-social-coding-to-agentic-coding
issue_id: "2026-W32"
title: "From Social Coding to Agentic Coding: Productivity and Relational Reconfiguration in Open-Source Communities"
record_type: paper-screening-record
status: candidate-reviewed
discovered_via: [manual-paper-scan]
published_at: "2026-08-04"
verification_status: full-paper-reviewed
evidence_record: "../evidence/papers/from-social-coding-to-agentic-coding.md"
---

# From Social Coding to Agentic Coding — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.03585
- Authors: Mengying Zhou, Yongjie Yin, Yang Chen

## Full-review resolution
Full-paper evidence is recorded in `../evidence/papers/from-social-coding-to-agentic-coding.md`.

The decisive interpretation boundary is that this is a **data-grounded LLM multi-agent simulation, not a field experiment**.

The simulator uses 1,084 selected historical GitHub developers, replays recent real activity as warmup and branches into coding-agent and no-coding-agent counterfactual conditions. The authors report higher simulated productivity, uneven agent adoption, a shift from direct human work toward agent-mediated work, and sharply lower retrievability of the simulated public knowledge corpus.

However, those differences are causal results only **inside the simulator**. The paper itself states that implications beyond the simulated OSS setting remain hypotheses.

## Screening state
Retain as a reviewed socio-technical Coding-Agent candidate. If used, every quantitative result must be explicitly framed as simulation output rather than measured productivity/collaboration change in real OSS communities.