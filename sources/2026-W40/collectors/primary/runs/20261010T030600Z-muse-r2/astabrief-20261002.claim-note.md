# CLAIM NOTE (derived) — AstaBrief 8B (Oct 2, TIME_UNRESOLVED HOLD)

- artifact_class: CLAIM_LEVEL_DERIVED_NOTE
- companion_excerpts: [`astabrief-20261002.source-excerpt.md`]
- read_status: READ (both Ai2 + HF pages 2026-10-10T03:06:46Z)
- event_date_basis: DAY ONLY Oct 2; NO exact time -> Discovery temporal TIME_UNRESOLVED; published_at NULL + DATETIME_NOT_PROVEN

## Consumed claims

1. RELEASE (day-level): Ai2 open-sourced AstaBrief 8B Oct 2 (day): Qwen3-8B-based cited-report model (SFT 47K + DPO 6K, citation-density filtering, one-pass generation); Fast mode in Asta (51.1s vs 178.5s Thinking, ~3.5x); weights + training data + ScholarQA-lite workflow open. (PRIMARY_FACT day-level; time unresolved)
2. VERSION/DATA: Qwen3-8B base; 90K filtered queries; judges GPT-4.1 + DeepSeek-R1 (95% human agreement); SQABench-CS2 200 Qs (rubric/answer-precision/citation-P/R); DeepScholarBench 63; 14-Q human study (3 researchers); 374-user Fast-mode usage (29.1% 2+ days, 84.2% positive). (PUBLISHER_CLAIM, 2025-era baselines per page)
3. LICENSE: Apache-2.0 per HF card header (needs repo SPDX pin at Evidence). (UNVERIFIED_SPDDX)
4. RELEVANCE: Scientific cited-report generation; scope-preservation caveats on page (sample->population drift). Material lead/HOLD, NOT confirmed ordinary, NOT selection.

## Boundaries

- Must NOT auto-classify ordinary without exact time before 22:00Z. If Sol requires, keep HOLD.
- 2025-era comparison baselines; do not present as vs-today-frontier.
