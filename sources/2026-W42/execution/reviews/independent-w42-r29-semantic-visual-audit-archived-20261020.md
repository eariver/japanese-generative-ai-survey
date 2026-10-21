# J-GAS W42 r29 — 独立Semantic / Visual監査報告書

- **監査日時:** 2026-10-20 JST
- **監査方式:** 独立 Sol / read-only / GitHub固定commit参照、原典の抜取再確認、実バイトSHA-256独立計算、21頁の個別PNG目視
- **総合結論:** **PASS_WITH_LIMITATIONS**
- **区分判定:** `CONTENT / SEMANTIC = PASS_WITH_LIMITATIONS`、`VISUAL / PRINT = PASS_WITH_LIMITATIONS`、`PROVENANCE / SOURCE FIDELITY = PASS_WITH_LIMITATIONS`、`PROCESS / EVIDENCE SUFFICIENCY = PASS_WITH_LIMITATIONS`
- **出版承認:** **NO**。本報告は正式Gate、Reader-Surface Gate、Publication Preview、Release等のいかなる承認も生成しない。

## 0. 固定対象と監査権限

| 固定識別子 | 実際の取得・照合結果 |
|---|---|
| Repository | `eariver/japanese-generative-ai-survey` |
| Branch | `weekly/2026-W42-v2-work` |
| Exact audit commit | `9207767cff484b2766bd00b28da120bb58b002d8` — GitHub Git Commit APIで一致 |
| Exact root Tree | `10a77f0ea934993ca2e2b70c718cfaea8d946f03` — GitHub Git Commit APIで一致 |
| Branch HEAD（照合時） | 上記commitと一致。以後の変更があっても本監査は固定commitのみを対象とする |
| PDF SHA-256 | `8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9` — 固定commitの実PDFバイトから独立算出、一致 |
| TeX SHA-256 | `2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3` — 固定commitの実TeXバイトから独立算出、一致 |

PDF 505,102バイト（`%PDF-1.7`）、TeX 96,790バイトを実際に取得し、base64復号後のバイト列から標準SHA-256を独立実装して比較した。SHA-256実装は `abc` の既知テストベクトル（`ba7816bf...f20015ad`）で確認した。PDF先頭ヘッダも実バイトで確認した。ファイルの存在や一致はWorkerの表だけから推測していない。

監査URL：
- 固定commit: https://github.com/eariver/japanese-generative-ai-survey/commit/9207767cff484b2766bd00b28da120bb58b002d8
- 固定PDF: https://github.com/eariver/japanese-generative-ai-survey/blob/9207767cff484b2766bd00b28da120bb58b002d8/surveys/weekly/2026-W42/main.pdf
- 固定TeX: https://github.com/eariver/japanese-generative-ai-survey/blob/9207767cff484b2766bd00b28da120bb58b002d8/surveys/weekly/2026-W42/main.tex
- Reader原本: `sources/2026-W42/execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json`（blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`）
- 対象manifest: `sources/2026-W42/publication/v2/reader-manuscript-v2.json` および `sources/2026-W42/execution/publication-build-r29/build-manifest-r29.json`

## 1. CONTENT / SEMANTIC — PASS_WITH_LIMITATIONS

### 1.1 原稿の文字列保全：PASS

r18 Reader JSONを独立にパースし、canonical r29 `main.tex` を直接走査した。

| 項目 | 独立計測 | 結果 |
|---|---:|---|
| 章 | 7、P1–P7 | 一致 |
| 原稿ブロック合計 | 157 | 一致 |
| ブロック内訳 | HEADING 7、PARAGRAPH 136、NOTE 7、TABLE 7 | 一致 |
| 非TABLEブロック文字列 | 150/150件がTeXに**文字列そのまま包含** | 欠落0 |
| TeX `\section` | 7 | 一致 |
| 全幅 `tabularx` | 7 | 一致 |
| `\captionof{table}` | 7 | 一致 |

ブロック「包含一致」は文字列保持の証明であって、印刷済み全字形の自動照合ではない。28 selected topicsについてはArchitecture・Human Route A決定文書の選定数、本文7章の配置を確認したが、28件を構成する選定候補IDの完全な1対1再集計は本監査で実施していないため、この粒度を留保する。

### 1.2 全表セルの直接再照合：PASS

Readerの各TABLE先頭caption行の後を改行で行分割、全角`｜`でセル分割し、r29 TeXの各 `tabularx` を `\toprule/\midrule/\bottomrule` による構造で識別し、各行の`&`と終端`\\`でセル分割。表示用の末尾 `\cite{...}` と外周空白だけを除去して**全セル文字列を比較**した。数字、括弧内条件、主語、単位、来歴、語彙は正規化・意訳しなかった。

| 表 | 頁 | Reader 行/セル | TeX 行/セル | 不一致 |
|---|---:|---:|---:|---:|
| T1 Wonder / Argon | 04 | 2 / 11 | 2 / 11 | 0 |
| T2 Maia / LFM2.5 | 06 | 2 / 8 | 2 / 8 | 0 |
| T3 重み・実装・ライセンス | 09 | 6 / 23 | 6 / 23 | 0 |
| T4 生産性とゲート | 12 | 6 / 26 | 6 / 26 | 0 |
| T5 安全の四局面 | 14 | 4 / 15 | 4 / 15 | 0 |
| T6 科学エージェント | 16 | 4 / 15 | 4 / 15 | 0 |
| T7 専門・身体 | 17 | 3 / 12 | 3 / 12 | 0 |
| **総計** | | **27 / 110** | **27 / 110** | **0** |

表のcaptionがすべて該当頁にあり、実目視では表題欠落・列外逸脱・行カットは見られなかった。

### 1.3 書誌、引用、公開先：PASS（書式・内部一貫性）

- `\cite{...}` 呼出 **169箇所**、展開後 **729キー指定**、**固有90キー**、未登録参照 **0**。
- `\bibitem[Bxx]{Bxx}` **90件**、r18 `bibliography-map-r18.json` のB01～B90 **90件**と同一集合（欠損・余分とも0）。
- `bibliography-duplicate-matrix-r18.json` のalias **19組**を実読みし、全19組 `identical=true` と書誌mapの`alias_of`参照を照合、矛盾0。
- r18 citation repair ledger実数 **177行**（PARAGRAPH 135、TABLE 8、TABLE_ROW 27、NOTE 7）。TABLE_ROW 27は表実数27と一致。
- TeX `\url{...}` **71件**、二次参考表示 `[二次・参考]` **17件**、未翻訳 `[SECONDARY]` **0件**。
- B28はp20、B57・B74・終端B90はp21の個別画像で可読。長いURLは行送りしつつ右端での明瞭なクリップは見られない。ただし71個の**リンク先全件の稼働確認**はしていない。

### 1.4 r25の既往指摘と本文上の条件：PASS

- **T2 / p06 LFM2.5ライセンス条件**：r18原文とr29 TeXが `商用上限1000万米ドル（法主体の年商）` で完全一致。p06 PNGでも`法主体の年商`まで実視認。r25の短縮形`商用上限1000万ドル`はTeXに再発していない。Liquid AI公開LFM Open License v1.0のThreshold `$10,000,000` と `Legal Entity` 定義を直接参照して条件の方向性を確認。注意：閾値を「単独モデルの売上」等と取り違えていない。
- **T3 / p09 Nemotron 3.5 Super VL**：r18原文とr29 TeXが `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用` で完全一致。p09 PNGでも可読。誤記`Super VL未開封`再発なし。NVIDIA 2026-10-15公開の公式技術記事で120B/12B、MOPD、MTP、QADに関する説明の存在を一次確認。ライセンス個別ファイルの不存在を実地再調査したわけではないので、「ファイル未確認」という制約を維持することが妥当。
- **その他重要留保の実記述**：P1 Minecraftランダム生成・単一試行・構造化情報入力、P2 Maia24トレイ/96アクセラレータ/167kWと帯域単位・改善値の発行者帰属、P3 Beam全文確認とGranite/MiniCPMタグのみの区別、P4 Codexの社内単一チーム・AI Scan助言限定・Decider版継承、P5防御効果の事業者計測とMETR未公表成果、P6地球AIの分母と失敗込みコスト・Deep Reviewの6月論文を背景扱い、P7 Valsの独立性限定・ASPIRE実機報告の発行者帰属・GlimpseのHSS不足と非公開重みを、r29本文/画像で実際に確認。
- 数字を並べるだけで独立検証済みとする記述は、抜取確認した主要論点では発見しなかった。

### 1.5 Architecture内容要件：主要配置の実質確認、全件の原典再検証は未了

固定 `architecture-v2.json` のmust-coverを直接数えると `P1=4, P2=4, P3=4, P4=4, P5=4, P6=4, P7=3`、計**27**。r29 Reader manifestのカバレッジ表も27行で各Section Nへ紐付く。ただしManifest上の`FULFILLED`はWorker自身の主張なので、**これを独立PASSとして転記していない**。各章の実TeX・実PNGで前節の主要要件を照らし合わせ、明白なmust-cover欠落は見られなかった。

Reader追加要件は、`FINAL_SYNTHESIS`が第7章p18終盤の三件を条件で束ねる総括として確認でき、`WEEKLY_COMMUNITY_MOVEMENT`は第1～3章p02–p09でSNS告知と性能証拠の分離として明記。いずれも存在・方向性を確認。ただし全27項目×すべての原典の文節単位意味監査ではない。

### 1.6 Editorial日本語

誤訳や技術条件の削除にあたる確定的な新規重大欠陥は確認できない。文章には「裏づけ」「分母」「監査口」「測定の形」「留保」といった抽象語の密度が高い箇所（p04–p06、p14–p18）があり、一般読者には硬い。一方、技術用語の過度な言い換えで条件を歪める例は今回の抜取では確認できなかった。意図的な全面言い換えを行うとr18同一性を損ねるので、次工程で修辞改善するなら変更部分を限定し再監査すること。

## 2. VISUAL / PRINT — PASS_WITH_LIMITATIONS

### 2.1 全21頁を個別に開いた検査

`publication-build-r29/pages/p-01.png` ～ `p-21.png` **21画像を1枚ずつGitHub固定commitから取得し、実際に表示して目視**した。Contact sheetは全頁目視の代用にしていない。個々の観察一覧：

| 頁 | 監査内容と目視所見 |
|---|---|
| p01 | 正式表紙、`週刊Technical Survey`、号・日付・見出し。診断用刻印・APPROVED/RELEASED表示なし。 |
| p02 | P1開始、2段の文字判読、ページ番号との干渉なし。 |
| p03 | P1終盤、**下部大余白**。文字途中欠落の徴候なし。 |
| p04 | T1 caption・Wonder/Argon全2行と注意BOX、P2開始。同一頁完結。 |
| p05 | P2連続、余白中程度。`
| p06 | T2 caption・2行、LFM法主体条件と引用を判読。 |
| p07 | P3開始、技術・ライセンス本文。 |
| p08 | P3連続、Nemotron/Granite/MiniCPM/FLUX比較の前段。 |
| p09 | T3 caption＋6行を完結。Nemotron `Super VLファイル未確認` 目視、余白等によるカットなし。 |
| p10 | P4開始、Codex/Scion/HydraFusion。 |
| p11 | P4後段、**下部大余白**。Decider本文を判読。 |
| p12 | T4 caption＋6行・Decider v1.2、注意BOX、P5開始。以前のフッター衝突・表題孤立は見られない。 |
| p13 | P5後段、**下部大余白**。テキスト末端は見える。 |
| p14 | T5 caption＋4行、P5後段からP6冒頭へ正常に接続。 |
| p15 | P6科学エージェント本文・数値、2段可読。 |
| p16 | T6 caption＋4行、P6後段からP7開始。 |
| p17 | T7 caption＋3行、ASPIRE条件列と引用まで見える。 |
| p18 | P7末尾・総括を2段で確認。本文は途中で切れていないが下部に余白。 |
| p19 | 書誌B01～B27、ラベル/URLを確認。 |
| p20 | 書誌B28～B54、B28・B54を確認。 |
| p21 | 書誌B55～B90、B57/B74/B90を確認。末尾の書誌キー/URLまで可読。 |

p05の文字列だけではなく実画像にも可読な2段本文がある。表1～表7はcaptionだけが孤立した頁や、複数頁に割れて行が欠落した表を見つけていない。ページ番号、表の罫線、脚注/本文の明瞭な衝突も発見していない。T3、T4、T7は行末まで実確認済み。

### 2.2 r26からの視覚的退行：差分なし（p02–p21）、表紙のみ変更

r26 `diagnostic-r26/pages/` とr29 `publication-build-r29/pages/` の**各PNGのGit blob SHAを21組直接比較**した。p02～p21は**20/20バイト同一**。p01だけSHAが異なり、正式表紙から診断用の文字を除いた。実TeXのr26→r29行単位差分も**4行のみ**（ヘッダ来歴コメント2行、正式版descriptor1行、表紙診断文字削除1行）で、本文・表・引用・needspace・余白を変えていない。

従ってp02～p21のPNG上でr26に存在しなかった印刷退行は**Git blob同一性により否定できる**。ただし当該固定PDFを独立レンダラーに取り込んで全21頁のPNGとpixel-by-pixelで一致させる再レンダリングはこの実行環境では完了していない。**この限界の下での画像差分・ソース照合PASSであり、PDFのレンダラー間一致PASSを主張しない。**

### 2.3 Route Aの受容済み制約

`execution/governance/pageplan-r27/human-w42-r27-conditional-route-a-approval-20261020.md`を直接読み、Humanは**概ね21頁、p03/p11/p13の余白**を版固有の編集制約として条件付き受容していることを確認。r1 Architectureの`target_pages=28`はadvisory、`max_pages=30`は上限であり、r1改版や水増しは要求されていない。r29は21頁で構成がcover1＋article17＋bibliography3、上限内。したがって既知余白は新規BLOCKERではなく残存LIMITATION。占有面積は実測していないので「余白xx％」という架空の数字は付さない。

## 3. PROVENANCE / SOURCE FIDELITY — PASS_WITH_LIMITATIONS

### 3.1 一次原典の独立抜取照合

以下の発行元資料を直接公開Web上で確認し、固定版の関連本文・表現と比較した（Workerの記載の単純引用ではない）。

1. **Liquid AI LFM Open License v1.0** — https://www.liquid.ai/lfm-license 。`Threshold`がannual revenue `$10,000,000`以上、`Legal Entity`がcontrol関係の事業体を含む定義であることを確認。T2 p06の年商/法主体の限定と整合。ただし個別のLFM2.5-24Bモデルファイルの別契約存在は今回未検証。
2. **Microsoft Azure Maia 300** — https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/ 。SDLA、NUMA化、HBM4 8スタック 288GB/18TB/s、24トレイ・96アクセラレータ・167kW、Maia 200を比較対象とした最大7倍のラック規模token throughput主張を確認。基準の詳細なベンチ条件は独立測定できないため「vendor-only」の留保を維持。
3. **NVIDIA Nemotron 3.5 Super VL技術記事（2026-10-15）** — https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/ 。120B/12B、MOPD・MTP・QADの定義と事例が見られる。T3のモデル機構と発行者帰属に整合。Super VLのライセンスファイル全文や第三者学習再現を確認したと主張しない。
4. **NVIDIA ASPIRE研究紹介** — https://research.nvidia.com/labs/gear/aspire/ 。研究発行者のロボット学習/実証と限界に照らした。6月論文が今週発表されたという誤認はr29で回避されているが、10月16日のOSS GitHub公開日についてはリポジトリ履歴の独立日付監査を実施していない。
5. **地球AI arXiv論文・Google記事** — https://arxiv.org/abs/2610.15750 および https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/ 。研究論文と発行元ブログという異なる証拠種類を切り分け、地理空間評価の限界が本文に保持されることを確認（数値全表の再計算は実施せず）。

**原典のサンプリングと出典の完全再監査を区別する。** 71 URL全件のHTTP疎通、90論理書誌キーが指す全資料の公開日/版・全文、Beam License実ファイル、Valsの評価手順、MiniCPM/Graniteの個別ライセンスファイル等は未検証である。書誌内部の一貫性が証明されても、外部の全文真偽までは確約できない。とりわけB54（独立Vals順位）、B16（Beam全文）、B57（ASPIRE OSS日付）は次の重点追跡候補。

### 3.2 刊行日・二次出典・ライセンスの扱い

対象本文は、SNS投稿を告知存在の裏づけに限定、ベンチ主張は発行者計測と明記、未取得のファイルを確認済みと記さないなど、証拠水準の書き分けをほぼ維持する。書誌ラベルも `[一次・発行者]`、`[二次・参考]`、`[論文]`、`[独立評価]` 等を見て取れる。原典アクセスできなかった範囲は本報告によって**承認へ格上げしない**。

## 4. PROCESS / EVIDENCE SUFFICIENCY — PASS_WITH_LIMITATIONS

- `publication-build-r29/build-manifest-r29.json` 実在、`reader-manuscript-v2.json` 実在、原稿・style・PDF・21個別PNG・3 contact sheets・`main.log`・r29各種証拠を固定commitで所在確認。
- PDF・TeXの実バイトSHA-256は独立一致。ログを直接検索し、`LaTeX Warning` 0、`Overfull` 0、`Underfull` 0、`Missing character` 0、`Output written on main.pdf (21 pages, 505102 bytes).` 1件を確認。**ログがクリーンでも視覚異常の不在は保証しない**。
- r18 Reader、Architecture、書誌map、duplicate matrix、ledgerは固定commitに実在。r29 Reader manifestが参照するr18 blob、7章27 must-cover・2 Reader requirementsに整合する構造を確認。
- r26先行独立監査は `CONTENT=PASS / PRINT=PASS_WITH_LIMITATIONS / PROCESS deviation`、対象固定r26 commitのみ。r29の判断は新たに行った。r26のローカルreset逸脱処置は過去のHuman記録であり、今回のGitHub書込みを許すものではない。
- `production-state.json`固定版を取得し `lifecycle_state=DRAFT_COMPLETE`、`human_gates.architecture_review=approved`、`human_gates.publication_preview=pending`、`machine_checkpoints.validation=pending`を確認。独立監査完了だけではGate PASSEDやstage遷移にならない。
- r29のHuman承認書 `execution/governance/human-w42-r29-canonical-reader-pdf-build-authorization-20261020.md`は構築と独立監査依頼**のみ**を許可する。正式Publication Preview・Freeze・Releaseを承認していない。
- **新しい正式review/gate recordの作成、repo変更、stage advanceは一切行っていない。** 監査報告書の外部Google Driveへの保存のみ許容される。

## 5. 指摘一覧・Residual limitations

| ID | Severity | 分類 / 位置 | 実測・再現根拠 | 推奨処置 / Gate上の扱い |
|---|---|---|---|---|
| W42-R29-L01 | **LOW / ACCEPTED** | VISUAL p03, p11, p13、軽微にp05/p18 | 個別PNG21頁の目視。表直前/章境界で大きな下部余白あり。p02–p21はr26 PNGとGit blob完全同一。Human Route Aに同種余白の明示的受容あり | 記録してHuman Preview時に提示。必須の再組版や無理な28頁化を要求しない。 |
| W42-R29-L02 | **MEDIUM / AUDIT-SCOPE** | SOURCE p05–p09/p17、B16・B54・B57等 | 一次発行元の代表例を検証したが全71 URL・90キー先を独立再閲覧していない。Beam全文、Vals方法、ASPIRE 10/16公開日の再現を未実施 | 刊行前に高リスク3点を重点確認。未確認を既確認・独立検証済みへ格上げしない。現時点で具体的誤りは発見していない。 |
| W42-R29-L03 | **MEDIUM / VERIFICATION-LIMIT** | PDF/PNG 21頁対応 | PDF実バイトの正しいハッシュは証明済み。Git格納の個別PNGは21/21目視済み、r26→r29 p02–p21は20/20同一。**PDFを独立レンダラーで再描画し、全頁PNGとピクセル照合する工程は未実施** | 正式Visual Gateで必要と判断する場合に、同じPDF SHA256から再レンダリング・画像diffを行い、結果を版に固定する。独立レンダラーによる完全一致を監査報告で僭称しない。 |
| W42-R29-L04 | **LOW / TRACEABILITY** | 28 selected topics, Architecture 27/2 | 7章157ブロックと本文カバレッジは確認済み。28件はHuman/Architectureの選定数を参照し、28選定候補IDの一対一照合までは独立再実行していない | Selectionの28対象IDから章/項目へのcrosswalkを必要に応じ次工程で確認。内容の欠落を示す実測所見はない。 |
| W42-R29-L05 | **LOW / EDITORIAL** | p04–p06、p14–p18 | 抽象的な語（「分母」「監査口」「条件の束」「証拠の形」）が連続する箇所あり。特定の意味改変は検出せず | 出版のための文体改善は任意。原文と内容が変わるなら差分だけ再監査する。 |

**今回新たに発見した致命的な脱落・表セル不一致・引用不整合・表の裁断・診断刻印残存は0。** 見つからなかった事柄を「全原典・全PDF描画の完璧さ」とは同一視しない。

## 6. Editorial recommendation to Sol

**推奨判断: `PASS_WITH_LIMITATIONS`として本独立監査報告を編纂Solへ返送。r29 PDFを直ちに修正要求する根拠はない。** 少なくとも再組版・Reader改稿を要求するCONTENT/PRINT blockerは見つからなかった。r29の原本忠実度は全表110セル、非表150本文ブロック、729引用展開、20頁のr26視覚バイト同一性で強く裏付けられる。一方、L02–L04の限界は明示的に引き継ぐ。

具体的な進め方は次のとおり。

1. 編纂Solが本報告の**限定付き**判定を読んで、B16/B54/B57等の追加原典照合、およびPDF→PNG再レンダリングを正式Gate前に必須とするか判断する。必要であればedition-local read-only追加確認として限定実施する。大規模な再Researchやr1 Architecture改変を機械的に要求しない。
2. 完了条件と責任者の区別を維持する。**Muse deterministic QA ≠ r26独立監査 ≠ r29本独立監査 ≠ Human Publication Preview**。
3. Reader-Surface Gate、Semantic/Visual Gate、`ADVANCE_STAGE`、Publication Candidate、Freeze、Releaseの進行可否は編纂Solの別契約およびHuman Ownerの別決定に委ねる。この報告書はGate入力の一つであってGateレコードそのものではない。
4. Humanに対してはRoute Aで既知の余白を再度示し、表1～7の読み順、B90までの到達、内容非欠落を説明する。**Human未提示のr29 PDFに対する承認と解釈しない**。

---

### Evidence authority separation

- **Independent direct:** GitHub commit/Tree・生バイトSHA256・r18→r29全表/非表照合・引用/Bib/alias/ledger直接再計算・全21頁PNG直接目視・r26とr29のGit PNG blob比較・r29コンパイルログ文字検索・一次資料抜取。
- **Worker-authored, used only as navigation/corroboration:** `build-manifest-r29.json`、`reader-manuscript-v2.json` の`FULFILLED`、`reader-fidelity-and-bibliography-parity-r29.md`、`physical-print-page-and-table-ledger-r29.md`、`canonical-build-provenance-and-diff-r29.md`。
- **Prior independent, different bytes:** `independent-w42-r26-focused-reaudit-PASS_WITH_LIMITATIONS-20261019.md`。
- **Human governance, scoped:** `human-w42-r27-conditional-route-a-approval-20261020.md`、`human-w42-r29-canonical-reader-pdf-build-authorization-20261020.md`。

**監査の終端:** `SOL_W42_R29_INDEPENDENT_SEMANTIC_VISUAL_PASS_WITH_LIMITATIONS / READ_ONLY / NOT_PUBLICATION_APPROVAL`。
