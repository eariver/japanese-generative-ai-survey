# W41 supplement access-provenance ledger r5 (SC-E41-06)

Precision: all `accessed_at` below are **BUNDLE_WINDOW_ESTIMATE / PER_PAGE_UNKNOWN**.
The r3 retrieval ran 2026-10-12 ~00:33–00:40Z in four bundle windows (A-openai, B-google/anthropic, C-openweights, D-direct). No per-page HTTP access log exists; per-page minute precision is NOT demonstrated. Schema-required `accessed_at` carries the bundle-window instant; this ledger is the visible caveat. No per-page exact fetch clock is claimed. All raw files are **BOUNDED_EXCERPT** (bounded verbatim quotes + reviewer PROVENANCE header/NOTEs), not full-byte HTML/PDF.

| supplement_source_id | task (discovery) | locator | raw file (SHA/bytes) | accessed_at (label) | capture |
|---|---|---|---|---|---|
| supplement-src-360435193adc7df6 | w41-x-nanobanana21-20261006 | deepmind.google model card | nanobanana-model-card-r4… (see manifest) | 2026-10-12T00:36:00Z BUNDLE_WINDOW_ESTIMATE | DELEGATED verbatim |
| supplement-src-bd822c4689ba127c | w41-dailyx-synthid-portal-20261008 | blog.google synthid post | synthid-blog-r4… | 2026-10-12T00:36:00Z BUNDLE_WINDOW_ESTIMATE | DELEGATED verbatim |
| supplement-src-4ab03c9b7af83795 | w41-dailyx-nace-drex-20261010 | nace.ai/drex + blog | nace-drex-docs-r4… | 2026-10-12T00:37:00Z BUNDLE_WINDOW_ESTIMATE | DELEGATED verbatim |
| supplement-src-c10ede7c23828f99 | w41-primary-mistral-large4-20261006 | docs.mistral.ai + blog | mistral-docs-pin-r4… | 2026-10-12T00:37:00Z BUNDLE_WINDOW_ESTIMATE | DELEGATED verbatim |
| supplement-src-1fa2e6b4e1db612f | w41-primary-embeddinggemma2-20261006 | blog.google egemma post | embeddinggemma-blog-r4… | 2026-10-12T00:36:00Z BUNDLE_WINDOW_ESTIMATE | DELEGATED verbatim |
| supplement-src-d6dd5c50f1794c7d | w41-dailyx-textgrain-20261006 | openai.com eu-text-provenance | textgrain-blog-r4… | 2026-10-12T00:38:00Z BUNDLE_WINDOW_ESTIMATE | DIRECT_READ (Muse r3) |
| supplement-src-df537ff932f91343 | w41-primary-decisions-beta-20261006 | developers.openai.com changelog | openai-changelog-oct68-r4… | 2026-10-12T00:38:00Z BUNDLE_WINDOW_ESTIMATE | DIRECT_READ (Muse r3) |
| supplement-src-ec5b609a5f24671e | w41-primary-ultrafast-sol-20261008 | developers.openai.com changelog | openai-changelog-oct68-r4… | 2026-10-12T00:38:00Z BUNDLE_WINDOW_ESTIMATE | DIRECT_READ (Muse r3) |

Negative-search note (Nano Banana): "no matching blog.google 2.1 rollout post located among issuer pages checked" is a labeled negative-search observation (2026-10-12), NOT exhaustive web-wide proof; the model card is positive evidence only.
textGrain method note: method-level paper assertions restricted to blog-documented facts; technical-report internals unverified (PDF binary-unparsed).
