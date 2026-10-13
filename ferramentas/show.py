import json,sys,re
f=json.load(open('fontes_29ed.json'))
norma,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
for x in f[norma]:
    if a<=x['art']<=b and not x['revogado']:
        print(f"## {norma} {x['art']}{x['suf']}")
        for d in x['disp']:
            t=re.sub(r'\s+',' ',d['texto'])
            print(f"[{d['loc']}] {t[:300]}")
