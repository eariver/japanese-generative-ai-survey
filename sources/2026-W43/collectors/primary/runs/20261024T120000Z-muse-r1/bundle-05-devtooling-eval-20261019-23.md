# W43 primary bundle 05 — agentic devtooling, runtime and evaluation (claim-level, 2026-10-24)

Collector run: `20261024T120000Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-24T12:00:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. GitHub platform (Oct 19/22/23) — IN-WINDOW, CHANGELOG-LEVEL
- URLs:
  - https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams (Oct 23)
  - https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode (Oct 23, totals_by_client, OpenCode newly captured)
  - https://github.blog/changelog/2026-10-22-github-copilot-in-visual-studio-september-update-2 (Oct 22)
  - https://github.blog/changelog/2026-10-19-github-copilot-models-deprecated-on-october-19-2026 (Oct 19 deprecations)
  - https://github.blog/changelog/2026-10-15-copilot-in-slack-and-teams-adds-model-and-repository-updates (Oct 15, OUT background for multi-repo)
  - https://github.blog/changelog/2026-10-13-gemini-4-argon-in-github-copilot (Oct 13, OUT background distribution proof)
- Claims: Teams notifications→Copilot code (issue/PR + thread context, reproduce/test/fix/PR); usage metrics now include OpenCode etc.; model deprecations Oct 19 (list unpinned here).
- Status: LOCATOR_ONLY (changelog bodies not fully read). Evidence must pin each changelog + docs.

## 2. TanStack AI 1.0 (Oct 23, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- URLs: https://tanstack.com/blog/tanstack-ai-1-0 (Oct 23), MakeBetter 2026-10-23, AI Agent Reviews 2026-10-23.
- Claims:
  - 76 stable packages, 23 provider adapters (+OpenAI-compat), 8-11 UI/sandbox integrations; portable skills/subagents/computer-use/MCP; 140+ contributors.
  - Harness explicitly EXPERIMENTAL (0.x); client/server + all stable pkgs must upgrade together; threadId required; 3 older UI pkgs have no 1.0.
- Status: CAPTURED_BUT_UNCONSUMED. Evidence must fetch blog + upgrade guide + repo tag.

## 3. Evaluation and safety papers/docs — MIXED, mostly leads
- arXiv 2610.24264 AM-Bench (submitted Oct 16): agentic misalignment taxonomy, 35 scenarios, 7 industries, fraud-triangle. Date precision: day-only; time vs 22:00Z cutoff UNPROVEN — treat as EDGE/UNRESOLVED, background unless time pinned.
- arXiv 2610.24087 OR-License (submitted Oct 16): 31 instances, 10 industrial OR scenarios, $3.68M engagements. Same cutoff uncertainty.
- arXiv 2610.16067v2 (revised Oct 21): agent-eval oracle failures; 4194→2883 replay, 94.3→65.5% — methodology caution, but Oct 12 v1 is OUT; v2 revision is IN as correction signal.
- Gemini 4 Argon Safety Report (Oct 2026 PDF): radicalization/fraud/illegal-access, pattrn.ai external eval — doc exists, body UNREAD.
- Google Cloud Gemini Enterprise safety overview (Oct 22 docs): eval taxonomy — LOCATOR_ONLY.
- EU STOA study Oct 19 (PE 788.151): GenAI in scientific exchange — secondary, context only.
- AHA→FDA GenAI device feedback Oct 19: benchmarking + clinical confirmation — regulatory context, not model release.
- Status: ALL UNCONSUMED. No Selection value claimed.

## 4. Other in-window signals (leads, thin)
- Agentic AI Foundation: Agent Skills (Anthropic) + Open Responses (OpenAI) + OpenEnv (HF) + OpenSandbox (Alibaba) under vendor-neutral governance (reported Oct 24 AI Agent News; primary dated proof needed; post-cutoff risk).
- OrcaCyber Zero 1.5 (Oct 10, OUT), OrcaCyber DeepSeek Abliterated (Oct 23 listing, vendor page only) — do not cite as primary.
- MiniMax M3.1 Flash / Mercury 3 (Oct 19 listings), Flint / Mammoth-1/Elephant-1 (Oct 21 listings) via NoCode tracker — SECONDARY_LIST_ONLY, no primary bodies; must not become candidates without primary.
- JLS Vision AI / Bear KINO-2 / Unitree anniversary / FLAIR Hub (Oct 20-23 robotics trade signals) — trade-press only, no technical disclosure; background at most.

## Gaps
- All changelogs/docs/papers: UNCONSUMED.
- Primary bodies for tracker-listed models: NOT FOUND in this pass.
