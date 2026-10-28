<!-- GitHub TEXT-NORMALIZED TRANSCRIPTION of independent Sol original. NOT byte-identical to original. Original received attachment: 20261025180802_SolReview.md; 19491 bytes, UTF-8 BOM + CRLF, SHA-256 2a4b54078e6da63d5b03d25f7c2e67d5ae2f5880c82b40d6f17d219b061c21f2. GitHub copy has UTF-8 LF normalization and this prefatory provenance comment. Fixed audit subject ee206400c9740dd2288b894f31f79a119b7758bc. -->

# J-GAS 2026-W43 Architecture r4 修正後包括独立監査 — Sol Review


- 監査種別: 独立Sol / GitHub READ_ONLY / Human Gate不操作 / Stage不操作
- 監査日: 2026-10-25 JST
- 対象repository: eariver/japanese-generative-ai-survey
- 固定対象HEAD: `ee206400c9740dd2288b894f31f79a119b7758bc` （GitHub commit API相当のconnector読取で確認）
- 契約記載Root Tree: `49f55eef6e8fc5beacc1645b62ba0d25e42ccb1d` （**独立Tree取得不可、NOT_VERIFIED**）
- 対象branch観測HEAD: `92396ac93f1b60fe5eace7c02f64b2bf9a1798cd`。契約ファイル追記後の先端であり、監査自体は固定`ee2064…`を使用。
- 参照main HEAD: `041a08dfef3112643cbf85b4a86a7b6f9128aed6`
- 参照Frozen Core v2 HEAD: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- 比較基点: `db78839bd7cb858a6cc5b1620bf6c574f064339f` → `ee2064…`、ahead=1、変更20ファイル
- 監査契約: [r4 post-fix comprehensive audit request](https://github.com/eariver/japanese-generative-ai-survey/blob/92396ac93f1b60fe5eace7c02f64b2bf9a1798cd/sources/2026-W43/execution/audits/independent-sol-w43-architecture-r4-postfix-comprehensive-review-request-20261025.md)


## 1. 総合結論と権限境界


| 判断対象 | 独立判定 | 理由 |
|---|---|---|
| Selection | **PASS_WITH_LIMITATIONS** | 32件のIDと19/1/12、r3とr4のバイト一致、19件の非重複配置、各リスク登録を検証。ただし全一次資料の生バイト照合・全選定根拠の原典再現は未完。 |
| Architecture | **REQUEST_CHANGES** | ISA-001/002の修正は適切に限定されたが、r4実行時刻の自己矛盾、新規FLUX一次資料差分・提供範囲の未解決、Tree/validator未再現が残る。 |
| Selection Trusted Bridge提案 | **NO / HOLD** | 人間による編集判定はOperatorの正規receiptではない。対象Treeおよびnative precheck独立実行が未検証。 |
| Architecture Trusted Bridge提案 | **NO / HOLD** | Architectureに新規P2と未解決原典差分。現stateはEVIDENCE_REVIEWEDでSelection/Architecture checkpointともpending。 |
| Human Architecture Gate | **未実行・未承認** | 監査者が承認を代行しない。 |


**P0は確認範囲では検出しなかった。新規P2を3件特定した。** 対象固定コミットのRoot Treeが契約値と一致することは今回のコネクタでは取得できておらず、契約記載値を独立検証済みと表現しない。本判定はStage遷移権限を付与しない。


## 2. 方法・閲覧した範囲・未実施


1. GitHubコネクタから固定HEAD、移動後W43 HEAD、main HEAD、Frozen Core HEADをread-only取得。Git compareの変更20ファイルを独立取得し、変更が`sources/2026-W43`内のArchitecture提案/補助文書/interactive input・auditに限定されることを確認。変更リスト上、`production-state.json`、Discovery/Screening/Evidence/Views/Materiality/Completeness、shared Core、Gate/Checkpointへの変更なし。**Git Root Tree自体の値は提供APIに出ないため未検証。**
2. 固定HEADの`candidate-matrix-v2.json`全32行、`candidate-selection-v2.json`全32割当、`architecture-v2.json`全8 packageと31 must-cover条項、`architecture-review-summary-v2.json`、`architecture-review-attention-v2.json`全68 items、interactive input/audit、production-stateをJSON解析。Materiality 51、Completeness LIMITED、accepted Evidence index 32 PARTIAL、accepted Edition Views index 32件も閲覧。r3 history内の7 JSONと`SHA256SUMS`を取得・SHA-256再計算。
3. 各packageの`purpose`、`must_cover_requirements`、`boundaries`、配置先とページ見積を全文閲覧。選定19件のtitle/disposition/source件数/limitation件数/配置先を突合し、selected-19独立risk ledgerのID記載を検査。Attentionをmateriality/screening/selectionの母集合と突合。全31技術条項は**記載内容を読んだ**が、将来の本文31節はまだ存在せず、本文実証を意味しない。
4. 前回r3独立監査、Sol裁定、r4修正指示、r4一次資料crosswalk、selected-risk ledgerを読了。Muse自己PASSは独立検証結果と混同せず、独立に再実行できたのはJSON解析・SHA-256計算・算術・一部公開原典照合のみ。
5. 外部一次資料を再参照: DeepInferの固定`9bd9cf24` README/environ.py（GitHub connector）、Mistral告知・モデルカード・言語表、NVIDIA Nemotronカード、Recursive Flintカード、fal製品頁/blog/公式配信PR、OpenAI Decisionsガイド・発表・料金資料、MemT README、1Password発表、Eleven Realtime発表、OpenAI Bio/低資源評価、TanStack 1.0発表。これは**選定19件の全original rawを取得したことを意味しない**。GitHubで取得した固定ソースとWebの可変レンダリングを区別。
6. **NOT_EXECUTED**: 固定コミットの全root Git Treeの再算出、6方向のTree照合、Frozen Core-native runner / validators・Stage precheck実行、全19候補のaccepted Evidence task JSON / 25件supplement raw / Edition View bodyとの行単位全件照合、MemT論文65頁の数式/ablation精読、Artificial Analysis原表取得、ベンチ実測、API/SDK/ライセンス適用の実機試験、Human Gate・Operator receipt・Draft/TeX/PDF検証。


## 3. 構造・不変条件と再計算


- Candidate Matrix `32`（一意ID32）。Selection `32`：`SELECTED=19`、`HOLD=1`、`REJECT=12`。Matrix/Selectionのr3 snapshotとr4現物は**Git blob SHAと独立計算SHA-256の双方が完全一致**。
- Package `P1…P8`の8件、must-cover個数 `5+6+4+3+4+3+3+3=31`。primary/supportingを横断したplacementは**19件・一意19・SELECTEDの漏れ0・重複0・非selected混入0**。P4は1件、P8は3件という元構成を維持。
- Review Attention `total=shown=68`、`overflow=0`、`truncated=false`、limit 100、item_id一意68。groupは`EXCLUDED19、NON_MATERIAL2、DROP19、INSPECT4、MAYBE11、HOLD1、REJECT12`（和68）。Attentionのsubjectに孤児0。原生68は**例外中心でありSelected全19の妥当性検査ではない**。別のHuman向けledgerにselected全19 IDの記載を確認。
- Completeness `LIMITED`：3 obligation中LIMITATION 2 / SATISFIED 1。residual 5件（Metrics OUT、日付時刻の曖昧さ、NULL時計9件、ベンチ非再現/AA欠落/版差、render-only/weight/connector）をreview summaryが維持。
- 状態は`EVIDENCE_REVIEWED`、next_action `stage:selection`、Selection/Architecture checkpoint `pending`、Human Architecture/Publication Preview Gateとも`pending`。Architecture JSON `PROPOSED`、Summary `READY_FOR_ARCHITECTURE_REVIEW`は機械的準備状態であり人間の承認ではない。
- r3保存のSHA-256 7件は`SHA256SUMS`と全一致。r4独立計算値：Matrix `16a6bbfe569b3215d05fbae7175b3ca04efc6c1846d28c48662245b68f854c3b`、Selection `50decd8697e1737d7adf6fe9f1ac0f4c7cc891353a7be09461b86e8b90beccea`、Architecture `9ab37dd600d76056306f5a8419f6dbb42bf59866e559bede4f85fe49a958055a`、Review Summary `c8bb6e2ec9df59bebf1aafab5995e549970ee7660c8e2bd69f95a26f52d87172`、Attention `7c3e4deb4a2cd077acac148c777aa2300f1f4dad45bbc4d0624a6b693528f12b`。
- r4 input SHA-256 `67d0f39f2c3da4c08a23c3acfd0e58963fedb22577b24c5496c6b6ba847323b3`、compat inputは同一Git blob/SHA-256。runner auditのinput/全5 output hashは独立計算実体と一致。**これはファイル完全性の整合であり、実際にCore runnerを実行した証明ではない。**
- ページ見積 `5.0+6.0+4.5+3.0+4.5+4.0+4.5+3.5=35.0`、front matter等`2.0`を加えて`37.0`。目標38/上限44との内部計算に不整合なし。ただしPDF出来高の実績ではない。


## 4. W43-ISA-001～009 再監査結果


| 旧ID | 判定 | 独立確認と残存境界 |
|---|---|---|
| ISA-001 DeepInfer | **PASS** | P2 `2.2が可変長DSparkの`DEEPINFER_ENABLE_MTP_VARLEN=1`・NEXTN既定5と、deterministic samplingの`MTP_VARLEN=0` + `BATCH_INVARIANT=1` + fixed `seq_seed` (NVIDIA)を排他的構成として明記。固定9bd9cf24 README `L25/L29`とenviron.py `L130–132/L198`を再読。実行再現はなし。 |
| ISA-002 Voxtral | **LIMITED** | P5 `5.1/目的/境界は35+ / model card 9 / docs 35、preset 18/22行、11評価標本を区別し`UNRESOLVED_VENDOR_DOC_CONFLICT`を明記。発行者文書間の矛盾そのものは解消せず、Draftでも単一言語数を断定不可。 |
| ISA-003 Nemotron/Flint | **PASS** | P1 `1.2/`1.5にNemotron 8B total/4B effective、Flint 39.8B total/~2.5B active per token（output head込/input embedding除外、body約2.2B）、非等価計数、OpenMDW-1.1とGemma-4 Apache-2.0の分離。OSI認定・weight hash未検証。 |
| ISA-004 FLUX | **LIMITED** | 分母を旧277.80sとする独立再計算値は正しいが、fal側の速度・Elo原データ差分とPR raw未保存が継続。独立性能実測ではない。新規発見R4-011/012参照。 |
| ISA-005 Decisions | **PASS** | P8 `8.1は400 questions per request、$0.10/M uncached input、$0.01/M cached reads、cache-write別課金、regional/long-context加算、output無料≠総請求0を明記。メーカー公式guideと合致。 |
| ISA-006 68 Attention | **PASS** | native 68 JSONバイト維持、separate selected-19 risk registerあり、19 selected ID全件を照合。risk registerはnative Core outputではない。 |
| ISA-007 P8 3.5頁 | **LIMITED** | 3.5頁がESTIMATEであり、Decisions例・stable/experimental対照・DeepSeek差分の優先順を記録。原稿がないため真の密度・水増し有無は未評価。 |
| ISA-008 日本語 | **PASS** | 8 packageの見出し・目的・31条項・境界を点検。`コード生成モデル`、`Gated DeltaNet-2`/`Mixture-of-Storage`、`context biasing`、`cpWER`等に説明/原語あり。将来の本文への伝播は別検査。 |
| ISA-009 時刻・可用性 | **PASS** | W43期間`[2026-10-16T22:00Z, 2026-10-23T22:00Z)`、Kimi X 17:15:24Z IN・weights Nov4 FUTURE、1Password coming soon、TanStack product Oct22とblog Oct23時刻未詳の分離、Metrics 23:42:03Z OUT、Grok NEVER_STORYを確認。 |


## 5. 新規に検出した欠陥と残る未解決事項


### R4-010 / P2 / 実行メタデータの未来時刻 — 新規FAIL


- **場所**: `/sources/2026-W43/orchestration/v2/interactive/selection-architecture-input.json#/runner/generated_at`、同`selection-architecture-audit.json#/runner/generated_at`、`execution/compat/selection-architecture-input-r4.json#/runner/generated_at`。
- **実体値**: `2026-10-25T12:00:00Z`。一方GitHubの対象コミット`ee2064…`の`created_at`は`2026-10-25T08:40:48Z`。記録上、成果物がコミットの**3時間19分12秒後に生成された**形であり、当該コミット時点での作成時刻として成立しない。ハッシュ一致は時刻の真正性を救済しない。
- **リスク**: runnerの発生時点に関する来歴が自己矛盾。`generated_at`が予約・計画時刻を意味する特殊仕様なら、その契約根拠が不明。
- **要求修正**: 時計の実測・ログ・生成イベントとの照合、時刻フィールドの意味定義、根拠付き訂正。修正後はinput/compat/runner-audit/derived hashを再連結し、r3 archiveとMatrix/Selection不変を再検証。
- **回帰検査**: `generated_at <= first-containing-commit.created_at`を保守的な時系列妥当性検査として用いる（特別な生成・コミット時計契約が立証された場合を除く）。時刻の後付け推測は禁止。
- **未確認**: runner実行ログ、Gitコミッタのローカル時計、Core側generated_at契約。
- **根拠**: [監査対象commit](https://github.com/eariver/japanese-generative-ai-survey/commit/ee206400c9740dd2288b894f31f79a119b7758bc) と固定対象のinteractive JSON。


### R4-011 / P2 / FLUX 3 MaxのElo改善幅を単一確定値として記載 — 新規LIMITED


- **場所**: `architecture-v2.json#/packages/3/must_cover_requirements/2`（P4 `4.3）。
- **記述**: `FLUX3 比+47`。
- **一次資料間の相違**: falの[2026年10月ブログ](https://fal.ai/blog/introducing-flux-3-max-by-fal)は+47 Eloとする。一方、[fal公式製品頁](https://fal.ai/flux-3-max)と[fal名義PR（2026-10-19 15:46 ET）](https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html)は`1,139 − 1,089 = +50 Elo`と明記する。差は**同一発行者の文書版・arena snapshotの不一致**であり、r4では+47のみを提示して別資料との関係を示していない。
- **修正要求**: 比較対象/arena/投票時点・文書観測時刻を別列とし、本文は「falブログの時点では+47、別のfal資料では+50」と帰属するか、比較幅自体を省く。独立AA original未取得を明示。
- **回帰検査**: `1139-1089=50`、数字を+47にするなら別の基準Eloまたは別snapshotを記録。ベンダー測定を独立Elo測定と表現しない。
- **未確認**: AAの原表/snapshot履歴、ブログの後日更新履歴。


### R4-012 / P2 / FLUX keyframes-to-videoの発表時点提供状況が不明 — 新規LIMITED


- **場所**: `architecture-v2.json#/packages/3/must_cover_requirements/0`（P4 `4.1）：「`text/image/keyframes`」を一括して列挙。
- **一次資料差分**: [falブログ](https://fal.ai/blog/introducing-flux-3-max-by-fal)には`keyframes-to-video`への導線がある。一方、[fal製品頁](https://fal.ai/flux-3-max)のFAQは発売時`Two at launch: text to video and image to video`と記載。FAQ自体の更新時点にも限界がある。**第三エンドポイントをW43 cutoffで一般提供済みとするだけの整合した根拠が不足**。
- **修正要求**: 各endpointを「告知・リンク存在・API schema存在・実call可能・一般提供」別statusで扱い、W43時点の実availability不明なら明記。P4 `4.1は「keyframes機能について提供状態未照合」とする。
- **回帰検査**: launch時3 endpointを断定する記述に、同日時のAPI docs/schema/提供可否証拠を要求。
- **未確認**: W43当時のendpoint response・pricing API・アクセス地域、正式snapshot。


### 既知かつ今回追加参照したFLUX速度の不整合（ISA-004に包含）


- `277.80/10.95=25.3699…`、`277.80/12.45=22.3133…`、`(277.80−12.45)/277.80=95.5184%`を再計算。fal blogの`26.5x/96.2%`は公表秒数と合わない。
- 新たに実際の[fal名義PR](https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html)をレンダリングで閲覧。**10.95秒と277.80秒の一次発表が存在**する。ただしこの監査者はW43 edition-localの immutable rawとして新規保存しておらず、「preserved raw確認済み」とはしない。PRの見出し「22倍」は25.37倍に対する緩い下限表現とも読め、機械的に「誤り」と断じない。
- fal製品頁の速度比較は10秒、720p/768p、16:9平均と記載するが、元実験のGPU/batch/cold-warm/統計的同等条件の独立保証はない。**独立再計算 ≠ 独立測定**。


## 6. 一次資料対応の対象全19件 — 実査到達度


`A=固定版の原典ファイルをconnector取得`、`B=発行元のWebレンダリングを再読`、`C=accepted index/Matrix/Architecture/ledgerの連関は読んだが、当該原典の独立取得なし`。A/Bでも実測や完全raw archiveを保証しない。


| パッケージ | 選定候補（19件を重複なく列挙） | 今回の到達度・重要境界 |
|---|---|---|
| P1 | Kimi K3.1 Pro / Recursive Flint / NVIDIA Nemotron Bolt | Kimi C（Xの元投稿raw未再取得、Nov4 FUTURE）、Flint B（39.8B/2.5B head規約）、Nemotron B（8B/4B・二層ライセンス）。 |
| P2 | DeepInfer / MemT-1.0 | DeepInfer **A**（固定9bd9cf24 README + environ.py）、MemT B（READMEのGDN-2/MoS/66x）。MemT長論文65頁の式は未精読。 |
| P3 | Claude Duet / 1Password for Agents / Anthropic auto-mode | Duet C、1Password B（coming soon/rolling逐次）、auto-mode C。live connectorとclassification実挙動は未検証。 |
| P4 | fal FLUX 3 Max | B（公式製品頁/blog/発行者PR）。独立速度/Elo測定なし。 |
| P5 | Mistral Voxtral 3 / Ming-3.0-tts / Eleven Realtime v1 | Voxtral B（告知+model card+language matrix）、Ming C（MIT/AAの原典再確認なし）、Eleven B（90+/17k+・Speech-to-Speech発表）。 |
| P6 | Patch the Planet / Securing frontier training | Patch C（render-onlyの既往記録、原HTML未取得）、Securing B（公開日を発行元research一覧で確認、手続き本文実験なし）。 |
| P7 | OpenAI distributed Bio / low-resource coding | Bio B（共同研究チーム評価）、low-resource B（20言語、MultiLangBench 87.4/26.8、COBOL 86.6/97.9）。blind/hidden独立再現なし。 |
| P8 | OpenAI Decisions / TanStack AI 1.0 / DeepSeek V4.1-Flash-1017 | Decisions B（価格/400 per request）、TanStack B（stable vs experimental、ブログOct23 day-only）、DeepSeek 1017 C（weight/価格/移行original未再取得）。 |


この表により、**全19件の構造・配置・リスク転記は検査したが、全19件の一次資料rawを全件読んだとは主張しない**。特にCの6件および他のモデルのバイナリ/長論文は、Stage前後のDraft検証で再取得対象。


## 7. 最小限の次工程（監査者は指示・書込みしない）


1. 編集Solが本レビューを裁定する。新規`R4-010`は先に provenance 修正と hash再束縛を必要とする。`R4-011/012`はfal一次資料差分を版/時刻別に注記し、現在のr4 Architectureに残る単一確定記載を修正するか、未検証として狭める。
2. Root Treeの六方向照合（fixed W43 / 現remote W43 / main / Frozen Coreの関係）と、**Frozen Coreを一切変更せず** isolated checkoutでnative Selection→Architectureの適法な検証を実施・receiptを確認する。現在stateのまま二段階目を「実行済みPASS」に偽装しない。
3. 次の独立レビューで、今回Cとした元資料、25 supplement sourceの必要な原本、MemT長論文・AA原表の可用範囲を限定しつつ取得する。Evidence真正性に重大矛盾が見つかった場合は再選定せず`SELECTION_REVIEW_REQUIRED`として編集Sol判断に戻す。
4. 改訂Architectureが改めて独立PASSとなった場合に限り、権限者がSelection BridgeとArchitecture Bridgeを**別々に**提案し、Human GateはOwnerの明示的判断を待つ。


## 8. 保存・完全性メモ


この監査は固定コミットに対するread-onlyの編集評価であり、GitHub・Human Gate・Production State・Frozen Coreに書込みを行っていない。Google Driveへの本独立Markdownの保存のみが明示許可された変更。レポート自体のraw SHA-256はGoogle Drive上の最終raw bytesを取得・計算できた場合に別途報告し、未算出の場合はハッシュ値を推測記入しない。
