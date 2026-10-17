# W42 r2 bundle — full-body upgrades: Wonder, Spark Open, Maia 300, Nemotron 3.5 + Bolts, Glimpse, Beam card/safety (2026-10-17)

Collector run: `20261017T071000Z-muse-r2` / collector_id `primary-webfetch`
Observed at: `2026-10-17T07:22:00Z`
Upgrades r1 SEARCH_CONFIRMED → BODY_CONSUMED (claim-level derived notes; full-byte archives still absent).

## 1. Muse Wonder official blog (about.fb.com, Oct 12, updated Oct 13) — BODY CONSUMED
- Frontier agentic family on Muse Spark groundwork; expert domains law/finance/health + frontier coding; Active Memory (cross-conversation context) + Active Focus (persist/try-alternatives/recover, clarify + check-in before important acts) — definitions source-backed.
- Safety: no private-info sharing without permission; refuse harmful acts; cyber dual-use allowed for defenders; Meta Superintelligence Scaling Framework; FULL REPORT SOON (pending — gap).
- Pricing/benchmark numbers NOT on this page (live on dev blog/API: $4/$20 per r1 search; AA 52/56 max-effort per Daily X) — denominator gap preserved; research-blog pointer for build/test details (unfetched).

## 2. Muse Spark Open research blog (research.meta.ai, Oct 15) — BODY CONSUMED
- 816B/42B, 1M ctx; desktop-first: 2× M5 Ultra (512 GB each, 1.2 TB/s) behave as 1 TB Supercomputer; on-device agentic workflows demoed (Ice Cubes iOS changes, DaVinci Resolve frame review).
- Helion auto-tuned kernels in SGLang: 1.03–3.95× kernel-level (NVIDIA+AMD), 3% end-to-end on AMD MI350 (vendor).
- Safety: extra post-training for standalone; Scaling Framework thresholds met; MODEL CARD NOW, full evaluation report SOON (pending).
- License: Muse Model License, limited commercial, free for many (full text unread — gap); HF collection link given.
- Benchmark section exists but numbers sit behind evaluation-methodology report link (unfetched — denominator gap).

## 3. Maia 300 architecture deep dive (azure.microsoft.com, Oct 12, Borkar/Dighe) — BODY CONSUMED
- SDLA dataflow; UMA→NUMA chiplets; MXFP4 + sub-3-bit storage; vector ISA (softmax/cast); N2P compute die + bandwidth/IO dies (+36% FLOPs, 2.5× HBM BW, +14% scale-up BW).
- 8× HBM4 = 288 GB @ 18 TB/s per accelerator; 2.5× BW, +33% capacity, ~2× BW/W vs Maia 200.
- Network: custom Ethernet AI transport; half-switched in-rack (96 pod); optical tier-2 to 12,288 superpod; disaggregated prefill/decode; 750 GB/s peer; hot-spare racks.
- Rack: 96 tray in 167 kW; 6 switch ASICs; 50 V busbar + ATS; >80% liquid cooling; datacenter telemetry/RAS.
- Delivers: up to 7× rack token throughput + >2.5× perf/W vs Maia 200. 2027 production; Ignite Nov 2026 more. Related Oct 16 post on open-weight risk noted (unfetched).
- Efficiency baseline STILL unnamed GPU/config (vendor-only; nobody outside MS can test — honesty preserved).

## 4. Nemotron 3.5 Super VL developer blog (developer.nvidia.com, Oct 15, Alexiuk/Patel) — BODY CONSUMED
- Denominators now source-backed: CharXiv 80.8% (84% w/ code) vs Nano Omni 63%; Hermes 63.44% vs Ultra 56.33%; LangChain 87.05% vs 84.3%; Scale 40× cost/5× latency; Ramp 50% throughput/10× latency; AI21 +41% acc; Indic +10B tokens w/ IIT Madras (2.8T/22-lang set released); EXO Labs Pareto (independent); Dynamo 8× users/−85% TTFT; 600+ TPS AA agentic on Baseten.
- Training: Ultra-distilled, MOPD multi-teacher, SkewReverse loss, MTP-boost, LiLiCorr (2.3× on DGX Spark), NVFP4-QAD, prefix/Mamba-state reuse; 40 VL + finance/tool/chat datasets on HF; NeMo/cookbook/NIM.
- Siblings: Lightning 30B/3B text (related post); post-training partners (Scale/Ramp/AI21/Harvey/Perplexity).
- License: OpenMDW-1.1 per model card (r1; full license text unread — gap).
- BOLT available-vs-future: Super VL + Bolt 74B-A9B (24 GB) AVAILABLE NOW; Bolt E4B (4 GB) coming Oct 23 — FUTURE, outside W42 window (do not claim as W42 availability).

## 5. Glimpse official blog (elorian.ai, Oct 16) — BODY CONSUMED (full benchmark table)
- Table (max effort; HSS paper-reported): WGO 42.70 / ERQA 83.75 (tie Astra) / BabyVision 95.36 / HSS 46.36 (Astra 53.6, Sol 46.6, Opus 44.6) / CharXiv-R 92.90 / UGC-VideoCap 82.66 / DREAM-1K 76.04 / TOMATO 93.60 / Video-MME v2 56.68 / E.T. 63.55 / FSC-147 83.36 / CountQA 82.66.
- Pricing: in $0.60 vs Astra $10.00 / out $3 vs $50 (94% lower; table-backed). VLA planning $0.035 vs $0.249 Astra.
- Base model UNDISCLOSED ("post-trained on an open weights base model") → weights NOT open; API + chat only. Token efficiency = next focus (looking closely costs tokens). Direct action = future work. HSS benchmark vendor-built (credibility note kept).

## 6. Beam model card + safety (reflection.ai/beam-model-card) — BODY CONSUMED (headers + tables)
- 501.3B/23.4B MoE; 52 layers (3 dense + 49 MoE); Gated GQA + SWA; 1M ctx; 152k vocab; 256 experts; BF16/FP8/NVFP4; cutoff Jun 30 2026; English-dominant.
- Benchmarks (temp 0.7/top_p 0.99, vendor): DeepSWE 43.3 / SWE Pro v2-Hard 78.6 / Verified 81.6 / Terminal-Bench 80.1 / AIME 97.7 / HLE 36.0 (51.1 w/ tools) / GPQA 90.6 / MCP Atlas 80.8 / BrowseComp 76.8 — full table captured.
- Safety ISE (in-house, soon-OSS): harmful refusal ~89%, harmless compliance ~82%; Open Safety Framework + third-party assurance + full Safety Technical Report (report body unfetched — gap).
- Distillation explicitly NOT prohibited (fine-tune/quantize/merge/distill allowed); commercial + research use; usage policy + legal (privacy/export) caveats.
