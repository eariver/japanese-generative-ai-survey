# Collector raw — arXiv: Context Language Models (Sep 29, in-window)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of arXiv abs page)
- source_url: https://arxiv.org/abs/2609.37725
- source_type: PRIMARY_RESEARCH_ABSTRACT
- published: 2026-09-29 (arXiv v1 submitted Tue 29 Sep 2026 14:50:08 UTC; within W40 [Sep 25 22Z, Oct 2 22Z))

## Consumed claims (claim-level, abstract only)

1. EVENT: New submission "Context Language Models" (Shao et al., 13 authors) Sep 29: models natively manage own context as editable file; multi-agent contexts as files. (PRIMARY_FACT: submission occurred, date)
2. RESULTS (paper-claimed, attribution required): Zero-shot CLMs beat SOTA context strategies: +11.4% acc / -21.5% FLOPs BrowseComp-Plus; +5% / -59% FLOPs 12h EdgeBench; +65% improvement same compute 24h multi-repo swarm; skill-optimization steering +35.9pp held-out; online RL Qwen3.5-9B +47.6% / -12% FLOPs BrowseComp-Plus; Suffix Cache Reuse -35% server compute vs SGLang matched perf. (PAPER_CLAIM: abstract-reported, not independently reproduced)
3. SCOPE: Abstract consumed; full PDF/code/configs NOT consumed in this run. (ACCESS_BOUNDARY)

## Boundaries / unresolved

- W40 new submission, not X-post-date item; distinct from pre-window LIFT.
- Full experimental setup, baselines, compute accounting need PDF consumption at Evidence.
