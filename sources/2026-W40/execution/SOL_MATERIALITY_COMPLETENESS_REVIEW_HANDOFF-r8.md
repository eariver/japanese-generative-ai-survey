# SOL_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r8 — 2026-W40 (Muse r8, 2026-10-10Z)

Status: `SOL_MATERIALITY_COMPLETENESS_REVIEW_READY` candidate — Sol independently reviews materiality/completeness/omissions against accepted Evidence/Views, then authorizes Selection. **REVIEW_PENDING; NO EVIDENCE_REVIEWED transition; NO Selection/Architecture/Human action.** Canonical state stays `CANDIDATES_NORMALIZED`.

## 1. Identity, ancestry, allowlist, readback, invariants

- Starting HEAD `98ef2db27bd11fef3ab96bef5a77af3f43aa59b0` / Tree `dc126139938e7bb56b71a60fd14314a9ff1c5440` (remote read-only match; local ff-only sync, NO reset). Reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (match). R7 ancestor PASS.
- Final HEAD / Tree: filled at commit (normal commit, non-force ff push, remote read-back verified).
- Changed-file allowlist (all `sources/2026-W40/`, NO Core/branch/Gate/State-transition writes):
  - `execution/provenance-exceptions/LEGACY_UNVERIFIED_DO_NOT_CITE-guard-title.md` (NEW immutable exception)
  - `evidence/v2/results/r8/interactive-evidence-r8.json` (35 records; guard v1/v2-only) + `stage-cards/` (35) + `materiality-ledger-DRAFT.json` + `completeness-assessment-DRAFT.json`
  - `execution/compat/evidence-supplement-card-binding-r8/` (build script + package `30b63b11…` IDENTICAL to r7 + ledger r1→…→r8 + validation report)
  - `evidence/v2/accepted/0a62346f…/` (package copy + 35 tasks + 35 results + `evidence-accepted.json`)
  - `evidence/v2/views/r8/` (35 staging) + `evidence/v2/views/accepted/60b622f6…/` (35 views + acceptance)
  - `execution/sessions/muse-w40-r8-20261010.md` (NEW) + this handoff + `execution/index.md`
- Preserved byte-identical: 37 Discovery (+acceptance), 37 Screening acceptance, 35 canonical tasks, r1/r5/r6/r7 files + proposals, r6/r7 supplements + packages + cards, 35 draft views, Grok Raw, DailyX 64, W39 HOLDs.
- State: `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; evidence/materiality/completeness pending (acceptances exist as artifacts; NO checkpoint claimed); gates pending/pending.

## 2. SC-E10 cleanup diff/grep + version proof (v3-positive REMOVED)

- QA method: regex scan for `v3 (Aug|2026|current|latest|exist|body|NOT|adds)` / `Aug 27` / `08-27` / `assumed v3` / `v3-latest|v3 current|v3 NOT consumed|v3-existence|v3 adds` (DeBERTa-v3 model name excluded) over ALL new reader-facing fields.
- Result: **0 hits** in r8 records (35), r8 stage cards (35), accepted cards (35), r8 views (35), accepted views (35).
- Guard record changes (r7→r8): claim-1 parenthetical → `(v1 Jun 16 / v2 Jul 26; both pre-window)`; claim-2 context → v2-only history (`only versions displayed`); abs-tail bracket → v1/v2 only; claim-4 rewritten without version claims (catalogs-not-consumed phrasing mirrors Sol); limitations/verification → `revisions beyond v2 uncompared`. Other 34 records byte-identical.
- Version proof: primary v2 HTML read (header + four authors + CC BY-NC-SA 4.0; 9-row field match archived r7); abs currently displays v1/v2 ONLY (Sol-confirmed; no v3 asserted anywhere new).
- Immutable legacy title (`...paper Aug 27 pre-window` in Discovery/Screening/task copies + auto-carried Card `sources[]`): covered by `LEGACY_UNVERIFIED_DO_NOT_CITE` exception (no-chronology-citation ruling; paper authority = supplement v2; W40 event = Sep 29 blog). Card schema forbids editorial annotation fields, so the file IS the annotation. Paper-result claims bind ONLY `supplement-src-700ea3fb3655e466`; event claims bind `src-1` for the Sep 29 exposition only.
- Supplement r7 kept byte-identical (`8012cec0…`) per explicit instruction (locator v2 + July date + raw SHA/rights all pass). Its relation's `v3 NOT consumed` negative disclaimer is disclosed (not a positive assertion; not reissued to avoid SHA cascade for zero technical change). Views contain zero v3 prose (grep-proved), so no View resurrects it.

## 3. R8 projection + supplement SHAs, task/card chains, Core exits, negatives

- R8 package `30b63b11fa7d57cf4345969881dbde3f8762f5b72dfb6714be22af2379557c76` (== r7 bytes; 35 tasks all identical; 3 projected + 3 supplement-bound) via frozen rebuild under current impl `98ef2db2…`; `validate_evidence_package_basis` PASS; `task_authority_sources` 35/35 PASS; double-build identical; original-3 + BOGUS negatives fail closed. Ledger `projection-ledger-r8.json` (r1→r5→r6→r7→r8 per-task SHAs).
- Cards: build 35/35 OK; `validate_evidence_card` 35/35 PASS exit 0. Guard card: [src-1 + v2-sup], Jul 26 event only.
- Evidence acceptance (frozen `accept_evidence_results`, impl `98ef2db2…`, override context): `evidence/v2/accepted/0a62346f0729e768d1b67305dd96e0e99224326c862831abe79e43ced4875e07/evidence-accepted.json` (35 results: 29 VERIFIED / 6 PARTIAL; digest `0a62346f…`); `validate_evidence_acceptance` PASS.
- Views acceptance (frozen): 35 rebuilt from accepted SHAs, validated 35/35, `views/accepted/60b622f659224cf1862ecdb4aa06563ee4f31ed69d2bb74f9e88c32f76e2925e/edition-views-accepted.json`; `validate_edition_views_acceptance` PASS.

## 4. Canonical acceptances: paths/SHAs, 35 cards + source map, 35 bound view links

- Evidence: `sources/2026-W40/evidence/v2/accepted/0a62346f0729e768d1b67305dd96e0e99224326c862831abe79e43ced4875e07/` — package copy (`package.json`), `tasks/` (35), `results/` (35, filename rule same-basename-as-task), `evidence-accepted.json` (result_set `0a62346f…`).
- Source map per card: 32 cards → [src-1] (Discovery source); guard → [src-1 + sup-v2paper]; contextlm → [src-1 + sup-clmpaper]; elyza → [src-1 + sup-33b + sup-32b]. 127 claims all cite src-1 lineage; 22 supplement citations on repaired cards.
- Views: `sources/2026-W40/evidence/v2/views/accepted/60b622f659224cf1862ecdb4aa06563ee4f31ed69d2bb74f9e88c32f76e2925e/` — `views/` (35, `view-<taskhash>.json`) + `edition-views-accepted.json` (view_set `60b622f6…`; per-row evidence↔view SHA links).

## 5. Provisional 37/37/35 materiality + completeness; consumption; counterfactual; HOLDs

- Ledger draft (`results/r8/materiality-ledger-DRAFT.json`, schema PASS): 37 rows = 30 MATERIAL / 4 HOLD (pixelcanary, tbc, astabrief, autosynthdata) / 2 EXCLUDED (sweep logs) / 1 CONTEXT (LIFT). ELYZA MATERIAL provisional (JA-vendor open-weight + full JA tables; counterfactual HOLD on global-rank lens documented). DGX MATERIAL provisional (timestamp resolved; future-shipping caveat; Selection examines price/inclusion).
- Completeness draft (`completeness-assessment-DRAFT.json`, frozen-built + `validate_completeness` PASS with override): 3 obligations SATISFIED; 11 residuals; overall LIMITED (honest, not READY).
- Consumption: CONSUMED 29 bodies + 7 delegated pins; CAPTURED_BUT_UNCONSUMED enumerated (cards/repos/weights/scripts/replays/rates/paper tails/code); RETRIEVAL_FAILED (AutoSynthData standalone, ELYZA eval void, /pricing banner direct, Olmo body, PDF bytes); NOT_FOUND (Pixel Canary card/outage, TBC bench/paper).
- Lanes A–L covered (A/C strong; B/F/I/K filled by backfills; D/E/G/H moderate-thin with honest stops); counterfactual: full consumption deepens the SAME ~30 MATERIAL items; no 38th event (Oct 2 day-only + Oct 8/9 post-window guarded, not qualifying); issue is full, not sparse.
- Alternative grouping for Selection: frontier-model spine (Sonnet/GPT-6.1/Argon/Holo4/ELYZA) vs decision-model cluster (Ollama/Clef/Decider + OpenAI Decisions API within DevDay) vs safety/provenance (OpenShell/Sentry/safety-cases/SynthID/ProvenanceGuard) vs eval/infra (AgentPerf/OpenTTS/ContextLM/Olmo-core/RL-Env/AutoSynthData-HOLD) vs platform/services (dots/Codex/AISearch/MCPAuth/VSS/Relay/ASR/Ross/FLUX/DGX). Strong omissions: none hidden; weak exclusions reasoned per record.

## 6. Unresolved first-party gaps (never downgraded) + DM-016

- Paper tails/appendices/code, PDF bytes, Olmo report retry avenue, AstaBrief/AutoSynthData times, AutoSynthData standalone, Selection-depth pins (cards/repos/weights/scripts/replays/rates), delegated-pin readback, Oct 2 day-only Cloudflare items, W39 HOLDs, post-window guards — all carried with original severity.
- CV2-DM-016 OPEN_CORE (no patch; edition-local approved mapping only; closure update due at edition closure).

## 7. Next Sol questions + terminal

- Sol: (a) accept 30/4/1 materiality + LIMITED completeness as Selection input? (b) authorize combined Evidence+Materiality+Completeness checkpoint + `EVIDENCE_REVIEWED` transition (separate unit)? (c) ELYZA/DGX inclusion guidance? (d) HOLD/time resolutions needed before Selection?
- Terminal: `SOL_MATERIALITY_COMPLETENESS_REVIEW_READY` candidate (REVIEW_PENDING).
