"""Auditoria de gabaritos (C e E): truncados (…), >30 palavras, <5 palavras, ou C com gabarito igual ao do par.
  fila            -> grava fabrica/gabaritos_v3/fila.json (por relevância, tópico)
  ver N [T=30]    -> imprime o lote N
  aplicar         -> aplica fabrica/gabaritos_v3/out/*.json (id -> gabarito) com validações
Formato do gabarito: 'Fonte, art.: regra em até 25 palavras com **negrito** no ponto que a banca troca.'"""
import json, re, sys, glob, collections
A = "dados/site/banco.json"; F = "fabrica/gabaritos_v3/fila.json"
B = json.load(open(A, encoding="utf-8"))
def motivos(q, byc):
    c = q["c"]; n = len(c.split()); m = []
    if re.search(r"…(?:;|\]|\s*$)|\[…", c): m.append("trunc")
    if n > 30: m.append(">30")
    if n < 5: m.append("curto")
    if q["g"] == "C" and byc[c] > 1: m.append("par")
    return m
cmd = sys.argv[1]
if cmd == "fila":
    byc = collections.Counter(q["c"] for q in B)
    L = sorted([q for q in B if motivos(q, byc)], key=lambda q: (0 if set(motivos(q, byc)) & {"trunc", ">30"} else 1 if "par" in motivos(q, byc) else 2, q.get("r", 1), q["t"], q["id"]))
    json.dump([q["id"] for q in L], open(F, "w")); print(len(L))
elif cmd == "ver":
    n = int(sys.argv[1+1]); T = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    ids = json.load(open(F))[(n-1)*T:n*T]; M = {q["id"]: q for q in B}
    for i in ids:
        q = M[i]; s = " ".join(" ".join(b["l"]) for b in q.get("s", []))[:300]
        print(f'#{i} [{q["g"]}]\nITEM: {q["e"][:380]}\nC: {q["c"][:60]}\nFONTE: {s}\n')
elif cmd == "aplicar":
    M = {q["id"]: q for q in B}; n = rej = 0
    for f in sorted(glob.glob("fabrica/gabaritos_v3/out/*.json")):
        for i, c in json.load(open(f, encoding="utf-8")).items():
            ok = i in M and 3 <= len(c.replace("**", "").split()) <= 30 and c.count("**") % 2 == 0 and not c.endswith("…")
            if ok: M[i]["c"] = c; n += 1
            else: rej += 1; print("rejeitado", i, len(c.split()))
    json.dump(B, open(A, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":")); print("aplicados", n, "rejeitados", rej)
