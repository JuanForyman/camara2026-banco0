"""Junta lotes nq/*.py (questões novas redigidas a partir do texto oficial) -> questoes_novas_p1.json
Uso: python3 -I build_new.py <atomos_regimentos.json> <fontes_29ed.json> <nq_dir> <out.json>"""
import json, sys, glob, re, runpy, hashlib
at = {a["id"]: a for a in json.load(open(sys.argv[1]))["atomos"]}
fon = json.load(open(sys.argv[2]))
txt = {}
for n in ("RICD", "RC"):
    for a in fon[n]:
        txt[(n, a["art"], a["suf"])] = re.sub(r"\s+", " ", " ".join(d["texto"] for d in a["disp"])).lower()
NUMW = {"um":1,"uma":1,"dois":2,"duas":2,"três":3,"quatro":4,"cinco":5,"seis":6,"sete":7,"oito":8,"nove":9,"dez":10,"onze":11,"doze":12,"quinze":15,"vinte":20,"trinta":30,"quarenta":40,"cinquenta":50,"sessenta":60,"setenta":70,"noventa":90}
out, n = [], 0
for f in sorted(glob.glob(sys.argv[3] + "/b*.py")):
    ns = runpy.run_path(f)
    for (top, norma, arts, gab, tx, com, tipo) in ns["Q"]:
        n += 1; ids = []; chk = {"artigos_existem": True, "numeros_ancorados": None}; body = ""
        for a in arts:
            s = re.match(r"(\d+)([A-Z]*)", str(a)); k = (norma, int(s.group(1)), s.group(2))
            aid = f"A-{norma}-{k[1]:04d}{k[2]}"
            if aid in at and k in txt: ids.append(aid); body += " " + txt[k]
            else: chk["artigos_existem"] = False
        if gab == "C" and body:
            have = set(re.findall(r"\d+", body)) | {str(NUMW[w]) for w in re.findall(r"[a-zçêé]+", body) if w in NUMW}
            low = tx.lower(); want = set(re.findall(r"\d+", low)) | {str(NUMW[w]) for w in re.findall(r"[a-zçêé]+", low) if w in NUMW}
            miss = sorted(x for x in want if x not in have and x not in {"1"})
            chk["numeros_ancorados"] = not miss
            if miss: chk["numeros_sem_ancora"] = miss
        out.append({"id": f"Q-P1N-{n:04d}", "tipo": "CE", "topico": top, "atomos": ids, "externos": [], "enunciado": tx,
                    "gabarito": gab, "comentario": com, "erro_tipo": tipo, "origem": "ia-texto-oficial-29ed", "validada": False, "checks": chk})
json.dump({"schema": "v2", "questoes": out}, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
bad = [q["id"] + " " + q["enunciado"][:60] + str(q["checks"]) for q in out if not q["checks"]["artigos_existem"] or q["checks"]["numeros_ancorados"] is False]
print(len(out), "questões;", sum(q["gabarito"] == "C" for q in out), "C;", len(bad), "alertas"); print("\n".join(bad))
