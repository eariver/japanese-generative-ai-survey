# Supplied fresh independent content review — materialization (CONTENT REVISION REQUIRED)

Provenance: materialized from supplied fresh independent content review received 2026-10-04
against Exact Starting SHA `382833c30d294f54e847c0333fc4a03a58748a32`
(tree `08d50dfa7bf3150051564c1b6cc08bf4c9ad7c4b`).
Reviewed main `d6381568cc897a47d6de992189e20339350342b7`
(tree `83ce3a216d852a1c32d0138f9c56fadefa800666`).
Frozen Production Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
(tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`).
All three verified read-only exact-match before any write.

This file is a worker transcription of the supplied review's decision and directives.
It is NOT a worker-performed review, NOT a Human review, and NOT an Architecture Review.

## Decision

- `CONTENT REVISION REQUIRED` on Draft JSON reader-facing content (Draft-level only).
- Human Architecture r4 `APPROVED` is fully preserved.
  Architecture authority: `sources/SP-vision-multimodal-2026/architecture-v2.json`
  SHA-256: `71cb47989f328ed002f5db561345c7031d3360e6e4d7e0b0ee8d5f53d5975f72`.
- Current lifecycle: `DRAFT_COMPLETE`.
- Prohibited: Discovery / Screening / Evidence / Materiality / Completeness / Selection /
  Architecture rerun.
- Normal end state: revised Draft JSON → bounded validation → lifecycle remains
  `DRAFT_COMPLETE` → STOP for fresh independent JSON content review.
- Must NOT advance to `reader-publication-validation`.

## Directives (faithful transcription, sections 1–20)

1. P15 mixed-placement cross-package synthesis compatibility overlay (edition-local, this run
   only; NOT a shared-Core change). Allowlist = Architecture
   `publication_extensions.p15_cross_package_synthesis_map` only. Resolve each Discovery ID
   deterministically via current Candidate Matrix → current Selection → accepted Evidence
   Acceptance → exact accepted Evidence Card. No new candidates. No Selection change. No
   PRIMARY/SUPPORTING destination change. Cross-package use = `CROSS_PACKAGE_SYNTHESIS_REFERENCE`
   only. Do NOT add P12 etc. candidates to P15 supporting_candidate_ids. Overlay artifact
   (e.g. `execution/<new-dir>/p15-cross-package-synthesis-authority.json`) must record per
   entry at minimum: synthesis axis / map key, Discovery ID, candidate_id, canonical home
   package, evidence_task_id, accepted Evidence SHA-256, Evidence subject ID, Architecture SHA,
   Architecture approval SHA, Candidate Matrix SHA, Evidence Acceptance SHA — all derived
   mechanically from current authority. P15 `draft-result.json` `evidence_refs` may reference
   only the union of (a) canonical P15 `draft-package.json` Evidence inputs and (b) overlay
   allowlisted Evidence. 15 other packages use frozen Core validator unchanged. P15-only
   execution-local compatibility validator: no result-schema change; keep canonical P15
   draft-package SHA binding; normal refs via canonical package; cross refs via overlay;
   verify down to accepted Evidence bytes/hash; FAIL refs outside Architecture extension map,
   unselected candidates, unknown Evidence. Do NOT edit `scripts/survey_drafting_v2.py` etc.
   Record deviation in execution report. Do NOT report `canonical validation PASS` while hiding
   that generic Core validator rejects P15 cross-refs. Correct reporting e.g.:
   `15/16 canonical Draft validation PASS` + `P15 edition-local cross-package compatibility
   validation PASS`. Record frozen-Core limitation as deferred Core maintenance candidate
   execution-locally; do NOT change shared Core summary/main/implementation this run.
2. P15 stays methodology-first (no benchmark-catalogue return). One evaluation contract =
   single pass of input → target → metric semantics → failure exposed → confounder →
   evidence strength. Do not repeat same caveat per benchmark. P15 b9: delete current
   VM-D112-specific mechanism description (VM-D112 not in `p15_cross_package_synthesis_map`;
   do NOT describe transcription/frame/audio on-demand acquisition, adaptive frame count,
   adaptive resolution, selective acquisition concrete VM-D112 mechanism in P15; VM-D112 detail
   stays in P09/P11 per approved Architecture). In P15, use allowlisted P11 Evidence to focus
   on evaluation-contract differences (offline duration breadth, referred-context reasoning,
   online streaming). Stored-timeline on-demand navigation in P15 only as editorial synthesis
   that it is a separate contract in P11, without idiosyncratic mechanism/numbers. P15
   cross-package use must traceably synthesize at least P05 document/chart/OCR, P10
   reasoning/hallucination, P11 video, P12 GUI/Computer Use, P13 VLA, P14 predictive/world-model,
   P09 vendor-vs-independent, X01 supervision/data/post-training, X02 objective/interface, X03
   token/context/memory/latency, X04 reliability/provenance. In particular make P12 OSWorld /
   OSWorld 2.0 / SeeClick-ScreenSpot formally referenceable via overlay, satisfying
   Architecture contract.
3. P15 factual contamination: remove MMBench-derived conditions (e.g. 英語と中国語, EN/CN
   bilingual benchmark) from MMMU block entirely. MMMU only within current Evidence Card scope.
   MMBench bilingual scope stays only in MMBench block. Make cross-benchmark contamination a QA item.
4. P06 DINO self-supervised: delete current teacher/student temperature explanation, especially
   `生徒側を尖らせ教師側を滑らかにする`. Do NOT newly import correct temperature values from
   Raw Source/web this run. Return P06 to Evidence-bounded scope: self-distillation without
   labels, emergent properties in ViT, CLS attention semantic-segmentation information, momentum
   encoder, multi-crop, small patches, ImageNet results recorded on card, detector-DINO name
   distinction. Delete centering/sharpening/exact temperature schedule etc. not on accepted Card.
   Same Evidence-Card bound for DINOv2.
5. P04 tokenization synthesis: do NOT derive as factual source claims from P04 MiDaS/OpenPose/
   Visual Genome/DUSt3R Evidence alone (token increase from higher resolution, token memory
   increase, pixel-detail loss via tokenization, relation-triple discretization fragility, etc.).
   Do not delete wholesale since Architecture needs `what survives tokenization`; where
   Architecture cross-synthesis needs it, either explicitly reference appropriate P06/P09
   Evidence as edition-local synthesis authority, or weaken generalization labeled as editorial
   inference. Keep P04 four-node hard cap.
6. P05 Evidence discipline + Japanese rewrite: substantially re-edit reader-facing prose.
   Do NOT expand DocVQA「9 reasoning-type categories」into own 9-way taxonomy beyond Evidence
   Card; do NOT state operator-inference contamination risk / language-prior risk as paper facts;
   do NOT supplement Nougat/GOT mechanism/detail beyond accepted Evidence Cards. Delete taxonomy
   finer than Evidence-Card granularity. Fix Japanese thoroughly; leave no `框`, `複数切断の読みは
   頁を割りて細かく受け` style artifacts. Tidy disorderly English mixing around Nougat/GOT
   (model/encoder/decoder/markup/token/suite/pair etc.) without force-translating established
   technical terms.
7. P02 RetinaNet: separate Focal Loss contribution from RetinaNet detector architecture. Strictly
   keep accepted Evidence boundary `loss-centric contribution; architecture claims require
   detector-side sources`. Delete generalizations to architecture invariance from Evidence
   (e.g. `骨格や解像度を変えず目的関数だけで解決した`). Limit theme to class-imbalance
   diagnosis → focal loss mechanism → one-stage detection training impact.
8. P07A/P07B source discipline: CLIP bag-of-words limitation within accepted Evidence may stay.
   Do NOT supplement fine-grained diagnostics not explicit on Evidence Cards from downstream
   knowledge (attribute swap, word order, counting, spatial relations, etc.). Limit OVD/grounding
   bridging to accepted Cards + Architecture synthesis scope. P07B not as「六段の一本道」;
   reorganize as parallel/branching lineage. Keep current high chain completeness.
9. P10 POPE terminology: do NOT translate `polling-based` as「投票型」 (misread as ensemble
   voting). E.g. at first use `反復的な二値質問によるobject probing（polling-based query）`
   or equivalent operation-revealing phrasing; thereafter `POPEの質問方式` as needed. Do not
   overgeneralize evaluation procedure as「定石」.
10. P09 minor: basically keep. Where pixel-unshuffle etc. assert `情報を落とさず` in strong
    mathematical/information-theoretic terms, soften to Evidence-grounded limited phrasing
    (e.g. `空間情報をチャネル方向へ再配置する`, `単純な縮小とは異なる形で高解像度情報を保持する`).
    Keep VM-D112 placement in P09/P11.
11. P11: keep three-contract separation (offline breadth / online streaming / stored-timeline
    on-demand navigation), no conflation. Main work is semantic-repetition removal. No new
    technical detail needed.
12. P12: unify `接地` (vision-language/GUI grounding sense) to `グラウンディング` in principle;
    at first use explain e.g. `画像中の要素・座標と指示を対応づけるグラウンディング` as needed.
    Fix `通貨の確認が必要` style generation errors. Do NOT estimate token magnification from
    OSWorld 2.0 step counts.
13. P13/P14: keep P13 seven-node lineage; do not re-expand P13, only semantic-repetition/table
    cleanup. Keep P14 four-pole contract. I-JEPA phrasing: avoid vague `意味を言い当てる`;
    return to latent/representation-prediction technical meaning. Do not describe V-JEPA decoder
    as `接地` in vision-language grounding sense.
14. Private benchmark / contamination wording: in P15 etc. prohibit sentences meaning
    `private setで一致すれば汚染がない` / `privateであること自体が漏洩対策を証明する`.
    Limit private/hidden evaluation to `公開benchmarkへの過適合や既知問題の影響を緩和・検出する
    ための補助的手段` level. Never treat as proof of absence of contamination.
15. Terminology normalization — all 16 packages: re-audit existing `terminology-map-ja.md` and fix
    application gaps in actual prose. Minimum: grounding→グラウンディング, model→モデル,
    encoder→エンコーダ, decoder→デコーダ, token→トークン, dataset→データセット,
    benchmark→ベンチマーク, mask→マスク, frame→フレーム, interface→インターフェース,
    bounding box→バウンディングボックス, DOM→DOM（Document Object Model, first-use explanation
    allowed). Audit all 16 packages for disorderly generic English tokens. Do not replace
    established technical terminology with unnatural Japanese. Especially prohibited/fix:
    接地→原則グラウンディング, 投票型→explain POPE actual query method, 框, 檔案系統,
    文書物体模型, 言う側/できる側, 通貨の確認, unnatural archaic/Sinicized forms.
16. Semantic padding: do not use exact-duplicate count alone as quality metric. Centered on P15,
    treat repetitions like `〜について見ると`, `別の欄に置く`, `一面だけの結論は出さない`,
    `測ることは〜、測っていないことは〜`, `順序を変えない` as semantic duplication and consolidate.
    One evaluation contract: attribution/boundary disclaimer in principle once. After revision run
    semantic-repetition audit with concrete examples in execution report.
17. Profile synthesis: after all 16 packages fixed, freshly regenerate
    `profile-synthesis-input.json` + `profile-synthesis-result.json` (do not patch-only current
    synthesis prose). Regenerate from revised package authority. In particular do not carry over
    投票/接地/言う側・できる側/順序を変えない/一本に合わせない/範囲を守る style unnatural or
    repetitive generated expressions. Profile synthesis itself must not newly generate
    source-specific factual detail.
18. No new research rule: principle `unknowns remain unknown`. Even if independent review used
    external primary sources to find errors, if that detail is absent from current accepted
    Evidence Card, prefer retreating Draft to Evidence scope. Do NOT bring raw web source/paper
    text directly into Draft for this revision. Stop only if formal Evidence regeneration is truly
    needed, reporting `Evidence insufficiency requiring upstream repair` (current review judges
    large Evidence rerun unnecessary).
19. QA / execution records: create new execution directory holding at minimum supplied
    independent review materialization, repair plan, cross-package synthesis compatibility design,
    P15 overlay authority, overlay validation result, technical correctness audit,
    cross-benchmark contamination audit, Evidence-boundary audit, terminology audit, semantic
    repetition audit, before/after package statistics, worker QA, final execution report.
    State new Core defect candidate explicitly:
    `mixed-placement synthesis package cannot consume Architecture-authorized cross-package
    Evidence under current frozen Draft validator`. This is NOT an instruction to fix Core now.
20. Validation truthfulness: 15 packages PASS with frozen canonical validator. P15 PASS with
    edition-local overlay validator. If generic Core validator rejects P15 overlay refs, report as
    normal known compatibility boundary. Never falsely write `all canonical validators PASS`.
    Final report must show at minimum: Starting HEAD/Tree, Final HEAD/Tree, Architecture r4
    approval preserved, lifecycle remains DRAFT_COMPLETE, 112 Discovery/Selection/Evidence
    authority preserved, shared Core changed: NO, 15/16 canonical package/result validation,
    P15 compatibility-overlay validation, P15 overlay Evidence count, P15 Architecture-map
    coverage, MMMU/MMBench contamination removed, DINO unsupported temperature detail removed,
    P05 unsupported taxonomy removed, RetinaNet source boundary corrected, POPE terminology
    corrected, grounding terminology normalization count, semantic repetition before/after,
    profile synthesis regenerated, TeX changed: NO, PDF generated: NO,
    reader-publication-validation executed: NO, Publication Candidate generated: NO,
    next action = fresh independent JSON content review.

## Terminal condition (from supplied review)

`DRAFT_COMPLETE` → bounded content/evidence-discipline repair → P15 edition-local
cross-package synthesis compatibility PASS → package/profile synthesis regeneration →
worker QA → lifecycle remains `DRAFT_COMPLETE` → **STOP FOR FRESH INDEPENDENT JSON CONTENT REVIEW**.

Do not proceed to TeX/PDF.
