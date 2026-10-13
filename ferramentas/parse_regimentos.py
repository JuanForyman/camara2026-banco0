"""Extrai artigos do RICD e do Regimento Comum a partir do texto do PDF (pdftotext -layout).
Uso: python3 -I parse_regimentos.py <ricd29.txt> <saida.json>
Saída: {"RICD": [artigo...], "RC": [artigo...], "meta": {...}}
artigo = {art, suf, estrutura, revogado, disp:[{loc, texto, nota, revogado}]}"""
import json
import re
import sys
from collections import Counter

src, out = sys.argv[1], sys.argv[2]
L = open(src, encoding="utf-8").read().split("\n")

HDR = re.compile(r"^\s*\d{0,3}\s*REGIMENTO (INTERNO DA C[ÂA]MARA DOS DEPUTADOS|COMUM DO CONGRESSO NACIONAL)\d*\s*\d{0,3}\s*$")
PAGE = re.compile(r"^\s*\d{1,3}\s*$")
HEAD = re.compile(r"^\s*(TÍTULO|CAPÍTULO|SEÇÃO|SUBSEÇÃO|Título|Capítulo|Seção|Subseção)\s+([IVXLC]+(?:-[A-Z])?|ÚNICO|ÚNICA)\s*(?:[–-]\s*(.*))?$")
ART = re.compile(r"^\s*Art\.\s*(\d+)\s*(?:º|°|o)?(?:-([A-Z]{1,2}))?\s*[\.\-–]?\s*(.*)$")
PAR = re.compile(r"^§\s*(\d+)\s*(?:º|°|o)?(?:-([A-Z]{1,2}))?\s*[\.\-–]?\s*(.*)$")
PU = re.compile(r"^Parágrafo único\.?\s*(.*)$")
INC = re.compile(r"^([IVXLC]+)(?:-([A-Z]{1,2}))?\s*[–-]\s*(.*)$")
ALI = re.compile(r"^([a-z])\)\s*(.*)$")
NOTE = re.compile(r"\((?:[^()]*?(?:Resolu[çc][ãa]o|Emenda|Ato da Mesa|Decreto|Revogad|Vetad|Parágrafo|Inciso|Alínea|Artigo|Caput)[^()]*)\)")


def region(start_pat, stop_after=None):
    s = next(i for i, l in enumerate(L) if re.match(start_pat, l))
    return s


# regiões (índices 0-based) determinadas pelo conteúdo
ricd_start = next(i for i, l in enumerate(L) if l.strip().startswith("Art. 1º A Câmara dos Deputados, com sede"))
etica_start = next(i for i, l in enumerate(L) if i > ricd_start + 4000 and l.strip().startswith("Art. 1º O Código de Ética"))
rc_start = next(i for i, l in enumerate(L) if l.strip().startswith("Art. 1º A Câmara dos Deputados e o Senado Federal, sob a direção"))
rc_end = next(i for i, l in enumerate(L) if i > rc_start and l.strip().startswith("Art. 1º Esta Resolução é parte integrante do Regimento Comum"))

# vocabulário para decidir hifenização de fim de linha
words_inline, words_hyph = Counter(), set()
for l in L:
    toks = re.findall(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)*", l)
    for t in toks[:-1] if l.rstrip().endswith("-") else toks:
        if "-" in t:
            words_hyph.add(t.lower())
        else:
            words_inline[t.lower()] += 1


def join_lines(a, b):
    a, b = a.rstrip(), b.strip()
    if a.endswith("-") and len(a) > 1 and a[-2].isalpha() and b[:1].isalpha():
        f1 = re.findall(r"[A-Za-zÀ-ÿ]+$", a[:-1])
        f2 = re.match(r"[A-Za-zÀ-ÿ]+", b)
        if f1 and f2:
            joined = (f1[0] + f2.group(0)).lower()
            hy = (f1[0] + "-" + f2.group(0)).lower()
            if words_inline.get(joined, 0) > 0 or hy not in words_hyph:
                return a[:-1] + b
            return a + b
    return a + " " + b


def parse(start, end):
    arts, cur, disp = [], None, None
    estr = {"T": "", "C": "", "S": "", "SS": ""}
    last = (0, "")
    par_ctx = "c"
    inc_ctx = None
    i = start
    while i < end:
        raw = L[i]
        i += 1
        if not raw.strip() or HDR.match(raw) or PAGE.match(raw):
            continue
        line = raw.strip()
        mh = HEAD.match(raw)
        if mh and not ART.match(raw):
            kind = {"TÍTULO": "T", "CAPÍTULO": "C", "SEÇÃO": "S", "SUBSEÇÃO": "SS"}[mh.group(1).upper()]
            title = (mh.group(3) or "").strip()
            j = i
            while j < end and (not title or title.endswith(",") or (L[j].strip() and L[j].strip().isupper() and not ART.match(L[j]) and not HEAD.match(L[j]) and len(L[j].strip()) < 80 and title.endswith(("DE", "DA", "DO", "E", "DAS", "DOS")))):
                nxt = L[j].strip()
                if nxt and nxt.isupper() and not ART.match(L[j]) and not HEAD.match(L[j]):
                    title = (title + " " + nxt).strip()
                    j += 1
                    i = j
                else:
                    break
            label = f"{mh.group(1)} {mh.group(2)}" + (f" – {title}" if title else "")
            order = ["T", "C", "S", "SS"]
            estr[kind] = label
            for k in order[order.index(kind) + 1:]:
                estr[k] = ""
            continue
        ma = ART.match(raw)
        if ma:
            n, suf = int(ma.group(1)), ma.group(2) or ""
            rest0 = ma.group(3).strip()[:1]
            ok = (n == last[0] and suf and suf > last[1]) or (
                last[0] < n <= last[0] + 40 and (rest0.isupper() or rest0 in "([")) or (last[0] == 0)
            if ok:
                last = (n, suf)
                cur = {"art": n, "suf": suf, "estrutura": " > ".join(v for v in estr.values() if v), "revogado": False, "disp": []}
                arts.append(cur)
                par_ctx, inc_ctx = "c", None
                disp = {"loc": "c", "texto": ma.group(3).strip()}
                cur["disp"].append(disp)
                continue
        if cur is None:
            continue
        m = PAR.match(line)
        if m:
            par_ctx = "p" + m.group(1) + (m.group(2) or "")
            inc_ctx = None
            disp = {"loc": par_ctx, "texto": m.group(3).strip()}
            cur["disp"].append(disp)
            continue
        m = PU.match(line)
        if m:
            par_ctx, inc_ctx = "pu", None
            disp = {"loc": "pu", "texto": m.group(1).strip()}
            cur["disp"].append(disp)
            continue
        m = INC.match(line)
        if m and (m.group(1) in {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"} or len(m.group(1)) > 1 or inc_ctx):
            inc_ctx = m.group(1) + (("-" + m.group(2)) if m.group(2) else "")
            disp = {"loc": f"{par_ctx}.{inc_ctx}", "texto": m.group(3).strip()}
            cur["disp"].append(disp)
            continue
        m = ALI.match(line)
        if m and inc_ctx:
            disp = {"loc": f"{par_ctx}.{inc_ctx}.{m.group(1)}", "texto": m.group(2).strip()}
            cur["disp"].append(disp)
            continue
        if disp is not None:
            disp["texto"] = join_lines(disp["texto"], line) if disp["texto"] else line
    # pós-processamento: notas de alteração e revogação
    for a in arts:
        for d in a["disp"]:
            notas = NOTE.findall(d["texto"])
            d["nota"] = " ".join(notas)
            t = d["texto"]
            for nt in notas:
                t = t.replace(nt, " ")
            d["texto"] = re.sub(r"\s+", " ", t).strip()
            d["revogado"] = bool(re.search(r"Revogad[oa]|Vetad[oa]", d["nota"] + " " + d["texto"][:30])) and len(d["texto"]) < 4
        a["revogado"] = all(d["revogado"] or not d["texto"] for d in a["disp"])
    return arts


ricd = parse(ricd_start - 3, etica_start)  # inclui TÍTULO I e CAPÍTULO I, que antecedem o art. 1º
rc = parse(rc_start - 2, rc_end)           # inclui TÍTULO I do Regimento Comum


def faltando(arts, lo, hi):
    have = {a["art"] for a in arts}
    return [n for n in range(lo, hi + 1) if n not in have]


meta = {
    "fonte": "Regimento Interno da Câmara dos Deputados, 29ª ed., Edições Câmara, 2025 (atualizada até 15/05/2025)",
    "linhas": {"ricd": [ricd_start + 1, etica_start], "rc": [rc_start + 1, rc_end]},
    "ricd_artigos": len(ricd), "ricd_max": max(a["art"] for a in ricd),
    "rc_artigos": len(rc), "rc_max": max(a["art"] for a in rc),
    "ricd_faltando": faltando(ricd, 1, max(a["art"] for a in ricd)),
    "rc_faltando": faltando(rc, 1, max(a["art"] for a in rc)),
}
json.dump({"RICD": ricd, "RC": rc, "meta": meta}, open(out, "w", encoding="utf-8"), ensure_ascii=False)
print(json.dumps(meta, ensure_ascii=False))


def blocos(arts, nome):
    print(f"-- estrutura {nome}")
    prev, ini = None, None
    for a in arts + [{"estrutura": None, "art": 0, "suf": ""}]:
        if a["estrutura"] != prev:
            if prev is not None:
                print(f"  arts. {ini}–{last_a}: {prev}")
            prev, ini = a["estrutura"], f'{a["art"]}{a["suf"]}'
        last_a = f'{a["art"]}{a["suf"]}'


blocos(rc, "RC")
