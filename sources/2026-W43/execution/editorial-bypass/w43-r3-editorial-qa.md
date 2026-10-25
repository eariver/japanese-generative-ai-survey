# W43 Core-free editorial QA r3 (UNVALIDATED, noncanonical)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED / NOT_DRAFT_COMPLETE`
Date: 2026-10-25. Branch: `weekly/2026-W43-v2-work`.
r3 preview: `execution/editorial-bypass/w43-r3-reader-preview-UNVALIDATED-20261025.md`（本文約32,100字）
Ledger: `execution/editorial-bypass/w43-r3-citation-confidence-ledger.json`（96 rows: 62P＋20T＋8N＋1 recap＋3 FIGURE＋2 CODE；SHA256 `f0a607457a4e9d6f57a858c8d73352f6c3a62e53d7ca7bcb1efc086096c7b260`）
Crosswalk: `execution/editorial-bypass/w43-r3-source-crosswalk.md`
Method: 独立11件 binding 修正。直接一次バイト（Flint card/announce・MemT README 208–219・DeepInfer README/environ.py・changelog・Patch rendered）を自読・逐語引用。FLUX算術・GH/npm時刻は再照合。

## 1. 31 must-cover truth values（r2の31/31 Y表示を訂正）

`SUBSTANTIVE_COMPLETE` 28 ／ `PARTIAL` 3 ／ `MENTIONED_ONLY` 0 ／ `NOT_ADDRESSED` 0 ／ `NOT_VERIFIABLE` 0。
`EDIT_FIXED`（r1→r2の13＋r3の文言・実物追加）と `SOURCE_VERIFIED`（独立再計算・直接バイト確認）は別 tracking。下表の Location は preview 内位置。

| Req | Verdict | Location / anchors |
|---|---|---|
| §1.1 | SUBSTANTIVE_COMPLETE | p1-p1/p1-t1/p1-p7/n1；KIMI-X秒確定・Nov4 FUTURE分離 |
| §1.2 | SUBSTANTIVE_COMPLETE | p1-p3/p1-p4/p1-t2；三規約を列見出しで分離、等価比較禁止 |
| §1.3 | SUBSTANTIVE_COMPLETE | p1-p2/p1-t2/p1-p10/**p1-f1三層図実物**；対応512k・推奨256k・設定262144を層別 |
| §1.4 | SUBSTANTIVE_COMPLETE | p1-p5/p1-t3/p1-p8/p1-p9；Flint評価条件（1.0/0.95/20・pass@1・†）をcard逐語で追加 |
| §1.5 | SUBSTANTIVE_COMPLETE | p1-p6/p1-t4；Flint=Apache-2.0・Nemotron=OpenMDW-1.1分離 |
| §2.1 | SUBSTANTIVE_COMPLETE | p2-p1/p2-t1/p2-p8；核×役割表＋行別典拠 |
| §2.2 | SUBSTANTIVE_COMPLETE | p2-p2/p2-p3/p2-p9/**p2-f1二設定例実物**（排他・NOT_EXECUTED明示） |
| §2.3 | SUBSTANTIVE_COMPLETE | p2-p4/p2-p3；SM100/Ascend950・1017・4xSM100+64・除外列挙 |
| §2.4 | SUBSTANTIVE_COMPLETE | p2-p5/p2-t2/p2-p10；1.86x/66x分母分離 |
| §2.5 | SUBSTANTIVE_COMPLETE | p2-p6/**p2-f2権利対応表実物**（CC BY-NC-SA 4.0／PolyForm NC 1.0.0／MIT／weights除外） |
| §2.6 | SUBSTANTIVE_COMPLETE | p2-p7/p2-n1；DEPTH_LIMITED注記（vendor-only宣言として完備） |
| §3.1 | SUBSTANTIVE_COMPLETE | p3-p2/p3-t1/p3-p7；待機・先行・共有制限・接続先一覧vs実live |
| §3.2 | SUBSTANTIVE_COMPLETE | p3-p3/p3-p4/p3-p8/**p3-f1資格フロー図実物**（coming-soon段階つき） |
| §3.3 | SUBSTANTIVE_COMPLETE | p3-p3/p3-p5/p3-p9；積層の記述vs試験分離 |
| §3.4 | SUBSTANTIVE_COMPLETE | p3-p6/p3-t2；旧/新/未来三段 |
| §4.1 | PARTIAL | p4-p2/p4-p3；keyframes live/schema/GA証明不能のためUNRESOLVED維持（FAQ暫定表現に後退） |
| §4.2 | SUBSTANTIVE_COMPLETE | p4-p4/p4-t1；25.37x/22.31x/95.52%再計算VERIFIED・26.5x不整合保持 |
| §4.3 | SUBSTANTIVE_COMPLETE | p4-p5/p4-p6；+47/+50非統一・1089導出値注記・従量条件 |
| §5.1 | PARTIAL | p5-p2/p5-p3/p5-t1；単一TTS数への統一が設計上不能（UNRESOLVED維持は正当） |
| §5.2 | SUBSTANTIVE_COMPLETE | p5-p4/**p5-f1実数行列**；判定器のvendor性明示 |
| §5.3 | SUBSTANTIVE_COMPLETE | p5-p5/p5-t2/p5-p8；MIT・tag/task・roadmap保留・月精度区別 |
| §5.4 | SUBSTANTIVE_COMPLETE | p5-p6/p5-p9；互換と指南未開封の分離 |
| §6.1 | SUBSTANTIVE_COMPLETE | p6-p2/p6-p3/p6-p6/**p6-f1五段階図実物**（担い手・RENDERED_ONLY・CVE留保） |
| §6.2 | SUBSTANTIVE_COMPLETE | p6-p4/p6-p7；頁/日付・RSS10:00Z secondary分離 |
| §6.3 | SUBSTANTIVE_COMPLETE | p6-p3/p6-p5；Oct23/W42 lineage分離 |
| §7.1 | SUBSTANTIVE_COMPLETE | p7-p2/p7-t1/p7-p6；班内・盲検・wet-lab未 |
| §7.2 | SUBSTANTIVE_COMPLETE | p7-p3/p7-p4/p7-t2/**p7-f1言語別デルタ表実物**（OCaml/Fortran/VB・61%・−78%・罠/飽和注記） |
| §7.3 | SUBSTANTIVE_COMPLETE | p7-p5/p7-n1；限界・来歴保存 |
| §8.1 | PARTIAL | p8-p2/p8-t1/p8-p6/**p8-f1例はILLUSTRATIVE**（endpoint・版文字列・TTL・出力値が未検証のため実行例化不能） |
| §8.2 | SUBSTANTIVE_COMPLETE | p8-p3/p8-p4/p8-p7/**p8-f2安定vs実験表実物**（二時刻再確認） |
| §8.3 | SUBSTANTIVE_COMPLETE | p8-p5/p8-t2/p8-p8/**p8-f3重みvsAPI表実物**（MIT/SHA未取得/課金未試験分離） |

PARTIAL 3件はいずれも設計上・証拠上の到達不能（live証明／単一数統一／実行例化）を正直に残したものであり、水増しで完結させていない。

## 2. Artifact inventory（実物・位置つき）

| ID | 種別 | 位置 | 典拠 |
|---|---|---|---|
| p1-f1 | 三層文脈図 | P1末 | FLINT-CARD＋FLINT-ART＋NEMO-CARD |
| p2-f1 | 排他二設定例（bash＋python、NOT_EXECUTED） | P2 §2.2後 | DI-README 24–28行・DI-ENV 129–132・197行 |
| p2-f2 | MemT権利対応表 | P2 §2.5内 | MEMT-README 208–219行逐語 |
| p3-f1 | 資格・承認フロー図 | P3末 | Duet/1Password/auto-mode発表（vendor記述明示） |
| p5-f1 | 様式×評価料金実数行列 | P5末 | Voxtral card claim-1/2/3（独立再現なし明示） |
| p6-f1 | 協調開示五段階図 | P6末 | Patch card＋PATCH_RAW（RENDERED_ONLY） |
| p7-f1 | 言語別デルタ・労力費用表 | P7 §7.2内 | Low-resource card claim-1/2/3 |
| p8-f1 | Decisions構成要素スケルトン（ILLUSTRATIVE/SAMPLE_ONLY/NOT_RUN） | P8 §8.1内 | changelog原文＋Decisions card claim-1/2 |
| p8-f2 | 安定核vs実験harness表 | P8 §8.2内 | GH 15:18:14Z／npm 15:21:49Z |
| p8-f3 | 重みvs API vs追加物表 | P8 §8.3内 | DeepSeek card（SHA未取得・課金未試験明示） |

Tables content verdict: 20/20 OK（15既存＋5新規）。Per-row source: 15既存表に典拠キー行を追加＋新規表は行内典拠つき。Layout: 全てfenced delimiter text（DRAFT_TEXT、組版未検証・将来render工程）。

## 3. 19 placements・5 LIMITED・68 Attention

12 PRIMARY＋7 SUPPORTINGを8章に重複なく配置。HOLD/REJECT12/Metrics OUT/Grok NEVER_STORYの昇格なし。未選択の主役化なし。
32 PARTIAL・51 Materiality・Completeness LIMITED・residual 5は各章NOTE＋限定文に継承。68/68 AttentionはArchitecture不変のため継承（再生成なし）。
Human Architecture r1 APPROVED維持。総括はDraft要件・P9非該当・32件目非該当。

## 4. Depth assessment（R2-SOL-03回答）

r2約22,200字 → r3約32,100字（＋約9,900字の実質加筆、重複段落の圧縮含む）。加筆は全て受理証拠・保存一次バイトの範囲：Flint card逐語（2.5B/2.2B/262144/評価条件）・announce原文（512k/256k）・MemT版つき約款・DeepInfer設定例・Voxtral実数（WER/cpWER/recall/料金/LiveKit）・低資源言語別デルタ・Decisions changelog原子・TanStack/DeepSeek対照表。
圧縮：p2-p9（反復→経路差分説明＋設定例）、p5-p8（重複削除・roadmap/月精度に特化）。35pp body見積に対する不足は表組版・図版・出典一覧等の出版工程で吸収すべきで、本文水増しは行わない旨を維持する。
P6/P7が4–4.5pp相当の実質説明を持つか：工程図・言語別表・労力費用注記・盲検/hidden分離により機構・条件・分母の三点は充足。独立再現の欠如は残留リスクとして明示（下記）。

## 5. 「今週の総括」（配置・抜粋・変更点）

- 配置：P8末NOTEの後、見出し exactly `今週の総括`、実質5段落。P9非該当。新規候補配置なし。
- r3変更：段1の「能力が向上したという事実」→「性能・能力向上が報告されたこと」。独立確認済みの断定から発行元報告の記述に後退。r2改訂（50超・約款分離・GPT-6.1等）と矛盾する数値・時刻なし。変更不要の残り4段落は維持。
- 運用メモ（編集注記・校閲前留意事項）は本QA §8に移管し、読者向け本文から除去した。
- 抜粋（段1全文）：「今週の生成AI関連の発表を貫くのは、モデルの性能・能力向上が報告されたこと自体ではなく、その能力を**どの時点で、どの条件で、実際に利用できるのか**という問題である。KimiではAPI提供と将来の重み配布を区別する必要がある。一方、FlintやNemotronのように重みを入手できる場合でも、総パラメータ数と稼働パラメータ数、文脈長、実行条件、重みに適用されるライセンスまで確かめなければ、導入可能性は判断できない。DeepInferの高速化も、設定の排他性や実行環境を無視して評価できず、MemTの記憶機構も論文中の比較条件から切り離して優劣を語れない。」

## 6. Residual risks

1. FAQ原文・PRNewswire原文・AA原表・Voxtral細部URL・bioRxiv/HF/GitHub exact URL・TanStack blog URLは未取得（UNRESOLVED維持、捏造なし）。
2. 全ベンチ・速度・Elo・費用は発行元測定（独立再現なし）。p2-f1設定例・p8-f1スケルトンはNOT_EXECUTED。
3. 表20・図3・コード2の組版・検証は未実施（DRAFT_TEXT）。
4. Core Draft Stageは依然BLOCKED。`runner.generated_at=2026-10-25T14:00:00Z`は未検証のまま provenance に昇格させない。
5. 原本 `20261025212008_SolReview.md`（23,861B、`fa0d8d7a…`）は本sessionで未読。裁定・receipt・11件マトリクスで代用した旨を開示する（契約§1.1の review limitation）。

## 7. 非改変の記録

State（`ARCHITECTURE_ESTABLISHED`）・Gate承認・Architecture/Selection/Evidence・main/Frozen Core・共有Core rootsに変更なし。Native Draft Package/Result・Synthesis・QA receipt・`DRAFT_COMPLETE`・`ADVANCE_STAGE`・TeX/PDF・Publication Preview・Freeze/Releaseは生成・要求せず。r1/r2資産・UNVALIDATED入力は不変保全。

## 8. 本文から移管した運用メモ（r3で除去分）

- 総括の編集注記：「この総括はW43の承認済みArchitectureと未検証Draft入力を横断して作成したedition-localな編集案です。新規の独立実験・一次資料取得を示すものではありません。正式本文に採用する際はP1～P8の検証済み記述と整合させ、読者向け原稿のP8直後・出典一覧前に配置してください。」（r3でP1～P8改訂本文との整合確認済み）
- 校閲前留意事項：「8章・113ブロック・独立した「今週の総括」が揃っていることを確認済み。本文内容、出典、章立てと根拠の適合性を編集者・独立Solが確認する必要がある。現在のCore ValidatorはScreening packageの古いState SHAを比較して停止する。Production State、Screening package、Frozen Coreコードを改変していない。独立性の未確認なベンダー数値や日付、引用、ライセンス断定は今後のレビュー対象である。Canonical Draft Package/Result・Synthesis・Checkpoint・TeX・PDF・Publication Previewは作成・承認されていない。」（r3では8章・96行台帳・実物10件・総括5段落に更新、他は維持）
