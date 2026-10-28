# J-GAS W43 Muse r3.3 — 包括監査10件の一括修正契約

Date: 2026-10-26 JST
Status: SOLE_MUSE_EXECUTION / R32_FULL_REQUEST_CHANGES / CORE_FREE / NO_PDF_IN_THIS_UNIT
Repository: eariver/japanese-generative-ai-survey
Existing branch ONLY: weekly/2026-W43-v2-work

## 0. 開始条件
**WorkのExact Starting HEAD/Treeは、この契約の配置後に編纂Solが別途指定する。** r3.2監査対象HEADを開始HEADとして使わない。
Reviewed main HEAD: 041a08dfef3112643cbf85b4a86a7b6f9128aed6
Reviewed main Tree: a134dc36a407d08ab1de416324229b3955e0325a
Frozen Core branch HEAD: 774dd39a951c9ac3818e83dfffd4c7666efb0a20
Frozen Core Tree: cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481

最初にremote Work/main/Frozen Coreの6項目HEAD+Root Treeをread-onlyで比較。1件でも不一致ならZERO_WRITESで停止しexpected/actualを報告。cleanでfast-forward可能なローカルの遅れのみ、remote guard後のfetch＋ff-onlyを許可。既存branchだけを使い、normal commit・non-force push・remote read-back。新規branch/fallback/reset/rebase/force/merge commitは禁止。

## 1. 読む資料と監査基準
最初に、独立Sol報告「20261026022400_SolReview.md」（原文45,043bytes、SHA256 78a61517d59c8140f1c32eff21376657374ab2d7d37af7a4939e63f7bfb1846f）を参照可能なら全文読む。参照できない場合は「原文未読」と明記し、GitHubの監査受領記録と編纂Sol裁定および本契約を読む。
固定監査対象r3.2 HEAD: efac8324ff7a9f35ad34be391ba2ea328cfc1722
固定r3.2 Root Tree: 61e33ad8c9b8bb1a3a5e51dbc1d9d5b5b2222c43
r3.2 reader/ledger/crosswalk/QAはsources/2026-W43/execution/editorial-bypass/にある。元のr1～r3.2は不変として保存。承認済みArchitecture r6、19 selected、8 packages、31 must-cover、5 LIMITED、68 inherited Attentionを保持。独立監査の要件充足基準は20 complete/11 partial。
W43記事窓は[2026-10-16T22:00:00Z,2026-10-23T22:00:00Z)。公開日時と後日の観測日を混同しない。

## 2. P1×3 — Preview停止指摘

### R32-FULL-001 MemT
P2 p2-p5/p2-t2/p2-p10の「66x持続性能」をすべて是正。原READMEの「128K履歴におけるfull-context KV cache比のstorage footprint約66倍削減」であり、速度/スループット/レイテンシの66倍ではない。MemT-Flash/Nanoの11benchmark順位はevaluated parametric-memory methods内での1位/2位。textual-memory方式が上位の可能性を明示。別指標1.86xは一次資料の比較対象・測定条件が確認できなければSOURCE_UNVERIFIEDとして限定または本文から除外。表、主張、本文、図説明、台帳、crosswalk、総括を同時に照合。
保存一次資料: sources/2026-W43/collectors/primary/runs/20261025T044100Z-muse-r3-evidence/raw/memt-readme-e75c13d.md

### R32-FULL-002 協調開示の五段階
P6 p6-f1の工程を原資料どおり、1) upstream validate/fix、2) affected organizationsへ時間確保、3)政府パートナーとの調整、4)影響製品の更新準備、5)パッチ利用可能後の案内公表と展開支援に訂正する。Daybreak資金やCodex PHP checkerは工程外の関連施策とし、段階4へ入れない。Calif/Wiz/maintainerの役割を混同しない。CVEは当該頁から識別子未特定であり不存在証明ではない。原資料はRENDERED_TEXTであって元HTMLではない。本文/図/台帳/crosswalkの5段階を1:1で照合する。
原資料: sources/2026-W43/collectors/primary/runs/20261025T044100Z-muse-r3-evidence/raw/openai-patch-planet-rendered-20261025.md

### R32-FULL-003 全20表の双方向完全性
各表の物理データ行と表示上の注記/見出しを区別し、一意なrow_idを作る。読者本文行、ledger.table_rows[].row_id、5新表の全29 claims[].row_idを結び、モデル/版/主張/数値/単位/比較分母/出典URL/保存原本/エビデンスclaim/時間精度/source tierを正確に結合する。原典未取得なら未検証のままにする。
既知の欠陥: p3-t2の「分類器」行がledgerから欠落、p1-t2「注意」を製品データ行扱い、p2-t2「11bench」、p4-t1「22x見出し」、p5-t1「STT Small Transcribe 3」、p5-t2「Controlled Voice」等の短縮名や別名混同、p8-f2 npm package誤対応。20表すべてを実際に解析して更なる欠落を検出。
Frozen Coreと独立したedition-local検査スクリプトを作り、本文↔台帳↔claimの双方向join、孤立行/claim、重複row_id、source/variant/unit違い、表注記扱いをチェックし、実行した証跡とJSON結果を保存する。79=79等の総件数だけでPASSを宣言しない。構造PASSと原資料の真正性は別判定。

## 3. P2×7 — 同じ修正で解消・限定

- 004 TanStack: npm registryの unscoped /ai は誤り。対象は @tanstack/ai、time["1.0.0"] = 2026-10-22T15:21:49.491Z（r6 crosswalk）。GitHub release 15:18:14Zは別ソース。registryの生応答を未取得ならRAW_NOT_ARCHIVED。偽の直接検証を主張しない。
- 005 清書対象の冒頭からUNVALIDATED/Stage/実行根拠/検証SHA等の運用情報を取り除き、内部QAとファイル名に保存する。末尾「今週の総括」5段落を維持。
- 006 FLUX keyframes: 実在するfal PR/blog主張と原典未照合の「Two at launch」FAQ由来とされる記述を区別。公式資料同士の確定した矛盾と断言しない。UNRESOLVED_FAQ_ATTRIBUTION、live/schema/GA UNKNOWN維持。速度10.95/12.45秒、Elo+47/+50等の実資料差は保存。
- 007 P3 Duetの発表済みVM/browser権限境界とcoming-soon 1Password承認/secret注入を別概念経路として図示し、NOT_LIVE_VERIFIED、発行者設計の主張と記す。
- 008 P5 Voxtral: WER4.1/4.0、cpWER18.4/18.6、recall94.6/81.4の各variant/標本/比較対象を原表から確認し、未取得ならCOMPARATOR_UNVERIFIED。Small$0.004、Realtime$0.008、agent$0.04/$0.08は請求単位未確認ならUNIT_UNVERIFIED、Mini$0.0035/分とSpeech$13/100万字等の既知単位と混ぜない。STT/Realtime/TTS言語数・11言語標本は別集計。
- 009 P7 COBOL72.1%は19/20言語83%以上の例外、hidden86.6/97.9は別試験。Luna$0.77/Sol$3.48の費用差は品質同等を意味しない。P8 DeepSeek MITはベンダー公表、重み各artifactのLICENSE実バイト/SHA未確認なら明示し、API/harnessの許諾と混同しない。
- 010 DeepInfer SamplingParams(seq_seed=1234)はimport未確認ならNONRUNNABLE/PSEUDOCODE/NOT_EXECUTEDとし、実行可能例に見せない。日本語の「程序」等の不自然な訳語と過剰な留保重複を修正。

## 4. 成果物と終了条件
新しいr3.3 edition-local読者原稿、96件以上の台帳、source crosswalk、10件の是正QA、20表を読取検査する独立スクリプトと実行結果、Muse handoff/作業記録/indexを作る。既存r1-r3.2ファイルは上書き禁止。原稿P1～P8と「今週の総括」5段落を保ち、P9不要。非正規のPDF Previewは**この工程ではまだ作成しない**。
全P1の修正根拠・全20表の完全な構造joinを実証し、P2はFIXEDか根拠あるQUALIFIED_WITH_LIMITATIONにする。32 accepted sourcesや68 Attentionを未実施で再検証済みと主張しない。品質不足ならSOL_W43_R33_PUBLICATION_BLOCKEDで停止。正常ならnormal commit/nonforce pushとremote HEAD/Tree readback後、SOL_W43_CORE_FREE_EDITORIAL_R3_3_BATCHED_REPAIR_READY_FOR_INDEPENDENT_CLOSUREで停止。

次は編纂Solと独立Solで一度の限定クローズ監査。重大問題が解消した場合のみ別途、Frozen Core v2を変更しない非正規PDF Previewを組版しHumanに提示。正式Draft StageやHuman Publication Preview Gate、Freeze、Releaseは進めない。