# W43 Sol Discovery Completeness Review r4 — substantive PASS, two provenance corrections before authority freeze

Status: `SOL_EDITORIAL_DISCOVERY_COMPLETENESS_PASS_WITH_LIMITATIONS / PRE_ACCEPTANCE_METADATA_REPAIR`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Reviewed Muse r4 remote HEAD: `59798654f24f5c096f06bcd816b7cb06c80ff8d5`
Reviewed r4 Root Tree: `e21e7ae8850ef901a2515d367c09082c6c578ffe`
Reviewed main HEAD/Tree: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`
Frozen Core v2 HEAD/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

## Reviewed authority

- Muse r4 result `sources/2026-W43/discovery/discovery-v2-proposal-r4.jsonl` (51 rows / 46 families); handoff `execution/SOL_DISCOVERY_COMPLETENESS_REVIEW_HANDOFF-r4.md`.
- Actual Git: r4 commit is a single normal fast-forward descendant of exact r4 starting HEAD `c6f18d46318325907b0b22d1b0a47185667ff0ba`; edited W43 edition-local files only. Frozen Core and main HEAD/Tree remained identical.
- X manifest `sources/2026-W43/external/x/x-source-intake-v2.json` now `COMPLETE`, produced via canonical `survey_x_intake_v2 record-result` according to worker execution record, with original `PARTIAL` Grok sensor result (exact 13425 bytes, SHA256 `4571e0de469a7143fb1c46710c2e419a91404ff2d9538ae4d9a31a8b8f0be54a`, observed at `2026-10-24T12:43:17Z`, imported at `2026-10-24T12:59:53Z`). This is correct: `COMPLETE` refers to **registration**, not source-independent technical verification.
- New first-party Flint official announcement HTML (366583 bytes), full Hugging Face metadata body (5478 bytes), publication date Oct 21 and HF repo created 2026-10-21T14:20:58Z. Apache 2.0 is HF metadata; exact license text, full weights integrity, independent eval remain downstream Evidence obligations.
- Reflection Beam original Oct 16 13:01Z OUT of W43 ordinary period starting 22:00Z. Muse Spark Open initial weights Oct 15 likewise OUT. FLUX 3 Max video and MemT memory remain retained despite Grok topic-level negative X findings. r3 49 rows preserved exactly in r4, +Flint and X sensor ledger only.
- r4 reports Core discovery pre-acceptance sandbox PASS (51 rows, graph `5a94b757…`), X require_complete PASS, Production Profile/State PASS and execution-record validator PASS. No accepted Discovery artifact or canonical Stage Checkpoint has been committed yet; official State remains `ISSUE_INITIALIZED`.
- 12 W42 HOLD/INSPECT carry-over leads remain unpromoted. Published benchmarks are vendor-reported; there are zero demonstrated independent full reproductions. Several license/PDF/model-card primary bodies still require Evidence scrutiny. This is a transparent limitation, NOT a claim of independent confirmation.

## Human decision

**NONE / NOT_APPLICABLE.** This document is Sol's edition-local editorial Discovery completeness ruling, NOT a Human Architecture Review or Publication Preview decision. Both Human Gates remain `pending`. Sol editorial judgment: **substantive Discovery coverage PASS_WITH_LIMITATIONS; permit canonical acceptance only after the two bounded provenance repairs below**. No human APPROVED status or editorial Selection granted.

## Requested changes

**CR-01 — Grok sensor ledger authority misclassified in active Discovery.**
`w43-r4-grok-x-ledger-20261024` has `source.source_type="PRIMARY_OFFICIAL"` despite `collector_id="grok-x-import"`, locator `grok-task:weekly-x-2026-W43`, metadata `authority_class="X_OBSERVATION"` and a raw Grok sensor report. It is **not first-party primary source**. Correct its active r5 canonical proposal `source.source_type="X_OBSERVATION"` (or exact appropriate existing equivalent) and, if helpful, mark it as a post-window **collection** that describes the W43 ordinary window, NOT a new Oct 24 technical event. Keep exact Grok raw path and binding, collector run and sensor timestamp. Do not count the sensor ledger as a scientific/technical event release. Leave r4 proposal immutable as historical evidence.

**CR-02 — Incorrect cited Muse Spark X post ID in crosswalk.**
Exact Grok Raw says `https://x.com/lm_zheng/status/2110889410615234942`, whereas `collectors/primary/runs/20261024T133000Z-muse-r4/notes/r4-note-03-grok-crosswalk.md` says `https://x.com/lm_zheng/status/2110889415895234942` and falsely presents it as present in Grok Raw. The two IDs are distinct. Write a truthful edition-local r5 erratum identifying the exact Raw ID; do **not** silently alter historical r4 notes. Neither source can establish a new in-window model weights release; no X-only candidate promotion. The Kimi 19-digit official post locator is correctly represented.

These are **bounded metadata/citation repairs**. The previous four Discovery research/normalization cycles must not be repeated. All previous r1–r4 raw files/proposals and Sol reviews remain as evidence.

## Regeneration boundary

Permit Muse r5 to (a) create an active corrected `discovery/discovery-v2.jsonl` sourced from r4 and a retained r5 proposal/history or documented approved freeze, (b) use the **canonical `scripts/survey_discovery_v2.py build_acceptance`** to create `sources/2026-W43/discovery/discovery-accepted-v2.json` with the actual validated X manifest and exact Grok-binding, and (c) validate frozen Core v2 Schema/graph/acceptance/Execution Record. Do not manually forge Acceptance, output State, Human decision, or validator PASS. Do **not** `ADVANCE_STAGE` before subsequent Sol readback and a trusted immutable operator request via Issue #448. Remain at `ISSUE_INITIALIZED`; no Screening/Evidence/Selection/Architecture until Sol confirms official `DISCOVERY_COLLECTED`.

## Shared-Core implication

**NONE.** Frozen Core v2 preserved. Prior `execution/reviews` heading failures were Sol-authored record-format errors, corrected without creating any Human decision; Muse r4 reports execution-record validator PASS. Two remaining issues are edition-local authority metadata/citation defects, not Core v2 maintenance tasks.
