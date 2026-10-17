# W42 temporal provenance repair r3 — authoritative proof (2026-10-17)

Scope: ONLY AgentHorizon (§A), Qwen-Image-2.1-Turbo (§B), Grok-scale provenance label (§C). All other 46 records, 7 Daily X originals, Frozen Core unchanged.

## §A AgentHorizon — underlying paper OUT, X discussion IN (r2 claim FALSE, corrected)
- BEFORE (r2): `arXiv 2610.11050 submitted Oct 8 IN-window` (summary + reason).
- Authoritative proof: arXiv abs page (fetched r2, re-verified r3): v1 submitted **2026-10-08 01:03:48 UTC** (= 2026-10-08 10:03 JST).
- Window: W42 start **2026-10-09T22:00:00Z** (= 2026-10-10 07:00 JST). Delta: Oct 8 01:03:48 → Oct 9 22:00:00 = **44 h 56 m 12 s BEFORE start** → UNDERLYING OUT.
- X discussion: Daily X 10-11 topic (X post Oct 10 15:45Z, author @xhluca = paper author Xing Han Lu) → discussion IN.
- AFTER: `UNDERLYING_PAPER_OUT_OF_WINDOW / X_POST_IN_WINDOW / BACKGROUND_OR_DISCUSSION_ONLY`. Record kept as comparator lead (not erased); NOT a W42 paper launch. Sidebar/comparator justification belongs to Screening/Selection.

## §B Qwen-Image-2.1-Turbo — Oct 9 weights OUT, Oct 14 APIs unproven (r2 IN claim UNSUPPORTED, corrected)
- BEFORE (r2): Oct 9 open-weights + Oct 14 APIs as IN dual-trigger.
- Authoritative checks (r3):
  1. First-party Model Studio doc (`algin.../newly-released-models`, fetched r3): Turbo row is **day-only `2026-10-09`** (no clock) — cannot clear 22:00Z start. Doc `Last Updated: Oct 11, 2026` = document timestamp, NOT launch proof (Sol's distinction confirmed).
  2. Contemporary JP report (Sol-verified): 2026-10-09 23:59 JST = **2026-10-09 14:59 UTC**, already describing downloadable weights → **7 h before W42 start** → weights OUT.
  3. ModelScope model page: JS-gated (title only retrievable here) — no UTC clock obtainable; logged limitation, not evidence.
  4. Oct 14 API story: date-frequency scan of the Model Studio doc finds rows only for Oct 2/3/8/9 — **NO Oct 14 entry exists**. The Oct 14 "Pro and Turbo APIs" narrative is secondary press citing the doc + repos. Per Sol rule (`updated_at` ≠ launch proof): NO distinct in-window API launch corroborated.
- AFTER: `W42 DISCUSSION/BACKGROUND lead, NOT an in-window release`. Record kept (not erased); reopen only on a first-party dated (clock-bearing) launch entry.

## §C Grok-scale — provenance label overstated (corrected, no timestamp change)
- BEFORE (r2): `capture_class=CLAIM_LEVEL_DERIVED_NOTE__BODY_CONSUMED` with raw_paths = Daily X only → proves Daily X was read, NOT the original X post.
- AFTER: `DAILYX_RAW_CONSUMED__ORIGINAL_X_UNVERIFIED` (Sol-sanctioned value). Timestamp basis unchanged (X post 2026-10-15 22:52Z per Daily X, Weekly-IN; independently unverified). Grok native pass still AWAITING_GROK/PARTIAL.

## Clock table (UTC, half-open W42 [2026-10-09T22:00Z, 2026-10-16T22:00Z))
| Item | Instant | Position |
|---|---|---|
| AgentHorizon arXiv v1 | 2026-10-08T01:03:48Z | OUT (−44 h 56 m) |
| AgentHorizon X post | 2026-10-10T15:45Z | IN (discussion) |
| Qwen Turbo contemporary report | 2026-10-09T14:59Z (23:59 JST) | OUT (−7 h) |
| Qwen Turbo listing | 2026-10-09 day-only | UNPROVEN vs 22:00Z → OUT |
| Grok-scale X post (per Daily X) | 2026-10-15T22:52Z | IN (unverified original) |
