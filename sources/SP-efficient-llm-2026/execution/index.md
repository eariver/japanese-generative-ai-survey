# Survey Production execution index — SP-efficient-llm-2026

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/SP-efficient-llm-2026/production-state.json`.

## Current authority

- Issue / edition: `SP-efficient-llm-2026`
- Research Profile: `THEMATIC`
- Publication Profile: `LONGFORM_SPECIAL`
- Work branch: `special/efficient-llm-2026-work`
- Start-of-run reviewed `main`: `f85539c31a079ab7a7fa86185f3cbb0fcad0485a`
- Run started: `2026-09-21T16:10:00Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/SP-efficient-llm-2026/production-profile.json`
- Production State: `sources/SP-efficient-llm-2026/production-state.json`
- Current State SHA-256: `5b5f351762e183ea0aa4830d0f1a2b895d27aed6b71923bad78195f1be4dd7ae`
- Current lifecycle: `CANDIDATES_NORMALIZED`
- Current terminal reason: `none`
- Current next action: `stage:evidence-materiality-completeness` (NOT ENTERED — stop is Sol screening review)

## Human Gates

- Architecture Review: `pending`
- Publication Preview: `pending`
- Detailed review records: none recorded yet

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Discovery (r1 base; superseded as canonical by refresh below)

- Collector run: `efficient-llm-discovery-r1` (observed 2026-09-21T17:00:00Z)
- Raw lanes: 12 files `raw/discovery-observations-*.md` (S01–S100) + `raw/discovery-negative-space-2026-09-21.md` (G01–G11)
- r1 records adopted into canonical `discovery/discovery-v2.jsonl` (161 records total; see refresh section); standalone r2/r3 companion files retained as immutable provenance
- Prior r1 canonical bytes preserved under `execution/discovery-refresh-after-sol-pass/prior-authority/`
- Stage checkpoint: `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json` (CORE_STAGE_CONTRACT PASS)
- Bridge requests: `execution/requests/init-thematic-20260922-01.json`, `execution/requests/advance-discovery-20260922-01.json`
- Bridge receipts: `execution/bridge-runs/init-thematic-20260922-01/receipt.json`, `execution/bridge-runs/advance-discovery-20260922-01/receipt.json`

## Discovery expansion r2 (Sol R1 gap-fill; lifecycle unchanged)

- Collector run: `efficient-llm-discovery-r2` (observed 2026-09-21T17:30:00Z)
- Raw lanes: 7 files `raw/discovery-observations-r2-*.md` (S101–S142: dist-training, KV-mgmt, cond-depth,
  harnesses, capstone-firstparty, routing-lowbit, data-jev)
- Discovery JSONL: `discovery/discovery-v2-r2.jsonl` (42 records EFF-D101–EFF-D142, GAP_FILL/pass 1)
- Acceptance: `discovery/discovery-accepted-v2-r2.json` (record_count 42, standalone-validated)
- Combined inventory: 100 (r1) + 42 (r2) + 19 (r3) = 161 Discovery records
- r3: collector run `efficient-llm-discovery-r3`; 4 Raw files (S143–S161: conditional-memory,
  test-time-compute, model-routing, D09-check); `discovery/discovery-v2-r3.jsonl` (GAP_FILL/pass 2,
  obligations EFF-O13/14/15); acceptance `discovery-accepted-v2-r3.json` (19 records)
- Ledgers: `execution/gap-fill/r2-sol-r1-dispositions.md`, `execution/gap-fill/r3-final-dispositions.md`
  (cross-cutting nine-axes hypothesis recorded; carried-forward limitations bounded)
- r1/r2 provenance preserved: files untouched, acceptances re-validated intact
- Session: `sessions/ts001-reissue-discovery-r2-20260922.md`
- Session: `sessions/ts001-reissue-discovery-r3-20260922.md`
- Ledger: `execution/gap-fill/r2-sol-r1-dispositions.md` (G01–G20 dispositions + NOT_FOUND registry)
- r1 provenance preserved: r1 files untouched, r1 acceptance re-validated intact
- Session: `sessions/ts001-reissue-discovery-r2-20260922.md`

## Discovery canonical refresh (Sol PASS adopted; lifecycle unchanged)

- Sol Discovery Completeness Review: `PASS` (Sol / GPT-5.6) — `execution/reviews/sol-discovery-completeness-review-pass.md`
- Canonical Discovery JSONL: `discovery/discovery-v2.jsonl` (161 records EFF-D001–EFF-D161: r1 BASE 100 + r2 GAP_FILL 42 + r3 GAP_FILL 19; SHA `a94d8cbb64e1049480ea13690e7584e79ed6cdf7b830ba150f594e046880f53d`)
- Canonical acceptance: `discovery/discovery-accepted-v2.json` (record_count 161, Core-built; SHA `3aa62c4218df55155e99a8eb5de3158a4b5e0ac950a9ddbffcc6099f2f69e79c`)
- Stage checkpoint: `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json` (refreshed via `CURRENT_CORE_DISCOVERY_STAGE_BUILDER_REPLAY`, W34 precedent `8a937da`; SHA `28cdd7755b8cb003c9917e8899f95e3a31468162c583474ad4021b4fa51611ca`)
- Prior authority snapshot: `execution/discovery-refresh-after-sol-pass/prior-authority/` (exact pre-refresh bytes)
- Refresh tooling/validation: `execution/discovery-refresh-after-sol-pass/refresh_discovery_checkpoint.py`, `validation/`
- r2/r3 standalone artifacts unchanged and still valid; EFF-O13/14/15 retained as Discovery provenance (no profile/Core edits)
- Screening preflight: real resolver → `DIRECT`, 161 effective records; Screening NOT executed
- Session: `sessions/ts001-reissue-discovery-refresh-20260922.md`

## Grok/X

- Profile applicability policy: `CHATGPT_DECIDES`
- Initial decision: `NOT_REQUIRED` for first run (primary map first; Sol designs later reception pass)
- Current decision: `REQUIRED` — one bounded reception/deployment pass (`efficient-llm-reception-pass-01`); Human-requested practical dimension became material after Sol technical Discovery PASS (which remains valid)
- Manifest: `external/x/x-source-intake-v2.json` (`REQUIRED / COMPLETE`; r3 SUCCESS, DISCOVERY_RECORDED [EFF-D162])
- Repository task: `external/x/efficient-llm-reception-pass-01/grok-task.md` (20555 bytes, SHA `c1150730c6a0a758c4fd2e85928e593e49484765c4fe68864fe784fdde9220e2`)
- Expected Drive task path: `Grok_X_SourseIntake/Thematic_Special/efficient-llm-2026/efficient-llm-reception-pass-01/grok-task.md`
- Expected Drive result path: `Grok_X_SourseIntake/Thematic_Special/efficient-llm-2026/efficient-llm-reception-pass-01/x-reception-result.md`
- Result: pending (no Grok run, no Drive action by Muse)
- Pre-Grok Sol review: `execution/reviews/sol-pre-grok-reception-task-review-r1.md` (Sol / GPT-5.6, PASS, DRIVE_HANDOFF_AUTHORIZED)
- X reception reviews: r1 `execution/reviews/sol-x-reception-r1-review-20260922.md` (REQUEST_CORRECTION — six records only, no ledger; NOT imported); r2 `execution/reviews/sol-x-reception-r2-review-20260922.md` (REQUEST_CORRECTION — FIRST_HAND recount 17/3/7 vs claimed 19/3/5, no consistency token, bad observed_at; NOT imported); r3 `execution/reviews/sol-x-reception-r3-review-20260922.md` (Sol / GPT-5.6 PASS / IMPORT_AUTHORIZED — 27 records / 27 URLs / 24 accounts / 20 independent; Drive ID `181CYeFFZDtucPikWJr3EzWZGycdF_Mxo`, 30213 bytes, SHA `b3a8a0404e6d4a1abfaa6bde54c4a6f5d7979ec24870bcd629865f8443377d79`)
- r3 import status: `EXACT_RAW_BYTES_UNAVAILABLE` — Muse has no Drive channel; no Raw import, no manifest completion, no X Discovery record, no F1–F4, no refresh performed. Resume criteria in `sessions/ts001-reissue-x-r3-import-blocked-20260922.md` (verify 30213 bytes + SHA before any import).
- Boundary: machine lifecycle stays `DISCOVERY_COLLECTED`; operational interpretation `TECHNICAL_DISCOVERY_CANONICAL / TARGETED_X_SOURCE_INTAKE_REOPENED / AWAITING_GROK`; Screening NOT authorized until X result disposition + canonical Discovery refresh
- Session: `sessions/ts001-reissue-x-reception-prep-20260922.md`

## Deviations

- None. No Screening/Evidence/Selection/Architecture/Draft work performed (out of scope for this run).

## Shared Core defects

- None encountered. No shared-Core files modified (verified: only tracked change is planning
  authority `docs/thematic-special-backlog.md`; all else is edition-local under
  `sources/SP-efficient-llm-2026/`).

## Sessions

- `sessions/ts001-reissue-discovery-20260922.md`
- `sessions/ts001-reissue-discovery-r2-20260922.md`
- `sessions/ts001-reissue-discovery-r3-20260922.md`
- `sessions/ts001-reissue-discovery-refresh-20260922.md`
- `sessions/ts001-reissue-x-reception-prep-20260922.md`
- `sessions/ts001-reissue-x-r3-import-blocked-20260922.md`
- `sessions/ts001-reissue-x-completion-screening-20260922.md`
- `sessions/ts001-reissue-evidence-20260922.md`

## Screening (COMPLETE — Sol PASS recorded; package corrected)

- Canonical Discovery at Screening: 165 records (`7074cef2…`); acceptance 165 via Core tooling.
- New this run: `discovery/discovery-v2-r4.jsonl` (EFF-D162 X ledger + F1–F3 EFF-D163–165, GAP_FILL/pass 3); F4 `INDEPENDENT_WRITEUP_NOT_RESOLVED`; raw `raw/discovery-observations-r4-x-followup.md`.
- X manifest COMPLETE (r3 SUCCESS, DISCOVERY_RECORDED [EFF-D162]).
- Screening acceptance: `screening/v2/accepted/24bac6aa5c849eb2f6ac46f2162c7333137230cfec2610e908815a0e591b045d/screening-accepted.json` (DIRECT basis, 165 records).
- Dispositions: 135 KEEP / 20 MAYBE / 5 INSPECT / 5 DROP (DROPs are accepted PRIMARY_PAPER D140 D158 D159 D160 D161; no primary/capstone authority dropped; X D162 KEEP with boundary).
- Checkpoint: `orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`; lifecycle `CANDIDATES_NORMALIZED`.
- Sol review package r1: `execution/reviews/screening-review-package-r1.md` (preserved as historical output; factually defective counts).
- Corrected package r2: `execution/reviews/screening-review-package-r2.md` (`CORRECTED / SUPERSEDES_R1_FOR_SOL_REVIEW`; all counts mechanically recomputed from canonical bytes: source-class table, obligation table, O11 32/9/2/0; r1 defect ledger included).
- Sol Screening review: `execution/reviews/sol-screening-review-pass-20260922.md` (Sol / GPT-5.6, `PASS / PROCEED_TO_EVIDENCE`; acceptance unchanged; Selection NOT authorized).
- Run tooling: `execution/x-completion/` (prior-authority, refresh/advance scripts, decisions provenance, validation).

## Evidence (STAGE-BLOCKED by shared-Core defect; Luna input ready)

- Canonical Evidence/Materiality/Completeness production run did NOT complete: `run_evidence_v2_interactive.py` fail-closes with `unsupported source_type for Evidence authority: 'PRIMARY_DOC'` (first failure on EFF-D004). No Evidence/Views/Ledger/Completeness artifact was produced.
- Defect: `execution/defects/shared-core-evidence-source-map-gap-20260922.md` — Core v2 Evidence `SOURCE_CLASS_MAP` lacks 10 Thematic Discovery source types (PRIMARY_DOC 13, PRIMARY_REPO 21, PRIMARY_ANNOUNCEMENT 8, PRIMARY_MODEL_CARD 6, PRIMARY_SPEC 4, SECONDARY_REFERENCE 8, SECONDARY_TECHNICAL 4, RUNTIME_RECIPE 1, PACKAGING_DOCS 1, RUNTIME_PR 1 = 67/160 tasks). Runnable: 93 (PRIMARY_PAPER 92 + x-community-signal 1). Shared Core unchanged; no silent patch; failed run is failed evidence.
- Preserved Luna input: `execution/evidence-interactive-input/` — 160-record `interactive-evidence.json` (SHA `6cac92b1…`; 155 PARTIAL / 5 VERIFIED; 134 MATERIAL / 24 CONTEXT / 2 HOLD) + generator parts + task-target dump + README with resume criteria. Validated: exact 160-ID coverage, exact per-task verification-target match, Completeness O01–O12 (3 SATISFIED / 9 LIMITATION, LIMITED).
- Authority-consumption package r1 (stage-blocked): `execution/reviews/evidence-authority-consumption-package-r1.md` — 95 arXiv abstracts + 9 full pages consumed; 9 wrong-identity bound arXiv locators found with verified true identities (gap-fill triggers G-EV-01–11: D005/D061/D062/D093/D094/D098/D112/D117/D139 + DSA URLs + AIPerf successor); INSPECT outcomes (D032/D093 HOLD; D077/D119/D150 PARTIAL); MAYBE outcomes (watches held); capstone/Jev/X/F1–F4/O13–O15/methodology status; bodies-richer-than-claims list; Selection-must-not-proceed reasons.
- Authority states: CONSUMED (95 abstracts at scope + 9 pages + X ledger); CAPTURED_BUT_UNCONSUMED (54 locator-bound + abstract-only full bodies); RETRIEVAL_FAILED (none); NOT_FOUND (F4, AIPerf product surface, T-Bench v1 ID, DeepSWE primary, Jev independent reproduction + calibration protocol, non-MSR 1-bit deployment).
- Lifecycle remains `CANDIDATES_NORMALIZED`; Selection NOT started. Resume: reviewed Core map repair → clean re-run of preserved input → `EVIDENCE_REVIEWED` → Sol authority-consumption/materiality review.
- Session: `sessions/ts001-reissue-evidence-20260922.md`.

## Final disposition

`SCREENING_CORRECTED_SOL_PASS / EVIDENCE_STAGE_BLOCKED_BY_SHARED_CORE_DEFECT / SELECTION_NOT_STARTED` (machine lifecycle `CANDIDATES_NORMALIZED`) — Screening corrected (r2) with Sol PASS recorded; canonical Evidence input (160 records) authored and preserved; Evidence production run fail-closed on the recorded shared-Core source-map defect with Core unchanged. No failed-run verdict carried forward.
