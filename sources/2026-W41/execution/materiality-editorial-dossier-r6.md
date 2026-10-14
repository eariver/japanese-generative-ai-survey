# W41 Materiality / Completeness editorial dossier r6 (SC-M41-03/04, Sol-facing)

Status: `EDITION_LOCAL / EDITORIAL / NON_SCHEMA / SELECTION_INPUT`
Date: 2026-10-12 JST
Basis:
- Evidence acceptance `717ea04a51bda4ab8b1d652d9ca92122e6f67431815c5bd910de15e2bad522db` (36 cards: 3 VERIFIED / 21 PARTIAL / 12 NEEDS_MORE) — immutable.
- Edition Views acceptance `cd661097ccfb2c4e3960a334d2aab39b629fc656436593186011fe416f0a04b2` (36 views: 20 MATERIAL / 13 HOLD / 3 CONTEXT) — r6 reaccepted, Grok ledger corrected MATERIAL→CONTEXT.
- Materiality ledger `execution/materiality-ledger-r6.PROPOSED.json` SHA `51890f067daf8d5f850a3166204d0a7bc6e4073ab11d1842f241155aee9f2997` (37 rows: 20 MATERIAL / 13 HOLD / 3 CONTEXT / 1 EXCLUDED).
- Completeness `execution/profile-completeness-r6.PROPOSED.json` SHA `f3d5a122534b74409bce69f3eaec03f51e23e299e610721ac0b80e6d3d4508d8` (overall LIMITED).
- Exclusion overlay: `execution/nanobanana-legacy-negative-exclusion-r6.md` (`LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE`).

This dossier is NOT a Core schema. Core's ledger rationale (`Screening=KEEP; Edition View=MATERIAL`)
is structural coverage only. What follows is independent editorial judgment:
what each of the 20 genuine technology MATERIAL candidates actually proves,
what is vendor-stated only, how thin each would be standalone, and how they
should be grouped into a full Weekly issue without inflating the Grok
provenance ledger into an article.

Grok weekly X ledger `w41-grok-x-ledger-20261011` (`evidence:2026-W41:d3b121be6163f0ef`,
PARTIAL, View CONTEXT, window OTHER) is a research-provenance source only.
It binds 14 X posts (12 in-window / 2 post-cutoff) and DailyX crosswalk
provenance. It is never an article candidate and contributes zero article count.

## 0. Source-intake and provenance coverage (carried, truthful)

- 7 DailyX originals / 92 topics consumed (16/49/3/14/2/8 crosswalk preserved
  from r2c/r2d). No 09:00 independent DailyX runs exist for any of the 7 dates;
  exhaustiveness is not claimed.
- Weekly Grok: 14 posts, 12 in-window / 2 post-cutoff (Clef-omni X 23:11Z is
  post-cutoff and is NOT the event clock; the event clock is the blog JSON-LD
  18:27:34Z). X post existence/authorship unverified beyond Snowflake
  format-only; Drive text is not X HTML capture.
- Unconsumed / gated: textGrain tech-report PDF binary-unparsed (method
  second-hand); StepFun official page JS-gated; synthid.com portal JS-shell;
  EmbeddingGemma model-card fetch timeout (blog only); NDI 1.0 version label
  and ElevenLabs WG docs not found; MS-Decision-1 day-only (no clock);
  Tencent month-only ([2026-10] bullets, no day upload date).
- Model-weight license uncertainty: Clef-omni (blog says HF open weights,
  SPDX/download unverified), Liquid d1 (HF stated, SPDX absent), Kolibri
  (HF + Apache-2.0 vendor-stated, download VERIFIED as stated-location only),
  EmbeddingGemma 2 (Apache-2.0 + HF/Kaggle vendor-stated, card unfetched),
  Reflection Beam (Apache-2.0 intent, weights later this month, not
  downloadable), Mistral Large 4 (weights end of month, not downloadable),
  Perplexity decider/embed (HF stated in forum, repo paths/specs/license
  absent). Publisher "open weights" claims are distinct from downloaded bytes.
- Cutoff sensitivity: Clef-omni IN-WINDOW pinned by JSON-LD 18:27:34Z
  (< 22:00Z Oct 9 cutoff); MS-Decision-1 and unintended-actions day-only
  → HOLD (cutoff unprovable); Tencent month-only → HOLD.
- Vendor-only metrics throughout: no benchmark independently reproduced.
  Every vendor number below must be attributed as publisher-measured.
- W40 four carryover HOLDs (AstaBrief, AutoSynthData, PixelCanary, TBCVideo)
  rechecked, no W41 new dated evidence → HOLD retained. ELYZA pre-window
  (`w41-weak-elyza-rsi-20261002`) is CONTEXT, not newness.
- 8 supplements are BUNDLE_WINDOW_ESTIMATE / PER_PAGE_UNKNOWN and
  BOUNDED_EXCERPT, per `w41-supplement-access-provenance-r5.md`. Delegated
  reads are verbatim excerpts pending Sol direct re-verification; no
  byte-identical HTML captures.

## 1. Theme A — Frontier flagships (5 candidates)

### A1. GPT-6 + Intelligent UI rollout — `w41-primary-gpt6-intelligent-ui-20261007`
- Evidence `evidence:2026-W41:5ca8cd2c65ec98d8` (PARTIAL, task-e82f6c680a8d3099cabd).
  Sources: PRIMARY_OFFICIAL `openai.com/index/gpt-6-for-everyone` (delegated read).
  Claims: rollout Oct 7 paid (Plus/Pro/Business/Enterprise, Chat tab) / Oct 8
  Free-Go; Sol for paid, Luna for Free-Go (VENDOR_CLAIM); 44% sooner answering
  is time-to-start via interleaved thinking/answering, not wall-time
  (VENDOR_CLAIM, distinction VERIFIED on page).
- Verified vs vendor: tier/date/tab mapping VERIFIED as vendor-stated on page;
  44% figure is vendor-measured time-to-start; no wall-time reduction number;
  system-card numbers not enumerated; pricing absent.
- Mechanism actually read: Intelligent UI Chat-tab rollout + model-tier mapping
  (Sol/Luna); latency claim is start-latency, not final-answer latency.
- Japanese relevance: highest. ChatGPT tier rollout timing directly affects JP
  Plus/Free users; Sol/Luna naming matters for JP product coverage.
- Links: pairs with A2 (Haiku pricing), A5 (Ultrafast latency), C1/C2 (Decisions
  API + Ultrafast Sol infra).
- Proposed role: LEAD candidate (issue cover). Minimum to explain without
  inflation: tier/date/tab table + Sol/Luna mapping + 44%-is-start-latency
  caveat + "system-card details not on page" boundary. Do not claim wall-time
  speedup or benchmark leadership.

### A2. Claude Haiku 5.5 — `w41-primary-haiku55-20261007`
- Evidence `evidence:2026-W41:c880db78235eeef3` (PARTIAL, task-4690400bcb127ce71b7e).
  Sources: PRIMARY_OFFICIAL `anthropic.com/claude-haiku-5-5` (delegated).
  Claims: split ≤/>100k pricing, cache-read $0.01/$0.05; Sonnet 5.5 cache-read
  halved $0.20→$0.10 (VERIFIED as vendor-stated); vendor bench table
  (GDPval 1620, OSWorld 72.4%, HLE 45.9/57.4, TB4 39.2%) publisher-measured.
- Verified vs vendor: pricing split VERIFIED as stated; all benchmarks
  vendor-only, independent reproduction explicitly pending.
- Mechanism: price-tier split + cache-read economics; no architecture detail
  on page; system-card evals unfetched.
- Japanese relevance: high for JP developers (Haiku cost tiering, Sonnet cache
  halving). Price table is directly usable.
- Links: comparator with A1 (frontier pricing week), F1 (Nova Sonic speech
  pricing absence as contrast).
- Proposed role: DEEP-DIVE (pricing + bench table with attribution) or joint
  LEAD sidebar with A1. Minimum: price table verbatim + "all benchmarks
  vendor-measured" + system-card-unfetched boundary. Do not rank Haiku vs GPT-6.

### A3. Nano Banana 2.1 (DeepMind model card) — `w41-x-nanobanana21-20261006`
- Evidence `evidence:2026-W41:e9e13879f1c0fcf8` (PARTIAL, task-1a529893f55caf14d80f).
  Sources: SOCIAL X-lead + PRIMARY_OFFICIAL DeepMind model card
  `deepmind.google/models/model-cards/nano-banana-2-1/` (bounded excerpt,
  `supplement-src-360435193adc7df6`).
  Claims: Gemini 3 series / 3.6 Flash-based; 1M input, 4K image + 64K text out;
  7-channel distribution; vendor SxS Elo (VENDOR_CLAIM, card-positive).
  Admissible negative: matching issuer blog post not found among pages checked
  2026-10-12 (claim-2, PRIMARY_FACT). FORBIDDEN legacy phrases excluded per
  overlay (`no blog post exists`, `rollout post nonexistent`).
- Verified vs vendor: card existence + spec block VERIFIED via supplement;
  Elo is vendor SxS; arena basis UNRESOLVED; pricing/license absent; docs
  unfetched.
- Mechanism: image+text model spec (context/output/distribution); no training
  or eval methodology on excerpt.
- Japanese relevance: high (image generation model, JP creator audience).
  Keep spec factual; do not moralize absence.
- Links: media/provenance theme (D1/D2) as image-model comparator; NOT linked
  to Grok ledger as event.
- Proposed role: BRIEF (spec box + vendor-Elo caveat + narrowed blog-search
  note). Minimum: card spec verbatim + "Elo vendor SxS, arena pending" +
  admissible one-line blog-search note. Any sentence asserting web-wide
  non-existence BLOCKS the issue.

### A4. Nova 2.5 Sonic GA — `w41-primary-nova-sonic-20261005`
- Evidence `evidence:2026-W41:3297d2869fcc9dbb` (PARTIAL, task-d0891837ce8f4a4b1995).
  Sources: PRIMARY_OFFICIAL AWS Nova Sonic page (delegated).
  Claims: GA Oct 5 speech-to-speech; Bedrock 4 regions; same-as-Nova-2-Sonic
  pricing (no numerics); 256K context (VENDOR_CLAIM).
- Verified vs vendor: GA date/regions VERIFIED; pricing UNRESOLVED (no
  numerics); no benchmarks/license on body.
- Mechanism: speech-to-speech GA + region list; no latency/quality numbers.
- Japanese relevance: medium (Bedrock ap-northeast-1 includes JP region;
  speech products relevant to JP voice builders).
- Links: comparator with A1/A2 (GA week) and B-group (audio omnis: Clef-omni).
- Proposed role: BRIEF, thin standalone — combine with Clef-omni as
  "speech/audio omni GA week" comparator. Minimum: date/regions/context +
  "pricing numerics absent" boundary. Do not claim price or quality leadership.

### A5. Gemini agent at Work 2026 — `w41-primary-gemini-agent-20261008`
- Evidence `evidence:2026-W41:9fdd36169d2efaf7` (PARTIAL, task-2c55480d86af19a4435b).
  Sources: PRIMARY_OFFICIAL `blog.google/.../gemini-at-work` stub only.
  Claims: universal work agent (prompt box, skills/tools, cost controls,
  enterprise governance) announced Oct 8 (VENDOR_CLAIM); rollout specifics
  deferred to Cloud blog, unfetched (PRIMARY_FACT).
- Verified vs vendor: announcement existence VERIFIED at stub level; GA date,
  SKU, pricing, regions, Workspace-vs-Cloud split all absent; customer figures
  vendor-stated per r2, not re-verified.
- Mechanism: effectively unread — feature list only, no architecture/API.
- Japanese relevance: medium-high IF enterprise rollout details existed;
  currently too thin to serve JP enterprise readers.
- Links: agent theme (C1 Decisions API, C3 Ultrafast, E1 Ironclad research).
- Proposed role: COMPARATOR/BRIEF ONLY — too thin standalone. Combine with
  Decisions API beta as "agent platform week: OpenAI shipped changelog-tier
  detail, Google shipped stub" contrast. Minimum: announce-date + feature
  bullets + explicit "rollout specifics unfetched" box. Do not present as
  GA/launch article.

## 2. Theme B — Open weights / local / edge (6 candidates)

### B1. Kolibri (Aleph Alpha) — `w41-primary-kolibri-20261003`
- Evidence `evidence:2026-W41:a85f8a48d5995bc6` (PARTIAL, task-6ef696cfd74b23a37c0d).
  Sources: PRIMARY_OFFICIAL Aleph Alpha page.
  Claims: 78B/3B MoE (78.1B/3.46B), 1M context, Apache-2.0, HF
  Aleph-Alpha/Kolibri-1 downloadable; 20T tokens, 768×B200 (VENDOR_CLAIM);
  vendor benches AIME 96.0, GPQA 84.3 (publisher-measured).
- Verified vs vendor: HF-downloadability/license-location VERIFIED as
  vendor-stated; all benches vendor-only; fetch truncated past tables.
- Mechanism: MoE scale + context + token/compute budget; no training recipe.
- Japanese relevance: medium (EU open-weights alternative; Apache-2.0 matters
  to JP builders). EU angle is the JP hook (sovereignty-adjacent).
- Links: open-weights comparator set (B2/B4/B5/B6, C-group deciders).
- Proposed role: DEEP-DIVE anchor for open-weights theme. Minimum: scale/
  context/license/download table + bench table with attribution + "tables
  truncated" boundary.

### B2. Liquid d1 decision models — `w41-primary-liquid-d1-20261007`
- Evidence `evidence:2026-W41:b4bafa16abf012ea` (PARTIAL, task-d744e3d3b41d59840ff9).
  Sources: PRIMARY_OFFICIAL Liquid AI page.
  Claims: d1-3B + d1-omni-600M open weights on HF today; Decision Index
  48.57/15.95; 8ms RTX4090 (VENDOR_CLAIM, vendor-measured).
- Verified vs vendor: HF availability VERIFIED as stated; Decision Index and
  8ms figure vendor-only; pricing/license SPDX absent.
- Mechanism: small decision-model pair + Decision Index metric + edge latency
  claim; no eval protocol on body.
- Japanese relevance: high for edge/JP on-device builders (600M omni,
  RTX4090 latency framing).
- Links: decision-model comparator (C-group Perplexity decider, MS-Decision-1
  HOLD as counterfactual).
- Proposed role: BRIEF or joint DEEP-DIVE with B1 as "small-decision vs large
  MoE" contrast. Minimum: HF paths + Index numbers with attribution + 8ms
  vendor caveat + license-absent boundary.

### B3. EmbeddingGemma 2 — `w41-primary-embeddinggemma2-20261006`
- Evidence `evidence:2026-W41:36ef2bcb44f844f9` (PARTIAL, task-49389f88b1d34f497f7d).
  Sources: PRIMARY_OFFICIAL model-card page (timeout) + launch blog
  (bounded excerpt `supplement-src-1fa2e6b4e1db612f`).
  Claims: 740M (270M+170M+300M), 768-d MRL, 8K context, Apache-2.0, HF
  google/embeddinggemma-2 + Kaggle (VENDOR_CLAIM); MTEB-Code +9.92
  (vendor, full metrics deferred to card).
- Verified vs vendor: download locations + 8K context VERIFIED as blog-stated;
  card bytes unfetched; architecture table snippet-only; MTEB vendor-only.
- Mechanism: embedding size/MRL/context; no training/eval protocol.
- Japanese relevance: high (embedding upgrades affect JP RAG builders; MRL
  Matryoshka + 8K context are the JP-relevant specs).
- Links: retrieval theme (F-group math/embed), open-weights set.
- Proposed role: BRIEF (spec box). Minimum: size/MRL/context/license/download
  + MTEB figure with "full metrics in unfetched card" boundary. Do not claim
  retrieval leadership.

### B4. Reflection Beam preview — `w41-primary-reflection-beam-20261005`
- Evidence `evidence:2026-W41:5d2673f475348f6f` (PARTIAL, task-6dc00490d25b0578d3fc).
  Sources: PRIMARY_OFFICIAL Reflection page.
  Claims: 501B/23B MoE (Oct 5, updated Oct 8); weights/report/card later this
  month, Apache-2.0 intent; early-access signup only (VENDOR_CLAIM); vendor
  benches DeepSWE 44.4, TB2.1 80.1, AIME 97.8; 23.8T tokens, GB300 RL scale.
- Verified vs vendor: preview/date/license-intent VERIFIED as stated; weights
  NOT downloadable; all benches vendor-only.
- Mechanism: MoE scale + token/RL-scale framing; no consumable artifact.
- Japanese relevance: low-medium (preview only; no downloadable artifact for
  JP builders this week).
- Links: open-weights comparator (B1 as downloadable contrast).
- Proposed role: COMPARATOR ONLY — too thin standalone (no weights, no card).
  Pair with Kolibri ("shipped weights vs promised weights"). Minimum:
  scale/intent/date + bench table attributed + "weights later this month"
  boundary. Do not present as available model.

### B5. Mistral Large 4 preview — `w41-primary-mistral-large4-20261006`
- Evidence `evidence:2026-W41:95e0813c100e3798` (PARTIAL, task-40a492061f3d95fb06b9).
  Sources: PRIMARY_OFFICIAL blog + docs pins (bounded excerpt
  `supplement-src-c10ede7c23828f99`).
  Claims: 52B active / 1–1.05T total, 1M context, preview API today, weights
  end of month, sale pricing $0.68/$2.09 (VENDOR_CLAIM, VERIFIED as stated);
  Grok X says 49B active — disagreement PRESERVED, 49B absent from official
  bodies (SOCIAL_OBSERVATION, VERIFIED as disagreement).
- Verified vs vendor: 52B/docs pins + weight-date + pricing VERIFIED as
  blog-stated; weights NOT downloadable; WEIGHTS tab/license unfetched; 49B
  X-body unfetched.
- Mechanism: dense/MoE scale + context + API-vs-weights split; no eval method.
- Japanese relevance: medium (EU flagship; API pricing usable by JP devs).
- Links: open-weights set; 49B/52B pin is the issue's version-discipline
  exemplar — cite as "official pins 52B, X says 49B, not reconciled."
- Proposed role: BRIEF with version-pin box. Minimum: 52B/1M/API-today/
  weights-end-month/pricing + 49B-disagreement note + "weights not yet"
  boundary. Do not resolve 49B vs 52B.

### B6. Clef-omni (Cloudflare) — `w41-primary-clef-omni-20261009`
- Evidence `evidence:2026-W41:5bfb1ea9fbad4623` (PARTIAL, task-007e44bf88724312afdc).
  Sources: PRIMARY_OFFICIAL `developers.cloudflare.com/changelog/.../clef-omni`.
  Claims: JSON-LD datePublished 2026-10-09T18:27:34Z → IN-WINDOW pinned
  (PRIMARY_FACT, VERIFIED); Qwen3-Omni-30B-A3B MoE; omni $0.15/M (flash cut
  $0.09→$0.038); HF open weights; vendor benches (VENDOR_CLAIM).
- Verified vs vendor: timestamp VERIFIED (cutoff logic holds); all specs/
  pricing/weights vendor-stated, HF download + SPDX unverified.
- Mechanism: omni MoE + Workers AI pricing; no eval protocol.
- Japanese relevance: medium-high (Cloudflare edge + HF weights matter to JP
  edge builders; cutoff-pin is a process exemplar).
- Links: audio/speech comparator with A4 (Nova Sonic); open-weights set.
- Proposed role: BRIEF, pair with Nova Sonic as "speech/audio omni" item.
  Minimum: timestamp-pin + spec/pricing table attributed + "HF/SPDX
  unverified; X 23:11Z post-cutoff" boundary.

## 3. Theme C — Decision models & agents / infra (4 candidates)

### C1. Decisions API public beta — `w41-primary-decisions-beta-20261006`
- Evidence `evidence:2026-W41:9719a94be83e645f` (VERIFIED, task-02f4ba5be618d07cff4a).
  Sources: PRIMARY_OFFICIAL changelog (Muse DIRECT_READ) + bounded excerpt
  `supplement-src-df537ff932f91343`.
  Claims: Decisions API beta with gpt-6-luna (`v1/decisions`), 10× faster
  than Responses API (VENDOR_CLAIM); exact changelog entry VERIFIED first-hand.
- Verified vs vendor: entry text VERIFIED (strongest authority in the issue
  alongside C3); 10× methodology absent; pricing ($0.10/M per r2 community)
  not on changelog page (UNRESOLVED).
- Mechanism: decision endpoint + model binding; no latency methodology.
- Japanese relevance: high (agent builders; beta API + model pin).
- Links: agent platform pair with A5 (stub vs changelog contrast) and C3
  (Ultrafast tier).
- Proposed role: DEEP-DIVE anchor for agent/infra theme (only VERIFIED API
  in the issue). Minimum: changelog entry verbatim + 10×-methodology-absent
  caveat + pricing-unresolved boundary.

### C2. Perplexity decider v1.1-27b — `w41-primary-perplexity-decider-20261006`
- Evidence `evidence:2026-W41:25abdeecf0872e56` (PARTIAL, task-af9f304cf7534a4d3855).
  Sources: PRIMARY_OFFICIAL issuer forum Oct 6 21:11Z (delegated).
  Claims: updated open-weights multimodal decision model; HF Decision Index
  0.3 top; $0.02/M input half v1 (VENDOR_CLAIM, forum-stated); Decision Bench
  Oct 9: 94.5% / 1071 cases @ $0.017/1k decisions (vendor).
- Verified vs vendor: forum date VERIFIED; HF benchmarks UNRESOLVED (readme
  unfetched); params beyond 27B title, license SPDX, HF URLs absent.
- Mechanism: decision-model + Decision Index/Bench framing; no protocol.
- Japanese relevance: medium (decision-model + price point for JP agent
  builders).
- Links: decision comparator (B2 Liquid d1, MS-Decision-1 HOLD, Nace Drex HOLD).
- Proposed role: BRIEF, pair with C4 (Perplexity embed) as "Perplexity pair"
  or with B2 as "decision-model week." Minimum: forum date/model/price/Index
  + "HF readme unfetched" boundary. Do not claim benchmark leadership.

### C3. Ultrafast for GPT-6.1 Sol — `w41-primary-ultrafast-sol-20261008`
- Evidence `evidence:2026-W41:7fe2d805045a8e79` (VERIFIED, task-4d4f3d1498ba6929f752).
  Sources: PRIMARY_OFFICIAL changelog Oct 8 (delegated + bounded excerpt
  `supplement-src-ec5b609a5f24671e`).
  Claims: `service_tier: ultrafast` for gpt-6.1-sol (Responses API); all users
  with rate limits; global + US/EU residency (PRIMARY_FACT, VERIFIED);
  purpose is inter-token latency, latency-vs-wall-time distinction preserved.
- Verified vs vendor: entry terms + residency VERIFIED (strongest authority
  alongside C1); pricing linked not inline; no latency numbers on page.
- Mechanism: service-tier infra primitive; no performance numbers.
- Japanese relevance: high (latency tier + residency affects JP enterprise).
- Links: infra pair with C1; latency-contrast with A1 44% claim.
- Proposed role: BRIEF (infra box) inside agent/infra deep-dive. Minimum:
  tier/model/API/residency table + "no latency numbers on page" boundary.
  Do not claim measured speedup.

### C4. Perplexity embed v2-late pair — `w41-primary-perplexity-embed-20261007`
- Evidence `evidence:2026-W41:cc453f1da5f006f9` (PARTIAL, task-f735bdb6864637a09a08).
  Sources: PRIMARY_OFFICIAL issuer forum Oct 7 16:30Z (delegated).
  Claims: two late-interaction embedding models, frontier, HF-public
  (VENDOR_CLAIM, forum-stated).
- Verified vs vendor: timestamp VERIFIED; HF availability UNRESOLVED
  (repo paths/specs/license absent); thinnest MATERIAL in the set.
- Mechanism: effectively title-only ("late-interaction pair"); no specs.
- Japanese relevance: low-medium (relevant only as Perplexity-pair context).
- Links: pair with C2 only.
- Proposed role: COMPARATOR ONLY — too thin standalone. Fold into C2 as
  one-line "plus embed pair announced next day, specs unfetched." Minimum:
  forum date + "two late-interaction models, specs/HF paths unfetched"
  boundary. A standalone article would be empty.

## 4. Theme D — Media / provenance (2 candidates)

### D1. SynthID portal — `w41-dailyx-synthid-portal-20261008`
- Evidence `evidence:2026-W41:ef2ef9a25ec009ba` (PARTIAL, task-d78c93e1181a782d035b).
  Sources: SOCIAL X-lead + PRIMARY_OFFICIAL DeepMind blog Oct 7 (bounded
  excerpt `supplement-src-bd822c4689ba127c`).
  Claims: portal global in English from Oct 7; checks image/video/audio from
  Google or partners (OpenAI, NVIDIA, Kakao, soon Apple); scale counts
  vendor-stated; text NOT listed (VENDOR_CLAIM, blog scope VERIFIED);
  synthid.com JS-shell, formats/pricing/license unfetchable (PRIMARY_FACT).
- Verified vs vendor: blog scope/partners/scale VERIFIED as stated; partner
  coverage vendor-stated; portal itself unverifiable via fetch; detection
  accuracy benchmarks absent.
- Mechanism: verification portal scope (modalities/partners), not detection
  algorithm.
- Japanese relevance: high (provenance tooling for JP media/AI governance;
  Kakao partnership is Asia-relevant).
- Links: provenance pair with D2 (textGrain) as "provenance week: Google
  portal + OpenAI watermark."
- Proposed role: DEEP-DIVE (with D2) on provenance. Minimum: scope/partner/
  modality table + "text excluded" + "portal unfetchable, accuracy absent"
  boundaries. Do not claim detection efficacy.

### D2. textGrain (OpenAI EU watermark) — `w41-dailyx-textgrain-20261006`
- Evidence `evidence:2026-W41:6601f7ffad5b2624` (PARTIAL, task-5168f0d6e2b8385c3776).
  Sources: PRIMARY_OFFICIAL `openai.com/index/eu-text-provenance` (Muse
  DIRECT_READ full body) + bounded excerpt `supplement-src-d6dd5c50f1794c7d`.
  Claims: statistical watermark; API opt-in now; EU ChatGPT/Codex coming
  weeks; detector researcher-gated; 1% FPR ~80%@200tok/~95%@400tok;
  edit-weakening numbers; Astra quality table (PRIMARY_FACT, blog-consumed
  first-hand — strongest quantitative read in the issue); tech-report PDF
  linked but binary-unparsed (PRIMARY_FACT).
- Verified vs vendor: blog body VERIFIED first-hand including FPR/token/edit
  figures + 5 non-claims; PDF captured-but-unconsumed; method internals
  restricted to blog facts.
- Mechanism: the only MATERIAL with a real quantitative methodology actually
  read (FPR/token-length/edit-robustness + quality table). Still vendor-run,
  not independently reproduced.
- Japanese relevance: highest in theme D (EU watermark precedent directly
  relevant to JP policy discourse; researcher-gated detector matters to JP
  researchers).
- Links: pair with D1; quantitative contrast to all vendor-bench-only items.
- Proposed role: DEEP-DIVE anchor for provenance theme (lead with numbers).
  Minimum: FPR/token/edit table + rollout/detector-gating + "PDF unread,
  vendor-run" boundaries. Do not present vendor FPR as independent validation.

## 5. Theme E — Safety / cyber (1 MATERIAL + HOLD context)

### E1. Cyber Mission (Anthropic) — `w41-primary-cyber-mission-20261008`
- Evidence `evidence:2026-W41:cd3f94caf69926d9` (PARTIAL, task-2e2a2ec51512e38b4bfd).
  Sources: PRIMARY_OFFICIAL `anthropic.com/news/anthropic-cyber-mission`
  (delegated).
  Claims: CIDP (11 named founding partners) + OSS Scanner (opt-in, free,
  model-generated PoC reports, no human review, >90% TP expected)
  (VENDOR_CLAIM; partners/opt-in/no-review/>90% VERIFIED as stated).
- Verified vs vendor: program scope/partners VERIFIED as listed; scanner
  efficacy (>90% TP) is vendor-expected, no measured outcomes; scanner post
  and CIDP form internals unfetched.
- Mechanism: program + scanner offering; no detection methodology.
- Japanese relevance: medium-high (security audience; partner list + free
  opt-in scanner are actionable).
- Links: safety context with HOLD `unintended-actions` (day-only, HOLD) as
  "published safety program vs unpinnable incident report" contrast.
- Proposed role: BRIEF (program box). Minimum: CIDP/scanner terms + partner
  count + ">90% expected, no measured outcomes" boundary. Do not claim
  measured protection.

## 6. Theme F — Retrieval / science / speech-infra (3 candidates)

### F1. OpenAI mathematics results — `w41-primary-openai-math-20261006`
- Evidence `evidence:2026-W41:feec9ec0eabe1d59` (PARTIAL, task-81377ee6d9f7f12eaf29).
  Sources: PRIMARY_OFFICIAL OpenAI math release page (delegated).
  Claims: broad new mathematical results from internal frontier model
  (unnamed); GitHub `openai/math` repo + Lean partial formalizations + 10
  reasoning summaries + Pro-usage compute stats (~3h avg) (VENDOR_CLAIM);
  model itself NOT released, responsible-release ongoing, no date
  (VENDOR_CLAIM, boundary VERIFIED).
- Verified vs vendor: repo/formalization/summary/compute contents VERIFIED
  as listed; repo file counts/licenses unenumerated; model identity withheld.
- Mechanism: release-of-results (not release-of-model); Lean formalization
  extent is the technical substance, but files unenumerated.
- Japanese relevance: medium (math/science audience; Lean formalization is
  the hook; unnamed-model boundary must be explicit for JP readers).
- Links: science item; no close comparator — place as standalone BRIEF.
- Proposed role: BRIEF. Minimum: repo/Lean/summary/compute list + "model
  not released, no date" boundary. Do not name the model or claim proof
  verification.

### F2. Ironclad computer-use research — `w41-primary-ironclad-20261006`
- Evidence `evidence:2026-W41:ad97bfa3daa6e156` (PARTIAL, task-b526a5361c5274a82fe0).
  Sources: PRIMARY_OFFICIAL `openai.com/index/advancing-computer-use-with-ironclad`
  (delegated).
  Claims: 11 contracting tasks, EDGAR-simulated (no customer/internal/
  nonpublic data); Astra Max 55.0% vs Sol High 41.6% (+32%), 37.0→19.2 min
  (−48%), all simulated vendor-stated (VENDOR_CLAIM, simulation boundary
  VERIFIED); Ironclad product launches separate, not on page (PRIMARY_FACT).
- Verified vs vendor: simulation scope + numbers VERIFIED as stated; rubric/
  per-task/RL details absent; provisional research only.
- Mechanism: simulated contracting eval (EDGAR-simulated contracting tasks);
  vendor-run, not deployment measurement.
- Japanese relevance: medium (computer-use eval design is relevant to JP
  enterprise automation readers; simulation boundary is the lesson).
- Links: agent/eval bridge (C-group); product-separation note prevents
  Ironclad-product confusion.
- Proposed role: BRIEF with simulation-boundary box. Minimum: 11-task/
  EDGAR-simulated scope + numbers attributed + "rubric absent, provisional"
  boundary. Do not present as deployment gain.

### F3. (Speech-infra comparator — Nova/Clef already covered)
Nova Sonic (A4) and Clef-omni (B6) serve as the speech/audio infra pair;
no third F-item is needed. Do not manufacture a retrieval/science article
from Perplexity embed (C4, too thin) or Nace Drex (HOLD).

## 7. Why 13 HOLD / 3 CONTEXT are not selected (with counterfactuals)

HOLD 13 = 12 NEEDS_MORE cards + Drex PARTIAL/HOLD. Each HOLD is a genuine
Evidence limitation, not incomplete consumption:

- `w41-dailyx-agr-20261006` (NEEDS_MORE): X-only Agr decision-model announce;
  HF repo/card/evals unverified. Counterfactual: if HF repo were opened and
  card/evals read, could be B-group brief. Now: HOLD correct.
- `w41-dailyx-elevenlabs-20261010` (NEEDS_MORE): X-only detection+WG announce;
  Audio Detector + SynthID docs exist but WG charter/membership/spec not found.
  Counterfactual: if WG charter retrieved, could be D-theme sidebar. Now: HOLD.
- `w41-dailyx-nace-drex-20261010` (PARTIAL/HOLD): nace.ai/drex docs read
  (128K ctx, Index 58.28, API, Sep GA) but W41 X shortlink/HF/license
  unverified. The highest-material HOLD. Counterfactual: if shortlink/HF
  resolved in-window, could join C-group decision brief. Screening=INSPECT
  + unresolved W41 hook → HOLD is correct, not a miss.
- `w41-dailyx-nace-ndi-20261010` (NEEDS_MORE): X intro only; no 1.0 version
  label/date/pricing/bench/license. Counterfactual: if docs version label
  found, could be brief. Now: HOLD.
- `w41-dailyx-nemotron-hf-20261006` (NEEDS_MORE): X + HF existence per raw;
  weights/cards unopened. Modest distribution event. HOLD correct.
- `w41-dailyx-stepfun-20261009` (NEEDS_MORE): X + OpenRouter snippet
  (600B/27B, $1/$2.70, 1M ctx, free week) but official page JS-gated,
  preview-vs-weights distinction pending. Highest-regret HOLD alongside Drex.
  Counterfactual: if official page retrievable, could be B-group deep-dive.
  Now: HOLD correct; snippet-only pricing must not anchor an article.
- 4 W40 carry HOLDs (AstaBrief, AutoSynthData, PixelCanary, TBCVideo):
  rechecked, no W41 new dated evidence. HOLD retained; no promotion without
  new dated evidence. Not counterfactuals — correctly aged out.
- `w41-hold-tencent-20261011` (NEEDS_MORE): HF card read but News bullets
  month-only, no day upload date; papers pre-window. Upload recency ≠ dated
  event. HOLD correct.
- `w41-primary-ms-decision1-20261009` (NEEDS_MORE): page dated 2026.10.09 with
  NO clock; Qwen3.5-9B scorer, Foundry+OpenRouter, $0.042/M. Clock absence →
  cutoff unprovable. Counterfactual: if clock < 22:00Z proven, could join
  C-group. Now: HOLD correct and must stay HOLD.
- `w41-primary-unintended-actions-20261009` (NEEDS_MORE): day-only Oct 9
  report, body not consumed in r3, instant unproven vs cutoff. Counterfactual:
  if instant pinned in-window and body consumed, could be E-theme sidebar.
  Now: HOLD correct.

CONTEXT 3:
- `w41-grok-x-ledger-20261011`: provenance-only (see §0). Never an article.
- `w41-primary-usage-policy-20261008`: governance page, CONTEXT sidebar at most.
- `w41-weak-elyza-rsi-20261002`: pre-window JP RSI work, CONTEXT background.
  JP relevance is real (ELYZA) but newness is absent; CONTEXT is correct.

EXCLUDED 1:
- `w41-sweep-negativespace-20261011`: sweep artifact, not an event. Correct.

No justified-hold gap blocks issue formation: 20 MATERIAL already cover
frontier/open-weight/audio/safety/retrieval/agent lanes with first-party
corroboration. The 12 NEEDS_MORE need Sol's gap-fill-vs-HOLD call, but none
is a missing lead article.

## 8. Article-grouping recommendation (do not equate 20 subjects to 20 articles)

Thin standalone risks (must be combined):
- Gemini agent (stub) → fold into Decisions/Ultrafast agent-infra item.
- Perplexity embed (title-only) → fold into Perplexity decider pair line.
- Reflection Beam (no weights) → comparator inside Kolibri-led open-weights.
- Nova Sonic (no numerics) → comparator with Clef-omni speech/audio.
- Mistral Large 4 (preview) → brief with version-pin box, not deep-dive.
- F-math (unnamed model) → brief, not a model-release article.

Proposed 6-theme packaging (5–7 reader articles, not 20):
1. Frontier rollout week (A1+A2, with A5/C3 infra sidebar).
2. Open weights: shipped vs promised (B1 anchor + B2/B3/B6 briefs + B4/B5 comparators).
3. Agent platform + infra (C1 anchor + C3 box + A5 contrast + C2 brief; C4 one-liner).
4. Image model spec (A3 brief with exclusion-compliant blog note).
5. Provenance week (D2 anchor + D1 deep-dive pair).
6. Safety + science briefs (E1 + F1 + F2 + A4/B6 speech box as needed).

Page/word-depth honesty: exact pagination is NOT fixed at this stage (no TeX).
Qualitative estimate only: items 1–3 and 5 can carry deep-dive weight (vendor
tables + first-party pins); items 4 and 6 are briefs by evidence boundary.
Any plan promising 20 full articles from these 20 MATERIAL would be inflation;
the honest issue is 5–7 grouped articles plus sidebars.

## 9. Completeness LIMITED is truthful (SC-M41-04)

`LIMITED` is retained because: 09:00 absence, X-authorship, unread PDF/JS
bodies, day/month clocks, snippet-only pricing, delegated re-verification
pending, projection approval pending, no byte-identical HTML. Current
relevance SATISFIED (37/37 disposed, Grok corrected to CONTEXT), carry-over
SATISFIED (4 W40 HOLDs + ELYZA bounded), technical significance LIMITATION
(vendor-only metrics, 5 partial bodies). No NEEDS_RESEARCH is open that would
force INCOMPLETE, and READY would require dropping limitations — forbidden.
Core `validate_profile_completeness` PASS (override, historical screening
state-basis drift only) confirms LIMITED is the honest terminal for this stage.

(End of file)
