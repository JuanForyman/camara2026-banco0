# Ciência Política — lote L14
Q = []
TAILS=[" Essa seria a posição predominante na literatura especializada de ciência política.",
 " Trata-se de entendimento consolidado na teoria política contemporânea.",
 " Tal conclusão decorreria, segundo esse entendimento, das características do arranjo institucional descrito.",
 " Essa seria a leitura mais aceita entre os estudiosos do tema."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
FD={"tipo":"doutrina","ref":"doutrina de ciência política; CF e Lei 9.096/1995","versao":"conhecimento do autor","conferida":"conhecimento"}
FJ={"tipo":"jurisprudencia","ref":"jurisprudência e legislação eleitoral","versao":"conhecimento do autor","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, jur=False, lei=False):
    ex = {}
    if lei: ex["fonte"]={"tipo":"lei","ref":"CF; Lei 9.096/1995","versao":"vigente","conferida":"conhecimento"}
    elif jur: ex["fonte"]=FJ; ex["risco"]=["jurisprudencia_conhecimento"]
    else: ex["fonte"]=FD; ex["risco"]=["doutrina_conhecimento"]
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# Q01 Regimes políticos
P("Q01",["1"],"conceito_correto","confusao_instituto",3,
 "Para Robert Dahl, as poliarquias são regimes reais de ampla contestação pública e participação inclusiva, e não a democracia ideal, e entre suas instituições estão eleições livres, justas e frequentes, liberdade de expressão e de associação e fontes alternativas de informação.",
 "Para Robert Dahl, a poliarquia é a democracia ideal, plenamente realizada, em que há igualdade política absoluta entre os cidadãos e participação direta de todos nas decisões, dispensadas eleições periódicas.",
 "Dahl, Poliarquia.","confunde poliarquia com democracia ideal","q01a")
P("Q01",["1"],"conceito_correto","confusao_instituto",3,
 "Segundo Schumpeter, a democracia é um método institucional para chegar a decisões políticas, em que indivíduos adquirem o poder de decidir mediante a competição pelo voto do povo.",
 "Segundo Schumpeter, a democracia é a realização da vontade geral por meio da participação direta e permanente dos cidadãos, o que dispensa a competição entre elites pelo voto.",
 "Schumpeter, Capitalismo, Socialismo e Democracia.","atribui concepção de Rousseau","q01b")
P("Q01",["1"],"conceito_correto","excecao_omitida",3,
 "Na tipologia de Juan Linz, os regimes autoritários se distinguem dos totalitários por apresentarem pluralismo político limitado e baixa mobilização política, sem uma ideologia oficial abrangente e elaborada.",
 "Na tipologia de Juan Linz, os regimes autoritários se distinguem dos totalitários por apresentarem partido único de massa, ideologia oficial abrangente e mobilização política intensa, com controle monopolista dos meios de comunicação.",
 "Linz, regimes totalitários e autoritários.","atribui traços do totalitarismo ao autoritarismo","q01c")
P("Q01",["1"],"conceito_correto","excecao_omitida",4,
 "O conceito de democracia delegativa, de Guillermo O'Donnell, designa regimes em que o presidente eleito se considera autorizado a governar como entender conveniente, com fraca accountability horizontal.",
 "O conceito de democracia delegativa, de Guillermo O'Donnell, designa regimes em que o presidente eleito compartilha o poder com assembleias, com forte accountability horizontal e controle mútuo entre os Poderes.",
 "O'Donnell, democracia delegativa.","inverte accountability","q01d")
P("Q01",["2"],"conceito_correto","excecao_omitida",4,
 "Segundo Huntington, a terceira onda de democratização teve início em 1974, com a transição em Portugal, e foi seguida de países do sul da Europa, da América Latina e do Leste Europeu.",
 "Segundo Huntington, a terceira onda de democratização teve início em 1945, após a Segunda Guerra Mundial, e se encerrou com a queda do Muro de Berlim, em 1989.",
 "Huntington, A Terceira Onda.","troca marco temporal","q01e")
P("Q01",["2"],"conceito_correto","excecao_omitida",4,
 "Na classificação de Arend Lijphart, a democracia majoritária concentra o poder na maioria, com tendência ao bipartidarismo e ao sistema eleitoral majoritário, ao passo que a democracia consensual partilha o poder, com multipartidarismo, representação proporcional e federalismo.",
 "Na classificação de Arend Lijphart, a democracia consensual concentra o poder na maioria, com tendência ao bipartidarismo e ao sistema eleitoral majoritário, ao passo que a democracia majoritária partilha o poder, com multipartidarismo e representação proporcional.",
 "Lijphart, Modelos de Democracia.","inverte modelos","q01f")
P("Q01",["2"],"conceito_correto","excecao_omitida",4,
 "Para Linz e Stepan, a democracia está consolidada quando se torna the only game in town, isto é, quando nenhum ator relevante tenta derrubar o regime democrático e a disputa política se dá segundo suas regras.",
 "Para Linz e Stepan, a democracia está consolidada quando o primeiro governo eleito conclui seu mandato, o que basta para caracterizar a ausência de risco de reversão autoritária.",
 "Linz e Stepan, consolidação democrática.","reduz consolidação a um mandato","q01g")
# Q02 sistemas e formas de governo
P("Q02",["3"],"conceito_correto","confusao_instituto",2,
 "No presidencialismo, o chefe de Estado e o chefe de governo são a mesma pessoa, eleita para mandato fixo, e a sobrevivência do governo não depende da confiança da maioria parlamentar.",
 "No presidencialismo, o chefe de Estado e o chefe de governo são pessoas distintas, e a sobrevivência do governo depende da confiança da maioria parlamentar, que pode destituí-lo por moção de desconfiança.",
 "Sistemas de governo.","atribui traços do parlamentarismo","q02a")
P("Q02",["3"],"conceito_correto","confusao_instituto",3,
 "No parlamentarismo, o Gabinete depende da confiança do Parlamento, e o chefe de Estado, monarca ou presidente, em regra não exerce a chefia do governo.",
 "No parlamentarismo, o Gabinete independe da confiança do Parlamento, e o chefe de Estado exerce a chefia do governo por mandato fixo, não podendo o Parlamento ser dissolvido.",
 "Sistemas de governo.","atribui traços do presidencialismo","q02b")
P("Q02",["3"],"conceito_correto","excecao_omitida",4,
 "O semipresidencialismo caracteriza-se por um Presidente eleito diretamente pelo povo, com poderes relevantes, que convive com um Primeiro-Ministro responsável perante o Parlamento, como ocorre na França.",
 "O semipresidencialismo caracteriza-se por um Presidente escolhido pelo Parlamento, sem poderes relevantes, que convive com um Primeiro-Ministro responsável apenas perante o Presidente, como ocorre na França.",
 "Semipresidencialismo.","troca origem e responsabilidade","q02c")
P("Q02",["3"],"conceito_correto","confusao_instituto",3,
 "Monarquia e república distinguem-se, quanto à forma de governo, pela hereditariedade, vitaliciedade e irresponsabilidade política do monarca, em contraste com a eletividade, a temporariedade e a responsabilidade do governante republicano.",
 "Monarquia e república distinguem-se, quanto à forma de governo, pela eletividade, temporariedade e responsabilidade do monarca, em contraste com a hereditariedade e a vitaliciedade do governante republicano.",
 "Formas de governo.","inverte características","q02d")
P("Q02",["3"],"conceito_correto","excecao_omitida",3,
 "Na federação, os entes possuem autonomia política e repartição constitucional de competências, ao passo que na confederação a união ocorre entre Estados soberanos, com direito de secessão.",
 "Na federação, os entes são soberanos e podem separar-se da união por decisão própria, ao passo que na confederação há autonomia dos entes sem direito de secessão.",
 "Formas de Estado.","atribui soberania e secessão à federação","q02e")
P("Q02",["3"],"caso_concreto","caso_concreto",4,
 "Em um país, o Primeiro-Ministro precisa manter a confiança da maioria parlamentar e pode ser destituído por moção de censura, enquanto o Presidente da República, eleito pelo voto popular direto, nomeia o Primeiro-Ministro e dispõe de poderes próprios em política externa e defesa. Esse arranjo corresponde ao semipresidencialismo.",
 "Em um país, o Primeiro-Ministro precisa manter a confiança da maioria parlamentar e pode ser destituído por moção de censura, enquanto o Presidente da República, eleito pelo voto popular direto, nomeia o Primeiro-Ministro e dispõe de poderes próprios em política externa e defesa. Esse arranjo corresponde ao presidencialismo.",
 "Semipresidencialismo.","classifica como presidencialismo","q02f")
# Q03 representação política
P("Q03",["4"],"conceito_correto","confusao_instituto",3,
 "Para Burke, o representante é um fiduciário, que deve exercer seu julgamento em benefício do interesse nacional, e não um delegado vinculado às instruções de seus eleitores locais, o que corresponde ao mandato livre.",
 "Para Burke, o representante é um delegado, que deve seguir fielmente as instruções de seus eleitores locais, o que corresponde ao mandato imperativo.",
 "Burke, discurso aos eleitores de Bristol.","inverte mandato livre e imperativo","q03a")
P("Q03",["4"],"conceito_correto","excecao_omitida",3,
 "No mandato livre o representante não está juridicamente vinculado às instruções de seus eleitores nem pode ser por eles revogado durante o mandato, ao passo que no mandato imperativo o representante age conforme instruções vinculantes e pode ser revogado.",
 "No mandato imperativo o representante não está vinculado às instruções de seus eleitores, ao passo que no mandato livre ele age conforme instruções vinculantes e pode ser revogado a qualquer tempo.",
 "Mandato livre e imperativo.","inverte mandatos","q03b")
P("Q03",["4"],"conceito_correto","troca_autoridade",3,
 "Segundo a Constituição, o plebiscito é a consulta prévia ao povo sobre determinada matéria, e o referendo é a consulta posterior, para ratificar ou rejeitar ato já editado.",
 "Segundo a Constituição, o referendo é a consulta prévia ao povo sobre determinada matéria, e o plebiscito é a consulta posterior, para ratificar ou rejeitar ato já editado.",
 "CF, art. 14, I e II.","inverte plebiscito e referendo","q03c",lei=True)
P("Q03",["4"],"conceito_correto","excecao_omitida",4,
 "A Constituição consagra a democracia semidireta, ao dispor que todo o poder emana do povo, que o exerce por meio de representantes eleitos ou diretamente, e prevê, como instrumentos de participação direta, o plebiscito, o referendo e a iniciativa popular.",
 "A Constituição consagra a democracia exclusivamente representativa, ao dispor que o poder emana do povo, que o exerce somente por meio de representantes eleitos, sem previsão de instrumentos de participação direta.",
 "CF, art. 1º, parágrafo único, e art. 14.","nega participação direta","q03d",lei=True)
P("Q03",["4"],"conceito_correto","excecao_omitida",4,
 "Para Madison, no Federalista n. 10, a república representativa, em um território extenso, é um meio de controlar os efeitos das facções, em contraste com a democracia direta, mais vulnerável a elas.",
 "Para Madison, no Federalista n. 10, a democracia direta, em território reduzido, é o melhor meio de controlar os efeitos das facções, em contraste com a república representativa em território extenso.",
 "Madison, O Federalista, n. 10.","inverte conclusão","q03e")
P("Q03",["4"],"conceito_correto","confusao_instituto",4,
 "Para Hanna Pitkin, a representação descritiva refere-se à semelhança entre representantes e representados, ao passo que a representação substantiva refere-se à atuação do representante em favor dos interesses dos representados.",
 "Para Hanna Pitkin, a representação substantiva refere-se à semelhança de características entre representantes e representados, ao passo que a representação descritiva refere-se à atuação em favor dos interesses dos representados.",
 "Pitkin, O Conceito de Representação.","inverte descritiva e substantiva","q03f")
# Q04 poderes e relações
P("Q04",["5"],"conceito_correto","confusao_instituto",3,
 "Em Montesquieu, a separação das funções de legislar, executar e julgar em órgãos distintos é concebida como meio de impedir o abuso, pois o poder deve limitar o poder.",
 "Em Montesquieu, a separação das funções de legislar, executar e julgar em órgãos distintos tem por objetivo concentrar o poder no Executivo, para garantir a eficiência do governo.",
 "Montesquieu, O Espírito das Leis.","inverte objetivo","q04a")
P("Q04",["5"],"conceito_correto","excecao_omitida",4,
 "O conceito de presidencialismo de coalizão, de Sérgio Abranches, descreve a combinação, no Brasil, de presidencialismo, federalismo, representação proporcional e multipartidarismo, o que leva o Presidente a formar grandes coalizões para obter maioria no Congresso.",
 "O conceito de presidencialismo de coalizão, de Sérgio Abranches, descreve a combinação, no Brasil, de parlamentarismo, unitarismo e bipartidarismo, o que dispensa o Presidente de formar coalizões para obter maioria no Congresso.",
 "Abranches, Presidencialismo de coalizão.","troca elementos","q04b")
P("Q04",["5"],"conceito_correto","excecao_omitida",5,
 "Segundo Limongi e Figueiredo, o Executivo brasileiro tem forte poder de agenda, devido a prerrogativas como a iniciativa legislativa, as medidas provisórias e o pedido de urgência, e os partidos votam de forma disciplinada, sob o comando de seus líderes.",
 "Segundo Limongi e Figueiredo, o Executivo brasileiro tem fraco poder de agenda, e os partidos votam de forma indisciplinada, de acordo com as preferências individuais dos parlamentares, que agem de forma paroquial.",
 "Limongi e Figueiredo, Executivo e Legislativo na nova ordem constitucional.","inverte conclusão","q04c")
P("Q04",["5"],"conceito_correto","excecao_omitida",3,
 "A Constituição estabelece que são Poderes da União, independentes e harmônicos entre si, o Legislativo, o Executivo e o Judiciário.",
 "A Constituição estabelece que são Poderes da União, harmônicos e subordinados entre si, o Legislativo, o Executivo, o Judiciário e o Ministério Público.",
 "CF, art. 2º.","altera rol e relação","q04d",lei=True)
P("Q04",["5"],"conceito_correto","excecao_omitida",4,
 "A judicialização da política refere-se à transferência, para o Judiciário, de decisões políticas relevantes, favorecida pela ampliação do controle de constitucionalidade e dos legitimados para propor ações diretas.",
 "A judicialização da política refere-se à transferência, para o Legislativo, de decisões que seriam do Judiciário, favorecida pela restrição do controle de constitucionalidade a poucos legitimados.",
 "Judicialização da política.","inverte transferência","q04e")
# Q05 sistemas eleitorais
P("Q05",["6"],"conceito_correto","confusao_instituto",3,
 "No sistema majoritário vence o candidato mais votado, e no Brasil ele é adotado para as eleições de Presidente, Governador, Prefeito e Senador, ao passo que o sistema proporcional é adotado para Deputados Federais, Estaduais e Distritais e Vereadores.",
 "No sistema proporcional vence o candidato mais votado, e no Brasil ele é adotado para as eleições de Presidente, Governador e Senador, ao passo que o sistema majoritário é adotado para Deputados Federais e Vereadores.",
 "Sistemas eleitorais brasileiros.","inverte sistemas","q05a")
P("Q05",["6"],"conceito_correto","troca_numero",3,
 "O quociente eleitoral é obtido pela divisão dos votos válidos pelo número de cadeiras em disputa, e o quociente partidário, pela divisão dos votos do partido pelo quociente eleitoral.",
 "O quociente eleitoral é obtido pela divisão dos votos totais, incluídos brancos e nulos, pelo número de partidos, e o quociente partidário, pela divisão dos votos do partido pelo número de cadeiras.",
 "Quociente eleitoral e partidário.","troca fórmulas","q05b")
P("Q05",["6"],"conceito_correto","excecao_omitida",3,
 "Segundo a lei de Duverger, o sistema majoritário de turno único tende ao bipartidarismo, ao passo que a representação proporcional tende ao multipartidarismo.",
 "Segundo a lei de Duverger, o sistema majoritário de turno único tende ao multipartidarismo, ao passo que a representação proporcional tende ao bipartidarismo.",
 "Duverger, leis sociológicas.","inverte tendências","q05c")
P("Q05",["6"],"conceito_correto","excecao_omitida",4,
 "Para Duverger, o efeito mecânico do sistema eleitoral decorre da forma como os votos se convertem em cadeiras, e o efeito psicológico, do comportamento dos eleitores que evitam o desperdício do voto em partidos sem chances, o chamado voto útil.",
 "Para Duverger, o efeito psicológico do sistema eleitoral decorre da forma como os votos se convertem em cadeiras, e o efeito mecânico, do comportamento dos eleitores que evitam o desperdício do voto, o chamado voto útil.",
 "Duverger, efeitos mecânico e psicológico.","inverte efeitos","q05d")
P("Q05",["6"],"conceito_correto","excecao_omitida",3,
 "No sistema distrital puro, o território é dividido em distritos e, em cada um, elege-se um representante pelo critério majoritário, ao passo que, no distrital misto, parte das cadeiras é preenchida por voto distrital e parte por lista proporcional.",
 "No sistema distrital puro, as cadeiras são distribuídas entre os partidos em proporção aos votos obtidos em todo o território, ao passo que, no distrital misto, todas as cadeiras são preenchidas por voto majoritário.",
 "Sistemas distritais.","confunde distrital e proporcional","q05e")
P("Q05",["6"],"conceito_correto","troca_numero",3,
 "No Brasil, nos municípios com mais de duzentos mil eleitores, a eleição do Prefeito ocorre pelo sistema majoritário em dois turnos, se nenhum candidato alcançar a maioria absoluta dos votos válidos no primeiro.",
 "No Brasil, nos municípios com mais de cem mil eleitores, a eleição do Prefeito ocorre pelo sistema majoritário em turno único, vencendo o candidato que obtiver mais votos, sem exigência de maioria absoluta.",
 "CF, art. 29, II.","troca número de eleitores e turnos","q05f",lei=True)
P("Q05",["6"],"conceito_correto","excecao_omitida",4,
 "A lista aberta, adotada no Brasil nas eleições proporcionais, permite ao eleitor votar em candidato, e a ordem de eleição dos candidatos de cada partido é definida pelo número de votos nominais que recebem.",
 "A lista fechada, adotada no Brasil nas eleições proporcionais, permite ao eleitor votar somente na legenda, e a ordem de eleição dos candidatos de cada partido é definida pelo partido antes da eleição.",
 "Lista aberta e fechada.","troca lista aberta por fechada","q05g")
# Q06 partidos
P("Q06",["7"],"conceito_correto","confusao_instituto",3,
 "Para Duverger, os partidos de quadros caracterizam-se por reunir notáveis, com caráter predominantemente eleitoral, ao passo que os partidos de massas se organizam com grande número de filiados e se financiam por suas contribuições.",
 "Para Duverger, os partidos de massas caracterizam-se por reunir notáveis, com caráter predominantemente eleitoral, ao passo que os partidos de quadros se organizam com grande número de filiados e se financiam por suas contribuições.",
 "Duverger, Os Partidos Políticos.","inverte quadros e massas","q06a")
P("Q06",["7"],"conceito_correto","excecao_omitida",3,
 "A lei de ferro da oligarquia, de Robert Michels, afirma que a organização partidária tende a concentrar o poder em uma elite dirigente, mesmo em partidos que se declaram democráticos.",
 "A lei de ferro da oligarquia, de Robert Michels, afirma que a organização partidária tende a distribuir o poder igualmente entre os filiados, especialmente nos partidos que se declaram democráticos.",
 "Michels, Sociologia dos Partidos Políticos.","inverte conclusão","q06b")
P("Q06",["7"],"conceito_correto","confusao_instituto",4,
 "O partido catch-all, formulado por Kirchheimer, atenua a ideologia para ampliar seu eleitorado, ao passo que o partido cartel, formulado por Katz e Mair, aproxima-se do Estado e depende de recursos públicos.",
 "O partido catch-all, formulado por Kirchheimer, aproxima-se do Estado e depende de recursos públicos, ao passo que o partido cartel, formulado por Katz e Mair, atenua a ideologia para ampliar seu eleitorado.",
 "Kirchheimer; Katz e Mair.","inverte catch-all e cartel","q06c")
P("Q06",["7"],"conceito_correto","excecao_omitida",4,
 "Para Sartori, os sistemas partidários classificam-se pelo número de partidos relevantes e pela distância ideológica entre eles, o que permite distinguir o pluralismo moderado do pluralismo polarizado.",
 "Para Sartori, os sistemas partidários classificam-se apenas pelo número total de partidos registrados, sendo irrelevante a distância ideológica entre eles.",
 "Sartori, Partidos e Sistemas Partidários.","ignora relevância e distância ideológica","q06d")
P("Q06",["7"],"conceito_correto","excecao_omitida",3,
 "Entre as funções clássicas dos partidos políticos estão a agregação de interesses, o recrutamento de elites políticas, a organização do governo e a estruturação do debate político.",
 "Entre as funções clássicas dos partidos políticos estão o julgamento de litígios eleitorais, a fiscalização do pleito e a diplomação dos eleitos.",
 "Funções dos partidos.","atribui funções da Justiça Eleitoral","q06e")
P("Q06",["8"],"conceito_correto","excecao_omitida",3,
 "No Brasil, os partidos políticos são pessoas jurídicas de direito privado, que adquirem personalidade jurídica na forma da lei civil e registram seus estatutos no Tribunal Superior Eleitoral.",
 "No Brasil, os partidos políticos são pessoas jurídicas de direito público, que adquirem personalidade jurídica mediante registro de seus estatutos no Tribunal Superior Eleitoral.",
 "CF, art. 17, § 2º.","atribui natureza de direito público","q06f",lei=True)
P("Q06",["8"],"conceito_correto","excecao_omitida",4,
 "A Constituição veda a celebração de coligações nas eleições proporcionais, e as federações partidárias permitem a atuação conjunta de dois ou mais partidos, como se fossem uma única agremiação, pelo prazo mínimo de quatro anos.",
 "A Constituição veda a celebração de coligações nas eleições majoritárias, e as federações partidárias permitem a atuação conjunta de dois ou mais partidos, como se fossem uma única agremiação, sem prazo mínimo de duração.",
 "CF, art. 17, § 1º; Lei 9.096/1995, art. 11-A.","troca eleições vedadas e prazo","q06g",lei=True)
P("Q06",["8"],"conceito_correto","troca_numero",4,
 "A cláusula de desempenho condiciona o acesso aos recursos do fundo partidário e ao tempo gratuito de rádio e televisão, e seu percentual de votos válidos cresce gradualmente, tendo sido de 2% em 2022, e de 2,5% em 2026.",
 "A cláusula de desempenho condiciona o registro do partido no Tribunal Superior Eleitoral, e seu percentual de votos válidos é fixo, de 1,5%, para todas as eleições.",
 "CF, art. 17, § 3º; EC 97/2017.","troca efeito e percentual","q06h",lei=True)
P("Q06",["8"],"conceito_correto","excecao_omitida",3,
 "A Constituição assegura aos partidos autonomia para definir sua estrutura interna, organização e funcionamento, vedando o recebimento de recursos de entidade ou governo estrangeiros e a subordinação a estes.",
 "A Constituição assegura aos partidos autonomia para definir sua estrutura interna, organização e funcionamento, permitindo o recebimento de recursos de governos estrangeiros, desde que declarados à Justiça Eleitoral.",
 "CF, art. 17.","admite recursos estrangeiros","q06i",lei=True)
# Q07 organização política brasileira
P("Q07",["9"],"conceito_correto","excecao_omitida",2,
 "O voto no Brasil é obrigatório para os maiores de dezoito anos e facultativo para os analfabetos, os maiores de setenta anos e os maiores de dezesseis e menores de dezoito anos.",
 "O voto no Brasil é obrigatório para os maiores de dezesseis anos e facultativo para os analfabetos e os maiores de sessenta e cinco anos.",
 "CF, art. 14, § 1º.","troca idades","q07a",lei=True)
P("Q07",["9"],"conceito_correto","excecao_omitida",3,
 "A organização político-administrativa da República Federativa do Brasil compreende a União, os Estados, o Distrito Federal e os Municípios, todos autônomos, nos termos da Constituição.",
 "A organização político-administrativa da República Federativa do Brasil compreende a União, os Estados, o Distrito Federal, os Municípios e os Territórios Federais, todos soberanos, nos termos da Constituição.",
 "CF, art. 18.","inclui territórios e soberania","q07b",lei=True)
P("Q07",["9"],"conceito_correto","troca_autoridade",3,
 "O pluralismo político é um dos fundamentos da República Federativa do Brasil, ao lado da soberania, da cidadania, da dignidade da pessoa humana e dos valores sociais do trabalho e da livre iniciativa.",
 "O pluralismo político é um dos objetivos da República Federativa do Brasil, ao lado da construção de uma sociedade livre, justa e solidária e da erradicação da pobreza.",
 "CF, art. 1º e art. 3º.","troca fundamento por objetivo","q07c",lei=True)
P("Q07",["9"],"conceito_correto","excecao_omitida",4,
 "O plebiscito de 1993, previsto no ADCT, consultou o eleitorado sobre a forma e o sistema de governo, e resultou na manutenção da república e do presidencialismo.",
 "O plebiscito de 1993, previsto no ADCT, consultou o eleitorado sobre a forma e o sistema de governo, e resultou na adoção da república e do parlamentarismo.",
 "ADCT, art. 2º.","troca resultado","q07d",lei=True)
# Q08 política internacional
P("Q08",["10"],"conceito_correto","excecao_omitida",3,
 "Entre os princípios que regem as relações internacionais do Brasil estão a independência nacional, a prevalência dos direitos humanos, a autodeterminação dos povos, a não intervenção, a igualdade entre os Estados e a defesa da paz.",
 "Entre os princípios que regem as relações internacionais do Brasil estão a intervenção humanitária, a hierarquia entre os Estados, a primazia do comércio exterior e o alinhamento automático às potências.",
 "CF, art. 4º.","troca princípios","q08a",lei=True)
P("Q08",["10"],"conceito_correto","excecao_omitida",3,
 "A Constituição estabelece que o Brasil buscará a integração econômica, política, social e cultural dos povos da América Latina, visando à formação de uma comunidade latino-americana de nações.",
 "A Constituição estabelece que o Brasil buscará a integração econômica dos povos da América do Sul, com a criação de uma moeda única e a abdicação de parcela de sua soberania.",
 "CF, art. 4º, parágrafo único.","altera âmbito e efeitos","q08b",lei=True)
P("Q08",["10"],"conceito_correto","excecao_omitida",3,
 "A Paz de Westfália, de 1648, é tradicionalmente apontada como marco do sistema de Estados soberanos, fundado nos princípios da soberania territorial e da não intervenção.",
 "A Paz de Westfália, de 1648, é tradicionalmente apontada como marco do fim do sistema de Estados soberanos e da criação de um governo mundial supranacional.",
 "Ordem westfaliana.","inverte significado","q08c")
P("Q08",["10"],"conceito_correto","excecao_omitida",4,
 "O Conselho de Segurança da ONU é composto por cinco membros permanentes com direito de veto, a saber, Estados Unidos, Rússia, China, Reino Unido e França.",
 "O Conselho de Segurança da ONU é composto por cinco membros permanentes sem direito de veto, a saber, Estados Unidos, Alemanha, China, Japão e França.",
 "ONU, Conselho de Segurança.","troca membros e veto","q08d")
P("Q08",["10"],"conceito_correto","excecao_omitida",4,
 "Para a perspectiva realista das relações internacionais, os Estados são os atores centrais em um sistema internacional anárquico, em que poder e segurança são os principais objetivos, ao passo que a perspectiva liberal destaca o papel das instituições e da cooperação.",
 "Para a perspectiva realista das relações internacionais, as organizações internacionais são os atores centrais, e a cooperação institucional é o principal objetivo, ao passo que a perspectiva liberal destaca o poder e a segurança dos Estados.",
 "Teorias das relações internacionais.","inverte realismo e liberalismo","q08e")
# Q09 teoria do Estado
P("Q09",["11"],"conceito_correto","excecao_omitida",3,
 "Os elementos constitutivos do Estado são o povo, o território e o governo soberano, e a nacionalidade distingue o povo, conjunto de nacionais, da população, conjunto de pessoas que residem no território.",
 "Os elementos constitutivos do Estado são o povo, o território e a nação, e a população se distingue do povo por abranger somente os nacionais residentes no território.",
 "Teoria do Estado, elementos.","troca elementos e conceito de população","q09a")
P("Q09",["11"],"conceito_correto","confusao_instituto",3,
 "Para Hobbes, o estado de natureza é uma guerra de todos contra todos, e os indivíduos pactuam a submissão a um soberano absoluto, para garantir a paz e a segurança.",
 "Para Hobbes, o estado de natureza é um estado de paz e de liberdade, e os indivíduos pactuam a criação de um governo limitado, com direito de resistência, para proteger a propriedade.",
 "Hobbes, Leviatã.","atribui ideia de Locke","q09b")
P("Q09",["11"],"conceito_correto","confusao_instituto",4,
 "Para Locke, o governo se funda no consentimento e tem por finalidade proteger os direitos naturais à vida, à liberdade e à propriedade, admitindo-se o direito de resistência quando o governo viola a confiança.",
 "Para Locke, o governo se funda na vontade geral e tem por finalidade a submissão total dos indivíduos ao soberano, sendo vedado o direito de resistência.",
 "Locke, Segundo Tratado sobre o Governo.","atribui ideias de Hobbes e Rousseau","q09c")
P("Q09",["11"],"conceito_correto","excecao_omitida",4,
 "Para Rousseau, a soberania pertence ao povo, expressa-se na vontade geral e é inalienável e indivisível.",
 "Para Rousseau, a soberania pertence ao monarca, expressa-se na vontade de todos e é alienável e divisível entre os Poderes.",
 "Rousseau, Do Contrato Social.","troca titular e características","q09d")
P("Q09",["11"],"conceito_correto","excecao_omitida",3,
 "Segundo Weber, o Estado é a comunidade humana que reivindica, com êxito, o monopólio do uso legítimo da força física dentro de um determinado território.",
 "Segundo Weber, o Estado é a comunidade humana que reivindica, com êxito, o monopólio da propriedade dos meios de produção dentro de um determinado território.",
 "Weber, A Política como Vocação.","troca monopólio","q09e")
P("Q09",["11"],"conceito_correto","confusao_instituto",3,
 "Os tipos puros de dominação legítima, em Weber, são a tradicional, fundada no costume, a carismática, fundada no dom do líder, e a legal-racional, fundada em regras impessoais.",
 "Os tipos puros de dominação legítima, em Weber, são a tradicional, fundada em regras impessoais, a carismática, fundada no costume, e a legal-racional, fundada no dom do líder.",
 "Weber, tipos de dominação.","troca fundamentos","q09f")
P("Q09",["11"],"conceito_correto","excecao_omitida",4,
 "Em Maquiavel, a política possui autonomia em relação à moral tradicional, e a conservação do poder exige do príncipe virtù para enfrentar a fortuna.",
 "Em Maquiavel, a política subordina-se à moral cristã, e a conservação do poder depende da vontade divina, sendo irrelevante a virtù do príncipe.",
 "Maquiavel, O Príncipe.","subordina política à moral","q09g")
P("Q09",["12"],"conceito_correto","excecao_omitida",4,
 "Segundo Tilly, a guerra foi decisiva para a formação dos Estados europeus, porque a necessidade de extrair recursos para a guerra impulsionou a construção de um aparato fiscal e administrativo.",
 "Segundo Tilly, a guerra foi irrelevante para a formação dos Estados europeus, que resultaram do consentimento voluntário entre os povos, sem necessidade de aparato fiscal e administrativo.",
 "Tilly, Coerção, Capital e Estados Europeus.","nega papel da guerra","q09h")
P("Q09",["12"],"conceito_correto","troca_numero",3,
 "A Paz de Westfália, de 1648, consagrou a soberania territorial dos Estados, e as revoluções liberais inglesa, americana e francesa ocorreram, respectivamente, em 1688, 1776 e 1789.",
 "A Paz de Westfália, de 1648, consagrou o império universal do Papa, e as revoluções liberais inglesa, americana e francesa ocorreram, respectivamente, em 1789, 1688 e 1776.",
 "Formação dos Estados nacionais.","troca datas e conteúdo","q09i")
P("Q09",["12"],"conceito_correto","confusao_instituto",3,
 "O Estado social, ou de bem-estar, caracteriza-se pelo reconhecimento de direitos sociais e pela atuação estatal na provisão de serviços, ao passo que o Estado liberal clássico se caracteriza pela limitação do poder e pela proteção das liberdades individuais.",
 "O Estado liberal clássico caracteriza-se pelo reconhecimento de direitos sociais e pela ampla atuação estatal na provisão de serviços, ao passo que o Estado social se caracteriza pela abstenção estatal e pelo Estado mínimo.",
 "Estado liberal e social.","inverte características","q09j")
# Q10 formação do Estado brasileiro
P("Q10",["13"],"conceito_correto","excecao_omitida",3,
 "Para Raymundo Faoro, em Os Donos do Poder, o patrimonialismo estamental, com um estamento burocrático que se apropria do aparelho do Estado, é herança da formação portuguesa e marcou a vida política brasileira.",
 "Para Raymundo Faoro, em Os Donos do Poder, o Estado brasileiro nasceu de uma burguesia industrial autônoma, que submeteu o aparelho estatal aos interesses de mercado, rompendo com a herança portuguesa.",
 "Faoro, Os Donos do Poder.","nega patrimonialismo","q10a")
P("Q10",["13"],"conceito_correto","confusao_instituto",3,
 "Para Sérgio Buarque de Holanda, em Raízes do Brasil, o homem cordial expressa a dificuldade de separar o público do privado, em razão do predomínio das relações pessoais e afetivas na vida social e política.",
 "Para Sérgio Buarque de Holanda, em Raízes do Brasil, o homem cordial expressa a ética protestante, o que explica a nítida separação entre o público e o privado e a impessoalidade nas relações políticas.",
 "Buarque de Holanda, Raízes do Brasil.","atribui impessoalidade","q10b")
P("Q10",["13"],"conceito_correto","excecao_omitida",4,
 "Para Victor Nunes Leal, o coronelismo resulta de um sistema de compromisso entre o poder público, em crescente fortalecimento, e o poder privado, decadente, dos grandes proprietários rurais.",
 "Para Victor Nunes Leal, o coronelismo resulta de uma ruptura entre o poder público e o poder privado dos grandes proprietários rurais, o que levou à extinção do mandonismo local na Primeira República.",
 "Nunes Leal, Coronelismo, Enxada e Voto.","nega compromisso","q10c")
P("Q10",["13"],"conceito_correto","excecao_omitida",4,
 "Para José Murilo de Carvalho, no Brasil os direitos sociais antecederam os direitos políticos e civis, em contraste com a sequência inglesa descrita por Marshall, que parte dos direitos civis, passa pelos políticos e chega aos sociais.",
 "Para José Murilo de Carvalho, no Brasil a cidadania seguiu a sequência inglesa descrita por Marshall, com os direitos civis, depois os políticos e por fim os sociais, em um processo linear e sem inversões.",
 "Carvalho, Cidadania no Brasil.","nega inversão da sequência","q10d")
P("Q10",["13"],"conceito_correto","confusao_instituto",4,
 "A cidadania regulada, de Wanderley Guilherme dos Santos, designa o arranjo em que os direitos dependem da inserção do trabalhador em ocupação reconhecida e regulada pelo Estado, o que deixou à margem trabalhadores sem carteira de trabalho.",
 "A cidadania regulada, de Wanderley Guilherme dos Santos, designa o arranjo em que os direitos são universais e independem da ocupação profissional, o que assegurou proteção a todos os trabalhadores, com ou sem carteira de trabalho.",
 "Santos, Cidadania e Justiça.","atribui universalidade","q10e")
P("Q10",["13"],"conceito_correto","troca_numero",3,
 "Entre os marcos da formação política brasileira estão a Independência, em 1822, a Proclamação da República, em 1889, a Revolução de 1930, o Estado Novo, em 1937, o golpe de 1964 e a Constituição de 1988.",
 "Entre os marcos da formação política brasileira estão a Independência, em 1808, a Proclamação da República, em 1899, a Revolução de 1930, o Estado Novo, em 1947, o golpe de 1964 e a Constituição de 1988.",
 "Cronologia política brasileira.","troca datas","q10f")
# Q11 história do voto e dos partidos
P("Q11",["14"],"conceito_correto","excecao_omitida",3,
 "A Constituição de 1824 adotou o voto censitário e as eleições indiretas em dois graus, e a Lei Saraiva, de 1881, instituiu a eleição direta, mantendo o critério censitário e excluindo os analfabetos.",
 "A Constituição de 1824 adotou o voto universal e direto, e a Lei Saraiva, de 1881, instituiu as eleições indiretas, assegurando o direito de voto aos analfabetos.",
 "História do voto no Império.","inverte sistemas e inclusão","q11a")
P("Q11",["14"],"conceito_correto","excecao_omitida",4,
 "O Código Eleitoral de 1932 instituiu o voto secreto, o voto feminino, a Justiça Eleitoral e a representação proporcional.",
 "O Código Eleitoral de 1932 manteve o voto aberto, vedou o voto feminino e atribuiu a verificação dos poderes ao Poder Legislativo, sem criar a Justiça Eleitoral.",
 "Código Eleitoral de 1932.","nega inovações","q11b")
P("Q11",["14"],"conceito_correto","troca_numero",3,
 "O voto dos analfabetos foi permitido pela Emenda Constitucional 25/1985, e a Constituição de 1988 o manteve de forma facultativa, assim como o voto dos maiores de setenta anos e dos maiores de dezesseis e menores de dezoito anos.",
 "O voto dos analfabetos foi permitido pela Constituição de 1934, e a Constituição de 1988 o tornou obrigatório, assim como o voto dos maiores de setenta anos e dos maiores de dezesseis anos.",
 "História do voto no Brasil.","troca marco e obrigatoriedade","q11c")
P("Q11",["14"],"conceito_correto","excecao_omitida",4,
 "A Constituição de 1891 aboliu o critério censitário para o voto, mas manteve a exclusão dos analfabetos e das mulheres, e o voto era aberto.",
 "A Constituição de 1891 manteve o critério censitário para o voto, mas assegurou o voto às mulheres e aos analfabetos, e o voto era secreto.",
 "Primeira República.","troca características","q11d")
P("Q11",["15"],"conceito_correto","troca_numero",3,
 "O Ato Institucional n. 2, de 1965, extinguiu os partidos existentes, e o Ato Complementar n. 4, de 1966, viabilizou a criação de duas organizações, a ARENA e o MDB, instituindo o bipartidarismo.",
 "O Ato Institucional n. 5, de 1968, extinguiu os partidos existentes, e o Ato Complementar n. 4, de 1966, viabilizou a criação de três organizações, a ARENA, o MDB e o PTB, instituindo o tripartidarismo.",
 "Bipartidarismo no regime militar.","troca ato e número de partidos","q11e")
P("Q11",["15"],"conceito_correto","excecao_omitida",3,
 "A reforma partidária de 1979 extinguiu o bipartidarismo e restabeleceu o pluripartidarismo, e a Constituição de 1988 assegurou ampla liberdade de criação de partidos.",
 "A reforma partidária de 1979 consolidou o bipartidarismo, e a Constituição de 1988 restabeleceu a exigência de autorização prévia do Estado para a criação de partidos.",
 "Lei 6.767/1979; CF, art. 17.","inverte reforma","q11f")
P("Q11",["15"],"conceito_correto","excecao_omitida",4,
 "A Emenda Constitucional 97/2017 vedou as coligações nas eleições proporcionais a partir de 2020 e instituiu a cláusula de desempenho, de aplicação gradual.",
 "A Emenda Constitucional 97/2017 vedou as coligações nas eleições majoritárias a partir de 2020 e instituiu a cláusula de desempenho, de aplicação imediata e com percentual fixo.",
 "EC 97/2017.","troca eleições e gradualidade","q11g",lei=True)
P("Q11",["15"],"conceito_correto","excecao_omitida",3,
 "No Império, os principais partidos eram o Conservador e o Liberal, e a alternância entre os gabinetes era mediada pelo Poder Moderador do Imperador.",
 "No Império, os principais partidos eram o PSD e a UDN, e a alternância entre os gabinetes era definida diretamente pelo voto popular, sem interferência do Imperador.",
 "Partidos no Império.","anacronismo e nega Poder Moderador","q11h")
