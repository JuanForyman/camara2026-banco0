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
