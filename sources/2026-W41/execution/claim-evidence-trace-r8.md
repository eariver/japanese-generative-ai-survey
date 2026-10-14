# W41 Claim–Evidence traceability matrix r8 (Repair R7-03)

Status: `EDITION_LOCAL / AUDIT_MATRIX / NON_SCHEMA`
Date: 2026-10-12 JST
Sources of truth: accepted Cards under `evidence/v2/accepted/717ea04a…/results/`,
Matrix `candidate-matrix-v2.json` (`0d56de2b…`), Architecture `architecture-v2.json`
(`3554041e…`, P1–P6). Claim/source IDs below are verbatim from Cards; no IDs or
experimental content invented. Full claim texts live in Cards (abbreviated here).

Global classification note: **independently reproduced = 0 rows in this issue**.
Every numeric is either Publisher claim (vendor-measured, first-party stated) or
unresolved (not on page / unfetched). Column `母集団/比較/方法` records whether the
denominator, comparator and method are known from consumed sources.

凡例: Pkg＝配置先 / Cand＝candidate末尾12桁 / Task＝evidence task末尾12桁 /
区分＝Publisher claim｜unresolved（本号にindependently reproducedは0件）.

## P1 — Frontier rollout week

| Pkg | Cand / Task | Claim | Source＋消費範囲 | 技術主張・数値 | 母集団/比較/方法 | 区分 | Draft日本語＋必須留保 |
|---|---|---|---|---|---|---|---|
| P1 | `e82f6c680a8d3099` / `5ca8cd2c65ec98d8` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL rollout page (delegated verbatim) | GPT-6＋Intelligent UI：10/7有料 tiers（Chat tab）、10/8 Free/Go、Sol＝有料・Luna＝Free/Go | 日付・tier・tab・割当は既知 | Publisher claim | 「10月7日に有料プラン向け、8日に無料プラン向け提供」＋留保「料金・system-card数値は本ページにない」 |
| P1 | 同上 claim-2 [VENDOR_CLAIM] | src-1 同上 | 44% sooner answering（GPT-6 Instant vs 5.6 Instant、web検索質問）は交錯思考/回答による回答開始短縮で、最終回答のwall-time短縮ではない | 母集団＝web検索質問サブセット、比較＝5.6 Instant、方法＝開始遅延計測 | Publisher claim | 「回答開始が44%早期化（ベンダー計測）」＋留保「最終回答時間の短縮を示す数値はない」 |
| P1 | `4690400bcb127ce7` / `c880db78235eeef3` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL release page (delegated) | Haiku 5.5：10万境スプリット料金、cache-read $0.01/$0.05、Sonnet 5.5 cache-read半額 $0.20→$0.10 | 料金表として既知 | Publisher claim | 料金表を逐語＋留保「system-card全評価は未取得」 |
| P1 | 同上 claim-2 [VENDOR_CLAIM] | src-1 同上 | ベンチ表 GDPval 1620、OSWorld2.1 72.4%、HLE 45.9/57.4、TB4 39.2% | 比較・方法＝発行者計測のみ | Publisher claim | 数表＋留保「発行者計測、独立再現待ち」 |

## P2 — Agent and Decisions infrastructure

| Pkg | Cand / Task | Claim | Source＋消費範囲 | 技術主張・数値 | 母集団/比較/方法 | 区分 | Draft日本語＋必須留保 |
|---|---|---|---|---|---|---|---|
| P2 | `02f4ba5be618d07c` / `9719a94be83e645f` claim-1 [PRIMARY_FACT] | src-1 changelog＋supplement-src-df537ff932f91343  bounded excerpt（Muse DIRECT_READ相当の逐語確認） | Decisions API beta（gpt-6-luna、`v1/decisions`）、Responses API比10x高速（ベンダー主張） | エントリ文言は既知、10xの方法論は不明 | 一部 unresolved（10x方法論・料金ページ未取得。r2 community $0.10/Mはchangelog外） | 「changelogにbeta記載（逐語）」＋留保「10xの測定方法は本ページになく、料金は未確認」 |
| P2 | `af9f304cf7534a4d` / `25abdeecf0872e56` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL issuer forum 10/6 21:11Z (delegated) | open-weights multimodal decision model更新、HF Decision Index 0.3 top、$0.02/M input（v1半額） | 母集団・方法＝不明（README未取得） | Publisher claim | フォーラム日付・価格・Indexを伝聞形＋留保「HF README・ライセンス・repo URL未確認」 |
| P2 | 同上 claim-2 [VENDOR_CLAIM] | src-1 同上 | Decision Bench 10/9：94.5%／1071 cases、$0.017/1k decisions（ベンダー） | 母集団＝1071 cases既知、方法＝不明 | Publisher claim | 同上＋留保「ベンチ運営主体・再現なし」 |
| P2 | `f735bdb6864637a0` / `cc453f1da5f006f9` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL issuer forum 10/7 16:30Z (delegated) | late-interaction embedding 2種、frontier、HF-public | 仕様・母集団・方法＝不明 | unresolved（発表事実のみ既知） | 一行言及のみ＋留保「仕様・repo path未確認、単独記事化不可」 |
| P2 | `4d4f3d1498ba6929` / `7fe2d805045a8e79` claim-1 [PRIMARY_FACT] | src-1 changelog＋supplement-src-ec5b609a5f24671e bounded excerpt | service_tier ultrafast（gpt-6.1-sol、Responses API）、全user＋rate limits、global＋US/EU residency | 適用範囲として既知 | VERIFIED相当の事実（料金はlink先のみ、遅延数値なし→一部 unresolved） | 「tier・対象・residencyを表に」＋留保「遅延の実測値は本ページにない」 |
| P2 | 同上 claim-2 [PRIMARY_FACT] | 同上 | 目的はtoken間遅延の短縮（wall-time区別維持） | 定義として既知 | 同上 | 同上 |
| P2 | `2c55480d86af19a4` / `9fdd36169d2efaf7` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL stub (delegated) | Gemini at Work 2026で汎用work agent発表（prompt box・skills/tools・cost controls・governance） | 母集団・方法＝不明 | Publisher claim | 箇条書き＋留保「GA日・SKU・料金・地域・Workspace/Cloud区分はstubになく、Cloud blog未取得」 |
| P2 | 同上 claim-2 [PRIMARY_FACT] | src-1 同上 | Rollout詳細はCloud blog（未取得） | — | unresolved | 同上 |

## P3 — Shipped vs promised weights + speech

| Pkg | Cand / Task | Claim | Source＋消費範囲 | 技術主張・数値 | 母集団/比較/方法 | 区分 | Draft日本語＋必須留保 |
|---|---|---|---|---|---|---|---|
| P3 | `6ef696cfd74b23a3` / `a85f8a48d5995bc6` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL page (delegated) | 78B/3B MoE（表78.1B/3.46B）、1M context、Apache-2.0、HF Aleph-Alpha/Kolibri-1、20T tokens、768×B200 | 規模・条件として既知 | Publisher claim | 規模表＋留保「料金なし、表途中から未取得」 |
| P3 | 同上 claim-2 [VENDOR_CLAIM] | src-1 同上 | AIME 2026 96.0、GPQA 84.3等 | 方法＝発行者計測のみ | Publisher claim | 留保「独立再現なし」 |
| P3 | `d744e3d3b41d5984` / `b4bafa16abf012ea` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL page (delegated) | d1-3B＋d1-omni-600M（HF LiquidAI/d1-3b等）、Decision Index 48.57/15.95、8ms RTX4090（ベンダー） | Index運営・方法＝不明 | Publisher claim | 留保「Indexの方法・ライセンスSPDXなし」 |
| P3 | `49389f88b1d34f49` / `36ef2bcb44f844f9` claim-1 [VENDOR_CLAIM] | src-1＋supplement-src-1fa2e6b4e1db612f blog excerpt | 740M（270M+170M+300M）、768-d MRL、8K context、Apache-2.0、HF＋Kaggle | 仕様として既知（card timeoutでblogのみ） | Publisher claim | 留保「card本体未取得、arch表は断片のみ」 |
| P3 | 同上 claim-2 [VENDOR_CLAIM] | 同上 | MTEB-Code +9.92 | 方法・母集団＝cardに委譲（未取得） | unresolved | 留保「全指標は未取得cardに委譲」 |
| P3 | `6dc00490d25b0578` / `5d2673f475348f6f` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL page (delegated) | 501B/23B MoE、weights/report/cardはlater this month、Apache-2.0 intent、early accessのみ | 状態として既知 | Publisher claim | 留保「重み未公開、比較対象専用」 |
| P3 | 同上 claim-2 [VENDOR_CLAIM] | src-1 同上 | DeepSWE 44.4、TB2.1 80.1、AIME 97.8、23.8T tokens、GB300 RL scale（ベンダー） | 方法＝不明 | Publisher claim | 留保「独立再現なし」 |
| P3 | `40a492061f3d95fb` / `95e0813c100e3798` claim-1 [VENDOR_CLAIM] | src-1＋supplement-src-c10ede7c23828f99 docs/blog pins | 52B active／1–1.05T total、1M context、preview API today、weights end of month、$0.68/$2.09 | ピンとして既知 | Publisher claim | 留保「重み未公開、WEIGHTSタブ・ライセンス未取得」 |
| P3 | 同上 claim-2 [SOCIAL_OBSERVATION] | 同上 | Grok X 10/6は49B activeと発表、公式blog/docs本体に49Bなし、不一致を未解決のまま保持 | 49B X本体は未取得 | unresolved | 「公式52B・X 49B、不一致のまま」＋留保「裁定しない」 |
| P3 | `007e44bf88724312` / `5bfb1ea9fbad4623` claim-1 [PRIMARY_FACT] | src-1 PRIMARY_OFFICIAL changelog (JSON-LD含む delegated) | datePublished 2026-10-09T18:27:34Z（cutoff内確定） | 時刻として既知 | 確定事実（cutoff判定用） | 「JSON-LD時刻でin-window確定」＋留保「X 23:11Zはcutoff外でevent clockでない」 |
| P3 | 同上 claim-2 [VENDOR_CLAIM] | src-1 同上 | Qwen3-Omni-30B-A3B MoE、omni $0.15/M（flash $0.09→$0.038）、HF open weights、vendor benches | 方法＝不明、HF/SPDX未検証 | Publisher claim | 留保「HF download・SPDX未検証、発行者言明と実バイトは別」 |
| P3 | `d0891837ce8f4a4b` / `3297d2869fcc9dbb` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL AWS page (delegated) | GA 10/5 speech-to-speech、Bedrock 4 regions、旧同等料金（数値なし）、256K context | 日付・地域・context既知、料金数値なし | 一部 unresolved（料金・ベンチ・ライセンスなし） | 留保「料金数値は本文になし、品質首位主張不可」 |

## P4 — Image brief

| Pkg | Cand / Task | Claim | Source＋消費範囲 | 技術主張・数値 | 母集団/比較/方法 | 区分 | Draft日本語＋必須留保 |
|---|---|---|---|---|---|---|---|
| P4 | `1a529893f55caf14` / `e9e13879f1c0fcf8` claim-1 [VENDOR_CLAIM] | src-1 SOCIAL（X-derived lead）＋supplement-src-360435193adc7df6 model card excerpt | Gemini 3 series／3.6 Flash base、1M input、4K image＋64K text out、7-channel、vendor SxS Elo | 仕様として既知、Eloの母集団・方法＝不明 | Publisher claim | スペック表＋留保「EloはベンダーSxS、arena根拠未解決、料金・ライセンスなし」 |
| P4 | 同上 claim-2 [PRIMARY_FACT] | 同上 | checked pages中の一致blogなし（2026-10-12 delegated search）、cardはweb-wide不存在の証拠でない | 否定探索の範囲として既知 | 確定事実（範囲限定） | 許容文言のみ「確認した発行者ページの中に一致blogなし（2026-10-12）」＋旧断定文言の使用禁止 |

## P5 — Provenance week

| Pkg | Cand / Task | Claim | Source＋消費範囲 | 技術主張・数値 | 母集団/比較/方法 | 区分 | Draft日本語＋必須留保 |
|---|---|---|---|---|---|---|---|
| P5 | `5168f0d6e2b8385c` / `6601f7ffad5b2624` claim-1 [PRIMARY_FACT] | src-1 blog full body（Muse DIRECT_READ）＋supplement-src-d6dd5c50f1794c7d excerpt | 統計透かし、API opt-in now、EU ChatGPT/Codex coming weeks、detector研究者限定、1% FPRで200tok～80%・400tok～95%、edit weakening数値、Astra品質表 | FPR・token・edit・品質表は既知（ベンダー実施） | Vendor-runだがfirst-hand読了（独立再現なし→Publisher claim相当の扱い） | 数表＋留保「ベンダー実施、独立検証なし、PDF未読」 |
| P5 | 同上 claim-2 [PRIMARY_FACT] | 同上 | Tech-report PDFはlinkのみ未読、著者・方法は二手のみ | — | unresolved | 留保「論文内部の方法主張はblog事実のみ」 |
| P5 | `d78c93e1181a782d` / `ef2ef9a25ec009ba` claim-1 [VENDOR_CLAIM] | src-1 SOCIAL＋supplement-src-bd822c4689ba127c blog excerpt | portal英語global 10/7～、image/video/audio（Google・partners: OpenAI・NVIDIA・Kakao・soon Apple）、scale counts、text除外 | 範囲として既知 | Publisher claim | 範囲表＋留保「partner coverageはベンダー言明、portal自体はfetch不可」 |
| P5 | 同上 claim-2 [PRIMARY_FACT] | 同上 | synthid.comはJS-shellのみ、formats/pricing/license取得不可 | — | 確定事実（取得失敗） | 留保「精度ベンチなし、text対象外、他modalityへの転用不可」 |

## P6 — Safety and science briefs

| Pkg | Cand / Task | Claim | Source＋消費範囲 | 技術主張・数値 | 母集団/比較/方法 | 区分 | Draft日本語＋必須留保 |
|---|---|---|---|---|---|---|---|
| P6 | `2e2a2ec51512e38b` / `cd3f94caf69926d9` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL page (delegated) | CIDP（11 founding partners）＋OSS Scanner（opt-in・free、model-generated PoC reports、human reviewなし、>90% TP expected） | 制度条件として既知、効果母集団・方法＝なし | Publisher claim | 留保「scanner post・form内部未取得、実測アウトカムなし」 |
| P6 | `81377ee6d9f7f12e` / `feec9ec0eabe1d59` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL page (delegated) | 未命名frontier model由来の数学成果、GitHub openai/math、Lean部分形式化、10 reasoning summaries、Pro-usage compute stats（平均～3h） | 列挙として既知、file counts・license未列挙 | Publisher claim | 留保「model未公開・期日なし、証明検証の主張不可」 |
| P6 | 同上 claim-2 [VENDOR_CLAIM] | src-1 同上 | Model自体は未公開、responsible-release継続中 | — | 確定事実（非公開宣言） | 同上 |
| P6 | `b526a5361c5274a8` / `ad97bfa3daa6e156` claim-1 [VENDOR_CLAIM] | src-1 PRIMARY_OFFICIAL page (delegated) | 11 contracting tasks（EDGAR-simulated、非公開データなし）、Astra Max 55.0% vs Sol High 41.6%（+32%）、37.0→19.2 min（-48%）、全てsimulated vendor-stated | 母集団＝11 EDGAR模擬tasks既知、rubric・per-task・RL詳細なし | Publisher claim | 留保「provisional・rubricなし、導入効果としての提示不可」 |
| P6 | 同上 claim-2 [PRIMARY_FACT] | src-1 同上 | Ironclad product launchesは本ページ外の別event | — | 確定事実（範囲） | 留保「製品発表と混同不可」 |

## 優先数値の所在確認（指示対応）

- GPT-6 44%：P1行2（開始遅延、wall-timeでない）。
- Decisions 10x：P2行1（方法論なし）。
- Kolibri性能・公開状況：P3行1–2（78B/3B・1M・Apache-2.0・HF stated、ベンチは発行者計測）。
- textGrain FPR・編集耐性：P5行1–2（FPR/token/edit・品質表、PDF未読）。
- Nova Sonic：P3行12（GA・地域・256K、料金数値なし）。
- Cyber Mission：P6行1（11社・scanner条件・>90% expected、実測なし）。
- Ironclad：P6行4–5（11 tasks・EDGAR・vendor deltas、provisional）。

(End of file)
