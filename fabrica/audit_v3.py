"""Gate mecânico v3 (lei): números/prazos dos itens C (e do 'correto' do comentário nos E) devem estar no texto dos artigos citados;
campos obrigatórios; pares; balanço. Uso: python3 -I fabrica/audit_v3.py dados/v3/<sigla>.json dados/<sigla>_artigos.json"""
import json, re, sys, collections
Q = json.load(open(sys.argv[1], encoding="utf-8")); A = json.load(open(sys.argv[2], encoding="utf-8"))
NW = {"um":1,"uma":1,"dois":2,"duas":2,"três":3,"quatro":4,"cinco":5,"seis":6,"sete":7,"oito":8,"nove":9,"dez":10,"quinze":15,"vinte":20,"trinta":30,"quarenta":40,"sessenta":60,"dezoito":18,"dezesseis":16,"terceiro":3,"quinto":5,"dobro":2,"triplo":3}
def nums(t):
    t = t.lower(); s = set(re.findall(r"\d+", t))
    for w in re.findall(r"[a-zçêéãíõ]+", t):
        if w in NW: s.add(str(NW[w]))
    return s
bad = []
for q in Q:
    for k in ["id","t","a","g","e","c","padrao","dif","r","fonte","origem","lote","val"]: assert k in q, (q["id"], k)
    if q["fonte"]["tipo"] != "lei": continue
    body = " ".join(" ".join(A[a]["x"]) for a in q["a"]); hv = nums(body) | {re.search(r"art\. (\d+)", A[a]["t"]).group(1) for a in q["a"]}
    want = nums(q["e"]) if q["g"] == "C" else nums(re.sub(r"^[^:]*:", "", q["c"])) - nums(q["e"])
    miss = sorted(x for x in want - hv if x != "1")
    if miss: bad.append((q["id"], q["g"], miss, q["e"][:70]))
for b in bad: print(b)
C = sum(q["g"] == "C" for q in Q); unp = sum(1 for q in Q if not q["par"] and q["g"] == "C")
lens = [len(q["e"]) for q in Q if q["g"] == "C"], [len(q["e"]) for q in Q if q["g"] == "E"]
print(f"alertas {len(bad)} | {len(Q)} itens | C {C/len(Q):.0%} | C sem par {unp} ({unp/len(Q):.0%}) | tam médio C {sum(lens[0])/len(lens[0]):.0f} E {sum(lens[1])/len(lens[1]):.0f}")
