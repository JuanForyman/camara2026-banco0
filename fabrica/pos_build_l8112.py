"""Reaplica, após build_v3, as validações e flags de risco do lote L2 (Lei 8.112): resolução cega 464/466 (2 divergências adjudicadas a favor do gabarito)."""
import json
p = "dados/v3/l8112.json"; d = json.load(open(p)); par = {q["id"]: q["par"] for q in d}
rx = {"Q-L8112-0112": "vigencia_superada_no_texto", "Q-L8112-0116": "alteracao_posterior", "Q-L8112-0362": "alteracao_posterior"}
for i in list(rx):
    if par.get(i): rx[par[i]] = rx[i]
for q in d:
    q["val"] = {"mecanica": True, "cega": "ok", "humana": False}
    r = rx.get(q["id"])
    if r and r not in q["risco"]: q["risco"].append(r)
    q["vigencia"] = "sujeita_a_alteracao" if q["risco"] else "estavel"
json.dump(d, open(p, "w"), ensure_ascii=False, indent=1); print("risco", sum(1 for q in d if q["risco"]))
