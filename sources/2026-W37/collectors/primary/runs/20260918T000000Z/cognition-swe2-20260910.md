# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w37-primary-20260918-r1
- locator: https://cognition.com/blog/swe-2
- observed_at: 2026-09-18T00:00:00Z
- published_at: 2026-09-10
- retrieval: webfetch markdown of Cognition SWE-2 announcement; stored claim-relevant verbatim excerpts as returned. Page header shows By The Cognition Team 09.10.26. Full page consumed via webfetch 2026-09-18.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (claim-relevant verbatim excerpts)

# Introducing SWE-2: Pushing the Pareto Frontier

By The Cognition Team 09.10.26

Today we're introducing SWE-2, our most advanced coding model yet. It pushes the Pareto frontier of capability and cost, achieving 50.0% on FrontierCode 1.1 Main, within one point of Fable 5.1 while being 64% cheaper.

With SWE-2, we scaled RL to the multi-trillion-parameter regime for the first time, building on the SWE-1.7 training infrastructure and recipe.

The result is our closest model yet to the frontier. On FrontierCode 1.1 Main and DeepSWE 1.1, SWE-2 beats SWE-1.7 and Grok 4.6 on both score and cost, matches GPT-5.6 Sol and Fable 5/5.1 at a fraction of their price, and comes within a few points of GPT-6 Astra at a quarter of the cost.

SWE-2 is post-trained from Kimi K3, a 2.8T-parameter model that had already undergone extensive RL for agentic coding.

Coding benchmark results (vendor table):

- FrontierCode 1.1 Main: SWE-2 50.0%, Kimi K3 44.2%, Grok 4.6 48.0%, Fable 5.1 50.9%, GPT-5.6 Sol 47.5%, GPT-6 Astra 53.3%, SWE-1.7 42.0%
- DeepSWE 1.1: SWE-2 73.0%, Kimi K3 68.5%, Grok 4.6 67.5%, Fable 5.1 67.4%, GPT-5.6 Sol 72.7%, GPT-6 Astra 74.1%, SWE-1.7 37.7%
- Terminal-Bench 2.1: SWE-2 92.8%
- Terminal-Bench 4: SWE-2 27.3%

On FrontierCode 1.1 Main, SWE-2 medium scores higher than SWE-1.7 while taking 58% fewer turns and costing 81% less on average.

SWE-2 is available starting today in Devin Desktop and CLI. We're also rolling it out on Devin Web and Fusion.

Cost penalties, reward baselines, RL rollout serving, training data sections describe RL methodology (vendor-described).

Appendix A: For each model-benchmark pair, we report the publicly available result where one exists. Otherwise, we evaluate on internal framework using harness for which it was primarily developed: Claude Code for Anthropic, Codex for OpenAI, Grok Build for xAI, Devin CLI for open-weight models.
