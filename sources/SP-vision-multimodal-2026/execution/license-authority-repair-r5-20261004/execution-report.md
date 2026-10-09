# Final execution report — TS-003 Final License Authority Repair (日本語)

## 起点 / 終点

- Starting HEAD / Tree: `089af4726d21575a40130e37adf367c90d26e475` /
  `344674e32b495da68c52459b568fbb2c23dd830e`（remote一致をread-only確認）
- Final HEAD / Tree: `3de418c4c87b7343f079ba615d698b6b5b30fa54` / `114df7ecef9b072cb9146642ab536cc676ea4417`（remote一致確認済み、working tree clean）

## 修正内容

- D074 old/new Evidence SHA: `a05409d2a4a8` → `76ec39d0b998`
- D075 old/new Evidence SHA: `ae9c79b3cf3f` → `a9518ae9d571`
- old/new Evidence result-set SHA: `446f359c7265` → `d62028f5f68f`
- exact official license sources + historical revision/date + snapshot hashes:
  `evidence-authority-supplement-vm-d074.json`（4 sources: repo LICENSE current +
  2024-09-06 pinned + 8B card current + 2025-10-11 pinned）,
  `evidence-authority-supplement-vm-d075.json`（4 sources: repo LICENSE current +
  2025-09-22 pinned + 30B card current + 2025-09-20 pinned）。全てfirst-party、
  正確バイトhash-bind済み（snapshots/）。
- D074 code readback: Apache 2.0 repo-bound（2024-09-06以降不変）。
  D074 weight readback: 8B-Instruct（4B sibling確認）card apache-2.0、
  bound artifactのみ。checked外への一般化なし。
- D075 code readback: Apache 2.0 repo-bound（2025-09-22以降不変）。
  D075 weight readback: 30B-A3B-Instruct card apache-2.0、
  bound artifact `model-00001-of-00015.safetensors` のみ。
- PROJECT_CLAIM vs pipeline-state分離: 両カードから
  `... remains unresolved in canonical Evidence` 系文言を除去。
  living-surface caveatsは維持。
- unaffected Evidence count: 110件 basis除きbyte-identical（検証済み）。
- Selection semantic diff: 0（112 selected維持、disposition/placement不変）。
- Architecture semantic diff: basis再bind＋P09ライセンスbucket更新のみ
  （Qwen3-VL weights resolved、Qwen3-Omni weights resolved、
  旧scoped companion除去）。他は不変。
- P09 final bucket state: Qwen3-VL code確認済み／weightsはbound scope内Apache 2.0；
  Qwen3-Omni code確認済み／weightsはbound scope内Apache 2.0；
  Molmo 2現行bucket維持；InternVL file-level PARTIAL/INSPECT維持。
  包括文への潰しなし。
- G06 still resolved（stale 0件）。G01/G02 preserved（residual維持）。
- P15 39-authority map preserved（49 refs / 39 distinct）。16 skeleton preserved。
- Summary/Attention regenerated（Core-derived; READYはmachine readiness）。
- shared Core changed: NO。Draft changed: NO（TeX/PDFなし）。
- lifecycle `ARCHITECTURE_ESTABLISHED`。r5 PENDING（r5 recordなし）。

## Rewind

- 正式path неприменим（fail-closed probe、zero writes）→ §2事前承認により
  Core-controlled rewind（CANDIDATES_NORMALIZED）＋replay完遂。
  Human-gate decision生成なし。manual編集なし。
