# Session — TS-003 Draft Content Revision r5-rev1 (DRAFT_COMPLETE held)

## Starting authority (read-only verified before any write)

- Repository: `eariver/japanese-generative-ai-survey`
- Branch (existing only): `special/vision-multimodal-2026-work`
- Starting HEAD: `eafb68eaf6a009be33c003877d2dbc9360f0129b` ✓ (remote match)
- Starting tree: `34dd4a627259f3ab9b5a5e9a76a3ba6d7230691d` ✓ (remote match)
- Lifecycle at start: `DRAFT_COMPLETE`; Human Architecture Review r5: `APPROVED`
- next_action at start: `stage:reader-publication-validation` (NOT executed in this run)

Mismatch policy: any mismatch → zero writes + report. No mismatch occurred.

## Run kind

Bounded Draft CONTENT revision. No new Discovery, Screening, Evidence research,
Architecture redesign, Human Architecture Review, TeX/PDF, Candidate, Preview,
Freeze, or Release. `reader-publication-validation` NOT started.

## What was wrong (supplied review)

The fresh 121-authority Draft passed deterministic validation but did not
semantically realize approved Architecture r5 + cross-package authority mappings:
P15 consumed 14/40 mapped authorities (26 missing, incl. full P12/X01-X04 threads);
P10 lacked Evidence-bound D111/D112 three-role chain; P12 lacked token/context
economics; P11 left SAM 3 as name-only without D115; P06 Qwen reuse cited only
SigLIP-side authority; P09 Molmo 2 weight/data terms misleading; LongVideoBench
6,668 numeric error; reader-facing Japanese/internal-vocabulary leaks.

## Actions performed

1. Created `execution/content-revision-r5-20261006/`.
2. Built multi-consumer edition-local overlay authority
   (`build_overlay_authority.py` → `cross-package-synthesis-authority.json`):
   30 entries / 29 unique Discovery IDs, all SELECTED, all card bytes SHA-verified —
   P15 26 non-canonical map IDs; P10 D111+D112 (P10 must_cover-named);
   P11 D115 (P11 must_cover-named); P06 D065 (P06 must_cover-named, claim-3).
   No Selection/destination change; role `CROSS_PACKAGE_SYNTHESIS_REFERENCE`.
3. Authored revised specs from the fresh-run `compact-input.json`
   (`revise_p15.py`, `revise_mid.py`, `revise_rest.py`, `apply_revisions.py`
   → `compact-input-rev1.json`, `draft_version fresh-121-r5-rev1`):
   60 exact-once replacements + P15 13-block synthesis rebuild + new blocks
   (P10 b6/b7, P11 b10, P12 B8) + truthful must_cover maps (P10/P11/P12/P15) +
   reader-facing boundaries text (all 16) + P06 D065 claim-3-only binding +
   P09 Molmo 2 four-bucket separation + LongVideoBench 6678 + full JP cleanup.
4. Regenerated deterministically (`regenerate_r5.py`): 16 draft-packages asserted
   byte-identical; 16 draft-results rewritten; 12 canonical PASS +
   4 overlay PASS (`validate_overlay.py`); frozen generic cross-ref rejection
   recorded as known boundary (81 errors on P15, same class as r4's 64 — not hidden).
   Synthesis input rebuilt overlay-aware; synthesis result payloads preserved with
   refreshed basis binding; validated.
5. Edition-local semantic audits (`gen_audits.py` → `semantic-audit-r5-rev1.json`):
   ALL PASS — P15 40/40 with per-thread 4/4, 4/4, 4/4, 4/4, 3/3, 5/5, 5/5, 5/5,
   5/5, 5/5, 6/6; no blanket must_cover rows in P15; P10 D111/D112 + PARTIAL
   restraint + streaming disclaimer; P11 D115 + no name-only; P06 D065 claim-3 +
   Omni narrowed; P12 B8 axis; P09 bucket separation; 6678/no 6668; banned-token
   purge (incl. 般化×2, 動作点×6+headline, 管路×2, 枠率/映像枠/伝送路/枠 counters,
   本パッケージ×15, カード internal senses, 正準×5, G01-G05, PARTIAL/INSPECT codes);
   オープンボキャブラリー normalization; all 9 regression guards incl. VM-D122 absent.
6. Rebuilt draft checkpoint + state provenance (`rebuild_checkpoint.py` →
   `stage-validation-r5-rev1.json`; `ARCHITECTURE_ESTABLISHED.json` artifact SHAs
   refreshed; `production-state.json` draft checkpoint SHA updated — the ONLY
   state change); `validate_agent_state` CLEAN. Lifecycle/gates untouched.
7. Mid-run corrections re-applied cleanly via restore-and-regenerate
   (checkpoint state-gate is circular mid-revision — same documented pattern as r4):
   leftover 本パッケージ×7, 筋道×1, 開放集合→オープンボキャブラリー.

## Deviations / failures

- Frozen Core cannot express mixed-placement cross-package synthesis refs
  (P15 + now P06/P10/P11): canonical `draft-package.json` kept byte-identical,
  edition-local overlay validator used instead. Shared Core untouched.
  Recorded as Core-maintenance candidate in `core-defect-note.md`; repaired in
  edition, not in Core.
- Regen re-run after first PASS hit the checkpoint state-gate (artifact drift by
  design); restored canonical bytes via `git checkout -- draft/v2/` and re-ran
  once from the patched spec. No upstream bytes changed.
- Regen is slow (~5 min for 16 derive+validate cycles); ran in background.

## Deferred future-edition context (NO intake)

- `V-JEPA Policy`: review-surfaced post-freeze candidate; NOT admitted because
  current TS-003 Discovery coverage is frozen (`DISCOVERY_COVERAGE_FROZEN_FINAL`)
  and approved Architecture r5 is the drafting authority. No materiality
  screening performed, no Architecture change. Only an explicit future Human
  Owner override may reopen Discovery.

## External handoff

- None. Direct exact local CLI only. No Issue #448, no operator PR, no bridge workflow.

## End state

- Lifecycle: `DRAFT_COMPLETE` (held; `reader-publication-validation` NOT started)
- Architecture r5: APPROVED / unchanged. Discovery/Screening/Evidence (121)/
  Selection (121)/approval: unchanged. Shared Core: unchanged. TeX/PDF: none.
- STOP for Human/Sol Draft content review.
