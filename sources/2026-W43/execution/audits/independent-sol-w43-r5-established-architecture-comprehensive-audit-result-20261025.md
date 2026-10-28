<!-- Edition-local GitHub TRANSCRIPTION of the independent Sol Google Drive original, not guaranteed byte-identical. Exact original: https://drive.google.com/file/d/1mYjruB6L4gHdkEFh001VGXPOqwnFNgCW/view?usp=drivesdk, file ID 1mYjruB6L4gHdkEFh001VGXPOqwnFNgCW, name 20261025184803_SolReview.md, Drive metadata 34,405 bytes. Source is UTF-8 BOM+CRLF text; this repository copy uses LF and drops BOM, plus this header. DO NOT substitute GitHub text blob hash for raw Drive SHA-256. Fixed audit subject: 6f961295c6743248c2bccb34e15cb84116bf4de7 / Root Tree 6a1f716b024cf742162a95dfb0bace227ee29f5e. -->

# J-GAS 2026-W43 Architecture r5 — 独立Sol包括監査（post Trusted Operator）


- 監査日時: 2026-10-25 18:48:03 JST
- 監査種別: read-only / 固定HEAD / 人間によるArchitecture Review前 / 独立Sol監査
- リポジトリ: https://github.com/eariver/japanese-generative-ai-survey
- 監査契約: https://github.com/eariver/japanese-generative-ai-survey/blob/333c41a611d9c5d499556338e1af61c5335b68c6/sources/2026-W43/execution/audits/independent-sol-w43-r5-established-architecture-comprehensive-review-request-20261025.md
- 固定対象HEAD: `6f961295c6743248c2bccb34e15cb84116bf4de7`（commit読取成功）
- 契約に指定されたRoot Tree: `6a1f716b024cf742162a95dfb0bace227ee29f5e`（**Git treeの独立取得はNOT_VERIFIED**。記載値をPASSに流用しない）
- Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / 指定Tree `a134dc36a407d08ab1de416324229b3955e0325a`（commit読取済、Tree非照合）
- Frozen production/survey-core-v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / 指定Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`（commit読取済、Tree非照合）
- 可変branchの実際の最新HEAD/Tree: **NOT_VERIFIED**。監査は最新ではなく上記固定HEADのファイルを参照。


## 0. 判定（Human Gateを承認しない）


| 対象 | 独立判定 | 理由 |
|---|---|---|
| Selection | **PASS_WITH_LIMITATIONS** | 32件→19 SELECTED/1 HOLD/12 REJECT、ID・配置は自己集計一致。ただし全32 Evidence Card・原典rawの再hash未了。 |
| Architecture | **REQUEST_CHANGES（P2中心）** | 8/31の構造と重要な既知境界は保持するが、割合計算の説明矛盾、製品メタデータ時刻ラベル逆転、CVE語の不適切な短縮が残る。 |
| Upstream Evidence | **PARTIAL / LIMITED維持** | source-tierは限定的。AA原表、重みbytes、製品live試験、MemT論文数式などを再現済みと記せない。 |
| Trusted Stage | **RECORDED/PASS receipt をreadback** | Selection→Architectureのoperator receiptとproduction-stateに矛盾なし。ただしCore-native validatorを独立再実行していない。 |
| Human Architecture Review提示 | **現状の無条件提示は推奨しない** | R5-N01～N03をedition-localで是正・再確認し、既知未解決問題を明示した資料を提示するのが適切。監査者はGateを操作しない。 |


P0は今回アクセスした範囲で検出なし。新規P1なし、新規P2候補3件。これは31節を実際に発行済みの本文とみなす検査ではなく、提案Architecture全31項の内容・境界審査である。


## 1. 手続き・実査した範囲と欠落


**独立実施（今回）:** GitHubコネクタで固定対象commit、main/Coreの指定commitを取得。固定HEADでArchitecture、Selection、Matrix、Summary、Attention、State、両Bridge receiptをread-onlyで再取得してJSON構造・ID/配置・件数を独立集計。独立監査契約、selected-19の別risk ledger、r4の監査結果、r5のfal原典crosswalkを照合。公式一次ページを独立閲覧し、一部主張と計算式を再検算。


**未実施/取得不可（NOT_EXECUTED または NOT_VERIFIED）:** Gitのroot Tree/remote branch HEADの厳密照合（connectorのcommit応答にtreeがなく、公共API読み取りも失敗）、Core-native runner/validatorの再実行、JSON file raw SHA256を各ファイルでバイト再算出、r3/r4/r5の全history snapshot再hash、32件のaccepted Evidence Task本文と32 Edition View本文の全件参照・32対32行単位crosswalk、51 Materiality本文、25件source supplementのraw bytes完全対照、MemT 65頁の数式/ablations通読、AA原表と投票原データの検査、API/SDK/モデル重み/性能の独立再現。


「readbackしたPASS」「原典をブラウザで閲覧した」「独立実測した」「原ファイルbytesを検証した」を混同しない。原文が変化しうるWebページは現在の表示であり、W43当時の固定raw snapshotを再現するものではない。


## 2. Trusted Operator・Stageと固定対象


| 照合 | 固定HEADで直接確認した値 | 独立結果 |
|---|---|---|
| `production-state.json` | `ARCHITECTURE_ESTABLISHED` / `HUMAN_GATE_REACHED` | READBACK PASS |
| machine selection / architecture | `passed` / `passed` | READBACK PASS |
| Human Architecture / Publication Gate | `pending` / `pending` | **双方pending** |
| Selection trusted receipt | `PASS`, lifecycle `SELECTION_COMPLETE`, event `f0b82346a16cac0eea091c39e1d6b8a786ca99ee` | READBACK PASS |
| Architecture trusted receipt | `PASS`, lifecycle `ARCHITECTURE_ESTABLISHED`, event `bf5d8d14897c14d42931de0604df64df9255643e` | READBACK PASS |
| Architecture JSON | `PROPOSED` | machine EstablishedとHuman未承認の両立 |
| Core-native validation rerun | — | NOT_EXECUTED |
| Frozen Core filesのSHA/Tree差分 | — | NOT_VERIFIED（固定対象にCore改変を確認できないが、全Tree差分照合なし） |


Bridge receiptがPASSであることは、独立技術審査のPASSではない。Trust境界は、operator requestのimmutable SHA→受理receipt→generated commit→machine stageまでに限る。Human判断の生成や代行は許されない。


## 3. 独立集計の構造不変条件


- Matrix 32行 / ID unique 32。Selection 32件（SELECTED 19、HOLD 1、REJECT 12）。
- 8パッケージ / must_cover 31件、内訳 `5+6+4+3+4+3+3+3=31`。
- SELECTED配置 19・unique 19。未配置 0、非SELECTED混入 0。
- Attention `68/68`、ID unique 68、limit 100、overflow 0、truncated false。カテゴリ内訳: MATERIALITY:EXCLUDED=19、MATERIALITY:NON_MATERIAL=2、SCREENING:DROP=19、SCREENING:INSPECT=4、SCREENING:MAYBE=11、SELECTION:HOLD=1、SELECTION:REJECT=12。
- Evidence manifestは32件すべてPARTIAL、Edition Views manifestは32件。Materiality summary=51（MATERIAL 20/CONTEXT 10/NON_MATERIAL 2/EXCLUDED 19）、Completeness `LIMITED`（LIMITATION 2/SATISFIED 1）。
- 既知r4独立selected-19 ledgerはネイティブAttention 68とは**別**の原稿上の管理簿。68件の主用途は例外・非採用側で、19選定候補の技術信頼性PASSを意味しない。
- Evidence/Matrix/Architectureの参照SHA文字列は読み取ったが、全実体とのraw-binary hash一括再計算はNOT_EXECUTED。Coreの検証受領を独立hash検査の代用にしない。


## 4. 採用19候補 — 配置/証拠密度/評価の一覧


次表の出典件数・主張件数・制限件数は固定HEADのMatrixに**記録された数**であり、今回独立閲覧した原典数を示さない。19件の配置は自己集計で一意と確認した。


|Pkg|位置|候補 ID末尾|候補|Matrix記録: source/claim/limit|独立審査上の主な制限|
|---|---|---|---|---:|---|
| P1 | PRIMARY | `98f3617da0de4365` | Moonshot Kimi K3.1 Pro | 2/4/3 | X投稿の諸元値、重みNov4 FUTURE / 価格liveと配布区分 |
| P1 | PRIMARY | `4cea29268a132917` | Recursive Flint | 3/3/3 | active約2.5B対total39.8B、Eureka/速度は販売者条件 |
| P1 | SUPPORTING | `8f140062cf7044ea` | NVIDIA Nemotron 3.5 Bolt E4B 4GB | 3/2/3 | effective4Bとtotal8B、OpenMDWとGemma基盤の別条件 |
| P2 | PRIMARY | `409f6833c40c6428` | DeepSeek DeepInfer | 4/4/3 | MTP可変長とdeterministic排他、SM100/Ascendの実走なし |
| P2 | PRIMARY | `b09782ca929b9fa5` | MemTensor MemT-1.0 | 3/3/3 | Gated DeltaNet2/MoS原典数式未精査、1.86倍/66倍は著者測定 |
| P3 | PRIMARY | `3670fe4328b9fa32` | Anthropic Claude Duet | 1/5/3 | 待機列とライブ実装の差、接続可否/安全性未再現 |
| P3 | SUPPORTING | `673368bcdc8bcd59` | 1Password for Agents | 1/3/3 | 資格情報注入はvendor説明、Duet連携はcoming soon |
| P3 | SUPPORTING | `ac27404fe35327b7` | Anthropic auto-mode default | 2/2/2 | Oct22更新INと次週自動既定FUTURE |
| P4 | PRIMARY | `02df2773fd2e9fdb` | fal FLUX 3 Max | 3/3/3 | 10.95/12.45秒やAA Eloは複数公式版で不一致、独立計測なし |
| P5 | PRIMARY | `18a859ebb1ef5004` | Mistral Voxtral 3 | 1/4/1 | TTS言語35+/9/35、preset18/22のvendor内矛盾 |
| P5 | SUPPORTING | `4aa7ba129fdeec8b` | InclusionAI Ming-3.0-tts | 3/3/3 | 月単位日付と独立AA原表欠落 |
| P5 | SUPPORTING | `4514088790849f9c` | ElevenLabs Eleven Realtime v1 | 1/3/1 | AAスコア原表未取得、互換はWebSocket/API範囲に限る |
| P6 | PRIMARY | `5d21d93e7679f544` | OpenAI Patch the Planet | 2/3/3 | rendered-text、PHPパッチ/CVE原証拠未確認 |
| P6 | PRIMARY | `eb7312062a02d1c3` | OpenAI frontier training containment and red-teaming | 2/2/2 | DNS・RL再開・隔離はベンダー記述、独立確認なし |
| P7 | PRIMARY | `6c420e98c87871e4` | OpenAI distributed biological reasoning | 1/3/3 | blind 75% preferenceの外部追試/wet-labなし |
| P7 | PRIMARY | `160489b77720f40b` | OpenAI low-resource language coding evaluations | 1/3/3 | SQLite構築とCOBOL hidden testは別、著者測定 |
| P8 | PRIMARY | `d278dfe78685d601` | OpenAI Decisions API | 2/3/1 | 400問/request、cache write/地域/長文脈の費用 |
| P8 | SUPPORTING | `20a36d83656e2a4b` | TanStack AI 1.0 | 2/2/2 | stable 1.0 vs experimental harness、公開時計の逆転あり |
| P8 | SUPPORTING | `d5bceca2dab4af9d` | DeepSeek V4.1-Flash-1017 | 1/3/1 | 重みSHA/利用料/bench独立追試なし |


## 5. 8パッケージ/31技術小節の全項目レビュー


判定用語：OK(構造・帰属条件は合理的)、LIMITED(原典/追試不足を記事に明示)、FIX(P2相当の具体的修正)。これらは**将来の本文そのものの検証ではない**。


### P1 公開予定の重みと、すでに動かせるモデル:Kimi の API 先行と Flint/Nemotron の重み・ライセンス（5節 / 5.0頁見積）
- 総評: 計数規約が異なる MoE 指標を非等価と記述し、重み配布予定と利用可能状態を分離。Kimiの2.8T/104BはX原文のみ。 ベンチマーク装置・試行条件を比較列に指定した点は妥当。ただしactual HF weight blob/hashやKimi実行の独立照合は未完。
- **§1.1 [LIMITED]** 条件付き妥当: 速報と重み配布は別。設計原文: §1.1 Kimi:API 先行の事実(17:15:24Z・4h44m36s・post ID・$2/$10)と Nov4 FUTURE の区別 — 表:公開状態×時点 [X 原文/supplement 041ec6…/blog]
- **§1.2 [LIMITED]** 条件付き妥当: active/effectiveの非等価。設計原文: §1.2 構成の対比:MoE(2.8T/104B は X のみ・blog は 3T 級 / Flint 39.8B total・~2.5B active per token[出力head含み・入力embedding除外、active body約2.2B]・49 層・256 experts・SWA-513 / Nemotron 8B total・4B effective[計数規約非一致、等価比較禁止])と語彙・打切り・64K〜1M — 表:total/effective/active/ctx[計数方法を列見出しに明記]
- **§1.3 [LIMITED]** 条件付き妥当: 上限/推奨/設定値を別。設計原文: §1.3 文脈長の運用意味:1M / 512K 対応・256K 推奨・262144 設定・64K の区別 — 図:対応/推奨/設定の三層
- **§1.4 [LIMITED]** 試験条件不完全: 比較不能例を脚注へ。設計原文: §1.4 学習・量子化の手続き(Kimi のサイバー除去と RL / Flint の Eureka 探索と 4bit lm_head / Nemotron のフィルタ)とベンチ(分母・harness・温度・top-p・試行平均)の帰属 — 表:bench×harness×分母
- **§1.5 [LIMITED]** ライセンスと可用性は独立バイト未検証。設計原文: §1.5 重み可用性とライセンス(API live、Nov4重み FUTURE[発表・weights配布・再現可能を別status]、HF 14:20/15:12–19:03、重み約款OpenMDW-1.1[OSI未検証]と基盤Gemma-4 Apache-2.0を混同禁止)と価格・API 条件 — 表:可用性×時刻×約款[発表/プレビュー/GA/重み配布/再現を別列]


### P2 推論と記憶の基盤:DeepInfer と MemT の機構（6節 / 6.0頁見積）
- 総評: DSpark の MTP_VARLEN=1 と deterministic の MTP_VARLEN=0、BATCH_INVARIANT=1、seq_seedを排他的に記した。固定版との整合を公式READMEで照合。 MemTの1.86倍と66倍は速度と保存領域で母集団が異なる。65頁数式/ablationの完全精査および学習再現は未実施。
- **§2.1 [LIMITED]** 機構を列挙、実装機能はvendor記載。設計原文: §2.1 DeepInfer の核:FlashMLA/DeepGEMM/DeepEP/TileKernels/DeepSelect/TileLang、注意の DP/均衡 CP、MoE の EP+EPLB、DSpark と確信度予定検証 — 表:核×役割
- **§2.2 [LIMITED]** 排他設定を公式README照合済み。設計原文: §2.2 推測デコード系 DSpark可変長MTP(DEEPINFER_ENABLE_MTP_VARLEN=1、DEEPINFER_USE_NEXTN_DECODE既定5・0で無効、9bd9cf24固定)と決定的サンプリング系(DEEPINFER_ENABLE_MTP_VARLEN=0＋DEEPINFER_BATCH_INVARIANT=1＋seq_seed固定・SamplingParams、NVIDIA限定)は排他的構成例 — 同時有効の記述禁止[MUST-NOT] — コード抜粋 [README・environ.py 8738B]
- **§2.3 [LIMITED]** ハードウェア環境・ベンチ未再現。設計原文: §2.3 実装条件:SM100+Ascend950・toolchain・1017 checkpoint・4xSM100 prefill+64 decode bench・除外(KV・VE/prefill/decode 分離・cross-DP 均衡)の明示
- **§2.4 [LIMITED]** 2つの異種改善指標を別軸で扱う。設計原文: §2.4 MemT の記憶:Gated DeltaNet-2(ゲート付きデルタネット2、Gated DeltaNet-2)・Mixture-of-Storage(混合ストレージ記憶、Mixture-of-Storage)・34B token・二段階+事後、Nano(Qwen3.6-35B-A3B)・Flash(DeepSeek-V4-Flash)、11 bench(Flash 1st/Nano 2nd、vendorのみ)、1.86x end-to-end 128K・66x 持続 vs KV cache(分母相違) — 表:bench×分母×条件
- **§2.5 [LIMITED]** READMEのライセンス来歴に依存。設計原文: §2.5  Paper と README の分離(paper=CC BY-NC-SA・software=PolyForm Noncommercial・第三者 MIT・重み除外、paper に条項なし)と SGLang snapshot・save/restore — 図:ライセンス対応
- **§2.6 [LIMITED]** 65頁数式・ablationの原典精読は未完。設計原文: §2.6 限界:vendor bench のみ、独立実行・供用試験なし、65 頁の式・ablation 未精読、商用可否の断定なし — DEPTH_LIMITED 注記


### P3 働くエージェント:Duet の権限境界と 1Password・auto-mode の安全（4節 / 4.5頁見積）
- 総評: Duetの待機列、権限境界、6,000超カタログ、1Password coming soon、auto-mode翌週展開を区分。 隔離環境・分類器・資格情報注入の安全性はベンダー説明で、独立実機検証なし。
- **§3.1 [LIMITED]** 待機列・プラン制約は未再現。設計原文: §3.1 待機列・US Pro/Max 先行・共有制限・背景消費と、朝の要点・接続監視・表・予報・web 作成・離席継続・要所確認の振舞い — 表:権限×条件
- **§3.2 [LIMITED]** カタログ数と実live連携に区別。設計原文: §3.2 VM・browser、6000+ 目録と実liveの区別[発表/待機/順次公開/GAを別status]、Stripe Link/Shop Pay、1Password coming soon[公開時はliveと書かない]、証券・送金の禁止 — 図:資格の流れ(見ない設計、credential never visible)
- **§3.3 [LIMITED]** 脅威モデルは仮説として提示。設計原文: §3.3 安全対策の積層(trustworthy-agents、Managed-Agents の秘匿不保持、分類器承認、browser prompt 注入対策、red-team・外部 pen-test・bounty、CC・gov-ID 分類)と 1Password の承認注入(agent は暗証・OTP を見ない)
- **§3.4 [LIMITED]** 次週予定はFUTURE/分類器実測なし。設計原文: §3.4 auto-mode の Oct22 更新(8/7 OUT)と翌週FUTURE[完了と書かない]・分類器(classifier gating)の未検証 — 表:旧/新/未来の三段[発表/プレビュー/GAを別列]


### P4 映像の速度を疑う:FLUX 3 Max の数表批判（3節 / 3.0頁見積）
- 総評: fal の製品頁・blog・発行者PRの10.95秒/12.45秒および+47/+50 Eloを異なる観測として記す判断は妥当。 新規欠陥 R5-N01: §4.2 95.52%減少式に、速度比の分母/分子の説明を誤って括弧接続。読者に率の分母が12.45秒と誤認させる。
- **§4.1 [OK/LIMITED]** keyframes GAは供給者文書が不一致。設計原文: §4.1 fal+BFL の post-train(RL・推論最適)と text/image[発売時公式確認]・keyframes[Oct19 PRが可用と主張・blogが導線、Oct18 FAQ「Two at launch」と矛盾→UNRESOLVED_VENDOR_DOC_CONFLICT、W43 live未検証]・従量、Oct19 IN(Klein Oct15 OUT)
- **§4.2 [FIX]** 要修正: 率と倍率の分母説明を分割。設計原文: §4.2 速度の独立再計算(独立測定ではない):277.80/10.95≈25.37x[Oct19発行者PR、10.95s/277.80s、rawはRENDERED_ONLY]、277.80/12.45≈22.31x[blog/製品頁、12.45s/277.80s]、(277.80-12.45)/277.80×100≈95.52%[t_baseline/t_candidate、分母=新候補秒、分子=旧基準277.80秒] — PRはPRNewswire経由の発行者一次声明(第三者benchではない)、blog 26.5x/96.2%は同入力で不整合、見出し「22x」は下限表現で数学的誤りと断じない — 最速見出し禁止 — 表:分母×倍率×出典/版/時刻
- **§4.3 [OK/LIMITED]** AA原表/投票集計を独立未取得。設計原文: §4.3 質 Elo 1139(暫定・4868 票、AA原表未取得・VENDOR扱い):blog時点ではFLUX3比+47、製品頁/PR(Oct19 15:46 ET)では1139-1089=+50[比較対象/版/snapshot相違、背後のAA変動UNKNOWN] — 単一確定改善幅に統一禁止 — と価格($0.0425/$0.0725→$0.17/$0.29)


### P5 声の様式:Voxtral・Ming・Eleven の合成と認識（4節 / 4.5頁見積）
- 総評: 公式発表とMistral Docsの35+言語・モデルカード9言語・プリセット18/22・評価11言語の母集団を分離。 資料間差は未解消。モデル/タスク/言語と方言/評価標本を表で並べて未整合を明記する条件。
- **§5.1 [LIMITED]** ベンダー文書衝突を解消したふりはしない。設計原文: §5.1 Voxtral 家族[UNRESOLVED_VENDOR_DOC_CONFLICT、単一TTS言語数に統一禁止]:STT書起こし Small Transcribe 3 50言語・Realtime 35言語超/40+言語方言・TTS Speech 3は発表35+言語/50+方言 vs モデルカード9言語 vs 言語表35言語/50+方言・プリセット18言語(発表)/22表(Docs)・voice cloning別枠・評価標本11言語は対応数ではない — 書起こし・diarization・context-biasing(用語辞書による認識誘導、context biasing)(FLEURS WER・cpWER[連結最小置換WER、concatenated minimum permutation WER]・recall・500ms 未満) — 表:機能×モデル×対応言語×出典/版/時刻
- **§5.2 [LIMITED]** 11言語のjudge標本≠サポート全言語。設計原文: §5.2 TTS 内部評価(Voice Code Bench 300・pronunciation 300・multilingual 377[11言語標本、対応言語数ではない]・expressive 237・gemini-3.8-flash判定[ベンダー選択判定器])と価格・EU/US・自己配備・Pro Voice — 判定器の vendor 性を明示
- **§5.3 [LIMITED]** AA原表不在/roadmap未確定。設計原文: §5.3 Ming の開放(0.5B・7.9B-A1.3B MoE Ling V3、MIT、7 言語+方言、14 tag、9 task)と AA 引用(Controlled Voice・Robustness・Provider Voice、原表未取得)・roadmap 保留・月精度 — 表:AA×原表有無
- **§5.4 [LIMITED]** protocol互換≠無改修置換。設計原文: §5.4 Eleven の realtime 互換(v1 Mini/Max、90+・17k+ voice、Agents・Realtime API・OpenAI 互換・WebSocket)と AA(BBA・TTFA・Full-Duplex・Arena・tool-use、原表未取得)・Pareto・SDK 改修・指南未開封


### P6 安全の両相:見つけて直す協調開示と先端モデルの学習環境の隔離（3節 / 4.0頁見積）
- 総評: PHP修正はメンテナ主導で、CalifとWizの発見、協調開示・補修までの流れをベンダー記述として扱う。 新規修辞リスク R5-N03: §6.1『CVE ゼロ』は『このページにCVE番号の列挙を確認できない』へ限定。CVE不存在/対象脆弱性ゼロを暗示させない。
- **§6.1 [FIX]** CVE『ゼロ』語の読者誤認リスクあり。設計原文: §6.1 Patch(Oct21 RENDERED_TEXT、bot-wall 9946B のみ):Calif GPT-5.6 Sol、Wiz 独立双方、maintainer 主導、Wiz/Cloudflare、5 段階 validate+fix/advance-notice/政府 SIF-ONCD-CISA+国際/prepare/publish、$1B Daybreak、Codex PHP checker、CVE ゼロ(報告≠証明) — 工程図
- **§6.2 [OK/LIMITED]** DNS/隔離/RL再開はベンダー主張。設計原文: §6.2 Securing(offline・defense in depth[多層防御]、9/20 DNS、数百B red-team、Kata/gVisor/Moby/kernel CVE、10/1 RL 再開、safety gating、頁日付のみ+RSS 10:00Z secondary)と攻撃者有利の留保
- **§6.3 [OK/LIMITED]** 時系列の分離は妥当。設計原文: §6.3 Oct23 囲い・W42 申立てとの区別と、来歴の保存


### P7 科学の手続き:生体と低資源言語の評価（3節 / 4.5頁見積）
- 総評: 生物系はblind preferenceとwet-labの不存在、低資源言語系は共有SQLite仕様と非公開hidden移行テストを分離。 測定者は著者側。75%選好、20言語87.4%、移行86.6/97.9%、API費用は独立評価と表現しない。
- **§7.1 [LIMITED]** 盲検75%・wet-lab独立検証なし。設計原文: §7.1 Bio(GPT-Rosalind 数千 agent・全脳 CRISPR 数百万細胞 32 分、摂動報告→ atlas、Tsc1/Tsc2・DCTN1、700+ vs 11、盲検 75% 分散選好、bioRxiv/HF/GitHub 来歴、in-loop、wet-lab 未・ZERO 再現) — 表:手順×来歴×限界
- **§7.2 [LIMITED]** 20言語の公開suiteと秘匿テスト別。設計原文: §7.2 Low-resource(MultiLangBench SQLite 自作 20 言語・DB 共有・参照 SQLite 照合 Astra 87.4 vs Sol 26.8・COBOL 10.9→72.1 等 19/20≧83%、COBOL hidden byte-parity・Sol 86.6% low・97.9% high、suite 公開≠再現、専門家審査、COBOL 40%・Luna $0.77 vs $3.48、we/our 手続き)と費用・hidden の vendor 保持 — 表:bench×分母×条件
- **§7.3 [LIMITED]** サンプル/採点/請求独立性不足。設計原文: §7.3 盲検(blinded evaluation)・標本・請求の限界と、来歴の保存


### P8 作る道具:Decisions API と AI toolkit・配布（3節 / 3.5頁見積）
- 総評: Decisionsの400件は1リクエスト当たり、キャッシュ書込み/地域/長文脈の請求を残す。TanStack stable coreとexperimental harnessを分ける。 新規欠陥 R5-N02: §8.2のregistryとGH release時刻ラベルがSelection根拠と逆転している。blogの日付をrelease時計に代替しない。
- **§8.1 [OK/LIMITED]** 料金/型/400件は公式ガイド一致。設計原文: §8.1 Decisions GA Oct22 v1/Luna(beta Oct6 区別、3 型 predicate/choice/score、text/image/JSON、400問 per request[総呼出上限ではない]・2x beta、cache[読取$0.01/書込別課金]、GPT-Live avatar triggers、$0.10/M uncached入力・cache $0.01読取・出力トークン課金なし[≠総無料、地域上乗せ・長文脈乗数あり]、US/EU・ZDR、10x vendor[独立未測定]、証言 Box/Datadog/Ramp/Sierra/SpeakBox の選択bias、製品頁未 archive) — 表:料金×条件×版
- **§8.2 [FIX]** 要修正: npm/GH timestamp label逆転。設計原文: §8.2 TanStack(76 pkgs・23 adapters・8 UI・143 人、harness 0.x 実験[安定核 vs 実験harness対照表]、codemod threadId、非 sandbox、製品Oct22 IN[registry 15:18:14Z/release 15:21:49Z]・blog Oct23日付のみ UNRESOLVED分離[製品時刻に読まない])
- **§8.3 [OK/LIMITED]** 配布/SLA/料金移行テスト未実施。設計原文: §8.3 DeepSeek 1017(V4.1-Flash Sep10、強 bench・高速・短出力、web/app/API、RL 自己feedback demo、MIT HF/ModelScope・GreenBitAI/Baekpica、Harness v0.2.1-rc.1、CodeBuddy/WorkBuddy、Search/Fetch $0.75/1k・Oct31 16:00 UTC 迄無料[移行・約款表]、DeepSWE 77 vs 74.2・HLE) — 表:API×移行×約款[発表/配布/無料期限を別status]


## 6. 新たな欠陥（既知の再掲とは分ける）


### R5-N01 — P2 / 比率と減少率の算式注釈を誤接続
- 対象: `sources/2026-W43/architecture-v2.json#/packages/3/must_cover_requirements/1`（P4 §4.2、0-based pointer）。
- 観測: 率の式 `(277.80−12.45)/277.80×100≈95.52%` の直後に『`t_baseline/t_candidate、分母=新候補秒、分子=旧基準277.80秒`』が付く。後者は倍数 `277.80/12.45≈22.31` に対する説明であり、**95.52%減の分母は旧基準277.80秒**。
- 独立算術: `277.80/12.45=22.3133`、`277.80/10.95=25.3699`、`(277.80−12.45)/277.80×100=95.5184%`。数値そのものは妥当、注釈が同じ節で矛盾。
- 修正条件: 「倍率＝基準秒/新候補秒、25.37x/22.31x」「削減率＝(基準秒−新候補秒)/基準秒、95.52%」を別式・別分母として明記。ベンダー算術再計算≠独立latency測定。
- 一次資料: https://fal.ai/flux-3-max ; https://fal.ai/blog/introducing-flux-3-max-by-fal ; https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html


### R5-N02 — P2 / TanStack 1.0 のReleaseとRegistry時刻の主語が逆転
- 対象: `sources/2026-W43/architecture-v2.json#/packages/7/must_cover_requirements/1`（P8 §8.2）。
- 観測: Architectureは『registry 15:18:14Z/release 15:21:49Z』と記す。一方、同じ固定HEADの `candidate-selection-v2.json` TanStack candidate `20a36d83656e2a4b` のrationaleは『npm 1.0.0 15:21:49Z + GH release 15:18:14Z』と逆に記録。r4 risk ledgerの記述もGithub release 15:18:14Z、npm 15:21:49Zを支持。
- 判定: **固定HEAD内部の不一致は確認済み**。GitHub Release原API timestampとnpm registry publish時刻の外部独立raw照会は今回未取得なので、どちらが絶対正しいかの第三者確証はNOT_VERIFIED。
- 修正条件: publisher APIを照会しUTC秒のlabelごとsource URL/JSON keyを示してから、Architecture側かSelection側のラベル誤りをedition-localに是正。Oct23のblog日付はOct22製品時刻の根拠に転用しない。
- 一次参照先: https://github.com/TanStack/ai/releases ; https://www.npmjs.com/package/@tanstack/ai ; https://tanstack.com/blog/tanstack-ai-1-0


### R5-N03 — P2 editorial-risk / 『CVEゼロ』という短縮表現が誤認誘発
- 対象: `sources/2026-W43/architecture-v2.json#/packages/5/must_cover_requirements/0`（P6 §6.1）。
- 観測: 『CVE ゼロ(報告≠証明)』の記法は、ページ内にCVE IDを見付けられないという調査結果を、脆弱性のCVE採番数が0であるとの断定に読み替えさせる余地がある。
- 修正条件: 『当該公開ページの確認範囲ではCVE番号を直接特定できず、CVE付与の有無は未検証』へ限定し、特定の修正版とCVE/アドバイザリの対応を断定しない。
- 根拠: https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/ ; 発行者の主張とCVE registryの独立照合は今回していない。


## 7. 既知重要論点の追跡（再検証/限定承継）


|ID|監査所見|処遇|
|---|---|---|
|K-01 DeepInfer| `MTP_VARLEN=1` のDSparkと `MTP_VARLEN=0,BATCH_INVARIANT=1,seq_seed` のdeterministicは別構成。公式READMEで確認。 | 区別維持、再現性はNVIDIA限定 |
|K-02 Voxtral| 公告35+とModel card9、Docs35/50+、preset18対22、11評価標本は同じ母数ではない。 | UNRESOLVED_VENDOR_DOC_CONFLICT、単一数字断定禁止 |
|K-03 Kimi/Flint/Nemotron| total/active/effective規約非等価、Nov4重み配布はFUTURE。 | 比較表の数値に計数規約・時刻・契約列必須 |
|K-04 FLUX| 10.95/12.45, 26.5x/96.2%, Elo +47/+50, keyframes availabilityの発行者不一致を独立照合。 | source×版×条件を別行、AA原表欠落注記 |
|K-05 Decisions| 1-400質問/request、出力token課金なしでもcache write、regional、long-context課金は残る。公式ガイドと整合。 | 固定単価/無料と誤訳しない |
|K-06 68件Attention| exception collectionでありselected19件の主張保証ではない。 | selected-19 risk registerを別添維持 |
|K-07 W43 cutoff| `[2026-10-16T22:00:00Z,2026-10-23T22:00:00Z)`。Metrics 23:42:03ZはOUT、midnight placeholder9件は正確な時計ではない。 | OUT情報をW43主記事へ移入禁止 |
|K-08 MemT| 65pp数式未精読、README/Licensesとpaperを分離、vendor 1.86x/66xを実験再現と言わない。 | 文献深度LIMITED |
|K-09 P8頁数| 3.5頁はESTIMATE。計画35頁+前付/後付2頁=37頁、目標38/上限44。 | 短い原典に合わせ記事を縮約可、水増し禁止 |


## 8. 原典の照合記録 — 表示閲覧とraw archivalを区別


|Package|今回直接照合した公開原典|確認した具体的根拠|残余|
|---|---|---|---|
|P1|選定Matrix・Architectureに記録されたKimi/Flint/NVIDIA来歴とr4監査文書|active/effective非等価を編集案として照合|元のHF model bytesとX原文の全raw再取得なし|
|P2|https://github.com/deepseek-ai/DeepInfer ; https://github.com/memtensor/memt-1.0 ; https://arxiv.org/abs/2610.26825|DSpark/deterministic環境変数、MemT 34B tokenと128K 1.86x/66xの著者値|固定Git revision全ソース/65ppの数学的検証なし|
|P3|リポジトリ収集済みDuet/1Password/auto-mode根拠のr4 risk ledger|待機列・coming soon・次週の区分|公式個別コネクタ一覧のlive試験なし|
|P4|https://fal.ai/flux-3-max ; https://fal.ai/blog/introducing-flux-3-max-by-fal ; fal発行PR|12.45秒と277.80秒から22.31x/95.52%、10.95秒から25.37x、Elo+50と+47を照合|AA原表とkeyframes live/schema未取得|
|P5|https://mistral.ai/news/voxtral-3/ ; https://docs.mistral.ai/studio/audio/specs-and-limits/languages|TTS 35+/50+、preset18とdocs22、real-time 40+/docs45以上の表現差、評価11言語|別の公式model card9言語を此次のrawで再取得なし|
|P6|https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/|Calif GPT-5.6 Sol、Wizの両件発見、PHPメンテナー主導修正を確認|CVE/patch ID照合、Securingの外部corroborationなし|
|P7|https://openai.com/index/low-resource-programming-languages/|20言語87.4%/26.8%、COBOL 10.9→72.1%、hidden移行86.6/97.9%の別測定|Bio元論文、低資源モデル実走、hidden testsにアクセスなし|
|P8|https://developers.openai.com/api/docs/guides/decisions ; https://tanstack.com/blog/tanstack-ai-1-0|400問/request、cache書込・地域/長文脈、TanStack 76 stable＋harness experimentalを確認|npm/GH release元メタデータ独立照合、DeepSeek重量hashなし|


原典をウェブで閲覧しただけの箇所はW43当時の原本バイトを再検証できたとは書かない。Architectureの「31節」は構造全件を確認したが、本文が未作成のため「本文の記述31節」監査ではない。


## 9. 日本語・翻訳・計数・誌面計画の判定


- 用語: コード生成、重み公開、実効パラメータ、1トークン当たりactive、推測的デコード、文脈バイアス付け（context biasing）、話者分離評価cpWER、盲検評価、過渡/持続メモリを初出で日英併記。英語のAPI/flag名は翻訳しない。
- 『最速』『最高』『独立検証』『安全を保証』『全言語対応』『来週提供済み』といった絶対表現を抑止。統計量と対象母集団・confidence interval・vendor測定であることを必須脚注に。
- P5: 35言語の対応と11言語の評価標本は異なる。P7: SQLite実装課題とCOBOL既存プログラム変換は異なる。P2: 倍率と保存量のベースラインは異なる。
- ページ密度: 全35.0予定頁、前後2.0=37.0、38頁target/44maxは工程見積。P2 6.0頁の深い機構を要求する一方、65頁の数学精査が不足しており「概観＋厳密な資料限定」へ調整余地。P4 3.0頁は数表矛盾解説と方法論に有意義。P8 3.5頁はAPI例+安定/実験対照表+配布注記を優先し、資料不足時は短縮。


## 10. Muse/編纂Solへの推奨修正指示（実行は本監査者の権限外）


1. **R5-N01**: Architecture P4 §4.2の「22.31x/25.37x」と「95.52%減」の定義・分母を別々に記述して再検算。数値の帰属は発行者測定のまま。
2. **R5-N02**: P8 §8.2のnpm時刻とGitHub Release時刻をpublisher metadataの元JSON timestampによって確定し、Selection rationaleとの逆転を是正。既存Selectionを勝手に再生成せず、Core v2に反する修正をしない。
3. **R5-N03**: 『CVEゼロ』→『確認範囲にCVE番号記載なし、CVE照合未実施』へ置換。
4. r5知見を損なわないよう、FLUX keyframes、Voxtral TTS言語/プリセット、AA原表、ベンチ独立再現、重みライセンスの未検証を明示する。
5. 事後reviewは**固定対象の次版を別SHA/Tree**で宣言して行い、今回は `6f961295c6743248c2bccb34e15cb84116bf4de7` の結論を上書きしない。Selectionの未検証Evidence主張が確定的に誤っていると判明したら `SELECTION_REVIEW_REQUIRED` として上流へ戻す。
6. 上記修正と独立再照合が済んだら初めて、Human Ownerに技術的境界/ページ見積とLIMITEDを添えてArchitecture Reviewを提示する。**Human承認・Draft・TeX・PDF・Releaseはいずれも実行しない。**


## 11. 監査の制限・最終停止点


本監査は差分監査でなく、8パッケージ31 must-coverと19選定を対象とする固定snapshotでの独立編集・技術監査。ただしsource raw全32件、各raw DOI/HTML、ベンチ再現、Core Native validator等の未実施を明記した限定的な包括審査であり、完全再現を偽装しない。**Human Architecture Reviewはpendingのまま**、新たなStage遷移なし。GitHubには一切書き込んでいない。