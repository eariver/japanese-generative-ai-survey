# Currency Sweep Record — cutoff 2026-09-30 (r13 repair pass)

- Date: 2026-10-03 JST
- Cutoff context: `production-profile.json` temporal_policy `OPEN_HISTORY_AS_OF = 2026-09-30T00:31:34Z`; discovery observations `observed_at 2026-09-30T00:38:52Z`.
- Method: official-source read-only verification only. No new candidates, no Discovery, no Evidence created by this record.

## 1. Gemini 3.7 Flash — EXCLUDE (as standalone TS-003 anchor)

- Verified: exists; official date 2026-08-13 (blog.google Introducing Gemini 3.7 Flash; ai.google.dev model page + changelog "August 13, 2026 Gemini 3.7 Flash GA").
- Summary: efficiency-tier Flash workhorse iteration for coding/agents; same 1M-input/65K-output envelope (Text/Image/Video/Audio/PDF in, Text out); gains are coding/agentic benchmarks at half 3.6 price. No context/tokenization/fusion/time-alignment mechanism change.
- Reason: point-release iteration with no P09 context-economics mechanism delta; closed-endpoint version churn is at most a deployment case, not a lineage node.

## 2. Gemini 3.8 Flash — EXCLUDE (as standalone TS-003 anchor)

- Verified: exists; official date 2026-09-02 (blog.google 3.8 Flash + 3.8 Flash Cyber; deepmind model card "Published 2 September 2026"; ai.google.dev page + changelog GA).
- Summary: same Flash envelope (1M input context); "most intelligent Flash" for long-horizon SWE/agents. Only P09-adjacent datum is its LVBench long-video row 87.8% agentic vs 87.1% static — evidence for item 3, not a mechanism.
- Reason: no D09 mechanism delta; Cyber variant is cybersecurity post-training, outside TS-003 scope.

## 3. Agentic video understanding — INSPECT (pipeline referral, NOT admitted)

- Verified: exists; official date 2026-09-01 (blog.google introducing-agentic-video-in-gemini; ai.google.dev changelog: dynamically navigates video timelines, requesting transcripts, frames, or audio tracks on demand; up to 88% fewer tokens for long-form content; mechanism detail at video-understanding docs).
- Summary: replaces default static 1-FPS full-timeline ingest with a goal-directed loop — dynamic timeline exploration, selective transcript inspection, adaptive frame rate/resolution, on-demand transcript/frame/audio loading. Official conditions: up to 88% fewer tokens AND up to 66% lower cost AND up to ~7% higher quality — ceilings across standard video analysis benchmarks / for long-form content (launch chart: Gemini 3.7 Flash on LongVideoBench). Supported models: 3.8/3.7/3.6 Flash + 3.5 Flash-Lite. Caveats: navigation may increase TTFT on short clips (<5 min); nav reasoning billed as thinking tokens, on-demand media as tool prompt tokens.
- Reason: directly load-bearing for P09 context/KV/memory/latency economics and P11 long-video vs streaming contract; quantified load-only-what-is-needed mechanism with stated conditions. Requires formal Discovery admission + Evidence body consumption (benchmark conditions, LongVideoBench scope, cost/token/quality separation) through the governed pipeline — explicitly NOT admitted by this sweep record.

## 4. Gemini Omni Flash — EXCLUDE

- Verified: exists (ai.google.dev omni + video docs; model gemini-omni-1.1-flash; Text/Image/Video≤10s in, Video 3–10s out; GA 2026-08-27; preview from I/O).
- Summary: text/image/video→video generator + multi-turn conversational editor (extend, interpolate, resolution control, subject reference).
- Reason: generative endpoint; profile exclusion assigns generation lineage to TS-002; TS-003 D14 keeps only non-generative-predictive or action-conditioned-simulation poles, D09 input-side fusion only. Cross-reference at most.
