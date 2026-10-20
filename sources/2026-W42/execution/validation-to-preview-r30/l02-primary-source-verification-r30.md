# W42 r30 L02 — bounded primary-source verification (B16 / B54 / B57)

Scope: Sol disposition `W42-R29-L02` (MEDIUM / AUDIT-SCOPE). No general re-research; no published-word change.
Date: 2026-10-20 JST. Method: bibmap + TeX claim capture, one live fetch per URL, verbatim short excerpts only.
Worker: Muse (W42 r30 execution). This is worker evidence, not an independent verdict.

## B16 — Beam LICENSE (bibmap `bibliography-map-r18.json`, TeX `\bibitem[B16]`)

- URL (bibmap = TeX, exact match): `https://huggingface.co/reflection/Beam-1.0-501B-A23B/resolve/main/LICENSE`
- TeX claims: repository LICENSE full text confirms Apache 2.0 application; no unique display-badge duty; standard redistribution conditions remain (license copy, copyright/attribution/NOTICE retention, change notice, patent, third-party terms); third-party portions separate.
- Fetch: SUCCESS. Full Apache License 2.0 Sections 1–9 + Appendix returned.
- Verbatim: "Apache License Version 2.0, January 2004" / "Licensed under the Apache License, Version 2.0 (the 'License'); you may not use this file except in compliance with the License."
- Confidence: **CONFIRMED** for license-text claims (full text served, Apache 2.0, standard conditions, no Beam-specific extra clause in returned body).
- Limitation: Oct 7 creation / Oct 16 release day-dates in body prose are not evidenced by the LICENSE file content itself (needs repo commit/release page). Recorded as disclosed limitation, not a content revision.

## B54 — Vals independent evaluation (GLM-Legal)

- URL: `https://www.vals.ai/models/zai_glm-legal` (bib label `[独立評価]`, with printed caveat "方法・再現の限界つき").
- TeX claims: 19.17% · 7th of 79 · $0.15/test estimate · 72 min/test · LegalBench 86.23% (Fable 88.56); Z.ai chart omission is publisher choice, not evaluator omission.
- Fetch: SUCCESS. Model page with header card, benchmarks table, Updates prose.
- Verbatim: header "GLM Legal is an open-weight model from zAI, released October 12, 2026. Its best result is #7 of 81 on Harvey's Legal Agent Benchmark." / Updates "#7 of 79 on Harvey's Legal Agent Benchmark (19.17%) at $0.15 per test, the cheapest model in the top 10." / table "Harvey's Legal Agent Benchmark 19.17%±3.25, 7/81; LegalBench 86.23%±0.41".
- Confidence: **PARTIAL** (core anchor confirmed; drift documented below).
- Observations (disclosed, no silent revision; claim predates r29, matches r18 bytes):
  1. Denominator drift inside source: Updates prose `#7 of 79` vs header/table `#7 of 81` (leaderboard growth after issue window; TeX pins the 79 snapshot).
  2. Latency: TeX `1件72分` vs current card `Latency 37 min 25 s`. The 72-min figure is not found in the fetched excerpt — source drift or a different timing field (total vs per-test). Window-time page state cannot be re-fetched; retained as disclosed limitation.
  3. LegalBench: TeX 86.23% matches table (15/151); prose says 86.24% (#14 of 150) — minor display rounding/snapshot difference.
  4. Fable 88.56 comparison and chart-omission distinction require the Z.ai blog (B55) side-by-side; not confirmable from the Vals page alone.
- Materiality: must-cover P7 requires anchoring on the Vals result with chart-omission, regression, price, weights caveats — all hold (ranking, methodology disclosure, $0.15/test, printed limits). The latency detail is secondary; no must-cover breach. Non-blocking with disclosure.

## B57 — ASPIRE OSS release date/provenance

- URL: `https://github.com/NVlabs/ASPIRE` (bib label `[一次・発行者]`).
- TeX claims: Oct 16 repo publication (NVIDIA-owned Apache 2.0, third-party terms retained) is the week's event; June 30 paper (B56 `arXiv:2607.00272`) is background; announcement post is announcement, not proof of ownership.
- Fetch: SUCCESS. Repo exists (691 stars / 58 forks / 5 commits in fetched view); README News `[2026-10] ASPIRE v1.0 is out!` vs `[2026-06] ASPIRE is out!`; citation `arXiv:2607.00272` matches B56.
- Verbatim: "ASPIRE is a new type of continual learning: 'training' is skill refinement instead of gradient descent." / "[2026-10] ASPIRE v1.0 is out! ASPIRE can now solve a Rubik's Cube, and it achieves 99% success on 80 LIBERO-Pro Goal / Object / Spatial / Long tasks…" / "ASPIRE material owned by NVIDIA or contributed under the project license is available under the Apache License 2.0. Third-party materials retain their original terms."
- Confidence: **PARTIAL** (existence, license apportionment, June-vs-October split confirmed; day-precision disclosed below).
- Limitation: README shows month granularity `[2026-10]` only; no Oct-16 commit/release timestamp in fetched excerpt. The body's `10月16日` is window-consistent (in-window event, cutoff Oct 16 18:00 ET; the table states month-granularity `10月公開`). No separate ASPIRE X-post bib key exists in the 90 keys; the body's X-post sentence is announcement-discipline prose, not a dated-artifact citation. Recorded as disclosed limitation.

## Summary

| Key | Reachable | Core claim | Confidence |
|-----|-----------|------------|------------|
| B16 | Yes, full Apache 2.0 text | Full LICENSE = Apache 2.0, standard conditions | CONFIRMED (text); dates need repo page |
| B54 | Yes, model page + table + Updates | #7 / 19.17% / $0.15 / methodology | PARTIAL (anchor confirmed; 79/81 drift, latency field drift disclosed) |
| B57 | Yes, repo exists | Oct OSS release; June paper background; license split | PARTIAL (all structural claims confirmed; day-precision month-only) |

No concrete error requiring content revision was found; three bounded limitations are carried into formal review details as disclosed facts. No secondary paraphrase was substituted for any direct source.
