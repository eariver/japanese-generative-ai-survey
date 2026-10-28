# W43 Oct23 event-clock audit (cutoff `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`, exclusive end)

Status: `EDITION_LOCAL_DIAGNOSTIC / READ_ONLY / NO_STAGE_ADVANCE`
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. Window: EDT Oct16 18:00–Oct23 18:00 = UTC Oct16 22:00–Oct23 22:00, right edge exclusive.

## Method

- Canonical Discovery `discovery-v2.jsonl` (51) + Screening `screening-accepted.json` (KEEP17/MAYBE11/INSPECT4/DROP19) read, not reconstructed.
- r3 Cards/Views/ledger/completeness + Supplement r3 (21) + archived raws read; live primary pages + registry/API metadata fetched read-only for clock proof (no canonical writes).
- `published_at` day-only is NOT a clock; `T00:00:00Z` normalization is a placeholder, not observation. SEO index time, post EDT calendar day, social reaction are not IN proof.

## Per-ID verdicts (Oct23-relevant + carries)

| Discovery | Screening | Publisher source / observed clock (UTC) | Precision | Verdict | Action |
|---|---|---|---|---|---|
| `w43-primary-github-metrics-20261023` MAYBE | reason metering change, low confidence | `github.blog/changelog/...-opencode/` JSON-LD `2026-10-23T16:42:03-07:00` = **`2026-10-23T23:42:03Z`**; `dateModified 23:43:37Z` distinct; archived 107700B `be7fab…`; external first-seen 23:53Z | EXACT (publisher JSON-LD) | **OUT_OF_WINDOW** (+1h42m03s after exclusive cutoff) | W43 story prohibited; stage in W44 or explicit past-window CONTEXT only after authority decision |
| `w43-primary-github-teams-20261023` MAYBE | changelog-level, low | Same changelog host: JSON-LD `2026-10-23T14:29:58-07:00` = **`21:29:58Z`**; Yoast `21:29:58+00:00`; `dateModified 23:46:48Z` ≠ publication; displayed `October 23, 2026` day-only | EXACT (JSON-LD) | **IN** (30m02s before cutoff) | Keep; do NOT infer from Metrics lateness |
| `w43-primary-kimi-20261023` KEEP high | announce/API 17:15:24Z | X `2026-10-23T17:15:24Z` = **17:15:24Z IN** (4h44m36s inside); blog day-only (no clock); weights Nov 4 FUTURE | EXACT (X post) | **IN via X**; blog `T00:00Z` is placeholder | Membership on X event, not blog midnight |
| `w43-primary-nemotron-e4b-20261023` KEEP high | 64K, OpenMDW | Research page `article:published_time 2026-10-23T00:00:00-07:00` = **07:00Z**; `<time 2026-10-23T00:00:00-07:00>`; S3 `last-modified 14:11:55Z`; HF `NVIDIA-Nemotron-3.5-Bolt-E4B-4GB` commits 15:12:12Z→19:03:57Z (initial→GGUF 65536), `createdAt Oct05` = staging not availability | EXACT (page TZ + HF commits) | **IN** (07:00Z / 14:11Z / 15:12–19:03Z all < 22Z) | Keep; supplement midnight `T00:00Z` must be relabeled DATE_ONLY (page TZ is 07:00Z) |
| `w43-primary-tanstack-20261023` KEEP med | 76 pkgs stable, harness 0.x | Blog `article:published_time 2026-10-23`, JSON-LD `datePublished 2026-10-23`, `<time datetime=2026-10-23>` — day-only, no TZ/clock | DAY_ONLY | **UNRESOLVED (blog clock)** | Blog alone cannot prove IN; proxies IN (npm `1.0.0 2026-10-22T15:21:49Z`, GH release `published_at 2026-10-22T15:18:14Z`, `15:20/15:18 Oct22` UI) support package availability Oct22 but do not resolve blog clock |
| `w43-r2-openai-securing-20261023` KEEP high | containment, red-team | Page displayed `October 23, 2026` only; static HTML has zero `article:published_time/datePublished/ld+json` (only `publicationDateText/Date: October 23, 2026`); curl 403 Cloudflare challenge (~10KB, no date); official RSS `pubDate Fri, 23 Oct 2026 10:00:00 GMT` = **10:00Z** | DAY_ONLY page + SECONDARY RSS | **IN with caveat / UNRESOLVED on page-primary-only strict rule** | IN depends on accepting official RSS 10:00Z; page alone cannot prove <22Z |
| `w43-support-vercel-ollama-20261017` MAYBE low | distribution proof only | Composite: Vercel leg **Oct17** (`vercel.com/changelog/...-1017` Published Oct17; `deepseek-v4.1-flash-1017`; X Oct17 9:02AM; upstream `news261017`); Bolt/Ollama/Unsloth leg **Oct23** (research page Oct23; HF/Build Oct23; `ollama:e4b` tags `e4b/7.2-7.9GB`, page `Updated yesterday`, no hard date; Unsloth `v0.1.910-beta 2026-10-23T15:26:53Z`); Discovery `published_at 2026-10-23` + Card `event 2026-10-23` collapse two legs under Ollama locator (`FULL_BODY_UNCONSUMED`) | MIXED (range Oct17–23) | **UNRESOLVED (identity)** | Do NOT redate ID or event; split legs or explicit range with pins (`deepseek-1017 10/17`; Bolt 10/23 + blobs `fe4af3f5/69f2be39` + Unsloth `15:26:53Z`) |
| Other Oct23 `published_at` day-only (Decisions Oct22, auto-mode Oct22, Patch Oct21, Flint Oct21, FLUX Oct19 — not Oct23) | — | No additional Oct23 day-only non-DROP beyond the 7 above; DROP/OUT rows excluded from table (19 DROP + 12 carries retained) | — | — | 12 W42 carries 11 DROP / 1 CONTEXT unchanged |

## Nine `T00:00:00Z` placeholders (Supplement r3)

`auto-mode 2026-10-22T00:00Z`, `Decisions 2026-10-22T00:00Z`, `FLUX ×2 2026-10-19T00:00Z`, `Kimi blog 2026-10-23T00:00Z`, `Nemotron 2026-10-23T00:00Z`, `Patch 2026-10-21T00:00Z`, `Flint ×2 2026-10-21T00:00Z` — all `DATE_ONLY_PLACEHOLDER_NOT_OBSERVED_CLOCK`. Schema (`evidence-authority-supplement-v2.schema.json`) permits `published_at: string|null (date-time)`; null + relation precision note is the supported non-fabricating option. GCP midnight was already corrected to NULL in r3; the other nine remain labeled only in this diagnostic — accepted JSON unchanged per contract. Especially near cutoff (Kimi blog, Nemotron), midnight must never be read as `<22:00Z` proof (Kimi IN rests on X 17:15:24Z; Nemotron IN rests on 07:00Z page TZ + 15:12–19:03Z commits, not midnight).

## Raw provenance used (existing, no new canonical archive)

- Metrics 107700B `be7fab…` (JSON-LD 23:42:03Z = OUT proof); Teams live HTML (21:29:58Z = IN proof, not archived as canonical — diagnostic only); Nemotron card 59009B (IN corroboration; HF commits/API live); TanStack npm/GH release Oct22 (proxy, not blog clock); Securing RSS 10:00Z (secondary); Kimi X 208731B + blog 390347B (X IN, blog day-only); Vercel Oct17 + Unsloth `15:26:53Z` + research Oct23 (composite proof).
- No forged SHA/clock/source-type/full-read claims. Duplicate archive avoided where existing raw suffices.
