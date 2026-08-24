# SP001 post-integration primary-source observations — fresh r2

Status: `FRESH DISCOVERY RAW OBSERVATION / NOT YET EVIDENCE ACCEPTANCE`

Observed-at authority: `2026-08-24T17:24:00Z`
Collector: `ChatGPT GPT-5.6 Sol`
Collector run: `postintegration-sp001-primary-r2`

This is a fresh post-PR#452 materialization from the current clean SP001 research pass. It is not copied or relabeled from the archived failed pre-redesign acceptance tree. Each entry records the first-party/technical source locator and the bounded material point that Discovery may carry forward. Exact numerical, license, priority, benchmark, and causal claims remain subject to Evidence verification.

## SP001-D001 — DeepSeek LLM: Scaling Open-Source Language Models with Longtermism
- Locator: https://arxiv.org/abs/2401.02954
- Source type: PRIMARY_PAPER
- Family/context: DeepSeek
- Published: 2024-01-05
- Obligations: SP001-O01, SP001-O02, SP001-O06
- Discovery observation: 7B/67B foundation family; 2T-token Chinese/English pretraining; scaling-law and SFT/DPO baseline preceding the later efficiency line.

## SP001-D002 — DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model
- Locator: https://arxiv.org/abs/2405.04434
- Source type: PRIMARY_PAPER
- Family/context: DeepSeek
- Published: 2024-05-07
- Obligations: SP001-O01, SP001-O02, SP001-O04
- Discovery observation: MoE, MLA and DeepSeekMoE establish efficiency as a first-class architectural strategy; report describes 236B total / 21B activated and 128K context.

## SP001-D003 — DeepSeek-V3 Technical Report
- Locator: https://arxiv.org/abs/2412.19437
- Source type: PRIMARY_PAPER
- Family/context: DeepSeek
- Published: 2024-12-27
- Obligations: SP001-O01, SP001-O02, SP001-O04
- Discovery observation: Scales the V2 efficiency line with 671B total / 37B activated, MLA/DeepSeekMoE, 14.8T tokens, load-balancing and multi-token-prediction changes.

## SP001-D004 — DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- Locator: https://arxiv.org/abs/2501.12948
- Source type: PRIMARY_PAPER
- Family/context: DeepSeek
- Published: 2025-01-22
- Obligations: SP001-O02, SP001-O03, SP001-O06
- Discovery observation: Separates reasoning/post-training into an explicit line: R1-Zero large-scale RL, followed by cold-start data and multi-stage training in R1; distilled derivatives require upstream-license care.

## SP001-D005 — DeepSeek V4 official release/transparency material
- Locator: https://www.deepseek.com/en/transparency/
- Source type: PRIMARY_OFFICIAL
- Family/context: DeepSeek
- Published: 2026-04-24
- Obligations: SP001-O03, SP001-O04, SP001-O05, SP001-O07
- Discovery observation: 2026 frontier endpoint: 1M context, sparse/token-compression mechanisms, thinking/non-thinking operation and agentic-coding/API deployment emphasis; performance claims remain source-local.

## SP001-D006 — Qwen2 Technical Report
- Locator: https://arxiv.org/abs/2407.10671
- Source type: PRIMARY_PAPER
- Family/context: Qwen
- Published: 2024-07-15
- Obligations: SP001-O01, SP001-O02, SP001-O05, SP001-O06
- Discovery observation: Dense and MoE family across broad sizes with multilingual/coding/math/reasoning coverage and distribution through Hugging Face/ModelScope plus quantization/fine-tuning/deployment resources.

## SP001-D007 — Qwen3 Technical Report
- Locator: https://arxiv.org/abs/2505.09388
- Source type: PRIMARY_PAPER
- Family/context: Qwen
- Published: 2025-05-14
- Obligations: SP001-O02, SP001-O03, SP001-O04, SP001-O06
- Discovery observation: Unified thinking/non-thinking modes, thinking budget, dense/MoE family and broad multilingual expansion; report states public accessibility under Apache 2.0.

## SP001-D008 — Qwen3.8 official repository
- Locator: https://github.com/QwenLM/Qwen3.8
- Source type: PRIMARY_REPOSITORY
- Family/context: Qwen
- Published: 2026-08-12
- Obligations: SP001-O02, SP001-O03, SP001-O05, SP001-O06, SP001-O07
- Discovery observation: 2026 open-weight agent/coding/research line and Hugging Face/ModelScope distribution; repository license and checkpoint-specific weight licenses must be distinguished.

## SP001-D009 — GLM-130B: An Open Bilingual Pre-trained Model
- Locator: https://arxiv.org/abs/2210.02414
- Source type: PRIMARY_PAPER
- Family/context: GLM
- Published: 2022-10-05
- Obligations: SP001-O01, SP001-O02
- Discovery observation: Early large bilingual GLM anchor before ChatGLM and the later agentic GLM family.

## SP001-D010 — ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools
- Locator: https://arxiv.org/abs/2406.12793
- Source type: PRIMARY_PAPER
- Family/context: GLM
- Published: 2024-06-18
- Obligations: SP001-O01, SP001-O02, SP001-O03, SP001-O05
- Discovery observation: Family evolution through GLM-4, long-context/tool-use direction and bridge from bilingual/open ChatGLM adoption to general-purpose agent/tool systems.

## SP001-D011 — GLM-4.5: Agentic, Reasoning, and Coding Foundation Models
- Locator: https://arxiv.org/abs/2508.06471
- Source type: PRIMARY_PAPER
- Family/context: GLM
- Published: 2025-08-08
- Obligations: SP001-O02, SP001-O03, SP001-O04
- Discovery observation: 355B total / 32B active MoE, 23T-token pretraining and explicit reasoning/coding/agentic target.

## SP001-D012 — GLM-5 official repository and technical report
- Locator: https://github.com/zai-org/GLM-5
- Source type: PRIMARY_REPOSITORY
- Family/context: GLM
- Published: 2026-02-18
- Obligations: SP001-O02, SP001-O03, SP001-O04, SP001-O05, SP001-O06
- Discovery observation: 744B / 40B active, 28.5T tokens, sparse-attention reuse, asynchronous RL infrastructure, long-horizon agentic engineering and multiple local-serving recipes.

## SP001-D013 — Kimi k1.5: Scaling Reinforcement Learning with LLMs
- Locator: https://arxiv.org/abs/2501.12599
- Source type: PRIMARY_PAPER
- Family/context: Kimi
- Published: 2025-01-21
- Obligations: SP001-O02, SP001-O03
- Discovery observation: Long-context multimodal reasoning/RL step that precedes the K2/K3 open-weight agentic line.

## SP001-D014 — Kimi K2 official repository
- Locator: https://github.com/MoonshotAI/Kimi-K2
- Source type: PRIMARY_REPOSITORY
- Family/context: Kimi
- Published: 2025-07-11
- Obligations: SP001-O02, SP001-O03, SP001-O04, SP001-O05, SP001-O06
- Discovery observation: Large MoE, agentic/coding emphasis and first-party deployment guidance; exact active experts, token counts and license details remain artifact-level Evidence checks.

## SP001-D015 — Kimi Agent/product evolution documentation
- Locator: https://github.com/MoonshotAI/kimi-help-center/blob/master/en-US/agent/overview.md
- Source type: PRIMARY_REPOSITORY
- Family/context: Kimi
- Published: not fixed in this intake
- Obligations: SP001-O01, SP001-O03, SP001-O05
- Discovery observation: First-party product chronology and Agent distribution layer connecting K2/K2.5/K2.6/K3 product evolution.

## SP001-D016 — Kimi K3 official repository
- Locator: https://github.com/MoonshotAI/Kimi-K3
- Source type: PRIMARY_REPOSITORY
- Family/context: Kimi
- Published: 2026-07-16
- Obligations: SP001-O02, SP001-O03, SP001-O04, SP001-O05, SP001-O06, SP001-O07
- Discovery observation: 2.8T open-weight native multimodal model with efficient-attention/residual mechanisms, 1M context, sparse MoE and long-horizon coding/agentic focus; exact license/card terms remain evidence-bound.

## SP001-D017 — MiniMax-01: Scaling Foundation Models with Lightning Attention
- Locator: https://arxiv.org/abs/2501.08313
- Source type: PRIMARY_PAPER
- Family/context: MiniMax
- Published: 2025-01-14
- Obligations: SP001-O02, SP001-O04
- Discovery observation: Alternative long-context/attention-efficiency trajectory useful as a counterexample to single-lineage explanations.

## SP001-D018 — Yi: Open Foundation Models by 01.AI
- Locator: https://arxiv.org/abs/2403.04652
- Source type: PRIMARY_PAPER
- Family/context: Yi
- Published: 2024-03-07
- Obligations: SP001-O01, SP001-O02, SP001-O06
- Discovery observation: Supporting 2023–24 Chinese/English open-weight family for chronology, long-context and model-size strategy.

## SP001-D019 — Baichuan 2: Open Large-scale Language Models
- Locator: https://arxiv.org/abs/2309.10305
- Source type: PRIMARY_PAPER
- Family/context: Baichuan
- Published: 2023-09-18
- Obligations: SP001-O01, SP001-O02, SP001-O06
- Discovery observation: Supporting 2023 open-model family establishing a plural ecosystem before later DeepSeek/Qwen/GLM/Kimi convergence.
