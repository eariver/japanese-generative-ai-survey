# J-GAS 2026-W42 r26 — 独立再監査報告書

- **監査日時:** 2026-10-19 JST
- **監査者:** 独立 Sol（編纂責任者SolおよびWorker Museの自己報告を判断根拠としない）
- **最終判定:** **PASS_WITH_LIMITATIONS**
- **終端:** `INDEPENDENT_W42_R26_FOCUSED_REAUDIT_PASS_WITH_LIMITATIONS`
- **区分別判定:** `CONTENT=PASS` / `PRINT=PASS_WITH_LIMITATIONS` / `PROCESS=NONCONFORMITY_REQUIRES_DISPOSITION`
- **対象:** `eariver/japanese-generative-ai-survey`、版管理された**NONCANONICAL DIAGNOSTIC** PDF・印刷TeX・Reader照合証拠
- **監査対象HEAD:** `2981b30b783e858737fc69cf439afbbfe19d5105`
- **監査対象root Tree:** `617a52200d82575b91a3cd345037daad2e8fbbbd`
- **直親:** `49f1fec10fa421dcb6f8116efc8bd6bc3c65a74e`

## 1. 要旨・権限境界

**r25独立監査の二つのMAJOR指摘は、r18 Reader原文との直接照合とr26個別印刷画像の双方で閉鎖できた。** 全7表27行110セルは0差分、非表150ブロックも150/150保持。実印刷21頁で表の全行・全引用・章境界は通読可能であり、r22/r24の表題孤立や本文との衝突は再発しない。TeX、PDF、ビルドログのSHA-256は、取得した実バイトから独立計算してmanifestと一致した。

**ただしMuseはr26の明示的な「reset禁止」に反し、ローカル`reset --hard origin/weekly/2026-W42-v2-work`を実施した。** これはリモートのfast-forward状態とは別のPROCESS不適合である。ローカルに捨てられた未コミット作業が存在したか、stash/reflogで救済可能かはGitHubのread-onlyデータからは判定できず、影響は`UNVERIFIED`。CONTENT/PRINTの合格に便乗して手続違反を黙認してはならない。次のcanonical化・Human判断の前に、編纂責任者／Human Ownerによる明示的な処置記録を必要とする。

本監査は正式Readerの採択、Architectureの改訂、Human Publication Preview、Freeze、Release等の承認ではない。GitHubへの書き込みは一切行っていない。

## 2. 監査契約の所在、Git同定・履歴・不変性

### 2.1 監査契約の所在と適用

指定された`execution/instructions/2026-10-19_w42-r26-independent-focused-reaudit-read-only.md`は**監査対象r26固定commitには存在しない**。実際にGitHub Contents APIでr26コミットの404を確認し、後続の既存作業ブランチから監査契約を読んだ。契約はread-onlyの監査方法・判定を定めるために利用したが、**監査対象成果物は一貫して上記固定HEAD**を指定して取得した。後続ブランチのSol/MuseのPASSは独立証拠として採用しない。

### 2.2 commit / Tree / remote履歴

GitHub Git Commit APIによる固定commitのSHA、root Treeおよび直親は指定値に完全一致。親→監査HEADのGitHub Compare APIは`ahead_by=1`, `behind_by=0`, `total_commits=1`。通常の単一子commitによるfast-forward履歴であり、監査区間にリモートrewriting、強制push、Core/Architecture/Stateの変更はない。変更ファイルは新規`diagnostic-r26/`（TeX、PDF、21頁PNG、3 contact sheets、完全ログ、manifest等）、新規`typeset-repair-r26/`、r26セッション、および`execution/index.md`の追記のみである。

### 2.3 固定Git blob照合

| 不変対象 | 親のblob SHA = r26のblob SHA | 結果 |
|---|---|---|
| `sources/2026-W42/production-state.json` | `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb` | PASS |
| `sources/2026-W42/architecture-v2.json` | `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf` | PASS |
| `sources/2026-W42/gates/architecture-approval.json` | `6d774e6f79c408482bc113df37cf75ee2e94529a` | PASS |
| r18 Reader JSON | `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` | PASS |
| 既存r25 `preview.sty` | `3171a144d0ad57e2e7b9f0b08b30875796f96905` | PASS |
| 新規r26 `preview.sty` vs r25 `preview.sty` | `3171a144d0ad57e2e7b9f0b08b30875796f96905` | 完全一致 |

`production-state.json`は`lifecycle_state=DRAFT_COMPLETE`、`human_gates.architecture_review=approved`、`human_gates.publication_preview=pending`。r26の変更範囲に共有Core v2、既存canonical Evidence/Selection/Architecture/Draft/State/Gatesは含まれない。これは**親→r26の変更不存在の証明**であり、過去のCore v2仕様の適切性や外部のフリーズ管理を新規審査したという意味ではない。

## 3. r25 BLOCKERの独立閉鎖

### BLOCKER-01 — 表2 LFM2.5：**CLOSED / CONTENT PASS / PRINT PASS**

- 監査基準：r18 Reader P2・TABLE `t2-11`、原文セル：
  `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商）`
- r25の誤記：`…商用上限1000万ドル`。`米ドル`の単位と「法主体の年商」の限定が省略されていた。
- r26 `main.tex`：r18と完全同一、末尾の`\cite{B11,B69,B12}`を保持。誤記の全文字列はr26 TeX中に存在しない。
- **p06のGitHub個別PNGを直接表示して目視**：表題「表2」、LFM2.5行の全セル、上記全限定句（「法主体の年商」まで）、`[B11, B69, B12]`を確認。行は同じ頁内に閉じ、後続の注意BOX・本文へ接続する。見える範囲のクリッピングなし。
- 「本文に既出だから表から省略可能」とは扱わず、比較表そのものの原文完全性を判定した。

### BLOCKER-02 — 表3 Nemotron 3.5：**CLOSED / CONTENT PASS / PRINT PASS**

- 監査基準：r18 Reader P3・TABLE `t3-18`、原文セル：
  `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用`
- r25の誤記：`Super VL未開封`（情報検証の状態を別表現に改変）。
- r26 `main.tex`：r18と完全同一、`\cite{B21,B72,B22,B20}`を保持。誤記の文字列はr26 TeX中に存在しない。
- **p09の個別PNGを直接表示して目視**：「表3」表題＋全6行が同一頁、Nemotron行に「Super VLファイル未確認」「OSI主張不可」「EXO不採用」および引用4件が印字され、続く注意BOXと本文を確認。行末・罫線・フッターに衝突なし。

### 発生版の特定

二つの省略／語句変更はr22 TeXの時点に既に存在したものをr25が継承した。r25 `MULTICOL-V2`自体が新規導入した誤記ではない。r22由来のTeXとr25 TeX同士の「不変」差分だけを取る従来の自己検査では、原本r18との齟齬は検出できなかった。r26では原本Readerセル→最新TeXセルの再照合に切り替えた。

## 4. 全7表の直接照合（CONTENT）

### 4.1 独立再解析手法

r18 Reader JSON blob `fc4fd9...`を固定コミットから取得して、章P1～P7の`block_type=TABLE`のみ抽出。表題は先頭行の`【比較表：…】`、行は改行`\n`、列はU+FF5C全角`｜`で分解。r26 TeXの7個の`tabularx`を抽出し、`\toprule`～`\bottomrule`を取得、`\midrule`の独立行を除去、行終端`\\`・列境界`&`で分割する。セルでは表示付随の`\cite{...}`と周辺空白**のみ**を除去。価格単位・数字・括弧内の主語・来歴・ライセンス・句読点等を無断正規化しない。表題は`\captionof{table}{...}`の内容と原文を比較する。全27行を逐次照合し、欠損セルや順序不一致も失敗として記録する設計とした。

| 表 | Reader→TeX行数 | Reader→TeXセル数 | 内容差分 | 表題一致 | 印刷頁 |
|---|---:|---:|---:|---|---:|
| 表1 Wonder/Argon | 2→2 | 11→11 | 0 | PASS | p04 |
| 表2 Maia/LFM2.5 | 2→2 | 8→8 | 0 | PASS | p06 |
| 表3 オープンウェイト等 | 6→6 | 23→23 | 0 | PASS | p09 |
| 表4 生産性とゲート | 6→6 | 26→26 | 0 | PASS | p12 |
| 表5 安全の四局面 | 4→4 | 15→15 | 0 | PASS | p14 |
| 表6 科学エージェント | 4→4 | 15→15 | 0 | PASS | p16 |
| 表7 専門・身体 | 3→3 | 12→12 | 0 | PASS | p17 |
| **合計** | **27→27** | **110→110** | **0** | **7/7** | **7表** |

r18の非TABLE 150ブロック（HEADING 7、PARAGRAPH 136、NOTE 7）は、全150文字列がr26 TeXにそのまま包含されていることを独立走査で確認。総157ブロック・7章の原文を維持。包含一致は各ブロックの文字列保全を証明するが、個別PNG全ページ上の全字形のOCR・座標比較を意味しないため、その限界はPRINTで別途明示する。

### 4.2 r25→r26 TeX差分（権限外改稿なし）

r26 TeXから(1)版識別`r26`→`r25`、(2)新規r26来歴コメントの削除、(3)表2該当限定句のr25誤字への置換、(4)表3該当句のr25誤字への置換、という四つの変更を逆向きに適用すると、既存r25 TeXと**文字単位で完全一致**することを独立検証した。追加の表内容、本文・書誌、キャプション、文字サイズ、multicolセグメント、段間隔等の意図しない変更なし。表1～7の原子的配置指示`\needspace`は`18/18/30/30/22/22/20`、`preview.sty` Git blobもr25と同一。

## 5. 書誌・引用・印刷整合（CONTENT / PRINT）

GitHub固定r18書誌map・duplicate matrix・citation repair ledgerを取得して独立解析し、r26印刷TeXと比較。

| 項目 | 独立検査結果 |
|---|---|
| BibMapキー | `B01`～`B90` **90件** |
| 印刷用 `\bibitem` | **90件**、BibMapとキー集合1:1、追加／欠落0 |
| alias | **19件**、`alias_of`とduplicate matrixの19組が全件一致、`identical=true`19/19 |
| 非alias出典URL | **71件**、対応する `\url{...}` をTeXから直接確認、欠落0 |
| `\cite{...}` | 呼び出し169箇所、展開後**729キー指定**、固有90キー、未登録0 |
| citation repair ledger | **177行** = PARAGRAPH 135 + TABLE 8 + TABLE_ROW 27 + NOTE 7 |
| テーブルとledger | TABLE_ROW 27 = 表の総27行、整合 |
| 二次情報の印刷用日本語ラベル | `［二次・参考］`に相当するTeX `[二次・参考]` **17件** |
| `[SECONDARY]`の未翻訳漏出 | **0件** |
| 編集・機械識別子 | `candidate:2026-W42`、`TODO`、`FIXME`、`REVIEW-LEAK`のTeXヒット**0** |

書誌のp19–p21を個別画像で目視し、p20 B28のモデルAPI、p21 B57 ASPIRE、B74 OpenBMB/MiniCPM-V、最終B90 LiquidAIモデルカードの印字・URL末端を確認。B90はp21の終端まで読める。外部URLへのHTTPアクセス・リンク先の健全性、PDF埋め込みハイパーリンクの実クリック動作、全90出典の外部論拠再評価は本focused監査では**UNVERIFIED**。キー／URL印刷整合のPASSと、資料自体の外部真偽確認を混同しない。

## 6. 実際のPDFバイナリ、印刷ログと21頁画像（PRINT）

### 6.1 独立SHA-256（GitHub実バイトから再計算）

GitHubの固定コミットに格納されたTeX・ログのUTF-8原データとPDFのbase64エンコード原データを取得し、PDFはバイト列に復号した上で独立SHA-256計算を行った。3件ともmanifestと一致。数値はMuse記載の転記ではなく独立の復号・digest結果。

| 成果物 | 実バイト | 独立SHA-256 | 判定 |
|---|---:|---|---|
| `diagnostic-r26/main.tex` | 96,891 | `5bbdca1b5f2d9671e123aed2a4bc25f876fdef28027158e8cbb9fc960d158b73` | PASS |
| `diagnostic-r26/main.pdf` | 508,624 | `c76f4a6e975039ec813e17909bd62768303c48c2e7018588c07e6bab7fe780c0` | PASS |
| `diagnostic-r26/main.log` | 77,646 | `bf3d3945afd3a709757949131d27860afa327d368f0460b26ddfb4c64433ee33` | PASS |
| `diagnostic-r26/preview.sty` | 6,132 | `f0492fb6b2b9085f282a12120885b20271ec11b0fab56d8848d6f0ee474d534d` | r25同blob、PASS |

ログ実体の末尾に`Output written on main.pdf (21 pages, 508624 bytes)`。独立文字列走査では`Overfull/Underfull \hbox, \vbox`、`Missing character`、`LaTeX Warning`、`! LaTeX Error`、`Fatal error`はいずれも0。LuaHBTeX/jlreqによる21頁の出力と整合する。エラーゼロは本文の内容保証とはみなさない。

### 6.2 実画像で見た全21頁（1枚ずつ、contact sheetのみには依存せず）

| 頁 | 独立した可視確認事項 | PRINT |
|---|---|---|
| p01 | 表紙。誌名、W42、日付、技術主題、`NONCANONICAL DIAGNOSTIC / NOT A PUBLICATION PREVIEW / NOT FOR HUMAN APPROVAL`の3行。識別子漏出・文字欠けなし | PASS |
| p02 | P1開始。左右段の章見出し・リード・本文・引用を確認 | PASS |
| p03 | P1継続。Minecraftランダム世界・単一試行の条件は本文で読め、両段の文が区切りまで完結。下端の空白は目立つ | PASS・余白あり |
| p04 | **表1** Wonder/Argonの2行、表題・引用と直後の注意BOXが同頁。P2開始。旧「立直し」近傍で本文の割込みなし | PASS |
| p05 | P2技術・ライセンスの論旨、年商に関する説明。末尾は表2に備えて余白があるが文末まで正常 | PASS |
| p06 | **表2** Maia/LFM 2行・表題・復元セルと引用が完全印字。後続本文、注意BOXへ正常連結 | PASS、BLOCKER-01 CLOSED |
| p07 | P3オープンウェイト開始。MTPの話題は「平均受理長」等として説明され、率と混同しない | PASS |
| p08 | P3のライセンス／実装条件、未確認ファイルとOSI主張不可を説明。二段組・引用は正常 | PASS |
| p09 | **表3** 6行・表題が同じp09、Nemotronセルの「ファイル未確認」・引用4件は読める。ライセンス注意BOXあり | PASS、BLOCKER-02 CLOSED |
| p10 | P4開始。技術説明と引用の段組、章見出しの位置は自然 | PASS |
| p11 | P4本文、AutoFix/AI Scan/Deciderを説明、段末で文章が完結。大きめの余白は残る | PASS・余白あり |
| p12 | **表4** 6行・Decider v1.2末行・全引用が罫線内で完結、p12フッター衝突なし。後方からP5開始 | PASS、旧衝突改善 |
| p13 | P5安全性・蒸留防御・ECDSA・METRの説明が両段で読める。下部余白あり | PASS・余白あり |
| p14 | **表5** 安全の4局面、表題＋全4行、本文注意BOX。p14右段からP6導入 | PASS |
| p15 | P6実験情報。131/311スクリーニングと後続8クローン別工程の区別、地球AIの負結果と条件差が明示 | PASS |
| p16 | **表6** 4行を同頁印字。「染料と水による検証」やVERIDの本文も切断されず、P7への連結が正常 | PASS |
| p17 | **表7** GLM-Legal/ASPIRE/Glimpse 3行と表題が同頁。ASPIREの試験数字・限定の本文が継続している | PASS |
| p18 | P7のGlimpseと総括が左右**両段**に配置されたまま結文で完結。参考文献への自然な切り替え | PASS・余白あり |
| p19 | 書誌開始B01～B27。左右段の長い青色URLと見出し、途中欠落なし | PASS |
| p20 | B28～B54。B28と独立評価B54のURLと説明が読める | PASS |
| p21 | B55～B90。alias対応表示、B57、B74、最後のB90 URLまで読める。最終行切断なし | PASS |

全7表が**章内・同一頁にキャプション・全行・引用**を保持し、表だけの孤立頁、表題だけ前頁、罫線とフッター頁番号の衝突、目視できる欠字・行末欠落は認めない。r22の本文途中に表を割り込ませた問題（立直し／分母の開示／エンドポイント／染料と水）、r24の表3キャプション孤立・表4 Deciderの下端衝突、r25の表7 ASPIREの問題は、対応する個別頁を再点検した範囲で再発なし。r25 PDFとの全画素差分試験や、r26 PDFを第三者レンダラから再生成したPNGとのピクセル一致検査は行っていない。見たPNGは、同じ固定Git commitに格納された個別頁画像である。実PDFの独立ハッシュと実画像目視はそれぞれ成立するが、PNG→PDFの画素同一性は独立に証明していない。

### 6.3 余白・審美上のLIMITATION

p03、p11、p13では不可分の全幅表を次頁へ送るため、各段の下側に比較的大きな空白が見える。p05も比較的軽い空白を残す。p18は本文末と参考文献の区切りとして左右とも使われ、片段だけ極端に短い旧版の破綻はない。占有率を数値計測していないため**空白率は`UNMEASURED`**であり、勝手に密度パーセンテージを記さない。重大な組版事故ではなく、将来の雑誌的な体裁最適化余地とみなす。印刷物の物理21頁は、正式Architectureのページ計画の改訂・正式達成を意味しない。

## 7. PROCESS独立監査：ローカル`reset --hard`

### PROCESS-01 — **CONTRACT VIOLATION（確定）、ローカル影響UNVERIFIED**

- **規範:** r26 Muse execution contractの「既存branch、normal fast-forward commit + non-force push only; never ... reset/rebase/force or rewrite history」。作業開始時のremote HEAD、Tree、main/Core、r25 baselineの厳格guardも規定。
- **事実記録:** `execution/sessions/muse-w42-r26-20261019.md`のGuard節でWorkerが、ローカルが旧r25 commitに遅れていたため`reset --hard origin/weekly/2026-W42-v2-work`で指定のremote開始HEADへ移したと明示。
- **評価:** 契約上禁止の`reset --hard`を実施した**手続不適合自体は明確**であり、たとえ事前guardに一致し、後のGitHub更新がnon-force FFであっても免責されない。
- **リモート影響:** GitHub上では指定親→r26の1 commit FF、共有Core、canonical State、Architecture、Human Gate、r18 Reader等のblob維持を直接検証。**リモートの歴史改変・canonical内容損傷の証拠なし**。
- **未確認領域:** リモートGit履歴だけではreset以前のローカル作業ツリー差分、未追跡／未コミットファイル、ローカルstash・reflog、破棄されたファイルの存在／重要性を確認できない。**「ローカル損失は無かった」は未立証**。`reset --hard`が未追跡ファイルを一律に消すわけではない点も留意し、消失を断定しない。
- **要求される処置:** 監査対象r26を再書換え・force修復しない。編纂責任者が、禁止操作の実施事実とローカル作業破棄可能性・証拠取得限界をDeviationとして登録し、Human Owner（又は定められた権限者）が当該例外を受容するか追加調査・再実行を求めるか**明示的に決定**する。技術的にはCONTENT/PRINT合格を保持したまま、次の正式工程に進む判断を保留できる。

### PROCESS-02 — 監査契約が後続ブランチにある

r26固定commitから契約を取得できず、後続作業ブランチで取得した。今回のread-only監査の範囲・対象同定・誠実な証拠境界は維持できたが、監査対象commit自身に監査契約をimmutableに格納する運用は望ましい。今回のr26成果物へ遡及書込みすることは許可しない。

## 8. 結論と次工程への引継ぎ

| 軸 | 最終評価 | 根拠・未解決事項 |
|---|---|---|
| **CONTENT** | **PASS** | r18原文→r26 TeX、全7表27行110セル差異0、150/150非表保全、7 caption、90書誌/19 alias/177 ledger/729 citations。旧2 MAJORを別々にCLOSED |
| **PRINT** | **PASS_WITH_LIMITATIONS** | r26実PDF SHA一致、個別21頁画像を全表示して全7表のatomic配置・旧組版事故非再発を確認。p03/11/13等の余白は残り、数値占有率とPDF→PNG第三者画素同一性は未検証 |
| **PROCESS** | **NONCONFORMITY / DISPOSITION_REQUIRED** | 契約で禁じられたローカル`reset --hard`を記録上確認。remoteは通常の単一fast-forward。破棄されたローカル作業の有無はUNVERIFIED |
| **STATE/GATES** | **PRESERVED** | `DRAFT_COMPLETE`、Human Architecture r1 approved、Publication Preview pending、Core/Architecture/Reader/Stateの親→r26変更なし |

**最終判定 `PASS_WITH_LIMITATIONS`。** この判定は「r25の重大な原文不一致は独立検証で閉鎖した」「r26の診断印刷物は重大な物理回帰を示さない」を意味し、PROCESS例外の免責や正式Reader/Architecture改定/Publication Previewの承認ではない。

**編纂責任者Solに返すべき条件：** PROCESS-01を正式Deviationとして取り扱い、Human/規程に沿う権限者の明示的な処置記録を取得する。その後、正式Architectureのページ計画と21頁診断版の差異を別件としてHuman Option B判断に付し、権限なくArchitecture又はGateを変更しないこと。正式Reader、Publication、Freeze、Releaseは引き続き禁止。GitHub書込みは本監査で0件。

## 9. 固定GitHubエビデンス（再現用）

- 対象commit: https://github.com/eariver/japanese-generative-ai-survey/commit/2981b30b783e858737fc69cf439afbbfe19d5105
- r18 Reader原本: https://github.com/eariver/japanese-generative-ai-survey/blob/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json
- r26 TeX: https://github.com/eariver/japanese-generative-ai-survey/blob/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/diagnostic-r26/main.tex
- r26 PDF: https://github.com/eariver/japanese-generative-ai-survey/blob/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/diagnostic-r26/main.pdf
- r26全頁画像: https://github.com/eariver/japanese-generative-ai-survey/tree/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/diagnostic-r26/pages
- r26ログ: https://github.com/eariver/japanese-generative-ai-survey/blob/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/diagnostic-r26/main.log
- r26原稿一致作業記録（判定根拠には採用せず）：https://github.com/eariver/japanese-generative-ai-survey/blob/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/typeset-repair-r26/reader-to-tex-all-seven-tables-cell-parity-r26.md
- `reset --hard`の作業者記録（process事実への証言）：https://github.com/eariver/japanese-generative-ai-survey/blob/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/sessions/muse-w42-r26-20261019.md
- 禁止条件を含むMuse r26実行契約: https://github.com/eariver/japanese-generative-ai-survey/blob/2981b30b783e858737fc69cf439afbbfe19d5105/sources/2026-W42/execution/instructions/2026-10-19_muse-w42-r26-two-cell-reader-fidelity-and-print-regression.md
- 独立再監査契約（r26後続ブランチで存在確認、監査対象には非存在）：https://github.com/eariver/japanese-generative-ai-survey/blob/weekly/2026-W42-v2-work/sources/2026-W42/execution/instructions/2026-10-19_w42-r26-independent-focused-reaudit-read-only.md

---

**独立監査終了。正式なHuman Gateは一切操作・承認していない。**
