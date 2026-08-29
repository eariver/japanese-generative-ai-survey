# SP001 — Post-merge primary-source intake

Status: `RESEARCH INTAKE / NOT YET CANONICAL CORE ACCEPTANCE`

Run: clean post-redesign validation

Reviewed Core / starting `main`: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`

Research Profile: `THEMATIC`

Publication Profile: `LONGFORM_SPECIAL`

As-of: `2026-08-23T12:29:15Z`

Planning authority: `docs/thematic-special-backlog.md` / `TS-001`

This file records the primary-source research used to prepare the clean SP001 Architecture. It is deliberately **not** a substitute for `discovery-accepted-v2.json`, Screening/Evidence acceptance, Profile Completeness, Candidate Matrix, or other canonical Core artifacts. Those remain subject to the canonical deterministic validators.

## X / Grok applicability

Decision: `NOT_REQUIRED`.

Reason: SP001 asks for technical history, model-family strategy, architecture/training/post-training transitions, serving/deployment ecosystem, open-weight/licensing boundaries, and developer distribution. These questions can be closed primarily with technical reports, official model repositories/model cards, and official API/project documentation. X would add community reaction but is unlikely to materially change the approved technical Architecture. The parallel W33 clean validation separately exercises the Core's required Grok/X path.

## Research boundary

The edition must not flatten DeepSeek, Qwen, GLM, Kimi, MiniMax, Yi, and Baichuan into one homogeneous “Chinese model” strategy. Direct ancestry is asserted only where first-party/technical-report evidence supports it. Benchmark numbers are not normalized across different versions, prompts, harnesses, dates, or evaluation conditions.

“Open Source” and “Open Weight” are not synonyms here. For every family where licensing is discussed, code license, weight/model license, redistribution/commercial-use terms, and availability of training recipe/data are treated separately.

## Primary-source map

### DeepSeek lineage

1. **DeepSeek LLM** — early foundation/scaling-law phase  
   Source: https://arxiv.org/abs/2401.02954  
   Material points: 7B/67B family; 2T-token Chinese/English pretraining; scaling-law investigation; LLaMA-derived architecture with training changes; SFT/DPO discussion.  
   Obligations: `SP001-O01`, `SP001-O02`, `SP001-O06`.

2. **DeepSeek-V2** — efficiency architecture becomes a first-class strategy  
   Source: https://arxiv.org/abs/2405.04434  
   Material points: MoE with 236B total / 21B activated; Multi-head Latent Attention (MLA); DeepSeekMoE; 128K context; explicit training/inference-efficiency objective.  
   Obligations: `SP001-O01`, `SP001-O02`, `SP001-O04`.

3. **DeepSeek-V3** — scaling the V2 efficiency line  
   Sources: https://arxiv.org/abs/2412.19437 ; https://github.com/deepseek-ai/DeepSeek-V3  
   Material points: 671B total / 37B activated; MLA + DeepSeekMoE retained; 14.8T pretraining tokens; auxiliary-loss-free load balancing and multi-token prediction; official repository distinguishes MIT code license from model license and states commercial use is supported.  
   Obligations: `SP001-O01`, `SP001-O02`, `SP001-O04`, `SP001-O06`.

4. **DeepSeek-R1** — reasoning becomes an explicit post-training line  
   Sources: https://arxiv.org/abs/2501.12948 ; https://github.com/deepseek-ai/DeepSeek-R1  
   Material points: R1-Zero demonstrates large-scale RL without preliminary SFT; R1 adds cold-start data and multi-stage training; distilled models are released; official repository licenses code and primary R1 weights under MIT while noting upstream licenses for Qwen/Llama-derived distillations.  
   Obligations: `SP001-O02`, `SP001-O03`, `SP001-O06`.

5. **DeepSeek-V4** — 2026 long-context/agentic/efficiency convergence  
   Sources: https://www.deepseek.com/en/transparency/ ; https://deepseek.com/en/news/v4-preview/ ; https://api-docs.deepseek.com/news/news260424/  
   Material points: official release date 2026-04-24; V4-Pro 1.6T total / 49B active and V4-Flash 284B / 13B; 1M context; token-wise compression + DeepSeek Sparse Attention; thinking/non-thinking modes; API compatibility and agentic-coding emphasis.  
   Obligations: `SP001-O03`, `SP001-O04`, `SP001-O05`, `SP001-O07`.

### Qwen lineage

6. **Qwen2 Technical Report**  
   Source: https://arxiv.org/abs/2407.10671  
   Material points: dense and MoE models across 0.5B–72B; multilingual/coding/math/reasoning coverage; weights distributed through Hugging Face and ModelScope; associated quantization, fine-tuning, deployment resources.  
   Obligations: `SP001-O01`, `SP001-O02`, `SP001-O05`, `SP001-O06`.

7. **Qwen3 Technical Report**  
   Source: https://arxiv.org/abs/2505.09388  
   Material points: dense and MoE from 0.6B to 235B; unified thinking/non-thinking modes; thinking budget; multilingual expansion; all Qwen3 models described by the report as publicly accessible under Apache 2.0.  
   Obligations: `SP001-O02`, `SP001-O03`, `SP001-O04`, `SP001-O06`.

8. **Qwen3.8 official repository** — 2026 open release / agent execution  
   Source: https://github.com/QwenLM/Qwen3.8  
   Material points: flagship open Qwen3.8 line; 2026-08-12 2.4T-A95B release and 2026-08-14 27B release; coding/professional/research/long-horizon-agent emphasis; Hugging Face and ModelScope distribution; repository itself Apache-2.0 while weight licenses are to be read from the corresponding model pages.  
   Obligations: `SP001-O02`, `SP001-O03`, `SP001-O05`, `SP001-O06`, `SP001-O07`.

### GLM lineage

9. **GLM-130B**  
   Source: https://arxiv.org/abs/2210.02414  
   Material role: early large bilingual GLM lineage and a necessary pre-ChatGLM anchor.  
   Obligations: `SP001-O01`, `SP001-O02`.

10. **ChatGLM / GLM-4 family report**  
    Source: https://arxiv.org/abs/2406.12793  
    Material points: family evolution through GLM-4; large-scale pretraining, long-context and tool-use direction; useful bridge from bilingual/open ChatGLM adoption to later general-purpose/agentic GLM systems.  
    Obligations: `SP001-O01`, `SP001-O02`, `SP001-O03`, `SP001-O05`.

11. **GLM-4.5**  
    Source: https://arxiv.org/abs/2508.06471  
    Material points: 355B total / 32B active MoE; 23T-token pretraining; hybrid reasoning and explicit coding/agentic target.  
    Obligations: `SP001-O02`, `SP001-O03`, `SP001-O04`.

12. **GLM-5 official repository/report**  
    Sources: https://github.com/zai-org/GLM-5 ; https://arxiv.org/abs/2602.15763  
    Material points: 744B / 40B active, 28.5T pretraining tokens; DeepSeek Sparse Attention integration; asynchronous RL infrastructure (`slime`) described as a post-training throughput mechanism; long-horizon agentic engineering; local deployment recipes for vLLM, SGLang, xLLM and KTransformers; repository Apache-2.0.  
    Obligations: `SP001-O02`, `SP001-O03`, `SP001-O04`, `SP001-O05`, `SP001-O06`.

### Kimi / Moonshot lineage

13. **Kimi k1.5**  
    Source: https://arxiv.org/abs/2501.12599  
    Material role: long-context multimodal reasoning/RL step before the K2/K3 open-weight agentic line.  
    Obligations: `SP001-O02`, `SP001-O03`.

14. **Kimi K2**  
    Source: https://github.com/MoonshotAI/Kimi-K2  
    Material points to verify in Evidence stage: 1T-total / 32B-active MoE; 15.5T-token training; MuonClip; 128K context; agentic/coding emphasis; first-party deployment guidance including vLLM/SGLang.  
    Obligations: `SP001-O02`, `SP001-O03`, `SP001-O04`, `SP001-O05`, `SP001-O06`.

15. **Kimi K2.5 / Kimi product evolution**  
    Source: https://github.com/MoonshotAI/kimi-help-center/blob/master/en-US/agent/overview.md  
    Material role: first-party chronology from K2 to K2.5/K2.6/K3 and the product/Agent distribution layer.  
    Obligations: `SP001-O01`, `SP001-O03`, `SP001-O05`.

16. **Kimi K3**  
    Source: https://github.com/MoonshotAI/Kimi-K3  
    Material points: 2.8T open-weight native multimodal model; Kimi Delta Attention and Attention Residuals; 1M context; high-sparsity MoE; long-horizon coding/agentic focus. Official product chronology records K3 release on 2026-07-16 and full weights on 2026-07-27.  
    Obligations: `SP001-O02`, `SP001-O03`, `SP001-O04`, `SP001-O05`, `SP001-O06`, `SP001-O07`.

### Supporting families / cross-checks

17. **MiniMax-01**  
    Source: https://arxiv.org/abs/2501.08313  
    Material role: alternative long-context/attention-efficiency trajectory; useful counterexample to treating all Chinese MoE/long-context work as DeepSeek-derived.  
    Obligations: `SP001-O02`, `SP001-O04`.

18. **Yi family technical report**  
    Source: https://arxiv.org/abs/2403.04652  
    Material role: 2023–24 Chinese/English open-weight model formation, long-context and model-size strategy; supporting chronology rather than a primary chapter axis.  
    Obligations: `SP001-O01`, `SP001-O02`, `SP001-O06`.

19. **Baichuan 2**  
    Source: https://arxiv.org/abs/2309.10305  
    Material role: another 2023 Chinese open model family, useful for establishing that the ecosystem was plural before the later DeepSeek/Qwen/GLM/Kimi frontier convergence.  
    Obligations: `SP001-O01`, `SP001-O02`, `SP001-O06`.

## Cross-source findings for Architecture

1. **The central story is a convergence, not a single lineage.** Early bilingual/base-model scaling, efficient sparse architectures, long-context methods, RL reasoning/post-training, multimodality, and agentic tooling developed along partly independent tracks and later converged.

2. **DeepSeek's most legible through-line is efficiency architecture plus open-weight availability.** V2 establishes MLA/DeepSeekMoE; V3 scales it; R1 makes reasoning/post-training a separate headline; V4 combines sparse/long-context and agentic deployment.

3. **Qwen's differentiator is breadth plus distribution.** The family spans dense/MoE sizes, multilingual/coding/reasoning, Hugging Face + ModelScope, and broad downstream runtime/tool compatibility. This should not be collapsed into “another DeepSeek”.

4. **GLM moves from an early bilingual/research lineage toward agentic engineering.** GLM-4/4.5/5 provide a useful narrative of long context/tooling, hybrid reasoning, sparse attention, RL infrastructure, and local serving.

5. **Kimi makes long context and agentic execution structurally central.** k1.5, K2 and K3 show a transition from long-context multimodal RL to very large sparse open-weight models with dedicated efficient-attention mechanisms and productized Agent distribution.

6. **Open-weight competition is partly a systems/distribution phenomenon.** Model availability on Hugging Face/ModelScope, OpenAI-compatible APIs, vLLM/SGLang/KTransformers/llama.cpp-class runtimes, quantization/fine-tuning paths and permissive-or-custom licenses materially affect adoption.

7. **License semantics must remain model-specific.** DeepSeek-V3 distinguishes code and model licenses; R1 primary weights are MIT but some distilled derivatives inherit upstream Qwen/Llama constraints; Qwen3 is Apache 2.0 per report while later Qwen3.8 weight pages remain the exact authority; other families similarly require artifact-level checks. “Open source Chinese models” is therefore too coarse.

8. **Benchmark claims are evidence of a model's reported position, not a common cross-family league table.** Different test versions, prompts, tool scaffolds, contamination controls and dates make naive normalized ranking editorially unsafe.

## Remaining Evidence-stage questions

- exact weight/license terms for each Qwen3.8 checkpoint and Kimi K2/K3 checkpoint must be captured from the artifact-specific model page/license before reader-facing claims;
- direct influence claims such as “GLM-5 adopted DeepSeek's DSA” may be made only where the GLM-5 first-party report explicitly states the integration; broader ancestry should remain phrased as technique reuse/convergence rather than institutional lineage;
- Kimi K2/K3 exact active-expert counts, training-token counts and license details need first-party card verification before numerical use;
- 2026 frontier performance comparisons should be presented as source-local reported results unless identical evaluation conditions can be demonstrated;
- supporting MiniMax/Yi/Baichuan material should remain subordinate unless it closes an Architecture obligation that the four primary families cannot cover.

## Intake conclusion

All seven initial obligations have credible primary-source coverage paths. No obligation currently requires X/Grok evidence. The material is sufficient to propose Architecture, subject to canonical Screening/Evidence/Completeness validation and exact source verification before the first Human Gate.
