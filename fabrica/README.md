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

## Lote L11 — Modelos de gestão e governança (P1-M3-8 e P1-M3-9, edital 8 e 9)
58 itens (29 C/29 E), pontos G01–G06, 12 átomos doutrinários em dados/leis/ges.json (Weber, Plano Diretor 1995, EC 19/98, NPM, NPG, Moore, Decreto 9.203 arts. 2º e 3º). Fonte conferida = "conhecimento" com risco; resolução cega embaralhada 58/58 sem divergência. Itens de governança (G05, G06) gravados no tópico P1-M3-9.

## Lote L12 — Agentes públicos (P1-M3-3, edital 3)
74 itens (37 C/37 E), pontos S01–S06, 11 átomos em dados/leis/agp.json (CF arts. 37, 38 e 41, MI 708, Temas 161 e 531, SV 13/37/43/44, Súmulas 15 e 683, conceitos). Texto constitucional reproduzido por conhecimento: conferir a redação vigente. Resolução cega embaralhada 73/74; a divergência (Q-AGP-0017, redação ambígua do C) foi corrigida para o texto literal do art. 37, V. Lei 8.112 está no lote L2.

## Lote L13 — Direito administrativo disciplinar (P1-M3-4, edital 4)
66 itens (33 C/33 E), pontos D01–D07, 9 átomos em dados/leis/dis.json (Lei 8.112 arts. 121–131, 142–152, 167–169, conferidos contra dados/leis/l8112.json; Lei 9.784 art. 69; SV 5; Súmulas 18–21 do STF; Súmulas 591, 592, 611, 635, 650 e 651 do STJ). Súmulas por conhecimento, com risco. Resolução cega embaralhada 66/66 sem divergência. Complementa L1 e L2.

## Lote L14 — Ciência Política (P2-M9-1 a P2-M9-11, edital 9)
146 itens (73 C/73 E), pontos Q01–Q11 (um por tópico), 15 átomos doutrinários em dados/leis/pol.json (Weber, Dahl, Linz, Lijphart, Duverger, Sartori, Abranches, Limongi e Figueiredo, Faoro, Buarque de Holanda, Nunes Leal, Carvalho; CF arts. 1º, 2º, 4º, 14 e 17; Lei 9.096/1995; EC 97/2017). Os temas foram escolhidos por recorrência em provas de ciência política; não reproduzem questões reais do Cebraspe (sem acesso a texto confiável). Fonte conferida = "conhecimento" com risco. Resolução cega embaralhada 146/146. Pendente: conferir o regime das sobras eleitorais (STF 2024; fora dos itens), cláusula de desempenho e federações. O último concurso da Câmara (2023) foi da FGV, não do Cebraspe.

### L14 — Ciência Política, segunda leva (POL: 404 itens, P2-M9)
+258 itens (pol_b.py), átomos 16–37 (teorias da democracia, Tocqueville, Marx/Gramsci, Bobbio, poder, capital social, escolha racional, clivagens, indicadores, CF 14–16 e 44–46, impeachment, federalismo, políticas públicas, RI, nação, interpretações do Brasil 2, participação, política externa) e novos ângulos nos átomos 1–15. Lint 0; resolução cega embaralhada: 5 divergências, 2 itens reescritos (idades de elegibilidade ambíguas; EC 25/1985), 3 eram erro do resolvedor. Itens doutrinários: fonte "conhecimento" + risco; não reproduzem questões reais da banca.

### L14 — Ciência Política, terceira leva (POL: 646 itens, P2-M9)
+242 itens (pol_c/d/e.py), átomos 38–52 (regimes híbridos/autoritarismo e transições; parlamentarismo, monarquia e formas de Estado; representação e accountability; relações Executivo–Legislativo–Judiciário; fórmulas eleitorais; partidos e cláusula de desempenho; organização política brasileira CF; ordem internacional e política externa; teoria e formação do Estado; Estado brasileiro; história do voto e dos partidos). Lint 0; resolução cega embaralhada (4 lotes, sonnet): 11 divergências em 242, todas revistas (resolvedor errou ou hesitou; gabarito mantido) e 1 imprecisão corrigida (AI-2 × Ato Complementar n. 4). Itens de jurisprudência/prazos marcados `jur`; conferência por conhecimento (val.humana=false). Cláusula de desempenho conforme EC 97/2017 (2026: 2,5%/1,5% ou 13 deputados).

### L15 — Fala, Transcrição e IA (FIA: 314 itens, P2-M7, 25 tópicos 1.1–4.3)
25 átomos doutrinários (um por tópico do edital 7), ~12 itens por tópico, ~50% C/E. Fonte: conhecimento técnico (ASR, Whisper, CTC/RNN-T, diarização, degravação, HITL, busca semântica/RAG) e LGPD/Lei 9.610/1998 (arts. citados marcados lei=True, ainda a conferir no texto oficial). Lint 0; resolução cega embaralhada: 1 divergência em 314 (item de ITN, gabarito mantido). Pendências: padrão de formatação parlamentar da Câmara não verificado em manual oficial; sem itens reais da banca.


### L15 — Fala, Transcrição e IA, segunda leva (FIA: 566 itens, P2-M7)
+252 itens (fia_b/fia_c.py) sobre 25 átomos de aprofundamento (26–50, um por tópico 1.1–4.3): MFCC/decodificação/WFST, Conformer/SpecAugment/wav2vec 2.0, correção generativa e áudio nativo, DER/x-vectors/EEND, ITN e pontuação, corpora e homófonos do português, VAD/RTF/streaming, Whisper e variantes (faster-whisper, whisper.cpp, WhisperX), taquigrafia e notas taquigráficas, HITL e LGPD art. 20, fidelidade, formatação, normalização, formatos de legenda, WER/kappa/amostragem, biasing/LoRA, captação, ROUGE/map-reduce, BM25/nDCG, embeddings/RAG, LLM (tokens, temperatura, prompt injection), BERTimbau/NER, LGPD (arts. 6, 7, 12, 18, 38, 41, 48), Lei 9.610 (arts. 11, 24, 28, 41), CF art. 5º XXVIII a, PL 2338/2023 (jur), ISO 27001/27002, NIST, criptografia, ICP-Brasil, backup 3-2-1. Lint 0; resolução cega embaralhada (4 lotes): 0 divergências em 252. Fonte: conhecimento (val.humana=false); itens de lei a conferir no texto oficial.
### L16 — Linguística (LIN: 558 itens, P2-M6, 13 tópicos 6.1–6.13)
13 átomos doutrinários (signo, categorias semânticas, leitura/coesão, recursos de produção, enunciação/AD, gêneros/tipologia, variação, gramática, funções, retórica e figuras, redação oficial, lógica, LC 95/1998) apoiados nas anotações do usuário (Drive "6. LINGUÍSTICA"). Lint 0; resolução cega embaralhada em duas metades: 4 divergências em 558; 1 item reescrito (partes da retórica, ambíguo), 3 mantidos (LC 95 art. 6º, 11 II f, 12 III; resolvedor errou). Pendências: texto da LC 95 e do Manual de Redação (3ª ed.) de memória, conferir no Planalto; itens de doutrina sem texto-fonte.

## L17 — Tecnologia da Informação e Dados (P1-M5)
- 386 itens (193 C / 193 E), 8 tópicos (P1-M5-1 a 8), 8 átomos em dados/leis/ti.json (T01 Office 56, T02 Redes 54, T03 Comunicação 32, T04 Segurança 70, T05 IA 52, T06 Ética 28, T07 Dados 46, T08 Visualização 48).
- Lint 0 alertas (T01 corrigido: palavras absolutas). Resolução cega (2 subagentes sonnet, ordem embaralhada): 1 divergência (Q-TI-0106, erro do resolvedor: 80 MB = 640 Mb → 8 s).
- Fonte "conhecimento" com risco: nomes de recursos/atalhos do Microsoft 365, prazo da lixeira do OneDrive (93 dias em contas corporativas), Lei 14.129/2021, Lei 14.063/2020, Lei 13.146/2015, LGPD art. 6º citados de memória. Edital cita "Data Studio" (hoje Looker Studio).
- L17 reforço (mesmo lote, ti_b.py): +146 itens → TI total 532 (por tópico P1-M5-n: 1:96, 2:84, 3:40, 4:90, 5:76, 6:36, 7:46, 8:64). Átomos ampliados (Outlook/SharePoint/Copilot, OSI/CIDR/ping/WPA, A1/A3, temperatura, matriz de confusão, Marco Civil). Lint 0; cega: 1 divergência (Q-TI-0511, prazos do Marco Civil arts. 13 e 15: 1 ano/6 meses; conferir na lei).

## L16 — Linguística 6.11 e 6.13 refeitas a partir das fontes (Manual de Redação 3ª ed. e LC 95/1998)
- Texto-fonte: Manual (PDF do usuário, extraído) e LC 95 compilada (captura do usuário, OCR). Átomos 11 e 13 reescritos e criados 14–21 (`fabrica/atomos/lin_b.py`); itens antigos de G(11)/G(13) removidos de `lin_a.py` e substituídos por `lin_b.py` (L11, 90 pares) e `lin_c.py` (L13, 82 pares) → LIN 752 itens (376 C/376 E).
- Erros corrigidos do banco anterior: atributos da redação oficial (a 3ª ed. lista sete; "linguagem simples e direta" não consta); aviso/ofício/memorando (distinção abolida na 3ª ed.); vocativo (Excelentíssimo só para Chefes de Poder; demais, "Senhor + cargo"); numeração de parágrafos (três ou mais); LC 95 art. 11, II, f (exceções: data, número de lei, prejuízo à compreensão); art. 12, III, b (renumeração vedada só para artigos e unidades superiores; reordenação interna admitida com NR); NR (uma vez ao final do artigo); art. 18 (inexatidão formal) separado do entendimento doutrinário.
- Divergência de descrição: Manual (dia da publicação = dia zero) × LC 95, art. 8º, §1º (inclui a data da publicação e o último dia; vigência no dia seguinte). O resultado prático coincide (ex.: publicada em 1º/3 com 30 dias → vigor em 31/3).
- Fonte `conferida: pdf_usuario`; por conhecimento: símbolos de unidades (SI) e o entendimento majoritário de que violar a LC 95 não invalida a lei por si só. Lint 0 alertas; resolução cega (3 subagentes, 344 itens): 4 divergências, todas erro do resolvedor conferido no texto (retificação×republicação, contagem da vacância, linha pontilhada, ausência do País).
- Pendência: o Decreto 9.758/2019 (pronomes de tratamento) saiu do banco por não estar verificado; reintroduzir quando houver o texto.

## L18 — Língua Portuguesa, onda 1 (pontuação e concordância)
Lote LP: itens curtos (frases de ~20 palavras), gabarito de ≤25 palavras e "saiba mais" em mini-aula por átomo (regra, dois exemplos, pegadinha). Incidência baseada no raio-x Cebraspe 2025–2026. Onda 1: 36 pares de pontuação + 34 de concordância (140 itens, 12 átomos, 0 alertas no lint). Resolução cega: 135/140; os 5 divergentes eram 1 par ambíguo (vírgulas de adjunto intercalado, reescrito) e 3 itens corretos de adjetivas restritiva/explicativa, mantidos. Faltam ondas: interpretação, orações, reescrita, coesão, pronomes/classes, sentido, tipologia, verbos, regência, crase, ortografia.
