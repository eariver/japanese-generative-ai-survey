# J-GAS W42 r23 BLOCKED — Sol disposition and r24 routing

Date: 2026-10-18 JST
Authority: SOL_EDITORIAL_DISPOSITION / R23_BLOCKING_STOP_ACCEPTED / R24_NONFLOATING_FULLWIDTH_FEASIBILITY / NO_HUMAN_GATE
Repository: eariver/japanese-generative-ai-survey
Read-only observed r23 HEAD: `7f9ccdbe573850021b787c694b30ebd756c37576`
Observed root tree: `6c019ee0333888e032b00b8d514c193ac8661c27`
Baseline Sol r23 dispatch HEAD: `d430894b3675195b02886c459eeff58819a183ea`

## 1. Stopping classification and verified scope

r23 technically completed as one normal fast-forward commit with new edition-local `typeset-repair-r23/`, `diagnostic-r23/`, session and append-only execution index. Reviewed main and Frozen Core v2 heads remain unchanged. Formal machine lifecycle stays DRAFT_COMPLETE, Human Architecture r1 approved, Publication Preview pending. No canonization, Gate, Core or release authorization is inferred from r23.

Accept Worker terminal `R23_SYSTEMIC_LAYOUT_BLOCKED` as a correct fail-closed disposition **for the solutions tested**. This is NOT proof of mathematical impossibility of a compliant two-column layout.

Worker compared:
- C2 r22: 21 pp, 4 whole-page top `table*` sentence bisections.
- B r22: 20 pp, 3 bisections.
- r23 SA: 22 pp, repeated `needspace`, one new demonstrated Table2 word bisection and p12 713/p19 702 low-fill tails.
- r23 SB: 22 pp, `[bp]` + `dblfloatfix`, persistent Table1 bisection and p09 856 sparse region.
- r23 SC: 23 pp, chapter-end anchoring + barriers, multiple severely sparse pages, hash-only proof.

The root failure is *asynchronously drifting two-column-wide floats*: a full-width table positioned at next page top can interpose between two halves of a continuing paragraph. TeX source position and log warnings are not a physical reading-order certification. Sol r22 direct PNG proof discovered T1/T2/T3/T6 failures. r23 correctly retained them as blockers.

## 2. Remaining untested feasible mechanism

Investigate **non-floating, in-flow, full-width** inserts at paragraph boundaries while retaining the two-column body design. The CTAN sttools/cuted documentation describes the `strip` environment for inserting full-width material in `\twocolumn` documents while resuming two-column text. It warns of potential interactions with floats and footnotes. It is an untested option in W42, and `jlreq` + LuaLaTeX + luatexja/tcolorbox/tabularx/caption/hyperref interoperability must be tested in Muse's actual TeX Live 2026 environment.

References:
- https://www.ctan.org/tex-archive/macros/latex/contrib/sttools/ (current package bundle description)
- https://ctan.tikz.jp/macros/latex/contrib/sttools/cuted.pdf (package description and warnings)
- https://tex.stackexchange.com/questions/752734/cuted-package-conflicts-footnote-misplacement-and-figure-b-drifting/752784 (illustrative caution, not authority for compatibility)

Sol locally compiled a **synthetic** `jlreq` + LuaLaTeX + `cuted` + `captionof` 2-strip, 4-page demonstration in a separate TeX Live 2025 environment: compilation completed, but class-caption warning and an overfull vbox were emitted. It is NOT W42-proof and is not a publication candidate. Actual Muse environment may be materially different. Do not report cuted as a verified solution before real r24 rendered whole-issue comparison.

## 3. Decision

Authorize one narrowly bounded r24 **feasibility +, only if feasible, full noncanonical print proof** execution. Keep r18 Reader and canonical/State/Gates byte-exact; only print TeX table containers/placement controls may be adapted. Unlike r23, an in-flow replacement changes `table*`/caption macros, so preserve all table **cells, row order, captions' visible words, labels/citation mapping, chapter membership and counts** verbatim, while permitting justified *wrapper-only* changes. Verify caption numbering/link anchors, printed citations and typography on actual PDF. Never present failure to produce a clean strip build as grounds for changing frozen Core.

Reassess all 7 physical table boundaries, P1–P7 headings, p18 tail, B28/B57/B74/B90, cover, full bibliography and every page individually. Compare against r22 C2 and r23 SA/SB. If no compliant method is found, stop BLOCKED with evidence; do not authorize Human Architecture r2, Publication, Freeze or Release.

Next contract:
`sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r24-inflow-fullwidth-strip-feasibility.md`.
