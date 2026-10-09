# TS-003 r4 → r5 immutability/provenance repair report (Sol r4 R4-F1)

Issue: `SP-vision-multimodal-2026` | Date: `2026-09-30 UTC` | Lifecycle: `CANDIDATES_NORMALIZED` (unchanged)

Baseline: r3 accepted Evidence `evidence/v2/accepted/c6763f1c...` + r3 Views `fc8556a3...`
r5 acceptance: `evidence/v2/accepted/4182d7d5...` (manifest sha `5cc951bd...`, 111 Cards)
r5 views: `evidence/v2/views/accepted/e3d0b3b3...` (manifest sha `78a08d3c...`, 111 Views)
Same canonical task package; Discovery/Screening unchanged; r1–r4 artifacts untouched.

## Changed payloads: exactly 4 Cards + 4 Views (D074, D075, D077, D111)

All four carry the Sol-accepted r4 wording cleanup (no unbound `HF`/`Hugging Face`/
`release API`/`release tag`/audit-note naming; unresolved license/data statuses kept
explicit) with r3 provenance timestamps (`temporal.observed_at` +
`sources[0].accessed_at` = `2026-09-30T14:24:47Z`) restored. All other 107 Cards and
107 Views are byte-for-byte copies of r3 (verified by file hash, §6 checks 3/4/7).

D101 is byte-for-byte identical to r3 (content, `observed_at`, `accessed_at`,
formatting, ordering all verified by hash).

## Build method (no Shared Core change)

Copy-based construction with canonical validators/acceptors only:
`build_evidence_r5.py` copies 107 r3 result files byte-for-byte, stages the 4 repaired
Cards (r4 wording + r3 timestamps, each re-validated per-card against its task authority),
accepts via canonical `accept_evidence_results`, stages 107 r3 View copies + 4 rebuilt
Views bound to new card hashes, accepts via canonical `accept_edition_views`, and runs
both canonical acceptance validators. No ledger/completeness/state advance.

## Tooling anomaly encountered and resolved by byte verification

During the build, the reported views-acceptance path was inconsistent with the
freshly created, fully verified acceptance directory. Resolution: the adopted r5 views
acceptance `e3d0b3b3...` was verified byte-by-byte — 107 Views identical to r3, 4 Views
rebuilt for exactly the authorized Cards and bound to the new r5 card hashes, manifest
binding the r5 Evidence acceptance (`5cc951bd...`), full canonical validation PASS.
A prior-turn r4 views directory (`54045b59...`, committed history) was briefly deleted
during forensics and immediately restored byte-identical via `git checkout`
(verified clean afterward). No history was rewritten; r1–r4 remain immutable.

## Statuses, classes, gaps

VERIFIED 106 / PARTIAL 5 (unchanged, evidence-driven). Zero PRIMARY_FACT. G01–G06 preserved.
No Materiality/Completeness/Selection/Architecture/Human Gate artifacts created.
