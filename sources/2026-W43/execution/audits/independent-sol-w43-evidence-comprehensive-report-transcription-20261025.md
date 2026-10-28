# Source provenance (editorial ingest)

This file is a text-normalized **copy**, not a byte-identical original, of the user-supplied independent review `20261025125414_SolReview.md` (2026-10-25 JST), source raw file **44,914 bytes; SHA256 `8e3218ec5eef385764935d4790e0b333ac93e211285ab889ea6ff6910bbcda63`**. The original is held in the user's connected Drive. This copy preserves the review narrative and is supplied to Muse as **audit findings, not execution instructions or machine authorization**. Never edit the historical result copy; corrections to findings require an explicit new Sol adjudication record. GitHub branch at intake `46d8efc8aeb04903660f9e4754687d49b2543a55` tree `826469a884576efe22281e1109db38031b54fbb2`. The audit author did not authorize any repository writes.

---

# 日本語版週刊AIサーベイ — 2026-W43 独立Sol総合監査


**判定：REQUEST_CHANGES / EVIDENCE_REVIEWED 移行不可。**
監査基準：2026-10-25 JST、`eariver/japanese-generative-ai-survey`、完全固定コミット `46d8efc8aeb04903660f9e4754687d49b2543a55`。独立監査者として編纂統括Sol/Museの結論は保証と扱わず、まず実物のCard/View/ledgerを閲覧してから過去レビューを照合した。GitHub/Repository は read-only（書込み0）、修正指示保留のまま、`ADVANCE_STAGE`未実行。Google Driveへの本監査報告の保存のみ許可済み。


## 1. 起点6件の厳密照合


| 対象 | Expected | Actual | 判定 |
|---|---|---|---|
| W43 remote HEAD | `46d8efc8aeb04903660f9e4754687d49b2543a55` | 同左 | MATCH |
| W43 root Tree | `826469a884576efe22281e1109db38031b54fbb2` | 同左 | MATCH |
| main HEAD | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | 同左 | MATCH |
| main root Tree | `a134dc36a407d08ab1de416324229b3955e0325a` | 同左 | MATCH |
| frozen Core ref HEAD | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | 同左 | MATCH |
| frozen Core root Tree | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` | 同左 | MATCH |


Root Treeは Git commit object の `tree.sha`、枝は `git/ref` を読んだ。監査契約：`sources/2026-W43/execution/audits/independent-sol-w43-evidence-comprehensive-audit-request-20261025.md`。


## 2. 対象範囲と検査深度


- 対象の **Evidence Card 32/32件、Edition View 32/32件** をそれぞれ実ファイルから個別に読んだ。各Cardのsource_id/URL/class、claim-1等、verificationとlimitation、各Viewのmateriality/rationale/windowを突き合わせた。**全64実体の抜き取り検査ではない**。
- accepted Discovery 51件、Screening 51件、Evidence manifest、View manifest、Materiality ledger 51行、Completeness 3義務、Production Profile/State、2 Checkpoint、X Intake manifest、r2 supplement 6行、compat projection ledger 32行、compat builder、過去のSolレビュー・Muse handoff・保留r3指示を検査した。
- 公式一次資料に対して独立にウェブ本文を照合した重要系列は Patch、Google Cloud、Recursive Flint、DeepInfer（READMEとコード）、GitHub metrics、Anthropic auto-mode、MemT repository README、Ming、OpenAI生命科学、FLUX 3 Max等。**これは一次主張を参照先と照合した行為であり、モデル/ベンチマークの独立再現ではない**。
- **未完了の深部検査**：AM-Bench v2 38頁・Oracle v2 29頁のv1→v2全文diff、MemT 65頁の式・ablation全文査読、モデル重み/LICENSE原ファイルのbyte-hash全件、MOSS trainer実行、AA原ベンチサイト、網羅的なvendor harness再実行、raw HTML/PDF 6個の独立SHA再計算、frozen Core全スクリプトの動的試験。結果は **NOT_EXECUTED / UNVERIFIED** とし、workerのPASSを転記して独立PASSにしない。上の32/32は「実カードを査読」であり「32件すべての実世界主張が裏付いた」という意味ではない。
- 出典深度：`PARTIAL_PRIMARY_READ`は主要一次本文の部分的独立閲覧、`METADATA_ONLY`は論文metadata/配布告知等、`SECONDARY_OR_X_ONLY`はX・報道中心、`UNVERIFIED`は今回独立裏付け不能。内容判定は全件見直し対象としたが「FULL_PRIMARY_READ」達成は主張しない。


## 3. Executive disposition


**REQUEST_CHANGES**：重大なモデル名誤記（既知）に加え、公開日／preview可用性、コンテキスト長、実行設定の環境変数、API列挙値、速度算術、独立性の誇張等の**新規不整合**がある。Accepted 32 PARTIAL + Core Schema PASSは主張内容を正当化しない。正しい復元・新たなCore受入・Materiality/Completeness再生成・独立再審査前のtrusted `EVIDENCE_REVIEWED` 移行は**NO**。Human Architecture/Publicationはpendingのまま。


## 4. 全32 Card／全32 Edition Viewの個別監査マトリクス


`T`は `evidence:2026-W43:<T>`、`F`は `task-<F>.json` ／ `view-<F>.json`。Cardの正規ルート：
`sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/`
Viewの正規ルート：
`sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/`
各行の「C」はclaim-1等、検査上注目したclaim番号。全行 `status=PARTIAL` は実データ値。


| Discovery ID | Screening / Evidence / View | T / F | 独立ソース深度 | 該当claim | 査読結論・次のアクション |
|---|---|---|---|---|---|
| `w43-carry-7151fcdc6c3ee392` | MAYBE / PARTIAL / CONTEXT | `3ef7317714013eb9` / `692a004fb38c5539d8da` | SECONDARY_OR_X_ONLY | C1 | 保留可／因果測定なし、支援文脈のみ |
| `w43-lead-muse-10m-20261021` | MAYBE / PARTIAL / CONTEXT | `e79cd46ed4df7c56` / `9281a9c6770f46d57c0f` | SECONDARY_OR_X_ONLY | C1 | 一次決算資料と集計母集団を要求 |
| `w43-lead-oracle-revision-20261021` | MAYBE / PARTIAL / CONTEXT | `0574663ab3a2123e` / `1d7d93a70eeabd2b1c4e` | METADATA_ONLY | C1–3 | v1→v2差分・評価器再検証を要求 |
| `w43-primary-automode-20261021` | INSPECT / PARTIAL / MATERIAL | `956202d0dbd04246` / `ac27404fe35327b74df9` | PARTIAL_PRIMARY_READ | C1–3 | 10/22更新と翌週展開を分離し保持 |
| `w43-primary-decisions-api-20261022` | INSPECT / PARTIAL / MATERIAL | `77109787dd13a833` / `d278dfe78685d601d67a` | PARTIAL_PRIMARY_READ | C1–3 | 400設問/API応答型/GA制限の脚注を確認 |
| `w43-primary-deepinfer-20261020` | KEEP / PARTIAL / MATERIAL | `76da1b3274338d00` / `409f6833c40c6428a43e` | PARTIAL_PRIMARY_READ | C2 | 環境変数名を訂正、LICENSEとベンチ実行条件確認 |
| `w43-primary-deepseek-1017-20261017` | KEEP / PARTIAL / MATERIAL | `46d725d80f715ede` / `d5bceca2dab4af9d685b` | PARTIAL_PRIMARY_READ | C1–3 | 1017版、実API識別子、重量SHAを照合 |
| `w43-primary-duet-20261021` | KEEP / PARTIAL / MATERIAL | `88b6116628d87dd1` / `3670fe4328b9fa322a0b` | PARTIAL_PRIMARY_READ | C1–5 | ウェイトリストと接続先live/comingを分離 |
| `w43-primary-eleven-20261020` | KEEP / PARTIAL / MATERIAL | `5ad9cc05a9516cd6` / `4514088790849f9ca699` | PARTIAL_PRIMARY_READ | C1–3 | AA原表・protocol対応・TTFA条件を要求 |
| `w43-primary-flux-max-20261019` | KEEP / PARTIAL / MATERIAL | `7b57cbc37d685ab4` / `02df2773fd2e9fdb1cd5` | PARTIAL_PRIMARY_READ | C2–3 | 10.95/12.45秒・倍率の算術矛盾を訂正 |
| `w43-primary-github-deprecation-20261019` | MAYBE / PARTIAL / CONTEXT | `8f41546b23a773ab` / `ff78deda46feb19e843c` | METADATA_ONLY | C1 | 廃止対象モデル一覧・代替策を補完 |
| `w43-primary-github-metrics-20261023` | MAYBE / PARTIAL / CONTEXT | `951626f8f98cc50d` / `642c261d5e82c786ecf6` | PARTIAL_PRIMARY_READ | C1–2 | 列挙値・適用レポート・request数を訂正 |
| `w43-primary-github-teams-20261023` | MAYBE / PARTIAL / CONTEXT | `35f6d2e0ae45482d` / `e4b1869996b82b4aac60` | METADATA_ONLY | C1–2 | 権限条件と既存アプリ廃止日を補完 |
| `w43-primary-kimi-20261023` | KEEP / PARTIAL / MATERIAL | `0186d12abaa2b682` / `98f3617da0de43652fcd` | PARTIAL_PRIMARY_READ | C1–4 | X/ブログ分割・ベンチ母集団・11/4は予定 |
| `w43-primary-nemotron-e4b-20261023` | KEEP / PARTIAL / MATERIAL | `a5013a51058f975a` / `8f140062cf7044ea898a` | PARTIAL_PRIMARY_READ | C1–4 | 64K/ライセンス実ファイル/OSI注意 |
| `w43-primary-openai-cloud-20261021` | INSPECT / PARTIAL / CONTEXT | `f6f8199fe5ebe98f` / `0851e82f8db3889fc465` | PARTIAL_PRIMARY_READ | C1–2 | 10/21日付・private preview限定を訂正 |
| `w43-primary-patch-planet-20261021` | INSPECT / PARTIAL / MATERIAL | `bc5b384e48b50605` / `5d21d93e7679f5441b8a` | PARTIAL_PRIMARY_READ | C1–2 | GPT-5.6 Sol訂正、公式URLにsource束縛 |
| `w43-primary-tanstack-20261023` | KEEP / PARTIAL / MATERIAL | `f35c6ce039a8d355` / `20a36d83656e2a4bc1b4` | PARTIAL_PRIMARY_READ | C1–2 | 1.0 coreと0.x harness、タグ照合 |
| `w43-primary-voxtral-20261020` | KEEP / PARTIAL / MATERIAL | `67a30ffa2455924c` / `18a859ebb1ef50040078` | PARTIAL_PRIMARY_READ | C1–3 | STT/TTS比較の評価条件・CJK指標補足 |
| `w43-r2-1password-20261022` | KEEP / PARTIAL / MATERIAL | `972ae1540f70e008` / `673368bcdc8bcd59d611` | PARTIAL_PRIMARY_READ | C1–3 | 承認/認証の実提供と予定を区別 |
| `w43-r2-ambench-v2-20261020` | MAYBE / PARTIAL / CONTEXT | `4502b183faa5cf60` / `1fc486ce9ce010e398e9` | METADATA_ONLY | C1–3 | 改訂差分未読、W43新規研究扱い禁止 |
| `w43-r2-memt-20261019` | KEEP / PARTIAL / MATERIAL | `8c735edcfc5e51f3` / `b09782ca929b9fa55af1` | PARTIAL_PRIMARY_READ | C1–3 | 論文/READMEライセンス分離・数値帰属 |
| `w43-r2-ming-20261019` | KEEP / PARTIAL / MATERIAL | `aecfbb1186d2a6ec` / `4aa7ba129fdeec8b2555` | PARTIAL_PRIMARY_READ | C1–3 | AA原表/ライセンス本体/日付精度確認 |
| `w43-r2-moss-api-20261020` | MAYBE / PARTIAL / CONTEXT | `cea4e497dda757d2` / `11123030a87c7b84c6d2` | METADATA_ONLY | C1 | プラットフォーム実証、README行のみ |
| `w43-r2-moss-report-announce-20261019` | MAYBE / PARTIAL / CONTEXT | `29dd9729d8676386` / `b87e32087dcd83a7c46c` | METADATA_ONLY | C1–2 | 研究は10/16 OUT、報告告知のみ |
| `w43-r2-moss-trainer-20261018` | KEEP / PARTIAL / MATERIAL | `2223bd7df5bb3a3b` / `b26dfd2c2e5ac943e476` | PARTIAL_PRIMARY_READ | C1–2 | 第三者実装、GPU/VRAM計測未再現 |
| `w43-r2-openai-bio-20261021` | KEEP / PARTIAL / MATERIAL | `64a0ea7f8bf66edc` / `6c420e98c87871e4a2a0` | PARTIAL_PRIMARY_READ | C1–3 | 共同研究評価≠独立再現、wet-lab未検証 |
| `w43-r2-openai-lowresource-20261019` | KEEP / PARTIAL / MATERIAL | `6125808e31e3fd0e` / `160489b77720f40bd1e1` | PARTIAL_PRIMARY_READ | C1–3 | ベンダー評価≠独立評価、suite条件明示 |
| `w43-r2-openai-securing-20261023` | KEEP / PARTIAL / MATERIAL | `ffb39177c31de9ea` / `eb7312062a02d1c37826` | PARTIAL_PRIMARY_READ | C1–4 | 提供済攻撃資料条件/事故と対策区分 |
| `w43-r4-flint-20261021` | KEEP / PARTIAL / MATERIAL | `81d172340376c7d1` / `4cea29268a1329179dac` | PARTIAL_PRIMARY_READ | C1–3 | 512K対応/256K推奨を分離、source URL分割 |
| `w43-r4-grok-x-ledger-20261024` | MAYBE / PARTIAL / NON_MATERIAL | `0714ceb7b0ee82be` / `55f087dd70eb920ce6d4` | SECONDARY_OR_X_ONLY | C1–3 | 本文採用禁止、2 postIDのPARTIALセンサー |
| `w43-support-vercel-ollama-20261017` | MAYBE / PARTIAL / CONTEXT | `8b3185b608af1c84` / `6dea52dc4120157072fb` | UNVERIFIED | C1–2 | 配布バージョン/各原サイト要照合 |


全行のMaterialityは仮の編集分類として存在を確認した。強度の偏りがあるため、固定20本採用ではなく、修正後のproof depthと読者にとっての新規性で再採点する。


## 5. 全19 DROPと12 W42 carry-over（Coverage/Completeness）


| Discovery ID | 除外理由（accepted ledger要約） | 独立方針 |
|---|---|---|
| `w43-background-qwen-20261009` | DROP: pre-window Oct 9 Pro/Turbo APIs and weights; secondary Oct 16 listing is not primary; W42-tracked background with no new W43 event. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-background-step5-20261015` | DROP: open weights Oct 15 OUT of window; Oct 22 SF meetup is community/distribution, not a new model event. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-017c9bbc00134ae8` | DROP: uncorroborated vendor X-only security allegation; Patch the Planet is a different process, not corroboration; must NOT repeat as fact. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-10d76dec5907fe46` | DROP: X-only single-poster order claim; no corroborating contract, release or security documentation; Meta shopping signal is separate. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-1b1aea9beacefbcd` | DROP: 17-author harness paper still not located; AM-Bench and OR-License are different papers and must not be conflated. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-2177831df4f20832` | DROP: app exists but Qwen3.8-27B name unverified by issuer or weights; Kimi/Qwen-Image do not verify it; name quarantine holds. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-2cd2da5b249062c9` | DROP: no first-party SMLIB contribution confirmation; Oct 20-23 infra news does not resolve SMLIB status. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-517550f1eb0dda9d` | DROP: LTX-2.3 video still thin on method/license/eval; FLUX 3 Max is a separate model family, not LTX evidence. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-7eb212557bbc5909` | DROP: single-vendor Enterprise/Business sample; no representative sample; Oct 21-22 deployment signals are not methodology repair. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-800408dab7fcce56` | DROP: X-only bot-growth claim with unverified original post; no verified infrastructure metrics or first-party record. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-b2ee0e1dffa42188` | DROP: Fish Audio Drama 3 still thin on usability/licensing/independent eval; Oct 20 Voxtral/Eleven are separate speech events. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-b80ab4ccd3469c31` | DROP: W41 HOLD carry with day-only dating and no clock; digest adds no timing; Granite comparison is not fresh Decision-1 evidence. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-carry-c3439ff42a96e600` | DROP: Le Chonk grounding weights/methods still not open; Voxtral 3 is a different speech/TTS/SDK family and resolves nothing. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-lead-gemini-safety-202610` | DROP: safety-report lead with locator-level body and unproven exact date; no consumed mechanism or dated in-window event. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-r2-out-arc-20261013` | DROP: ARC Prize Argon page Oct 13 OUT of window; leaderboard Qwen3.8 row is not issuer proof for the quarantined W42 name; background with reason, never redated. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-r2-out-deepinfer-repo-20261016` | DROP: repo created Oct 16 07:47Z OUT; Oct 20 X/PyPI announce is the separate IN distribution event; keep distinct, no redating. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-r2-out-moss-base-20261016` | DROP: Base/SFT code and weights Oct 16 01:18Z OUT; Oct 18 trainer, Oct 19 report-announce and Oct 20 API are separate IN events; keep distinct. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-r2-out-orlicense-20261016` | DROP: v1 submitted Oct 16 18:13:25Z OUT (only version); background unless a new revision appears. | EXCLUDED維持（一次資料出現まで非掲載） |
| `w43-r3-ambench-v1-out-20261016` | DROP: v1 submitted Oct 16 21:46:19Z OUT (13m41s before start); replaces contradictory unknown-clock row; v2 revision row separate. | EXCLUDED維持（一次資料出現まで非掲載） |


W42 carry-overは `w43-carry-*` **12行**：11 DROP、`w43-carry-7151fcdc6c3ee392`のみMAYBE→CONTEXT。未証明のX情報やモデル名は隔離継続。これは「12行すべての処分が記録された」ことを示し、「隔離根拠の全原本を再取得した」ことは意味しない。


## 6. 発見事項台帳（優先順、追加P1を含む）


### W43-IA-001 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-primary-openai-cloud-20261021`。Evidence Task suffix: `f6f8199fe5ebe98f`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-0851e82f8db3889fc465.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-0851e82f8db3889fc465.json`）。
フィールド: `claim-1; temporal.events[1]; supplement published_at; view`。現文最小引用: `Google Cloud blog dated Oct 22, 2026`。
**監査認定・読者リスク**：実際のGoogle Cloud公式記事は **October 21, 2026** と表示。しかも3モデルは select enterprise customers 向け **rolling private preview**、一般提供ではない。
**参照一次資料・証拠**：https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers/
**必要修正**：本体を10/21日精度に訂正、observed RSSとpublicationを分離。preview/selected customers/coming soon機能を明記。新r3 supplementの published_at を偽の 00:00Z として時刻事実化しない。
影響範囲：Card+View+Materiality/Completeness。


### W43-IA-002 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-r4-flint-20261021`。Evidence Task suffix: `81d172340376c7d1`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-4cea29268a1329179dac.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-4cea29268a1329179dac.json`）。
フィールド: `claim-1; view rationale`。現文最小引用: `SWA-513, 262144 ctx`。
**監査認定・読者リスク**：公式発表は **supports up to 512k tokens**, **recommend staying within 256k**。262144を最大対応長とする現記述は誤読のおそれ。
**参照一次資料・証拠**：https://recursive.com/updates/introducing-recursive-flint
**必要修正**：製品宣言512K対応と推奨256K、モデルconfig値を別フィールドで区別。速度125+/150+ tok/sはvendor計測、短文/128k session・prefill除外など比較条件注記。
影響範囲：Card+View。


### W43-IA-003 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-primary-deepinfer-20261020`。Evidence Task suffix: `76da1b3274338d00`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-409f6833c40c6428a43e.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-409f6833c40c6428a43e.json`）。
フィールド: `claim-2 / configuration`。現文最小引用: `ENABLE_MTP_VARLEN=1, NEXTN_DECODE default 5`。
**監査認定・読者リスク**：公式実装では環境変数名が **DEEPINFER_ENABLE_MTP_VARLEN=1**、**DEEPINFER_USE_NEXTN_DECODE** default 5。記載どおりでは設定手順として使用できない。
**参照一次資料・証拠**：https://github.com/deepseek-ai/DeepInfer/blob/main/deepinfer/environ.py
**必要修正**：正確な名前・default・0 disableを修正。README/コードの固定SHAあるいは本監査時に確認したbranch-refを明記、低レベル実装再現なしは保持。
影響範囲：Card。


### W43-IA-004 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-primary-github-metrics-20261023`。Evidence Task suffix: `951626f8f98cc50d`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-642c261d5e82c786ecf6.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-642c261d5e82c786ecf6.json`）。
フィールド: `claim-1 / model_selection_mode`。現文最小引用: `user/auto/product/other/unknown`。
**監査認定・読者リスク**：公式API列挙値は **user_selected/auto/product_selected/other/unknown**。また enterprise-user/organization-user レポートも適用対象、request_countはプロンプト数ではなくモデル呼出回数。
**参照一次資料・証拠**：https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode/
**必要修正**：列挙値を正確に記述し、scope / metric denominator / integration ID best-effort制約を付与。
影響範囲：Card+View。


### W43-IA-005 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-primary-flux-max-20261019`。Evidence Task suffix: `7b57cbc37d685ab4`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-02df2773fd2e9fdb1cd5.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-02df2773fd2e9fdb1cd5.json`）。
フィールド: `claim-2; claim-3; view rationale`。現文最小引用: `10.95s vs 277.80s Seedance 2.5 (22x) / 12.45s`。
**監査認定・読者リスク**：算術：277.80÷10.95≈25.4、277.80÷12.45≈22.3。fal公式モデルページの **22x** は12.45秒を分母とする。fal公式ブログには12.45秒から **26.5x** とする記述もあり、自社資料間の矛盾がある。
**参照一次資料・証拠**：https://fal.ai/flux-3-max ; https://fal.ai/blog/introducing-flux-3-max-by-fal
**必要修正**：数値別の計測基準と出典を１行ずつ分ける。判定不能な10.95値は出典を再捕捉、共通基準を満たすまで最大22xなどの見出しを断定しない。vendor claim・AA ranking原表未照合を注記。
影響範囲：Card+View。


### W43-IA-006 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-primary-patch-planet-20261021`。Evidence Task suffix: `bc5b384e48b50605`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-5d21d93e7679f5441b8a.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-5d21d93e7679f5441b8a.json`）。
フィールド: `claim-1; all claims source_ids; sources[0].url`。現文最小引用: `Calif via GPT-6 Sol / primary:openai.com/index/patch-the-planet`。
**監査認定・読者リスク**：OpenAI英日原文は **GPT-5.6 Sol**。ソース識別子が実際の事件解説記事でなく偽装でない別のpseudo locatorを参照。事実と出典を切り離してはならない。
**参照一次資料・証拠**：https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
**必要修正**：新r3 Cardのみモデルを限定置換、実出版社URLを真の収集・閲覧証拠に基づく補足sourceへ束縛。本文原生HTML未取得ならrendered extractionと明記、偽のSHA禁止。CVE推測禁止。
影響範囲：Card+View+Provenance。


### W43-IA-007 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-r2-memt-20261019`。Evidence Task suffix: `8c735edcfc5e51f3`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-b09782ca929b9fa55af1.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-b09782ca929b9fa55af1.json`）。
フィールド: `claim-2; claim-3; verification.tech-report-pdf`。現文最小引用: `CC BY-NC-SA / PolyForm Noncommercial というlicenseをpaperのsource_idsだけで支持 / PDF license sections`。
**監査認定・読者リスク**：ライセンス区分は**別の公式GitHub README**に明記され、論文PDFだけでは支持できない。MemT Nano/Flashと1.86x・66x比較条件の帰属も混同を避ける必要。
**参照一次資料・証拠**：https://github.com/MemTensor/MemT-1.0/blob/main/README.md
**必要修正**：READMEを取得日時とcommitとbyte SHA付きの独立一次sourceに束縛。paper=CC BY-NC-SA4.0, repo software=PolyForm Noncommercial1.0.0, 重み/データは対象外、第三者ライセンス別扱い。証拠なしなら当該断言削除。
影響範囲：Card+Provenance。


### W43-IA-008 — P1 MUST_FIX_BEFORE_STAGE
対象Discovery: `w43-r2-openai-bio-20261021 / w43-r2-openai-lowresource-20261019 / w43-r2-ming-20261019`。Evidence Task suffix: `64a0ea7f8bf66edc / 6125808e31e3fd0e / aecfbb1186d2a6ec`。ファイル: 複数: 対象それぞれ `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-<token>.json` と `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-<token>.json`。
フィールド: `view materiality.rationale; claim-1..3`。現文最小引用: `Independent technical evaluation event / Independent eval methodology / independent #1 robustness`。
**監査認定・読者リスク**：企業/共同研究チームが測った評価、ブラインド選好、AA順位のベンダー転載を『独立再現済』に読める文面へ押し上げている。研究組織とは別の独立再現の有無を峻別。
**参照一次資料・証拠**：https://openai.com/index/scaling-ai-research-for-complex-biological-data/ ; https://github.com/inclusionAI/Ming-3.0-tts
**必要修正**：三つのViewを『公開された評価手順』『共著研究の内部/共同評価』『第三者サイト数値の著者転載、元表未閲覧』に修正。datasetやwet-lab未検証・sample biasをlimitationへ。
影響範囲：Views+Materiality。


### W43-IA-009 — P2 EDITORIAL_IMPROVEMENT
対象Discovery: `w43-primary-kimi-20261023 / w43-r4-flint-20261021`。Evidence Task suffix: `0186d12abaa2b682 / 81d172340376c7d1`。ファイル: 複数: 対象それぞれ `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-<token>.json` と `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-<token>.json`。
フィールド: `sources[0].url; claim-1..4`。現文最小引用: `https://x.com/... + primary:kimi.ai/... / primary:recursive.com/... + primary:huggingface.co/...`。
**監査認定・読者リスク**：単一url値に独立した2ソースを接合し、source_idでどの文章と生バイトを支持するか追跡不能。KimiのX原文をPRIMARY_OFFICIAL一括扱いする解像度不足。
**参照一次資料・証拠**：https://www.kimi.ai/blog/kimi-k3-1-pro ; https://recursive.com/updates/introducing-recursive-flint
**必要修正**：元のDiscoveryは維持し、派生Supplementを別source_id/actual URL・観測日時・source_classで分割。Kimi発表10/23 17:15:24Zの原X/記事、将来11/4 weightsを別イベントとして保持。
影響範囲：Card+Provenance。


### W43-IA-010 — P2 EDITORIAL_IMPROVEMENT
対象Discovery: `w43-lead-oracle-revision-20261021 / w43-r2-ambench-v2-20261020`。Evidence Task suffix: `0574663ab3a2123e / 4502b183faa5cf60`。ファイル: 複数: 対象それぞれ `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-<token>.json` と `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-<token>.json`。
フィールド: `claim-1..3; verification.v1-v2-substantive-delta`。現文最小引用: `v2 is a revision event pending substantive delta check`。
**監査認定・読者リスク**：最新版の公開日だけで新しい研究成果とは言えない。PDFはリポジトリに保存済みだがv1差分と式・ablationは独立再閲覧していない。
**参照一次資料・証拠**：https://arxiv.org/abs/2610.16067 ; https://arxiv.org/abs/2610.24264
**必要修正**：v1/v2の該当本文差分、評価セット、異常oracle修復内容を箇所別に照合。判定できなければCONTEXT/bibliography維持。
影響範囲：Card+View+Completeness。


### W43-IA-011 — P2 EDITORIAL_IMPROVEMENT
対象Discovery: `w43-primary-duet-20261021 / w43-r2-1password-20261022`。Evidence Task suffix: `88b6116628d87dd1 / 972ae1540f70e008`。ファイル: 複数: 対象それぞれ `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-<token>.json` と `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-<token>.json`。
フィールド: `claim-2..5; claim-1..3`。現文最小引用: `6000+ Marketplace connectors / 1Password coming soon / rolling-out`。
**監査認定・読者リスク**：製品の宣伝上の接続数と現在本人アカウントで利用可能な接続は別。1Passwordの承認・autofillも『全コネクタで提供済』と誤解させない。
**参照一次資料・証拠**：https://1password.com/blog/1password-for-ai-agents
**必要修正**：実稼働（rolling）／coming soon／独立未検証をパートナー別に付記。credential injection、agent-visible password/OTP、承認境界を区別。
影響範囲：Card+View。


### W43-IA-012 — P2 EDITORIAL_IMPROVEMENT
対象Discovery: `w43-primary-nemotron-e4b-20261023 / w43-r2-ming-20261019 / w43-primary-deepinfer-20261020 / w43-r2-moss-trainer-20261018`。Evidence Task suffix: `a5013a51058f975a / aecfbb1186d2a6ec / 76da1b3274338d00 / 2223bd7df5bb3a3b`。ファイル: 複数: 対象それぞれ `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-<token>.json` と `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-<token>.json`。
フィールド: `licensing verification / performance benchmark`。現文最小引用: `OpenMDW-1.1 / MIT / Apache-2.0 / KohakuMoss License 1.0`。
**監査認定・読者リスク**：ライセンスの配布README主張とライセンス原文・weight/model repo・OSI適合は同一でない。Kohaku等のカスタム条件は特に独立に確認を要する。
**参照一次資料・証拠**：https://github.com/inclusionAI/Ming-3.0-tts
**必要修正**：License/LICENSE.txtのactual byte、パーミッション、weight commitとartifact URLを取得するまで商用可否/OSI認証/配布可否を断定せず制限を残す。
影響範囲：Card+Completeness。


### W43-IA-013 — P2 EDITORIAL_IMPROVEMENT
対象Discovery: `w43-primary-automode-20261021 / w43-r2-moss-report-announce-20261019 / w43-r2-moss-api-20261020`。Evidence Task suffix: `956202d0dbd04246 / 29dd9729d8676386 / cea4e497dda757d2`。ファイル: 複数: 対象それぞれ `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-<token>.json` と `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-<token>.json`。
フィールド: `temporal.events / claim-1`。現文最小引用: `original 2026-08-07 / 10-22 update; report submission 10/16 OUT; API README 10/20`。
**監査認定・読者リスク**：公表/更新・研究本文/告知・API記載/稼働確認を異種イベントのままにする必要。auto-modeの大半アプリdefault化は翌週予定で、10/22完了扱い禁止。
**参照一次資料・証拠**：https://claude.com/ja/resources/articles/auto-mode-default-in-claude-code
**必要修正**：event_type/source publication/updateとrolloutを別々に扱う。プラットフォームWebページ独立閲覧未了はmetadata-onlyとする。
影響範囲：Card+View。


### W43-IA-014 — P2 EDITORIAL_IMPROVEMENT
対象Discovery: `w43-r4-grok-x-ledger-20261024 / original 7 projected cards`。Evidence Task suffix: `0714ceb7b0ee82be`。ファイル: `sources/2026-W43/evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/results/task-55f087dd70eb920ce6d4.json`（View: `sources/2026-W43/evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/views/view-55f087dd70eb920ce6d4.json`）。
フィールド: `source_class projection; X Intake status`。現文最小引用: `X intake COMPLETE / sensor PARTIAL / PAPER_LEAD→SOCIAL`。
**監査認定・読者リスク**：X受付のCOMPLETEは受領契約を満たした意味のみ。2 pinned post IDs以外のX topic signalは原投稿を追跡不能。7派生source_typeプロジェクションを一次資料への自動昇格と扱うと循環検証。
**参照一次資料・証拠**：sources/2026-W43/execution/compat/evidence-source-class-projection/projection-ledger-r2.json
**必要修正**：原source_typeと投影先を列管理し、PRIMARY_PAPERはsupplement真のPDF/本文経由でのみ追加。GrokをSelection本文素材にせず、topic-level X主張を独立裏付け扱いしない。
影響範囲：Provenance+Completeness。


### W43-IA-015 — P2 EDITORIAL_IMPROVEMENT
対象Discovery: `r2 Muse handoff/session, frozen accepted authorities`。Evidence Task suffix: `-`。ファイル: 該当execution manifest、ledger、session／handoff。
フィールド: `supplement sources.length; starting Tree transcription`。現文最小引用: `supplement 8 entries / b8e1a207edb3cc92827284241e486ce4683612`。
**監査認定・読者リスク**：実物のr2 supplementは6件（2既存+4新規）。starting parent `6a389877...`の実Treeは `b8e1a207edb3cc82927284241e486ce468360642`（過去Sol検出の転記修正）。旧文書は変更しない。
**参照一次資料・証拠**：sources/2026-W43/external/evidence-supplement/evidence-authority-supplement-r2.json
**必要修正**：履歴errataを新報告で明示し、accepted r1/r2や過去handoffはimmutability維持。
影響範囲：Report only。


## 7. Source-class/provenance crosswalk


| original source_type | derived projected class | ID／対象 | 判定 |
|---|---|---|---|
| X_OBSERVATION | SOCIAL | carry `7151fcdc6c3ee392`、Grok `0714ceb7b0ee82be` | 正常：Xをprimaryに昇格させない |
| X_VENDOR_STATEMENT | SOCIAL | auto-mode `956202d0dbd04246` | XはSOCIAL、10/22公式記事は別supplement |
| PAPER_LEAD | SOCIAL | oracle `0574663ab3a2123e`、AM-Bench `4502b183faa5cf60` | 元のleadはSOCIAL、PDFのみPRIMARY_PAPER |
| SECONDARY_CLAIM | SECONDARY | Meta adoption `e79cd46ed4df7c56` | 二次報道のまま |
| SECONDARY_OR_COMMUNITY_LEAD | SECONDARY | Vercel/Ollama `8b3185b608af1c84` | 配布元が公式でも探索leadはSECONDARYに投影 |
| その他25 | passthrough | 25 tasks | frozen Core vocab基準のまま、実在ソースは各Cardで検証 |


7 mapped / 25 passthrough、source-type以外差分禁止のbuilder規則はread-onlyで確認。ただしこの監査で凍結Core自体の単体試験は **NOT_EXECUTED**。


r2 Supplement Manifestは現物で **6 sources**（oracle-v2.pdf 261,750B、am-bench-v2.pdf 2,379,235B、auto-mode.html 599,884B、OpenAI changelog.html 553,250B、GCP HTML 224,991B、MemT PDF 7,096,280B）。Manifest記載のbyte_countはGitHub directory metadataのサイズと照合。Manifest記載SHA256を**独立byte-hash計算したとは主張しない**。Supplementの各sourceは task scope 1:1、paper READMEライセンスには該当しない。r2ハンドオフの「8件」と明白に食い違う。


Evidence authority set `3e7fa827…` / View set `c4e0ce93…`、Screening set `75dd95db…`、Discovery acceptance `discovery-accepted-v2.json`、Graph `5a94b757…`。Base acceptanceのmetadata SHAと実ファイル原文を確認したが、全rawファイルの暗号学的再ハッシュは未実行。


## 8. Date/event matrix


| 事件 | 期間判定 | 意味／指摘 |
|---|---|---|
| 一般W43窓 | **[2026-10-16 22:00Z, 2026-10-23 22:00Z)** | EDTでは10/16 18時から10/23 18時。終端exclusive |
| Qwen 10/09、Step 5 10/15、ARC 10/13 | OUT | 背景情報のみ |
| MOSS weights/code 10/16 01:18Z、DeepInfer repo 10/16 07:47Z、OR License 10/16 18:13:25Z | OUT | 10/18 trainer/10/20 announcer別件はIN |
| AM-Bench v1 10/16 21:46:19Z | **OUT（13分41秒差）** | v2 10/20は文書改訂のみ、substantive delta要確認 |
| DeepSeek-1017 10/17 / MOSS Trainer 10/18 / FLUX Max 10/19 | IN | API/model/tooling event identityを分離 |
| MemT 10/19 | IN (author date) | PDF real archived、式全文は今回独立未照合 |
| Anthropic 8/07原文 / 10/22更新 | original OUT / update IN | 10/22時点の翌週デフォルト化は**未来のrollout** |
| Google Cloud/OpenAI配布 | **10/21公式掲載** | r2 Cardの10/22と競合、private preview |
| Recursive Flint 10/21 | IN | HF weightsとannounce、512Kと256K推奨を区別 |
| Kimi 10/23 17:15:24Z | **IN（残4h44m36s）** | API／発表と **11/04 weight予定**を別々に扱う |
| Grok observed 10/24 12:43:17Z | post-window ingestion | X rawの取得時刻はイベントの公開時刻ではない |


## 9. 31 substantive + 1 Grok 編集評点


20 MATERIAL候補：モデル/学習・配布（Kimi、Flint、DeepSeek1017、Nemotron、MemT、Ming）、infra（DeepInfer、MOSS trainer）、voice/video（Voxtral、Eleven、FLUX）、agents（Duet、1Password、auto-mode、Decisions、TanStack）、研究/安全（低資源言語、biology、training containment、Patch）の合計20。**評価は候補の技術的重要性に対する暫定賛成であり、裏付け足りない数値・条件・表示上の可用性を修正しないまま20件を本文確約しない**。特にKimiの重み予定日、Flint 512K/256K、DeepInfer設定、FLUX速度、ベンチvendor claimとlicenseは必修。


11 CONTEXT候補：Claude gzip carry、Meta利用者数、oracle v2、GitHub deprecation/metrics/Teams、OpenAI GCP配布、AM-Bench v2、MOSS API/報告告知、Vercel/Ollama配布。重要性と深さは不均一。**Github metrics のAPI実装変更は方法論的独自性がありCONTEXTのままでも、導入時の技術的価値を説明すべき**。OpenAI GCPは10/21 private previewであり、editorial MATERIALへの機械的promotionも不要。MOSS reportは研究の新発表と取り違え禁止。


**1 Grok NON_MATERIAL**は監査用Xセンサーbinderであり、独立技術記事でもSelection候補でもない。計51行に対して 19 EXCLUDEDが明記される。Materiality ledgerの非DROP rationale はほぼ `Screening=X; Edition View=Y` という機械的参照に止まり、**独立の採否根拠・重要度の差を比較できる記述ではない**。これは本監査の新たな編集品質指摘であり、差分解消後にledger rationale/edition-local decision noteに内容根拠を付すべき。


Completeness：`weekly:current-relevance = LIMITATION` **適切**（preview/発表日/弱いセンサー補正が必要）；`weekly:technical-significance = LIMITATION` **適切**（vendor benchmark, license, evaluation independence未解決）；`weekly:carry-over = SATISFIED` **形式的な12行dispositionとして適切**（継続隔離を意味する）。overall `LIMITED`を維持し、修正後も自動FULLへ昇格しない。まだSelection/Architecture gateの判断はしていない。


## 10. 過去Sol/Museとの矛盾／新発見


| 出典／既存理解 | 監査結論 |
|---|---|
| r2 Muse: supplement=8 | **実際6**。既存Sol r2と held r3が既に指摘 |
| r2 Muse: starting Tree転記 `b8e1a207edb3cc92827284241e486ce4683612` | **実際 `b8e1a207edb3cc82927284241e486ce468360642`**。既知erratum |
| held r3: Patch `GPT-6 Sol` | 正式はGPT-5.6 Sol、独立一次照合済み。**既知** |
| held r3: MemT README licenseとpaper URL混同 | GitHub READMEに独自license区分確認。**既知** |
| held r3: 27 unaffected、修正2 topicsのみ | **棄却**。追加 Cloud日付/preview、Flint ctx、DeepInfer env var、GitHub enum、FLUX算術、Viewの評価独立性、source二重URL等の修正対象を増やすべき |
| r2 Card Google Cloud: blog 10/22 | **一次原本10/21**（本監査新発見） |
| r2 Flint Card: max 262144 ctx | **一次原本512K supported / 256K recommended**（新発見） |
| r2 DeepInfer Card: `ENABLE_MTP_VARLEN` | **実装 `DEEPINFER_ENABLE_MTP_VARLEN`**（新発見） |
| r2 Github metrics Card: user/product | **実装 `user_selected/product_selected`**（新発見） |
| r2 FLUX card: 10.95対277.80=22x | これは**25.4x**。12.45対277.80=22.3x、公式ブログは26.5x記載で自社矛盾（新発見） |
| r2 Views: Independent technical evaluation | independent reproductionは一度も実施されていない。表現を控える（新発見） |
| Machine PASS | 正規Schema/結合の受理であり、技術的正しさの証明ではない。worker報告のstage scratch precheckは独立再実行していない |


## 11. 編纂統括Sol向け単一統合・限定再生成案（**提案のみ**）


1. 既存保留r3命令の発行・実行は引き続き保留。統括Solが **W43-IA-001〜015** を重複排除して**一つの新しい有界修正契約**を策定。作業起点のremote HEAD/Tree等6-way strict preflightを再要求。担当Museへの直接dispatchは本監査では行わない。
2. 対象Card優先：必修 `w43-primary-openai-cloud-20261021`, `w43-r4-flint-20261021`, `w43-primary-deepinfer-20261020`, `w43-primary-github-metrics-20261023`, `w43-primary-flux-max-20261019`, `w43-primary-patch-planet-20261021`, `w43-r2-memt-20261019`。View文言 `w43-r2-openai-bio-20261021`, `w43-r2-openai-lowresource-20261019`, `w43-r2-ming-20261019` と source URL `Kimi`, `Flint` を加える。これ以外は必要な機械的hash伝播のみ、意味変更ゼロであることを32行diffで確認する。
3. **新規の正真正銘raw sourceが必要**：Patch公式英語本文（botwallならrendered extractionと明記）、MemT原README revision+SHA、Google Cloud 10/21公式本文とtimestamp、Flint公式本文/config/weight license、DeepInfer README + environ.py固定commit、GitHub metrics changelog、fal blog/model-pageの矛盾箇所、Kimi blogとXの分離。派生supplementのsource_idはtask拘束し、raw/source/observationの違いを正直に保存。AM-Bench/oracle v1-v2 deltaは補助調査、判定不能なら未解決維持。
4. edition-localの新r3 supplement/兼容投影package/interactive-Evidenceを作成し、Frozen Core既存native agent-first adapterでEvidence prepare→32 Card validation→新Evidence accepted→32 Views→新Views accepted→51 Materiality ledger→3 Completeness obligationsを順に再生成・検査。r1/r2 accepted dirs と過去Source/Discovery/Screening/State/Checkpoints/Human Gateはimmutable。r2 ledger/completenessをhistory/r2 snapshotしてからcanonical derived ledger更新、既存manifest改変禁止。
5. 検証：32件 source→claim trace、source_type 7投影の non-primary-inflation、Grok `COMPLETE`登録 vs `PARTIAL`センサー、raw size/SHA、二重URL禁止、異種sourceの1:1同定、in/out date、README license source境界、FLUX再計算、変数名・enum literal、明示的なnegative/tamper test、適切な scratch Stage precheckを**実際に**実行しstdout/exit codeを記録。Legacy direct-helper #568 / source vocab #569のfrozen Core本体には手を加えない。
6. 新r3は独立Solが再度内容をレビューするまで**trusted Stage移行禁止**。Core validationは自己記録を査読者が再閲覧する。Human Architecture/Publication承認・Selection・執筆・Freeze・Releaseは対象外。


## 12. 監査上の限界・宣言


この監査は**32 Card＋32 Viewの網羅的文書監査**として実施した。一方、全32対象の元source HTML/PDF/weight/licenseを完全に再取得したわけではない。32/32「深く独立した一次資料全文・式・再現試験」ではないため、全source対向チェック済みと偽らない。対象原料の一部は論文PDF・ベンダー重み・AA original benchmarkへの読み取り/再現を残す。Core Scriptの動的再検証とraw SHA独立再計算も **NOT_EXECUTED**。その制約の下で**確認された複数の新規P1技術不整合**があり、REQUEST_CHANGES結論は十分に成立するが、網羅的な正確性PASSは成立しない。


**停止状態：`INDEPENDENT_SOL_W43_EVIDENCE_COMPREHENSIVE_AUDIT_COMPLETE`。**
これは**監査行為終了（REQUEST_CHANGES、実体調査の残余を開示）**を意味し、Edition acceptance・EVIDENCE_REVIEWED承認・Human Gateを意味しない。
