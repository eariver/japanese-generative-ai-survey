# Draft guard handoff — mandatory regression constraints for next fresh Draft (§8)

以下は次fresh Draftへの必須制約（今回実行しない。旧r4 Draftは再利用・patch禁止）。

- LLaVA training topology: Stage 1両frozen＋Wのみ／Stage 2 encoder-frozen継続＋W/LLM更新
  （system-level end-to-end表現とcomponent-level更新の混同禁止）
- VQA v2 complementary image pairs（評価条件の正確な扱い）
- DINOv2 masked patch feature prediction vs pixel reconstruction（区別の維持）
- P07B taxonomy mapping（card範囲を超える細粒度diagnosticの持ち込み禁止）
- P09 input/fusion scope（契約範囲の遵守）
- P10 causal attribution＋editorial synthesis attribution（correlationから
  language-prior causal mechanismを断定しない；attribution明示）
- OpenVLA real-robot task success terminology（用語の正確性）
- Genie 3 no latent-action inference（断定しない）
- standard Japanese ML/CV terminology（terminology-map準拠）
- semantic repetition reduction（per-contract single disclaimer）
