# W43 primary bundle 01 — frontier agents and deployment (claim-level, 2026-10-24)

Collector run: `20261024T120000Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-24T12:00:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.
No original HTML/PDF bytes captured in this environment; all bodies are search-confirmed claim notes. Full-body consumption is an explicit gap for Evidence.

## 1. Anthropic Claude Duet (Oct 21, 2026) — BODY SEARCH-CONFIRMED
- URL: https://claude.com/resources/articles/claude-duet (page shows Oct 21, 2026, 5 min read).
- Corroboration: NYT 2026-10-21, CNBC 2026-10-21 17:42 EDT, The Verge 2026-10-21 19:53 UTC, TechCrunch 2026-10-22, Reuters via Tacoma Tribune 2026-10-21.
- Claims (vendor + secondary, unvalidated):
  - Research preview by waitlist, US Pro/Max first, existing usage limits; iOS/Android/claude.ai.
  - Proactive agent: daily brief, monitors connected apps, completes tasks (scheduling, dashboards, financial forecasts, web apps), keeps working when away, checks before key actions.
  - Runs on Opus 5.5; 6000+ connectors/plugins via Marketplace; Stripe Link / Shopify Shop Pay for purchases with user approval for sensitive steps.
  - Safety: model-level training + Claude Code / Managed Agents safeguards + auto-mode classifier approval + VM background work; passwords/tokens not seen.
- Timestamp: IN-WINDOW (Oct 21). Status: CAPTURED_BUT_UNCONSUMED (official page not fully read). Evidence must fetch page + safety/connector docs + independent repro.

## 2. Anthropic auto-mode default (announced ~Oct 21) — X-LEVEL ONLY
- Locator: x:claudeai/status/2113360845409583307 (Starting next week, sessions across web/desktop/mobile run in auto mode by default on Pro/Max/Team).
- Status: LOCATOR_ONLY, no primary page body. Evidence must pin official changelog/docs.

## 3. OpenAI on Google Cloud + Decisions API + Patch the Planet (Oct 21-22)
- URLs: https://openai.com/index/openai-models-google-cloud (Oct 21), https://openai.com/index/decisions-api (Oct 22), https://openai.com/index/patch-the-planet (Oct 21 per RSS), plus AT&T legal (Oct 21), FDE (Oct 21), ChatGPT Ads 26 countries (Oct 21), Uber ChatGPT Work (Oct 22), bio research leads (Oct 21).
- Claims (RSS-level only):
  - Frontier models + Codex workflows in Gemini Model Garden via GCP Marketplace.
  - Decisions API: fast/focused/low-cost decisions for any application.
  - Patch the Planet: global response coordination as agents uncover critical vulns.
- Status: LOCATOR_ONLY (RSS titles, no bodies). In-window but unvalidated. Evidence must fetch each page.

## 4. Meta Muse 10M users, shopping top activity (Oct 21 earnings)
- Locator: TechCrunch 2026-10-21 via poweredbyai (Q3 earnings call; Sensor Tower estimate corroboration).
- Claims: 10M+ Muse adoption; shopping top activity; Zuckerberg: Muses working with friends/family Muses; agentic purchase via business agent.
- Status: SECONDARY_CLAIM_ONLY. Industry signal, not technical release. Context at most; never standalone package.

## Gaps
- Duet page body, safety framework, connector/Marketplace docs, pricing/limits: UNCONSUMED.
- OpenAI pages: UNFETCHED.
- Independent Duet repro/benchmarks: NONE found in this pass.
