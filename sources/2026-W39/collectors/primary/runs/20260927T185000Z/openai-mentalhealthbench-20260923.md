# Collector raw — OpenAI: Introducing MentalHealthBench (Sep 23)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:41:00Z (webfetch excerpt of live page)
- source_url: https://openai.com/index/introducing-mentalhealthbench
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-23

## Consumed claims

1. EVENT: Open benchmark for AI responses in realistic mental-health conversations, co-created with 80+ licensed psychologists/psychiatrists across 22 countries, 19 languages, ~20 subspecialties. (PRIMARY_FACT)
2. DESIGN (vendor-described): 1,215 synthetic conversations (privacy-preserving, reflect real usage); acuity spectrum non-acute/high-acuity/emergencies; personas adults/teens/caregivers/clinicians, multilingual; rubric criteria per conversation (weights -10..+10), each reviewed by ≥3 experts, retained on ≥2-expert agreement without third-expert contradiction. (PRIMARY_FACT as design description)
3. GRADING BOUNDARY: automated grader is GPT-5.6 Sol (vendor model grading vendors' benchmark) — methodology circularity risk explicitly noted; paper describes settings in detail (paper NOT separately consumed). Scores normalized per behavior; experts emphasize context-seeking, users emphasize tone/next-steps (44-adult side study, non-acute only). (PRIMARY_FACT with disclosed grader identity)
4. RESULT FRAMING: "steady improvement" vendor reading; ChatGPT-not-therapy disclaimer; adjacent product moves (crisis resources, Trusted Contact, ChatGPT for Teens) cited. (VENDOR_CLAIM + context)

## Boundaries

- Grader-model overlap (GPT-5.6 Sol) means scores are not independent validation of OpenAI models; treat comparative readings as vendor-framed.
- Paper-level methodology (agreement stats, grader validation) not consumed — no deep methodological verdict.
