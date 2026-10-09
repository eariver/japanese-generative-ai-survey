# Collector raw — Ollama v0.35 decision-model support (Sep 29 interface)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (search-excerpt + blog-header capture; full endpoint spec NOT re-fetched in this run)
- source_url: https://ollama.com/blog/ollama-now-supports-jev-style-decision-models
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-29 (vendor blog header; v0.35.0 release Sep 28 per third-party release notes; /v1/systemone endpoint)
- access_status: CONTENT_ACCESS_LIMITED (header + search excerpts consumed; full docs/repo diff pending Evidence gap-fill)

## Consumed claims (claim-level)

1. EVENT: Ollama added Jev-style decision-model support via /v1/systemone in v0.35 (Sep 28-29, 2026), based on TypeSafe Jev API; typed choices/probabilities/scores instead of text; e.g. ticket triage, model routing, classification. (PRIMARY_FACT as vendor feature announcement, date-bounded by blog + release notes)
2. MODELS: Nimble (Bespoke Labs) + Tev1 (Together AI) pullable at launch (`ollama pull nimble`); example curl + typed response with confidence 0.8906 documented in release notes mirrors. (PRIMARY_FACT as vendor availability statement; needs repo/doc pin)
3. POSITION: Precedes Oct 1 Clef/Decider 2B weights; serving interface, not a model release itself. Do not merge with Clef/Decider benchmarks. (EDITORIAL_BOUNDARY)

## Boundaries / unresolved

- Full endpoint schema, M5 Max 91ms Pac-Man illustrative figure (Sol register), and registry vs ollama.com URL canonicalization need direct doc/repo capture before Evidence.
- Vendor latency/accuracy figures, if any, are illustrative, not universal performance.
