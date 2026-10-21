# W42 r30 L04 — 28 selected IDs → P1–P7 → Reader/TeX crosswalk

Scope: Sol disposition `W42-R29-L04` (LOW / TRACEABILITY). Method: `candidate-selection-v2.json` (28 SELECTED) × `architecture-v2.json` packages (primary/supporting IDs), spot-checked against TeX sections.
Date: 2026-10-20 JST. Worker: Muse (W42 r30 execution).

## Result: 28/28 mapped, 0 unmapped, 0 extras

| Package / Section | Role | Candidate (short) | Topic |
|---|---|---|---|
| P1 §フロンティアエージェント | PRIMARY | 7250cc3e8b36 | Frontier agentic family launch Oct 12 (Meta Wonder) |
| P1 | PRIMARY | bb9272a30e90 | Argon Global GA Oct 13 (1M output context, pricing) |
| P2 §推論の経済学 | PRIMARY | 9659dd683c56 | Hyperscaler silicon Oct 12 (Maia SDLA/NUMA/HBM4) |
| P2 | SUPPORTING | a79f0a6c53138 | Liquid AI LFM2.5-24B-A2B |
| P3 §オープンウェイト | PRIMARY | b7c4cf541cd78 | Muse Spark Open 816B-A42B MoE Oct 15 |
| P3 | PRIMARY | e188cdb3b910 | Reflection Beam 501B-A23B MoE Oct 16 |
| P3 | PRIMARY | d9bb954ecc5d0 | NVIDIA Nemotron 3.5 Super VL + Bolt |
| P3 | SUPPORTING | 778de6f30485 | IBM Granite Switch 4.1 Oct 14 |
| P3 | SUPPORTING | 78638c331f26 | OpenBMB MiniCPM-V 4.7 |
| P3 | SUPPORTING | 48361c0e84a0 | FLUX 3 Image Klein 5.6B |
| P4 §エージェント工学 | PRIMARY | dee80649da784 | OpenAI Codex GPT-6 maintenance practice |
| P4 | PRIMARY | 48528585077b | Anthropic Scion merges |
| P4 | PRIMARY | efe069fadbff | GitHub HydraFusion + Max orchestration |
| P4 | SUPPORTING | 1ec47d9f5640 | GitHub agentic autofix GA Oct 15 |
| P4 | SUPPORTING | 9fe5ee469de97 | GitHub AI Scan for PRs GA Oct 15 |
| P4 | SUPPORTING | d997b2fff60ac | Perplexity Decider v1.2 Oct 16 |
| P5 §安全性と透明性 | PRIMARY | 4e12f3a2f4b59 | Anthropic unintended-actions report Oct 9 |
| P5 | PRIMARY | c09819779a92 | Anthropic distillation defenses Oct 12 |
| P5 | SUPPORTING | a25b967858d26 | Claude ECDSA seed-origin mystery closure |
| P5 | SUPPORTING | 2e9e77e7d214c | METR employee-like evaluator access |
| P6 §科学エージェント | PRIMARY | 2ea6d2cbb7e9b | Google autonomous wet-lab building blocks |
| P6 | PRIMARY | b97b99b689ba | Google Earth AI Geospatial Reasoning agent |
| P6 | PRIMARY | 218deec1c05ee | Google Deep Review launch |
| P6 | SUPPORTING | 9a9366a65d344 | Rosalind discovery pricing listing |
| P6 | SUPPORTING | 8488f19293a65 | OpenAI Rosalind Academic Plan |
| P7 §専門・身体性 | PRIMARY | 07cca85d36bd | Z.ai GLM-Legal (Vals anchor) |
| P7 | PRIMARY | effbda250795 | NVIDIA ASPIRE robotics OSS Oct 16 |
| P7 | SUPPORTING | 0e7f72be6503 | Elorian Glimpse visual scratch space |

(Candidate IDs shown short; full form `candidate:2026-W42:<hex>`. Roles PRIMARY/SUPPORTING per `architecture-v2.json`; all 28 carry `SELECTED` disposition in `candidate-selection-v2.json` status ESTABLISHED.)

## Spot checks (materiality / citations / presence)

- ASPIRE (`effbda25…`, P7 PRIMARY): TeX table row + body Oct/background split + cites B57/B56/B89 — present.
- Beam (`e188cd…`, P3 PRIMARY): TeX table row + full-text claims + cites B17/B19/B18/B16 — present.
- GLM-Legal (`07cca85…`, P7 PRIMARY): TeX table row + Vals anchor + cites B55/B53/B54 — present.
- Decider (`d997b2…`, P4 SUPPORTING): TeX table T4 Decider row p12 + body v1.1 chain — present.
- No selected ID lacks a chapter home; no invented mapping (all bindings read from approved Architecture bytes).
