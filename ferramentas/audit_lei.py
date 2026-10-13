"""Auditoria mecânica: números/prazos de itens C (e do 'correto' do comentário nos E) devem existir no texto dos artigos citados.
Uso: python3 -I audit_lei.py <texto.json> <nq_dir>"""
import json, re, glob, runpy, sys
T = json.load(open(sys.argv[1], encoding="utf-8"))
NW = {"um":1,"uma":1,"dois":2,"duas":2,"três":3,"quatro":4,"cinco":5,"seis":6,"sete":7,"oito":8,"nove":9,"dez":10,"onze":11,"doze":12,"quinze":15,"vinte":20,"trinta":30,"quarenta":40,"cinquenta":50,"cinqüenta":50,"sessenta":60,"setenta":70,"noventa":90,"cem":100,"cento":100,"terça":3,"terço":3,"quinto":5,"quintos":5,"décimo":10,"décimos":10,"metade":2,"dobro":2,"dezoito":18,"sessenta":60}
def nums(t):
    t = t.lower(); s = set(re.findall(r"\d+", t))
    for w in re.findall(r"[a-zçêéãíõ]+", t):
        if w in NW: s.add(str(NW[w]))
    return s
bad = 0
for f in sorted(glob.glob(sys.argv[2] + "/q*.py")):
    for (top, arts, g, tx, com, tipo) in runpy.run_path(f)["Q"]:
        b = " ".join(" ".join(T[re.match(r"\d+[A-Z]?", a).group(0)]) for a in arts)
        hv = nums(b) | {re.match(r"\d+", a).group(0) for a in arts}
        want = nums(tx) if g == "C" else nums(re.sub(r"^[^:]*:", "", com)) - nums(tx)
        miss = sorted(x for x in want - hv if x not in {"1"} or g == "C")
        if miss: bad += 1; print(g, arts, miss, "|", tx[:80], "||", com[:80])
print("alertas", bad)
