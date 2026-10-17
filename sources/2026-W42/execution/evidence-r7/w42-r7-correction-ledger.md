# r7 correction ledger — E42-R6-A..E item-by-item (2026-10-17)

Basis: r6 cards (151 claims) → r7 cards (151 claims, same count; precision repaired, no inflation).

## E42-R6-A — 22 non-URL sources resolved (script-verified 0 remaining)
- 4× `grok:…#N` → exact X post URLs (Sol-audited IDs), kind X_OBSERVATION, authority X_OBSERVDubbed_VIA_GROK. No direct-X read claimed (DailyX/Grok-read basis preserved in limits).
- 6× `x:user/status/…` → `https://x.com/…` exact URLs, kind X_OBSERVATION.
- 9× `analyst-note…` → kind EDITORIAL + exact repo bundle path source (ev-bundle-09/08). Editorial synthesis never carries VENDOR/primary authority.
- 1× `developer.nvidia.com citation` (EXO anchor) → dev-blog URL, authority VENDOR_CITED_UNFETCHED.
- 1× malformed 3druck → exact article URL + first-party GitHub repo (NVIDIA-Omniverse/usd-brep, Apache tag, created Oct 8).
- 2× AWS roundup shorthand → exact roundup URL (Oct 13 15:59Z verified).
- Every claim now carries an `authority` field (CONSUMED_BODY / X_OBSERVED_* / EDITORIAL_* / VENDOR_CITED_UNFETCHED / SECONDARY / NEGATIVE_SEARCH_LOG).

## E42-R6-B — stale limits/targets reconciled (5 named + sweep)
- Wonder: research-blog target RESOLVED; eval-report/model-card/AA-method stay UNRESOLVED.
- Nemotron: tech-report PDF RESOLVED (method detail); NEW explicit appendix-audit UNRESOLVED (was hidden inside old pending).
- FLUX: license-fulltext RESOLVED.
- Wet-lab: 3 PDFs RESOLVED (equation-level audit logged as not-attempted, not pending-discovery).
- MiniCPM: license-tag RESOLVED vs license-file UNRESOLVED as SEPARATE targets (was one muddled line).
- Sweep: all other 44 cards' limits/targets re-checked against r6 bundles; no other stale pendings found.

## E42-R6-C — authority states at source granularity
- Rule applied: card state CONSUMED iff every claim derives from read bytes (scoped to those claims); gaps live in limits/targets/per-claim authority, not in a blanket state.
- Result: 48 CONSUMED + 1 NOT_FOUND (harness-17, bounded retry, no conflation). Zero CAPTURED_BUT_UNCONSUMED remain because no repo-held text sits unincorporated (appendix-skims logged as limits, not hidden stores).
- METR: CONSUMED-mechanism (outcomes nonexistent — not "unread"). MiniCPM/FLUX: CONSUMED-scoped (tag-vs-file nuance in limits).

## E42-R6-D — kinds + license precision
- analyst-note claims → EDITORIAL (9). X-post claims → X_OBSERVATION (11). No analyst text carries VENDOR/primary authority.
- OpenMDW-1.1: NO OSI-approval assertion anywhere (per Sol: submission ≠ approval). State: "permissive LF framework; OSI approval not established".
- Beam Apache 2.0: full repo LICENSE text verified; scope explicit — license status of the licensed files, NOT a guarantee every training artifact/datum is open-source. (Refines r6 bundle-06's "OSI-style permissive" shorthand; r6 file itself left byte-identical.)

## E42-R6-E — 49 substantive views regenerated
- All formulaic `AUTHORITY_CONSUMED + N claims` placeholders replaced with grounded importance/method/tradeoff/limits/chronology/reader-learning notes; HOLD/CONTEXT rationale where applicable (grok pair, backgrounds, carry, digests, security-X-only). Non-binding; no selection implied.
