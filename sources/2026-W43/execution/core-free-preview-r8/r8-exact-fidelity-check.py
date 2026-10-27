#!/usr/bin/env python3
"""r8 exact prose fidelity checker (edition-local).

Proves fixed r7 TeX -> r8 TeX preservation with ONLY the three authorised
A/B/C replacements, and detects ordinary-prose semantic inversions (N10).

Strategy:
  expected = immutable fixed r7 TeX with exactly A/B/C whitelisted substitutions
  actual   = candidate r8 TeX file
  clean PASS requires full byte/UTF-8 visible-body identity plus structural
  preservation (tables/rows/cells, figures, code, recap, bib, claims, TOC,
  qualifiers, meta, layout, proof). No global token bag, count-only oracle,
  missing-paragraph skip, or excessive normalization.

Usage:
  python3 r8-exact-fidelity-check.py --repo-root <repo> [--tex PATH]
      [--staged-dir DIR] [--mode clean|negatives]

Exit 0 on PASS / NEGATIVES_PASS. Distinct fail causes:
  READER_META_LEAK, LAYOUT_NOT_TWO_COLUMN, ROW_CELL_CLAIM_LOSS,
  SCIENTIFIC_QUALIFIER_LOSS, DOC_PROOF_STATUS_MISSING, PROSE_FIDELITY_LOSS.
"""
import argparse, hashlib, json, pathlib, re, sys

FAIL = {"READER_META_LEAK": [], "LAYOUT_NOT_TWO_COLUMN": [],
        "ROW_CELL_CLAIM_LOSS": [], "SCIENTIFIC_QUALIFIER_LOSS": [],
        "DOC_PROOF_STATUS_MISSING": [], "PROSE_FIDELITY_LOSS": []}

R7_TEX_REL = "sources/2026-W43/execution/core-free-preview-r7/main.tex"
R7_TEX_SHA256 = "9791a545c1ed363f8abace62c90bdbfe15f31dac4017b80a5109907c35509ea0"
R7_TEX_BYTES = 97572
R8_TEX_DEFAULT = "sources/2026-W43/execution/core-free-preview-r8/main.tex"

# Exact authorised A/B/C replacements (whitelist)
A_OLD = "（計数規約は承認済みArchitecture境界注記）"
A_NEW = "（totalとactive per tokenは計数規約が異なり、直接比較できない）"
B_OLD = "FLUX 3 Max は fal と BFL による post-train（強化学習 RL・推論最適）の成果として提示され、text・image・keyframes-to-video の三様式が語られる。text／image は発売時の公式確認がある一方、keyframes の扱いは、10月19日のプレスリリース（PR）の可用主張・ブログ導線と、FAQに由来するとされる未照合の記述「Two at launch（二様式で開始）」との未照合の食い違いがある（FAQ原文の出典・版・観測時刻は未特定）。この食い違いは 未照合の記述の食い違い（出典・版・観測時刻は未特定のため確定した矛盾としない）（FAQに由来するとされる未照合の記述との食い違い。原文の出典・版・観測時刻は未特定のため、確定した発行者間の矛盾として扱わない。承認済みArchitectureの旧ラベルはraw検証待ちの legacy として保持）として残し、W43時点の live／schema／GA を確定として書かない。従量課金などの条件は記されるが、解像度・GPU・batch・cold／warm といった装置条件は不明（UNKNOWN）のままである。"
B_NEW = "FLUX 3 Max は fal と BFL による post-train（強化学習 RL・推論最適）の成果として提示され、text・image・keyframes-to-video の三様式が語られる。text／image は発売時の公式確認がある一方、keyframes の扱いは、10月19日のプレスリリース（PR）の可用主張・ブログ導線と、FAQに由来するとされる未照合の記述「Two at launch（二様式で開始）」との未照合の食い違いがある（FAQ原文の出典・版・観測時刻は未特定）。PR・ブログは可用主張を示すが、FAQに由来するとされる記述は原文URL・版・観測時刻が未検証のため、発行者間の確定した矛盾とはしない。この未確定の帰属からはkeyframes・live／schema／GAの提供確定は導けず、W43時点では確定として書かない。従量課金などの条件は記されるが、解像度・GPU・batch・cold／warm といった装置条件は不明（UNKNOWN）のままである。"
C_OLD = "P1-P8横断の編集合成"
C_NEW = "本号の各主題を整理した派生記述"

META_PATTERNS = ["印刷用原稿", "編集プレビュー・未承認", "読者確認用プレビュー",
                 "非正準の編集 proof", "受理済み Core 証拠",
                 "p1-f1", "p2-f2", "p3-f1", "p5-f1", "p6-f1", "p7-f1",
                 "p8-f1", "p8-f2", "p8-f3", "§1.3実物", "§2.5実物",
                 "§3.2実物", "§5.1", "§6.1実物", "§7.2実物", "§8.1実物",
                 "§8.2実物", "§8.3実物", "分離記録した文脈注記の詳細は引用対応表を参照",
                 "承認済みArchitecture", "承認済みArchitecture境界注記",
                 "承認済みArchitectureの旧ラベル", "raw検証待ちの legacy",
                 "P1-P8横断の編集合成"]
# A/B/C old strings must be absent from r8 visible (they are the authorised removals)
QUALIFIERS_CORE = ["未検証", "未実行", "発行元測定", "独立再現なし", "未取得"]

# 29 claim facets carried from r7 (scientific anchors, not meta).
# These are distinctive stable strings that must survive r7->r8 (none overlap A/B/C old).
CLAIM_ANCHORS_29 = [
    "2.8T", "104B", "3T級", "1M対応", "39.8B", "約2.5B", "262,144",
    "256 experts", "SWA-513", "Apache-2.0", "8B", "4B", "effective",
    "2026-10-23T17:15:24Z", "11月4日", "FUTURE", "277.80", "10.95",
    "25.37倍", "22.31倍", "95.52", "12.45秒", "277.80秒",
    "15:18:14Z", "15:21:49", "404", "独立再現なし", "発行元測定",
    "未取得",
]

def build_expected(r7_text):
    assert r7_text.count(A_OLD) == 1, "A_OLD not unique in r7"
    assert r7_text.count(B_OLD) == 1, "B_OLD not unique in r7"
    assert r7_text.count(C_OLD) == 1, "C_OLD not unique in r7"
    exp = r7_text.replace(A_OLD, A_NEW).replace(B_OLD, B_NEW).replace(C_OLD, C_NEW)
    assert A_NEW in exp and B_NEW in exp and C_NEW in exp
    assert A_OLD not in exp and B_OLD not in exp and C_OLD not in exp
    return exp

def visible_body(tex):
    body = tex.split("\\begin{document}")[1].split("\\end{document}")[0]
    return "\n".join(l for l in body.split("\n") if not l.lstrip().startswith("%"))

def split_amp(s):
    parts, cur = [], []
    i = 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s):
            cur += [s[i], s[i+1]]; i += 2; continue
        if s[i] == "&":
            parts.append("".join(cur)); cur = []
        else:
            cur.append(s[i])
        i += 1
    parts.append("".join(cur))
    return parts

def parse_r7_tables(t):
    out = []
    for m in re.finditer(r"\\captionof\{table\}\{(.*?)\}.*?\\begin\{tabularx\}\{[^}]*\}\{(.*?)\}(.*?)\\end\{tabularx\}", t, re.S):
        cap, _, inner = m.group(1), m.group(2), m.group(3)
        rows = []
        for ln in inner.splitlines():
            s = ln.strip()
            if not s or s.startswith("\\toprule") or s.startswith("\\midrule") or s.startswith("\\bottomrule"):
                continue
            if not s.endswith("\\\\"):
                continue
            s = s[:-2].strip()
            if "&" not in s:
                continue
            rows.append(split_amp(s))
        out.append({"caption": cap, "rows": rows})
    return out

def parse_figures_r7(t):
    figs = []
    for m in re.finditer(r"\\begin\{tcolorbox\}\[colback=SurveySoft,colframe=SurveyAccent.*?title=\{(.*?)\}\](.*?)\\end\{tcolorbox\}", t, re.S):
        title, inner = m.group(1).strip(), m.group(2)
        body = []
        mm = re.search(r"\{\\footnotesize\s(.*)", inner, re.S)
        src = mm.group(1) if mm else inner
        for ln in src.splitlines():
            x = ln.strip()
            if not x:
                continue
            if x.endswith("\\par}"):
                x = x[:-len("\\par}")].strip()
            elif x.endswith("\\par"):
                x = x[:-len("\\par")].strip()
            if x in ("{", "}", "\\par", ""):
                continue
            body.append(x)
        figs.append({"title": title, "body": body})
    return figs

def parse_verbatims(t):
    return re.findall(r"\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}", t, re.S)

def parse_bibkeys(t):
    return re.findall(r"\\bibitem\[(.*?)\]", t)

def parse_recap_r7(t):
    m = re.search(r"\\section\*\{今週の総括\}(.*?)\\section\*\{出典一覧", t, re.S)
    if not m:
        return []
    region = m.group(1)
    region = re.sub(r"\\label\{[^}]*\}", "", region)
    region = re.sub(r"\\begin\{multicols\}\{2\}|\\end\{multicols\}[^\n]*", "", region)
    region = "\n".join(l for l in region.split("\n") if not l.lstrip().startswith("%"))
    return [p.strip() for p in re.split(r"\n\s*\n", region) if p.strip() and re.search(r"[぀-ヿ一-鿿A-Za-z0-9]", re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\})?", "", p))]

def parse_toc_titles(t):
    return re.findall(r"\\section(\*)?\{([^}]+)\}", t)

def extract_prose_paras(tex):
    """Ordinary P1-P8 narrative paragraphs: blank-separated blocks inside
    multicols containing 。, excluding tables/figures/verbatim/bib/section heads."""
    body = tex.split("\\begin{document}")[1].split("\\end{document}")[0]
    # isolate inside-multicols segments
    segs = re.split(r"\\begin\{multicols\}\{2\}|\\end\{multicols\}[^\n]*", body)
    inside = "\n".join(segs[i] for i in range(1, len(segs), 2))
    # remove verbatim/code and bib from inside (recap lives inside too; keep recap separately?)
    inside = re.sub(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", "", inside, flags=re.S)
    blocks = [p.strip() for p in re.split(r"\n\s*\n", inside) if p.strip()]
    prose = []
    for p in blocks:
        if p.lstrip().startswith(("\\", "%", "{\\centering", "{\\footnotesize", "{\\scriptsize")):
            continue
        if "captionof" in p or "tabularx" in p or "tcolorbox" in p or "bibitem" in p:
            continue
        if "。" not in p and "．" not in p:
            continue
        # strip latex comments already; require CJK/alnum content
        txt = re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\})?", "", p)
        if not re.search(r"[぀-ヿ一-鿿A-Za-z0-9]", txt):
            continue
        prose.append(p)
    return prose

def check_layout(tex):
    errs = []
    nb, ne = tex.count("\\begin{multicols}{2}"), tex.count("\\end{multicols}")
    if nb == 0 or nb != ne:
        errs.append(f"multicols unbalanced begin={nb} end={ne}")
    if "\\begin{table}" in tex or "\\begin{figure}" in tex:
        errs.append("floating table/figure env remains")
    body = tex.split("\\begin{document}")[1]
    if re.search(r"\\caption\{", body.split("\\end{document}")[0]):
        # \captionof contains \caption substring? No: check raw \caption{
        # already filtered: captionof{table} does not match \\caption{
        errs.append("raw \\caption{} remains")
    segs = re.split(r"\\begin\{multicols\}\{2\}|\\end\{multicols\}", body)
    inside = "".join(segs[i] for i in range(1, len(segs), 2))
    for sec in ["公開前の巨大さ", "推論を切り出し", "働く前に権限", "速さの見出し",
                "声の三様式", "見つけて直し", "手順が結果", "判断をAPI"]:
        if sec not in inside:
            errs.append(f"section not in two-column: {sec}")
    outside = "".join(segs[i] for i in range(0, len(segs), 2))
    if outside.count("captionof{table}") < 20:
        errs.append(f"full-width tables outside multicols <20: {outside.count('captionof{table}')}")
    return errs, {"multicols_begin": nb, "multicols_end": ne}

def check_meta_visible(tex):
    body = tex.split("\\begin{document}")[1]
    visible = "\n".join(l for l in body.split("\n") if not l.lstrip().startswith("%"))
    leaks = [p for p in META_PATTERNS if p in visible]
    for p in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
        if re.search(r"\\section\{" + p + r"\s*---", visible):
            leaks.append(p + " ---")
    return leaks, visible

def run_clean_on_texts(r7_text, actual_text):
    results = []
    def rec(cid, ok, cause, detail):
        results.append({"id": cid, "result": "PASS" if ok else "FAIL",
                        "cause": "—" if ok else cause, "detail": detail})
    # 0. r7 immutability
    r7sha = hashlib.sha256(r7_text.encode("utf-8")).hexdigest()
    r7bytes = len(r7_text.encode("utf-8"))
    rec("R-r7-immutable", r7sha == R7_TEX_SHA256 and r7bytes == R7_TEX_BYTES,
        "ROW_CELL_CLAIM_LOSS", f"r7 sha={r7sha} bytes={r7bytes} (expect {R7_TEX_SHA256}/{R7_TEX_BYTES})")
    # 1. build expected
    try:
        expected = build_expected(r7_text)
        rec("R-expected-build", True, "—", f"expected bytes={len(expected.encode('utf-8'))}")
    except AssertionError as e:
        rec("R-expected-build", False, "ROW_CELL_CLAIM_LOSS", str(e))
        return results, None
    # 2. full byte identity actual vs expected
    rec("S-exact-bytes", actual_text == expected, "PROSE_FIDELITY_LOSS",
        "actual byte-identical to expected (r7+ABC only)" if actual_text == expected else
        f"byte mismatch: actual={len(actual_text.encode('utf-8'))} expected={len(expected.encode('utf-8'))}")
    # 3. visible-body identity
    vis_exp, vis_act = visible_body(expected), visible_body(actual_text)
    rec("S-visible-body-identity", vis_act == vis_exp, "PROSE_FIDELITY_LOSS",
        "visible-body identical" if vis_act == vis_exp else
        f"visible mismatch len act={len(vis_act)} exp={len(vis_exp)}")
    # 4. ordinary prose paragraphs (full list identity)
    p_exp, p_act = extract_prose_paras(expected), extract_prose_paras(actual_text)
    rec("S-prose-count", len(p_act) == len(p_exp), "PROSE_FIDELITY_LOSS",
        f"prose paras act={len(p_act)} exp={len(p_exp)}")
    if len(p_act) == len(p_exp):
        mism = sum(1 for a, b in zip(p_act, p_exp) if a != b)
        rec("S-prose-identity", mism == 0, "PROSE_FIDELITY_LOSS",
            "all ordinary paragraphs identical" if mism == 0 else f"prose mismatch in {mism}/{len(p_exp)} paras")
    # 5. tables
    t_exp, t_act = parse_r7_tables(expected), parse_r7_tables(actual_text)
    rec("S-tables-count", len(t_act) == 20 and len(t_exp) == 20, "ROW_CELL_CLAIM_LOSS",
        f"tables act={len(t_act)} exp={len(t_exp)} (expect 20/20)")
    if len(t_act) == 20 and len(t_exp) == 20:
        rows_act = sum(len(tb["rows"]) for tb in t_act)
        rows_exp = sum(len(tb["rows"]) for tb in t_exp)
        cells_act = sum(1 for tb in t_act for r in tb["rows"] for c in r if c.strip())
        cells_exp = sum(1 for tb in t_exp for r in tb["rows"] for c in r if c.strip())
        rec("S-rows", rows_act == 80 and rows_exp == 80, "ROW_CELL_CLAIM_LOSS", f"rows act={rows_act} exp={rows_exp}")
        rec("S-cells", cells_act == 307 and cells_exp == 307, "ROW_CELL_CLAIM_LOSS", f"cells act={cells_act} exp={cells_exp}")
        mism = sum(1 for a, b in zip(t_act, t_exp) if a["rows"] != b["rows"])
        rec("S-row-identity-vs-expected", mism == 0, "ROW_CELL_CLAIM_LOSS",
            "table bodies identical to expected" if mism == 0 else f"table mismatch {mism}/20")
    # 6. figures
    f_exp, f_act = parse_figures_r7(expected), parse_figures_r7(actual_text)
    rec("S-figures-count", len(f_act) == 3 and len(f_exp) == 3, "ROW_CELL_CLAIM_LOSS",
        f"figures act={len(f_act)} exp={len(f_exp)}")
    if len(f_act) == 3 and len(f_exp) == 3:
        bm = sum(1 for a, b in zip(f_act, f_exp) if a["body"] != b["body"])
        rec("S-figure-body", bm == 0, "ROW_CELL_CLAIM_LOSS", f"figure body mismatch {bm}/3")
    # 7. code
    v_exp, v_act = parse_verbatims(expected), parse_verbatims(actual_text)
    rec("S-code-count", len(v_act) == 5 and len(v_exp) == 5, "ROW_CELL_CLAIM_LOSS",
        f"verbatim act={len(v_act)} exp={len(v_exp)}")
    if len(v_act) == 5 and len(v_exp) == 5:
        cm = sum(1 for a, b in zip(v_act, v_exp) if a != b)
        rec("S-code-body", cm == 0, "ROW_CELL_CLAIM_LOSS", f"code mismatch {cm}/5")
    # 8. recap (5 paras, must be identical: C is bib, not recap)
    rc_exp, rc_act = parse_recap_r7(expected), parse_recap_r7(actual_text)
    rec("S-recap-count", len(rc_act) == 5 and len(rc_exp) == 5, "ROW_CELL_CLAIM_LOSS",
        f"recap act={len(rc_act)} exp={len(rc_exp)}")
    if len(rc_act) == 5 and len(rc_exp) == 5:
        rec("S-recap-identity", all(a == b for a, b in zip(rc_act, rc_exp)), "ROW_CELL_CLAIM_LOSS",
            "recap identical" if all(a == b for a, b in zip(rc_act, rc_exp)) else "recap differs")
    # 9. bib keys (36, order identical; recap body differs by whitelist C)
    b_exp, b_act = parse_bibkeys(expected), parse_bibkeys(actual_text)
    rec("S-bib-count", len(b_act) == 36 and len(b_exp) == 36, "ROW_CELL_CLAIM_LOSS",
        f"bibkeys act={len(b_act)} exp={len(b_exp)}")
    if len(b_act) == 36 and len(b_exp) == 36:
        rec("S-bib-keys", b_act == b_exp, "ROW_CELL_CLAIM_LOSS", "bibkey order identical" if b_act == b_exp else "bibkey mismatch")
    # bib recap entry must contain C_NEW and not C_OLD
    rec("S-bib-recap-whitelist", (C_NEW in actual_text and C_OLD not in actual_text), "READER_META_LEAK",
        "recap bib whitelisted" if (C_NEW in actual_text and C_OLD not in actual_text) else "recap bib whitelist broken")
    # 10. 29 claim facets
    missing = [a for a in CLAIM_ANCHORS_29 if a not in vis_act]
    rec("S-claims-29", len(missing) == 0, "ROW_CELL_CLAIM_LOSS",
        "29 anchors kept" if not missing else f"missing anchors: {missing}")
    # also verify r7->actual delta does not drop anchors except none (A/B/C do not contain anchors)
    # 11. TOC titles
    toc_exp, toc_act = parse_toc_titles(expected), parse_toc_titles(actual_text)
    rec("S-toc-titles", toc_act == toc_exp, "ROW_CELL_CLAIM_LOSS",
        f"TOC titles {len(toc_act)} identical" if toc_act == toc_exp else "TOC titles differ")
    # 12. meta leak
    leaks, _ = check_meta_visible(actual_text)
    rec("M-meta-leak", len(leaks) == 0, "READER_META_LEAK", "no leaks" if not leaks else f"leaks: {leaks}")
    # A/B/C new present, old absent
    rec("M-abc-new-present", (A_NEW in actual_text and B_NEW in actual_text and C_NEW in actual_text),
        "READER_META_LEAK", "A/B/C new present" if (A_NEW in actual_text and B_NEW in actual_text and C_NEW in actual_text) else "A/B/C new missing")
    rec("M-abc-old-absent", (A_OLD not in actual_text and B_OLD not in actual_text and C_OLD not in actual_text),
        "READER_META_LEAK", "A/B/C old absent" if (A_OLD not in actual_text and B_OLD not in actual_text and C_OLD not in actual_text) else "A/B/C old remains")
    # 13. qualifiers
    missing_q = [q for q in QUALIFIERS_CORE if q not in vis_act]
    rec("M-qualifiers", len(missing_q) == 0, "SCIENTIFIC_QUALIFIER_LOSS",
        "core qualifiers kept" if not missing_q else f"missing: {missing_q}")
    # 14. proof status (protective NONCANONICAL layer + NOT A PUBLICATION PREVIEW; forbid APPROVED)
    has_meta = "NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF" in actual_text
    has_footer = vis_act.count("NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF") >= 1
    has_not_pub = "NOT A PUBLICATION PREVIEW" in actual_text
    has_approved = "APPROVED PUBLICATION" in actual_text
    proof_ok = has_meta and has_footer and has_not_pub and (not has_approved)
    rec("M-proof-layer", proof_ok, "DOC_PROOF_STATUS_MISSING",
        f"pdfmeta={has_meta} footers={vis_act.count('NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF')} not_pub={has_not_pub} approved={has_approved}")
    # 15. layout
    errs, linfo = check_layout(actual_text)
    rec("L-two-column", len(errs) == 0, "LAYOUT_NOT_TWO_COLUMN",
        "segmented 2-col ok " + json.dumps(linfo, ensure_ascii=False) if not errs else "; ".join(errs))
    return results, expected

def check_mutation_new(r7_text, mut_text):
    """Run SAME full clean logic on mutant, return failure causes."""
    res, _ = run_clean_on_texts(r7_text, mut_text)
    causes = []
    for r in res:
        if r["result"] == "FAIL" and r["cause"] != "—":
            if r["cause"] not in causes:
                causes.append(r["cause"])
    return causes, res

def run_clean(repo_root, tex_path):
    r7t = (repo_root / R7_TEX_REL).read_text(encoding="utf-8")
    actual = pathlib.Path(tex_path).read_text(encoding="utf-8")
    return run_clean_on_texts(r7t, actual)

def run_negatives(repo_root, tex_path):
    r7t = (repo_root / R7_TEX_REL).read_text(encoding="utf-8")
    base = pathlib.Path(tex_path).read_text(encoding="utf-8")
    cases = []
    N10_OLD = "MoonshotのKimi K3.1 Proは10月23日の告知とAPI提供が先行し、重み配布は11月4日の将来予定である。"
    N10_MUT = "MoonshotのKimi K3.1 Proは10月23日の告知後、API提供も重み配布もすべて終了した。"
    cases.append(("N10-prose-semantic-inversion", base.replace(N10_OLD, N10_MUT), ["PROSE_FIDELITY_LOSS"]))
    # N-qualifier reversal in another ordinary paragraph (Nemotron effective vs total)
    cases.append(("N-qualifier-reversal", base.replace("8B・4B・39.8B・2.5Bを等価に比較して優劣表を作ってはならない", "8B・4B・39.8B・2.5Bを等価に比較して優劣表を作ってもよい"), ["PROSE_FIDELITY_LOSS"]))
    # N-FLUX unverified FAQ -> confirmed contradiction (forbidden upgrade)
    cases.append(("N-flux-faq-confirmed", base.replace("発行者間の確定した矛盾とはしない", "発行者間の確定した矛盾である"), ["PROSE_FIDELITY_LOSS"]))
    # N-numeric cell change (2.8T -> 9.9T)
    cases.append(("N-numeric-cell", base.replace("2.8T total", "9.9T total"), ["ROW_CELL_CLAIM_LOSS", "PROSE_FIDELITY_LOSS"]))
    # N-clock change (GH timestamp)
    cases.append(("N-clock-swap", base.replace("15:18:14Z", "TEMP_XX").replace("15:21:49", "15:18:14").replace("TEMP_XX", "15:21:49"), ["ROW_CELL_CLAIM_LOSS", "PROSE_FIDELITY_LOSS"]))
    # N-adjacent paragraph swap (swap two consecutive ordinary prose paras in P1)
    def swap_adjacent(t):
        paras = extract_prose_paras(t)
        if len(paras) < 2:
            return t
        # swap first two occurrences in text
        a, b = paras[0], paras[1]
        # use placeholder to avoid overlap
        tmp = "___SWAP_TMP___"
        t2 = t.replace(a, tmp, 1).replace(b, a, 1).replace(tmp, b, 1)
        return t2
    cases.append(("N-paragraph-swap", swap_adjacent(base), ["PROSE_FIDELITY_LOSS"]))
    # N-figure body change
    mfig = re.search(r"(\\begin\{tcolorbox\}\[colback=SurveySoft,colframe=SurveyAccent.*?\{\\footnotesize\s.*?\n)(.*? Commission.*?\n)", base, re.S)
    # fallback: mutate first figure body line
    figs = parse_figures_r7(base)
    if figs and figs[0]["body"]:
        cases.append(("N-figure-body", base.replace(figs[0]["body"][0], figs[0]["body"][0] + "改変", 1), ["ROW_CELL_CLAIM_LOSS", "PROSE_FIDELITY_LOSS"]))
    # N-code token change
    cases.append(("N-code-token", base.replace('"gpt-6-luna"', '"gpt-9-omega"'), ["ROW_CELL_CLAIM_LOSS", "PROSE_FIDELITY_LOSS"]))
    # N-recap paragraph change (mutate first recap para)
    cases.append(("N-recap-change", base.replace("検証する姿勢が必要だ", "検証する姿勢は不要だ", 1) if "検証する姿勢が必要だ" in base else base.replace("今週の総括", "今週の総括改変", 1), ["ROW_CELL_CLAIM_LOSS", "PROSE_FIDELITY_LOSS"]))
    # N-bib key deletion
    cases.append(("N-bib-drop", re.sub(r"\\bibitem\[tanstack-npm\].*?\n", "", base, count=1), ["ROW_CELL_CLAIM_LOSS", "PROSE_FIDELITY_LOSS"]))
    # N-operator sentence insertion
    cases.append(("N-operator-insert", base.replace("今週の巻頭は「発表された能力」と「動かせる実物」を切り分けて読む。", "今週の巻頭は「発表された能力」と「動かせる実物」を切り分けて読む。編集承認ゲート通過済み。", 1), ["READER_META_LEAK", "PROSE_FIDELITY_LOSS"]))
    # N-proof removed/approved
    cases.append(("N-proof-remove", base.replace("NOT A PUBLICATION PREVIEW", "APPROVED PUBLICATION"), ["DOC_PROOF_STATUS_MISSING", "PROSE_FIDELITY_LOSS"]))
    results = []
    for cid, mut, expect in cases:
        # verify mutation actually introduced (mut != base)
        if mut == base:
            results.append({"id": cid, "result": "FAIL", "cause": "NEGATIVE_NOT_INTRODUCED",
                            "detail": f"mutation not introduced; expected {expect}"})
            continue
        causes, _full = check_mutation_new(r7t, mut)
        ok = any(e in causes for e in expect)
        # also require any failure (must not PASS clean)
        if not causes:
            ok = False
        results.append({"id": cid, "result": "PASS" if ok else "FAIL",
                        "cause": "—" if ok else "NEGATIVE_NOT_DETECTED",
                        "detail": f"expected {expect}, got {causes}"})
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--tex", default=None)
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--staged-dir", default=None)
    ap.add_argument("--mode", default="clean", choices=["clean", "negatives"])
    a = ap.parse_args()
    repo = pathlib.Path(a.staged_dir) if a.staged_dir else pathlib.Path(a.repo_root)
    tex = a.tex or str(repo / R8_TEX_DEFAULT)
    if a.mode == "clean":
        res, _ = run_clean(repo, tex)
    else:
        res = run_negatives(repo, tex)
    fails = [r for r in res if r["result"] == "FAIL"]
    print(json.dumps({"mode": a.mode, "pass": len(res) - len(fails),
                      "fail": len(fails), "total": len(res),
                      "verdict": "R8_EXACT_FIDELITY_PASS" if a.mode == "clean" and not fails else
                                 ("R8_NEGATIVES_PASS" if a.mode == "negatives" and not fails else "FAIL"),
                      "results": res}, ensure_ascii=False, indent=2))
    return 0 if not fails else 3

if __name__ == "__main__":
    sys.exit(main())
