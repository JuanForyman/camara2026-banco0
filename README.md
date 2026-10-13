# Banco de questões — Câmara dos Deputados 2026 (Registro e Redação)

- dados/banco_regimentos_P1.jsonl e _P2.jsonl: questões C/E (schema v2; primeira linha é cabeçalho). validada=false até amostragem humana.
- dados/taxonomia.json: tópicos do edital. dados/atomos_regimentos.json: artigos (RICD 29ª ed. e Regimento Comum).
- dados/relatorio_cobertura.json: átomos-alvo sem questão.
- ferramentas/: scripts de extração, conversão e geração (nq/ = fonte das questões novas).
Memória do projeto: pasta QUARTEL GENERAL - CÂMARA no Drive.

## Lote CF (Direito Constitucional) — 2026-10-13
- `ferramentas/nq_cf/c01..c03` = 302 questões C/E (CF/88: M4-1 a M4-6), fonte: conhecimento do texto, **conferidas mecanicamente (artigos, números, prazos, quóruns) contra o PDF da CF (ed. Câmara/CDI, com EC 122/2022), que o usuário anexou. `validada=false` (sem revisão humana). Texto dos artigos em `dados/cf_texto.json` (`ferramentas/parse_cf.py`, `audit_cf.py`).
- `ferramentas/build_cf.py` gera `dados/cf_banco.json` e `dados/cf_artigos.json`; `dados/site/` = pacote atual do site (banco 677, artigos 328).

## Motor v2 — campos (2026-10-13)
- `q.f` = campo (grupo de átomos vizinhos; `ferramentas/campos.py` atribui para a CF; regimentos ainda sem agrupamento: campo = átomo). `dados/site/campos.json` = nomes.
- Acerto dá crédito parcial (TW=0,3) aos átomos irmãos e rebaixa o "novo" deles; erro não transfere e abre "lacuna" no campo.
- Quarentena no sorteio: campo respondido nas últimas 3 respostas pesa 0,1; nas últimas 10, 0,4 (átomo errado por último: 0,6/0,9).
- Dominado: 4+ respostas e 3+ questões distintas em 90 dias, p≥0,8, ao menos um acerto em item Errado, sem erro aberto; novo em campo dominado pesa 0,4.
- Painel mostra a tabela de campos. Testes: `node motor/test_engine.js` (v1 + v2).
- Direito Constitucional completo (595 questões, 41 campos): ferramentas/nq_cf/c01..c06; auditoria: ferramentas/audit_cf.py + dados/cf_texto.json.
