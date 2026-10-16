"""Fase B (parte 2): aplica gabaritos curtos (dados/gabaritos_b.json) em q.c e o trecho pertinente da aula (saiba_conceitual.json) em q.s.
Idempotente: só toca questões sem q.s da Fase A (as de dispositivo de lei)."""
import json, glob, os
raiz = os.path.join(os.path.dirname(__file__), "..")
out = {}
for f in sorted(glob.glob(f"{raiz}/fabrica/gabaritos_b/out/*.json")): out.update(json.load(open(f, encoding="utf-8")))
json.dump(out, open(f"{raiz}/dados/gabaritos_b.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
SC = json.load(open(f"{raiz}/dados/saiba_conceitual.json", encoding="utf-8"))
p = f"{raiz}/dados/site/banco.json"
B = json.load(open(p, encoding="utf-8"))
n = ns = 0
for q in B:
    r = out.get(q["id"])
    if not r or q.get("s"): continue
    q["c"] = r; n += 1
    bl = [b for b in SC.get(q["id"], []) if b.get("l")]
    if bl: q["s"] = bl; ns += 1
json.dump(B, open(p, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("gabaritos:", n, "| com Saiba mais focado:", ns)
