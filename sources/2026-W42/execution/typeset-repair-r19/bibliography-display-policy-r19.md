# W42 r19 bibliography display policy (print-only; authority unchanged)

Authority (evidence, immutable): `editorial-revision-r18/bibliography-map-r18.json` (90 keys, 19 `alias_of`, categories), `bibliography-duplicate-matrix-r18.json`, `citation-repair-ledger-r18.json` (177 rows). r19 changes NOTHING in authority; all print cleanup lives in `typeset-repair-r19/bibliography-display-map-r19.json` + TeX `thebibliography` rendering below.

## Print rules

1. Every logical Bxx key keeps exactly one printed entry (90 printed entries; Bxx citation targets intact; 177 ledger rows untouched).
2. Full entries (71): `[ publisher — kind ]: clean \url{}` + optional concise significance note. No invented author/year/title; unverified titles use grounded site/publisher labels (e.g., `Hugging Face API — モデルAPI参照`).
3. Alias entries (19): `[Bxx] publisher — kind → [Byy]（同一資料）` + optional significance note. No duplicate URL print; no machine mechanics in print. Canonical publisher/kind shown so the reader knows what the duplicate is.
4. Banned from print: `alias-of`, `www/trailing-slash normalization`, `identical source snapshot`, prior SECONDARY reclassification history, `see ledger`, `card part duplicates … context`, raw X/HTTP retrieval notes (`via X mention`, `via @OpenBMB X …`, `Life sciences section`, `Source: (via secondary press…)`), English audit parentheticals.
5. Kept in print (source-significance only, concise Japanese):
   - B38/B59/B88 OpenRouter: 集約掲載であり独立の測定/再現ではない（B88 additionally: 仕様は発行者ブログに依る is in body; print keeps the aggregator warning).
   - B54 Vals.ai: 本号唯一の真正な独立評価者URL（方法・再現の限界つき）.
   - B89 GEAR/ASPIRE page: 対話図中の数値は本文から読めず未取得.
6. Entry keep-together: `\needspace` before long-URL entries at risk of page-top orphan fragments (B28 applied in r19; B57 kept from r18). No font shrink, no margin/width change, no forced whitespace beyond single entry-level penalties.
7. URL validity: all 71 printed URLs are the authority bare URLs (parser-valid 90/90 in r18; display map references them by key, no retyping).

## Trace example

- Logical `B72` → authority URL `https://blogs.nvidia.com/blog/nemotron-3-5-super-vl` (= B20 normalized) → display `[B72] NVIDIA — 発行者ブログ → [B20]（同一資料）`. Original URL recoverable from authority map; no information discarded.
- Logical `B74` → authority bare `https://github.com/OpenBMB/MiniCPM-V` (+ sidecar `locator_note: via @OpenBMB X 2026-10-12`) → display `[B74] OpenBMB GitHub — リポジトリ: <clean link>` (retrieval note in sidecar only).
- Logical `B88` → alias of B59 → display `[B88] OpenRouter — モデル掲載 → [B59]（同一資料）集約掲載であり独立の再現ではない`.

## Pagination effect

Alias entries are shorter than full URL prints; total bibliography may shrink vs r18 4pp. Actual pages re-measured after build (not presumed).
