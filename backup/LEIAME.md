# Backup do histórico do aluno

Gerado por `ferramentas/backup_dados.py`. Repositório privado.

## Como rodar
`python3 -I ferramentas/backup_dados.py <dump> --push`
`<dump>` = pasta com `estado/`, `eventos/`, `simulados/` (um JSON por documento, lidos do banco do site) ou o arquivo `historico_camara2026.json` do botão "Exportar" da aba Painel.

## Regras de substituição
- `raw/eventos.jsonl`: união por id. Nunca apaga; só acrescenta.
- `raw/estado.json`: por questão, vence o documento de maior campo `u` (mais recente).
- `raw/simulados.json`: união por id.
- Todo o resto (`eventos/`, `estado/`, `analise/`) é recalculado a partir do `raw` + `dados/site/*.json`, então sempre reflete o banco de questões atual.
- Se nada mudou, não há commit.

## Conteúdo
- `eventos/AAAA-MM.jsonl`: cada resposta com data, questão, resposta, gabarito, acerto, tempo, confiança, modo, tópico, matéria, bloco, campo, átomos, artigos, tipo, relevância e se foi a primeira vez.
- `estado/questoes.json`: por questão respondida, estado de revisão (caixa, vencimento, causas), enunciado, regra correta e sequência de acertos.
- `estado/erros_abertos.jsonl`: questões cuja última resposta foi errada.
- `analise/`: acerto, líquido, pior caso (limite inferior), primeira vez, tempo mediano e últimas 10 por matéria, tópico, campo, átomo, tipo, gabarito, modo; `diario.json`; `confusao_CE.json`.
- `manifest.json`: contagens e hashes.

## Restaurar
O `raw/` tem o formato exato dos documentos do banco (`estado` por id de questão, `eventos` por id). Para reimportar, peça ao Claude: ele lê `raw/` e grava de volta com a ferramenta de dados do artefato.
