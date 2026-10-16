"""Mapa de lacunas: peso esperado de cada tópico do edital na prova x profundidade do banco.
Pesos de matéria (WT) = estimativa dos 90 itens de cada prova; pesos de tópico = estimativa de incidência (nivel: P=padrão de prova observado, C=conhecimento do autor). Refinar por camadas."""
import json, os, math, collections
raiz = os.path.join(os.path.dirname(__file__), "..")
B = json.load(open(f"{raiz}/dados/site/banco.json", encoding="utf-8")); T = json.load(open(f"{raiz}/dados/site/topicos.json", encoding="utf-8"))
MW = {"Língua Portuguesa": 25, "Língua Inglesa": 10, "Noções de Direito Administrativo e Administração Pública": 25, "Noções de Direito Constitucional e de Regimento Interno da Câmara": 20, "Tecnologia da Informação e Dados": 10,
      "Processo Legislativo, RICD e Regimento Comum": 35, "Linguística": 20, "Ciência Política": 20, "Reconhecimento de Fala, Transcrição e IA": 15}
S = {  # participação relativa do tópico dentro da matéria
 "P1-M1-1": .22, "P1-M1-2": .04, "P1-M1-3": .05, "P1-M1-4": .12, "P1-M1-5": .40, "P1-M1-6": .17,
 "P1-M2-1": .50, "P1-M2-2": .35, "P1-M2-3": .15,
 "P1-M3-1": .08, "P1-M3-2": .10, "P1-M3-3": .15, "P1-M3-4": .13, "P1-M3-5": .05, "P1-M3-6": .06, "P1-M3-7": .07, "P1-M3-8": .05, "P1-M3-9": .07, "P1-M3-10": .12, "P1-M3-11": .04, "P1-M3-12": .06,
 "P1-M4-1": .03, "P1-M4-2": .16, "P1-M4-3": .08, "P1-M4-4": .06, "P1-M4-5": .10, "P1-M4-6": .07, "P1-M4-7.1": .14, "P1-M4-7.2": .12, "P1-M4-7.3": .08, "P1-M4-7.4": .04, "P1-M4-8.1": .04, "P1-M4-8.2": .08,
 "P1-M5-1": .18, "P1-M5-2": .12, "P1-M5-3": .08, "P1-M5-4": .15, "P1-M5-5": .15, "P1-M5-6": .06, "P1-M5-7": .12, "P1-M5-8": .14,
 "P2-M8-1.1": .06, "P2-M8-1.2": .08, "P2-M8-1.3": .09, "P2-M8-1.4": .04, "P2-M8-1.5": .03, "P2-M8-2.1": .05, "P2-M8-2.2": .05, "P2-M8-2.3": .05, "P2-M8-2.4": .05, "P2-M8-2.5": .02,
 "P2-M8-2.6": .03, "P2-M8-2.7": .04, "P2-M8-2.8": .04, "P2-M8-2.9": .06, "P2-M8-2.10": .06, "P2-M8-2.11": .08, "P2-M8-3.1": .02, "P2-M8-3.2": .04, "P2-M8-3.3": .03, "P2-M8-3.4": .05, "P2-M8-3.5": .04,
 "P2-M6-1": .06, "P2-M6-2": .04, "P2-M6-3": .12, "P2-M6-4": .05, "P2-M6-5": .08, "P2-M6-6": .07, "P2-M6-7": .07, "P2-M6-8": .04, "P2-M6-9": .06, "P2-M6-10": .06, "P2-M6-11": .17, "P2-M6-12": .06, "P2-M6-13": .12,
 "P2-M9-1": .10, "P2-M9-2": .10, "P2-M9-3": .09, "P2-M9-4": .09, "P2-M9-5": .09, "P2-M9-6": .09, "P2-M9-7": .07, "P2-M9-8": .06, "P2-M9-9": .08, "P2-M9-10": .07, "P2-M9-11": .06}
for i in range(1, 9): S[f"P2-M7-1.{i}"] = .05
for i in range(1, 9): S[f"P2-M7-2.{i}"] = .0475
for i in range(1, 7): S[f"P2-M7-3.{i}"] = .02
for i in range(1, 4): S[f"P2-M7-4.{i}"] = .0333
K = 12  # questões no banco por item esperado na prova (variações C/E + reforço)
n = collections.Counter(q["t"] for q in B); r1 = collections.Counter(q["t"] for q in B if (q.get("r") or 1) == 1)
por_m = collections.defaultdict(float)
for t, s in S.items(): por_m[T[t]["m"]] += s
rows = []
for t, s in S.items():
    m = T[t]["m"]; e = MW[m] * s / por_m[m]; alvo = math.ceil(K * e)
    rows.append({"t": t, "tema": T[t]["t"], "m": m, "b": T[t]["b"], "esp": round(e, 2), "alvo": alvo, "n": n[t], "falta": max(0, alvo - n[t]), "r1": r1[t], "razao": round(n[t] / max(.1, e), 1)})
json.dump(rows, open(f"{raiz}/dados/mapa_cobertura.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
rows.sort(key=lambda r: (-r["falta"], r["razao"]))
print("tópico | esperado na prova | banco | alvo | falta")
for r in rows[:22]: print(f'{r["t"]:11} {r["esp"]:5} n={r["n"]:4} alvo={r["alvo"]:4} falta={r["falta"]:3} {r["tema"][:48]}')
print("total falta:", sum(r["falta"] for r in rows), "| tópicos com falta:", sum(1 for r in rows if r["falta"]))
print("\nmenor razão banco/esperado (profundidade relativa):")
for r in sorted(rows, key=lambda r: r["razao"])[:12]: print(f'{r["t"]:11} razão={r["razao"]:5} n={r["n"]:4} esp={r["esp"]:5} {r["tema"][:48]}')
