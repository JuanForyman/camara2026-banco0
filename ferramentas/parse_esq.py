"""Lei esquematizada (pdftotext -layout; texto legal em coluna 0, comentários indentados) -> {art:[itens]}.
Uso: parse_esq.py in.txt out.json"""
import re, json, sys
L = open(sys.argv[1], encoding="utf-8").read().replace("\f", "\n")
L = re.sub(r"\((?:Redação dada|Incluíd[oa]|Vide|Regulamento|Revogad|Vigência|Renumerad|Promulgação|Vetado|Acrescid)[^()]*\)", "", L, flags=re.S)
STRUCT = re.compile(r"(§ ?\d+|Parágrafo único|[IVXLC]+( e [IVXLC]+)? ?[-–]|[a-z]\) |\d+\) )")
cur, out, prev_blank, open_ = None, {}, True, False
for ln in L.split("\n"):
    if not ln.strip(): prev_blank = True; continue
    col0 = not ln.startswith(" ")
    s = ln.strip()
    blank, prev_blank = prev_blank, False
    if re.search(r"www\.estrategiaconcursos|^Profs?\. .*\d+ de \d+$|^Profs?\. [A-Z ]+ e [A-Z ]+$|^Lei 8\.112/90 – Atualizada", s): prev_blank = blank; continue
    m = re.match(r"Art\. (\d+)(?:º|o|°|\.)?(?:-([A-Z]))?\.?\s+(.*)", s) if col0 else None
    if m:
        k = m.group(1) + (m.group(2) or "")
        if k in out: cur = None; continue
        cur = k; out[cur] = [f"Art. {m.group(1)}{'-'+m.group(2) if m.group(2) else ''} {m.group(3)}"]; continue
    if not col0 or cur is None: 
        if not col0: cur = cur if False else cur
        if not col0: open_ = False
        continue
    if STRUCT.match(s): out[cur].append(s); continue
    if re.fullmatch(r"(Prof\. Antonio Daud|@professordaud)", s): prev_blank = blank; continue
    if not blank or (s[0].islower() and not re.search(r"[.;:]$", out[cur][-1].rstrip())): out[cur][-1] += " " + s
    else: continue   # texto solto em coluna 0 apos branco = comentario/titulo (ignorado)
out = {k: v for k, v in out.items() if not re.search(r"^Art\. \S+\s*\(?\s*(Revogado|Vetado)", v[0]) and len(" ".join(v)) > 25}
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "artigos")
