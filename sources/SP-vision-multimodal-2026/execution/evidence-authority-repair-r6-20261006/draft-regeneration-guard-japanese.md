# Japanese editorial guards for the post-r6 fresh Draft (record only, no prose regen)

Avoid in regenerated body prose:

- 証し (use 根拠 / 検証結果)
- 問いかけ (use 質問 / クエリ)
- 道具呼び出し (use ツール呼び出し)
- 開放的な課題非依存の学習 (explain open-ended / task-agnostic in standard terms fitting context)
- 模型の重み (use モデル重み)
- over-repeated templates: `論文著者は報告する`, `新たに可能になった`, `〜に委ねる`
  (vary with 著者らの評価 / 報告値 / 原論文では as appropriate)

Prefer standard technical Japanese; do not invent native-Japanese paraphrases for
established ML/CV terms. Preserve π₀ (not pi-zero) where typography permits.

Do NOT reduce attribution precision merely to vary prose: every varied paragraph
must keep its source attribution and boundary condition, and JSON evidence
bindings remain the authority.

Carried-over standing rules from prior revisions remain in force: no 管路 for
pipeline, 汎化 (not 般化), フレーム/フレームレート, open-vocabulary vs open-set
distinction, no internal workflow vocabulary in reader prose.
