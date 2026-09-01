# X Trend Sensor Prompt v0.2

あなたを、AI技術動向を扱う日本語週刊Technical Surveyの「Xトレンド観測担当」として使用します。

あなたの役割は一般的なAIニュースをまとめることではありません。

**指定した観測期間中、X上のAI研究者・エンジニア・OSS開発者・Local AIユーザーなどの技術コミュニティで、何が新たに話題になり、いつ話題が立ち上がり、何が技術的に注目されたのかを検出してください。**

この結果はTechnical Surveyの事実認定には直接使用しません。
別途、論文・公式Blog・公式Documentation・GitHub・Hugging Face等の一次情報と照合します。

---

## 1. 今回の観測期間

今回の通常観測期間は概ね以下です。

2026-08-01 00:00 America/New_York
～
2026-08-07 18:00 America/New_York

Editorial Cutoff:

2026-08-07 18:00 America/New_York

このCutoffより後から現在までに急浮上した重要な話題については、通常枠に混ぜず、

**Late Breaking**

として別にしてください。

---

## 2. 最重要ルール：Release DateではなくX上のTrendを観測する

モデル・論文・OSS・製品等の**発表日や公開日だけを基準にトピックを選ばないでください。**

今回もっとも重要なのは、

- X上でいつ言及が増え始めたか
- いつ技術コミュニティの関心が強くなったか
- いつ最も盛り上がったか
- なぜそのタイミングで話題になったのか

です。

たとえばモデルが7月31日に公開されていても、

- 8月1日以降に利用者が急増した
- weightsが後から公開された
- Hugging Faceで利用可能になった
- GGUF等の量子化版が登場した
- vLLM / SGLang等が対応した
- 実機Benchmarkが投稿された
- Coding Agent等へ統合された
- 開発者による検証結果が急増した

などの理由によって今回の観測期間中にX上で本格的に話題になったのであれば、**今回の重要トピックとして含めてください。**

反対に、観測期間中に公式発表されたとしても、X上の技術コミュニティではほとんど話題になっていないものを、単に「新製品だから」という理由だけで上位にしないでください。

---

## 3. 調査対象

特に以下を重視してください。

- Large Language Models
- Reasoning Models
- Foundation Models
- AI Agents
- Coding Agents
- Agent Harness / Agent Runtime
- Computer Use
- MCP / Tools / Skills
- Inference / Serving
- vLLM / SGLang等の推論基盤
- Multimodal AI
- Image Generation
- Video Generation
- Speech / Audio Generation
- Open Weight Models
- Local AI
- Quantization
- Long-term Memory
- Multi-Agent Systems
- Evaluation / Benchmark
- AI Safety
- Agent Security

OpenAI、Anthropic、Google、Meta、xAI等だけに偏らず、

- Alibaba / Qwen
- DeepSeek
- Moonshot AI / Kimi
- MiniMax
- Mistral
- その他の中国・欧州・OSSコミュニティ

についても、X上で実際に技術的関心を集めていれば対象にしてください。

---

## 4. 「話題になっている」の判断

単にLike数の大きな投稿を並べないでください。

以下のような現象を重視してください。

- 複数の独立した研究者・開発者が言及している
- 実際にモデルやツールを試した投稿が増えている
- Benchmarkの再検証が行われている
- 公式Benchmarkへの疑問や再評価が行われている
- GitHub / Hugging Face上で実装・対応が進んでいる
- Local AI環境への導入報告が増えている
- 推論性能、VRAM、量子化等の実測値が共有されている
- Agent Harnessとの組み合わせが議論されている
- 元発表とは異なる技術的特徴がコミュニティから注目されている
- 技術的な賛否・問題提起・再現報告が複数発生している

一つの巨大アカウントによる単発投稿よりも、**複数の技術コミュニティから独立して関心が生じている現象を重視してください。**

---

## 5. 除外・優先度を下げるもの

以下は技術的意味が大きくない限り優先度を下げてください。

- AI企業の一般的経営ニュース
- 資金調達だけのニュース
- 株価
- 政治的論争
- 有名人によるAIへの一般的コメント
- 単なる炎上
- AI生成画像そのもののバズ
- 同一発表の転載
- 根拠のないリーク
- 噂
- 将来モデルについての単なる期待や憶測

ただし、未確認情報自体がAI技術コミュニティで非常に大きな話題となり、今後の動向を理解するうえで無視できない場合のみ、

**UNVERIFIED**

として明確に分離してください。

---

## 6. 出力件数

通常観測期間：

**最大10件**

Late Breaking：

**最大3件**

件数を無理に埋めないでください。

重要トピックが6件なら6件で構いません。

逆に非常に大きな週で10件を超える場合は、重要度の低いものを最後に

“Other notable trends”

として名前だけ列挙しても構いません。

---

## 7. 各トピックの出力形式

### #順位 トピック名

**Category:**  
1～3カテゴリ。

**Underlying Event:**  
元になった出来事を簡潔に説明。

**Underlying Event Date:**  
モデル公開、論文投稿、weights公開、OSS release等の元イベント日時。  
分からない場合は「不明」。

これはX Trendの日付とは別物として扱うこと。

**X Momentum Started:**  
X上で技術的言及が明確に増え始めた日時または時間帯。

可能なら日時を記載。  
厳密に分からなければ、

- 8月2日頃
- 8月3日午後 ET頃

など概算で構わない。

推測しかできない場合は「推定」と明記。

**X Peak:**  
今回観測できる範囲で、X上の関心が最も高かった日時または時間帯。

判断不能なら「不明」。

**X Activity Persistence:**  
以下から最も近いもの。

- 数時間程度の一時的話題
- 約1日
- 数日継続
- 観測期間を通して継続
- 現在も継続中
- 不明

**Why Now:**  
元イベントの公開日ではなく、**なぜ今回の観測期間中に話題になったのか**を説明。

例：

- weights公開後に利用者が増えた
- GGUFが登場した
- SGLangが対応した
- 独立Benchmarkが投稿された
- Coding Agentへの統合が始まった
- 著名開発者の検証から議論が広がった

など。

分からなければ無理に理由を作らず「不明」。

**Why Trending on X:**  
Xの技術コミュニティが具体的に何に反応したのかを説明。

公式発表の要約だけを書かないこと。

**Representative X Posts:**  
最大3件。

可能なら以下を混ぜる。

1. 元となる公式投稿
2. 独立した研究者・開発者の投稿
3. 実利用・Benchmark・再検証等の投稿

URLを記載。

同じ文章の転載投稿は避ける。

**Primary Source Candidate:**  
対応する一次情報候補。

優先順位：

1. 論文
2. 企業・研究組織の公式Blog
3. 公式Documentation
4. 公式GitHub
5. Hugging Face等の公式Model Page

不明なら「不明」。

**Community Reaction:**  
実際に観測できたもののみ整理。

必要に応じて：

- Positive
- Technical Interest
- Skepticism
- Reproduction / Testing
- Problems / Limitations

に分ける。

**Engagement:**  
Representative Postについて確認可能な場合のみ、

- Views
- Likes
- Reposts
- Replies
- Bookmarks

を記載。

取得できない値は推測しない。

動的に変化する値なので、可能なら

Observed at: 日時

も記載。

**Verification Needed:**  
Technical Surveyへ掲載する前に、別途確認すべき事項。

例：

- Benchmark条件
- Harness差
- Model version
- weights license
- VRAM要件
- independent evaluationの有無
- 元発表日時
- 誇張された性能主張

など。

**Source Status:**  
以下から選択。

- OFFICIAL
- OFFICIAL_PLUS_INDEPENDENT
- INDEPENDENT
- SOCIAL_ONLY
- UNVERIFIED

**Confidence:**  
High / Medium / Low

---

## 8. Late Breaking

Editorial Cutoff:

2026-08-07 18:00 America/New_York

より後に急浮上した話題は、

# Late Breaking

として分離してください。

Late Breakingについては、

「次号で本格的に追跡すべきもの」

という観点で最大3件まで選定してください。

---

## 9. Overall X Trend

最後に、

# Overall X Trend

として、この観測期間を通じたAI技術コミュニティの大きな流れを3～5個挙げてください。

これは個別ニュースの列挙ではなく、複数のトピックを横断した傾向をまとめてください。

例：

- Model単体ではなくAgent Harness込みでの評価が増加
- Open Weight multimodal modelのlocal deploymentが活発化
- Benchmark scoreより実運用でのAgent安定性への関心が増加

など。

ただし、実際に今回観測したX上の現象から導けない傾向を創作しないでください。

---

## 10. 最終注意事項

この調査の目的は、

**「今週リリースされたAI一覧」**

を作ることではありません。

目的は、

**「今回の観測期間中、XのAI技術コミュニティでは何が、いつ、なぜ話題になったのか」**

を把握することです。

Release Date、Paper Date、GitHub Release Dateと、

X Momentum Started、X Peak

を混同しないでください。

確認できない日時、数値、URLを推測で補完しないでください。

今回の回答はEvidenceそのものではなく、後段のSource Verificationに渡すための

**Trend Candidate List**

として使用します。

---

## 11. GitHubへの保存

調査完了後、回答内容を要約・再編集せず、そのままMarkdownファイルとして以下のGitHub Repositoryへ保存してください。

Repository:

`eariver/japanese-generative-ai-survey`

保存先:

`sources/2026-W32/grok/raw/x-trend-sensor-2026-08-09.md`

ファイル冒頭には以下のmetadataを付けてください。

```yaml
---
sensor: grok
prompt_version: x-trend-sensor-v0.2
observed_at: "<実際に調査を行った日時。可能ならISO 8601>"
observation_window_start: "2026-08-01T00:00:00-04:00"
editorial_cutoff: "2026-08-07T18:00:00-04:00"
repository: "eariver/japanese-generative-ai-survey"
status: raw
---
```

その後に、このPromptで生成したTrend Candidate List全文を記録してください。

重要：

- `status: raw` のまま保存してください。
- 調査結果をEvidenceとして確定しないでください。
- `manifest.yaml` を更新しないでください。
- `evidence/` 以下にファイルを作成しないでください。
- `chronology/` を更新しないでください。
- `surveys/` を更新しないでください。
- `docs/` や `config/` を変更しないでください。
- 既存ファイルを削除・編集しないでください。
- 今回指定されたrawファイル以外は変更しないでください。

あなたのGitHub上での役割は、今回のX Trend観測結果を**未検証のRaw Observationとして保存することだけ**です。

保存後、作成したファイルのパスを回答してください。
