# J-GAS W42 r22 — Sol direct-visual preflight: REQUEST_CHANGES

Date: 2026-10-18 JST
Authority: `SOL_DIRECT_VISUAL_PREFLIGHT / R22_PRINT_NOT_APPROVED / R23_SYSTEMIC_LAYOUT_REPAIR_REQUIRED / NO_HUMAN_GATE_ACTION`
Repository: `eariver/japanese-generative-ai-survey`
Exact inspected r22 commit: `d0cf7cb82d744260f630a5f9043fecc80d4b139f`
Root tree: `f21e36ec710dc1a717060804961a2ede25043a7f`
Predecessor: `4850a017dcec38269ffdd943141e15d2a7c5ca48`.

## 1. Scope and authority

This is Sol editor's independent-of-Worker direct opening of fixed-commit PNG page images, plus read-only GitHub diff, r22 session/audit/manifest/TeX/source mapping. It is NOT an external independent reviewer report or Human Gate action. Do NOT approve r22 PDF as formal Reader/Publication. Machine `DRAFT_COMPLETE`, Human Architecture r1 approved, Publication Preview pending; Option B is only editorial preference (7 chapters/28 selected, provisional body17.0), Sol 21 target/23 max only tentative. r18 Reader, Core v2, canonical Draft/Architecture/State/Gates all protected.

## 2. Identity and positive work

Remote W42 r22 HEAD/tree fixed above, exactly one normal FF commit after prior r22 instruction. Changed files only `sources/2026-W42/execution/`: selected `diagnostic-r22/main.pdf`, all 21 page PNGs/log/TeX/manifest; full rejected B 20pp PDF/20 PNGs and evidence; r22 audit, source-invariance, page-plan PROPOSED, session and index append. Main remains `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`; Frozen Core v2 `774dd39a951c9ac3818e83dfffd4c7666efb0a20`. Production State blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb` preserved.

C2 21-page diagnostic source unchanged except print-only `\\needspace{8\\baselineskip}` before ASPIRE. The earlier r21 ASPIRE sentence break across Table7 on p16→p17 IS fixed: p16 closes a full GLM-Legal paragraph; p17 Table7 precedes a fresh complete ASPIRE paragraph. Table4 p11→p12 and Table5 p13→p14 appear to have paragraph-complete preceding pages. No source expansion needed.

## 3. NEW DIRECTLY OBSERVED HARD FAILS (reproduced from actual published GitHub PNGs)

Muse's r22 assertion "7/7 tables at paragraph boundaries; zero bisections" is contradicted by images. All snippets below are physical page-end/page-below-table observations, not TeX source placement assertions. The table is a FULL-WIDTH top-of-page float between source-contiguous sentence fragments.

| ID | Severity | Physical proof at selected C2 fixed commit | Disposition |
|---|---|---|---|
| F22-01 | HIGH | Table1 at p04 top. p03 right-column last text ends `失敗の記録と立直`; p04 below Table1 begins `しの手順が残ることが…`. r22 main.tex confirms the source sentence `失敗の記録と立直しの手順が残ることが、実行主張の検証口になる。` | FAIL: Table1 bisects word/sentence |
| F22-02 | HIGH | Table2 at p06 top. p05 right-column tail `16種ベンチを温度条件つきで示す流儀は分母の開`; p06 below Table2 begins in mid-prose `も、温度・ベンチ名とセットで読む…` (left column) with further continuation in right column. r22 main.tex contains source-contiguous `分母の開示だ。AutomationBench 27.69対次点8.72という差も、温度・ベンチ名とセットで読む。`. The reading boundary is not paragraph-safe and must be reconstructed exactly from PDF column order, not an abbreviated assumed single adjacent token pair. | FAIL: Table2 interrupts a paragraph; printed continuation is not clean |
| F22-03 | HIGH | Table3 at p09 top. p08 right-column tail `一つのエンドポ`; p09 below Table3 starts `イントではほぼ基盤と同等のVRAM…`. | FAIL: Table3 bisects word/sentence |
| F22-04 | HIGH | Table6 at p16 top. p15 right-column tail `VERID較正の意味を確認する。染料と水によ`; p16 below Table6 starts `る検証、フィードバックで5倍超の精度という記述は…`. r22 main.tex confirms unbroken source phrase `染料と水による検証、フィードバックで5倍超の精度`. | FAIL: Table6 bisects word/sentence |
| F22-05 | MAJOR | p18 is P7 closing body with just 702 pdftotext raw characters, upper-left portion of one column only; entire right column and most lower page blank before bibliography p19. p11 right-bottom and p16 right-bottom also contain avoidable-looking voids caused by barrier/needspace. Worker labels this "honest reasonable"; direct image does NOT justify print-quality PASS. | REQUEST_CHANGES: compare and fix/quantify, without filler or shrinking fonts |

Individually opened fixed-commit PNGs: selected p03/p04, p05/p06, p08/p09, p11/p12, p13/p14, p15/p16, p16/p17, p18. Table4 (p12), Table5 (p14), Table7 (p17) are currently clean at these specific boundaries but must be rechecked after all subsequent layout changes. No claim of a completed independent all-21-page certification is made by this Sol note.

## 4. Editor disposition and process correction

`REQUEST_CHANGES / R22_PRINT_NOT_APPROVED`. r22 Muse execution is committed/completed technically, but `SOL_W42_R22_HOLISTIC_PRINT_AUDIT_READY` is only Worker self-report, NOT an accepted print PASS. At least FOUR of seven top-of-page full-width tables cross active narrative sentences despite log=0. The same systematic two-column `table*` float-placement failure survived r19–r22 piecemeal fixes and multiple self-certifications. The p18 mostly blank terminal body page is an additional layout-quality finding.

Do not immediately ask external reviewer to approve r22 or Human to approve Architecture r2 / Publication. Next r23 must redesign or reliably schedule full-width table placement as a SYSTEM, prove every physical page boundary, compare genuinely rendered alternatives, and retain r18 Reader bytes. Avoid merely placing `needspace` before one observed split; such local shifts can create new splits elsewhere. If no compliant layout is achievable without content/style violation, terminal `R23_SYSTEMIC_LAYOUT_BLOCKED` with proof, not fake PASS.

No Gate/Architecture/Reader/Freeze/Release/Core writes authorized. New r23 execution instruction: `sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r23-systemic-fullwidth-table-boundary-and-tail-repair.md`.
