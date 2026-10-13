"""Junta nq_cf/c*.py -> questões no formato do site (banco.json) + átomos CF (artigos.json).
Uso: python3 -I build_cf.py <nq_cf_dir> <out_dir> [cf_texto.json]   (gera cf_banco.json, cf_artigos.json)"""
import json, sys, glob, runpy, re, collections
import os
TXT = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
def corpo(num, inc):
    its = [re.sub(r"\s*\((?:[^()]*?)(?:Emenda|redação|Redação|Revogad)[^()]*\)\s*", " ", x).strip() for x in TXT.get(str(num), [])]
    if inc:
        out, on = [its[0]] if its else [], False
        for x in its[1:]:
            if x.startswith(inc + " -"): out.append(x); on = True
            elif on and re.match(r"[a-z]\)", x): out.append(x)
            else: on = False
        return out
    if len(its) > 70: its = [x for x in its if x.startswith(("Art.", "§", "Parágrafo"))]
    return its
out, atoms, n = [], {}, 0
seen = collections.Counter()
for f in sorted(glob.glob(sys.argv[1] + "/c*.py")):
    for (top, arts, gab, tx, com, tipo) in runpy.run_path(f)["Q"]:
        n += 1
        ids = []
        for a in arts:
            m = re.match(r"(\d+)(?:\.([IVXLC]+))?$", a); assert m, a
            aid = f"A-CF-{int(m.group(1)):04d}" + (f".{m.group(2)}" if m.group(2) else "")
            ids.append(aid)
            atoms[aid] = {"t": "CF art. " + m.group(1) + (f", {m.group(2)}" if m.group(2) else ""), "x": corpo(int(m.group(1)), m.group(2))}
        assert gab in "CE" and tx.strip() and com.strip(), (n, tx)
        seen[tx] += 1
        out.append({"id": f"Q-CF-{n:04d}", "t": top, "a": ids, "g": gab, "e": tx, "c": com, "k": tipo})
dups = [t for t, c in seen.items() if c > 1]
json.dump(out, open(sys.argv[2] + "/cf_banco.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(atoms, open(sys.argv[2] + "/cf_artigos.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
c = collections.Counter((q["t"], q["g"]) for q in out)
print(len(out), "questões;", sum(q["g"] == "C" for q in out), "C;", len(atoms), "átomos; dups:", len(dups))
for k in sorted(c): print(k, c[k])
