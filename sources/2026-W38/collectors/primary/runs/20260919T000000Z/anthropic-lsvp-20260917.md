# Retrieval provenance (edition-local collector raw, NOT exact HTTP bytes)
- source_url: https://www.anthropic.com/news/life-sciences-verification-program
- retrieved_at: 2026-09-19T00:00:00Z (worker webfetch markdown excerpt; exact HTTP bytes not captured)
- collector_id: primary-webfetch
- collector_run_id: w38-primary-20260919-r1
- published_date_on_page: Sep 17, 2026
- authority_class: PRIMARY_OFFICIAL (Anthropic first-party announcement)

# Introducing the Life Sciences Verification Program (excerpt)

Today, we are introducing the Life Sciences Verification Program (LSVP), which gives life science professionals access to our Mythos, Opus, and Sonnet models with a refined set of safeguards more permissive for biology-related work. Already onboarded dozens of organizations via early access; now opening applications to broader life-science community. Launching in beta, initially for teams and institutions; individual Pro/Max plans later.

LSVP enables work currently blocked in generally available Fable models: drug discovery, research biology, clinical development, manufacturing. Built for academic labs, startups, pharma.

## Verification and access types
- Applicants pass verification: research credentials, security standards, ethical research oversight review.
- Standard Use grants: most life-science work; extended to entire teams; renewed yearly; access to Mythos, Opus, Sonnet with refined classifiers more permissive for science; applies to Mythos 5.1, Opus 5, Sonnet 5 today and future models. Covers basic science, R&D, supply chain/manufacturing, clinical development, QA, regulatory affairs, investing/diligence.
- High-risk Use add-on: single research project (not full team); renewed every 6 months; removes all safeguards blocking life-science requests (e.g., characterizing one viral-vector family's immune recognition). Available today for Opus 5 and Sonnet 5; Mythos high-risk limited to small set with additional vetting pending US government coordination.
- Other safeguards (e.g., cyber classifiers) remain. Offline monitoring replaces real-time blocking: 30-day data retention for flagged activity; strictly compartmentalized, not used for training, inaccessible to life-science research teams; integration with Enterprise Frontier Safeguards (EFS) explored.

## Threat models addressed
Access compromise (malware/account takeover), insider threats (rogue/coerced employees), agent misuse (swarms, long-horizon). Usage tied to stated use-cases; continuous monitoring flags out-of-scope patterns to org admins with pre-agreed triage timeframes.

## Availability
First-party console (API), Claude Enterprise/Team plans. Not on third-party platforms; beta not for BAA-enabled orgs (PHI customers use separate non-BAA orgs). Expect hundreds of orgs in first week.

## Claim boundary notes (Sol consumption)
- VERIFIED from this page: LSVP existence/launch (Sep 17 2026); Mythos/Opus/Sonnet scope; Standard vs High-risk grant mechanics; 30-day retention; beta/team-only limits.
- Mythos 5.1 association appears in this LSVP page (Standard Use applies to Mythos 5.1 today) — the "Mythos 5.1 launch" itself is NOT evidenced here; do not date Mythos 5.1 release from this page.
- Dual-use/biology risk framing is vendor context; wider community risk discussion retained as context only.
