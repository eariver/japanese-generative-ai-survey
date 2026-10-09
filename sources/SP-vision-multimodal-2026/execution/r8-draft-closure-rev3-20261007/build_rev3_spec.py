#!/usr/bin/env python3
"""Build compact-input-fresh-121-r8-rev3.json: bounded reader-facing cleanup.

Every replacement asserts its hit count (no silent no-ops). Block rewrites assert
old-form presence. discovery_ids/must_cover_map untouched (no map change per §14).
draft_version fresh-121-r8-rev3. No upstream/Architecture change.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-draft-closure-rev3-20261007"
IN = SRC / "execution/r8-draft-closure-rev2-20261007/compact-input-fresh-121-r8-rev2.json"
OUT = EDIR / "compact-input-fresh-121-r8-rev3.json"

# (old, new, expected_hits)
REPLACEMENTS = [
    # §4 P15-B09 duplicated condition clause -> exactly one
    ("へ移り、Claude Opus 4.7・最大思考・単一行動設定での108課題Claude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回",
     "へ移り、Claude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回", 1),
    # §5 grounding normalization: P07B deck gloss + consistent terms
    ("語句接地と指示参照、オープンボキャブラリー検出と接地検出、分割分岐を指標ごとに切り離して、次の演算に見合う接地表現を問う。",
     "語句grounding（グラウンディング）と指示参照、オープンボキャブラリー検出とグラウンディング検出、分割分岐を指標ごとに切り離して、次の演算に見合うグラウンディング表現を問う。", 1),
    ("課題は語句の接地であり", "課題は語句グラウンディングであり", 1),
    ("語句接地の次に足りなかったのは", "語句グラウンディングの次に足りなかったのは", 1),
    ("構成的文脈のモデル化と接地正解率の指標", "構成的文脈のモデル化とグラウンディング正解率の指標", 1),
    ("V2L投影と接地やマスク言語モデル", "V2L投影とグラウンディングやマスク言語モデル", 1),
    ("教師に縛られた検出器のオープンボキャブラリー化が果たされ", "教師モデルへの依存が残る検出器のオープンボキャブラリー化が果たされ", 1),
    # §6 P07B-B07 merge (handled as block rewrite below)
    # §7 B14 + data terms
    ("語句と領域の対応づけを担う資料（Flickr30k Entitiesの24.4万共参照鎖・27.6万箱）",
     "語句と領域の対応づけを担うFlickr30k Entitiesの領域―語句対応データ（24.4万共参照鎖・27.6万箱）", 1),
    ("教師の置き方（ViLDの蒸留かGLIPの資料実践か）と融合の位置（MDETRの早期融合か後段での融合）と出力（箱か語句接地か）で系統が分かれる。",
     "教師信号の構成（ViLDの蒸留かGLIPの大規模グラウンディングデータ構築か）と融合の位置（MDETRの早期融合か後段での融合）と出力（箱か語句グラウンディングか）で系統が分かれる。", 1),
    ("ウェブ資料依存の限界を条件づける", "ウェブ由来データへの依存という限界を条件づける", 1),
    # §8 B12
    ("再学習や追加試料なしのゼロショット汎化を可能にした。",
     "再学習や追加学習データなしのゼロショット汎化を可能にした。", 1),
    ("統合はX-Decoder側に委ねられる。", "より広い統合は後述するX-Decoderで扱う。", 1),
    # §9 B13
    ("拡散依存と他巻越境は段落で区切る。",
     "拡散モデルとしての詳細は本節の対象外とし、ここではオープンボキャブラリー分割に利用される表現としての役割に限定する。", 1),
    # §10 P05-B08
    ("本段の懸念は編集部の推論であり、原論文の測定ではない。",
     "以上は本稿における監査上の注意点であり、原論文が測定した混入率ではない。", 1),
    # §11 P06-B07 LVD (evidence: LVD-1689M, 1,689M hierarchical sampling)
    ("DINOv3は70億変数の自己教師あり視覚モデルで、LVD-1689Mの1689M階層抽出で学ばれる。",
     "DINOv3は70億変数の自己教師あり視覚モデルで、16.89億画像の階層サンプリングによるLVD-1689Mで学習する。", 1),
    # §12 bounded cleanup
    ("凍結画像の調整であるSigLiTは4基のTPUv4で2日",
     "Locked-image Tuning（画像エンコーダ固定の調整）であるSigLiTは4基のTPUv4で2日", 1),
    ("閉じた到達点は能力と評価の到達点として置く。",
     "非公開モデル側の比較対象は能力と評価の到達点として置く。", 1),
    ("閉じた側の到達点が比較対象になった一方で",
     "非公開モデル側の到達点が比較対象になった一方で", 1),
    ("閉じた側記録は能力提供域であり、機構を断定しない。",
     "非公開モデルについては提供元が示す能力範囲に限って扱い、機構は断定しない。", 1),
    ("検出を語句の接地へ書き直す資料実践（GLIPの27M接地集合：人手3Mとウェブ由来24M）",
     "検出を語句グラウンディングへ書き直す大規模グラウンディングデータ構築（GLIPの27M件グラウンディングデータ：人手3Mとウェブ由来24M）", 1),
    ("閉じた到達点と選択的取得の効率値は提供元とベンダーの報告で上限表示であり",
     "非公開モデル側の到達点と選択的取得の効率値は提供元とベンダーの報告で上限表示であり", 1),
    ("携帯端末からクラウドまでの提供面を示し",
     "携帯端末からクラウドまでの提供形態を示し", 1),
    ("ストリーミング対応の提供面と事例集を示し",
     "ストリーミング対応の提供内容と事例集を示し", 1),
    # §5 cross-package grounding normalization
    ("接地の振る舞いはGrounding DINO側の資料で扱う。",
     "グラウンディングの振る舞いはGrounding DINO側の記述で扱う。", 1),
    ("新規性は画像と映像の規模の上に載る言語接地の概念接点にあるとされる。",
     "新規性は画像と映像の規模の上に載る言語グラウンディングの概念接点にあるとされる。", 1),
    ("後の検出-接地統一学習（GLIPの語句接地への書き直し）が前提にする領域と言語の対応づけの原型を示す",
     "後の検出-グラウンディング統一学習（GLIPの語句グラウンディングへの書き直し）が前提にする領域と言語の対応づけの原型を示す", 1),
    ("RefCOCOの接地、OWL-ViTによるオープンボキャブラリー検出、密な探索でSigLIPを上回り",
     "RefCOCOのグラウンディング、OWL-ViTによるオープンボキャブラリー検出、密な探索でSigLIPを上回り", 1),
    ("位置への接地とは指標も機構も切り離して", "位置へのグラウンディングとは指標も機構も切り離して", 1),
    ("接地のAPとは別の契約で測る。", "グラウンディングのAPとは別の契約で測る。", 1),
    ("位置や領域への接地とは別の評価で測られる。", "位置や領域へのグラウンディングとは別の評価で測られる。", 1),
    ("RefCOCOの接地やOWL-ViTの検出や密な探索", "RefCOCOのグラウンディングやOWL-ViTの検出や密な探索", 1),
    ("位置や領域への接地そのものは次節の契約であり", "位置や領域へのグラウンディングそのものは次節の契約であり", 1),
    ("本節の契約はゼロショット分類と画像文検索のRecall@Kであり、語句の接地や検出のAPとは別の指標で測る。",
     "本節の契約はゼロショット分類と画像文検索のRecall@Kであり、語句グラウンディングや検出のAPとは別の指標で測る。", 1),
    ("残したまま接地側へ受け渡す。", "残したままグラウンディング側へ受け渡す。", 1),
    ("ボックスは接地の代理を記号で表すものであり", "ボックスはグラウンディングの代理を記号で表すものであり", 1),
    ("指さしは接地を直接の出力とするもので", "指さしはグラウンディングを直接の出力とするもので", 1),
    ("位置への接地を別の契約として区別し", "位置へのグラウンディングを別の契約として区別し", 1),
    ("プランニング側の接地からjointな表象", "プランニング側のグラウンディングからjointな表象", 1),
    ("プランニング側の接地を示す分岐点である", "プランニング側のグラウンディングを示す分岐点である", 1),
    ("接地ありが接地なし基準のほぼ2倍に達した", "グラウンディングありがグラウンディングなし基準のほぼ2倍に達した", 1),
    ("言語接地へ、画面と身体の行動へ", "言語グラウンディングへ、画面と身体の行動へ", 1),
    ("GLIPは検出を句接地として書き直し、27M接地集合",
     "GLIPは検出を句グラウンディングとして書き直し、27M件のグラウンディングデータ", 1),
    ("接地の正確さと総作業費用は別軸であり", "グラウンディングの正解率と総作業費用は別軸であり", 1),
    ("Flickr30kの語句接地やRefCOCO系列のREC", "Flickr30kの語句グラウンディングやRefCOCO系列のREC", 1),
    ("接地学習と検出器を三段階で密に結ぶ融合設計として", "グラウンディング学習と検出器を三段階で密に結ぶ融合設計として", 1),
    ("検出と接地と説明文のデータで事前学習する", "検出とグラウンディングと説明文のデータで事前学習する", 1),
    ("GLIPの再定式とは契約が異なり", "GLIPの再定式とは契約が異なり", 1),
]

NEW_P07B_B07 = ("検出を語句グラウンディングへ書き直す再定式化として、GLIPは検出とグラウンディングの統一事前学習を行った。27M件のグラウンディングデータ、すなわち人手3Mとウェブ由来24Mから自己学習で起こしたグラウンディング箱を用い、COCOゼロショット49.8、LVIS26.9APとされる。COCO画像を見ない条件で教師あり基準を上回るとされ、微調整でCOCO検証60.8と開発集合61.5、13転移課題で1-shotが教師ありDynamic Headに匹敵するとされる。コードが公開された。グラウンディングデータ実践による検出の再定義が果たされた。規模主張は論文報告として扱う。Visual Genomeの領域記述データの蓄積がGoldGのデータ体制へつながる来歴は、GLIPの節で扱う範囲として添える。")


def main() -> int:
    EDIR.mkdir(parents=True, exist_ok=True)
    spec = json.loads(IN.read_text(encoding="utf-8"))
    fired = []
    missed = []
    for p in spec["packages"]:
        for field in ("headline", "deck"):
            if p.get(field):
                for old, new, expected in REPLACEMENTS:
                    if old in p[field]:
                        p[field] = p[field].replace(old, new)
                        fired.append((p["package_id"], field, old[:40]))
        for b in p["blocks"]:
            if not b.get("text"):
                continue
            for old, new, expected in REPLACEMENTS:
                if old in b["text"]:
                    b["text"] = b["text"].replace(old, new)
                    fired.append((p["package_id"], b["block_id"], old[:40]))
        if p.get("boundaries_text"):
            for old, new, expected in REPLACEMENTS:
                if old in p["boundaries_text"]:
                    p["boundaries_text"] = p["boundaries_text"].replace(old, new)
                    fired.append((p["package_id"], "boundaries", old[:40]))
    from collections import Counter as _C
    counts = _C(o for _, _, o in fired)
    for old, _, expected in REPLACEMENTS:
        if expected == 0:
            continue
        got = sum(1 for _, _, o in fired if o == old[:40])
        # count actual replacements via fresh scan below; prefix-collision safe check:
        if got != expected:
            missed.append((old[:70], expected, got))
    print(f"replacements fired: {len(fired)}")
    if missed:
        print("COUNT MISMATCH:")
        for m in missed:
            print("  -", m)
        raise SystemExit("replacement count mismatch")

    def get_block(pid, bid):
        p = next(x for x in spec["packages"] if x["package_id"] == pid)
        return p, next(x for x in p["blocks"] if x.get("block_id") == bid)

    _, b07 = get_block("P07B", "P07B-B07")
    assert "GLIPは検出を語句の接地へ書き直した。GLIPは検出を語句の接地として再定式化し" in b07["text"], "B07 dup opener missing"
    b07["text"] = NEW_P07B_B07

    # P07B-B10/B14/D114/D115 grounding normalization (full rewrites keep all
    # facts/numbers/refs; discovery_ids untouched)
    _, _b10 = get_block("P07B", "P07B-B10")
    assert "language-guided query selection" in _b10["text"]  # post-replacement form present
    _b10["text"] = ("グラウンディング学習と検出器を三段階で密に結ぶ融合設計として、Grounding DINOが示された。"
        "Grounding DINOはfeature enhancer（特徴強化器）とlanguage-guided query selection（言語誘導型クエリ選択）と"
        "cross-modality decoder（クロスモダリティ・デコーダ）の3段階でDINO検出器とグラウンディング学習を結合し、"
        "検出とグラウンディングと説明文のデータで事前学習する。検出器DINOは技術的土台として区別され、集合予測系の"
        "系譜に属する。COCOゼロショット52.5APとされ、ここでのゼロショットは学習に検証区分を使わない論文定義である。"
        "ODinWゼロショット平均26.1APが記録され、チェックポイントと推論コードが公開された。密な融合による"
        "オープンボキャブラリー検出が実現された。GLIPの再定式とは契約が異なり、融合設計としての位置が保たれる。"
        "RECのゼロショット性能は今後の注目を要すると論文自身が述べており、言い切らない。")
    _, _b14 = get_block("P07B", "P07B-B14")
    assert "大規模グラウンディングデータ構築" in _b14["text"]  # post-replacement form present
    _b14["text"] = ("本節の系譜は、語句と領域の対応づけを担うFlickr30k Entitiesの領域―語句対応データ"
        "（24.4万共参照鎖・27.6万箱）から、検出を語句グラウンディングへ書き直す大規模グラウンディングデータ構築"
        "（GLIPの27M件グラウンディングデータ：人手3Mとウェブ由来24M）、検出器とグラウンディング学習を三段階で結ぶ密な融合"
        "（Grounding DINO）へ進んだ。教師信号の構成（ViLDの蒸留かGLIPの大規模グラウンディングデータ構築か）と融合の位置"
        "（MDETRの早期融合か後段での融合）と出力（箱か語句グラウンディングか）で系統が分かれる。LVIS-rareのAPと語句"
        "グラウンディングのRecallを別指標で測り、画像水準のゼロショットや検索Recall@Kとも混ぜない点が共通の約束である。"
        "希少区分の手順は利用ごとに明示し、ウェブ由来データへの依存という限界を条件づける。単一構成の勝利ではなく、"
        "粒度と代償の未解決を残す。")
    _, _d114 = get_block("P07B", "P07B-D114")
    assert "RefCOCOの接地" in _d114["text"]
    _d114["text"] = _d114["text"].replace("RefCOCOの接地", "RefCOCOのグラウンディング")
    _, _d115 = get_block("P07B", "P07B-D115")
    assert "後発の接地拡張" in _d115["text"]
    _d115["text"] = _d115["text"].replace("後発の接地拡張", "後発のグラウンディング拡張").replace("概念接地の拡張", "概念グラウンディングの拡張")

    spec["draft_version"] = "fresh-121-r8-rev3"
    spec["runner"] = {
        "provider": "Muse",
        "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
        "invocation": ("TS-003 Draft closure revision r8-rev2 from Architecture r8 APPROVED "
                       "(same authority; final reader-facing cleanup: P15 dup, grounding norm, "
                       "P07B rhythm/synthesis, editorial vocabulary; r8 authority unchanged; "
                       "no TeX/PDF; DRAFT_COMPLETE held for final independent content review)"),
        "generated_at": "2026-10-07T11:00:00Z",
        "run_reference": None,
    }
    OUT.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blob = OUT.read_text(encoding="utf-8")
    must_be_gone = [
        "Claude Opus 4.7・最大思考・単一行動設定での108課題Claude Opus",
        "GLIPは検出を語句の接地へ書き直した。GLIPは検出を語句の接地として再定式化し",
        "資料実践", "ウェブ資料依存", "追加試料なし", "他巻越境", "編集部の推論",
        "LVD-1689Mの1689M階層抽出", "凍結画像の調整", "閉じた到達点", "閉じた側の到達点",
        "閉じた側記録", "提供面", "本記録は著者測定", "本記録は変種",
        "後継側の記録", "第三者文書", "〜側の記録に委ねる", "〜側の資料に委ねる",
    ]
    bad = [s for s in must_be_gone if s in blob]
    assert not bad, bad
    assert "Claude Opus 4.7・最大思考・単一行動設定での108課題Claude Opus 4.7" not in blob
    _b09 = next(x for x in next(p for p in spec["packages"] if p["package_id"] == "P15")["blocks"] if x["block_id"] == "P15-B09")
    assert _b09["text"].count("Claude Opus 4.7・最大思考・単一行動設定での108課題平均318.4回") == 1
    # grounding audit: remaining 接地 must not mean ML grounding (checked in audit_rev3)
    print(f"rev2-clean spec verified: {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
