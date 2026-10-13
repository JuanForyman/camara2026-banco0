// Extrai as estruturas de dados do artefato M8 (Processo Legislativo e RICD) para JSON.
// Uso: node extract_m8.js <index.html> <saida.json>
const fs = require('fs');
const vm = require('vm');
const [,, src, out] = process.argv;
const lines = fs.readFileSync(src, 'utf8').split('\n');
const start = lines.findIndex(l => l.startsWith('const GLOSS_RAW'));
const end = lines.findIndex(l => l.startsWith('const esc='));
if (start < 0 || end < 0) { console.error('marcadores não encontrados', start, end); process.exit(1); }
const code = lines.slice(start, end).join('\n') +
  '\n;globalThis.__out = {GLOSS_RAW, MODS, ITEMS, SEQS, MATCH, CARDS_RAW, QART};';
const ctx = vm.createContext({});
try {
  vm.runInContext(code, ctx, { timeout: 5000 });
} catch (e) {
  console.error('erro ao avaliar:', e.message);
  process.exit(2);
}
const o = ctx.__out;
fs.writeFileSync(out, JSON.stringify(o, null, 1));
const n = k => Array.isArray(o[k]) ? o[k].length : typeof o[k];
console.log(JSON.stringify({
  linhas: [start + 1, end],
  mods: n('MODS'),
  fichas: o.MODS.reduce((s, m) => s + m.fichas.length, 0),
  itens: n('ITEMS'),
  seqs: n('SEQS'),
  match: n('MATCH'),
  cards: n('CARDS_RAW'),
  qart: n('QART'),
  glossario_chars: o.GLOSS_RAW.length
}));
