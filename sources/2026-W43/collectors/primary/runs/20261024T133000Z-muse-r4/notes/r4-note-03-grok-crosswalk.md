# W43 r4 Grok 12-lane crosswalk vs r3 11-lane research (X-03)

Grok Raw: `sources/2026-W43/external/x/weekly-x-2026-W43/weekly-x-2026-W43.md` (13425B, SHA `4571e0de…`, observed `2026-10-24T12:43:17Z`, PARTIAL sensor observation — NOT Evidence, NOT Selection).

| Grok lane | Grok status | r3 correspondence | r4 treatment |
|---|---|---|---|
| A. Foundation/Reasoning | SELECTED (Kimi, Beam, Muse Spark, DeepSeek, Mercury 3) | Kimi ✓ IN; Beam OUT; Muse Spark OUT; DeepSeek 1017 ✓ IN; Mercury 3 unsupported | Kimi/DeepSeek retained; Beam/Muse OUT kept; Mercury 3 parked (no post ID, no primary) |
| B. Agents/Coding/Harness | SELECTED (Flint, Beam, Muse Spark, Duet, Dojo, Bolt) | Flint MISSING in r3; rest covered/OUT | **Flint added (new family)**; Dojo parked (no IDs) |
| C. Multimodal | SELECTED (Kimi, Nemotron Super VL, Muse) | ✓ covered | Retained |
| D. Image | CANDIDATE_NOT_SELECTED (sparse) | No standout (consistent) | Retained as sparse; no candidate |
| E. Video | NONE_FOUND_CONFIRMED | **FLUX 3 Max video Oct 19 (r2 primary)** | X-signal-only negative ≠ global veto; FLUX retained. Grok E is sensor coverage, not Source Intake verdict |
| F. Speech/Audio | SELECTED (Voxtral + SDK) | ✓ covered | Retained |
| G. Open/Local/Quant | SELECTED (Kimi pending, Flint, Beam, Muse, Nemotron 4GB, Sage) | ✓ except Flint/Sage | Flint added; Sage quants parked (no IDs/primary) |
| H. Inference/Serving | SELECTED (SGLang+Muse, speed claims, OpenAI-on-GCP, Beam throughput) | ✓ covered | Retained |
| I. Memory/Multi-agent | CANDIDATE (Agent Dojo, OpenClaw) | **MemT Oct 19 (r2 primary)** | X-signal-only; MemT retained (primary technical authority beats sensor sparsity) |
| J. Evaluation | SELECTED (AA, Terminal-Bench, community) | ✓ covered | Retained; all vendor numbers still unreproduced |
| K. Safety/Security | SELECTED (OpenAI internet-cut; AFM music campaign) | OpenAI securing ✓; AFM not in r3 | AFM "Human Made" parked (no primary, no post ID) |
| L. Other | CANDIDATE (Dojo, GitHub autofix sparse) | Thin (consistent) | Parked as leads; no GitHub X elevation |

## Genuinely new vs duplicate vs OUT vs unsupported
- New (added r4): Flint (Oct 21 first-party + Grok-observed).
- Duplicates (no new row): Kimi pinned post = r3 `w43-primary-kimi-20261023`; Muse Spark pinned post = OUT background (Oct 15); Nemotron Bolt mentions = r3 row; Voxtral/Duet/DeepSeek mentions = r3 rows.
- OUT confirmed: Beam 1.0 weights (Oct 16 13:01Z); Muse Spark weights (Oct 15); Liquid LFM2.5 (pre-window per Grok).
- Unsupported/quarantined (generic claims, no post IDs, no primary): Mercury 3, Mammoth/Elephant, Sage-A1.5 quants, Perplexity Decider updates, Agent Dojo/OpenClaw campaigns, AFM campaign, "125+/150+ tok/s" beyond Flint publisher claim, engagement metrics/likes. Never elevated to candidates.

## Pinned-post inventory (exact IDs present in Grok Raw)
1. `https://x.com/Kimi_Moonshot/status/2113680701770068067` (Kimi official, ~17:15Z Oct 23) — binds existing Kimi event.
2. `https://x.com/lm_zheng/status/2110889415895234942` (Lianmin Zheng/Meta-affiliated, ~Oct 16) — Muse Spark + SGLang pairing note (adoption signal for OUT weights).
All other community claims: no exact IDs. Post timestamps/engagement as returned by X search; secondary amplification may continue post-cutoff (Late Breaking noted by Grok, not adopted here).
