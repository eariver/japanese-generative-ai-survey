# Repair plan — post-Architecture-r4 Draft JSON content revision (CONTENT REVISION REQUIRED)

Source: `supplied-independent-review-materialization.md` (worker transcription; worker does not
claim reviewer identity). Boundary `DRAFT_COMPLETE`; Architecture r4 APPROVED preserved
(`architecture-v2.json` 71cb4798…); no Discovery/Screening/Evidence/Materiality/Completeness/
Selection/Architecture rerun; no `reader-publication-validation`; no TeX/PDF/Candidate.

Starting authority (read-only verified before any write):
- Branch `special/vision-multimodal-2026-work`, HEAD `382833c30d294f54e847c0333fc4a03a58748a32`,
  tree `08d50dfa7bf3150051564c1b6cc08bf4c9ad7c4b` (remote HEAD/tree match).
- Reviewed main `d6381568cc897a47d6de992189e20339350342b7` /
  `83ce3a216d852a1c32d0138f9c56fadefa800666` ✓.
- Frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` /
  `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` ✓.

## 1. P15 overlay (edition-local, this run only)

- Allowlist = `publication_extensions.p15_cross_package_synthesis_map` only (11 axes, 39 IDs).
- Deterministic resolution: Discovery ID → Candidate Matrix row (candidate_id/evidence_task_id/
  evidence_sha256/discovery_ids) → Selection (all 112 SELECTED verified) → accepted Evidence
  Acceptance result (task/sha/filename) → exact accepted Evidence Card bytes (subject IDs).
  No new candidates; no Selection change; no PRIMARY/SUPPORTING destination change;
  cross-package use = `CROSS_PACKAGE_SYNTHESIS_REFERENCE` only.
- Artifact: `p15-cross-package-synthesis-authority.json` (per-entry: axis/map key, Discovery ID,
  candidate_id, canonical home package + usage, evidence_task_id, accepted Evidence SHA-256,
  Evidence subject ID(s), Architecture SHA, approval SHA, Matrix SHA, Acceptance SHA).
- Canonical `draft-package.json` for P15 stays byte-identical (14 inputs); result schema unchanged;
  canonical SHA binding maintained.
- P15-only compatibility validator `validate_p15_overlay.py`: normal refs via canonical package
  index; cross refs via overlay index (accepted bytes/hash verified); FAIL map-outside refs,
  unselected candidates, unknown Evidence, subject mismatch, duplicates; attribution checks
  identical to frozen validator.
- Truthful reporting: `15/16 canonical PASS` + `P15 overlay PASS`; generic Core validator's
  P15 cross-ref rejection recorded as known compatibility boundary, not hidden.
- Deferred Core maintenance candidate recorded execution-locally; shared Core untouched.

## 2. Content repairs (Evidence-bounded; unknowns remain unknown)

- P15 b9: delete VM-D112 mechanism sentences (transcription/frame/audio on-demand, adaptive
  frame/resolution, selective acquisition); rewrite as evaluation-contract difference
  (offline breadth vs referred-context reasoning vs online streaming) with editorial-synthesis
  note that stored-timeline navigation is a separate P11 contract; no mechanism/numbers.
- P15 cross-package: add traceable synthesis refs covering P05 (VM-D027/028 + 108/109),
  P10 (VM-D080 + 078/079/081), P11 (VM-D088/089 + 086/087), P12 (VM-D090/091/092),
  P13 (VM-D098 + 099/100), P14 (VM-D103/104/105 + 106/107), P09 (VM-D065/070/071 + 072/073),
  X01 (VM-D003/035/051/062/096), X02 (VM-D010/047/097 + 092/104), X03 (VM-D059 + 065/089/091/100),
  X04 (VM-D056/080/098/099/100/110). P12 OSWorld trio formally referenced. Prose stays at
  contract/comparison level supported by cards; no new numbers beyond cards.
- MMMU/MMBench: delete `英語と中国語`/`EN/CN bilingual` from MMMU block (2 sentences);
  bilingual scope stays only in MMBench block. QA-itemized.
- P06: delete 4 DINO temperature/centering/sharpening sentences incl. `生徒側を尖らせ教師側を
  滑らかにする`; no new temperature import; keep self-distillation/momentum/multi-crop/
  small-patch/ViT emergence/CLS segmentation/ImageNet/detector-distinction scope.
- P04 b5/b6: reframe token claims as editorial inference or P06/P09 synthesis reference;
  no factual source claims from 4-node Evidence alone. Keep four-node hard cap.
- P05: delete 9-taxonomy expansion (2 sents), operator-contamination-as-fact (3 sents),
  Nougat/GOT beyond-card mechanism (targeted deletions), fix `框`×5 + garbled sentence,
  tidy model/encoder/decoder/markup/token/suite/pair mixing (katakana normalization).
- P02: delete architecture-invariant generalization sentence(s); keep loss-centric scope.
- P07A: delete 6+2 fine-grained diagnostics beyond cards; keep bag-of-words scope.
  P07B: delete six-stage linear sentence; keep parallel/branching + completeness.
- P10: `投票型`×3 → operation-revealing phrasing; `定石`×2 removed; `投票` retained only
  where operation-clear or replaced by `POPEの質問方式`.
- P09: soften `情報を落とさず` → limited phrasing; `接地`×9 → `グラウンディング` (first-use
  explanation kept); VM-D112 placement kept.
- P11: keep 3 contracts; delete semantic-repetition closings; no new detail.
- P12: `接地`×8 → `グラウンディング`; fix `通貨の確認が必要` → `鮮度の確認が必要`;
  no step→token magnification (already qualitative; keep).
- P13: keep 7-node lineage; `言う側/できる側` → `言語側/行動側` (consistent, non-factual);
  trim `について見ると`×7 repetition. P14: keep 4-pole; `意味を言い当てる`×2 → latent/
  representation-prediction phrasing; V-JEPA decoder `接地` fixed; `復号器` → `デコーダ`.
- Private wording: P15 b1/b10 rewritten to auxiliary-means framing; never proof of absence.
- Terminology: re-audit map + apply to all 16 + synthesis (grounding/model/encoder/decoder/
  token/dataset/benchmark/mask/frame/interface/bounding box/DOM; banned forms fixed).
- Semantic padding: per-contract single disclaimer; consolidate `について見ると/別の欄に置く/
  一面だけ/測ることは〜/順序を変えない` repetitions with concrete before/after counts.
- Synthesis: fresh regeneration from revised packages; no patch-only; no carried-over
  unnatural expressions; no new source-specific facts.

## 3. Regeneration + validation

- Working input: copy of `bounded-revision-112-20261004/compact-input.json` revised in this dir
  (`compact-input-revised.json`), same envelope + `draft_version: content-revision-r4`.
- Regen via edition-local `regenerate_content_revision.py` (mirrors bounded-revision runner;
  identical derive/refs/validation except P15 result refs via overlay-extended index +
  P15 overlay validation; ONLY deviation, recorded here). 16 draft-packages byte-identical
  (upstream untouched); 16 results + synthesis regenerated.
- Stage semantics + `validate_agent_state` clean; lifecycle stays `DRAFT_COMPLETE`;
  checkpoint `ARCHITECTURE_ESTABLISHED.json` rebuilt deterministically; state provenance
  updated (provenance SHA only, no lifecycle/gate change).
- 15/16 canonical `validate_draft_result` PASS; P15 overlay PASS; generic Core P15 check
  expected FAIL on cross refs (recorded as boundary, not hidden).

## 4. Records in this dir

supplied review, repair plan (this), overlay design, overlay authority, overlay validation
result, technical-correctness audit, contamination audit, evidence-boundary audit, terminology
audit, semantic-repetition audit, before/after stats, worker QA, final execution report,
regen scripts, revised compact input, defect candidate note. Shared Core changed: NO.
