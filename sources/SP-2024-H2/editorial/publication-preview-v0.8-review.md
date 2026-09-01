# SP-2024-H2 Publication Preview v0.8 — pre-Human-Gate review

Status: READY FOR HUMAN GATE 2 REVIEW

PDF build workflow: 31858197515
PDF pages: 41
PDF SHA256: `8f2e7e34b71237840de67dae035e64f42b73a92fe3cb17adc3ce050f4a2e807b`
Source version: v0.8
Source manifest SHA256: `5c7b6eb4a475bd13b77ce44e1c6c13eec0fe40fd71ea0afad82e43b23995cf75`

## Human Visual Review findings addressed

- #139: 68 visible Technical Notes cards use event-bounded accepted Screening provenance for source-specific technical detail. Legacy generic fallback phrases are 0 hits. Thin provenance fails closed; one selected GPT-4o mini card is reader-facing suppressed rather than fabricated, and hash-bound overrides are used for the explicitly reviewed thin cases.
- #128: independent reader-facing layers exist for Half-year Reclassification, Cross-month Comparison, and Cross-layer Synthesis before the final Half-year Synthesis.
- #153: Detailed Chronology is a compact dated 8-event list with item-level source mapping; it does not reprint full Technical Notes cards.
- #140: repeated `Primary source used for chronology and technical verification.` bibliography boilerplate is 0 hits; References purpose is stated once.
- #54: `安全性事象` is 0 hits; reader taxonomy distinguishes e.g. `Alignment研究` and `安全性手法`.
- #172: corrupted `モデル_CARD.md` is 0 hits. PDF annotation inspection found 184 external URI annotations, 0 non-ASCII URI targets, and the Llama 3.3 target remains `.../MODEL_CARD.md`.

## Build and visual QA

Strict source preflight, LuaLaTeX compilation, TeX log/page gate, and PDF build gate all passed. All 41 rendered pages were visually inspected. No clipped text, overlapping content, broken glyphs/black boxes, URL overflow, orphaned TOC continuation, or boilerplate-only isolated final page was observed.

This review does not authorize Visual Review acceptance, Freeze, work-PR merge, or public release. Those remain gated by explicit Publication Preview Human Gate 2 approval.
