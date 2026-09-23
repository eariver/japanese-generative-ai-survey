# Survey Production execution index — SP-beyond-text-2026

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/SP-beyond-text-2026/production-state.json`.

## Current authority

- Issue / edition: `SP-beyond-text-2026`
- Research Profile: `THEMATIC`
- Publication Profile: `LONGFORM_SPECIAL`
- Work branch: `special/beyond-text-2026-work`
- Start-of-run reviewed `main`: `0bbb02b3c5963403860897daec2feaf61e82589a`
- Run started: `2026-09-23T17:03:09Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/SP-beyond-text-2026/production-profile.json`
- Production State: `sources/SP-beyond-text-2026/production-state.json`
- Current State SHA-256: `85fdc492c12be9ac7e217976ba23e8d4980d1f681fa2379ce9dfe440453b8886`
- Current lifecycle: `DISCOVERY_COLLECTED`
- Current terminal reason: `none`
- Current next action: `stage:screening` (HELD — Sol Discovery completeness review required first)
- Operational meaning: `AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW`

## Human Gates

- Architecture Review: `pending`
- Publication Preview: `pending`
- Detailed review records: none recorded yet

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `CHATGPT_DECIDES`
- Decision for first run: `NOT_REQUIRED` (primary-technical map first; Sol designs later reception pass)
- Manifest: `external/x/x-source-intake-v2.json` (`NOT_REQUIRED / COMPLETE`, zero runs)
- Latest Drive task-file path/reference: none (no Grok task created in this run)
- Latest result disposition: none recorded yet

## Discovery (primary-technical first run; canonical)

- Collector run: `beyond-text-discovery-r1` (observed 2026-09-23T17:30:00Z)
- Raw lanes: 12 files `raw/discovery-observations-*.md` (BT-D001–BT-D128) + `raw/discovery-negative-space-2026-09-24.md` (G01–G12)
- Canonical Discovery JSONL: `discovery/discovery-v2.jsonl` (128 BASE records, pass 0; 127 unique locators)
- Canonical acceptance: `discovery/discovery-accepted-v2.json` (record_count 128, Core-built, graph validated)
- Coverage accounting: `execution/discovery-coverage-20260924.md` (D01–D12, modality, transition, capstone, evaluation, negative space; anti-collapse all PASS)
- Current-capstone refresh at execution time: Wan last-open 2.2 verified; Sora lifecycle (product end 2026-04-26, Videos API removal 2026-09-24) verified 2026-09-23
- Stage checkpoint: `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json` (CORE_STAGE_CONTRACT PASS)
- Bridge requests: `execution/requests/init-thematic-20260924-01.json`, `execution/requests/advance-discovery-20260924-01.json`
- Bridge receipts: `execution/bridge-runs/init-thematic-20260924-01/receipt.json`, `execution/bridge-runs/advance-discovery-20260924-01/receipt.json`

## Deviations

- None. No Screening/Evidence/Selection/Architecture/Draft work performed (out of scope for this run).

## Shared Core defects

- None encountered. No shared-Core files modified (verified at commit time; only tracked change
  outside the edition root is planning authority `docs/thematic-special-backlog.md`).

## Sessions

- `sessions/ts002-beyond-text-discovery-20260924.md`

## Final disposition

`DISCOVERY_COLLECTED / AWAITING_SOL_DISCOVERY_COMPLETENESS_REVIEW` (first-run terminal stop; Screening NOT authorized)
