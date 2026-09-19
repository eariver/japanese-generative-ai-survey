# W37 Sol Evidence authority-consumption review

Status: `SOL_AUTHORITY_CONSUMPTION_REVIEW / CLEAN_WITH_BOUNDS`
Date: `2026-09-18T23:30:00Z`
Issue: `2026-W37`
Evidence set: `2ab4421b` (13 results: 11 VERIFIED + 2 PARTIAL)
Views set: `2f281601`
Materiality: derived; Completeness: `LIMITED` with 3/3 obligations `SATISFIED`

## Authority states (Sol independent inspection)

- AUTHORITY_CONSUMED (11): FinServ, GPT-Live, Agents API, DeepSeek news, DeepSeek API docs, SWE-2, Fusion, MiniCPM, North, Ling VL, Threat report. Each primary body actually read; claims bounded to source; limitations reflect source (methodology/judge/partnered/repro gaps), not generic placeholders.
- AUTHORITY_NOT_FOUND (0): no material candidate lacks a suitable primary locator (GLM rumor correctly has none and is DROPped at Screening, not Evidence).
- AUTHORITY_RETRIEVAL_FAILED (0): all suitable locators retrieved (OpenAI via webfetch excerpts; DeepSeek HTML full; others full).
- AUTHORITY_CAPTURED_BUT_UNCONSUMED (0 after check): sampled substantive bodies (SWE-2 cost tables, Fusion savings tables, MiniCPM eval table, North WMT breakdown, Threat case classes) — all material claim families converted to bounded claims; no richer body left unmined that would change materiality.

## Unselected-evidence spot checks (pre-Selection)

- DeepSeek API docs vs news: complementary, not duplicative (operational binding vs launch claims); both consumed.
- Threat report truncated fetch: excerpts cover scope + 7 areas + case classes; full PDF/IOCs explicitly bounded as not consumed; no hidden material claim asserted.
- Resignation PARTIAL: secondary only, SOCIAL_OBSERVATION, correctly CONTEXT-bound; no technical promotion.
- X PARTIAL: ledger PRIMARY_FACT + SOCIAL_OBSERVATION, correctly MATERIAL as community signal, never technical.

## Gap-fill saturation

- One verification attempt was not the stopping rule: DeepSeek (news+API+HF via search), SWE-2 (blog+leaderboard+secondary benchmarks), MiniCPM (HF+recipe+secondary dates), North (blog+HF+docs), Ling (HF+OpenRouter+Novita), Threat (landing+secondary NPR/Reuters), GLM rumor (tracker + HF/API absence) — iterative across announcement/docs/repo/card/secondary.
- Remaining UNRESOLVED are source-backed and defensible (methodology/judge/partner costs, repo hour, late-detail exclusion), not unprocessed.

## Verdict

`CLEAN` — Evidence is sufficient basis for Selection. Proceed to SELECTION_COMPLETE via canonical Selection/Architecture runner. No additional gap-fill loop required before Selection.
