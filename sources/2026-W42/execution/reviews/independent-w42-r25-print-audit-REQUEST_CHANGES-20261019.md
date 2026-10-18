# J-GAS W42 r25 — 独立印刷品質監査報告書

**監査日時:** 2026-10-19 01:31 JST  
**監査者:** 独立 Sol / ChatGPT（Muse／編纂責任者の自己申告を証拠として採用しない read-only 監査）  
**判定:** **REQUEST_CHANGES**  
**終端:** `INDEPENDENT_W42_R25_PRINT_AUDIT_REQUEST_CHANGES`  
**監査対象:** `eariver/japanese-generative-ai-survey` / commit `b992685a66ccfd9eef3073a448771d2f224bea9c` / root Tree `d552721744c4e8b6e71adf0bdb90753f36036066`

## 1. 対象同定・監査境界

- GitHub Git Commit API の read-back により、指定HEAD `b992685a66ccfd9eef3073a448771d2f224bea9c`、root Tree `d552721744c4e8b6e71adf0bdb90753f36036066` の完全一致を独立確認。親コミットは `929df060312daf79f6c5737a1d3bb5a146028e61`。
- 監査契約 `sources/2026-W42/execution/instructions/2026-10-19_w42-r25-independent-print-audit-one-shot-read-only.md` は監査対象コミットには存在せず、現在の既存作業ブランチ `weekly/2026-W42-v2-work` から取得した。同契約が定める**監査資料の固定参照はr25コミット**に厳格に限定した。
- 対象は `sources/2026-W42/execution/diagnostic-r25/main.pdf`。NONCANONICAL / DIAGNOSTIC であり、正式Publication Previewではない。`main.pdf`のバイナリをGitHub経由で取得してSHA-256を再計算し、21個の個別PNG（`pages/p-01.png`～`p-21.png`）を**全頁それぞれ実画像表示して独立目視**した。比較資料としてr22 p03/p04およびr24 p09/p11/p12も実画像確認した。
- 印刷の判定は実頁画像に依拠した。PDFのリンク遷移先のインタラクティブなクリック試験、頁PNGをPDFから第三者の処理系で再レンダリングしてピクセル同値を確定する試験、外部URLのHTTP疎通／掲載内容の再取得は**未実施／UNVERIFIED**。文字列のPDF抽出結果を画像確認の代替とはしていない。実効占有面積は**UNMEASURED**であり、以下の余白の印象は数値計測値ではない。

## 2. 結論と重大な指摘

**誌面の物理的欠陥（表の途中欠落、頁下端衝突、キャプション孤立、文字切断）は21頁画像では確認されない。全7表の表題・全行は同頁内に収まり、r22～r24の深刻な印刷崩れは改善している。しかし、r18 Readerとr25 TeX・印刷表の厳密同一性は不成立である。** 編集責任者・Workerの「wrapper-only／原稿不変」という主張には以下の反例がある。

### BLOCKER-01（MAJOR）— p6 表2 LFM2.5行のライセンス条件省略

- **r18 Reader** (`reader-preview-r18.PROPOSED.json` / P2 / `t2-11`): `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商）`
- **r25 TeXおよびp06実印刷:** `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万ドル`（後続に `[B11, B69, B12]`）。
- 「法主体の年商」は適用閾値の主体・分母を特定する**重要な契約上の限定**で、単純な字数節約ではない。r25本文には法主体年商の説明が残るものの、比較表単体では意味の完全性が失われ、印刷におけるr18 Reader本文・表の完全同一性も失敗している。
- **要求:** r18セルの限定句を復元して再組版するか、厳格な改稿承認を明示的に得る。印刷専用変更として無断省略してはならない。

### BLOCKER-02（MAJOR）— p9 表3 Nemotron行の検証状態改変

- **r18 Reader** (P3 / `t3-18`): `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用`
- **r25 TeXおよびp09実印刷:** `OpenMDW：Super VL未開封、OSI主張不可、EXO不採用`（後続に `[B21, B72, B22, B20]`）。
- 「ファイル未確認」と「未開封」は似ていても厳密同一ではなく、どの情報を確認済みかという来歴の表現に差が生じる。r18原稿を不変とする契約に反する。
- **要求:** 原文「Super VLファイル未確認」を復元するか、別工程で編集変更として承認・根拠付けする。

**差分検査の範囲:** r18の7章157ブロック（HEADING 7、PARAGRAPH 136、TABLE 7、NOTE 7）のうち、非表150ブロックはr25 TeXへの原文文字列の包含一致150/150。表7本の**各行各セルを表ごとに区間限定して照合**した結果、表2の1セル、表3の1セルだけがReader文言と一致しなかった。表1・4・5・6・7の全セル、および表2・3の残余セルは一致。これはTeX原稿レベルの同値検査であり、すべてのPDFグリフに対する機械的文字位置検査を済ませたとの意味ではない。両箇所は個別PNG画像でも実際に異なる表記であることを確認した。

## 3. 七表の独立物理配置台帳

| 表 | 章・頁 | 視認した行 | 表の直前／直後の位置関係 | 物理評価 |
|---|---|---|---|---|
| T1 Wonder／Argon | P1, p04 | Wonder / Argon = 2行 | p03のP1本文は引用の終端で完結。p04先頭に表題＋両行、その下の注意BOXと「Wonderの例示タスク…」へ接続。p04右段後半からP2が開始。 | **PASS**。ただしp03の下部余白は残る |
| T2 効率主張 | P2, p06 | Maia 300 / LFM2.5 = 2行 | p05のP2本文完結後、p06上部に表。注意BOXと「LFMの五段階の事後学習…」で続く。P3見出しはp07。 | **PRINT PASS / CONTENT FAIL**（BLOCKER-01） |
| T3 重み・実装・ライセンス | P3, p09 | Spark Open / Beam / Nemotron 3.5 / Granite Switch 4.1 / MiniCPM-V 4.7 / FLUX 3 Klein = 6行 | p08のP3説明を受けてp09上部にキャプション＋全6行、下にライセンス注意BOXと本文。次章P4はp10。 | **PRINT PASS / CONTENT FAIL**（BLOCKER-02） |
| T4 生産性とゲート | P4, p12 | Codex / Scion / HydraFusion / AutoFix / AI Scan / Decider v1.2 = 6行 | p11のP4本文が完結してからp12上部に全行。Decider最終行と `[B37,B36,B38]` を目視。注意BOX、P4結びの後にP5見出し。 | **PASS**。r24の下端衝突が解消 |
| T5 安全の四つの局面 | P5, p14 | 開示 / 防御 / 解明 / 接近 = 4行 | p13の安全性本文に続きp14上部に全行。下にBOXと安全性の結論、同頁右側からP6見出し。 | **PASS** |
| T6 科学エージェントの証拠 | P6, p16 | ウェットラボ / 地球AI / Deep Review / Rosalind = 4行 | p16上部のP6記述に続いて中ほどに表題＋全4行。下でRosalindおよびVERIDの「染料と水による検証」を含む本文が継続し、下部右段でP7が始まる。 | **PASS** |
| T7 専門・身体の三件 | P7, p17 | GLM-Legal / ASPIRE / Glimpse = 3行 | p16右段でP7見出しと導入、p17最上段の導入数行の後に表題＋3行。下に「独立評価の設計を読む」。ASPIREの「80課題で99%」「卓上片づけ」の記述は表で寸断されない。 | **PASS** |

表題番号は誌面上で1～7の順、全表でキャプションと全行が同一頁、分割・欠落・フッター衝突・表のみの独立頁は見られない。本文について `立直し` / `分母の開示` / `エンドポイント` / `染料と水による検証` / `80課題で99%` の語句が表割込みで切断されていないことを、該当するp04/p06/p09/p16/p17の画像で確認した。**PDF内に表示される文字列の完結性は、TeX原稿の不変性とは別の判定**である。

## 4. 全21頁の個別実画像目視記録

| 頁 | 独立所見 |
|---|---|
| p01 | 表紙1頁。タイトル・年月・技術軸・診断用英字3行が明瞭。機械識別子漏れなし。 |
| p02 | P1開始。左右2段を印刷、見出しと本文・引用を確認。 |
| p03 | P1継続、左右段とも文章と参照で完結。**下方の空きが目立つ**が段途中の文切れはなし。T1を次頁に原子配置した結果。 |
| p04 | T1先頭、P1結び、右段からP2導入。レイアウト連続。 |
| p05 | P2継続。次頁T2確保のため下方に一定の余白。段内本文欠落なし。 |
| p06 | T2先頭2行＋注意BOX、P2継続。印字正常。セル内容はBLOCKER-01。 |
| p07 | P3の大見出し・記事導入。左右2段が通読可能。 |
| p08 | P3の実装・権利内容。表3直前まで文章と引用が完結。 |
| p09 | T3全6行が同一頁。下段に注意BOX／段落。セル内容はBLOCKER-02。表題孤立なし。 |
| p10 | P4開始。文字組・2段・引用に重大異常なし。 |
| p11 | P4継続、Decider説明の終端と引用を確認。**下方余白が目立つ**が、T4の前頁下端衝突を防ぐための余白。 |
| p12 | T4全6行とDecider末行まで確認。p12下部にP5開始。下端衝突なし。 |
| p13 | P5安全性の両段本文が中下部で完結。**下方余白が目立つ**がT5原子配置の直前頁。 |
| p14 | T5全4行、P5まとめ、P6見出し。先頭から本文のつながり正常。 |
| p15 | P6深掘り。ウェットラボ131/311と8クローン、地球AIの条件差、引用を左右段で視認。 |
| p16 | P6説明、T6全4行、Rosalind、注意BOX、P7開始。表と本文の混在に衝突なし。 |
| p17 | T7全3行とASPIRE詳述、左右2段を確認。読順の逆転・表切断なし。 |
| p18 | P7のGlimpse、注意BOX、法律・身体領域の結び。**両段が使われたまま中下部で終わる**。下方余白はあるが片段のみ極端に短い旧版の破綻はない。 |
| p19 | 参考文献開始。B01～B27、連続した青いURL、左右段。列を跨ぐ単語の配置に視認不能な欠落なし。 |
| p20 | B28～B54。B28長いURL、B54独立評価を表示。字の欠けは見当たらない。 |
| p21 | B55～B90、19 aliasを含む。B57、B74、末尾B90のURLを印刷上確認。下端でB90の切れなし。 |

### 余白の評価

- **p03、p11、p13:** 二段とも下部に比較的大きな空きを残す。表を不可分なブロックとして次頁に配置する設計上の対価であり、表が切れるよりは妥当。ただし雑誌としては最適な誌面密度ではなく、整版改善余地がある。測定した占有率は提示しない（`UNMEASURED`）。
- **p05:** 上記より軽度の余白。p06全幅表2の準備と整合。許容可能。
- **p18:** 本文末頁と文献頁の切り替えという自然な境界。左右両段に内容が残るため、片段孤立の印象は大きく改善。最終頁下部の空白は概ね許容範囲。
- 全体として余白の審美的判断だけなら**PASS_WITH_LIMITATIONS相当**だが、ここでは原稿非同一性の独立検出により**REQUEST_CHANGES**とする。21頁は「表紙1＋本文17＋参考文献3」の物理頁数であり、「承認Architecture本文割当26.5頁」と同義ではない。

## 5. Reader、書誌、引用・ソースと印刷の照合

- **r18 Reader:** 固定Git blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` をGitHubから実読。7章／計157ブロック、非表150ブロックはTeX原文の全文文字列との包含一致150/150、表7件について上記2セルの実差分を検出。章順P1～P7、表番号1～7、NOTE 7件の存在は保持。
- **正式書誌マップ:** `bibliography-map-r18.json` からB01～B90の90キーを実数え、19件は `alias_of`。duplicate matrixの19組すべて `identical=true`。r25 TeX `\bibitem[Bxx]{Bxx}` の90件とキーが1対1対応し、alias 19件の指すB番号も一致。alias以外の書誌URL71件はr18マップ中のURLとr25 `\url{...}` のバイト表記上1対1で一致した（HTTPの生存検証とは異なる）。
- **引用:** TeXの全 `\cite{...}` を展開すると、延べ729キー指定、ユニーク90キーで、未知キー0。r18 citation repair ledgerは**177行**（PARAGRAPH 135、TABLE 8、TABLE_ROW 27、NOTE 7）。書誌印字のカテゴリー `[二次・参考]` は17箇所、英語漏出 `[SECONDARY]` は0。機械IDおよび編集用ステータス記号の読者面への漏出は画像上見当たらない。
- **書誌の重点箇所:** B28 (p20, BFLのモデルAPI)、B57 (p21, NVlabs/ASPIRE)、B74 (p21, OpenBMB/MiniCPM-V)、B90 (p21, `https://huggingface.co/LiquidAI/LFM2.5-24B-A2B`) の表示URLと末端は目視でも確認。
- **技術的論旨の保全:** Argonのランダム生成Minecraft世界／単一試行（p03）、Maiaの24トレイ・96加速器・750GB/s（p04～p06）、EarthのFlash/Proを含む負結果（p15）、NVIDIAのMTPは受理**長**で受理率ではない（p07）、ウェットラボ131/311スクリーニングと独立8クローン工程（p14～p15）、LFM制限の法主体（p05～p06本文）、ASPIREの発行者報告と実機／模擬機条件（p17）を画像上認める。ただし表2の法主体文言は上記のとおり欠落している。
- **限界:** PDF hyperlinkの実クリック先と外部サーバの応答は未確認。画像上の青文字表示とTeX上の `\cite`・`\url` の整合までは検証済み。

## 6. ビルドとバイナリ実証

r25 GitHubから**バイナリをbase64で取得→復号→独立SHA-256計算**し、労働者が記録したmanifestと別法で一致した。

| 対象 | bytes | SHA-256（独立再計算結果） | 結果 |
|---|---:|---|---|
| `diagnostic-r25/main.pdf` | 508569 | `ce1d50cd748601013455c6164ce83e981edb4e39dc93ddf5c68dec8a00fbe251` | PASS |
| `diagnostic-r25/main.tex` | 96705 | `837f553533c7e673d2430f6f5a010d59584e537e77c193d53680df311630f1c5` | PASS |
| `diagnostic-r25/main.log` | 77646 | `ea428d9facfd1c9df1c269e666f28a2f4312d69a2bddf14b6703d67fbd486e89` | PASS |

実ログの末尾に `Output written on main.pdf (21 pages, 508569 bytes)` を確認。独立文字列走査では `Overfull`、`Underfull`、`Missing character`、`LaTeX Warning`、`Package ... Warning`、fatal errorに該当する行はなかった。LuaHBTeX 1.24.0（TeX Live 2026）、`jlreq`、`multicol`、`capt-of` 構成。ログ0警告は**印刷内容完全性の証明にはならない**（上記2差分が反例）。実画像上にも顕著な欠字やクリップはないが、全文字のフォント内部調査は未実施。

## 7. r22～r24の再発確認

- **r22 p03/p04を個別実画像で再確認:** p03最下部の「…長時間実行…」本文が次頁T1に先回りされる前組版と比較し、r25 p03本文は引用を含めてまとまって終了、p04のT1直後に続く本文は「失敗の内訳…立直しの手順…」というまとまりで印字。表への文章割込みは見られない。r22で問題とされたその他の語の分断もr25該当頁で確認した範囲では再発なし。
- **r24 p11を個別実画像で再確認:** 表4がp11のページ下端からはみ出し、罫線・行がフッター頁番号11に重なって破綻している。r25 p12では表4全6行をフッターから十分離して配置し、Deciderの最終行・引用まで視認できる。**旧F24-01を修復。**
- **r24 p09を個別実画像で再確認:** 表3の全6行はp09にあるものの、上端にキャプションがない（前頁に置き去り）。r25 p09ではキャプション「表3」が6行と同頁になった。**旧F24-02を修復。**
- r25の新規問題として**表2・表3のReaderセル不一致を検出**。これらは外観の修復だけでは検出できず、以前の自己報告「reader bytes preserved」に依存してはいけない。

## 8. Governance / 不変性 / Architectureとの関係

- 固定対象コミットの `production-state.json` は `DRAFT_COMPLETE`、Architecture Human Gate `approved`、Publication Preview `pending`。`gates/architecture-approval.json` はHuman Ownerによる正式`APPROVED`（r1）。
- 親コミットと監査対象コミットのGit blob SHAを直接比較し、`production-state.json`、`architecture-v2.json`、`gates/architecture-approval.json`、r18 Reader JSONは**4/4で不変**。r25コミット変更ファイル一覧に共有Core v2の変更なし。共有Coreの全ファイルの別途全量diffは今回実施していない（監査コミットの変更範囲による不変確認）。
- `sources/2026-W42/architecture-v2.json` はP1～P7の7パッケージ、正式Page Planは**本文合計26.5頁、号全体のtarget 28頁・max 30頁**。今回の診断PDFは21頁、本文は物理17頁であり、正式計画の26.5頁を充足した証拠にはならない。Humans向けOption Bや編纂責任者の暫定21/23方針は**正式Architectureを上書きしない**。内容密度とArchitectureの整合・承認の扱いは独立した編集判断として残す。
- この監査はread-only。Repository/GitHubへの書き込み、正式Reader／Publication Preview／Architecture／State／Human Gate／Freeze／Releaseの操作は**一切実施していない**。

## 9. 修正要求と再監査の受入基準

1. **必須** p06表2 LFM2.5行にr18原稿の `商用上限1000万米ドル（法主体の年商）` を印字し、句とB11/B69/B12引用を落とさないこと。
2. **必須** p09表3 Nemotron行にr18原稿の `Super VLファイル未確認` を印字すること。読者面の来歴ラベル・OSI留保を保持すること。
3. 修正は引き続き**edition-local NONCANONICAL診断**に限定。再コンパイルの後、r18の全7表についてセル単位の同値検査、150非表ブロックの保持、7表の実画像位置、全21頁（頁数変化があれば変更後の全頁）目視、書誌B01～B90の保全、警告なしビルド、独立ハッシュ検証を再実施すること。
4. 補助的な審美改善としてp03/p11/p13の下部余白を試行することは可能。ただし表の不可分配置や文章連続性を壊してまで詰めない。正式Architectureのページ割当に関する裁定はこの印刷監査では代行しない。

### 最終判定

**`INDEPENDENT_W42_R25_PRINT_AUDIT_REQUEST_CHANGES`**

**理由:** 全21頁／全7表の物理印刷品質自体は概ね良好だが、r18 Readerの重要な限定句・来歴句が、r25の表2・表3で各1箇所、合計2セル改変されている。**印刷ソースへの内容忠実性が破れた状態でのPASSは不可**。本文中の説明残存やworkerの自己証明は、この不一致を解消しない。正式Publication Preview・Gate・Freeze・Releaseを承認したものではない。

---

#### 参照GitHub固定ファイル

- 監査対象PDF: https://github.com/eariver/japanese-generative-ai-survey/blob/b992685a66ccfd9eef3073a448771d2f224bea9c/sources/2026-W42/execution/diagnostic-r25/main.pdf
- r25印刷TeX: https://github.com/eariver/japanese-generative-ai-survey/blob/b992685a66ccfd9eef3073a448771d2f224bea9c/sources/2026-W42/execution/diagnostic-r25/main.tex
- r25全頁画像: https://github.com/eariver/japanese-generative-ai-survey/tree/b992685a66ccfd9eef3073a448771d2f224bea9c/sources/2026-W42/execution/diagnostic-r25/pages
- r18 Reader JSON: https://github.com/eariver/japanese-generative-ai-survey/blob/b992685a66ccfd9eef3073a448771d2f224bea9c/sources/2026-W42/execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json
- 監査契約（当該監査コミットより後の既存ブランチに存在）: https://github.com/eariver/japanese-generative-ai-survey/blob/weekly/2026-W42-v2-work/sources/2026-W42/execution/instructions/2026-10-19_w42-r25-independent-print-audit-one-shot-read-only.md
