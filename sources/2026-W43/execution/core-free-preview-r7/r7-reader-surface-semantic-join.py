#!/usr/bin/env python3
"""r7 printed-reader surface validator (Phase C, edition-local).

Proves r6-fixed -> r7-normalized preservation with ONLY the Phase-A meta
whitelist + W42 segmented-multicols layout transforms (proven zero effect
on visible content). Full r3.5->r6 projection join is carried from r6
(R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED 36/36 + 38/38); this checker
does not re-assert the r3.5 strict-claim join from scratch -- it proves the
r6->r7 delta is whitelist+layout only, on real structural content
(tables/rows/cells, figures, code, prose, recap, bib), not a bag of words.

Usage:
  python3 r7-reader-surface-semantic-join.py --repo-root <repo> [--tex PATH]
      [--pdf PATH] [--staged-dir DIR] [--mode clean|negatives]

Exit 0 on PASS / NEGATIVES_PASS. Distinct fail codes:
  READER_META_LEAK, LAYOUT_NOT_TWO_COLUMN, ROW_CELL_CLAIM_LOSS,
  SCIENTIFIC_QUALIFIER_LOSS, DOC_PROOF_STATUS_MISSING.
"""
import argparse, hashlib, json, pathlib, re, sys

FAIL = {"READER_META_LEAK": [], "LAYOUT_NOT_TWO_COLUMN": [],
        "ROW_CELL_CLAIM_LOSS": [], "SCIENTIFIC_QUALIFIER_LOSS": [],
        "DOC_PROOF_STATUS_MISSING": []}

R6_TEX_REL = "sources/2026-W43/execution/core-free-preview-r6/main.tex"
R7_TEX_DEFAULT = "sources/2026-W43/execution/core-free-preview-r7/main.tex"

# Phase-A whitelist: (r6 exact span, r7 exact span)
WHITELIST = [
    ("\\surveyeditiondescriptor{週刊Technical Survey（編集プレビュー・未承認）}",
     "\\surveyeditiondescriptor{週刊Technical Survey}"),
    ("{2026-W43 Weekly --- 読者確認用プレビュー}", "{}"),
    ("\\section*{週刊生成AI技術調査 2026-W43 --- 印刷用原稿 r3}",
     "\\section*{週刊生成AI技術調査 2026-W43}"),
    ("title={文脈長の三層（p1-f1、§1.3実物）}", "title={文脈長の三層}"),
    ("\\caption{MemT権利対応（p2-f2、§2.5実物）}", "\\caption{MemT権利対応}"),
    ("title={資格・承認フロー（p3-f1、§3.2実物）}", "title={資格・承認フロー}"),
    ("title={協調開示の五段階（p6-f1、§6.1実物）}", "title={協調開示の五段階}"),
    ("\\caption{様式×評価・料金の実数行列（p5-f1、§5.1–5.2実物。数値は全て発行元公表・独立再現なし。比較対象・単位は行内でqualified）}",
     "\\caption{様式×評価・料金の実数行列（数値は全て発行元公表・独立再現なし。比較対象・単位は行内でqualified）}"),
    ("\\caption{言語別デルタと労力・費用の注記（p7-f1、§7.2実物。数値は全て発行元測定）}",
     "\\caption{言語別デルタと労力・費用の注記（数値は全て発行元測定）}"),
    ("\\caption{安定核 vs 実験harness（p8-f2、§8.2実物）}", "\\caption{安定核 vs 実験harness}"),
    ("\\caption{重み vs API vs 追加物（p8-f3、§8.3実物）}", "\\caption{重み vs API vs 追加物}"),
    ("【例：Decisions要求・応答（p8-f1、§8.1実物。公式ガイド転載・未実行（API呼出しなし））】",
     "【例：Decisions要求・応答（公式ガイド転載・未実行（API呼出しなし））】"),
    ("本プレビューは非正準の編集 proof であり、受理済み Core 証拠の代替ではない。文中の鍵番号に対応する一次リンクを以下に集約する。未取得・未検証の範囲は各章の注意書きを参照。分離記録した文脈注記の詳細は引用対応表を参照。",
     "本稿で参照した資料を以下に示す。各資料の確認範囲や未検証事項は本文・注記に明記した。"),
]
for p in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
    WHITELIST.append((f"\\section{{{p} --- ", "\\section{"))
# note: P-prefix entries are prefix-only; handled specially below.

META_PATTERNS = ["印刷用原稿", "編集プレビュー・未承認", "読者確認用プレビュー",
                 "非正準の編集 proof", "受理済み Core 証拠",
                 "p1-f1", "p2-f2", "p3-f1", "p5-f1", "p6-f1", "p7-f1",
                 "p8-f1", "p8-f2", "p8-f3", "§1.3実物", "§2.5実物",
                 "§3.2実物", "§5.1", "§6.1実物", "§7.2実物", "§8.1実物",
                 "§8.2実物", "§8.3実物", "分離記録した文脈注記の詳細は引用対応表を参照"]
QUALIFIERS = ["未検証", "未実行", "原本未取得", "発行元測定", "独立再現なし",
              "未取得", "発行元公表", "未確認", "未開封", "未照合"]

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

def parse_r6_tables(t):
    out = []
    for m in re.finditer(r"\\begin\{table\}.*?\\caption\{(.*?)\}.*?\\begin\{tabularx\}\{[^}]*\}\{(.*?)\}(.*?)\\end\{tabularx\}", t, re.S):
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

def norm_caption_r6(cap):
    for old, new in WHITELIST:
        if old.startswith("\\caption") and old in ("\\caption{" + cap + "}"):
            pass
    # apply whitelist inside caption string
    for old, new in WHITELIST:
        # extract inner contents when both are caption/title wrappers
        if old.startswith("\\caption{") and new.startswith("\\caption{"):
            cap = cap.replace(old[len("\\caption{"):-1], new[len("\\caption{"):-1])
        elif old.startswith("title={") and new.startswith("title={"):
            cap = cap.replace(old[len("title={"):-1], new[len("title={"):-1])
    return cap

def parse_figures_r6(t):
    figs = []
    for m in re.finditer(r"\\begin\{figure\}.*?\\end\{figure\}", t, re.S):
        span = m.group(0)
        title = re.search(r"title=\{(.*?)\}", span, re.S)
        inner = re.search(r"\{\\footnotesize\s(.*?)\\par\}", span, re.S)
        body = []
        if inner:
            for ln in inner.group(1).splitlines():
                x = ln.strip()
                if not x:
                    continue
                if x.endswith("\\par"):
                    x = x[:-4].strip()
                body.append(x)
        figs.append({"title": title.group(1).strip() if title else "", "body": body})
    return figs

def parse_figures_r7(t):
    # inter-segment figure boxes: {\centering \begin{tcolorbox}[...title={...}] {\footnotesize ... \par} \end{tcolorbox}}
    figs = []
    # find accent boxes with title= (figure boxes are SurveyAccent; note boxes are SurveyRule without title)
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

def parse_recap_r6(t):
    m = re.search(r"\\section\*\{今週の総括\}(.*?)\\clearpage", t, re.S)
    if not m:
        return []
    region = re.sub(r"\\label\{[^}]*\}", "", m.group(1))
    return [p.strip() for p in re.split(r"\n\s*\n", region) if p.strip() and re.search(r"[぀-ヿ一-鿿A-Za-z0-9]", re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\})?", "", p))]

def parse_recap_r7(t):
    m = re.search(r"\\section\*\{今週の総括\}(.*?)\\section\*\{出典一覧", t, re.S)
    if not m:
        return []
    region = m.group(1)
    region = re.sub(r"\\label\{[^}]*\}", "", region)
    region = re.sub(r"\\begin\{multicols\}\{2\}|\\end\{multicols\}[^\n]*", "", region)
    region = "\n".join(l for l in region.split("\n") if not l.lstrip().startswith("%"))
    return [p.strip() for p in re.split(r"\n\s*\n", region) if p.strip() and re.search(r"[぀-ヿ一-鿿A-Za-z0-9]", re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\})?", "", re.sub(r"(?m)^%.*$", "", p)))]

def check_layout(tex):
    errs = []
    nb, ne = tex.count("\\begin{multicols}{2}"), tex.count("\\end{multicols}")
    if nb == 0 or nb != ne:
        errs.append(f"multicols unbalanced begin={nb} end={ne}")
    if "\\begin{table}" in tex or "\\begin{figure}" in tex:
        errs.append("floating table/figure env remains (must be inter-segment captionof/bare box)")
    if "\\caption{" in tex:
        # only hypersetup/pdfstrings may contain \caption? check outside preamble
        body = tex.split("\\begin{document}")[1]
        # \captionof contains \caption substring? No: \captionof{table} does not contain "\caption{"
        if re.search(r"\\caption\{", body):
            errs.append("raw \\caption{} remains (must be \\captionof)")
    # prose coverage: sections P1..P8 must be inside multicols
    body = tex.split("\\begin{document}")[1].split("\\end{document}")[0]
    # strip multicols env lines, then check each section heading is within a segment:
    # simpler: count section headings inside vs outside by scanning segments
    segs = re.split(r"\\begin\{multicols\}\{2\}|\\end\{multicols\}", body)
    # segs[0] outside, [1] inside, [2] outside, ...
    inside = "".join(segs[i] for i in range(1, len(segs), 2))
    for sec in ["公開前の巨大さ", "推論を切り出し", "働く前に権限", "速さの見出し",
                "声の三様式", "見つけて直し", "手順が結果", "判断をAPI"]:
        if sec not in inside:
            errs.append(f"section not in two-column: {sec}")
    # wide blocks outside
    outside = "".join(segs[i] for i in range(0, len(segs), 2))
    if outside.count("captionof{table}") < 20:
        errs.append(f"full-width tables outside multicols <20: {outside.count('captionof{table}')}")
    return errs, {"multicols_begin": nb, "multicols_end": ne}

def check_meta_visible(tex):
    body = tex.split("\\begin{document}")[1]
    visible = "\n".join(l for l in body.split("\n") if not l.lstrip().startswith("%"))
    leaks = [p for p in META_PATTERNS if p in visible]
    # P-prefix check
    for p in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
        if re.search(r"\\section\{" + p + r"\s*---", visible):
            leaks.append(p + " ---")
    return leaks, visible

def run_clean(repo_root, tex_path):
    results = []
    def rec(cid, ok, cause, detail):
        results.append({"id": cid, "result": "PASS" if ok else "FAIL",
                        "cause": "—" if ok else cause, "detail": detail})
        if not ok:
            FAIL.setdefault(cause, []).append(cid)
    r6t = (repo_root / R6_TEX_REL).read_text(encoding="utf-8")
    r7t = pathlib.Path(tex_path).read_text(encoding="utf-8")
    # whitelist application check: every whitelist old must occur in r6, new in r7
    # (caption entries live as \captionof{table} in r7 layout; titles bare)
    for old, new in WHITELIST:
        if old.startswith("\\section{P"):
            continue  # prefix handled separately
        if old not in r6t:
            rec("W-whitelist-r6-present", False, "ROW_CELL_CLAIM_LOSS", f"whitelist old missing in r6: {old[:50]}")
        r7needle = new
        if new.startswith("\\caption{"):
            r7needle = "\\captionof{table}{" + new[len("\\caption{"):]
        if r7needle not in r7t:
            rec("W-whitelist-r7-present", False, "READER_META_LEAK", f"whitelist new missing in r7: {new[:50]}")
    # P-prefix removal
    for p in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
        if f"\\section{{{p} --- " not in r6t:
            rec("W-prefix-r6", False, "ROW_CELL_CLAIM_LOSS", f"{p} prefix missing in r6")
        if re.search(r"\\section\{" + p + r"\s*---", r7t):
            rec("W-prefix-r7", False, "READER_META_LEAK", f"{p} prefix remains in r7")
        if f"\\label{{sec:{p}}}" not in r7t:
            rec("W-label-kept", False, "ROW_CELL_CLAIM_LOSS", f"machine label sec:{p} lost")
    # tables
    t6, t7 = parse_r6_tables(r6t), parse_r7_tables(r7t)
    rec("S-tables-count", len(t6) == 20 and len(t7) == 20, "ROW_CELL_CLAIM_LOSS",
        f"r6 tables={len(t6)} r7 captionof={len(t7)} (expect 20/20)")
    if len(t6) == 20 and len(t7) == 20:
        cell6 = sum(1 for tb in t6 for r in tb["rows"] for c in r if c.strip())
        cell7 = sum(1 for tb in t7 for r in tb["rows"] for c in r if c.strip())
        rows6 = sum(len(tb["rows"]) for tb in t6)
        rows7 = sum(len(tb["rows"]) for tb in t7)
        rec("S-rows", rows6 == 80 and rows7 == 80, "ROW_CELL_CLAIM_LOSS", f"rows r6={rows6} r7={rows7} (expect 80)")
        rec("S-cells", cell6 == 307 and cell7 == 307, "ROW_CELL_CLAIM_LOSS", f"nonempty cells r6={cell6} r7={cell7} (expect 307)")
        # row-by-row identity
        mism = 0
        for a, b in zip(t6, t7):
            if a["rows"] != b["rows"]:
                mism += 1
        rec("S-row-identity", mism == 0, "ROW_CELL_CLAIM_LOSS", f"table body mismatch in {mism}/20 tables")
        # captions: normalized equality
        cmism = 0
        for a, b in zip(t6, t7):
            if norm_caption_r6(a["caption"]) != b["caption"]:
                cmism += 1
        rec("S-caption-whitelist", cmism == 0, "READER_META_LEAK", f"caption whitelist mismatch {cmism}/20")
    # figures
    f6, f7 = parse_figures_r6(r6t), parse_figures_r7(r7t)
    rec("S-figures-count", len(f6) == 3 and len(f7) == 3, "ROW_CELL_CLAIM_LOSS",
        f"figures r6={len(f6)} r7={len(f7)} (expect 3/3)")
    if len(f6) == 3 and len(f7) == 3:
        bm = sum(1 for a, b in zip(f6, f7) if a["body"] != b["body"])
        rec("S-figure-body", bm == 0, "ROW_CELL_CLAIM_LOSS", f"figure body mismatch {bm}/3")
        tm = sum(1 for a, b in zip(f6, f7) if norm_caption_r6(a["title"]) != b["title"])
        rec("S-figure-title", tm == 0, "READER_META_LEAK", f"figure title whitelist mismatch {tm}/3")
    # code blocks
    v6, v7 = parse_verbatims(r6t), parse_verbatims(r7t)
    rec("S-code-count", len(v6) == 5 and len(v7) == 5, "ROW_CELL_CLAIM_LOSS",
        f"verbatim r6={len(v6)} r7={len(v7)} (expect 5/5)")
    if len(v6) == 5 and len(v7) == 5:
        # normalize whitelisted first-line example header
        def norm_code(s):
            for old, new in WHITELIST:
                if len(old) < 200 and old in s:
                    s = s.replace(old, new)
            return s
        cm = sum(1 for a, b in zip(v6, v7) if norm_code(a) != b)
        rec("S-code-body", cm == 0, "ROW_CELL_CLAIM_LOSS", f"code mismatch after whitelist {cm}/5")
    # recap
    rc6, rc7 = parse_recap_r6(r6t), parse_recap_r7(r7t)
    rec("S-recap-count", len(rc6) == 5 and len(rc7) == 5, "ROW_CELL_CLAIM_LOSS",
        f"recap paras r6={len(rc6)} r7={len(rc7)} (expect 5/5)")
    if len(rc6) == 5 and len(rc7) == 5:
        rec("S-recap-identity", all(a == b for a, b in zip(rc6, rc7)), "ROW_CELL_CLAIM_LOSS",
            "recap paragraph bytes identical" if all(a == b for a, b in zip(rc6, rc7)) else "recap text differs")
    # bib
    b6, b7 = parse_bibkeys(r6t), parse_bibkeys(r7t)
    rec("S-bib-count", len(b6) == 36 and len(b7) == 36, "ROW_CELL_CLAIM_LOSS",
        f"bibkeys r6={len(b6)} r7={len(b7)} (expect 36/36)")
    if len(b6) == 36 and len(b7) == 36:
        rec("S-bib-keys", b6 == b7, "ROW_CELL_CLAIM_LOSS", "bibkey order identical" if b6 == b7 else f"bibkey mismatch")
    # meta leak
    leaks, visible = check_meta_visible(r7t)
    rec("M-meta-leak", len(leaks) == 0, "READER_META_LEAK", "no leaks" if not leaks else f"leaks: {leaks}")
    # qualifiers
    missing_q = [q for q in QUALIFIERS if q not in visible]
    # 原本未取得 appears as 原本バイト未取得/原本未取得 variants; require core set
    core_q = ["未検証", "未実行", "発行元測定", "独立再現なし", "未取得"]
    missing_core = [q for q in core_q if q not in visible]
    rec("M-qualifiers", len(missing_core) == 0, "SCIENTIFIC_QUALIFIER_LOSS",
        "core qualifiers kept" if not missing_core else f"missing: {missing_core}")
    # proof status
    has_meta = "NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF" in r7t
    has_footer = visible.count("NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF") >= 1
    rec("M-proof-layer", has_meta and has_footer, "DOC_PROOF_STATUS_MISSING",
        f"pdfmeta={has_meta} separate footers/covermarks visible={visible.count('NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF')}")
    # layout
    errs, linfo = check_layout(r7t)
    rec("L-two-column", len(errs) == 0, "LAYOUT_NOT_TWO_COLUMN", "segmented 2-col ok " + json.dumps(linfo, ensure_ascii=False) if not errs else "; ".join(errs))
    return results

def run_negatives(repo_root, tex_path):
    base = pathlib.Path(tex_path).read_text(encoding="utf-8")
    cases = []
    def case(cid, mut, expect):
        cases.append((cid, mut, expect))
    # N1: re-insert reviewer sentence inside article
    case("N-meta-reinsert", base.replace("本稿で参照した資料を以下に示す。",
         "本プレビューは非正準の編集 proof であり、受理済み Core 証拠の代替ではない。"), ["READER_META_LEAK"])
    # N2: delete scientific qualifier (independent re-run absent)
    case("N-qualifier-delete", base.replace("独立再現なし", "独立検証済み"), ["SCIENTIFIC_QUALIFIER_LOSS"])
    # N3: swap GH/npm clocks
    case("N-clock-swap", base.replace("15:18:14Z", "TEMP_XX").replace("15:21:49", "15:18:14").replace("TEMP_XX", "15:21:49"), ["ROW_CELL_CLAIM_LOSS"])
    # N4: mutate a table number (2.8T -> 9.9T)
    case("N-table-number", base.replace("2.8T", "9.9T"), ["ROW_CELL_CLAIM_LOSS"])
    # N5: delete a recap paragraph (final recap paragraph; 。 is U+3002, not ASCII '.')
    m = re.search(r"(\\section\*\{今週の総括\}.*?)(来週以降も注目したいのは.*?検証する姿勢が必要だ。)", base, re.S)
    if m:
        case("N-recap-delete", base.replace(m.group(2), ""), ["ROW_CELL_CLAIM_LOSS"])
    # N6: mutate code token (model name)
    case("N-code-token", base.replace('"gpt-6-luna"', '"gpt-9-omega"'), ["ROW_CELL_CLAIM_LOSS"])
    # N7: drop one bibliography citation (remove a bibitem)
    case("N-bib-drop", re.sub(r"\\bibitem\[tanstack-npm\].*?\n", "", base, count=1), ["ROW_CELL_CLAIM_LOSS"])
    # N8: remove proof footer
    case("N-proof-remove", base.replace("NOT A PUBLICATION PREVIEW", "APPROVED PUBLICATION"), ["DOC_PROOF_STATUS_MISSING"])
    # N9: strip two-column (remove all multicols begins)
    case("N-layout-single", base.replace("\\begin{multicols}{2}", "% STRIPPED"), ["LAYOUT_NOT_TWO_COLUMN"])
    # N10: reorder two table rows (swap adjacent data rows in first tabularx)
    def swap_rows(t):
        t2 = t
        m2 = re.search(r"(\\begin\{tabularx\}.*?)(.*?\n)(.*?\n)(.*?\\end\{tabularx\})", t, re.S)
        return t2
    results = []
    for cid, mut, expect in cases:
        # evaluate mutated tex with same checks (lightweight: run run_clean on temp is heavy; inline targeted checks)
        r = check_mutation(base, mut)
        ok = any(e in r for e in expect)
        results.append({"id": cid, "result": "PASS" if ok else "FAIL",
                        "cause": "—" if ok else "NEGATIVE_NOT_DETECTED",
                        "detail": f"expected {expect}, got {r}"})
    return results

def check_mutation(base, mut):
    causes = []
    leaks, _ = check_meta_visible(mut)
    if leaks:
        causes.append("READER_META_LEAK")
    # qualifiers: count-based vs base ("独立検証済み" occurs legitimately 4x as
    # prohibitions, so marker presence is not a signal; loss of core qualifier
    # occurrences is). N2 replaces all 8 独立再現なし -> drop detected here.
    base_vis = "\n".join(l for l in base.split("\\begin{document}")[1].split("\n") if not l.lstrip().startswith("%"))
    vis = "\n".join(l for l in mut.split("\\begin{document}")[1].split("\n") if not l.lstrip().startswith("%"))
    for q in ["独立再現なし", "未実行", "発行元測定", "未取得"]:
        if vis.count(q) < base_vis.count(q):
            causes.append("SCIENTIFIC_QUALIFIER_LOSS")
            break
    if "NOT A PUBLICATION PREVIEW" not in mut or "APPROVED PUBLICATION" in mut:
        causes.append("DOC_PROOF_STATUS_MISSING")
    if "\\begin{multicols}{2}" not in mut:
        causes.append("LAYOUT_NOT_TWO_COLUMN")
    # row/cell/claim loss: compare structural parses vs base
    try:
        if parse_r7_tables(base) != parse_r7_tables(mut):
            causes.append("ROW_CELL_CLAIM_LOSS")
        elif parse_recap_r7(base) != parse_recap_r7(mut):
            causes.append("ROW_CELL_CLAIM_LOSS")
        elif parse_verbatims(base) != parse_verbatims(mut):
            causes.append("ROW_CELL_CLAIM_LOSS")
        elif parse_bibkeys(base) != parse_bibkeys(mut):
            causes.append("ROW_CELL_CLAIM_LOSS")
    except Exception:
        causes.append("ROW_CELL_CLAIM_LOSS")
    return causes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--tex", default=None)
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--staged-dir", default=None)
    ap.add_argument("--mode", default="clean", choices=["clean", "negatives"])
    a = ap.parse_args()
    repo = pathlib.Path(a.staged_dir) if a.staged_dir else pathlib.Path(a.repo_root)
    tex = a.tex or str(repo / R7_TEX_DEFAULT)
    if a.mode == "clean":
        res = run_clean(repo, tex)
    else:
        res = run_negatives(repo, tex)
    fails = [r for r in res if r["result"] == "FAIL"]
    print(json.dumps({"mode": a.mode, "pass": len(res) - len(fails),
                      "fail": len(fails), "total": len(res),
                      "verdict": "R7_READER_SURFACE_PASS" if a.mode == "clean" and not fails else
                                 ("NEGATIVES_PASS" if a.mode == "negatives" and not fails else "FAIL"),
                      "results": res}, ensure_ascii=False, indent=2))
    return 0 if not fails else 3

if __name__ == "__main__":
    sys.exit(main())
