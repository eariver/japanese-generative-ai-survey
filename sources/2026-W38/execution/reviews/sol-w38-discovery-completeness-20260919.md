# W38 Sol Discovery completeness review

Status: `SOL_DISCOVERY_COMPLETENESS_REVIEW / NON_BLOCKING_WITH_INDIVIDUAL_LIMITS`
Date: `2026-09-19T04:50:00Z`
Issue: `2026-W38`
Discovery acceptance: `sources/2026-W38/discovery/discovery-accepted-v2.json` (13 records, graph validated)
X manifest: `COMPLETE`, run `weekly-x-2026-W38`, discovery `w38-grok-r2-25-url-ledger` bound

## Surfaces exercised

- Grok/X r2 Raw (25 URLs: 23 ordinary / 0 pre-window / 2 late-breaking, Sol-corrected 7 ordinary INDEPENDENT) as one sensor, not universe
- Primary official: OpenAI Astra for Law Sep 17, Google Gemini 3.8 Live Sep 15, Anthropic LSVP Sep 17, Anthropic Accenture Sep 18, Anthropic R&D metrics Sep 17, TypeSafe Jev Sep 15, Amodei pacing essay Sep 12, Cognition Devin Code Scans Sep 16, Character.ai CAI-Image Sep 16, PixAI Tsubaki.3 Sep 16
- Secondary/carry-over: DeepSeek V4-Pro routing occurrence Sep 14 (secondary-verified), GLM-5.5 absence re-verified (rumor disposal)
- Web open-world sweep for Sep 11-18 window across all 12 lanes (15-item sweep + Grok verification pass)

## Lane coverage (12 required)

- A Foundation/Reasoning: Astra for Law (Astra base pre-window context), Anthropic R&D index, Jev System One — COVERED
- B Agents/Coding/Harness: Astra for Law workflows, Gemini Live voice agents, Devin Code Scans, Jev routing — COVERED (strong)
- C Multimodal: Gemini 3.8 Live visual grounding, CAI-Image — COVERED
- D Image Gen/Edit: CAI-Image (Qwen-Image post-tune), PixAI Tsubaki.3 GA — COVERED
- E Video Gen/Edit: PixAI Tsubaki Video series (creator tool); HiDream-O1 / Creatify Boreal press items secondary-only, not primary-ev evidenced — PARTIAL (honest: foundation video-model lane thin; creator-tool coverage only)
- F Speech/Audio/Music: Gemini 3.8 Live speech-to-speech — COVERED
- G Open Weight/Local/Quant: DeepSeek V4.1-Flash MIT (carry-over occurrence), GLM-5.5 absence note, CAI Qwen-Image lineage — COVERED (as operational/lineage notes, no new W38 open-weight drop)
- H Inference/Serving/Systems: DeepSeek Sep-14 routing cutover (secondary PARTIAL), Devin Agentic MapReduce (vendor-described) — COVERED with stated limits
- I Memory/Multi-Agent/Retrieval: examined (xAI Grok Build memory + Claude Code Projects secondary-only, not primary-retrieved; no W38 primary) — QUIET (legitimate; secondary leads disposed at Screening, not silently dropped)
- J Evaluation/Benchmarks: Anthropic R&D index methodology, vendor bench tables (Vals 54.0/38.7, S2S 82.6, tau-Voice), Real-SWE/BLINDSPOT secondary-only — COVERED with vendor-reported bounds
- K Safety/Security: LSVP, Accenture embedded evaluation, Amodei essay, Astra privilege counter-signal — COVERED (strong)
- L Other Emerging: Jev structured decisions, Bodhan Indic suite (secondary-only, primary pending) — COVERED (Jev primary; Bodhan disposed as secondary-only)

## Negative-space sweep

- Checked OpenAI (Astra Sep 3/10 pre-window context captured; Law Sep 17 in-window), Google (Flash Sep 2 pre-window; Live Sep 15 captured), Anthropic (3 in-window posts + essay captured), TypeSafe (captured), Meta/xAI/Mistral/Qwen (no new W38-window primary located in sweep), Z.ai (no 5.5; 5.3 Aug pre-window)
- Image lane covered by two primaries; pure foundation video-model lane thin after targeted check — recorded as limitation, not gap-fill failure
- No silent drop of technically material alternatives detected at Discovery stage

## Duplicate/concentration

- Anthropic triple (LSVP / Accenture / RDI) are distinct Sep 17-18 publications, not duplicates
- Image double (CAI-Image / Tsubaki.3) are distinct vendor lines, not duplicates
- 13 records not inflated by X ledger (1 record for 25 URLs)

## W37 carry-over

- Released W37 authority scanned fresh (14 discovery records, all BASE carry_over:false; 12 SELECTED MATERIAL primaries all pre-W38; 1 HOLD safety-resignation; 1 EXCLUDED/DROP GLM rumor; 20 late-breaking X URLs; DeepSeek Sep-14 routing future-tense; Sep-11 distillation naming detail)
- Disposition: DeepSeek routing occurrence re-verified in-window (CARRY_OVER record, secondary PARTIAL); GLM-5.5 absence re-verified (CARRY_OVER record, DROP); Sep-11 distillation naming detail NOT pursued (no fresh primary located in sweep; X-only; disposed explicitly — residual risk noted); W37 HOLD safety item stale (no fresh W38 development); 24 ordinary + 1 pre-window W37 X URLs disposed as stale
- Two CARRY_OVER Discovery records with explicit external parent refs; no W37 decisions copied

## Residual limitations

- All primaries via webfetch excerpts (curl blocked); claim-relevant excerpts stored, full pages consumed at claim level 2026-09-19
- Vendor benchmarks unreproduced (Vals, S2S/tau-Voice/BBA, Jev workflow evals, Devin pilot metrics) — carried as stated-with-attribution
- Accenture announcement hour not on page (date Sep 18; ordinary membership via date + X row 20:05Z)
- Jev/TypeSafe exact hour unverified (Sep 15 date + corroboration)
- Amodei essay day via secondary Sep-12 + Accenture backlink (month-certain on page)
- DeepSeek routing primary-docs capture open (secondary PARTIAL)
- Biomolecular-optimization dedicated repo NOT located — PARTIAL/UNRESOLVED, must not be claimed
- E-lane foundation-model thinness; I-lane primary-quiet; both legitimate after check

## Verdict

`NON_BLOCKING` — Discovery is sufficient basis for Screening/Evidence. Proceed to CANDIDATES_NORMALIZED via canonical Screening. No Exception Gate.
