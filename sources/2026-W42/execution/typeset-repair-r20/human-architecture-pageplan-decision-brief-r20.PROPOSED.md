# Human Architecture page-plan decision brief r20 (PROPOSED / DRAFT ONLY — no approval authority)

Date: 2026-10-18 JST. Author: Muse (execution). Status: `PROPOSED / NONCANONICAL / NO_HUMAN_VOTE`. For Sol vetting + independent focused r18→r20 print-surface/page-plan audit BEFORE any Human consultation. Supersedes r19 brief only on measured pagination (r19 21pp incl. diagnostic-only terminal stub → r20 20pp intrinsic); r16–r19 briefs retained as history. Approved Architecture + r1 approval unchanged.

## 1. Approved (unchanged)

7 packages / 28 selected (PRIMARY16+SUPPORTING12); body plan **26.5**; issue target **28** / max **30**; Human r1 `approved`; lifecycle `DRAFT_COMPLETE`; Publication `pending`. Nothing here amends them.

## 2. Measured r20 (auditable counts; area honestly bounded)

- r20 diagnostic (SHA `e0e0f56f…`, 508,316B, deterministic epoch, final two byte-identical): **20 total = cover1 (p1) + body physical16 (p2–p17) + bib3 (p18–p20)**. NO diagnostic-only terminal page. Terminal stamp block deleted; cover 3 warnings intact.
- Distinguish r19: **21 total = cover1 + body16 + bib3 + stamp-terminal1 (p21, footer safety block only, 167 raw chars, otherwise empty)**. r19 p21 was NOT magazine content and is NOT counted as publication need. r20 p1–p20 extracted-text raw lengths identical to r19 p1–p20 (480/2495/2668/2353/2552/2431/2731/2674/1787/2526/2482/2306/2262/2443/2420/2462/2115/2850/3108/2729); full-text diff 167 = p21 only. No body/bib reflow.
- Body-physical counting rule: a page counts as body iff it carries P1–P7 prose/table/note; shared chapter-boundary pages counted once (NOT added per chapter); tables counted in hosting chapter. p2–p17 = 16.
- Chapter locations re-verified on r20 pages AND columns (two chapters share pages; intervals overlap and are NOT additive): P1 p2–p4 / P2 p4–p6 / P3 p6–p9 / P4 p9(right)–p11(left) / P5 p11(right)–p13 / P6 p13(right)–p15 / P7 p15–p17 (Table 7 p17 in-flow, t7-07 complete below, t7-17 completed above). Same as r19 (body identical); rechecked on r20 PNGs p02–p17, not assumed.
- EFFECTIVE AREA: no credible independent area metric exists → **`UNMEASURED; <= 16 PHYSICAL BODY PAGES`** (table/note/heading-inclusive upper bound, no double counting). The withdrawn r16–r18 `15.5–17` estimate is NOT revived. No numeric gap to 26.5 is issued.
- r19 history kept distinct: 21 = 1+16+3+1 (stamp). r20 bib remains 3pp from mandated alias cleanup (71 full + 19 `→ [Bxx]（同一資料）`); stamp is gone, not merged into bib.

## 3. Conditional hypothetical (labeled; NOT a rendered PDF)

IF the approved 26.5 body were rendered AND r20 nonbody layout persisted (cover1 + bib3 = 4), total = **26.5 + 4 = 30.5** vs target28/max30 (exceeds max by 0.5). r19 historical variant (cover1+bib3+stamp-terminal1 = 5) totaled 31.5 by including artificial diagnostic matter — kept distinct, not conflated, and NOT an appropriate future-publication hypothetical. Neither 30.5 nor 31.5 is a real printed document. Do NOT hardcode 30.5 to future layouts (bib length depends on display rules).

## 4. Reader sufficiency (unchanged from r18/r19; zero body edits in r20)

All 7 chapters meet reader goals at current density (conditions/denominators/licenses/negatives preserved). Shortfall vs 26.5 is pagination vs plan, not thinness; padding prohibited. r18 Reader master 136 paras/25,015 chars/7 tables/7 notes/7 headings/157 reader blocks and 90 keys/19 aliases/177 ledger rows unchanged.

## 5. Options (no preference selected)

- **A retain** (26.5/28/30): needs listed new primary evidence (aptamer Methods, ASPIRE figures, Earth SHA/splits, Vals methods/rate, Maia baseline, Nemotron PDF bytes, HF per-file LICENSEs, METR downstream, independent reruns). None obtained in r20 (out of scope by design). Gap stands; no padding meanwhile.
- **B provisional reallocation** (sums verified: 2.5+2.5+3+2.5+2+2.5+2 = **17.0 planned**): P1 2.5 / P2 2.5 / P3 3 / P4 2.5 / P5 2 / P6 2.5 / P7 2. Explicitly a PLANNING proposal, NOT measured body (measured body physical = 16; area UNMEASURED). Preserves 28/7 + qualifications; no filler. Requires Human Architecture amendment (see §6).
- **C structural redesign**: only on compelling newly documented reason; none found. NOT recommended.

## 6. Gate procedure (consultation vs authorization; no r2 assumption)

- Current state (`DRAFT_COMPLETE`/approved/pending) does NOT permit assuming direct `record_architecture_approval r2` or `request_architecture_revision` executability now: frozen gate code requires suitable pending gate/lifecycle, and any amendment needs a separate lawful transition/regeneration contract + explicit Human decision (silence ≠ approval). Read-only finding only; nothing invoked, nothing written to gates/index/state.
- Distinguish: (i) **Human editorial-preference consultation** — may occur now, changes nothing in-repo; (ii) **future authorized workflow** — separate read-only investigation of exact Core-compliant path, explicit scope, Human authority, then execution. Sol to sequence after r20 audit.
- Table arithmetic above independently verified (16/3/20 counts; 17.0 sum; 30.5 conditional; r19 21 vs r20 20 split). Brief is `PROPOSED / NO_HUMAN_VOTE`.
