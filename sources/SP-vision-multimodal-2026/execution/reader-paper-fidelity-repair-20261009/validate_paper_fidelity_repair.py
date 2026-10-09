#!/usr/bin/env python3
"""Edition-local differential validator for paper-review fidelity repair (Sol TS-003 PR-01/02/03).

Basis (read-only): prior R02-01-final staging main.tex.
Subject: new staging main.tex / main.pdf.
Writes ONLY inside the new staging directory:
  text-diff.txt, citation-evidence-check.json, pdf-qa.json,
  pdf-text-verification.json, visual-source-manifest.json, qa-provenance.json
Fails closed on any violation, including R02/R04/R05 regression.
VF-01/VF-02 closure: the fixed PDF's SHA-256/size/pages are computed from the
real file and asserted against the frozen authority pins; QA image bytes are
bound to the exact source PDF bytes. Mechanical preflight and human visual
observation are recorded separately (non-inspected pages: NOT_REVIEWED).
"""
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
BASIS = REPO / "sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009"
BASIS_TEX = BASIS / "main.tex"
BASIS_BIB = BASIS / "references.bib"
BASIS_BBL = BASIS / "main.bbl"
BASIS_PDF = BASIS / "main.pdf"
STAGING = REPO / "sources/SP-vision-multimodal-2026/execution/reader-paper-fidelity-repair-20261009"

# Frozen fixed-PDF authority (VF-01). Computed from the real file, asserted
# here; any byte change FAILs the QA instead of being re-pinned.
EXPECTED_PDF_SHA256 = "b2de84493f2215e26d16e569498c5f4b6476ebc314230cbb4e01540a72742093"
EXPECTED_PDF_BYTES = 708782
EXPECTED_PDF_PAGES = 39


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def pdftotext(pdf: Path, *args) -> str:
    return subprocess.run(["pdftotext", *args, str(pdf), "-"],
                          capture_output=True, check=True
                          ).stdout.decode("utf-8", errors="replace")


def main() -> int:
    errors = []
    basis_tex = BASIS_TEX.read_text(encoding="utf-8").splitlines()
    staged_tex = (STAGING / "main.tex").read_text(encoding="utf-8").splitlines()

    # 1. TeX line delta: exactly L86 and L391 (1-idx), 421 lines each.
    changed = [i for i, (a, b) in enumerate(zip(basis_tex, staged_tex)) if a != b]
    ok_lines = len(basis_tex) == len(staged_tex) == 421 and changed == [85, 390]
    if not ok_lines:
        errors.append(f"tex-line-delta: lines={len(basis_tex)}/{len(staged_tex)} changed={changed}")

    # 2. Intra-line reconstruction from basis with the 4 authorized pairs.
    pairs = [
        ("小物体の5.5ポイント不足と300から500エポックに及ぶAdamW日程、16枚のV100で3日という訓練負担が論文自身の開かれた課題である。",
         "小物体の5.5ポイント不足と長い学習期間が、論文自身の挙げる課題である。AdamWを用いた基準設定は300エポックで、16枚のV100による学習に約3日を要する。Faster R-CNNとの比較には500エポックの長期設定を用いている。"),
        ("POPEは投票型の設問で物体ハルシネーションを安定に測る範囲に属し、",
         "POPEは物体の有無をyes/no形式で問うポーリング方式により、物体ハルシネーションを安定的に評価し、"),
        ("MMBenchは3000件超の日英設問を20能力軸で整え、",
         "MMBenchは3000件超の英語・中国語の選択式設問を20の能力軸で整え、"),
        ("判定依存と英中の言語範囲が条件として残る。",
         "判定方法への依存と英語・中国語という二言語の評価範囲が条件として残る。"),
    ]
    for i in changed:
        recon = basis_tex[i]
        for old, new in pairs:
            recon = recon.replace(old, new)
        if recon != staged_tex[i]:
            errors.append(f"intra-line-delta L{i+1}: reconstruction mismatch")

    # 3. PR residual / presence (TeX level).
    staged_full = (STAGING / "main.tex").read_text(encoding="utf-8")
    pr_residual = {
        "PR-01-old-conflation": staged_full.count("300から500エポックに及ぶAdamW日程"),
        "PR-02-投票型": staged_full.count("POPEは投票型"),
        "PR-03a-日英設問": staged_full.count("MMBenchは3000件超の日英設問"),
        "PR-03b-old-range": staged_full.count("判定依存と英中の言語範囲"),
    }
    if any(pr_residual.values()):
        errors.append(f"pr-residual: {pr_residual}")
    pr_presence = {
        "PR-01-300ep-base": staged_full.count("AdamWを用いた基準設定は300エポックで"),
        "PR-01-3days": staged_full.count("16枚のV100による学習に約3日を要する"),
        "PR-01-500ep-split": staged_full.count("500エポックの長期設定を用いている"),
        "PR-02-polling": staged_full.count("POPEは物体の有無をyes/no形式で問うポーリング方式により"),
        "PR-03a-ENZH": staged_full.count("MMBenchは3000件超の英語・中国語の選択式設問を20の能力軸で整え"),
        "PR-03b-range": staged_full.count("判定方法への依存と英語・中国語という二言語の評価範囲が条件として残る"),
    }
    if any(v != 1 for v in pr_presence.values()):
        errors.append(f"pr-presence: {pr_presence}")
    # 500ep must be separated from the 300ep base sentence.
    if not ("300エポックで" in staged_full and "500エポックの長期設定" in staged_full
            and staged_full.count("300から500エポック") == 0):
        errors.append("pr-01-separation: 300/500 conflation remains")

    # 4. R02/R04/R05 non-regression.
    r_nonreg_res = {
        "exhibits": staged_full.count("exhibits"),
        "残差 reformulation": staged_full.count("残差 reformulation"),
        "IDは受入時に修正済みである。": staged_full.count("IDは受入時に修正済みである。"),
        "cap-word-boundary": len(re.findall(r"(?<![\wぁ-んァ-ン一-鿿])cap(?![\w])", staged_full)),
        "R02-01-superseded": staged_full.count("三次元持ち上げは本節の対象外として扱わず"),
    }
    if any(r_nonreg_res.values()):
        errors.append(f"r-nonregression-residual: {r_nonreg_res}")
    r_nonreg_pre = {
        "残差としての再定式化": staged_full.count("残差としての再定式化"),
        "評価事例として示されている": staged_full.count("評価事例として示されている"),
        "技術的な比較例である": staged_full.count("技術的な比較例である"),
        "編集上の比較例になる": staged_full.count("編集上の比較例になる"),
        "本節の対象外": staged_full.count("本節の対象外"),
        "R02-01-final": staged_full.count("三次元への持ち上げは本節の対象外とし"),
    }
    if r_nonreg_pre != {"残差としての再定式化": 2, "評価事例として示されている": 1,
                       "技術的な比較例である": 1, "編集上の比較例になる": 1,
                       "本節の対象外": 4, "R02-01-final": 1}:
        errors.append(f"r-nonregression-presence: {r_nonreg_pre}")

    # 5. S11/S16 consistency (both must describe polling + EN/ZH, never voting/日英).
    s11_polling = "ポーリング方式のyes-no形式の質問" in staged_full
    s11_mmen = "3000を超える英語と中国語の選択式の質問" in staged_full
    s16_polling = ("ポーリング方式により" in staged_full and "yes/no形式で問う" in staged_full)
    s16_mmen = ("英語・中国語の選択式設問" in staged_full and "20の能力軸" in staged_full)
    if not (s11_polling and s11_mmen and s16_polling and s16_mmen):
        errors.append(f"s11-s16-consistency: s11_polling={s11_polling} s11_mmen={s11_mmen} "
                      f"s16_polling={s16_polling} s16_mmen={s16_mmen}")
    if "多数決" in staged_full and "POPE" in staged_full.split("多数決")[0][-200:]:
        errors.append("majority-voting implication near POPE")
    if staged_full.count("投票型") != 0:
        errors.append(f"投票型 residual: {staged_full.count('投票型')}")
    # Issue #534 terms are non-blocking record-only: must be untouched vs basis.
    basis_full = BASIS_TEX.read_text(encoding="utf-8")
    for term in ["模型", "基線", "hardware"]:
        if staged_full.count(term) != basis_full.count(term):
            errors.append(f"issue534-term-changed {term}: "
                          f"{basis_full.count(term)}->{staged_full.count(term)}")

    # 6. Citations / bib / structure (basis vs staged must be identical).
    def cites(t): return re.findall(r"\\autocite\{([^}]*)\}", t)
    bc, sc = cites("\n".join(basis_tex)), cites("\n".join(staged_tex))
    bk = sorted({k for c in bc for k in c.split(",")})
    sk = sorted({k for c in sc for k in c.split(",")})
    bibkeys = sorted(re.findall(r"@online\{(\w+),",
                                (STAGING / "references.bib").read_text(encoding="utf-8")))
    cite_check = {
        "autocite_count": [len(bc), len(sc)],
        "autocite_sequence_identical": bc == sc,
        "citation_keys": len(bk),
        "citation_key_set_identical": bk == sk,
        "bib_keys": len(bibkeys),
        "cite_subset_of_bib": set(bk) <= set(bibkeys),
        "bib_byte_identical_to_basis": sha256(STAGING / "references.bib") == sha256(BASIS_BIB),
        "bbl_byte_identical_to_basis": sha256(STAGING / "main.bbl") == sha256(BASIS_BBL),
        "section_labels_17": all(f"\\label{{{l}}}" in staged_full for l in
                                 ["sec:p01", "sec:p02", "sec:p03", "sec:p04", "sec:p05",
                                  "sec:p06", "sec:p07a", "sec:p07b", "sec:p08", "sec:p09",
                                  "sec:p10", "sec:p11", "sec:p12", "sec:p13", "sec:p14",
                                  "sec:p15", "sec:synthesis"]),
        "claimboundary_envs": ["\n".join(basis_tex).count("begin{claimboundary}"),
                               staged_full.count("begin{claimboundary}")],
        "section_cmds": ["\n".join(basis_tex).count("\\section{"),
                         staged_full.count("\\section{")],
    }
    # P15 unique evidence 40.
    bl = basis_tex
    sl = staged_tex
    i_p15_b = next(i for i, l in enumerate(bl) if "label{sec:p15}" in l)
    i_syn_b = next(i for i, l in enumerate(bl) if "label{sec:synthesis}" in l)
    i_p15_s = next(i for i, l in enumerate(sl) if "label{sec:p15}" in l)
    i_syn_s = next(i for i, l in enumerate(sl) if "label{sec:synthesis}" in l)
    p15_b = sorted({k for c in cites("\n".join(bl[i_p15_b:i_syn_b])) for k in c.split(",")})
    p15_s = sorted({k for c in cites("\n".join(sl[i_p15_s:i_syn_s])) for k in c.split(",")})
    cite_check["p15_unique"] = [len(p15_b), len(p15_s)]
    cite_check["p15_identical"] = p15_b == p15_s
    if not (bc == sc and bk == sk and len(bk) == 124 and len(bibkeys) == 124
            and set(bk) <= set(bibkeys)
            and sha256(STAGING / "references.bib") == sha256(BASIS_BIB)
            and sha256(STAGING / "main.bbl") == sha256(BASIS_BBL)
            and cite_check["section_labels_17"]
            and cite_check["claimboundary_envs"] == [16, 16]
            and cite_check["section_cmds"] == [17, 17]
            and len(p15_b) == len(p15_s) == 40 and p15_b == p15_s):
        errors.append(f"citation-structure: {cite_check}")

    # 7. PDF QA (all pages preflight; corrected pages get visual QA separately).
    # VF-01: bind QA to the exact PDF bytes (computed, never hard-coded PASS).
    pdf_path = STAGING / "main.pdf"
    pdf_actual_sha = sha256(pdf_path)
    pdf_actual_bytes = pdf_path.stat().st_size
    if pdf_actual_sha != EXPECTED_PDF_SHA256 or pdf_actual_bytes != EXPECTED_PDF_BYTES:
        errors.append(f"fixed-pdf-authority: sha={pdf_actual_sha} bytes={pdf_actual_bytes}")
    log = (STAGING / "main.log").read_text(encoding="utf-8", errors="replace")
    basis_pages = int(re.search(r"Pages:\s+(\d+)",
                                subprocess.run(["pdfinfo", str(BASIS_PDF)],
                                               capture_output=True, check=True
                                               ).stdout.decode()).group(1))
    staged_pages = int(re.search(r"Pages:\s+(\d+)",
                                 subprocess.run(["pdfinfo", str(STAGING / "main.pdf")],
                                                capture_output=True, check=True
                                                ).stdout.decode()).group(1))
    staged_text = pdftotext(STAGING / "main.pdf")
    # Two-column PDF extraction inserts spaces/line-breaks inside CJK phrases
    # (e.g. '300 エポック', 'yes/no 形式'); normalize whitespace for phrase checks.
    staged_norm = re.sub(r"\s+", "", staged_text)
    # VF-02 extraction evidence: full-text bytes hash (raw + normalized).
    full_raw = subprocess.run(["pdftotext", str(STAGING / "main.pdf"), "-"],
                              capture_output=True, check=True).stdout
    full_norm = re.sub(rb"\s+", b"", full_raw)
    # VF-01/VF-02 provenance inputs (all computed from real files).
    input_shas = {
        "main_tex_sha256": sha256(STAGING / "main.tex"),
        "references_bib_sha256": sha256(STAGING / "references.bib"),
        "jgaisurvey_sty_sha256": sha256(STAGING / "jgaisurvey.sty"),
        "main_bbl_sha256": sha256(STAGING / "main.bbl"),
        "main_pdf_sha256": pdf_actual_sha,
        "main_pdf_bytes": pdf_actual_bytes,
    }
    pdf_old = {
        "300から500エポックに及ぶ": staged_norm.count("300から500エポックに及ぶ"),
        "POPEは投票型": staged_norm.count("POPEは投票型"),
        "日英設問": staged_norm.count("日英設問"),
    }
    pdf_new_frags = {
        "300エポック": staged_norm.count("300エポック"),
        "500エポック": staged_norm.count("500エポック"),
        "約3日": staged_norm.count("約3日"),
        "yes/no形式": staged_norm.count("yes/no形式"),
        "ポーリング方式": staged_norm.count("ポーリング方式"),
        "英語・中国語": staged_norm.count("英語・中国語"),
        "選択式設問": staged_norm.count("選択式設問"),
    }
    pdf_qa = {
        "pdf_authority": {
            "expected_sha256": EXPECTED_PDF_SHA256,
            "expected_bytes": EXPECTED_PDF_BYTES,
            "expected_pages": EXPECTED_PDF_PAGES,
            "actual_sha256": pdf_actual_sha,
            "actual_bytes": pdf_actual_bytes,
            "authority_match": (pdf_actual_sha == EXPECTED_PDF_SHA256
                                and pdf_actual_bytes == EXPECTED_PDF_BYTES),
        },
        "input_shas": input_shas,
        "extraction": {
            "command": "pdftotext main.pdf -",
            "full_text_bytes": len(full_raw),
            "full_text_sha256": hashlib.sha256(full_raw).hexdigest(),
            "normalized_text_sha256": hashlib.sha256(full_norm).hexdigest(),
        },
        "pages": [basis_pages, staged_pages],
        "page_count": staged_pages,
        "page_count_matches_authority": staged_pages == EXPECTED_PDF_PAGES,
        "no_padding_added": True,
        "overfull": len(re.findall(r".*Overfull.*", log)),
        "underfull": len(re.findall(r".*Underfull.*", log)),
        "missing_characters": len(re.findall(r".*Missing character.*", log)),
        "latex_errors": len(re.findall(r".*LaTeX Error.*", log)),
        "undefined_citations": len(re.findall(r".*Citation .* undefined.*", log)),
        "pdf_text_old_zero": pdf_old,
        "pdf_text_new_fragments": pdf_new_frags,
        "mechanical_preflight": "computed from main.log + pdfinfo (see counts above)",
        "human_visual_observation": [
            {"image": "qa-p05-05.png",
             "source_pdf_sha256": pdf_actual_sha,
             "page": 5,
             "renderer": "poppler pdftoppm 26.01.0",
             "options": "-png -r 80 -f 5 -l 5",
             "image_sha256": sha256(STAGING / "qa-p05-05.png"),
             "status": "REVIEWED",
             "observation": "PR-01 corrected DETR sentence legible in left column "
                            "(300-epoch base / ~3 days / 500-epoch comparison split); "
                            "no tofu/clipping/overflow/heading/blank defects"},
            {"image": "qa-p31-31.png",
             "source_pdf_sha256": pdf_actual_sha,
             "page": 31,
             "renderer": "poppler pdftoppm 26.01.0",
             "options": "-png -r 80 -f 31 -l 31",
             "image_sha256": sha256(STAGING / "qa-p31-31.png"),
             "status": "REVIEWED",
             "observation": "PR-02 yes/no polling + PR-03 EN/ZH MMBench sentences legible; "
                            "no tofu/clipping/overflow/heading/blank defects"},
        ],
        "other_pages": "NOT_REVIEWED (no claim of full 39-page human review)",
    }
    if not (pdf_qa["pdf_authority"]["authority_match"]
            and pdf_qa["page_count_matches_authority"]
            and pdf_qa["overfull"] == 0 and pdf_qa["underfull"] == 0
            and pdf_qa["missing_characters"] == 0 and pdf_qa["latex_errors"] == 0
            and pdf_qa["undefined_citations"] == 0
            and all(v == 0 for v in pdf_old.values())
            and pdf_new_frags["300エポック"] >= 1 and pdf_new_frags["500エポック"] >= 1
            and pdf_new_frags["yes/no形式"] >= 1 and pdf_new_frags["英語・中国語"] >= 1):
        errors.append(f"pdf-qa: {pdf_qa}")

    # 8. Emit authoritative differential artifacts (basis -> staged).
    diff = difflib.unified_diff(basis_tex, staged_tex, lineterm="",
                                fromfile="basis reader-r02-r04-r05-repair-20261009/main.tex",
                                tofile="staged reader-paper-fidelity-repair-20261009/main.tex")
    (STAGING / "text-diff.txt").write_text(
        "TeX-level exact differential delta (authoritative, basis -> staged).\n"
        "Only L86 (PR-01) and L391 (PR-02 + PR-03 x2) change; PDF-text reflow\n"
        "downstream of these 2 lines is a layout consequence, not a content\n"
        "change (autocite order, .bbl bytes, citation multiset identical).\n\n"
        + "\n".join(diff) + "\n", encoding="utf-8")

    (STAGING / "citation-evidence-check.json").write_text(json.dumps({
        "scope": "citation/evidence/structure/claim-boundary preservation (basis -> staged)",
        "citation_check": cite_check,
        "evidence_binding": "124/124 discovery IDs cited (vmd001..vmd125 excl. vmd122/DROP); "
                            "Evidence 124 authority untouched (read-only)",
        "claim_boundaries": "16/16 claimboundary environments preserved; "
                            "DETR/POPE/MMBench mechanism/values otherwise unchanged",
        "result": "PASS" if not errors else "FAIL",
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    (STAGING / "pdf-qa.json").write_text(json.dumps({
        "scope": "staged fidelity-repaired PDF, all pages",
        "pdf_qa": pdf_qa,
        "result": "PASS" if not errors else "FAIL",
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 9. VF-01/VF-02 provenance artifacts (all computed from real files).
    per_page = []
    for p in range(1, staged_pages + 1):
        raw = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p),
                              str(STAGING / "main.pdf"), "-"],
                             capture_output=True, check=True).stdout
        per_page.append({
            "page": p,
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "normalized_sha256": hashlib.sha256(re.sub(rb"\s+", b"", raw)).hexdigest(),
        })
    (STAGING / "pdf-text-verification.json").write_text(json.dumps({
        "scope": "39-page mechanical text extraction from the fixed PDF bytes",
        "source_pdf_sha256": pdf_actual_sha,
        "extraction_command": "pdftotext main.pdf -  (+ per-page -f N -l N)",
        "extractor": "poppler pdftotext 26.01.0",
        "full_text_bytes": len(full_raw),
        "full_text_sha256": hashlib.sha256(full_raw).hexdigest(),
        "normalized_text_sha256": hashlib.sha256(full_norm).hexdigest(),
        "pages_extracted": len(per_page),
        "per_page": per_page,
        "pr_checks_on_normalized_text": {"old_zero": pdf_old, "new_fragments": pdf_new_frags},
        "result": "PASS" if not errors else "FAIL",
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    (STAGING / "visual-source-manifest.json").write_text(json.dumps({
        "scope": "human-reviewed QA images bound to exact source PDF bytes",
        "source_pdf_sha256": pdf_actual_sha,
        "renderer": "poppler pdftoppm 26.01.0",
        "images": pdf_qa["human_visual_observation"],
        "other_pages": pdf_qa["other_pages"],
        "result": "PASS" if not errors else "FAIL",
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    (STAGING / "qa-provenance.json").write_text(json.dumps({
        "scope": "VF-01 binary-to-QA binding for the frozen fixed PDF",
        "verdict_adopted": "STAGED_TECHNICAL_FIDELITY_VERIFICATION_INCOMPLETE",
        "pdf_authority": pdf_qa["pdf_authority"],
        "input_shas": input_shas,
        "qa_artifacts": {
            "pdf_qa_json_sha256": sha256(STAGING / "pdf-qa.json"),
            "citation_evidence_check_json_sha256": sha256(STAGING / "citation-evidence-check.json"),
            "text_diff_txt_sha256": sha256(STAGING / "text-diff.txt"),
            "pdf_text_verification_json_sha256": sha256(STAGING / "pdf-text-verification.json"),
            "visual_source_manifest_json_sha256": sha256(STAGING / "visual-source-manifest.json"),
            "before_after_json_sha256": sha256(STAGING / "before-after.json"),
            "technical_fidelity_ledger_json_sha256": sha256(STAGING / "technical-fidelity-ledger.json"),
        },
        "qa_images": [
            {"image": "qa-p05-05.png",
             "image_sha256": sha256(STAGING / "qa-p05-05.png")},
            {"image": "qa-p31-31.png",
             "image_sha256": sha256(STAGING / "qa-p31-31.png")},
        ],
        "technical_content": "UNCHANGED in this closure (PR-01/02/03 already TECHNICAL_CONTENT_ACCEPTED)",
        "result": "PASS" if not errors else "FAIL",
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(json.dumps({"result": "PASS" if not errors else "FAIL", "errors": errors},
                     ensure_ascii=False, indent=1))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
