# Evidence collector run r3-A — OpenAI first-party bundle (2026-10-12)

Capture: MIXED — DELEGATED subagent webfetch excerpts (verbatim, marked) + Muse DIRECT_READ corroboration for textGrain blog and API changelog.
No original-byte HTML captures (NO_BYTE_HTML). PDF bytes unparsed.

## A1. textGrain blog https://openai.com/index/eu-text-provenance/ — DIRECT_READ (Muse) + DELEGATED corroboration
- Date: October 5, 2026 (IN-WINDOW). Title: Our approach to EU text provenance rules.
- Scheme (vendor): invisible statistical signal in word choices; detector looks for signal.
- Detection (vendor): FPR target 1%; ~80% @200 tokens vs ~95% @400 tokens (psychology/ELI5); substantially lower for mathematics; synonym-edit 400tok 92%->66% (10%) ->17% (25%).
- Rollout (vendor): API global opt-in for select models (off default) from Oct 5; EU ChatGPT/Codex eligible output over coming weeks (EU only, all plans); detector application-gated to approved researchers/expert orgs.
- Limits (vendor): 5 non-claims (contribution/ownership/user/accuracy; absence != human proof).
- Quality table (vendor, Astra max): AAP Index 49.57/49.76, AutomationBench 34.09/34.86, DeepSWE 72.80/71.68, TB4 53.90/56.06, TBSci 56.90/60.00, BrowseComp 87.92/87.35, HealthBench 64.27/64.60, GPQA 94.44/93.94.
- Open-source intent (vendor): plan to open-source; tech report to be updated.
- NOT on page: pricing, license text, select-model list, detector criteria.

## A2. textGrain tech-report PDF — DELEGATED, NOT_ACCESSIBLE direct
- Direct fetch returned binary (unparsed). Title/authors/method second-hand via search only: "textGrain: Entropy-Calibrated Watermarking..." (Oct 5 2026, 20pp per third-party). Authors second-hand: Li/Wen/Chen/Long/Jain/Joly/Lam/Song/Su. Method second-hand: token-generation coupling via optimal transport + Gumbel/KL, detector needs text + secret key only.
- Evidence class: AUTHORITY_CAPTURED_BUT_UNCONSUMED (link known, body unread).

## A3. API changelog https://developers.openai.com/api/docs/changelog — DIRECT_READ (Muse)
- Oct 8 (IN-WINDOW): Ultrafast for gpt-6.1-sol, Responses API, service_tier ultrafast, all users w/ rate limits, global + US/EU residency. (Sep 29 Astra Ultrafast lacks EU — disambiguated.)
- Oct 6 (IN-WINDOW): Decisions API beta, gpt-6-luna, v1/decisions, 10x vs Responses API (vendor claim, no methodology on page).
- Oct 6: usage tiers 5->3 (Build/Launch/Grow).

## A4. Math page https://openai.com/index/sharing-ai-progress-in-mathematics — DELEGATED
- Date Oct 6 2026. Internal frontier model (no name); GitHub openai/math repo + Lean partial formalizations + 10 reasoning summaries + compute in Pro-usage terms (~3h Pro thinking avg); IAS AGMAI advisory. No benchmarks/pricing/license on page.

## A5. Ironclad page https://openai.com/index/advancing-computer-use-with-ironclad — DELEGATED
- Date Oct 6 2026. 11 contracting tasks (legal/commercial/procurement), EDGAR-simulated (no customer/internal/nonpublic data), 8-50 criteria rubrics; Astra Max 55.0% vs Sol High 41.6% (+32% vendor), 37.0->19.2 min (-48% vendor, simulated); scope limited to 11 research tasks. Ironclad product launches NOT on page (separate vendor events).

## A6. GPT-6 page https://openai.com/index/gpt-6-for-everyone — DELEGATED
- Date Oct 7 2026. 44% = time-to-start for web-search questions (GPT-6 Instant vs 5.6 Instant), NOT wall-time. Rollout: Oct 7 Plus/Pro/Biz/Ent (Chat tab), Oct 8 Free/Go; Sol for paid tiers, Luna for Free/Go; Chat only.
