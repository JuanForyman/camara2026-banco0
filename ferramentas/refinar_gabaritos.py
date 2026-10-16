"""Fase A: refaz gabarito (c) e monta o trecho do "Saiba mais" (s) para questões fundamentadas em lei/regimento.
Saída: dados/gabaritos_v2.json  {id: {"c": ..., "s": [{"t": titulo, "c": cabeça, "l": [linhas]}]}}
Uso: python3 -I ferramentas/refinar_gabaritos.py [--aplicar]   (--aplicar grava c/s em dados/site/banco.json)"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from dispositivo import *

LAW = re.compile(r"^A-(CF|RICD|RC|L8112|L8429|L9784|L12527|L13709|L14133|D9203)-(\d+)([A-Z]*)(?:\.([IVXLC]+))?$")
raiz = os.path.join(os.path.dirname(__file__), "..")
B = json.load(open(f"{raiz}/dados/site/banco.json", encoding="utf-8"))
A = json.load(open(f"{raiz}/dados/site/artigos.json", encoding="utf-8"))

def label(n):
    if n["sc"] == "pu" and n["inc"] is None and n["ali"] is None: return "Parágrafo único."
    if n["sc"].startswith("§") and n["inc"] is None and n["ali"] is None: return "§ " + n["sc"][1:] + "º"
    if n["ali"]: return n["ali"] + ")"
    if n["inc"]: return n["inc"] + " –"
    return ""
def line(n): return (label(n) + " " + n["t"]).strip()

def bloco(q, atom):
    m = LAW.match(atom)
    if not m or atom not in A: return None
    num = int(m.group(2)); a = A[atom]; nodes = parse_nodes(a["x"])
    ar, head = art_head(q["c"], num)
    sels = parse_tokens(head) if ar else []
    stems, sel = select(nodes, sels) if sels else ([], [])
    modo = "ref"
    if not sel:
        tot = sum(len(n["t"].split()) for n in nodes)
        if tot <= 90 or (sels and all(s["sc"] == "caput" and not s["incs"] for s in sels)) and len(nodes) == 1:
            sel, stems, modo = nodes, [], "inteiro"
        else:
            sel = overlap(nodes, q["e"]); modo = "sobreposicao"
            if sel and any(n["inc"] or n["ali"] for n in sel): stems = [nodes[0]]
            if not sel: sel, stems, modo = nodes[:1], [], "caput"
    if modo != "ref" and sel and sel[0]["sc"] != "caput" and not stems and nodes[0]["sc"] == "caput" and len(sel) < len(nodes):
        stems = [nodes[0]]
    st = trim(stems[0]["t"], 25) if stems else ""
    return {"t": a["t"], "c": st, "l": [trim(line(n), 70) for n in sel][:8], "modo": modo, "sel": sel, "stems": stems}

def bare(c):
    """True se o gabarito atual é só referência/etiqueta (sem explicação)."""
    resto = re.sub(r"(CF|RC|RICD|Lei [\d./]+)?,?\s*[Aa]rts?\.?\s*[\d\w.º°\-–, §e]*?(caput|p\.ú\.|parágrafo único|[IVXLC]+|[a-z]\b)*", "", c)
    return len(c.split()) <= 9 and ":" not in c or len(re.sub(r"[\W\d]+", " ", resto).split()) <= 3

def refstr(q, blocos):
    c = q["c"].strip()
    m = re.search(r"[Aa]rts?\.?\s*\d", c)
    if not m: return blocos[0]["t"]
    r = re.split(r"[:;—(]", c)[0].strip().rstrip(".,")
    return re.sub(r"^art", "Art", r)

def principal(q, bl):
    m = re.search(r"[Aa]rts?\.?\s*(\d+)", q["c"])
    if m:
        for i, b in enumerate(bl):
            if re.search(r"art\.?\s*" + m.group(1) + r"\b", b["t"]) or b["t"].endswith(" " + m.group(1)): return i
    return 0

def citacao(b):
    sel = b["sel"]; txt = []
    st = b["c"].rstrip(":") if b["c"] and len(b["c"].split()) <= 10 and any(n["inc"] or n["ali"] for n in sel) else ""
    for n in sel[:2]: txt.append(trim(n["t"].rstrip(";"), 26 if len(sel) == 1 else 20))
    q = "; ".join(txt)
    if len(sel) > 2: q += " […]"
    return (st + ": " if st else "") + q

out = {}; est = {"leis": 0, "mantidos": 0, "gerados": 0, "modos": {}}
for q in B:
    at = q.get("a", [])
    if not at or not all(LAW.match(x) for x in at): continue
    est["leis"] += 1
    bl = [bloco(q, x) for x in at]
    if any(b is None for b in bl): continue
    s = [{"t": b["t"], "c": b["c"], "l": b["l"]} for b in bl]
    for b in bl: est["modos"][b["modo"]] = est["modos"].get(b["modo"], 0) + 1
    ip = principal(q, bl); s = [s[ip]] + s[:ip] + s[ip+1:]
    multi = bool(re.search(r"[Aa]rts?\.[^;:]*;\s*(?:[Aa]rts?\.|\d)", q["c"])) or len(at) > 1 and bool(re.search(r"[Aa]rts?\.[^:]*\be\b[^:]*\d", q["c"].split(":")[0]))
    rem = q["c"].split(":", 1)[1].strip() if ":" in q["c"] else ""
    nrem = len(rem.split())
    if nrem >= 5:
        c = q["c"]; est["mantidos"] += 1
    elif multi and len(bl) > 1:
        c = "; ".join(f"{b['t']}: {trim(citacao(b).rstrip(':').strip(), 22)}" for b in bl[:2])
        est["gerados"] += 1
    elif multi:
        c = q["c"]; est["mantidos"] += 1
    else:
        r = refstr(q, bl); cit = citacao(bl[ip]).rstrip(":").strip()
        c = f"{r}: {cit}"
        if nrem >= 2 and re.sub(r"\W+", "", rem.lower()) not in re.sub(r"\W+", "", cit.lower()):
            c += (" " if c.endswith((".", "…")) else ". ") + "Atenção: " + rem
        est["gerados"] += 1
    out[q["id"]] = {"c": c, "s": s}
json.dump(out, open(f"{raiz}/dados/gabaritos_v2.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(est, len(out))
if "--aplicar" in sys.argv:
    for q in B:
        if q["id"] in out: q["c"] = out[q["id"]]["c"]; q["s"] = out[q["id"]]["s"]
    json.dump(B, open(f"{raiz}/dados/site/banco.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("aplicado")
