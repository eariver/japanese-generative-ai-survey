# W42 r19 finding-closure matrix (F-01..F-07)

Date: 2026-10-18 JST. Baseline r18 HEAD `f3840b42…`, dispatch HEAD `8fc8c416…`.
r18 Reader body frozen: 7 chapters, 136 PARAGRAPH / 25,015 chars, 7 TABLE / 7 NOTE / 7 HEADING, 157 reader blocks; 90 keys / 19 aliases / 177 rows. No body byte changed in r19 (verified 150/150 non-TABLE blocks byte-present in r19 TeX; 7 table captions/cells preserved).
Status: `SOL_W42_R19_PRINT_AND_PAGEPLAN_AUDIT_READY / NONCANONICAL` candidate.

## F-01 [HIGH] p16→p17 Glimpse sentence split by Table 7 — PASS

- Old observation (r18 actual): p16 right-column tail `ElorianのGlimpseは、視覚的作業空間（高密度`; p17 top full-width Table 7; then same-sentence continuation `の再走査・ズーム・追跡…`. Table no longer orphaned but bisects one paragraph.
- New (r19 actual): p16 ends at completed t7-17 paragraph + cite `[B57,B56,B89]` (transfer-design limits); p17 opens with in-flow Table 7, then the COMPLETE t7-07 mechanism paragraph (`Elorian のGlimpse は、視覚的作業空間（高密度の再走査…` unbroken through baselines/pricing). No sentence split by table; no orphan page; no cross-chapter float; table content/caption/cites byte-identical.
- Method: table code relocated to P7-intro boundary (after t7-02, completed paragraph) + `\needspace{4\baselineskip}` before t7-07 so its start clears the float zone (standard pagination control, ~1 line; no font/margin/whitespace targeting). Alternatives rendered and rejected with receipts: Alt A (after t7-08) → 22pp + p18 table-only orphan; Alt B (after t7-19) → 22pp + p18 table-only orphan; Alt D/F (before t7-07 / after t7-02 without needspace) → 21pp but same bisection. Winner Alt G adopted. p16→p17 render compared across all; p15→p17 flow read before marking PASS.
- Remaining: none for F-01. PASS.

## F-02 [MEDIUM] B28 URL p18→p19 orphan — PASS

- Old: p18 bottom `…flux-3-image-k`, p19 top lone `lein` (B28 label not on p19).
- New: B28 entry kept together on p19 via entry-level `\needspace` (full entry + URL `…klein` complete on same page; verified in p19 PNG). `https://huggingface.co/api/models/black-forest-labs/flux-3-image-klein` intact as clickable link; citations preserved.
- All-90 recheck after reflow: B57 `…/NVlabs/ASPIRE` wraps ASPI/RE across two lines WITHIN its p20 entry (readable, entry kept together via kept r18 needspace; page-top orphan gone). B74/B89/B90 full URLs intact. New minor: B28 shift moved bib flow so no other page-top stray fragments observed in all-90 scan (extracted-text check: no entry label separated from its URL across pages; p19 top now starts with complete B28 entry).
- No font shrink, no forced whitespace (needspace only). PASS.

## F-03 [HIGH] diagnostic stamp split — PASS

- Old: p21 two-column flow split `NOT FOR HUMAN` / `APPROVAL —`; cover wrapped `AP-/PROVAL`.
- New: cover shows 3 unbreakable centered lines (`NONCANONICAL DIAGNOSTIC` / `NOT A PUBLICATION PREVIEW` / `NOT FOR HUMAN APPROVAL`, verified in p1 PNG, no mid-word wrap). p21 footer shows all three phrases contiguous via `\mbox` (`— NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL —`) + compact JP line `非正準の診断文書であり、正式公開文書でも人承認用でもない` (verified in p21 PNG, single column block, no column/page split).
- Warning kept prominent in diagnostic PDF; NOT injected into canonical Reader/reader text (TeX body scan: stamp strings appear only in cover macro argument + terminal center block, never inside P1–P7 prose). No formal publication candidate. PASS.

## F-04 [HIGH] machine provenance in Reader bibliography — PASS

- Old print (r18 p20–p21): `alias-of`, `www/trailing-slash normalization`, `identical source snapshot`, reclassification history, `see ledger`, raw X/HTTP retrieval notes.
- New print (r19 p18–p21): 90 entries as `[publisher — kind]: clean link` (71 full) or `[Bxx] publisher — kind → [Byy]（同一資料）` (19 alias, no duplicate URLs). Machine phrases scanned over TeX bib strings AND extracted PDF text: 0 hits (`alias-of`, `normalization`, `identical source`, `see ledger`, `via @OpenBMB`, `via X mention`, `Life sciences section`, `Source: (via`, `trailing-slash`, `reconciled r1`, `card part duplicates`).
- Kept (source-significance, concise Japanese): B38/B59/B88 aggregator warnings (OpenRouter NOT independent), B54 sole-independent-evaluator note (with method limits), B89 dialog-figure values unavailable. Categories distinguish 一次/論文/二次/独立評価. All 90 Bxx targets + 19 aliases + classifications retained in authority sidecars (r18 map/matrix/ledger untouched); display map traces each key. No invented authors/years/titles. PASS.

## F-05 [MEDIUM] page-plan units and chapter ranges — MEASURED (corrected, no fake precision)

- r19 measured: 21 total = cover1 (p1) + body physical16 (p2–p17) + bib3 (p18–p20) + stamp-terminal p21 (footer only, ~4 lines). Body physical counted by section/column presence, tables once in hosting chapter, no double-counting of shared pages.
- Effective area: NO credible independent area metric available → reported as `UNMEASURED; <= 16 PHYSICAL BODY PAGES` (table/note/heading-inclusive bound). r16/r17/r18 `15.5–17` WITHDRAWN as undefined. No fake gap number issued.
- Chapter locations re-verified on r19 pages+columns (not hardcoded from r18): P1 p2–p4 / P2 p4–p6 / P3 p6–p9 / P4 p9(right)–p11(left) / P5 p11(right)–p13 / P6 p13(right)–p15 / P7 p15–p17 (Table 7 p17 in-flow). Overlapping shared-page intervals NOT additive.
- Conditional hypothetical (labeled, not rendered): 26.5 + actual nonbody (cover1+bib3+stamp-page1 = 5) = 31.5 vs target28/max30. r18 historical 26.5+1+4 = 31.5 kept distinct (its bib was 4pp + footer in-flow). Option B 17.0 is PROPOSAL (2.5+2.5+3+2.5+2+2.5+2, sum verified), NOT measured body.
- Verdict: MEASURED with stated uncertainties (counts exact; area UNMEASURED).

## F-06 [LOW] audit-wrapper leak risk — PASS

- `reader-preview-r18.PROPOSED.md` wrapper header (`PROPOSED/CLAIM_BOUNDARY` boilerplate) verified ABSENT from r19 TeX/PDF (body built from JSON blocks only; MD never ingested; TeX scan 0 hits). r18 JSON preserved exactly.

## F-07 [MEDIUM] post-approval Architecture workflow — DOCUMENTED (no assumption)

- Current: lifecycle `DRAFT_COMPLETE`, Architecture r1 `approved`, Publication `pending` (blob `63edc922…` unchanged). No `record_architecture_approval r2` / `request_architecture_revision` invoked or promised.
- Read-only finding: frozen `survey_human_gate_v2.py` supports contiguous revisions (Architecture r2…) + Preview `REQUEST_CHANGES` with upstream `regeneration_boundary` reopening Architecture; both need new explicit Human decisions under a separate lawful contract. Human editorial-preference consultation distinguished from future authorized workflow (see r19 brief §6). No gate/index/state writes. PASS (as documentation, not execution).

## Overall

F-01 PASS, F-02 PASS, F-03 PASS, F-04 PASS, F-05 MEASURED (area UNMEASURED, counts exact), F-06 PASS, F-07 DOCUMENTED. No new body bytes; no padding/shrinking/fonts/margins; no formal publication. Residuals: p21 near-empty terminal stamp page (honest consequence of mandated alias shortening + required unbreakable stamp; documented, not filler); B57 intra-entry ASPI/RE wrap (readable, kept together).
