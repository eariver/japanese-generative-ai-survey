# J-GAS W42 r30 — 独立Publication Readiness監査


監査日：2026-10-20 JST
判定：**REQUEST_CHANGES**
性質：独立read-only監査。Human Publication Preview承認ではない。GitHubへの書込み、Gate操作、Freeze/Release、コミット操作は一切実施していない。


## 0. Executive disposition


対象Repository：eariver/japanese-generative-ai-survey
対象Branch：weekly/2026-W42-v2-work
指定HEAD：b33098f32027d52a245fbbeb07586d52fa7ae6f0
指定Root Tree：a2ace998c38c94a3260371bbe8f8acd4511e6feb
PDF：surveys/weekly/2026-W42/main.pdf
PDF SHA256：8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9


**判断：現時点でHuman Publication Previewへの提示・承認を進めず、限定修正と実行経路の正式整理を要求する。** B54は一次資料で実質解消できた。他方、B57本文の「10月16日にリポジトリが公開」という読者に伝わる事実は、8月21日「Public release」と両立しない。10月16日は「ASPIRE v1.0 release」であってリポジトリの初公開ではない。さらにMuseが行ったローカルCLI実行はCoreのStage validatorを呼ぶ技術的経路ではあるが、r30承認契約が指定したGitHub Actions operator workflowによるtrusted admissionを経た証拠がない。これらを、既に存在するVALIDATED_DRAFT/RELEASE_CANDIDATE Stateの存在と混同してはならない。


r29独立監査済み21ページ・110表セルの全面再監査は実施しない。r29のPASS_WITH_LIMITATIONSを無条件PASSへ読み替えない。


## 1. Git genealogy, change allowlist, protected invariants


- HEADとBranchのGitHub Compare（指定HEAD→Branch）が identical / ahead 0 / behind 0。監査時点のremote branchは指定HEADと一致。
- 開始HEAD 4ac9e5eb8aee164a0ff15427bea4dd26716240cd から指定HEADまでGitHub Compareは ahead 3 / behind 0 / merge base=開始HEAD。順序は aee3a287d2e5912840c40929abc7312cbb5ef805（証拠・正式レビュー・候補作成）、454e838eb5b7e4a7a0225bf20776ef2aeee7a253（Bridge 1: VALIDATED_DRAFT）、b33098f32027d52a245fbbeb07586d52fa7ae6f0（Bridge 2: RELEASE_CANDIDATE）。
- 比較差分26ファイル。新規publication/v2品質・レビュー・候補、execution/validation-to-preview-r30、Bridge request/receipt/checkpoints、production-state.jsonおよびexecution/index.mdの追記とsession文書に限定される。差分に既監査TeX/PDF/Reader、r1 Architecture、Selection、共有Core、schemas、scripts、config、workflow、main変更はない。ArchitectureのGit blob 14e17d80c148747ef1804ac7d80a3cf4e5d12bbfも開始時指定値と一致。
- **限界**：GitHub connectorのcommit responseはroot tree SHAを露出しない。よって指定Root Tree a2ace998...の厳密な独立照合は未完了。Commit SHA/祖先比較/ファイルblob/保護差分の確認は完了。Tree照合済みと偽称しない。
- 固定コミット：https://github.com/eariver/japanese-generative-ai-survey/commit/b33098f32027d52a245fbbeb07586d52fa7ae6f0


## 2. Formal authorities, binding and separation of roles


1. Quality Bundle：3件のDETERMINISTIC checkがPASS（IDENTIFIER_PRESERVATION / PDF_PREFLIGHT / SUBJECT_ENTITY_PROPERTY_BINDING）。各resultのパスとSHA256を持つ。Bundle JSONを独立SHA256計算し、Candidateが参照する d127d2cfe8fe57eda05d2096ff77be1496f1eec120fbb7994633fa0cc8be0eae に一致。
2. Semantic review：11件のchecks、status PASSED、reviewed_byは明確に Muse worker。実体SHA256=2638c2bf28316e501b646f619adab7f7eb2194fc6407f995bf93c8f077211d88、Candidate参照に一致。独立Solの判定ではない。
3. Visual review：2件PASS、status PASSED、Muse worker作成。実体SHA256=af243137f7a8e116508f3fa4e68596fe96604519c12489b9eb45b2ce09b53731、Candidate参照に一致。
4. Reader-Surface semantic：Museとは別のsubagent（記録上の「Sol review role」）がTeX SHAを自己計算、8/8 PASS、3 WARNING/UNRESOLVED、INFO 1 RESOLVEDと記録。raw reportは execution/validation-to-preview-r30/independent-surface-review-raw-r30.md として保存され、正式JSONにcheck/findingsが転記。実体のファイルSHA256は 383acda6afbe365c32a40930db0d5b209dc283b3f0885dcee9a30070e7ec4c84。JSON内部review_sha256=2bc7ca076b0e5a1befe415933c80a42e8e9bc297514577dd390f640cc9fb3319 はファイルSHAではなく、Core validatorがreview_sha256を除外したpayloadから算出する論理digest（scripts/survey_reader_surface_gate_v2.py 912,937-941）であり、値の相違を不整合と誤判定しない。
5. Reader-Surface Gate：PASSED、11ルール、WARNING 3 / BLOCKING 0。原稿・preview.sty・r18・Readerなどのsurfaceをバイト参照。独立レビュアー欄はsubagentで、**別workerであっても同一Muse実行内部の委託レビュー**。ChatGPT側の真に別セッションの独立人間承認や本監査と等価ではない。
6. Publication Candidate：READY_FOR_PUBLICATION_PREVIEW、JSON実体SHA256=9add24b0432d990f8c85515ed17a90d7bf80a1d267efec4cb47093922a19c00b。TeX=2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3、PDF=8c7a06e7...、Reader=47634ae3...、Bundle/Semantic/Visualを参照。全ての主要JSON実体digest参照に独立照合成功。
7. Core Stage checkpoints：DRAFT_COMPLETE.json（DRAFT_COMPLETE→VALIDATED_DRAFT、7名のauthority）、VALIDATED_DRAFT.json（VALIDATED_DRAFT→RELEASE_CANDIDATE、publication-candidate）。Bridge receipt、contract結果、request等の主要SHA256参照を独立に計算して一致。これはレコードとStage validatorの実行証拠であり、後述のworkflow admissionの証明とは異なる。


## 3. Operator Bridge: local CLI vs approved transport


**F-OP01 — HIGH / PROCESS-AUTHORITY / UNRESOLVED**


位置：
- sources/2026-W42/execution/instructions/2026-10-20_muse-w42-r30-integrated-validation-to-publication-preview.md §3
- .github/workflows/survey-production-v2-operator-bridge.yml lines 101–140, 170–250, 295–329
- sources/2026-W42/execution/sessions/muse-w42-r30-20261020.md steps 7–8
- r30 commits 454e838... / b33098f...


根拠：承認済み契約は「既存のtrusted-reviewed GitHub Actions Operator Bridge workflow → first-party CLI」という権限経路を指定し、workflow制約に阻まれれば停止、代替routeは禁止している。Workflowのpreflightは request commitが「新規request JSON一件だけの変更」であることを強制し、reviewed-mainのtrusted runtimeと保護authority等を検査する。一方r30の2つのStage移行は、セッション自身が「local first-party CLI」と記録し、requestを含むコミット454e838...は他のState/checkpoint/receiptも同時に変更、b33098f...も同様に8ファイルの変更。該当するrequest-only dispatch commit、workflow run ID、preflight成功ログは示されていない。過去r9 precedentへの言及は、本件r30の明示契約の例外承認に代わらない。


評価：同じCoreのstage validatorを通した可能性は高く、Stage成果物の真正性を一概に否定するものではない。しかし「承認されたtrusted Operator Bridge transportの通過」は未立証、literalな契約経路と非整合。ローカル実行をGitHub Actions admission済みと記載してはならない。


推奨処置：Human Ownerによる明示的な経路例外・等価統制の追加監査か、正式な復旧実行契約を先に確立する。直接State変更、既存歴史改変、強制push、無権限Gate変更、stage replayは禁止。実行方法・使用trusted script SHA・環境隔離・preflight相当チェック・requestのcommit単位・run evidenceを残す。既に到達したStateを黙って承認扱いしない。


## 4. High-risk primary sources B16 / B54 / B57


**B16 / CONFIRMED (bounded)**：Reflection BeamのHugging Face LICENSE実体ページでApache License Version 2.0全文と11.4kBのLICENSE配置を確認。独自Built-with表示バッジを課す追加文言は本文に確認されず、通常のApache 2.0義務と第三者部分の扱いを残すTeX §3、Table T3は妥当。「10月7日作成・16日release」はLICENSE自体からは立証しないという境界を維持。
一次資料：https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/LICENSE


**B54 / CONFIRMED with snapshot caveat**：Valsの2026-10-12「Updates」は 7/79、19.17%、$0.15/test を明示。一方動的model cardの順位母数は新しいcrawlで7/80、Muse取得時は7/81であり、リアルタイム母数は変動。TeX §7 lines 720, 742の「79件中7位」は10月12日時点snapshotとして支持される。見出し・追記・表の母数を同時刻の値と誤読しないよう注記推奨。
**重要な再確認**：Vals一次資料「Harvey's Legal Agent Benchmark v1」ランキングはGLM Legal行を 19.17% / $0.15 / **1h12m** と表示する。したがってTeXの「1件72分」（§7 lines 720, 742）は事実上立証された。r30 F02の「不明・37m25sとのドリフト」は別スコープのモデルカード遅延値とベンチマークdurationの混同であり、今回の独立監査では**解消**。既存r30 formal recordsは後から上書きせず、次版のレビューでF02を明示的に再裁定すること。
一次資料：https://www.vals.ai/models/zai_glm-legal
ベンチマーク一次資料：https://www.vals.ai/benchmarks/hlab-v1


**F-B57 — HIGH / READER-FACTUAL / UNRESOLVED**


位置：surveys/weekly/2026-W42/main.tex §7 lines 759, 763、Table T7 line 732。参照 B57=NVlabs/ASPIRE、B56=6月論文。
再現：NVlabs/ASPIREコミット 7ba73d3bcac8f6b6d4a7d67ed4040988f768d282 は **2026-08-21T19:53:37Z**、メッセージ「Public release」でREADME/LICENSE/実装を追加。コミット fa00f0ef2bc1d91d594b9aa502c22133c9f538f7 は **2026-10-16T03:57:48Z**、メッセージ「ASPIRE v1.0 release」。READMEの[2026-10] v1.0も裏付け。したがって「NVlabs/ASPIREリポジトリの公開が10月16日の今週の出来事」と書くと、8月公開済みのリポジトリを10月16日に初公開したように誤記する。日付精度の不足ではなくイベント種別の誤同定。10月16日のv1.0は真実。
推奨：文章を「8月に公開済みのNVlabs/ASPIREで、10月16日にv1.0が公開された。6月論文は背景」と訂正。Table T7の「10月公開」も「10月16日のv1.0公開」等に精緻化。§7 line 763の「10月16日のX投稿」は別の投稿一次証拠が書誌にないため、投稿URL・日付を追加確認できなければ単に「告知投稿」に緩和。TeX/PDF変更時は候補ハッシュとFormalレビュー/Reader-Surface Gateを新しい原稿に適切に再結合し、正規の状態回復計画を取る。
一次資料：https://github.com/NVlabs/ASPIRE/commit/7ba73d3bcac8f6b6d4a7d67ed4040988f768d282
v1.0：https://github.com/NVlabs/ASPIRE/commit/fa00f0ef2bc1d91d594b9aa502c22133c9f538f7


**F-B54 — LOW / SNAPSHOT-DISCLOSURE**：TeX §7 lines 720,742に「10月12日時点のVals公表値：79件中7位」のような時点表示を推奨。数値の差し替え自体は不要で、Human Preview blocking itemとはしない。


## 5. L03/L04 narrow reproducibility


L03（PDF 21/21）：r30報告書は不変PDF SHA256=8c7a06e7...、505102 bytes、PyMuPDF 1.28.2、150 dpi、A4、p-01...p-21の既存PNGと21件全件byte-identicalと明記。入力・関数・解像度・判定基準があり同じレンダラー条件で再現可能。ただしr30 L03ファイルに個別21対のSHA表やコマンド実行標準出力までは記録されず、**本監査が21枚を自ら再レンダリングしたわけではない**。r29で全ページ既監査済み、今回はPDF/PNG未変更なのでlimited assuranceとして採用。第三のレンダラーでの一致は主張しない。
L04（28/28）：sources/2026-W42/candidate-selection-v2.json のSELECTED=28を実際に抽出し、sources/2026-W42/architecture-v2.json 7 packagesのprimary/supporting IDs集合と機械照合。28件すべてちょうど1 packageに対応、未対応0、重複0、選外混入0。package配分はP1=2、P2=2、P3=6、P4=6、P5=4、P6=5、P7=3。TeX各節への配置の全面再監査はr29監査に依拠し、r30のspot checksを利用。


## 6. Final State and decision boundary


- production-state.json: lifecycle_state RELEASE_CANDIDATE、next_action PUBLICATION_PREVIEW、terminal_reason HUMAN_GATE_REACHED。
- human_gates.architecture_review=approved、publication_preview=pending、publication_preview provenance=null。
- machine_checkpoints.validation=passed、publication_preview=pending、freeze=pending、release=pending。
- Human Preview承認記録・Freeze・Release・main mergeはこのr30差分に存在しない。HUMAN_GATE_REACHEDは停止地点であり承認ではない。
- Stateが正しく記録されたことと、operator transportの契約上の正当性と、読者本文の誤りの不存在とは独立した命題。


**最終判定：REQUEST_CHANGES。**
B54は出版を止める理由ではない（79は10月12日時点の数、72分は公式ベンチで裏付け）。B57は放置してHuman Previewに進めず、「リポジトリ公開」対「v1.0公開」の事実訂正を必須とする。加えてF-OP01の経路例外/正規復旧をHuman Ownerに明示承認してもらう。これらが解決して改訂された正確なPDF・候補・State根拠が揃った後、別途Human Publication Previewに提示すること。**本監査はPublication Preview承認を行わない。**


## 7. Evidence index (fixed references)


- W42 r30 SHA: https://github.com/eariver/japanese-generative-ai-survey/commit/b33098f32027d52a245fbbeb07586d52fa7ae6f0
- r30 evidence: https://github.com/eariver/japanese-generative-ai-survey/tree/b33098f32027d52a245fbbeb07586d52fa7ae6f0/sources/2026-W42/execution/validation-to-preview-r30
- r30 canonical reviews: https://github.com/eariver/japanese-generative-ai-survey/tree/b33098f32027d52a245fbbeb07586d52fa7ae6f0/sources/2026-W42/publication/v2
- r30 State: https://github.com/eariver/japanese-generative-ai-survey/blob/b33098f32027d52a245fbbeb07586d52fa7ae6f0/sources/2026-W42/production-state.json
- Fixed PDF: https://github.com/eariver/japanese-generative-ai-survey/blob/b33098f32027d52a245fbbeb07586d52fa7ae6f0/surveys/weekly/2026-W42/main.pdf
- Reviewed bridge workflow: https://github.com/eariver/japanese-generative-ai-survey/blob/c8d0ecc1c9566a2303ad3b4c42635d4b672650e4/.github/workflows/survey-production-v2-operator-bridge.yml
- B16 primary: https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/LICENSE
- B54 primary: https://www.vals.ai/models/zai_glm-legal ; https://www.vals.ai/benchmarks/hlab-v1
- B57 primary chronology: https://github.com/NVlabs/ASPIRE/commit/7ba73d3bcac8f6b6d4a7d67ed4040988f768d282 ; https://github.com/NVlabs/ASPIRE/commit/fa00f0ef2bc1d91d594b9aa502c22133c9f538f7