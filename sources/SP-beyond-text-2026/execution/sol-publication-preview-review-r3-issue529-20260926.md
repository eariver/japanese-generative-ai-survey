# Sol Publication Preview Review r3 — Issue #529

Status: `PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW_DECISION_R3`

Edition: `SP-beyond-text-2026`
Branch: `special/beyond-text-2026-work`
Issue: `#529 — [Depth][TS-002][Special] Beyond Textの中核4章をLONGFORM_SPECIAL相当のsemantic depthへ増補する`
Reviewed branch HEAD before this review record: `63dfd441c0cdd4ca8119e920073c9f7d1b3f1e65`
Reviewed tree: `6669ba5ce2fc6d04d4cac1fc9b03483bdea53176`
Reviewed main: `0bbb02b3c5963403860897daec2feaf61e82589a` / tree `e4ddde5ed5059d303b818f54e27204369b256bcb`

## 1. Disposition

Issue #529 is satisfied at the bounded manuscript-repair level. The revised Publication Preview is suitable for Human Publication Preview review.

This PASS does **not** approve the Publication Preview on behalf of the Human Owner. `publication_preview` remains pending and Freeze/Release remain unauthorized until the Human Owner makes the next gate decision.

## 2. Change containment

Compared with the Issue #529 starting authority `05b010c39edf81473761e75b6ce37b71fe41f4cc`, the reader-facing changes are confined to:

- `surveys/special/beyond-text-2026/main.tex`
- `surveys/special/beyond-text-2026/main.pdf`

`references.bib` remains unchanged from the repaired r2 version. Other changed files are canonical Human revision records, validation/checkpoint artifacts, longform depth audit, and production-state derivatives.

The manuscript delta is +194 / -18 lines and the session report records +43 KB of prose confined to §2 / §6 / §7 / §8, with non-focus sections byte-identical.

## 3. Issue #529 focus-chapter review

### §2 — Generative paradigms and objectives

PASS.

The revised text now separates the design axes the Issue requested:

- architecture/backbone,
- training objective,
- probability/path formulation,
- inference/sampling,
- representation space,
- few-step execution.

Specific read-back findings:

- DDPM is described with fixed Gaussian forward process, learned reverse process, and the simplified noise-prediction objective.
- DDIM is explicitly identified as an inference/sampling-side transition that does not replace the training objective.
- classifier guidance and classifier-free guidance are separated as different conditioning/guidance mechanisms.
- score-SDE is described as a continuous-time unification with predictor-corrector and probability-flow ODE views.
- EDM is intentionally bounded to abstract-level framing because BT-D022 full-body design-space evidence is unavailable.
- LDM is explicitly described as a representation-space transition rather than a replacement of diffusion itself.
- DiT is treated as a backbone-axis change, while SiT/interpolant and flow-matching/rectified-flow are treated as objective/path-formulation changes.
- consistency/distillation/few-step execution is connected to inference cost rather than confused with backbone changes.

The section now reads as a sequence of bottleneck → mechanism → changed axis → improvement → residual/trade-off → inheritance rather than a model-name chain.

### §6 — Speech / Voice

PASS.

The revision makes the modeling position explicit across waveform, acoustic/mel, neural vocoder, end-to-end, semantic/acoustic/codec tokens, codec LM, flow-based completion, streaming, and full-duplex systems.

It distinguishes:

- sample-level autoregressive waveform cost,
- acoustic-intermediate + vocoder division of labor,
- end-to-end integration,
- semantic vs acoustic vs neural-codec token roles,
- zero-shot speaker/context conditioning,
- speaker similarity vs content fidelity,
- streaming causality/latency constraints,
- full-duplex turn-taking / interruption / overlap constraints.

PARTIAL records BT-D059 and BT-D134 remain fenced; the revision does not upgrade their evidence level.

### §7 — Music / General Audio

PASS.

The revision now separates local acoustic fidelity from long-range musical structure, and separates generation / continuation / editing / control. It also separates text-audio alignment from musical coherence and explicitly refuses to treat supported duration as evidence of long-range structure.

Evaluation is decomposed into sound quality, alignment, structural control, and human preference, with incompatible conditions kept non-comparable.

### §8 — Video

PASS.

The revision now treats spatial latent and temporal compression as separate design concerns and distinguishes 2D+temporal factorization, spatiotemporal/3D modeling, and transformer-based temporal modeling. It also separates:

- frame fidelity,
- motion quality,
- temporal consistency,
- object/identity persistence,
- short-clip vs long-horizon behavior,
- conditioning/reference/editing,
- audio-video synchronization,
- compute/memory/runtime envelope.

The two critical Issue #529 boundaries are preserved and strengthened:

- `maximum supported duration != demonstrated coherence`
- `fixed short-frame training != long-horizon consistency`

Closed systems remain capability/workflow/lifecycle evidence only; no hidden architecture inference was introduced.

## 4. Longform depth audit

The Issue #529 audit uses a stricter vocabulary rather than inheriting the old r2 classes:

- `LONGFORM_SUBSTANTIVE`: 33
- `BOUNDARY_LIMITED`: 7
- `EVIDENCE_BLOCKED`: 3

The three `EVIDENCE_BLOCKED` transitions are acceptable because the missing depth is evidence-side rather than prose-side:

- `T-PAR-06`: EDM full-body design-space/ablation evidence absent (BT-D022 remains PARTIAL/abstract-level).
- `T-EV-01`: evaluation source body/tables not fully consumed.
- `T-EV-02`: locator/snippet/gated evaluation authority remains incomplete.

No unsupported prose was generated to hide these gaps.

## 5. PDF / visual review

The exact rebuilt CI artifact was inspected.

- pages: 73
- page size: A4
- PDF is not encrypted
- fonts are embedded
- focus chapter allocation: §2 ≈ 6 pp, §6 ≈ 6 pp, §7 ≈ 6 pp, §8 ≈ 5 pp
- bibliography remains the repaired r2 bibliography
- no clipping, overflow, systematic blank pages, broken glyphs, or table-margin failures observed in the focus-page visual read-back
- additional pages are substantive prose/tables, not padding

The growth from 65 to 73 pages is therefore an effect of the bounded longform expansion, not a page-count target or artificial filler.

## 6. Gate state

Production state is correctly stopped at:

`RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending / HUMAN_GATE_REACHED`

Architecture review remains approved. Publication Preview remains pending. Freeze and Release remain pending.

## 7. Sol conclusion

Issue #529's longform-depth concern is resolved for the current bounded authority. The remaining `EVIDENCE_BLOCKED` items are explicitly represented as evidence limitations and do not constitute hidden manuscript omissions.

Final Sol disposition:

`PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW_DECISION_R3`

The next action is Human review of the exact 73-page Publication Preview PDF. No Freeze/Release action is authorized before that Human decision.
