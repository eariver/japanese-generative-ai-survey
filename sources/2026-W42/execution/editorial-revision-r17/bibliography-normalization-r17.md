# W42 r17 bibliography normalization (90 keys, 19 aliases, B74 repair)

Date: 2026-10-18. Base: `bibliography-map-r16.json` (90 keys). Output: `bibliography-map-r17.json` (90 keys, invalid=0), `bibliography-duplicate-matrix-r17.json`, `citation-repair-ledger-r17.json` (177 rows, invalid=0).

## 1. URL syntax validation (parser, not startsWith)

Validator: `urllib.parse.urlparse` — scheme in {http,https}, hostname non-empty, no whitespace, trailing commentary rejected. All 90 map URLs + all ledger `narrowed_source_urls` checked.

- r16 invalid in map: B74 `https://github.com/OpenBMB/MiniCPM-V (via @OpenBMB X 2026-10-12)` (whitespace/parens).
- r16 invalid in ledger (5 patterns, 38 instances): B74 same; B73 `https://huggingface.co/blog/ibm-granite/granite-switch-4-1 + card …`; B69-series `https://liquid.ai/blog/lfm2-5-24b-a2b (via X)` (12 instances); B86 `https://developers.openai.com/api/docs/pricing (Life sciences section)`; B88 `https://openrouter.ai/elorian/glimpse Source: …`.
- r17: map invalid 0/90; ledger invalid 0/177. B74 bare + `locator_note: via @OpenBMB X 2026-10-12` + `provenance_note`.

HTTP: 7 key critical sources tested 2026-10-18 via curl (all 200): Maia blog (333,115B), LFM license (179,469B), Minecraft arXiv (108,772B), MiniCPM-V repo (363,809B), LFM blog (1,831,956B), Nemotron blog (128,710B), LFM HF card (281,618B). Remaining 83 keys parser-valid only, reachability `UNVERIFIED` — never claimed 90/90 HTTP.

## 2. Duplicate normalization (19 pairs)

Normalization: lowercase host, strip leading `www.`, strip single trailing slash (root preserved), preserve path case, ignore empty query/fragment (none present). All 19 pairs identical post-normalization — genuine aliases, not distinct snapshots.

| canonical | alias | normalized identity |
|---|---|---|
| B01 | B62 | https://about.fb.com/news/2026/10/introducing-muse-wonder-models |
| B05 | B65 | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon |
| B11 | B69 | https://liquid.ai/blog/lfm2-5-24b-a2b |
| B20 | B72 | https://blogs.nvidia.com/blog/nemotron-3-5-super-vl |
| B24 | B73 | https://huggingface.co/blog/ibm-granite/granite-switch-4-1 |
| B32 | B75 | https://anthropic.com/engineering/redesigning-source-control |
| B33 | B76 | https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option |
| B34 | B77 | https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability |
| B35 | B78 | https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available |
| B39 | B82 | https://anthropic.com/news/an-update-on-independent-evaluators |
| B40 | B79 | https://anthropic.com/news/investigating-unintended-model-actions |
| B41 | B80 | https://anthropic.com/research/distillation-defenses |
| B42 | B81 | https://anthropic.com/research/ecdsa-curve-origins |
| B43 | B83 | https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs |
| B48 | B84 | https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges |
| B50 | B85 | https://research.google/blog/analyzing-technical-documents-with-deep-review |
| B51 | B86 | https://developers.openai.com/api/docs/pricing |
| B52 | B87 | https://openai.com/index/introducing-the-rosalind-academic-plan |
| B59 | B88 | https://openrouter.ai/elorian/glimpse |

All 90 Bxx keys retained; alias entries carry `alias_of` + `locator_note`; 177 ledger rows retained with bare URLs.

## 3. Category reconciliation

- B62/B65: r16 SECONDARY while same first-party page as B01/B05 — classification error. r17: 一次・発行者 (same as canonical) + note “prior SECONDARY tag was classification error, reconciled r17”.
- B88: r16 一次・発行者 while duplicate of B59 二次・参考 (OpenRouter aggregator) — r17: 二次・参考 + alias_of B59 + “vendor numbers relayed via secondary press”.
- Others: canonical categories preserved (一次・発行者 / 論文 / 二次・参考 / 独立評価).

## 4. Reader display plan (no invented metadata)

Per-entry: `[publisher/author — kind]` + clean `\url{}` link; alias entries: `→ Bxx を参照（同一URL …）` with no duplicate URL print. Publisher labels grounded (e.g., “Meta — 発行者ページ”, “Faldor et al., arXiv 2610.22319 — 論文”, “Hugging Face API — モデルAPI参照”); unverified titles marked via site/publisher label, never invented. B74 shows `(2026) — リポジトリ — via @OpenBMB X 2026-10-12 (…)`. B89/B90 show section/figure-value caveats. Citations `\cite{Bxx}` unchanged; no dropped claims.

Printed count: 90 logical keys = 71 canonical prints + 19 alias cross-refs. No orphan aliases. TeX print rules: `alias_of` entries use cross-ref text (underscores sanitized to hyphens for LaTeX); URLs only inside `\url{}` (xurl wrapping).

## 5. Preserved source trace

Earth 220/210 + 44/45, NVIDIA MTP acceptance length, wet-lab 131/311 vs 8-clone, W42 cutoff, license tiers, vendor-vs-independent attribution — all held. No unsupported interpretation via dedupe.

## 6. Files

- `bibliography-map-r17.json` (SHA to be recorded at commit)
- `bibliography-duplicate-matrix-r17.json`
- `citation-repair-ledger-r17.json`
- TeX `thebibliography` generated from map (see `diagnostic-r17/main.tex` §§出典一覧)
