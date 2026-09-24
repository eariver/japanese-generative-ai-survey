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
- Current State SHA-256: `b8a0521c98d5e4d28124aa8e7342f1553bf81757f6e103a62ae5939576241c1f`
- Current lifecycle: `CANDIDATES_NORMALIZED`
- Current terminal reason: `none`
- Current next action: `stage:evidence-materiality-completeness` (HELD — fresh Sol Evidence Semantic Review required first; Materiality/Completeness/Selection/Architecture NOT entered)
- Operational meaning: `EVIDENCE_REBUILT / AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R2` (r1 preserved as history; r2 rebuilt from source bodies; Sol r1 REQUEST_CHANGES E1-E5 repaired)

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
- Decision: `REQUIRED` (Sol Discovery r2 PASS authorizes one bounded reception/deployment pass before Screening)
- Manifest: `external/x/x-source-intake-v2.json` (`REQUIRED / COMPLETE`, one run)
- Latest Drive task-file path/reference: `Grok_X_SourseIntake/Thematic_Special/beyond-text-2026/beyond-text-reception-pass-01/grok-task.md`
- Latest result disposition: `beyond-text-reception-pass-01` r3 `SUCCESS` (27/27/27 Sol-audited, `OBS-SPEECH-01 YES->NO` downstream; raw sha `ebfce3bf…`, 39000 bytes) → one X-bound Discovery record `BT-D139`; r1/r2 Drive-history only

## Discovery (primary-technical first run; canonical)

- Collector run: `beyond-text-discovery-r1` (observed 2026-09-23T17:30:00Z)
- Raw lanes: 12 files `raw/discovery-observations-*.md` (BT-D001–BT-D128) + `raw/discovery-negative-space-2026-09-24.md` (G01–G12)
- Canonical Discovery JSONL: `discovery/discovery-v2.jsonl` (139 records: 128 BASE + 10 GAP_FILL + 1 X-bound `BT-D139`)
- Canonical acceptance: `discovery/discovery-accepted-v2.json` (record_count 139, Core-built, graph + X integration validated)
- Preflight: `BT-D137` raw note `CLAP alignment` → `CLIP alignment` (transcription only)
- Coverage accounting: `execution/discovery-coverage-20260924.md` (D01–D12, modality, transition, capstone, evaluation, negative space; anti-collapse all PASS)
- Current-capstone refresh at execution time: Wan last-open 2.2 verified; Sora lifecycle (product end 2026-04-26, Videos API removal 2026-09-24) verified 2026-09-23
- Stage checkpoint: `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json` (CORE_STAGE_CONTRACT PASS)
- Bridge requests: `execution/requests/init-thematic-20260924-01.json`, `execution/requests/advance-discovery-20260924-01.json`
- Bridge receipts: `execution/bridge-runs/init-thematic-20260924-01/receipt.json`, `execution/bridge-runs/advance-discovery-20260924-01/receipt.json`

## Screening (canonical, over 139)

- Decisions: `execution/x-import-screening-evidence-20260924/interactive-decisions.json` (KEEP 134 / MAYBE 3 / INSPECT 2 / DROP 0; non-DROP 139)
- Acceptance: `screening/v2/accepted/2a3e28dacadf9496db9109ff5dde58663767f280766c56b08c7bc03e72689966/screening-accepted.json` (Core `run_screening_v2_interactive`, validated)
- Stage checkpoint: `orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json` (CORE_STAGE_CONTRACT PASS) → advanced to `CANDIDATES_NORMALIZED`

## Evidence r1 (historical, preserved)

- Input: `execution/x-import-screening-evidence-20260924/evidence-interactive-input.json` (139 records, all PARTIAL)
- Acceptance: `evidence/v2/accepted/f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7/evidence-accepted.json` (139 Cards; Sol r1 REQUEST_CHANGES E1-E5)
- Views: `evidence/v2/views/accepted/b7c96f6245c7a58201c1369551b30bea8c215f793235f5d39c4eddc9dfdc41cc/edition-views-accepted.json` (139 Views)

## Evidence r2 (rebuilt from source bodies, not advanced)

- Input: `execution/evidence-semantic-depth-r2/evidence-interactive-input-r2.json` (139 records: VERIFIED 125 / PARTIAL 9 / NEEDS_MORE 5; Layer A factual only, no lineage prose)
- Acceptance: `evidence/v2/accepted/048cbd0942f073ed6ba134c97a5691e9ea4eb1eb0db6fa1ed842abe5faf2810e/evidence-accepted.json` (139 Cards, canonical validators PASS)
- Views: `evidence/v2/views/accepted/273e04d410be4e3800a89516399400d626a4dda95f311d37af7040def9553dd4/edition-views-accepted.json` (139 Views, PASS)
- Access ledger: `execution/evidence-semantic-depth-r2/source-body-access-ledger.json` (139 rows; FULL 125 / PARTIAL 9 / BLOCKED 5)
- Transition ledger (Layer B): `execution/evidence-semantic-depth-r2/transition-ledger.json` (43 entries, 41 multi-task) + `.md` companion
- Delta audit: `execution/evidence-semantic-depth-r2/semantic-delta-audit.md`
- Validation receipt: `execution/evidence-semantic-depth-r2/validation-r2.json` (14/14 PASS)
- Compat reuse: narrow source-type projection only (37/102); shared Core untouched
- Ledger/Completeness/advance: NOT performed (stop boundary; State remains `CANDIDATES_NORMALIZED`)

## Deviations

- Shared-Core vocabulary gap handled via reproducible edition-local compat (no Core edits); see below. Otherwise none. No Materiality/Completeness/Selection/Architecture/Draft work performed (out of scope for this run).

## Shared Core defects

- `x-import-screening-evidence-20260924/defects/shared-core-evidence-source-map-gap-bt-20260924.md` (`OPEN_CORE / EDITION_WORKAROUND`; same family as TS-001 CV2-DM-016): Evidence `SOURCE_CLASS_MAP` lacks five BT Discovery `source_type` values (37/139 tasks fail closed). No shared-Core files modified. Resume requires reviewed Core repair + clean rerun before any `EVIDENCE_REVIEWED` advance.

## Sessions

- `sessions/ts002-beyond-text-discovery-20260924.md`
- `sessions/ts002-beyond-text-discovery-repair-r2-20260924.md`
- `sessions/ts002-x-import-screening-evidence-20260924.md`
- `sessions/ts002-evidence-semantic-depth-r2-20260924.md`

## Final disposition

`EVIDENCE_REBUILT / AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R2` (r2 committed on the work branch for Sol r2 review; Screening passed, r2 Evidence built+validated, Materiality and later stages pending; no Human Gate fabricated)
