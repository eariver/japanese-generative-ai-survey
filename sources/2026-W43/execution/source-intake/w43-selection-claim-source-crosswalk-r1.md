# W43 Selection claim → true primary source crosswalk r1 (no fused URLs)

Status: `EDITION_LOCAL_CITATION_MAP / PROPOSED`
Date: 2026-10-25. All reader citations must use exact supplement IDs + URLs + excerpts below. Fused Discovery `src-1` locators (Kimi `X + blog`, Flint `article + HF`) are `DISCOVERY_ONLY_NOT_CITABLE` — retained internally by frozen Card schema, never presented as one URL.

## P1 open-weights (Kimi P + Flint P + Nemotron S)

- Kimi 17:15:24Z + 4h44m36s + post ID + API live → `src-1` X leg (`https://x.com/Kimi_Moonshot/status/2113680701770068067`, raw 208731B `0891bc1e…`, `2026-10-23T17:15:24.000Z`).
- Kimi 1M ctx + Highspeed 2–3x + Nov4 FUTURE + $2/$10 + harnesses + cyber removal → `supplement-src-041ec6c5600beb4d` (`https://www.kimi.ai/blog/kimi-k3-1-pro`, 390347B `86cc8bbe…`; excerpts `1-million-token context`, `released by Nov 4`, `2–3× Highspeed`, `temperature = 1.0, top-p = 0.95, max`, Claude-Code harnesses). `2.8T/104B` X-only — never cite blog for it.
- Flint 512K/256K + 125+/150+ apparatus + Eureka + benches → `supplement-src-d2d2f48e181fb4dd` (`https://recursive.com/updates/introducing-recursive-flint`, 366583B `ce42b796…`; excerpts `up to 512k`, `within 256k`, `125 … M4 Pro … 150 … RTX Spark … short contexts`, `128k-token session … prefill excluded`).
- Flint 39.8B/2.5B + 49 layers + 256 experts + SWA-513 + 262144 + Apache-2.0 + 14:20:58Z weights → `supplement-src-e1fe975d225aaa88` (`https://huggingface.co/RecursiveSI/flint`, 6250B `43244381…`).
- Nemotron 64K + OpenMDW-1.1 + Gemma Apache-2.0 → `supplement-src-9e10348cb212038f` (card 59009B `8a06cc67…`, DATE_ONLY null) + commits `supplement-src-deae3d33c374f4eb` (API 1307B `09fcdd58…`: `15:12:12Z initial` → `19:03:57Z`; `createdAt Oct05` = staging). OSI recognition: no claim (UNVERIFIED).

## P2 infra (DeepInfer P + MemT P)

- DeepInfer literals → `supplement-src-e20f1cffc1444d3a` (environ.py 8738B `fe2c5319…` @9bd9cf243…: `DEEPINFER_ENABLE_MTP_VARLEN`, `DEEPINFER_USE_NEXTN_DECODE … default 5`) + `supplement-src-d0805b13331ce793` (README 4660B: `SET DEEPINFER_ENABLE_MTP_VARLEN=1 … default: 5`) + `supplement-src-d818147e4521ac7a` (LICENSE 11357B Apache-2.0). Repo OUT Oct16 vs content IN Oct20 distinguished.
- MemT architecture/benches/serve → `supplement-src-927931f4a303eaa6` (paper 7096280B `959206da…`, NO license terms) + license split → `supplement-src-baee90a6382ccdbd` (README 10170B `5d576f44…` @e75c13d0…: `Paper … CC BY-NC-SA 4.0`, `Repository software … PolyForm Noncommercial 1.0.0`, `flash-linear-attention … MIT`, `weights, datasets … NOT covered`).

## P3 agent (Duet P + 1Password S + Automode S)

- Duet waitlist/plan-limits/behaviour/VM/6000+/payments/safety → `src-1` (`primary:claude.com/resources/articles/claude-duet`, Discovery-bounded; no new supplement — wording fix only, vendor-described limits preserved).
- 1Password approval/injection/plan → `src-1` (`primary:1password.com/blog/1password-for-ai-agents`); coming-soon vs live distinguished in prose.
- Automode Aug7 OUT/Oct22 IN/FUTURE + classifier → `src-1` + `supplement-src-6f18c05b01b43f45` (article 599884B `8ed45487…`); X is SOCIAL observation, not clock.

## P4 video (FLUX P)

- Platform/availability → `src-1` + `supplement-src-1ae0efcded48b6e4` (model 326207B `9e8ddfd6…`: `12.45 seconds`, `277.80 seconds`, `22 times`) + `supplement-src-32e30026645a68d3` (blog 225919B `50ac7df9…`: `12.45 seconds`, `277.80`, `26.5×`, `96.2%`). Arithmetic 25.37/22.31/95.52 shown; `26.5×/96.2%` contradiction preserved; 10.95 PR origin noted (not on current pages). Elo/pricing vendor-cited, AA unfetched.

## P5 speech (Voxtral P + Ming S + Eleven S)

- Voxtral family/evals/pricing/SDK → `src-1` (`primary:mistral.ai/news/voxtral-3`); vendor evals + vendor-chosen judge + AA unfetched noted.
- Ming tasks/AA/MIT → `supplement-src-1d329e6cfb492783` (README 74543B @028c1ea) + `supplement-src-5bb55c72ae60d4a2` (LICENSE 1067B MIT); AA ranks publisher-cited, pages unfetched.
- Eleven models/AA/protocol → `src-1` (`primary:elevenlabs.io/blog/realtime`); AA via vendor blog (BBA/TTFA/Full-Duplex/Arena/tool-use), protocol compat, guide unopened.

## P6 security (Patch P + Securing P)

- Patch GPT-5.6 Sol + 5-stage + Wiz/Cloudflare + $1B + checker + zero CVE → `supplement-src-fe148ca1b75a67dd` (RENDERED 3210B `f70ef5b3…`; curl 9946B spinner only, NOT original HTML) + `src-1`. Vendor disclosure ≠ CVE proof.
- Securing containment/red-team/gating + RSS hour → `src-1` (page day-only) + `supplement-src-7648a293320fac45` (RSS 803075B `6ab1e0…`: `<link>…securing…</link>` + `<pubDate>Fri, 23 Oct 2026 10:00:00 GMT</pubDate>` — secondary provenance labeled).

## P7 science (Bio P + Lowresource P)

- Bio protocol/cases/preference/provenance → `src-1` (`primary:openai.com/index/scaling-ai-research-for-complex-biological-data/`); team evaluation + blinded 75% + wet-lab pending + ZERO repro.
- Lowresource protocol/tables/migration/suite/costs → `src-1` (`primary:openai.com/index/low-resource-programming-languages/`); we/our language, suite release ≠ repro, hidden tests held, costs vendor-measured.

## P8 devtooling (Decisions P + TanStack S + DeepSeek S)

- Decisions GA/specs/pricing/testimonials → `src-1` + `supplement-src-2a49a7d4f6f2ae5a` (changelog 553250B `ea48630a…`); 10x/testimonial bias noted; main page not archived.
- TanStack stable/harness/codemod + product/blog split → `src-1` (blog day-only, DATE_ONLY null) + `supplement-src-22fcccb239a19447` (GH release 27590B `0ab83c0d…`: `published_at 2026-10-22T15:18:14Z`, `created 15:17:40Z`; npm `1.0.0 15:21:49Z` corroborates).
- DeepSeek snapshot/demos/weights/Harness/pricing/benches → `src-1` (`primary:api-docs.deepseek.com/news/news261017` + converts); SHA/billing untested.

## Excluded (never cited as W43 story)

- Metrics: `src-1` (day-precision history) + `supplement-src-1a8d33ae41ab22ad` (107700B, 23:42:03Z OUT) — cited only for post-cutoff correction + W44 pointer.
- Grok: `src-1` only (X raw 13425B) — audit binder, never story.
- 10 CONTEXT REJECT + 19 DROP: Discovery/Screening history only; no reader citation as W43 article.
