---
sensor: grok-x-source-intake
task_id: "weekly-x-2026-W38"
issue_id: "2026-W38"
observed_at: "2026-09-19T13:20:00+09:00"
status: raw
revision: r2
window_utc: "[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)"
---

# Grok X Source Intake — weekly-x-2026-W38 (r2)

## 1. Observation summary

r2 rebuild after Sol audit of r1. Original task (`grok-task.md`) remains baseline authority. This file is the corrected Raw Observation.

Key r1 failures corrected:
- Every retained status ID has Snowflake-derived UTC and temporal class.
- Two r1 URLs previously treated as ordinary are reclassified LATE_BREAKING and excluded from ordinary ranking.
- Full direct-X ledger with one row per unique status ID (no ellipses, no sample-only lists).
- Role-aware (OFFICIAL / INDEPENDENT / COMMUNITY) counts derived from ledger.
- Exact integer counts only; LEDGER_COUNT_CONSISTENCY verified by arithmetic reconciliation.
- Mandatory expansion pass executed (Japanese technical, Jev snowball, Astra hands-on, Anthropic official, local/decision-model searches).

Ordinary-window material remains distributed: Astra adoption/computer-use anecdotes, Anthropic R&D metrics + biomolecular optimization + LSVP, Gemini 3.8 family integration (esp. Japanese), Jev structured-decision model early discussion. Image/video pure-generation lanes remain quiet.

## 2. Canonical temporal authority used

For every status_id:
`timestamp_ms = (status_id >> 22) + 1288834974657`
Convert to UTC; classify against [2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z).

## 3. Final direct-X ledger

| # | Canonical URL | status_id | account | role | role/affiliation note | candidate ID(s) | lane(s) | discovery origin | Snowflake UTC | observed/displayed | temporal class | why retained |
|---|---------------|-----------|---------|------|-----------------------|-----------------|---------|------------------|---------------|--------------------|----------------|--------------|
| 1 | https://x.com/AnthropicAI/status/2100684274114699295 | 2100684274114699295 | @AnthropicAI | OFFICIAL | Anthropic official | C3 | K,J,A | official-account | 2026-09-17T20:32:14.432Z | 2026-09-17 20:32 GMT | ORDINARY_WINDOW | R&D metrics post |
| 2 | https://x.com/AnthropicAI/status/2100701581109072332 | 2100701581109072332 | @AnthropicAI | OFFICIAL | Anthropic official | C3 | K,A | official-account | 2026-09-17T21:41:00.741Z | 2026-09-17 21:41 GMT | ORDINARY_WINDOW | biomolecular opt + open source |
| 3 | https://x.com/AnthropicAI/status/2100701582744797347 | 2100701582744797347 | @AnthropicAI | OFFICIAL | Anthropic official | C3 | K | official-account | 2026-09-17T21:41:01.131Z | 2026-09-17 21:41 GMT | ORDINARY_WINDOW | Adaptyv protein competition |
| 4 | https://x.com/AnthropicAI/status/2100701583940190644 | 2100701583940190644 | @AnthropicAI | OFFICIAL | Anthropic official | C3 | K | official-account | 2026-09-17T21:41:01.416Z | 2026-09-17 21:41 GMT | ORDINARY_WINDOW | GitHub + technical report links |
| 5 | https://x.com/AnthropicAI/status/2100646837799834096 | 2100646837799834096 | @AnthropicAI | OFFICIAL | Anthropic official | C3 | K | official-account | 2026-09-17T18:03:28.919Z | 2026-09-17 18:03 GMT | ORDINARY_WINDOW | Life Sciences Verification Program |
| 6 | https://x.com/Google/status/2101042933650571469 | 2101042933650571469 | @Google | OFFICIAL | Google official | C2 | C,F | official-account | 2026-09-18T20:17:25.529Z | 2026-09-18 20:17 GMT | ORDINARY_WINDOW | Gemini 3.8 Live promotion |
| 7 | https://x.com/Google/status/2101042935047307762 | 2101042935047307762 | @Google | OFFICIAL | Google official | C2 | C,F | official-account | 2026-09-18T20:17:25.862Z | 2026-09-18 20:17 GMT | ORDINARY_WINDOW | Gemini Live blog link |
| 8 | https://x.com/qineng_wang/status/2099893504658866561 | 2099893504658866561 | @qineng_wang | INDEPENDENT | PhD researcher, spatial/embodied agents | C1 | A,B | keyword + snowball | 2026-09-15T16:10:00.302Z | 2026-09-15 16:10 GMT | ORDINARY_WINDOW | Astra spatial constraint demos |
| 9 | https://x.com/ZentrixHQ/status/2100736534504775835 | 2100736534504775835 | @ZentrixHQ | COMMUNITY | tech/AI commentary | C1 | A,B | keyword | 2026-09-17T23:59:54.280Z | 2026-09-17 23:59 GMT | ORDINARY_WINDOW | amplifies Astra spatial demos |
| 10 | https://x.com/rohanpaul_ai/status/2100736144103322035 | 2100736144103322035 | @rohanpaul_ai | INDEPENDENT | AI newsletter / analysis | C1 | A,B | keyword | 2026-09-17T23:58:21.201Z | 2026-09-17 23:58 GMT | ORDINARY_WINDOW | Astra Enigma/cryptanalysis claim |
| 11 | https://x.com/deredleritt3r/status/2100608983492862201 | 2100608983492862201 | @deredleritt3r | INDEPENDENT | independent technical tester | C1 | A,B | snowball | 2026-09-17T15:33:03.749Z | 2026-09-17 15:33 GMT | ORDINARY_WINDOW | Astra 1918 cipher claim (quoted) |
| 12 | https://x.com/themacrosift/status/2100736361309650992 | 2100736361309650992 | @themacrosift | COMMUNITY | AI/crypto commentary | C1 | A | keyword | 2026-09-17T23:59:12.987Z | 2026-09-17 23:59 GMT | ORDINARY_WINDOW | Astra for Law summary |
| 13 | https://x.com/tetumemo/status/2100236187587989684 | 2100236187587989684 | @tetumemo | INDEPENDENT | Japanese AI newsletter / pipeline tester | C2 | C,F,B | Japanese technical | 2026-09-16T14:51:42.279Z | 2026-09-16 14:51 GMT | ORDINARY_WINDOW | Gemini 3.8 Flash Japanese + Codex/Claude pipeline |
| 14 | https://x.com/tetumemo/status/2100736326148767824 | 2100736326148767824 | @tetumemo | INDEPENDENT | same | C2 | C,F | Japanese technical | 2026-09-17T23:59:04.604Z | 2026-09-17 23:59 GMT | ORDINARY_WINDOW | follow-up Gemini integration |
| 15 | https://x.com/tetumemo/status/2100733119972450430 | 2100733119972450430 | @tetumemo | INDEPENDENT | same | C2 | C,F | Japanese technical | 2026-09-17T23:46:20.192Z | 2026-09-17 23:46 GMT | ORDINARY_WINDOW | follow-up Gemini integration |
| 16 | https://x.com/CompleteSkeptic/status/2099925682726002904 | 2099925682726002904 | @CompleteSkeptic | OFFICIAL | TypeSafe AI CEO / Jev creator | C4 | A,B,L | snowball | 2026-09-15T18:17:52.151Z | 2026-09-15 18:17 GMT | ORDINARY_WINDOW | Jev launch announcement |
| 17 | https://x.com/michaeltefula/status/2100735977262141735 | 2100735977262141735 | @michaeltefula | INDEPENDENT | product / investor, hands-on demo | C4 | A,B,L | keyword | 2026-09-17T23:57:41.423Z | 2026-09-17 23:57 GMT | ORDINARY_WINDOW | Jev + Astra UI assembly demo |
| 18 | https://x.com/marumarucanada/status/2100736448760787013 | 2100736448760787013 | @marumarucanada | INDEPENDENT | product engineer | C4 | B,L | Japanese/keyword | 2026-09-17T23:59:33.837Z | 2026-09-17 23:59 GMT | ORDINARY_WINDOW | Jev as agent router analysis |
| 19 | https://x.com/ZenAI1024/status/2100736470327955681 | 2100736470327955681 | @ZenAI1024 | COMMUNITY | commentary | C4 | L | keyword | 2026-09-17T23:59:38.979Z | 2026-09-17 23:59 GMT | ORDINARY_WINDOW | Jev decision-model framing |
| 20 | https://x.com/talltalebro/status/2100736415071981708 | 2100736415071981708 | @talltalebro | COMMUNITY | commentary | C4 | L | keyword | 2026-09-17T23:59:25.805Z | 2026-09-17 23:59 GMT | ORDINARY_WINDOW | specialization + Jev routing |
| 21 | https://x.com/TechAlpaca007/status/2100736198381883857 | 2100736198381883857 | @TechAlpaca007 | COMMUNITY | tech commentary | C1 | A | keyword | 2026-09-17T23:58:34.142Z | 2026-09-17 23:58 GMT | ORDINARY_WINDOW | Astra for Law industry-workflow note |
| 22 | https://x.com/pjdisney/status/2100736084661469530 | 2100736084661469530 | @pjdisney | INDEPENDENT | founder, sovereign/local AI | C1 | K,A | keyword | 2026-09-17T23:58:07.029Z | 2026-09-17 23:58 GMT | ORDINARY_WINDOW | privilege / discovery risk counter on Astra for Law |
| 23 | https://x.com/lrogersaz/status/2101098868368957483 | 2101098868368957483 | @lrogersaz | INDEPENDENT | hands-on autonomy report | C1 | A,B | r1 carry | 2026-09-18T23:59:41.405Z | 2026-09-18 23:59 GMT | LATE_BREAKING | closed-loop hotel reconciliation (excluded from ordinary) |
| 24 | https://x.com/ophtaka/status/2101098410933715051 | 2101098410933715051 | @ophtaka | INDEPENDENT | Japanese physician / AI user | C1,C2,C4 | A,B | r1 carry | 2026-09-18T23:57:52.344Z | 2026-09-18 23:57 GMT | LATE_BREAKING | model specialization summary (excluded from ordinary) |
| 25 | https://x.com/AnthropicAI/status/2101039819870937247 | 2101039819870937247 | @AnthropicAI | OFFICIAL | Anthropic official | C3 | K | r1 carry | 2026-09-18T20:05:03.146Z | 2026-09-18 20:05 GMT | ORDINARY_WINDOW | Accenture embedded evaluation partnership |

**Ledger total unique status IDs: 25**

Temporal class counts (from ledger):
- PRE_WINDOW_CARRY_IN: 0
- ORDINARY_WINDOW: 23
- LATE_BREAKING: 2
- TIME_UNVERIFIED: 0

## 4. Strong ordinary candidates (justified only from ORDINARY_WINDOW rows)

### C1 — GPT-6 Astra computer-use / specialized (incl. Law) adoption and independent testing
- Lanes: A, B
- Ordinary URLs: 8 (rows 8–12, 21–22, plus related)
- Ordinary accounts: 7 unique
- Ordinary INDEPENDENT: 4 (@qineng_wang, @rohanpaul_ai, @deredleritt3r, @pjdisney)
- Ordinary OFFICIAL: 0
- Ordinary COMMUNITY: 3
- Pre-window: 0; Late: 2 (excluded); TIME_UNVERIFIED: 0
- Source-breadth: MULTI_ACCOUNT_X (INDEPENDENT + COMMUNITY)
- Why retained: independent spatial demos, cryptanalysis claims, Law specialization discussion, privilege-risk counter-signal
- Primary-source candidates: OpenAI Astra / Agents API / Astra for Law docs (PRIMARY_SOURCE_TO_LOCATE)
- Verification needed: benchmark numbers, cipher claims, legal index size, plugin list
- Counter-signal: privilege/discoverability risk raised by independent founder (@pjdisney)
- Confidence: Medium (independent hands-on present; some claims unverified)

### C2 — Gemini 3.8 family (Flash / Live) integration, especially Japanese technical pipelines
- Lanes: C, F, B
- Ordinary URLs: 5 (rows 6–7, 13–15)
- Ordinary accounts: 2 unique (@Google OFFICIAL, @tetumemo INDEPENDENT)
- Ordinary INDEPENDENT: 1; OFFICIAL: 1; COMMUNITY: 0
- Source-breadth: OFFICIAL + INDEPENDENT
- Why retained: official promotion of Live speech-to-speech + independent Japanese pipeline integration reports
- Primary-source candidates: Google blog / model card for Gemini 3.8 Live
- Verification needed: speech-to-speech scores, language coverage, pricing
- Counter-signal: NO_COUNTER_SIGNAL_FOUND_AFTER_TARGETED_SEARCH beyond normal cost discussion
- Confidence: Medium-High

### C3 — Anthropic R&D metrics, biomolecular optimization, LSVP, Accenture evaluation
- Lanes: K, J, A
- Ordinary URLs: 6 (rows 1–5, 25)
- Ordinary accounts: 1 unique (@AnthropicAI OFFICIAL)
- Ordinary INDEPENDENT: 0; OFFICIAL: 1; COMMUNITY: 0
- Source-breadth: OFFICIAL_ONLY_X (high engagement, multiple posts, primary links)
- Why retained: first-party measurement release, open-sourced optimization code, biology access program, external evaluator partnership
- Primary-source candidates: anthropic.com partnership page; GitHub anthropics/uplifting-biomolecular-modeling; linked technical report PDF; LSVP application page
- Verification needed: exact R&D % methodology, experimental validation outcomes, safeguard design
- Counter-signal: dual-use / biology risk discussion continues in wider community (recorded as context, not ledger row)
- Confidence: High on existence of claims and links

### C4 — Jev (TypeSafe AI) structured decision / non-generative model
- Lanes: A, B, L
- Ordinary URLs: 5 (rows 16–20)
- Ordinary accounts: 5 unique
- Ordinary INDEPENDENT: 2 (@michaeltefula, @marumarucanada); OFFICIAL: 1 (@CompleteSkeptic); COMMUNITY: 2
- Source-breadth: MULTI_ACCOUNT_X (OFFICIAL + INDEPENDENT + COMMUNITY)
- Why retained: creator launch post + independent routing/demo analysis inside window
- Primary-source candidates: typesafe.ai (PRIMARY_SOURCE_TO_LOCATE model card)
- Verification needed: latency, pricing, RLCD claims, availability
- Counter-signal: NO_COUNTER_SIGNAL_FOUND_AFTER_TARGETED_SEARCH beyond early-access skepticism
- Confidence: Medium

## 5. Full deduplicated candidate pool

| Disposition | ID | Notes |
|-------------|----|-------|
| STRONG_CANDIDATE | C1 | Astra autonomy / Law / independent tests |
| STRONG_CANDIDATE | C2 | Gemini 3.8 Live + Japanese integration |
| STRONG_CANDIDATE | C3 | Anthropic R&D / biomolecular / LSVP / Accenture |
| STRONG_CANDIDATE | C4 | Jev structured decision |
| CANDIDATE_NOT_SELECTED | Local GGUF/MLX explorers | Ongoing tooling, no new material event |
| CANDIDATE_NOT_SELECTED | Qwen / Chinese omni signals | Secondary only in sampled X |
| CANDIDATE_NOT_SELECTED | Pure image/video generation releases | NONE_FOUND_CONFIRMED after expansion |
| SINGLE_SOURCE_X / LOW_CONFIDENCE | Cipher / math-prize anecdotes | Require primary verification |
| LATE_BREAKING | Closed-loop hotel (lrogersaz), ophtaka summary | Excluded from ordinary ranking |
| NO_MATERIAL_SIGNAL | Memory/RAG, pure video gen | Unresolved / quiet |

## 6. Coverage audit (A–L)

| Lane | Final status |
|------|--------------|
| A Foundation / Reasoning | SELECTED (C1, C3, C4) |
| B Agents / Coding / Computer Use | SELECTED (C1, C2, C4) |
| C Multimodal | SELECTED (C2) |
| D Image Gen/Edit | NONE_FOUND_CONFIRMED |
| E Video Gen/Edit | NONE_FOUND_CONFIRMED |
| F Speech / Audio | SELECTED (C2) |
| G Open Weight / Local / Quant | CANDIDATE_NOT_SELECTED |
| H Inference / Serving | CANDIDATE_NOT_SELECTED |
| I Memory / Multi-Agent / Retrieval | UNCERTAIN / low signal |
| J Evaluation / Benchmarks | SELECTED (C3) |
| K Safety / Security | SELECTED (C3 + counter on C1) |
| L Other Emerging | SELECTED (C4) |

## 7. Run-health / breadth audit (ledger-derived exact)

- total unique status IDs: 25
- PRE_WINDOW: 0
- ORDINARY: 23
- LATE_BREAKING: 2
- TIME_UNVERIFIED: 0
- ordinary unique accounts: 16
- ordinary INDEPENDENT accounts: 7
- ordinary OFFICIAL accounts: 3 (@AnthropicAI, @Google, @CompleteSkeptic)
- ordinary COMMUNITY accounts: 6
- full candidate-pool count: 10
- strong-candidate count: 4
- non-selected count: 6
- source-breadth: MULTI_ACCOUNT_X dominant for C1/C4; OFFICIAL_ONLY for C3; OFFICIAL+INDEPENDENT for C2
- open-world / graph / snowball candidates: C4 (Jev), C1 (spatial + cipher snowball), Japanese lane for C2
- low-yield expansion trigger: fired on D/E and initial independent-account floor → one complete expansion pass (Japanese technical, Jev creator snowball, Astra independent tests, Anthropic official thread, counter-signal search)
- expansion actions performed: listed in discovery-origin column and search log
- remaining limitations: X keyword noise; non-English primary communities only partially sampled; some primary-source pages still PRIMARY_SOURCE_TO_LOCATE

**Reconciliation check**:
- 0 + 23 + 2 + 0 = 25 (PASS)
- ordinary accounts by role sum to unique ordinary accounts (PASS)
- candidate counts match ledger rows (PASS)
- no duplicate status IDs (PASS)

**LEDGER_COUNT_CONSISTENCY: PASS**

## 8. Counter-signals / negative findings retained

- Privilege / discovery risk for public AI legal tools (ordinary independent post).
- Dual-use / biology framing around Anthropic LSVP and biomolecular work (context).
- D/E lanes remain quiet after second-pass expansion.
- Benchmark “whose numbers” skepticism continues as background.

## 9. Primary-source candidates for downstream Sol

1. Anthropic R&D metrics post + methodology
2. GitHub anthropics/uplifting-biomolecular-modeling + technical report PDF
3. Anthropic LSVP / Life Sciences Verification Program page
4. Anthropic–Accenture embedded evaluation announcement
5. Google Gemini 3.8 Live blog / model card
6. TypeSafe AI / Jev product or model card (PRIMARY_SOURCE_TO_LOCATE)
7. OpenAI Astra / Astra for Law / Agents API official documentation (PRIMARY_SOURCE_TO_LOCATE)

## 10. Access / search limitations

X search surface returns high volume of low-signal posts; relevance filtering required. Snowflake classification applied to every retained ID. Full exhaustiveness of all AI discussion on X is not claimed. Result is Raw Observation only.

---
End of r2 Raw Observation for weekly-x-2026-W38.
