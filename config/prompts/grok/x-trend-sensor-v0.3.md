# X Trend Sensor Prompt v0.3

Status: Current Grok execution prompt  
Supersedes: v0.2 for future runs  

## 1. Base instructions

まず、このRepository内の以下のファイルを読んでください。

- `config/prompts/grok/x-trend-sensor-v0.2.md`
- `docs/editorial-specification.md`

v0.2の **Sections 2–7, 9–10** に記載された調査目的、観測対象、Trend判定、出力項目、Overall X Trend、事実と推測の分離に関する方法論を適用してください。

ただし、v0.2に直接記載されている **2026-W32固有の日付・時刻は過去回の値なので再利用しないでください。**

また、v0.2の **Section 11「GitHubへの保存」も使用しないでください。** GitHub ConnectorはRead-Onlyとして扱い、GitHubへの作成・更新・Pushを試みないでください。

このv0.3の指示が、v0.2と矛盾する場合はv0.3を優先してください。

---

## 2. 今回の観測期間をRepositoryから決定する

### Editorial Cutoff

`docs/editorial-specification.md` に従い、通常のEditorial Cutoffは

```text
Friday 18:00 America/New_York
```

です。

実行時点から見て直近の、すでに到来したFriday 18:00 America/New_Yorkを今回の通常Editorial Cutoffとしてください。

### Observation Window Start

Repository内の

```text
sources/*/grok/raw/x-trend-sensor-*.md
```

を確認し、**直前の正常なRaw Observation** のFront Matterにある `observed_at` を今回の観測開始時刻の第一候補としてください。

原則：

```text
previous successful Grok observation
    -> current observation
```

ただし通常枠とLate Breakingの境界はEditorial Cutoffです。

直前のRaw Observationが存在しない場合のみ、今回のEditorial Cutoffのおよそ1週間前から広めに観測してください。その場合、開始時刻が暫定値であることをFront Matterまたは本文で明記してください。

### Late Breaking

今回のEditorial Cutoffより後、実際の観測時刻までに急浮上した重要トピックは、v0.2の方針に従って **Late Breaking** として通常枠から分離してください。

### 重要

Release Dateではなく、今回のObservation Window中における

- `X Momentum Started`
- `X Peak`
- `Why Now`

を重視してください。

Underlying Eventが前回Cutoff以前でも、今回の観測期間に技術コミュニティで本格的に話題化した場合は対象です。

---

## 3. 最終成果物は必ずMarkdownファイルとして提示する

調査結果は、**チャット本文へ全文を貼り付けないでください。**

最終成果物は必ず `.md` のMarkdownファイルとして生成し、ユーザーがそのファイル自体を取得・添付・転送できる形で提示してください。

これは必須要件です。

### 禁止

- 調査結果全文を通常のチャット回答として貼り付ける
- Markdownコードブロック内に全文を貼り付ける
- 「以下をコピーしてファイルにしてください」とユーザーへ依頼する
- GitHubへのPushを試みる
- 調査結果を要約してからファイル化する

### 必須

- 調査結果全文を1つの `.md` ファイルとして生成する
- Raw Observationとして、調査結果を省略せず保存する
- ユーザーには**ファイルそのものを提示する**
- チャット本文には、ファイル生成完了とファイル名だけを簡潔に伝える

**テキスト貼り付けではなく、ファイル提示を最優先してください。**

---

## 4. ファイル名

原則として以下の形式にしてください。

`x-trend-sensor-YYYY-MM-DD.md`

`YYYY-MM-DD` は実際に観測を実施した日付としてください。

Rawファイル名はIssue IDではなく観測日を基準にします。

---

## 5. Front Matter

生成するMarkdownファイルの先頭に、必ず以下のYAML Front Matterを付けてください。

```yaml
---
sensor: grok
prompt_version: x-trend-sensor-v0.3
observed_at: "<実際に調査を行った日時。可能ならISO 8601、timezone付き>"
observation_window_start: "<Repository上の直前観測から決定した開始時刻>"
editorial_cutoff: "<今回のFriday 18:00 America/New_York>"
repository: "eariver/japanese-generative-ai-survey"
status: raw
---
```

日時が厳密に分からない場合は推測で補完せず、分かる粒度で記載してください。

`status` は必ず `raw` としてください。

---

## 6. Raw Observationとして保持する

生成するファイルは後段のSource Verificationへ渡すための **Raw Observation** です。

したがって、以下を行わないでください。

- Evidenceとして確定する
- Primary Sourceの内容を確認したことにする
- 不明な日時やEngagementを補完する
- Trend Candidateを後から都合よく削除する
- Survey記事として文章を整える
- Chronologyへ確定Eventとして登録する

観測結果に不確実性がある場合は、v0.2のルールに従ってConfidenceやVerification Neededへ残してください。

---

## 7. GitHubへの搬送は後段で行う

あなた自身はGitHubへ書き込まないでください。

生成した `.md` ファイルはユーザーが別のAgent / ChatGPTへ渡し、後段で以下のような場所へRawのまま保存します。

```text
sources/<issue-id>/grok/raw/<generated-file-name>
```

この搬送工程を前提としているため、**ファイルの内容をチャット本文へ複製する必要はありません。**

---

## 8. 最終回答

調査とMarkdownファイル生成が完了したら、チャット本文は短くしてください。

例：

> 調査が完了しました。Raw Observationを `x-trend-sensor-2026-08-16.md` として作成しました。ファイルを添付します。

この後に、**実際のMarkdownファイルを提示してください。**

調査結果全文を本文へ再掲しないでください。

---

## 9. 最重要事項

最終成果物は会話テキストではなく、**Markdownファイルです。**

ユーザーがそのまま別のChatGPTセッションへ添付できるよう、必ずファイルとして提示してください。

**「回答をMarkdown形式で書く」のではなく、「Markdownファイルを生成して提示する」ことを要求しています。**
