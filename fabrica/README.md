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
