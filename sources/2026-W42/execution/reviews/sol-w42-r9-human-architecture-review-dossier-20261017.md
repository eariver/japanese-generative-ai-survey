# W42 Human Architecture Review Dossier — Sol independent r9

Date: 2026-10-17 JST  
Edition: 2026-W42 / WEEKLY_MAGAZINE  
Reviewed Muse r9 commit: 4a1cb6b9df5a7b64bacdcd881af201e7bf0d28a1  
Review-status: **SOL_INDEPENDENT_PASS_WITH_LIMITATIONS / AWAITING_HUMAN_DECISION**  
Frozen Core v2: 774dd39a951c9ac3818e83dfffd4c7666efb0a20 (unchanged)  
Reviewed main: c8d0ecc1c9566a2303ad3b4c42635d4b672650e4 (unchanged).

## 1. 審査対象・正式状態

週刊2026-W42のArchitecture r9。Canonical Stateは **ARCHITECTURE_ESTABLISHED**。Discovery、Screening、Evidence、Materiality、Completeness、Selection、Architecture各checkpointの機械検証がPASS。Human Architecture Review、Publication Previewはいずれも**pending**。Architecture本体は `PROPOSED`、`human_review` はすべてnull。本文・TeX・PDFは未作成。これはPDF/内容への承認ではない。

本レビューは初回のHuman Architecture Review dossierであり、採否判断の前に研究量、情報源の実態、除外候補、誌面配分、代替構成、リスクを提示する。

## 2. 情報源の広がり・Source Intake

週刊窓: 米東部時刻2026-10-09 18:00から10-16 18:00まで（UTC 10-09 22:00から10-16 22:00）。一般公開一次資料（企業技術ブログ、モデルカード/リポジトリ、ライセンス、論文/技術報告、製品変更履歴）に加え、Daily X 7日分・Grok X 18投稿を発見窓として照合。

Grok 18投稿は既存の7候補群を再照合する材料で、18件の独立技術発表ではない。原投稿の作者本人性・内容真偽をX-HTML取得により全検証したわけではなく、この欠落は「投稿が報告された」以上の結論に使用しない。

- Canonical Discovery 50件 = 技術候補49 + Grok/Xの来歴台帳1。Screening KEEP 29（台帳を含む）/INSPECT16/MAYBE5。
- post-Screening Evidence Authority Supplementは91個の出典参照（90の一意URL等ロケータ、90の一意の短い派生メモファイル）。分類はPRIMARY_OFFICIAL 39、PRIMARY_REPOSITORY 16、PRIMARY_PAPER 12、SECONDARY 24。これらは**保存済み原文フルアーカイブ91件ではない**。
- r6作業記録に、重要論文/技術レポート8件の本文消費、ライセンス調査7件（全文2・条項中心3・タグ確認のみ2）が記載されている。Solはこの読解履歴の作業記録・抽出メモを確認したが、元PDF/LICENSE原本の全バイトはW42に保存されておらず、「全文読解を独立追試済み」とは主張しない。
- 技術領域は、frontier/agent、チップと推論効率、open weights/権利、コード基盤・運用、セキュリティ/評価、科学実験/地理、法務・ロボティクス・視覚。JP専用の発表と音声映像は今週の中心選定に足る根拠密度が弱く、今号での相対的欠落として明示する。

## 3. Evidenceの水準と承認済み情報量

Evidence Cards 50件、Edition Views 50件をFrozen Coreで正式受理。Evidenceステータスは **PARTIAL 43 / NEEDS_MORE 7 / VERIFIED 0**。根拠付きの短い主張は計152（技術候補151 + 来歴受領1）。Materiality 28 MATERIAL /14 CONTEXT /7 HOLD /1 NON_MATERIAL。Completenessは **LIMITED**（3 obligation中2 SATISFIED、技術的重要性1 LIMITATION）。

今回採用した28件のEvidenceには117件の候補別主張があり、r9の編集用対応表では62種類の最適出典URL（28ホスト）へ対応する。ただし、これらは117件の独立認証や実測値を意味しない。独立Sol監査にて、6件のベンダー自己申告に誤った「独立」との編集ラベルがあり、さらに未読EXO第三者評価を独立実証として扱う危険な1件を確認した。後続のedition-local errataで訂正し、EXOの未確認独立評価を掲載可能な根拠から除外した。実質的には最大116件を条件付きで引用可能、残る引用も一次資料ごとの方法・分母・ベースライン・ライセンス注意を要する。採用済みCore Artifactは書き換えない。

**出典水準の差**: Beam Apache2.0原LICENSE全文とFLUX Kommunityの全文を取得・読解したと報告、LFMライセンスは発行者条項、Muse Sparkはモデルページ＋mirrorの条項、Granite/MiniCPMはライセンスタグだけ、Nemotron Super VLの個別LICENSE FILE未確認。OpenMDW-1.1のOSI承認は確認されていない。商用利用条件を「open weights」の一語でまとめない。

## 4. 大きな候補の整理とSelection採否

正式Candidate Matrix 50、正式Candidate Selection 50。**SELECTED28（PRIMARY16、SUPPORTING12）/INSPECT5/HOLD7/REJECT10**。人間向け記事対象は28件（複数を統合する章立て）であり、Grok/X台帳は記事ではない。

以下は28件全体が漏れなく配置された誌面設計である。主題16候補には図表・方法比較・実測条件の検討を優先し、補助12候補は無理に単独フル記事化しない。

## 5. 除外・HOLD・ネガティブスペース監査

**INSPECT5**: Fish Audio Drama 3（10/14の論文とHFは実在する有力な音声テーマだが、ライセンス/使用感/独立ベンチの比較が薄いため今号独立章は保留）、Claude Code速度変更（公式投稿と変更履歴はあるが他社比較や因果測定なし）、Le Chonk（前週のLarge 4を今週新発売と誤読できず、1ppのベンダー差とweights予告のみ）、NVIDIA OCP/SMLIB（実際の開放規格の技術的意義はあるがオープンCAD kernel一次確認の不足）、OpenAI EU agent adoption（Enterprise/Business標本限定による偏り）。

**HOLD7**: 時刻不明のMicrosoft Decision-1継続保留、Grok購入実行/規模主張のX単独証言2件、出典未同定の「17名著者ハーネス論文」、SplashboardのQwenモデル名未確認、Sulphur2の手法/権利確認不足、OpenAIセキュリティ事件のX由来未裏取り主張。**セキュリティ疑惑を実在事件として誌面に記載しない。**

**REJECT10**: 古いAgentHorizon/Amazon RWM/Sakanaの論文を新週の発表に数えない3件、OSS動画ラウンドアップとQwen-Image Turboの新規性不足2件、AWS Bedrockの配布まとめ・NVIDIA UK投資・Simons数学施策（技術的発表本体ではない）3件、ArgonのCopilot搭載（Argon本文に統合）1件、Grok/X来歴台帳（記事ではない）1件。論文の価値を否定したわけではなく、今週の新規イベントとは分ける判断。

Architecture Review Attentionは51項目だが機械出力に表示上限50があり1項目が省略。省略行はQwen-Image TurboのREJECTで、正式SelectionおよびReview Summaryには記録済み。除外理由もこのdossierに掲載した。

## 6. 編集主題

**今週は新モデル一覧ではなく、「モデル能力がエージェントの実行能力・推論コスト・権利条件・運用安全性・科学研究へ展開した週」である。** 研究面のどの改善が現実的な動作に結びつくかを比較し、ベンダー主張・自社評価・独立第三者測定の区別を通して、一貫した読後理解を形成する。

編纂上の主軸は Frontier実行→アクセラレータ・推論効率→重み/ライセンス→開発・安全運用→科学・専門応用の因果的連関。「各社リリースを書き並べる」だけの短文集ではない。

## 7. Architectureパッケージ（正式な7章）

| 章 | 技術テーマ | PRIMARY | SUPPORTING | 本文目標 | 特に必要な技術説明 |
|---|---|---|---|---:|---|
| P1 | フロンティアエージェント | Wonder, Gemini 4 Argon | なし | 4.0頁 | Active Memory/Focusの定義と持続実行、Minecraft四-agent実験、評価基準と独立性 |
| P2 | チップ・推論経済 | Microsoft Maia 300 | Liquid LFM2.5 | 2.5頁 | HBM4、NUMA、prefill/decode、モデル実行速度とスループットの比較可能性 |
| P3 | Open-weight・権利・効率 | Spark Open, Beam, Nemotron 3.5 | Granite Switch 4.1, MiniCPM-V 4.7, FLUX3 Klein | 5.0頁 | 総/活性パラメータ、context、QAD/MTP/MOPD、LICENSE本文とタグの違い、商用制限 |
| P4 | Agent開発・運用 | Codex GPT-6, Scion, HydraFusion | Agentic Autofix, AI Scan, Decider 1.2 | 4.0頁 | Git競合/統合性能、コード生産と保守コスト、監査/セキュリティゲート |
| P5 | 安全・検証アクセス | Anthropic unintended actions, distillation defenses | NIST ECDSA, METR | 3.0頁 | 公表インシデントの確度、蒸留検出、追試可能範囲、METRが結果公開ではなくアクセス方針であること |
| P6 | 科学エージェント | 自律wet-lab, Earth AI, Deep Review | Rosalind Discovery価格、Rosalind Academic Plan | 4.5頁 | Aptamer/epitopeの実験分母、VERID/HITL、地理空間agentのアブレーション/評価者設計、PAT査読手法 |
| P7 | 特化・身体性 | GLM-Legal, ASPIRE robotics | Glimpse | 3.5頁 | 法務性能におけるVals独立値と比較、ロボット論文の発表日差分、視覚ベンチの負の結果 |

本文計26.5頁。冒頭/方法説明/出典案内1〜2頁で **target 28頁、Architectureのmax 30頁**。ユーザーの求める技術的情報密度を優先し、ページ稼ぎの空行/大きな余白/内容の薄い表は作らない。30頁制限で十分な本文深度が保てない場合、黙って本文を削らず、Architecture変更とHuman再審査の要否を提示する。

## 8. 内容深度と誌面配分の監査

P3（6候補、5頁）は必要なライセンス比較表を保持すること。P4（6候補、4頁）は主題3件に技術的深度を割き、補助3件は運用ゲートの横断比較にする。P6（5候補、4.5頁）は三つのscientific evidence chain（wet-lab、Earth、PAT）を方法・分母ごとに論じ、APIプランと料金だけで紙幅を消費しない。

各PRIMARYについて、少なくとも「何が新しいか、動作方式、実験/ベンチ条件、反証/弱点、他章との関係」を説明できるかをDraftで監査する。原文PDFの実ファイルがW42上にない場合、そのことを証拠書誌に明示する。日本語文体では過剰な漢語化・誤訳を避け、MoE/MTP/QAD/HITL等の既知の技術語を自然に使う。

## 9. 代替構成と選ばなかった理由

A. **安全性先頭版** — Anthropic/METR/蒸留をP1にする。安全保障やRed Teamが中心読者なら有効だが、今週の技術動向全体はagent実行→効率化→導入/権利の流れの方が説明力が高い。
B. **推論経済先頭版** — Maia 300/効率モデルをP1にする。システムハードウェア専門誌なら適切だが、幅広い週刊AI読者にとってフロンティアagent実行を起点とした方が読みやすい。
C. **16頁ほどの圧縮版** — 各社情報を浅く羅列する危険があるため不採用。P3/P6の手法・評価分母を省かない。
D. **音声・映像独立章追加版** — Fishは実際に技術論文があるため魅力的だが、比較対象と独立評価の消費が不足。現時点の材料で独立章は軽薄になりやすく、今号では保留する。今後根拠が揃えば別号で深掘り可能。

**Sol推奨**: P1→P7の7章で約28頁。安全性・科学エージェントを埋没させず、権利と推論性能を同じ設計論で扱う。

## 10. 既知のリスク・承認上の留保

1. VERIFIED0件、Completeness LIMITED。一次サイトの記事自体は実在するが、ベンダー実測値の独立再現はない。2026-W42の観測された発表を扱う資料であって、全性能実証済みのレビュー論文ではない。
2. 91派生メモはURLと記録内容に紐づいているが原本の完全保存ではない。Muse r6が「全文読解した」と述べた8本文のフルアーカイブはこの版では追試不能。重要な数値には原本へのリンク/節を付け、全文が未保存の限界を示す。
3. r9編集用crosswalkの7独立性誤認/3誤ったlegal-text扱い/複合ソース主張はSol errataで拘束的に修正。第三者未確認EXOを独立数値として採用しない。r9 footer「NON_PROMOTABLE0」は訂正後の見解ではない。
4. W42窓より古い論文はbackground、次週以降の発表予定はfuture。X単独セキュリティ主張を掲載しない。Wonderの未公開安全レポート/ライセンス未確認を曖昧化しない。
5. Core v2は完全不変。Issues #568 / #569 とFreeze後課題CV2-DM-016/023は未解決のまま。既存Coreのnative overrideと派生Task projectionによるedition-local受理は成功したが、共有Core修正済みとは表現しない。
6. ページ案はDraft前の設計値。本文品質を見ずに「28頁分を完成」と言うことはできない。大幅な変更は再度Human Architecture Reviewが必要になる。
7. Review Attention 51中50表示の1件（Qwen-Image Turbo REJECT）を別途確認済み。
8. 応答に添付したerrataはSol自身の編集上の再分類であり、Source-readを自動実行した原資料追試ではない。必要に応じてDraft QAで一次資料の確認を再実施する。

## 11. Sol独立監査判定と推奨

**PASS_WITH_LIMITATIONS — Human Architecture Reviewに提示可。**

判定の根拠は、Coreの機械PASSだけではない。SolがCandidate Matrix/Selection/Architectureの50対28対7配置、未採用22件の実際のEvidenceカードをサンプル、出典Crosswalk117件、独立性分類、ページ構成、Attentionの省略1件、対象窓とOpen-weightの権利階層を独立照合したことによる。

Draftへ移るための拘束条件は次のとおり。
- Sol errata `sol-w42-r9-claim-provenance-editorial-errata-20261017.md` をr9 crosswalkの誤分類に優先適用する。
- 候補と章立ては28件/7章を維持し、原文読解で根拠不足を認めれば誇張せず削る・注記する。大幅な採否変更が必要ならSolへ戻す。
- ベンダー公表値と独立評価を原資料単位で区別し、単純に「独立ベンチで優越」と書かない。評価分母、前提、制限、LICENSEが読めるだけの具体性を保持する。
- 草稿の日本語文体と内容量を別途Sol/独立reviewerが監査し、PDFまで無審査の自動進行を許可しない。
- Frozen Core不変。承認後もHuman Publication Previewは別途要求。

## 12. Human decision（ここで初めて要請）

**Option 1: APPROVED** — 本dossier記載のP1〜P7、28件SELECTED、約28頁（Architecture上限30頁）と上記のDraft品質条件を了解し、正式Human Architecture Review Gateを承認。これにより次のMuse Draft実行を指示可能になる。**PDFはまだ承認しない。**

**Option 2: REQUEST_CHANGES** — どの章、候補の採否、資料調査、文字量・最大頁数を変更したいかを指定。Architecture・Selectionの変更をEdition-localに検討し、必要な場合のみ正当な工程・Gate再評価を経て再提示。

**Option 3: DEFER** — 今回のArchitectureは未承認のまま保存し、詳細な資料の追確認などを行う。Human Gateへの書き込みはしない。

承認はこのファイルやSolレビューでは行っていない。Human回答を受けて初めて正式Gateの承認処理へ進む。
