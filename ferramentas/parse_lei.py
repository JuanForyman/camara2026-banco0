"""Texto de lei (pdftotext -layout do Planalto) -> {art(str, ex. '54' ou '69A'): [itens]}. Uso: parse_lei.py in.txt out.json"""
import re, json, sys
L = open(sys.argv[1], encoding="utf-8").read()
L = re.sub(r"\((?:Redação dada|Incluíd[oa]|Vide|Regulamento|Revogad|Vigência|Renumerad|Promulgação)[^()]*\)", "", L)
cur, out = None, {}
for ln in L.split("\n"):
    s = ln.strip()
    if not s or re.fullmatch(r"\d+", s): continue
    m = re.match(r"Art\. (\d+)(?:º|o|°|\.)?(?:-([A-Z]))?\.?\s+(.*)", s)
    if m:
        cur = m.group(1) + (m.group(2) or ""); out[cur] = [f"Art. {m.group(1)}{'-'+m.group(2) if m.group(2) else ''} {m.group(3)}"]; continue
    if re.match(r"(CAPÍTULO|TÍTULO|SEÇÃO|Seção|DAS?|DOS?|Brasília)", s) and s.upper() == s or s.startswith("Brasília"): continue
    if cur:
        if re.match(r"(§ ?\d+|Parágrafo único|[IVXLC]+ ?[-–]|[a-z]\))", s) or not out[cur]: out[cur].append(s)
        else: out[cur][-1] += " " + s
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "artigos")
