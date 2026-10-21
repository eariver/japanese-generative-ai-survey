# W42 r2 bundle — paper abstracts + strengthened leads + bounded lane sweeps (2026-10-17)

Collector run: `20261017T071000Z-muse-r2` / collector_id `primary-webfetch`
Observed at: `2026-10-17T07:25:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES` + live search excerpts.

## 1. Papers (abs-level: title/authors/dates/abstracts consumed; PDF bodies unparsed — logged limitation)
- PAT/Deep Review paper arXiv 2606.28277 (submitted Jun 26 2026 — OUT-of-window background): 4-level collaboration taxonomy; PAT +34% zero-shot recall on math errors (SPOT); STOC+ICML pilots. The W42 event is the Oct 14 LAUNCH, not the paper.
- Earth AI report arXiv 2610.15750 (submitted Oct 11 2026 16:31 UTC — IN-window; 39 pp; 37 authors): GRA system + 4-benchmark eval (GeoExpertQueries/GeoKTools new, dev splits on GitHub; CBGB/UnivEARTH external, UnivEARTH saturated 93.6%); tools = largest step, planning adds open-ended gain, Flash ≥ Pro cheaper.
- AgentHorizon arXiv 2610.11050 (submitted Oct 8 2026 01:03 UTC — IN-window; 10 authors incl. Xing Han Lu = Daily X @xhluca author match): 1,373 tasks / 166 h / 3 OS; paired instruction-swap negatives; 3 splits (AH/AH-S/AH-D); 11 judges; best GPT-5.5 80.9%; tool-use hurts open-weights. Strengthens r1 paper lead to IN-window + author-verified.
- Grad-counterexample application paper arXiv 2610.07304 (submitted Oct 5 2026 — OUT-of-window): symmetry-breaking stellarator generalization (Issan/Citrin/Landreman/Tracey). Background for Argon's fusion claim; Argon's use is IN, paper is OUT — chronology preserved.
- Sakana MLR / harness-17 / Amazon world-model PDFs: still unfetched (locator-only; Evidence gap retained).

## 2. Qwen lane (strengthens r1 weak lead; independent queries 2026-10-17)
- Qwen-Image-2.1-Turbo: OPEN-WEIGHTS release Oct 9 2026 (in-window; 8 denoising steps) + Pro/Turbo hosted APIs Oct 14 (in-window; Model Studio release log) — upgrades r1 "Qwen Turbo" from UNVER to dual-triggered (open checkpoint + APIs). Base 2.1-Pro listed Oct 2 (OUT background).
- QwenGyre OSS (RL framework for hour-long agents; 44% faster on 2.4T Qwen3.8; NL2RepoBench 52.48→58.54%): announced Oct 12–13 (secondary press; paper Sep 27 OUT) — observed but OMITTED from proposal (no first-party body fetched; press-only). Recorded here, not proposed.
- Qwen3.8-Omni-Flash (blog Sep 14 OUT; API listing Oct 13) + Flash-Next 685 tok/s claim (Oct 14 vendor) — background/context only.

## 3. AWS lane (first bounded sweep; secondary roundup + change tracker)
- AWS Weekly Roundup Oct 13 (in-window): Haiku 5.5 on Bedrock (−75% vs 4.5, effort controls) + Nova 2.5 Sonic voice GA (7 langs, 256K, Strands Bidi GA) + GPT-6.1 Sol GA on Bedrock (Oct 12 per change tracker) + Sonnet 4 EOL Oct 14. Distribution/availability events (no AWS-native model); proposed as ONE distribution record (secondary-vendor roundup, not independent).
- Strands Box/Continuum preview, Prime Day infra numbers: noted, not proposed (preview/non-AI).

## 4. DeepSeek lane (negative finding — do NOT manufacture)
- V4.1 Flash Sep 10 OUT (552B/8B-16B/1M/MIT); V4.1 Pro UNRELEASED as of Oct 16 (gated-testing rumors, 16% market odds, no card/price/bench) → NO in-window DeepSeek event. Omitted with this evidence.

## 5. JP lane (negative finding)
- ELYZA Thinking/RSI Research Oct 2 OUT; Sakana Namazu Mar 2026 OUT; Fugu Max/Ultra Oct 1 OUT → NO in-window JP-lab primary. Omitted with evidence (queries: ELYZA/Lightblue/Sakana/Kotoba).

## 6. Serving/perf + HF lanes
- TokenSpeed 685 tok/s (Qwen3.8-Flash-Next, Oct 14 vendor claim via @Alibaba_Qwen) + EXO Labs Pareto (via Nemotron blog) + vLLM day-0 (Spark/Beam) — folded as evaluation context into existing records, no standalone records.
- HF lane covered via Granite blog+card + HF model pages (Spark/Beam/Granite); Falcon ASR remains one-liner (omitted).

## 7. Grok-scale correction (r1 crosswalk promised a record that does not exist)
- 6-7 Grok Bot scale post (2026-10-15 22:52Z, Weekly-IN): r1 crosswalk listed w42-dailyx-grok-scale-20261015 but r1 proposal NEVER contained it. r2 ADDS it honestly as X-observed lead (no usage stats) and documents the correction in the r1→r2 diff.
- Omitted-in-r1, still omitted (reasons stand): 1-5 rumor, 1-7 tips, 1-10 demo, 1-11 routing-obs, 2-4 rsiarena-unver, 2-6 mcp-discussion, 2-10 digest, 2-12 falcon, 3-9 coinbase-ctx, 3-10 guides, 5-5 apple-press, 5-6 desktop-unaffiliated, 5-8 enforcement-unver, 6-8 ling-digest, 7-10 export-unver, 7-12 anecdote (16 topics; full reasons in crosswalk r2).
