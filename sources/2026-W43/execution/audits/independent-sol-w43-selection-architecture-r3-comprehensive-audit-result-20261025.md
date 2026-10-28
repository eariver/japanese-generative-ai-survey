# Provenance — independently written audit, preserved transcription

Original user-provided Google Drive / uploaded file: `20261025170711_SolReview.md` (UTF-8 with BOM/CRLF); **62,790 raw bytes**, raw SHA-256 `a54defbb90ac8ad768c4f5f6c9791a93e04de632df427ad74af6e71815ed0b59`. This is a **text-normalized non-byte-identical copy** of the user's source; original remains authoritative for raw bytes and timestamps. The independent reviewer was read-only and audited W43 HEAD `dd2595862fb6b8172179594868eecad0b08a8e17` / Tree `9eef50f540982ae265ad5bc0fd6b5bf4cebcb721`. **No Human Gate, Stage or repository-write authority is conferred by this document.** Findings are subject to exact first-party corroboration and Sol editorial adjudication.

---

# W43 r3 Selection / Architecture 総合独立監査 — Sol
**監査日時** 2026-10-25 17:07 JST / **Status** INDEPENDENT_READ_ONLY_EXTERNAL_AUDIT / **基準コミット** `dd2595862fb6b8172179594868eecad0b08a8e17`
**本監査報告の保存先** Google Drive `GPT-Sol_Review` / **適用契約** `sources/2026-W43/execution/audits/independent-sol-w43-selection-architecture-r3-comprehensive-audit-request-20261025.md`


## 1. Executive decision
- **Selection: PASS_WITH_LIMITATIONS.** 採用19／保留1／不採用12、Architecture配置19/19、NON_MATERIAL・post-cutoffの漏出0を確認。選定範囲の再選定を要求する根拠は現時点でない。
- **Architecture: REQUEST_CHANGES.** P2の決定性設定条件が不十分で、P5 Voxtral TTSの一次資料が35+言語対9言語で不一致。両者は読者向け技術説明に直結するP1修正事項。P4演算式はr3で修正済みだが出典・比較条件の制約は残存する。
- **2つのtrusted Bridge Stage移行可否: NO / NO.** EVIDENCE_REVIEWED→SELECTION_COMPLETEを本監査が実行・承認せず、さらにARCHITECTURE_ESTABLISHEDも不可。P1是正と編集統括Solによる再判定が必要。
- **P0:** なし。**P1:** W43-ISA-001,002。**P2:** ISA-003〜009。**Human Architecture Approval:** 未付与。本レポートはHuman決定の代替ではない。
- Core schema validation PASS / READY_FOR_ARCHITECTURE_REVIEWは内容・source authority PASSではない。


## 2. Starting preflight: exact six
|対象|期待HEAD / 実HEAD|期待Root Tree / 実Root Tree|判定|
|---|---|---|---|
|W43 remote|dd2595862fb6b8172179594868eecad0b08a8e17|9eef50f540982ae265ad5bc0fd6b5bf4cebcb721|一致|
|main remote|041a08dfef3112643cbf85b4a86a7b6f9128aed6|a134dc36a407d08ab1de416324229b3955e0325a|一致|
|Frozen Core v2|774dd39a951c9ac3818e83dfffd4c7666efb0a20|cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481|一致|


実際にGitHub remote ref(HEAD)とGit commit treeを直接取得した。以後のrepository読出しはW43固定SHA指定。現 Production State `EVIDENCE_REVIEWED`、Next `stage:selection`、機械Checkpoints selection/architecture `pending/pending`、Human Gates `pending/pending`、`architecture-v2.json.human_review`は全null。GitHubへの書込み・Stage移行・PDF作成はゼロ。


## 3. Coverage & limits
- Candidate Matrix 32/32、Selection assignment 32/32、Evidence Result 32/32をread-only取得し構造・claims・source/limitation概数を照合。全32一次資料をline-by-lineで再監査し直したわけではない。
- Architecture 8/8パッケージ、実際のmust_cover 31/31を項目ごとに評価。候補配置は19/19、非採用/保留配置0。
- Review Attention item_id 68/68 unique、native limit100、shown68/68、truncated=false。ただし優先度フィールドなし、SELECTED候補への直接attention0件。**例外項目の全件表示**であって全技術主張の査読を意味しない。
- Screening accepted 51件＝KEEP17/MAYBE11/INSPECT4/DROP19。Evidence Result 32件は全件PARTIAL。Materiality MATERIAL20/CONTEXT10/NON_MATERIAL2/EXCLUDED19。Completeness LIMITED、残余5。
- 外部一次サイトは末尾のURLを実際に参照した範囲で記載。日本語品質はArchitecture構成・用語のみ評価（完成原稿なし）。Native Python検証・全source raw byte独立SHA256 rehash・GPU/benchmark独立再現・PDF頁数の実測は **NOT_EXECUTED**。
- 5生成JSONのHashについてrunner auditに期待SHA256が記載されていることと、実際に独立再計算したことは区別する。今回はGit blob同一性とJSON参照整合を一部直接確認したが、5/5 SHA256計算を独立実行したとは主張しない。


## 4. Findings register（修正順）
### W43-ISA-001 — P1 MUST_FIX — DeepInfer の決定性が設定条件で欠落（NEW）
- 対象: `sources/2026-W43/architecture-v2.json#/packages/1/must_cover_requirements/1` (§2.2); 同 `orchestration/v2/interactive/selection-architecture-input.json#/architecture/packages/1/must_cover_requirements/1`、候補 `409f6833c40c6428`。
- 現記述: `DEEPINFER_ENABLE_MTP_VARLEN=1` と `batch-invariant・deterministic sampling` が同一の機能説明に併記され、両者を同時有効にできるよう読める。
- 根拠: DeepInfer公式 README https://github.com/deepseek-ai/DeepInfer — deterministic samplingは `DEEPINFER_BATCH_INVARIANT=1` + `DEEPINFER_ENABLE_MTP_VARLEN=0` + fixed `seq_seed`、NVIDIA限定。通常のDSpark可変MTP `=1` と別モード。env default nextn=5、0で無効も公式。
- 修正: `推測デコード系（MTP_VARLEN=1）` と `決定的サンプリング系（MTP_VARLEN=0, BATCH_INVARIANT=1, seq_seed固定, NVIDIA）` を**排他的構成例**として分離し、同時利用の主張を禁止。§2.2表・コード・境界に記載。必要対象: Architecture + input + Summary派生。Selectionの19件維持。
- 影響: 実装再現性、誤ったチューニング指示。旧SA-001..007で未指摘。


### W43-ISA-002 — P1 MUST_FIX — Voxtral TTSの言語数に公式資料間不整合（NEW）
- 対象: `architecture-v2.json#/packages/4/must_cover_requirements/0` (§5.1)、`/packages/4/boundaries`; 候補 `18a859ebb1ef5004`。
- 現記述: `50+・35+・50+ 言語`（STT/TTS/方言）が安定した単一仕様のように並ぶ。
- 根拠: Mistral公式発表 https://mistral.ai/news/voxtral-3/ はTTS `35+ languages / 50+ dialects`。公式モデルカード https://docs.mistral.ai/models/voxtral-mini-tts-3-0 はTTS `9 languages`。公式言語表 https://docs.mistral.ai/studio/audio/specs-and-limits/languages は35言語/50+方言、プリセット声の対応はより限定。これらは2026-10-25時点の公開ページ間で不整合。
- 修正: 製品・モデル版・機能（合成/プリセット音声/voice cloning）を軸に対応言語数を別表化し、範囲不明の項目は「発表記事による」「モデルカードとは不整合、要確認」として確定仕様扱い禁止。TTS評価標本11言語は製品対応言語数ではない。Mistral側更新時刻・版を記録できなければ数字を断定せず縮約。
- 影響: 読者の製品選択・SDK設計判断。旧SA-001..007で未指摘。Architecture内のsource limitationsだけでは衝突は明示されていない。


### W43-ISA-003 — P2 — Nemotron総数/effective と Flint active の非等価比較（NEW）
- 対象: `architecture-v2.json#/packages/0/must_cover_requirements/1` (§1.2)、§1.5、候補 `8f140062cf7044ea` と `4cea29268a132917`。
- NVIDIA BF16公式 https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16 は **8B total, 4B effective**、基盤Gemma4 E4B。Flint card https://huggingface.co/RecursiveSI/flint は **39.8B total, ~2.5B active**, output headを含みinput embeddingを除く。
- 現行の「Nemotron 4B級」だけでは、総数・実効・activeの比較条件が明示されない。修正: 8B/4B、39.8B/2.5Bを「計数規約非一致」を明記して別列で表示。licenseはBolt OpenMDW-1.1、基盤Gemma4 Apache2.0を混同禁止。要 Architecture内表とDraft制限。


### W43-ISA-004 — P2 — FLUX演算修正済みでも速度比較は未同定（RESIDUAL）
- 対象: §4.2, §4.3、候補 `02df2773fd2e9fdb`。
- 演算は `277.80/10.95=25.3699`, `277.80/12.45=22.3133`, `(277.80-12.45)/277.80*100=95.5184%` で成立。一方fal公式ブログ https://fal.ai/blog/introducing-flux-3-max-by-fal は**12.45s / 277.80sと26.5x /96.2%を同時掲載**し数学的に不整合。10.95s原PRは現回収バイトにない。
- 修正: vendor chartのresolution、生成尺10秒、GPU、batch、画質、cold/warmなど同一性の証拠がない限り「原資料内の算術を独立再計算した」とだけ記載。「独立計測」「実性能で22倍高速」には昇格させない。r2 ISA相当の算術逆数はr3で修正済み。


### W43-ISA-005 — P2 — Decisions APIの料金説明の条件不足（NEW）
- 対象: `architecture-v2.json#/packages/7/must_cover_requirements/0` (§8.1)、候補 `d278dfe78685d601`。
- 公式 https://developers.openai.com/api/docs/guides/decisions はGPT-6 Lunaのみ、input $0.10/1M、cache hit $0.01/1M、output 0という基本仕様を支持するが、30分/12時間cache **writes are charged**、地域処理プレミアムと長文脈乗数が適用される。
- 修正: 「出力無料」は出力トークン課金なしの意味に限定。$0.10/$0.01を総運用単価・全条件の固定価格と誤読させない。400 questionsは**per request**でありAPI総呼出上限ではない。


### W43-ISA-006 — P2 — Review Attention 68件の重要度とSelectedリスクへの橋渡し不足（NEW）
- 対象: `architecture-review-attention-v2.json#/items`、人向けReview Packet。68/68 unique, limit100, overflow0は実測。しかし要素にpriorityがなく、68=19 EXCLUDED+2 NON_MATERIAL+19 DROP+4 INSPECT+11 MAYBE+1 HOLD+12 REJECT、SELECTED自体への項目0。
- これはCore機械出力の不具合と断定しない（exception-focusedの仕様）。**人間が読む追加リスク表**をedition-localに添付: selected19中のP1/一次資料衝突・vendor-only bench・将来可用性を先頭にまとめ、68機械Attentionとの重複と分類を明示。Core変更禁止。


### W43-ISA-007 — P2 — P8記事密度・3.5頁見積の能力上限（RESIDUAL）
- 対象 `architecture-v2.json#/packages/7/profile_extensions/page_allocation`。P8はDecisions GA・TanStack 1.0・DeepSeek 1017を3.5頁に掲載予定。§8.1–8.3は各々 API型・料金・rate/beta、monorepo stable/experimental、model update/free期限/license を持つ。
- 修正: 決定APIの1例＋安定/実験表＋DeepSeek更新差分の短い対照表を優先し、実測を伴わない優劣表や長いPRコピーは省く。出典が足りなければDeepSeek/TanStackを短い囲み記事へ縮約。ページ数水増し禁止。r1 SA-003の十分性リスクは部分改善に留まる。


### W43-ISA-008 — P2 — 特定言語の翻訳・出典表記（NEW）
- 対象: P1〜P8のtitle/purpose/must_cover_requirements。`hyper 記憶`, `符号生成モデル`, `声の様式`, `先端モデルの学習環境の隔離`, `数表批判`など、読者に意味が伝わる初出定義が必要。特に「最速」「世界最高」「優位」をベンダー評価から断定しない。
- 修正: `Gated DeltaNet-2`, `Mixture-of-Storage`, `context biasing(用語辞書による認識誘導)`, `cpWER`, `effective parameters`を初出で自然な日本語と英語併記。r1の`辺境訓練`や`符号化`は修復済みで再発なし。


### W43-ISA-009 — P2 — 可用性と日時のreader-facing固定（RESIDUAL）
- 対象 P1 §1.1/§1.5、P3 §3.2/§3.4、P8 §8.2。
- Kimi Oct23 17:15:24Zは IN、Nov4重みはFUTURE。1Password/Duetはcoming soon、Duet waitlist US Pro/Max。TanStack release Oct22 15:18:14Z/registry 15:21:49ZはIN、blog日付Oct23とは区別。GitHub Metrics 23:42:03Zはexclusive cutoff後でW43から除外。
- 修正: 記事タイトルと比較表は「発表・プレビュー・GA・重み配布・利用者が再現可能」を別status列に。日時欠測は埋めず、引用に出典種別を併記。


## 5. All 32 Selection decisions (no skipped candidate)
Evidence statusは全件PARTIAL。判定SUPPORTED_WITH_LIMITATIONSは技術主張の独立再現完了を意味しない。
|#|Candidate suffix|題名|Screen|Materiality|Selection/role|配置|固有のリスク・境界|判定|
|---:|---|---|---|---|---|---|---|---|
|1|98f3617da0de4365|Moonshot Kimi K3.1 Pro|KEEP|MATERIAL|SELECTED/PRIMARY|P1/主|X only 2.8T/104B; API available, Nov4 weights future|SUPPORTED_WITH_LIMITATIONS|
|2|1d7d93a70eeabd2b|Agent-eval oracle integrity audit (2610.16067v2)|MAYBE|CONTEXT|REJECT/NONE|—|Full 29pp body beyond abs+intro unread; v1-to-v2 delta unchecked; paper claims unreproduced here|SUPPORTED (不採用)|
|3|55f087dd70eb920c|Grok X weekly intake ledger|MAYBE|NON_MATERIAL|REJECT/NONE|—|audit binder NEVER_STORY|SUPPORTED (不採用)|
|4|b26dfd2c2e5ac943|KohakuMossTrainer|KEEP|MATERIAL|HOLD/NONE|—|HOLD: no independent 5090 rerun; custom license|UNRESOLVED|
|5|b87e32087dcd83a7|MOSS-Image technical report arXiv announcement|MAYBE|CONTEXT|REJECT/NONE|—|Report body Oct16 OUT; announcement IN; substantive v1->v2 delta if any unchecked|SUPPORTED (不採用)|
|6|e4b1869996b82b4a|GitHub Copilot in Teams notifications-to-code|MAYBE|CONTEXT|REJECT/NONE|—|Changelog-level only; per-plan rollout unvalidated|SUPPORTED (不採用)|
|7|692a004fb38c5539|Claude Code gzip and startup performance|MAYBE|CONTEXT|REJECT/NONE|—|No causal benchmark; X-HTML unauthenticated; changelog bodies partially read|SUPPORTED (不採用)|
|8|1fc486ce9ce010e3|AM-Bench v2 revision|MAYBE|CONTEXT|REJECT/NONE|—|Full 38pp body beyond abs+intro unread; v1-to-v2 delta unchecked; findings unreproduced|SUPPORTED (不採用)|
|9|d5bceca2dab4af9d|DeepSeek V4.1-Flash-1017|KEEP|MATERIAL|SELECTED/SUPPORTING|P8/補|license/model weights/1017 artifact not local rehashed|SUPPORTED_WITH_LIMITATIONS|
|10|4514088790849f9c|ElevenLabs Eleven Realtime v1|KEEP|MATERIAL|SELECTED/SUPPORTING|P5/補|OpenAI protocol compatibility not drop-in; migration guide unopened|SUPPORTED_WITH_LIMITATIONS|
|11|160489b77720f40b|OpenAI low-resource language coding evaluations|KEEP|MATERIAL|SELECTED/PRIMARY|P7/主|hidden tests vendor-held; 19/20 not independent replication|SUPPORTED_WITH_LIMITATIONS|
|12|6c420e98c87871e4|OpenAI distributed biological reasoning|KEEP|MATERIAL|SELECTED/PRIMARY|P7/主|blinded 75% internal/coauthored; wet-lab unavailable|SUPPORTED_WITH_LIMITATIONS|
|13|18a859ebb1ef5004|Mistral Voxtral 3|KEEP|MATERIAL|SELECTED/PRIMARY|P5/主|TTS languages vendor announcement 35+ vs product model card 9|NEEDS_CORRECTION|
|14|409f6833c40c6428|DeepSeek DeepInfer|KEEP|MATERIAL|SELECTED/PRIMARY|P2/主|deterministic sampling requires MTP_VARLEN=0 and fixed seq_seed|NEEDS_CORRECTION|
|15|d278dfe78685d601|OpenAI Decisions API|INSPECT|MATERIAL|SELECTED/PRIMARY|P8/主|cached writes and regional/long-context multipliers need cost qualifiers|SUPPORTED_WITH_LIMITATIONS|
|16|02df2773fd2e9fdb|fal FLUX 3 Max|KEEP|MATERIAL|SELECTED/PRIMARY|P4/主|10.95s raw absent; 12.45s blog contradictory with 26.5x|SUPPORTED_WITH_LIMITATIONS|
|17|4cea29268a132917|Recursive Flint|KEEP|MATERIAL|SELECTED/PRIMARY|P1/主|2.5B counts output head, not input embedding; speed vendor|SUPPORTED_WITH_LIMITATIONS|
|18|3670fe4328b9fa32|Anthropic Claude Duet|KEEP|MATERIAL|SELECTED/PRIMARY|P3/主|6000+ inventory not live; waitlist preview|SUPPORTED_WITH_LIMITATIONS|
|19|6dea52dc41201570|Vercel/Ollama/Unsloth distribution|MAYBE|CONTEXT|REJECT/NONE|—|Composite ID vs two event families; single 2026-10-23 event_date insufficient — split legs required|SUPPORTED (不採用)|
|20|b09782ca929b9fa5|MemTensor MemT-1.0|KEEP|MATERIAL|SELECTED/PRIMARY|P2/主|65pp equations unreviewed; 1.86x/66x author only|SUPPORTED_WITH_LIMITATIONS|
|21|ff78deda46feb19e|GitHub Copilot model deprecations|MAYBE|CONTEXT|REJECT/NONE|—|Deprecated model list unpinned; docs/migration bodies unfetched|SUPPORTED (不採用)|
|22|642c261d5e82c786|GitHub Copilot usage metrics API|MAYBE|NON_MATERIAL|REJECT/NONE|—|POST_CUTOFF 2026-10-23T23:42:03Z|SUPPORTED (不採用)|
|23|ac27404fe35327b7|Anthropic auto-mode default|INSPECT|MATERIAL|SELECTED/SUPPORTING|P3/補|auto-mode next-week future at cutoff|SUPPORTED_WITH_LIMITATIONS|
|24|673368bcdc8bcd59|1Password for Agents|KEEP|MATERIAL|SELECTED/SUPPORTING|P3/補|1Password Duet coming soon; approval not independently tested|SUPPORTED_WITH_LIMITATIONS|
|25|8f140062cf7044ea|NVIDIA Nemotron 3.5 Bolt E4B 4GB|KEEP|MATERIAL|SELECTED/SUPPORTING|P1/補|8B total/4B effective; OpenMDW-1.1 not Apache model license|SUPPORTED_WITH_LIMITATIONS|
|26|4aa7ba129fdeec8b|InclusionAI Ming-3.0-tts|KEEP|MATERIAL|SELECTED/SUPPORTING|P5/補|AA ranked scores publisher-cited, AA originals missing|SUPPORTED_WITH_LIMITATIONS|
|27|5d21d93e7679f544|OpenAI Patch the Planet|INSPECT|MATERIAL|SELECTED/PRIMARY|P6/主|official rendered, not raw HTML; disclosure not independently reproduced|SUPPORTED_WITH_LIMITATIONS|
|28|11123030a87c7b84|MOSS-Image MOSI API availability|MAYBE|CONTEXT|REJECT/NONE|—|README line vs live deployment distinguished; independent API call absent|SUPPORTED (不採用)|
|29|9281a9c6770f46d5|Meta Muse adoption and shopping activity|MAYBE|CONTEXT|REJECT/NONE|—|Earnings transcript unread; Sensor Tower methodology unvalidated; spend figures uncorroborated|SUPPORTED (不採用)|
|30|20a36d83656e2a4b|TanStack AI 1.0|KEEP|MATERIAL|SELECTED/SUPPORTING|P8/補|1.0 stable packages but agent harness experimental; Oct22 release vs Oct23 article|SUPPORTED_WITH_LIMITATIONS|
|31|0851e82f8db3889f|OpenAI models on Google Cloud|INSPECT|CONTEXT|REJECT/NONE|—|Vendor distribution claims; no independent GA verification; OpenAI-side page unopened|SUPPORTED (不採用)|
|32|eb7312062a02d1c3|OpenAI frontier training containment and red-teaming|KEEP|MATERIAL|SELECTED/PRIMARY|P6/主|RSS publication hour != page hour; threat environment vendor-described|SUPPORTED_WITH_LIMITATIONS|


## 6. Eight packages, 31 actual required subsections
|Package|記事軸|主/補候補数|must_cover数|計画頁（拘束力なし）|主要問題|原稿準備|
|---|---|---:|---:|---:|---|---|
|P1|公開予定の重みと、すでに動かせるモデル:Kimi の API 先行と Flint/Nemotron の重み・ライセンス|2/1|5|5.0|vendor-only・独立再現なし|条件付き本文準備可|
|P2|推論と記憶の基盤:DeepInfer と MemT の機構|2/0|6|6.0|MTP決定性条件の衝突|要修正|
|P3|働くエージェント:Duet の権限境界と 1Password・auto-mode の安全|1/2|4|4.5|vendor-only・独立再現なし|条件付き本文準備可|
|P4|映像の速度を疑う:FLUX 3 Max の数表批判|1/0|3|3.0|測定条件と10.95秒原表欠落|条件付き本文準備可|
|P5|声の様式:Voxtral・Ming・Eleven の合成と認識|1/2|4|4.5|TTS対応言語の一次資料間矛盾|要修正|
|P6|安全の両相:見つけて直す協調開示と先端モデルの学習環境の隔離|2/0|3|4.0|vendor-only・独立再現なし|条件付き本文準備可|
|P7|科学の手続き:生体と低資源言語の評価|2/0|3|4.5|vendor-only・独立再現なし|条件付き本文準備可|
|P8|作る道具:Decisions API と AI toolkit・配布|1/2|3|3.5|価格・比較条件・3.5頁の情報密度|条件付き本文準備可|


**31 item checklist**: SOURCE_SUPPORTEDはfirst-partyがその内容を*記述*したこと、VENDOR_ONLYは独立再現なし、UNRESOLVEDは現行本文では技術断定禁止を意味する。
|Requirement|正規JSONでの記載|技術的評価|修正・Draft条件|
|---|---|---|---|
|P1.1|§1.1 Kimi:API 先行の事実(17:15:24Z・4h44m36s・post ID・$2/$10)と Nov4 FUTURE の区別 — 表:公開状態×時点 [X 原文/supplement 041ec6…/blog]|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P1.2|§1.2 構成の対比:MoE(2.8T/104B は X のみ・blog は 3T 級 / Flint 39.8B/2.5B・49 層・256 experts・SWA-513 / Nemotron 4B 級)と語彙・打切り・64K〜1M — 表:params/active/ctx|UNRESOLVED_OR_UNSUPPORTED|追加: Nemotron総数8B・effective4B, Flint 2.5B算定範囲を注記|
|P1.3|§1.3 文脈長の運用意味:1M / 512K 対応・256K 推奨・262144 設定・64K の区別 — 図:対応/推奨/設定の三層|SOURCE_SUPPORTED|本文で分母・来歴・ライセンス・時点を明示|
|P1.4|§1.4 学習・量子化の手続き(Kimi のサイバー除去と RL / Flint の Eureka 探索と 4bit lm_head / Nemotron のフィルタ)とベンチ(分母・harness・温度・top-p・試行平均)の帰属 — 表:bench×harness×分母|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P1.5|§1.5 重み可用性とライセンス(API live、Nov4 FUTURE、HF 14:20/15:12–19:03、OpenMDW-1.1 は OSI 未検証・Gemma Apache-2.0)と価格・API 条件 — 表:可用性×時刻×約款|SOURCE_SUPPORTED|本文で分母・来歴・ライセンス・時点を明示|
|P2.1|§2.1 DeepInfer の核:FlashMLA/DeepGEMM/DeepEP/TileKernels/DeepSelect/TileLang、注意の DP/均衡 CP、MoE の EP+EPLB、DSpark と確信度予定検証 — 表:核×役割|SOURCE_SUPPORTED|本文で分母・来歴・ライセンス・時点を明示|
|P2.2|§2.2 環境変数の固定(DEEPINFER_ENABLE_MTP_VARLEN=1、DEEPINFER_USE_NEXTN_DECODE 既定 5・0 で無効、9bd9cf24 に固定)と SWA 有界再生(YOCO compact・KEEP140)・非同期・batch-invariant・deterministic sampling — コード抜粋 [environ.py 8738B]|UNRESOLVED_OR_UNSUPPORTED|P1: deterministic samplingにはMTP_VARLEN=0・seq_seed固定・NVIDIA条件|
|P2.3|§2.3 実装条件:SM100+Ascend950・toolchain・1017 checkpoint・4xSM100 prefill+64 decode bench・除外(KV・VE/prefill/decode 分離・cross-DP 均衡)の明示|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P2.4|§2.4 MemT の記憶:Gated DeltaNet-2・Mixture-of-Storage・34B token・二段階+事後、Nano(Qwen3.6-35B-A3B)・Flash(DeepSeek-V4-Flash)、11 bench(Flash 1st/Nano 2nd)、1.86x end-to-end 128K・66x 持続 vs KV cache — 表:bench×分母×条件|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P2.5|§2.5  Paper と README の分離(paper=CC BY-NC-SA・software=PolyForm Noncommercial・第三者 MIT・重み除外、paper に条項なし)と SGLang snapshot・save/restore — 図:ライセンス対応|SOURCE_SUPPORTED|本文で分母・来歴・ライセンス・時点を明示|
|P2.6|§2.6 限界:vendor bench のみ、独立実行・供用試験なし、65 頁の式・ablation 未精読、商用可否の断定なし — DEPTH_LIMITED 注記|SOURCE_SUPPORTED|本文で分母・来歴・ライセンス・時点を明示|
|P3.1|§3.1 待機列・US Pro/Max 先行・共有制限・背景消費と、朝の要点・接続監視・表・予報・web 作成・離席継続・要所確認の振舞い — 表:権限×条件|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P3.2|§3.2 VM・browser、6000+ 目録と実 live の区別、Stripe Link/Shop Pay、1Password coming soon、証券・送金の禁止 — 図:資格の流れ(見ない設計)|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P3.3|§3.3 安全対策の積層(trustworthy-agents、Managed-Agents の秘匿不保持、分類器承認、browser prompt 注入対策、red-team・外部 pen-test・bounty、CC・gov-ID 分類)と 1Password の承認注入(agent は暗証・OTP を見ない)|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P3.4|§3.4 auto-mode の Oct22 更新(8/7 OUT)と翌週 FUTURE・分類器の未検証 — 表:旧/新/未来の三段|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P4.1|§4.1 fal+BFL の post-train(RL・推論最適)と text/image/keyframes・従量、Oct19 IN(Klein Oct15 OUT)|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P4.2|§4.2 速度の再計算(277.80/10.95≈25.37x、277.80/12.45≈22.31x、(277.80-12.45)/277.80×100≈95.52%、頁~22x は正、blog 26.5x/96.2% は同入力で不整合)と最速見出しの禁止 — 表:分母×倍率×出典（分母=新候補の秒数、分子=旧基準 277.80 秒、t_baseline/t_candidate）|NUMERIC_CORRECT_BUT_BENCHMARK_UNVERIFIED|比率の計算は正しい。10.95秒の原表・GPU・ワークロード同一性は未検証|
|P4.3|§4.3 質 Elo 1139(暫定・4868 票、FLUX3 比+47)と価格($0.0425/$0.0725→$0.17/$0.29)・AA 未取得の VENDOR 扱い|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P5.1|§5.1 Voxtral 家族(Small Transcribe 3・Mini 4B・Realtime・Speech 3 TTS・LiveKit 単管・1s 未満・割込み、50+・35+・50+ 言語)と書起こし・diarization・context-biasing(FLEURS WER・cpWER・recall・500ms 未満) — 表:指標×条件|UNRESOLVED_OR_UNSUPPORTED|P1: TTS 35+言語の発表とモデルカード9言語の衝突。対応モードの範囲を分離|
|P5.2|§5.2 TTS 内部評価(Voice Code Bench 300・ pronunciation 300・multilingual 377・expressive 237・gemini-3.8-flash 判定)と価格・EU/US・自己配備・Pro Voice — 判定器の vendor 性を明示|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P5.3|§5.3 Ming の開放(0.5B・7.9B-A1.3B MoE Ling V3、MIT、7 言語+方言、14 tag、9 task)と AA 引用(Controlled Voice・Robustness・Provider Voice、原表未取得)・roadmap 保留・月精度 — 表:AA×原表有無|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P5.4|§5.4 Eleven の realtime 互換(v1 Mini/Max、90+・17k+ voice、Agents・Realtime API・OpenAI 互換・WebSocket)と AA(BBA・TTFA・Full-Duplex・Arena・tool-use、原表未取得)・Pareto・SDK 改修・指南未開封|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P6.1|§6.1 Patch(Oct21 RENDERED_TEXT、bot-wall 9946B のみ):Calif GPT-5.6 Sol、Wiz 独立双方、maintainer 主導、Wiz/Cloudflare、5 段階 validate+fix/advance-notice/政府 SIF-ONCD-CISA+国際/prepare/publish、$1B Daybreak、Codex PHP checker、CVE ゼロ(報告≠証明) — 工程図|SOURCE_SUPPORTED_WITH_RENDERED_ONLY|本文で分母・来歴・ライセンス・時点を明示|
|P6.2|§6.2 Securing(offline・defense in depth、9/20 DNS、数百B red-team、Kata/gVisor/Moby/kernel CVE、10/1 RL 再開、safety gating、頁日付のみ+RSS 10:00Z secondary)と攻撃者有利の留保|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P6.3|§6.3 Oct23 囲い・W42 申立てとの区別と、来歴の保存|SOURCE_SUPPORTED|本文で分母・来歴・ライセンス・時点を明示|
|P7.1|§7.1 Bio(GPT-Rosalind 数千 agent・全脳 CRISPR 数百万細胞 32 分、摂動報告→ atlas、Tsc1/Tsc2・DCTN1、700+ vs 11、盲検 75% 分散選好、bioRxiv/HF/GitHub 来歴、in-loop、wet-lab 未・ZERO 再現) — 表:手順×来歴×限界|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P7.2|§7.2 Low-resource(MultiLangBench SQLite 自作 20 言語・DB 共有・参照 SQLite 照合 Astra 87.4 vs Sol 26.8・COBOL 10.9→72.1 等 19/20≧83%、COBOL hidden byte-parity・Sol 86.6% low・97.9% high、suite 公開≠再現、専門家審査、COBOL 40%・Luna $0.77 vs $3.48、we/our 手続き)と費用・hidden の vendor 保持 — 表:bench×分母×条件|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|
|P7.3|§7.3 盲検・標本・請求の限界と、来歴の保存|SOURCE_SUPPORTED|本文で分母・来歴・ライセンス・時点を明示|
|P8.1|§8.1 Decisions GA Oct22 v1/Luna(beta Oct6 区別、3 型 predicate/choice/score、text/image/JSON、400 問 2x beta、cache、GPT-Live avatar triggers、$0.10/M・cache $0.01・出力無料、US/EU・ZDR、10x vendor、証言 Box/Datadog/Ramp/Sierra/SpeakBox の選択 bias、製品頁未 archive)|SOURCE_SUPPORTED_WITH_COST_QUALIFICATION|キャッシュ書込み費、地域処理上乗せ、長文脈の乗数を補足|
|P8.2|§8.2 TanStack(76 pkgs・23 adapters・8 UI・143 人、harness 0.x 実験、codemod threadId、非 sandbox、製品 Oct22 IN・blog UNRESOLVED 分離)|SOURCE_SUPPORTED_WITH_HARNESS_EXCEPTION|本文で分母・来歴・ライセンス・時点を明示|
|P8.3|§8.3 DeepSeek 1017(V4.1-Flash Sep10、強 bench・高速・短出力、web/app/API、RL 自己 feedback demo、MIT HF/ModelScope・GreenBitAI/Baekpica、Harness v0.2.1-rc.1、CodeBuddy/WorkBuddy、Search/Fetch $0.75/1k・Oct31 16:00 UTC 迄無料、DeepSWE 77 vs 74.2・HLE) — 表:API×移行×約款|VENDOR_ONLY_WITH_EXPLICIT_ATTRIBUTION|本文で分母・来歴・ライセンス・時点を明示|


## 7. Review Attention full 68/68
Review Attentionには優先度フィールドなし。本表末列は独立Solのeditorial triageでありCore原データを書き換えたものではない。
|#|native item_id|段階/区分|原文rationale要約|Sol対応|
|---:|---|---|---|---|
|1|MATERIALITY:w43-background-qwen-20261009:EXCLUDED|MATERIALITY/EXCLUDED|DROP: pre-window Oct 9 Pro/Turbo APIs and weights; secondary Oct 16 listing is not primary; W42-tracked background with no new W43 event.|記録・整理|
|2|MATERIALITY:w43-background-step5-20261015:EXCLUDED|MATERIALITY/EXCLUDED|DROP: open weights Oct 15 OUT of window; Oct 22 SF meetup is community/distribution, not a new model event.|記録・整理|
|3|MATERIALITY:w43-carry-017c9bbc00134ae8:EXCLUDED|MATERIALITY/EXCLUDED|DROP: uncorroborated vendor X-only security allegation; Patch the Planet is a different process, not corroboration; must NOT repeat as fact.|記録・整理|
|4|MATERIALITY:w43-carry-10d76dec5907fe46:EXCLUDED|MATERIALITY/EXCLUDED|DROP: X-only single-poster order claim; no corroborating contract, release or security documentation; Meta shopping signal is separate.|記録・整理|
|5|MATERIALITY:w43-carry-1b1aea9beacefbcd:EXCLUDED|MATERIALITY/EXCLUDED|DROP: 17-author harness paper still not located; AM-Bench and OR-License are different papers and must not be conflated.|記録・整理|
|6|MATERIALITY:w43-carry-2177831df4f20832:EXCLUDED|MATERIALITY/EXCLUDED|DROP: app exists but Qwen3.8-27B name unverified by issuer or weights; Kimi/Qwen-Image do not verify it; name quarantine holds.|記録・整理|
|7|MATERIALITY:w43-carry-2cd2da5b249062c9:EXCLUDED|MATERIALITY/EXCLUDED|DROP: no first-party SMLIB contribution confirmation; Oct 20-23 infra news does not resolve SMLIB status.|記録・整理|
|8|MATERIALITY:w43-carry-517550f1eb0dda9d:EXCLUDED|MATERIALITY/EXCLUDED|DROP: LTX-2.3 video still thin on method/license/eval; FLUX 3 Max is a separate model family, not LTX evidence.|記録・整理|
|9|MATERIALITY:w43-carry-7eb212557bbc5909:EXCLUDED|MATERIALITY/EXCLUDED|DROP: single-vendor Enterprise/Business sample; no representative sample; Oct 21-22 deployment signals are not methodology repair.|記録・整理|
|10|MATERIALITY:w43-carry-800408dab7fcce56:EXCLUDED|MATERIALITY/EXCLUDED|DROP: X-only bot-growth claim with unverified original post; no verified infrastructure metrics or first-party record.|記録・整理|
|11|MATERIALITY:w43-carry-b2ee0e1dffa42188:EXCLUDED|MATERIALITY/EXCLUDED|DROP: Fish Audio Drama 3 still thin on usability/licensing/independent eval; Oct 20 Voxtral/Eleven are separate speech events.|記録・整理|
|12|MATERIALITY:w43-carry-b80ab4ccd3469c31:EXCLUDED|MATERIALITY/EXCLUDED|DROP: W41 HOLD carry with day-only dating and no clock; digest adds no timing; Granite comparison is not fresh Decision-1 evidence.|記録・整理|
|13|MATERIALITY:w43-carry-c3439ff42a96e600:EXCLUDED|MATERIALITY/EXCLUDED|DROP: Le Chonk grounding weights/methods still not open; Voxtral 3 is a different speech/TTS/SDK family and resolves nothing.|記録・整理|
|14|MATERIALITY:w43-lead-gemini-safety-202610:EXCLUDED|MATERIALITY/EXCLUDED|DROP: safety-report lead with locator-level body and unproven exact date; no consumed mechanism or dated in-window event.|記録・整理|
|15|MATERIALITY:w43-r2-out-arc-20261013:EXCLUDED|MATERIALITY/EXCLUDED|DROP: ARC Prize Argon page Oct 13 OUT of window; leaderboard Qwen3.8 row is not issuer proof for the quarantined W42 name; background with reason, never redated.|記録・整理|
|16|MATERIALITY:w43-r2-out-deepinfer-repo-20261016:EXCLUDED|MATERIALITY/EXCLUDED|DROP: repo created Oct 16 07:47Z OUT; Oct 20 X/PyPI announce is the separate IN distribution event; keep distinct, no redating.|記録・整理|
|17|MATERIALITY:w43-r2-out-moss-base-20261016:EXCLUDED|MATERIALITY/EXCLUDED|DROP: Base/SFT code and weights Oct 16 01:18Z OUT; Oct 18 trainer, Oct 19 report-announce and Oct 20 API are separate IN events; keep distinct.|記録・整理|
|18|MATERIALITY:w43-r2-out-orlicense-20261016:EXCLUDED|MATERIALITY/EXCLUDED|DROP: v1 submitted Oct 16 18:13:25Z OUT (only version); background unless a new revision appears.|記録・整理|
|19|MATERIALITY:w43-r3-ambench-v1-out-20261016:EXCLUDED|MATERIALITY/EXCLUDED|DROP: v1 submitted Oct 16 21:46:19Z OUT (13m41s before start); replaces contradictory unknown-clock row; v2 revision row separate.|記録・整理|
|20|MATERIALITY:w43-primary-github-metrics-20261023:NON_MATERIAL|MATERIALITY/NON_MATERIAL|Screening=MAYBE; Edition View=NON_MATERIAL|記録・整理|
|21|MATERIALITY:w43-r4-grok-x-ledger-20261024:NON_MATERIAL|MATERIALITY/NON_MATERIAL|Screening=MAYBE; Edition View=NON_MATERIAL|記録・整理|
|22|SCREENING:w43-background-qwen-20261009:DROP|SCREENING/DROP|DROP: pre-window Oct 9 Pro/Turbo APIs and weights; secondary Oct 16 listing is not primary; W42-tracked background with no new W43 event.|記録・整理|
|23|SCREENING:w43-background-step5-20261015:DROP|SCREENING/DROP|DROP: open weights Oct 15 OUT of window; Oct 22 SF meetup is community/distribution, not a new model event.|記録・整理|
|24|SCREENING:w43-carry-017c9bbc00134ae8:DROP|SCREENING/DROP|DROP: uncorroborated vendor X-only security allegation; Patch the Planet is a different process, not corroboration; must NOT repeat as fact.|記録・整理|
|25|SCREENING:w43-carry-10d76dec5907fe46:DROP|SCREENING/DROP|DROP: X-only single-poster order claim; no corroborating contract, release or security documentation; Meta shopping signal is separate.|記録・整理|
|26|SCREENING:w43-carry-1b1aea9beacefbcd:DROP|SCREENING/DROP|DROP: 17-author harness paper still not located; AM-Bench and OR-License are different papers and must not be conflated.|記録・整理|
|27|SCREENING:w43-carry-2177831df4f20832:DROP|SCREENING/DROP|DROP: app exists but Qwen3.8-27B name unverified by issuer or weights; Kimi/Qwen-Image do not verify it; name quarantine holds.|記録・整理|
|28|SCREENING:w43-carry-2cd2da5b249062c9:DROP|SCREENING/DROP|DROP: no first-party SMLIB contribution confirmation; Oct 20-23 infra news does not resolve SMLIB status.|記録・整理|
|29|SCREENING:w43-carry-517550f1eb0dda9d:DROP|SCREENING/DROP|DROP: LTX-2.3 video still thin on method/license/eval; FLUX 3 Max is a separate model family, not LTX evidence.|記録・整理|
|30|SCREENING:w43-carry-7eb212557bbc5909:DROP|SCREENING/DROP|DROP: single-vendor Enterprise/Business sample; no representative sample; Oct 21-22 deployment signals are not methodology repair.|記録・整理|
|31|SCREENING:w43-carry-800408dab7fcce56:DROP|SCREENING/DROP|DROP: X-only bot-growth claim with unverified original post; no verified infrastructure metrics or first-party record.|記録・整理|
|32|SCREENING:w43-carry-b2ee0e1dffa42188:DROP|SCREENING/DROP|DROP: Fish Audio Drama 3 still thin on usability/licensing/independent eval; Oct 20 Voxtral/Eleven are separate speech events.|記録・整理|
|33|SCREENING:w43-carry-b80ab4ccd3469c31:DROP|SCREENING/DROP|DROP: W41 HOLD carry with day-only dating and no clock; digest adds no timing; Granite comparison is not fresh Decision-1 evidence.|記録・整理|
|34|SCREENING:w43-carry-c3439ff42a96e600:DROP|SCREENING/DROP|DROP: Le Chonk grounding weights/methods still not open; Voxtral 3 is a different speech/TTS/SDK family and resolves nothing.|記録・整理|
|35|SCREENING:w43-lead-gemini-safety-202610:DROP|SCREENING/DROP|DROP: safety-report lead with locator-level body and unproven exact date; no consumed mechanism or dated in-window event.|記録・整理|
|36|SCREENING:w43-r2-out-arc-20261013:DROP|SCREENING/DROP|DROP: ARC Prize Argon page Oct 13 OUT of window; leaderboard Qwen3.8 row is not issuer proof for the quarantined W42 name; background with reason, never redated.|記録・整理|
|37|SCREENING:w43-r2-out-deepinfer-repo-20261016:DROP|SCREENING/DROP|DROP: repo created Oct 16 07:47Z OUT; Oct 20 X/PyPI announce is the separate IN distribution event; keep distinct, no redating.|記録・整理|
|38|SCREENING:w43-r2-out-moss-base-20261016:DROP|SCREENING/DROP|DROP: Base/SFT code and weights Oct 16 01:18Z OUT; Oct 18 trainer, Oct 19 report-announce and Oct 20 API are separate IN events; keep distinct.|記録・整理|
|39|SCREENING:w43-r2-out-orlicense-20261016:DROP|SCREENING/DROP|DROP: v1 submitted Oct 16 18:13:25Z OUT (only version); background unless a new revision appears.|記録・整理|
|40|SCREENING:w43-r3-ambench-v1-out-20261016:DROP|SCREENING/DROP|DROP: v1 submitted Oct 16 21:46:19Z OUT (13m41s before start); replaces contradictory unknown-clock row; v2 revision row separate.|記録・整理|
|41|SCREENING:w43-primary-automode-20261021:INSPECT|SCREENING/INSPECT|INSPECT: X-level locator only for auto-mode default on Pro/Max/Team; no official changelog or docs body pinned; classifier-gating claim unverified.|高優先再確認|
|42|SCREENING:w43-primary-decisions-api-20261022:INSPECT|SCREENING/INSPECT|INSPECT: RSS-title-level product signal only; speed/cost claims with no specs, pricing, limits or docs body consumed.|高優先再確認|
|43|SCREENING:w43-primary-openai-cloud-20261021:INSPECT|SCREENING/INSPECT|INSPECT: RSS-level deployment signal (frontier models plus Codex in Gemini Model Garden via GCP Marketplace); no page bodies; distribution, not a new model.|高優先再確認|
|44|SCREENING:w43-primary-patch-planet-20261021:INSPECT|SCREENING/INSPECT|INSPECT: RSS-level vuln-coordination process signal; distinct from Duet safety and from any incident fact; no page body or disclosed-CVE proof consumed.|高優先再確認|
|45|SCREENING:w43-carry-7151fcdc6c3ee392:MAYBE|SCREENING/MAYBE|MAYBE: no causal benchmark for gzip/TTFT claim, but W43 GitHub perf-adjacent changelogs keep the lane warm; supporting mention at most, never standalone.|記録・整理|
|46|SCREENING:w43-lead-muse-10m-20261021:MAYBE|SCREENING/MAYBE|MAYBE: Q3 earnings 10M Muse plus shopping-top-activity is industry signal, not a technical release; context with sample/bias disclosure at most.|記録・整理|
|47|SCREENING:w43-lead-oracle-revision-20261021:MAYBE|SCREENING/MAYBE|MAYBE: v2 corrects oracle failures (4194 to 2883 replay, 94.3 to 65.5 percent) as methodology caution; v1 Oct 12 OUT; v2 is a correction signal, not a new capability|記録・整理|
|48|SCREENING:w43-primary-github-deprecation-20261019:MAYBE|SCREENING/MAYBE|MAYBE: Oct 19 model deprecations across Chat/inline/agent/completions; availability boundary with unpinned model list; metering context at most.|記録・整理|
|49|SCREENING:w43-primary-github-metrics-20261023:MAYBE|SCREENING/MAYBE|MAYBE: usage metrics API now captures OpenCode and others via totals_by_client; metering change, not a model; additive scope.|記録・整理|
|50|SCREENING:w43-primary-github-teams-20261023:MAYBE|SCREENING/MAYBE|MAYBE: Teams notifications to Copilot issue-to-PR flow Oct 23 (reproduce, test, fix, PR); changelog-level only; legacy app retires Nov 16; product flow, not a model.|記録・整理|
|51|SCREENING:w43-r2-ambench-v2-20261020:MAYBE|SCREENING/MAYBE|MAYBE: v2 Oct 20 IN as revision event only; substantive delta vs v1 unchecked; must not promote v1 OUT original into a W43 research claim.|記録・整理|
|52|SCREENING:w43-r2-moss-api-20261020:MAYBE|SCREENING/MAYBE|MAYBE: MOSI API Platform availability Oct 20 per README News; availability signal distinct from Oct 16 OUT code/weights; platform terms and coverage unvalidated.|記録・整理|
|53|SCREENING:w43-r2-moss-report-announce-20261019:MAYBE|SCREENING/MAYBE|MAYBE: Oct 19 README announcement of report 2610.23374 is distribution, not new research (submission Oct 16 OUT); no redating of the original.|記録・整理|
|54|SCREENING:w43-r4-grok-x-ledger-20261024:MAYBE|SCREENING/MAYBE|MAYBE: PARTIAL Grok sensor ledger (13425B, SHA 4571e0de, observed 12:43:17Z); binds exact Grok Raw for manifest X integration; audit and provenance binder, NOT a tec|記録・整理|
|55|SCREENING:w43-support-vercel-ollama-20261017:MAYBE|SCREENING/MAYBE|MAYBE: Vercel Gateway, Ollama and Unsloth same-week entries are distribution proof only (V4.1-1017 snapshot, Bolt E4B blobs, 0.1.910-beta); versions need pinning; no|記録・整理|
|56|SELECTION:candidate:2026-W43:b26dfd2c2e5ac943:HOLD|SELECTION/HOLD|HOLD: third-party KohakuMossTrainer Oct18 IN (base Oct16 OUT distinct): streamed full finetune RTX5090 36864×GRAD_ACC8 (294912 tok/step) 117.7s/step vs 8.8s micro-ba|要Human審査|
|57|SELECTION:candidate:2026-W43:0851e82f8db3889f:REJECT|SELECTION/REJECT|REJECT as model story: distribution via private preview (not a new model): Astra/Sol/Luna via Model Garden/Marketplace, single invoice/commitments, perimeters; ZDR/C|要Human審査|
|58|SELECTION:candidate:2026-W43:11123030a87c7b84:REJECT|SELECTION/REJECT|REJECT: API README News line as IN mention only; live deployment proof unknown (README ≠ deployment). CONTEXT mention, no article. [MAYBE; CONTEXT]|要Human審査|
|59|SELECTION:candidate:2026-W43:1d7d93a70eeabd2b:REJECT|SELECTION/REJECT|REJECT as new research: v2 revision event only (v1 Oct12 OUT); substantive v1→v2 delta UNRESOLVED (38pp + eval/ablation not line-read). CONTEXT bibliography, never p|要Human審査|
|60|SELECTION:candidate:2026-W43:1fc486ce9ce010e3:REJECT|SELECTION/REJECT|REJECT as new research: v2 revision only (v1 Oct16 OUT 13m41s before window); substantive delta UNRESOLVED. CONTEXT bibliography. [MAYBE; CONTEXT]|要Human審査|
|61|SELECTION:candidate:2026-W43:55f087dd70eb920c:REJECT|SELECTION/REJECT|REJECT: audit sensor binder, NEVER story/article nor corroboration. Registration COMPLETE / sensor PARTIAL (2 pinned IDs); 7 projections SOCIAL/SECONDARY, no primary|要Human審査|
|62|SELECTION:candidate:2026-W43:642c261d5e82c786:REJECT|SELECTION/REJECT|REJECT from W43 story: official publication 23:42:03Z is 1h42m03s AFTER exclusive cutoff; POST_CUTOFF/NON_MATERIAL. Technical facts preserved as PARTIAL Evidence (en|要Human審査|
|63|SELECTION:candidate:2026-W43:692a004fb38c5539:REJECT|SELECTION/REJECT|REJECT: X-only gzip support signal, no causal measurement; CONTEXT support only, no article depth. [MAYBE; CONTEXT]|要Human審査|
|64|SELECTION:candidate:2026-W43:6dea52dc41201570:REJECT|SELECTION/REJECT|REJECT as unified story: composite Oct17 Vercel/DeepSeek gateway + Oct23 Bolt/Ollama/Unsloth (15:26:53Z) under one day-precision event; no unified timestamp; version|要Human審査|
|65|SELECTION:candidate:2026-W43:9281a9c6770f46d5:REJECT|SELECTION/REJECT|REJECT as W43 story: secondary-reported 10M users + shopping activity only; no primary books/population disclosed. CONTEXT adoption signal at most; thin for article.|要Human審査|
|66|SELECTION:candidate:2026-W43:b87e32087dcd83a7:REJECT|SELECTION/REJECT|REJECT as new research: Oct19 announcement of Oct16 OUT body; v1→v2 delta if any unchecked. CONTEXT bibliography. [MAYBE; CONTEXT]|要Human審査|
|67|SELECTION:candidate:2026-W43:e4b1869996b82b4a:REJECT|SELECTION/REJECT|REJECT from narrative despite IN 21:29:58Z (30m02s inside): changelog-level Teams notifications-to-code only (reproduce/test/fix/PR; legacy app retires Nov16); produ|要Human審査|
|68|SELECTION:candidate:2026-W43:ff78deda46feb19e:REJECT|SELECTION/REJECT|REJECT: model deprecation + migration changelog-level only; ops hygiene, no article depth. Model list/migration path noted. [MAYBE; CONTEXT]|要Human審査|


## 8. Original 19 DROP reconciled
|#|Discovery ID|理由|結論|
|---:|---|---|---|
|1|w43-background-qwen-20261009|DROP: pre-window Oct 9 Pro/Turbo APIs and weights; secondary Oct 16 listing is not primary; W42-tracked background with no new W43 event.|除外維持|
|2|w43-background-step5-20261015|DROP: open weights Oct 15 OUT of window; Oct 22 SF meetup is community/distribution, not a new model event.|除外維持|
|3|w43-carry-017c9bbc00134ae8|DROP: uncorroborated vendor X-only security allegation; Patch the Planet is a different process, not corroboration; must NOT repeat as fact.|除外維持|
|4|w43-carry-10d76dec5907fe46|DROP: X-only single-poster order claim; no corroborating contract, release or security documentation; Meta shopping signal is separate.|除外維持|
|5|w43-carry-1b1aea9beacefbcd|DROP: 17-author harness paper still not located; AM-Bench and OR-License are different papers and must not be conflated.|除外維持|
|6|w43-carry-2177831df4f20832|DROP: app exists but Qwen3.8-27B name unverified by issuer or weights; Kimi/Qwen-Image do not verify it; name quarantine holds.|除外維持|
|7|w43-carry-2cd2da5b249062c9|DROP: no first-party SMLIB contribution confirmation; Oct 20-23 infra news does not resolve SMLIB status.|除外維持|
|8|w43-carry-517550f1eb0dda9d|DROP: LTX-2.3 video still thin on method/license/eval; FLUX 3 Max is a separate model family, not LTX evidence.|除外維持|
|9|w43-carry-7eb212557bbc5909|DROP: single-vendor Enterprise/Business sample; no representative sample; Oct 21-22 deployment signals are not methodology repair.|除外維持|
|10|w43-carry-800408dab7fcce56|DROP: X-only bot-growth claim with unverified original post; no verified infrastructure metrics or first-party record.|除外維持|
|11|w43-carry-b2ee0e1dffa42188|DROP: Fish Audio Drama 3 still thin on usability/licensing/independent eval; Oct 20 Voxtral/Eleven are separate speech events.|除外維持|
|12|w43-carry-b80ab4ccd3469c31|DROP: W41 HOLD carry with day-only dating and no clock; digest adds no timing; Granite comparison is not fresh Decision-1 evidence.|除外維持|
|13|w43-carry-c3439ff42a96e600|DROP: Le Chonk grounding weights/methods still not open; Voxtral 3 is a different speech/TTS/SDK family and resolves nothing.|除外維持|
|14|w43-lead-gemini-safety-202610|DROP: safety-report lead with locator-level body and unproven exact date; no consumed mechanism or dated in-window event.|除外維持|
|15|w43-r2-out-arc-20261013|DROP: ARC Prize Argon page Oct 13 OUT of window; leaderboard Qwen3.8 row is not issuer proof for the quarantined W42 name; background with reason, never redated.|除外維持|
|16|w43-r2-out-deepinfer-repo-20261016|DROP: repo created Oct 16 07:47Z OUT; Oct 20 X/PyPI announce is the separate IN distribution event; keep distinct, no redating.|除外維持|
|17|w43-r2-out-moss-base-20261016|DROP: Base/SFT code and weights Oct 16 01:18Z OUT; Oct 18 trainer, Oct 19 report-announce and Oct 20 API are separate IN events; keep distinct.|除外維持|
|18|w43-r2-out-orlicense-20261016|DROP: v1 submitted Oct 16 18:13:25Z OUT (only version); background unless a new revision appears.|除外維持|
|19|w43-r3-ambench-v1-out-20261016|DROP: v1 submitted Oct 16 21:46:19Z OUT (13m41s before start); replaces contradictory unknown-clock row; v2 revision row separate.|除外維持|


### W42 carry (12)
|#|Carry ID|Screening|Selection|理由|
|---:|---|---|---|---|
|1|w43-carry-017c9bbc00134ae8|DROP|Matrix対象外|DROP: uncorroborated vendor X-only security allegation; Patch the Planet is a different process, not corroboration; must NOT repeat as fact.|
|2|w43-carry-10d76dec5907fe46|DROP|Matrix対象外|DROP: X-only single-poster order claim; no corroborating contract, release or security documentation; Meta shopping signal is separate.|
|3|w43-carry-1b1aea9beacefbcd|DROP|Matrix対象外|DROP: 17-author harness paper still not located; AM-Bench and OR-License are different papers and must not be conflated.|
|4|w43-carry-2177831df4f20832|DROP|Matrix対象外|DROP: app exists but Qwen3.8-27B name unverified by issuer or weights; Kimi/Qwen-Image do not verify it; name quarantine holds.|
|5|w43-carry-2cd2da5b249062c9|DROP|Matrix対象外|DROP: no first-party SMLIB contribution confirmation; Oct 20-23 infra news does not resolve SMLIB status.|
|6|w43-carry-517550f1eb0dda9d|DROP|Matrix対象外|DROP: LTX-2.3 video still thin on method/license/eval; FLUX 3 Max is a separate model family, not LTX evidence.|
|7|w43-carry-7151fcdc6c3ee392|MAYBE|REJECT|MAYBE: no causal benchmark for gzip/TTFT claim, but W43 GitHub perf-adjacent changelogs keep the lane warm; supporting mention at most, never standalo|
|8|w43-carry-7eb212557bbc5909|DROP|Matrix対象外|DROP: single-vendor Enterprise/Business sample; no representative sample; Oct 21-22 deployment signals are not methodology repair.|
|9|w43-carry-800408dab7fcce56|DROP|Matrix対象外|DROP: X-only bot-growth claim with unverified original post; no verified infrastructure metrics or first-party record.|
|10|w43-carry-b2ee0e1dffa42188|DROP|Matrix対象外|DROP: Fish Audio Drama 3 still thin on usability/licensing/independent eval; Oct 20 Voxtral/Eleven are separate speech events.|
|11|w43-carry-b80ab4ccd3469c31|DROP|Matrix対象外|DROP: W41 HOLD carry with day-only dating and no clock; digest adds no timing; Granite comparison is not fresh Decision-1 evidence.|
|12|w43-carry-c3439ff42a96e600|DROP|Matrix対象外|DROP: Le Chonk grounding weights/methods still not open; Voxtral 3 is a different speech/TTS/SDK family and resolves nothing.|
W42 carry は多数がDROP、行外例外はCONTEXT/REJECT。carry由来の未確認名称、未確認安全断定、source窓外研究を「W43確定ニュース」へ昇格させない。


## 9. 25 supplement sources / authority inventory
Supplement25は原source-to-claim map全量ではなく、r4補完出典レコード。GitHub等のページは観測日と文書公開時刻が必ずしも等しくない。
|#|Supplement ID|source class|published timestamp|locator|raw SHA256 prefix|
|---:|---|---|---|---|---|
|1|supplement-src-0226e32d4252d42c|PRIMARY_PAPER|2026-10-21T04:47:46Z|paper:arxiv.org/abs/2610.16067|8d8ef345301cd7b4|
|2|supplement-src-6f18c05b01b43f45|PRIMARY_OFFICIAL|日付/時刻不明|https://claude.com/resources/articles/auto-mode-default-in-claude-code|8ed45487ed320dbd|
|3|supplement-src-2a49a7d4f6f2ae5a|PRIMARY_OFFICIAL|日付/時刻不明|https://developers.openai.com/api/docs/changelog|ea48630a81d9a540|
|4|supplement-src-e20f1cffc1444d3a|PRIMARY_REPOSITORY|2026-10-21T04:55:43Z|https://github.com/deepseek-ai/DeepInfer/blob/main/deepinfer/environ.py|fe2c531989c419f0|
|5|supplement-src-d0805b13331ce793|PRIMARY_REPOSITORY|2026-10-21T04:55:43Z|https://github.com/deepseek-ai/DeepInfer/blob/main/README.md|b55624158ada4dc2|
|6|supplement-src-d818147e4521ac7a|PRIMARY_REPOSITORY|2026-10-21T04:55:43Z|https://github.com/deepseek-ai/DeepInfer/blob/main/LICENSE|c71d239df91726fc|
|7|supplement-src-1ae0efcded48b6e4|PRIMARY_OFFICIAL|日付/時刻不明|https://fal.ai/flux-3-max|9e8ddfd658d0f8e5|
|8|supplement-src-32e30026645a68d3|PRIMARY_OFFICIAL|日付/時刻不明|https://fal.ai/blog/introducing-flux-3-max-by-fal|50ac7df999673e27|
|9|supplement-src-1a8d33ae41ab22ad|PRIMARY_OFFICIAL|2026-10-23T23:42:03Z|https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode|be7faba3e913c52e|
|10|supplement-src-52dba048e55beefa|PRIMARY_OFFICIAL|2026-10-23T21:29:58Z|https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams|d0a38eac3f3f11fc|
|11|supplement-src-041ec6c5600beb4d|PRIMARY_OFFICIAL|日付/時刻不明|https://www.kimi.ai/blog/kimi-k3-1-pro|86cc8bbeaa22aeec|
|12|supplement-src-9e10348cb212038f|PRIMARY_REPOSITORY|日付/時刻不明|https://huggingface.co/nvidia/Nemotron-3.5-Bolt-E4B-4GB|8a06cc67a204a173|
|13|supplement-src-deae3d33c374f4eb|PRIMARY_REPOSITORY|2026-10-23T15:12:12Z|https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/commits/main|09fcdd58ed329ef6|
|14|supplement-src-ea58a61c3678ad4a|PRIMARY_OFFICIAL|日付/時刻不明|https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers|d77a629158ed49e1|
|15|supplement-src-fe148ca1b75a67dd|PRIMARY_OFFICIAL|日付/時刻不明|https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/|f70ef5b35513aa27|
|16|supplement-src-22fcccb239a19447|PRIMARY_REPOSITORY|2026-10-22T15:18:14Z|https://api.github.com/repos/TanStack/ai/releases/tags/%40tanstack%2Fai%401.0.0|0ab83c0d7bcf3f42|
|17|supplement-src-b06a31536a4f162a|PRIMARY_PAPER|2026-10-20T15:40:19Z|paper:arxiv.org/abs/2610.24264|fc3b7f964b21099e|
|18|supplement-src-927931f4a303eaa6|PRIMARY_PAPER|日付/時刻不明|paper:arxiv.org/abs/2610.26825|959206da6621d9ba|
|19|supplement-src-baee90a6382ccdbd|PRIMARY_REPOSITORY|2026-10-20T08:42:18Z|https://github.com/MemTensor/MemT-1.0/blob/main/README.md|5d576f44316398f8|
|20|supplement-src-1d329e6cfb492783|PRIMARY_REPOSITORY|2026-10-21T11:03:57Z|https://github.com/inclusionAI/Ming-3.0-tts/blob/main/README.md|6931f3bd024c4e17|
|21|supplement-src-5bb55c72ae60d4a2|PRIMARY_REPOSITORY|2026-10-21T11:03:57Z|https://github.com/inclusionAI/Ming-3.0-tts/blob/main/LICENSE|2872f1918dfc04fd|
|22|supplement-src-b751c2c90f23c12a|PRIMARY_REPOSITORY|2026-10-20T18:30:30Z|https://github.com/KohakuBlueleaf/KohakuMossTrainer/blob/main/LICENSE|2e63789e1bd0f581|
|23|supplement-src-7648a293320fac45|PRIMARY_OFFICIAL|2026-10-23T10:00:00Z|https://openai.com/news/rss.xml|6ab1e0ffee12b966|
|24|supplement-src-d2d2f48e181fb4dd|PRIMARY_OFFICIAL|日付/時刻不明|https://recursive.com/updates/introducing-recursive-flint|ce42b796c43e695e|
|25|supplement-src-e1fe975d225aaa88|PRIMARY_REPOSITORY|日付/時刻不明|https://huggingface.co/RecursiveSI/flint|43244381065d603b|
**Reader bibliography:** `src-1`はEvidence Task内ローカル参照なので他Taskと混同禁止。各claimをTask ID → source ID → supplement source ID(if present) → immutable raw_path/SHA → 公式URL の順に接続。PRIMARY_REPOSITORYは実コードの根拠になってもベンダーbenchの独立再現証明にはならない。Kimi Xや原AA未取得は型を正しく表記。


## 10. Numeric/source checks and timeline
|数値・計算|分子 / 分母・条件|本監査評価|
|---|---|---|
|P1 Kimi 2.8T /104B|ベンダーXのtotal/active。3Tは概数blog|VENDOR_ONLY、Nov4重み未配布|
|P1 Flint 39.8B/2.5B|total / active(出力head含む)|SOURCE_SUPPORTED、他モデルと算定差|
|P1 Nemotron 8B/4B|total / effective|SOURCE_SUPPORTED、OpenMDW license|
|P2 MemT 1.86x/66x|end-to-end 128K / persistent storage対KV、異なる分母|VENDOR_ONLY、同一速度の2指標ではない|
|P2 DeepInfer nextn=5|env default、0 disabled|SOURCE_SUPPORTED、deterministic mode構成分離必須|
|P4 277.80 / 10.95|baseline秒 / target秒|25.37x、算術PASS、10.95s origin未取得|
|P4 277.80 / 12.45|baseline秒 / target秒|22.31x、算術PASS、blog 26.5xと矛盾|
|P4 (277.80-12.45)/277.80|秒 / 秒|95.52% time saving、blog 96.2%と矛盾|
|P4 price 0.0425*4、0.0725*4|$/unitを4倍|0.17,0.29 計算だけPASS。単位・尺・課金対象に注意|
|P5 Voxtral TTS 35+ vs9|発表記事vsモデルカード|SOURCE_CONFLICT、断定禁止|
|P5 Voice Code Bench 300等|vendor sampled prompts + chosen judge|VENDOR_ONLY、独立judgeではない|
|P6 Oct1 resumed vs Oct23 public|実施日vs発表日|SOURCE_SUPPORTED vendor story|
|P7 700+ vs11 /75%|内部研究・盲検・異種標本|VENDOR_ONLY、wet-lab追証なし|
|P7 19/20・86.6/97.9%|内部benchmark / hidden-test|VENDOR_ONLY、分母と環境を記事に明示|
|P8 Decisions 400|questions per API request|SOURCE_SUPPORTED、rate limitではない|
|P8 $0.10/M, $0.01/M|input /cached hit; output token fee 0|BASE_PRICING_ONLY、cache write/地域追加料金あり|
|P8 TanStack 76/23/8/143|publisher monorepo count|SOURCE_SUPPORTED_BY_VENDOR、harness experimental|
|P8 DeepSeek $0.75/1000 calls|Search/Fetch each endpoint、限定free期間|SOURCE_SUPPORTED_BY_VENDOR、token価格ではない|
|Page plan P1..P8|5+6+4.5+3+4.5+4+4.5+3.5=35, plus2=37|算術PASS、target38/max44 非拘束見積|


W43 UTC cutoff **[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)**、右開区間。
|Event|Time/Window|本監査扱い|
|---|---|---|
|DeepInfer repo creation|Oct16 07:47Z OUT|Oct20公開/告知と分離|
|MOSS Base source|Oct16 01:18Z OUT|Oct18 Trainer/Oct20 APIと分離|
|AM-Bench v1|Oct16 21:46:19Z OUT|v2 INはrevisionのみ|
|Kimi announced|Oct23 17:15:24Z IN|API先行、weights Nov4 FUTURE|
|TanStack 1.0 release|Oct22 15:18:14Z IN|blog Oct23 day-onlyから独立|
|GitHub Teams|Oct23 21:29:58Z IN|薄いCONTEXT / REJECT合理的|
|GitHub Metrics|Oct23 23:42:03Z OUT|W44 pointer only、W43非採用|
|OpenAI containment|Oct23 day-level IN|RSS 10:00ZはRSS metadata、記事本文の時計ではない|
|1Password Duet integration|coming soon as of cutoff|live扱い禁止|


## 11. Historical integrity and validation
r2 archive `execution/history/selection-architecture-r2/` と現r3をGitHubから再取得し、JSON structural diffを独立検査:
- `candidate-matrix-v2.json` and `candidate-selection-v2.json` **byte identical**。
- `architecture-v2.json` は `#/packages/3/must_cover_requirements/1` **1項目のみ変更**。修正後分子/分母が正しく並ぶ。
- `architecture-review-summary-v2.json` は `#/basis/architecture_sha256` **1項目のみ変更**。
- `architecture-review-attention-v2.json` **byte identical**。全68 unique、truncated=false。
- Interactive input/auditにもr3版が存在し、Audit SHA256宣言の整合は記録。ただし本Solの全5 SHA256独立再計算 **NOT_EXECUTED**。
- 以前の独立Sol SA-001〜SA-006は主なタイトル/翻訳/紙幅/attention全量の改善が反映。SA-007 FLUX逆数はr3修正済み。ISA-001,002,003,005,006は新規の技術/編集リスク。
- ネイティブvalidatorをこの独立接続環境で実行していない。r3原レポートのPASSは独立再実行結果ではない。r1/r2履歴保存と親子関係の存在は確認、別途全archiveの生byte rehashまでは行っていない。


## 12. One consolidated repair recommendation (Museへ直接発注しない)
1. 既存ブランチ・HEAD exactを作業開始時に再照合する。drift時STOP。Frozen Core v2/read-only main不可変。Stage/Human Gate維持。
2. **Architecture r4** としてISA-001/002を優先修正、ISA-003/005/006を可能な範囲で同じ一括修正に統合。ISA-004/007/008/009はDraft禁止事項とHuman packetへ明文化。これ以上単発反復は避ける。
3. Candidate Matrix32・Selection32・採用19・8 packages・19 placementsは基本不変。ただしP1事実が採用理由自体を壊す新sourceが出た場合は監査停止して人に再選定要否を委ねる。
4. Edition-local input→frozen native runner→Architecture canonical→Summary/Attention/input/audit を同一系統で整合再生成。previous r3 proposed authorityは履歴snapshot+SHAで保存。r3/ r4差分を説明。全5 SHA256 を別実装で再計算、native validators真正PASS、accepted r4 Evidence/Views binding及び17+11+4/19 Screening再照合。**scratch precheckを本Stage移行済みと誤称しない**。
5. 人間向けレビューの先頭にP1二件、selected technical provenance表、残余5 LIMITED、保留1、IN/OUT/FUTURE、ページ見積を集約。68 attentionは原件のまま維持し、重要な新問題を追加reader-facing packetで示す。
6. 改訂後も編纂統括SolがSelectionおよびArchitectureを**別判定**。P1が残ればBridge2段ともNO。PASSと判断して初めて順番に信頼されたstage transitionを検討し、真のPENDING Human Architecture Gateで停止。今回の独立Solはどちらも実行しない。


## 13. Human decision packet（承認ではない）
8本の軸は (P1) 可用性/モデル (P2) 推論/記憶 (P3) エージェント権限 (P4) 動画の実測条件 (P5) 音声 (P6) 協調開示/隔離 (P7) 科学的評価 (P8) 開発API。選定外13件はHOLD1+REJECT12、内訳はMATERIAL1、CONTEXT10、NON_MATERIAL2。19 DROPは受入前除外で32候補とは別集合。
承認者が実際に承認すべき内容: (i) ISSUE時刻とfuture boundary、(ii) ソース帰属の不確実性、(iii) P2/P5の新P1解消、(iv) 約37頁計画（38目標/44上限は固定保証ではない）、(v) 部分検証・ベンダー実験・独立再現の表示ルール。具体的原稿が希薄なら記事を短縮し、架空の技術説明で埋めない。


## 14. Consulted external primary URLs (live checks, not all historical raw rehashed)
- Moonshot: https://www.kimi.ai/blog/kimi-k3-1-pro
- DeepInfer pinned/source: https://github.com/deepseek-ai/DeepInfer
- Flint model card: https://huggingface.co/RecursiveSI/flint
- Nemotron BF16 model card: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16
- Nemotron 4GB model card: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
- FLUX 3 Max: https://fal.ai/blog/introducing-flux-3-max-by-fal
- Claude Duet: https://claude.com/resources/articles/claude-duet
- 1Password Agents: https://1password.com/blog/1password-for-ai-agents
- Mistral Voxtral 3 announcement: https://mistral.ai/news/voxtral-3/
- Mistral Voxtral TTS 3 model card: https://docs.mistral.ai/models/voxtral-mini-tts-3-0
- Mistral audio language matrix: https://docs.mistral.ai/studio/audio/specs-and-limits/languages
- Mistral changelog: https://docs.mistral.ai/resources/changelogs
- OpenAI Patch: https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
- OpenAI containment: https://openai.com/index/securing-our-frontier-model-training-environment/
- OpenAI Decisions: https://openai.com/index/decisions-api/
- OpenAI Decisions guide: https://developers.openai.com/api/docs/guides/decisions
- TanStack AI 1.0: https://tanstack.com/blog/tanstack-ai-1-0
- DeepSeek Flash 1017: https://api-docs.deepseek.com/news/news261017/


---
**停止地点:** `INDEPENDENT_SOL_W43_SELECTION_ARCHITECTURE_R3_COMPREHENSIVE_AUDIT_COMPLETE`（候補/要件/Attention全件の構造監査完了。上記の独立ベンチ再現・全byte rehashは未実施という限定あり）
