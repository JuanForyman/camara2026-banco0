"""Lei esquematizada (Herbert Almeida; pdftotext -layout): texto legal em coluna 0-3, comentários após 'Comentários:' com ▪ indentado.
Uso: parse_esq2.py in.txt out.json"""
import re, json, sys
L = open(sys.argv[1], encoding="utf-8").read().replace("\f", "\n")
L = re.sub(r"\((?:Redação dada|Incluíd[oa]|Vide|Regulamento|Revogad|Vigência|Renumerad|Promulgação|Vetado|Acrescid|Atualizad)[^()]*\)", "", L, flags=re.S)
STRUCT = re.compile(r"(§ ?\d+[º°o]?|Parágrafo único|[IVXLC]+( e [IVXLC]+)? ?[-–—]|[a-z]\) |\d+\) )")
ART = re.compile(r"Art\. (\d+)(?:º|o|°|\.)?(?:-([A-Z]))?\.?\s+(.*)")
out, cur, comment, blank = {}, None, False, True
for ln in L.split("\n"):
    s = ln.strip()
    if not s: blank = True; continue
    ind = len(ln) - len(ln.lstrip()); b, blank = blank, False
    if re.fullmatch(r"\d{1,3}", s) or re.search(r"estrategiaconcursos|herbertalmeida|Prof\. Herbert|Esquematizada", s): blank = b; continue
    if s.startswith("Comentários") or s.startswith("Comentário"): comment = True; continue
    if s.startswith("▪") or s.startswith("•"):
        comment = True; continue
    m = ART.match(s) if ind <= 1 else None
    if m and not s.endswith("[...]"):
        k = m.group(1) + (m.group(2) or "")
        comment = False
        if k in out: cur = None; continue
        cur = k; out[cur] = [f"Art. {m.group(1)}{'-'+m.group(2) if m.group(2) else ''} {m.group(3)}"]; continue
    if cur is None: continue
    if comment:
        if ind <= 1 and (STRUCT.match(s)):
            comment = False; out[cur].append(s)
        elif ind <= 1 and b and s[0].isupper() and False: pass
        continue
    if ind > 3: continue
    if STRUCT.match(s): out[cur].append(s); continue
    if not b or (s[0].islower() and not re.search(r"[.;:]$", out[cur][-1].rstrip())): out[cur][-1] += " " + s
out = {k: v for k, v in out.items() if not re.search(r"^Art\. \S+\s*\(?\s*(Revogado|Vetado)", v[0]) and len(" ".join(v)) > 25}
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "artigos")
