/* Motor de estudo v2 (puro, sem DOM): v1 + campos (famílias de átomos vizinhos). Usado pelo site e por scripts.
   Entrada: eventos {q, ok(true|false|null), t(ms)} e questões {id,t,a[],g}.
   Unidade de conhecimento: átomo (artigo). Questão sem átomo vira átomo próprio "Q:<id>". */
(function (root) {
  const DAY = 864e5;
  const INT = [0.007, 1, 3, 7, 16, 35, 80]; // dias até a próxima revisão, por sequência de acertos
  const META = { pp: 0.65, ampla: 0.705, nota: "estimada pela prova anterior da Câmara (corte 117/180 PP, 127/180 ampla); outra prova, outra especialidade" };

  const atomsOf = q => (q.a && q.a.length ? q.a : ["Q:" + q.id]);
  // Campo = grupo de átomos vizinhos (q.f). Sem q.f, o campo é o próprio átomo (sem agrupamento).
  const campoOf = q => q.f || atomsOf(q)[0];
  const TW = 0.3;          // peso da transferência de um acerto para átomos irmãos do campo (só acertos)

  function build(events, Q) {
    const qm = new Map(Q.map(q => [q.id, q]));
    const A = {}, camp = new Map();
    for (const q of Q) { const c = campoOf(q); const set = camp.get(c) || camp.set(c, new Set()).get(c); atomsOf(q).forEach(a => set.add(a)); }
    const mk = a => A[a] || (A[a] = { ev: [], tr: [], streak: 0, last: 0, n: 0, ok: 0 });
    const ev = events.filter(e => e.ok === true || e.ok === false).sort((a, b) => a.t - b.t);
    for (const e of ev) {
      const q = qm.get(e.q); if (!q) continue;
      atomsOf(q).forEach((a, i) => {
        const x = mk(a);
        const w = i === 0 ? 1 : 0.5;
        x.ev.push([e.t, e.ok ? 1 : 0, w]); x.n += w;
        if (e.ok) { x.ok += w; x.streak++; } else x.streak = 0;
        x.last = e.t;
      });
      if (e.ok === true) { // transferência parcial: acerto vale um pouco para os irmãos; erro não reduz nada
        const own = new Set(atomsOf(q));
        for (const a of camp.get(campoOf(q)) || []) if (!own.has(a)) mk(a).tr.push([e.t, TW]);
      }
    }
    return A;
  }

  // Probabilidade de acerto: Beta(1,1) com evidência que esmaece (meia-vida 60 dias).
  // Regra do teto: menos de 2 respostas -> no máximo 0,75.
  function pAtom(x, t) {
    if (!x || !x.n) return { p: 0.5, neff: 0 };
    let s = 1, f = 1, ne = 0;
    for (const [te, w] of x.tr || []) s += w * Math.pow(0.5, (t - te) / DAY / 60);
    for (const [te, ok, w] of x.ev) {
      const ww = w * Math.pow(0.5, (t - te) / DAY / 60);
      ne += ww; if (ok) s += ww; else f += ww;
    }
    let p = s / (s + f);
    if (x.n < 2) p = Math.min(p, 0.75);
    return { p, neff: ne };
  }

  function urgency(x, t) { // >=1 significa vencido
    if (!x || !x.n) return 0;
    return (t - x.last) / DAY / INT[Math.min(x.streak, INT.length - 1)];
  }

  function priority(x, t, cov) {
    if (!x || !x.n) { // novo: mais valioso em tópico pouco coberto; menos se um irmão do campo já foi acertado
      let tr = 0; for (const [te, w] of (x && x.tr) || []) tr += w * Math.pow(0.5, (t - te) / DAY / 30);
      return 0.45 * (1 + (1 - cov)) * (1 - 0.4 * Math.min(1, tr / 0.6));
    }
    const { p } = pAtom(x, t), u = urgency(x, t);
    if (x.streak === 0) return 0.6 + (1 - p); // errou por último: outra questão do mesmo artigo logo
    return Math.max(0.02, (1 - p) * (0.6 + 0.4 * Math.min(u, 3)) + (u >= 1 ? 0.35 : -0.25 * (1 - u)));
  }

  function motivo(x, t) {
    if (!x || !x.n) return "nova";
    const u = urgency(x, t), { p } = pAtom(x, t);
    if (x.streak === 0) return "você errou por último";
    if (u >= 1) return "revisão vencida";
    return p < 0.6 ? "ponto fraco" : "reforço";
  }

  function coverage(Q, A) {
    const c = {};
    for (const q of Q) { const k = q.t, o = c[k] || (c[k] = { n: 0, v: 0 }); o.n++; if (A[atomsOf(q)[0]] && A[atomsOf(q)[0]].n) o.v++; }
    return c;
  }

  // Estado de cada campo. dominado: >=4 respostas e >=3 questões distintas nos últimos 90 dias, p>=0,8 e ao menos
  // um acerto em item Errado (isca), se o campo tiver algum. lacuna: algum átomo errado por último.
  function campos(Q, events, t) {
    const qm = new Map(Q.map(q => [q.id, q])), out = {};
    for (const q of Q) { const c = campoOf(q), o = out[c] || (out[c] = { id: c, n: Q.length && 0, atomos: new Set(), qs: new Set(), temE: false, ev: [], status: "novo", p: 0.5 }); atomsOf(q).forEach(a => o.atomos.add(a)); o.temE = o.temE || q.g === "E"; o.t = o.t || q.t; }
    for (const e of events.filter(e => e.ok === true || e.ok === false).sort((a, b) => a.t - b.t)) {
      const q = qm.get(e.q); if (!q) continue; const o = out[campoOf(q)]; o.ev.push({ t: e.t, ok: e.ok, q: q.id, g: q.g });
    }
    const A = build(events, Q);
    for (const o of Object.values(out)) {
      let s = 1, f = 1; const rec = o.ev.filter(e => t - e.t <= 90 * DAY);
      for (const e of o.ev) { const w = Math.pow(0.5, (t - e.t) / DAY / 60); if (e.ok) s += w; else f += w; }
      o.p = s / (s + f); o.resp = o.ev.length; o.atomos = [...o.atomos];
      const lacuna = o.atomos.some(a => A[a] && A[a].n && A[a].streak === 0);
      const qs = new Set(rec.map(e => e.q)), acE = rec.some(e => e.ok && e.g === "E");
      const ult = rec.slice(-4).filter(e => e.ok).length;
      if (!o.resp) o.status = "novo";
      else if (lacuna) o.status = "lacuna";
      else if (rec.length >= 4 && qs.size >= 3 && ult >= 4 - 0 && o.p >= 0.8 && (acE || !o.temE)) o.status = "dominado";
      else o.status = "em andamento";
      delete o.ev; delete o.qs;
    }
    return out;
  }

  const RW = { 1: 1, 2: 0.55, 3: 0.15 }; // peso por relevância de prova
  // Escolhe a próxima questão. allowed: lista de questões elegíveis (já sem lixeira e com filtro).
  function pick(allowed, events, t, rnd) {
    rnd = rnd || Math.random;
    if (!allowed.length) return null;
    const A = build(events, allowed), cov = coverage(allowed, A);
    const byAtom = new Map();
    for (const q of allowed) for (const a of atomsOf(q)) { (byAtom.get(a) || byAtom.set(a, []).get(a)).push(q); }
    const last = {}; // última vez que cada questão apareceu
    for (const e of events) last[e.q] = Math.max(last[e.q] || 0, e.t);
    // quarentena: campo respondido nas últimas 3 respostas pesa 0,1; nas últimas 10, 0,4 (atomo errado por último: 0,6 / 0,9)
    const qm = new Map(allowed.map(q => [q.id, q])), recent = new Map();
    const ord = events.filter(e => qm.has(e.q)).sort((u, v) => v.t - u.t);
    ord.forEach((e, i) => { const c = campoOf(qm.get(e.q)); if (!recent.has(c)) recent.set(c, i); });
    const CS = campos(allowed, events, t);
    const cand = [];
    for (const [a, qs] of byAtom) {
      const top = qs[0].t, c = cov[top] ? cov[top].v / cov[top].n : 0, cp = campoOf(qs[0]), x = A[a];
      let pr = priority(x, t, c), i = recent.has(cp) ? recent.get(cp) : 99;
      const err = x && x.n && x.streak === 0;
      if (i < 3) pr *= err ? 0.6 : 0.1; else if (i < 10) pr *= err ? 0.9 : 0.4;
      if ((!x || !x.n) && CS[cp] && CS[cp].status === "dominado") pr *= 0.4; // terreno dominado: o novo espera
      const rr = Math.min(...qs.map(q => q.r || 1)); pr *= RW[rr] || 1; // relevância de prova (q.r)
      cand.push({ a, qs, pr, x, cp });
    }
    cand.sort((u, v) => v.pr - u.pr);
    const top = cand.slice(0, 6), wsum = top.reduce((s, c) => s + c.pr * c.pr, 0);
    let r = rnd() * wsum, ch = top[0];
    for (const c of top) { r -= c.pr * c.pr; if (r <= 0) { ch = c; break; } }
    const qs = ch.qs.slice().sort((a, b) => ((a.r || 1) - (b.r || 1)) * 1e14 + (last[a.id] || 0) - (last[b.id] || 0) + (rnd() - 0.5) * 1e3);
    return { q: qs[0], motivo: motivo(ch.x, t), atomo: ch.a, campo: ch.cp, prioridade: ch.pr };
  }

  // Aproveitamento líquido esperado (acerto − erro), por tópico e geral. Não visto vale 0.
  function readiness(Q, events, t) {
    const A = build(events, Q), out = { topicos: {}, geral: 0, vistos: 0, n: Q.length };
    let soma = 0;
    for (const q of Q) {
      const a = atomsOf(q)[0], x = A[a], p = pAtom(x, t).p;
      const ev = x && x.n ? Math.max(0, 2 * p - 1) : 0;
      const k = out.topicos[q.t] || (out.topicos[q.t] = { n: 0, v: 0, liq: 0 });
      k.n++; k.liq += ev; if (x && x.n) { k.v++; out.vistos++; }
      soma += ev;
    }
    out.geral = Q.length ? soma / Q.length : 0;
    for (const k of Object.values(out.topicos)) k.liq = k.n ? k.liq / k.n : 0;
    return out;
  }

  // Átomos mais prioritários agora (para o painel)
  function fila(Q, events, t, n) {
    const A = build(events, Q), cov = coverage(Q, A), seen = new Map();
    for (const q of Q) for (const a of atomsOf(q)) if (!seen.has(a)) seen.set(a, q);
    return [...seen].map(([a, q]) => {
      const c = cov[q.t] ? cov[q.t].v / cov[q.t].n : 0;
      return { a, t: q.t, pr: priority(A[a], t, c), motivo: motivo(A[a], t), p: pAtom(A[a], t).p };
    }).sort((u, v) => v.pr - u.pr).slice(0, n || 8);
  }

  const api = { build, pAtom, urgency, priority, pick, readiness, fila, coverage, campos, campoOf, atomsOf, META, INT, DAY, TW };
  if (typeof module !== "undefined") module.exports = api; else root.Motor = api;
})(typeof window !== "undefined" ? window : globalThis);
