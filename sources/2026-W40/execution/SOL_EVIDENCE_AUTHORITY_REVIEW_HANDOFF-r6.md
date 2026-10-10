# SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF-r6 — 2026-W40 (Muse r6, 2026-10-10Z)

Status: `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` candidate — Sol final Evidence/Card source-binding review; decides formal acceptance vs further repair. **REVIEW_PENDING; NO Evidence Acceptance; NO State transition.** Canonical state stays `CANDIDATES_NORMALIZED`.

## 1. Identity, ancestry, allowlist, readback, invariants

- Starting HEAD `edaa67d3684c878221f071a5da327b7d1f8faf77` / Tree `0ae1f83b41e27fceb18ce23d43171a34f76dd6d7` (remote read-only match; local ff-only sync, NO reset). Reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (match). R5 ancestor PASS.
- Final HEAD / Tree: filled at commit (normal commit, non-force ff push, remote read-back verified).
- Changed-file allowlist (all `sources/2026-W40/`, NO Core/branch/Gate/State-transition writes):
  - `external/evidence-supplement/evidence-authority-supplement-r6.json` (NEW, SHA `8872acfd…`, 4 entries, frozen-built + validated)
  - `execution/compat/evidence-supplement-card-binding-r6/` (build script + compat-package `11e46044…` 35 tasks + ledger r1→r5→r6 + double-build + negatives)
  - `evidence/v2/results/r6/interactive-evidence-r6.json` (35 records) + `record-audit-r6.json` (30 audit) + `card-candidates/` (35 PROPOSED) + `card-build-log.json`
  - `execution/sessions/muse-w40-r6-20261010.md` (NEW) + this handoff + `execution/index.md`
- Preserved byte-identical: 37 Discovery (+acceptance graph `27e9efde…`), 37 Screening acceptance (`2409f568…`), 35 canonical tasks, r1/r5 evidence files, 35 draft views, Grok Raw 20477B, DailyX 64, W39 HOLDs.
- State: `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; evidence/materiality/completeness pending; gates pending/pending.

## 2. Projection SHA diff (r5→r6) + one-to-one classification + negative tests

- Approved r5 map retained verbatim (2 mappings, 3 tasks); r6 adds supplement bindings only. Lineage per task (ledger `projection-ledger-r6.json`):
  - lift / agentperf: r1 → r5 projected → r6 IDENTICAL to r5 (no supplement; projection only).
  - contextlms: r1 `c1d1027c…` → r5 `07091638…` → r6 `04a54295…` (+ sup `ed880012…`).
  - guard: r1 `fa18ee70…` == r5 (passthrough) → r6 `eb572bab…` (+ sup `a390cdf7…`).
  - elyza: r1 `d255b1e7…` == r5 (passthrough, SECONDARY native) → r6 `bb95cd9a…` (+ sup `5287b436…` + `7f8ef96a…`).
  - Other 32: r6 == r1 bytes (passthrough; only package-level supplement pointer added, task files untouched).
- Only-expected-changes proof: per-task invariant (only source_type differs, r5) + supplement-ID attachment (r6); double-build identical; compat package `11e46044…`.
- Negative tests: original 3 tasks STILL raise unsupported-type (no skipped illusion); `BOGUS_UNREVIEWED_TYPE` FAIL_CLOSED_PASS. Unknown-source guard intact.

## 3. Supplement manifest SHA + 4 entries + raw SHA/bytes + canonical identities + bound IDs

- Manifest `external/evidence-supplement/evidence-authority-supplement-r6.json`, SHA `8872acfd2bebcc6b01907be9a219e33b1ce86dc39d023e585893f917e23e9c88`, supplement_id `w40-evidence-authority-supplement-r6`; basis binds Discovery JSONL `7232d808…` + Screening acceptance `4bae12ed…` (both current canonical).
- Entries (all validated: task-ID == stable_task_id, non-DROP, class==map(source_type), unique (task,locator), instants parsed, raws exist + SHA/bytes match):
  1. `supplement-src-5287b4364ef7b4ea` → elyza task `evidence:2026-W40:66aacc54064b63d6`; PRIMARY_REPOSITORY; 33B card @6ca556b; published `2026-10-02T00:46:49Z` (Hub creation as first-publication evidence); accessed `2026-10-10T05:27:24Z` (actual r5 access log); raw r5 excerpt (3520B, `aff50bfb…`).
  2. `supplement-src-7f8ef96a047e41dd` → same task; 32B card @5260ecc; published `2026-10-02T00:47:54Z`; raw (2058B, `df8ce7d6…`).
  3. `supplement-src-a390cdf7ffadb62c` → guard task `evidence:2026-W40:8c75a77f0becb78b`; PRIMARY_PAPER; abs URL; published `2026-08-27T16:15:34Z` (v3, rendered revision assumption noted); raw r5 paper excerpt (3667B, `9cf1f973…`).
  4. `supplement-src-ed880012d11eae67` → contextlm task `evidence:2026-W40:8d261dee1d3bdf14`; PRIMARY_PAPER; v1 URL; published `2026-09-29T14:50:08Z`; raw r5 fulltext excerpt (3949B, `6b3f172f…`).
- Rights: model cards Apache-2.0; papers arXiv (CLM CC-BY-4.0 per PDF metadata); excerpts bounded + attributed; NO full-HTML/PDF-byte equivalence claimed.

## 4. 35 Card candidates + full validator exits; bindings; claim→source counts; unresolved

- Build: 35/35 via `_build_card` against r6 package tasks (supplement-aware authority); filenames `card-<discovery_id>.PROPOSED.json` in `results/r6/card-candidates/`; basis binds r6 package task SHAs + screening `4bae12ed…` + prompt + card contracts.
- Validation: `validate_evidence_card(..., repo_root=...)` 35/35 PASS, exit 0 (log `card-build-log.json` with per-card SHA prefix). Card statuses 29 VERIFIED / 6 PARTIAL (match records).
- Claim→source: 127 claims / 105 limitations; ALL 127 cite src-1 (legacy lineage preserved); supplement cited 22× on repaired cards (elyza 6×2 IDs, guard 5, contextlm 5); 7 temporal events (exact published instants only).
- Impossible/incomplete bindings: NONE (all 35 tasks resolve; 0 skipped). Remaining UNRESOLVED targets inside cards are content gaps (paper tails, code, rate pages), not binding failures.
- Views NOT rebound (drafts keep package-task SHAs; no result-SHA until acceptance) — staged replacement deferred per contract.

## 5. ProvenanceGuard dates + Sep 29 distinction + version used

- CORRECTED everywhere in r6 records: v1 2026-06-16T15:10:29Z / v2 2026-07-26T10:47:53Z / v3 2026-08-27T16:15:34Z (current); r5 `Aug 27 as publication` phrasing replaced (7 sites). Sep 29 team-blog exposition = the W40 event (unchanged); paper versions all pre-window (no W40-newness impact).
- Consumed revision: ar5iv latest rendering ASSUMED v3-current at access (abs current abstract matches consumed numbers: 0.802/0.858/0.846/0.503/0.229/50 probes); v2-vs-v3 delta NOT diffed — explicit limitation. No invented version.
- Supplement published_at uses v3 date with assumption noted in relation; Sol can re-pin to v2 if the delta matters.

## 6. ELYZA MATERIAL-vs-HOLD + benchmark footnotes (regressions preserved)

- Provisional MATERIAL retained (Sol r2: ELYZA SHOULD be a MATERIAL Selection candidate): in-window + Apache-2.0 + domestic foundation + full JA tables.
- Regressions preserved (no blanket improvement): JMMLU 84.69 < base 85.22 (33B); JMMLU 81.05 < 81.32 (MoE); vs llm-jp-4.1 rows (60.64/53.89); trails Qwen3.5/Gemma4 globally. Footnotes preserved (parallel-call floor 10.00/11.58, temp/effort/max-output, chart-images unread).
- Cards now cite BOTH primary card source IDs (6 claims × 3 source_ids); legacy SECONDARY src-1 retained for lineage, NOT sole support. Screening MAYBE untouched.

## 7. True residual limitations

- Olmo report body still RETRIEVAL_FAILED (>5MB ×2); reporter-level bound retained; retry avenue documented.
- Paper tails/appendices + figures + code + PDF bytes unconsumed (CLM B–F/code; Guard VI+/schema/code/poster/PR).
- AstaBrief/AutoSynthData release times still unknown (unchanged); AutoSynthData standalone still NOT_FOUND.
- W39 Pixel Canary/TBC HOLD unchanged; Oct 8/9 post-window + Oct 2 day-only Cloudflare items guarded.
- Selection-depth pins (system cards, repo docs, weights, scripts, replays, rates) per record; delegated pins need Sol/issuer readback.
- Shared-Core DM-016 OPEN (W40 r5/r6 recurrences logged; closure update due at edition closure per maintenance §2).

## 8. Terminal

- `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` candidate (REVIEW_PENDING). Sol: authorize exact r6 ledger + supplement for formal acceptance (separate unit), or issue targeted repair.
