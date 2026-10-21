# W42 r12 change ledger (Sol R11 F01–F03 + D refinements closure)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-18 JST
Old: `execution/editorial-revision-r11/proposals/*/draft-result-r11.PROPOSED.json` (v11.0, 82 paras / 20,082 chars)
New: `execution/editorial-revision-r12/proposals/*/draft-result-r12.PROPOSED.json` (v12.0, 92 paras / 21,281 chars, 7 tables / 7 notes)
Method: r11 base retained block-for-block except listed repairs; new sequential `rN-##` IDs in flow order; `block-diff-r11-r12.json` maps every ID.

## F01 — LFM license level + Beam Apache conditions — RESOLVED
- P2 `q2-07` rewritten: LFM terms are now `発行者サイトで公開された主要条項` with explicit `対象モデルのLICENSE原文ファイルおよび24B個別重みの確認は未了`; tier explicitly distinguished from both tag-only and Beam full-file levels.
- P3 `q3-03` rewritten: no custom Built-with badge obligation, BUT ordinary Apache 2.0 conditions preserved (license-text reproduction, copyright/attribution/NOTICE retention, changed-file notice, patent terms, third-party terms). Removed blanket `表示義務がない`.
- P3 `q3-t1` Beam row rewritten to the bounded form; `q3-n1` already correct (OSI status of the license text vs per-model coverage) and left aligned; `q3-02` gained the artifact-scope qualifier (`個別配布物や第三者部分への適用は別途確認`).
- Consistency swept across P2/P3 tables, notes, and license passages; no independent-legal-review claims; no OSI claim for bespoke licenses.

## F02 — seven bad source URLs + one latent — RESOLVED
- Root cause: three accepted-card INFERENCE claims (ai-scan C3, metr C3, rosalind-plan C3) plus wetlab C5 carry a local r6 bundle path as claim `context` (editorial-derivation provenance, content-mismatched with the citing subject). r11 ledger harvested contexts verbatim → 7 rows listed non-http bundle paths.
- Fix: resolver-level exclusion of all four bundle-sourced refs from every r12 proposal block; `narrowed_source_urls` now 100% external http(s) (programmatic scan: zero non-http rows of 106).
- Affected text handled without deleting support: `q4-07/q4-08` keep product-doc refs (non-conflation guidance is now explicit editorial synthesis on cited docs); `q5-06/q5-10` keep announcement refs (zero-outcome stance explicit); `q5-08` converted to `attribution NONE` editorial framing (no external refs); `q6-06` Nipah sentence converted to explicit editorial non-use stance on the announcement ref.
- `internal_provenance_paths` left empty: no internal path content matched any citing clause, so nothing qualified for retention.

## F03 — density — ADDRESSED (proof via TeX layout in Phase B)
- +10 source-backed paragraphs: P2 hardware efficiency ×2 (prefill/decode separation +167kW ops; incomparability methodology), P4 Scion design ×2 + Decider format ×1 (WAL/derived-data role; API-query/sparse-checkout ops), P5 method comparison ×2 (three independence forms; defense bundle+admitted bypass), P6 denominators ×2 (VERID calibration meaning; autorater-limits/unexecuted-publication handling), P7 eval/failure-modes ×2 (frozen-frontier dependence implication; direct-action boundary).
- Volume: 92 paragraphs + 7 tables + 7 notes ≈ 21.3k body chars. No padding (each addition resolves a Sol-listed thin spot). Page feasibility is measured from the actual TeX proof, not estimated here.

## D refinements
- Closings rewritten without formulaic endings (`q2-10`, `q5-07`, `q7-07`); P3 headline/HEADING de-duplicated (`条件の違いが実装の可否を決める`); r12 IDs sequential in narrative order (old `qN-12/13-after-closing` ordering eliminated).
- `SRFT` retained once (`q3-08`) as a named fine-tuning method per B04's named-term allowance; documented here as the single accepted exception.

## Coverage / dispositions (validator-enforced, 7/7 PASS)
- must_cover mapped to explaining blocks only (no blanket); boundaries EXPLICITLY_STATED with preserved rationale; frozen `draft-check` 7/7 PASS; `synthesis-check` PASS on proposed pair-built input.
