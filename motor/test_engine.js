const M = require("./engine.js"); const DAY = M.DAY;
const Q = [
 {id:"q1",t:"T1",a:["A1"],g:"C"},{id:"q2",t:"T1",a:["A1"],g:"E"},{id:"q3",t:"T1",a:["A2"],g:"C"},
 {id:"q4",t:"T2",a:["A3"],g:"C"},{id:"q5",t:"T2",a:[],g:"E"}];
const t0 = Date.now();
let ev = [];
const assert = (c, m) => { if (!c) { console.error("FALHA:", m); process.exit(1); } };
// sem eventos: tudo novo, prioridade igual -> pick devolve algo
let r = M.pick(Q, ev, t0); assert(r && r.motivo === "nova", "pick novo");
// erro recente em A1 deve virar prioridade
ev.push({q:"q1",ok:false,t:t0-1000});
let f = M.fila(Q, ev, t0, 5); assert(f[0].a === "A1" && f[0].motivo === "você errou por último", "erro vira topo: " + JSON.stringify(f[0]));
// acertos em sequência afastam a revisão
ev = [{q:"q1",ok:true,t:t0-3*DAY},{q:"q2",ok:true,t:t0-2*DAY},{q:"q1",ok:true,t:t0-1*DAY}];
const A = M.build(ev, Q); assert(A.A1.streak === 3 && M.urgency(A.A1, t0) < 1, "intervalo");
// teto: uma resposta certa nunca passa de 0.75
const one = M.build([{q:"q3",ok:true,t:t0}], Q); assert(M.pAtom(one.A2, t0).p <= 0.75, "teto");
// preparo líquido cresce com acertos
const r0 = M.readiness(Q, [], t0).geral, r1 = M.readiness(Q, ev, t0).geral;
assert(r0 === 0 && r1 > 0, "readiness " + r0 + " " + r1);
// esquecimento: evidência antiga pesa menos
const old = M.pAtom(M.build([{q:"q1",ok:false,t:t0-200*DAY},{q:"q1",ok:true,t:t0}], Q).A1, t0).p;
assert(old > 0.5, "esmaecimento");
// pick nunca devolve questão fora do filtro
for (let i = 0; i < 50; i++) assert(["q4","q5"].includes(M.pick(Q.filter(q=>q.t==="T2"), ev, t0).q.id), "filtro");
console.log("motor ok");
// ---- v2: campos ----
{
 const Q2=[
  {id:"a1",t:"T",a:["X1"],f:"F1",g:"C"},{id:"a2",t:"T",a:["X2"],f:"F1",g:"C"},{id:"a3",t:"T",a:["X3"],f:"F1",g:"E"},{id:"a4",t:"T",a:["X1"],f:"F1",g:"E"},
  {id:"b1",t:"T",a:["Y1"],f:"F2",g:"C"},{id:"b2",t:"T",a:["Y2"],f:"F2",g:"C"},{id:"c1",t:"T",a:["Z1"],f:"F3",g:"C"}];
 const t=Date.now();
 // transferência: acerto em X1 reduz prioridade do irmão novo X2 abaixo de um átomo novo de outro campo
 let e=[{q:"a1",ok:true,t:t-1000}];
 const A=M.build(e,Q2); assert(A.X2.tr.length===1 && !A.X2.n,"transferência registrada sem contar como resposta");
 assert(M.priority(A.X2,t,0)<M.priority(A.Y1,t,0),"irmão novo vale menos que novo de outro campo");
 // erro não transfere
 const Ae=M.build([{q:"a1",ok:false,t:t-1000}],Q2); assert(!(Ae.X2&&Ae.X2.tr.length),"erro não transfere");
 // quarentena: após responder no campo F1, as próximas 3 escolhas não vêm de F1 (há alternativas)
 {let n=0;for(let i=0;i<400;i++){const r=M.pick(Q2,[{q:"a1",ok:true,t:t-1000}],t); if(r.campo==="F1")n++;} assert(n<400*0.08,"quarentena do campo: "+n+"/400 vieram de F1");}
 // erro no átomo: o campo fica 'lacuna' e a volta do mesmo átomo não é bloqueada de vez
 const Ce=M.campos(Q2,[{q:"a1",ok:false,t:t-1000}],t); assert(Ce.F1.status==="lacuna","lacuna");
 let vol=0; for(let i=0;i<200;i++){ if(M.pick(Q2,[{q:"a1",ok:false,t:t-1000}],t).campo==="F1") vol++; } assert(vol>0,"átomo errado ainda volta");
 // dominado exige 4+ respostas, 3+ questões, p>=.85 e um acerto em item Errado
 const ok=(q,d)=>({q,ok:true,t:t-d*3600e3});
 let st=M.campos(Q2,[ok("a1",5),ok("a2",4),ok("a3",3),ok("a4",2)],t).F1.status; assert(st==="dominado","dominado: "+st);
 st=M.campos(Q2,[ok("a1",5),ok("a2",4),ok("a1",3),ok("a2",2)],t).F1.status; assert(st==="em andamento","sem isca E e 2 questões não domina: "+st);
 st=M.campos(Q2,[ok("a1",5),ok("a2",4),ok("a3",3),{q:"a4",ok:false,t:t-1000}],t).F1.status; assert(st==="lacuna","erro derruba o domínio: "+st);
 // novo em campo dominado espera: se o campo tiver átomo novo, prioridade cai
 console.log("motor v2 ok");
}
// relevância de prova: r=3 aparece bem menos que r=1 (mesmo campo/átomos equivalentes)
{
 const Q3=[{id:"u1",t:"T",a:["U1"],f:"G1",g:"C",r:1},{id:"u2",t:"T",a:["U2"],f:"G2",g:"C",r:3}];
 let n=0; for(let i=0;i<400;i++) if(M.pick(Q3,[],Date.now()).q.id==="u2") n++;
 assert(n<400*0.15,"r=3 deveria sair pouco: "+n);
 const Q4=[{id:"v1",t:"T",a:["V1"],f:"H",g:"C",r:3},{id:"v2",t:"T",a:["V1"],f:"H",g:"E",r:1}];
 for(let i=0;i<20;i++) assert(M.pick(Q4,[],Date.now()).q.id==="v2","no mesmo átomo, r=1 vem antes");
 console.log("relevância ok");
}
