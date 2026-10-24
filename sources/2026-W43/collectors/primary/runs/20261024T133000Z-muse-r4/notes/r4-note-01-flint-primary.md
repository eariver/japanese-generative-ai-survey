# W43 r4 Flint primary note (X-01, SUBSTANTIVELY_CONSUMED 2026-10-24)

Method: `recursive.com/updates` index + `introducing-recursive-flint` announcement HTML (curl HTTP 200, 366583 bytes archived as raw) + HF card/API (full 5478-byte API body archived) + WIRED Oct 21 hands-on corroboration. Retrieval UTC 2026-10-24T13:27–13:30Z.

## Event identity (IN, Oct 21)
- Updates index entry dated **Oct 21, 2026**: "Introducing Flint — Local model with the fastest inference and strongest coding performance in its class. Built with automated research."
- HF repo `RecursiveSI/flint` `createdAt` **2026-10-21T14:20:58Z** (`lastModified` 14:24:03Z, sha `2a247be2…`, 733 likes, license `apache-2.0`). Weights available IN-window.
- WIRED Oct 21 hands-on ("scary good", RSI framing) corroborates same-day availability.
- Announcement page `Published Oct 23, 8:37 PM UTC` is Framer site republish metadata; event date Oct 21 stands on index + HF + WIRED triple corroboration (quirk recorded, not used as event date).

## Model (first-party, HF card + announcement)
- 39.8B total / ~2.5B active (2.2B body + head convention; "40B-A2.5B" rounded designation); decoder-only MoE Transformer; 49 layers (2 dense + 47 MoE); 256 routed experts, 6/token + always-active shared; 35 SWA (513-token window: current + 512) + 14 full-attention; 32Q/4KV heads d128; per-head QK RMSNorm + learned sinks; RoPE on SW only; ctx 262,144 incl. prompt+output; vocab 150,144; text in/out; cutoff June 2026.
- Training: from scratch — pretrain, mid-train, SFT, RL; text + code + instruction + agentic; Eureka Machine searched data/recipes/infra/quant (lm_head 4-bit against common practice given large head share).

## Evaluation (vendor release evals, unreproduced here)
- Temp 1.0 / top-p 0.95 / top-k 20; Terminus 2 harness; mini-swe-agent; avg pass@1 ≥5 attempts; web-retrieval solutions counted as failures.
- Terminal-Bench 2.1 **54.9%**, SWE-bench Pro v2 **89.7%**, SWE-bench Verified **74.2%**. † = Recursive-measured; other comparisons developer-reported; setups vary.
- Speed (publisher-claimed, short contexts): **125+ tok/s M4 Pro MBP**, **150+ tok/s 64GB RTX Spark**, up to 2x class, 5x+ vs dense 25–40B; avg tok/s over 128k session (*Muse measured at 124k, prefill excluded). NOT independently benchmarked here.

## Serving/availability/license
- 1× B200/H200 per replica via SGLang kit (`sglang/`), ~80GB BF16; OpenAI-compat tool calls; output budget ≥32768 hard problems; `rec` engine for M4 Pro/M5 Pro/Max; Unsloth/LM Studio/vLLM/SGLang; 43 community quants, 8 finetunes, 4795 downloads last month.
- Weights Apache 2.0 on HF; hosted API terms separate. Contact: support@ (model/serving + repro), safety@, security@recursive.com.
- Limitations (vendor-stated): SFT safety examples yet real harm/faulty-code/tool-misuse possible; long reasoning can exhaust budget; ctx is capacity not uniform accuracy; results vary by checkpoint/runtime.

## X linkage
Grok observed Flint Oct 21 + M4 Pro speed chatter (no post IDs except topic). This primary record binds the exact Grok Raw path as second raw_ref alongside first-party captures — one event family, no duplicate Selection identity.
