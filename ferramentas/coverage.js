// Cobertura de artigos (RICD e Regimento Comum) citados no material do M8.
// Uso: node coverage.js m8_extract.json
const o = require(require('path').resolve(process.argv[2]));

function parseCitation(str, defaultNorma) {
  const hits = []; // {norma, art}
  let norma = defaultNorma;
  for (let seg of String(str).split(/;/)) {
    if (/\bRC\b|Regimento Comum/.test(seg)) norma = 'RC';
    else if (/\bCF\b|Constitui/.test(seg)) norma = 'CF';
    else if (/RICD/.test(seg)) norma = 'RICD';
    else if (/\bLC\b|Lei\b|Res\./.test(seg)) norma = 'OUTRA';
    // remove referências a parágrafos
    let s = seg.replace(/§§?\s*\d+º?(?:\s*(?:,|e|a)\s*\d+º?)*/g, ' ');
    // trecho de artigos: "art(s). 52, 56 e 150" ou segmento iniciado por número
    const m = s.match(/arts?\.?\s*((?:\d+º?(?:\s*(?:,|e|a)\s*)?)+)/i) ||
              (/^\s*\d/.test(s) ? [null, s] : null);
    if (!m) continue;
    const toks = m[1].match(/\d+º?|\ba\b/g) || [];
    let prev = null, range = false;
    for (const t of toks) {
      if (t === 'a') { range = true; continue; }
      const n = parseInt(t, 10);
      if (range && prev !== null && n >= prev && n - prev <= 120) {
        for (let k = prev; k <= n; k++) hits.push({ norma, art: k, faixa: true });
      } else hits.push({ norma, art: n, faixa: false });
      range = false; prev = n;
    }
  }
  return hits;
}

const prec = { RICD: new Set(), RC: new Set(), CF: new Set() }; // citados de forma direta (itens, cartões, qart, pares, sequências)
const faixa = { RICD: new Set(), RC: new Set(), CF: new Set() }; // só em faixas ou fichas

function add(str, def, fromFicha) {
  for (const h of parseCitation(str, def)) {
    if (!prec[h.norma]) continue;
    (fromFicha || h.faixa ? faixa : prec)[h.norma].add(h.art);
  }
}
o.ITEMS.forEach(i => add(i.art, 'RICD'));
o.CARDS_RAW.forEach(c => add(c[2], 'RICD'));
o.QART.forEach(q => { add(q[1], 'RICD'); (q[2] || []).forEach(x => add(x, 'RICD')); });
o.SEQS.forEach(s => s.steps.forEach(st => add(st[1], 'RICD')));
o.MATCH.forEach(m => m.rows.forEach(r => add(r[1], 'RICD')));
o.MODS.forEach(m => m.fichas.forEach(f => add(f.base, 'RICD', true)));

function ranges(set, lo, hi) {
  const miss = []; let a = null;
  for (let n = lo; n <= hi + 1; n++) {
    const ok = n > hi || set.has(n);
    if (!ok && a === null) a = n;
    if (ok && a !== null) { miss.push(a === n - 1 ? String(a) : a + '-' + (n - 1)); a = null; }
  }
  return miss.join(', ');
}
function rep(label, norma, blocks) {
  let tot = 0, p = 0, f = 0; const rows = [];
  for (const [lo, hi, nome] of blocks) {
    let bt = 0, bp = 0, bf = 0;
    for (let n = lo; n <= hi; n++) { bt++; if (prec[norma].has(n)) bp++; else if (faixa[norma].has(n)) bf++; }
    tot += bt; p += bp; f += bf;
    const union = new Set([...prec[norma], ...faixa[norma]]);
    rows.push(`  ${nome} (${lo}-${hi}): direto ${bp}/${bt}; só em faixa/ficha ${bf}; sem citação: ${ranges(union, lo, hi) || '—'}`);
  }
  console.log(`${label}: direto ${p}/${tot}, só faixa/ficha ${f}, sem citação ${tot - p - f}`);
  rows.forEach(r => console.log(r));
}
console.log('== P2 (itens 2 e 3 do bloco de Processo Legislativo)');
rep('RICD P2', 'RICD', [[25, 64, 'arts. 25-64'], [95, 200, 'arts. 95-200']]);
rep('RC P2', 'RC', [[1, 71, 'arts. 1-71']]);
console.log('== P1 (Direito Constitucional e Regimentos)');
rep('RICD P1', 'RICD', [[1, 24, 'arts. 1-24'], [65, 94, 'arts. 65-94'], [226, 251, 'arts. 226-251'], [262, 273, 'arts. 262-273']]);
rep('RC P1 (Título IV, Caps. II e III até art. 103; Título I a confirmar)', 'RC', [[72, 103, 'arts. 72-103']]);
const fora = [...prec.RICD].filter(n => !((n >= 25 && n <= 64) || (n >= 95 && n <= 200))).sort((a, b) => a - b);
console.log('RICD citado fora de 25-64/95-200:', fora.join(', ') || '—');
console.log('CF citada (art):', [...prec.CF, ...faixa.CF].sort((a, b) => a - b).join(', ') || '—');
