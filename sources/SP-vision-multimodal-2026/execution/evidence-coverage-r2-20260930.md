# TS-003 r2 Evidence coverage — Sol Evidence Semantic Review r2 surface

Issue: `SP-vision-multimodal-2026` | Date: `2026-09-30 UTC` | Lifecycle: `CANDIDATES_NORMALIZED` (unchanged)

r2 input: `execution/evidence-semantic-repair-r1-20260930/evidence-interactive-input-r2.json` (111 records)
r2 acceptance: `evidence/v2/accepted/3f6be211.../evidence-accepted.json` (sha `d01bd6e3...`, 111 Cards)
r2 views: `evidence/v2/views/accepted/73c06689.../edition-views-accepted.json` (sha `512e4238...`, 111 Views)
r1 artifacts (`3b183719...`, `ed7ebf97...`) unchanged (immutable history).
Same canonical task package as r1; Discovery/Screening unchanged; no ledger/completeness/state advance.

## 1. Task coverage and statuses

111/111 tasks covered. Statuses: VERIFIED 106 / PARTIAL 5 (D001 paywall, D002 font-encoded PDF,
D076 data-release scope, D077 license mix, D111 paper depth) — identical counts to r1 by design
(no VERIFIED-count optimization; two records gained stronger bindings without status change).

Per-obligation counts unchanged from r1 (O01:4, O02:8, O03:6, O04:4, O05:10, O06:7, O07:5, O08:19,
O09:7, O10:17, O11:9, O12:9, O13:3, O14:9, O15:7, O16:12 via shared records).

## 2. Depth accounting (full-body / abstract / page / repo)

- Full paper bodies: 101 records (95 arXiv HTML + 6 proceedings/PDF bodies), findings name consumed sections.
- Abstract/page-level: D001 (Springer abstract), D111 (abstract + HF viewer).
- Encoding-barrier: D002 (LeNet PDF custom fonts; predecessor-context scope only).
- Repo/HF/vendor surfaces, re-verified live 2026-09-30: 10 records + 3 fresh license/API bindings
  (molmo2 LICENSE, Qwen3-VL LICENSE + HF tag, HF Molmo2-8B + Qwen3-Omni-30B tags with SHAs/dates).
- Aggregate accounting matches per-card semantics (§11 check: r2 aggregate == per-Card).

## 3. G01–G06 disposition (all preserved)

G01 independent VLA eval — UNRESOLVED. G02 control-oriented world-model bench — UNRESOLVED.
G03 same-protocol doc comparison — UNRESOLVED (NO_CROSS_MODEL_NUMERIC_COMPARISON stands).
G04 deployment latency beyond author-reported — UNRESOLVED. G05 independent reproduction — UNRESOLVED.
G06 SigLIP2 citation — UNRESOLVED (mechanism verified; exact citation still unbound; Molmo2 paper's
SigLIP 2 reference is a pointer, not the source).

## 4. Current source-role summary (post-repair)

Paper cards carry paper-supported facts only; repo cards carry deployment/license facts with exact
bindings (SHAs/dates); vendor/card/blog cards remain role-capped with vendor attribution.
License posture after repair: Qwen3-VL weights+code Apache 2.0 (bound); Molmo2 weights+code
Apache 2.0 (bound), data available with per-dataset terms unbound (PARTIAL); Qwen3-Omni weights
license:other (bound correction), code unbound. No architecture inferred from pages/demos.
No cross-condition ranking constructed. D07A/D07B, streaming/offline, four-pole, TS boundaries intact.

## 5. Validation

- §11 semantic checks: 44/44 PASS (bindings, attribution, zero PRIMARY_FACT, lineage, gaps).
- Canonical per-card validation against task authority: 111/111 PASS (build time).
- r2 acceptance re-validation + views acceptance validation: PASS (see session receipts).
- r1 acceptance/views re-validated unchanged.
