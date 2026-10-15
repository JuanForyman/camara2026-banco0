"""Verificador mecânico de qualidade do banco (S4 da Fábrica). Uso: python3 -I fabrica/lint.py dados/site/banco.json [saida.json]
Mede por tópico: balanço C/E, viés de tamanho, pista por palavra absoluta, quase-duplicatas, peso de 'leitura', cobertura de padrões."""
import json, re, sys, collections, hashlib
B = json.load(open(sys.argv[1], encoding="utf-8"))
ABS = re.compile(r"\b(sempre|nunca|jamais|exclusivamente|somente|apenas|qualquer|todos|todas|todo|toda|unicamente|em nenhuma hipótese|necessariamente)\b", re.I)
def norm(s): return re.sub(r"[^a-zà-ú0-9 ]", "", s.lower())
def sh(s):
    w = norm(s).split(); return {" ".join(w[i:i+4]) for i in range(max(1, len(w)-3))}
por = collections.defaultdict(list)
for q in B: por[q["t"]].append(q)
rel = {}
for t, qs in sorted(por.items()):
    n = len(qs); C = sum(q["g"] == "C" for q in qs)
    lc = [len(q["e"]) for q in qs if q["g"] == "C"]; le = [len(q["e"]) for q in qs if q["g"] == "E"]
    viés = (sum(le)/len(le) - sum(lc)/len(lc)) / (sum(lc)/len(lc)) if lc and le else 0
    absE = sum(1 for q in qs if q["g"] == "E" and ABS.search(q["e"])); E = n - C
    absC = sum(1 for q in qs if q["g"] == "C" and ABS.search(q["e"]))
    leit = sum(1 for q in qs if q.get("k") == "leitura")
    # quase-duplicatas (4-gramas) dentro do mesmo átomo
    dup = 0; porat = collections.defaultdict(list)
    for q in qs: porat[(q["a"][0] if q.get("a") else q["id"], q["g"])].append(sh(q["e"]))  # gêmeos C/E não contam
    for L in porat.values():
        for i in range(len(L)):
            for j in range(i+1, len(L)):
                if len(L[i] & L[j]) / max(1, min(len(L[i]), len(L[j]))) > 0.6: dup += 1
    rel[t] = {"n": n, "pctC": round(C/n, 2), "vies_tamanho_E_vs_C": round(viés, 2), "E_com_absoluto": round(absE/max(1, E), 2), "C_com_absoluto": round(absC/max(1, C), 2),
              "pct_leitura": round(leit/n, 2), "quase_duplicatas": dup, "r": dict(collections.Counter(q.get("r", 1) for q in qs))}
g = {"questoes": len(B), "pctC": round(sum(q["g"] == "C" for q in B)/len(B), 3)}
alertas = []
for t, m in rel.items():
    if m["n"] >= 10 and not (0.40 <= m["pctC"] <= 0.60): alertas.append(f"{t}: {int(m['pctC']*100)}% C (fora de 40-60)")
    if m["n"] >= 10 and abs(m["vies_tamanho_E_vs_C"]) > 0.12: alertas.append(f"{t}: viés de tamanho {m['vies_tamanho_E_vs_C']:+.0%} (E vs C)")
    if m["pct_leitura"] > 0.35: alertas.append(f"{t}: {int(m['pct_leitura']*100)}% de itens de leitura")
    if m["quase_duplicatas"] > 3: alertas.append(f"{t}: {m['quase_duplicatas']} pares quase duplicados no mesmo átomo")
    if m["n"] >= 10 and m["E_com_absoluto"] > 0.5 and m["C_com_absoluto"] < 0.1: alertas.append(f"{t}: palavra absoluta denuncia o E ({int(m['E_com_absoluto']*100)}% dos E x {int(m['C_com_absoluto']*100)}% dos C)")
out = {"geral": g, "topicos": rel, "alertas": alertas}
json.dump(out, open(sys.argv[2] if len(sys.argv) > 2 else "/dev/stdout", "w", encoding="utf-8"), ensure_ascii=False, indent=1) if len(sys.argv) > 2 else None
print(g); print(len(alertas), "alertas"); [print(" -", a) for a in alertas[:40]]
