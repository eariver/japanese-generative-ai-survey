# R1->R2 supersession + capture-reclassification ledger (SC-D02/SC-D03)

- ledger_id: w40-r1-r2-supersession-20261010
- r1_baseline: HEAD `05bfeca3b`, Tree `116258827fec38fb1d3aa3f706b777d26cf335b9`, 29 Discovery records
- r2_run: `20261010T030600Z-muse-r2`, retrieved_at `2026-10-10T03:06:46Z`
- principle: preserve r1 files as auditable history (NO rewrite/delete); append r2 snapshots; this ledger is the supersession authority.

## SC-D03: capture reclassification (truthful)

### R1 run `20261009T171300Z-muse-r1` (24 md files): ALL `CLAIM_LEVEL_DERIVED_NOTE`, NONE is byte-identical original capture

- Captured original bodies (byte-identical remote HTML): **0**.
- Full pages READ via webfetch (rendered markdown consumed, only claim summaries archived): ~15 page-loads (Sonnet, GPT-6.1, dots, DevDay, NVIDIA safety, safety-cases, Argon, SynthID, Clef, Strands, AMD-WorldLabs, AA-AgentPerf, ContextLM abs, LIFT abs, FLUX model page, Holo/Olmo/TTS/Guard/Asta/Auto NOT in r1).
- Claim-consumed notes archived: 24 (all files).
- Of which locator/excerpt-grade (CONTENT_ACCESS_LIMITED, full body NOT read): 8 — `ollama-jev-20260929.md`, `cloudflare-aisearch-mcpauth-20261001.md`, `agents-api-computeruse-20260929.md`, `nvidia-vss33-20260929.md`, `nvidia-relay-asr-amdross-20260930.md`, `nvidia-dgxspark64-20261002-unresolved.md`, `elyza-openweights-20261002-unverified.md`, `w39-carryover-recheck-20261009.md` (recheck log).
- Sweep log `openworld-negativespace-20261009.md`: `CLAIM_LEVEL_DERIVED_NOTE / SWEEP_LOG` (queries + matrix, not source capture).
- Consequence: r1 summary "24 Raw files" MUST be read as "24 derived claim notes, 0 original bodies". Corrected in r2 Discovery metadata + handoff.

### R2 run `20261010T030600Z-muse-r2` (15 files)

- Byte-identical original HTML captures: **0** (webfetch returns rendered markdown; honestly stated per file).
- `COPYRIGHT_BOUNDED_EXCERPT` (bounded verbatim quotes + URL/time/method/anchors/redistribution limits): **8** (holo4 newsroom, holo4 HF blog, holo4 license page, olmocore3, open-TTS, provenanceguard, astabrief, autosynthdata).
- `CLAIM_LEVEL_DERIVED_NOTE`: **7** (6 per-source claim notes + 1 r2 sweep log).
- Read vs consumed: 8 source pages fully READ (newsroom, HF holo4, models license, olmocore3, openTTS, provenanceguard, Ai2 AstaBrief + HF AstaBrief counted as one source-pair, AutoSynthData); all 8 claim-consumed in notes; 8 bounded excerpts archived.
- Locator-only: 0 new (all new sources read); prior r1 locator-grade items remain open for Evidence refetch (see handoff N-findings).

## SC-D02: 21 artificial-noon audit (T12:00:00Z)

Method: parsed all 29 r1 `source.published_at`; 21 exactly `T12:00:00Z` with no `timestamp_basis`. Each audited against its collector note's date evidence:

| # | Discovery ID | r1 published_at | Source evidence | r2 fix |
|---|---|---|---|---|
| 1 | w40-primary-sonnet55-20260928 | 2026-09-28T12:00Z | page header "September 28, 2026" DAY ONLY | NULL + pub_date_day 2026-09-28 + DATETIME_NOT_PROVEN + tz-ambiguous |
| 2 | w40-primary-nvidia-agentsafety-20260928 | 2026-09-28T12:00Z | newsroom "September 28, 2026" DAY ONLY | NULL + day + NOT_PROVEN |
| 3 | w40-primary-amd-worldlabs-20260928 | 2026-09-28T12:00Z | newsroom Sep 28 DAY ONLY | NULL + day + NOT_PROVEN |
| 4 | w40-primary-openai-safetycases-20260928 | 2026-09-28T12:00Z | page Sep 28 DAY ONLY | NULL + day + NOT_PROVEN |
| 5 | w40-primary-gpt61-sol-20260929 | 2026-09-29T12:00Z | page Sep 29 DAY ONLY | NULL + day + NOT_PROVEN |
| 6 | w40-primary-openai-dots-20260929 | 2026-09-29T12:00Z | page Sep 29 DAY ONLY | NULL + day + NOT_PROVEN |
| 7 | w40-primary-openai-devday-20260929 | 2026-09-29T12:00Z | page Sep 29 DAY ONLY (bundle hub) | NULL + day + NOT_PROVEN |
| 8 | w40-primary-agentsapi-computeruse-20260929 | 2026-09-29T12:00Z | changelog entry date per register, locator-only | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 9 | w40-primary-ollama-jev-20260929 | 2026-09-29T12:00Z | blog header Sep 29, locator-grade | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 10 | w40-primary-aa-agentperf-20260929 | 2026-09-29T12:00Z | article Sep 29 DAY ONLY | NULL + day + NOT_PROVEN |
| 11 | w40-primary-vss33-20260929 | 2026-09-29T12:00Z | blog Sep 29, locator-grade | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 12 | w40-primary-gemini-argon-20260930 | 2026-09-30T12:00Z | page Sep 30 DAY ONLY | NULL + day + NOT_PROVEN |
| 13 | w40-primary-synthid-bio-20260930 | 2026-09-30T12:00Z | blog Sep 30 DAY ONLY (X Oct 1 = momentum) | NULL + day + NOT_PROVEN |
| 14 | w40-primary-nemorelay-20260930 | 2026-09-30T12:00Z | blog Sep 30, locator-grade | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 15 | w40-primary-nemotron-asr-20260930 | 2026-09-30T12:00Z | blog Sep 30, locator-grade | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 16 | w40-primary-amd-ross-20260930 | 2026-09-30T12:00Z | newsroom Sep 30, locator-grade | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 17 | w40-primary-strands-decider-20261001 | 2026-10-01T12:00Z | blog Oct 1 DAY ONLY | NULL + day + NOT_PROVEN |
| 18 | w40-primary-cloudflare-aisearch-20261001 | 2026-10-01T12:00Z | changelog Oct 1, locator-grade | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 19 | w40-primary-cloudflare-mcpauth-20261001 | 2026-10-01T12:00Z | changelog Oct 1, locator-grade | NULL + day + NOT_PROVEN + LOCATOR_GRADE |
| 20 | w40-hold-dgxspark64-20261002 | 2026-10-02T12:00Z | calendar Oct 2, NO time | NULL + day + TIME_UNRESOLVED (HOLD) |
| 21 | w40-weak-elyza-20261002 | 2026-10-02T12:00Z | NO dated proof | NULL + UNRESOLVED weak |

Non-noon records audited:

- w40-grok-x-ledger-20261009 `2026-10-09T16:42:00Z`: Raw self-declared approx ("~16:42Z"), NOT exact -> r2 NULL + raw_self_declared_approx_2026-10-09 + observed_at Drive creation (traceable).
- w40-primary-contextlms-20260929 `2026-09-29T14:50:08Z`: arXiv v1 exact -> KEEP + timestamp_basis arxiv-v1-submission-UTC.
- w40-primary-cloudflare-clef-20261001 `2026-10-01T15:34:02Z`: page JSON-LD datePublished 15:34:02.111Z -> KEEP (trim ms) + basis json-ld-datePublished + zone-qualified.
- w40-primary-flux3-image-20261001 `2026-10-01T19:00:27Z`: X post time misused as publication -> r2 NULL + pub_date_day Oct 1 + X_LEAD_19:00:27Z-kept-separately + NON_X_PIN_PARTIAL.
- w40-prewindow-lift-20260925 `2026-09-25T11:31:02Z`: arXiv v1 exact -> KEEP + basis.
- w40-carryover-pixelcanary/tbc + w40-sweep `2026-10-09T17:13:32Z` as published: batch time misused -> r2 NULL + recheck/sweep date-day + basis batch-log (published N/A for logs/rechecks).

Result: **21/21 artificial-noon repaired; 4 additional timestamp-misuse records repaired (flux, grok-ledger, 2 carryover + sweep log = 4 groups); 3 exact instants preserved with basis (contextlms, clef, lift).**

## R1->R2 ID tracking

- KEPT (repaired, same ID, new published_at/metadata/raw-refs where applicable): all 29 r1 IDs (no silent drops).
- ADDED (6 + 1): `w40-primary-holo4-20260928`, `w40-primary-olmocore3-20261001`, `w40-primary-opentts-20260930`, `w40-primary-provenanceguard-20260929`, `w40-hold-astabrief-20261002`, `w40-hold-autosynthdata-20261002`, `w40-sweep-negativespace-r2-20261010` (GAP_FILL r2).
- REMOVED: none. MERGED/SPLIT: none (DevDay split deferred to Evidence per SC-D06; Holo4 kept single record covering 27B+35B with license split inside to avoid volume inflation).
- Total r2: 29 + 7 = **36 records**.
- Raw graph: r1 raws preserved (all 24 + Grok Raw); r2 adds 15 files; each new record binds its excerpt + note (+ license excerpt for Holo4); sweep r2 binds sweep log.
