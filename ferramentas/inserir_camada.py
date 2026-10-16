"""Insere uma camada de questões (fabrica/camadas/cNN_*.py) em dados/site/banco.json. Uso: python3 -I ferramentas/inserir_camada.py fabrica/camadas/c01_legislativo.py NN"""
import json, re, runpy, sys, collections
arq, nn = sys.argv[1], sys.argv[2]
raiz = "."
B = json.load(open(f"{raiz}/dados/site/banco.json", encoding="utf-8")); A = json.load(open(f"{raiz}/dados/site/artigos.json", encoding="utf-8")); T = json.load(open(f"{raiz}/dados/site/topicos.json", encoding="utf-8"))
M = runpy.run_path(arq); Q = M["Q"]
for k_, v_ in M.get("ATOMOS", {}).items(): A[k_] = v_
if M.get("ATOMOS"): json.dump(A, open(f"{raiz}/dados/site/artigos.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
norm = lambda s: re.sub(r"\s+", " ", " ".join(s) if isinstance(s, list) else s)
B = [q for q in B if not q["id"].startswith(f"Q-N{nn}-")]  # idempotente
fcamp = {t: collections.Counter(q.get("f") for q in B if q["t"] == t and q.get("f")).most_common(1) for t in T}
novos = []
atop = {}
for q in B:
    for a_ in q["a"]: atop.setdefault(a_, collections.Counter())[q["t"]] += 1
for i, (t, a, g, e, c, fr, k) in enumerate(Q, 1):
    if t == "auto": t = atop[a].most_common(1)[0][0]
    assert t in T and a in A, (t, a)
    txt = norm(A[a]["x"]); assert fr in txt, fr
    segs = re.split(r"(?= § \d+º| Parágrafo único| [IVX]+ [-–] | [a-z]\) )", txt)
    seg = next((s.strip() for s in segs if fr in s), None) or txt[max(0, txt.index(fr)-40):txt.index(fr)+len(fr)+120]
    seg = seg[:420]
    novos.append({"id": f"Q-N{nn}-{i:03d}", "t": t, "a": [a], "g": g, "e": e, "c": c, "k": k, "f": (fcamp[t][0][0] if fcamp[t] else "geral"), "r": 1,
                  "s": [{"t": A[a]["t"], "c": "", "l": [seg]}]})
B += novos
json.dump(B, open(f"{raiz}/dados/site/banco.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("inseridas", len(novos), "total", len(B))
