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

## Lote Direito Administrativo — Lei 9.784/1999
176 questões (121 C / 55 E) sobre o processo administrativo federal (tópico P1-M3-4), 78 átomos, 11 campos (`L9784-*`). Fonte: PDF anexado pelo usuário (sem o art. 69-A e alterações posteriores). Auditoria mecânica: 6 alertas, todos falsos positivos. `validada=false`.
Build: `python3 -I ferramentas/build_lei.py L9784 "Lei 9.784/99" ferramentas/nq_leis/l9784 dados/leis/l9784.json dados`.

## DIRETRIZ DE RELEVÂNCIA DE PROVA (permanente)
Toda questão nova deve ser confrontada com o que o Cebraspe realmente cobra (formato Certo/Errado, pegadinhas, trocas de prazo/quórum/competência, exceções, generalizações "sempre/somente/qualquer", dispositivos de alta incidência), e não apenas com a letra da lei. Evitar lotes de "leitura" (paráfrase do artigo, gabarito C). Meta de equilíbrio ≈ 50% C / 50% E por tópico. Volume proporcional à incidência do tema/artigo.
Implementação: campo `q.r` (1 = padrão de prova, 2 = plausível, 3 = letra seca); motor serve r=1 primeiro (pesos 1 / 0,55 / 0,15). `ferramentas/relevancia.py` atribui r.
Estado em 13/10: Lei 9.784 = 123 r1, 25 r2, 28 r3; 96 das 176 eram "leitura", todas gabarito C (69% C no lote): precisam de variantes Errado e poda.

## Lote L1 da Fábrica — Lei 9.784/99 refeita (2026-10-15)
247 itens v3 (123 C / 124 E; tam. médio C 161 x E 164 caracteres; 23 pontos de cobrança; 6 itens C sem par) substituem os 176 anteriores (arquivados em dados/legado_l9784_banco.json). Metadados completos em dados/v3/l9784.json; blueprint em fabrica/blueprints/l9784.json; itens em fabrica/questoes/l9784_a..d.py; build: `python3 -I fabrica/build_v3.py fabrica/blueprints/l9784.json dados/leis/l9784.json dados L1`; auditoria: fabrica/audit_v3.py (22 alertas, todos falsos positivos).
Resolução cega por revisor independente (agente sem acesso ao gabarito): 247/247 concordam; 1 item (Q-L9784-0157, SV 21) apontado como ambíguo e reescrito. Itens de jurisprudência (SV 3, 5, 21; Súm. STF 346 e 473; Súm. STJ 633) = fonte por conhecimento, marcados com risco. Pendente: art. 69-A e alterações posteriores (PDF atualizado).

## Lote L2 da Fábrica — Lei 8.112/90 (2026-10-15)
466 itens v3 (233 C / 233 E), 31 pontos de cobrança (provimento a seguridade, PAD, casos integrados, jurisprudência). Fonte: PDF "esquematizada" do usuário, lido por `ferramentas/parse_esq.py` (245 artigos). Build: `python3 -I fabrica/build_v3.py fabrica/blueprints/l8112.json dados/leis/l8112.json dados L2` e SEMPRE depois `python3 -I fabrica/pos_build_l8112.py` (reaplica val/risco). Mescla no site: `python3 -I ferramentas/merge_lote.py L8112 dados/l8112_banco.json dados/l8112_artigos.json` + `ferramentas/campos.py` (26 campos L8112). Resolução cega por agentes independentes: 464/466 (3 divergências conferidas contra o texto; gabarito mantido). 32 itens com risco (vigência: estágio probatório 24 x 36 meses/EC 19, art. 186 superado pelas ECs 20/41/103, teto, licenças ampliadas por leis posteriores). Pendente: texto posterior a 2015 e alíneas truncadas pelo parser (art. 36 c–.., 60-B).

## Lote L3 da Fábrica — Lei 8.429/92 com a Lei 14.230/21 (2026-10-15)
258 itens v3 (129 C / 129 E; lint 0 alertas), 16 pontos (dolo, sujeitos, arts. 9/10/11/12, indisponibilidade, rito, ANPC, sentença, prescrição, jurisprudência, casos integrados). Build: `python3 -I fabrica/build_v3.py fabrica/blueprints/l8429.json dados/leis/l8429.json dados L3` (depois marcar val/risco como nos lotes anteriores); merge: `ferramentas/merge_lote.py L8429 ...` + `campos.py` (13 campos L8429). Resolução cega por 3 agentes: 258/260 iniciais concordaram (2 divergências conferidas; 5 enunciados ajustados). 14 itens de jurisprudência (STF Temas 1.199 e 897, ADIs 7042/7043, SV 13, Pet 3240) com fonte "conhecimento" e risco. Retirado: art. 17, § 20 (possível suspensão na ADI 7236). Pendente: texto vigente após ADIs 7042/7043/7236; arts. 12 e 13 com trechos truncados no parser.
