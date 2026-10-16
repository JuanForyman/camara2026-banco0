"""Localiza o dispositivo exato (caput, § , inciso, alínea) que fundamenta uma questão e monta
(a) o trecho para o "Saiba mais" e (b) a transcrição curta para o gabarito.
Uso interno de refinar_gabaritos.py."""
import re

ROM = "IVXLC"
def rom2int(s):
    v = {"I":1,"V":5,"X":10,"L":50,"C":100}; t = 0
    for i, ch in enumerate(s):
        t += -v[ch] if i+1 < len(s) and v[ch] < v[s[i+1]] else v[ch]
    return t

def trim(s, n):
    w = s.split()
    return s if len(w) <= n else " ".join(w[:n]).rstrip(",;:") + "…"

def parse_nodes(lines):
    """Retorna lista de nós: {'sc': escopo ('caput','pu','§N'), 'inc': 'XXVII'|None, 'ali': 'a'|None, 't': texto}"""
    nodes = []; scope = "caput"; inc = None
    for i, l in enumerate(lines):
        l = l.strip()
        if not l: continue
        if i == 0:
            m = re.match(r"^Art\.?\s*\d+[º°o.]*(?:-[A-Z])?\s*[-–—]?\s*(.*)$", l)
            nodes.append({"sc": "caput", "inc": None, "ali": None, "t": (m.group(1) if m else l) or l}); continue
        m = re.match(r"^§\s*(\d+)\s*[°ºo.]?\s*[-–—]?\s*(.*)$", l)
        if m: scope = "§" + m.group(1); inc = None; nodes.append({"sc": scope, "inc": None, "ali": None, "t": m.group(2)}); continue
        if re.match(r"^Parágrafo único", l, re.I):
            scope = "pu"; inc = None; nodes.append({"sc": scope, "inc": None, "ali": None, "t": re.sub(r"^Parágrafo único\.?\s*", "", l, flags=re.I)}); continue
        m = re.match(r"^([IVXLC]+)\s*[–\-—]\s*(.*)$", l)
        if m: inc = m.group(1); nodes.append({"sc": scope, "inc": inc, "ali": None, "t": m.group(2)}); continue
        m = re.match(r"^([a-z])\)\s*(.*)$", l)
        if m: nodes.append({"sc": scope, "inc": inc, "ali": m.group(1), "t": m.group(2)}); continue
        nodes[-1]["t"] += " " + l   # continuação
    return nodes

def art_head(c, num):
    """Recorta de c o trecho de referência (após 'Art. N') da norma/atom numerado `num` (int)."""
    for m in re.finditer(r"[Aa]rts?\.?\s*(\d+)[º°o.]*(?:-[A-Z])?", c):
        if int(m.group(1)) == num:
            rest = c[m.end():]
            head = re.split(r"[:;—(]| - |\.\s+[A-ZÀ-Ú]|\.$", rest)[0]
            return m.group(0).strip(), head
    return None, ""

def parse_tokens(head):
    """Converte 'cabeça' da referência em seleções: lista de dicts {sc, incs[], alis[]}"""
    h = head.replace("p.ú.", "pu").replace("parágrafo único", "pu").replace("Parágrafo único", "pu")
    h = re.sub(r"(\d)[º°o.]+", r"\1", h)
    toks = re.findall(r"caput|pu|§§?|\d+|[IVXLC]+(?![a-zà-ú])|\b[a-z]\b|,|\be\b|\ba\b", h)
    sels = []; cur = None; i = 0
    def new(sc):
        d = {"sc": sc, "incs": [], "alis": [], "range": False}; sels.append(d); return d
    while i < len(toks):
        t = toks[i]
        if t == "caput": cur = new("caput")
        elif t == "pu": cur = new("pu")
        elif t in ("§", "§§"):
            nums = []; j = i+1
            while j < len(toks) and (toks[j].isdigit() or toks[j] in (",", "e", "a")):
                if toks[j].isdigit(): nums.append(toks[j])
                j += 1
            for n in nums: cur = new("§" + n)
            i = j; continue
        elif re.fullmatch(r"[IVXLC]+", t):
            if cur is None: cur = new("caput")
            if i >= 1 and toks[i-1] == "a" and cur["incs"]: cur["range"] = True
            cur["incs"].append(t)
        elif re.fullmatch(r"[a-z]", t) and t not in ("e", "a"):
            if cur is not None and cur["incs"]: cur["alis"].append(t)
        i += 1
    return sels

def select(nodes, sels):
    """Devolve (stem, [linhas selecionadas]) com os nós indicados. Vazio se nada casou."""
    out = []; stems = []
    for s in sels:
        sc = s["sc"]
        scope_nodes = [n for n in nodes if n["sc"] == sc]
        if not scope_nodes: continue
        head = scope_nodes[0] if scope_nodes[0]["inc"] is None and scope_nodes[0]["ali"] is None else None
        if s["incs"]:
            incs = s["incs"]
            if s["range"] and len(incs) >= 2:
                a, b = rom2int(incs[0]), rom2int(incs[-1])
                pool = [n for n in scope_nodes if n["inc"] and n["ali"] is None and a <= rom2int(n["inc"]) <= b]
            else:
                pool = [n for n in scope_nodes if n["inc"] in incs and n["ali"] is None]
            if not pool: continue
            if head: stems.append(head)
            for n in pool:
                out.append(n)
                kids = [k for k in scope_nodes if k["inc"] == n["inc"] and k["ali"]]
                if s["alis"]:
                    out.extend([k for k in kids if k["ali"] in s["alis"]])
                elif len(kids) <= 4 and not s["range"]:
                    out.extend(kids)
        else:
            if head: out.append(head)
            if sc.startswith("§") or sc == "pu":
                kids = [k for k in scope_nodes if k["inc"] and k["ali"] is None]
                if 0 < len(kids) <= 3: out.extend(kids)
    return stems, out

STOP = set("para pelo pela pelos pelas sobre entre quando como mais cujo cuja será serão podem pode deve devem este esta esses essas aquele aquela seus suas desde até apenas somente mesmo qualquer todos todas outros outras nos nas dos das num numa uma uns umas que com sem por dos das ser são foi não nem também ainda após antes durante conforme segundo".split())
def words(s): return {w for w in re.findall(r"[a-zà-ú]{4,}", s.lower()) if w not in STOP}

def overlap(nodes, e):
    q = words(e); sc = []
    for idx, n in enumerate(nodes):
        s = len(q & words(n["t"]))
        if s >= 2: sc.append((s, -idx, idx))
    sc.sort(reverse=True)
    return [nodes[i] for _, _, i in sorted(sc[:2], key=lambda x: x[2])]

def render(nodes_sel, stems, whole_len=None):
    """texto da citação: stem (≤14 palavras) + linhas"""
    st = trim(stems[0]["t"], 14).rstrip(":") + ":" if stems else ""
    return st, [n["t"] for n in nodes_sel]
