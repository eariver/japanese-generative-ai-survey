---
candidate_id: paper-livemem
issue_id: "2026-W32"
title: "LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference"
record_type: paper-screening-record
status: candidate-reviewed
discovered_via: [manual-paper-scan]
published_at: "2026-08-03"
verification_status: full-paper-reviewed
evidence_record: "../evidence/papers/livemem.md"
---

# LiveMem — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.02515
- Authors: Zhichen Liu, Ruihan Sun, Hengjie Yang, Zipeng Wu, Zhaohan Chen, Xiaofan Zhang, Yang Xu

## Full-review resolution
Full-paper evidence is recorded in `../evidence/papers/livemem.md`.

The paper's strongest editorially useful idea is **state continuity under context turnover**: a fixed-size recurrent state persists while old KV pages leave the active attention window.

Important boundaries established by full review:
- LiveMem is a lossy latent state, not an exact archive.
- It does not reliably recover arbitrary token-level needles once their KV entries are gone.
- Retrieval/external storage remains complementary for exact recall.
- The demonstrated implementation still has the backbone's finite positional horizon; it is not literal unlimited context.
- Aggregate benchmark results favor LiveMem-RL in the authors' setup, but other approaches win individual tasks.

## Screening state
Retain as a reviewed Memory / continual-inference candidate. It is now comparison-ready, with quantitative claims governed by the evidence record rather than the original abstract summary.