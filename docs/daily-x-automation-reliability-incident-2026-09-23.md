# Daily X 自動実行欠落事象と信頼性対策案 — 2026-09-23

Status: `INCIDENT_NOTE / MITIGATION_PROPOSAL / BRANCH_LOCAL_ONLY`

Branch: `agent/daily-x`

Date: `2026-09-23 JST`

## 1. 目的

2026-09-21 および 2026-09-23 の Daily X 朝刊自動実行で、当日入力が Google Drive に存在し、自動実行自体も起動していたにもかかわらず、Git / Drive に成果物が残らない欠落事象が発生した。

本書は、現時点で確認できている事実、原因評価、再発防止案を `agent/daily-x` branch 内に残し、後続セッションが会話履歴なしで再開できるようにするための incident note である。

本書の対策は **proposal** であり、`docs/daily-x-compilation.md` の正式手順変更はまだ行わない。また、この記録を `main` にマージしない。

## 2. 影響範囲

### 2.1 2026-09-21

- 当日入力 `2026-09-21_0700.md` は Google Drive `DailyX` フォルダに 2026-09-21 07:05 JST 頃には存在していた。
- Daily X recurring automation は同日朝に起動していた。
- しかし自動実行後、以下は存在しなかった。
  - `sources/daily-x/2026-09-21/2026-09-21_0700.md`
  - `surveys/daily-x/2026-09-21/`
  - `DailyX-2026-09-21.pdf`
- 後続の手動 backfill では同じ入力から正常に編纂できた。
- backfill commit: `bb804892bcdf3bab5610f76e536bed8f216959c1`

### 2.2 2026-09-23

- 当日入力 `2026-09-23_0700.md` は Google Drive `DailyX` フォルダに 2026-09-23 07:16:19 JST 頃には存在していた。
- Daily X recurring automation は 2026-09-23 07:26:49 JST 頃に起動した記録がある。
- したがって、automation 起動時点で当日入力は存在していた。
- しかし自動実行後、以下は存在しなかった。
  - `sources/daily-x/2026-09-23/2026-09-23_0700.md`
  - `surveys/daily-x/2026-09-23/`
  - `DailyX-2026-09-23.pdf`
- 後続の手動 backfill では同じ入力から正常に編纂できた。
- backfill commit: `8d255a398d238fab4026b36188071de120f5ee06`

## 3. 確認できたこと

### 3.1 入力欠落ではない

9/21、9/23 とも、自動実行時点で当日 07:00 版入力が利用可能だった。したがって `docs/daily-x-compilation.md` に定義されている「当日入力が見つからない場合の正常 skip」には該当しない。

### 3.2 recurring automation の無効化ではない

調査時点で Daily X recurring automation は `is_enabled: true` であり、欠落日は automation 停止・無効化によるものではない。

### 3.3 Git 永続化より前に終了している

欠落日の自動実行は source / TeX commit を一切残していない。このため、少なくとも現行実行順序では、最終 commit より前の処理中にセッションが終了したと考えられる。

### 3.4 手動 backfill で LuaLaTeX 初回タイムアウトを再現

9/21 および 9/23 の手動 backfill では、初回の LuaLaTeX / `latexmk main.tex` 実行時に、実行環境側の TeX / font database 初期化で長時間を消費し、初回ビルドがタイムアウトする挙動を観測した。

同一成果物を再実行すると、font cache が生成された後は正常に PDF をビルドできた。

これは「TeX本文の構文エラー」ではなく、cold runtime における初回 font/cache 初期化コストと整合する。

## 4. 原因評価

### 4.1 最有力原因

**cold な実行環境で LuaLaTeX の font database / cache 初期化が発生し、初回 `latexmk main.tex` が実行時間上限に達した可能性が高い。**

根拠:

1. 当日入力は automation 起動時点で存在していた。
2. automation は有効で、実際に起動記録がある。
3. 自動実行では Git / Drive に成果物が一切残っていない。
4. 同日入力を使った手動 backfill で、初回 LuaLaTeX の font DB 初期化によるタイムアウトを再現した。
5. 同じ TeX を再実行すると正常終了した。

### 4.2 確定できない点

automation run の詳細な tool-call transcript / exception log を現在の実行環境から取得できないため、上記は **再現事象に基づく最有力仮説** であり、scheduler 側ログによる100%の root-cause confirmation ではない。

9/21 と 9/23 が完全に同一原因だったことも断定しない。

### 4.3 被害を拡大した要因

現行手順では、source / TeX の Git 永続化が PDF ビルド・検査に近い後段まで行われないことがある。

そのため build 前後でセッションが失敗すると、入力を取得して TeX を生成済みであっても repository 上には何も残らず、外部からは「何も実行されなかった」ように見える。

## 5. 対策案

### A. LuaLaTeX build の bounded retry

`latexmk main.tex` が初回だけ timeout した場合、同一 edition に対して **1回だけ再試行**する。

再試行対象は以下に限定する。

- process timeout
- font database / font cache 初期化を示すログがある場合
- 初回ビルドで PDF が生成されず、TeX構文エラーが明確に出ていない場合

構文エラーや missing file などの deterministic failure を無条件に再試行しない。

目的は、cold runtime の一度きりの初期化コストを吸収することであり、無限 retry を導入することではない。

### B. TeX / font cache の pre-warm

本番 `latexmk main.tex` の前に、LuaLaTeX / luaotfload の font cache を軽量に warm-up する工程を検討する。

候補:

- 小さな LuaLaTeX smoke document の1回コンパイル
- 環境で利用可能なら `luaotfload-tool` による cache 準備

ただし warm-up 自体が長時間化する可能性があるため、これにも上限時間を設ける。

優先順位としては、まず A の bounded retry を実装し、その後必要なら B を追加する。

### C. build 前の persistent checkpoint

入力取得・機械的 intake check・TeX生成が完了した時点で、PDFビルド前に repository へ状態を永続化する。

推奨案:

1. raw Grok Markdown を canonical path へ保存
2. TeX 一式を生成
3. source + TeX を checkpoint commit
4. PDF build / visual QA
5. レイアウト修正が必要なら追加 commit
6. validated PDF は従来どおり Git に commit せず Drive へ upload

これにより build が失敗しても、次回セッションは repository から再開できる。

Daily X は毎日独立した edition なので、1 edition あたり commit が1つ増えるコストより、完全消失を防ぐ利点の方が大きい。

### D. failure checkpoint の明示

build / Drive upload / connector failure が発生した場合、可能であれば repository に短い failure checkpoint を残す。

最低限記録する項目:

- edition date
- input filename
- last completed stage
- failure stage
- retry performed / not performed
- PDF generated / not generated
- Drive uploaded / not uploaded
- automation state を変更していないこと

配置先は将来的に `docs/checkpoints/` または edition-local execution metadata を検討する。

### E. recurring automation state を run failure と分離

per-run failure はその日だけの failure とし、以下を禁止する。

- recurring automation の disable
- pause
- stop
- delete
- deactivation

この invariant は現在の automation prompt と整合しており、今後も維持する。

### F. resume-first recovery

翌日以降に欠落を発見した場合、まず canonical path の存在を確認し、partial source / TeX が残っていればそこから resume する。

何も残っていない場合のみ Drive の authoritative intake から backfill する。

## 6. 推奨実装順

1. **C: build 前 persistent checkpoint**
   - まず「何も残らない」failure mode をなくす。
2. **A: `latexmk` bounded retry**
   - cold font cache に対する直接対策。
3. **B: optional pre-warm**
   - retry 発生率が高い場合に追加。
4. **D: failure checkpoint**
   - 診断可能性を上げる。
5. **F: resume-first recovery**
   - partial state を安全に再利用する。

## 7. 受け入れ条件案

対策実装後は最低限、以下を満たすこと。

- cold runtime で初回 LuaLaTeX が timeout しても、1回の bounded retry で継続可能。
- retry でも失敗した場合、raw intake と TeX が Git に残り、次セッションで resume 可能。
- TeX 構文エラーを retry で隠蔽しない。
- generated PDF は Git に commit しない。
- validated PDF だけを Drive に保存する。
- same-day Drive PDF の重複を増やさない。
- per-run failure で recurring automation を無効化しない。
- failure 後も翌日の scheduled run が通常どおり実行される。

## 8. 非対象

本 incident 対策では以下を変更しない。

- Grok Markdown を authoritative intake とする責務境界
- Daily X で独自のWeb/source validationを追加しない方針
- TeXレイアウト要件
- PDFをGitへcommitしない方針
- Weekly / Special pipeline
- `main` branch

## 9. 関連 state

- Daily X operational procedure: `docs/daily-x-compilation.md`
- 2026-09-21 backfill commit: `bb804892bcdf3bab5610f76e536bed8f216959c1`
- 2026-09-22 successful daily commit: `f5fb14dc6574fc5eb215dec73539772b666d22e4`
- 2026-09-23 backfill commit: `8d255a398d238fab4026b36188071de120f5ee06`

## 10. Current decision

現時点では、本書を `agent/daily-x` にのみ保存する。

`main` への merge、PR作成、正式手順への変更は行わない。

次に対策を実装する場合は、本書を設計根拠として `agent/daily-x` 上で bounded に変更し、実運用で再発率を確認してから、必要に応じて正式手順への反映可否を判断する。
