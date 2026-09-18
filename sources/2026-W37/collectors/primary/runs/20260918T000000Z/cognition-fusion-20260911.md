# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w37-primary-20260918-r1
- locator: https://cognition.com/blog/local-fusion
- observed_at: 2026-09-18T00:00:00Z
- published_at: 2026-09-11
- retrieval: webfetch markdown of Cognition Fusion announcement; stored claim-relevant verbatim excerpts as returned. Page header shows 09.11.26. Full page consumed via webfetch 2026-09-18.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (claim-relevant verbatim excerpts)

# Introducing Fusion in Devin Desktop & CLI

09.11.26

Fusion is the most efficient frontier harness for Fable and Astra, up to 39% more efficient compared to other model harnesses across major coding benchmarks. Today, we're making it available in Devin Desktop and CLI.

Artificial Analysis Coding Agent Index v1.5 cited: Devin Fusion Fable 5.1 + SWE-2 vs Claude Code Fable 5.1: 36% lower cost; Devin Fusion Astra + SWE-2 vs Codex Astra: 39% lower cost.

When selecting Fusion, you pick two models instead of one. Pick a frontier model for planning and review (the "lead"), and a cost-effective model for execution (the "sidekick"). For best results, we recommend pairing Fable 5.1 with SWE-2.

Savings table (vendor, with Artificial Analysis and Vals AI):

- DeepSWE 1.1: Fable 5.1 64.3 $14.63 -> Fusion 63.1 $7.88 (-46%); Astra 67.6 $7.88 -> Fusion 67.3 $4.69 (-40%)
- Terminal-Bench 4: Fable 57.6 $17.46 -> Fusion 56.1 $13.37 (-23%); Astra 55.6 $10.08 -> Fusion 50.0 $6.06 (-40%)
- SWE-Atlas QnA: Fable 64.8 $7.57 -> Fusion 65.9 $5.00 (-34%); Astra 61.8 $5.72 -> Fusion 59.4 $3.59 (-37%)
- Vals Code Migration: Fable 54.6 $70.97 -> Fusion 57.3 $42.00 (-41%); Astra 67.7 $44.36 -> Fusion 61.3 $35.51 (-20%)
- FrontierCode 1.1 (Extended): Fable 63.6 $2.68 -> Fusion 63.5 $1.67 (-38%); Astra 63.1 $2.62 -> Fusion 63.4 $2.34 (-11%)

Fusion architecture: running two parallel agents, each with its own persistent context and tools. The lead agent runs with a frontier model and is in charge. Sidekick explores code, implements changes, runs tests, reports back. Lead reviews, identifies problems, can take control back.

Try via Devin CLI install.
