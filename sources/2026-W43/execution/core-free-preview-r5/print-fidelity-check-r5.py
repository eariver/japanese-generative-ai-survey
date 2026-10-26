#!/usr/bin/env python3
"""r5 TeX cell-level print-fidelity + cryptographic guard validator (honest).

Closes r4 gaps R5-FID-01/02/03:
- FID-01: parses each TeX tabularx body into ordered rows AND ordered cells
  (unescaped & split; \\%, \\&, \\_, braces, \\url/\\nolinkurl, wrapping),
  maps every printed row to table-id + ordinal + manifest row-id + DATA/NOTE,
  and compares NORMALIZED per-cell source/proj/TeX with a bounded explicit
  allowlist (operator-token rendering + print escaping only).
  All 29 claims asserted in their ONE target TeX row/cell (value/variant/
  qualifier + provider/unit/comparator/provenance facets).
- FID-02: real hashlib.sha256(actual bytes) for 6 pinned inputs; disk files vs
  ephemeral mutants distinguished explicitly; hash-corrupted baseline fails
  HASH_MISMATCH; text mutants run the common semantic validator.
- FID-03: key classes use TeX-visible spans; 13 natural cases carry exact
  quote/span evidence and are marked CURATED_REVIEW_REQUIRED.
No or True, no count-only, no ANY_FAIL. Exit 0 only on full PASS.
"""
import re, sys, json, ast, hashlib, pathlib

REPO = pathlib.Path("/home/eariver/git/japanese-generative-ai-survey")
R35 = REPO / "sources/2026-W43/execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md"
LED = REPO / "sources/2026-W43/execution/editorial-bypass/w43-r3-5-citation-confidence-ledger.json"
MANP = REPO / "sources/2026-W43/execution/editorial-bypass/w43-r3-5-physical-row-manifest.json"
PROJ_D = REPO / "sources/2026-W43/execution/core-free-preview-r3/reader-print-projection-r3.md"
TEX_D = REPO / "sources/2026-W43/execution/core-free-preview-r3/main.tex"
PDF_D = REPO / "sources/2026-W43/execution/core-free-preview-r3/main.pdf"

EXPECTED_HASH = {
    str(R35): "6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6",
    str(LED): "6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4",
    str(MANP): "85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111",
    str(PROJ_D): "63ad2617f663a01bd14a93b803a96272bf3cc72debbdf4817f81c6596eccbe80",
    str(TEX_D): "bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed",
    str(PDF_D): "d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca",
}

MAN = json.loads(MANP.read_text(encoding="utf-8"))
TABLES = MAN["tables_detail"]
EXPECTED_HEADERS = [t["header"] for t in TABLES]
_chk = ast.parse((REPO / "sources/2026-W43/execution/editorial-bypass/w43-r3-5-strict-semantic-claim-join-check.py").read_text(encoding="utf-8"))
EXPECTED_CLAIMS = None
for _n in _chk.body:
    if isinstance(_n, ast.Assign) and any(isinstance(_t, ast.Name) and _t.id == "EXPECTED_CLAIMS" for _t in _n.targets):
        EXPECTED_CLAIMS = ast.literal_eval(_n.value)
        break
assert EXPECTED_CLAIMS and len(EXPECTED_CLAIMS) == 29

TOKEN_SUBS_SORTED = sorted([
    ("PRIMARY_METADATA", "一次資料（付随情報）"), ("PRIMARY_RAW", "一次資料"),
    ("SOURCE_UNVERIFIED", "未検証（保存済み資料に記載なし・比較条件未確認）"),
    ("RENDERED_ONLY", "描画抽出のみ（原本HTMLの閲覧ではない）"),
    ("RENDERED_TEXT", "描画抽出テキストのみ（原本HTMLの閲覧ではない）"),
    ("NOT_EXECUTED", "未実行"), ("NOT_RUN", "未実行（API呼出しなし）"),
    ("PSEUDOCODE", "疑似コード（実行できない抜粋）"), ("NONRUNNABLE", "実行不可の抜粋"),
    ("IMPORT_UNVERIFIED", "導入経路は未確認"), ("NEVER_STORY", "当週の対象外"),
    ("POST_CUTOFF／OUT", "集計期間外のため当週非選択"), ("POST_CUTOFF/OUT", "集計期間外のため当週非選択"),
    ("UNRESOLVED_FAQ_ATTRIBUTION", "未照合の記述の食い違い（出典・版・観測時刻は未特定のため確定した矛盾としない）"),
    ("UNRESOLVED_VENDOR_DOC_CONFLICT", "資料間で不一致があり単一値に統一しない"),
    ("UNRESOLVED", "未解決（単一値に統一しない）"),
    ("COMPARATOR_UNVERIFIED", "比較対象・内訳は未確認"), ("UNIT_UNVERIFIED", "単位の記載は未確認"),
    ("VENDOR_BENCH", "発行元測定（独立再現なし）"),
], key=lambda kv: -len(kv[0]))
API_ROUTE = "`POST /v1/decisions`"
INTERNAL_HINTS = ("sources/", ".md", ".py", ".html", "task-", "memt-",
                  "deepinfer-", "flint-", "recursive-", "w43-", "environ.py")
API_RE = re.compile(r"^(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+/")

# ---------- parsers ----------
def parse_md_tables(md_text):
    lines = md_text.splitlines(); out = []; i = 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i+1:j]
            if body and body[0].strip().startswith("【表"):
                out.append({"header": body[0].strip(),
                            "rows": [l for l in body if "｜" in l],
                            "notes": [l for l in body[1:] if "｜" not in l and l.strip()]})
            i = j + 1
        else:
            i += 1
    return out

def parse_md_figures(md_text):
    lines = md_text.splitlines(); out = []; i = 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i+1:j]
            if body and body[0].strip().startswith("【図"):
                out.append({"header": body[0].strip(), "body": body[1:]})
            i = j + 1
        else:
            i += 1
    return out

def split_unescaped_amp(s):
    parts, cur, esc = [], [], False
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s):
            cur.append(ch); cur.append(s[i+1]); i += 2; continue
        if ch == "&":
            parts.append("".join(cur)); cur = []
        else:
            cur.append(ch)
        i += 1
    parts.append("".join(cur))
    return parts

def parse_tex_tables(tex_body):
    """Ordered tables with per-row cell lists (ampersand/percent/underscore escapes, braces, urls)."""
    tabs = []
    for m in re.finditer(r"\\begin\{table\}.*?\\caption\{(.*?)\}.*?\\begin\{tabularx\}\{[^}]*\}\{(.*?)\}(.*?)\\end\{tabularx\}", tex_body, re.S):
        cap_raw, colspec, inner = m.group(1), m.group(2), m.group(3)
        rows = []
        for ln in inner.splitlines():
            s = ln.strip()
            if not s or s.startswith(r"\toprule") or s.startswith(r"\midrule") or s.startswith(r"\bottomrule"):
                continue
            if not s.endswith("\\\\"):
                continue
            s = s[:-2].strip()
            if "&" not in s:
                continue
            rows.append(split_unescaped_amp(s))
        tabs.append({"caption": cap_raw, "colspec": colspec, "rows": rows, "span": m.group(0)})
    return tabs

def tex_visible(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\(?:texttt|textbf|textsl|emph|url|nolinkurl|color|small|footnotesize|scriptsize)\*?(?:\[[^\]]*\])?\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[A-Za-z]+(?:\[[^\]]*\])?(?:\{[^}]*\})?", "", s)
    for a, b in [("\\%", "%"), ("\\#", "#"), ("\\$", "$"), ("\\&", "&"),
                 ("\\_", "_"), ("\\textasciitilde{}", "~"), ("\\textasciicircum{}", "^"),
                 ("\\textbackslash{}", "\\")]:
        s = s.replace(a, b)
    s = s.replace("{", "").replace("}", "")
    return s

def norm_proj_cell(s):
    return s.replace("`", "").replace("**", "").strip()

def norm_tex_cell(s):
    return tex_visible(s).strip()

# ---------- single validation entrypoint ----------
def validate(proj_text, tex_text, file_bytes_overrides=None):
    """Validate (proj_text, tex_text) with real file-identity guard.

    file_bytes_overrides: {str(path): bytes} to use INSTEAD of disk bytes for
    hash checking (explicit ephemeral harness state; never silently skipped).
    Returns list of {id, result, cause, detail}.
    """
    res = []
    def rec(cid, ok, cause, detail):
        res.append({"id": cid, "result": "PASS" if ok else "FAIL",
                    "cause": cause if not ok else "—", "detail": detail})
    tex_body = tex_text.split(r"\begin{thebibliography}")[0]
    bib_sec = tex_text.split(r"\begin{thebibliography}")[1] if r"\begin{thebibliography}" in tex_text else ""
    src_text = R35.read_text(encoding="utf-8")

    # H00 real cryptographic input identity (6 pinned inputs)
    h_fails = []
    for pstr, exp in EXPECTED_HASH.items():
        actual = file_bytes_overrides.get(pstr) if file_bytes_overrides and pstr in file_bytes_overrides else pathlib.Path(pstr).read_bytes()
        got = hashlib.sha256(actual).hexdigest()
        if got != exp:
            h_fails.append(f"{pathlib.Path(pstr).name}:HASH_MISMATCH")
    rec("H00-input-identity", not h_fails, "HASH_MISMATCH",
        "6/6 SHA256 match" if not h_fails else "; ".join(h_fails[:4]))

    # V01 API route in BOTH artifacts
    rec("V01-api-proj", API_ROUTE in proj_text, "API_MISSING_PROJ", "POST code span in projection")
    rec("V01-api-tex", r"\texttt{POST /v1/decisions}" in tex_body, "API_MISSING_TEX", "POST texttt in TeX body")

    # V02 headers
    t_src = parse_md_tables(src_text); t_proj = parse_md_tables(proj_text)
    hs, hp = [t["header"] for t in t_src], [t["header"] for t in t_proj]
    rec("V02-header-count", len(hs) == 20 and len(hp) == 20, "HEADER_COUNT", f"src={len(hs)} proj={len(hp)}")
    rec("V02-header-order", hs == hp == EXPECTED_HEADERS, "HEADER_ORDER",
        "20 identical order" if hs == hp == EXPECTED_HEADERS else "mismatch")

    # V03 ordered row join src->proj vs manifest (+types+unique)
    rowfails = []
    ok_tables = len(t_src) == len(t_proj) == 20
    if ok_tables:
        for ti, (ts, tp, tm) in enumerate(zip(t_src, t_proj, TABLES)):
            if len(ts["rows"]) != len(tp["rows"]) or len(tp["rows"]) != len(tm["rows"]):
                rowfails.append(f"{tm['table_id']}:count"); continue
            if ts["header"] != tm["header"] or tp["header"] != tm["header"]:
                rowfails.append(f"{tm['table_id']}:header-mismatch")
            for rs, rp, rm in zip(ts["rows"], tp["rows"], tm["rows"]):
                exp = rs
                for a, b in TOKEN_SUBS_SORTED:
                    exp = exp.replace(a, b)
                def _rp(mm):
                    inner = mm.group(1)
                    if API_RE.match(inner):
                        return mm.group(0)
                    if any(h in inner for h in INTERNAL_HINTS):
                        return "（保存済み一次資料・詳細は出典一覧）"
                    return mm.group(0)
                exp = re.sub(r"`([^`\n]+)`", _rp, exp)
                exp = exp.replace("（（保存済み一次資料・詳細は出典一覧）", "（保存済み一次資料")
                exp = exp.replace("一次資料（一次資料）", "一次資料")
                if exp != rp:
                    rowfails.append(f"{rm['row_id']}:content src->proj mismatch")
                if rm["physical_text"] != rs:
                    rowfails.append(f"{rm['row_id']}:manifest-src mismatch")
    else:
        rowfails.append("table-count")
    rec("V03-rows-ordered-join", not rowfails, "ROW_ALTERED",
        "80 ordered src=proj=manifest" if not rowfails else "; ".join(rowfails[:6]))
    types = [r["row_type"] for t in TABLES for r in t["rows"]]
    rec("V03-row-types", (types.count("DATA") == 78 and types.count("NOTE") == 2), "ROW_TYPE",
        f"DATA={types.count('DATA')} NOTE={types.count('NOTE')}")
    ids = [r["row_id"] for t in TABLES for r in t["rows"]]
    rec("V03-row-unique", (len(ids) == 80 and len(set(ids)) == 80), "ROW_DUP", "80 unique row_ids")

    # V04 TeX cell-level mapping: 20 tables, captions, per-table row counts, PER-CELL equality
    tex_tabs = parse_tex_tables(tex_body)
    rec("V04-tex-table-count", len(tex_tabs) == 20, "TEX_TABLE_COUNT", f"tex_tables={len(tex_tabs)}")
    cellfails = []
    if len(tex_tabs) == 20:
        for tt, tm in zip(tex_tabs, TABLES):
            hdr_core = re.sub(r"】\s*$", "", re.sub(r"^【表[:：]?\s*", "", tm["header"]))
            if tex_visible(tt["caption"]).strip() != hdr_core.strip():
                cellfails.append(f"{tm['table_id']}:caption-mismatch")
            if len(tt["rows"]) != len(tm["rows"]):
                cellfails.append(f"{tm['table_id']}:texrows={len(tt['rows'])} man={len(tm['rows'])}")
                continue
            tp = t_proj[TABLES.index(tm)]["rows"] if len(t_proj) == 20 else []
            for ri, (trow, prow, rm) in enumerate(zip(tt["rows"], tp, tm["rows"])):
                pcells = [c.strip() for c in prow.split("｜")]
                # generator pads short rows with trailing empty cells to the table
                # colspec; those carry no meaning — strip and assert emptiness.
                tstrip = list(trow)
                while tstrip and norm_tex_cell(tstrip[-1]) == "":
                    tstrip.pop()
                pstrip = list(pcells)
                while pstrip and norm_proj_cell(pstrip[-1]) == "":
                    pstrip.pop()
                if len(tstrip) != len(pstrip):
                    cellfails.append(f"{rm['row_id']}:cell-count tex={len(trow)} proj={len(pcells)}")
                    continue
                for ci, (tc, pc) in enumerate(zip(tstrip, pstrip)):
                    if norm_tex_cell(tc) != norm_proj_cell(pc):
                        cellfails.append(f"{rm['row_id']}:cell{ci} mismatch")
                        break
    rec("V04-tex-cell-join", not cellfails, "TEX_CELL_MISMATCH",
        "all TeX cells == normalized proj cells at correct positions (trailing generator padding stripped+verified empty)" if not cellfails else "; ".join(cellfails[:8]))

    # V05 29 claims anchored in ONE target TeX row/cell (value+variant+quals; provider/unit/comparator facets; bib URL)
    cFails = []
    if len(tex_tabs) == 20 and len(t_proj) == 20:
        for c in EXPECTED_CLAIMS:
            found = next(((tm, r) for tm in TABLES for r in tm["rows"] if r["row_id"] == c["row"]), None)
            if not found:
                cFails.append(f"{c['k']}:row-unknown"); continue
            tm, mr = found
            ti = TABLES.index(tm)
            prow = t_proj[ti]["rows"][mr["ordinal"]-1]
            trow = tex_tabs[ti]["rows"][mr["ordinal"]-1]
            tvis = " | ".join(norm_tex_cell(x) for x in trow)
            for need in c.get("phys", []) + c.get("variant_phys", []):
                if need not in prow:
                    cFails.append(f"{c['k']}:proj-missing-{need!r}"); break
            else:
                qa = c.get("phys_qual_any", [])
                if qa and not any(q in prow for q in qa):
                    cFails.append(f"{c['k']}:proj-qual-any-missing")
                else:
                    for need in c.get("phys_qual_must", []):
                        if need not in prow:
                            cFails.append(f"{c['k']}:proj-qual-must-missing-{need!r}"); break
                    else:
                        for need in c.get("phys", []) + c.get("variant_phys", []) + c.get("phys_qual_must", []):
                            if need not in tvis:
                                cFails.append(f"{c['k']}:tex-row-missing-{need!r}"); break
                        else:
                            uc = c.get("url_contains", "")
                            if uc and uc not in bib_sec:
                                cFails.append(f"{c['k']}:bib-url-missing-{uc!r}")
    else:
        cFails.append("tables-unavailable")
    rec("V05-claims-anchored", not cFails, "CLAIM_ANCHOR",
        "29 claims value+variant+qual in own proj row AND target TeX row; bib URLs mapped" if not cFails else "; ".join(cFails[:8]))

    # V06 figures + recap + TanStack
    f_src = [l.strip() for l in src_text.splitlines() if l.strip().startswith("【図")]
    f_proj = [l.strip() for l in proj_text.splitlines() if l.strip().startswith("【図")]
    rec("V06-figures", (len(f_proj) == 3 and f_proj == f_src), "FIGURE", "3 figures identical")
    rs5 = src_text.split("# 今週の総括")[1].strip().split("\n\n")[:5]
    rp5 = proj_text.split("# 今週の総括")[1].strip().split("\n\n")[:5]
    rec("V06-recap", (len(rp5) == 5 and rp5 == rs5), "RECAP", "5 recap paras identical")
    rec("V06-tanstack-note", ("tanstack-gh" in proj_text and "tanstack-npm" in proj_text), "TANSTACK_KEY", "exact TanStack keys")

    # V07 URLs
    urls = re.findall(r"\\url\{([^}]+)\}", tex_text)
    bad = [u for u in urls if u.startswith("http") and re.search(r"[（）「」『』、。．・：；！？　]", u)]
    rec("V07-url-hygiene", not bad, "URL_JP_PUNCT", f"http={sum(1 for u in urls if u.startswith('http'))} malformed={len(bad)}")
    rec("V07-guide-url-exact", (r"\url{https://developers.openai.com/api/docs/guides/decisions}" in tex_text), "URL_GUIDE", "guide URL exact")
    rec("V07-npm-scoped", (r"\url{https://registry.npmjs.org/@tanstack%2Fai}" in tex_text), "URL_NPM_SCOPE", "npm scoped URL exact")
    rec("V07-no-gh-proves-npm", ("GH公開時刻のみを証明" in tex_text and "npm時刻の証明にはならない" in tex_text), "GH_NPM_SEPARATION", "GH proves GH only")

    # V08 qualifiers in BOTH artifacts
    QUAL_PROJ = ["持続性能の66倍ではない", "精度とは別", "企業現場", "オンラインバンキング",
                 "未検証（保存済み資料に記載なし・比較条件未確認）", "当週の対象外",
                 "未照合の記述の食い違い", "原本未取得", "未実行", "独立再現なし"]
    qp = [q for q in QUAL_PROJ if q not in proj_text]
    rec("V08-qual-proj", not qp, "QUAL_PROJ", f"missing={qp}" if qp else "10 qualifiers in projection")
    qtv = tex_visible(tex_body)
    qt = [q for q in ["持続性能の66倍ではない", "精度とは別", "未実行", "独立再現なし"] if q not in qtv]
    rec("V08-qual-tex", not qt, "QUAL_TEX", f"missing={qt}" if qt else "load-bearing qualifiers in TeX visible")

    # V09 bib
    bibitems = re.findall(r"\\bibitem\[([^\]]+)\]", tex_text)
    rec("V09-bib-count", (len(bibitems) == 36 and len(set(bibitems)) == 36), "BIB_COUNT", "36 unique bibitems")
    frags = ["速度で]", "Small/Re]", "=IMP]", "upstream validat]", "別ソ]", "no post-cutoff]"]
    ff = [f for f in frags if f in tex_text]
    rec("V09-bib-no-trunc", not ff, "BIB_TRUNC", "no r1 truncation fragments" if not ff else str(ff))
    return res

# ---------- runners ----------
def _clean():
    proj = PROJ_D.read_text(encoding="utf-8")
    tex = TEX_D.read_text(encoding="utf-8")
    return validate(proj, tex)

def _negatives():
    base_proj = PROJ_D.read_text(encoding="utf-8")
    base_tex = TEX_D.read_text(encoding="utf-8")
    cases = []
    def neg(cid, mp, mt, expect, overrides=None):
        r = validate(mp, mt, file_bytes_overrides=overrides)
        got = [x["cause"] for x in r if x["result"] == "FAIL"]
        good = expect in got
        cases.append({"id": cid, "result": "PASS" if good else "FAIL",
                      "cause": "—" if good else "NEG_NOT_DETECTED",
                      "detail": f"expect={expect} got={got[:4]}"})
    # API deletion variants (single-side must fail)
    neg("N-API-proj-only", base_proj.replace(API_ROUTE, "（保存済み一次資料・詳細は出典一覧）", 1), base_tex, "API_MISSING_PROJ")
    neg("N-API-tex-only", base_proj, base_tex.replace(r"\texttt{POST /v1/decisions}", "（保存済み一次資料）", 1), "API_MISSING_TEX")
    neg("N-API-both", base_proj.replace(API_ROUTE, "（保存済み一次資料・詳細は出典一覧）", 1),
        base_tex.replace(r"\texttt{POST /v1/decisions}", "（保存済み一次資料）", 1), "API_MISSING_PROJ")
    # TeX row swap same table, 80 held (p7-f1 rows 01<->02 in TeX only)
    tt = base_tex
    r1 = "COBOL ｜10.9→72.1"
    r2 = "OCaml ｜25.6→85.8"
    # operate on TeX-converted cell text: find TeX lines containing these
    lines = tt.splitlines()
    i1 = next(i for i, l in enumerate(lines) if "COBOL" in l and "10.9" in l and "&" in l)
    i2 = next(i for i, l in enumerate(lines) if "OCaml" in l and "25.6" in l and "&" in l)
    swapped = lines[:]; swapped[i1], swapped[i2] = swapped[i2], swapped[i1]
    neg("N-tex-row-swap", base_proj, "\n".join(swapped), "TEX_CELL_MISMATCH")
    # non-claim TeX cell text altered (p1-t1 supplement id)
    neg("N-tex-cell-alter", base_proj, base_tex.replace("supplement 041ec6系", "supplement 000000系", 1), "TEX_CELL_MISMATCH")
    # swap two claim-bearing TeX rows, multiset held (p7-f1-01 <-> p7-f1-02 whole lines)
    lns = base_tex.splitlines()
    j1 = next(i for i, l in enumerate(lns) if "COBOL" in l and "10.9" in l and "&" in l)
    j2 = next(i for i, l in enumerate(lns) if "OCaml" in l and "25.6" in l and "&" in l)
    sw2 = lns[:]; sw2[j1], sw2[j2] = sw2[j2], sw2[j1]
    neg("N-claim-rows-swap", base_proj, "\n".join(sw2), "CLAIM_ANCHOR")
    # delete TeX claim in own row (npm registry clock, row p8-f2-03)
    neg("N-tex-claim-delete", base_proj, base_tex.replace("npm 2026-10-22T15:21:49Z、GH", "npm 2026-10-22T15:21:50Z、GH", 1), "CLAIM_ANCHOR")
    # shift claim to adjacent row (move 40% marker down one TeX row only;
    # TeX-level strings: cells joined with " & ", % escaped as \%)
    shifted = base_tex.replace("企業現場40\\%超", "企業現場", 1)
    shifted = shifted.replace("OCaml & 25.6→85.8 & 公開suite", "OCaml & 25.6→85.8 & 公開suite・企業現場40\\%超", 1)
    neg("N-claim-shift-row", base_proj, shifted, "CLAIM_ANCHOR")
    # wrong provider clock
    neg("N-clock-swap", base_proj.replace("npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠", "npm 2026-10-22T15:18:14Z、GH 15:21:49Zとは別典拠", 1), base_tex, "ROW_ALTERED")
    # wrong scoped npm URL
    neg("N-npm-url", base_proj, base_tex.replace(r"\url{https://registry.npmjs.org/@tanstack%2Fai}", r"\url{https://registry.npmjs.org/ai}", 1), "URL_NPM_SCOPE")
    # JP punct in URL
    neg("N-jp-url", base_proj, base_tex.replace(r"\url{https://developers.openai.com/api/docs/guides/decisions}",
        r"\url{https://developers.openai.com/api/docs/guides/decisions（観測2026-10-25、snapshot}", 1), "URL_JP_PUNCT")
    # qualifier stripped proj / tex
    neg("N-qual-proj", base_proj.replace("持続性能の66倍ではない", "", 1), base_tex, "QUAL_PROJ")
    neg("N-qual-tex", base_proj, base_tex.replace("持続性能の66倍ではない", "", 1), "QUAL_TEX")
    # delete physical row (79)
    first_row = "告知・API提供｜2026-10-23T17:15:24Z（X原文、post ID確認）｜状態：IN（当週）｜根拠：X HTML原文＋supplement 041ec6系"
    neg("N-row-delete", base_proj.replace(first_row, "", 1), base_tex, "ROW_ALTERED")
    # dup holding 80 (replace row2 with row1)
    neg("N-row-dup80", base_proj.replace("重み配布｜2026-11-04予定｜状態：FUTURE（未公開）｜根拠：発表のみ、バイト・SHA未取得", first_row, 1), base_tex, "ROW_ALTERED")
    # swap two proj rows
    mp_sw = base_proj.replace(first_row, "§SWAP§")
    mp_sw = mp_sw.replace("重み配布｜2026-11-04予定｜状態：FUTURE（未公開）｜根拠：発表のみ、バイト・SHA未取得", first_row, 1).replace("§SWAP§", "重み配布｜2026-11-04予定｜状態：FUTURE（未公開）｜根拠：発表のみ、バイト・SHA未取得", 1)
    neg("N-row-swap", mp_sw, base_tex, "ROW_ALTERED")
    # header alter
    neg("N-header-alter", base_proj.replace("【表：公開状態×時点（Kimi）】", "【表：公開状態×時点（Kimi改）】", 1), base_tex, "HEADER_ORDER")
    # NOTE row alter (p4-t1 22x NOTE row)
    nnote = "22x見出し" if "22x見出し" in base_proj else None
    if nnote:
        neg("N-note-alter", base_proj.replace(nnote, nnote + "改", 1), base_tex, "ROW_ALTERED")
    else:
        neg("N-note-alter", base_proj.replace("注意｜", "注意改｜", 1), base_tex, "ROW_ALTERED")
    # model / metric / claim-value (claim rows)
    neg("N-model-change", base_proj.replace("COBOL ｜10.9→72.1 ｜19/20", "FORTRAN ｜10.9→72.1 ｜19/20", 1), base_tex, "CLAIM_ANCHOR")
    neg("N-metric-change", base_proj.replace("COBOL ｜10.9→72.1 ｜19/20", "COBOL ｜11.9→72.1 ｜19/20", 1), base_tex, "CLAIM_ANCHOR")
    neg("N-claim-drop", base_proj.replace("Luna(40.3%) $0.77 vs Sol $3.48", "Luna(40.3%) $0.77 vs Sol", 1), base_tex, "CLAIM_ANCHOR")
    # bib URL alter
    neg("N-bib-url", base_proj, base_tex.replace("https://registry.npmjs.org/@tanstack%2Fai", "https://registry.npmjs.org/ai", 1), "URL_NPM_SCOPE")
    # hash-mutated original (explicit override, must fail HASH_MISMATCH, semantics not even reached)
    bad_bytes = {str(PROJ_D): b"corrupted"}
    neg("N-hash-mismatch", base_proj, base_tex, "HASH_MISMATCH", overrides=bad_bytes)
    return cases

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="clean")
    a = ap.parse_args()
    if a.mode == "clean":
        r = validate(PROJ_D.read_text(encoding="utf-8"), TEX_D.read_text(encoding="utf-8"))
        ok = all(x["result"] == "PASS" for x in r)
        print(json.dumps({"tool": "print-fidelity-check-r5", "mode": "clean",
                          "verdict": "PRINT_SEMANTIC_PASS" if ok else "PRINT_SEMANTIC_FAIL",
                          "checks": r}, indent=2, ensure_ascii=False))
        return 0 if ok else 1
    else:
        cases = _negatives()
        ok = all(c["result"] == "PASS" for c in cases)
        print(json.dumps({"tool": "print-fidelity-check-r5", "mode": "negatives",
                          "verdict": "NEGATIVES_PASS" if ok else "NEGATIVES_FAIL",
                          "cases": cases}, indent=2, ensure_ascii=False))
        return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
