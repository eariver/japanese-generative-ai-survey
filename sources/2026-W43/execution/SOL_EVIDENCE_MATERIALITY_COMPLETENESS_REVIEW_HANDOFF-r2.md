# Sol Evidence/Materiality/Completeness Review handoff r2 — 2026-W43 (2026-10-24)

Status: `SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_READY_R2`
Edition `2026-W43` / WEEKLY / WEEKLY_MAGAZINE. Branch `weekly/2026-W43-v2-work`.
Starting HEAD/Tree (remote-verified read-only): `6a3898771038d64fc2cd6a911c4445177d43a8e2` / `b8e1a207edb3cc92827284241e486ce4683612`.
Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
State at work: `CANDIDATES_NORMALIZED` (unchanged; no `ADVANCE_STAGE`). Contract: r2 `sol-w43-evidence-r2-first-party-deepening-20261025.md`; Sol r1 review `sol-w43-evidence-r1-first-party-gaps-and-memt-archive-20261025.md` (REQUEST_CHANGES: 4 first-party gaps + MemT archive conflation). r1 acceptances + supplement + compat package + interactive input preserved unchanged.

## What r2 changed (bounded; no re-research beyond assigned gap-fill)
- CR-01 (4 first-party sources actually read, raw archived where obtainable):
  - Anthropic auto-mode article: HTML raw 599,884B archived; Oct 22 IN update (future rollout next week) vs Aug 7 OUT original; classifier + red-team + scope read. NEEDS_MORE/HOLD → PARTIAL/MATERIAL.
  - Decisions API: product page rendered-read (curl 403 bot-wall, no byte archive) + API changelog HTML raw 553,250B archived (Oct 22 GA entry, Oct 6 beta, 400-question limit, pricing). NEEDS_MORE/HOLD → PARTIAL/MATERIAL.
  - Patch the Planet: page rendered-read (curl 403, no byte archive); PHP incident + 5-stage framework + parties read; NO CVE IDs on page (do not invent). NEEDS_MORE/HOLD → PARTIAL/MATERIAL with CVE caveat.
  - Open Cloud on GCP: blog HTML raw 224,991B archived (page dated Oct 22, RSS observed Oct 21); Astra/Sol/Luna + Marketplace billing + perimeters. NEEDS_MORE/HOLD → PARTIAL/CONTEXT (distribution, not new capability).
- CR-02 (MemT archive conflation fixed): real MemT PDF fetched (65pp, 7,096,280B, SHA `959206da…`) and abs+intro+spec sections consumed; r1 "2.38MB" claim belonged to AM-Bench and is removed; licenses live in repo README, not paper text (verified absence); claim now PRIMARY_FACT + AUTHOR_CLAIM with exact provenance. Verification tech-report-pdf: UNRESOLVED (abs+intro consumed, full body unaudited) → r2 **VERIFIED** (PDF archived; abs+intro+Nano/Flash/benchmark/license sections consumed; equation-level audit not attempted).
- Re-audit: all other 27 records byte-identical (no silent edits); oracle/ambench source_bindings carried; Grok ledger/notes unchanged; re3 Kimi/DeepSeek/etc. claims already byte-accurate.

## Outputs (paths + SHA-256)
- Compat package r2 `execution/compat/evidence-source-class-projection/compat-package-r2/package.json` — `d06cc6d8…` (32 tasks: 25 passthrough + 7 projected SOCIAL/SECONDARY; ledger `d2e11023…`).
- Supplement r2 `external/evidence-supplement/evidence-authority-supplement-r2.json` — `f876e81f…` (8 entries: 2 carried papers + automode/changelog/GCP/MemT raws; Kimi X post deliberately NOT a supplement source — SOCIAL class unsupported by schema; X evidence stays Discovery-bound with raw_refs).
- Interactive input r2 `execution/compat/evidence-source-class-projection/interactive-evidence-r2.json` — `cffa7be9…` (32 records).
- Evidence accepted (NEW dir) `evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/evidence-accepted.json` — `7615b2ce0…` (32 cards: PARTIAL 32, HOLD 0).
- Views accepted (NEW dir) `evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/edition-views-accepted.json` — `5b04bc16…` (32 views: MATERIAL 20 / CONTEXT 11 / NON_MATERIAL 1 / HOLD 0).
- Materiality ledger `materiality-ledger-v2.json` — `6a5c2321…` (51 rows: MATERIAL 20 / CONTEXT 11 / HOLD 0 / NON_MATERIAL 1 / EXCLUDED 19).
- Completeness `profile-completeness-v2.json` — `09e1a206…` (LIMITED: LIMITATION/LIMITATION/SATISFIED).
- Source-depth ledger r2: `execution/source-intake/w43-evidence-source-depth-r2.md`; r1 history snapshot: `execution/history/r1/` (r1 ledger/completeness SHAs preserved).

## 32-card r1→r2 diff summary
- Upgraded NEEDS_MORE→PARTIAL (4): automode, decisions-api, patch-planet (+MATERIAL), openai-cloud (+CONTEXT).
- Fixed MemT archive claim (PARTIAL stays; tech-report-pic VERIFIED with caveat; materiality stays MATERIAL).
- Source bindings added for 6 supplement-bound tasks (2 carried + 4 new); all other records byte-identical; NO other claim/verification/materiality changes.

## Validation (real stdout/exit, pre-commit)
- prepare (compat r2) + validate package basis PASS; interactive 32/32 PASS; cards validated per task (basis/sha/identity/sources) PASS; accept_evidence PASS; views built + accept views PASS; materiality Core-derived PASS; completeness schema + validate PASS (LIMITED, honest).
- X `require_complete` PASS; stage precheck PASS (`CANDIDATES_NORMALIZED`→`EVIDENCE_REVIEWED`, `/tmp/w43-evidence-stage-precheck-r2.json`, state untouched); profile/state PASS; execution-record PASS; adapter unit tests 5/5 PASS.
- Negative: tampered screening acceptance copy rejected; forged r2 card basis rejected; tampered r2 supplement byte_count rejected (repo-local scratch, removed); legacy direct prepare still FAILs with zero writes (Issue #568 OPEN); claim-text edits remain validator-undetectable by design (integrity via content-addressed acceptance).
- Changed-file safeguard: edition-local W43 only (supplement PDFs/manifest, compat r2, interactive r2, evidence/views accepted r2, materiality/completeness, depth notes, handoff, session, index). No shared/W42/Grok-Raw/State/checkpoint/Core/Discovery/Screening/Human Gate writes; r1 artifacts byte-identical.

## Still conditional
PARTIAL sensor Grok; rendered-only reads (Decisions product page, Patch the Planet) explicitly marked; 0 independent reproductions; weight/card/license bytes for some families; AM-Bench v2 delta unchecked; robotics thin; v2 rollout future (auto-mode); CVE specifics absent (Patch the Planet); OpenAI news corroboration unopened (GCP).

## Sol decision requested
r2 Evidence authority/materiality/completeness readback (diff, strength, gaps, bindings). Trusted `ADVANCE_STAGE` only after Sol approval via immutable operator request.
