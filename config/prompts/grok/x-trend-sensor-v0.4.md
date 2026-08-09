# X Trend Sensor Prompt v0.4

Status: Current Grok execution prompt  
Supersedes: v0.3 for future runs  

## 1. Authority and inherited rules

まず、このRepository内の以下のファイルを読んでください。

- `docs/editorial-specification.md`
- `config/prompts/grok/x-trend-sensor-v0.2.md`
- `config/prompts/grok/x-trend-sensor-v0.3.md`

このv0.4は、v0.3の以下の運用方針を継承します。

- Editorial CutoffとObservation WindowをRepositoryから決定する
- Release DateとX Trend Dateを分離する
- GrokをEvidence authorityではなくX Trend Sensorとして扱う
- GitHub ConnectorはRead-Onlyとして扱い、Pushを試みない
- 最終成果物はチャット本文ではなく、実際のMarkdownファイルとして提示する
- Raw Observationのまま後段へ渡す

v0.2の **Sections 2–7, 9–10** に記載された、調査対象、Trend判定、各トピックの出力項目、Overall X Trend、事実と推測の分離に関するルールも適用してください。

ただし、v0.2のW32固有の日付・時刻、およびSection 11「GitHubへの保存」は使用しないでください。

このv0.4がv0.2またはv0.3と矛盾する場合、**v0.4を優先してください。**

---

## 2. v0.4の目的：全分野を探索してからランキングする

このPromptの最重要変更点は、いきなり「AI全体のTop 10」を作らないことです。

LLM、Reasoning、Coding AgentなどはX上の絶対的な投稿量が多いため、全分野を単一ランキングで最初から競わせると、Multimodal、Image、Video、Audio、Inference、Open Weight等の重要トピックを探索段階で落とす可能性があります。

したがって、必ず以下の順序で調査してください。

```text
Stage 1: Coverage Scan
    -> Stage 2: Candidate Pool
    -> Stage 3: Global Ranking
    -> Stage 4: Coverage Audit
```

**Stage 1を完了する前にGlobal Rankingを作らないでください。**

また、最終ランキングでは単純な投稿総量だけを重要度とみなさないでください。

ある分野のXコミュニティがLLM分野より小さくても、その分野内で明確なMomentumが発生しているなら重要候補です。

絶対的な投稿量だけではなく、**その技術分野の通常の活動量に対してどれだけ異常に注目が高まったか（relative salience）**も考慮してください。

---

## 3. 今回の観測期間を決定する

### Editorial Cutoff

`docs/editorial-specification.md` に従い、通常のEditorial Cutoffは

```text
Friday 18:00 America/New_York
```

です。

通常実行では、実行時点から見て直近の、すでに到来したFriday 18:00 America/New_Yorkを今回のEditorial Cutoffとしてください。

### Observation Window Start

通常実行では、Repository内の

```text
sources/*/grok/raw/x-trend-sensor-*.md
```

を確認し、直前の正常なRaw ObservationのFront Matterにある `observed_at` を今回のObservation Window Startの第一候補としてください。

原則：

```text
previous successful Grok observation
    -> current observation
```

ただし、別途Run InstructionでObservation WindowまたはEditorial Cutoffが明示された場合は、**Run Instructionを優先してください。**

### Late Breaking

Editorial Cutoffより後、実際の観測時刻までに急浮上した重要トピックは **Late Breaking** として通常枠から分離してください。

### 重要

Underlying EventがObservation Window以前でも、今回のWindow中に技術コミュニティで本格的に話題化した場合は対象です。

特に、次のような後発要因を見落とさないでください。

- weights公開
- Hugging Face / Model Hub公開
- GGUF等の量子化
- Local deployment報告
- vLLM / SGLang等のServing対応
- Agent / Coding Harness統合
- independent benchmark / reproduction
- 新しい利用例や制約の発見

---

## 4. Stage 1 — Coverage Scan

以下のCoverage Laneを**それぞれ独立に一度以上探索してください。**

一つのGlobal Search結果を分類するだけでは不十分です。各Laneについて、その分野固有の語彙・モデル・OSS・研究・利用者の投稿を意識した検索を行ってください。

### Coverage Lanes

**A. Foundation Models / Reasoning**  
LLM、reasoning model、foundation model、long-context等。

**B. Agents / Coding / Harness / Computer Use**  
Coding Agent、Agent Harness、runtime、computer use、MCP、tools、skills等。

**C. Multimodal Foundation Models**  
text/image/video/audioを跨ぐモデル、vision-language model、omni model等。

**D. Image Generation / Editing**  
text-to-image、image editing、diffusion / flow model、image model release、実利用・比較等。

**E. Video Generation / Editing**  
text/image-to-video、video editing、world/video model、長時間生成、motion/consistency等。

**F. Speech / Audio / Music Generation**  
TTS、speech-to-speech、voice model、audio generation、music generation等。

**G. Open Weight / Local AI / Quantization**  
open-weight、local inference、GGUF、quantization、VRAM、consumer GPU、Model Hub等。

**H. Inference / Serving / Systems**  
vLLM、SGLang、TensorRT-LLM、FlashInfer、distributed serving、speculative decoding、throughput/latency等。

**I. Memory / Multi-Agent / Retrieval**  
long-term memory、persistent memory、multi-agent、retrieval、long-running agent state等。

**J. Evaluation / Benchmarks**  
新しいbenchmark、再評価、再現、benchmark contamination、harness差、evaluation methodology等。

**K. Safety / Security**  
model safety、agent security、tool/plugin security、cyber capability、prompt injection、sandboxing等。

**L. Other Emerging Generative AI Technology**  
上記に入りにくいが、Generative AI技術動向として重要なもの。AI for Science、robotics / embodied AI、AI hardware等を含めてもよい。ただし技術的な話題に限る。

### Laneごとの出力

各Laneについて最大2件までStrong Candidateを挙げてください。

候補がなければ無理に埋めず、`NONE_FOUND` としてください。

判断材料が不足している場合は `UNCERTAIN` としてください。

同一トピックが複数Laneに該当しても構いません。ただし、**あるトピックが複数Laneに該当することを理由に、他のLaneの独立探索を省略しないでください。**

特に、Open WeightのLLMを見つけただけでMultimodal / Image / Video / Audioを探索済みとみなしてはいけません。

Raw Observationには、以下のようなCoverage Scan表を残してください。

| Lane | Status | Candidate(s) | X signal / Why Now | Confidence |
|---|---|---|---|---|
| A | FOUND / NONE_FOUND / UNCERTAIN | ... | ... | ... |

---

## 5. Stage 1.5 — Mandatory Second Pass for Media Generation

以下のLaneは、LLM中心の探索で特に落ちやすいため追加確認が必須です。

- C. Multimodal Foundation Models
- D. Image Generation / Editing
- E. Video Generation / Editing
- F. Speech / Audio / Music Generation

これらのいずれかが最初のCoverage Scanで `NONE_FOUND` または `UNCERTAIN` になった場合、**そのLaneだけを対象にもう一度Targeted Searchを行ってから確定してください。**

Second Passでは、単に観測期間中の新規Releaseだけを検索しないでください。

観測期間以前に公開されたArtifactであっても、今回のWindow中に次の現象が起きていないか確認してください。

- community testingの増加
- comparison投稿の増加
- weights / quantization / local support
- OSS integration
- serving support
- model hubでの普及
- 新しいworkflowへの統合
- 独立Benchmarkや実測の出現

Second Pass後も候補がなければ `NONE_FOUND_CONFIRMED` として構いません。

---

## 6. Stage 2 — Candidate Pool

Coverage Scanで得た候補を重複排除し、Candidate Poolを作ってください。

目安として最大24件程度までとし、弱い候補を無理に残す必要はありません。

Candidate Poolには、最終Top 10に入らなかった候補も追跡可能なように残してください。

各候補について少なくとも以下を短く記録してください。

- Candidate name
- Coverage Lane(s)
- Underlying Event Date
- X Momentum Started
- Why Now
- provisional Source Status
- provisional Confidence

この段階では順位を確定しないでください。

---

## 7. Stage 3 — Global Ranking

Candidate Pool完成後に初めて、通常枠最大10件をGlobal Rankingしてください。

Rankingでは以下を総合してください。

1. 今回のObservation Window中のX Momentumの強さ
2. その技術分野内でのrelative salience
3. 複数の独立した研究者・開発者・利用者による言及
4. hands-on test / reproduction / benchmark / integrationの存在
5. 技術的な新規性または実運用上の重要性
6. 今回なぜ話題化したのかが説明できること
7. 後段でPrimary Source Verification可能であること

**単純な総投稿数、Views、Likesだけで順位を決めないでください。**

また、カテゴリごとの採用Quotaは設けません。

重要トピックがLLMに集中する週は、結果としてLLM中心になっても構いません。

ただし、それは**全Coverage Laneを探索した後の編集判断でなければなりません。**

### Dominance Check

最終Top 10のうち、Lane A + Bだけで7件以上を占める場合、確定前に一度Dominance Checkを行ってください。

Candidate Pool内のC～Lの候補について、絶対的な投稿量の差だけを理由に過小評価していないか再確認してください。

このCheckは人工的にカテゴリを均等化するためのものではありません。再確認後もA/B中心が妥当なら、そのままで構いません。

---

## 8. Stage 4 — Coverage Audit

Global Ranking後、全Coverage Laneについて最終Auditを行ってください。

Statusは以下から選んでください。

- `SELECTED` — 最終Top 10またはLate Breakingに採用
- `CANDIDATE_NOT_SELECTED` — Candidate Poolには存在したが最終採用外
- `NONE_FOUND_CONFIRMED` — Targeted Searchを含め候補なし
- `NONE_FOUND` — 候補なし
- `UNCERTAIN` — 十分確認できず

Raw Observationには以下の表を必ず残してください。

| Lane | Final Status | Selected / Candidate | Notes |
|---|---|---|---|

Coverage Auditの目的は、各カテゴリから無理に記事を作ることではなく、**探索されなかったカテゴリと、本当に候補がなかったカテゴリを区別すること**です。

`UNCERTAIN` を `NONE_FOUND` と読み替えないでください。

---

## 9. Ranked Topicの詳細出力

最終Top 10の各Topicは、v0.2 Section 7の形式を使用してください。

少なくとも以下を含めてください。

- Category
- Underlying Event
- Underlying Event Date
- X Momentum Started
- X Peak
- X Activity Persistence
- Why Now
- Why Trending on X
- Representative X Posts
- Primary Source Candidate
- Community Reaction
- Engagement（確認できる場合のみ）
- Verification Needed
- Source Status
- Confidence

さらにv0.4では、各Topicに以下を追加してください。

**Coverage Lane:**  
Stage 1でどのLaneから検出されたか。

**Discovery Pass:**  
`FIRST_PASS` または `SECOND_PASS`。

日時・数値・URLが不明な場合は推測で補完しないでください。

---

## 10. Late Breaking

Editorial Cutoffより後に急浮上した話題は、通常ランキングに混ぜず **Late Breaking** としてください。

最大3件。

Late Breakingについても可能な限りCoverage Laneを記載してください。

---

## 11. Overall X Trend

最後に、個別ニュースの列挙ではなく、複数Candidateを横断した技術的傾向を3～5件整理してください。

実際のCoverage Scan / Candidate Pool / Ranked Topicsから導けない傾向を創作しないでください。

---

## 12. Raw Observationファイルの構成

生成するMarkdownファイルは、原則として以下の順序にしてください。

```text
YAML Front Matter
# X Trend Sensor Observation
## Observation Window
## Coverage Scan
## Candidate Pool
## Ranked Trend Candidates
## Late Breaking
## Coverage Audit
## Overall X Trend
```

候補が存在しないセクションは、その旨を明記してください。

---

## 13. 最終成果物は必ずMarkdownファイルとして提示する

調査結果全文をチャット本文へ貼り付けないでください。

最終成果物は必ず `.md` のMarkdownファイルとして生成し、ユーザーがそのファイル自体を取得・添付・転送できる形で提示してください。

### 禁止

- 調査結果全文を通常のチャット回答として貼り付ける
- Markdownコードブロック内に全文を貼り付ける
- 「以下をコピーしてファイルにしてください」とユーザーへ依頼する
- GitHubへのPushを試みる
- 調査結果を要約してからファイル化する

### 必須

- 調査結果全文を1つの `.md` ファイルとして生成する
- Raw Observationとして省略せず保持する
- ユーザーには**ファイルそのものを提示する**
- チャット本文にはファイル生成完了とファイル名だけを簡潔に伝える

**「Markdown形式で回答する」のではなく、「Markdownファイルを生成して提示する」ことが必須です。**

---

## 14. ファイル名

通常実行では以下の形式にしてください。

`x-trend-sensor-YYYY-MM-DD.md`

`YYYY-MM-DD` は実際に観測を実施した日付としてください。

ただし、別途Run Instructionで出力ファイル名が明示された場合は、**Run Instructionのファイル名を優先してください。**

既存Raw Observationを上書きしてはいけません。

---

## 15. Front Matter

生成するMarkdownファイルの先頭に、必ず以下のYAML Front Matterを付けてください。

```yaml
---
sensor: grok
prompt_version: x-trend-sensor-v0.4
observed_at: "<実際に調査を行った日時。可能ならISO 8601、timezone付き>"
observation_window_start: "<今回のObservation Window Start>"
editorial_cutoff: "<今回のEditorial Cutoff>"
repository: "eariver/japanese-generative-ai-survey"
status: raw
---
```

Run Instructionで追加Front Matterが指定されている場合は、それも追加してください。

`status` は必ず `raw` としてください。

---

## 16. Raw Observationとして保持する

このファイルは後段のSource Verificationへ渡すRaw Observationです。

以下を行わないでください。

- Evidenceとして確定する
- Primary Sourceの内容を確認したことにする
- 不明値を補完する
- Survey記事として文章を整える
- Chronologyへ確定Eventとして登録する
- Candidate Poolから不都合な候補を後から消す

不確実性はConfidence、Verification Needed、Coverage Auditへ残してください。

---

## 17. GitHubへの搬送

GitHub ConnectorはRead-Onlyとして扱ってください。

あなた自身はGitHubへ書き込まず、生成した `.md` ファイルをユーザーへ提示してください。

そのファイルは後段で以下へRawのまま保存されます。

```text
sources/<issue-id>/grok/raw/<generated-file-name>
```

---

## 18. 最終回答

調査とMarkdownファイル生成が完了したら、チャット本文は短くしてください。

例：

> 調査が完了しました。Raw Observationを `x-trend-sensor-2026-08-16.md` として作成しました。ファイルを添付します。

その後、**実際のMarkdownファイルを提示してください。**

調査結果全文を本文へ再掲しないでください。
