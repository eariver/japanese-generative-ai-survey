# Survey Production session — ts002-issue529-depth-expansion-20260926

Issue: `#529` — Beyond Text core-4-chapter LONGFORM_SPECIAL depth expansion (Human Owner revision request)
Sol boundary: Issue #529 latest Sol execution-boundary comment (eariver/OWNER, 2026-09-25)
Branch: `special/beyond-text-2026-work` (existing only)
Prior Sol r2 PASS (`05b010c39`) explicitly superseded by Issue #529 while open (not treated as final disposition).

## Starting guards (read-only, all PASS; zero writes until Human decision)

- Remote work HEAD `05b010c39edf81473761e75b6ce37b71fe41f4cc` == Exact Starting SHA.
- Remote work tree `5d3a33e685e70351ba79ffe713333e7a134c1a29` == Expected Starting Tree.
- Remote main `0bbb02b3c5963403860897daec2feaf61e82589a` / `e4ddde5ed5059d303b818f54e27204369b256bcb` == reviewed main.
- New Sol r2 PASS file read (`sol-publication-preview-review-r2-20260926.md`); in-scope Evidence statuses checked (only BT-D022/D059/D134 non-VERIFIED).

## Canonical Human revision record

- Human explicitly selected `REQUEST_CHANGES @ DRAFT_COMPLETE` in-session (no inference from silence).
- Recorded via `survey_human_gate_v2.request_publication_preview_revision` (expected_revision=2):
  `gates/reviews/publication-r2.json`, lifecycle RELEASE_CANDIDATE → DRAFT_COMPLETE,
  Architecture approval preserved, invalidated validation checkpoints removed by Core.
- State revalidated clean before any repair write.

## Changed files

- `surveys/special/beyond-text-2026/main.tex` (§2/§6/§7/§8 expanded; rest byte-identical)
- `surveys/special/beyond-text-2026/main.pdf` (rebuilt 73pp)
- `sources/SP-beyond-text-2026/publication/v2/*` (manuscript/deterministic/bundle/surface/semantic/visual/candidate rebuilt)
- `sources/SP-beyond-text-2026/orchestration/v2/checkpoints/{DRAFT_COMPLETE,VALIDATED_DRAFT}.json` (rebuilt for new bytes)
- `sources/SP-beyond-text-2026/execution/depth-audit-issue529/longform-depth-audit.{json,md}` (new)
- `sources/SP-beyond-text-2026/execution/draft-through-preview-20260925/` (pdf-build-audit-issue529.json, build_validation_529.py, advance_*_529.py, validation receipts)
- `references.bib`: unchanged (r2 repaired version retained; no new authority needed).

## Focus-chapter before/after depth summary

- §2 paradigms (T-PAR-01..09 re-reviewed): six-axis separation table added; GAN/DCGAN/StyleGAN arch-vs-objective split; pixel-AR sequential cost; DDPM forward/reverse + Lsimple positioning; classifier vs classifier-free (btd032 cross-ref); DDIM as sampling-only; score-SDE↔DDPM relation; EDM abstract-level framing (BT-D022 PARTIAL kept); LDM as representation change; DiT backbone axis; SiT interpolant axis; FM/rectified-flow reformulation; consistency→execution-cost bridge (high-level, detail in §10). Repair pass: btd020↔btd030 citation swap fixed (4 locations); DDPM/ADM/DDIM-step/LDM condition-bound numbers restored from active Evidence.
- §6 speech: modeling-position axis section added (what each stage models); waveform cost/stability; vocoder division of labor; VITS integration inventory; semantic/acoustic/codec token roles; codec-LM scheme + zero-shot conditioning needs; similarity-vs-fidelity trade-off; streaming causality/latency vs full-duplex turn-taking/interrupt/overlap as separate constraints; §1 link in words only. D059/D134 PARTIAL fenced.
- §7 music: fidelity-vs-structure axes; hierarchy role in music; structure across 4 regimes; generation/continuation/editing/control table; alignment-vs-coherence; duration-vs-maintenance; 4-way eval split. No new model names; FAD/CLAP limits kept.
- §8 video: spatial vs temporal latent; factorization vs 3D vs transformer; image-prior benefit/limits; fidelity/motion/consistency/identity axes; short-vs-long wall; reference/FiVE; joint-AV capability-level; compute envelope; duration!=coherence spine kept and deepened.
- Non-focus (§1/3/4/5/9/10/11/12/13/14/15 + front matter): verified byte-identical per-section.

## Exact transition audit (43; new LONGFORM vocabulary, prior classes not inherited)

- LONGFORM_SUBSTANTIVE: 33; BOUNDARY_LIMITED: 7; EVIDENCE_BLOCKED: 3.
- EVIDENCE_BLOCKED (reported to Sol, not filled): T-PAR-06 (EDM full body BT-D022 absent — preconditioning/schedule/solver ablations beyond abstract), T-EV-01 (D083 abstract-only, D086 tables unconsumed), T-EV-02 (D089 snippet-only, D091 gated).
- Canonical file: `execution/depth-audit-issue529/longform-depth-audit.json` (+ `.md` companion).

## Evidence-blocked items

- Above 3 transitions. Expansion without new retrieval is forbidden; manuscript marks consumption levels; evidence-side re-consumption is future work outside this bounded pass.

## PDF before/after metrics

- Total: 65 → 73 pages (+8, within +8..12 outcome guide; observation, not target). CI PASS both, 0 blocking + 0 layout findings both.
- Body: ~59 → ~67 (refs ~8 stable). §2: 4→6pp; §6: 4→6pp; §7: 4→6pp; §8: 4→5pp (TOC-derived).
- Prose: main.tex 293701 → 337126 bytes (+43KB, all in 4 focus chapters); extracted text r2 200473 chars → (r3 count in build driver context).
- Transition classes: r2 (24 SUBSTANTIVE/16 COMPRESSED/3 BOUNDARY/0 UNDER) → Issue529 (33 LONGFORM_SUBSTANTIVE/7 BOUNDARY_LIMITED/3 EVIDENCE_BLOCKED) under stricter bar.
- r2 candidate `c3a01a5b` (65pp) superseded by `8a3ed52a57df8ca5` (73pp); prior bytes in git history + review records.

## Validator results

- Manuscript manifest, deterministic ×4, quality bundle, surface review, surface gate, semantic (9 PASS), visual (5 PASS, incl. refs author-rendering regression + full-page scan).
- Stage validations (reader-publication-529, publication-candidate-529) PASS; advances DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE PASS.
- Final `validate_agent_state`: clean. Prose QA: 0 leaked IDs outside autocite, 0 TODO, 0 superlatives, 0 stale-provenance phrases, 139/139 citation coverage intact, no uncited/undefined keys.
- Visual regression: TOC, §2/§6/§8 openings, table pages, refs beginning/middle/end rendered and inspected; no clipping/overflow/blank-systematic defects (refs tail p73 sparse by single-entry tail, acceptable).

## Final stop state

- RELEASE_CANDIDATE, architecture_review approved, publication_preview pending, HUMAN_GATE_REACHED.
- Review index: ARCH r1 APPROVED; PUB r1 REQUEST_CHANGES (Human); PUB r2 REQUEST_CHANGES (Human, this session). Next Human decision records publication-r3.
- Semantics: `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`. No preview approval fabricated. Freeze/Release/merge/release-record: none, prohibited and not entered.

## Final remote HEAD/tree

- (recorded after push)
