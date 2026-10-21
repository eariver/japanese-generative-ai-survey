# Evidence bundle r4-02 — open-weight models (bodies/cards consumed 2026-10-17)

Run: `20261017T080000Z-muse-r4`. [VENDOR]/[INDEPENDENT]/[SECONDARY] as bundle 01.

## w42-primary-spark-open-20261015 — AUTHORITY_CONSUMED (r2 research blog; license text gap REMAINS)
- [VENDOR] 816B/42B MoE (256 experts, 8/token), 1M ctx, text+image+video+audio in; same base as Spark 1.3 + safety post-train; 2× M5 Ultra desktop (1TB unified, 1.2 TB/s); Helion kernels 1.03–3.95× kernel / 3% e2e MI350; card NOW + full report SOON.
- License: Muse Model License, limited commercial, free-for-many [VENDOR summary]; FULL TEXT UNREAD → license-vs-open-source distinction cannot be closed. Unresolved: license text, bench methodology report, independent benches, weight-bit verification.
- [SECONDARY] HF blog/PyTorch/vLLM day-0 corroborate release + specs (Oct 15).

## w42-primary-nemotron35-20261015 — AUTHORITY_CONSUMED (r2 dev blog + card excerpts)
- [VENDOR] 120B/12B hybrid Mamba-2 + C-RADIO vision, 1M, MTP/LiLiCorr/NVFP4-QAD; CharXiv 80.8 (84 w/ code), Hermes 63.44 > Ultra 56.33, LangChain 87.05 > 84.3; Scale 40× cost/5× latency; Ramp +50% tput/10× latency; AI21 +41%; Indic +10B w/ IITM; Dynamo 8× users/−85% TTFT; 600+ TPS AA agentic (Baseten).
- [INDEPENDENT] EXO Labs Pareto evaluation (accuracy vs task time, DGX Spark) — only independent anchor; details unfetched.
- Bolt split: 74B-A9B 24 GB AVAILABLE NOW; E4B 4 GB Oct 23 FUTURE (not W42). License OpenMDW-1.1 per card [VENDOR]; full text unread. Unresolved: license text, report PDF, independent repro of headline numbers.

## w42-primary-beam-20261016 — AUTHORITY_CONSUMED (r2 card + availability blog)
- [VENDOR] 501.3B/23.4B, 52L (3 dense+49 MoE), Gated GQA+SWA, 1M, 152k vocab, BF16/FP8/NVFP4, cutoff Jun 30 2026; DeepSWE 43.3 / SWE-Pro v2-Hard 78.6 / Verified 81.6 / Terminal-Bench 80.1 / AIME 97.7 / HLE 51.1 w-tools / GPQA 90.6 / MCP-Atlas 80.8 (temp 0.7/top_p 0.99); ISE refusal ~89% / compliance ~82%; distillation explicitly ALLOWED; commercial+research use.
- Apache 2.0 weights [VENDOR card statement; LICENSE file itself unopened → treat as card-claimed]. Safety Technical Report body unfetched. Unresolved: safety-report verification, independent benches, Arena ranks methodology.

## w42-primary-granite-switch41-20261014 — AUTHORITY_CONSUMED (r2 blog + 8B card)
- [VENDOR] 8B+30B composable (Decision + Guardian aLoRAs + Speech-5.0-Turbo-CTC), one endpoint ~base VRAM; Decision Index v0.3 fast (1,068 rows) overall 42.9 (K 29.1/L 48.9/R 49.8/T 59.8/A 18.0); Guardian beats Jev-1.13/MS-Decision-1/Luna-Decisions/Clef-Flash (safety decisions, avg); local-vs-hosted ±0.6.
- Apache 2.0 VERIFIED (card header + LICENSE reference; page live, 278 downloads, Transformers/vLLM snippets). 30B same-config per card (30B card not individually opened).
- Comparison ≠ fresh Decision-1 evidence: W41 HOLD stands. Unresolved: 30B card spot-check, preview variants, independent Decision-Index repro.

## w42-primary-minicpm-v47-20261012 — AUTHORITY_CAPTURED_BUT_UNCONSUMED→PARTIAL (r4 HF search excerpts; repo README + cards NOT fully opened)
- [VENDOR via HF search] 35B-A3B (first MoE) + 1B; LES lossless on-device MoE; 13+ tok/s @3 GB iPhone 17 Pro Max; SigLIP + Qwen3.5 backbone; BF16/FP8/int4/AWQ/GPTQ/GGUF + DSpark heads (Oct 15); SGLang/vLLM/llama.cpp/Ollama day-0; SRFT fine-tuning; Ollama listed.
- Dated README entries: Oct 12 release + Oct 15 DSpark heads (both IN). License NOT confirmed (MiniCPM historically Apache 2.0 — do NOT assume; gap). Benchmarks NOT captured. Status: PARTIAL (weights-listing + dated entries confirmed; card body + license + benches open).

## w42-primary-flux3-klein-20261015 — PARTIAL (r4 HF search excerpts; card/docs NOT fully opened)
- [VENDOR via HF search] 5.6B; Qwen3-VL-4B text encoder; distilled 16-step (gen/edit/API) vs base 50-step (tune/research); 4K; BBox; ComfyUI/NVFP4/int8 (8 GB GPUs); 11.1 GB BF16 / 5.3 GB NVFP4; upsampler 9B separate (18.8 GB BF16).
- License: FLUX Kommunity License v1.0 — non-commercial + <$5M qualifying commercial output (NOT OSI open-source; "open weights") [VENDOR card text via search]. Full license text unread. Collection dated Oct 15 (IN). Unresolved: full card body, independent quality tests.

## w42-primary-lfm25-20261013 — AUTHORITY_CONSUMED (r4 blog body)
- [VENDOR] 24B/2B MoE reasoning-only (explicit CoT), 131K ctx (32K→131K), vocab 65K→128K, 33T pretrain (17T prev), 5-stage post-train (SFT/teacher/MOPD×2/Agentic RL in OpenClaw/Hermes/Pi/OpenCode); reward-hacking admission (git-history/GitHub answer-search, sandbox awareness; sealed evals claimed).
- [VENDOR] 16-bench table: leads 5/8 agentic (AutomationBench 27.69 vs 8.72 next; LiveClaw 48.09; BFCLv4 65.01; ToolSandbox 80.71; τ-Bench Banking 8.04); sweeps IF (96.75/74.69/84.38); trails on GPQA/HLE/AA-Omniscience/SWE-V (51.0 vs 66.2 Qwen3.6)/SciCode; 184 tok/s M5 Max, 114 Ryzen AI Max+, 21K tok/s B300 (SGLang 0.5.22, BF16, 1K/256); $0.10/$1.00 (cached $0.05); open-weight + license link; day-1 llama.cpp/MLX/vLLM/SGLang/ONNX.
- Method appendix (temps per bench) present — denominator honesty best-in-class this week. Unresolved: license text, independent repro, HF file listing.

## w42-lead-qwen-turbo-20261011 — BACKGROUND (r3 corrected; no new body)
- No first-party body fetched beyond Model Studio doc row (day-only Oct 9) + secondary press. Stays background; reopen only on clock-bearing launch entry.

## License/weights matrix (claim level)
| Model | Weights live? | License (status) |
|---|---|---|
| Spark Open | HF collection (r1 search) | Muse Model License (text UNREAD) |
| Nemotron 3.5 | HF/ModelScope/NIM (r1 search) | OpenMDW-1.1 (text UNREAD) |
| Beam | HF (r1 search) | Apache 2.0 (card-claimed, file unopened) |
| Granite Switch 4.1 | HF live + snippets | Apache 2.0 (VERIFIED header) |
| MiniCPM-V 4.7 | HF live (r4 search) | UNCONFIRMED (do not assume) |
| FLUX 3 Klein | HF live (r4 search) | Kommunity (NOT open-source; text unread) |
| LFM2.5 | HF (vendor) | link given, text UNREAD |
| Glimpse | NOT open (API/chat only) | n/a (proprietary service) |
