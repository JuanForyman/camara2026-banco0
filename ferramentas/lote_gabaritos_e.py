"""Itens E de lei/regimento cujo gabarito é só citação longa/truncada. Uso:
  python3 -I ferramentas/lote_gabaritos_e.py fila     -> grava fabrica/gabaritos_e/fila.json (ids ordenados por r, tópico)
  python3 -I ferramentas/lote_gabaritos_e.py ver N    -> imprime o lote N (50 itens) para redigir
  python3 -I ferramentas/lote_gabaritos_e.py aplicar  -> aplica fabrica/gabaritos_e/out/*.json (id -> novo gabarito) em banco.json"""
import json, re, sys, glob, os
raiz = "."; arqB = f"{raiz}/dados/site/banco.json"; fila = f"{raiz}/fabrica/gabaritos_e/fila.json"
B = json.load(open(arqB, encoding="utf-8"))
ref = re.compile(r"^(Lei [\d\.]+/?\d*|RICD|RC|Regimento|Art\.|CF|Decreto|STJ|STF|LC|Súmula|Res)", re.I)
def ruim(q): return q["g"] == "E" and ref.match(q["c"]) and ("…" in q["c"] or len(q["c"].split()) > 25)
cmd = sys.argv[1]
if cmd == "fila":
    L = sorted([q for q in B if ruim(q)], key=lambda q: (q.get("r", 1), q["t"], q["id"]))
    json.dump([q["id"] for q in L], open(fila, "w")); print(len(L))
elif cmd == "ver":
    n = int(sys.argv[2]); ids = json.load(open(fila))[(n-1)*30:n*30]; M = {q["id"]: q for q in B}
    for i in ids:
        q = M[i]; s = " / ".join(" ".join(b["l"]) if b.get("l") else b.get("c", "") for b in q.get("s", []))[:300]
        print(f'#{i}\nE: {q["e"][:240]}\nTXT: {q["c"][:70]} || {s}\n')
elif cmd == "aplicar":
    M = {q["id"]: q for q in B}; n = 0
    for f in sorted(glob.glob(f"{raiz}/fabrica/gabaritos_e/out/*.json")):
        for i, c in json.load(open(f, encoding="utf-8")).items():
            if i in M and len(c.split()) <= 30: M[i]["c"] = c; n += 1
    json.dump(B, open(arqB, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":")); print("aplicados", n)
