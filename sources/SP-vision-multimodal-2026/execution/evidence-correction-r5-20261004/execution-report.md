# Final execution report — TS-003 targeted Evidence correction + replay to r5 PENDING

## §15 readback

- Starting HEAD/Tree: `382833c30d294f54e847c0333fc4a03a58748a32` /
  `08d50dfa7bf3150051564c1b6cc08bf4c9ad7c4b` (remote HEAD/tree, main HEAD/tree,
  Frozen Core commit/tree all read-only exact-match verified; no stop needed).
- Final HEAD/Tree: HEAD unchanged `382833c…` / `08d50dfa…` (no commits created by this
  run — not a Human Gate presentation). Working tree holds replayed bytes + two
  untracked execution dirs; shared roots clean.
- Re-entry boundary: `CANDIDATES_NORMALIZED`, via Human-authorized Owner Exception
  (`owner-exception-authorization.md` + `owner-exception-execution.json`) driving ONLY
  Core machinery (`_revised_state`, `_superseded_*`, Core state IO, `validate_agent_state`).
  Three formal paths probed fail-closed with zero writes first (`reentry-analysis.md`).
  No Human-gate decision function called; no `reviewed_by/reviewed_at` fabricated.
- Evidence result-set old/new hash:
  `33ec63cbd5bbe776fb106f57fa64ca448061dfe92cbbfe3684848ddb17010b69` →
  `4e77d1c6f8bf52ccd7b6e64a1787012c325ade49304884e7d92a44e7305deb22`
  (append-only; old sets retained). Views acceptance new:
  `1aec74a0ad1663f8c27f3e1b392ec2c45e3b61f0d7673434f7fe6bc3d1472a98`.
- Corrected Evidence records (8): VM-D062 LLaVA (rewrite), VM-D061 MiniGPT-4 (+3 claims),
  VM-D034 DINO (+2 operator claims), VM-D033 MAE (+3 recipe claims), VM-D024 LayoutLMv3
  (+1 line), VM-D028 GOT (+1 line), VM-D108 DocVQA (+1 line), VM-D077 molmo2 (+2 bucket
  claims, lim narrowed, PARTIAL kept). All staged canonical-validated before consumption.
- Unchanged Evidence count: 104 basis-excluded byte-identical (verified card-by-card).
- LLaVA old/new claim diff: old `claim-1` (`end-to-end vision-encoder+LLM tuning` with
  85.1%/92.53%/open/Bench) REMOVED as factually wrong → new claims 1–6 (instruction-data
  generation / architecture-interface / Stage 1 both-frozen-W-only / Stage 2 encoder-frozen
  W+LLM + system-vs-component distinction / eval conditions / X01 INFERENCE); limitation
  extended with paper Limits. Old/new texts in staged card
  `staged-cards/staged-VM-D062-task-2ca5c465106302004bdd.json`.
- MiniGPT-4 Evidence depth: single-projection/frozen-frozen/two-stage carried + BLIP-2
  ViT-G/14+Q-Former frozen provenance + 5M/3.5K data + Q-Former-removal ablation variant
  (level distinction resolves the self-contradiction recurrence).
- DINO/MAE depth decisions: DINO +centering/sharpening-pair + temperature-direction
  (teacher smaller/sharper; reverse REFUTED); MAE +normalized-pixel FINAL +decoder-depth/
  mask-ratio ablations +linear-vs-finetune +DEFAULT-vs-FINAL. Both primary-verified.
- Molmo 2 currentness: code Apache-2.0 (already bound, reconfirmed) / weights Apache-2.0 +
  academic-noncommercial third-party caveat (resolves bucket) / 9-dataset family ODC-BY
  availability (resolves bucket) / third-party restrictions bucketed (report-only, no new
  Discovery). VM-D077 stays PARTIAL; PARTIAL×5 preserved.
- Discovery/Selection/Evidence counts: Discovery 112 (jsonl untouched) / Selection
  112 SELECTED (assignments byte-identical, basis rebased) / Evidence 112 (104+8).
- Architecture semantic diff (r4-approved → fresh, 28 diff lines): basis-hash rebinding
  (4 SHAs) + 2 limitation-boundary swaps (LLaVA extended, VM-D077 narrowed). NOTHING else.
  (`architecture-r4-to-fresh.diff`.) Fresh arch SHA
  `f69daac4286090bd731388faf680bfa831535b451f5a3d34306c33d3e31b2e87`, PROPOSED, null review.
- P15 39-authority map preservation: 39/39 IDs, VM-D112 absent, VM-D089 present; map bytes
  untouched; skeleton 16 packages; P04 four-node; P07A/B split; P11 three contracts;
  P14 four-pole; VM-D112 P09/P11 SUPPORTING only; SS V1 lineage; no overlay implemented
  this run (post-r5 handoff recorded).
- VM-D089/VM-D112 mapping: VM-D089 = Flash-VStream (streaming; in P15 map); VM-D112 =
  Agentic Video Understanding (stored-timeline/query-driven; NOT in P15 map, never added).
- Core changed: NO (shared roots clean; frozen modules only).
- Draft regenerated: NO (draft/ bytes untouched by this run; prior-turn bytes remain on
  disk unbound). TeX changed: NO. PDF generated: NO. reader-publication-validation: NO.
- Final lifecycle: `ARCHITECTURE_ESTABLISHED`; `human_gates` arch+publication pending;
  `next_action: ARCHITECTURE_REVIEW`; review-index r1–r4 + pub-r1 (NO r5 record) →
  next required Human review = **Human Architecture Review r5 PENDING**.
- r4 APPROVED preserved as history ONLY (`gates/reviews/architecture-r4.json` + approvals
  snapshot intact; active `gates/architecture-approval.json` superseded by the authorized
  cross-gate rewind; fresh Architecture NEVER treated as r4-approved).

## Records in this dir

supplied-review-materialization.md (with §2 reviewer-side corrections) /
owner-exception-authorization.md / owner-exception-execution.json / reentry-analysis.md /
core-process-gap.md / granularity-ledger.md / replay-plan.md /
staged-cards/ (8, canonical-validated) + staging-report.json /
replay_evidence.py / replay_views_materiality.py / replay_selection.py /
replay_architecture.py / execute_exception_rewind.py / stage_corrections.py /
validation/ (3 stage validations + reviews) / architecture-r4-to-fresh.diff /
session.md / this report.
