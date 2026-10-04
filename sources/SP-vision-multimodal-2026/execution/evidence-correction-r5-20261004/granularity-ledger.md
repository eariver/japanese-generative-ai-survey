# P05/P06/P08 Evidence-granularity audit ledger — evidence-correction-r5

Method: CURRENT working-tree Draft sentence → accepted Card claim/metric/limitation →
verdict (supported / unsupported / over-specific) → disposition
(strengthen-Evidence / delete-from-Draft / hold). Full statement-level mapping was
produced read-only by an independent mapping pass (see §A summaries); dispositions below
are worker decisions under §6 (load-bearing FULL/TRANSITION mechanism first; no mechanical
prose-exists-so-expand). Depth classes: P05 FULL=VM-D026/027/028, TRANSITION=VM-D023/024/025;
P06 FULL=VM-D030/036, TRANSITION=VM-D033/034/035; P08 FULL=VM-D059/062, BRIEF=VM-D061.

## Dispositions: strengthen-Evidence (STAGED in staged-cards/, canonical-validated)

1. VM-D062 LLaVA (FULL, mandatory §4): old `end-to-end vision-encoder+LLM tuning` claim-1
   REMOVED as factually wrong. Replaced with 6 trackable claims: instruction-data generation
   (GPT-4-only teacher, caption+box symbols, COCO, 158K=58K/23K/77K) / architecture-interface
   (ViT-L/14 + Vicuna via W) / Stage 1 (both frozen, W-only, 595K) / Stage 2 (encoder frozen,
   W+LLM, 158K/ScienceQA) + system-vs-component distinction / eval conditions (85.1% protocol,
   92.53% ensemble, Bench limits) / X01 supervision-contract INFERENCE. Limitation kept +
   paper Limits folded in.
2. VM-D061 MiniGPT-4 (BRIEF, mandatory §5 granularity): +claim-2 BLIP-2 ViT-G/14+Q-Former
   frozen provenance (querying inside frozen Q-Former; own path linear-only) / +claim-3
   two-stage data (5M; 3.5K/5K) / +claim-4 Q-Former-removal ablation variant note.
   Resolves `own-query-selection-less` vs `borrows-frozen-ViT+Q-Former` recurrence by
   level distinction (own path vs borrowed stack).
3. VM-D034 DINO (TRANSITION, §5): +claim-3 centering(teacher-only EMA)+sharpening pair
   necessity / +claim-4 temperature DIRECTION (teacher smaller/sharper; τs=0.1, τt 0.04→0.07;
   momentum λ 0.996→1) with explicit reversal of student-sharpen/teacher-smooth.
4. VM-D033 MAE (TRANSITION, §5): +claim-2 normalized-pixel FINAL target / +claim-3
   decoder-depth + mask-ratio ablations / +claim-4 linear-vs-finetune + DEFAULT-vs-FINAL.
5. VM-D024 LayoutLMv3 (TRANSITION): +claim-3 discrete codebook-token MIM target (8,192 vocab,
   blockwise ~40%), enabling the MAE-raw vs v3-discrete contrast.
6. VM-D028 GOT (FULL): +claim-3 synthetic data-engine composition (nuanced: rendered/
   pseudo-centered WITH Common-Crawl PDF extraction alongside).
7. VM-D108 DocVQA (BRIEF): +claim-3 ANLS one-line definition (DocVQA §5.1 scope; no threshold).
8. VM-D077 molmo2 repo (PARTIAL kept): +claim-3 weight-license bucket (Apache-2.0 +
   academic/non-commercial third-party caveat) / +claim-4 dataset-availability bucket
   (ODC-BY + output-ToS + CC BY-4.0 subset); limitation-1 narrowed to bucket-level bound
   with individual third-party texts unbound. NO Discovery mutation (all repo-linked
   first-party). Third-party per-set Discovery would need new Discovery — report-only.

## Dispositions: delete-from-Draft (post-r5 Draft revision handoff, §12 — NOT this run)

- Scale-tier catalogs (BASE/LARGE/HUGE, SMALL/BASE, 7B/13B), exact widths/layers/epochs
  (512/8L, 1600ep as prose, 40–80% sweep patter, 2+8 crop counts, 3-layer head, 30/60 Bench
  split, 5M/3500 as numbers), dataset-name provenance bundles (CC/SBU/LAION),
  SynthDoG element inventories, doc-type lists, span-split glosses, stop-control /
  hallucination causal glosses, triplicated definitions (ANLS×3, MAE pattern×2).
- Nougat S11 stop-control causality + S15 scale + S16 textbook-eval (unless paper-grounded).
- MiniGPT-4 provenance/count details beyond staged claims; S22 language-prior causality
  (re-hedge to limitation-1).
- GOT S15 training-distribution prose beyond staged claim-3; S16 per-signal list (keep quarantine).
- MAE bulk ablation catalog beyond staged claims 2–4.
- LLaVA linear-layer/Vicuna-tier/Bench-split enumerations.

## Dispositions: hold / compliant (no action)

- DocVQA 9-category EXISTENCE without bespoke breakdown: PASS (BRIEF).
- DocVQA MEDIUM/HIGH kept out of paper-fact voice: PASS (stay edition-INFERENCE if surfaced).
- Nougat/GOT quarantine discipline, DINO operator absence in current Draft, LLaVA closed/
  partner eval qualifiers, GOT compression numbers withheld to card: PASS.
- LLaVA S03 end-to-end contrast sentence: HOLD for card-sync post-acceptance (do not delete
  now; replace phrasing once corrected card is accepted).
- VM-D103 I-JEPA: card already holds `single context block → multiple target-block
  representations`; NO card change. Canonical wording readback for post-r5 Draft:
  `predict target-block representations from a single context block` (matches current
  Draft b3 `一つの文脈ブロックから目標ブロックの表現を予測し`).
- VM-D102 DreamerV3: current card (RSSM + imagination-based policy improvement with
  normalization/balancing/transformations + 150+ tasks + Minecraft diamond) is SUFFICIENT
  for post-r5 mechanism-depth restoration (current Draft b2 uses exactly this scope);
  NO expansion.

## §A. Statement-level mapping summaries (mapping pass evidence)

- LayoutLMv3 p05-b2: S02–S07/S11/S13 supported (backbone/objectives/ablation/future-work);
  over-specific S12/S15/S16 (discrete-token/BEiT lineage — now STAGED claim-3, flips to
  supported post-acceptance), S14 (tiers), S17 (task names), unsupported S19 (release).
- Donut p05-b3: S01–S03/S06–S08/S10/S12 supported (OCR-free/SynthDoG-existence/resolution);
  over-specific S11/S13/S18/S19/S23 (JSON/bbox-bypass, element inventory, dict-swap,
  finetune list, shared vocab) → delete-from-Draft.
- Nougat p05-b5/b7: contract/limits/quarantine supported; over-specific S11/S15/S16/S17 →
  delete (or paper-ground S11); gap note: card's Swin/Donut-lineage token exceeds Draft
  (Architecture relies on card — fine).
- GOT p05-b6/b7: theory/outputs/quarantine supported (S05/S12 correctly withhold numbers);
  over-specific S15/S16 → staged claim-3 covers composition; list → delete.
- DocVQA p05-b8: 50K/12K/9-existence/split/ANLS-use/baselines/open supported; S05 method-rule
  + S11 disclosure phrasing compliant; over-specific ANLS-tolerance×3 (staged claim-3 +
  consolidate), S15/S19 → delete.
- MAE p06-b3: asymmetric/75%/scale/reconstruction-caution supported; ablation bulk
  over-specific → staged claims 2–4 cover the review-listed 7 items; rest → delete.
- DINO p06-b4: emergence/numbers/naming/scope supported; operator sentences ABSENT
  (compliant); crop-count/head/prototype/eval-semantics over-specific → delete;
  operators staged (claims 3–4) for post-r5 depth option.
- MiniGPT-4 p08-b5: projection/two-stage/exhibits/restraint supported; provenance/count
  over-specific → staged claims 2–4; S22 causality → re-hedge.
- LLaVA p08-b6: instruction-data/eval-qualifier/open/Bench supported; S03 inherits
  known-wrong phrasing → hold-for-sync; composition over-specifics → staged claims 1/3/6;
  S20/S22/S23 enumerations → delete.
