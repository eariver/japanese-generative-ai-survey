# Retrieval provenance (edition-local collector raw, NOT exact HTTP bytes)
- source_url: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- retrieved_at: 2026-09-19T00:00:00Z (worker webfetch markdown excerpt; exact HTTP bytes not captured)
- collector_id: primary-webfetch
- collector_run_id: w38-primary-20260919-r1
- published_date_on_page: Sep 15, 2026 (page front matter "published: Sep 18, 2026, 11:44 PM UTC" appears to be fetch/transform artifact; article header says Sep 15, 2026; secondary corroboration Sep 15-18 — treat Sep 15 as publication date)
- authority_class: PRIMARY_OFFICIAL (TypeSafe AI first-party lab blog)

# Introducing System One Models & Jev (excerpt, founder Diogo Almeida)

TypeSafe AI releases first System One Model: new class of frontier models for fast, structured decisions software can use directly. New stack: new model architecture + parallel sampler + training method "Reinforcement Learning for Calibrated Decisions (RLCD)".

Jev (early access, available today): similar intelligence on System One tasks vs existing LLMs; ~2 orders of magnitude faster/more efficient. Gives up string generation; optimized for structured outputs; "can't hallucinate" (schema-bound: never makes type errors; calibrated probabilities/confidence scores).

Positioning: "frontier-intelligence function call: unstructured state in, typed probabilistic decisions out." Primitives (Noul/Choice/Score); structured program state inputs; parallel sampling (all outputs single query); hardware-aware.

Pricing: input $0.042/MTok ($42/B tokens); output FREE (too cheap to meter). Speed: 70ms-500ms end-to-end (claimed 40x-200x faster same intelligence); workflow evals claim up to 193.6x faster / 444.6x cheaper (stated higher-end). Confidence: calibrated (higher confidence = higher accuracy), consistent.

Use cases: AI-powered workflows/smart if-statements; map-reduce over big data; real-time apps; verify-everything (score/judge/verify/guardrail/jailbreak-detect).

Evals (vendor-reported with nuance sections): side-by-side demo vs GPT-5.6 Terra (simplified query caveat); 4 workflow evals vs GPT-6 Astra + Fable 5.1 average as reference (possible bias noted on page); hallucination/type-safety (LLM numbers from OpenRouter, own 0% non-empirical/schema-guaranteed); Doom + Wikiracing fun demos (caveats on page).

What's next: early access; waitlist; docs.typesafe.ai; evals.typesafe.ai; github.com/typesafe-ai/system-one-adapter-python.

## Claim boundary notes (Sol consumption)
- VERIFIED from this page: lab/product existence; System One framing; RLCD method name/purpose; early-access availability; pricing/speed figures as vendor-stated commercial/technical claims (NOT independently measured); schema-guarantee logic (mathematical, per page) vs empirical quality claims.
- Do NOT convert to: parameter counts/topology/loss (absent); "can't hallucinate" beyond schema-bound scope (wrong choice still possible — page-adjacent nuance + secondary analysis); community latency/pricing summaries as technical architecture.
- Release timing: page header Sep 15 (inside W38); exact hour unverified — ordinary-window membership supported by date + X ordinary rows Sep 15/17 + secondary Sep 15-18.
