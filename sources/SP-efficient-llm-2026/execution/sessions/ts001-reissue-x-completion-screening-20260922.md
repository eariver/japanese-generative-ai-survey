# Survey Production session — ts001-reissue-x-completion-screening-20260922

Issue: `SP-efficient-llm-2026`
Started: `2026-09-22 UTC`

## Starting authority

- Branch head: `d2f02ffbe9c8c63084f45e613eb3b7f0a1e1558a` (== remote branch HEAD after ff-only pull of Sol's exact-byte bridge; verified pre-write)
- Remote main: `f85539c31a079ab7a7fa86185f3cbb0fcad0485a` (== reviewed main, verified pre-write)
- Prior session `ts001-reissue-x-r3-import-blocked-20260922.md` treated as historical provenance (EXACT_RAW_BYTES_UNAVAILABLE resolved by Sol bridge commit).
- Existing r1/r2/r3 X reviews reused, not recreated.
- Session objective: X manifest COMPLETE → X + F1–F4 Discovery → canonical refresh → canonical Screening → stop before Evidence.

## Guard (§2 — all PASS before any write)

- Remote work HEAD == `d2f02ffbe9c8c63084f45e613eb3b7f0a1e1558a`; remote main == reviewed main.
- Lifecycle `DISCOVERY_COLLECTED`; screening/evidence/selection/architecture pending; canonical 161; X `REQUIRED / AWAITING_GROK`.
- Bridged Raw independently verified: 30213 bytes, SHA `b3a8a0404e6d4a1abfaa6bde54c4a6f5d7979ec24870bcd629865f8443377d79`. Raw file NOT rewritten.

## Actions actually performed

1. X manifest → COMPLETE (schema-only fields; r3 result SUCCESS, DISCOVERY_RECORDED [EFF-D162], counts/revision/review path in rationale; validates under require_complete=True).
2. Bounded F1–F4 web follow-up: F1 vLLM V4.1 recipe (new vs D040/D078/D153 — recipe floor, AMD refusal, MTP-module drop); F2 Unsloth GLM-5.3-Flash docs (Unsloth previously absent); F3 llama.cpp PR #27742 merged (exact authority behind OBS-R2-009, beyond generic D050); F4 `INDEPENDENT_WRITEUP_NOT_RESOLVED` (vesko_st link unresolvable; no substitute).
3. Raw observations `raw/discovery-observations-r4-x-followup.md`; standalone `discovery/discovery-v2-r4.jsonl` (EFF-D162–D165, GAP_FILL/pass 3); prior draft `make_screening_decisions.py` kept as judgment provenance.
4. Canonical Discovery 161 → 165 (byte-identical concatenation, IDs exact); canonical acceptance rebuilt via Core tooling (165, validates incl. X integration); prior 161 authority snapshotted under `execution/x-completion/prior-authority/`.
5. Discovery checkpoint/state refresh via `CURRENT_CORE_DISCOVERY_STAGE_BUILDER_REPLAY` (`execution/x-completion/refresh_discovery_checkpoint.py`); lifecycle returned to DISCOVERY_COLLECTED.
6. Screening via official `run_screening_v2_interactive.py` from `execution/x-completion/interactive-decisions.json` (165 explicit operator judgments): DIRECT basis, 135 KEEP / 20 MAYBE / 5 INSPECT / 5 DROP; acceptance `screening/v2/accepted/24bac6…/screening-accepted.json`.
7. Stage validation + checkpoint (`orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`) + advance → CANDIDATES_NORMALIZED. Evidence NOT entered.
8. Sol review package `execution/reviews/screening-review-package-r1.md` (complete ID lists, no trigger). Updated `execution/index.md`.

## End state

- Lifecycle: `CANDIDATES_NORMALIZED` (Core machine authority); operational stop `SCREENING_COMPLETED / AWAITING_SOL_SCREENING_REVIEW`.
- Canonical Discovery 165 (`7074cef2bfc3b2dd034addbd778055bc2fed962e9845c756f32f9b3c848199d3`); acceptance 165; screening checkpoint `3914fd87…`; state `5b5f3517…`.
- Evidence/materiality/completeness/selection/architecture: pending (verified).
- Session status: `COMPLETE`
