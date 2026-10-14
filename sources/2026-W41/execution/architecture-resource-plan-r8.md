# W41 Architecture editorial resource plan r8 (Repair R7-01)

Status: `EDITION_LOCAL / EDITORIAL_BUDGET / NON_PAGINATION`
Date: 2026-10-12 JST
Architecture: `sources/2026-W41/architecture-v2.json` (`3554041e…`, 6 packages, PROPOSED)
Roles preserved: 5 PRIMARY exactly once, 15 SUPPORTING at least once, 20/20 placed.
No HOLD promotion, no new articles from HOLDs, no page-count cap.

This plan is an Architecture-stage editorial budget, NOT measured PDF pagination.
No rendered page count is fixed at this stage. Ranges below are grounded in Evidence:
per-package `must_cover_requirements` counts from the canonical Architecture
(P1:4, P2:5, P3:7, P4:3, P5:5, P6:3 = 27 total) plus required comparison tables
(P1, P3, P5) and spec/figure boxes. Paragraph estimates assume a dense Weekly
register (roughly 90–130 Japanese characters per paragraph equivalent of explanatory
prose plus table/box callouts); word ranges are proportional shares, not layout promises.

## Issue-total technical volume

- Planned substantive body: **57–80 paragraphs** across 6 packages plus 3 required
  comparison tables and 5–7 spec boxes. Basis: 27 must-cover items at roughly 2–3
  paragraphs each (54–81), rounded down for shared table callouts.
- Relative resource shares: P1 20% / P2 18% / P3 25% / P4 7% / P5 18% / P6 12%.
  Largest is P3 (7 must-covers plus the 7-row availability table); smallest is P4
  (single brief, 3 must-covers, one spec box).
- Tables/figures total: 3 comparison tables (P1 tier-price-latency; P3 availability;
  P5 modality-gating-status) + 5–7 spec boxes (Haiku price card, Decisions changelog
  excerpt, Kolibri scale, Nano spec, textGrain figures, Cyber terms, math listing).
  Sourcing is first-party pages and bounded excerpts only; no invented figures.

## P1 — Frontier rollout week (PRIMARY GPT-6 UI + Haiku)

- Article type: LEAD deep-dive (two flagship rollouts as one priced pair).
- Editorial purpose: tier/date/tab mechanics plus price cards with the latency
  definition kept exact; benchmarks stay vendor-attributed.
- Body: **11–15 paragraphs** (4 must-covers: rollout table 3–4, 44% definition 2–3,
  Haiku card 3–4, bench attribution + boundaries 2–3, plus table callout 1).
- Mechanisms/params/conditions: tier mapping (Plus/Pro/Business/Enterprise Oct 7,
  Free/Go Oct 8, Chat tab, Sol/Luna); 44% time-to-start on web-search questions
  (GPT-6 Instant vs 5.6 Instant denominator); split ≤/>100k rates + Sonnet halving;
  bench table values as publisher-measured.
- Tables/figures: P1 comparison table (tier / price / availability / latency-definition
  columns, 2 flagship rows + Ultrafast pointer row) with ~2 paragraphs of callout.
- Resource share: ~20% of issue body. No cap implied; if Draft exceeds, split the
  Haiku card into a sidebar rather than cutting boundaries.

## P2 — Agent and Decisions infrastructure (PRIMARY Decisions + 4 SUPPORTING)

- Article type: platform deep-dive with briefs and one comparator box.
- Editorial purpose: verified changelog versus forum observations versus stub.
- Body: **10–14 paragraphs** (5 must-covers: changelog 3, decider 2–3, embed 1,
  Ultrafast box 2, Gemini box 2, plus transitions 1).
- Mechanisms/params/conditions: `v1/decisions` endpoint + gpt-6-luna binding + beta
  status; 10x claim without methodology (stated as absent); decider Index/Bench forum
  figures with README-unfetched boundary; Ultrafast tier/residency without latency numbers;
  Gemini bullets with unfetched box.
- Tables/figures: changelog excerpt box (Decisions entry verbatim) + forum-figure box;
  no comparison table required (single verified anchor + briefs).
- Resource share: ~18%. Embed stays one paragraph (one-liner); Gemini stays a 2-paragraph
  box. Expansion beyond these bounds would require fetched README or Cloud blog (absent).

## P3 — Shipped vs promised weights + speech (PRIMARY Kolibri + 6 SUPPORTING)

- Article type: survey deep-dive anchored by availability table (largest package).
- Editorial purpose: availability states separated honestly; speech pair inside same group.
- Body: **14–20 paragraphs** (7 must-covers: Kolibri 3, Liquid 2, EGemma 2–3, Beam+Mistral 3–4,
  Clef 2, Nova 2, table callout 2; shared scale framing absorbs the rest).
- Mechanisms/params/conditions: MoE active/total pairs, context lengths, license strings
  as stated, stated locations, weight-date states; MRL/embedding dims; price points as
  stated; timestamp pin (JSON-LD 18:27:34Z vs post-cutoff X); GA regions.
- Tables/figures: P3 availability table (7 rows; columns stated-license / stated-location /
  download-status / weight-date) with ~2 paragraphs callout + MoE scale box.
- Resource share: ~25%. If Draft runs long, cut Beam/Mistral comparator prose first
  (promised weights), never the availability table or version-pin box.

## P4 — Image brief (SUPPORTING Nano Banana 2.1)

- Article type: small spec brief (smallest package, by evidence boundary).
- Editorial purpose: card-positive specs with one narrowed blog line.
- Body: **4–6 paragraphs** (3 must-covers: spec box 2, narrowed blog line 1, Elo caveat 1,
  plus boundaries pointer 1).
- Mechanisms/params/conditions: base series, 1M input, 4K image + 64K text output,
  7-channel distribution, vendor side-by-side Elo (unresolved arena basis).
- Tables/figures: one spec box; no comparison table (single member).
- Resource share: ~7%. Expansion is forbidden without a fetched docs page or arena basis.

## P5 — Provenance week (PRIMARY textGrain + SynthID)

- Article type: methods deep-dive (issue's only first-hand quantitative read + scope brief).
- Editorial purpose: read numbers versus stated scope with no cross-modality transfer.
- Body: **10–14 paragraphs** (5 must-covers: FPR points 3, rollout/gating 2, SynthID scope 3,
  non-equivalence 1, table callout 1–2, PDF-unread boundary 1).
- Mechanisms/params/conditions: 1% FPR operating points (~80% at 200 tokens, ~95% at 400),
  edit-weakening numbers, quality table (all vendor-run, first-hand read); API opt-in,
  EU rollout window, researcher gating; portal modalities/partners/scale with text excluded.
- Tables/figures: P5 comparison table (artifact / modality scope / gating / verification-status
  limits) + FPR figure box (blog numbers only).
- Resource share: ~18%. The FPR section carries the deepest methods prose in the issue;
  PDF internals are explicitly out of budget (binary-unparsed).

## P6 — Safety and science briefs (3 SUPPORTING)

- Article type: bounded digest (three briefs, no synthesis claim).
- Editorial purpose: program terms, results listing, simulated eval with non-claims explicit.
- Body: **8–11 paragraphs** (3 must-covers at 2–3 each plus digest framing 2).
- Mechanisms/params/conditions: CIDP partner count + scanner terms + >90% expected figure;
  repo/Lean/summary/compute listing with withheld identity; 11 EDGAR-simulated tasks with
  vendor deltas and provisional status.
- Tables/figures: three term/listing boxes; no comparison table (independent briefs).
- Resource share: ~12%. Promotion to deep-dives would require fetched scanner post,
  enumerated repo, or released rubric respectively (all absent).

## Budget integrity notes

- Ranges derive from must-cover counts and table obligations in the canonical Architecture;
  no HOLD content is budgeted anywhere; Grok ledger budgets zero article paragraphs
  (methods provenance line only); INSPECT sidebars (usage-policy, ELYZA) budget zero unless
  Architecture-legality review later admits a sidebar slot.
- No maximum page cap is set at Architecture (`target_pages`/`max_pages` remain null by
  Core contract); the shares above are proposals. Downstream Draft may reallocate shares
  but must not silently drop boundaries or inflate briefs into deep-dives without new evidence.

(End of file)
