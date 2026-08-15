# 2026-W33 X Trend Sensor Run Instruction — v0.4

このRunは `2026-W33` のX Trend Discoveryを行うためのissue-specific instructionです。

Instruction ID:

`2026-W33-grok-trend-v0.4-2026-08-15`

## 1. 使用するPrompt

以下を読み、その指示に従ってください。

`config/prompts/grok/x-trend-sensor-v0.4.md`

Authority / Context:

- `docs/editorial-specification.md`
- `docs/editorial-style-guide.md`

Prompt SHA-256:

`sha256:823dfc4ee31676caa7fac17e6d655ff1323209940ccb5a7378a99fc13bf1b89e`

## 2. Observation Window

今回のObservation Window Start:

`2026-08-09T23:40:00+09:00`

Editorial Cutoff:

`2026-08-14T18:00:00-04:00`

重要:

- Release/Event dateとX momentum dateを分離してください。
- Cutoff後、実際の観測時刻までに急浮上した重要事項は `Late Breaking` として分離してください。
- Underlying EventがWindow以前でも、今回のWindow中にtechnical-community momentumが生じた場合は候補になり得ます。
- Window開始以前の既存Rawを、今回の検索結果の代用として再利用しないでください。

## 3. Coverage

`x-trend-sensor-v0.4.md` のCoverage Scan、Media Generation Second Pass、Candidate Pool、Global Ranking、Coverage Auditを省略せず実行してください。

Laneが弱い場合は `NONE_FOUND` / `UNCERTAIN` を使用し、枠を埋めるために弱い候補を昇格させないでください。

## 4. Evidence boundary

この出力はTrend Candidate / Raw Observationです。

- Technical Factの最終Evidenceではありません。
- release date、parameter count、license、benchmark score、hardware requirement等は後段でprimary-source verificationします。
- X Post内の主張を、そのまま技術的事実へ昇格させないでください。

## 5. Output

出力ファイル名:

`x-trend-sensor-2026-08-15-v0.4.md`

想定Repository path:

`sources/2026-W33/grok/raw/x-trend-sensor-2026-08-15-v0.4.md`

同名ファイルが既に存在する場合は上書きせず、`-r2` 等のsuffixを追加してください。

Front Matterには少なくとも以下を含めてください。

```yaml
sensor: grok
prompt_version: x-trend-sensor-v0.4
issue_id: "2026-W33"
observation_window_start: "2026-08-09T23:40:00+09:00"
editorial_cutoff: "2026-08-14T18:00:00-04:00"
status: raw
```

`observed_at` は実際にGrokが観測を完了した時刻を記録してください。Run Instruction生成時刻を代入しないでください。

## 6. Completed run provenance

このinstruction JSONは実行前metadataです。Grok実行完了後は、`schemas/collector-run.schema.json` に従う別のrun provenance recordで、実際の `observed_at`、出力path、SHA-256、bytes、実行結果を記録してください。

## 7. Final artifact

最終成果物はチャット本文へ貼らず、実際のMarkdownファイルとして提示してください。

GitHubへのPushは試みないでください。Raw fileは後段でwrite-capable toolがRepositoryへ取り込み、SHA-256 provenance indexへ追加します。
