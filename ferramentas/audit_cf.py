import json,re,glob,runpy,sys
T=json.load(open('cf_texto.json'))
NW={"um":1,"uma":1,"dois":2,"duas":2,"três":3,"quatro":4,"cinco":5,"seis":6,"sete":7,"oito":8,"nove":9,"dez":10,"onze":11,"doze":12,"quinze":15,"vinte":20,"trinta":30,"quarenta":40,"cinquenta":50,"sessenta":60,"setenta":70,"noventa":90,"cem":100,"cento":100,"terça":3,"terço":3,"quinto":5,"quintos":5,"décimo":10,"décimos":10,"metade":2}
def nums(t):
    t=t.lower(); s=set(re.findall(r"\d+",t))
    for w in re.findall(r"[a-zçêéãí]+",t):
        if w in NW:s.add(str(NW[w]))
    return s
def body(a):
    m=re.match(r"(\d+)(?:\.([IVXLC]+))?$",a); n=m.group(1)
    its=T[n]
    if m.group(2): its=[x for x in its if x.startswith(m.group(2)+" -")]
    return " ".join(its)
bad=0
for f in sorted(glob.glob('/home/claude/camara2026-banco0/ferramentas/nq_cf/c*.py')):
  for (top,arts,g,tx,com,tipo) in runpy.run_path(f)["Q"]:
    if not arts: continue
    b=" ".join(body(a) for a in arts)
    hv=nums(b)|{str(int(a.split('.')[0])) for a in arts}
    want=nums(tx) if g=="C" else nums(re.sub(r"^Art\. \d+[^:]*:","",com))
    miss=sorted(x for x in want-hv if x not in {"1","2"} or g=="C")
    miss=[x for x in miss if not (g=="E" and x in nums(tx))]
    if miss: bad+=1; print(g,arts,miss,"|",tx[:90],"||",com[:80])
print("alertas",bad)
