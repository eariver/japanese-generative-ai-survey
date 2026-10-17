# r14 new source readings (edition-local sidecar; NOT accepted Evidence)

Status: `EDITORIAL_SIDECAR / NON_ACCEPTANCE / NO_CORE_CHANGE`
Date: 2026-10-18 JST. Reader: Muse (execution). Purpose: carry over r13 S1/S2 reads and add r14 S3a/S3b verification for M01/TECH-01. These readings do NOT rewrite accepted Evidence/Views, are not archived full-byte captures, and do not select new candidates. These readings do NOT rewrite accepted Evidence/Views, are not archived full-byte captures, and do not select new candidates.

## S1 — NVIDIA Nemotron 3.5 Super VL technical blog (live read)
- URL: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
- Title: "NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning"
- Authors: Chris Alexiuk, Chintan Patel. Dated: Oct 15, 2026 (page header).
- Accessed: 2026-10-18 JST via webfetch text (full body obtained live; NOT an archived byte capture).
- Sections read and usable:
  - LiLiCorr: open speculative decoding; joint evaluation across entire draft; compatibility network scores in a single pass; up to 2.3x faster token generation on DGX Spark; recommended low-latency drafter. (P3 expansion)
  - MTP: internal drafter proposes several tokens; main model verifies in one forward pass; accepting multiple tokens at once reduces verification steps. NO draft-length / greedy condition / numeric acceptance value stated in the sections read. (M01: supports "acceptance length, not rate"; does NOT support greedy/draft-7 qualifiers.)
  - QAD: quantized model learns to match BF16 outputs; KV cache in NVFP4 instead of FP8; no inference overhead because QAD happens during training. (P3 expansion)
  - Context reuse: prefix caching; Mamba recurrent states preserved; additional Mamba checkpoints reduce replay; internal checkpointing avoids extra model passes. (P3 expansion)
  - Dynamo: 16×B200, 50 tok/s/user, KV-aware routing, 8x users, −85% first-token latency; 600+ TPS AA agentic on Baseten endpoint. (P3 expansion)
  - MOPD: teachers score for video reasoning/tracking, vision tool use, alignment. (P3 expansion)
  - Post-train cases: Scale 40x cost/5x latency; Ramp +50%/10x; AI21 +41%; Indic +10B (IITM, 2.8T/22-lang). (Already in accepted card; corroborated here.)
  - EXO Labs: "An independent evaluation by EXO Labs placed [the model] on the Pareto frontier" — existence of the sentence confirmed; NO scores, NO method in the sections read. Kept OUT of draft (unchanged policy).
- Retrieval status: OK (live). Not independently archived.

## S2 — Earth AI GRA systematic evaluation paper, arXiv HTML (live read)
- URL: https://arxiv.org/html/2610.15750v1
- Title: "Google Earth AI Geospatial Reasoning Agent: Capabilities and a Systematic Evaluation"
- Authors: Noam Slonim et al. (Google Research / Google Geo / Spatial Bytes). License: arXiv.org perpetual non-exclusive. Dated: 11 Oct 2026 (arXiv header).
- Accessed: 2026-10-18 JST via webfetch text (abstract→§5 excerpts + tables obtained live; NOT an archived byte capture;unchanged accepted card remains the formal authority).
- Sections read and usable:
  - 4-configuration comparison on fixed Gemini model (standalone / +basic tools / +GRA tools reactive / full GRA); §5.1: GeoExpertQueries 63 vs unusable baselines; GeoKTools 86 vs 41 (standalone no-tool strongest baseline); CBGB >80 vs <20; Flash $0.199 vs $0.167 (+10.5pp for ~3 cents); Flash <1/3 Pro cost. (P6 expansion, m02-adjacent cost method)
  - Tool contribution: tools alone lift 3→52 (Flash, GeoExpertQueries); planning adds 52→63; searches 7.0→3.2/query; Earth Engine use 54% vs 38%. (P6 expansion)
  - Golden workflows: 3 independent experts blind to GRA/tools; consensus merge; 4 queries unreconciled and KEPT as informative (water-quality example). 101 queries (25 dev/76 test); GeoKTools 305 (85/220), 92 templates, 24 tool types, K=1–4. (P6 expansion)
  - Saturation: UnivEARTH standalone 87–94 (saturated; answers from published text without analysis); CBGB 45 external deterministic. (P6 expansion)
  - Execution limits (§3.4): max 100 LLM calls, 30-min wall clock, **1M-token context window** abort cap; 3 repeats; cost includes failures. → resolves m02: the "1M" cap IS the 1M-token context window. (m02 fix evidence)
  - Release: dev splits + autorater prompts + scoring code + GeoKTools solvers released. (P6 expansion)
- Retrieval status: OK (live). Long paper; only cited sections consumed; no claim beyond cited passages.

## Usage rule
r13 draft prose may cite S1/S2 section content with explicit "live-read sidecar" qualification where the accepted card lacks the detail; accepted Evidence remains the formal authority for Core validation. No new candidate selected on this basis.

## S3a — NVIDIA Nemotron 3.5 research page (live read, r14)
- URL: https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/
- Title: "NVIDIA Nemotron 3.5 Super and Lightning". Published: October 14, 2026. Document type: Technical Report (landing page).
- Accessed: 2026-10-18 JST via webfetch text (full body obtained live; NOT an archived byte capture).
- Sections read and usable:
  - MTP boosting improves average speculative-decoding acceptance length from 4.287 to 4.718 under greedy decoding and from 3.787 to 4.612 under probabilistic draft sampling. (M01 core fix: length, not rate; both conditions.)
  - 100B-token MTP warm-up; 1T-token distillation; Indic/Long-context/Agentic mid-training stages; long-context recovery 33.5→81.0.
  - Checkpoints list (Super VL 120B-A12B Base/BF16/NVFP4/LiLiCorr drafter; Lightning 30B-A3B variants).
- Retrieval status: OK (live). Full 79pp PDF itself not retained.

## S3b — Nemotron 3.5 Super Training Recipe, Stage 2 RL (live read, r14)
- URL: https://docs.nvidia.com/nemotron/latest/nemotron/super35/rl/index.html
- Title: "Nemotron 3.5 Super Training Recipe — Stage 2: Reinforcement Learning (RL)".
- Accessed: 2026-10-18 JST via webfetch text (MTP Boosting + methodology sections obtained live; NOT an archived byte capture).
- Sections read and usable (TECH-01, all verified):
  - MTP Boosting Table 8: average acceptance length on SPEED-Bench qualitative split at draft length 7; rows SFT native 4.589/4.048; SFT+4K 5.080/4.730; Final native 4.287/3.787; Final+MTP-head 4.528/4.436; Final+25K boosting (released) 4.718/4.612 — columns greedy temp-0 / sampled temp-1.
  - Boosting +10.1% greedy / +21.8% sampled, largest per-position gains at deeper draft positions; cross-model sampled best 4.612 (Gemma-4 31B 4.565; Qwen3.5 4.331; Qwen3.8-Flash-Next ≤4.213); greedy Gemma-4 4.837 / Qwen3.5 4.799 higher.
  - Recipe: 5 repeated detached MTP heads, loss 0.3 per config (reference runs varied); policy MTP speculative decoding OFF except reasoning teacher; backbone frozen, hidden-state mixing, LK distillation; temp-1 ≤8K on-policy rollouts; recipe does NOT include MTP boosting (report trains separately).
  - MOPD phases with prompt shares (35/25/20/15 + 5% self-anchor; 30/20/20/20 + 10%); agentic-teacher edge DASHED = unconfirmed lineage (must stay unconfirmed).
- Retrieval status: OK (live). Table 8 values quoted verbatim in r14 P3.
