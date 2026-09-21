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
- Current State SHA-256: `8f0d37807a22c8cea94559c122474f58f7a4a0e43ee3884867f65e25ca90f0b1`
- Current lifecycle: `DISCOVERY_COLLECTED`
- Current terminal reason: `none`
- Current next action: `stage:screening` (NOT EXECUTED — awaiting separately specified targeted X/community reception pass)

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
- Decision: `NOT_REQUIRED` for first run (primary map first; Sol designs later reception pass)
- Manifest: `external/x/x-source-intake-v2.json` (COMPLETE, zero runs)
- Latest Drive task-file path/reference: none (no Grok task created)
- Latest result disposition: none (no collection)

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

## Final disposition

`DISCOVERY_COLLECTED / TECHNICAL_DISCOVERY_CANONICAL / AWAITING_TARGETED_X_RECEPTION_PASS` — Sol-reviewed 161-record canonical Discovery adopted. No Screening executed. No Sol/Human decision fabricated beyond the recorded Sol PASS. Next step is the separately specified targeted X/community reception pass.
