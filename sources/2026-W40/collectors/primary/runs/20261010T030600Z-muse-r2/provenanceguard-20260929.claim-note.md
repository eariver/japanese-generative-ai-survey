# CLAIM NOTE (derived) — ProvenanceGuard (Sep 29)

- artifact_class: CLAIM_LEVEL_DERIVED_NOTE
- companion_excerpts: [`provenanceguard-20260929.source-excerpt.md`]
- read_status: READ (full page 2026-10-10T03:06:46Z)
- event_date_basis: DAY ONLY "September 29, 2026" (HF team blog); original paper arXiv 2606.18037 published Aug 27 (pre-window) -> blog is the W40 event, NOT the paper. Do not cite team blog as independent result.

## Consumed claims

1. EVENT: Multiverse Computing published team-blog exposition of ProvenanceGuard Sep 29, 2026: source-aware factuality verification for MCP agents (per-claim source routing + NLI support + attribution check + allow/block + RARR repair). Paper itself is Aug 27 pre-window. (PRIMARY_FACT: blog publication, day only)
2. METHOD (as described): post-generation layer on black-box MCP traces; MiniLM routing + DeBERTa NLI + local LM decomposition; literal value checks; calibrated block; RARR repair. Local-config evaluation, adaptable to hosted. (VENDOR_CLAIM as method description)
3. RESULTS (paper-reported, team-blog relayed): 281 traces / 361 held-out claims; 138/139 should-block caught, 67 supported held; source-ID 86%; reject-F1 0.802 vs MiniCheck 0.783 / RAGAS 0.758 / AlignScore 0.662 / SummaC 0.436; similar-source 0.846 block-F1 / 50.3% exact-source; 50/50 attribution-swap caught; repair 173 blocked (144 fallback) / 59 (2 fallback); ~0.5s/answer. (PAPER_CLAIM relayed by team blog; original paper + protocol checks still needed per Sol)
4. ADOPTION (vendor-stated): NVFlow PR#9 merged optional grounding stage; Berkeley poster. (VENDOR_CLAIM)

## Boundaries

- Team blog is NOT independent validation; original paper/experimental protocol not consumed here. Material agent retrieval/provenance lead (discovery, not selection).
- Date DAY ONLY -> published_at NULL + DATETIME_NOT_PROVEN.
