# CLAIM NOTE (derived) — AutoSynthData (Oct 2, TIME_UNRESOLVED HOLD)

- artifact_class: CLAIM_LEVEL_DERIVED_NOTE
- companion_excerpts: [`autosynthdata-20261002.source-excerpt.md`]
- read_status: READ (full page 2026-10-10T03:06:46Z)
- event_date_basis: DAY ONLY Oct 2; NO exact time -> temporal TIME_UNRESOLVED; published_at NULL

## Consumed claims

1. RELEASE (day-level): ServiceNow CoreAI published AutoSynthData blog Oct 2 (day): failure-driven synthetic task curriculum (capability cards -> target/multiply generation -> sample/batch verification -> moving frontier); env-grounded (feasibility/realism/difficulty; verifier consistency/soundness/completeness). (PRIMARY_FACT day-level)
2. EXPERIMENTS (publisher-reported): EnterpriseOps-Gym Hybrid (Gemma-4-26B-A4B-it target, Qwen3.8-27B teacher, 2000 samples/18h, Pass@1 +7.2pp/35% rel, verifier 63.01%->68.55%, 59% gap closed, best epoch 5); ITSM (DeepSeek-V4.1-Flash teacher, 1994 samples/66h, 18.77%->27.18%). Generator blinded to eval tasks via sanitized cards. (PUBLISHER_CLAIM)
3. SCOPE: Training-data methodology for enterprise agents, NOT a foundation model. Prior Gym paper (Mar 2026) is background. Relevance for K/C lanes as lead; NOT selection.
4. LICENSE/CODE: dataset released (HF ServiceNow-AI/EnterpriseOps-Gym); code adapters implied; exact license pin pending Evidence.

## Boundaries

- Must NOT auto-classify ordinary without exact time. Keep HOLD.
- Figures are publisher-measured in stated envs; do not generalize.
