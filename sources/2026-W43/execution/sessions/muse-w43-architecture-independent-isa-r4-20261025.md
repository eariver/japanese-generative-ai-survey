# Muse W43 Architecture r4 session (ISA-001…009 integrated repair)

## Starting authority

- Branch `weekly/2026-W43-v2-work`; remote HEAD `db78839bd7cb858a6cc5b1620bf6c574f064339f` / Tree `b1ee9c3e686e3f50cfabc9d679eff7e01937726e` (6-way remote MATCH: main `041a08df…`/`a134dc36…`, Frozen `774dd39a…`/`cd46a6f7a…`). Local was one stale fetch behind (`46f24027…`); fetched read-only, verified, then aligned to exact remote HEAD before any write.
- Mandatory reads: independent audit result (Selection PASS_WITH_LIMITATIONS / Architecture REQUEST_CHANGES, P1 x2 + P2 x7), Sol adjudication (9 dispositions + corroborations), r4 execution contract (single integrated repair, 7-file archive, isolated regen, 68/68, no Stage/Human/Draft/PDF). State `EVIDENCE_REVIEWED`, selection/architecture pending, Gates pending; accepted r4 Evidence/Views, Discovery/Screening, State/Checkpoints, Core/main/Gates immutable.

## Actions actually performed

- Snapshotted r3 (7 JSON + README/SHA256SUMS, cmp OK) to `execution/history/selection-architecture-r3/`.
- Built `execution/compat/selection-architecture-input-r4.json` (runner `2026-10-25T12:00:00Z`): 32 assignments byte-identical r3; 9-item architecture text corrections (DeepInfer排他, Voxtral UNRESOLVED table, 8B/4B + 39.8B/2.5B conventions + license split, FLUX recomputation labels, Decisions per-request/write-billed/regional, 68→separate ledger, P8 ESTIMATE plan, Japanese日英併記, availability status columns).
- Live first-party reads 2026-10-25 (rendered): DeepInfer README (MTP=1 vs deterministic MTP=0+BATCH_INVARIANT=1+seq_seed NVIDIA), Voxtral announcement 35+/50+ vs model card 9 vs matrix 35/50+ (UNRESOLVED), language-matrix preset table + cloning note, Decisions guide (400/request, writes charged, regional/long-context), Flint 39.8B/2.5B convention footnote, Nemotron 8B/4B + OpenMDW-1.1/Gemma Apache-2.0, FLUX blog 12.45s/277.80s vs 26.5x/96.2%. No new canonical raw archived.
- Isolated detached scratch @`db78839bd…` (`/home/eariver/w43-r4-scratch-20261025`, no new branch): removed proposal outputs only in scratch; frozen runner exit 0 → 32/8/READY; Matrix/Selection byte-identical r3; Architecture `529ce4b3…→9ab37dd6…`, Summary `26817906…→c8bb6e2e…`; rebuilt attention limit=100 → 68/68 byte-identical `7c3e4deb…`; reconciled audit (`ff2267e2…`); stage scratch precheck EVIDENCE_REVIEWED→SELECTION_COMPLETE PASS (impl `db78839bd…`, no writes); second bridge NOT run; 9 negatives + P4 divisions + page budget verified (Selection-rationale historic `10.95/277.80` preserved for invariance, Architecture authoritative).
- Wrote crosswalk, 9-closure, 19-risk ledger, handoff, this session, index append. Reflected exact tested bytes to branch (proposal surfaces + r3 archive + editorial pack only). No ADVANCE/Bridge/Human/Draft/PDF/force.

## External handoff

- No Grok task/transport; reused Raw 13425B SHA `4571e0de…` only as binder reference. No Issue #448 comment/PR.

## Deviations / failures

- None blocking (no `BLOCKED_ARCHITECTURE_R4_AUTHORITY` / `BLOCKED_ARCHITECTURE_R4_PROVENANCE`). Residuals: Voxtral UNRESOLVED (reported, not unified); 5 LIMITED; AA/v1-v2/deployment/Grok/hygiene/clocks unchanged. Scratch worktree placed outside `/tmp` (`/home/eariver/w43-r4-scratch-20261025`) because `/tmp` had only 1.6G free for a 3.6G checkout; worktree metadata removed after use.

## End state

- Lifecycle: `EVIDENCE_REVIEWED`
- Terminal reason: `none`
- Next action: `stage:selection`
- Review target: `SOL_W43_ARCHITECTURE_R4_INDEPENDENT_ISA_REVIEW_READY`
- Session status: `COMPLETE`
