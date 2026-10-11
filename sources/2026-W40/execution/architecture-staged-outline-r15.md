# W40 staged Architecture outline r15 — boundary-anchored (NOT Architecture)

Status: STAGED_R15 / OUTLINE_ONLY / NO_ARCHITECTURE_ACCEPTANCE
Supersedes as working outline (r14 preserved immutable):
`execution/architecture-staged-outline-r14.md`
Authoritative inputs (unchanged bytes): Selection preview-r13 (SHA `dc024778…`,
28 SELECTED = 20P/8S) + r10 Matrix (SHA `f07b1166…`) + coverage-r14 (SHA `3de8bd56…`).
Boundary inheritance: `execution/architecture-boundaries-r15.json`
(SHA `1736737e…`; 28 entries, exact verbatim `remaining_boundaries`, no normalization)
+ `execution/architecture-boundaries-validation-r15.json` (status PASS: 113/113 literal
membership, missing 0; raw 113 vs dedup-unique 105; ephemeral in-memory PROPOSED run of
unmodified reviewed-main `validate_architecture` → 0 errors with disclosed placeholders).
This outline creates NO `architecture-v2.json`, NO checkpoint, NO State change, claims NO
Reader Manifest `architecture_coverage`, and spans NO page budget.
Package boundary arrays live EXACTLY in the SHA-bound JSON (per-package counts below);
this file references them rather than duplicating 105 strings (no paraphrase risk).

## Package map (roles + boundary references)

| Pkg | PRIMARY (exact IDs) | SUPPORTING (exact IDs) | boundaries: raw → unique (JSON ref) |
|---|---|---|---|
| P1 frontier-models | 50847d0a9 Sonnet 5.5; 34e0532a2 GPT-6.1 Sol; 2fc5e5025 Gemini 4 Argon | — | 12 → 12 (`packages.P1.boundaries`) |
| P2 open-reasoning | 6fa837285 Holo4; 61859ff02 ELYZA | — | 8 → 8 (`packages.P2.boundaries`) |
| P3 decision-inference | c779a6e34 Ollama; 230500269 Clef; f92f1c9c9 Strands | — | 13 → 13 (`packages.P3.boundaries`) |
| P4 devday-product-surface | 5e276e2fc Agents API; ebe4568ec dots | 74c6428e8 DevDay Hub (spine) | 11 → 8 (`packages.P4.boundaries`) |
| P5 safety-provenance | 1e165c26e ProvenanceGuard; 415837190 Open Agent Safety; 488969327 SynthID Bio | 30e4d9ba0 safety cases; 8479c9784 OAuth v1 | 19 → 17 (`packages.P5.boundaries`) |
| P6a training-methods-and-systems | 4368e1305 ContextLM; 24719b616 Olmo-core 3 | — | 10 → 10 (`packages.P6a.boundaries`) |
| P6b evaluation-and-execution-infra | 245268468 AgentPerf; cb642e557 OpenTTS | 08da5f196 RL-Env Hub (interop) | 15 → 15 (`packages.P6b.boundaries`) |
| P7 multimodal-serving-observability | 22bb2c7fa FLUX 3; 3f5be21c2 VSS 3.3; 6dd7c91d3 Nemotron ASR | 79687e931 NeMo Relay; db63bd8b3 Ross (embedded note) | 16 → 16 (`packages.P7.boundaries`) |
| P8 enterprise-industry-digest | — | 45d769ec1 World Labs; dcad0b509 AI Search | 6 → 6 (`packages.P8.boundaries`) |

(Full IDs: `candidate:2026-W40:` + suffix above; roles/usages byte-equal to Selection;
see coverage-r14 for architecture_role values.)

Totals: 28 placed / 28 SELECTED; PRIMARY 20 (P8 0); SUPPORTING 8.
Raw relationships 113; package-unique strings 105 (8 in-package identical-string
dedups: P4 −3, P5 −2; accepted de-dup, each explained as identical strings within one
package — no semantic substitution, no cross-package merging).
Zero HOLD/REJECT placed; zero invented IDs; Ross placed (P7 supporting).
P6a/P6b share `WEEKLY:training-eval-infra` with NO fictional split role — editorial
split within the existing role only.
COND-A AstaBrief / COND-B AutoSynthData: NON_CANONICAL HOLD, NOT in map/packages/boundaries.

## Content requirements per package (staging guidance, not canonical must-cover)

- P1 largest: per-vendor tables, cost-per-task frame; P2 large: generalist/JA halves +
  comparison table; P3 medium, axes separated; P4 medium, hub zero-headline spine;
  P5 medium, five independent subsections, never one "safety performance" claim;
  P6a/P6b medium-large, FULL depth reserved (see `technical-prep-r15/` r15 prose);
  P7 medium; P8 small digest. Every package at authorship: mechanisms + metrics WITH
  conditions + comparisons WITH limits + sources + inherited boundary strings HONORED
  (each boundary string must be visibly addressed where its package is drafted — the
  literal strings are the checklist).
- DGX Spark: evidence/background only, no package. W39 HOLDs: unplaced.
- Compression guard unchanged (28-item spine; re-baseline only post-supersession by Sol).
