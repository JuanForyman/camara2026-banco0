"""Mescla um lote da Fábrica em dados/site. Uso: python3 -I merge_lote.py L8112 dados/l8112_banco.json dados/l8112_artigos.json"""
import json, sys
sig, bf, af = sys.argv[1:4]
B = "dados/site/banco.json"; A = "dados/site/artigos.json"
b = [q for q in json.load(open(B)) if not q["id"].startswith(f"Q-{sig}-")]
a = {k: v for k, v in json.load(open(A)).items() if not k.startswith(f"A-{sig}-")}
b += json.load(open(bf)); a.update(json.load(open(af)))
json.dump(b, open(B, "w"), ensure_ascii=False, separators=(",", ":"))
json.dump(a, open(A, "w"), ensure_ascii=False, separators=(",", ":"))
print(len(b), "questões;", len(a), "átomos")
