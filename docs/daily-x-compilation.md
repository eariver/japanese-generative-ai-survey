# Daily X 編纂手順（ChatGPT向け）

## 1. 目的と責務境界

Daily X は、Grok が X 上から収集した直近24時間の生成AI関連トピックを、毎朝数ページの日本語PDFへ編纂する軽量な日刊物である。

Daily X の編纂担当は **Grokの収集結果を記事へ変換すること**に専念する。週刊版で実施するような一次資料の再調査、ソース妥当性評価、Evidence chainの構築、重要度の再判定は原則として行わない。

Grok成果物を authoritative intake として扱う。ただし、次の機械的な整合性確認は行う。

- Run metadata と観測窓が存在すること。
- 観測窓が原則 `前日07:00 JST -- 当日07:00 JST` であること。
- Topics セクションを読み取れること。
- URLを新たに推測・生成しないこと。
- Grok自身が「観測窓外」「未確認」「一次投稿なし」等と明示している場合、その注記を消して確定事実のように書き換えないこと。

## 2. 毎朝の実行タイミング

定常運用では、Grok が毎朝 `07:00 JST` に収集を開始し、ChatGPT 側は `07:05 JST` に編纂を開始する。

Grok の通常実行は数分以内で完了する想定である。07:05時点で当日07:00版がまだ存在しない場合は、直ちに前日版へフォールバックせず、Google Drive の `DailyX` フォルダを再確認する。利用可能な当日入力が見つからない場合は、入力欠落として明示してその日の編纂を失敗扱いにする。

## 3. 入力

Google Drive の `DailyX` フォルダから対象日のMarkdownを取得する。

通常の主入力:

1. `YYYY-MM-DD_0700.md`
2. 同日07:00版に明示的な retry ファイルがあり、通常版が破損・不完全な場合は適切な retry を使用する。

09:00版は定常07:05編纂では使用しない。将来09:00版を別用途で生成する場合も、Daily X朝刊の既定入力は07:00版とする。

取得した原文は、改変せず次へ保存する。

```text
sources/daily-x/YYYY-MM-DD/YYYY-MM-DD_0700.md
```

retry を採用した場合は、実際の入力ファイル名を保持して保存する。

## 4. 出力ディレクトリ

各号は次の構成とする。

```text
surveys/daily-x/YYYY-MM-DD/
  .latexmkrc
  main.tex
  sections/
    00-introduction.tex
    01-*.tex
    02-*.tex
    ...
    99-conclusion.tex
```

共通TeXスタイルは `templates/daily-x/jgaidailyx.sty` を使用する。

生成PDFはビルド成果物であり、原則としてGitへコミットしない。

## 5. 記事構成

Grok Markdown の Topics を **記載順のまま**記事化する。Daily版では独自のランキングや並べ替えを行わない。

### 5.1 タイトル

1ページ目最上部に全幅で配置する。タイトル領域のみ1段幅を許可する。

- `生成AI Daily X レポート`
- 対象日
- 観測範囲
- 使用したGrok Run

### 5.2 序論

`sections/00-introduction.tex` に置く。

観測範囲全体で何が話題になっていたかを2--4段落で概観する。個別項目の羅列ではなく、複数トピックを横断する傾向を説明する。

### 5.3 個別トピック

Grokの各Topicにつき原則1セクションを作る。

- 見出しは日本語で簡潔にする。
- GrokのSummary / Evidence / observations を読みやすい説明文へ再構成する。
- 原則として1トピック150--350字程度を目安とし、重要項目は多少長くしてよい。
- Grokにある `Importance` や `Confidence` を毎回本文へ列挙する必要はない。
- `Unverified` な内容は「投稿では〜とされる」「〜との主張が共有された」のように、観測された主張として書く。
- `Confirmed` の場合でも、Daily版で追加検証は行わない。
- GrokにPrimary X postがある場合のみ `\dailyxsource` で掲載する。
- Primary X postが `未確認` / `N/A` の場合、URLを作らない。
- Grokが観測窓外と明示した投稿を根拠に含める場合は、その事実を短く注記する。

### 5.4 結言

`sections/99-conclusion.tex` に置く。

その日のX上の生成AI動向を2--4段落でまとめる。単なる記事一覧の再掲ではなく、観測日の特徴、複数トピックを結ぶテーマ、翌日以降も継続しそうな流れを述べる。

## 6. 文体

- 日本語の技術ニュース解説として自然な文章にする。
- 週刊版ほど学術的・監査的にはしない。
- 「何が起きた／何が話題だった／なぜ注目されたか」が短時間で分かることを優先する。
- Grokの文章を機械的に直訳せず、重複するEvidence/Follow-upを整理して読み物へ変換する。
- Daily版では独自のWeb検索を追加しない。
- Grokにない事実、数値、URLを補完しない。

## 7. TeXレイアウト要件

- A4縦。
- LuaLaTeX + LuaTeX-ja。
- タイトル領域のみ全幅。
- **序論から結言まで全て2段組。**
- 本文中で `\onecolumn` を使用しない。
- 長いX URLは `xurl` / `hyperref` で改行可能にする。
- 数ページ程度で毎朝読める密度を目標とする。
- `flushend` により最終ページの左右カラムを自動的に均衡させる。大きく崩れる場合は目視確認のうえ段落量を調整する。

`main.tex` の基本形:

```tex
\documentclass[10pt,a4paper]{ltjsarticle}
\usepackage{jgaidailyx}
\dailyxsetup{YYYY-MM-DD}{前日07:00 -- 当日07:00 JST}{YYYY-MM-DD 07:00 JST}
\begin{document}
\dailyxtitle
\input{sections/00-introduction}
\input{sections/01-...}
% Grok Topicsの順序を維持
\input{sections/99-conclusion}
\end{document}
```

## 8. ビルド

対象号ディレクトリで実行する。

```bash
cd surveys/daily-x/YYYY-MM-DD
latexmk main.tex
```

`.latexmkrc` からリポジトリ共通設定と `templates/daily-x` を参照する。

## 9. PDF確認

ビルド成功だけで完了にしない。

1. `pdfinfo main.pdf` でページ数・用紙を確認する。
2. `pdftotext main.pdf -` で文字化けや欠落を確認する。
3. PDFをPNGへレンダリングし、全ページを目視する。
4. 次を確認する。
   - タイトル以外が2段組である。
   - 見出し、本文、URLに重なり・はみ出しがない。
   - 日本語グリフが欠落していない。
   - 不自然な大空白や孤立見出しがない。
5. 問題があればTeXを修正し、再ビルド・再確認する。

## 10. Google Driveへの成果物保存

目視確認に合格した最終PDFを、入力Markdownと同じ Google Drive の `DailyX` フォルダ直下へアップロードする。

既定ファイル名:

```text
DailyX-YYYY-MM-DD.pdf
```

同名PDFがすでに存在する場合は、意図せず重複ファイルを増やさない。既存ファイルが同日の旧ビルドであることを確認できる場合は、同じDriveファイルを更新して置換する。判断できない場合は上書きせず、状況を報告する。

アップロード後は、Drive上でファイルの存在を読み戻して確認する。保存失敗を成功として報告してはならない。

## 11. 完了条件

以下をすべて満たした時点でDaily X編纂完了とする。

- 当日 `YYYY-MM-DD_0700.md` を主入力として取得できている。
- Grok原文が `sources/daily-x/` に保存されている。
- 対象日のTeX一式が `surveys/daily-x/` にある。
- 序論・全トピック・結言が揃っている。
- PDFが正常にビルドできる。
- タイトル以外が全て2段組であることを目視確認済み。
- Grokに存在しないURLや事実を追加していない。
- 最終PDF `DailyX-YYYY-MM-DD.pdf` が Google Drive の `DailyX` フォルダに保存され、読み戻し確認済みである。

## 12. Daily版とWeekly版の分離

Daily Xで未確認情報や弱いソースが含まれていても、それ自体を理由に編纂を止めない。Daily Xは「Xで何が話題になっていたか」を短い遅延で読むためのレポートである。

ソースの妥当性、一次情報との照合、採否、正確なタイムライン、Evidence chainは週刊版の編纂工程で扱う。
