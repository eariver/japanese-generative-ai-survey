---
sensor: grok-x-source-intake
task_id: "weekly-x-2026-W36"
issue_id: "2026-W36"
revision: "r4"
observed_at: "2026-09-16T14:51:00+00:00"
status: raw
supersedes: "grok-x-result-r3.md"
augmentation_scope: "ordinary-independent-signal"
---

# Observation Summary

r4 is a targeted augmentation of r3 focused solely on recovering additional ordinary-window independent / non-official X posts to strengthen community-momentum substantiation. r3 remains the canonical base; no existing r3 URLs, timestamps, window classifications, candidate dispositions, or lane statuses were altered.

Canonical ordinary window (end-exclusive):
- UTC: [2026-08-28T22:00:00Z, 2026-09-04T22:00:00Z)

Only posts with exact recoverable canonical URLs, independent account_type, and posted_at inside the ordinary window were added. Targeted searches prioritized hands-on testing, coding/agent/computer-use reports, local/quantization feasibility, comparisons, and technical constraints across Priority-1 candidates (Astra, Fable/Mythos, Fermat, GLM-5.3, Gemini 3.x, Muse Spark) and Priority-2 themes.

augmentation_result: LIMITED_RECOVERY (7 new ordinary independent URLs recovered from 7 distinct independent accounts).

# Findings by Research Question / Coverage Focus

(r3 substance retained.) Material generative-AI community momentum inside the ordinary window centered on OpenAI GPT-6 Astra, Anthropic Fermat formalization, NVIDIA–Hugging Face acquisition, and supporting ranking/discussion of Fable 5.1, Gemini 3.x Flash, GLM-5.3, and Muse Spark 1.3. r4 adds concrete independent hands-on and comparison signals for computer-use expectations, cost/quality trade-offs, local multi-agent workflows, and Muse Spark coding quality.

All capability, pricing, benchmark, and architecture claims remain X-observed only.

# Representative X Posts (URL-recovered only)

## Existing r3 posts (unchanged)

### POST-001 (ORDINARY_WINDOW, OFFICIAL)
- post_id: 2095595741528125780
- url: https://x.com/OpenAI/status/2095595741528125780
- author: OpenAI (@OpenAI)
- account_type: OFFICIAL
- posted_at: 2026-09-03T19:32:13Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: A, B, K
- candidate_id: CAND-ASTRA
- observation: Official announcement of GPT-6 Astra with computer-use emphasis (“Anything you can do on a computer, Astra can do for you. Fast.”). Follow-on thread posts claim SOTA on multiple agent/computer and science benchmarks and limited rollout beginning that day.
- why_it_matters: Primary official launch surface for the highest-salience frontier model of the window; anchors subsequent independent testing.
- engagement_snapshot: ~339k likes, ~35k reposts, ~137M views (observed at fetch)
- primary_source_candidate: https://openai.com/index/gpt-6-astra/ (linked in thread)
- verification_needed: Exact access tiers, preparedness classification language, benchmark definitions and scores, computer-use tool behavior.

### POST-002 (ORDINARY_WINDOW, OFFICIAL)
- post_id: 2095947707605266436
- url: https://x.com/AnthropicAI/status/2095947707605266436
- author: Anthropic (@AnthropicAI)
- account_type: OFFICIAL
- posted_at: 2026-09-04T18:50:48Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: A, B, I, K
- candidate_id: CAND-FERMAT
- observation: Official claim that Claude completed the first formalized proof of Fermat’s Last Theorem in Lean (largest Lean proof, >13M lines, >29k intermediate theorems, largely autonomous multi-agent work over ~11 days). Links to Science Blog and GitHub.
- why_it_matters: Highest-profile formal-verification / multi-agent result of the window; direct primary announcement.
- engagement_snapshot: ~14.1k likes, ~1.9k reposts, ~4.7M views
- primary_source_candidate: Anthropic Science Blog + GitHub repo linked in post
- verification_needed: Autonomy degree, exact process, repo contents, intermediate theorem claims, cost estimates circulating elsewhere.

### POST-003 (ORDINARY_WINDOW, OFFICIAL)
- post_id: 2095482998674112733
- url: https://x.com/ClementDelangue/status/2095482998674112733
- author: clem 🤗 (@ClementDelangue)
- account_type: OFFICIAL
- posted_at: 2026-09-03T12:04:13Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: G, H, L
- candidate_id: CAND-HF-NVIDIA
- observation: HF CEO announces intention to join forces with NVIDIA in a $12,930,300,000 acquisition; platform to remain open, independent, compute-agnostic; founders and team staying.
- why_it_matters: Primary ecosystem / infrastructure event for open-weight distribution and tooling.
- engagement_snapshot: ~13.4k likes, ~1.2k reposts, ~1.5M views
- primary_source_candidate: Official HF / NVIDIA statements and any SEC or press releases
- verification_needed: Deal structure, valuation confirmation, continuity guarantees, regulatory status.

### POST-004 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095360980851347559
- url: https://x.com/forloopcodes/status/2095360980851347559
- author: forloop (@forloopcodes)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T03:59:22Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: A, G
- candidate_id: CAND-ASTRA, CAND-FABLE, CAND-MUSE, CAND-GEMINI, CAND-GLM
- observation: Community synthesis listing recent and expected releases including Qwen3.8-Max, Meta Muse Spark 1.3, Gemini 3.8 Flash/Cyber, MiniMax H3 Max, Claude Fable 5.1, Claude Mythos 5.1, and expected Astra.
- why_it_matters: Independent ranking/calendar signal showing perceived density of frontier drops inside the window.
- engagement_snapshot: ~1.3k likes, 67 reposts, ~79k views
- primary_source_candidate: None (synthesis)
- verification_needed: Accuracy of listed model identifiers and release status.

### POST-005 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095591376058744864
- url: https://x.com/forloopcodes/status/2095591376058744864
- author: forloop (@forloopcodes)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T19:14:52Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: A
- candidate_id: CAND-ASTRA
- observation: Updated ranking post declaring “ASTRA ENDED THE BATTLE” and marking prior models as mogged after Astra appearance.
- why_it_matters: Rapid independent community ranking reaction within hours of official Astra post.
- engagement_snapshot: ~235 likes, ~20k views
- primary_source_candidate: None
- verification_needed: None beyond X observation itself.

### POST-006 (LATE_BREAKING, INDEPENDENT)
- post_id: 2096025503329091995
- url: https://x.com/DavidOndrej1/status/2096025503329091995
- author: David Ondrej (@DavidOndrej1)
- account_type: INDEPENDENT
- posted_at: 2026-09-04T23:59:56Z
- window_class: LATE_BREAKING
- coverage_lanes: A
- candidate_id: CAND-ASTRA, CAND-FABLE
- observation: “Fable feels like a total moron after using Astra”
- why_it_matters: High-engagement independent comparison; correctly excluded from ordinary accounting because posted after cutoff.
- engagement_snapshot: ~720 likes, ~37k views
- primary_source_candidate: None
- verification_needed: None (subjective ranking).

### POST-007 (LATE_BREAKING, INDEPENDENT)
- post_id: 2096025501886214553
- url: https://x.com/dui_toledo/status/2096025501886214553
- author: Dui Toledo (@dui_toledo)
- account_type: INDEPENDENT
- posted_at: 2026-09-04T23:59:56Z
- window_class: LATE_BREAKING
- coverage_lanes: B, K
- candidate_id: CAND-ASTRA
- observation: Report that Astra supplied exploits for 7 of 9 findings, built an RCE for one, and reclassified severity; intention to use as security reviewer.
- why_it_matters: Concrete independent cyber-capability testing claim; post-cutoff so LATE_BREAKING only.
- engagement_snapshot: low single-digit engagement at fetch
- primary_source_candidate: None
- verification_needed: Exploit claims, success rates, classification details (must not be accepted from X alone).

### POST-008 (LATE_BREAKING, OFFICIAL)
- post_id: 2096024903027974535
- url: https://x.com/neondatabase/status/2096024903027974535
- author: Neon (@neondatabase)
- account_type: OFFICIAL
- posted_at: 2026-09-04T23:57:33Z
- window_class: LATE_BREAKING
- coverage_lanes: H
- candidate_id: CAND-SERVING
- observation: Neon AI Gateway now lists Fable 5.1, GLM 5.3 Flash, Grok 4.6, and notes OpenAI GPT-6 Astra landing soon.
- why_it_matters: Serving/gateway integration signal for multiple window models; post-cutoff.
- engagement_snapshot: ~54 likes, ~5.5k views
- primary_source_candidate: Neon product documentation
- verification_needed: Actual availability dates and model identifiers.

## New ordinary independent posts recovered in r4

### POST-009 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095662839893827837
- url: https://x.com/OooCoder/status/2095662839893827837
- author: OooCoder | AI Builder (@OooCoder)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T23:58:51Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: B
- candidate_id: CAND-ASTRA
- observation: Independent commentary on Astra computer-use potential for enterprise long-tail scenarios (legacy systems, desktop software, incomplete APIs, cross-system workflows); notes structured interfaces remain preferred where available.
- why_it_matters: Early independent technical framing of computer-use value beyond demo cases.
- engagement_snapshot: low engagement at fetch
- primary_source_candidate: None
- verification_needed: None (opinion).

### POST-010 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095661656064004390
- url: https://x.com/vansh22b/status/2095661656064004390
- author: Vansh (@vansh22b)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T23:54:08Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: A, B
- candidate_id: CAND-ASTRA, CAND-FABLE
- observation: Subjective comparison: Grok 4.6 preferred for most work under Cursor Pro+; Astra better when heavy computer-use is needed; Fable 5.1 better for frontend coding; notes high cost of Astra/Fable relative to hiring.
- why_it_matters: Independent multi-model practical ranking including cost constraint.
- engagement_snapshot: 18 likes, 422 views
- primary_source_candidate: None
- verification_needed: None (subjective).

### POST-011 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095649747667440027
- url: https://x.com/bchap1n/status/2095649747667440027
- author: brrrock (@bchap1n)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T23:06:49Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: A, B
- candidate_id: CAND-MUSE
- observation: Hands-on positive report on Muse Spark 1.3 for Python audio DSP coding; notes 1.2 coding quality was weaker while 1.3 is “absolute beast” and fast.
- why_it_matters: Concrete independent coding-task feedback for Muse Spark.
- engagement_snapshot: 1 like, 70 views
- primary_source_candidate: None
- verification_needed: None (hands-on anecdote).

### POST-012 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095644046945390625
- url: https://x.com/atillayurtseven/status/2095644046945390625
- author: Atilla Yurtseven (@atillayurtseven)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T22:44:10Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: A, B
- candidate_id: CAND-FABLE, CAND-GEMINI
- observation: Real-project sequential testing: Claude Fable 5.1 Ultracode, Codex 5.6 Ultra, and Gemini 3.8 Flash all failed the same task; preparing Grok and local Qwen next. Emphasizes real-life project rather than synthetic benchmark.
- why_it_matters: Independent failed-reproduction / multi-model stress test signal.
- engagement_snapshot: 4 likes, ~8k views
- primary_source_candidate: None
- verification_needed: Task details not public; treat as anecdotal.

### POST-013 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095656804449763817
- url: https://x.com/Tono_Ken3/status/2095656804449763817
- author: となりのトトノ🏯Local LLM | Tonoken3 (@Tono_Ken3)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T23:34:52Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: G, B
- candidate_id: CAND-GLM, CAND-LOCAL
- observation: Discussion of multi-agent local workflow using Fable as planner and multiple GLM-5.3 / Flash instances as workers; estimates gross 3000–5000 TPS possible.
- why_it_matters: Independent local multi-agent / throughput feasibility signal for GLM-5.3.
- engagement_snapshot: 12 likes, 1.7k views
- primary_source_candidate: None
- verification_needed: Throughput numbers and exact configuration are claims only.

### POST-014 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095641040015565024
- url: https://x.com/pxlboy/status/2095641040015565024
- author: Zach (@pxlboy)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T22:32:13Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: B
- candidate_id: CAND-ASTRA, CAND-FABLE
- observation: Interest in Astra computer-use for Mac-app agent testing environments; prior experience with Sol was flaky and Fable “hijacked my mouse using AppleScript or something.”
- why_it_matters: Independent computer-use testing intent + prior regression/constraint report on Fable.
- engagement_snapshot: low engagement
- primary_source_candidate: None
- verification_needed: None (anecdotal).

### POST-015 (ORDINARY_WINDOW, INDEPENDENT)
- post_id: 2095662045169672685
- url: https://x.com/uuzzrm/status/2095662045169672685
- author: Raymond Zhao (@uuzzrm)
- account_type: INDEPENDENT
- posted_at: 2026-09-03T23:55:41Z
- window_class: ORDINARY_WINDOW
- coverage_lanes: B
- candidate_id: CAND-MUSE
- observation: Notes Meta-reported ~20% fewer tool calls and ~25% fewer tokens for Muse Spark 1.3 vs 1.2 in coding comparisons; highlights clarification-before-action as agent quality signal.
- why_it_matters: Independent citation of efficiency and agent-behavior claims for Muse Spark.
- engagement_snapshot: low engagement
- primary_source_candidate: Meta release notes (claimed)
- verification_needed: Exact Meta-reported deltas must be confirmed from primary source.

# Canonical X Post Ledger

| post_id | canonical_url | author | account_type | posted_at_utc | window_class | lane(s) | candidate_id | disposition |
|---------|---------------|--------|--------------|---------------|--------------|---------|--------------|-------------|
| 2095595741528125780 | https://x.com/OpenAI/status/2095595741528125780 | @OpenAI | OFFICIAL | 2026-09-03T19:32:13Z | ORDINARY_WINDOW | A,B,K | CAND-ASTRA | RETAINED_SIGNAL |
| 2095947707605266436 | https://x.com/AnthropicAI/status/2095947707605266436 | @AnthropicAI | OFFICIAL | 2026-09-04T18:50:48Z | ORDINARY_WINDOW | A,B,I,K | CAND-FERMAT | RETAINED_SIGNAL |
| 2095482998674112733 | https://x.com/ClementDelangue/status/2095482998674112733 | @ClementDelangue | OFFICIAL | 2026-09-03T12:04:13Z | ORDINARY_WINDOW | G,H,L | CAND-HF-NVIDIA | RETAINED_SIGNAL |
| 2095360980851347559 | https://x.com/forloopcodes/status/2095360980851347559 | @forloopcodes | INDEPENDENT | 2026-09-03T03:59:22Z | ORDINARY_WINDOW | A,G | CAND-ASTRA,CAND-FABLE,CAND-MUSE,CAND-GEMINI,CAND-GLM | RETAINED_SIGNAL |
| 2095591376058744864 | https://x.com/forloopcodes/status/2095591376058744864 | @forloopcodes | INDEPENDENT | 2026-09-03T19:14:52Z | ORDINARY_WINDOW | A | CAND-ASTRA | RETAINED_SIGNAL |
| 2096025503329091995 | https://x.com/DavidOndrej1/status/2096025503329091995 | @DavidOndrej1 | INDEPENDENT | 2026-09-04T23:59:56Z | LATE_BREAKING | A | CAND-ASTRA,CAND-FABLE | LATE_BREAKING |
| 2096025501886214553 | https://x.com/dui_toledo/status/2096025501886214553 | @dui_toledo | INDEPENDENT | 2026-09-04T23:59:56Z | LATE_BREAKING | B,K | CAND-ASTRA | LATE_BREAKING |
| 2096024903027974535 | https://x.com/neondatabase/status/2096024903027974535 | @neondatabase | OFFICIAL | 2026-09-04T23:57:33Z | LATE_BREAKING | H | CAND-SERVING | LATE_BREAKING |
| 2095662839893827837 | https://x.com/OooCoder/status/2095662839893827837 | @OooCoder | INDEPENDENT | 2026-09-03T23:58:51Z | ORDINARY_WINDOW | B | CAND-ASTRA | RETAINED_SIGNAL |
| 2095661656064004390 | https://x.com/vansh22b/status/2095661656064004390 | @vansh22b | INDEPENDENT | 2026-09-03T23:54:08Z | ORDINARY_WINDOW | A,B | CAND-ASTRA,CAND-FABLE | RETAINED_SIGNAL |
| 2095649747667440027 | https://x.com/bchap1n/status/2095649747667440027 | @bchap1n | INDEPENDENT | 2026-09-03T23:06:49Z | ORDINARY_WINDOW | A,B | CAND-MUSE | RETAINED_SIGNAL |
| 2095644046945390625 | https://x.com/atillayurtseven/status/2095644046945390625 | @atillayurtseven | INDEPENDENT | 2026-09-03T22:44:10Z | ORDINARY_WINDOW | A,B | CAND-FABLE,CAND-GEMINI | RETAINED_SIGNAL |
| 2095656804449763817 | https://x.com/Tono_Ken3/status/2095656804449763817 | @Tono_Ken3 | INDEPENDENT | 2026-09-03T23:34:52Z | ORDINARY_WINDOW | G,B | CAND-GLM,CAND-LOCAL | RETAINED_SIGNAL |
| 2095641040015565024 | https://x.com/pxlboy/status/2095641040015565024 | @pxlboy | INDEPENDENT | 2026-09-03T22:32:13Z | ORDINARY_WINDOW | B | CAND-ASTRA,CAND-FABLE | RETAINED_SIGNAL |
| 2095662045169672685 | https://x.com/uuzzrm/status/2095662045169672685 | @uuzzrm | INDEPENDENT | 2026-09-03T23:55:41Z | ORDINARY_WINDOW | B | CAND-MUSE | RETAINED_SIGNAL |

# Deduplicated Candidate Ledger

(r3 dispositions retained; only X signal assessment updated where new ordinary independent posts strengthen observation.)

| candidate_id | candidate | lane(s) | underlying_event_date | ordinary X URLs | late X URLs | primary-source candidate | X signal assessment | final disposition |
|--------------|-----------|---------|-----------------------|-----------------|-------------|---------------------------|---------------------|-------------------|
| CAND-ASTRA | GPT-6 Astra (OpenAI) | A, B, K | ~2026-09-03 | 6 (1 official + 5 independent) | 2 | openai.com/index/gpt-6-astra/ + system/model cards | Strong official launch + ranking + independent computer-use framing, cost/quality comparisons, and testing intent | SELECTED |
| CAND-FERMAT | Anthropic Fermat / Lean formalization | A, B, I, K | ~2026-09-04 (announced; work claimed prior) | 1 (AnthropicAI official) | 0 | Anthropic Science Blog + GitHub | High-engagement official primary announcement of large-scale formalization | SELECTED |
| CAND-HF-NVIDIA | NVIDIA / Hugging Face acquisition | G, H, L | 2026-09-03 | 1 (ClementDelangue) | 0 | HF / NVIDIA official statements | Clear official CEO announcement with continuity language | SELECTED |
| CAND-FABLE | Claude Fable 5.1 / Mythos 5.1 | A | ~2026-09-01–02 (community) | 3 (ranking + comparisons + local workflow) | 1 | Anthropic release / model cards | Ranking + independent multi-model comparisons and prior computer-use friction reports; still no recovered ordinary official launch post | CANDIDATE_NOT_SELECTED |
| CAND-GEMINI | Gemini 3.x Flash / Omni related | A, C | Aug–early Sep 2026 | 2 (ranking + failed real-project test) | 0 | Google DeepMind / Google AI posts | Ranking + independent real-project failure report; still limited high-signal volume | CANDIDATE_NOT_SELECTED |
| CAND-GLM | GLM-5.3 / Flash / local inference | A, G | ~2026-08-28 onward | 2 (ranking + local multi-agent) | 0 | Z.ai / Hugging Face weights + license | Ranking + independent local multi-agent / TPS discussion | CANDIDATE_NOT_SELECTED |
| CAND-MUSE | Meta Muse Spark 1.3 | A | early Sep 2026 | 3 (ranking + 2 hands-on) | 0 | Meta release notes | Ranking + independent coding quality and efficiency/agent-behavior reports | CANDIDATE_NOT_SELECTED |
| CAND-SOLARIS | Runway Solaris | E | ~2026-08-31 (digest) | 0 | 0 | Runway official materials | Secondary digests only; no recoverable primary X post in ordinary window after second pass | UNCERTAIN |
| CAND-SERVING | Gateway / serving additions (Neon etc.) | H | 2026-09-04 | 0 | 1 | Neon / provider docs | Post-cutoff integration note | CANDIDATE_NOT_SELECTED |
| CAND-SAFETY | Safety / cyber observations | K | concurrent with Astra / Fermat | (covered under ASTRA/FERMAT) | (covered) | Preparedness docs, formalization repo | Co-occurring with selected candidates (via ASTRA/FERMAT) | SELECTED |
| CAND-LOCAL | Local / quantization observations | G | concurrent | 1 (GLM multi-agent) | 0 | Model cards / GGUF repos | Strengthened by independent local multi-agent report | CANDIDATE_NOT_SELECTED |

# Coverage Audit (final status)

(r3 statuses retained; no lane status changed by the limited independent augmentation.)

| Lane | Status | Notes |
|------|--------|-------|
| A. Foundation Models / Reasoning | SELECTED | Astra (official + ranking + independent comparisons), Fermat, HF acquisition context; Fable/Gemini/GLM/Muse ranking + limited independent testing |
| B. Agents / Coding / Harness / Computer Use | SELECTED | Astra computer-use official claim + independent framing/testing intent; Fermat multi-agent claim; Muse/Fable coding reports |
| C. Multimodal Foundation Models | CANDIDATE_NOT_SELECTED | Ranking mentions only; second pass performed, no dominant ordinary primary post recovered |
| D. Image Generation / Editing | NONE_FOUND_CONFIRMED | Quiet; second pass performed |
| E. Video Generation / Editing | UNCERTAIN | Solaris secondary only; targeted second pass performed, no recoverable ordinary primary URL |
| F. Speech / Audio / Music Generation | NONE_FOUND_CONFIRMED | Quiet; second pass performed |
| G. Open Weight / Local AI / Quantization | SELECTED | HF acquisition official; GLM/Muse ranking + independent local multi-agent discussion |
| H. Inference / Serving / Systems | CANDIDATE_NOT_SELECTED | Neon post is LATE_BREAKING only |
| I. Memory / Multi-Agent / Retrieval | CANDIDATE_NOT_SELECTED | Covered under Fermat multi-agent claim; no separate high-signal ordinary post |
| J. Evaluation / Benchmarks | CANDIDATE_NOT_SELECTED | Claims appear inside Astra/Fermat official threads; no independent benchmark release post recovered |
| K. Safety / Security | SELECTED | Computer-use + formal verification + cyber framing inside selected official posts |
| L. Other Emerging Generative AI Technology | SELECTED | NVIDIA–Hugging Face acquisition |

# Late Breaking

(Unchanged from r3.)

Three recovered posts fall after 2026-09-04T22:00:00Z and are excluded from ordinary accounting:

- https://x.com/DavidOndrej1/status/2096025503329091995 (Astra vs Fable subjective ranking)
- https://x.com/dui_toledo/status/2096025501886214553 (Astra security/exploit testing claim)
- https://x.com/neondatabase/status/2096024903027974535 (Neon gateway model list including window models)

These may be useful context for downstream review of post-cutoff momentum on ordinary-window events, but they do not count toward ordinary-window signal.

# Independent Source Diversity Audit

| account | ordinary URLs contributed | candidate(s) | signal type |
|---------|---------------------------|--------------|-------------|
| @forloopcodes | 2 | ASTRA, FABLE, MUSE, GEMINI, GLM | ranking / calendar synthesis |
| @OooCoder | 1 | ASTRA | computer-use enterprise framing |
| @vansh22b | 1 | ASTRA, FABLE | multi-model practical comparison + cost |
| @bchap1n | 1 | MUSE | hands-on coding quality |
| @atillayurtseven | 1 | FABLE, GEMINI | real-project multi-model failure |
| @Tono_Ken3 | 1 | GLM, LOCAL | local multi-agent / TPS |
| @pxlboy | 1 | ASTRA, FABLE | computer-use testing intent + prior friction |
| @uuzzrm | 1 | MUSE | agent efficiency / clarification behavior |

Distinct ordinary independent accounts: 8  
No single account dominates the new augmentation set.

# Canonical Accounting (from ledger)

unique X URLs: 15  
ORDINARY_WINDOW: 12  
BACKGROUND_ONLY: 0  
LATE_BREAKING: 3  

ordinary official-account posts: 3  
ordinary independent/non-official posts: 9  

distinct ordinary independent accounts: 8  
new ordinary independent URLs added in r4: 7  

URL_UNRECOVERED observations: (unchanged from r3) multiple aggregate or low-specificity statements from earlier revisions remain outside canonical counts.

# Primary-Source Boundary

(Unchanged.) No X claim of parameter counts, benchmark scores, acquisition valuation, autonomy degree, exploit success rates, access tiers, license terms, training compute, or architecture is treated as verified technical fact. Downstream must obtain primary documents.

# Unresolved / Access Limitations

(Unchanged.) Several earlier aggregate observations remain URL_UNRECOVERED. Runway Solaris and pure image/speech lanes produced no recoverable ordinary primary posts after targeted second passes. X search surfaces are incomplete. All technical claims remain Raw Observation.
