"""Aplica fabrica/ingles/out/*.json ao banco: {id:{"tr":..., "c":..., "v":...}}.
tr = traducao pt-BR do item inteiro; c = explicacao (3-34 palavras, ** par); v = vocabulario (vira linha em s[0].l).
Uso: python3 -I ferramentas/lote_ingles.py aplicar | falta"""
import json,glob,sys,re
P='dados/site/banco.json'
def load(): return json.load(open(P,encoding='utf-8'))
def falta():
    b=load(); f=[q['id'] for q in b if q['t'].startswith('P1-M2') and not q.get('tr')]
    print(len(f),'sem traducao'); return f
if sys.argv[1]=='falta':
    f=falta(); print(f[:5])
else:
    b=load(); by={q['id']:q for q in b}; ok=rej=0
    for fn in sorted(glob.glob('fabrica/ingles/out/*.json')):
        for i,d in json.load(open(fn,encoding='utf-8')).items():
            q=by.get(i); tr=d.get('tr','').strip(); c=d.get('c','').strip(); v=d.get('v','').strip()
            n=len(c.replace('**','').split())
            if not q or not tr or c.count('**')%2 or not 3<=n<=34 or c.endswith('…'):
                print('rejeitado',i,n); rej+=1; continue
            q['tr']=tr; q['c']=c
            if q.get('s'):
                l=[x for x in q['s'][0]['l'] if not x.startswith('Vocabulário:')]
                if v: l.append('Vocabulário: '+v)
                q['s'][0]['l']=l
            ok+=1
    json.dump(b,open(P,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    print('aplicados',ok,'rejeitados',rej)
