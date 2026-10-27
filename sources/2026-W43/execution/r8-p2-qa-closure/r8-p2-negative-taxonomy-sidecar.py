#!/usr/bin/env python3
"""r8 P2-02 QA sidecar: strict negative taxonomy wrapper (NO fixed-artifact edit).

Wraps the immutable fixed r8 checker read-only; adds:
  - explicit all-required-causes assertion (original uses any(), NOT all)
  - controlled process-meta taxonomy for unknown insertion 編集承認ゲート通過済み

Original fixed checker: sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py
This sidecar never writes to r6/r7/r8 namespaces; prints JSON to stdout only.

Usage:
  python3 r8-p2-negative-taxonomy-sidecar.py --repo-root . [--staged-dir DIR] [--mode all|clean|operator-baseline|strict-operator|n10|n13]
Exit 0 on strict PASS, 3 on FAIL.
"""
import argparse, hashlib, importlib.util, json, pathlib, re, sys

R7_TEX_REL = "sources/2026-W43/execution/core-free-preview-r7/main.tex"
R7_SHA = "9791a545c1ed363f8abace62c90bdbfe15f31dac4017b80a5109907c35509ea0"
R8_TEX_REL = "sources/2026-W43/execution/core-free-preview-r8/main.tex"
R8_SHA = "4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d"
ORIG_CHECKER_REL = "sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py"
ORIG_CHECKER_SHA = "58abfc0dd3fcb38bc1461a540b62ecbce92ab84eddcd5ed60439489e057e5e98"

EXTRA_PROCESS_META = ["編集承認ゲート通過済み"]

def load_orig(repo):
    p = repo / ORIG_CHECKER_REL
    data = p.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    assert sha == ORIG_CHECKER_SHA, f"orig checker SHA mismatch {sha}"
    spec = importlib.util.spec_from_file_location("r8orig", str(p))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def strict_leaks(orig_mod, tex):
    leaks, vis = orig_mod.check_meta_visible(tex)
    extra = [x for x in EXTRA_PROCESS_META if x in vis]
    return sorted(set(leaks) | set(extra)), vis

def run_case(orig_mod, r7t, base_clean, mut, expect_all, cid):
    # original baseline causes via same full checker
    causes_orig, _ = orig_mod.check_mutation_new(r7t, mut)
    # strict: full clean on mutant + extra taxonomy
    res, _ = orig_mod.run_clean_on_texts(r7t, mut)
    causes = []
    for r in res:
        if r["result"] == "FAIL" and r["cause"] != "—" and r["cause"] not in causes:
            causes.append(r["cause"])
    leaks_strict, _ = strict_leaks(orig_mod, mut)
    if leaks_strict:
        if "READER_META_LEAK" not in causes:
            causes.append("READER_META_LEAK")
    causes = sorted(causes)
    ok = all(e in causes for e in expect_all) and len(causes) > 0
    return {"id": cid, "result": "PASS" if ok else "FAIL",
            "expected_all_required": sorted(expect_all),
            "actual_causes": causes,
            "original_baseline_causes": sorted(causes_orig),
            "mut_sha256": sha256_text(mut), "mut_bytes": len(mut.encode("utf-8")),
            "detail": f"require ALL {sorted(expect_all)}, got {causes} (orig baseline {sorted(causes_orig)})"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--staged-dir", default=None)
    ap.add_argument("--mode", default="all",
                    choices=["all", "clean", "operator-baseline", "strict-operator", "n10", "n13"])
    a = ap.parse_args()
    repo = pathlib.Path(a.staged_dir) if a.staged_dir else pathlib.Path(a.repo_root)
    orig = load_orig(repo)
    r7t = (repo / R7_TEX_REL).read_text(encoding="utf-8")
    r8t = (repo / R8_TEX_REL).read_text(encoding="utf-8")
    assert hashlib.sha256(r7t.encode()).hexdigest() == R7_SHA
    assert hashlib.sha256(r8t.encode()).hexdigest() == R8_SHA
    out = {"python": sys.version.split()[0], "deps": "stdlib only",
           "orig_checker_sha": ORIG_CHECKER_SHA, "r7_sha": R7_SHA, "r8_sha": R8_SHA,
           "r8_clean_sha": sha256_text(r8t), "results": []}
    def clean_case():
        res, _ = orig.run_clean_on_texts(r7t, r8t)
        fails = [r for r in res if r["result"] == "FAIL"]
        out["results"].append({"id": "clean-strict", "result": "PASS" if not fails else "FAIL",
                               "expected_all_required": [], "actual_causes": sorted({r["cause"] for r in fails if r["cause"] != "—"}),
                               "detail": f"clean {len(res)-len(fails)}/{len(res)}"})
    N10_OLD = "MoonshotのKimi K3.1 Proは10月23日の告知とAPI提供が先行し、重み配布は11月4日の将来予定である。"
    N10_MUT = "MoonshotのKimi K3.1 Proは10月23日の告知後、API提供も重み配布もすべて終了した。"
    N13_OLD = "発行元引用として扱う"
    N13_MUT = "独立測定結果として扱う"
    assert r8t.count(N13_OLD) == 1, f"N13 anchor count {r8t.count(N13_OLD)} != 1"
    cases = {
        "clean": lambda: clean_case(),
        "operator-baseline": lambda: out["results"].append(
            {"id": "N-operator-insert-original-baseline",
             "result": "INFO",
             "expected_all_required": [],
             "actual_causes": sorted(orig.check_mutation_new(r7t, r8t.replace(
                 "今週の巻頭は「発表された能力」と「動かせる実物」を切り分けて読む。",
                 "今週の巻頭は「発表された能力」と「動かせる実物」を切り分けて読む。編集承認ゲート通過済み。", 1))[0]),
             "detail": "original evaluator any() baseline; NOT strict"}),
        "strict-operator": lambda: out["results"].append(run_case(
            orig, r7t, r8t, r8t.replace(
                "今週の巻頭は「発表された能力」と「動かせる実物」を切り分けて読む。",
                "今週の巻頭は「発表された能力」と「動かせる実物」を切り分けて読む。編集承認ゲート通過済み。", 1),
            ["READER_META_LEAK", "PROSE_FIDELITY_LOSS"], "N-operator-insert-strict")),
        "n10": lambda: out["results"].append(run_case(
            orig, r7t, r8t, r8t.replace(N10_OLD, N10_MUT),
            ["PROSE_FIDELITY_LOSS"], "N10-prose-semantic-inversion-strict")),
        "n13": lambda: out["results"].append(run_case(
            orig, r7t, r8t, r8t.replace(N13_OLD, N13_MUT),
            ["PROSE_FIDELITY_LOSS"], "N13-ming-vendor-quote-to-independent-measurement-strict")),
    }
    if a.mode == "all":
        for k in ["clean", "operator-baseline", "strict-operator", "n10", "n13"]:
            cases[k]()
    else:
        cases[a.mode]()
    fails = [r for r in out["results"] if r["result"] == "FAIL"]
    out.update({"pass": len([r for r in out["results"] if r["result"] in ("PASS", "INFO")]),
                "fail": len(fails), "total": len(out["results"]),
                "verdict": "SIDECAR_STRICT_PASS" if not fails else "SIDECAR_STRICT_FAIL"})
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if not fails else 3

if __name__ == "__main__":
    sys.exit(main())
