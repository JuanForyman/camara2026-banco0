# Lei 8.429/92 (com Lei 14.230/21) — lote L3, parte c (Q13–Q16: prescrição, custas/capacitação, jurisprudência, casos integrados)
JUR = lambda tipo, ref: {"fonte": {"tipo": tipo, "ref": ref, "conferida": "conhecimento"}, "risco": ["jurisprudencia_mutavel"]}
Q = []
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# ---- Q13
P("Q13",["23"],"conceito_correto","troca_numero",2,
 "A ação para a aplicação das sanções da Lei de Improbidade prescreve em oito anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência.",
 "A ação para a aplicação das sanções da Lei de Improbidade prescreve em dez anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que o ato foi conhecido pelo poder público.",
 "Art. 23, caput: 8 anos; fato ou cessação da permanência.","troca prazo e termo inicial","q13a")
P("Q13",["23"],"conceito_correto","troca_numero",3,
 "A instauração de inquérito civil ou de processo administrativo para apuração dos ilícitos suspende o curso do prazo prescricional por, no máximo, cento e oitenta dias corridos, recomeçando a correr após a sua conclusão ou, não concluído o processo, esgotado o prazo de suspensão.",
 "A instauração de inquérito civil ou de processo administrativo para apuração dos ilícitos interrompe o curso do prazo prescricional, que recomeça por inteiro após a conclusão da apuração, não havendo limite de tempo para essa causa interruptiva.",
 "Art. 23, § 1.º: suspensão, até 180 dias.","confunde suspensão com interrupção","q13b")
P("Q13",["23"],"conceito_correto","troca_numero",3,
 "O inquérito civil para apuração do ato de improbidade será concluído no prazo de trezentos e sessenta e cinco dias corridos, prorrogável uma única vez por igual período, mediante ato fundamentado submetido à revisão da instância competente do órgão ministerial.",
 "O inquérito civil para apuração do ato de improbidade será concluído no prazo de cento e oitenta dias corridos, prorrogável por períodos sucessivos, mediante ato fundamentado do próprio membro do Ministério Público que o presidir.",
 "Art. 23, § 2.º.","troca prazo e prorrogações","q13c")
P("Q13",["23"],"conceito_correto","troca_numero",3,
 "Encerrado o prazo do inquérito civil, a ação deverá ser proposta no prazo de trinta dias, se não for caso de arquivamento do inquérito civil.",
 "Encerrado o prazo do inquérito civil, a ação deverá ser proposta no prazo de sessenta dias, sob pena de preclusão da pretensão sancionadora quanto aos atos apurados.",
 "Art. 23, § 3.º.","troca prazo e efeito","q13d")
P("Q13",["23"],"conceito_correto","excecao_omitida",4,
 "O prazo da prescrição interrompe-se pelo ajuizamento da ação, pela publicação da sentença condenatória e pela publicação de decisão ou acórdão de tribunal que confirma sentença condenatória ou reforma sentença de improcedência.",
 "O prazo da prescrição interrompe-se pela instauração do inquérito civil, pelo ajuizamento da ação e pela publicação da sentença condenatória, recomeçando a correr por inteiro após cada causa interruptiva.",
 "Art. 23, § 4.º: a instauração do inquérito suspende (§ 1.º), não interrompe; e o recomeço é pela metade (§ 5.º).","troca marcos e recomeço","q13e")
P("Q13",["23"],"conceito_correto","troca_numero",3,
 "Interrompida a prescrição, o prazo recomeça a correr do dia da interrupção, pela metade do prazo previsto no caput do art. 23, ou seja, em quatro anos.",
 "Interrompida a prescrição, o prazo recomeça a correr do dia da interrupção, por inteiro, ou seja, em oito anos, salvo na hipótese de sentença condenatória, em que será de quatro anos.",
 "Art. 23, § 5.º.","recomeço integral","q13f")
P("Q13",["23"],"conceito_correto","troca_efeito",3,
 "A suspensão e a interrupção da prescrição produzem efeitos relativamente a todos os que concorreram para a prática do ato de improbidade, e, nos atos conexos objeto do mesmo processo, estendem-se aos demais.",
 "A suspensão e a interrupção da prescrição produzem efeitos apenas em relação ao réu contra quem foi praticado o ato processual, sendo individuais para cada um dos que concorreram para o ato de improbidade.",
 "Art. 23, §§ 6.º e 7.º.","individualiza os efeitos","q13g")
P("Q13",["23"],"conceito_correto","excecao_omitida",3,
 "O juiz ou tribunal, depois de ouvido o Ministério Público, deverá, de ofício ou a requerimento da parte, reconhecer a prescrição intercorrente da pretensão sancionadora e decretá-la de imediato, se, entre os marcos interruptivos, transcorrer o prazo de recomeço.",
 "O juiz ou tribunal somente poderá reconhecer a prescrição intercorrente da pretensão sancionadora a requerimento da parte interessada, sendo vedado o reconhecimento de ofício, e a decisão dependerá de oitiva do réu.",
 "Art. 23, § 8.º.","exige requerimento","q13h")
P("Q13",["23"],"caso_concreto","caso_concreto",5,
 "Ação de improbidade foi ajuizada em 2022. Sentença condenatória publicada em abril de 2022. O acórdão do Tribunal de Justiça que a confirmou foi publicado somente em setembro de 2026, ou seja, mais de quatro anos e meio depois. Nessa hipótese, em tese, a prescrição intercorrente pode ser reconhecida, já que entre os marcos interruptivos transcorreu prazo superior à metade do prazo do caput.",
 "Ação de improbidade foi ajuizada em 2022. Sentença condenatória publicada em abril de 2022. O acórdão do Tribunal de Justiça que a confirmou foi publicado somente em setembro de 2026, ou seja, mais de quatro anos e meio depois. Nessa hipótese, não há prescrição intercorrente, pois esta só ocorre quando o intervalo entre os marcos interruptivos supera oito anos.",
 "Art. 23, §§ 5.º e 8.º. Raciocínio da lei: intervalo > 4 anos entre marcos interruptivos. Aplicação a fatos anteriores à Lei 14.230/21 foi limitada pelo Tema 1199/STF.","adota o prazo do caput na intercorrente","q13i",
 {"risco": ["marcos_temporais"]})
# ---- Q14
P("Q14",["23A"],"conceito_correto","troca_efeito",2,
 "É dever do poder público oferecer contínua capacitação aos agentes públicos e políticos que atuem com prevenção ou repressão de atos de improbidade administrativa.",
 "É faculdade do poder público, a depender de disponibilidade orçamentária, oferecer capacitação aos agentes públicos e políticos que atuem com prevenção ou repressão de atos de improbidade administrativa.",
 "Art. 23-A.","transforma dever em faculdade","q14a")
P("Q14",["23B"],"conceito_correto","excecao_omitida",3,
 "Nas ações e nos acordos regidos pela Lei de Improbidade, não haverá adiantamento de custas, de preparo, de emolumentos, de honorários periciais e de quaisquer outras despesas, e, no caso de procedência, as custas e demais despesas serão pagas ao final.",
 "Nas ações regidas pela Lei de Improbidade, o autor, ainda que seja o Ministério Público, deverá adiantar os honorários periciais, ficando dispensado apenas do pagamento de custas e emolumentos, que serão pagos ao final no caso de procedência.",
 "Art. 23-B, caput e § 1.º.","exige adiantamento de perícia","q14b")
P("Q14",["23B"],"conceito_correto","excecao_omitida",3,
 "Haverá condenação em honorários sucumbenciais em caso de improcedência da ação de improbidade se comprovada má-fé.",
 "Haverá condenação do autor em honorários sucumbenciais em todo caso de improcedência da ação de improbidade, em razão do princípio da causalidade, independentemente de má-fé.",
 "Art. 23-B, § 2.º.","dispensa má-fé","q14c")
P("Q14",["23C"],"conceito_correto","confusao_instituto",3,
 "Os atos que ensejem enriquecimento ilícito, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação de recursos públicos dos partidos políticos ou de suas fundações serão responsabilizados nos termos da Lei dos Partidos Políticos (Lei n.º 9.096/1995).",
 "Os atos que ensejem enriquecimento ilícito, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação de recursos públicos dos partidos políticos ou de suas fundações serão responsabilizados pela Lei de Improbidade Administrativa, nos termos dos arts. 9.º e 10.",
 "Art. 23-C.","aplica a LIA a partidos","q14d")
P("Q14",["19"],"conceito_correto","troca_efeito",3,
 "Constitui crime a representação por ato de improbidade contra agente público ou terceiro beneficiário, quando o autor da denúncia o sabe inocente, ficando o denunciante sujeito, além da sanção penal, a indenizar o denunciado pelos danos materiais, morais ou à imagem que houver provocado.",
 "Constitui crime a representação por ato de improbidade contra agente público ou terceiro beneficiário cuja ação for julgada improcedente, independentemente do conhecimento do denunciante sobre a inocência do denunciado, ficando ele sujeito à indenização por danos materiais.",
 "Art. 19: crime só quando o denunciante sabe inocente; indenização por danos materiais, morais ou à imagem.","objetiviza o crime","q14e")
# ---- Q15 (jurisprudência e direito intertemporal)
P("Q15",["1","10"],"jurisprudencia","jurisprudencia",4,
 "Segundo o Supremo Tribunal Federal (Tema 1.199), é necessária a presença do elemento subjetivo dolo para a tipificação dos atos de improbidade administrativa, exigindo-se, nos arts. 9.º, 10 e 11 da Lei n.º 8.429/1992, a presença do dolo.",
 "Segundo o Supremo Tribunal Federal (Tema 1.199), é suficiente a culpa grave para a tipificação dos atos de improbidade que causam lesão ao erário, exigindo-se dolo apenas nos arts. 9.º e 11 da Lei n.º 8.429/1992.",
 "STF, Tema 1.199 (ARE 843.989), tese 1.","admite culpa grave","q15a",JUR("tema_repercussao","STF, Tema 1.199"))
P("Q15",["1","10"],"jurisprudencia","jurisprudencia",5,
 "Segundo o Tema 1.199 do STF, a norma mais benéfica da Lei n.º 14.230/2021, que revogou a modalidade culposa do art. 10, é irretroativa quanto às condenações com trânsito em julgado e à execução das penas, mas se aplica aos atos culposos praticados na vigência do texto anterior se ainda não houver condenação transitada em julgado, cabendo ao juízo analisar eventual dolo do agente.",
 "Segundo o Tema 1.199 do STF, a norma mais benéfica da Lei n.º 14.230/2021, que revogou a modalidade culposa do art. 10, retroage para alcançar as condenações já transitadas em julgado, devendo o juízo da execução extinguir as penas impostas por atos culposos.",
 "STF, Tema 1.199, tese 2 e 3: irretroatividade quanto à coisa julgada e à execução; aplicação às ações em curso sem condenação definitiva.","retroatividade sobre coisa julgada","q15b",JUR("tema_repercussao","STF, Tema 1.199"))
P("Q15",["23"],"jurisprudencia","jurisprudencia",5,
 "Segundo o Tema 1.199 do STF, o novo regime prescricional da Lei n.º 14.230/2021 é irretroativo, aplicando-se os novos marcos temporais a partir da publicação da lei.",
 "Segundo o Tema 1.199 do STF, o novo regime prescricional da Lei n.º 14.230/2021, por ser mais benéfico, retroage para alcançar os processos em curso, inclusive quanto à prescrição intercorrente de quatro anos.",
 "STF, Tema 1.199, tese 4.","retroatividade da prescrição","q15c",JUR("tema_repercussao","STF, Tema 1.199"))
P("Q15",["23"],"jurisprudencia","jurisprudencia",4,
 "Segundo o Supremo Tribunal Federal (Tema 897), são imprescritíveis as ações de ressarcimento ao erário fundadas na prática de ato doloso tipificado na Lei de Improbidade Administrativa.",
 "Segundo o Supremo Tribunal Federal (Tema 897), são imprescritíveis as ações de ressarcimento ao erário fundadas em qualquer ato ilícito, doloso ou culposo, praticado por agente público ou terceiro.",
 "STF, Tema 897 (RE 852.475): imprescritibilidade só para ato doloso de improbidade; ilícito civil comum é prescritível (Tema 666).","amplia imprescritibilidade","q15d",JUR("tema_repercussao","STF, Tema 897"))
P("Q15",["17"],"jurisprudencia","jurisprudencia",5,
 "O Supremo Tribunal Federal, ao julgar as ADIs 7042 e 7043, reconheceu a legitimidade ativa concorrente e disjuntiva entre o Ministério Público e as pessoas jurídicas interessadas (entes públicos lesados) para a propositura da ação de improbidade, declarando a inconstitucionalidade parcial da regra de legitimidade exclusiva do Ministério Público.",
 "O Supremo Tribunal Federal, ao julgar as ADIs 7042 e 7043, confirmou a constitucionalidade da legitimidade ativa exclusiva do Ministério Público para a propositura da ação de improbidade, vedada a atuação autônoma dos entes públicos lesados.",
 "STF, ADIs 7042 e 7043: legitimidade ativa concorrente; o art. 17 da LIA, no texto da Lei 14.230/21, atribuía-a apenas ao MP.","mantém legitimidade exclusiva","q15e",JUR("adi","STF, ADI 7042 e ADI 7043"))
P("Q15",["11.XI"],"jurisprudencia","jurisprudencia",4,
 "Segundo a Súmula Vinculante 13 do STF, a nomeação de cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, inclusive, da autoridade nomeante ou de servidor da mesma pessoa jurídica investido em cargo de direção, chefia ou assessoramento, para o exercício de cargo em comissão ou de confiança, viola a Constituição Federal.",
 "Segundo a Súmula Vinculante 13 do STF, a nomeação de parentes até o quarto grau da autoridade nomeante viola a Constituição Federal, aplicando-se a vedação inclusive aos cargos de natureza política, como os de secretário estadual e municipal.",
 "STF, SV 13 (terceiro grau, inclusive); a jurisprudência do STF excepciona cargos políticos, salvo nepotismo cruzado, fraude ou inidoneidade (Rcl 6.650, RE 579.951 etc.).","amplia grau e alcance","q15f",JUR("sumula_vinculante","STF, Súmula Vinculante 13"))
P("Q15",["2"],"jurisprudencia","jurisprudencia",4,
 "O Supremo Tribunal Federal entende que os agentes políticos, com exceção do Presidente da República, que responde apenas por crime de responsabilidade (art. 85, V, da CF), sujeitam-se a duplo regime sancionatório, podendo ser responsabilizados por improbidade administrativa.",
 "O Supremo Tribunal Federal entende que os agentes políticos, por responderem por crime de responsabilidade, não se sujeitam à Lei de Improbidade Administrativa, sendo esta aplicável apenas aos servidores públicos e particulares.",
 "STF, Pet 3.240: agentes políticos, exceto o Presidente da República, respondem por improbidade.","exclui agentes políticos","q15g",JUR("jurisprudencia","STF, Pet 3.240 (Plenário, 2018)"))
# ---- Q16 (casos integrados)
P("Q16",["9","12","20"],"caso_concreto","caso_concreto",5,
 "Servidor público federal, ocupante de cargo efetivo, foi condenado, em sentença de primeira instância, por receber vantagem econômica de empresa interessada em contrato do seu órgão (art. 9.º), com sanções de perda da função, suspensão de direitos políticos por catorze anos e multa equivalente ao acréscimo patrimonial. Interposta apelação, as sanções ainda não podem ser executadas, pois dependem do trânsito em julgado.",
 "Servidor público federal, ocupante de cargo efetivo, foi condenado, em sentença de primeira instância, por receber vantagem econômica de empresa interessada em contrato do seu órgão (art. 9.º), com sanções de perda da função, suspensão de direitos políticos por catorze anos e multa equivalente ao acréscimo patrimonial. Interposta apelação, as sanções já podem ser executadas, pois a apelação não possui efeito suspensivo nas ações de improbidade.",
 "Art. 12, caput, I e § 9.º; art. 20.","execução provisória","q16a")
P("Q16",["10","17","12"],"caso_concreto","caso_concreto",5,
 "O Ministério Público ajuizou ação de improbidade imputando a prefeito, genericamente, a prática de atos do art. 10 e do art. 11 pelo mesmo fato (dispensa irregular de licitação sem perda patrimonial comprovada). Diante disso, o ato deverá ser enquadrado em um único tipo e, inexistindo perda patrimonial efetiva, não cabe condenação por lesão ao erário, nem ressarcimento.",
 "O Ministério Público ajuizou ação de improbidade imputando a prefeito, genericamente, a prática de atos do art. 10 e do art. 11 pelo mesmo fato (dispensa irregular de licitação sem perda patrimonial comprovada). Diante disso, o juiz pode condenar cumulativamente nos dois tipos, impondo ressarcimento presumido do dano pela só ilegalidade da dispensa.",
 "Art. 17, § 10-D; art. 10, VIII e § 1.º.","cumula tipos e presume dano","q16b")
P("Q16",["3","12","17C"],"caso_concreto","caso_concreto",5,
 "Empresa de engenharia e seu sócio-administrador foram réus em ação de improbidade ao lado de um secretário municipal. O sócio não participou da contratação nem obteve benefício direto. Nessa situação, o sócio não responde pelo ato imputado à pessoa jurídica, e, se houver condenação de vários réus, esta será no limite da participação e dos benefícios de cada um, vedada a solidariedade.",
 "Empresa de engenharia e seu sócio-administrador foram réus em ação de improbidade ao lado de um secretário municipal. O sócio não participou da contratação nem obteve benefício direto. Nessa situação, o sócio responde pelo ato imputado à pessoa jurídica por ser administrador, e, havendo condenação, todos os réus respondem solidariamente pelo dano.",
 "Art. 3.º, § 1.º; art. 17-C, § 2.º.","responsabilidade objetiva e solidária","q16c")
P("Q16",["16","17"],"caso_concreto","caso_concreto",4,
 "Em ação de improbidade, o juiz decretou liminarmente, sem ouvir o réu, a indisponibilidade de bens, fundamentando a decisão apenas na gravidade abstrata dos fatos. Da decisão que deferir ou indeferir o pedido caberá agravo de instrumento, e a medida, para ser mantida, exigiria a demonstração concreta de perigo de dano irreparável ou de risco ao resultado útil do processo.",
 "Em ação de improbidade, o juiz decretou liminarmente, sem ouvir o réu, a indisponibilidade de bens, fundamentando a decisão apenas na gravidade abstrata dos fatos. Da decisão que deferir a medida não cabe recurso imediato, devendo a matéria ser impugnada em preliminar de apelação, e a urgência pode ser presumida nas ações do art. 9.º.",
 "Art. 16, §§ 3.º, 4.º e 9.º.","nega agravo e presume urgência","q16d")
P("Q16",["11","17B"],"caso_concreto","caso_concreto",4,
 "Após o ajuizamento da ação de improbidade contra ex-gestor, ele e o Ministério Público ajustaram acordo de não persecução civil, com integral ressarcimento do dano e reversão da vantagem. O acordo foi homologado judicialmente. Descumprido o acordo, o ex-gestor ficará impedido de celebrar novo acordo por cinco anos, contados do conhecimento pelo MP do efetivo descumprimento.",
 "Após o ajuizamento da ação de improbidade contra ex-gestor, ele e o Ministério Público ajustaram acordo de não persecução civil, com integral ressarcimento do dano e reversão da vantagem. O acordo foi homologado judicialmente. Descumprido o acordo, o ex-gestor ficará impedido de celebrar novo acordo por dez anos, contados da homologação judicial.",
 "Art. 17-B, §§ 1.º, 4.º e 7.º.","altera prazo e termo","q16e")
P("Q16",["18A"],"caso_concreto","caso_concreto",5,
 "Ex-prefeito foi condenado em dois processos por atos que o juiz reconheceu como continuidade de ilícito: suspensão dos direitos políticos de oito anos em um e de seis em outro. No cumprimento da sentença, a requerimento do réu, o juiz poderá unificar as sanções, aplicando a maior sanção aumentada de um terço ou a soma das penas, o que for mais benéfico, observado o limite de vinte anos.",
 "Ex-prefeito foi condenado em dois processos por atos que o juiz reconheceu como continuidade de ilícito: suspensão dos direitos políticos de oito anos em um e de seis em outro. No cumprimento da sentença, o juiz deverá, de ofício, somar as sanções, que poderão alcançar o limite de trinta anos.",
 "Art. 18-A, I e parágrafo único.","soma de ofício e limite","q16f")
