# SOL W40 r17 handoff — two minor documentation closure (REVIEW REQUIRED)

Status: `SOL_W40_R17_TWO_MINOR_DOCUMENTATION_REVIEW_REQUIRED`
Date: 2026-10-10 JST
Branch (existing only): `weekly/2026-W40-v2-work` — normal commits + non-force push ONLY.
Authorizing inputs: `execution/instructions/2026-10-10_muse-w40-r17-two-minor-documentation-closure.md`
+ `execution/reviews/sol-w40-r16-independent-audit-disposition-20261010.md`
(independent r16 `BOUNDED_REVISION_REQUIRED` adopted; R16-F01/F02 authorized; A01/A02/
A04/A05 CLOSED, A03 PARTIAL-documentation; staging technically accepted).

## 1. Git authority (exact bytes; F02-safe wording)

- (1) Remote W40 branch HEAD read-only pre-write (ls-remote + GH API, zero writes):
  `1d68247598d46900ff5d356a267a4373d854d497` == outer Exact Starting SHA
  (parent = r16 `aad4b80e6…`); commit tree `c739b10cebde84f20dcb1bf10817d7bb955ba97f`
  == Expected Tree.
- (2) Remote main HEAD == `afdb3df3faa20af3bb5798be429bba8dbd2100b1` == reviewed main,
  SEPARATELY. (1)≠(2) as SHAs; no branch equality implied or claimed.
- (3) Remote symbolic HEAD == main (informational only; never a substitute for (1)/(2)).
- Local 1-behind aligned fetch + FF-only. Pre-write guards PASS: `EVIDENCE_REVIEWED`,
  next `stage:selection`, Selection/Architecture pending, Gates pending/null, exception
  inactive; 4 source SHAs byte-matched (preview `dc024778…`, matrix `f07b1166…`,
  coverage-r14 `3de8bd56…`, boundaries-r15 `1736737e…`).
- Scope: R16-F01/F02 ONLY. No source regeneration, no Selection/Matrix/Coverage/Boundary
  mutation, no tech-draft rerun, no `scripts/`/`schemas/`/`config/`/`.github/`/Core/
  `main`/other-edition/upstream/State/checkpoint/Issue/Gate writes, no prior-file edits,
  no Acceptance/transition/Architecture/Gate/Freeze/Release/supplement.
- W40-local commits only (§4); final HEAD/Tree + remote readback in outer report.

## 2. Changed paths (W40-local only; 4 new + 1 appended)

NEW: `execution/architecture-boundaries-roundtrip-digests-r17.json` (F01);
`execution/SOL_W40_R16_HANDOFF_GIT_IDENTITY_CORRECTION_R17.md` (F02);
this handoff `execution/SOL_W40_R17_TWO_MINOR_DOCUMENTATION_HANDOFF.md`;
`execution/sessions/muse-w40-r17-20261010.md`.
APPENDED: `execution/index.md` (entry only).

## 3. Findings (evidence-graded)

| ID | Status | Disposition + evidence |
|---|---|---|
| R16-F01 | CORRECTED | NEW roundtrip-digests JSON: fixed canonical serializer (`json.dumps(..., ensure_ascii=False, separators=(',',':'))` → UTF-8, no BOM/newline; Python 3.14.4; code-point ordering) + `derivation_executed:true` (script `/tmp/opencode/r17_digests.py`, genuinely recomputed twice, no stored-checksum reuse). Per-package REAL 64-hex `pass1_sha256`/`pass2_sha256`/`stored_array_sha256` (e.g. P1 `d6a9474a…`/`d6a9474a…`/`3e67e0b9…`); pass-digests equal 9/9; stored_order_equal false 9/9 (insertion vs sorted — distinguished, r15 arrays untouched, no forced byte claim); semantic_set_equal true 9/9; missing/extra 0; totals 28/20/8/113/105/8; status PASS (all recomputed true). |
| R16-F02 | CORRECTED | NEW additive correction withdraws r16 Handoff §1 `HEAD == main` as SHA-equality reading; records exact r16 W40 HEAD/Tree, remote main SHA (different SHAs), final r16 HEAD/Tree; states the three-assertion rule. Historical r16 Handoff bytes preserved. |

Residual constraints (unchanged): State `EVIDENCE_REVIEWED`; #562 separate Core task;
AstaBrief/AutoSynthData canonical HOLD; `NO NORMAL SUPPLEMENT_PATH_ESTABLISHED`;
no normal-path content admission. `EDITION_LOCAL_STAGING_CLOSED` is Sol's decision,
not claimed here. No Selection Acceptance, Architecture approval, Release, or upstream
supersession authority arises from this documentation closure.

## 4. Commits + terminal

- Content commit on `weekly/2026-W40-v2-work` (SHA in outer report); FF child of
  `1d6824759…`, non-force push, remote readback verified.
- Terminal: `SOL_W40_R17_TWO_MINOR_DOCUMENTATION_REVIEW_REQUIRED`. STOP.
