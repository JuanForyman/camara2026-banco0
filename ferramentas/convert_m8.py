"""Converte o conteúdo do artefato M8 para schema v2 (átomos por artigo + questões) e gera taxonomia.
Uso: python3 -I convert_m8.py <m8_extract.json> <fontes_29ed.json> <mapa_topicos.json> <outdir>"""
import json, re, sys, hashlib, collections
ext, fon, mapa, out = sys.argv[1:5]
o = json.load(open(ext)); f = json.load(open(fon)); rows = json.load(open(mapa))["rows"]

# ---------- taxonomia ----------
M8_FINE = {  # id fino -> (título, norma, faixa)
 "2.1": ("RICD arts. 25–31", "RICD", (25,31)), "2.2": ("RICD arts. 32–38", "RICD", (32,38)),
 "2.3": ("RICD arts. 39–48", "RICD", (39,48)), "2.4": ("RICD arts. 49–59", "RICD", (49,59)),
 "2.5": ("RICD arts. 60–64", "RICD", (60,64)), "2.6": ("RICD arts. 95–99", "RICD", (95,99)),
 "2.7": ("RICD arts. 100–112", "RICD", (100,112)), "2.8": ("RICD arts. 113–125", "RICD", (113,125)),
 "2.9": ("RICD arts. 126–150", "RICD", (126,150)), "2.10": ("RICD arts. 151–164", "RICD", (151,164)),
 "2.11": ("RICD arts. 165–200", "RICD", (165,200)),
 "3.1": ("RC arts. 1–8", "RC", (1,8)), "3.2": ("RC arts. 9–21", "RC", (9,21)),
 "3.3": ("RC arts. 22–35", "RC", (22,35)), "3.4": ("RC arts. 36–52", "RC", (36,52)),
 "3.5": ("RC arts. 53–71", "RC", (53,71)),
}
P1_RANGES = [("RICD",(1,24),"P1-M4-7.1"),("RICD",(65,94),"P1-M4-7.2"),("RICD",(226,251),"P1-M4-7.3"),
             ("RICD",(262,273),"P1-M4-7.4"),("RC",(1,3),"P1-M4-8.1"),("RC",(53,71),"P1-M4-8.2"),("RC",(72,103),"P1-M4-8.2")]
tax = []
for r in rows:
    tax.append({"id": r["id"], "bloco": r["bloco"], "materia": r["materia"], "materia_nome": r["materia_nome"],
                "edital_item": r["item"], "titulo": r["titulo"], "peso": None, "peso_status": "estimado_uniforme"})
for k, (t, n, rg) in M8_FINE.items():
    tax.append({"id": f"P2-M8-{k}", "bloco": "P2", "materia": 8, "pai": ("P2-M8-2.1" if k.startswith("2") else "P2-M8-3.1"),
                "titulo": t, "norma": n, "faixa": list(rg)})
tax.append({"nota": "M7 do Painel tem 25 tópicos de curso vs 23 subitens do edital (edital 3.x dividido em 3.1–3.6): mapear via edital_ref em B-003b."})

# ---------- átomos ----------
def norm_txt(s): return re.sub(r"\s+", " ", s).strip()
atoms, byk = [], {}
def topics_for(norma, n):
    t = []
    for k, (_, nn, (a, b)) in M8_FINE.items():
        if nn == norma and a <= n <= b: t.append(f"P2-M8-{k}")
    for nn, (a, b), tid in P1_RANGES:
        if nn == norma and a <= n <= b: t.append(tid)
    return t
for norma in ("RICD", "RC"):
    for a in f[norma]:
        tp = topics_for(norma, a["art"])
        full = norm_txt(" ".join(d["texto"] for d in a["disp"]))
        rec = {"id": f"A-{norma}-{a['art']:04d}{a['suf']}", "norma": norma, "art": a["art"], "suf": a["suf"],
               "estrutura": a["estrutura"], "vigente": not a["revogado"], "n_disp": len(a["disp"]),
               "hash": hashlib.sha1(full.encode()).hexdigest()[:10], "chars": len(full),
               "ancora": full[:140], "topicos": tp, "tier": "A" if tp and not a["revogado"] else None}
        atoms.append(rec); byk[(norma, a["art"], a["suf"])] = (rec, full)
# ---------- questões ----------
NUMW = {"um":1,"uma":1,"dois":2,"duas":2,"três":3,"quatro":4,"cinco":5,"seis":6,"sete":7,"oito":8,"nove":9,"dez":10,"onze":11,"doze":12,"quinze":15,"vinte":20,"trinta":30,"quarenta":40,"cinquenta":50,"sessenta":60,"noventa":90,"cem":100}
def cites(s):
    res = []; norma = "RICD"
    for seg in str(s).split(";"):
        if re.search(r"\bRC\b|Regimento Comum", seg): norma = "RC"
        elif re.search(r"\bCF\b|Constitui", seg): norma = "CF"
        elif "RICD" in seg: norma = "RICD"
        elif re.search(r"\bLC\b|\bLei\b|Res\.", seg): norma = "OUTRA"
        seg2 = re.sub(r"§§?\s*\d+º?(?:\s*(?:,|e|a)\s*\d+º?)*", " ", seg)
        for m in re.finditer(r"arts?\.?\s*((?:\d+º?(?:-[A-Z])?(?:\s*(?:,|e|a)\s*(?=\d))?)+)", seg2, re.I):
            toks = re.findall(r"(\d+)º?(-[A-Z])?|\b(a)\b", m.group(1)); prev = None; rng = False
            for n, sf, a_ in toks:
                if a_: rng = True; continue
                n = int(n)
                if rng and prev is not None and prev <= n <= prev + 120: res += [(norma, k, "") for k in range(prev, n + 1)]
                else: res.append((norma, n, (sf or "")[1:]))
                rng = False; prev = n
    return list(dict.fromkeys(res))
def numbers(tx):
    ns = set(re.findall(r"\d+", tx))
    ns |= {str(NUMW[w]) for w in re.findall(r"[a-zçêé]+", tx.lower()) if w in NUMW}
    ns |= {str(int(x) // 1) for x in re.findall(r"\b(\d+)º", tx)}
    return ns
qs, problemas = [], collections.Counter()
for it in o["ITEMS"]:
    cs = cites(it["art"]); ids, ext_ = [], []
    for norma, n, sf in cs:
        if norma in ("RICD", "RC"):
            if (norma, n, sf) in byk: ids.append(byk[(norma, n, sf)][0]["id"])
            else: problemas["artigo_inexistente_no_texto"] += 1; ext_.append(f"{norma} art. {n}{sf} (não achado)")
        else: ext_.append(f"{norma} art. {n}")
    chk = {"artigos_existem": True, "vigentes": True, "numeros_ancorados": None}
    texts = " ".join(byk[(nm, n, sf)][1] for nm, n, sf in cs if (nm, n, sf) in byk)
    if any(e.endswith("(não achado)") for e in ext_): chk["artigos_existem"] = False
    for nm, n, sf in cs:
        if (nm, n, sf) in byk and not byk[(nm, n, sf)][0]["vigente"]: chk["vigentes"] = False
    if texts and it["r"]:
        low = texts.lower(); words = {str(NUMW[w]) for w in re.findall(r"[a-zçêé]+", low) if w in NUMW}
        have = set(re.findall(r"\d+", low)) | words
        missing = sorted(n for n in numbers(it["tx"]) if n not in have and not re.fullmatch(r"(19|20)\d\d", n))
        chk["numeros_ancorados"] = not missing
        if missing: chk["numeros_sem_ancora"] = missing
    for k, v in chk.items():
        if v is False: problemas[k] += 1
    qs.append({"id": f"Q-M8-{it['id']}", "tipo": "CE", "topico": it["t"], "atomos": ids, "externos": ext_,
               "enunciado": it["tx"], "gabarito": "C" if it["r"] else "E", "comentario": it["com"],
               "erro_tipo": it["e"], "citacao": it["art"], "origem": "artefato-M8" + ("-cf" if it["src"] == "cf" else ""),
               "validada": False, "checks": chk})
cob = collections.Counter(a for q in qs for a in q["atomos"])
for a in atoms: a["n_questoes"] = cob.get(a["id"], 0)
lac = [a["id"] for a in atoms if a["tier"] and a["n_questoes"] == 0]
rel = {"atomos_total": len(atoms), "atomos_alvo_tierA": sum(1 for a in atoms if a["tier"]),
       "atomos_alvo_sem_questao": len(lac), "questoes": len(qs), "problemas": dict(problemas),
       "C": sum(q["gabarito"] == "C" for q in qs), "E": sum(q["gabarito"] == "E" for q in qs),
       "sem_questao_por_topico": dict(collections.Counter(t for a in atoms if a["id"] in set(lac) for t in a["topicos"]))}
j = lambda p, d: open(f"{out}/{p}", "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, separators=(",", ":")))
j("taxonomia.json", tax); j("atomos_regimentos.json", {"fonte": f["meta"]["fonte"], "atomos": atoms})
j("questoes_regimentos.json", {"schema": "v2", "questoes": qs}); j("relatorio_cobertura.json", {**rel, "lacunas": lac})
print(json.dumps(rel, ensure_ascii=False, indent=1))
