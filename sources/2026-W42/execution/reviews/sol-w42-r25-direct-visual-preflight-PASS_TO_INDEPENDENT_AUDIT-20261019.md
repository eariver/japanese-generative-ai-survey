# J-GAS W42 r25 — Sol direct visual preflight, PASS to independent audit

Date: 2026-10-19 JST
Authority: `SOL_DIRECT_VISUAL_PREFLIGHT / PASS_TO_INDEPENDENT_AUDIT / NONCANONICAL_ONLY / HUMAN_GATE_UNTOUCHED`
Repository: `eariver/japanese-generative-ai-survey`
Examined immutable r25 HEAD: `b992685a66ccfd9eef3073a448771d2f224bea9c`
Examined root Tree: `d552721744c4e8b6e71adf0bdb90753f36036066`
Previous Sol dispatch: `929df060312daf79f6c5737a1d3bb5a146028e61`

## 1. Git and immutable authority

Read-only GitHub branch reference and commit root verified; r25 advanced from prior Sol dispatch exactly one fast-forward commit, adding only W42 edition-local `execution/diagnostic-r25/`, `execution/typeset-repair-r25/`, a Muse session and append-only index. Reviewed `main` remains `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`; frozen `production/survey-core-v2` remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20`. `sources/2026-W42/production-state.json` blob still `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb`: lifecycle DRAFT_COMPLETE, Architecture Review approved, Publication Preview pending. The r18 Reader blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` remains authoritative, not modified. No formal Architecture, Reader, Publication, Freeze, Release or Human Gate change authorized.

## 2. Artifact and source invariance claims independently framed

Worker-selected `MULTICOL-V2`, 21 physical pages, NONCANONICAL:
- Exact PDF path: `sources/2026-W42/execution/diagnostic-r25/main.pdf`
- PDF SHA256 (manifest; not yet independently recomputed by Sol): `ce1d50cd748601013455c6164ce83e981edb4e39dc93ddf5c68dec8a00fbe251`
- TeX SHA256 (manifest): `837f553533c7e673d2430f6f5a010d59584e537e77c193d53680df311630f1c5`
- LuaHBTeX 1.24.0, `multicol` v2.0b, `capt-of` v0.2, 21 = cover1 + 17 physical body (p02–p18) + bibliography3 (p19–p21).
- Exact TeX source comparison from Worker: r18 157 reader blocks, 136 paragraphs / 25,015 paragraph chars, 7 chapters / 28 topics / 7 table objects / 7 notes; table captions, cells, row order and citations preserved; 90 bibliography keys = 71 full + 19 aliases, 177 ledger rows. This Sol preflight verifies the commit-level protected-scope diff but does NOT independently prove all textual byte equivalence. Independent reviewer must verify rather than inherit self-certification.

## 3. Direct visual result — Sol opened ALL 21 individual fixed-commit PNGs

Sol independently fetched and directly inspected `diagnostic-r25/pages/p-01.png` through `p-21.png` from the exact r25 commit (some as lower-detail previews, key boundaries at original detail). Unlike previous r22/r24 Worker false-PASS, verified actual physical print as well as session/manifest.

- T1 p04: caption and Wonder/Argon rows together, in P1 before P2; r22 `立直/し` mid-word interruption absent.
- T2 p06: caption and Maia/LFM rows together in P2 before P3; r22 `開/示` interruption absent.
- T3 p09: six rows Spark/Beam/Nemotron/Granite/MiniCPM/FLUX and caption entirely on same p09; r24 p08-orphan / p09-body defect absent. In P3 before P4.
- T4 p12: six rows Codex/Scion/HydraFusion/AutoFix/AI Scan/Decider visible, including Decider final `2セント/M入力・出力無料` and citations; full table before P5 heading on p12, no footer intrusion. r24 p11 clipped-row defect absent.
- T5 p14: four comparison rows intact, P5 before P6 heading p14.
- T6 p16: four rows intact; source-contiguous VERID `染料と水による検証` not interrupted by table; P6 before P7 heading p16.
- T7 p17: three rows GLM-Legal/ASPIRE/Glimpse entirely visible; above-table GLM sentence completes before table, ASPIRE paragraph appears below and flows normally to p18, no table inside a sentence; within P7 before bibliography.
- p18: both columns contain genuine P7 narrative, note, closing; 1772 raw pdftotext chars per manifest (versus r24 508 and r22 702), no giant left-only terminal body-page void. Physical image still shows some intentional lower white space; avoid overstating fully occupied area.
- p01 warning three lines intact; p19–21 bibliography visible, B28 starts complete, B57 readable though wrapping, B74 clean, B90 terminal. No obvious printed internal IDs or truncated rows on observed images.

Remaining presentational residuals: several pages such as p03/p11/p13 have noticeable lower-column unused area caused by full-width indivisible table placement/segment boundaries; p18 also not completely filled. Sol did NOT measure effective occupied page area and does not claim page-perfect optimization. These voids are materially less severe than previous 508–702 character left-only terminal page and do not independently block passing the candidate to external audit. An independent print-quality reviewer should adjudicate whether their amount/placement is acceptable in a magazine. The direct visual inspection found no *new* high-severity print blocker, but cannot replace a separate independent review or final human approval.

## 4. Editorial decision

Decision: `SOL_W42_R25_DIRECT_VISUAL_PASS_TO_INDEPENDENT_AUDIT / NONCANONICAL`.

This is a **preflight handoff pass**, NOT formal r25 Publication approval and NOT a Human Gate, not Architecture r2 authority. The Worker `SOL_W42_R25_INDEPENDENT_PRINT_AUDIT_READY` is now supported by Sol full 21-page visual inspection at preflight level, subject to fresh independent one-shot read-only review of source/print equivalence, page geometry, tables, notes, bibliography and residual whitespace.

Human Option B (editorial preference) remains 7 chapters/28 topics, planned 17.0 body pages. Sol suggested provisional issue target21/max23, not Human-approved. Formal Architecture r1 still body26.5/issue target28/max30. Do not amend gate/state yet. If independent audit PASS, return to Sol for separate governance preflight and explicit human page-plan consultation before canonical Reader/Publication work.

Independent one-shot contract:
`sources/2026-W42/execution/instructions/2026-10-19_w42-r25-independent-print-audit-one-shot-read-only.md`.
