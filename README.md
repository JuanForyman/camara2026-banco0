# Banco de questões — Câmara dos Deputados 2026 (Registro e Redação)

- dados/banco_regimentos_P1.jsonl e _P2.jsonl: questões C/E (schema v2; primeira linha é cabeçalho). validada=false até amostragem humana.
- dados/taxonomia.json: tópicos do edital. dados/atomos_regimentos.json: artigos (RICD 29ª ed. e Regimento Comum).
- dados/relatorio_cobertura.json: átomos-alvo sem questão.
- ferramentas/: scripts de extração, conversão e geração (nq/ = fonte das questões novas).
Memória do projeto: pasta QUARTEL GENERAL - CÂMARA no Drive.

## Lote CF (Direito Constitucional) — 2026-10-13
- `ferramentas/nq_cf/c01..c03` = 302 questões C/E (CF/88: M4-1 a M4-6), fonte: conhecimento do texto, **conferidas mecanicamente (artigos, números, prazos, quóruns) contra o PDF da CF (ed. Câmara/CDI, com EC 122/2022), que o usuário anexou. `validada=false` (sem revisão humana). Texto dos artigos em `dados/cf_texto.json` (`ferramentas/parse_cf.py`, `audit_cf.py`).
- `ferramentas/build_cf.py` gera `dados/cf_banco.json` e `dados/cf_artigos.json`; `dados/site/` = pacote atual do site (banco 677, artigos 328).
