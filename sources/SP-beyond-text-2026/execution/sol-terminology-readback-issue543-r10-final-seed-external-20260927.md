# TS-002 Issue #543 — Sol independent readback after Publication Preview r11

Date: 2026-09-27 JST  
Disposition: `REQUEST_CHANGES / FINAL_SEED_EXTERNAL_RESIDUALS_FOUND / HUMAN_R12_REQUIRED`

## 1. Reviewed authority

Repository: `eariver/japanese-generative-ai-survey`  
Branch: `special/beyond-text-2026-work`

Reviewed r11 worker commit:

`f81694363a6d6fc3456c96d77e02ee8360728ef1`

Reviewed tree:

`0041c7d06a6b19543c92c3340f6aae5db225f4a4`

Reviewed publication candidate:

- source SHA-256: `d3543075351e14aaf95c2ada8099ec8dd122fb01e879be236a5b6fa162672782`
- candidate SHA-256: `79c3a4fd9a2e9b948920dcd85004f8c22108dfbd2ca7ee268e91a2186140ec9b`
- PDF SHA-256: `4e2250677716fba5cbfe3ea0e57d9f2174e83a93a15a361d8fbae164bf45089d`
- pages: `78`
- status: `READY_FOR_PUBLICATION_PREVIEW`

Reviewed main remains:

`0bbb02b3c5963403860897daec2feaf61e82589a`

with tree:

`e4ddde5ed5059d303b818f54e27204369b256bcb`

## 2. Worker execution result

The Publication Preview r11 worker execution is accepted as mechanically correct.

Verified state after r11:

- canonical `publication-r11` Human `REQUEST_CHANGES` recorded
- regeneration boundary `DRAFT_COMPLETE`
- Architecture approval preserved
- Sol r9 C001-C007 applied
- r9 exact residual list zero
- terminology ledger retained 276 semantic rows without duplicating r9 decisions
- `DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE` completed through the frozen Core path
- Publication Preview remains pending
- Issue #543 remains OPEN
- no r12 synthesized
- no Freeze / Release / merge
- reviewed main unchanged
- Frozen Core v2 identities unchanged

Therefore the worker execution itself is not rejected.

## 3. Why Issue #543 still cannot close

Issue #543 requires Sol's independent seed-independent reader-facing scan, not merely zero counts for the worker's current dictionary.

That independent scan found additional residuals beyond Sol r9. They fall into four classes:

1. grammatical/lexical variants of already-decided guidance-scale terminology;
2. remaining literalized or unnatural technical prose (`焼き直し`, `報告掃引`, `鋭敏`);
3. generic `装置` wording where the bound concept is compute hardware/GPU;
4. one actual source-binding defect between LCM (`btd079`) and LCM-LoRA (`btd080`).

The authoritative resolution is recorded in:

`sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r10-r11-final-seed-external-20260927.md`

Map commit:

`b9c31e03844f923ef249ed9570b976c701180522`

## 4. Confirmed residual findings

### A. Guidance-scale family

The source still contains reader-facing variants such as:

- `尺度の掃引`
- `尺度感度`
- technical `誘導尺度`

These denote the same classifier-free/image guidance-scale concept already normalized elsewhere as `ガイダンススケール` / `ガイダンススケールのスイープ`.

Consumed `btd032` Evidence explicitly describes inference guidance with swept `w` and the resulting FID/IS trade-off, so these are not generic scale uses.

### B. Technical-copy residuals

The source still contains:

- `画像域での焼き直し`
- `焼き直し検証`
- `超解像のテキスト条件の有用性の焼き直し`
- `報告掃引の範囲`

These are reader-facing copy defects, not canonical technical terms. The Sol map provides source-preserving nonsemantic rewrites using `再検証` and `報告された範囲`.

### C. DiT hardware/evaluation wording

The source compresses the btd025 limitations into `装置依存` and `評価手順への鋭敏さ` / `評価手順に鋭敏`.

Consumed Evidence separates the underlying facts: throughput is hardware-bound, while FID is sensitive to the evaluation suite. The final reader wording therefore needs to preserve those identities rather than use literalized `鋭敏` phrasing.

### D. LCM / LCM-LoRA source-binding defect

Current source says:

`一段階の隔たりと誘導や刻みへの鋭敏さは、四段階実用と一段階研究の線引きを示す。`

but binds the sentence to `btd080` (LCM-LoRA).

Consumed Evidence shows:

- `btd079` / LCM: `1-step gap remains; solver/skipping/guidance sensitive; custom sets need finetuning without universal module.`
- `btd080` / LCM-LoRA: heuristic combination weights and per-model generality need validation; no new benchmark.

Thus this is a real citation/source-binding defect.

New bounded authority:

`SOL-CIT-005`: LCM one-step-gap / solver-skipping-guidance-sensitivity boundary -> `btd079`; LCM-LoRA heuristic combination-weight / per-model-generality boundary remains `btd080`.

No other new citation change is authorized.

### E. Compute-hardware terminology

Several remaining `装置` occurrences unambiguously denote compute hardware/GPU. The map normalizes only those bound contexts. In particular, consumed Wan2.2 Evidence states `80 GB single-GPU / 8-GPU multi-GPU`, so `単一80GBや複数装置` should retain the GPU identity instead of a generic `装置` label.

## 5. Core / lifecycle judgment

Frozen Core v2 remains immutable:

- implementation SHA `95c03bf5285cb4b2c1103a14c460574183a8cb93`
- pipeline `ee89796245c22072cec98f34931180214a4928c24f399280793cd6420a4c8e71`
- quality `b5b955d524fb438c0f1b2c9490bea1da2083e79028d67a55ca424bbfc20f2958`
- research `0f575e6d97caec72b2bf8b7f6b78a562d97ca67b2071193417b968ba3d73e6e8`
- publication `a6859559dd1b9d42ab8fb4402b74b7bdd8611dbe65c8e02a7b022b545c20f4eb`

No Core repair is required or authorized.

Because the edition is currently `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending`, the new Sol map cannot be applied under r11 without another Human Publication Preview decision. The frozen Core's canonical return path requires a new Human revision.

Sol does **not** synthesize that Human decision.

Required next Human action:

`Publication Preview r12 / REQUEST_CHANGES / regeneration boundary DRAFT_COMPLETE`

solely to apply the Sol r10 map and bounded `SOL-CIT-005`, then rerun the full terminology/citation/validation/PDF path.

## 6. PDF closure audit boundary

The r11 worker reports the regenerated 78-page PDF and visual QA as passing, and the candidate metadata is internally bound to the exact source/PDF hashes above.

However Sol found blocking source-level residuals before Issue #543 closure. Therefore a final closure-grade exact-PDF audit is not used to override the source finding; the PDF must be regenerated after the authoritative r10 corrections and then undergo the final Sol exact-PDF audit.

## 7. Final disposition

`REQUEST_CHANGES / FINAL_SEED_EXTERNAL_RESIDUALS_FOUND / HUMAN_R12_REQUIRED`

- r11 worker execution: accepted
- r11 candidate as Issue #543 final: rejected
- Issue #543: OPEN
- Human Publication approval: absent
- Freeze: unauthorized
- Release: unauthorized
- merge: unauthorized
- Core v2: immutable
