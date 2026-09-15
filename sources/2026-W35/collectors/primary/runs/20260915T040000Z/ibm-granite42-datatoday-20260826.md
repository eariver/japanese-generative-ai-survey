# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w35-primary-20260915-r1
- locator: https://data-today.net/granite-4-2-native-reasoning-open-weights/
- observed_at: 2026-09-15T04:10:00Z
- published_at: 2026-08-26 (page date; event date 2026-08-25 per article)
- retrieval: webfetch text; boilerplate trimmed; substantive technical claims preserved verbatim in wording.
- authority_class: SECONDARY_TECHNICAL (independent technical press; IBM first-party release is the verification target)

# Retrieved content (substantive claims)

Title: IBM Granite 4.2 ships reasoning and agent RL under Apache 2.0. By Lars Cornelissen, August 26, 2026.

On August 25, 2026, IBM Research published Granite 4.2, a family of dense, decoder-only reasoning LLMs in three sizes: 3B, 8B, and 30B parameters, all under the Apache 2.0 license. Headline: native reasoning, switchable chain-of-thought "thinking" mode; for 8B and 30B, a multi-stage agentic RL pipeline training tool calls, code execution, terminal driving, and web search inside real sandboxed environments. First Granite release built for agents.

Three-way thinking switch: full thinking, low-effort thinking (short reasoning budget), non-thinking — same weights.

HF collection + GitHub repo live with weights, instruct checkpoints, quantized variants per size.

Architecture (all dense decoder-only, GQA, RoPE theta 10,000,000, SwiGLU, RMSNorm, bf16): 3B = 40 layers / 2560 embed; 8B = 40 layers / 4096 embed; 30B = 64 layers / 4096 embed. Base sequence 131,072, extended to 512K in fifth pre-training phase.

Pre-training from scratch ~15T tokens, five phases (foundational x2, mid-training annealing x2, long-context extension). Speculative decoding layer shipped for serving cost.

SFT: ~7.2M samples (~100B tokens, ~65B trainable); 31.6% agentic / 68.4% non-agentic. Agentic corpus: SWE 69%, tool calling 12.1%, terminal 8.0%, math 3.5%, search 0.8%, action 0.2%; scaffolds incl. OpenHands, OpenCode, Terminus-2, SWE-agent, OpenResearcher, MiniSWE, OpenSeeker, EnvScaler, Gemini CLI, Hermes, Codex, Goose. Non-agentic: instruction 18.8%, coding 18.8%, math 14.6%, multilingual 7.0%, science 5.4%, reasoning 3.0%, safety 0.8%. QC: OpenAI Chat format normalization; GPT-OSS-120B and Gemma 4 as judges; SHA-256 dedup over tools+messages. 30B adds second SFT phase on agentic coding (SWE upsampled, ~16% replay, ~1 epoch, lr 3.0e-6).

RL: multi-stage async GRPO; foundational RLVR (math boxed-answer + Lean proving, competitive coding hidden-test sandbox, science MCQA, instruction following, single-step tool calling, reasoning puzzles with abstention; 256 prompts x 16 responses = 4096-example batch); skill boosters (code/science/instruction). Agentic block (8B+30B only): SWE -> Terminal -> Search in real environments, sparse outcome rewards. Pipeline: SFT -> RLVR -> boosters -> SWE -> Terminal -> Search -> RLHF (GenRM + safety reward incl. jailbreak resistance; highest KL; reasoning-length penalty). 3B stops after foundational RL + RLHF (no agentic block).

Differentiation claimed: three-way thinking switch on same weights; agentic RL in real envs; OpenAI-compatible function calling via vLLM (SGLang recipe too); Apache 2.0 on weights/instruct/quants.

Open questions noted: agentic corpus 69% SWE-skewed (non-coding transfer unproven); reasoning-length penalty may hurt long-deliberation tasks; 3B not agent-trained; IBM's own benchmark numbers not independently verified.
