# W43 r5 fal official source conflict crosswalk (edition-local, noncanonical)

Status: `EDITION_LOCAL_SOURCE_NOTE / NO_CANONICAL_MUTATION`
Date: 2026-10-25. Starting HEAD `fe02b29ae026d7df3cf52a5a88a1c3c48d6268de` / Tree `769ba06f1dbd0f7c04cc40082a67bea2a8beb8fc`.
Scope: three fal first-party sources actually rendered-read 2026-10-25 for R4-011/012 + ISA-004. No new immutable raw bytes archived; accepted r4 Evidence / Views / supplement raw untouched. Rendered-only pages are marked RENDERED_ONLY — no original-page HTML byte claim.

## 1. fal publisher blog — https://fal.ai/blog/introducing-flux-3-max-by-fal

- observed_at: 2026-10-25 (rendered read; mutable page, no pinned version).
- Speed table (rendered): 12.45s (FLUX 3 Max 10-second video) vs 277.80s (Seedance 2.5), quoted as **26.5× faster, 96.2% lower latency**. Arithmetic check: 277.80/12.45=22.3133→22.31x; (277.80−12.45)/277.80=95.5184%→95.52%. The quoted 26.5x/96.2% pair is incompatible with the shown 12.45s/277.80s inputs.
- Quality delta (rendered): **+47 Elo** image-to-video improvement versus FLUX 3 (blog snapshot; comparison target/version implicit).
- keyframes: blog contains a keyframes-to-video導線 (link present).
- Byte provenance: RENDERED_ONLY. Not an independent speed/Elo study.

## 2. fal official product page — https://fal.ai/flux-3-max

- observed_at: 2026-10-25 (rendered read).
- Speed table (rendered): 12.45s vs 277.80s at tied 1,139 Elo, described as **about 22 times faster**. Table: FLUX 3 Max 1,139/12.45s; FLUX 3 1,089/126.44s; Seedance 2.5 1,139/277.80s. Note under table: "Elo: Artificial Analysis AA-Video-I2V v1.1, preliminary… Generation time: average for a 10-second, 16:9 video at 720p/768p."
- Quality delta (rendered): "**Post-training lifted FLUX 3 by 50 Elo points, from 1,089 to 1,139**"; FAQ repeats "scores 50 Elo points higher than FLUX 3 (1,139 against 1,089)". Check: 1,139−1,089=50.
- Endpoints FAQ (rendered): "**Two at launch: text to video and image to video. Information updated as of October 18, 2026.**" Hero/API docs expose text-to-video and image-to-video only.
- Byte provenance: RENDERED_ONLY. Publisher statement, not independent benchmark.

## 3. fal-issued PR via PRNewswire — https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html

- Publisher + distributor: fal-authored release, distributed by PRNewswire (distributor ≠ author). Published **Oct 19, 2026, 15:46 ET** — inside W43 window [2026-10-16T22:00Z, 2026-10-23T22:00Z).
- Speed (rendered): "**generating a 10-second video in 10.95 seconds, over 22× faster than Seedance 2.5** … (10.95s vs 277.80s) at the same reported Elo"; "11.5× faster inference than FLUX 3 (126.44s → 10.95s)". Check: 277.80/10.95=25.3699→25.37x. Headline "22×" reads as a lower-bound/conservative statement, not a precise quotient — do NOT call it mathematically false on headline alone.
- Quality (rendered): "**1,139 Elo rating across 4,868 votes** … among the highest-quality"; "**50-point improvement** (1,089 → 1,139)". Check: 1,139−1,089=50.
- Availability (rendered): "**available beginning October 19, 2026** … frontier **text-to-video, image-to-video, and keyframes-to-video generation through a unified API**."
- Byte provenance: RENDERED_ONLY (no new W43 edition-local raw archive in this pass). Publisher-authored first-party source, NOT a third-party benchmark.

## 4. Conflict matrix (what r5 Architecture now says)

| Dimension | Blog | Product page (Oct18 FAQ) | Oct19 PR | r5 binding |
|---|---|---|---|---|
| 10s latency | 12.45s | 12.45s | 10.95s | Both quoted with source/version; recomputed 22.31x / 25.37x; 95.52% for 12.45s leg |
| "× faster" | 26.5x (incompatible w/ shown inputs) | ~22x | over 22x / 11.5x vs FLUX 3 | 26.5x marked incompatible; 22x as lower-bound OK |
| Elo delta vs FLUX 3 | +47 (blog snapshot) | +50 (1139 vs 1089) | +50 (1089→1139) | No single universal delta; 1139−1089=50 verified; AA snapshot/version UNKNOWN |
| keyframes endpoint | link present | Two at launch (text+image), Oct18 | text+image+keyframes via unified API, Oct19 | UNRESOLVED_VENDOR_DOC_CONFLICT; no verified W43 live/schema/GA proof; neither asserted nor denied |
| Votes | — | — | 4,868 (preliminary) | Vendor-attributed; AA originals unarchived |

## 5. What was NOT done

- No 10.95s/12.45s independent timing, no Elo re-vote, no API live-call, no schema/GA proof, no AA original retrieval, no raw-byte archival. Independent reproduction remains NOT_DONE by design at Architecture stage.
