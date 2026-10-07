# Session — TS-003 r8 Draft Closure Revision rev2 (DRAFT_ONLY, r8 APPROVED held)

Run: `execution/r8-draft-closure-rev2-20261007`. No rewind, no replay, no upstream
mutation (verified byte-identical at close). Lifecycle DRAFT_COMPLETE throughout.

## Starting authority

- Branch `special/vision-multimodal-2026-work`, HEAD `146510fd48d198428657ceaf6dfb51d95be87c93`,
  tree `0e50686a0f10eb9bee2100ff668dceef0874236c` (remote match; clean tree).
- Architecture r8 APPROVED (`56658960…`), Evidence 121 (116/5), Draft fresh-121-r8-rev1.

## Work performed

1. Read full VM-D091 card (claim-1/2, limitation, verification). The §5 figures
   37K tokens/task, 13–14%, 150/300/500 steps are NOT in canonical Evidence;
   per §3 narrow-don't-invent, GPT-5.5 wording stays within the card
   (token-efficient plateau ~13% + axis distinctions). Reported explicitly.
2. Built rev2 spec (`compact-input-fresh-121-r8-rev2.json`, version fresh-121-r8-rev2):
   P13-B2 lineage split (+D097 canonical), P15-B04 GPT-5.5 rewrite, P15-B09/P12-B6
   condition binding (implemented in follow-up patch after scoping audit),
   P09-B10 dup handling, P11-b10 already correct, P07B triad/query/checkpoint terms,
   X01/P01 fixes, grounding normalization (P15-B09 opening, 位置座標), 資料→data fixes,
   editorial/workflow purge. Every replacement asserted to fire; output spec strictly
   verified (zero old-strings, all new-forms present, molmo2 ×1).
3. Regenerated via normal generation path (`regenerate_rev2.py`): 16/16
   (8 canonical + 8 overlay over unchanged 35-entry map). Mid-run notes: P04 needed
   overlay-consumer status (already in map); one partial-write run hit the
   stage-basis drift guard (restored canonical bytes, re-ran cleanly).
4. Full audit (`audit_rev2.py`): 75 checks ALL PASS incl. §§4-9 closure checks,
   FINAL effective consumption, Japanese/workflow scans, preserved guards
   (incl. rev1 SSv1/InstructBLIP/DETR/DocVQA), F1-F6 + G1-G7 + H1-H5 negatives.
5. Checkpoint rebuilt (`rebuild_checkpoint_rev2.py`): rev2 SHAs + review; state draft
   provenance refreshed; DRAFT_COMPLETE held; `validate_agent_state` CLEAN.

## Correction to review premises (verified on committed bytes)

- §8 duplicate: the committed r8 P09-B10 contains the molmo2 sentence exactly ONCE
  (697-char block identical spec/result). No duplication existed; rev2 preserves
  exactly one copy. Reported, not "fixed".
- §5 numeric specifics (37K, 13–14%, 150/300/500): absent from canonical VM-D091;
  omitted per §3 narrow rule; GPT-5.5 wording kept card-faithful.

## End state

DRAFT_COMPLETE, r8 APPROVED, reader-publication-validation NOT STARTED, no TeX/PDF.
STOP for fresh independent Sol/Human-facing content review.
