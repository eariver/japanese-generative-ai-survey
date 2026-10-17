# W42 source-timing audit r1 (2026-10-17)

Normative window: EDT `[2026-10-09T18:00:00-04:00, 2026-10-16T18:00:00-04:00)` = UTC `[2026-10-09T22:00:00Z, 2026-10-16T22:00:00Z)` = JST `[2026-10-10T07:00, 2026-10-17T07:00)`. Cutoff end-exclusive. Core-computed via `weekly_profile(2026-W42)` — matches instruction exactly; not transcribed.

## Report-window mapping (all 7 inside W42)
- 10-11 report [10-09 22:00Z, 10-10 22:00Z): IN.
- 10-12 report [10-10 22:00Z, 10-11 22:00Z): IN.
- 10-13 report [10-11 22:00Z, 10-12 22:00Z): IN.
- 10-14 report [10-12 22:00Z, 10-13 22:00Z): IN.
- 10-15 report [10-13 22:00Z, 10-14 22:00Z): IN.
- 10-16 report [10-14 22:00Z, 10-15 22:00Z): IN.
- 10-17 report [10-15 22:00Z, 10-16 22:00Z): IN (end-exclusive; events at 21:55Z IN, events at/after 22:00Z OUT — none observed at/after).

## Per-topic clock basis
- Preferred: X post timestamp (GMT/UTC/JST as given, converted to UTC). JST = UTC+9.
- 6-7 Grok scale post 2026-10-15 22:52Z: 52 min AFTER the Daily 10-16 report's nominal obs end (10-15 22:00Z) but BEFORE Weekly cutoff (10-16 22:00Z) → Weekly IN, Daily-boundary overshoot disclosed.
- 7-4/7-5/7-12 posts at 21:34–21:55Z Oct 16: within 5–26 min of cutoff, still IN (strict <22:00Z).
- 1-2 Anthropic post 2026-10-09 22:04:59Z: 5 min AFTER start (inclusive) → IN (edge, disclosed).
- Day-only dates (no clock): 1-3 (Oct 7), 1-4 (Oct 8), 2-2 model (Oct 6), 2-3 (~Oct 8) → OUT-BG by day even without clock; chatter timestamps do not promote them.
- Month-only / undated: none among Daily X topics (all have at least day + X timestamp); carry-over items with month-only dates handled in carryover table.
- 2026-10-10 Daily X (W41): NOT used as W42 report; only boundary reference (1-2/2-1 continuity checked, no double-count).

## Outside-window rule applied
- Daily's own "window-outside" labels refer to the 1-day obs window. Re-evaluated: e.g., 3-1/3-2 official Oct 12 posts were "in" their Daily window AND in Weekly; 1-3/1-4 official Oct 7/8 were "outside" Daily window but ALSO outside Weekly → confirmed OUT-BG (not promoted by in-window chatter).
- No topic was promoted solely on report inclusion; every IN requires event/X-post inside Weekly range.

## Residual timing risks
- X timestamps are post-creation times, not underlying event times (e.g., pricing-page update time unknown; Rosalind-discovery page-change instant unproven → Evidence must pin via page history/docs).
- Vendor blog dates are day-granularity (Oct 12/13/15/16); intraday order vs cutoff verified by X post clocks where available.
- Unverified claims (RSIArena, Qwen Turbo, Falcon ASR, Apple China, export control, EU enforcement) carry TIME_UNRESOLVED or SECONDARY-DATE-ONLY and must not anchor cutoff arguments.
