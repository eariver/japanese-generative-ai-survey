#!/usr/bin/env python3
"""W43 r3.5 STRICT SEMANTIC claim-join checker (Core-free, read-only).

Validates genuine semantic binding (not token-overlap vacuous PASS):
  20 reader fenced 表 tables (exact headers, order) <-> 80 physical ｜-rows (SHA, line, ordinal, row_id, row_type)
  <-> 80 ledger table_rows (1:1, DATA/NOTE match, 13 sanctioned aliases pinned)
  29 claims -> own-block DATA rows with physical-value proof (lexical map documented),
  variant/measure/unit/comparator/URL/source-tier honesty, no URL-only proof.
Runs in-memory negative mutations incl. ACTUAL physical reader mutations; each MUST fail
for its SPECIFIC semantic reason (not incidental guard). Writes JSON (--out).
Exit 0 only on EDITION_LOCAL_ROW_JOIN_PASS.

Scope: edition-local join proof only. Never source originality, native Stage,
guaranteed external provenance, or independent Sol sign-off.
"""
import json, re, sys, hashlib, argparse, copy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # sources/2026-W43
EB = ROOT / "execution" / "editorial-bypass"
REPOROOT = Path(__file__).resolve().parents[4]      # repo root for archive existence
TABLE_ORDER = ["p1-t1","p1-t2","p1-t3","p1-t4","p2-t1","p2-t2","p2-f2","p3-t1","p3-t2",
               "p4-t1","p5-t1","p5-t2","p5-f1","p7-t1","p7-f1","p7-t2","p8-t1","p8-f2","p8-t2","p8-f3"]

EXPECTED_HEADERS = [
 "【表：公開状態×時点（Kimi）】",
 "【表：total／effective／active と文脈（計数規約を見出しに明記）】",
 "【表：bench×harness×分母（帰属明示）】",
 "【表：可用性×時刻×約款（発表／プレビュー／GA／重み配布／再現を別列）】",
 "【表：核×役割（DeepInfer）】",
 "【表：bench×分母×条件（MemT）】",
 "【表：MemT権利対応（p2-f2、§2.5実物）】",
 "【表：権限×条件（Duet）】",
 "【表：旧／新／未来の三段（auto-mode）】",
 "【表：倍率×削減率×出典／版／時刻】",
 "【表：機能×モデル×対応言語×出典／版／時刻】",
 "【表：AA×原表有無（Ming）】",
 "【表：様式×評価・料金の実数行列（p5-f1、§5.1–5.2実物。数値は全て発行元公表・独立再現なし。比較対象・単位は行内でqualified）】",
 "【表：手順×来歴×限界（Bio）】",
 "【表：言語別デルタと労力・費用の注記（p7-f1、§7.2実物。数値は全て発行元測定）】",
 "【表：bench×分母×条件（Low-resource）】",
 "【表：料金×条件×版（Decisions）】",
 "【表：安定核 vs 実験harness（p8-f2、§8.2実物）】",
 "【表：API×移行×約款（発表／配布／無料期限を別status）】",
 "【表：重み vs API vs 追加物（p8-f3、§8.3実物）】",
]

# 13 sanctioned aliases: row_id -> (ledger_label, expected physical first segment)
EXPECTED_ALIASES = {
 "p1-t2-01": ("Kimi行", "Kimi K3.1 Pro"),
 "p1-t2-02": ("Flint行", "Flint"),
 "p1-t2-03": ("Nemotron行", "Nemotron Bolt E4B"),
 "p1-t4-01": ("Kimi行", "Kimi API"),
 "p1-t4-02": ("Flint行", "Flint重み"),
 "p1-t4-03": ("Nemotron行", "Nemotron重み"),
 "p2-t2-01": ("11bench（評価対象parametric-memory方式内）", "11 bench"),
 "p2-t2-02": ("1.86x（SOURCE_UNVERIFIED）", "1.86x"),
 "p2-t2-03": ("66x（保存容量約66倍削減）", "66x"),
 "p2-f2-02": ("原ソフトウェア", "原ソフトウェア（SGLang統合含む）"),
 "p2-f2-03": ("第三者", "第三者 flash-linear-attention"),
 "p4-t1-05": ("22x", "22x見出し"),
 "p5-t1-03": ("TTS", "TTS Speech 3"),
}

# Lexical representation map (narrow, documented):
# - "40%超" ≡ "40%+" (Japanese 超 = over/+) ; core "40%" must appear
# - "500ms未満" ≡ "sub-500ms" (未満 = sub-/under) ; core "500ms" must appear
# - "対象外" ≡ "excluded" (Japanese) ; core "対象外" must appear for that claim
# - seconds display "2026-10-22T15:21:49Z" normalizes millis ".491Z" documented in ledger clock
LEXICAL_MAP_NOTE = "40%超≡40%+ (core 40%); 500ms未満≡sub-500ms (core 500ms); 対象外≡excluded; npm seconds display normalizes .491Z millis (ledger clock retains millis)"

# Pinned independent expected claim baseline (29). Hardcoded, NOT generated from mutable ledger.
# Each: block, row, value_exact, metric_exact, variant_token (must appear in physical, case-insensitive, or special), phys_required (substrings that MUST appear in physical_text), phys_qual (extra qualifier required), unit_rule, denom_rule, url_rule, archive_rule
# variant_token "__SKIP_PHYS_VARIANT__" means variant English not expected in Japanese physical; baseline ledger-variant match still enforced.
EXPECTED_CLAIMS = [
 {"k":"p2-f2-01/CC","block":"p2-f2","row":"p2-f2-01","value":"CC BY-NC-SA 4.0","metric":"license","variant":"paper-related materials","variant_phys":["論文・原資料"],"phys":["CC BY-NC-SA 4.0"],"unit_contains":"not applicable","url_contains":"github.com/MemTensor/MemT-1.0","archive":"sources","raw_must_contain":"Attribution-NonCommercial-ShareAlike"},
 {"k":"p2-f2-02/PolyForm","block":"p2-f2","row":"p2-f2-02","value":"PolyForm Noncommercial 1.0.0","metric":"license","variant":"repo original software","variant_phys":["原ソフトウェア"],"phys":["PolyForm","1.0.0"],"unit_contains":"not applicable","url_contains":"github.com/MemTensor/MemT-1.0","archive":"sources","raw_must_contain":"PolyForm"},
 {"k":"p2-f2-03/MIT-flash","block":"p2-f2","row":"p2-f2-03","value":"MIT","metric":"license","variant":"third-party flash-linear-attention","variant_phys":["第三者","flash-linear-attention"],"phys":["MIT","flash-linear-attention"],"unit_contains":"not applicable","url_contains":"github.com/MemTensor/MemT-1.0","archive":"sources","raw_must_contain":"flash-linear-attention"},
 {"k":"p2-f2-04/excluded","block":"p2-f2","row":"p2-f2-04","value":"excluded","metric":"license-scope","variant":"weights/datasets/trademarks","variant_phys":["重み・データセット・商標"],"phys":["対象外"],"unit_contains":"not applicable","url_contains":"github.com/MemTensor/MemT-1.0","archive":"sources","raw_must_contain":"not covered"},
 {"k":"p5-f1-01/WER","block":"p5-f1","row":"p5-f1-01","value":"4.1/4.0","metric":"WER","variant":"Small Transcribe 3","variant_phys":["Small Transcribe 3"],"phys":["4.1/4.0"],"unit_contains":"not applicable","denom_contains":"COMPARATOR_UNVERIFIED","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-01/cpWER","block":"p5-f1","row":"p5-f1-01","value":"18.4/18.6","metric":"cpWER","variant":"Small diarization","variant_phys":["diarization","cpWER"],"phys":["18.4/18.6","Pyannote","19.0"],"unit_contains":"not applicable","denom_contains":"Pyannote","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-01/recall","block":"p5-f1","row":"p5-f1-01","value":"94.6/81.4","metric":"keyphrase recall","variant":"Small","variant_phys":["recall"],"phys":["94.6/81.4"],"unit_contains":"percent","denom_contains":"COMPARATOR_UNVERIFIED","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-02/latency","block":"p5-f1","row":"p5-f1-02","value":"sub-500ms","metric":"latency","variant":"Realtime","variant_phys":["Realtime"],"phys":["500ms","未満"],"unit_contains":"milliseconds","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-01/price-mini","block":"p5-f1","row":"p5-f1-01","value":"$0.0035/min","metric":"price","variant":"Mini","variant_phys":["Mini"],"phys":["$0.0035"],"unit_contains":"confirmed","unit_variant_must":"Mini","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-01/price-small","block":"p5-f1","row":"p5-f1-01","value":"$0.004","metric":"price","variant":"Small","variant_phys":["Small"],"phys":["$0.004"],"unit_contains":"UNIT_UNVERIFIED","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-02/price-rt","block":"p5-f1","row":"p5-f1-02","value":"$0.008","metric":"price","variant":"Realtime","variant_phys":["Realtime"],"phys":["$0.008"],"unit_contains":"UNIT_UNVERIFIED","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-03/price-tts","block":"p5-f1","row":"p5-f1-03","value":"$13/M chars","metric":"price","variant":"Speech TTS","variant_phys":["TTS"],"phys":["$13"],"unit_contains":"confirmed","unit_variant_must":"Speech","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p5-f1-04/price-agent","block":"p5-f1","row":"p5-f1-04","value":"$0.04/$0.08","metric":"price","variant":"agent API","variant_phys":["agent"],"phys":["$0.04","$0.08"],"unit_contains":"UNIT_UNVERIFIED","url_contains":"mistral.ai","archive":"QUALIFIED"},
 {"k":"p7-f1-01/acc-cobol","block":"p7-f1","row":"p7-f1-01","value":"10.9→72.1","metric":"accuracy","variant":"COBOL","variant_phys":["COBOL"],"phys":["10.9","72.1","→"],"unit_contains":"percent","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED"},
 {"k":"p7-f1-02/acc-ocaml","block":"p7-f1","row":"p7-f1-02","value":"25.6→85.8","metric":"accuracy","variant":"OCaml","variant_phys":["OCaml"],"phys":["25.6","85.8"],"unit_contains":"percent","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED"},
 {"k":"p7-f1-03/acc-fortran","block":"p7-f1","row":"p7-f1-03","value":"21.4→83.5","metric":"accuracy","variant":"Fortran","variant_phys":["Fortran"],"phys":["21.4","83.5"],"unit_contains":"percent","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED"},
 {"k":"p7-f1-04/acc-vb","block":"p7-f1","row":"p7-f1-04","value":"27.5→89.4","metric":"accuracy","variant":"VB","variant_phys":["VB"],"phys":["27.5","89.4"],"unit_contains":"percent","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED"},
 {"k":"p7-f1-05/acc-low","block":"p7-f1","row":"p7-f1-05","value":"86.6%","metric":"accuracy","variant":"GPT-6.1 Sol","variant_phys":["GPT-6.1","Sol"],"phys":["86.6%"],"unit_contains":"percent","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED"},
 {"k":"p7-f1-05/acc-high","block":"p7-f1","row":"p7-f1-05","value":"97.9%","metric":"accuracy","variant":"GPT-6.1 Sol","variant_phys":["GPT-6.1","Sol"],"phys":["97.9%"],"unit_contains":"percent","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED"},
 {"k":"p7-f1-06/cost","block":"p7-f1","row":"p7-f1-06","value":"$0.77 vs $3.48","metric":"cost","variant":"Luna vs Sol","variant_phys":["Luna","Sol"],"phys":["$0.77","$3.48"],"unit_contains":"USD","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED"},
 {"k":"p7-f1-01/enterprise-40p","block":"p7-f1","row":"p7-f1-01","value":"40%+","metric":"enterprise share","variant":"COBOL (field)","variant_phys":["COBOL"],"phys":["40%"],"phys_qual_any":["企業現場","オンラインバンキング"],"phys_qual_must":["精度とは別"],"unit_contains":"percent of online banking","denom_contains":"enterprise feedback","url_contains":"openai.com/index/low-resource","archive":"QUALIFIED","prevalence_note":"must NOT be treated as benchmark accuracy"},
 {"k":"p8-f2-01/gh-clock","block":"p8-f2","row":"p8-f2-01","value":"2026-10-22T15:18:14Z","metric":"release clock","variant":"TanStack AI 1.0.0 GH","variant_phys":["GH","15:18:14"],"phys":["15:18:14"],"unit_contains":"UTC","url_contains":"api.github.com/repos/TanStack/ai","archive":"sources","raw_must_contain":"15:18:14Z"},
 {"k":"p8-f2-03/npm-clock","block":"p8-f2","row":"p8-f2-03","value":"2026-10-22T15:21:49Z","metric":"registry clock","variant":"TanStack AI 1.0.0 npm","variant_phys":["npm","15:21:49"],"phys":["15:21:49","2026-10-22","npm"],"phys_qual_any":["GH","別典拠","別"],"unit_contains":"UTC","url_contains":"registry.npmjs.org/@tanstack","url_must_contain":"@tanstack","archive":"RAW_NOT_ARCHIVED","role_separation":"GH 15:18:14Z vs npm 15:21:49.491Z separate origins"},
 {"k":"p8-f2-01/scale","block":"p8-f2","row":"p8-f2-01","value":"76/23/8/143","metric":"package scale","variant":"TanStack AI 1.0 stable","variant_phys":["TanStack"],"phys":["76","143","pkgs"],"unit_contains":"counts","url_contains":"api.github.com/repos/TanStack/ai","archive":"QUALIFIED"},
 {"k":"p8-f2-03/metrics-out","block":"p8-f2","row":"p8-f2-03","value":"23:42:03Z OUT","metric":"cutoff clock","variant":"GitHub Metrics","variant_phys":["Metrics"],"phys":["23:42:03","OUT","Metrics"],"unit_contains":"UTC","url_contains":"registry.npmjs.org","archive":"QUALIFIED"},
 {"k":"p8-f3-01/mit","block":"p8-f3","row":"p8-f3-01","value":"MIT","metric":"license","variant":"V4.1-Flash","variant_phys":["V4.1-Flash"],"phys":["MIT","V4.1-Flash"],"unit_contains":"not applicable","url_contains":"api-docs.deepseek.com","archive":"QUALIFIED","caveat":"LICENSE bytes/SHA unseen; vendor-asserted"},
 {"k":"p8-f3-02/price","block":"p8-f3","row":"p8-f3-02","value":"$0.75/1k","metric":"price","variant":"Search/Fetch API","variant_phys":["Search","Fetch"],"phys":["$0.75"],"unit_contains":"USD/1k calls","url_contains":"api-docs.deepseek.com","archive":"QUALIFIED"},
 {"k":"p8-f3-02/free","block":"p8-f3","row":"p8-f3-02","value":"free till Oct31 16:00 UTC","metric":"free period","variant":"Search/Fetch","variant_phys":["Search","Fetch"],"phys":["10/31","16:00"],"unit_contains":"UTC deadline","url_contains":"api-docs.deepseek.com","archive":"QUALIFIED"},
 {"k":"p8-f3-03/bench","block":"p8-f3","row":"p8-f3-03","value":"77 vs 74.2","metric":"benchmark","variant":"DeepSWE","variant_phys":["DeepSWE"],"phys":["74.2","DeepSWE"],"unit_contains":"score","url_contains":"api-docs.deepseek.com","archive":"QUALIFIED"},
]

def parse_tables(reader_text):
    lines = reader_text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i+1:j]
            if body and body[0].startswith("【表"):
                phys = [(i+2+k, ln) for k, ln in enumerate(body) if "｜" in ln]
                out.append({"start": i+1, "end": j+1, "header": body[0], "rows": phys})
            i = j + 1
        else:
            i += 1
    return out

def validate(reader_text, manifest, ledger):
    fails = []
    tables = parse_tables(reader_text)
    byid = {r["block_id"]: r for r in ledger["rows"]}
    man_tabs = {t["table_id"]: t for t in manifest["tables_detail"]}

    # T0: ledger block count pinned
    if len(ledger["rows"]) != 96:
        fails.append(f"T0: ledger blocks {len(ledger['rows'])} != 96")

    # T1: exact 20 headers in order
    if len(tables) != 20:
        fails.append(f"T1-COUNT: reader 表 blocks {len(tables)} != 20")
        return fails
    for idx, (tab, exp_id, exp_hdr) in enumerate(zip(tables, TABLE_ORDER, EXPECTED_HEADERS)):
        if tab["header"] != exp_hdr:
            fails.append(f"T1-HEADER-MISMATCH: {exp_id} header mismatch: got {tab['header']!r} != expected {exp_hdr!r}")
        # header-to-manifest identity
        mt = man_tabs.get(exp_id)
        if mt is None:
            fails.append(f"T1-MANIFEST-MISSING: {exp_id} missing from manifest")
        elif mt.get("header") != exp_hdr or mt.get("header") != tab["header"]:
            fails.append(f"T1-HEADER-MANIFEST-MISMATCH: {exp_id} manifest header != reader header")
    if [t for t in TABLE_ORDER] != TABLE_ORDER or len(tables) != 20:
        fails.append("T1-ORDER: table order mismatch")
        return fails
    # also verify parsed order matches TABLE_ORDER via manifest table_id sequence? manifest order should match
    if [t["table_id"] for t in manifest["tables_detail"]] != TABLE_ORDER:
        fails.append(f"T1-MANIFEST-ORDER: manifest table order != expected")
    if fails:
        return fails

    # T2: bijection
    man_row = {}
    seen = set()
    for t in manifest["tables_detail"]:
        for r in t["rows"]:
            if r["row_id"] in seen:
                fails.append(f"T2-DUP: duplicate row_id {r['row_id']}")
            seen.add(r["row_id"])
            man_row[r["row_id"]] = (t["table_id"], r)
    if len(man_row) != 80:
        fails.append(f"T2-COUNT: manifest rows {len(man_row)} != 80")
    # DATA/NOTE counts
    data_n = sum(1 for _, r in man_row.values() if r.get("row_type")=="DATA")
    note_n = sum(1 for _, r in man_row.values() if r.get("row_type")=="NOTE")
    if data_n != 78 or note_n != 2:
        fails.append(f"T2-ROWTYPE-COUNT: DATA {data_n} (exp 78) NOTE {note_n} (exp 2)")
    # exact NOTE ids
    note_ids = sorted([rid for rid,(tid,r) in man_row.items() if r.get("row_type")=="NOTE"])
    if note_ids != ["p1-t2-04","p4-t1-05"]:
        fails.append(f"T2-NOTE-IDS: NOTE rows {note_ids} != ['p1-t2-04','p4-t1-05']")

    for tid, tab in zip(TABLE_ORDER, tables):
        mt = man_tabs.get(tid)
        if mt is None:
            continue
        if [s for s,_ in tab["rows"]] != [r["reader_line"] for r in mt["rows"]]:
            fails.append(f"T2-LINE: {tid} reader lines != manifest lines")
        if len(tab["rows"]) != len(mt["rows"]):
            fails.append(f"T2-COUNT: {tid} reader {len(tab['rows'])} != manifest {len(mt['rows'])}")
            continue
        for n, ((ln, tx), mr) in enumerate(zip(tab["rows"], mt["rows"]), 1):
            if mr["ordinal"] != n or mr["row_id"] != f"{tid}-{n:02d}":
                fails.append(f"T2-ORDINAL: {tid} ordinal/row_id break at {n} got {mr.get('row_id')}")
            h = hashlib.sha256(tx.encode("utf-8")).hexdigest()
            if h != mr["sha256"] or tx != mr["physical_text"]:
                fails.append(f"T2-HASH: {tid}-{n:02d} text/hash mismatch (swap/mutation/extra)")
        lrows = byid[tid].get("table_rows", [])
        if len(lrows) != len(mt["rows"]):
            fails.append(f"T2-LEDGER-COUNT: {tid} ledger {len(lrows)} != manifest {len(mt['rows'])}")
            continue
        for mr, lr in zip(mt["rows"], lrows):
            if lr.get("row_id") != mr["row_id"]:
                fails.append(f"T2-LEDGER-ROWID: {tid} ledger {lr.get('row_id')} != {mr['row_id']}")
            if lr.get("row_type") != mr.get("row_type"):
                fails.append(f"T2-ROWTYPE-MISMATCH: {mr['row_id']} manifest {mr.get('row_type')} != ledger {lr.get('row_type')}")
            first = mr["physical_text"].split("｜")[0]
            lm = mr.get("label_match")
            exp_alias = EXPECTED_ALIASES.get(mr["row_id"])
            if lm == "SANCTIONED_ALIAS":
                if exp_alias is None:
                    fails.append(f"T2-ALIAS-UNSANCTIONED: {mr['row_id']} self-declared alias not in pinned 13")
                else:
                    exp_label, exp_first = exp_alias
                    if lr.get("row") != exp_label:
                        fails.append(f"T2-ALIAS-LABEL: {mr['row_id']} ledger label {lr.get('row')} != pinned {exp_label}")
                    if first != exp_first and first.rstrip() != exp_first:
                        # allow trailing-space typography? first segment exact (r3.4 uses exact first segment without trailing space for aliases? check)
                        # For aliases, physical first segment must equal expected (modulo rstrip for padded?)
                        if first.strip() != exp_first.strip():
                            fails.append(f"T2-ALIAS-PHYS: {mr['row_id']} physical first {first!r} != pinned {exp_first!r}")
                    if lr.get("row") != mr.get("ledger_label"):
                        fails.append(f"T2-ALIAS-DRIFT: {mr['row_id']} alias label drift")
            elif lm == "EXACT":
                if lr.get("row") != first:
                    fails.append(f"T2-LABEL-EXACT: {tid} {mr['row_id']} label not exact: ledger {lr.get('row')!r} vs phys-first {first!r}")
            elif lm == "EXACT_AFTER_RSTRIP":
                if lr.get("row") != first.rstrip():
                    fails.append(f"T2-LABEL-RSTRIP: {tid} {mr['row_id']} label not exact-after-rstrip")
            else:
                fails.append(f"T2-LABEL-CLASS: {tid} {mr['row_id']} ungoverned label class {lm!r}")
    if fails:
        return fails

    # C0: exactly 29 claims, stable set
    all_claims = []
    for r in ledger["rows"]:
        for c in (r.get("claims") or []):
            all_claims.append((r["block_id"], c))
    if len(all_claims) != 29:
        fails.append(f"C0-COUNT: claims {len(all_claims)} != 29")
        # continue to itemize but count fails
    # Build lookup by (block,row,value) — metric checked separately so metric drift reports C-METRIC not just missing
    led_lookup = {}
    for blk, c in all_claims:
        led_lookup[(blk, c.get("row_id"), c.get("value"))] = (blk, c)

    # Direct ledger-claim audit (independent of expected baseline): every ledger claim must
    # itself be own-block DATA (catches mutated row_id even when baseline key drifts)
    for blk, c in all_claims:
        rid = c.get("row_id")
        where2 = f"{blk}/{c.get('value')}"
        if not rid or rid not in man_row:
            fails.append(f"C-UNKNOWN-ROW: {where2} unknown row_id {rid}")
            continue
        tid2, mr2 = man_row[rid]
        if tid2 != blk:
            fails.append(f"C-CROSS-BLOCK: {where2} cross-block {blk}->{tid2}")
            continue
        if mr2.get("row_type") == "NOTE":
            fails.append(f"C-NOTE-TARGET: {where2} points to NOTE row {rid}")
            continue

    # Validate each expected claim exists with exact baseline fields + physical proof
    for exp in EXPECTED_CLAIMS:
        key = (exp["block"], exp["row"], exp["value"])
        hit = led_lookup.get(key)
        where = f"{exp['k']}"
        if hit is None:
            fails.append(f"C-BASELINE-MISSING: {where} expected claim not found in ledger (block/row/value drift)")
            continue
        blk, c = hit
        # own-block
        if exp["block"] != exp["row"].split("-")[0].rsplit("-",1)[0] and False:
            pass
        # row must belong to expected block: row_id prefix must equal block_id
        row_prefix = exp["row"].rsplit("-",1)[0]  # e.g., p7-f1-01 -> p7-f1
        if row_prefix != exp["block"]:
            fails.append(f"C-CROSS-BLOCK-DEF: {where} row {exp['row']} not in block {exp['block']}")
        # NOTE exclusion
        tid_row, mr = man_row.get(exp["row"], (None, None))
        if mr is None:
            fails.append(f"C-UNKNOWN-ROW: {where} row {exp['row']} not in manifest")
            continue
        if tid_row != exp["block"]:
            fails.append(f"C-CROSS-BLOCK: {where} cross-block {exp['block']}->{tid_row}")
            continue
        if mr.get("row_type") == "NOTE":
            fails.append(f"C-NOTE-TARGET: {where} points to NOTE row {exp['row']}")
            continue
        # variant baseline: ledger model_variant must contain expected variant token (case-insensitive) or exact?
        # For pinned baseline, require expected variant substring present in ledger variant
        if exp["variant"].lower() not in (c.get("model_variant") or "").lower():
            # allow partial? e.g., expected "paper-related materials" vs ledger "paper-related materials" exact -> ok
            # For robustness, check all expected variant words? Use first word?
            fails.append(f"C-VARIANT-BASELINE: {where} ledger variant {(c.get('model_variant'))!r} != expected {exp['variant']!r}")
        # metric baseline exact
        if c.get("metric") != exp["metric"]:
            fails.append(f"C-METRIC-BASELINE: {where} ledger metric {c.get('metric')!r} != {exp['metric']!r}")
        # value baseline exact (already matched by key, but double-check)
        if c.get("value") != exp["value"]:
            fails.append(f"C-VALUE-BASELINE: {where} ledger value drift")
        # required fields nonempty
        for f in ("model_variant","metric","unit","denominator_comparison","evidence_task_id","archive_path"):
            if not c.get(f):
                fails.append(f"C-EMPTY: {where} empty field {f}")
        # unit rule
        unit = c.get("unit","")
        if "unit_contains" in exp and exp["unit_contains"] not in unit:
            fails.append(f"C-UNIT: {where} unit {unit!r} missing {exp['unit_contains']!r}")
        if exp.get("unit_variant_must") and exp["unit_variant_must"] not in (c.get("model_variant") or ""):
            fails.append(f"C-UNIT-VARIANT: {where} confirmed unit requires variant {exp['unit_variant_must']!r}")
        # false price confirmation guard: only Mini/Speech may be confirmed
        if c.get("metric")=="price" and "confirmed" in unit.lower():
            if not re.search(r"Mini|Speech", c.get("model_variant") or ""):
                fails.append(f"C-UNIT-FALSE-CONFIRM: {where} asserts confirmed unit without Mini/Speech basis")
        # comparator rule
        denom = c.get("denominator_comparison","")
        if exp.get("denom_contains") and exp["denom_contains"] not in denom:
            fails.append(f"C-COMPARATOR: {where} denominator missing {exp['denom_contains']!r}")
        if c.get("metric") in ("WER",) or "recall" in c.get("metric",""):
            if "COMPARATOR_UNVERIFIED" not in denom and "Pyannote" not in denom:
                fails.append(f"C-COMPARATOR-UNQUALIFIED: {where} comparator unqualified")
        # URL rule: ledger table row URL must contain expected
        lrow = next(tr for tr in byid[exp["block"]]["table_rows"] if tr["row_id"]==exp["row"])
        if exp.get("url_contains") and exp["url_contains"] not in lrow.get("url",""):
            fails.append(f"C-URL: {where} row URL {lrow.get('url')!r} missing {exp['url_contains']!r}")
        if exp.get("url_must_contain") and exp["url_must_contain"] not in lrow.get("url","").lower():
            fails.append(f"C-URL-SCOPE: {where} unscoped URL {lrow.get('url')!r} missing {exp['url_must_contain']!r}")
        # generic unscoped npm guard
        if "registry.npmjs.org" in lrow.get("url","") and "@tanstack" not in lrow.get("url","").lower():
            fails.append(f"C-URL-UNSCOPED: {exp['row']} unscoped npm URL {lrow.get('url')!r}")
        # source class: must be FIRST_PARTY/VENDOR_BENCH/DERIVED_ONLY as appropriate? enforce pinned per row?
        # For p7-f1 rows expect VENDOR_BENCH; p8-f2 rows FIRST_PARTY
        # (checked via ledger table_rows source_class vs manifest? manifest has no source_class; check ledger)
        # archive honesty
        ap = c.get("archive_path","")
        if exp.get("archive")=="sources":
            if not ap.startswith("sources/"):
                fails.append(f"C-PROVENANCE: {where} expected repo-archived source, got {ap!r}")
            else:
                p = REPOROOT / ap.split(":")[0]
                if not p.exists():
                    fails.append(f"C-PROVENANCE-MISSING: {where} archived bytes missing {ap}")
                else:
                    # validate actual relevant text, not mere existence
                    need = exp.get("raw_must_contain")
                    if need:
                        try:
                            raw = p.read_text(encoding="utf-8", errors="ignore")
                        except Exception:
                            raw = ""
                        if need not in raw:
                            # for JSON raw, check without strict? e.g., TanStack JSON contains 15:18:14Z
                            fails.append(f"C-PROVENANCE-CONTENT: {where} archived file missing relevant text {need!r}")
        elif exp.get("archive")=="QUALIFIED":
            if "ARCHIVE_UNAVAILABLE" not in ap and "RAW_NOT_ARCHIVED" not in ap:
                fails.append(f"C-PROVENANCE-QUALIFIED: {where} expected QUALIFIED marker, got {ap!r}")
            if ap.startswith("sources/"):
                # must not falsely claim file exists as raw proof? if starts with sources, must exist
                p = REPOROOT / ap.split(":")[0]
                if not p.exists():
                    fails.append(f"C-PROVENANCE-MISSING: {where} claimed repo path missing {ap}")
        elif exp.get("archive")=="RAW_NOT_ARCHIVED":
            if "RAW_NOT_ARCHIVED" not in ap:
                fails.append(f"C-PROVENANCE-RAW: {where} expected RAW_NOT_ARCHIVED, got {ap!r}")
            if "@tanstack" not in lrow.get("url","").lower():
                fails.append(f"C-URL-SCOPE: {where} npm claim without scoped URL")
        # PHYSICAL semantic proof: value + variant must appear in physical_text itself (not just URL/clock/note)
        phys = mr["physical_text"]
        for need in exp.get("phys", []):
            if need not in phys:
                fails.append(f"C-VALUE-MISSING-IN-PHYSICAL: {where} physical row {exp['row']} missing value substring {need!r}")
        for vt in exp.get("variant_phys", []):
            if vt.lower() not in phys.lower():
                fails.append(f"C-VARIANT-MISSING-IN-PHYSICAL: {where} physical row {exp['row']} missing variant token {vt!r} (wrong variant or misbound row)")
        for q in exp.get("phys_qual_must", []):
            if q not in phys:
                fails.append(f"C-QUALIFIER-MISSING: {where} physical missing qualifier {q!r} (prevalence/role separation)")
        if exp.get("phys_qual_any"):
            if not any(q in phys for q in exp["phys_qual_any"]):
                fails.append(f"C-QUALIFIER-MISSING: {where} physical missing any of {exp['phys_qual_any']!r}")
        # special: 40%+ must not be validated as accuracy; ensure enterprise context present (already via qual), and ensure not confused with 40.3%
        if exp["k"]=="p7-f1-01/enterprise-40p":
            if "40.3%" in phys and "40%超" not in phys and "40%+" not in phys:
                fails.append(f"C-PREVALENCE-CONFUSED: {where} only 40.3% cost present, enterprise 40%+ missing")
            if "精度とは別" not in phys and "prevalence" not in phys.lower():
                fails.append(f"C-PREVALENCE-UNQUALIFIED: {where} enterprise share not qualified separate from accuracy")
        if exp["k"]=="p8-f2-03/npm-clock":
            # require date + time + role separation in physical itself
            if "2026-10-22" not in phys:
                fails.append(f"C-DATE-MISSING: {where} physical missing date 2026-10-22 (display-normalization requires date)")
            if "GH" not in phys or "別" not in phys:
                fails.append(f"C-ROLE-SEPARATION-MISSING: {where} physical missing GH vs npm role separation")

    # extra claims beyond expected?
    exp_keys = set((e["block"], e["row"], e["value"]) for e in EXPECTED_CLAIMS)
    for blk, c in all_claims:
        if (blk, c.get("row_id"), c.get("value")) not in exp_keys:
            fails.append(f"C-EXTRA: {blk}/{c.get('value')} unexpected claim (count must stay 29 with stable IDs)")

    # T5 pinned anchors (evidence-grounded, independent of ledger generation)
    mtxt = {r["row_id"]: r["physical_text"] for t in manifest["tables_detail"] for r in t["rows"]}
    if "保存容量約66倍削減" not in mtxt.get("p2-t2-03",""):
        fails.append("T5: MemT storage meaning missing in p2-t2-03")
    if "SOURCE_UNVERIFIED" not in mtxt.get("p2-t2-02",""):
        fails.append("T5: 1.86x qualifier missing in p2-t2-02")
    if "parametric-memory" not in mtxt.get("p2-t2-01",""):
        fails.append("T5: parametric scope missing in p2-t2-01")
    if not any(r["ledger_label"] == "分類器" for r in man_tabs["p3-t2"]["rows"]):
        fails.append("T5: p3-t2 classifier missing")
    if not mtxt.get("p5-t1-03","").startswith("TTS Speech 3"):
        fails.append("T5: p5-t1 TTS Speech 3 missing")
    if not mtxt.get("p5-t2-01","").startswith("Controlled Voice"):
        fails.append("T5: p5-t2 Controlled Voice missing")
    if "40%" not in mtxt.get("p7-f1-01","") or ("企業現場" not in mtxt.get("p7-f1-01","") and "オンラインバンキング" not in mtxt.get("p7-f1-01","")):
        fails.append("T5: COBOL enterprise 40%+ prevalence missing/unqualified in p7-f1-01")
    if "10.9" not in mtxt.get("p7-f1-01","") or "72.1" not in mtxt.get("p7-f1-01",""):
        fails.append("T5: COBOL accuracy 10.9→72.1 missing in p7-f1-01")
    if "15:21:49" not in mtxt.get("p8-f2-03","") or "2026-10-22" not in mtxt.get("p8-f2-03",""):
        fails.append("T5: npm registry clock full timestamp missing in p8-f2-03")
    if "15:18:14" not in mtxt.get("p8-f2-01",""):
        fails.append("T5: GH release clock missing in p8-f2-01")
    return fails

CHECKS = []
def check(cid, ok, detail=""):
    CHECKS.append({"id": cid, "result": "PASS" if ok else "FAIL", "detail": detail})
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--reader", default=None)
    ap.add_argument("--ledger", default=None)
    ap.add_argument("--manifest", default=None)
    a = ap.parse_args()
    reader_p = Path(a.reader) if a.reader else EB / "w43-r3-5-reader-preview-UNVALIDATED-20261026.md"
    ledger_p = Path(a.ledger) if a.ledger else EB / "w43-r3-5-citation-confidence-ledger.json"
    manif_p = Path(a.manifest) if a.manifest else EB / "w43-r3-5-physical-row-manifest.json"
    reader_bytes = reader_p.read_bytes()
    ledger_bytes = ledger_p.read_bytes()
    manif_bytes = manif_p.read_bytes()
    reader = reader_bytes.decode("utf-8")
    ledger = json.loads(ledger_bytes.decode("utf-8"))
    manifest = json.loads(manif_bytes.decode("utf-8"))

    fails = validate(reader, manifest, ledger)
    check("T1-table-identity-20-headers", not [f for f in fails if f.startswith("T1")],
          "; ".join([f for f in fails if f.startswith("T1")][:4]) or "20 table headers exact, order pinned")
    check("T2-row-bijection-80", not [f for f in fails if f.startswith("T2") or f.startswith("T0")],
          "; ".join([f for f in fails if f.startswith("T2") or f.startswith("T0")][:4]) or "80 physical <-> 80 ledger, SHA/line/ordinal/row_type, 13 aliases pinned, 78 DATA/2 NOTE")
    check("C-claims-29-semantic", not [f for f in fails if re.match(r"C[0-9]?[-_]", f)],
          "; ".join([f for f in fails if re.match(r"C[0-9]?[-_]", f)][:4]) or "29 claims own-block DATA, physical-value proof, variant/metric/unit/comparator/URL/provenance")
    check("T5-anchors-incl-COBOL-npm", not [f for f in fails if f.startswith("T5")],
          "; ".join([f for f in fails if f.startswith("T5")][:4]) or "MemT/classifier/TTS/Controlled-Voice + COBOL 40%+ prevalence + npm full timestamp anchors hold")

    # Negative tests: each mutation MUST fail for its SPECIFIC semantic reason
    negs = []
    def neg(nid, mut, expect_substr):
        m2, l2, r2 = copy.deepcopy(manifest), copy.deepcopy(ledger), reader
        try:
            m2, l2, r2 = mut(m2, l2, r2)
        except Exception as e:
            negs.append({"id": nid, "result": "FAIL", "detail": f"mutation error: {e}"})
            return False
        f = validate(r2, m2, l2)
        ok = bool(f) and any(expect_substr in x for x in f)
        if bool(f) and not any(expect_substr in x for x in f):
            negs.append({"id": nid, "result": "FAIL", "detail": f"failed but for wrong reason (expected {expect_substr!r}): {f[0][:160]}"})
            return False
        negs.append({"id": nid, "result": "PASS" if ok else "FAIL",
                     "detail": ("fails as required ["+expect_substr+"]: " + next((x for x in f if expect_substr in x), f[0] if f else "")[:160]) if ok else "MUTATION NOT DETECTED or wrong reason"})
        return ok
    # --- preserved r3.4 regression negatives (manifest/ledger) ---
    def M_drop(m,l,r):
        m["tables_detail"][5]["rows"].pop(2); return m,l,r
    def M_dup(m,l,r):
        m["tables_detail"][0]["rows"].append(copy.deepcopy(m["tables_detail"][0]["rows"][0])); return m,l,r
    def M_swap(m,l,r):
        a = m["tables_detail"][9]["rows"]; a[0]["physical_text"], a[1]["physical_text"] = a[1]["physical_text"], a[0]["physical_text"]; return m,l,r
    def M_mut(m,l,r):
        m["tables_detail"][0]["rows"][0]["physical_text"] += "X"; return m,l,r
    def M_note(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        byid["p8-f2"]["claims"][0]["row_id"] = "p1-t2-04"; return m,l,r
    def M_xblock(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        byid["p8-f2"]["claims"][0]["row_id"] = "p8-f3-01"; return m,l,r
    def M_npm(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for tr in byid["p8-f2"]["table_rows"]:
            if tr["row_id"] == "p8-f2-03": tr["url"] = "https://registry.npmjs.org/ai"; return m,l,r
    def M_unit(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for c in byid["p5-f1"]["claims"]:
            if c["value"] == "$0.004": c["unit"] = "$/min (confirmed)"; return m,l,r
    def M_noteblock(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        byid["p1-t2"]["claims"] = [{"value": "SYNTH", "metric": "synth", "unit": "synth",
            "denominator_comparison": "synth", "model_variant": "Kimi test",
            "evidence_task_id": "synth", "claim_id": "synth",
            "archive_path": "ARCHIVE_UNAVAILABLE", "row_id": "p1-t2-04"}]; return m,l,r
    # --- new TRUE physical/semantic negatives (actual reader mutations) ---
    def P_del_row(m,l,r):
        # delete one physical ｜-line from reader (p1-t1-01)
        ls = r.split("\n")
        # find first physical row line containing 告知・API提供
        for i,ln in enumerate(ls):
            if "告知・API提供" in ln and "｜" in ln:
                del ls[i]; break
        return m,l,"\n".join(ls)
    def P_dup_row(m,l,r):
        ls = r.split("\n")
        for i,ln in enumerate(ls):
            if "告知・API提供" in ln and "｜" in ln:
                ls.insert(i+1, ln); break
        return m,l,"\n".join(ls)
    def P_swap_rows(m,l,r):
        ls = r.split("\n")
        idx=[i for i,ln in enumerate(ls) if ln.startswith("25.37x｜") or ln.startswith("22.31x｜")]
        if len(idx)>=2:
            ls[idx[0]], ls[idx[1]] = ls[idx[1]], ls[idx[0]]
        return m,l,"\n".join(ls)
    def P_mut_text(m,l,r):
        # target the physical COBOL row specifically (not prose): replace within the ｜-line
        ls = r.split("\n")
        for i,ln in enumerate(ls):
            if ln.startswith("COBOL ｜10.9→72.1"):
                ls[i] = ln.replace("10.9→72.1","10.8→72.1",1)
                break
        return m,l,"\n".join(ls)
    def P_header(m,l,r):
        return m,l,r.replace("【表：公開状態×時点（Kimi）】","【表：公開状態×時点（Kimi改）】",1)
    def P_cobol_strip(m,l,r):
        # pre-fix r3.4 counterexample: consistent reader+manifest WITHOUT enterprise facet,
        # so T2 passes but C-VALUE-MISSING must fail (semantic, not hash)
        r2 = r.replace("・企業現場40%超（オンラインバンキング言及、精度とは別）","",1)
        # keep manifest consistent with stripped reader so T2 does not mask C
        for t in m["tables_detail"]:
            if t["table_id"]=="p7-f1":
                for row in t["rows"]:
                    if row["row_id"]=="p7-f1-01" and "企業現場40%超" in row["physical_text"]:
                        row["physical_text"] = row["physical_text"].replace("・企業現場40%超（オンラインバンキング言及、精度とは別）","",1)
                        import hashlib as _hl
                        row["sha256"] = _hl.sha256(row["physical_text"].encode("utf-8")).hexdigest()
        return m,l,r2
    def P_npm_strip(m,l,r):
        r2 = r.replace("（npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠）","",1)
        for t in m["tables_detail"]:
            if t["table_id"]=="p8-f2":
                for row in t["rows"]:
                    if row["row_id"]=="p8-f2-03" and "npm 2026-10-22T15:21:49Z" in row["physical_text"]:
                        row["physical_text"] = row["physical_text"].replace("（npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠）","",1)
                        import hashlib as _hl
                        row["sha256"] = _hl.sha256(row["physical_text"].encode("utf-8")).hexdigest()
        return m,l,r2
    def L_claim_rm(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        byid["p7-f1"]["claims"] = [c for c in byid["p7-f1"]["claims"] if not (c["value"]=="40%+" )]
        return m,l,r
    def L_value_change(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for c in byid["p7-f1"]["claims"]:
            if c["value"]=="10.9→72.1": c["value"]="99.9→99.9"
        return m,l,r
    def L_variant(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for c in byid["p7-f1"]["claims"]:
            if c["value"]=="10.9→72.1": c["model_variant"]="Fortran"
        return m,l,r
    def L_metric(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for c in byid["p7-f1"]["claims"]:
            if c["value"]=="10.9→72.1": c["metric"]="cost"
        return m,l,r
    def L_url_wrong(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for tr in byid["p7-f1"]["table_rows"]:
            if tr["row_id"]=="p7-f1-01": tr["url"]="https://example.com/unrelated"
        return m,l,r
    def L_prov(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for c in byid["p7-f1"]["claims"]:
            if c["value"]=="10.9→72.1": c["archive_path"]="sources/nonexistent/missing.md"
        return m,l,r
    def L_rowtype(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for tr in byid["p7-f1"]["table_rows"]:
            if tr["row_id"]=="p7-f1-01": tr["row_type"]="NOTE"
        # also manifest must flip? mutate ledger only to trigger T2-ROWTYPE-MISMATCH
        return m,l,r
    def L_comparator(m,l,r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for c in byid["p5-f1"]["claims"]:
            if c["value"]=="4.1/4.0": c["denominator_comparison"]="none"
        return m,l,r

    results = []
    results.append(neg("NEG-drop-row-manifest", M_drop, "T2"))
    results.append(neg("NEG-dup-row-manifest", M_dup, "T2"))
    results.append(neg("NEG-swap-rows-manifest", M_swap, "T2-HASH"))
    results.append(neg("NEG-mutate-text-manifest", M_mut, "T2-HASH"))
    results.append(neg("NEG-claim-to-NOTE-xblock", M_note, "C-CROSS-BLOCK"))
    results.append(neg("NEG-claim-xblock", M_xblock, "C-CROSS-BLOCK"))
    results.append(neg("NEG-npm-unscoped", M_npm, "C-URL"))
    results.append(neg("NEG-unit-false-confirm", M_unit, "C-UNIT"))
    results.append(neg("NEG-note-sameblock-synth", M_noteblock, "C-NOTE"))
    results.append(neg("NEG-phys-del-row", P_del_row, "T2"))
    results.append(neg("NEG-phys-dup-row", P_dup_row, "T2"))
    results.append(neg("NEG-phys-swap-rows", P_swap_rows, "T2-HASH"))
    results.append(neg("NEG-phys-mutate-value", P_mut_text, "T2-HASH"))
    results.append(neg("NEG-phys-header-mutate", P_header, "T1-HEADER"))
    results.append(neg("NEG-claim-remove-29-28", L_claim_rm, "C0-COUNT"))
    results.append(neg("NEG-claim-value-change-no-row", L_value_change, "C-BASELINE-MISSING"))
    results.append(neg("NEG-variant-change", L_variant, "C-VARIANT"))
    results.append(neg("NEG-metric-change", L_metric, "C-METRIC"))
    results.append(neg("NEG-url-wrong-source", L_url_wrong, "C-URL"))
    results.append(neg("NEG-provenance-false-path", L_prov, "C-PROVENANCE"))
    results.append(neg("NEG-rowtype-DATA-NOTE-flip", L_rowtype, "T2-ROWTYPE"))
    results.append(neg("NEG-comparator-unqualified", L_comparator, "C-COMPARATOR"))
    results.append(neg("NEG-COBOL-prefixed-missing-40p", P_cobol_strip, "p7-f1-01/enterprise-40p"))
    results.append(neg("NEG-npm-prefixed-missing-clock", P_npm_strip, "p8-f2-03/npm-clock"))
    n_ok = all(results)
    check("NEG-all-detected-specific-reason", n_ok, f"{sum(1 for n in negs if n['result']=='PASS')}/{len(negs)} mutations detected for specific semantic reason")

    # Provenance tiers (report only)
    tiers = {"RAW_PRIMARY": 0, "QUALIFIED_UNAVAILABLE": 0, "OTHER": 0}
    for r in ledger["rows"]:
        for c in (r.get("claims") or []):
            ap2 = c.get("archive_path","")
            if ap2.startswith("sources/"): tiers["RAW_PRIMARY"] += 1
            elif "ARCHIVE_UNAVAILABLE" in ap2 or "RAW_NOT_ARCHIVED" in ap2: tiers["QUALIFIED_UNAVAILABLE"] += 1
            else: tiers["OTHER"] += 1
    check("TIER-report", True, json.dumps(tiers, ensure_ascii=False))

    verdict = "EDITION_LOCAL_ROW_JOIN_PASS" if all(c["result"]=="PASS" for c in CHECKS) else "ROW_JOIN_OPEN"
    if verdict != "EDITION_LOCAL_ROW_JOIN_PASS":
        verdict = "P1_OPEN" if any("C-" in f or "T5" in f for f in fails) else "ROW_JOIN_OPEN"
        # contract terminal: P1_OPEN on any failed required semantic assertion
    # itemize headers/rows/claims for auditability
    headers_out = [{"table_id": tid, "header": hdr} for tid, hdr in zip(TABLE_ORDER, EXPECTED_HEADERS)]
    rows_out = [{"row_id": r["row_id"], "row_type": r["row_type"], "sha256": r["sha256"][:12]+"…", "ledger_label": r.get("ledger_label")} for t in manifest["tables_detail"] for r in t["rows"]]
    claims_out = [{"key": e["k"], "block": e["block"], "row": e["row"], "value": e["value"], "metric": e["metric"], "variant": e["variant"]} for e in EXPECTED_CLAIMS]
    result = {"tool": "w43-r3-5-strict-semantic-claim-join-check.py",
              "scope": "edition-local join only; not source originality, not native Stage, not independent Sol sign-off",
              "lexical_map": LEXICAL_MAP_NOTE,
              "reader": reader_p.name, "reader_sha256": hashlib.sha256(reader_bytes).hexdigest(),
              "ledger": ledger_p.name, "ledger_sha256": hashlib.sha256(ledger_bytes).hexdigest(),
              "ledger_canonical_json_sha256": hashlib.sha256(json.dumps(ledger, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
              "manifest": manif_p.name, "manifest_sha256": hashlib.sha256(manif_bytes).hexdigest(),
              "manifest_canonical_json_sha256": hashlib.sha256(json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
              "verdict": verdict if verdict in ("EDITION_LOCAL_ROW_JOIN_PASS",) else verdict,
              "positive_exit_code_would_be": 0 if verdict=="EDITION_LOCAL_ROW_JOIN_PASS" else 1,
              "tables_expected": 20, "headers": headers_out,
              "rows_expected": 80, "rows": rows_out,
              "claims_expected": 29, "claims": claims_out,
              "tiers": tiers,
              "positive_failures": fails, "negative_tests": negs, "checks": CHECKS}
    js = json.dumps(result, ensure_ascii=False, indent=1)
    if a.out: Path(a.out).write_text(js, encoding="utf-8")
    print(js)
    return 0 if verdict == "EDITION_LOCAL_ROW_JOIN_PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
