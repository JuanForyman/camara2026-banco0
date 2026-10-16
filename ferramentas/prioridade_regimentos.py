"""Prioridade de incidência (q.r) para RICD e Regimento Comum, para o cargo Registro e Redação (Cebraspe, Câmara 2026).
Base: itens de regimento da prova de 8/3/2026 (Analista PL e Gestão, Assistente e Policial; 19 itens visíveis no QConcursos)
+ edital (P1: RICD 1–24, 65–94, 226–251, 262–273 e RC parcial; P2: RICD, RC, processo legislativo).
Temas que apareceram em 2026: atribuições da Mesa e do Presidente (agenda mensal, nº de deputados por partido nas comissões),
vedação de membros da Mesa em comissões, tipos e estrutura das sessões, interrupção da sessão legislativa, poderes das comissões
permanentes, voto do Presidente de comissão, votação nominal em quórum especial, urgência, Corregedoria e Polícia, decoro.
r = 1 (pesa 1,00), 2 (0,55), 3 (0,15). Questão com vários átomos fica com o menor r (mais relevante).
Uso: python3 -I ferramentas/prioridade_regimentos.py <banco.json> [v3.json ...]   (idempotente)"""
import json, re, sys
R1 = [(2,2),(7,8),(9,10),(12,13),(14,20),(25,32),(39,41),(65,67),(69,71),(79,79),(82,83),(87,87),(89,89),(91,92),(126,134),
      (151,157),(180,189),(226,226),(231,231),(235,235),(238,244),(250,251),(267,271)]
R3 = [(234,234),(259,261),(273,273)]
SUF_R1 = {(21,"E"),(21,"F"),(21,"G")}
SUF_R3 = {(13,"A"),(13,"B"),(20,"A"),(20,"B"),(20,"C"),(20,"D"),(20,"E"),(20,"F"),(20,"G"),(20,"H"),
          (21,"H"),(21,"I"),(21,"J"),(21,"K"),(21,"L"),(21,"M"),(21,"N"),(227,"A")}
RC1 = [(1,2),(10,10),(21,21),(27,28),(43,46)]
RC3 = [(57,71),(93,93),(96,98)]
def inr(n, rs): return any(a <= n <= b for a, b in rs)
def tier(atom):
    m = re.match(r"A-(RICD|RC)-(\d+)([A-Z]*)", atom)
    if not m: return None
    n, s = int(m.group(2)), m.group(3)
    if m.group(1) == "RICD":
        if (n, s) in SUF_R3: return 3
        if (n, s) in SUF_R1: return 1
        if s and not inr(n, R1): return 2
        if inr(n, R1): return 1
        if inr(n, R3): return 3
        return 2
    if inr(n, RC1): return 1
    if inr(n, RC3): return 3
    return 2
def apply(B):
    ch = {1: 0, 2: 0, 3: 0}
    for q in B:
        ts = [t for t in (tier(a) for a in q.get("a", [])) if t]
        if not ts: continue
        q["r"] = min(ts); ch[q["r"]] += 1
        if "incidencia" in q: q["incidencia"] = {1: "alta", 2: "media", 3: "baixa"}[q["r"]]
    return ch
if __name__ == "__main__":
    for p in sys.argv[1:]:
        B = json.load(open(p, encoding="utf-8")); c = apply(B)
        json.dump(B, open(p, "w", encoding="utf-8"), ensure_ascii=False, **({"indent": 1} if "/v3/" in p else {"separators": (",", ":")}))
        print(p, c)
