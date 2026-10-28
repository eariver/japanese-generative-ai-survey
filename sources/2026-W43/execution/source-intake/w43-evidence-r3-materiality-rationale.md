# W43 Evidence r3 materiality rationale — editor-facing (32 Cards + 51 ledger)

Status: `EDITION_LOCAL_EDITORIAL / R3_INTEGRATED / NO_SELECTION`
Date: 2026-10-25 JST. Work branch `weekly/2026-W43-v2-work`. New acceptances: Evidence `dbc27cd8…` (32 PARTIAL), Views `7a812053…` (MATERIAL 20 / CONTEXT 11 / NON_MATERIAL 1), Ledger `31929cf5…` (51 rows), Completeness `abd6dadf…` (LIMITED).

Canonical ledger `rationale` for non-DROP remains frozen-Core tautology (`Screening=X; Edition View=Y`) by design; DROP rows carry exclusion reasons. This document is the editorial basis the ledger cannot express. View `materiality.rationale` in r3 Cards carries the same per-ID basis below (non-tautological). No Selection is implied; 20 MATERIAL are potentially important, not 20 guaranteed stories.

## 32 Cards

- `w43-primary-kimi-20261023` MATERIAL — Late-window open-weight frontier (K3.1 Pro 1M ctx, API live 17:15:24Z 4h44m36s inside cutoff, weights Nov 4 FUTURE). Novelty high, proof vendor harness + X/blog split, duplication none, IN.
- `w43-r4-flint-20261021` MATERIAL — Local coding MoE 39.8B/2.5B, 512K capability/256K guidance pinned, Apple/RTX speed with apparatus. Novelty high, proof vendor (article + card split), IN.
- `w43-primary-deepseek-20261017` MATERIAL — 1017 API/model/tooling identity with real identifiers + weight SHA pending. Novelty moderate, proof partial, IN.
- `w43-primary-deepinfer-20261020` MATERIAL — Production inference OSS with exact env-var correction pinned to commit. Novelty high operational, proof code bytes, IN (repo OUT Oct16 vs announce IN Oct20 split).
- `w43-primary-voxtral-20261020` MATERIAL — Speech STT/TTS with eval conditions. Novelty moderate, proof vendor, IN.
- `w43-primary-eleven-20261020` MATERIAL — Realtime voice with AA/protocol/TTFA gaps. Novelty moderate, IN.
- `w43-primary-flux-max-20261019` MATERIAL — Video model with publisher arithmetic contradiction preserved (22x vs 26.5x). Novelty high reader-relevant, proof contradictory vendor, IN.
- `w43-primary-tanstack-20261023` MATERIAL — AI 1.0 core vs 0.x harness. Novelty moderate, IN.
- `w43-r2-1password-20261022` MATERIAL — Agent credential plane (approval injection, no-secrets) with live-vs-coming-soon bound. Novelty high safety, proof vendor, IN.
- `w43-primary-duet-20261021` MATERIAL — Proactive agent with permission/credential architecture. Novelty high, proof vendor, IN.
- `w43-r2-memt-20261019` MATERIAL — Memory-native foundation (MoS, 34B, 1.86x/66x) with license split corrected. Novelty high, proof author, IN.
- `w43-r2-ming-20261019` MATERIAL — Open TTS with publisher-cited AA ranks (AA unfetched). Novelty moderate, IN.
- `w43-primary-automode-20261021` MATERIAL — Auto-mode Oct22 update (Aug7 OUT) with future default rollout. Novelty process, IN (update).
- `w43-primary-decisions-api-20261022` MATERIAL — Decisions API GA with 400Q eval + footnotes. Novelty high dev-tooling, IN.
- `w43-r2-openai-bio-20261021` MATERIAL — Coauthored research-team protocol + blinded preference (not independent repro). Novelty high method, IN.
- `w43-r2-openai-lowresource-20261019` MATERIAL — Published eval protocol + open suite (not independent eval). Novelty high, IN.
- `w43-r2-openai-securing-20261023` MATERIAL — Frontier containment (provided attack data, incident vs countermeasure). Novelty high safety, IN.
- `w43-primary-nemotron-e4b-20261023` MATERIAL — Compact MoE with OpenMDW-1.1 boundary (OSI unverified). Novelty moderate, IN.
- `w43-primary-patch-planet-20261021` MATERIAL — Coordinated disclosure (GPT-5.6 Sol, maintainer-led, 5-stage) with CVE-proof withheld. Novelty high process, IN.
- `w43-r2-moss-trainer-20261018` MATERIAL — Third-party training efficiency (custom license, unreproduced). Novelty moderate tooling, IN.
- `w43-lead-oracle-revision-20261021` CONTEXT — Revision event only (v1 OUT, v2 IN); substantive delta UNRESOLVED. Bibliography, not new research.
- `w43-r2-ambench-v2-20261020` CONTEXT — Revision event only; delta UNRESOLVED. Bibliography.
- `w43-primary-openai-cloud-20261021` CONTEXT — Distribution via private preview (not new model). Ops signal, IN but CONTEXT.
- `w43-primary-github-metrics-20261023` CONTEXT — Metering change (exact enum + request-not-prompt). Methodology, IN but CONTEXT.
- `w43-primary-github-deprecation-20261019` CONTEXT — Model deprecation + migration. Ops hygiene.
- `w43-primary-github-teams-20261023` CONTEXT — Teams integration with permission limits. Integration.
- `w43-r2-moss-api-20261020` CONTEXT — API README mention without deployment proof. Mention only.
- `w43-r2-moss-report-announce-20261019` CONTEXT — Announcement of OUT body. Bibliography.
- `w43-carry-7151fcdc6c3ee392` CONTEXT — X-only gzip support signal, no causal measure.
- `w43-lead-muse-10m-20261021` CONTEXT — Secondary-reported adoption (no primary books).
- `w43-support-vercel-ollama-20261017` CONTEXT — Distribution versions unverified (UNVERIFIED).
- `w43-r4-grok-x-ledger-20261024` NON_MATERIAL — Audit sensor binder; NEVER story; COMPLETE registration / PARTIAL sensor.

## 51-ledger reconciliation (12 carries + 19 DROP)

- 19 DROP retain r2 exclusion reasons (pre-window, OUT-of-window v1/base/repo, X-only uncorroborated, name quarantine, thin method/license/eval). No promotion, no redating.
- 12 W42 carries: 11 DROP (same exclusions) + 1 MAYBE→CONTEXT (`7151fcdc…` gzip support). Quarantines hold (Qwen3.8-27B name, SMLIB, LTX-2.3, Fish Drama, Le Chonk, etc.).
- 32 non-DROP map 1:1 to Evidence tasks; ledger disposition equals View status (20/11/1); DROP rows have zero tasks/views.
- Grok binder is the single NON_MATERIAL; it is not a story candidate and must not enter Selection body.

## Completeness (LIMITED honest)

- `weekly:current-relevance` LIMITATION — 24 IN families + revisions covered with 21 bound supplements, but vendor numbers unreproduced and some bodies partially opened.
- `weekly:technical-significance` LIMITATION — Claim-level consumption with exact literals/math, but benchmarks unreproduced, v1-v2 deltas UNRESOLVED, weight/card SHAs partial, independent evaluation ZERO by design.
- `weekly:carry-over` SATISFIED — All 12 dispositions explicit; quarantines hold; no auto-promotion.
