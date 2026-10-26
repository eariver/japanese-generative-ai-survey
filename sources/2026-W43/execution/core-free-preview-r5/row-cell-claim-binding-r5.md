# W43 row-cell-claim binding r5 (source/proj/TeX per-cell, 20 tables / 80 rows / 29 claims)

Ground truth: r3.5 manifest (row_id/ordinal/physical_text/DATA-NOTE) + r3 print projection + r3 TeX.
Method: r5 validator V03 (ordered src=proj=manifest join) + V04 (TeX caption/row/cell positions) + V05 (claim own-row anchoring).
Clean: PRINT_SEMANTIC_PASS. Failure cases: any swapped/deleted/altered row or cell, moved claim, or bib URL change fails with ROW/HEADER/TEX_CELL/CLAIM cause (23 true negatives, exit 0).

## p1-t1 — 【表：公開状態×時点（Kimi）】  (rows=4)
- p1-t1-01 [DATA] TeX-table#1 row1: 告知・API提供｜2026-10-23T17:15:24Z（X原文、post ID確認）｜状態：IN（当週）｜根拠：X HTML原文＋supplement 041ec6系
- p1-t1-02 [DATA] TeX-table#1 row2: 重み配布｜2026-11-04予定｜状態：FUTURE（未公開）｜根拠：発表のみ、バイト・SHA未取得
- p1-t1-03 [DATA] TeX-table#1 row3: ブログ｜日付のみ（時刻なし）｜状態：PRIMARY_METADATA｜根拠：日次粒度、時刻の証拠にしない
- p1-t1-04 [DATA] TeX-table#1 row4: 料金｜入力$2・出力$10／100万トークン｜状態：API条件｜根拠：発表資料、重み約款とは別

## p1-t2 — 【表：total／effective／active と文脈（計数規約を見出しに明記）】  (rows=4)
- p1-t2-01 [DATA] TeX-table#2 row1: Kimi K3.1 Pro｜Xのみ2.8T total級／104B active（blogは3T級、根拠にしない）｜文脈1M対応｜重みFUTURE
- p1-t2-02 [DATA] TeX-table#2 row2: Flint｜39.8B total／約2.5B active per token（計数規約は承認済みArchitecture境界注記）｜49層・256 experts・SWA-513・文脈512K対応
- p1-t2-03 [DATA] TeX-table#2 row3: Nemotron Bolt E4B｜8B total／4B effective（公式カード）｜64K級｜重み・時刻確認可
- p1-t2-04 [NOTE] TeX-table#2 row4: 注意｜effective・active・totalの等価比較禁止｜文脈は対応／推奨／設定を別列

## p1-t3 — 【表：bench×harness×分母（帰属明示）】  (rows=3)
- p1-t3-01 [DATA] TeX-table#3 row1: Kimi系｜ベンダー harness・温度・top-p・試行平均つき｜分母・条件は発表資料｜独立再現なし
- p1-t3-02 [DATA] TeX-table#3 row2: Flint系｜短文脈・128K平均・prefill除外の装置記述｜分母はベンダー条件｜独立測定なし
- p1-t3-03 [DATA] TeX-table#3 row3: Nemotron系｜公式カード・HF時刻は確認、性能表はベンダー測定｜分母つきで読む｜SHA再ハッシュなし

## p1-t4 — 【表：可用性×時刻×約款（発表／プレビュー／GA／重み配布／再現を別列）】  (rows=3)
- p1-t4-01 [DATA] TeX-table#4 row1: Kimi API｜live（10月23日）｜料金$2/$10｜重みFUTURE（11月4日）｜再現なし
- p1-t4-02 [DATA] TeX-table#4 row2: Flint重み｜配布確認（HF時刻）｜約款Apache-2.0（カード明記）｜SHA再検証なし｜速度は条件つき
- p1-t4-03 [DATA] TeX-table#4 row3: Nemotron重み｜配布確認（HF時刻）｜OpenMDW-1.1（OSI未検証）｜基盤Apache-2.0と区別｜性能はベンダー表

## p2-t1 — 【表：核×役割（DeepInfer）】  (rows=5)
- p2-t1-01 [DATA] TeX-table#5 row1: FlashMLA｜注意の高速化｜DP／均衡CPと協調
- p2-t1-02 [DATA] TeX-table#5 row2: DeepGEMM｜行列積の最適化｜学習・推論の基盤
- p2-t1-03 [DATA] TeX-table#5 row3: DeepEP＋EPLB｜専門家並列と負荷均衡｜MoE分散の要
- p2-t1-04 [DATA] TeX-table#5 row4: TileKernels／TileLang｜カーネル生成・最適化｜実装の生産性
- p2-t1-05 [DATA] TeX-table#5 row5: DeepSelect・DSpark｜選択と推測デコード｜確信度スケジュール検証つき

## p2-t2 — 【表：bench×分母×条件（MemT）】  (rows=4)
- p2-t2-01 [DATA] TeX-table#6 row1: 11 bench｜Flash 1st／Nano 2nd（評価対象parametric-memory方式内・発行元のみ。textual-memory方式が全体で上位の可能性あり）｜分母・harnessは
- p2-t2-02 [DATA] TeX-table#6 row2: 1.86x｜end-to-end・128K（保存済みREADMEに記載なし・論文派生AUTHOR_CLAIM・比較対象/測定条件未確認=SOURCE_UNVERIFIED）｜本文から除外または限定読の
- p2-t2-03 [DATA] TeX-table#6 row3: 66x｜保存容量約66倍削減（128K履歴・full-context KV cache比。速度/スループット/持続性能ではない）｜原README 24行｜単一値に統合禁止
- p2-t2-04 [DATA] TeX-table#6 row4: 34B tokens｜二段階＋事後｜Nano／Flashで基盤相違｜式・ablation未精読

## p2-f2 — 【表：MemT権利対応（p2-f2、§2.5実物）】  (rows=4)
- p2-f2-01 [DATA] TeX-table#7 row1: 論文・原資料 ｜CC BY-NC-SA 4.0 ｜memt-readme-e75c13d.md:208-219 ｜商用不可（README宣言、PDF自体に条項なし）  CLAIMS: p2-f2-01/CC: value='CC BY-NC-SA 4.0' variant=['論文・原資料'] must=[]
- p2-f2-02 [DATA] TeX-table#7 row2: 原ソフトウェア（SGLang統合含む） ｜PolyForm Noncommercial 1.0.0 ｜同上 ｜商用不可、問合せは著者  CLAIMS: p2-f2-02/PolyForm: value='PolyForm Noncommercial 1.0.0' variant=['原ソフトウェア'] must=[]
- p2-f2-03 [DATA] TeX-table#7 row3: 第三者 flash-linear-attention ｜MIT ｜inference/README.md#licensing ｜同梱物の独自約款  CLAIMS: p2-f2-03/MIT-flash: value='MIT' variant=['第三者', 'flash-linear-attention'] must=[]
- p2-f2-04 [DATA] TeX-table#7 row4: 重み・データセット・商標 ｜対象外 ｜同上（別途提供予定） ｜再現・商用いずれも未確定  CLAIMS: p2-f2-04/excluded: value='excluded' variant=['重み・データセット・商標'] must=[]

## p3-t1 — 【表：権限×条件（Duet）】  (rows=4)
- p3-t1-01 [DATA] TeX-table#8 row1: 振舞い｜要点・監視・表・予報・web作成・離席継続・要所確認｜条件：権限と承認つき
- p3-t1-02 [DATA] TeX-table#8 row2: 提供｜待機列＋US Pro/Max先行＋共有制限｜状態：発表／待機／順次公開／GAを別列
- p3-t1-03 [DATA] TeX-table#8 row3: 接続｜6000+接続先一覧 vs 実live｜liveは接続別に未検証
- p3-t1-04 [DATA] TeX-table#8 row4: 消費｜背景消費の条件あり｜料金・範囲外は未検証

## p3-t2 — 【表：旧／新／未来の三段（auto-mode）】  (rows=4)
- p3-t2-01 [DATA] TeX-table#9 row1: 旧（8/7）｜OUT｜当週の根拠にしない
- p3-t2-02 [DATA] TeX-table#9 row2: 新（10/22）｜IN｜Pro/Max/Teamで既定化、例外つき
- p3-t2-03 [DATA] TeX-table#9 row3: 未来（翌週）｜FUTURE｜多くのアプリで既定化予定、完了と書かない
- p3-t2-04 [DATA] TeX-table#9 row4: 分類器｜gatingの説明あり｜独立試験なし

## p4-t1 — 【表：倍率×削減率×出典／版／時刻】  (rows=5)
- p4-t1-01 [DATA] TeX-table#10 row1: 25.37x｜277.80／10.95｜Oct19発行者PR（一次声明、raw RENDERED_ONLY）｜IN
- p4-t1-02 [DATA] TeX-table#10 row2: 22.31x｜277.80／12.45｜blog／製品頁｜IN
- p4-t1-03 [DATA] TeX-table#10 row3: 95.52%｜(277.80−12.45)／277.80｜分母＝旧基準277.80秒｜候補分母にしない
- p4-t1-04 [DATA] TeX-table#10 row4: 26.5x／96.2%｜同入力で不整合｜blog値｜正として引用しない
- p4-t1-05 [NOTE] TeX-table#10 row5: 22x見出し｜下限表現｜数学的誤りと断じない

## p5-t1 — 【表：機能×モデル×対応言語×出典／版／時刻】  (rows=4)
- p5-t1-01 [DATA] TeX-table#11 row1: STT Small Transcribe 3｜50超言語・diarization・context biasing｜出典：発表資料｜評価標本と区別
- p5-t1-02 [DATA] TeX-table#11 row2: Realtime｜35言語超／40+方言｜出典：発表資料｜対応数の確定にしない
- p5-t1-03 [DATA] TeX-table#11 row3: TTS Speech 3｜35+言語（発表）／9言語（カード）／35言語表／プリセット18（発表）・22（Docs）｜UNRESOLVED、統一禁止
- p5-t1-04 [DATA] TeX-table#11 row4: 評価標本｜11言語｜対応数ではない｜混同禁止

## p5-t2 — 【表：AA×原表有無（Ming）】  (rows=4)
- p5-t2-01 [DATA] TeX-table#12 row1: Controlled Voice｜ベンダー引用｜原表未取得｜独立検証にしない
- p5-t2-02 [DATA] TeX-table#12 row2: Robustness｜ベンダー引用｜原表未取得｜同上
- p5-t2-03 [DATA] TeX-table#12 row3: Provider Voice｜ベンダー引用｜原表未取得｜同上
- p5-t2-04 [DATA] TeX-table#12 row4: 開放条件｜MIT・tag・task｜README確認｜roadmap保留

## p5-f1 — 【表：様式×評価・料金の実数行列（p5-f1、§5.1–5.2実物。数値は全て発行元公表・独立再現なし。比較対象・単位は行内でqualified）】  (rows=4)
- p5-f1-01 [DATA] TeX-table#13 row1: STT Small Transcribe 3 ｜FLEURS WER Small 4.1/4.0（二値の内訳・比較対象は受理証拠に特定なし=COMPARATOR_UNVERIFIED）・diariza  CLAIMS: p5-f1-01/WER: value='4.1/4.0' variant=['Small Transcribe 3'] must=[] | p5-f1-01/cpWER: value='18.4/18.6' variant=['diarization', 'cpWER'] must=[] | p5-f1-01/recall: value='94.6/81.4' variant=['recall'] must=[] | p5-f1-01/price-mini: value='$0.0035/min' variant=['Mini'] must=[] | p5-f1-01/price-small: value='$0.004' variant=['Small'] must=[]
- p5-f1-02 [DATA] TeX-table#13 row2: Realtime ｜500ms未満（40超言語標本での測定条件） ｜料金 $0.008（単位未確認=UNIT_UNVERIFIED） ｜対応35言語超・40+方言（発表。40超は標本規模であって対応数  CLAIMS: p5-f1-02/latency: value='sub-500ms' variant=['Realtime'] must=[] | p5-f1-02/price-rt: value='$0.008' variant=['Realtime'] must=[]
- p5-f1-03 [DATA] TeX-table#13 row3: TTS Speech 3 ｜Voice Code Bench 300・発音300・多言語377（11言語標本）・表現力237・判定gemini-3.8-flash（ベンダー選択） ｜料金 $13/10  CLAIMS: p5-f1-03/price-tts: value='$13/M chars' variant=['TTS'] must=[]
- p5-f1-04 [DATA] TeX-table#13 row4: LiveKit音声エージェントSDK ｜聴取・推論・発話の単一管・1秒未満ターン・barge-in ｜料金agent API $0.04/$0.08（請求単位未確認=UNIT_UNVERIFIED）   CLAIMS: p5-f1-04/price-agent: value='$0.04/$0.08' variant=['agent'] must=[]

## p7-t1 — 【表：手順×来歴×限界（Bio）】  (rows=4)
- p7-t1-01 [DATA] TeX-table#14 row1: エージェント｜数千 agents（GPT-Rosalind）｜来歴：研究頁・bioRxiv・HF・GitHub｜独立再現なし
- p7-t1-02 [DATA] TeX-table#14 row2: 操作｜全脳CRISPR・数百万細胞・32分｜摂動報告→atlas｜wet-lab未
- p7-t1-03 [DATA] TeX-table#14 row3: 評価｜盲検75%分散選好｜班内手順＋班推定比較｜独立専門家再現なし
- p7-t1-04 [DATA] TeX-table#14 row4: 遺伝子｜Tsc1/Tsc2・DCTN1｜700+ vs 11｜標本bias未評価

## p7-f1 — 【表：言語別デルタと労力・費用の注記（p7-f1、§7.2実物。数値は全て発行元測定）】  (rows=6)
- p7-f1-01 [DATA] TeX-table#15 row1: COBOL ｜10.9→72.1 ｜19/20言語83%以上の例外（唯一83%未満・最難関） ｜hidden byte-parity（固定小数トランケーションの罠。公開suiteとは別試験）・企業現場  CLAIMS: p7-f1-01/acc-cobol: value='10.9→72.1' variant=['COBOL'] must=[] | p7-f1-01/enterprise-40p: value='40%+' variant=['COBOL'] must=['精度とは別']
- p7-f1-02 [DATA] TeX-table#15 row2: OCaml ｜25.6→85.8 ｜公開suite・参照SQLite照合 ｜—  CLAIMS: p7-f1-02/acc-ocaml: value='25.6→85.8' variant=['OCaml'] must=[]
- p7-f1-03 [DATA] TeX-table#15 row3: Fortran ｜21.4→83.5 ｜同上 ｜現場言及：気象／原子力  CLAIMS: p7-f1-03/acc-fortran: value='21.4→83.5' variant=['Fortran'] must=[]
- p7-f1-04 [DATA] TeX-table#15 row4: VB ｜27.5→89.4 ｜同上 ｜—  CLAIMS: p7-f1-04/acc-vb: value='27.5→89.4' variant=['VB'] must=[]
- p7-f1-05 [DATA] TeX-table#15 row5: 労力 ｜GPT-6.1 Sol 86.6% low（Sol 5.6比61%、対照5.4%起点）・97.9% high（飽和近傍。hidden別試験86.6/97.9で公開suiteと別） ｜hidde  CLAIMS: p7-f1-05/acc-low: value='86.6%' variant=['GPT-6.1', 'Sol'] must=[] | p7-f1-05/acc-high: value='97.9%' variant=['GPT-6.1', 'Sol'] must=[]
- p7-f1-06 [DATA] TeX-table#15 row6: 費用 ｜Luna(40.3%) $0.77 vs Sol $3.48（−78%。費用差は品質同等を意味しない） ｜ベンダー測定 ｜課金未検証  CLAIMS: p7-f1-06/cost: value='$0.77 vs $3.48' variant=['Luna', 'Sol'] must=[]

## p7-t2 — 【表：bench×分母×条件（Low-resource）】  (rows=4)
- p7-t2-01 [DATA] TeX-table#16 row1: SQLite自作｜20言語・DB共有・参照照合｜Astra87.4 vs Sol26.8・19/20≧83%（COBOL72.1%は例外）｜ベンダー測定
- p7-t2-02 [DATA] TeX-table#16 row2: COBOL hidden｜byte-parity・vendor保持（公開suiteとは別試験）｜GPT-6.1 Sol86.6%low・97.9%high｜外部一般化なし
- p7-t2-03 [DATA] TeX-table#16 row3: 費用｜$0.77 vs $3.48・COBOL40%｜ベンダー測定｜課金未検証
- p7-t2-04 [DATA] TeX-table#16 row4: 手順｜we/our第一者｜専門家審査記述｜独立harnessなし

## p8-t1 — 【表：料金×条件×版（Decisions）】  (rows=4)
- p8-t1-01 [DATA] TeX-table#17 row1: 入力｜$0.10／M（uncached）｜cache読取$0.01・書込別課金｜出力課金なし≠総無料
- p8-t1-02 [DATA] TeX-table#17 row2: 上限｜400問 per request｜総呼出上限ではない｜2x betaと区別
- p8-t1-03 [DATA] TeX-table#17 row3: 版｜v1 GA（10/22）／Luna（beta 10/6区別）｜3型・text/image/JSON｜avatar triggers
- p8-t1-04 [DATA] TeX-table#17 row4: 条件｜US/EU・ZDR・地域上乗せ・長文脈乗数｜10x vendor（独立未測定）｜証言は選択bias

## p8-f2 — 【表：安定核 vs 実験harness（p8-f2、§8.2実物）】  (rows=3)
- p8-f2-01 [DATA] TeX-table#18 row1: 安定核 ｜TanStack AI 1.0（76 pkgs・23 adapters・8 UI・143人） ｜製品時刻10月22日IN（GH 15:18:14Z／npm 15:21:49Z） ｜blog1  CLAIMS: p8-f2-01/gh-clock: value='2026-10-22T15:18:14Z' variant=['GH', '15:18:14'] must=[] | p8-f2-01/scale: value='76/23/8/143' variant=['TanStack'] must=[]
- p8-f2-02 [DATA] TeX-table#18 row2: 実験harness ｜0.x（実験明示） ｜codemod threadId・非sandbox ｜移行指南はベンダー記述・独立試験なし
- p8-f2-03 [DATA] TeX-table#18 row3: 版固定 ｜registry／releaseの時刻（npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠） ｜Metrics 23:42:03ZはOUT ｜GrokはNE  CLAIMS: p8-f2-03/npm-clock: value='2026-10-22T15:21:49Z' variant=['npm', '15:21:49'] must=[] | p8-f2-03/metrics-out: value='23:42:03Z OUT' variant=['Metrics'] must=[]

## p8-t2 — 【表：API×移行×約款（発表／配布／無料期限を別status）】  (rows=4)
- p8-t2-01 [DATA] TeX-table#19 row1: 配布｜V4.1-Flash Sep10 snapshot｜MITはベンダー公表（HF/ModelScope。各artifactのLICENSE実バイト/SHA未確認）｜SHA未取得・実行なし
- p8-t2-02 [DATA] TeX-table#19 row2: 移行｜Search/Fetch $0.75/1k｜10/31 16:00 UTC迄無料｜約款表で別列
- p8-t2-03 [DATA] TeX-table#19 row3: bench｜DeepSWE77 vs 74.2・HLE｜ベンダーharness｜独立なし
- p8-t2-04 [DATA] TeX-table#19 row4: demo｜RL自己feedback｜web/app/API｜CodeBuddy/WorkBuddy

## p8-f3 — 【表：重み vs API vs 追加物（p8-f3、§8.3実物）】  (rows=3)
- p8-f3-01 [DATA] TeX-table#20 row1: 重み ｜V4.1-Flash Sep10 snapshot・MITはベンダー公表（HF/ModelScope。各artifactのLICENSE実バイト/SHA未確認。API/harnessの許諾と混  CLAIMS: p8-f3-01/mit: value='MIT' variant=['V4.1-Flash'] must=[]
- p8-f3-02 [DATA] TeX-table#20 row2: API ｜Search/Fetch $0.75/1k・10/31 16:00 UTC迄無料 ｜課金移行は未試験 ｜発表／配布／無料期限を別status  CLAIMS: p8-f3-02/price: value='$0.75/1k' variant=['Search', 'Fetch'] must=[] | p8-f3-02/free: value='free till Oct31 16:00 UTC' variant=['Search', 'Fetch'] must=[]
- p8-f3-03 [DATA] TeX-table#20 row3: 追加物 ｜Harness v0.2.1-rc.1・CodeBuddy/WorkBuddy・RL自己feedback demo ｜bench DeepSWE77 vs 74.2・HLE（ベンダーharn  CLAIMS: p8-f3-03/bench: value='77 vs 74.2' variant=['DeepSWE'] must=[]
