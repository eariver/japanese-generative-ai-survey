# W42 r2 bundle — Google Deep Review + wet-lab agents + Earth AI (full bodies consumed, 2026-10-17)

Collector run: `20261017T071000Z-muse-r2` / collector_id `primary-webfetch`
Observed at: `2026-10-17T07:15:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES` (bounded excerpts, not byte archives).

## 1. Official: Analyzing technical documents with Deep Review (research.google, Oct 14, 2026) — BODY CONSUMED
- URL: https://research.google/blog/analyzing-technical-documents-with-deep-review/
- Page date Oct 14, 2026 → IN-WINDOW.
- Core facts (source-backed):
  - Public launch of Deep Review agentic document-review system (evolution of Paper Assistant Tool / PAT pilots: STOC 2026, ICML 2026, NeurIPS 2026, ICLR 2027; 16,000+ opt-in manuscripts).
  - Four-stage pipeline: (1) document segmentation (overlapping logical segments), (2) adaptive compute budgeting by information density, (3) deep parallel verification swarms with full-doc context, (4) global synthesis + agentic grounding (external tool checks vs hallucination).
  - Scope expanded beyond papers: design docs, presentations, legal/finance (consistency, ambiguity, grounding).
  - Access: 2 free reviews/week; Gemini API key for higher limits + Deep Review API; PDF/plain text now, multi-file soon; uploads NOT used for training, stored 1 year for UI display.
  - Validation-bottleneck framing (74,000+ submissions to ICLR/NeurIPS/ICML 2026 vs 45k/32k/23k); Gemini 4 Argon support improves quality further; Teamwork Deep Document Review Pattern in Antigravity (`/teamwork-preview`).
  - Accompanying paper: arXiv 2606.28277 (submitted Jun 26 2026 — OUT-of-window background; the Oct 14 LAUNCH is the W42 event). Abstract: 4-level AI-human collaboration taxonomy; PAT +34% over zero-shot recall on math errors (SPOT); STOC+ICML pilots. Full PDF not parsed (abs-level only).
- Chronology honesty: paper Jun 2026 OUT; launch + API + Antigravity pattern Oct 14 IN. Classify research/product (agentic review system + public API).
- AUTHORITY_CONSUMED (blog body); paper PDF full text: UNCONSUMED (abs only) — logged limitation.

## 2. Official: Grounding AI agents in biological reality / autonomous wet labs (research.google, Oct 16, 2026) — BODY CONSUMED
- URL: https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/
- Page date Oct 16, 2026 → IN-WINDOW.
- Core facts:
  - Three projects: VERID semantic digital twin (live 3D volumetric entity tree over PyLabRobot; dry-run sim, hardware safety gates, video+action logs; 5x reconstruction accuracy gain; mid-run plate-reader recovery; tip-carryover diagnostic) + aptamer closed-loop sandbox (3 rounds, myoglobin 33.5% / thrombin 42.1% on-target, G-quadruplex stickiness artifact learned) + epitope-excision protein design (FAP single-digit nM binders; 8.6x folding speedup; human-agent 2x in-silico hit rate; yeast display + FACS).
  - Three full papers linked (VERID, aptamer sandbox, epitope excision PDFs on gstatic — NOT fetched; titles/claims from blog only).
  - Safety: Frontier Safety Framework + bioresilience; non-infectious testbeds, biosecurity screening, sim-before-execution, human authorization of sequences/protocols/runs.
- Distinguish headline (single-digit nM) from boundary (one target FAP, human-agent hybrid, vendor-reported). AUTHORITY_CONSUMED (blog); 3 PDFs UNCONSUMED — logged.

## 3. Official: Putting Earth AI to work / Geospatial Reasoning agent (research.google, Oct 14, 2026) — BODY CONSUMED
- URL: https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/
- Page date Oct 14, 2026 → IN-WINDOW. Tech report arXiv 2610.15750 (submitted Oct 11 2026 16:31 UTC — IN-window; 39 pp; 37 authors).
- Core facts:
  - GRA = Gemini-powered agent over Earth AI foundation models (WeatherNext, Flood, PDFM, AlphaEarth, Remote Sensing) + Maps/ Earth Engine/ Data Commons; modular skills, upfront planning, dedicated spatial workspace, BYO data (CSV/GeoJSON/cloud), Planetary Prediction Engine.
  - Benchmarks: GeoKTools + GeoExpertQueries NEW (dev splits released on GitHub) + CBGB + UnivEARTH (saturated: standalone LLM 93.6%). Finding: tools = largest step; planning adds open-ended gain; Flash matches/exceeds Pro at lower cost. GeoExpertQueries scored by autorater vs golden workflows (first-draft, not final answer — limitation stated).
  - Partners: WHO AFRO Ebola (48 settlements/45.5k people), PiN cyclones, GiveDirectly, WPP, Milken. Early access: Ask Google Earth deep-research preview + A2A API.
- Gen-AI scope call: IN SCOPE — agent orchestration (skills/planning/tools/A2A) over foundation models is squarely generative-AI Weekly material (planning/tool-use evaluation + agent API). Not a pure geo-data release. INCLUDE with this written reason.
- AUTHORITY_CONSUMED (blog + report abstract/submission record); report PDF full text UNCONSUMED (abs-level) — logged.
