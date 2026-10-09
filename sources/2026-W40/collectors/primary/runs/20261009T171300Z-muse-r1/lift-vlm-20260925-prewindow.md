# Collector raw — arXiv: LIFT / Linguistic Reasoning Vectors (Sep 25, PRE-WINDOW)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of arXiv abs page)
- source_url: https://arxiv.org/abs/2609.31140
- source_type: PRIMARY_RESEARCH_ABSTRACT
- published: 2026-09-25T11:31:02Z (arXiv v1; BEFORE W40 cutoff 2026-09-25T22:00:00Z)
- temporal_disposition: PRE_WINDOW (CONTEXT only; X recirculation cannot make it a new W40 paper)

## Consumed claims (claim-level, abstract only)

1. EVENT: Submission "Can Linguistic Reasoning Vectors Enhance Multimodal Reasoning Ability?" (Wang et al.) Sep 25 11:31Z: LIFT vector-intervention transferring base-LLM reasoning to VLM without backbone retraining; reasoning vectors = answer-token hidden-state diffs (Reasoner vs Solver paths); learnable adaptation, frozen backbone; NeurIPS 2026 accepted. (PRIMARY_FACT: submission, date, method sketch)
2. RESULTS (paper-claimed): LLM-derived vectors beat VLM-derived under matched protocols on 2 VLMs x 6 benchmarks; partial recovery of degraded reasoning; vectors affect intermediate behavior, not just final answers. (PAPER_CLAIM)
3. TEMPORAL: Predates W40 by ~10.5h; belongs to CONTEXT/carry reasoning, not ordinary W40 discovery. (EDITORIAL_BOUNDARY)

## Boundaries / unresolved

- Full PDF/code (promised "will be released soon") NOT consumed; no W40 newness claim.
