# SP001 early Kimi lineage gap fill — 2026-08-23

Status: `RAW_OPERATOR_OBSERVATION`

Issue: `SP001`

## Purpose

The initial primary-source pass had strong Kimi technical coverage from k1.5 onward but did not adequately represent Moonshot AI's 2023–2024 long-context product lineage. This gap fill records historical Discovery sources and their evidence limitations.

## SRC-KIMI-LAUNCH-2023

- Title: `Moonshot AI Kicks Off the "Long-Context Era" for 100-Billion-Parameter Models`
- URL: https://elsewhere.news/en/monolith/moonshot-ai
- Source class: SECONDARY / INVESTOR_PORTFOLIO_ACCOUNT
- Published: 2023-10-09
- Obligations: SP001-O01, SP001-O03, SP001-O07
- Observation: Monolith, an early Moonshot investor, records the October 9, 2023 Kimi Chat launch and the product's emphasis on input up to 200,000 Chinese characters. This is useful chronology/context evidence but is not a Moonshot technical paper and must not be used alone to establish historical priority or exact token-equivalent claims.

## SRC-KIMI-INDEPENDENT-LONGCTX-2024

- Title: `L-Eval / long-context evaluation reference to Kimi-Chat`
- URL: https://openreview.net/pdf/15341095d44faf6237820dd73e26c19b746be1e4.pdf
- Source class: PRIMARY_PAPER / INDEPENDENT_EVALUATION
- Published lineage point: 2024
- Obligations: SP001-O03, SP001-O07
- Observation: an independent long-context evaluation describes Kimi-Chat as a proprietary Moonshot chat model designed for contexts up to 200K, providing external confirmation that long context was a defining early Kimi capability. Exact implementation details remain undisclosed in this source.

## SRC-KIMI-VL-2025

- Title: `Kimi-VL`
- URL: https://github.com/MoonshotAI/Kimi-VL
- Source class: PRIMARY_REPOSITORY
- Published lineage point: 2025
- Obligations: SP001-O03, SP001-O04
- Observation: Kimi-VL adds an efficient MoE multimodal branch with long-context understanding and agent capabilities while activating 2.8B parameters in the language decoder. This bridge helps connect Kimi's early long-context identity to the later K2/K3 native multimodal/agentic endpoint without claiming a simple direct architecture lineage.

## Disposition

For Architecture planning, Kimi's branch can be represented as:

`2023 long-context product differentiation -> 2025 long-context RL / multimodal research (k1.5, Kimi-VL) -> K2 open agentic MoE -> Kimi Linear efficiency research -> K3 multimodal long-horizon agentic frontier`

The 2023 launch date/context-window fact should remain explicitly source-qualified until a stronger archived Moonshot first-party artifact is located during Evidence work. Historical priority claims remain out of scope unless primary evidence supports them.
