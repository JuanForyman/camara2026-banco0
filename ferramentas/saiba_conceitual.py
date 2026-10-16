"""Fase B (parte 1): escolhe, na mini-aula do átomo, as linhas mais pertinentes à questão (Saiba mais) e exporta lotes para redação do gabarito.
Saída: dados/saiba_conceitual.json {id: [{"t","c","l":[...]}]} e fabrica/gabaritos_b/in/b_NNN.json"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from dispositivo import words, trim
raiz = os.path.join(os.path.dirname(__file__), "..")
B = json.load(open(f"{raiz}/dados/site/banco.json", encoding="utf-8"))
A = json.load(open(f"{raiz}/dados/site/artigos.json", encoding="utf-8"))
out = {}; todo = []
for q in B:
    if q.get("s"): continue
    blocos = []
    qw = words(q["e"] + " " + q["c"])
    for at in q.get("a", []):
        a = A.get(at)
        if not a: continue
        ls0 = a["x"][1:] if len(a["x"]) > 1 else a["x"]
        ls = []
        for l in ls0:
            if len(l.split()) > 45:
                ls += [t for t in re.split(r"(?<=[.;])\s+(?=(?:[IVXLC]+\s*[–-]\s|[a-z]\)\s|§\s*\d|[A-ZÀ-Ú]))", l) if t.strip()]
            else: ls.append(l)
        sc = sorted(((len(qw & words(l)), -i, i) for i, l in enumerate(ls)), reverse=True)
        pick = [i for s, _, i in sc[:2] if s >= 2]
        peg = [i for i, l in enumerate(ls) if l.startswith("Pegadinha")]
        if not pick: pick = [i for i, l in enumerate(ls) if not l.startswith("Pegadinha")][:1]
        if peg and peg[0] not in pick and len(ls) > 2 and len(pick) < 2: pick.append(peg[0])
        pick = sorted(set(pick))
        blocos.append({"t": a["t"], "c": "", "l": [trim(ls[i], 55) for i in pick]})
    if blocos: out[q["id"]] = blocos
    todo.append(q)
json.dump(out, open(f"{raiz}/dados/saiba_conceitual.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
d = f"{raiz}/fabrica/gabaritos_b/in"; os.makedirs(d, exist_ok=True)
fam = lambda q: q["id"].split("-")[1]
todo.sort(key=lambda q: (fam(q), q["id"]))
N = 70
for i in range(0, len(todo), N):
    lote = [{"id": q["id"], "g": q["g"], "e": q["e"], "velho": q["c"], "aula": [l for b in out.get(q["id"], []) for l in b["l"]]} for q in todo[i:i+N]]
    json.dump(lote, open(f"{d}/b_{i//N:03d}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(todo), "questões;", (len(todo)+N-1)//N, "lotes")
import collections; print(collections.Counter(fam(q) for q in todo))
