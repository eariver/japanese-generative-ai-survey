# W43 lane coverage matrix r1 (2026-10-24)

Window: UTC `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`. End exclusive. Event time controls, not scrape time.
Collector: `20261024T120000Z-muse-r1` (6 bundles, 0 full bodies consumed, 0 independent repros).
Discovery: `discovery-v2-proposal-r1.jsonl` (36 records, PROPOSED_NOT_ACCEPTED, 36/36 schema PASS).
X: `REQUIRED_BY_PROFILE`, `AWAITING_GROK`, `X_INTAKE_PENDING` — no Grok bytes, no fabrication.

| Lane | Covered | Families (discovery IDs) | First-party raw | Consumed | Gap |
|---|---|---|---|---|---|
| (a) frontier labs | YES | duet, automode, openai-cloud, decisions-api, muse-10m | claim notes only | 0 | Duet page body, OpenAI pages unfetched |
| (b) open models/repos/licenses | YES | kimi, deepseek-1017, nemotron-e4b, step5-bg, qwen-bg | claim notes only | 0 | Kimi blog, DeepSeek card, Nemotron PDF, license files unread |
| (c) arch/MoE/efficiency/quant/ctx | YES | kimi MoE, step5 MoE, deepinfer, unsloth quant | claim notes only | 0 | Kernels, parallelism, quant recipes unread |
| (d) pretrain/posttrain/synth/data | PARTIAL | step5 training blog (bg), deepseek post-train, kimi factuality | claim notes only | 0 | Pretrain tokens, synth pipelines thin |
| (e) eval/independent benchmarks | YES | am-bench edge, or-license edge, oracle-rev, AA via speech/video/kimi | claim notes only | 0 | All paper bodies + AA methodology unread; zero independent repro |
| (f) agentic coding/runtime/enterprise | YES | github-teams, github-metrics, github-deprecation, tanstack, harness | changelog-level | 0 | Changelog bodies, TanStack tag, harness docs unpinned |
| (g) speech/audio/image/video/vision | YES | voxtral, eleven, flux-max, qwen-bg | claim notes only | 0 | Announcement/docs/evals unread |
| (h) robotics/embodied/science | PARTIAL | trade signals (JLS/Bear/Unitree/FLAIR), AHA/FDA, OR-license | trade-press only | 0 | No technical disclosure; science bench thin |
| (i) safety/security/alignment/legal | YES | gemini-safety, patch-planet, EU STOA, kimi cyber removal, licenses | claim notes only | 0 | Safety PDFs, license texts unread; allegation quarantined |
| (j) X/Grok community | PENDING | x locators (kimi/duet/deepinfer/nvidia) | NONE | 0 | `X_INTAKE_PENDING`; Grok task ready, result absent |
| (k) deployment/product/industry | YES | openai-cloud, vercel/ollama, muse-10m, tanstack, github | claim notes only | 0 | Pricing/docs unvalidated |

Zero-coverage claim: NONE. Every lane has at least one lead, but (d) and (h) are thin and (j) is pending. Zero bodies consumed and zero independent repros are honestly marked as zero, never PASS.
