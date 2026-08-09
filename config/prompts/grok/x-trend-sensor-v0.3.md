# X Trend Sensor Prompt v0.3

Status: Current Grok execution prompt  
Supersedes: v0.2 for future runs  

## 1. Base instructions

まず、このRepository内の以下のファイルを読んでください。

`config/prompts/grok/x-trend-sensor-v0.2.md`

v0.2の **Sections 1–10** に記載された調査目的、観測対象、Trend判定、出力項目、Late Breaking、Overall X Trend、事実と推測の分離に関する指示をそのまま適用してください。

ただし、v0.2の **Section 11「GitHubへの保存」だけは使用しないでください。**
GitHub ConnectorがRead-Onlyの場合を前提とし、GitHubへの作成・更新・Pushを試みないでください。

以下のSection 2以降が、v0.2 Section 11を完全に置き換えます。

---

## 2. 最終成果物は必ずMarkdownファイルとして提示する

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

## 3. ファイル名

原則として以下の形式にしてください。

`x-trend-sensor-YYYY-MM-DD.md`

`YYYY-MM-DD` は実際に観測を実施した日付としてください。

Issue IDが明示されている場合でも、Rawファイル名は観測日を基準にしてください。

---

## 4. Front Matter

生成するMarkdownファイルの先頭に、必ず以下のYAML Front Matterを付けてください。

```yaml
---
sensor: grok
prompt_version: x-trend-sensor-v0.3
observed_at: "<実際に調査を行った日時。可能ならISO 8601、timezone付き>"
observation_window_start: "<今回の観測開始時刻>"
editorial_cutoff: "<今回のEditorial Cutoff>"
repository: "eariver/japanese-generative-ai-survey"
status: raw
---
```

日時が厳密に分からない場合は推測で補完せず、分かる粒度で記載してください。

`status` は必ず `raw` としてください。

---

## 5. Raw Observationとして保持する

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

## 6. GitHubへの搬送は後段で行う

あなた自身はGitHubへ書き込まないでください。

生成した `.md` ファイルはユーザーが別のAgent / ChatGPTへ渡し、後段で以下のような場所へRawのまま保存します。

```text
sources/<issue-id>/grok/raw/<generated-file-name>
```

この搬送工程を前提としているため、**ファイルの内容をチャット本文へ複製する必要はありません。**

---

## 7. 最終回答

調査とMarkdownファイル生成が完了したら、チャット本文は短くしてください。

例：

> 調査が完了しました。Raw Observationを `x-trend-sensor-2026-08-16.md` として作成しました。ファイルを添付します。

この後に、**実際のMarkdownファイルを提示してください。**

調査結果全文を本文へ再掲しないでください。

---

## 8. 最重要事項

最終成果物は会話テキストではなく、**Markdownファイルです。**

ユーザーがそのまま別のChatGPTセッションへ添付できるよう、必ずファイルとして提示してください。

**「回答をMarkdown形式で書く」のではなく、「Markdownファイルを生成して提示する」ことを要求しています。**
