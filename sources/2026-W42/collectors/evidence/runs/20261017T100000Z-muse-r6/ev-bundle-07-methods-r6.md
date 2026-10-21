# r6 methods corpus — papers/reports full-text depth (2026-10-17)

Run: `20261017T100000Z-muse-r6`.

## 1. PAT paper arXiv 2606.28277 — FULL TEXT CONSUMED (HTML)
- Pipeline: segmenter → Light/Medium/High thinking tracks → Deep Review agents (Gemini Deep Think) → synthesis with Google-search grounding; vs single-call (context budget) and Pass@k (precision collapse) baselines.
- SPOT case study: 26 papers/29 eq-proof errors; grader = logic-aware + human audit; 21.1% SOTA → 55.2% zero-shot → 89.7% PAT (+34pp); Banach-space counterexample anecdote.
- Pilots: STOC Nov 2025 (math pipeline) + ICML Jan 2026 (generalized); 4,700 submissions; survey n=124/733: reuse 97%/92.1%, theory gaps 11.6%/35.4%, new experiments 31% (ICML); named professor quotes; limitations: date hallucinations, PDF parsing, false-incorrect claims.
- Taxonomy Roles 1–4 (SAE parallel): Tool-for-Authors (pilots' role), Tool-for-Reviewers, Supporting Reviewer (+3.5 ratings), Total Automation (AIrXiv vision); Pangram 21% AI reviews; AAAI-26 pilot; NeurIPS consistency 23% vs 35% random; Table 1 submission stats 2020–2026.
- Paper itself Jun 26 OUT (background); Oct 14 LAUNCH/API is the W42 event. No independent audit of pilot stats.

## 2. Earth AI report arXiv 2610.15750 — FULL TEXT CONSUMED (HTML, appendices skimmed)
- Submitted Oct 11 IN; 39 pp; 37 authors. GRA: 23 skills, 62 tools, scratch datasets, upfront planning + execution guidance (proxy substitution, 3-strike dead-end, best-effort mode).
- Benchmarks: GeoExpertQueries 101 (25 dev/76 test; 3-expert golden workflows; tool-agnostic autorater; 4 unreconciled queries kept as multi-workflow); GeoKTools 305 (85/220; K=1–4 tool types); CBGB 45 (adapted); UnivEARTH 140 (saturated 87–94).
- Results: GeoExpertQueries 63 (baselines ~unusable), GeoKTools 86 vs 41, CBGB >80 vs <20; tools 3→52, planning 52→63 (Flash); Flash ≥ Pro cheaper. Cost: Oct 2026 token rates incl. failures; 100 calls/30 min/1M ctx caps; 3 repeats.
- Limits stated: autorater-vs-workflow (first-draft framing); best-effort proxy mode; saturated UnivEARTH; single-model-family eval (Gemini 3.1 Pro/3.8 Flash only).
- Dev splits + autorater prompts + scoring code released (reproducibility anchor, unexecuted here).

## 3. VERID paper (gstatic PDF, 16 pp, dated 2026-10-16 IN) — FULL TEXT EXTRACTED (pdftotext)
- Semantic digital twin: queryable introspection, time-compressed simulation, trace persistence, safe execution; 3 dye/water case studies; 5x+ accuracy gain across feedback cycles; HITL + biosecurity (§4.5: operational safety, HITL review, automated biosecurity) + methods/scoring appendices.
- Status: IN-window paper; methods consumed at structural + headline-number level (full equation-level audit not attempted).

## 4. Aptamer paper (gstatic PDF, 27 pp) — FULL TEXT EXTRACTED
- Exact counts: thrombin 0/167 → 54/208 → 131/311 (42.1%; 37.1% strict de novo); myoglobin 20/196 → 9/244 → 184/549 (33.5%); G4 collapse 75.0%→19.1% → recovery 72.4%; 8-clone titrations; R.2 0→42% lab-in-loop.
- Failure-mode learning (primer overhangs, G4 stickiness) is the substantive finding, not just hit rates.

## 5. Epitope paper (gstatic PDF, 17 pp) — FULL TEXT EXTRACTED
- HITL 5.06%→9.33% hit rate + 42% GPU cut (fixed budget); MSA-omission doubling artifact (method caveat — apparent yield inflation mechanism documented); yeast-display nanomolar binders; AlphaFold3 token-bucket bottleneck analysis.

## 6. Nemotron tech report PDF (79 pp, research.nvidia.com) — FULL TEXT EXTRACTED
- MOPD multi-teacher on-policy distillation (text-only base → multimodal agent); teacher specialization; SFT pipeline; MTP boosting 4.287→4.718 acceptance (greedy); QAD 99.62% median recovery over 36 benchmarks; 4,856 tok/s/GPU GB200 @≥50 tok/s/user; 2.34×/1.90× vs Qwen3.5/Flash-Next; Indic +10B (IIT Madras, 2.8T/22-lang set released); SWE-Pro 51.78% @4.6× fewer active.
- Vendor-run; harness/denominator appendix detail partially skimmed (full 79pp audit not attempted; logged).

## 7. Beam safety report (reflection.ai) — SUBSTANTIAL BODY CONSUMED (page sections)
- OSF framework; Bio/Chem/Cyber eval batteries with interpretation+limitations blocks; ISE refusal ~89%; comparative tables (e.g., bio-knowledge rankings with Kimi K3 leading one slice); n=20 human-uplift study (uncertainty-flagged); harness-confound caveats stated on-page.

## 8. Sakana MLR — PAPER TRACED (arXiv 2610.11087, Oct 8 OUT; TMLR) + INDEPENDENT PRESS
- 3 agents (Haiku 3.5 appendix, Sonnet 4 lit-review + review); Contradiction Benchmark (257 papers, 1,164 planted, GPT-4.1 rewriting); 73.43% distance-0 (4 reviews) / 60.79% single / 40.95% overall; WithdrarXiv 26.07%/16.11%; $0.47/review; Pearson 0.586; adversarial vulnerability ADMITTED.
- X-discussion Oct 11 IN (background retained). MarkTechPost Oct 10 + LinkedIn corroborate numbers.

## 9. Amazon RWM paper — TRACED (arXiv 2610.12235, Oct 8 OUT) + INDEPENDENT CRITICAL REVIEW
- Full numbers (2,653 records, 171,862 H100-h, 0.506→0.774, NDCG, Regret −52.2%, +15.8%/+11.6%, 13-LLM ablation, Opus 5 backbone) PLUS Pith independent review: cross-env non-significance 2/5 targets, single-env Autoresearch, Marin exception. Exemplary vendor-vs-independent separation. Background retained.

## 10. Minecraft Argon paper — TRACED (arXiv 2610.22319, submitted Oct 15 IN)
- 27h14m, 2,783 programs, 605 deaths, 229 messages, Easy/random-seed, Mineflayer-only, no human input (dashboard present), prior-wins acknowledged, limits (single run, structured info not vision, prior knowledge, no ablations). Secondary coverage Oct 16 (AIWeekly, OnTheWire). Evidence-depth follow-up for Argon card (NOT a new discovery record — accepted chain immutable).

## 11. Harness-17 paper — NOT_FOUND after bounded retry
- Queries run (agent-harness evaluation framings); found Doc2Harness/VeriHarness/TRACE/Interlock/LHTB (distinct works) but NOT the X-described "17 authors" paper. Explicit HOLD; do NOT conflate look-alikes.
