---
candidate_id: paper-livemem
issue_id: "2026-W32"
title: "LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference"
record_type: paper-screening-record
status: candidate
discovered_via: [manual-paper-scan]
published_at: "2026-08-03"
verification_status: abstract-screened
---

# LiveMem — Paper Screening Record

## Bibliographic source
- arXiv: https://arxiv.org/abs/2608.02515
- Authors: Zhichen Liu, Ruihan Sun, Hengjie Yang, Zipeng Wu, Zhaohan Chen, Xiaofan Zhang, Yang Xu

## Collected abstract-level information
The paper formulates a problem called `state continuity under context turnover`: carrying computation across a long-running interaction through a fixed-capacity memory state whose lifetime is independent of the active context window.

LiveMem augments a pretrained full-attention LLM with a persistent memory state while the main attention path keeps a bounded KV window. The authors combine context turnover, memory-state maintenance, memory-oriented post-training and state-aware serving.

## Author-reported results
- The authors report leading overall performance among evaluated intrinsic-memory systems.
- On LongMemEval, they report answering from the memory state even after supporting evidence has left the active context.

## Verification boundary
Only the title, metadata and abstract-level claims have been screened at this stage. No table/figure/methodology reproduction or independent evaluation has yet been performed.

## Screening note
Keep in the paper inventory for long-term memory / continual inference.