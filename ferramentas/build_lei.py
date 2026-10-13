"""Junta <nq_dir>/q*.py de UMA lei -> <out>/<sigla>_banco.json e <sigla>_artigos.json (formato do site; átomos A-<SIGLA>-NNNN[.ROMANO]).
Uso: python3 -I build_lei.py <SIGLA> <nome_curto> <nq_dir> <texto.json> <out_dir>"""
import json, sys, glob, runpy, re, collections
SIG, NOME, NQ, TXT, OUT = sys.argv[1:6]
T = json.load(open(TXT, encoding="utf-8")); ann = re.compile(r"\s*\((?:[^()]*?)(?:Redação|Incluíd|Vide|Revogad)[^()]*\)")
def corpo(num, inc):
    its = [ann.sub(" ", x).strip() for x in T.get(num, [])]
    if inc:
        out, on = [its[0]] if its else [], False
        for x in its[1:]:
            if x.startswith(inc + " -") or x.startswith(inc + " –"): out.append(x); on = True
            elif on and re.match(r"[a-z]\)", x): out.append(x)
            else: on = False
        return out
    return its
out, atoms, n, seen = [], {}, 0, collections.Counter()
for f in sorted(glob.glob(NQ + "/q*.py")):
    for (top, arts, gab, tx, com, tipo) in runpy.run_path(f)["Q"]:
        n += 1; ids = []
        for a in arts:
            m = re.match(r"(\d+[A-Z]?)(?:\.([IVXLC]+))?$", a); assert m and m.group(1) in T, (a, tx)
            aid = f"A-{SIG}-{int(re.match(r'\d+', m.group(1)).group(0)):04d}{re.sub(r'\d+', '', m.group(1))}" + (f".{m.group(2)}" if m.group(2) else "")
            ids.append(aid); atoms[aid] = {"t": f"{NOME} art. {m.group(1)}" + (f", {m.group(2)}" if m.group(2) else ""), "x": corpo(m.group(1), m.group(2))}
        assert gab in "CE" and tx.strip() and com.strip(), (n, tx); seen[tx] += 1
        out.append({"id": f"Q-{SIG}-{n:04d}", "t": top, "a": ids, "g": gab, "e": tx, "c": com, "k": tipo})
json.dump(out, open(f"{OUT}/{SIG.lower()}_banco.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(atoms, open(f"{OUT}/{SIG.lower()}_artigos.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "questões;", sum(q["g"] == "C" for q in out), "C;", len(atoms), "átomos; dups:", sum(c > 1 for c in seen.values()))
