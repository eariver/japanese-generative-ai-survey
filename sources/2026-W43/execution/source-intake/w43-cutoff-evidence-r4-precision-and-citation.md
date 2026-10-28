# W43 cutoff precision + citation crosswalk r4 (statement → supplement → excerpt)

Status: `EDITION_LOCAL_PROVENANCE / R4_POSTCUTOFF`
Date: 2026-10-25. Supplement-r4 25 (21 retained: 9 day-only + GCP/paper already-null → NULL/DATE_ONLY_PRECISION, 0 `T00:00Z`; + 4 exact: Teams/Nemotron-commits/TanStack-release/Securing-RSS). Fused Discovery `src-1` locators immutable (Kimi X+blog, Flint article+HF); reader citations must use exact supplement IDs below, never fused strings.

## Metrics (OUT, POST_CUTOFF/NON_MATERIAL)

- claim-1 (preserved API facts + clock) → `src-1` (`primary:github.blog/...opencode`, day-precision Discovery) + `supplement-src-1a8d33ae41ab22ad` (`https://github.blog/changelog/...opencode`, 107700B `be7fab…`): excerpt `datePublished 2026-10-23T16:42:03-07:00 = 2026-10-23T23:42:03Z`, `model_selection_mode user_selected/auto/product_selected/other/unknown`, `request_count = successful model requests NOT prompts`, `best-effort integration ID`.
- claim-2 (supersession: provisional `Fresh in-window lead` → verified OUT +1h42m03s, no pre-22Z event, W44-pointer-only) → same IDs; excerpt `dateModified 23:43:37Z distinct`, `exclusive cutoff 22:00:00Z`.
- View rationale: `POST_CUTOFF / NON_MATERIAL`, excluded from W43 story/Selection.

## Other Oct23 clocks (IN / caveat / split)

- Teams (IN 30m02s): claim → `src-1` + `supplement-src-52dba048e55beefa` (Teams HTML 105311B `d0a38e…`): `datePublished 2026-10-23T14:29:58-07:00 = 21:29:58Z`, `Yoast 21:29:58+00:00`, `modified 23:46:48Z distinct`.
- Kimi (IN via X): claim-1 (17:15:24Z + 4h44m36s + post ID + API live) → `src-1` (X leg) + `supplement-src-041ec6c5600beb4d` (blog 390347B, DATE_ONLY null): excerpts `17:15:24.000Z` vs `Full model weights will be released by Nov 4`; `2.8T/104B` X-only, `1M ctx` blog. W43 membership rests on X, not blog midnight.
- Nemotron (IN): claim (07:00Z + 15:12–19:03Z) → `src-1` + card `supplement-src-9e10348cb212038f` (59009B, DATE_ONLY null) + `supplement-src-deae3d33c374f4eb` (commits 1307B `09fcdd…`): `research page 00:00-07:00 = 07:00Z`, S3 `14:11:55Z`, HF `15:12:12Z initial → 19:03:57Z` (createdAt Oct05 = staging).
- TanStack (product IN / blog UNRESOLVED): claim → `src-1` + `supplement-src-22fcccb239a19447` (GH release 27590B `0ab83c…`): `published_at 2026-10-22T15:18:14Z` (`created 15:17:40Z`; npm `1.0.0 15:21:49Z` corroborates); blog `2026-10-23` day-only UNRESOLVED — two events, not conflated.
- Securing (IN-caveat): claim → `src-1` + `supplement-src-7648a293320fac45` (RSS 803075B `6ab1e0…`): `<link>.../securing-our-frontier-model-training-environment</link>` + `<pubDate>Fri, 23 Oct 2026 10:00:00 GMT</pubDate>`; page day-only (no `article:published_time`, curl 403). Hour = RSS (secondary), not page proof.
- Vercel/Ollama (split, CONTEXT): claim-1 (Vercel Oct17: changelog Published Oct17, X Oct17 9:02AM, `news261017`) + claim-2 (Bolt/Ollama Oct23: research Oct23, HF/Build Oct23, `ollama:e4b` tags, Unsloth `v0.1.910-beta 2026-10-23T15:26:53Z`) → `src-1` only (existing Discovery; no unified event date asserted).

## Nine DATE_ONLY nulls (r4)

Auto-mode / Decisions / FLUX×2 / Kimi blog / Nemotron card / Patch / Flint×2 (+ retained GCP/paper nulls) = 11 NULL / 0 `T00:00Z`. Relations state `DATE_ONLY_PRECISION + real date + no-clock warning`; bytes/SHA/IDs unchanged (same raw). Exact IN rests on Teams 21:29:58Z / Nemotron 15:12–19:03Z / Kimi X 17:15:24Z / TanStack product Oct22 / RSS 10:00Z, never midnight.

## IA-017 Kimi/Flint per-claim map (fused `src-1` = Discovery provenance only)

- Kimi 1–4 → blog-only facts (1M ctx, Highspeed 2–3x, Nov4, benches/cyber text) cite `supplement-src-041ec6c5600beb4d`; X-only facts (17:15:24Z, 4h44m36s, post ID, 2.8T/104B) cite `src-1` X leg. Never present `url1 + url2` as one URL.
- Flint 1–3 → capability/speed cite `supplement-src-d2d2f48e181fb4dd` (article 366583B: `up to 512k / within 256k`, `125+ M4 Pro / 150+ RTX Spark short-context 128K-avg prefill-excluded`); weights/config/license cite `supplement-src-e1fe975d225aaa88` (card 6250B: `39.8B/2.5B`, `262144`, `Apache-2.0`). Card schema retains `src-1` internally as `DISCOVERY_ONLY_NOT_CITABLE`.

## IA-018 erratum (append-only)

`interactive-evidence-r2.json → r3.json` = **19 substantive / 13 rationale-only / 0 identical** (JSON compare). All 32 accepted Card SHAs differ (package/basis regen, not 32 claim edits). Prior closure `20 changed / 12 same` (accepted-Card text compare) is superseded for semantic inputs. r3→r4 = **7 substantive** (Metrics/Teams/Kimi/Nemotron/TanStack/Securing/Vercel) **+ 25 identical** (focused correction, no churn). Old files unchanged.
