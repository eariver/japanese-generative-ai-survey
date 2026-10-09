#!/usr/bin/env python3
"""Render TS-003 reader source (main.tex + references.bib) from fresh-124-r9 Draft.

Content-preserving deterministic assembly: headline/deck/blocks/boundary text
are copied byte-identically from canonical Draft Results (TeX-escaped only);
structure (sections, TOC, front matter, synthesis reuse, bibliography) comes
from approved Architecture/Profile/Synthesis authority. No paraphrase, no new
claims, no new sources. Citations bind each block's Evidence refs to
per-discovery-ID bibliography keys (vmd001..vmd125 excl. vmd122/DROP).

r9 adaptation vs r1 precedent:
- Evidence dir rebound to 6b55033d (124 results, 119/5).
- 5 multi-source cards (VM-D038/D074/D075/D077/D112): bibliography cites
  sources[0] (discovery-bounded primary locator); supplement license/mirror
  records are not cited locators. Rule recorded here, applied uniformly.
- Header comment + bib header name fresh-124-r9 (not r6).
No shared-Core change.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
sys.path.insert(0, str(REPO))
from scripts.render_article_draft_tex import tex_escape

SRC = REPO / "sources/SP-vision-multimodal-2026"
EVID_DIR = SRC / "evidence/v2/accepted/6b55033d02efecf69d784ebe8af534058222f84e37668b16c6341f8cc2deacd5"
SURVEY = REPO / "surveys/special/vision-multimodal-2026"

KICKERS = {
    "P01": "REPRESENTATION", "P02": "DETECTION", "P03": "DENSE PERCEPTION",
    "P04": "SPATIAL SUBSTRATE", "P05": "DOCUMENT INTELLIGENCE",
    "P06": "VISUAL FOUNDATIONS", "P07A": "ALIGNMENT", "P07B": "GROUNDING",
    "P08": "BRIDGES", "P09": "FUSION", "P10": "REASONING", "P11": "VIDEO",
    "P12": "COMPUTER USE", "P13": "VLA", "P14": "WORLD MODELS",
    "P15": "MEASUREMENT",
}


def bib_key(did: str) -> str:
    m = re.fullmatch(r"VM-D(\d+)", did)
    assert m, did
    return f"vmd{m.group(1).zfill(3)}"


def split_author(title: str):
    m = re.search(r"\(([^()]+)\)\s*$", title.strip())
    if not m:
        return None, title.strip()
    return m.group(1).strip(), title.strip()


# Publication-layer repairs (explicit, evidence-neutral, draft authority untouched).
# Precedent: reader-publication-validation-r5-issue559 (bounded reader repair with
# traceability; canonical Draft bytes preserved as authority).
# RPV-01: Simplified-Chinese typo in canonical P12-B1 bytes (デスクトップ应用,
# 複数应用) renders as tofu (HaranoAjiMincho lacks U+5E94 应). Repair to 応用.
# RPV-02..12: reader-surface leaks in canonical bytes (internal package refs,
# Discovery IDs, workflow vocabulary) normalized per surface-gate guidance;
# meaning and attribution preserved, evidence refs unchanged.
PATCHES = [
    ("应用", "応用", 2),
    ("本パッケージ", "本節", 4),
    ("accepted evidence は抄録水準の consumption に限られ",
     "根拠の利用は抄録水準に留まり", 1),
    ("accepted evidence はPARTIALである",
     "根拠は要旨水準の裏付けに留まる", 1),
    ("文書領域資料のPARTIAL性",
     "文書領域資料が要旨水準に留まる点", 1),
    ("LeNetはPARTIALとして機構細部に立ち入らない",
     "LeNetは要旨水準の裏付けとして機構細部に立ち入らない", 1),
    ("前継統合の根拠はこのVM-D011資料に属し、VM-D123から125へ遡及配置しない",
     "前継統合の記述は検出器DINOの論文自身の系譜記述に属し、"
     "Deformable DETR・DAB-DETR・DN-DETRの各資料へ遡及配置しない", 1),
    ("この data regime から降りる",
     "このデータ条件を受け継ぐ", 1),
    ("本ブロックでは先行形態の位置づけに留める",
     "ここでは先行形態の位置づけに留める", 1),
    ("との報告内容であり、VM-D065の請求項3で結びつける。VM-D065はP09由来の重なり参照である",
     "との報告内容が結びつけの根拠である。詳しくは第10節で扱い、"
     "ここでは接続の記述に留める", 1),
    ("VM-D114はP06由来の重なり参照である",
     "SigLIP 2の段階的手順の詳細は第6節の範囲である", 1),
    ("VM-D114とVM-D115はいずれも他節由来の重なり参照である",
     "SigLIP 2の詳細は第6節、SAM 3の機構の詳細は第3節の範囲である", 1),
]


def apply_patches(text: str, counter: dict) -> str:
    for old, new, _ in PATCHES:
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            counter[old] = counter.get(old, 0) + n
    return text


def bib_escape(value: str) -> str:
    return tex_escape(value)


def main() -> int:
    arch = json.load(open(SRC / "architecture-v2.json"))
    mat = json.load(open(SRC / "candidate-matrix-v2.json"))
    task2did = {}
    for row in mat["rows"]:
        assert len(row["discovery_ids"]) == 1, row["candidate_id"]
        task2did[row["evidence_task_id"]] = row["discovery_ids"][0]
    acc = json.load(open(EVID_DIR / "evidence-accepted.json"))
    assert acc["result_count"] == 124, acc["result_count"]
    src_by_did = {}
    multi = {}
    for row in acc["results"]:
        assert len(row["discovery_ids"]) == 1
        card = json.load(open(EVID_DIR / "results" / row["filename"]))
        assert card.get("sources"), row["discovery_ids"]
        src_by_did[row["discovery_ids"][0]] = card["sources"][0]
        if len(card["sources"]) != 1:
            multi[row["discovery_ids"][0]] = len(card["sources"])

    ordered = sorted(arch["packages"], key=lambda r: (r["drafting_order"], r["package_id"]))
    assert [p["package_id"] for p in ordered] == (
        ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B",
         "P08", "P09", "P10", "P11", "P12", "P13", "P14", "P15"])

    cited: list[str] = []
    patch_counter: dict = {}

    def cite_key(did: str) -> str:
        if did not in cited:
            cited.append(did)
        return bib_key(did)

    def cite_refs(refs) -> str:
        keys = []
        for ref in refs or []:
            did = task2did[ref["evidence_task_id"]]
            k = cite_key(did)
            if k not in keys:
                keys.append(k)
        return (r"\autocite{" + ",".join(keys) + "}") if keys else ""

    lines = [
        "% Generated deterministically from fresh-124-r9 Draft bytes + approved r9 Architecture/Profile/Synthesis authority. Do not hand-edit.",
        r"\documentclass[lualatex,a4paper,10pt]{jlreq}",
        r"\usepackage{jgaisurvey}",
        r"\usepackage{needspace}",
        r"\usepackage{booktabs}",
        r"\usepackage{tabularx}",
        r"\usepackage{array}",
        r"\usepackage{multicol}",
        r"\usepackage{xurl}",
        r"\addbibresource{references.bib}",
        "",
        r"\setlength{\columnsep}{1.45em}",
        r"\setlength{\multicolsep}{0.65em}",
        "% RPV-L01: content-driven 3.88pt vertical overfull on one body page",
        "% (rigid CJK glue under flushbottom). Set text height to an integer",
        "% number of text lines: 43 lines x 17pt baselineskip + 10pt topskip",
        "% = 741pt (jlreq 10pt; measured). Deterministic; recorded here.",
        r"\setlength{\textheight}{741pt}",
        "",
        r"\surveysetup",
        "  {SP-vision-multimodal-2026}",
        "  {Japanese Generative AI Technical Survey Special}",
        "  {Vision \\& Multimodal AI --- 視覚表現から接地・推論・行動へ / Thematic survey as of 2026-09-30}",
        "  {Open history, evidence observed through 2026-09-30 UTC}",
        r"\surveyeditiondescriptor{Thematic Longform Special}",
        "",
        r"\surveycoverstory",
        "  {Vision \\& Multimodal AI}",
        "  {視覚表現から接地・推論・行動へ。分類から位置・構造・時間・空間の表現へ、言語への接地と複数モダリティの統合を経て、推論・予測・行動へ至る技術史。}",
        "  {Representation \\quad / \\quad Detection \\quad / \\quad Dense Perception \\quad / \\quad Alignment \\quad / \\quad Grounding \\quad / \\quad Fusion \\quad / \\quad Reasoning \\quad / \\quad Video \\quad / \\quad Action \\quad / \\quad Prediction}",
        "",
        r"\begin{document}",
        r"\surveycover",
        r"\clearpage",
        "",
        r"\section*{本巻の問いと読み方}",
        r"\addcontentsline{toc}{section}{本巻の問いと読み方}",
        "本巻の問いは、画像や映像を単に分類する段階から、対象の位置・構造・時間関係を認識し、言語概念へ接地し、複数モダリティを統合して推論し、予測や行動へ利用できる内部表現を形成する段階へ、どのように発展してきたのか、である。各段階で問うのは、次の計算に十分な世界の表現は何か、何が失われ、何が新たに操作可能になったかである。",
        "",
        r"\subsection*{層の見方}",
        "本巻は単一のモデル年代記ではなく、相互に関わる技術的問題の層として読む。すなわち表現、認識、位置特定と構造、言語アライメント、接地、マルチモーダル融合、時間と空間の状態、推論、行動と予測である。これらは時代ではなく、相互作用する問題層である。",
        "",
        r"\subsection*{比較の規律}",
        "条件の異なる数値を並べて優劣をつける読みは採らない。数値は測定条件・版・日付・測り手と組で読む。ベンダーの主張は帰属づきで引用し、独立した再現を待つ。未解決の事項は推測で補わない。",
        "",
        r"\subsection*{読者への道案内}",
        "第1節から第11節が知覚・接地・融合・推論・時間の歴史、第12節から第14節が画面操作・身体動作・予測という到達点の領域、第15節が評価の方法と収束の問いを扱う。各節末の読解上の境界が、その節の射程と留保を示す。",
        "",
        r"\tableofcontents",
        r"\clearpage",
        "",
    ]

    for ordinal, plan in enumerate(ordered, start=1):
        pid = plan["package_id"]
        result = json.load(open(SRC / f"draft/v2/packages/{pid}/draft-result.json"))
        assert result.get("draft_version") == "fresh-124-r9", pid
        headline = apply_patches(result["headline"], patch_counter)
        deck = apply_patches(result["deck"], patch_counter)
        lines.append(f"% package:{pid} draft-result-sha256 bound at publication build")
        lines.append(r"\Needspace{0.20\textheight}")
        lines.append(r"\section{" + tex_escape(headline) + "}")
        lines.append(r"\sectionkicker{" + KICKERS[pid] + "}")
        lines.append(r"\label{sec:" + pid.lower() + "}")
        lines.append(r"\begin{multicols}{2}")
        lines.append(r"\raggedcolumns")
        lines.append(r"\noindent\textbf{" + tex_escape(deck) + "}"
                     + cite_refs(result.get("deck_evidence_refs")) + r"\par\medskip")
        for block in result["blocks"]:
            if block["block_type"] == "CLAIM_BOUNDARY":
                continue
            assert block["block_type"] == "PARAGRAPH", (pid, block["block_id"])
            body = apply_patches(block["text"], patch_counter)
            lines.append(r"\noindent " + tex_escape(body)
                         + cite_refs(block.get("evidence_refs")) + r"\par\medskip")
        lines.append(r"\end{multicols}")
        for block in result["blocks"]:
            if block["block_type"] != "CLAIM_BOUNDARY":
                continue
            bounds = apply_patches(block["text"], patch_counter)
            lines.append(r"\begin{claimboundary}[本節の読解上の境界]")
            lines.append(r"\noindent " + tex_escape(bounds)
                         + cite_refs(block.get("evidence_refs")) + r"\par")
            lines.append(r"\end{claimboundary}")
        lines.append("")

    syn = json.load(open(SRC / "draft/v2/profile-synthesis-result.json"))
    assert syn.get("status") == "ESTABLISHED", syn.get("status")
    lines.append(r"\Needspace{0.20\textheight}")
    lines.append(r"\section{結び}")
    lines.append(r"\sectionkicker{SYNTHESIS}")
    lines.append(r"\label{sec:synthesis}")
    lines.append(r"\begin{multicols}{2}")
    lines.append(r"\raggedcolumns")
    for key in ("branch_transition_synthesis", "parallel_competing_relations",
                "unresolved_lineage_questions", "historical_attribution_boundaries"):
        lines.append(r"\noindent " + tex_escape(syn["profile_payload"][key]) + r"\par\medskip")
    lines.append(r"\end{multicols}")
    lines.append("")
    lines.append(r"\clearpage")
    lines.append(r"\onecolumn")
    lines.append(r"\printbibliography[title={References}]")
    lines.append(r"\end{document}")
    lines.append("")

    SURVEY.mkdir(parents=True, exist_ok=True)
    (SURVEY / "main.tex").write_text("\n".join(lines), encoding="utf-8")

    bib_lines = [
        "% Bibliography for SP-vision-multimodal-2026 (Vision & Multimodal AI), Draft fresh-124-r9.",
        "% Keys are VM-D discovery IDs (vmd001..vmd125 excl. vmd122/DROP), cited from the reader-facing source.",
        "% Generated deterministically from accepted Evidence source records; no invented metadata.",
        "% Multi-source cards: five cards carry supplement license/mirror records,",
        "% counted in subject binding but not cited as bibliography locators.",
        "% PARTIAL abs-level records keep abstract-level titles; URLs/dates preserved.",
        "",
    ]
    for did in sorted(cited):
        src = src_by_did[did]
        author, title = split_author(src["title"])
        bib_lines.append(f"@online{{{bib_key(did)},")
        if author:
            bib_lines.append(f"  author  = {{{{{bib_escape(author)}}}}},")
        bib_lines.append(f"  title   = {{{bib_escape(title)}}},")
        if src.get("published_at"):
            bib_lines.append(f"  date    = {{{src['published_at']}}},")
        bib_lines.append(f"  url     = {{{src['url']}}},")
        accessed = (src.get("accessed_at") or "")[:10]
        if accessed:
            bib_lines.append(f"  urldate = {{{accessed}}},")
        bib_lines.append("}")
        bib_lines.append("")
    (SURVEY / "references.bib").write_text("\n".join(bib_lines).rstrip() + "\n", encoding="utf-8")
    for old, new, expected in PATCHES:
        got = patch_counter.get(old, 0)
        assert got == expected, (old, expected, got)
    print(json.dumps({
        "main_tex": str(SURVEY / "main.tex"),
        "references_bib": str(SURVEY / "references.bib"),
        "cited_discovery_ids": len(cited),
        "multi_source_cards": multi,
        "applied_patches": [{"old": o, "new": n, "sites": patch_counter.get(o, 0)} for o, n, _ in PATCHES],
        "packages": len(ordered),
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
