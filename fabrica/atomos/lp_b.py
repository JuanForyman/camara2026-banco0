"""Língua Portuguesa — L19, onda 2: conectores/referenciação (13–15), orações (16–19), sintaxe (20), reescrita (21–23).
Uso: python3 -I fabrica/atomos/lp_b.py (idempotente; acrescenta ao dados/leis/lp.json e ao blueprint lp.json)."""
import json
ATOMOS = {
"13": ["Conectores coordenativos e relações de sentido",
 "Aditivas: e, nem, não só… mas também. Adversativas: mas, porém, contudo, todavia, entretanto, no entanto. Alternativas: ou, ora… ora, quer… quer. Conclusivas: logo, portanto, por isso, assim. Explicativas: que, porque, pois.",
 "'Pois' antes do verbo explica ('Cale-se, pois o juiz chegou'); depois do verbo conclui ('O réu é culpado; deve, pois, ser condenado'). O 'e' pode ter valor adversativo: 'Estudou e não passou'.",
 "Pegadinha: a banca troca a relação lógica (conclusão por oposição, adição por concessão) e pergunta se o sentido se mantém."],
"14": ["Conjunções subordinativas e seus valores",
 "Causais: porque, já que, visto que, uma vez que, como (no início). Concessivas: embora, conquanto, ainda que, mesmo que, se bem que. Condicionais: se, caso, desde que, a menos que. Finais: para que, a fim de que. Consecutivas: tão… que, de modo que.",
 "Temporais: quando, assim que, logo que, mal. Conformativas: conforme, segundo, consoante. Proporcionais: à medida que, quanto mais… mais. Comparativas: como, que nem.",
 "Pegadinha: concessão não é causa nem condição ('embora' ≠ 'porque'; 'mesmo que' = 'ainda que', não 'desde que'); 'como' inicial costuma ser causal."],
"15": ["Referenciação: anáfora, catáfora e pronomes",
 "Anáfora retoma termo já dito ('A emenda… Ela'); catáfora antecipa o que virá ('Uma coisa preocupava: o prazo'). Este/esta = mais próximo ou o que vem; esse/essa = o já citado; aquele = o mais distante. Entre dois termos: 'este' ao último, 'aquele' ao primeiro.",
 "'Cujo' indica posse, concorda com o possuído e dispensa artigo depois ('o servidor cujo cargo foi extinto'). Os pronomes o/a/os/as são objeto direto; lhe/lhes, objeto indireto. Substituição lexical: 'o Senado' → 'a Casa revisora'.",
 "Pegadinha: item pergunta a que termo o pronome se refere ou se 'cujo' concorda com o possuidor (não concorda)."],
"16": ["Orações coordenadas",
 "Coordenadas são independentes entre si. Assindéticas: sem conectivo ('Chegou, viu, venceu'). Sindéticas: aditiva, adversativa, alternativa, conclusiva e explicativa, conforme o conectivo (ver átomo 13).",
 "Explicativa (coordenada) justifica a afirmação anterior, em geral após vírgula ('Choveu, pois as ruas estão alagadas'); causal (subordinada) indica a causa do fato ('As ruas alagaram porque choveu').",
 "Pegadinha: confundir explicativa com causal e conclusiva com explicativa; ver 'logo' e 'pois' no lugar certo."],
"17": ["Orações subordinadas substantivas",
 "Fazem papel de substantivo; teste: troque por 'isso'. Subjetiva (sujeito): 'É necessário que ele venha'. Objetiva direta: 'Afirmou que votaria'. Objetiva indireta (com preposição): 'Insisti em que viessem'. Completiva nominal: 'Tenho medo de que falhe'.",
 "Predicativa (após verbo de ligação): 'O problema é que faltam recursos'. Apositiva (explica um termo, após dois-pontos): 'Fez um pedido: que votassem'. 'Se' interrogativo também introduz substantiva: 'Perguntei se viria'.",
 "Pegadinha: completiva nominal × objetiva indireta (a primeira completa um substantivo ou adjetivo); 'se' integrante × condicional."],
"18": ["Adjetivas e orações reduzidas",
 "Adjetivas começam por pronome relativo (que, o qual, cujo, quem, onde) e se ligam a um substantivo. 'Que' relativo retoma um termo ('O livro que li'); integrante introduz substantiva.",
 "Reduzidas não têm conectivo e têm verbo em infinitivo, gerúndio ou particípio: 'Ao concluir' = 'Quando concluiu' (tempo); 'Encerrada a sessão' = 'Quando a sessão foi encerrada'; 'Sendo o prazo curto' = 'Como o prazo era curto' (causa).",
 "Pegadinha: reescrever a reduzida com conectivo de outra relação (concessão no lugar de tempo ou causa)."],
"19": ["Equivalência entre orações adverbiais",
 "Troca de conectivo preserva o sentido só dentro da mesma relação: se = caso (condição); ainda que = embora = mesmo que = conquanto = posto que (concessão); já que = visto que = uma vez que (causa); assim que = logo que (tempo).",
 "Troca entre relações diferentes altera o sentido: 'embora' no lugar de 'porque' inverte a ideia. Atenção ao modo: concessivas e condicionais costumam pedir subjuntivo.",
 "Pegadinha: 'posto que' é concessivo (= embora), não causal (≠ visto que)."],
"20": ["Sintaxe: sujeito, objetos, predicativo e complementos",
 "Sem sujeito: haver (existir), fazer (tempo), fenômenos da natureza. Indeterminado: 3ª pessoa do plural sem referente, ou verbo sem objeto direto + se ('Precisa-se de servidores'). 'Vendem-se casas': se apassivador, 'casas' é sujeito.",
 "Objeto direto: sem preposição; indireto: com preposição ('Obedeceram às ordens'). Predicativo do sujeito (verbo de ligação) × do objeto ('considerar o texto inconstitucional'). Agente da passiva: 'por/de' + agente. Complemento nominal completa um nome e tem valor passivo ('leitura do parecer').",
 "Pegadinha: se apassivador × índice de indeterminação; complemento nominal × adjunto adnominal."],
"21": ["Reescrita: voz, nominalização e deslocamento",
 "Ativa → passiva: o objeto direto vira sujeito e o sujeito vira agente da passiva; o verbo concorda com o novo sujeito ('As emendas foram aprovadas'). 'Aprovaram-se as emendas' equivale à passiva. Só verbo com objeto direto vai à passiva.",
 "Nominalização: 'Ao aprovarem o projeto' = 'Com a aprovação do projeto'. Deslocar termos pode mudar o sentido, em especial palavras de escopo como 'só', 'também', 'até'.",
 "Pegadinha: passiva com troca de papéis; 'Aprovou-se as emendas' (errado)."],
"22": ["Reescrita: gramática disfarçada",
 "O item propõe nova redação e pergunta se mantém correção gramatical e sentido. Cheque nesta ordem: concordância, regência, crase, pontuação, pronomes, conectivo. Um erro basta para a reescrita estar errada.",
 "Exemplos: 'Haviam dúvidas' (errado) → 'Havia dúvidas'; 'Assisti o filme' (errado) → 'Assisti ao filme'; 'Informei ele' (inadequado) → 'Informei-o'; sem a crase em 'Fui a sessão' (errado).",
 "Pegadinha: reescrita correta, mas com sentido alterado (restritiva no lugar de explicativa)."],
"23": ["Reescrita: substituição de expressões",
 "Equivalências: a fim de = para; haja vista = tendo em vista; não obstante / a despeito de = apesar de; tampouco = também não; bem como = e também; porquanto = porque; ao passo que = oposição, proporção ou tempo; senão = exceto, a não ser.",
 "Distinguir senão (conjunção ou prep., 'a não ser') de se não (condição + negação): 'Não fez outra coisa senão reclamar'; 'Se não votar, será multado'.",
 "Pegadinha: trocar concessão por causa (não obstante → em razão de) ou causa por concessão (porquanto → embora)."],
}
PONTOS = {"13":"LP04","14":"LP04","15":"LP04","16":"LP06","17":"LP06","18":"LP06","19":"LP06","20":"LP07","21":"LP03","22":"LP03","23":"LP03"}
if __name__ == "__main__":
    tp = "dados/leis/lp.json"; d = json.load(open(tp, encoding="utf-8"))
    for k, v in ATOMOS.items(): d[k] = v
    json.dump(d, open(tp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bp = "fabrica/blueprints/lp.json"; b = json.load(open(bp, encoding="utf-8"))
    for k, v in ATOMOS.items(): b["rotulos"][k] = v[0]
    json.dump(b, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(ATOMOS), "átomos; total", len(d))
