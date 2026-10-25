# Independent Sol W43 Evidence r3 re-audit — source snapshot

Status: `READ_ONLY_INDEPENDENT_REVIEW / REQUEST_CHANGES / STAGE_BLOCKED`.
Source user-uploaded `20261025152137_SolReview.md`: **18,836 bytes**; SHA256 `310d28ca5b677f6403886525d46863cffa38126ed371c9e82cf5aeb812102f90`. This repository file is a text-normalized reading copy, not a byte-identical original. Original independent review had **no GitHub writes** and audited W43 at HEAD `dee2d3e8e18ad8eb1d01ac5b9d1c99d256c329a0` / Tree `5defa56f58597473338847bc7f0fd16ad4b2f17d`. **Independent findings are evidence, NOT authorization to alter Frozen Core, State, a Stage Checkpoint, or Human Gates.**

---

# 2026-W43 Evidence r3 — 独立Sol修正確認監査


監査日：2026-10-25 JST
監査種別：STRICT READ-ONLY / post-repair re-audit
判定：**REQUEST_CHANGES / EVIDENCE_REVIEWED移行 NO**
停止地点：`INDEPENDENT_SOL_W43_EVIDENCE_R3_REAUDIT_COMPLETE`


## 1. 対象・開始条件


Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W43-v2-work`
固定監査HEAD: `dee2d3e8e18ad8eb1d01ac5b9d1c99d256c329a0`
契約: `sources/2026-W43/execution/audits/independent-sol-w43-evidence-r3-reaudit-request-20261025.md`


| Remote確認対象 | Expected | Actual | 判定 |
|---|---|---|---|
| W43 HEAD | dee2d3e8e18ad8eb1d01ac5b9d1c99d256c329a0 | 同左 | PASS |
| W43 root Tree | 5defa56f58597473338847bc7f0fd16ad4b2f17d | 同左 | PASS |
| main HEAD | 041a08dfef3112643cbf85b4a86a7b6f9128aed6 | 同左 | PASS |
| main root Tree | a134dc36a407d08ab1de416324229b3955e0325a | 同左 | PASS |
| production/survey-core-v2 HEAD | 774dd39a951c9ac3818e83dfffd4c7666efb0a20 | 同左 | PASS |
| Frozen Core root Tree | cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481 | 同左 | PASS |


3 remote refsのGit data read、3 Git commitのtree SHA readにより6件一致。すべてのrepo読み取りは固定W43 HEAD、またはそれに特定されたr2/r3の既存コミット/公的一次資料を対象とした。GitHub書込み・Issue/PR操作・Stage操作なし。


## 2. 監査範囲と証拠強度


**独立実行した検査**：r3 accepted Evidence 32/32実体、Edition View 32/32実体の内容閲覧、acceptance manifest Task/SHA対応32/32、51 Materiality行、Completeness、Supplement r3 21件のsource/task binding、projection ledger 32件、accepted Screening 51件とcanonical Discovery 51件、r2/r3 interactive 32×2件のキー別構造差分、r2/r3 Card accepted SHA対応、r2以前のディレクトリの変更有無、GitHub MetricsアーカイブHTMLにおける日付メタデータ抽出、DeepInfer環境変数ファイル・MemT README・Patch rendered source等の根拠照合、公式公表ページ/独立初出記録を閲覧した。


**実行していない検査**：Frozen Core検証CLIやStage precheckの再実行、アーカイブ全21ソースの実バイトSHA256再計算、重み/PDFのbyte-hash全件照合、AM-Bench/Oracleのv1→v2本文差分全文査読、AA一次ランキングの原表取得、ベンチマーク/速度/製品機能の独立実機再現。Museのvalidator PASSをこれらの独立PASSに代用しない。一次ソースの多くは公式本文又はリポジトリ内アーカイブの部分照合であり、全主張の独立再現を意味しない。


## 3. W43-IA-001〜015 修正確認（全15件）


PASSは指摘された誤りの修正が現在のCard/View表現に反映されたこと、LIMITEDは利用時に明示すべき残存制限又は出典未解決があることを示す。ベンダー測定結果を独立検証済みと認定するものではない。


| ID | 優先度 | 結果 | r3の独立確認と読者リスク |
|---|---|---|---|
| IA-001 | P1 | **LIMITED** | Google Cloud Card `task-0851e82f8db3889fc465` はJSON-LD日付10/21、表示10/22、first_published 10/22T04:10という矛盾を露出し、select enterprise private preview、ZDR/Confidential Compute coming soonを記述。ViewはCONTEXT。いずれも窓内だが初公開日を10/21確定とする根拠は不十分。 |
| IA-002 | P1 | **PASS** | Flint `task-4cea29268a1329179dac` claim-1は512K対応・256K推奨・HF設定262144（入出力合計）を分離。125+/150+ tok/sはベンダー条件付報告であり独立再現ではない。 |
| IA-003 | P1 | **PASS** | DeepInfer `task-409f6833c40c6428a43e` の `DEEPINFER_ENABLE_MTP_VARLEN`、`DEEPINFER_USE_NEXTN_DECODE` default=5、0=無効を、archived `deepinfer-environ-9bd9cf24.py` の記述と照合。 |
| IA-004 | P1 | **PASS（技術表記のみ）** | Metrics `task-642c261d5e82c786ecf6` で `user_selected/auto/product_selected/other/unknown`、4種scope、request_count≠prompts、best-effort integration IDを公式Changelogと確認。ただし**IA-016の窓外問題は未修正**。 |
| IA-005 | P1 | **PASS** | FLUX `task-02df2773fd2e9fdb1cd5` で277.80÷10.95=25.37倍、277.80÷12.45=22.31倍、元記事の26.5倍/96.2%との矛盾を明記。未確認の「最速」見出しは禁止、AA原表未取得は残る。 |
| IA-006 | P1 | **PASS** | Patch `task-5d21d93e7679f5441b8a` はGPT-5.6 Solに修正し、OpenAIの実記事 `/index/coordinated-disclosure-of-critical-vulnerabilities/` を別sourceに追加。rendered-textでありnative HTMLではないと明記、CVE補完なし。 |
| IA-007 | P1 | **PASS** | MemT `task-b09782ca929b9fa55af1` はpaper CC BY-NC-SA 4.0、README software PolyForm Noncommercial 1.0.0、第三者MIT、重み/データ別扱いを区分。アーカイブREADMEのライセンス節も該当表記を確認。 |
| IA-008 | P1 | **PASS** | Bio `task-6c420e98c87871e4a2a0`、Low-resource `task-160489b77720f40bd1e1`、Ming `task-4aa7ba129fdeec8b2555` は共同研究・ベンダー評価・元表未閲覧のAA引用を独立再現と表現しない。各Viewも同様。 |
| IA-009 | P2 | **LIMITED** | Kimi `task-98f3617da0de43652fcd` とFlint `task-4cea29268a1329179dac` に個別supplementを追加した一方、旧連結 `src-1.url` を温存しclaim参照にも残す。source→claimの厳密1:1復元は未達（IA-017）。 |
| IA-010 | P2 | **LIMITED** | Oracle `view-1d7d93a70eeabd2b1c4e`、AM-Bench `view-1fc486ce9ce010e398e9` はv2 revisionのみINとしてCONTEXT限定。v1-v2本文/ablationの独立全文差分は未実施、新研究成果と断定不可。 |
| IA-011 | P2 | **LIMITED** | Duet `task-3670fe4328b9fa322a0b`、1Password `task-673368bcdc8bcd59d611` でcatalogue 6000+と利用可能数、rolling/coming soon、agentが資格情報を見ない等のベンダー主張を区分。ただし接続先別の実利用検証なし。 |
| IA-012 | P2 | **LIMITED** | Nemotron OpenMDW-1.1≠OSI認定、Ming MIT、DeepInfer Apache-2.0、Kohaku custom licenceの区分をCard/補助資料で確認。重み実ファイル・全license本文とOSI登録・商用可否を独立網羅検証はしていない。 |
| IA-013 | P2 | **PASS** | Auto-mode `task-ac27404fe35327b74df9` で8/7旧記事OUT、10/22更新IN、翌週展開はFUTURE。MOSS report/README APIの本文公開・告知・稼働証明も区別。 |
| IA-014 | P2 | **PASS** | Grok `view-55f087dd70eb920ce6d4` はNON_MATERIAL / OTHER。COMPLETE=受領完了、センサPARTIAL=2 pinned IDs、主張掲載禁止。projection ledgerで7 mapped / 25 passthrough確認。 |
| IA-015 | P2 | **PASS** | r2 supplement実体6件（8件ではない）と歴史的Tree SHA転記訂正を確認。旧r1/r2 acceptedは今回の変更ファイル0件、過去監査記録は上書きなし。 |


**総括**：PASS 10、LIMITED 5、FAIL 0（旧15件の修正評価）。ただし新規P1 IA-016により総合判定はREQUEST_CHANGES。元のP1が実質的に修正されたこととStage適格は独立の問題。


主要一次資料：GitHub Metrics https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode/ ; Flint https://recursive.com/updates/introducing-recursive-flint ; DeepInfer https://github.com/deepseek-ai/DeepInfer/blob/main/deepinfer/environ.py ; FLUX https://fal.ai/flux-3-max ; Patch https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/ ; MemT https://github.com/MemTensor/MemT-1.0/blob/main/README.md ; Google Cloud https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers/


## 4. W43-IA-016 — P1 GitHub Metricsの窓外公開（BLOCKER）


W43 profileはAmerica/New_Yorkで `[2026-10-16 18:00-04:00, 2026-10-23 18:00-04:00)` = UTC `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)` を定める。右端は**排他的**。


GitHub公式HTMLアーカイブ `sources/2026-W43/collectors/primary/runs/20261025T044100Z-muse-r3-evidence/raw/github-metrics-20261023.html` を独立に検索した結果：
- JSON-LD `datePublished="2026-10-23T16:42:03-07:00"` = `2026-10-23T23:42:03Z`
- 別JSON-LD `datePublished="2026-10-23T23:42:03+00:00"`
- `dateModified="2026-10-23T23:43:37+00:00"`。publishedとmodifiedは異なる。
- 表示HTMLの `<time datetime="2026-10-23">` は日付精度のみ。
- 外部独立観測 https://forck.live/items/27301-usage-metrics-api-adds-usage-from-tools-like-opencode は announced 23:42 UTC、first seen 23:53 UTC。補助資料 https://windowsforum.com/news/github-copilot-usage-metrics-api-adds-client-level-reporting-for-opencode-and-more.449825/ にも23:42:03+00:00への参照。


**結論**：公式記事の公開イベントはW43終了の**1時間42分03秒後**であり、OUT_OF_WINDOWが成立する。これは記事の最終更新時刻を初出と誤認したものではない。別のGitHub公式API稼働/公開イベントが**同日22:00Zより前**に存在するかは今回の一次資料から証明できなかった。「別イベント不存在」を証明したわけではないため、前倒し公開の可能性はUNVERIFIEDだが、現在の唯一立証済みイベントをIN扱いする根拠にはならない。


r3 Card `task-642c261d5e82c786ecf6.json` は正確な23:42:03Zを保有するのに、View `view-642c261d5e82c786ecf6.json` は `window_relation=MAIN_EVENT`、`materiality=CONTEXT`。accepted Discoveryも `published_at="2026-10-23"`、`provenance.reason="Fresh in-window lead"`。accepted ScreeningはMAYBE、ledgerはCONTEXT。**上流の期間内前提と下流の実時計証拠が衝突**し、技術enum修正によって消える問題ではない。


影響：Discoveryの時間精度・前提、Screeningの候補適格性、Card temporal/Event、View window_relation、Materiality/Completeness、後続Selection。Stageは未移行であるものの、accepted Screeningを正当性未確認のまま使ってtrusted `EVIDENCE_REVIEWED` に進むことは禁止。単にViewをNON_MATERIALに編集して隠すだけではaccepted Screeningの誤前提を修復しない。


**安全な修正経路（提案、未実施）**：
1. 対象Metricsの「記事公開」以外にUTC 22:00前の独立した一次イベントが存在するか、識別子・時刻・本文で決着させる。存在しなければ`OUT_OF_WINDOW`、W43新規記事として扱わない。翌週候補または明示した過去/期間外CONTEXTのみを検討。
2. operator/editorial SolがFrozen Coreのauthority invalidation規定と現在のaccepted Discovery/Screeningの関係を照合し、**上流Screening再生成を要するか**を正式に判定。今回の資料ではaccepted Discoveryの「Fresh in-window」が偽となるため、**上流authorityを失効して再Screeningを行う保守的な経路を推奨**。canonical受入済ファイルの直接書換え、履歴改変、Core修正は禁止。
3. 正規のoperator authority（必要ならHuman判断）のもと、対象の時刻精度と選定理由を改め、正規パイプラインの契約に従ってScreening→Evidence→View→Materiality→Completenessを再生成、受入ハッシュ/Stateとの整合を再検査。独立Solが再審査してからStage可否を新規判定。
4. ここでは**受入済み上流をderived-only変更で正当に迂回できるという根拠が未確認**。したがって「derived-onlyで十分」と承認せず `BLOCKED_REQUIRES_AUTHORITY_REVIEW`。Core/Human Gateを迂回しない。


## 5. 同じ10月23日の時間境界スイープ


| 対象 | r3のイベント時刻証拠 | 現在の独立判定 |
|---|---|---|
| GitHub Metrics | 23:42:03Z publisher JSON-LD | **OUT（確定）** |
| GitHub Teams (`w43-primary-github-teams-20261023`) | ChangelogはOct23表示のみ。exact UTC time未取得。公式関連GitHub discussionも日付表示。 | **UNRESOLVED**：Metricsと同様に遅い可能性を排除できない。時刻原本の取得が必要。 |
| Kimi K3.1 Pro | 公式X 17:15:24Z（Card）、blogは10/23日精度のみ | **X発表IN**。blogの00:00Zは実時計ではない。将来11/4 weightsと区別。 |
| NVIDIA Nemotron E4B | 10/23日精度、補助sourceは仮の00:00Z | **UNRESOLVED**：10/23 22Zより前の実公開時刻が必要。 |
| TanStack AI 1.0 | 10/23日精度のみ（公式blog） | **UNRESOLVED**：tag/publish metadataで時間決着。 |
| OpenAI frontier training security | 10/23日精度（公式記事）、外部feedには同日10:00Zという記録 | **INの傍証あり／時計一次証拠は限定**。日付だけから自動INとはしない。 |
| Vercel/Ollama distribution support | Cardは10/23日付、version/pin未確認 | **CONTEXTとしてLIMITED**、配布時刻の確証なし。 |


「日付のみ」の場合、`T00:00:00Z`を埋めても公表時計の検証にはならない。10/23の候補に対しては特に誤IN判定を誘発し得る。上記は網羅的な公開時計収集ではなく、**32 Card内のOct23該当行全件の時刻精度監査**である。


## 6. IA-017 — Kimi/Flintのsource provenance残欠


Kimi r3 Card `task-98f3617da0de43652fcd.json` の `sources[0].url` は依然として `https://x.com/Kimi_Moonshot/status/2113680701770068067 + primary:kimi.ai/blog/kimi-k3-1-pro`。Flint `task-4cea29268a1329179dac.json` は `primary:recursive.com/updates/introducing-recursive-flint + primary:huggingface.co/RecursiveSI/flint`。いずれも**有効な単一URLではない**。別々のsupplementは実際に存在するが、各claimの`source_ids`には旧`src-1`が残る。Kimi公式X＝vendor social statement、blog＝official documentation、Flint announce＝news、HF card＝artifactを一括一対一出典と誤って扱う余地がある。


**判定 LIMITED（P2）**：出典分割は大幅改善、厳密なclaim単位の1:1 provenanceには未達。Frozen Coreが元task `src-1`を温存するなら、canonical Discoveryを改変せずedition-local claim/citation crosswalkで各claimの支持箇所を**独立supplement IDに明示的に結び、旧fused locatorを引用表示に使用しない**。証明できないベンチマーク範囲・未発売weightsの断言は除く。単独ではIA-016と異なりStage再生成のP1根拠に格上げしない。


## 7. IA-018 — r2→r3 正規差分再計算


`execution/compat/evidence-source-class-projection/interactive-evidence-r2.json` と `r3.json` を全32 discovery_idで構造比較（追加0、削除0）。source_bindings、claims、verification、limitationsその他materiality_rationale以外に差分のあるもの**19件**。materiality_rationaleのみ変更**13件**。完全同一0件。前者19件のうちsource_bindings欄を含む変更はDeepInfer、FLUX、Metrics、Kimi、Nemotron、Patch、MemT、Ming、MOSS trainer、Flintの計10件（比較ベースのフィールド変化）。後者13件はcarry、Muse adoption、Oracle、Decisions、DeepSeek、Eleven、deprecation、Teams、TanStack、Voxtral、AM-Bench、OpenAI securing、Vercel/Ollama。


accepted Evidence manifestのr2→r3 `sha256` は**32/32変更**。これはCore task/basis/acceptanceの再生成を含むため、「32件のclaimが編集された」証拠ではない。Muse closureの「Card 20 changed / 12 same」は実際のinteractive入力の**19 substantive / 13 rationale-only**とは一致しない。区別せず統計に使用不可。


## 8. 整合性・Frozen Core・残余


- r3 Evidence acceptance **32件**、Card 32実体を閲覧し32 PARTIALを確認。r3 Views acceptance **32件**、View 32実体を閲覧しmanifest Task/SHAを32/32照合。
- Views: MATERIAL 20、CONTEXT 11、NON_MATERIAL 1（Grok）。Materiality Ledger 51行: 20/11/1/19 EXCLUDED。Screening accepted 51件: KEEP 17、INSPECT 4、MAYBE 11、DROP 19。19 DROPをledgerで個別に確認。12 W42 carryは11 EXCLUDED、1 CONTEXTで処分記録あり。
- Supplement r3 **21 source rows**、source_id unique 21、task binding 21/21 valid、raw_path非空21/21。実rawファイル21点のbyte SHA256検算はNOT_EXECUTED。
- Projection ledger 32件：7 projected / 25 passthrough。Xをprimaryへ昇格させる根拠なし。
- Completeness `LIMITED`：`weekly:current-relevance` LIMITATION、`weekly:technical-significance` LIMITATION、`weekly:carry-over` SATISFIED。zero independent benchmarking、AA原表なし、v1/v2差分未読は残存。20 MATERIALは候補分類でありSelectionで20記事を確定した意味ではない。
- r2 prior parent `f421dceb…`→固定HEADのGitHub compare（4 commits/164 files）は**全変更ファイルが `sources/2026-W43/` 内**で、古いr1/r2 acceptedディレクトリの変更0件、production-state/production-profile変更0件。mainとFrozen Core refの6件照合 PASS。ただしCore dynamic validatorやraw SHA検算を独立実行していないため、これらに「独立実行PASS」は付与しない。
- `supplement-r3.json`にはpublisher日付から仮置きした`T00:00:00Z`が9行（Auto-mode、Decisions、FLUX×2、Kimi blog、Nemotron、Patch、Flint×2）。その文字列が**実際に観測した公開時刻であるとの裏付けはない**。GCPの旧仮midnightはr3で撤回したが、他の9行の説明/精度ラベルは残余課題。


## 9. Trusted Stageと次の唯一の作業単位


**独立編集判定：`REQUEST_CHANGES`。**
**`CANDIDATES_NORMALIZED → EVIDENCE_REVIEWED`：** **NO**。
**`ADVANCE_STAGE` 実行：禁止、未実行。**
理由は(1) IA-016確定窓外イベントがaccepted Screening MAYBEとView MAIN_EVENTに混在、(2) 同日date-only隣接候補の時間境界適格性が未確認、(3) 上流accepted authorityの正規invalidaton手続の必要性が未裁定であること。既存15件の修正PASSはこれらを取り消さない。


**編集統括Solに推奨する次のbounded action（現セッションは実行しない）**：IA-016と同日date-only候補の公開時刻・独立イベントIDを一次資料で確定し、Frozen Coreの無改変手順で必要な上流失効/再Screeningとedition-local再生成の契約を**1件だけ**作成する。IA-017 citation crosswalkとIA-018集計訂正、9件midnight精度ラベルはその同じbounded修正に含める。P2のOracle/AM-Bench全文diffやベンチ再現を根拠なく新P1に昇格させない。未承認のhuman gatesを操作せず、Selection/Architecture/Draft/PDFへ進めない。


停止トークン：`INDEPENDENT_SOL_W43_EVIDENCE_R3_REAUDIT_COMPLETE`
