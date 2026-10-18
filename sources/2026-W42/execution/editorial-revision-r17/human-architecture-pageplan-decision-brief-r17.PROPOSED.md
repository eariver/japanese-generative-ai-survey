# Human Architecture page-plan decision brief r17 (PROPOSED / DRAFT ONLY — no approval authority)

Date: 2026-10-18 JST. Author: Muse (execution). Status: `PROPOSED / NONCANONICAL / NO_HUMAN_VOTE`. For Sol vetting and later Human decision after narrow independent r17 closure audit. This brief has no approval authority. Official `architecture-v2.json` and Human r1 approval unchanged.

## 1. Fixed approved allocations (unchanged)

- Architecture `architecture-v2.json`: P1 4.0 / P2 2.5 / P3 5.0 / P4 4.0 / P5 3.0 / P6 4.5 / P7 3.5; body 26.5pp; magazine target 28 / max 30. 7 packages / 28 selected (PRIMARY16+SUPPORTING12). Human Architecture r1 APPROVED (r1 review record + immutable snapshot + State `approved`; Publication Preview `pending`).
- No unilateral change by Muse. Any target revision requires Human re-gating via frozen Core `survey_human_gate_v2` authority confirmation (see §5).

## 2. Measured actuals (r16 original vs r17 repaired)

Method: parser-read PDF pages + text-length per page + two-column flow inspection (no double counting; tables counted in hosting chapter; cover/bib separate; effective-area range accounts for tables/notes/boxes).

|  | r16 diagnostic | r17 diagnostic |
|---|---|---|
| Total | 21pp, 506,978B, SHA `e2919ec9…` | 21pp, 512,182B, SHA `6b673a93…` (deterministic, final two byte-identical) |
| Cover | p1 (1pp) | p1 (1pp) |
| Body physical | p2–p18 (17pp; p18 Table-7-only sparse ~1/4) | p2–p17 (16pp; Table-7 p17 in-body with text, no orphan) |
| Bibliography | p19–p21 (3pp, dense raw URLs) | p18–p21 (4pp, publisher/kind/link + 19 alias cross-refs) |
| Effective body | ~15.5–17 (tables/notes/boxes discounted) | ~15.5–17 (same methodology; net +253 chars editorial precision, P6 −64 dedup; no padding) |
| Chapter ranges (approx, flow) | P1 p2–4, P2 p4–6, P3 p6–9, P4 p9–12, P5 p12–13, P6 p14–15, P7 p15–18 (Table-7 p18 orphan) | P1 p2–4, P2 p4–6, P3 p6–9, P4 p9–12, P5 p12–13, P6 p14–15, P7 p15–17 (Table-7 p17 in-body) |
| Table/footnote overhead | 7 tables + 7 notes + 7 claim boxes (excluded from reader) | same (content unchanged; Table-7 moved, not deleted) |
| Unresolved source constraints | aptamer Methods blocked; ASPIRE figure values unresolved; Earth SHA unknown; Vals methods unobtained; etc. (see closure matrix) | same (F16-08 bounded alternate attempted, Range ignored; all held, no invention) |

Gap: approved body 26.5 vs measured effective ~15.5–17 → ~9.5–11pp shortfall. Approved total 26.5+4=30.5 vs magazine max30 — quantitatively over target even before content gap. Prior 9,400-char / 6–7pp point estimates remain retracted as invalid exact claims.

Table-7 improvement separated from shrinkage: r17 body physical −1pp vs r16 is orphan elimination (p18 sparse) + bib +1pp (readability), not content loss (paras 136→136, chars +253).

## 3. Does content meet reader technical goals (per chapter, irrespective of 26.5)?

- P1 (frontier execution): Yes — Wonder/Argon definitions, pricing/distribution, Minecraft conditions/costs/limits, failure modes; denominators + single-run limits explicit. Depth sufficient for “conditions bundle” reading.
- P2 (inference economics): Yes — Maia circuit inventory + applicability conditions (full-96-config, 750GB/s band, Ignite), LFM bench temps + license operative scope (§§1/4/5/11, $10M entity, §5(c) qualified, per-artifact gap); vendor-vs-baseline discipline held. No independent reproduction (honestly marked).
- P3 (open weights): Yes — Spark/Beam/Nemotron + Granite/MiniCPM/FLUX对照, license tiers (FILE vs TAG vs MaaS-gate vs OpenMDW-gap vs Kommunity), MTP length, Bolt dating. B74 repaired.
- P4 (engineering): Yes — Codex practice vs cost ledger, Scion data/control planes distinct, HydraFusion/gates, Decider calibration. No new boilerplate.
- P5 (safety): Yes — 4局面 (disclosure/defense/explanation/access) separated, distillation efficacy vs adversary TPP vs durability ledger vs calibration distinct, ECDSA/METR boundaries. No padding.
- P6 (science): Yes — Earth 4×2 + GeoKTools/Table-5 negatives preserved (deduped, not deleted), wet-lab denominators separated, Deep Review SPOT, Rosalind conditions. Methods blocked honestly.
- P7 (specialty/embodiment): Yes — GLM-Legal Vals anchor + chart-omission, ASPIRE dating/real-robot design (figure values unresolved), Glimpse mechanism + HSS negative + comparability (deduped). Table-7 in-body.

Conclusion: substantive reader goals met at current density; shortfall is pagination vs 26.5 plan, not technical thinness requiring padding. Additional pages without new primary evidence would be padding (prohibited).

## 4. Options

### Option A — retain current targets (26.5 body / 28 target / 30 max)

Requires specific new original evidence (no padding):

- Aptamer Methods full thresholds (PDF >5MB accessible via alternate host/range; currently Range-ignored).
- ASPIRE interactive figure values (real-robot tokens/success cells).
- Earth repo commit SHA + withheld test splits (currently 1 commit/SHA unknown, tests withheld).
- Vals GLM-Legal full methods + rate card.
- Maia paper/baseline details (Maia-200 reference).
- Nemotron technical-report PDF bytes (currently URL only).
- HF per-artifact LICENSE files (24B individual weights).
- METR downstream results; independent reruns of any vendor bench.

Viability: low in short term (all currently inaccessible/withheld/unpublished per r16 A1–A8 + r17 F16-08 attempt). If obtained, added pages would be source-supported (methods, ablations, cross-tables), not padding. Risk: chasing length delays publication; sources may remain inaccessible (single-run, vendor-only, unreleased reports).

### Option B — provisional per-chapter reallocation preserving all 28 + 7 chapters (RECOMMENDED as proposal, Human decides)

Defensible provisional total anchored to measured r17 density (no padding, no scope cut):

- Body provisional ~16–17 (effective ~15.5–17 measured) + cover1 + bib4 = total ~21–22 (vs magazine target28/max30; magazine format would carry whitespace or additional non-article matter outside survey scope — not proposed here).
- Indicative per-chapter provisional (body-physical, tables included, rounded from measured flow; sums to 16.5):
  P1 2.5 / P2 2.5 / P3 3.0 / P4 2.5 / P5 2.0 / P6 2.5 / P7 2.0 = 17.0 (range 16–17 allowing float placement).
- Preserves all 28 selected, 7 technical chapters, must_cover/boundaries, source dates/certainty. No rescope, no deletions.
- Trade-off: magazine target28 not met by article body; non-article pages (editorial, ads, TOC) outside survey authority could fill magazine signature — Human/publishing decision, not survey content padding.
- Residual risk: provisional total still below 26.5 plan; requires Human Architecture amendment (see §5), not automatic.

### Option C — structural scope revision

Only if compelling newly documented reason (e.g., post-cutoff retraction, source invalidation, Human strategic reprioritization). r17 found none: 28 remain material, 7 packages technically coherent, no retractions. NOT recommended. If invoked, requires full Sol/Human evidence review, not editorial execution.

## 5. Human approval / re-gating mechanics (authority confirmation required, not forged)

- Current authority: Human Architecture r1 APPROVED (gates/architecture-approval.json + reviews/architecture-r1.json + approvals snapshot + review-index.json + State human_gates.architecture_review=approved). Publication Preview pending.
- Option A (retain): no Architecture change; needs Sol r17 closure audit PASS + Human Publication Preview decision via frozen `survey_human_gate_v2` (not execution). If new evidence later supports added pages, a bounded supplement + re-render + re-audit precedes Preview.
- Option B (provisional reallocation): amends approved page allocations (not topics/selection). Requires Human Architecture amendment (new review record, immutable snapshot, State update) via frozen Gate CLI + human decision (APPROVED/REQUEST_CHANGES per governance; silence ≠ approval). Muse/Sol cannot approve on Human’s behalf. Downstream: updated Architecture → new Reader/Publication path via Core QA gates (not diagnostic).
- Option C (rescope): requires full Architecture re-establishment (Selection → Architecture → Human Review) via frozen Core, not edition-local edit.
- No VALIDATED_DRAFT, Reader, Publication Preview, Freeze, Release, or Human Gate action taken in r17. All r17 artifacts NONCANONICAL.

## 6. Recommendation (non-binding)

Adopt Option B as provisional planning basis IF Human judges 26.5 unachievable without padding (r17 evidence strongly suggests so), preserving 28/7 and technical integrity, with magazine signature filled outside article scope. Otherwise Option A with explicit acceptance that 26.5 remains aspirational pending listed primary evidence (no padding in interim). Sol to vet measurement methodology; Human to decide after independent r17 closure audit.
