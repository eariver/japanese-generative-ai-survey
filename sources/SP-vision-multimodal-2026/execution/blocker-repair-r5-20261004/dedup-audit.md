# Boundary dedup audit — blocker-repair-r5 (read-only analysis, pre-replay)

Method: per package, union of placed candidates' matrix `remaining_boundaries` = REQ
(validator-mandated verbatim); all other lines = FREE. Only FREE near-duplicates are
removal-eligible; REQ lines can never be removed without an Evidence change (out of scope
except VM-D075).

## Findings

- P07B (18 bounds = 17 REQ + 1 FREE): GoldG pair — BOTH REQ (distinct candidates).
  REC pair — BOTH REQ (distinct candidates). KEEP both pairs. No FREE dups. → 0 removals.
- P09 (26 bounds = 21 REQ + 5 FREE): VM-D112 trio REQ in P09 and P11 (dual placement) —
  KEEP. Living-surface trio — all REQ (distinct candidates). Data-release pair — both REQ.
  FREE lines (M-RoPE thread, 3 canonical bucket lines, VM-D075 scoped companion) have no
  dups among themselves. → 0 FREE removals. NOTE: post Evidence-fix, the previously-added
  FREE scoped companion becomes redundant with the validator-propagated REQ scoped line
  (identical scoping); replay REMOVES that FREE companion (redundancy created by the fix
  itself, not an independent semantic deletion).
- P11 (14 bounds = 13 REQ + 1 FREE): VM-D112 trio REQ — KEEP. Single FREE line, no dup.
  → 0 removals.
- P15 (17 bounds = 14 REQ + 3 FREE): "No mechanism..." trio — all REQ (distinct
  candidates). FREE synthesis lines distinct. → 0 removals. No schema change; no two-layer
  restructure (explicitly forbidden).

## Conclusion

0 independent semantic deletions. The only boundary removal in this replay is the
now-redundant FREE VM-D075 scoped companion in P09 (superseded by the REQ line of the
same scoping from the corrected Evidence). All validator-required lines preserved;
no distinct candidate-specific limitations merged; no Evidence meaning changed;
no new Architecture concepts.
