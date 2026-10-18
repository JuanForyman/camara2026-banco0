#!/usr/bin/env python3
"""Backup completo e idempotente do histórico do aluno.
Uso: python3 -I ferramentas/backup_dados.py <dump> [--push]
<dump> = pasta com estado/ eventos/ simulados/ (um JSON por doc, saída do ArtifactData)
         ou arquivo historico_camara2026.json exportado pelo botão do site.
Regras: eventos = união (nunca apaga); estado = o doc de maior 'u' vence; derivados são recalculados."""
import json,sys,os,glob,hashlib,math,collections,statistics,subprocess,datetime
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));B=R+'/backup';S=R+'/dados/site'
def J(p,d=None):
    try:return json.load(open(p,encoding='utf-8'))
    except Exception:return d
def W(p,o):
    os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,'w',encoding='utf-8').write(json.dumps(o,ensure_ascii=False,indent=1,sort_keys=True)+'\n')
def WL(p,rows):
    os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,'w',encoding='utf-8').write(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows))
def RL(p):
    try:return [json.loads(l) for l in open(p,encoding='utf-8') if l.strip()]
    except Exception:return []
def lerdump(a):
    est,ev,sim={},{},[]
    if os.path.isfile(a):
        d=json.load(open(a,encoding='utf-8'))
        est=d.get('estado') or {};sim=d.get('simulados') or []
        for i,e in enumerate(d.get('eventos') or []):ev['x%s-%s-%s'%(e.get('t'),e.get('q'),i) if 'id' not in e else e['id']]=e
        return est,ev,sim
    for f in glob.glob(a+'/estado/*.json'):est[os.path.basename(f)[:-5]]=J(f)
    for f in glob.glob(a+'/eventos/*.json'):ev[os.path.basename(f)[:-5]]=J(f)
    for f in glob.glob(a+'/simulados/*.json'):sim.append(J(f))
    return est,ev,sim
def wil(k,n,z=1.64):
    if not n:return None
    p=k/n;d=1+z*z/n;c=p+z*z/(2*n);a=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n));return round((c-a)/d,3)
def main():
    a=sys.argv[1];push='--push' in sys.argv
    est_n,ev_n,sim_n=lerdump(a)
    banco={q['id']:q for q in J(S+'/banco.json',[])};top=J(S+'/topicos.json',{});camp=J(S+'/campos.json',{})
    # ---- união com o que já existe (nunca perde histórico)
    ev={r['id']:r for r in RL(B+'/raw/eventos.jsonl')}
    for k,v in ev_n.items():
        if v:ev[k]=dict(v,id=k)
    est=J(B+'/raw/estado.json',{})
    for k,v in est_n.items():
        if v and (k not in est or (v.get('u') or 0)>=(est[k].get('u') or 0)):est[k]=v
    sim={s.get('id',str(s.get('t'))):s for s in J(B+'/raw/simulados.json',[])}
    for s in sim_n:
        if s:sim[s.get('id',str(s.get('t')))]=s
    evl=sorted(ev.values(),key=lambda e:(e.get('t') or 0,e['id']))
    WL(B+'/raw/eventos.jsonl',evl);W(B+'/raw/estado.json',est);W(B+'/raw/simulados.json',sorted(sim.values(),key=lambda s:s.get('t') or 0))
    # ---- enriquecimento
    def ctx(qid,tid=None):
        q=banco.get(qid,{});t=top.get(q.get('t') or tid,{})
        return q,{'topico':q.get('t') or tid,'topico_nome':t.get('t'),'materia':t.get('m'),'bloco':t.get('b'),'campo':q.get('f'),'campo_nome':camp.get(q.get('f')),'atomos':q.get('a') or [],'tipo':q.get('k'),'relevancia':q.get('r'),'artigos':[x.get('t') for x in q.get('s',[])]}
    visto=set();rich=[]
    for i,e in enumerate(evl):
        q,c=ctx(e.get('q'),e.get('top'))
        ts=e.get('t') or 0
        rich.append(dict(c,id=e['id'],quando=datetime.datetime.fromtimestamp(ts/1000,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') if ts else None,t=ts,questao=e.get('q'),resposta=e.get('r'),gabarito=e.get('g'),acertou=e.get('ok'),ms=e.get('ms'),confianca=e.get('cf'),modo=e.get('m'),primeira_vez=e.get('q') not in visto,ordem_global=i+1))
        visto.add(e.get('q'))
    por_mes=collections.defaultdict(list)
    for r in rich:por_mes[(r['quando'] or '0000-00')[:7]].append(r)
    for f in glob.glob(B+'/eventos/*.jsonl'):os.remove(f)
    for m,rs in por_mes.items():WL(B+'/eventos/%s.jsonl'%m,rs)
    # ---- snapshot de questões (estado + conteúdo)
    ev_q=collections.defaultdict(list)
    for r in rich:ev_q[r['questao']].append(r)
    qs={}
    for qid,s in est.items():
        q,c=ctx(qid);h=ev_q.get(qid,[])
        qs[qid]=dict(c,estado=s,enunciado=q.get('e'),gabarito_item=q.get('g'),regra_correta=q.get('c'),respostas=len(h),acertos=sum(1 for x in h if x['acertou']),ultima_correta=(h[-1]['acertou'] if h else None),sequencia=[int(bool(x['acertou'])) for x in h])
    W(B+'/estado/questoes.json',qs)
    erros=[dict(id=k,**{f:v[f] for f in('materia','topico','topico_nome','campo','atomos','artigos','enunciado','gabarito_item','regra_correta','respostas','acertos')}) for k,v in qs.items() if v['ultima_correta'] is False]
    WL(B+'/estado/erros_abertos.jsonl',erros)
    # ---- agregados
    def agg(key,multi=False):
        d=collections.defaultdict(list)
        for r in rich:
            ks=r[key] if multi else [r[key]]
            for k in (ks or []):
                if k:d[k].append(r)
        out={}
        for k,rs in d.items():
            n=len(rs);o=sum(1 for x in rs if x['acertou']);pv=[x for x in rs if x['primeira_vez']];ms=[x['ms'] for x in rs if x.get('ms') and x['ms']<18e4]
            out[k]=dict(n=n,acertos=o,erros=n-o,acerto=round(o/n,3),liquido=round((2*o-n)/n,3),liquido_pior_caso=(None if wil(o,n) is None else round(2*wil(o,n)-1,3)),primeira_vez_n=len(pv),primeira_vez_acerto=(round(sum(1 for x in pv if x['acertou'])/len(pv),3) if pv else None),questoes_distintas=len({x['questao'] for x in rs}),ms_mediano=(int(statistics.median(ms)) if ms else None),ultimo=max(x['t'] for x in rs),acerto_ultimas10=round(sum(1 for x in rs[-10:] if x['acertou'])/len(rs[-10:]),3))
        return out
    for nome,key,mu in[('por_materia','materia',0),('por_topico','topico',0),('por_campo','campo',0),('por_atomo','atomos',1),('por_tipo','tipo',0),('por_gabarito','gabarito',0),('por_modo','modo',0)]:W(B+'/analise/%s.json'%nome,agg(key,mu))
    dia=collections.defaultdict(list)
    for r in rich:dia[(r['quando'] or '')[:10]].append(r)
    W(B+'/analise/diario.json',{d:dict(n=len(rs),acertos=sum(1 for x in rs if x['acertou']),liquido=round((2*sum(1 for x in rs if x['acertou'])-len(rs))/len(rs),3),materias=dict(collections.Counter(x['materia'] for x in rs)),minutos_aprox=round(sum(min(x['ms'] or 0,18e4) for x in rs)/6e4,1)) for d,rs in dia.items() if d})
    cm={}
    for r in rich:
        if r['acertou'] is False and r['resposta']:
            cm[r['gabarito']+'->'+r['resposta']]=cm.get(r['gabarito']+'->'+r['resposta'],0)+1
    W(B+'/analise/confusao_CE.json',cm)
    # ---- manifesto
    arqs=sorted(p for p in glob.glob(B+'/**/*',recursive=True) if os.path.isfile(p) and not p.endswith('manifest.json'))
    W(B+'/manifest.json',{'esquema':1,'eventos':len(evl),'questoes_com_estado':len(est),'simulados':len(sim),'primeiro_evento':evl[0].get('t') if evl else None,'ultimo_evento':evl[-1].get('t') if evl else None,'sha256':{os.path.relpath(p,B):hashlib.sha256(open(p,'rb').read()).hexdigest()[:16] for p in arqs}})
    print('eventos',len(evl),'estado',len(est),'simulados',len(sim),'erros abertos',len(erros))
    if push:
        sh=lambda *c:subprocess.run(c,cwd=R,capture_output=True,text=True)
        sh('git','add','backup')
        if sh('git','diff','--cached','--quiet').returncode==0:print('sem mudanças');return
        msg='Backup do histórico: %d eventos, %d questões, %s'%(len(evl),len(est),datetime.date.today())
        r=sh('git','commit','-m',msg,'-m','Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01EX5y4xfnya3eeqkBKCywHK')
        print(r.stdout.strip().splitlines()[0] if r.stdout else r.stderr)
        p=sh('git','push');print('push',p.returncode,p.stderr.strip()[-200:])
main()
