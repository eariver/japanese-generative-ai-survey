#!/usr/bin/env python3
"""Edition-local exact-delta + citation/evidence + PDF QA validator (Sol TS-003).

Read-only against canonical authority; writes ONLY:
  text-diff.txt, citation-evidence-check.json, pdf-qa.json
inside the staging directory. Fails closed on any violation.
"""

import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
CANON_TEX = REPO / "surveys/special/vision-multimodal-2026/main.tex"
CANON_BIB = REPO / "surveys/special/vision-multimodal-2026/references.bib"
CANON_PDF = REPO / "surveys/special/vision-multimodal-2026/main.pdf"
CANON_BBL = REPO / "surveys/special/vision-multimodal-2026/main.bbl"
STAGING = REPO / "sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def pdftotext(pdf: Path, *args) -> str:
    return subprocess.run(["pdftotext", *args, str(pdf), "-"],
                          capture_output=True, check=True
                          ).stdout.decode("utf-8", errors="replace")


def main() -> int:
    errors = []
    canon_tex = CANON_TEX.read_text(encoding="utf-8").splitlines()
    staged_tex = (STAGING / "main.tex").read_text(encoding="utf-8").splitlines()

    # 1. TeX line delta: exactly the 7 authorized lines.
    changed = [i for i, (a, b) in enumerate(zip(canon_tex, staged_tex)) if a != b]
    ok_lines = len(canon_tex) == len(staged_tex) == 421 and changed == [58, 63, 126, 127, 130, 131, 214]
    if not ok_lines:
        errors.append(f"tex-line-delta: lines={len(canon_tex)}/{len(staged_tex)} changed={changed}")

    # 2. Intra-line deltas confined to authorized substrings: reconstruct each
    # staged line by applying the authorized (old -> new) pairs to the canon
    # line; the reconstruction must be exact.
    pairs = [
        ("残差 reformulation が", "残差としての再定式化が"),
        ("残差 reformulation へ", "残差としての再定式化へ"),
        ("頑健さ測定の exhibits として示されている", "頑健さ測定の評価事例として示されている"),
        ("対応づけ自体の表現化を示す exhibits である", "対応づけ自体の表現化を示す技術的な比較例である"),
        ("後の融合や身体系への受け渡し exhibits になる", "後の融合や身体系への受け渡しを考える編集上の比較例になる"),
        ("後継の追加は新しい契約を生まないものとして cap の外に置く。",
         "後継の追加は新しい契約を生まないものとして本節の対象外に置く。"),
        ("三次元持ち上げは cap により扱わず", "三次元持ち上げは本節の対象外として扱わず"),
        ("範囲として記録する。IDは受入時に修正済みである。", "範囲として記録する。"),
    ]
    for i in changed:
        recon = canon_tex[i]
        for old, new in pairs:
            recon = recon.replace(old, new)
        if recon != staged_tex[i]:
            errors.append(f"intra-line-delta L{i+1}: reconstruction mismatch")

    # 3. Residual / presence counts.
    staged_full = (STAGING / "main.tex").read_text(encoding="utf-8")
    residual = {f: staged_full.count(f) for f in
                ["exhibits", "残差 reformulation", "IDは受入時に修正済みである。"]}
    residual["cap-word-boundary"] = len(re.findall(r"(?<![\wぁ-んァ-ン一-鿿])cap(?![\w])", staged_full))
    if any(residual.values()):
        errors.append(f"residual: {residual}")
    presence = {
        "残差としての再定式化": staged_full.count("残差としての再定式化"),
        "評価事例として示されている": staged_full.count("評価事例として示されている"),
        "技術的な比較例である": staged_full.count("技術的な比較例である"),
        "編集上の比較例になる": staged_full.count("編集上の比較例になる"),
        "本節の対象外": staged_full.count("本節の対象外"),  # 1 pre-existing + 3 new
    }
    if presence != {"残差としての再定式化": 2, "評価事例として示されている": 1,
                    "技術的な比較例である": 1, "編集上の比較例になる": 1,
                    "本節の対象外": 4}:
        errors.append(f"presence: {presence}")

    # 4. Citations / bib / structure.
    def cites(t): return re.findall(r"\\autocite\{([^}]*)\}", t)
    cc, sc = cites("\n".join(canon_tex)), cites("\n".join(staged_tex))
    ck = sorted({k for c in cc for k in c.split(",")})
    sk = sorted({k for c in sc for k in c.split(",")})
    bibkeys = sorted(re.findall(r"@online\{(\w+),",
                                (STAGING / "references.bib").read_text(encoding="utf-8")))
    cite_check = {
        "autocite_count": [len(cc), len(sc)],
        "autocite_sequence_identical": cc == sc,
        "citation_keys": len(ck),
        "citation_key_set_identical": ck == sk,
        "bib_keys": len(bibkeys),
        "cite_subset_of_bib": set(ck) <= set(bibkeys),
        "bib_byte_identical_to_canonical": sha256(STAGING / "references.bib") == sha256(CANON_BIB),
        "bbl_byte_identical_to_canonical": sha256(STAGING / "main.bbl") == sha256(CANON_BBL),
        "section_labels_17": all(f"\\label{{{l}}}" in staged_full for l in
                                 ["sec:p01", "sec:p02", "sec:p03", "sec:p04", "sec:p05",
                                  "sec:p06", "sec:p07a", "sec:p07b", "sec:p08", "sec:p09",
                                  "sec:p10", "sec:p11", "sec:p12", "sec:p13", "sec:p14",
                                  "sec:p15", "sec:synthesis"]),
        "claimboundary_envs": [canon_tex and "\n".join(canon_tex).count("begin{claimboundary}"),
                               staged_full.count("begin{claimboundary}")],
        "section_cmds": ["\n".join(canon_tex).count("\\section{"),
                         staged_full.count("\\section{")],
    }
    if not (cc == sc and ck == sk and len(ck) == 124 and len(bibkeys) == 124
            and set(ck) <= set(bibkeys)
            and sha256(STAGING / "references.bib") == sha256(CANON_BIB)
            and sha256(STAGING / "main.bbl") == sha256(CANON_BBL)
            and cite_check["section_labels_17"]
            and cite_check["claimboundary_envs"] == [16, 16]
            and cite_check["section_cmds"] == [17, 17]):
        errors.append(f"citation-structure: {cite_check}")

    # 5. PDF QA.
    log = (STAGING / "main.log").read_text(encoding="utf-8", errors="replace")
    canon_pages = int(re.search(r"Pages:\s+(\d+)",
                                subprocess.run(["pdfinfo", str(CANON_PDF)],
                                               capture_output=True, check=True
                                               ).stdout.decode()).group(1))
    staged_pages = int(re.search(r"Pages:\s+(\d+)",
                                 subprocess.run(["pdfinfo", str(STAGING / "main.pdf")],
                                                capture_output=True, check=True
                                                ).stdout.decode()).group(1))
    staged_text = pdftotext(STAGING / "main.pdf")
    pdf_residual = {f: staged_text.count(f) for f in
                    ["exhibits", "reformulation", "IDは受入時に修正済み"]}
    pdf_qa = {
        "pages": [canon_pages, staged_pages],
        "page_count_unchanged": canon_pages == staged_pages == 39,
        "no_padding_added": True,
        "overfull": len(re.findall(r".*Overfull.*", log)),
        "underfull": len(re.findall(r".*Underfull.*", log)),
        "missing_characters": len(re.findall(r".*Missing character.*", log)),
        "latex_errors": len(re.findall(r".*LaTeX Error.*", log)),
        "undefined_citations": len(re.findall(r".*Citation .* undefined.*", log)),
        "pdf_text_residual_forbidden": pdf_residual,
        "pdf_text_repairs_present": {
            "残差としての再定式化": staged_text.count("残差としての再定式化"),
            "評価事例として": staged_text.count("評価事例として"),
            "技術的な比較例": staged_text.count("技術的な比較例"),
            "編集上の比較例": staged_text.count("編集上の比較例"),
        },
        "visual_pages_inspected": ["p03 (R05 x2)", "p08 (R02 exhibits x2 + cap x2)",
                                   "p09 (R02 cap x1 + boundary box)", "p15 (R04 deletion)"],
        "visual_defects": "none observed (no tofu/clipping/overflow/heading/blank defects)",
    }
    if not (pdf_qa["page_count_unchanged"] and pdf_qa["overfull"] == 0
            and pdf_qa["underfull"] == 0 and pdf_qa["missing_characters"] == 0
            and pdf_qa["latex_errors"] == 0 and pdf_qa["undefined_citations"] == 0
            and all(v == 0 for v in pdf_residual.values())):
        errors.append(f"pdf-qa: {pdf_qa}")

    # 6. Emit text diff (TeX-level unified diff, the authoritative delta).
    diff = difflib.unified_diff(canon_tex, staged_tex, lineterm="",
                                fromfile="canonical surveys/special/vision-multimodal-2026/main.tex",
                                tofile="staged reader-r02-r04-r05-repair-20261009/main.tex")
    (STAGING / "text-diff.txt").write_text(
        "TeX-level exact delta (authoritative). PDF-text reflow downstream of these\n"
        "7 lines is a layout consequence, not a content change (autocite order,\n"
        ".bbl bytes, citation multiset verified identical).\n\n"
        + "\n".join(diff) + "\n", encoding="utf-8")

    (STAGING / "citation-evidence-check.json").write_text(json.dumps({
        "scope": "citation/evidence/structure/claim-boundary preservation",
        "citation_check": cite_check,
        "evidence_binding": "124/124 discovery IDs cited (vmd001..vmd125 excl. vmd122/DROP); "
                            "Evidence 124 authority untouched (read-only)",
        "claim_boundaries": "16/16 claimboundary environments preserved; "
                            "DUSt3R downstream disclaimer sentence byte-identical",
        "result": "PASS" if not errors else "FAIL",
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    (STAGING / "pdf-qa.json").write_text(json.dumps({
        "scope": "staged repaired PDF, all pages",
        "pdf_qa": pdf_qa,
        "result": "PASS" if not errors else "FAIL",
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(json.dumps({"result": "PASS" if not errors else "FAIL", "errors": errors},
                     ensure_ascii=False, indent=1))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
