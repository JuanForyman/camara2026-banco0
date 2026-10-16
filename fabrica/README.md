# FÁBRICA DE QUESTÕES — Câmara 2026 (Cargo 11, Cebraspe)

Objetivo: banco extenso, de qualidade de prova, com metadados completos, produzido **por partes** (matéria × bloco do edital), alimentado pelos pontapés do usuário. Este diretório é o espaço de trabalho; o banco publicado continua em `dados/site/`.

## Princípio
Não se escreve questão a partir do artigo. Escreve-se a partir do **ponto de cobrança**: o que a banca realmente testa e como erra o candidato. Primeiro o mapa de incidência (blueprint), depois as questões, depois os filtros de qualidade.

## Pipeline (por parte)
| Etapa | O que acontece | Saída |
|---|---|---|
| F0 Pedido | Usuário dá o pontapé: "faça a Parte X" e anexa fontes (leis em PDF, provas anteriores, aulas). Fica registrado em `pedidos/`. | `pedidos/AAAA-MM-DD_<parte>.md` |
| F1 Fonte | Texto vigente conferível (PDF do usuário, regimento, etc.). Sem fonte textual: itens marcados `fonte.conferida="conhecimento"` e `risco`. | `dados/leis/*.json` |
| F2 Blueprint | Para cada tópico: lista de **pontos de cobrança** com incidência (alta/média/baixa), padrões aplicáveis, armadilhas típicas e quota de itens. Calibrado por provas reais fornecidas e pelo padrão Cebraspe. | `blueprints/<parte>.json` |
| F3 Geração | Questões **por ponto**: par gêmeo C/E quando couber (`par`), caso concreto e texto-base nos pontos que pedem. Literalidade só em dispositivo central (≤15% do lote). Metas: 45–55% C. | `ferramentas/nq_*/` |
| F4 Gates | (a) lint mecânico `fabrica/lint.py`; (b) conferência contra a fonte; (c) **resolução cega**: revisor independente (agente que não vê o gabarito) julga cada item; divergência = reescrever ou descartar; (d) anti-viés de tamanho (E não pode ser sistematicamente mais curto). | `val.mecanica`, `val.cega` |
| F5 Publicação | Só entra em `dados/site/` o que passou nos gates, com metadados v3 e lote registrado. Itens ainda `val.humana=false`. | banco + site |
| F6 Monitor | Marcas do site (ruim, suspeita, lixeira) e taxa de erro anormal em quem domina o átomo mandam o item de volta ao F4. | `relatorios/` |

## Metadados (schema v3: `schema_questao_v3.json`)
Por questão: tópico, matéria, bloco, item do edital, átomos, campo, **ponto de cobrança**, gabarito, formato (assertiva/caso/texto-base), **padrão** (`padroes_cebraspe.json`), tipo de erro alvo, **par gêmeo**, dificuldade esperada (1–3), relevância de prova `r`, incidência, fonte estruturada (tipo, ref, versão, como foi conferida), vigência, flags de risco, origem (autoral/banca/ia), lote, versão, tags, validações (mecânica, cega, humana). Permite filtrar por padrão, dificuldade, risco, fonte, incidência e lote.

## Biblioteca de padrões (`padroes_cebraspe.json`)
19 padrões (troca de número/autoridade/efeito, exceção omitida, generalização, restrição indevida, confusão de instituto, caso concreto, jurisprudência, doutrina, texto-base, reescrita, norma culta, sequência, atribuição de autor, literalidade útil). Limites: literalidade ≤15%, C entre 45 e 55%, nenhum padrão >35% do lote.

## Partes e ordem (`PARTES.json`)
Painel por tópico: itens atuais (legado) × aprovados v3 × meta. Ordem sugerida: (1) Direito Administrativo [Lei 9.784 refeita como piloto → depois 8.112, 14.133, 8.429, 12.527, 13.709, Dec. 9.203 + temas conceituais]; (2) Língua Portuguesa e Inglês [texto-base, reescrita, norma culta]; (3) Regimentos (fechar 242 átomos, já com blueprint); (4) TI e Dados; (5) Ciência Política e Linguística; (6) Fala/IA. Direito Constitucional entra na fila de **revisão** pelo mesmo padrão (790 itens legados).

## Banco legado
1.146 itens atuais ficam no site, mas foram medidos (`relatorios/lint_2026-10-15_baseline.json`): C = 61%, itens E em média 15–30% mais curtos que os C na maior parte dos tópicos (pista de tamanho), lote da Lei 9.784 com 55% de itens de leitura. Plano: reprocessar tópico a tópico (reescrever E, criar pares, podar `r=3`), sem derrubar o que já funciona.

## Regras fixas
- Um item julga uma ideia. Nada de pista só gramatical ou só por palavra absoluta.
- Questão de banca real só com PDF do usuário (`origem="banca"`, `banca_ref`).
- Item de doutrina/jurisprudência sem fonte textual: `risco` e `fonte.conferida="conhecimento"`; nunca `r=1` sem fonte citada.
- A IA não marca `val.humana`; o usuário usa "Ruim" no site.
- Registrar cada lote no README do repositório e em `ESTADO_PROJETO.md` (Drive).

## L4 — Lei 12.527/2011 (LAI) — 2026-10-15
166 itens (83 C / 83 E), tópico P1-M3-11, 11 campos `LAI-*`. Lint 0 alertas, resolução cega ok (divergência no art. 45 corrigida).

## L5 — Lei 13.709/2018 (LGPD) — 2026-10-15
224 itens (112 C / 112 E), tópico P1-M3-12, 13 campos `LGPD-*`, pares C/E por ponto (G01–G15). Lint 0 alertas; auditoria mecânica: 4 alertas, falsos positivos (números de lei); resolução cega por 2 agentes: 222/224 coerentes, 2 divergências (arts. 52, II e 55-D) conferidas contra o texto da lei — gabarito mantido. Itens da ANPD refletem a natureza de autarquia especial (Lei 14.460/22). `validada=false`.

## L6 — Decreto 9.203/2017 (governança) — 2026-10-15
70 itens (35 C / 35 E), tópico P1-M3-9, 6 campos `D9203-*`. Fonte: captura do compilado do Planalto enviada pelo usuário (texto vigente: Dec. 9.901/2019 e 10.907/2021; art. 20 e 20-A revogados). Lint 0 alertas; resolução cega 70/70.

## Ajustes — 2026-10-15
- Lei 9.784: art. 69-A (Lei 12.008/2009) e art. 69 incorporados (ponto P24; +12 itens, 259 no total; cega 12/12). Texto-fonte: doc do Drive criado pelo usuário.
- Lei 8.112: itens do art. 45 reescritos (consignações do §§ 1º e 2º foram revogadas pela Lei 14.509/2022; permanece o caput). Item da licença-paternidade (art. 208, 5 dias) segue válido para o regime estatutário; a Lei 15.371/2026 (celetistas/RGPS; 10, 15 e 20 dias a partir de 2027–2029) não altera a 8.112 segundo a fonte consultada — conferir. Cauda neutra anexada em 35 E do tópico P1-M3-4 (viés de tamanho) direto nos JSON: perde-se se o lote for reconstruído. MP 805/2017 (auxílio-moradia) perdeu vigência — texto anterior vale. PDF da 8.112 do Drive é imagem (sem texto) e grande demais para o conector; conferência pós-2015 feita via web.

## L7 — Lei 14.133/2021 (licitações e contratos) — 2026-10-16
654 itens (327 C / 327 E), tópico P1-M3-10, 50 pontos T01–T50 (arts. 1º a 183), 29 campos `L14133-*`. Fonte: lei esquematizada (Herbert Almeida, 4ª ed., atualizada até 2023), lida por `ferramentas/parse_esq2.py`; arts. 172 e 188 ausentes no texto-fonte. Itens em `fabrica/questoes/l14133_a..g.py`; build: `python3 -I fabrica/build_v3.py fabrica/blueprints/l14133.json dados/leis/l14133.json dados L7` (depois reaplicar val `{mecanica:true,cega:ok,humana:false}`). Lint 0 alertas; auditoria mecânica: 25 alertas, falsos positivos (números de lei); resolução cega por agentes independentes em 654 itens sem divergência de gabarito. 16 itens com risco `valor_atualizado_por_decreto` (valores de dispensa, contrato verbal etc., atualizados por Decretos 11.317/2022 e 12.343/2024). Pendências: conferir alterações posteriores a 2023 (ex.: LC 182/2021 e Lei 14.770/2023 sobre art. 75), diversificar padrões (excecao_omitida ≈50%).

## Lote L8 — Responsabilidade civil do Estado (P1-M3-6, edital 6)
64 itens (32 C/32 E), pontos R01–R08, 15 átomos doutrinários em dados/leis/rce.json. Fonte: CF 37 §6º, CC 43 e teses do STF (Temas 130, 362, 365, 366, 512, 592, 666, 777, 940, 950, 1055, 1237, 1347), conferência = "conhecimento" com risco; nenhum item r=1 sem fonte citada. Resolução cega: 64/64 sem divergência. Revisar teses contra os acórdãos antes de tratar como definitivo.

## Lote L9 — Ato administrativo e poderes (P1-M3-2 e P1-M3-5, edital 2 e 5)
62 itens (31 C/31 E), pontos A01–A08, 12 átomos doutrinários em dados/leis/ato.json. Fonte: Lei 9.784/99, Súmulas 346/473 e SV 3, Temas 445 e 532 do STF, LINDB art. 28, doutrina; conferida = "conhecimento" com risco. Resolução cega (ordem embaralhada): 62/62 sem divergência.

## Lote L10 — Organização administrativa (P1-M3-1, edital 1)
62 itens (31 C/31 E), pontos O01–O09, 10 átomos em dados/leis/org.json (DL 200/67, CF 37 XIX/XX e 173, Leis 9.637, 9.790, 13.019, 13.303, 11.107 e 9.784 art. 1º, ADI 1.923, RE 220.906, Súmula 525 STJ). Fonte conferida = "conhecimento" com risco; resolução cega embaralhada 62/62 sem divergência.
