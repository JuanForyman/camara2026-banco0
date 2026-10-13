"""cf.txt (pdftotext -layout da CF, ed. Câmara/CDI) -> cf_texto.json {art:[linhas]} (somente artigos 1..250 do corpo permanente)"""
import re, json, sys
L = open(sys.argv[1], encoding="utf-8").read().split("\n")
arts, cur, started, last = {}, None, False, 0
for ln in L:
    s = ln.strip()
    if "ATO DAS DISPOSIÇÕES CONSTITUCIONAIS TRANSITÓRIAS" in s and started and last >= 240: break
    m = re.match(r"Art\. (\d+)(?:º|°|\.)?\s+(?!-)(.*)", s)
    if m and not re.match(r"Art\. \d+-[A-Z]", s):
        n = int(m.group(1))
        if n == last + 1 or (n == 1 and not started):
            cur = n; last = n; started = True; arts[n] = [s]; continue
    if cur and s and not re.match(r"^(TÍTULO|CAPÍTULO|SEÇÃO|Seção|Subseção)", s): arts[cur].append(s)
# junta linhas quebradas
out = {}
for n, ls in arts.items():
    items = []
    for s in ls:
        if re.match(r"(Art\.|§|Parágrafo único|[IVXLC]+ -|[a-z]\))", s) or not items: items.append(s)
        else: items[-1] += " " + s
    out[n] = items
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "artigos; último", max(out)); print([n for n in range(1, max(out)+1) if n not in out][:20])
