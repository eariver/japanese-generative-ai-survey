#!/usr/bin/env python3
"""Render TS-003 reader source (main.tex + references.bib) via recovery rebind.

Permitted layer (TS-003 Issue #559 bounded repair):
  1. checkpointed r1 canonical Draft authority for canonical provenance/integrity;
  2. reader-editorial-authority-r10.json for accepted reader wording (r9 + #559 A-F);
  3. approved Architecture/Profile;
  4. accepted Evidence for bibliography/citation resolution.

Must NOT read restored r1 Draft Result prose as final reader wording.
Content-preserving deterministic assembly: headline/deck/blocks/boundary text
are copied byte-identically from reader/editorial authority (TeX-escaped only);
structure (sections, TOC, front matter, synthesis reuse, bibliography) comes
from approved Architecture/Profile/Synthesis authority. No paraphrase, no new
claims, no new sources. Citations bind each block's Evidence refs to
per-discovery-ID bibliography keys (vmd001..vmd111).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
sys.path.insert(0, str(REPO))
from scripts.render_article_draft_tex import tex_escape

SRC = REPO / "sources/SP-vision-multimodal-2026"
EVID_DIR = SRC / "evidence/v2/accepted/4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34"
SURVEY = REPO / "surveys/special/vision-multimodal-2026"
READER_TITLE = "Vision & Multimodal AI — 視覚表現から接地・推論・行動へ"
AUTHORITY = SRC / "publication/editorial/reader-editorial-authority-r10.json"
CHECKPOINT = SRC / "orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json"

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


def bib_escape(value: str) -> str:
    return tex_escape(value)


def verify_canonical_integrity() -> None:
    """Checkpointed r1 canonical provenance/integrity gate (never reader wording)."""
    cp = json.load(open(CHECKPOINT, encoding="utf-8"))
    art = {a["path"]: a["sha256"] for a in cp["artifacts"]}
    for pid in ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B",
                "P08", "P09", "P10", "P11", "P12", "P13", "P14", "P15"]:
        for kind in ["draft-package.json", "draft-result.json"]:
            rel = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/{kind}"
            got = hashlib.sha256((REPO / rel).read_bytes()).hexdigest()
            assert got == art[rel], f"canonical integrity drift: {rel}"
    for rel in ["sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-input.json",
                "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-result.json"]:
        got = hashlib.sha256((REPO / rel).read_bytes()).hexdigest()
        assert got == art[rel], f"canonical integrity drift: {rel}"


def main() -> int:
    verify_canonical_integrity()
    auth = json.load(open(AUTHORITY, encoding="utf-8"))
    assert auth["issue_id"] == "SP-vision-multimodal-2026"
    assert auth["canonical_draft_authority"]["source_commit"] == "d1053e957d92cddd9d2759ec9713db59c66263ad"
    assert auth.get("reader_editorial_revision") == "r10"
    assert auth.get("parent_reader_revision") == "r9"
    assert auth["reader_editorial_authority"]["accepted_r9_commit"] == "79d2b3e291e10896ed616bd698abefc1e479ddbe"
    by_pid = {p["package_id"]: p for p in auth["reader_packages"]}

    arch = json.load(open(SRC / "architecture-v2.json"))
    mat = json.load(open(SRC / "candidate-matrix-v2.json"))
    task2did = {}
    for row in mat["rows"]:
        assert len(row["discovery_ids"]) == 1
        task2did[row["evidence_task_id"]] = row["discovery_ids"][0]
    acc = json.load(open(EVID_DIR / "evidence-accepted.json"))
    src_by_did = {}
    for row in acc["results"]:
        assert len(row["discovery_ids"]) == 1
        card = json.load(open(EVID_DIR / "results" / row["filename"]))
        assert len(card.get("sources", [])) == 1, row["discovery_ids"]
        src_by_did[row["discovery_ids"][0]] = card["sources"][0]

    ordered = sorted(arch["packages"], key=lambda r: (r["drafting_order"], r["package_id"]))
    assert [p["package_id"] for p in ordered] == (
        ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B",
         "P08", "P09", "P10", "P11", "P12", "P13", "P14", "P15"])
    assert auth["architecture_package_order"] == [p["package_id"] for p in ordered]

    cited: list[str] = []

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
        "% Generated deterministically from checkpointed canonical Draft r1 + edition-local Sol-accepted reader/editorial transformation (reader-editorial-authority-r10.json) + approved Architecture/Profile/Synthesis authority. Do not hand-edit.",
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
        result = by_pid[pid]
        lines.append(f"% package:{pid} reader-editorial-authority-r10 bound at publication build (canonical r1 provenance verified, wording from editorial authority)")
        lines.append(r"\Needspace{0.20\textheight}")
        lines.append(r"\section{" + tex_escape(result["headline"]) + "}")
        lines.append(r"\sectionkicker{" + KICKERS[pid] + "}")
        lines.append(r"\label{sec:" + pid.lower() + "}")
        lines.append(r"\begin{multicols}{2}")
        lines.append(r"\raggedcolumns")
        lines.append(r"\noindent\textbf{" + tex_escape(result["deck"]) + "}"
                     + cite_refs(result.get("deck_evidence_refs")) + r"\par\medskip")
        for block in result["ordered_blocks"]:
            if block["block_type"] == "CLAIM_BOUNDARY":
                continue
            assert block["block_type"] == "PARAGRAPH", (pid, block["block_id"])
            lines.append(r"\noindent " + tex_escape(block["reader_text"])
                         + cite_refs(block.get("evidence_refs")) + r"\par\medskip")
        lines.append(r"\end{multicols}")
        for block in result["ordered_blocks"]:
            if block["block_type"] != "CLAIM_BOUNDARY":
                continue
            lines.append(r"\begin{claimboundary}[本節の読解上の境界]")
            lines.append(r"\noindent " + tex_escape(block["reader_text"])
                         + cite_refs(block.get("evidence_refs")) + r"\par")
            lines.append(r"\end{claimboundary}")
        lines.append("")

    syn_payload = auth["reader_synthesis"]["profile_payload"]
    lines.append(r"\Needspace{0.20\textheight}")
    lines.append(r"\section{結び}")
    lines.append(r"\sectionkicker{SYNTHESIS}")
    lines.append(r"\label{sec:synthesis}")
    lines.append(r"\begin{multicols}{2}")
    lines.append(r"\raggedcolumns")
    for key in ("branch_transition_synthesis", "parallel_competing_relations",
                "unresolved_lineage_questions", "historical_attribution_boundaries"):
        lines.append(r"\noindent " + tex_escape(syn_payload[key]) + r"\par\medskip")
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
        "% Bibliography for SP-vision-multimodal-2026 (Vision & Multimodal AI), reader-editorial authority r9.",
        "% Keys are VM-D discovery IDs (vmd001..vmd111), cited from the reader-facing source.",
        "% Generated deterministically from accepted Evidence source records; no invented metadata.",
        "% PARTIAL abs-level records keep abstract-level titles; URLs/dates preserved.",
        "% Reader wording from reader-editorial-authority-r10.json; canonical provenance is checkpointed r1.",
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
    print(json.dumps({
        "main_tex": str(SURVEY / "main.tex"),
        "references_bib": str(SURVEY / "references.bib"),
        "cited_discovery_ids": len(cited),
        "packages": len(ordered),
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
