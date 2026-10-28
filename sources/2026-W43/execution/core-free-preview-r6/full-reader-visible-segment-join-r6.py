#!/usr/bin/env python3
"""r6 full reader-visible segment join validator (Phase A, edition-local).

Closes independent r5 P1 (W43-R5-AUD-01): r5 V06-recap/V06-figures checked
only headings/counts and its H00 hashed on-disk files instead of the actual
tested inputs. This checker proves ordered 1:1 content identity for EVERY
reader-visible segment from r3.5 reader -> r3 projection -> old r3 TeX:

  title, 8 P-sections, 28 subsections, 71 prose paragraphs, 8 reading-note
  blockquotes, 3 figures (full bodies), 5 code blocks, 20 tables / 80 ordered
  rows / 307 nonempty cells / 18 table notes, 29 anchored claims, all five
  recap paragraphs, 36 bibliography items, POST route / URLs / qualifiers.

Source->projection changes are allowed ONLY through an explicit per-segment
allowlist (operator token translations, internal-path masking, ONE title
relabel, ONE TanStack body addition F-R3-03, ONE POST_CUTOFF space rule).
Projection->TeX changes are allowed ONLY through formatting transforms
(escapes, textbf/texttt/url, heading dash rule, ONE authorized paragraph
split, ONE production-note insertion in r3 / deletion in r6, bibliography
apparatus transplant). Anything else is PARTIAL/BLOCKED, never lossless PASS.

No hardcoded repository paths: use --repo-root and/or explicit input paths.
Supports --staged-dir for offline independent replay. No network. No Core
dependencies beyond edition-local immutable originals + the r3.5 strict
checker EXPECTED_CLAIMS table (read-only, AST-parsed).

Exit 0 only on full PASS (clean) / all negatives detected (negatives).
"""
import argparse
import ast
import difflib
import hashlib
import json
import pathlib
import re
import sys

# --------------------------------------------------------------------------
# Pinned identity of the six immutable inputs (actual bytes, never asserted
# for files under test that are allowed to change).
# --------------------------------------------------------------------------
REL = {
    "r35_reader": "sources/2026-W43/execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md",
    "r35_ledger": "sources/2026-W43/execution/editorial-bypass/w43-r3-5-citation-confidence-ledger.json",
    "r35_manifest": "sources/2026-W43/execution/editorial-bypass/w43-r3-5-physical-row-manifest.json",
    "r3_projection": "sources/2026-W43/execution/core-free-preview-r3/reader-print-projection-r3.md",
    "r3_tex": "sources/2026-W43/execution/core-free-preview-r3/main.tex",
    "r3_pdf": "sources/2026-W43/execution/core-free-preview-r3/main.pdf",
}
EXPECTED_HASH = {
    "r35_reader": "6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6",
    "r35_ledger": "6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4",
    "r35_manifest": "85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111",
    "r3_projection": "63ad2617f663a01bd14a93b803a96272bf3cc72debbdf4817f81c6596eccbe80",
    "r3_tex": "bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed",
    "r3_pdf": "d0fa8b56c29971c5405f0e36dd856c07c14aa5cc8c9f4d17e14a2985949ef7ca",
}
STRICT_CHECKER_REL = "sources/2026-W43/execution/editorial-bypass/w43-r3-5-strict-semantic-claim-join-check.py"

TOKEN_SUBS_SORTED = sorted([
    ("PRIMARY_METADATA", "一次資料（付随情報）"),
    ("PRIMARY_RAW", "一次資料"),
    ("SOURCE_UNVERIFIED", "未検証（保存済み資料に記載なし・比較条件未確認）"),
    ("RENDERED_ONLY", "描画抽出のみ（原本HTMLの閲覧ではない）"),
    ("RENDERED_TEXT", "描画抽出テキストのみ（原本HTMLの閲覧ではない）"),
    ("NOT_EXECUTED", "未実行"),
    ("NOT_RUN", "未実行（API呼出しなし）"),
    ("PSEUDOCODE", "疑似コード（実行できない抜粋）"),
    ("NONRUNNABLE", "実行不可の抜粋"),
    ("IMPORT_UNVERIFIED", "導入経路は未確認"),
    ("NEVER_STORY", "当週の対象外"),
    ("POST_CUTOFF／OUT", "集計期間外のため当週非選択"),
    ("POST_CUTOFF/OUT", "集計期間外のため当週非選択"),
    ("UNRESOLVED_FAQ_ATTRIBUTION", "未照合の記述の食い違い（出典・版・観測時刻は未特定のため確定した矛盾としない）"),
    ("UNRESOLVED_VENDOR_DOC_CONFLICT", "資料間で不一致があり単一値に統一しない"),
    ("UNRESOLVED", "未解決（単一値に統一しない）"),
    ("COMPARATOR_UNVERIFIED", "比較対象・内訳は未確認"),
    ("UNIT_UNVERIFIED", "単位の記載は未確認"),
    ("VENDOR_BENCH", "発行元測定（独立再現なし）"),
], key=lambda kv: -len(kv[0]))

API_ROUTE = "`POST /v1/decisions`"
INTERNAL_HINTS = ("sources/", ".md", ".py", ".html", "task-",
                  "memt-", "deepinfer-", "flint-", "recursive-", "w43-", "environ.py")
API_RE = re.compile(r"^(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+/")

TITLE_R35 = "# W43 日本語本文プレビュー r3.5（非正規編集資産）"
TITLE_PROJ = "# 週刊生成AI技術調査 2026-W43 — 印刷用原稿 r3"
TANSTACK_ADDITION = "典拠: 安定核=tanstack-gh（GH 15:18:14Zのみ）／npm=tanstack-npm（15:21:49Z・別典拠・原本未取得）"
PRODUCTION_NOTE_TEX = "{\\small\\color{SurveyMuted}P8の後に置く独立した締めくくり（5段落）。新規のP9パッケージではない。\\par}"

# The independent auditor's exact adversarial mutant (must be caught by the
# recap semantic check while table/cell/claim/citation/qualifier checks stay
# green -- proving r5 scope could not see it).
RECAP_SEMANTIC_REVERSAL_NEEDLE = "all independently validated commercially"
RECAP_P1_HEAD = "今週の生成AI関連の発表を貫くのは"

NATURAL_QUOTES = {
    "1pw-blog-1022": "1Password発表（2026-10-22、coming soon）",
    "flux-elo-1139": "Elo 1139 は暫定値",
    "flux-keyframes-conflict": "Two at launch",
    "voxtral-card-units": "cpWER 18.4/18.6",
    "deepinfer-import-scope": "SamplingParams",
    "flux-speed-recalc": "277.80秒÷10.95秒",
    "ming-aa-cited": "AA三行=発行元引用",
    "eleven-blog": "移行指南は未開封",
    "patch-rendered": "五段階",
    "securing-page-rss": "RSS",
    "tanstack-blog": "blog10月23日は日付のみ",
    "decisions-guide-1025": "70f106a9",
    "decisions-ts-ref-1025": "30m",
}


# --------------------------------------------------------------------------
# Normalization
# --------------------------------------------------------------------------

def norm_src_line(s):
    """r3.5 reader line -> expected projection line (allowlisted only)."""
    # Observed byte-exact rule: the projection replaced the redundant
    # 'POST_CUTOFF／OUT であり当週非選択' with the cleaned translation
    # (the token already entails 当週非選択; the dangling であり moved).
    exp = s.replace("POST_CUTOFF／OUT であり当週非選択",
                    "集計期間外のため当週非選択であり")
    exp = exp.replace("POST_CUTOFF/OUT であり当週非選択",
                      "集計期間外のため当週非選択であり")
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
    return exp


def tex_visible(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(
        r"\\(?:texttt|textbf|textsl|emph|url|nolinkurl|color|small|footnotesize|scriptsize)"
        r"\*?(?:\[[^\]]*\])?\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[A-Za-z]+(?:\[[^\]]*\])?(?:\{[^}]*\})?", "", s)
    for a, b in [("\\%", "%"), ("\\#", "#"), ("\\$", "$"), ("\\&", "&"),
                 ("\\_", "_"), ("\\textasciitilde{}", "~"),
                 ("\\textasciicircum{}", "^"), ("\\textbackslash{}", "\\")]:
        s = s.replace(a, b)
    s = s.replace("{", "").replace("}", "")
    return s


def norm_md_inline(s):
    return s.replace("`", "").replace("**", "")


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def norm_tex_para(s):
    return collapse(tex_visible(s))


def norm_proj_para(s):
    return collapse(norm_md_inline(s))


# --------------------------------------------------------------------------
# Document structure parsers (shared by clean + negatives through ONE path)
# --------------------------------------------------------------------------

def split_fences(lines):
    """Yield ('fence', lang, body) or ('text', None, [line]) items."""
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^```(\S*)\s*$", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            out.append(("fence", m.group(1), lines[i + 1:j]))
            i = j + 1
        else:
            out.append(("text", None, [lines[i]]))
            i += 1
    return out


def parse_md_tables(md_text):
    lines = md_text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i + 1:j]
            if body and body[0].strip().startswith("【表"):
                out.append({"header": body[0].strip(),
                            "rows": [l for l in body if "｜" in l],
                            "notes": [l for l in body[1:]
                                      if "｜" not in l and l.strip()]})
            i = j + 1
        else:
            i += 1
    return out


def parse_md_figures(md_text):
    lines = md_text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i + 1:j]
            if body and body[0].strip().startswith("【図"):
                out.append({"header": body[0].strip(), "body": body[1:]})
            i = j + 1
        else:
            i += 1
    return out


def parse_md_code(md_text):
    """Non-table/non-figure fenced blocks, in order, with language."""
    lines = md_text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^```(\S*)\s*$", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i + 1:j]
            if not (body and (body[0].strip().startswith("【表")
                              or body[0].strip().startswith("【図"))):
                out.append({"lang": m.group(1), "body": body})
            i = j + 1
        else:
            i += 1
    return out


def parse_md_prose(md_text):
    """Ordered prose segments outside fences.

    Returns dict with title/headings (real markdown headings only -- fence
    content lines starting with '#' are NOT headings), paras (list of line
    lists, quotes separated), quotes, recap paras.
    """
    lines = md_text.splitlines()
    inf = False
    masked = []
    for ln in lines:
        if ln.strip().startswith("```"):
            inf = not inf
            masked.append(None)
            continue
        masked.append(None if inf else ln)
    title = None
    headings = []
    paras = []
    quotes = []
    cur = []
    in_recap = False
    recap = []

    def flush():
        nonlocal cur
        if cur:
            if in_recap:
                recap.append(cur)
            else:
                paras.append(cur)
            cur = []

    for ln in masked:
        if ln is None:
            flush()
            continue
        if ln.startswith("#"):
            flush()
            if title is None and ln.startswith("# ") and "今週の総括" not in ln:
                title = ln
            else:
                headings.append(ln)
            in_recap = (ln.strip() == "# 今週の総括")
            continue
        if not ln.strip():
            flush()
            continue
        if "｜" in ln or ln.strip().startswith("【") or ln.strip() == "---":
            flush()
            continue
        if ln.strip().startswith("> "):
            flush()
            quotes.append(ln.strip()[2:])
            continue
        cur.append(ln)
    flush()
    return {"title": title, "headings": headings, "paras": paras,
            "quotes": quotes, "recap": recap}


def split_unescaped_amp(s):
    parts, cur = [], []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s):
            cur.append(ch)
            cur.append(s[i + 1])
            i += 2
            continue
        if ch == "&":
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
        i += 1
    parts.append("".join(cur))
    return parts


def parse_tex_tables(tex_body):
    tabs = []
    for m in re.finditer(
            r"\\begin\{table\}.*?\\caption\{(.*?)\}.*?\\begin\{tabularx\}"
            r"\{[^}]*\}\{(.*?)\}(.*?)\\end\{tabularx\}", tex_body, re.S):
        cap_raw, _colspec, inner = m.group(1), m.group(2), m.group(3)
        rows = []
        for ln in inner.splitlines():
            s = ln.strip()
            if not s or s.startswith(r"\toprule") or \
                    s.startswith(r"\midrule") or s.startswith(r"\bottomrule"):
                continue
            if not s.endswith("\\\\"):
                continue
            s = s[:-2].strip()
            if "&" not in s:
                continue
            rows.append(split_unescaped_amp(s))
        tabs.append({"caption": cap_raw, "rows": rows, "span": m.group(0)})
    return tabs


def parse_tex_figures(tex_text):
    figs = []
    for m in re.finditer(r"\\begin\{figure\}.*?\\end\{figure\}",
                         tex_text, re.S):
        span = m.group(0)
        title = re.search(r"title=\{(.*?)\}", span, re.S)
        inner = re.search(r"\{\\footnotesize\s(.*?)\\par\}", span, re.S)
        bodylines = []
        if inner:
            for ln in inner.group(1).splitlines():
                t = ln.strip()
                if not t:
                    continue
                if t.endswith("\\par"):
                    t = t[:-len("\\par")].strip()
                bodylines.append(t)
        figs.append({"title": title.group(1).strip() if title else "",
                     "body": bodylines, "span": span})
    return figs


def parse_tex_noteblocks(tex_text):
    """SurveyRule reading-note boxes (md '> 【読み方の注意】' counterpart)."""
    notes = []
    for m in re.finditer(
            r"\\begin\{tcolorbox\}\[[^\]]*?SurveyRule.*?"
            r"\\end\{tcolorbox\}", tex_text, re.S):
        span = m.group(0)
        inner = re.search(r"\](.*?)\\end\{tcolorbox\}", span, re.S)
        text = inner.group(1).strip() if inner else ""
        text = norm_tex_para(text)
        notes.append(text)
    return notes


def parse_tex_verbatims(tex_text):
    return re.findall(r"\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}",
                      tex_text, re.S)


def parse_tex_prose_paras(tex_text):
    """Logical TeX prose paragraphs (tables/figures/code/noteboxes/bib out)."""
    body = tex_text.split(r"\begin{document}")[1].split(r"\end{document}")[0]
    b2 = re.sub(r"\\begin\{(verbatim|lstlisting|minted|Verbatim)\}.*?"
                r"\\end\{\1\}", "\n[CODE]\n", body, flags=re.S)
    b2 = re.sub(r"\\begin\{table\}.*?\\end\{table\}", "\n[TABLE]\n", b2,
                flags=re.S)
    b2 = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", "\n[FIG]\n", b2,
                flags=re.S)
    b2 = re.sub(r"\\begin\{tcolorbox\}.*?\\end\{tcolorbox\}",
                "\n[NOTEBOX]\n", b2, flags=re.S)
    pre, _sep, _bib = b2.partition(r"\begin{thebibliography}")
    chunks = [p.strip() for p in re.split(r"\n\s*\n", pre) if p.strip()]
    return chunks


def parse_tex_recap(tex_text):
    m = re.search(r"\\section\*\{今週の総括\}(.*?)\\clearpage",
                  tex_text, re.S)
    if not m:
        return {"found": False, "note_present": False, "paras": []}
    region = m.group(1)
    note_present = PRODUCTION_NOTE_TEX in region
    region_wo_note = region.replace(PRODUCTION_NOTE_TEX, "")
    region_wo_note = re.sub(r"\\label\{[^}]*\}", "", region_wo_note)
    paras = [p.strip() for p in re.split(r"\n\s*\n", region_wo_note)
             if p.strip() and re.search(r"[぀-ヿ一-鿿A-Za-z0-9]",
                                        tex_visible(p.strip()))]
    return {"found": True, "note_present": note_present, "paras": paras}


def load_expected_claims(repo_root):
    src = (repo_root / STRICT_CHECKER_REL).read_text(encoding="utf-8")
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "EXPECTED_CLAIMS"
                for t in node.targets):
            claims = ast.literal_eval(node.value)
            assert isinstance(claims, list) and len(claims) == 29, \
                f"EXPECTED_CLAIMS must hold 29 entries, got {len(claims) if isinstance(claims, list) else '?'}"
            return claims
    raise AssertionError("EXPECTED_CLAIMS not found in strict checker")

# --------------------------------------------------------------------------
# Single validation entrypoint (clean + negatives share this code path)
# --------------------------------------------------------------------------

def validate(ctx, proj_text, tex_text, file_bytes_overrides=None,
             tex_role="r3"):
    """Validate in-memory (proj_text, tex_text) against immutable originals.

    ctx: resolved paths + pinned hashes + manifest tables + claims.
    file_bytes_overrides: {role: bytes} replacing on-disk bytes for the hash
      gate (explicit ephemeral harness state; never silently skipped).
    tex_role: 'r3' (production note must be PRESENT once -- documents the
      known print defect) or 'r6' (note must be ABSENT -- authorized
      print-only deletion; reinsertion fails INTERNAL_PRINT_NOTE_LEAK).
    Returns (results, evidence) where results is a list of
    {id, result, cause, detail} and evidence carries segment maps.
    """
    res = []
    ev = {"segment_allowlist": [], "tested_hashes": {}}

    def rec(cid, ok, cause, detail):
        res.append({"id": cid, "result": "PASS" if ok else "FAIL",
                    "cause": "—" if ok else cause, "detail": detail})

    # ---- input bytes: pinned immutable six + actually-tested strings ----
    disk_bytes = {}
    for role, path in ctx["paths"].items():
        try:
            disk_bytes[role] = pathlib.Path(path).read_bytes()
        except OSError:
            disk_bytes[role] = None
    missing = [r for r, b in disk_bytes.items() if b is None]
    h_fails = []
    for role, exp in EXPECTED_HASH.items():
        actual = (file_bytes_overrides.get(role)
                  if file_bytes_overrides and role in file_bytes_overrides
                  else disk_bytes.get(role))
        if actual is None:
            h_fails.append(f"{role}:MISSING_INPUT")
            continue
        if hashlib.sha256(actual).hexdigest() != exp:
            h_fails.append(f"{role}:HASH_MISMATCH")
    if missing:
        rec("H00-input-identity", False, "MISSING_INPUT",
            "missing: " + ",".join(missing))
    else:
        rec("H00-input-identity", not h_fails, "HASH_MISMATCH",
            "6/6 SHA256 match" if not h_fails else "; ".join(h_fails[:6]))

    proj_bytes = proj_text.encode("utf-8")
    tex_bytes = tex_text.encode("utf-8")
    ev["tested_hashes"]["tested_proj_sha256"] = hashlib.sha256(
        proj_bytes).hexdigest()
    ev["tested_hashes"]["tested_tex_sha256"] = hashlib.sha256(
        tex_bytes).hexdigest()
    on_disk_proj = (file_bytes_overrides.get("r3_projection")
                    if file_bytes_overrides
                    and "r3_projection" in file_bytes_overrides
                    else disk_bytes.get("r3_projection"))
    on_disk_tex = (file_bytes_overrides.get("r3_tex")
                   if file_bytes_overrides and "r3_tex" in file_bytes_overrides
                   else disk_bytes.get("r3_tex"))
    ev["tested_hashes"]["ondisk_proj_sha256"] = \
        hashlib.sha256(on_disk_proj).hexdigest() if on_disk_proj else None
    ev["tested_hashes"]["ondisk_tex_sha256"] = \
        hashlib.sha256(on_disk_tex).hexdigest() if on_disk_tex else None
    proj_mutated = (ev["tested_hashes"]["tested_proj_sha256"]
                    != ev["tested_hashes"]["ondisk_proj_sha256"])
    tex_mutated = (ev["tested_hashes"]["tested_tex_sha256"]
                   != ev["tested_hashes"]["ondisk_tex_sha256"])
    ev["tested_hashes"]["proj_mutated_input"] = proj_mutated
    ev["tested_hashes"]["tex_mutated_input"] = tex_mutated
    rec("H01-mutant-binding", True, "—",
        f"tested proj==disk:{not proj_mutated} tex==disk:{not tex_mutated} "
        f"(hash-bound, no stale oracle)")

    reader_text = ctx["reader_text"]
    md_r = parse_md_prose(reader_text)
    md_p = parse_md_prose(proj_text)
    tex_body = tex_text.split(r"\begin{thebibliography}")[0]
    bib_sec = tex_text.split(r"\begin{thebibliography}")[1] \
        if r"\begin{thebibliography}" in tex_text else ""

    # ---- S01 title (single allowlisted relabel) ----
    if md_r["title"] == TITLE_R35 and md_p["title"] == TITLE_PROJ:
        ev["segment_allowlist"].append(
            {"segment": "TITLE", "rule": "TITLE_RELABEL",
             "from": TITLE_R35, "to": TITLE_PROJ})
        rec("S01-title", True, "—", "1 allowlisted title relabel")
    else:
        rec("S01-title", False, "TITLE",
            f"r35={md_r['title']!r} proj={md_p['title']!r}")

    # ---- S02 headings: 8 P + 28 sub + recap head ----
    rh = [h for h in md_r["headings"]]
    ph = [h for h in md_p["headings"]]
    p_secs = [h for h in ph if h.startswith("## ")]
    subs = [h for h in ph if h.startswith("### ")]
    heads_ok = (rh == ph and len(p_secs) == 8 and len(subs) == 28
                and "# 今週の総括" in ph)
    rec("S02-headings-reader-proj", heads_ok, "HEADING",
        f"P={len(p_secs)} sub={len(subs)} identical"
        if heads_ok else f"r35={len(rh)} proj={len(ph)}")
    # projection -> TeX headings with the single dash rule
    tex_secs = re.findall(r"\\(?:sub)?section\*?\{(.*?)\}", tex_text)
    md_heads_for_tex = [h for h in ph if h.startswith("## ")
                        or h.startswith("### ") or h == "# 今週の総括"]
    want = []
    for h in md_heads_for_tex:
        if h.startswith("## "):
            want.append(h[3:].replace(" — ", " --- ", 1))
        elif h.startswith("### "):
            want.append(h[4:])
        else:
            want.append("今週の総括")
    # tex also carries cover title + P-section labels + bib head; require the
    # 37 content headings to appear in order as a subsequence.
    seq = [s for s in tex_secs]
    ok, idx = True, 0
    for w in want:
        try:
            idx = seq.index(w, idx) + 1
        except ValueError:
            ok = False
            break
    dash_uses = sum(1 for h in ph if h.startswith("## ") and " — " in h)
    if ok:
        ev["segment_allowlist"].append(
            {"segment": "HEADINGS-TEX", "rule": "DASH_P_SECTION",
             "detail": f"{dash_uses} P-sections ' — ' -> ' --- '; "
                       f"28 subsections + recap verbatim"})
    rec("S02-headings-proj-tex", ok and len(want) == 37, "HEADING_TEX",
        f"{len(want)}/37 ordered" if ok else f"missing after idx {idx}")

    # ---- S03 prose ordered join (71 non-recap paras) ----
    r_paras_raw = [" ".join(b) for b in md_r["paras"]]
    p_paras_raw = [" ".join(b) for b in md_p["paras"]]
    if len(r_paras_raw) == len(p_paras_raw) == 71:
        fails = []
        for k, (rs, ps) in enumerate(zip(r_paras_raw, p_paras_raw)):
            if rs == ps:
                continue
            if norm_src_line(rs) == ps:
                rule = ("POST_CUTOFF_REDUNDANCY_CLEANUP"
                        if "POST_CUTOFF" in rs
                        else "TOKEN_OR_PATH_TRANSLATION")
                ev["segment_allowlist"].append(
                    {"segment": f"PROSE-r35p{k:02d}", "rule": rule})
                continue
            fails.append(f"PROSE-r35p{k:02d}")
        rec("S03a-prose-reader-proj", not fails, "PROSE_SRC_PROJ",
            "71/71 ordered" if not fails else "; ".join(fails[:6]))
    else:
        rec("S03a-prose-reader-proj", False, "PROSE_COUNT",
            f"r35={len(r_paras_raw)} proj={len(p_paras_raw)} want 71/71")

    # projection paras -> TeX logical body paras (recap handled in S07;
    # exactly one authorized split: 1 md para -> 2 TeX paras).
    t_chunks = parse_tex_prose_paras(tex_text)
    t_prose = [c for c in t_chunks
               if c not in ("[TABLE]", "[FIG]", "[CODE]", "[NOTEBOX]")
               and not c.startswith("\\")]
    # drop the bibliography-apparatus intro (transplant structure, S11 zone):
    # the '{\footnotesize\setlength...' line normalizes to '2pt0pt' and the
    # '本プレビューは非正準...' sentence lives inside a command chunk.
    bib_intro = [c for c in t_prose
                 if norm_tex_para(c) in ("2pt0pt", "")
                 or "非正準" in norm_tex_para(c)]
    t_mapped = [c for c in t_prose if c not in bib_intro]
    if bib_intro:
        ev["segment_allowlist"].append(
            {"segment": "BIB-APPARATUS", "rule": "PRINT_STRUCTURE_TRANSPLANT",
             "detail": f"{len(bib_intro)} TeX-only bibliography apparatus "
                       "chunk(s) excluded from prose mapping (checked in "
                       "S11, transplanted from the r2-complete block)"})
    tex_recap = parse_tex_recap(tex_text)
    if not tex_recap["found"] or len(tex_recap["paras"]) != 5:
        rec("S03b-prose-proj-tex", False, "RECAP_REGION",
            "TeX recap region must hold exactly 5 text paras")
        t_body = t_mapped
    else:
        pending = [norm_tex_para(p) for p in tex_recap["paras"]]
        t_body = []
        for c in t_mapped:
            n = norm_tex_para(c)
            if n in pending:
                pending.remove(n)
            else:
                t_body.append(c)
        if pending:
            rec("S03b-prose-proj-tex", False, "RECAP_REGION",
                f"{len(pending)} recap paras not located in TeX body")
            t_body = t_mapped
    md_body = md_p["paras"]  # non-recap only by construction (71)
    p_body_norm = [norm_proj_para(" ".join(b)) for b in md_body]
    t_body_norm = [norm_tex_para(x) for x in t_body]
    if not tex_recap["found"] or len(tex_recap["paras"]) != 5:
        pass  # already recorded above
    elif len(p_body_norm) == 71 and len(t_body_norm) == 72:
        sm = difflib.SequenceMatcher(a=p_body_norm, b=t_body_norm,
                                     autojunk=False)
        bad = [op for op in sm.get_opcodes() if op[0] != "equal"]
        # exactly one authorized paragraph split allowed:
        # one md para -> two consecutive TeX paras with identical
        # whitespace-collapsed concatenation.
        authorized = False
        if len(bad) == 1:
            tag, i1, i2, j1, j2 = bad[0]
            authorized = (tag == "replace"
                          and (i2 - i1) == 1 and (j2 - j1) == 2
                          and collapse(p_body_norm[i1])
                          == collapse(t_body_norm[j1] + " "
                                      + t_body_norm[j1 + 1]))
        if authorized:
            ev["segment_allowlist"].append(
                {"segment": "PROSE-split-reading-guide",
                 "rule": "AUTHORIZED_PARAGRAPH_SPLIT",
                 "detail": "1 md para (reading guide +典拠) -> 2 TeX paras"})
        rec("S03b-prose-proj-tex", authorized or not bad, "PROSE_PROJ_TEX",
            "71 md -> 72 tex (1 authorized split)"
            if (authorized or not bad) else f"non-equal: {bad[:3]}")
    else:
        rec("S03b-prose-proj-tex", False, "PROSE_COUNT_TEX",
            f"proj-body={len(p_body_norm)} tex-body={len(t_body_norm)} "
            f"(want 71/72)")

    # ---- S04 reading-note blockquotes (8) ----
    quotes_ok = (md_r["quotes"] == md_p["quotes"]
                 and len(md_p["quotes"]) == 8)
    rec("S04a-quotes-reader-proj", quotes_ok, "QUOTE",
        "8/8 identical" if quotes_ok
        else f"r35={len(md_r['quotes'])} proj={len(md_p['quotes'])}")
    tex_notes = parse_tex_noteblocks(tex_text)
    q_norm = [collapse(q) for q in md_p["quotes"]]
    if len(tex_notes) == 8 and q_norm and all(
            collapse(q) == t for q, t in zip(q_norm, tex_notes)):
        ev["segment_allowlist"].append(
            {"segment": "NOTES-TEX", "rule": "QUOTEBOX_WRAPPING",
             "detail": "8 md '> ' quotes -> 8 SurveyRule tcolorboxes"})
        rec("S04b-quotes-proj-tex", True, "—", "8/8 content-identical")
    else:
        rec("S04b-quotes-proj-tex", False, "QUOTE_TEX",
            f"md={len(q_norm)} tex={len(tex_notes)}")

    # ---- S05 figures (3 full bodies) ----
    f_r = parse_md_figures(reader_text)
    f_p = parse_md_figures(proj_text)
    f_t = parse_tex_figures(tex_text)
    fig_ok = len(f_r) == len(f_p) == len(f_t) == 3
    figfails = []
    if fig_ok:
        for k, (fr, fp, ft) in enumerate(zip(f_r, f_p, f_t)):
            if fr["header"] != fp["header"]:
                figfails.append(f"FIG{k}-header")
                continue
            # reader -> projection with token translation
            if [norm_src_line(x) for x in fr["body"]] != fp["body"]:
                figfails.append(f"FIG{k}-src-proj")
                continue
            ev["segment_allowlist"].append(
                {"segment": f"FIG{k}-src-proj",
                 "rule": "TOKEN_TRANSLATION_OR_IDENTICAL"})
            # projection -> TeX: title + par-joined body lines
            hdr_core = re.sub(r"^【図[:：]?\s*", "", fp["header"])
            hdr_core = re.sub(r"】\s*$", "", hdr_core)
            if collapse(ft["title"]) != collapse(hdr_core):
                figfails.append(f"FIG{k}-title")
                continue
            want_body = [norm_proj_para(x) for x in fp["body"]]
            got_body = [norm_tex_para(x) for x in ft["body"]]
            if want_body != got_body:
                figfails.append(f"FIG{k}-body")
    else:
        figfails.append("FIG_COUNT")
    rec("S05-figures-full", not figfails, "FIGURE",
        "3/3 full bodies" if not figfails else "; ".join(figfails[:6]))

    # ---- S06 code blocks (5, byte-exact proj->TeX) ----
    c_r = parse_md_code(reader_text)
    c_p = parse_md_code(proj_text)
    c_t = parse_tex_verbatims(tex_text)
    code_ok = (len(c_r) == len(c_p) == len(c_t) == 5)
    codefails = []
    if code_ok:
        for k, (cr, cp) in enumerate(zip(c_r, c_p)):
            if [norm_src_line(x) for x in cr["body"]] != cp["body"]:
                codefails.append(f"CODE{k}-src-proj")
            else:
                ev["segment_allowlist"].append(
                    {"segment": f"CODE{k}-src-proj",
                     "rule": "OPERATOR_TOKEN_TRANSLATION_IN_COMMENTS"})
        for k, (cp, tv) in enumerate(zip(c_p, c_t)):
            if cp["body"] != tv.splitlines():
                codefails.append(f"CODE{k}-proj-tex")
    else:
        codefails.append(f"CODE_COUNT r={len(c_r)} p={len(c_p)} t={len(c_t)}")
    # env-var/default sentinels: MTP defaults that negatives will mutate
    sentinel_ok = ("DEEPINFER_USE_NEXTN_DECODE=5" in tex_text
                   and 'os.environ["DEEPINFER_BATCH_INVARIANT"] = "1"'
                   in tex_text)
    if not sentinel_ok:
        codefails.append("CODE-SENTINEL")
    rec("S06-code-exact", not codefails, "CODE",
        "5/5 ordered" if not codefails else "; ".join(codefails[:6]))

    # ---- S07 recap (5 paras) + production-note gate ----
    rr = [" ".join(b) for b in md_r["recap"]]
    pr = [" ".join(b) for b in md_p["recap"]]
    recap_ok = (len(rr) == len(pr) == 5 and rr == pr)
    rec("S07a-recap-reader-proj", recap_ok, "RECAP",
        "5/5 identical" if recap_ok
        else f"r35={len(rr)} proj={len(pr)}")
    tr = tex_recap["paras"] if tex_recap["found"] else []
    tr_norm = [norm_tex_para(p) for p in tr]
    pr_norm = [norm_proj_para(p) for p in pr]
    recap_tex_ok = (len(tr) == 5 and tr_norm == pr_norm)
    rec("S07b-recap-proj-tex", recap_tex_ok, "RECAP_TEX",
        "5/5 visible-identical" if recap_tex_ok
        else f"tex={len(tr)}")
    if tex_role == "r3":
        note_ok = tex_recap["found"] and tex_recap["note_present"] and \
            tex_text.count(PRODUCTION_NOTE_TEX) == 1
        rec("S07c-print-note-r3", note_ok, "PRINT_NOTE",
            "known production note present x1 (defect documented)"
            if note_ok else "unexpected note state")
    else:
        note_ok = tex_recap["found"] and not tex_recap["note_present"] and \
            PRODUCTION_NOTE_TEX not in tex_text
        if note_ok:
            ev["segment_allowlist"].append(
                {"segment": "RECAP-note",
                 "rule": "AUTHORIZED_PRINT_ONLY_DELETION",
                 "detail": "exactly the P20 production-note line removed; "
                           "5 recap paras intact"})
        rec("S07c-print-note-r6", note_ok, "INTERNAL_PRINT_NOTE_LEAK",
            "production note absent, 5 paras intact"
            if note_ok else "note still present or region broken")

    # ---- S08/S09/S10: tables + cells + claims (r5 logic carried over) ----
    tables = ctx["tables"]
    exp_headers = [t["header"] for t in tables]
    t_src = parse_md_tables(reader_text)
    t_proj = parse_md_tables(proj_text)
    hs = [t["header"] for t in t_src]
    hp = [t["header"] for t in t_proj]
    rec("S08a-table-headers", hs == hp == exp_headers, "HEADER_ORDER",
        "20 identical order"
        if hs == hp == exp_headers else "mismatch")
    rowfails = []
    ok_tables = len(t_src) == len(t_proj) == 20
    if ok_tables:
        for _ti, (ts, tp, tm) in enumerate(zip(t_src, t_proj, tables)):
            if len(ts["rows"]) != len(tp["rows"]) or \
                    len(tp["rows"]) != len(tm["rows"]):
                rowfails.append(f"{tm['table_id']}:count")
                continue
            if ts["header"] != tm["header"] or tp["header"] != tm["header"]:
                rowfails.append(f"{tm['table_id']}:header-mismatch")
            for rs, rp, rm in zip(ts["rows"], tp["rows"], tm["rows"]):
                exp = norm_src_line(rs)
                if exp != rp:
                    rowfails.append(f"{rm['row_id']}:content src->proj")
                if rm["physical_text"] != rs:
                    rowfails.append(f"{rm['row_id']}:manifest-src")
    else:
        rowfails.append("table-count")
    rec("S08b-rows-ordered-join", not rowfails, "ROW_ALTERED",
        "80 ordered src=proj=manifest"
        if not rowfails else "; ".join(rowfails[:6]))
    types = [r["row_type"] for t in tables for r in t["rows"]]
    rec("S08c-row-types",
        types.count("DATA") == 78 and types.count("NOTE") == 2, "ROW_TYPE",
        f"DATA={types.count('DATA')} NOTE={types.count('NOTE')}")
    ids = [r["row_id"] for t in tables for r in t["rows"]]
    rec("S08d-row-unique", len(ids) == 80 and len(set(ids)) == 80,
        "ROW_DUP", "80 unique row_ids")
    # table fence trailing notes, reader -> projection
    notefails = []
    if ok_tables:
        for tm, tr, tpr in zip(tables, t_src, t_proj):
            if tr["notes"] == tpr["notes"]:
                continue
            if [norm_src_line(x) for x in tr["notes"]] == tpr["notes"]:
                ev["segment_allowlist"].append(
                    {"segment": f"TABLENOTE-{tm['table_id']}",
                     "rule": "TOKEN_TRANSLATION"})
                continue
            if (tm["table_id"] == "p8-f2"
                    and tr["notes"] == []
                    and tpr["notes"] == [TANSTACK_ADDITION]):
                ev["segment_allowlist"].append(
                    {"segment": "TABLENOTE-p8-f2",
                     "rule": "AUTHORIZED_BODY_ADDITION_F-R3-03",
                     "detail": TANSTACK_ADDITION})
                continue
            notefails.append(f"{tm['table_id']}:notes")
    else:
        notefails.append("table-count")
    rec("S08e-table-notes-reader-proj", not notefails, "TABLE_NOTE_SRC",
        "20/20 fence notes (1 token translation, 1 authorized addition)"
        if not notefails else "; ".join(notefails[:6]))

    tex_tabs = parse_tex_tables(tex_body)
    rec("S09a-tex-table-count", len(tex_tabs) == 20, "TEX_TABLE_COUNT",
        f"tex_tables={len(tex_tabs)}")
    cellfails = []
    if len(tex_tabs) == 20:
        for tt, tm in zip(tex_tabs, tables):
            hdr_core = re.sub(r"】\s*$", "",
                              re.sub(r"^【表[:：]?\s*", "", tm["header"]))
            if norm_tex_para(tt["caption"]) != collapse(hdr_core):
                cellfails.append(f"{tm['table_id']}:caption")
            if len(tt["rows"]) != len(tm["rows"]):
                cellfails.append(f"{tm['table_id']}:texrows="
                                 f"{len(tt['rows'])} man={len(tm['rows'])}")
                continue
            tp = t_proj[tables.index(tm)]["rows"] if len(t_proj) == 20 else []
            for _ri, (trow, prow, rm) in enumerate(
                    zip(tt["rows"], tp, tm["rows"])):
                pcells = [c.strip() for c in prow.split("｜")]
                tstrip = list(trow)
                while tstrip and norm_tex_para(tstrip[-1]) == "":
                    tstrip.pop()
                pstrip = list(pcells)
                while pstrip and norm_proj_para(pstrip[-1]) == "":
                    pstrip.pop()
                if len(tstrip) != len(pstrip):
                    cellfails.append(f"{rm['row_id']}:cell-count")
                    continue
                for _ci, (tc, pc) in enumerate(zip(tstrip, pstrip)):
                    if norm_tex_para(tc) != norm_proj_para(pc):
                        cellfails.append(f"{rm['row_id']}:cell-mismatch")
                        break
    nonempties = 0
    for t in t_proj:
        for r in t["rows"]:
            nonempties += sum(1 for c in r.split("｜") if c.strip())
    if nonempties != 307:
        cellfails.append(f"CELL-TOTAL={nonempties}")
    rec("S09b-tex-cell-join", not cellfails, "TEX_CELL_MISMATCH",
        "20 tables / 307 cells at correct positions"
        if not cellfails else "; ".join(cellfails[:8]))

    claims = ctx["claims"]
    cfails = []
    if len(tex_tabs) == 20 and len(t_proj) == 20:
        for c in claims:
            found = next(((tm, r) for tm in tables for r in tm["rows"]
                          if r["row_id"] == c["row"]), None)
            if not found:
                cfails.append(f"{c['k']}:row-unknown")
                continue
            tm, mr = found
            ti = tables.index(tm)
            prow = t_proj[ti]["rows"][mr["ordinal"] - 1]
            trow = tex_tabs[ti]["rows"][mr["ordinal"] - 1]
            tvis = " | ".join(norm_tex_para(x) for x in trow)
            for need in c.get("phys", []) + c.get("variant_phys", []):
                if need not in prow:
                    cfails.append(f"{c['k']}:proj-missing-{need!r}")
                    break
            else:
                qa = c.get("phys_qual_any", [])
                if qa and not any(q in prow for q in qa):
                    cfails.append(f"{c['k']}:proj-qual-any-missing")
                else:
                    for need in c.get("phys_qual_must", []):
                        if need not in prow:
                            cfails.append(
                                f"{c['k']}:proj-qual-must-{need!r}")
                            break
                    else:
                        for need in c.get("phys", []) + \
                                c.get("variant_phys", []) + \
                                c.get("phys_qual_must", []):
                            if need not in tvis:
                                cfails.append(
                                    f"{c['k']}:tex-row-missing-{need!r}")
                                break
                        else:
                            uc = c.get("url_contains", "")
                            if uc and uc not in bib_sec:
                                cfails.append(
                                    f"{c['k']}:bib-url-missing-{uc!r}")
    else:
        cfails.append("tables-unavailable")
    rec("S10-claims-anchored", not cfails, "CLAIM_ANCHOR",
        "29 claims in own proj row AND target TeX row; bib URLs mapped"
        if not cfails else "; ".join(cfails[:8]))

    # ---- S11 bibliography apparatus ----
    bibitems = re.findall(r"\\bibitem\[([^\]]+)\]", tex_text)
    rec("S11a-bib-count",
        len(bibitems) == 36 and len(set(bibitems)) == 36, "BIB_COUNT",
        "36 unique bibitems")
    frags = ["速度で]", "Small/Re]", "=IMP]", "upstream validat]",
             "別ソ]", "no post-cutoff]"]
    ff = [f for f in frags if f in tex_text]
    rec("S11b-bib-no-trunc", not ff, "BIB_TRUNC",
        "no r1 truncation fragments" if not ff else str(ff))

    # ---- S12 key spans (19/1/13/2/1/0, 13+2 quote-bound) ----
    vis = "\n".join(ln for ln in tex_body.splitlines()
                    if not ln.strip().startswith("%"))
    vis_nolabel = re.sub(r"\\label\{[^}]*\}", "", vis)
    natural = {"1pw-blog-1022", "flux-elo-1139", "flux-keyframes-conflict",
               "voxtral-card-units", "deepinfer-import-scope",
               "flux-speed-recalc", "ming-aa-cited", "eleven-blog",
               "patch-rendered", "securing-page-rss", "tanstack-blog",
               "decisions-guide-1025", "decisions-ts-ref-1025"}
    further = {"DI-ENV", "DI-LICENSE"}
    unavail = {"decisions-ref-create"}
    dist = {"EXACT_VISIBLE": 0, "EXACT_MACHINE_ONLY": 0, "NATURAL": 0,
            "FURTHER": 0, "UNAVAILABLE": 0, "ORPHAN": 0}
    quotefails = []
    orphans = []
    for k in bibitems:
        v = vis_nolabel.count(k)
        raw = tex_body.count(k)
        if v >= 1:
            dist["EXACT_VISIBLE"] += 1
        elif raw >= 1:
            dist["EXACT_MACHINE_ONLY"] += 1
        elif k in natural:
            dist["NATURAL"] += 1
            q = NATURAL_QUOTES[k]
            if q not in proj_text or q not in tex_visible(tex_text):
                quotefails.append(f"{k}:span")
        elif k in further:
            dist["FURTHER"] += 1
            q = {"DI-ENV": "environ.py",
                 "DI-LICENSE": "Apache-2.0"}[k]
            if q not in proj_text:
                quotefails.append(f"{k}:span")
        elif k in unavail:
            dist["UNAVAILABLE"] += 1
        else:
            dist["ORPHAN"] += 1
            orphans.append(k)
    want_dist = {"EXACT_VISIBLE": 19, "EXACT_MACHINE_ONLY": 1,
                 "NATURAL": 13, "FURTHER": 2, "UNAVAILABLE": 1, "ORPHAN": 0}
    rec("S12-key-spans", dist == want_dist and not quotefails
        and not orphans, "KEY_SPAN",
        f"{dist['EXACT_VISIBLE']}/{dist['EXACT_MACHINE_ONLY']}/"
        f"{dist['NATURAL']}/{dist['FURTHER']}/{dist['UNAVAILABLE']}/"
        f"{dist['ORPHAN']}"
        if dist == want_dist else f"got {dist} want {want_dist}; "
        f"span-fails={quotefails[:4]} orphans={orphans[:4]}")

    # ---- S13 routes / urls / qualifiers ----
    rec("S13a-api-proj", API_ROUTE in proj_text, "API_MISSING_PROJ",
        "POST code span in projection")
    rec("S13b-api-tex", r"\texttt{POST /v1/decisions}" in tex_body,
        "API_MISSING_TEX", "POST texttt in TeX body")
    urls = re.findall(r"\\url\{([^}]+)\}", tex_text)
    bad = [u for u in urls if u.startswith("http")
           and re.search(r"[（）「」『』、。．・：；！？　]", u)]
    rec("S13c-url-hygiene", not bad, "URL_JP_PUNCT",
        f"http={sum(1 for u in urls if u.startswith('http'))} "
        f"malformed={len(bad)}")
    rec("S13d-guide-url-exact",
        r"\url{https://developers.openai.com/api/docs/guides/decisions}"
        in tex_text, "URL_GUIDE", "guide URL exact")
    rec("S13e-npm-scoped",
        r"\url{https://registry.npmjs.org/@tanstack%2Fai}" in tex_text,
        "URL_NPM_SCOPE", "npm scoped URL exact")
    rec("S13f-gh-proves-gh",
        "GH公開時刻のみを証明" in tex_text
        and "npm時刻の証明にはならない" in tex_text, "GH_NPM_SEPARATION",
        "GH proves GH only")
    rec("S13g-tanstack-keys",
        "tanstack-gh" in proj_text and "tanstack-npm" in proj_text,
        "TANSTACK_KEY", "exact TanStack keys")
    qual_proj = ["持続性能の66倍ではない", "精度とは別", "企業現場",
                 "オンラインバンキング",
                 "未検証（保存済み資料に記載なし・比較条件未確認）",
                 "当週の対象外", "未照合の記述の食い違い", "原本未取得",
                 "未実行", "独立再現なし"]
    qp = [q for q in qual_proj if q not in proj_text]
    rec("S13h-qual-proj", not qp, "QUAL_PROJ",
        f"missing={qp}" if qp else "10 qualifiers in projection")
    qtv = tex_visible(tex_body)
    qt = [q for q in ["持続性能の66倍ではない", "精度とは別", "未実行",
                      "独立再現なし"] if q not in qtv]
    rec("S13i-qual-tex", not qt, "QUAL_TEX",
        f"missing={qt}" if qt else "load-bearing qualifiers in TeX visible")

    # ---- S14 table notes (18 md fence notes <-> TeX post-table notes) ----
    md_notes = []
    for t in t_proj:
        md_notes.extend(t["notes"])
    tex_notes_post = re.findall(
        r"\{\\scriptsize\\color\{SurveyMuted\} (.*?)\\par\}", tex_body)
    tn_norm = [norm_tex_para(x) for x in tex_notes_post]
    # the TanStack table note exists in proj (F-R3-03 addition) and TeX
    if len(md_notes) == 18 and len(tex_notes_post) == 18 and \
            [collapse(n) for n in md_notes] == tn_norm:
        ev["segment_allowlist"].append(
            {"segment": "TABLE-NOTES", "rule": "ESCAPE_ONLY",
             "detail": "18/18 fence notes == TeX post-table notes"})
        rec("S14-table-notes", True, "—", "18/18 notes escape-only")
    else:
        rec("S14-table-notes", False, "TABLE_NOTE",
            f"md={len(md_notes)} tex={len(tex_notes_post)}")

    # ---- S15 architecture 31-recount (report, never promotion) ----
    rec("S15-architecture-recount", True, "—",
        "see architecture-11-partial-disposition-r6.md (independent recount: "
        "diagnosis rows 18 SUBSTANTIVE / 13 PARTIAL vs header claim 20/11)")
    return res, ev

# --------------------------------------------------------------------------
# Negatives: every mutant runs through validate(); each asserts an explicit
# failure cause. Mandated mutants additionally assert that table / cell /
# claim / bibliography / route checks stay PASS (the old r5 scope could not
# see them -- the P1 point).
# --------------------------------------------------------------------------
OLD_SCOPE_OK = ["S08a-table-headers", "S08b-rows-ordered-join",
                "S08c-row-types", "S08d-row-unique",
                "S09a-tex-table-count", "S09b-tex-cell-join",
                "S10-claims-anchored", "S11a-bib-count", "S11b-bib-no-trunc",
                "S12-key-spans", "S13a-api-proj", "S13b-api-tex",
                "S13c-url-hygiene", "S13d-guide-url-exact",
                "S13e-npm-scoped", "S13f-gh-proves-gh", "S13g-tanstack-keys",
                "S13h-qual-proj", "S13i-qual-tex"]


def _once(text, needle, ctx_name):
    n = text.count(needle)
    if n != 1:
        raise AssertionError(
            f"mutant harness: needle for {ctx_name} found {n}x, want 1x: "
            f"{needle[:80]!r}")


def build_negatives(ctx, base_proj, base_tex):
    """Return list of negative case dicts (no validation run yet)."""
    cases = []
    base_psha = hashlib.sha256(base_proj.encode("utf-8")).hexdigest()
    base_tsha = hashlib.sha256(base_tex.encode("utf-8")).hexdigest()

    def case(cid, mp, mt, expect, role="r3", overrides=None,
             blindness=(), expect_pass=False, base_override=None):
        bpsha, btsha = base_psha, base_tsha
        if base_override is not None:
            bpsha = hashlib.sha256(
                base_override[0].encode("utf-8")).hexdigest()
            btsha = hashlib.sha256(
                base_override[1].encode("utf-8")).hexdigest()
        cases.append({"id": cid, "proj": mp, "tex": mt, "expect": expect,
                      "role": role, "overrides": overrides,
                      "blindness": list(blindness),
                      "expect_pass": expect_pass, "base_psha": bpsha,
                      "base_tsha": btsha})

    # -- mandated P1 adversarial: recap semantic reversal --
    # Exact replay of the independent auditor's in-memory TeX mutant: the
    # first recap paragraph's cautious view becomes an unqualified
    # 'all independently validated commercially' claim. Table / cell /
    # claim / citation / qualifier checks must stay green (blindness).
    r1_old = "その能力を**どの時点で、どの条件で、実際に利用できるのか**という問題である"
    r1_new = "その能力はall independently validated commerciallyという結論である"
    _once(base_proj, r1_old, "recap-proj")
    t1_old = ("その能力を\\textbf{どの時点で、どの条件で、"
              "実際に利用できるのか}という問題である")
    _once(base_tex, t1_old, "recap-tex")
    t1_new = ("その能力はall independently validated commercially"
              "という結論である")
    case("N-AUD-RECAP-SEMANTIC-REVERSAL",
         base_proj,
         base_tex.replace(t1_old, t1_new),
         ["RECAP_TEX"], blindness=OLD_SCOPE_OK)
    # Companion: the same reversal on the projection side proves the
    # reader-grounded S07a leg (not part of the audit mutant itself).
    case("N-RECAP-PROJ-DIVERGENCE",
         base_proj.replace(r1_old, r1_new),
         base_tex,
         ["RECAP"], blindness=OLD_SCOPE_OK)

    # -- delete one mid-section non-table paragraph (P4 Klein para) --
    klein = ("Klein（10月15日）は範囲外（OUT）、10月19日の PR が当週内（IN）"
             "という時間軸も要点である。")
    _once(base_proj, klein, "klein-para")
    lines = base_proj.splitlines()
    proj_del = "\n".join(l for l in lines if klein not in l)
    case("N-PARA-DELETE", proj_del, base_tex, ["PROSE_COUNT"],
         blindness=OLD_SCOPE_OK)

    # -- change an internal figure edge/step (p3-f1 route B state) --
    fig_old = "経路B（coming soon・NOT_LIVE_VERIFIED）"
    _once(base_proj, fig_old, "fig-edge")
    case("N-FIG-EDGE",
         base_proj.replace(fig_old, "経路B（live確定・NOT_LIVE_VERIFIED）"),
         base_tex, ["FIGURE"], blindness=OLD_SCOPE_OK)

    # -- change a code env default (TeX verbatim only) --
    code_old = "export DEEPINFER_USE_NEXTN_DECODE=5"
    _once(base_tex, code_old, "code-env")
    case("N-CODE-ENV", base_proj,
         base_tex.replace(code_old,
                           "export DEEPINFER_USE_NEXTN_DECODE=9"),
         ["CODE"], blindness=OLD_SCOPE_OK)

    # -- swap two full prose paragraphs (counts + word bag preserved) --
    pa = ("MoonshotのKimi K3.1 Proは10月23日の告知とAPI提供が先行し、"
          "重み配布は11月4日の将来予定である。")
    pb = "Kimiの規模をめぐる数字の扱いには慎重さが要る。"
    _once(base_proj, pa, "swap-a")
    _once(base_proj, pb, "swap-b")
    tok = "\ue000SWAP\ue001"
    assert tok not in base_proj
    swapped = base_proj.replace(pa, tok).replace(pb, pa).replace(tok, pb)
    case("N-PARA-SWAP", swapped, base_tex, ["PROSE_SRC_PROJ"],
         blindness=OLD_SCOPE_OK)

    # -- destroy one TeX recap paragraph (in-memory TeX only) --
    md_recaps = [" ".join(b) for b in parse_md_prose(base_proj)["recap"]]
    assert len(md_recaps) == 5
    victim = parse_tex_recap(base_tex)["paras"][2]
    _once(base_tex, victim, "tex-recap-victim")
    tex_rd = base_tex.replace(victim, "")
    case("N-TEX-RECAP-DESTROY", base_proj, tex_rd, ["RECAP_TEX"],
         blindness=OLD_SCOPE_OK)

    # -- alter only TeX body (one clock second; disk originals untouched) --
    clk_old = "17時15分24秒（協定世界時）"
    _once(base_tex, clk_old, "tex-clock")
    case("N-TEX-ONLY-ALTER", base_proj,
         base_tex.replace(clk_old, "17時15分25秒（協定世界時）"),
         ["PROSE_PROJ_TEX"], blindness=OLD_SCOPE_OK)

    # -- carried table/cell/claim/url/qualifier scope (dedup: single swap) --
    case("N-API-proj-only",
         base_proj.replace(API_ROUTE, "（保存済み一次資料・詳細は出典一覧）", 1),
         base_tex, ["API_MISSING_PROJ"])
    case("N-API-tex-only", base_proj,
         base_tex.replace(r"\texttt{POST /v1/decisions}", "（保存済み一次資料）", 1),
         ["API_MISSING_TEX"])
    case("N-API-both",
         base_proj.replace(API_ROUTE, "（保存済み一次資料・詳細は出典一覧）", 1),
         base_tex.replace(r"\texttt{POST /v1/decisions}", "（保存済み一次資料）", 1),
         ["API_MISSING_PROJ"])
    tlines = base_tex.splitlines()
    i1 = next(i for i, l in enumerate(tlines)
              if "COBOL" in l and "10.9" in l and "&" in l)
    i2 = next(i for i, l in enumerate(tlines)
              if "OCaml" in l and "25.6" in l and "&" in l)
    sw = tlines[:]
    sw[i1], sw[i2] = sw[i2], sw[i1]
    case("N-claim-rows-swap", base_proj, "\n".join(sw), ["CLAIM_ANCHOR"])
    case("N-tex-cell-alter", base_proj,
         base_tex.replace("supplement 041ec6系", "supplement 000000系", 1),
         ["TEX_CELL_MISMATCH"])
    case("N-tex-claim-delete", base_proj,
         base_tex.replace("npm 2026-10-22T15:21:49Z、GH",
                           "npm 2026-10-22T15:21:50Z、GH", 1),
         ["CLAIM_ANCHOR"])
    sh = base_tex.replace("企業現場40\\%超", "企業現場", 1)
    sh = sh.replace("OCaml & 25.6→85.8 & 公開suite",
                     "OCaml & 25.6→85.8 & 公開suite・企業現場40\\%超", 1)
    case("N-claim-shift-row", base_proj, sh, ["CLAIM_ANCHOR"])
    case("N-clock-swap",
         base_proj.replace("npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠",
                            "npm 2026-10-22T15:18:14Z、GH 15:21:49Zとは別典拠", 1),
         base_tex, ["ROW_ALTERED"])
    case("N-npm-url", base_proj,
         base_tex.replace(r"\url{https://registry.npmjs.org/@tanstack%2Fai}",
                            r"\url{https://registry.npmjs.org/ai}", 1),
         ["URL_NPM_SCOPE"])
    case("N-jp-url", base_proj,
         base_tex.replace(r"\url{https://developers.openai.com/api/docs/guides/decisions}",
                           r"\url{https://developers.openai.com/api/docs/guides/decisions（観測2026-10-25、snapshot}", 1),
         ["URL_JP_PUNCT"])
    case("N-qual-proj",
         base_proj.replace("持続性能の66倍ではない", "", 1),
         base_tex, ["QUAL_PROJ"])
    case("N-qual-tex", base_proj,
         base_tex.replace("持続性能の66倍ではない", "", 1), ["QUAL_TEX"])
    first_row = ("告知・API提供｜2026-10-23T17:15:24Z（X原文、post ID確認）"
                 "｜状態：IN（当週）｜根拠：X HTML原文＋supplement 041ec6系")
    case("N-row-delete", base_proj.replace(first_row, "", 1),
         base_tex, ["ROW_ALTERED"])
    case("N-row-dup80",
         base_proj.replace("重み配布｜2026-11-04予定｜状態：FUTURE（未公開）"
                            "｜根拠：発表のみ、バイト・SHA未取得",
                            first_row, 1),
         base_tex, ["ROW_ALTERED"])
    mp_sw = base_proj.replace(first_row, "§SWAP§")
    mp_sw = mp_sw.replace("重み配布｜2026-11-04予定｜状態：FUTURE（未公開）"
                          "｜根拠：発表のみ、バイト・SHA未取得", first_row, 1)
    mp_sw = mp_sw.replace("§SWAP§",
                          "重み配布｜2026-11-04予定｜状態：FUTURE（未公開）"
                          "｜根拠：発表のみ、バイト・SHA未取得", 1)
    case("N-row-swap", mp_sw, base_tex, ["ROW_ALTERED"])
    case("N-header-alter",
         base_proj.replace("【表：公開状態×時点（Kimi）】",
                            "【表：公開状態×時点（Kimi改）】", 1),
         base_tex, ["HEADER_ORDER"])
    case("N-note-alter",
         base_proj.replace("注意｜", "注意改｜", 1), base_tex, ["ROW_ALTERED"])
    case("N-model-change",
         base_proj.replace("COBOL ｜10.9→72.1 ｜19/20",
                            "FORTRAN ｜10.9→72.1 ｜19/20", 1),
         base_tex, ["CLAIM_ANCHOR"])
    case("N-metric-change",
         base_proj.replace("COBOL ｜10.9→72.1 ｜19/20",
                            "COBOL ｜11.9→72.1 ｜19/20", 1),
         base_tex, ["CLAIM_ANCHOR"])
    cd_old = "Luna(40.3%) $0.77 vs Sol $3.48"
    _once(base_proj, cd_old, "claim-drop")
    case("N-claim-drop",
         base_proj.replace(cd_old, "Luna(40.3%) $0.77 vs Sol", 1),
         base_tex, ["CLAIM_ANCHOR"])
    case("N-bib-url", base_proj,
         base_tex.replace("https://registry.npmjs.org/@tanstack%2Fai",
                           "https://registry.npmjs.org/ai", 1),
         ["URL_NPM_SCOPE"])

    # -- hash gate: one corruption per pinned input --
    for role in ["r35_reader", "r35_ledger", "r35_manifest",
                 "r3_projection", "r3_tex", "r3_pdf"]:
        case(f"N-HASH-{role}", base_proj, base_tex, ["HASH_MISMATCH"],
             overrides={role: f"corrupted::{role}".encode()})

    # -- r6 print-only text state (synthetic, then verified on real files) --
    assert base_tex.count(PRODUCTION_NOTE_TEX) == 1
    r6tex = base_tex.replace(PRODUCTION_NOTE_TEX + "\n", "")
    assert PRODUCTION_NOTE_TEX not in r6tex
    r6base = (base_proj, r6tex)
    case("R6-TEX-PRINT-ONLY-DELETE", base_proj, r6tex, [],
         role="r6", expect_pass=True, base_override=r6base)
    rein = r6tex.replace("\\label{sec:recap}",
                         "\\label{sec:recap}\n" + PRODUCTION_NOTE_TEX)
    case("N-PRINT-NOTE-LEAK", base_proj, rein,
         ["INTERNAL_PRINT_NOTE_LEAK"], role="r6", base_override=r6base)
    alt6 = r6tex.replace("17時15分24秒（協定世界時）",
                         "17時15分25秒（協定世界時）", 1)
    case("N-R6-TEX-ALTER", base_proj, alt6, ["PROSE_PROJ_TEX"], role="r6",
         blindness=OLD_SCOPE_OK, base_override=r6base)
    return cases


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def resolve_inputs(args):
    base = pathlib.Path(args.staged_dir) if args.staged_dir else None
    if base is None:
        if not args.repo_root:
            raise SystemExit(
                "missing inputs: provide --repo-root (or --staged-dir) "
                "and/or explicit --reader/--ledger/--manifest/"
                "--projection/--tex/--pdf paths")
        base = pathlib.Path(args.repo_root)
    paths = {}
    explicit = {"r35_reader": args.reader, "r35_ledger": args.ledger,
                "r35_manifest": args.manifest,
                "r3_projection": args.projection, "r3_tex": args.tex,
                "r3_pdf": args.pdf}
    for role, rel in REL.items():
        paths[role] = explicit[role] or str(base / rel)
    return paths


def build_ctx(paths):
    reader_text = pathlib.Path(paths["r35_reader"]).read_text(
        encoding="utf-8")
    manifest = json.loads(pathlib.Path(paths["r35_manifest"]).read_text(
        encoding="utf-8"))
    tables = manifest["tables_detail"]
    repo_root = pathlib.Path(paths["r35_reader"]).resolve()
    # walk up to the repository root that holds the strict checker
    for cand in [repo_root.parent, *repo_root.parents]:
        if (cand / STRICT_CHECKER_REL).exists():
            repo_root = cand
            break
    claims = load_expected_claims(repo_root)
    return {"paths": paths, "reader_text": reader_text, "tables": tables,
            "claims": claims}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=None)
    ap.add_argument("--staged-dir", default=None)
    ap.add_argument("--reader", default=None)
    ap.add_argument("--ledger", default=None)
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--projection", default=None)
    ap.add_argument("--tex", default=None)
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--test-tex", default=None,
                    help="tested TeX subject (defaults to --tex); in r6 mode "
                         "points at the new print file while H00 keeps "
                         "pinning the immutable r3 originals")
    ap.add_argument("--test-pdf", default=None,
                    help="tested PDF subject (defaults to --pdf)")
    ap.add_argument("--mode", default="clean",
                    choices=["clean", "negatives"])
    ap.add_argument("--tex-role", default="r3", choices=["r3", "r6"])
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    script_dir = pathlib.Path(__file__).resolve().parent
    out_dir = pathlib.Path(args.out) if args.out else script_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    paths = resolve_inputs(args)
    ctx = build_ctx(paths)
    base_proj = pathlib.Path(paths["r3_projection"]).read_text(
        encoding="utf-8")
    test_tex_path = pathlib.Path(args.test_tex) if args.test_tex else \
        pathlib.Path(paths["r3_tex"])
    test_pdf_path = pathlib.Path(args.test_pdf) if args.test_pdf else \
        pathlib.Path(paths["r3_pdf"])
    base_tex = test_tex_path.read_text(encoding="utf-8")

    if args.mode == "clean":
        res, ev = validate(ctx, base_proj, base_tex,
                           tex_role=args.tex_role)
        ok = all(r["result"] == "PASS" for r in res)
        doc = {"tool": "full-reader-visible-segment-join-r6",
               "mode": "clean", "tex_role": args.tex_role,
               "verdict": ("R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED"
                           if ok else
                           "MUSE_W43_R6_FULL_VISIBLE_FIDELITY_BLOCKED"),
               "checks": res, "evidence": ev}
        (out_dir / "full-segment-join-clean-r6.json").write_text(
            json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")
        print(json.dumps(doc, indent=2, ensure_ascii=False))
        # identity + mutant-binding record
        ident = {"tool": "six-input-identity-and-mutant-binding-r6",
                 "inputs": {}}
        for role, p in paths.items():
            b = pathlib.Path(p).read_bytes()
            ident["inputs"][role] = {
                "path": p, "bytes": len(b),
                "sha256": hashlib.sha256(b).hexdigest(),
                "expected": EXPECTED_HASH[role],
                "match": hashlib.sha256(b).hexdigest()
                == EXPECTED_HASH[role]}
        ident["tested"] = ev["tested_hashes"]
        ident["verdict"] = ("IDENTITY_PASS"
                            if all(v["match"]
                                   for v in ident["inputs"].values())
                            else "IDENTITY_FAIL")
        (out_dir / "six-input-identity-and-mutant-binding-r6.json").write_text(
            json.dumps(ident, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")
        return 0 if ok else 1

    cases = build_negatives(ctx, base_proj, base_tex)
    out_cases = []
    for c in cases:
        try:
            res, ev = validate(ctx, c["proj"], c["tex"],
                               file_bytes_overrides=c["overrides"],
                               tex_role=c["role"])
        except AssertionError as e:
            out_cases.append({"id": c["id"], "result": "FAIL",
                              "cause": "NEG_HARNESS_ERROR",
                              "detail": str(e)[:300],
                              "expected": c["expect"]})
            continue
        fails = {r["cause"] for r in res if r["result"] == "FAIL"}
        passes = {r["id"] for r in res if r["result"] == "PASS"}
        tested = ev["tested_hashes"]
        # The mutant is hash-bound iff the actually-validated strings differ
        # from the case's base inputs (or the hash gate was overridden).
        text_changed = (tested["tested_proj_sha256"] != c["base_psha"]
                        or tested["tested_tex_sha256"] != c["base_tsha"])
        if c["expect_pass"]:
            good = all(r["result"] == "PASS" for r in res)
            out_cases.append({
                "id": c["id"], "result": "PASS" if good else "FAIL",
                "cause": "—" if good else "UNEXPECTED_FAIL",
                "detail": ("r6 print-only text state passes clean"
                           if good else sorted(fails)[:4]),
                "expected": "ALL_PASS",
                "mutant_bound": tested})
        else:
            want = set(c["expect"])
            blind_ok = all(b in passes for b in c["blindness"])
            hash_case = any(h in c["id"] for h in ("N-HASH-",))
            bound_ok = text_changed or hash_case or c["overrides"]
            good = want <= fails and blind_ok and bound_ok
            out_cases.append({
                "id": c["id"], "result": "PASS" if good else "FAIL",
                "cause": "—" if good else "NEG_NOT_DETECTED",
                "detail": (f"expect={sorted(want)} got={sorted(fails)[:6]} "
                           f"blind_old_scope_pass={blind_ok} "
                           f"mutant_hash_bound={bound_ok}"),
                "expected": sorted(want), "mutant_bound": tested})
    ok = all(x["result"] == "PASS" for x in out_cases)
    doc = {"tool": "full-reader-visible-segment-join-r6",
           "mode": "negatives",
           "verdict": "NEGATIVES_PASS" if ok else "NEGATIVES_FAIL",
           "cases": out_cases}
    (out_dir / "full-segment-join-negatives-r6.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print(json.dumps(doc, indent=2, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())


