# Draft guard handoff — mandatory regression constraints (§11, preserved)

旧r4 Draftは再利用・patch禁止。次fresh Draftの必須制約（今回実行しない）。
Prior runs' guard files (`sync-repair-r5-20261004/draft-guard-handoff.md`,
`blocker-repair-r5-20261004/draft-guard-handoff.md`) remain in force; this run adds:

- LLaVA parameter-level freeze topology（Stage 1/2のfreeze/topology正確性）
- VQA v2 complementary image pairs（評価条件の正確な扱い）
- DINOv2 iBOT masked patch token prediction, not MAE-like pixel reconstruction
- P07B taxonomy/model mapping（card範囲遵守）
- P09 input/fusion boundary; TTS generation-side overexpansion禁止
- HallusionBench multi-failure diagnostic framing（単因果還元禁止）
- P10 cross-benchmark workflowはeditorial synthesis / INFERENCEとして扱う
- OpenVLA = real-robot task-success evaluation（用語正確性）
- Genie 3内部latent-action architectureを推測しない
- standard Japanese ML/CV terminology
- semantic repetition削減
- large ATTRIBUTED blockをclaim単位で分割
