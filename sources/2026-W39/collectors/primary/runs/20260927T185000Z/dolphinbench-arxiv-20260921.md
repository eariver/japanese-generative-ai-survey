# Collector raw — DolphinBench paper (arXiv 2609.24971, Sep 21; v2 Sep 22)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:42:00Z (arXiv abs page + search excerpts; full PDF not consumed)
- source_url: https://arxiv.org/abs/2609.24971
- source_type: PRIMARY_PAPER
- published: 2026-09-21 (v1); revised 2026-09-22 (v2)

## Consumed claims

1. EVENT: mem0 (Rathi/Yadav/Singh) released DolphinBench: agent-memory benchmark evaluating memory through task completion (not QA retrieval); 3 knowledge-work personas × ~500k tokens history × 200 tasks; history-necessity verified (success with / failure without); cost + latency reported alongside accuracy. 6 pages, 2 figures. Dataset + eval code at dolphinbench.ai. (PRIMARY_FACT at abs level)
2. DESIGN CLAIM: no existing memory benchmark combines all three (task-grounded memory + necessity verification + cost/latency reporting). (AUTHOR_CLAIM)
3. mem0 blog Sep 22 corroborates release (secondary corroboration, not separately retrieved).

## Boundaries

- PDF body not consumed: no verdict on task quality, baseline results, or comparison-table correctness.
- X ledger has ZERO rows for DolphinBench (r3 C7 UNVERIFIED) — community momentum unrecoverable in-ledger; paper authority stands alone.
