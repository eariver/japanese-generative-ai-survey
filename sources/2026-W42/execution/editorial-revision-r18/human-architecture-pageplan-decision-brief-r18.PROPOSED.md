# Human Architecture page-plan decision brief r18 (PROPOSED / DRAFT ONLY — no approval authority)

Date: 2026-10-18 JST. Author: Muse (execution). Status: `PROPOSED / NONCANONICAL / NO_HUMAN_VOTE`. For Sol vetting and later Human decision after independent r18 closure audit. Supersedes r17 brief (which contained the S17-02 arithmetic error); r17 file retained unchanged as history. Official `architecture-v2.json` and Human r1 approval unchanged.

## 1. Fixed approved allocations (unchanged)

- Architecture `architecture-v2.json`: P1 4.0 / P2 2.5 / P3 5.0 / P4 4.0 / P5 3.0 / P6 4.5 / P7 3.5; body 26.5pp; magazine target 28 / max 30. 7 packages / 28 selected (PRIMARY16+SUPPORTING12). Human Architecture r1 APPROVED (record + snapshot + State `approved`; Publication Preview `pending`).
- No unilateral change by Muse. Any revision requires a new Human decision (see §5).

## 2. Measured actuals (r18 diagnostic; r16/r17 history kept distinct)

Method: parser-read PDF pages + per-page text lengths + two-column flow inspection. Tables counted once in hosting chapter; cover/bib separate; effective range discounts tables/notes/boxes. Chapter spans are flow estimates, not double-counted.

|  | r16 (history) | r17 (history) | r18 (current) |
|---|---|---|---|
| Total (measured) | 21pp, 506,978B | 21pp, 512,182B | 21pp, 511,523B, SHA `d42510f9…` (deterministic, final two byte-identical) |
| Cover | p1 (1pp) | p1 (1pp) | p1 (1pp) |
| Body physical | p2–p18 (17pp; p18 Table-7-only sparse) | p2–p17 (16pp; Table-7 p17 in-body) | p2–p17 (16pp; Table-7 p17 in-body kept; S17-01 text fixes −70 chars) |
| Bibliography | p19–p21 (3pp, raw URLs) | p18–p21 (4pp, publisher labels + alias cross-refs) | p18–p21 (4pp; B57 kept together on p20 via needspace; B28 4-char wrap noted) |
| Effective body | ~15.5–17 | ~15.5–17 | ~15.5–17 (same method; leak removal only) |
| Chapter flow (approx) | P1 p2–4 … P7 p15–18 | P1 p2–4 … P7 p15–17 | P1 p2–4, P2 p4–6, P3 p6–9, P4 p9–12, P5 p12–13, P6 p14–15, P7 p15–17 |

r18 changes vs r17: 3 paragraphs decontaminated (t1-23/t6-08/t7-19), 136 paras kept, 25,085→25,015 chars. No content added or deleted beyond internal-note removal.

## 3. Corrected conditional arithmetic (S17-02 fix)

- r17 brief error: stated cover1 + bib4 yet computed `26.5+4=30.5` (cover dropped). Corrected here.
- Correct conditional: **IF** the approved 26.5 body pages were rendered **AND** the r18-observed cover+bibliography allocation (1+4) persisted, the hypothetical total would be `26.5+1+4=31.5` physical pages. This is a conditional extrapolation, NOT a rendered PDF (measured r18 total is 21).
- r16 historical comparison kept distinct and true: `26.5+1+3=30.5` for its observed nonbody split (cover1+bib3).
- target28/max30 remain approved; the 31.5 hypothetical exceeds max30 by 1.5pp — stated explicitly. Bibliography restyling (labels + alias cross-refs: r16 3pp → r17/r18 4pp) can move future counts; acknowledged.
- Physical (16pp body) vs effective (~15.5–17) never mixed; gap to 26.5 plan is ~9.5–11pp effective shortfall (point estimates retracted as exact claims, same as r17).

## 4. Reader sufficiency per chapter (unchanged verdicts, leak-free prose)

P1 frontier execution / P2 inference economics (ONE pod, 750 GB/s scope; Legal-Entity $10M, §5(c) qualified) / P3 open weights / P4 engineering / P5 safety 4局面 / P6 science (GeoKTools/Table-5 negatives kept; 131/311 vs 8-clone separate) / P7 specialty (Vals anchor, ASPIRE dating + figure UNKNOWN, Glimpse comparability) — all meet reader goals at current density without padding. S17-01 removal did not delete findings.

## 5. Options (no preference selected; Human decides after audit)

### Option A — retain current targets (26.5 body / 28 target / 30 max)

Needs specific new primary evidence (same list as r17; none obtained in r18 by design — no broad research): aptamer Methods thresholds, ASPIRE figure values, Earth SHA/withheld splits, Vals methods/rate, Maia baseline, Nemotron PDF bytes, HF per-file LICENSEs, METR downstream, independent reruns. Viable only if sources become accessible; otherwise gap persists. Risk: delay without new pages; no padding in interim.

### Option B — provisional reallocation preserving 28/7 (sums verified)

Indicative provisional body 16–17 (measured) + cover1 + bib4 = total ~21–22. Per-chapter indicative (body-physical incl. tables; sum verified algorithmically: 2.5+2.5+3+2.5+2+2.5+2 = 17.0): P1 2.5 / P2 2.5 / P3 3.0 / P4 2.5 / P5 2.0 / P6 2.5 / P7 2.0 (range 16–17 with float placement). No rescope, no deletions. Trade-off: below 26.5 plan; magazine signature outside article scope is a publishing matter, not survey padding (no decorative/sponsored matter proposed). Requires Human Architecture amendment (see §6).

### Option C — structural scope revision

Only on compelling newly documented reason (retraction, invalidation, strategic reprioritization). r18 found none. NOT recommended.

## 6. Governance: what an amendment would require (researched read-only; nothing invoked)

- Frozen Core (`scripts/survey_human_gate_v2.py`, read-only inspection): supports contiguous Human review revisions (e.g., Architecture r2 with new record/snapshot/index rows, r1 preserved) and Publication Preview `REQUEST_CHANGES` with an upstream `regeneration_boundary` reopening Architecture (cross-gate rule). No verified path for amendment without a new explicit Human decision; silence ≠ approval.
- Feasible paths for Human (not executed, no CLI invoked, no gate written): (a) new Architecture Review r2 with revised allocations (Human APPROVED/REQUEST_CHANGES); (b) Publication Preview revision with upstream boundary (reopens Architecture per rule). Uncertainty: exact CLI route/operator steps for (a)/(b) not exercised in r18; Sol/operator to confirm at execution time under frozen workflow.
- No VALIDATED_DRAFT, Reader, Publication Preview, Freeze, Release, or Human Gate action taken in r18. All r18 artifacts NONCANONICAL.
