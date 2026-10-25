# W43 — Bounded Core-free editorial drafting bypass (Sol ruling)

Status: `AUTHORIZED_EDITORIAL_SIDECAR_ONLY / NOT_NATIVE_DRAFT_VALIDATED / NOT_DRAFT_COMPLETE / CORE_V2_FROZEN`
Date: 2026-10-25 JST.
Repository: `eariver/japanese-generative-ai-survey`; existing branch `weekly/2026-W43-v2-work`.
Start remote 6-way read-only guard PASS at `8d46be258fb7b46944fd54e374272b553ad9c4cf` root tree `bfe23b75c954958b75012ce5d0d99556d79ece69`; main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`; Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## Explicit Human Owner instruction and scope

Human Owner: "**Blockedです、Core v2の修復は禁止なのでBypassしてください。**" Explicitly forbids Core v2 repair and authorizes bypass. Previous Human Owner approved Architecture r6 with final `今週の総括` as Draft requirement and expressly rejected Architecture reconsideration.

This is permission **only to continue preparation and independent editorial review outside the broken native Draft pipeline**. It does NOT authorize forging Core success, mutating source authority, bypassing canonical Stage to RELEASED, bypassing Human Publication Preview, changing frozen scripts, or silently treating a preview as approved.

## Observed native blocker

Frozen Core `survey_screening_v2.validate_package_basis` compares screening package basis `state_sha256=885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596` with legitimate post-bridge `production-state.json` SHA-256 `b0450d25b9dd4db8424d1c92d713d28c1b268b4e6a3b960a053f9684bb3eebb6`. Both screening r1/r2 use old SHA. P1 native derive fails `ValueError: Screening package basis drift: state_sha256`; all eight Draft Packages and Synthesis absent; no Stage contract executed. Muse preserved whole prepared input (eight package specs, 113 blocks, 62 paragraphs, 28 headings, 15 tables, 8 notes) at `execution/defects/w43-draft-r1-interactive-input-UNVALIDATED-20261025.json`. Detailed source diagnosis `execution/defects/w43-drafting-screening-basis-drift-20261025.md`.

The diagnostic input's `runner.generated_at` field is `2026-10-25T14:00:00Z`. This is not accepted here as proof of actual execution chronology and must not be promoted into native provenance without verification.

## Edition-local bypass outputs and guarantees

1. **Source input unchanged**. Eight chapters transcribed in exact block order to `execution/editorial-bypass/w43-r1-readable-reader-preview-UNVALIDATED-20261025.md`. Table body text remains publisher-qualified and as-authored, no made-up reconstructed numeric headers. Each block has a chapter and identifier in machine-readable `execution/editorial-bypass/w43-r1-block-index-UNVALIDATED-20261025.json`.
2. One **new concluding Japanese editorial draft**, `execution/editorial-bypass/w43-closing-weekly-summary-r1-UNVALIDATED-20261025.md`, appended **after P8** in reader preview and before any references. This is not P9 and has no new selected candidate placements.
3. All three are **edition-local noncanonical editorial artifacts**, status `UNVALIDATED`. They are NOT at `draft/v2/packages/**` and do not counterfeit a native Core `draft-result.json` or synthesis result. Original `runner.generated_at` remains untouched in preserved diagnostic file, and no runner success is claimed.
4. Next Muse/independent Sol must review draft prose, citation provenance, tables, cutoffs, licensing, contradictions and language. Every substantial claim needs its nearest accepted direct-source Evidence reference; `discovery_ids` provide tracing hints but **are not primary-source citations or proof**. FIX wording only in further noncanonical editoral revisions, not in immutable Core upstream.
5. Architecture approved; do not reopen. No changes to `scripts/`, `schemas/`, `config/`, `.github/`, accepted Evidence/Selection/Architecture, State, approval/Gate/index/receipts, or main/Frozen branch. No new branch, no force.
6. Freeze the automation boundary: **do NOT issue `ADVANCE_STAGE` from `ARCHITECTURE_ESTABLISHED` nor create/claim `DRAFT_COMPLETE`** while native validation is blocked. A later publication process cannot be called officially validated or released absent an independently authorized, auditable alternative. Document any future publication-stage bypass as a separate Owner decision with its risk implications.

## Editorial review gate to unblock now

- Edit to substantive Japanese prose P1–P8 plus true closing conclusion; check 19 selected placements, 31 must-cover, 5 LIMITED, 68/68 Attention inherited, 32 PARTIAL Evidence labels.
- Verify counts and copied text against original diagnostic input; do not treat editorial source refs as source bytes.
- Create per-claim provenance/citation confidence table for the 62 original prose blocks plus the new closing conclusion; cite exact URLs/evidence refs where verified and mark missing `SOURCE_NOT_VERIFIED` instead of inventing references.
- Stop `SOL_W43_CORE_FREE_EDITORIAL_DRAFT_AUDIT_READY` after editor review pack and non-force push. **Do not claim `SOL_W43_JAPANESE_DRAFT_R1_WITH_RECAP_EDITORIAL_AUDIT_READY` from the original native-only contract.**

Bypass scope is bounded. Exact approval and Core integrity remain preserved.