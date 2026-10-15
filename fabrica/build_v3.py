"""Fábrica: junta fabrica/questoes/<sigla>_*.py + blueprint + texto da lei -> dados/v3/<sigla>.json (metadados completos),
<out>/<sigla>_banco.json e <sigla>_artigos.json (formato do site; k=padrão, r, d). Uso: python3 -I fabrica/build_v3.py <blueprint.json> <texto.json> <out_dir> [lote]"""
import json, sys, glob, runpy, re, collections, os, datetime
BP, TXT, OUT = sys.argv[1:4]; LOTE = sys.argv[4] if len(sys.argv) > 4 else "L1"
bp = json.load(open(BP, encoding="utf-8")); T = json.load(open(TXT, encoding="utf-8")); SIG = bp["sigla"]
ann = re.compile(r"\s*\((?:[^()]*?)(?:Redação|Incluíd|Vide|Revogad)[^()]*\)")
inc = {p["id"]: p["incidencia"] for p in bp["pontos"]}
def corpo(num, ic):
    its = [ann.sub(" ", x).strip() for x in T.get(num, [])]
    if ic:
        out, on = [its[0]] if its else [], False
        for x in its[1:]:
            if x.startswith(ic + " -") or x.startswith(ic + " –"): out.append(x); on = True
            elif on and re.match(r"[a-z]\)", x): out.append(x)
            else: on = False
        return out
    return its
files = sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "questoes", SIG.lower() + "_*.py")))
rows = []
for f in files: rows += runpy.run_path(f)["Q"]
drop = set(bp.get("descartar_tags", []))
rows = [r for r in rows if r[8] not in drop]
atoms, full, slim, bytag = {}, [], [], collections.defaultdict(list)
for n, (ponto, arts, g, padrao, dif, e, c, terro, tag, ex) in enumerate(rows, 1):
    ids = []
    for a in arts:
        m = re.match(r"(\d+[A-Z]?)(?:\.([IVXLC]+))?$", a); assert m and m.group(1) in T, (a, e)
        aid = f"A-{SIG}-{int(re.match(r'\d+', m.group(1)).group(0)):04d}{re.sub(r'\d+', '', m.group(1))}" + (f".{m.group(2)}" if m.group(2) else "")
        ids.append(aid); atoms[aid] = {"t": f"{bp.get('nome_curto','Lei 9.784/99')} art. {m.group(1)}" + (f", {m.group(2)}" if m.group(2) else ""), "x": corpo(m.group(1), m.group(2))}
    qid = f"Q-{SIG}-{n:04d}"; bytag[tag].append(qid)
    i = inc[ponto]; r = 1 if i == "alta" else 2 if i == "media" else 3
    fonte = ex.get("fonte") or {"tipo": "lei", "ref": bp["fonte"]["ref"] + ", " + ", ".join("art. " + a for a in arts), "versao": bp["fonte"]["versao"], "conferida": bp["fonte"]["conferida"]}
    full.append({"id": qid, "t": bp.get("topico_por_ponto",{}).get(ponto,bp["topico"]), "materia": bp["materia"], "bloco": bp["bloco"], "item_edital": bp.get("item_edital_por_ponto",{}).get(ponto,bp["item_edital"]), "a": ids, "ponto": ponto, "g": g,
        "e": e, "formato": "caso_concreto" if padrao == "caso_concreto" else "assertiva", "c": c, "padrao": padrao, "tipo_erro": terro, "par": "", "dif": dif, "r": r, "incidencia": i,
        "fonte": fonte, "vigencia": "estavel", "risco": ex.get("risco", []), "origem": "autoral", "lote": LOTE, "criada": datetime.date.today().isoformat(), "versao": 1,
        "tags": [], "val": {"mecanica": False, "cega": "nao", "humana": False}, "_tag": tag})
for q in full:
    q["par"] = next((x for x in bytag[q["_tag"]] if x != q["id"]), ""); del q["_tag"]
    slim.append({"id": q["id"], "t": q["t"], "a": q["a"], "g": q["g"], "e": q["e"], "c": q["c"], "k": q["padrao"], "r": q["r"], "d": q["dif"], "p": q["ponto"]})
os.makedirs(os.path.join(OUT, "v3"), exist_ok=True)
json.dump(full, open(os.path.join(OUT, "v3", SIG.lower() + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(slim, open(os.path.join(OUT, SIG.lower() + "_banco.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(atoms, open(os.path.join(OUT, SIG.lower() + "_artigos.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(full), "questões;", sum(q["g"] == "C" for q in full), "C;", len(atoms), "átomos;", collections.Counter(q["padrao"] for q in full).most_common(6))
