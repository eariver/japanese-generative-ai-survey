# Human Architecture page-plan decision brief r21 (PROPOSED / DRAFT ONLY — no approval authority)

Date: 2026-10-18 JST. Author: Muse (execution). Status: `PROPOSED / NONCANONICAL / NO_HUMAN_VOTE / HUMAN_EDITORIAL_PREFERENCE_OPTION_B / NON-GATE`. For Sol vetting + independent focused r20→r21 print-surface/page-plan audit BEFORE any Human consultation. Supersedes r20 brief only on measured pagination (r20 20pp → r21 21pp via honest FloatBarrier fix + display-label consistency); r16–r20 briefs retained as history. Approved Architecture + r1 approval unchanged.

## 1. Approved (unchanged, immutable in this run)

7 packages / 28 selected (PRIMARY16+SUPPORTING12); body plan **26.5** (P1 4.0/P2 2.5/P3 5.0/P4 4.0/P5 3.0/P6 4.5/P7 3.5); issue target **28** / max **30**; Human r1 `approved`; lifecycle `DRAFT_COMPLETE`; Publication `pending`. Nothing here amends them. Formal page-only Architecture modification, even if page-only, requires a separate read-only Core-v2 legal-state-transition preflight and subsequent explicit Human authorization. No gate invoked, nothing written to gates/index/state. Current `DRAFT_COMPLETE/architecture approved` is not a directly pending approval.

## 2. Human editorial preference (non-Gate consultation, recorded separately)

Human selected **Option B** as editorial direction (record `sol-w42-human-editorial-option-b-consultation-record-20261018.md`, status `HUMAN_EDITORIAL_PREFERENCE / OPTION_B_SELECTED_FOR_PLANNING / NOT_HUMAN_GATE_APPROVAL`):

- Keep 7 chapters/28 SELECTED and substantive evidence (no watering down to meet count).
- Use provisional chapter allocation P1 2.5/P2 2.5/P3 3/P4 2.5/P5 2/P6 2.5/P7 2 = **17.0 PLANNED** as basis for reconsidering full-issue target.
- Formal Human Gate updates addressed separately; this preference does NOT authorize updating `architecture-v2.json`, `production-state.json`, approvals/review-index/checkpoints, canonical Draft, or invoking `record-architecture-approval`/revision.

Options A (retain 26.5 with genuinely new evidence) and C (structural only with new evidence) remain documented alternatives; this brief tags **B as Human-preferred for planning** per actual Human message and does NOT say A/B is unselected.

## 3. Measured r21 (auditable counts; area honestly bounded)

- r21 diagnostic (SHA `b8ac6172…`, 509,133B, deterministic epoch, all three runs byte-identical): **21 total = cover1 (p1) + body physical17 (p2–p18) + bib3 (p19–p21)**. NO diagnostic-only terminal page. Cover 3 warnings intact. TeX 95,112B/968 lines, log 77,332B/1475 lines, 0 overfull/underfull/errors/missing/undefined.
- Distinguish r20: **20 total = cover1 + body16 (p2–p17) + bib3 (p18–p20)**. r20 p01–p10 extracted-text raw + PNGs byte-identical to r21 p01–p10 (480/2495/2668/2353/2552/2431/2731/2674/1787/2526); p11–p18 reflowed by honest FloatBarrier repair (p11 2011/p12 2227/p13 2187/p14 2231/p15 2665/p16 2413/p17 2064/p18 702); bib p19–p21 (2850/3108/2698) with display-label fix only (7× `[SECONDARY]`→`[二次・参考]`, no URL/publisher change). No body/bib content change beyond layout + labels.
- Body-physical counting rule: a page counts as body iff it carries P1–P7 prose/table/note; shared chapter-boundary pages counted once (NOT added per chapter); tables counted in hosting chapter. p2–p18 = 17. p11 is P4 only; p12 Table4+P5; p14 Table5+P6; p16 Table6+P7; p18 P7 tail only (702 chars, honest expansion tail to inherited `\clearpage`, not padding, not stamp-only).
- Chapter locations re-verified on r21 PNGs + `pdftotext` page+column (two chapters share pages; intervals overlap and are NOT additive): P1 p2–p4 / P2 p4–p6 / P3 p6–p9 / P4 p9R–p11 (+ Table4 p12 top) / P5 p12–p13 (+ Table5 p14 top) / P6 p14–p15 (+ Table6 p16 top) / P7 p16–p18 (Table7 p17 in-flow, tail p18). F-08 all three SOLVED in physical reading order (Table BEFORE next heading on same p12/p14/p16). Tables1/2/3/7 remain in-chapter; Table7/Glimpse unbroken.
- EFFECTIVE AREA: no credible independent area metric exists → **`UNMEASURED; <= 17 PHYSICAL BODY PAGES`** (table/note/heading-inclusive upper bound, no double counting). The withdrawn r16–r18 `15.5–17` estimate is NOT revived. No numeric gap to 26.5 is issued. Planned 17.0 vs physical 17 is coincidental numeric equality, NOT observation of plan (see §4).
- r20 history kept distinct: 20 = 1+16+3. r21 bib remains 3pp from mandated alias cleanup (71 full + 19 `→ [Bxx]（同一資料）`); display-label fix does not change bib length (509,133B vs Alt-A-without-fix 509,136B, same 21pp).

## 4. Comparison (approved vs provisional vs tentative vs actual)

| Package | Current approved body plan | Human provisional Option B | Sol tentative whole-issue | r21 actual physical |
|:--|--:|--:|--:|--:|
| P1 | 4.0 | 2.5 | (in 17.0) | p2–p4 (part of 17 body pp) |
| P2 | 2.5 | 2.5 | (in 17.0) | p4–p6 |
| P3 | 5.0 | 3.0 | (in 17.0) | p6–p9 |
| P4 | 4.0 | 2.5 | (in 17.0) | p9R–p11 (+ T4 p12 top) |
| P5 | 3.0 | 2.0 | (in 17.0) | p12–p13 (+ T5 p14 top) |
| P6 | 4.5 | 2.5 | (in 17.0) | p14–p15 (+ T6 p16 top) |
| P7 | 3.5 | 2.0 | (in 17.0) | p16–p18 (T7 p17, tail p18) |
| **Body subtotal** | **26.5** | **17.0 PLANNED** | **17.0 provisional** | **17 physical (p2–p18)** |
| Cover | (in 1–2 ancillary) | — | 1 | 1 (p1) |
| References | (in 1–2 ancillary) | — | 3 | 3 (p19–p21) |
| **Issue total** | **target28 / max30** | **(body only)** | **target21 / max23 tentative** | **21 measured (1+17+3)** |
| Effective area | — | — | — | `UNMEASURED; <=17` |

- Approved 26.5/28/30 are canonical and unchanged in all historical references and repository files.
- Human provisional 17.0 is chapter allocation for future editorial planning, NOT a promise that exactly 17 full physical article pages will be consumed, nor an instruction to add text. r18 Reader content preserved (136 paras/25,015 chars/7 tables/7 notes/7 headings; 28 selected).
- Sol tentative whole-issue **21/23 are Sol's provisional recommendation only, NOT Human-approved**. 21 = provisional body17 + historical r20 cover1 + references3; max23 adds two pages of legitimate layout/bibliography/float variance above target (ceiling, not content-generation requirement). Both are **contingent on actual r21 physical pagination**, not fixed targets, word quota, or Human-approved fields. Do NOT carry forward 20 and 21+2 without remeasurement: r21 re-render changed chapter float pagination (body 16→17) and bibliography labels, remeasured to 21 total. If source-conserving float fix naturally produces 21 total, report actual and revise recommendation from measurable print evidence before seeking Gate decision. Don't conflate physical pages with measured occupied area. A page shared by chapter boundaries counts once.
- Current r21 measured 21 total happens to equal Sol tentative target21 numerically, but equality is **evidence, not approval**: 21 measured = 1+17+3 with body 17 physical (not 17.0 planned) and area UNMEASURED. If layout creates more than planned 17 body pages, explain (here: FloatBarrier honest +1 body page for correct physical order, p11 blank + p18 short tail as costs, no filler) rather than secretly changing proposal. No separate imposed minimum length, padding, spacing/font shrink, or citation/technical alteration to hit either number.

## 5. Reader sufficiency (unchanged from r18/r19/r20; zero body edits in r21)

All 7 chapters meet reader goals at current density (conditions/denominators/licenses/negatives preserved). Shortfall vs 26.5 is pagination vs plan, not thinness; padding prohibited. r18 Reader master 136 paras/25,015 chars/7 tables/7 notes/7 headings/157 reader blocks and 90 keys/19 aliases/177 ledger rows unchanged. F-08 repair first; all-page visual + prior-fix regressions required (see comparison doc §4; Tables1/2/3/7, B28/B57/B74/B90, notes, citations all PASS).

## 6. Gate procedure (consultation vs authorization; no r2 assumption)

- Current state (`DRAFT_COMPLETE`/approved/pending) does NOT permit assuming direct `record_architecture_approval r2` or `request_architecture_revision` executability now: frozen gate code requires suitable pending gate/lifecycle, and any amendment needs a separate lawful transition/regeneration contract + explicit Human decision (silence ≠ approval). Read-only finding only; nothing invoked, nothing written to gates/index/state. Do NOT invoke CLI gate actions.
- Distinguish: (i) **Human editorial-preference consultation** (Option B selected, recorded, changes nothing in-repo; Sol 21/23 tentative for discussion and post-r21 remeasurement only); (ii) **future authorized workflow** — separate read-only investigation of exact Core-compliant path, explicit scope, Human authority, then execution. Sol to sequence after r21 independent audit.
- Table arithmetic above independently verified (17/3/21 counts; 17.0 sum; 30.5 conditional; r20 20 vs r21 21 split). Brief is `PROPOSED / NO_HUMAN_VOTE / OPTION_B_PREFERRED_FOR_PLANNING`.
