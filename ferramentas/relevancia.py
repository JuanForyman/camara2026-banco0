"""Relevância de prova (q.r): 1 = padrão Cebraspe (pegadinha, número/prazo, exceção, generalização, dispositivo de alta incidência);
2 = plausível; 3 = letra seca/baixa chance. O motor serve r=1 primeiro (peso 1), r=2 (0,55), r=3 (0,15).
Uso: python3 -I relevancia.py <banco.json>   (idempotente; só mexe nas questões da Lei 9.784 por ora; demais ficam sem r = 1)."""
import json, re, sys
ALTA = {1: [], 2: "all", 3: [], 11: "all", 12: "all", 13: "all", 14: "all", 15: "all", 18: "all", 19: "all", 20: "all", 26: "all", 30: "all", 48: "all", 49: "all",
        50: "all", 53: "all", 54: "all", 55: "all", 56: "all", 57: "all", 59: "all", 60: "all", 61: "all", 63: "all", 64: "all", 65: "all"}
MEDIA = {3, 5, 9, 10, 17, 21, 22, 27, 31, 36, 38, 45, 58, 62, 66, 67}
B = json.load(open(sys.argv[1], encoding="utf-8"))
cnt = {1: 0, 2: 0, 3: 0}
for q in B:
    if not q["id"].startswith("Q-L9784-") or "d" in q: continue  # itens v3 já trazem r e d
    art = int(re.match(r"A-L9784-(\d+)", q["a"][0]).group(1))
    if q["k"] != "leitura": r = 1
    elif q["id"] in ("Q-L9784-0003",): r = 1  # aplicação ao Legislativo (art. 1º, §1º): tema da Câmara
    elif art in ALTA and ALTA[art] == "all": r = 2 if art in (15, 49, 60, 63, 30) else 1
    elif art in MEDIA: r = 2
    else: r = 3
    q["r"] = r; cnt[r] += 1
json.dump(B, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(cnt)
