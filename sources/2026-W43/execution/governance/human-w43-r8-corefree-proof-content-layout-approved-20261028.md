# J-GAS 2026-W43 — Human acceptance of fixed r8 noncanonical core-free PDF proof

Date: 2026-10-28 JST.
Status: HUMAN_NONCANONICAL_R8_CONTENT_LAYOUT_PRE_REVIEW_APPROVED / NOT_FORMAL_PUBLICATION_PREVIEW_GATE
Authority: Human Owner's explicit user decision in editorial Sol chat, received after independent technical PDF audit adjudication.
Decision text (verbatim): 「確認の結果OKです、承認します。」

## 1. Exactly approved artifact and prior authority

Repository: eariver/japanese-generative-ai-survey
Branch of record: weekly/2026-W43-v2-work
Fixed r8 PDF implementation HEAD: 953a9d331972fdae237da4bd0f1019b17168a118
Fixed r8 Root Tree: dfafff50c946e3d0abc051eb419797de283b192a
PDF: sources/2026-W43/execution/core-free-preview-r8/main.pdf
PDF SHA-256: abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72
PDF bytes/pages: 487351 / 22 pages A4
Fixed r8 TeX SHA-256: 4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d
Fixed P2 QA sidecar HEAD/Tree: de5e41c253de37015fdb828503040f818698c6bc / 5da261bfc4c1791f912033937ea1bf909f39ffc1
Independent Sol report supplied: 20261028001028_SolReview.md, terminal INDEPENDENT_W43_R8_P2_SIDECAR_AND_PDF_PASS (P0=0/P1=0/P2=4, all four P2 accepted as bounded nonblocking limitations).
Editorial Sol technical-audit reception:
sources/2026-W43/execution/reviews/sol-w43-r8-independent-zip-audit-acceptance-human-corefree-proof-review-offer-20261028.md
Human was offered EXACT fixed PDF after audit. Human then replied verbatim: 「確認の結果OKです、承認します。」 No new content changes or PDF rebuild were requested.

## 2. Decision, authorized scope and non-authorized scope

APPROVED: Human owner reviewed the presented fixed r8 PDF and accepts its article content and visual/layout presentation for the **noncanonical core-free UNVALIDATED PDF proof**, without further r8 revisions. This is an EDITORIAL PRE-REVIEW receipt, not a canonical pipeline or Publication Preview Gate authority.
- Fixed r8 immutable PDF approved as a proof by the human owner.
- Prior editorial Sol disposition accepts 4 residual P2 as nonblocking: original r8 manifest's malformed historical Tree (corrected in additive sidecar); original checker process-meta taxonomy (strict sidecar); old page QA positions (additive supersession); 2 minor Overfull vbox warnings p14/15 without visual clipping.
- The Human's assent applies to exactly the fixed r8 PDF SHA; no implicit approval of a regenerated PDF, different SHA, official preview, source upgrades, additional research or newly altered proof.

NOT AUTHORIZED by this decision:
- DO NOT write or change sources/2026-W43/gates/ or production-state.json.
- DO NOT set human_gates.publication_preview=approved, set DRAFT_COMPLETE, advance lifecycle, run ADVANCE_STAGE, Freeze, Release, merge to main, open PR or tag an official edition.
- DO NOT claim official Publication Preview validated, r8 is still NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF and NOT A PUBLICATION PREVIEW.
- DO NOT modify Frozen Core v2, common scripts/schemas, Architecture, Selection, Evidence, the fixed r8 PDF/TeX/QA or fixed P2 sidecar; no r9 merely for audit or Human pre-review.
- DO NOT infer authority to bypass blocked native Draft or to activate exception_gate.

## 3. Remaining production constraints, next governance task

As read from sources/2026-W43/production-state.json at the pre-receipt branch:
- lifecycle_state ARCHITECTURE_ESTABLISHED
- human_gates.architecture_review approved
- human_gates.publication_preview pending
- exception_gate.status inactive
- machine_checkpoints.draft/validation/publication_preview/freeze/release pending
- next_action stage:drafting-synthesis

Native Draft remains blocked by documented shared frozen-Core convention mismatch:
sources/2026-W43/execution/defects/w43-drafting-screening-basis-drift-20261025.md
error: Screening package basis drift: state_sha256.
Frozen Core v2 cannot be changed within W43 production.

The next EDITORIAL/SOL task is a separate **read-only lawful-path/exception-governance feasibility review** and, if useful, a concrete bounded proposal to the Human Owner, distinguishing:
(A) ordinary reviewed Core maintenance + immutable Frozen Core continuity under a new formally approved release/baseline (requires a separate authorization and cannot silently unfreeze Core v2);
(B) explicit human-governed exceptional publication lane if and ONLY if current production policy permits it, with true source/provenance limits, separate noncanonical label, clear Human scope, fail-closed gates and no fabricated canonical checkpoints;
(C) hold publication in the absence of permitted route.
No method is approved by the present core-free PDF content/layout decision. Publication readiness must not be inferred from human approval of a proof.

Source-based limitations preserved: 36 bibliography keys with 15 CURATED_REVIEW_REQUIRED (13 natural, 2 further). Historic architecture 31 grading r3.2 independent 20/11 vs r2 diagnostic 18/13 remains versioned and not a current automatic 31/31 validation.
Human click timestamp and user identity beyond "Human Owner" are not invented. Date indicates this Sol receipt record date, not an independently measured review click timestamp.
