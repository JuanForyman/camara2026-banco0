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
# Atom 16: teorias da democracia (Q01)
P("Q01",["16"],"conceito_correto","confusao_instituto",3,
 "Na teoria pluralista da democracia, de Dahl, o poder é disperso entre muitos grupos de interesse que competem e negociam, e o governo atua como árbitro entre eles.",
 "Na teoria pluralista da democracia, de Dahl, o poder está concentrado em uma única elite econômica coesa, e os grupos de interesse não influenciam as decisões do governo.",
 "Dahl e Truman.","atribui tese elitista ao pluralismo","q01h")
P("Q01",["16"],"conceito_correto","confusao_instituto",3,
 "A teoria participativa da democracia, associada a Pateman e Macpherson, defende a ampliação da participação dos cidadãos em esferas além do voto, por entender que a participação tem efeito educativo.",
 "A teoria participativa da democracia, associada a Pateman e Macpherson, defende que a participação dos cidadãos deve restringir-se ao voto periódico, por entender que a participação ampla ameaça a estabilidade.",
 "Pateman; Macpherson.","atribui tese elitista à teoria participativa","q01i")
P("Q01",["16"],"conceito_correto","confusao_instituto",4,
 "Para a democracia deliberativa, associada a Habermas, a legitimidade das decisões decorre do debate público racional, em que os cidadãos justificam seus argumentos uns aos outros, e não da mera agregação de preferências por meio do voto.",
 "Para a democracia deliberativa, associada a Habermas, a legitimidade das decisões decorre exclusivamente da agregação de preferências individuais por meio do voto, sendo dispensável o debate público.",
 "Habermas.","reduz deliberação a agregação","q01j")
P("Q01",["16"],"caso_concreto","caso_concreto",4,
 "Uma prefeitura convoca assembleias de bairro, em que moradores debatem e votam parte do orçamento municipal, com decisões vinculantes. A experiência é associada às teorias participativa e deliberativa da democracia.",
 "Uma prefeitura convoca assembleias de bairro, em que moradores debatem e votam parte do orçamento municipal, com decisões vinculantes. A experiência é associada à teoria elitista competitiva de Schumpeter, para quem a participação popular deve limitar-se à escolha dos governantes.",
 "Orçamento participativo.","atribui caso à teoria elitista","q01k")
P("Q01",["16"],"conceito_correto","excecao_omitida",4,
 "A democracia agonística, associada a Chantal Mouffe, reconhece o conflito como constitutivo da política e propõe transformar o antagonismo em disputa entre adversários legítimos.",
 "A democracia agonística, associada a Chantal Mouffe, defende que o consenso racional é o objetivo da política e que o conflito deve ser eliminado do debate democrático.",
 "Mouffe.","nega conflito","q01l")
# Atom 19: Bobbio (Q01)
P("Q01",["19"],"conceito_correto","excecao_omitida",4,
 "Para Bobbio, a definição mínima de democracia é o conjunto de regras que estabelecem quem está autorizado a tomar decisões coletivas e com quais procedimentos, o que pressupõe, entre outras, a regra da maioria e as liberdades de opinião e de associação.",
 "Para Bobbio, a definição mínima de democracia é o regime em que há igualdade econômica plena entre os cidadãos, independentemente das regras de decisão coletiva e das liberdades de opinião.",
 "Bobbio, O Futuro da Democracia.","substitui regras por igualdade econômica","q01m")
P("Q01",["19"],"conceito_correto","excecao_omitida",5,
 "Entre as promessas não cumpridas da democracia apontadas por Bobbio estão a persistência de oligarquias, a sobrevivência de poderes invisíveis e o espaço limitado da representação.",
 "Entre as promessas cumpridas da democracia apontadas por Bobbio estão o fim das oligarquias, a eliminação dos poderes invisíveis e a plena realização da participação direta.",
 "Bobbio, O Futuro da Democracia.","inverte promessas","q01n")
P("Q01",["19"],"conceito_correto","confusao_instituto",4,
 "Para Bobbio, o critério central que distingue a esquerda da direita é a atitude diante da igualdade, atribuindo a esquerda maior valor à igualdade.",
 "Para Bobbio, o critério central que distingue a esquerda da direita é a atitude diante da propriedade estatal, atribuindo a esquerda maior valor ao livre mercado.",
 "Bobbio, Direita e Esquerda.","troca critério","q01o")
P("Q01",["19"],"conceito_correto","excecao_omitida",4,
 "O liberalismo, em Bobbio, refere-se à limitação do poder do Estado, enquanto a democracia refere-se a quem governa, de modo que são conceitos distintos, embora historicamente articulados.",
 "O liberalismo, em Bobbio, refere-se a quem governa, enquanto a democracia refere-se à limitação do poder do Estado, de modo que são conceitos idênticos e inseparáveis.",
 "Bobbio, Liberalismo e Democracia.","identifica liberalismo e democracia","q01p")
# Atom 17: Tocqueville (Q03)
P("Q03",["17"],"conceito_correto","excecao_omitida",3,
 "Para Tocqueville, a igualdade de condições é o traço central da sociedade democrática, e entre seus riscos estão a tirania da maioria e o individualismo.",
 "Para Tocqueville, a desigualdade de condições é o traço central da sociedade democrática, e entre suas virtudes estão a proteção das minorias e o fortalecimento dos laços comunitários.",
 "Tocqueville, A Democracia na América.","inverte diagnóstico","q03g")
P("Q03",["17"],"conceito_correto","excecao_omitida",3,
 "Tocqueville aponta as associações civis, a liberdade de imprensa e o poder local descentralizado como antídotos contra o risco de despotismo na democracia.",
 "Tocqueville aponta a centralização administrativa, a restrição à imprensa e a supressão das associações civis como antídotos contra o risco de despotismo na democracia.",
 "Tocqueville.","inverte antídotos","q03h")
P("Q03",["17"],"conceito_correto","confusao_instituto",4,
 "Em O Antigo Regime e a Revolução, Tocqueville sustenta que a centralização administrativa já existia na monarquia francesa e foi aprofundada pela Revolução.",
 "Em O Antigo Regime e a Revolução, Tocqueville sustenta que a centralização administrativa foi uma invenção da Revolução Francesa, sem antecedentes na monarquia.",
 "Tocqueville, O Antigo Regime e a Revolução.","nega continuidade","q03i")
# Atom 21: capital social (Q03)
P("Q03",["21"],"conceito_correto","excecao_omitida",3,
 "Segundo Putnam, o melhor desempenho das instituições regionais do norte da Itália em comparação ao sul decorre do capital social, formado por redes de engajamento cívico, normas de reciprocidade e confiança.",
 "Segundo Putnam, o melhor desempenho das instituições regionais do norte da Itália em comparação ao sul decorre apenas do maior nível de renda e industrialização, e não do capital social ou da tradição cívica.",
 "Putnam, Comunidades e Democracia.","nega capital social","q03j")
P("Q03",["21"],"conceito_correto","confusao_instituto",4,
 "Para Almond e Verba, a cultura cívica resulta da mistura equilibrada entre as orientações paroquial, de sujeição e participante.",
 "Para Almond e Verba, a cultura cívica corresponde exclusivamente à orientação participante, sendo incompatível com as orientações paroquial e de sujeição.",
 "Almond e Verba, A Cultura Cívica.","reduz a cultura participante","q03k")
P("Q03",["21"],"conceito_correto","excecao_omitida",4,
 "Inglehart associa a prosperidade e a segurança econômica ao crescimento de valores pós-materialistas, como a qualidade de vida e a participação.",
 "Inglehart associa a escassez e a insegurança econômica ao crescimento de valores pós-materialistas, como a qualidade de vida e a participação.",
 "Inglehart, valores pós-materialistas.","inverte condições","q03l")
# Atom 35: participação (Q03)
P("Q03",["35"],"conceito_correto","troca_numero",4,
 "A iniciativa popular de projeto de lei federal exige subscrição de, no mínimo, um por cento do eleitorado nacional, distribuído pelo menos por cinco Estados, com não menos de três décimos por cento dos eleitores de cada um deles.",
 "A iniciativa popular de projeto de lei federal exige subscrição de, no mínimo, cinco por cento do eleitorado nacional, distribuído pelo menos por três Estados, com não menos de um por cento dos eleitores de cada um deles.",
 "CF, art. 61, § 2º.","troca percentuais e número de Estados","q03m",lei=True)
P("Q03",["35"],"conceito_correto","troca_autoridade",3,
 "Compete exclusivamente ao Congresso Nacional autorizar referendo e convocar plebiscito.",
 "Compete exclusivamente ao Presidente da República autorizar referendo e convocar plebiscito, mediante decreto, independentemente de manifestação do Congresso Nacional.",
 "CF, art. 49, XV.","atribui competência ao Presidente","q03n",lei=True)
P("Q03",["35"],"conceito_correto","troca_numero",3,
 "Em 2005, o referendo sobre a comercialização de armas de fogo e munição resultou na rejeição da proibição, prevalecendo o voto contrário a ela.",
 "Em 2005, o referendo sobre a comercialização de armas de fogo e munição resultou na aprovação da proibição, prevalecendo o voto favorável a ela.",
 "Referendo de 2005.","inverte resultado","q03o")
P("Q03",["35"],"conceito_correto","excecao_omitida",3,
 "Conselhos de políticas públicas, audiências públicas e orçamento participativo são instrumentos de participação social na gestão pública, que se somam ao plebiscito, ao referendo e à iniciativa popular.",
 "Conselhos de políticas públicas, audiências públicas e orçamento participativo são instrumentos de participação social previstos exclusivamente para os Poderes Legislativo e Judiciário, vedada sua utilização pelo Poder Executivo.",
 "Participação social.","restringe a órgãos de outros Poderes","q03p")
# Atom 20: poder (Q04)
P("Q04",["20"],"conceito_correto","confusao_instituto",3,
 "Para Max Weber, o poder é a probabilidade de impor a própria vontade em uma relação social, mesmo contra resistência.",
 "Para Max Weber, o poder é a capacidade de gerar consenso entre os membros de uma comunidade, de modo que a resistência é incompatível com o conceito.",
 "Weber, Economia e Sociedade.","exclui resistência","q04f")
P("Q04",["20"],"conceito_correto","excecao_omitida",4,
 "Bachrach e Baratz identificaram a segunda face do poder, que consiste em impedir que certas questões entrem na agenda de decisão, por meio das não decisões.",
 "Bachrach e Baratz sustentaram que o poder se manifesta somente nas decisões observáveis, e que a análise do que não entra na agenda de decisão é irrelevante para o estudo do poder.",
 "Bachrach e Baratz.","nega segunda face do poder","q04g")
P("Q04",["20"],"conceito_correto","excecao_omitida",5,
 "Na concepção tridimensional de Lukes, a terceira face do poder consiste em moldar as preferências e crenças dos dominados, de modo que aceitem a dominação.",
 "Na concepção tridimensional de Lukes, a terceira face do poder consiste na coerção física direta contra os dominados, de modo que dispensa o consentimento.",
 "Lukes, Power: A Radical View.","troca terceira dimensão","q04h")
P("Q04",["20"],"conceito_correto","confusao_instituto",4,
 "Para Foucault, o poder é disperso nas relações sociais e tem caráter produtivo, exercendo-se por meio de disciplina e vigilância, e não apenas como repressão localizada no Estado.",
 "Para Foucault, o poder é localizado exclusivamente no Estado e tem caráter meramente repressivo, exercendo-se apenas pela proibição e pela força.",
 "Foucault, Vigiar e Punir; Microfísica do Poder.","reduz o poder ao Estado repressor","q04i")
P("Q04",["20"],"conceito_correto","excecao_omitida",3,
 "Na concepção de Dahl, o poder se revela em decisões observáveis, e A tem poder sobre B quando consegue fazer B fazer algo que B não faria de outro modo.",
 "Na concepção de Dahl, o poder se revela na formação inconsciente das preferências dos dominados, e A tem poder sobre B mesmo quando B faria o mesmo sem a influência de A.",
 "Dahl, concepção unidimensional.","confunde com Lukes","q04j")
# Atom 30: políticas públicas (Q04)
P("Q04",["30"],"conceito_correto","excecao_omitida",4,
 "No modelo dos múltiplos fluxos, de Kingdon, a janela de oportunidade se abre quando convergem os fluxos dos problemas, das alternativas de política e da política, e os empreendedores de políticas atuam para aproveitá-la.",
 "No modelo dos múltiplos fluxos, de Kingdon, a mudança de política decorre exclusivamente da formulação racional e linear de alternativas, sem relação com a atuação de empreendedores ou com a convergência de fluxos.",
 "Kingdon, Agendas, Alternatives and Public Policies.","nega convergência dos fluxos","q04k")
P("Q04",["30"],"conceito_correto","confusao_instituto",4,
 "Na tipologia de Lowi, as políticas públicas dividem-se em distributivas, regulatórias, redistributivas e constitutivas, e a política determina a arena política em que o processo decisório se desenvolve.",
 "Na tipologia de Lowi, as políticas públicas dividem-se em federais, estaduais e municipais, e a arena política determina o tipo de política pública a ser formulada.",
 "Lowi, tipologia de políticas públicas.","troca tipologia","q04l")
P("Q04",["30"],"conceito_correto","excecao_omitida",4,
 "No incrementalismo, de Lindblom, as decisões públicas avançam por pequenas mudanças em relação ao status quo, em razão das limitações de informação e do conflito político.",
 "No incrementalismo, de Lindblom, as decisões públicas resultam de uma análise racional abrangente de todas as alternativas possíveis, o que afasta a mudança gradual.",
 "Lindblom, The Science of Muddling Through.","atribui racionalidade abrangente","q04m")
P("Q04",["30"],"conceito_correto","confusao_instituto",3,
 "O ciclo das políticas públicas compreende a formação da agenda, a formulação, a tomada de decisão, a implementação e a avaliação.",
 "O ciclo das políticas públicas compreende a implementação, a formulação, a avaliação e, por fim, a formação da agenda, nessa ordem obrigatória.",
 "Ciclo de políticas públicas.","inverte sequência","q04n")
P("Q04",["30"],"conceito_correto","excecao_omitida",4,
 "Lipsky chamou de burocratas de nível de rua os servidores que, na linha de frente, interagem diretamente com os cidadãos e exercem discricionariedade que afeta a implementação das políticas.",
 "Lipsky chamou de burocratas de nível de rua os dirigentes de cúpula que formulam as políticas, sem contato direto com os cidadãos e sem discricionariedade na implementação.",
 "Lipsky, Street-Level Bureaucracy.","inverte quem são os burocratas","q04o")
# Atom 22: escolha racional (Q06)
P("Q06",["22"],"conceito_correto","confusao_instituto",4,
 "Em Downs, os partidos agem como empresas que buscam maximizar votos, e, em competição bipartidária em uma única dimensão, tendem a convergir para as posições do eleitor mediano.",
 "Em Downs, os partidos agem como organizações voltadas exclusivamente à defesa de uma ideologia, e, em competição bipartidária em uma única dimensão, tendem a radicalizar suas posições para os extremos.",
 "Downs, Uma Teoria Econômica da Democracia.","inverte convergência","q06j")
P("Q06",["22"],"conceito_correto","excecao_omitida",4,
 "Segundo Olson, indivíduos racionais não cooperam espontaneamente para obter bens coletivos, e grupos pequenos se organizam com mais facilidade do que grandes, salvo existência de incentivos seletivos ou coerção.",
 "Segundo Olson, indivíduos racionais cooperam espontaneamente para obter bens coletivos, e grupos grandes se organizam com mais facilidade do que pequenos, mesmo na ausência de incentivos seletivos ou coerção.",
 "Olson, A Lógica da Ação Coletiva.","inverte a lógica da ação coletiva","q06k")
P("Q06",["22"],"conceito_correto","excecao_omitida",4,
 "O teorema da impossibilidade, de Arrow, sustenta que nenhum sistema de agregação de preferências individuais satisfaz, ao mesmo tempo, um conjunto de critérios razoáveis de justiça, e o paradoxo de Condorcet mostra que maiorias podem ser cíclicas.",
 "O teorema da impossibilidade, de Arrow, sustenta que a regra da maioria simples sempre produz uma escolha coletiva transitiva e consistente, e o paradoxo de Condorcet mostra que as maiorias nunca são cíclicas.",
 "Arrow; Condorcet.","nega impossibilidade e ciclos","q06l")
P("Q06",["22"],"conceito_correto","excecao_omitida",3,
 "A ignorância racional, em Downs, significa que o eleitor pode considerar racional não investir tempo em se informar, porque o custo da informação supera o benefício esperado de seu voto isolado.",
 "A ignorância racional, em Downs, significa que o eleitor é irracional ao não se informar, porque o benefício esperado do voto individual sempre supera o custo da informação.",
 "Downs.","inverte custo-benefício","q06m")
# Atom 23: clivagens e partidos (Q06)
P("Q06",["23"],"conceito_correto","excecao_omitida",4,
 "Lipset e Rokkan identificaram clivagens críticas que estruturaram os sistemas partidários europeus, como as oposições entre centro e periferia, Estado e Igreja, rural e urbano e capital e trabalho, e sustentaram que esses alinhamentos se congelaram.",
 "Lipset e Rokkan identificaram uma única clivagem estruturante, a oposição entre capital e trabalho, e sustentaram que os alinhamentos partidários se alteram completamente a cada eleição.",
 "Lipset e Rokkan.","reduz a uma clivagem e nega congelamento","q06n")
P("Q06",["23"],"conceito_correto","excecao_omitida",5,
 "Para Mainwaring, o sistema partidário brasileiro apresenta baixa institucionalização, com partidos fracos, alta volatilidade eleitoral e indisciplina dos parlamentares.",
 "Para Mainwaring, o sistema partidário brasileiro apresenta alta institucionalização, com partidos fortes, baixa volatilidade eleitoral e elevada disciplina dos parlamentares.",
 "Mainwaring, Rethinking Party Systems.","inverte diagnóstico","q06o")
P("Q06",["23"],"conceito_correto","excecao_omitida",5,
 "A leitura de Limongi e Figueiredo contesta a visão de partidos fracos e parlamentares individualistas, sustentando que os partidos votam de forma disciplinada, em razão dos poderes legislativos do Presidente e dos líderes partidários.",
 "A leitura de Limongi e Figueiredo corrobora a visão de Ames, de que os partidos são fracos e os parlamentares agem de forma individualista, sem disciplina, em busca de recursos para seus redutos.",
 "Limongi e Figueiredo x Ames.","confunde posições","q06p")
P("Q06",["23","24"],"conceito_correto","confusao_instituto",4,
 "O número efetivo de partidos, de Laakso e Taagepera, é o inverso da soma dos quadrados das proporções de votos ou cadeiras dos partidos, de modo que pondera o tamanho de cada um e mede a fragmentação do sistema.",
 "O número efetivo de partidos, de Laakso e Taagepera, é o número total de partidos registrados na Justiça Eleitoral, sem ponderar o tamanho de cada um e sem relação com a fragmentação do sistema.",
 "Laakso e Taagepera.","reduz ao número de partidos registrados","q06q")
# Atom 24: indicadores e outros sistemas (Q05)
P("Q05",["24"],"conceito_correto","excecao_omitida",3,
 "A volatilidade eleitoral mede a mudança agregada na votação dos partidos entre duas eleições sucessivas, e a desproporcionalidade mede a distância entre a proporção de votos e a proporção de cadeiras.",
 "A volatilidade eleitoral mede a distância entre a proporção de votos e a proporção de cadeiras, e a desproporcionalidade mede a mudança agregada na votação dos partidos entre duas eleições sucessivas.",
 "Pedersen; Gallagher.","inverte indicadores","q05h")
P("Q05",["24"],"conceito_correto","excecao_omitida",4,
 "O distritão é um sistema majoritário aplicado a cargos legislativos, em que são eleitos os candidatos mais votados, independentemente do partido, e não é adotado no Brasil para as eleições proporcionais.",
 "O distritão é um sistema proporcional de lista fechada, em que o partido define a ordem dos eleitos, e é adotado no Brasil para as eleições de Deputados e Vereadores.",
 "Distritão.","confunde com lista fechada","q05i")
P("Q05",["24"],"conceito_correto","excecao_omitida",4,
 "No sistema alemão, o eleitor tem dois votos, um para o candidato do distrito e outro para a lista do partido, e a composição final é proporcional.",
 "No sistema alemão, o eleitor tem um único voto, destinado ao candidato do distrito, e a composição final é majoritária.",
 "Sistema proporcional personalizado.","reduz a um voto majoritário","q05j")
P("Q05",["24"],"conceito_correto","excecao_omitida",3,
 "Quanto maior a magnitude do distrito, isto é, quanto maior o número de cadeiras em disputa, mais proporcional tende a ser o resultado da eleição.",
 "Quanto maior a magnitude do distrito, isto é, quanto maior o número de cadeiras em disputa, menos proporcional tende a ser o resultado da eleição.",
 "Magnitude do distrito.","inverte relação","q05k")
# Atom 25 e 36: elegibilidade e direitos políticos (Q05)
P("Q05",["25"],"conceito_correto","troca_numero",3,
 "A idade mínima para ser Presidente da República, Vice-Presidente e Senador é de trinta e cinco anos, para Governador, trinta anos, para Deputado Federal e Prefeito, vinte e um anos, e para Vereador, dezoito anos.",
 "A idade mínima para ser Presidente da República, Vice-Presidente e Senador é de trinta anos, para Governador, vinte e um anos, para Deputado Federal e Prefeito, dezoito anos, e para Vereador, dezesseis anos.",
 "CF, art. 14, § 3º, VI.","troca idades","q05l",lei=True)
P("Q05",["25"],"conceito_correto","excecao_omitida",3,
 "O Presidente da República, os Governadores, os Prefeitos e quem os houver sucedido ou substituído no curso do mandato poderão ser reeleitos para um único período subsequente.",
 "O Presidente da República, os Governadores, os Prefeitos e quem os houver sucedido ou substituído no curso do mandato poderão ser reeleitos para quantos períodos subsequentes desejarem.",
 "CF, art. 14, § 5º.","admite reeleição ilimitada","q05m",lei=True)
P("Q05",["25"],"conceito_correto","excecao_omitida",4,
 "O militar alistável é elegível e, se contar mais de dez anos de serviço, será agregado pela autoridade superior e, se eleito, passará à inatividade no ato da diplomação.",
 "O militar alistável é inelegível, vedada a candidatura a qualquer cargo eletivo enquanto estiver na ativa, independentemente do tempo de serviço.",
 "CF, art. 14, § 8º.","nega elegibilidade","q05n",lei=True)
P("Q05",["36"],"conceito_correto","excecao_omitida",3,
 "É vedada a cassação de direitos políticos, cuja perda ou suspensão só se dará nos casos previstos na Constituição, entre eles a condenação criminal transitada em julgado, enquanto durarem seus efeitos, e a improbidade administrativa.",
 "A cassação de direitos políticos é admitida por decisão fundamentada do Presidente da República, e a perda ou suspensão ocorre em qualquer caso de condenação criminal, ainda que sem trânsito em julgado.",
 "CF, art. 15.","admite cassação e dispensa trânsito","q05o",lei=True)
P("Q05",["36"],"conceito_correto","troca_numero",3,
 "A lei que alterar o processo eleitoral entra em vigor na data de sua publicação, mas não se aplica à eleição que ocorra até um ano da data de sua vigência, em respeito ao princípio da anualidade eleitoral.",
 "A lei que alterar o processo eleitoral entra em vigor após seis meses de sua publicação e aplica-se imediatamente a qualquer eleição, em respeito ao princípio da anualidade eleitoral.",
 "CF, art. 16.","troca prazos e efeitos","q05p",lei=True)
P("Q05",["36"],"conceito_correto","excecao_omitida",4,
 "A Lei da Ficha Limpa, Lei Complementar 135/2010, alterou a Lei Complementar 64/1990, que trata dos casos de inelegibilidade, instituídos por lei complementar nos termos do art. 14, § 9º, da Constituição.",
 "A Lei da Ficha Limpa, Lei Ordinária 135/2010, alterou o Código Eleitoral, e os casos de inelegibilidade podem ser instituídos por simples lei ordinária, nos termos do art. 14, § 9º, da Constituição.",
 "CF, art. 14, § 9º; LC 135/2010.","troca espécie normativa","q05q",lei=True)
# Atom 26: Câmara e Senado (Q07)
P("Q07",["26"],"conceito_correto","troca_numero",3,
 "O Senado compõe-se de três Senadores por Estado e pelo Distrito Federal, com mandato de oito anos, e sua representação é renovada de quatro em quatro anos, alternadamente, por um e dois terços.",
 "O Senado compõe-se de dois Senadores por Estado e pelo Distrito Federal, com mandato de seis anos, e sua representação é renovada de quatro em quatro anos, alternadamente, por um e dois terços.",
 "CF, art. 46.","troca número e mandato","q07e",lei=True)
P("Q07",["26"],"conceito_correto","confusao_instituto",3,
 "A Câmara dos Deputados compõe-se de representantes do povo, eleitos pelo sistema proporcional, e o Senado, de representantes dos Estados e do Distrito Federal, eleitos pelo princípio majoritário.",
 "A Câmara dos Deputados compõe-se de representantes dos Estados, eleitos pelo princípio majoritário, e o Senado, de representantes do povo, eleitos pelo sistema proporcional.",
 "CF, arts. 45 e 46.","inverte representação e sistema","q07f",lei=True)
P("Q07",["26"],"conceito_correto","troca_numero",4,
 "Nenhuma unidade da Federação pode ter menos de oito ou mais de setenta Deputados Federais, e o número total, bem como a representação por unidade, é fixado por lei complementar, proporcionalmente à população.",
 "Nenhuma unidade da Federação pode ter menos de três ou mais de cinquenta Deputados Federais, e o número total, bem como a representação por unidade, é fixado por lei ordinária, em partes iguais entre os Estados.",
 "CF, art. 45, § 1º.","troca limites e espécie normativa","q07g",lei=True)
P("Q07",["26"],"conceito_correto","excecao_omitida",3,
 "O bicameralismo, adotado pelo Congresso Nacional, associa-se ao federalismo, pois o Senado representa os Estados e o Distrito Federal em condição de igualdade numérica.",
 "O bicameralismo, adotado pelo Congresso Nacional, é incompatível com o federalismo, pois o Senado representa o povo em proporção à população de cada Estado.",
 "Bicameralismo e federalismo.","nega relação com federalismo","q07h")
# Atom 31: política brasileira (Q07)
P("Q07",["31"],"conceito_correto","excecao_omitida",3,
 "Tancredo Neves foi eleito Presidente da República, em 1985, de forma indireta, pelo Colégio Eleitoral, e, em razão de sua morte, José Sarney assumiu a Presidência.",
 "Tancredo Neves foi eleito Presidente da República, em 1985, de forma direta, pelo voto popular, e, após o término de seu mandato, José Sarney foi eleito como seu sucessor.",
 "Redemocratização.","troca forma de eleição","q07i")
P("Q07",["31"],"conceito_correto","excecao_omitida",3,
 "A emenda Dante de Oliveira, que previa eleições diretas para Presidente, foi rejeitada pela Câmara dos Deputados em 1984, apesar da mobilização popular das Diretas Já.",
 "A emenda Dante de Oliveira, que previa eleições diretas para Presidente, foi aprovada pela Câmara dos Deputados em 1984, em razão da mobilização popular das Diretas Já.",
 "Diretas Já.","inverte resultado","q07j")
P("Q07",["31"],"conceito_correto","troca_numero",3,
 "Fernando Collor foi eleito em 1989, na primeira eleição direta para Presidente desde 1960, e sofreu impeachment em 1992.",
 "Fernando Collor foi eleito em 1985, na primeira eleição direta para Presidente desde 1930, e sofreu impeachment em 1994.",
 "Marcos políticos.","troca datas","q07k")
P("Q07",["31"],"conceito_correto","excecao_omitida",4,
 "A Emenda Constitucional 86/2015 tornou de execução obrigatória as emendas parlamentares individuais ao orçamento, e a Emenda Constitucional 100/2019 estendeu a obrigatoriedade às emendas de bancada.",
 "A Emenda Constitucional 86/2015 tornou facultativa a execução das emendas parlamentares individuais ao orçamento, e a Emenda Constitucional 100/2019 proibiu as emendas de bancada.",
 "EC 86/2015; EC 100/2019.","inverte efeitos","q07l",lei=True)
# Atom 27: presidencialismo (Q02)
P("Q02",["27"],"conceito_correto","excecao_omitida",4,
 "Para Linz, o presidencialismo é mais propenso a crises em razão da rigidez do mandato fixo, da dupla legitimidade do Presidente e do Legislativo e da lógica de soma zero da eleição majoritária.",
 "Para Linz, o presidencialismo é mais estável que o parlamentarismo em razão da flexibilidade do mandato, da legitimidade única do governo e da lógica de soma positiva da eleição proporcional.",
 "Linz, O Fracasso do Presidencialismo.","inverte diagnóstico","q02g")
P("Q02",["27"],"conceito_correto","troca_numero",3,
 "Cabe à Câmara dos Deputados autorizar, por dois terços de seus membros, a instauração de processo contra o Presidente por crime de responsabilidade, e ao Senado Federal, sob a presidência do Presidente do STF, processá-lo e julgá-lo, exigindo-se dois terços dos votos para a condenação.",
 "Cabe à Câmara dos Deputados processar e julgar o Presidente por crime de responsabilidade, por maioria absoluta, e ao Senado Federal autorizar a instauração do processo, sob a presidência do Presidente da Câmara.",
 "CF, arts. 51, I, e 52, I e parágrafo único.","troca competências e quóruns","q02h",lei=True)
P("Q02",["27"],"conceito_correto","excecao_omitida",3,
 "A condenação do Presidente da República por crime de responsabilidade acarreta a perda do cargo, com inabilitação, por oito anos, para o exercício de função pública, sem prejuízo das demais sanções judiciais cabíveis.",
 "A condenação do Presidente da República por crime de responsabilidade acarreta somente a perda do cargo, sem inabilitação para o exercício de função pública, e impede outras sanções judiciais.",
 "CF, art. 52, parágrafo único.","omite inabilitação","q02i",lei=True)
P("Q02",["27"],"conceito_correto","excecao_omitida",4,
 "Shugart e Carey classificam os regimes presidencialistas segundo os poderes legislativos do Presidente, como o veto, o decreto e a iniciativa exclusiva de projetos.",
 "Shugart e Carey classificam os regimes presidencialistas segundo o número de partidos no Parlamento, sendo irrelevantes os poderes legislativos do Presidente.",
 "Shugart e Carey.","troca critério","q02j")
# Atom 28: federalismo (Q02)
P("Q02",["28"],"conceito_correto","confusao_instituto",3,
 "O federalismo dual separa rigidamente as competências entre a União e os Estados, ao passo que o federalismo cooperativo prevê competências comuns e concorrentes e a cooperação entre os entes.",
 "O federalismo cooperativo separa rigidamente as competências entre a União e os Estados, ao passo que o federalismo dual prevê competências comuns e concorrentes e a cooperação entre os entes.",
 "Federalismo dual e cooperativo.","inverte modelos","q02k")
P("Q02",["28"],"conceito_correto","excecao_omitida",4,
 "O federalismo brasileiro formou-se por desagregação, pois um Estado unitário se descentralizou em 1889, ao passo que o norte-americano formou-se por agregação de Estados antes independentes.",
 "O federalismo brasileiro formou-se por agregação de Estados antes independentes, ao passo que o norte-americano formou-se por desagregação de um Estado unitário.",
 "Federalismo por agregação e desagregação.","inverte origens","q02l")
P("Q02",["28"],"conceito_correto","excecao_omitida",3,
 "No Brasil, a forma federativa de Estado é cláusula pétrea, e os Municípios são entes federados, ao lado da União, dos Estados e do Distrito Federal.",
 "No Brasil, a forma federativa de Estado pode ser abolida por emenda constitucional, e os Municípios não são entes federados, mas apenas divisões administrativas dos Estados.",
 "CF, arts. 1º, 18 e 60, § 4º, I.","nega cláusula pétrea e status do Município","q02m",lei=True)
P("Q02",["28"],"conceito_correto","confusao_instituto",3,
 "No federalismo centrípeto, o poder tende a se concentrar na União, ao passo que no centrífugo se concentra nos entes subnacionais.",
 "No federalismo centrípeto, o poder tende a se concentrar nos entes subnacionais, ao passo que no centrífugo se concentra na União.",
 "Federalismo centrípeto e centrífugo.","inverte tendências","q02n")
# Atom 18 Marx/Gramsci/Poulantzas (Q09)
P("Q09",["18"],"conceito_correto","confusao_instituto",3,
 "Para a tradição marxista clássica, o Estado é instrumento da classe dominante, ao passo que Gramsci amplia a análise com o conceito de hegemonia, em que a dominação combina coerção e consenso.",
 "Para a tradição marxista clássica, o Estado é árbitro neutro entre as classes, ao passo que Gramsci rejeita o conceito de hegemonia e sustenta que a dominação se dá apenas por coerção.",
 "Marx; Gramsci.","inverte concepção de Estado e hegemonia","q09g")
P("Q09",["18"],"conceito_correto","excecao_omitida",4,
 "Em Gramsci, a sociedade civil, composta por escolas, igrejas, imprensa e associações, é espaço de disputa pela hegemonia, e os intelectuais orgânicos articulam a visão de mundo de uma classe.",
 "Em Gramsci, a sociedade civil é espaço alheio à disputa política, e os intelectuais orgânicos são servidores neutros que não vinculam suas ideias a nenhuma classe.",
 "Gramsci, Cadernos do Cárcere.","nega papel da sociedade civil","q09h")
P("Q09",["18"],"conceito_correto","confusao_instituto",4,
 "Poulantzas concebe o Estado como a condensação material de uma relação de forças entre classes e frações de classe, dotado de autonomia relativa.",
 "Poulantzas concebe o Estado como mero instrumento sem autonomia, controlado diretamente por uma única classe, sem qualquer relação de forças.",
 "Poulantzas, O Estado, o Poder, o Socialismo.","nega autonomia relativa","q09i")
# Atom 29 Marshall e Esping-Andersen (Q09)
P("Q09",["29"],"conceito_correto","excecao_omitida",3,
 "Para Marshall, a cidadania desenvolveu-se, na Inglaterra, em sequência de direitos civis, políticos e sociais, correspondentes aos séculos XVIII, XIX e XX.",
 "Para Marshall, a cidadania desenvolveu-se, na Inglaterra, em sequência de direitos sociais, políticos e civis, correspondentes aos séculos XVIII, XIX e XX.",
 "Marshall, Cidadania, Classe Social e Status.","inverte sequência","q09j")
P("Q09",["29"],"conceito_correto","excecao_omitida",4,
 "Carvalho observa que, no Brasil, a sequência de Marshall foi alterada: os direitos sociais antecederam os políticos plenos e os civis, o que explicaria uma cidadania de tipo estadualista.",
 "Carvalho observa que, no Brasil, a sequência de Marshall foi rigorosamente reproduzida, com a conquista dos direitos civis antes dos políticos e sociais.",
 "Carvalho, Cidadania no Brasil.","afirma reprodução da sequência","q09k")
P("Q09",["29"],"conceito_correto","confusao_instituto",4,
 "Esping-Andersen distingue três regimes de bem-estar: o liberal, o conservador-corporativo e o social-democrata, diferenciados pelo grau de desmercantilização dos direitos sociais.",
 "Esping-Andersen distingue dois regimes de bem-estar, o capitalista e o socialista, diferenciados pela propriedade estatal dos meios de produção.",
 "Esping-Andersen, Três Mundos do Welfare State.","troca tipologia","q09l")
P("Q09",["29"],"conceito_correto","excecao_omitida",4,
 "No regime liberal descrito por Esping-Andersen, predominam benefícios assistenciais focalizados e baixa desmercantilização, ao passo que o social-democrata é universalista e redistributivo.",
 "No regime liberal descrito por Esping-Andersen, predominam benefícios universais e alta desmercantilização, ao passo que o social-democrata é focalizado e mínimo.",
 "Esping-Andersen.","inverte regimes","q09m")
# Atom 33 nação, nacionalismo, soberania (Q09)
P("Q09",["33"],"conceito_correto","confusao_instituto",3,
 "Para Benedict Anderson, a nação é uma comunidade política imaginada, limitada e soberana, e a imprensa e o capitalismo editorial contribuíram para sua formação.",
 "Para Benedict Anderson, a nação é uma realidade natural e eterna, anterior a qualquer construção social, e a imprensa não teve papel em sua formação.",
 "Anderson, Comunidades Imaginadas.","naturaliza nação","q09n")
P("Q09",["33"],"conceito_correto","excecao_omitida",4,
 "Para Gellner, o nacionalismo é anterior às nações e as produz, pois a industrialização exigiu culturas homogêneas e educação padronizada.",
 "Para Gellner, as nações são anteriores ao nacionalismo, que apenas as revela, e a industrialização foi irrelevante para sua formação.",
 "Gellner, Nações e Nacionalismo.","inverte relação nação-nacionalismo","q09o")
P("Q09",["33"],"conceito_correto","excecao_omitida",4,
 "Hobsbawm e Ranger tratam as tradições nacionais como em grande parte inventadas, isto é, práticas que aparentam antiguidade mas são recentes e servem à construção da identidade.",
 "Hobsbawm e Ranger tratam as tradições nacionais como genuinamente imemoriais, sem qualquer componente de invenção política.",
 "Hobsbawm e Ranger, A Invenção das Tradições.","nega invenção","q09p")
P("Q09",["33"],"conceito_correto","confusao_instituto",3,
 "Para Bodin, a soberania é o poder absoluto e perpétuo de uma república, e, no direito internacional contemporâneo, ela se expressa também na igualdade jurídica entre os Estados.",
 "Para Bodin, a soberania é um poder temporário, limitado por todos os demais Estados, e, no direito internacional contemporâneo, ela é incompatível com a igualdade jurídica entre os Estados.",
 "Bodin, Os Seis Livros da República.","nega perpetuidade","q09q")
P("Q09",["33"],"conceito_correto","excecao_omitida",3,
 "Estados falidos são aqueles que perdem a capacidade de exercer o monopólio da violência legítima e de prover serviços básicos em seu território.",
 "Estados falidos são aqueles que mantêm plenamente o monopólio da violência legítima e a prestação de serviços básicos, mas descumprem tratados internacionais.",
 "Estados falidos.","troca critério","q09r")
# Atom 11 e 12: Estado e Estados nacionais (Q09)
P("Q09",["11"],"conceito_correto","confusao_instituto",3,
 "Em Hobbes, o contrato social origina um soberano forte para pôr fim ao estado de natureza de guerra de todos contra todos, ao passo que em Locke o governo é limitado e a sociedade conserva o direito de resistência.",
 "Em Hobbes, o contrato social origina um governo limitado e a sociedade conserva o direito de resistência, ao passo que em Locke o soberano é absoluto para pôr fim ao estado de natureza.",
 "Hobbes; Locke.","inverte contratualistas","q09s")
P("Q09",["11"],"conceito_correto","excecao_omitida",3,
 "Para Weber, o Estado moderno é a comunidade humana que reivindica, com êxito, o monopólio do uso legítimo da força física em um território.",
 "Para Weber, o Estado moderno é a comunidade humana que renuncia ao uso da força física, delegando-o inteiramente à sociedade civil em seu território.",
 "Weber, A Política como Vocação.","nega monopólio","q09t")
P("Q09",["11"],"conceito_correto","confusao_instituto",4,
 "Weber distingue três tipos de dominação legítima: a tradicional, a carismática e a racional-legal, sendo esta última típica da burocracia moderna.",
 "Weber distingue três tipos de dominação legítima: a monárquica, a aristocrática e a democrática, sendo esta última típica da burocracia moderna.",
 "Weber, tipos de dominação.","troca tipos","q09u")
P("Q09",["11"],"conceito_correto","excecao_omitida",4,
 "Para Rousseau, a soberania pertence ao povo e se expressa pela vontade geral, que é inalienável e indivisível.",
 "Para Rousseau, a soberania pertence ao monarca e se expressa pela soma das vontades particulares, sendo alienável e divisível.",
 "Rousseau, Do Contrato Social.","atribui soberania ao monarca","q09v")
P("Q09",["12"],"conceito_correto","excecao_omitida",4,
 "A Paz de Westfália, de 1648, é tradicionalmente apontada como marco do sistema de Estados soberanos na Europa, fundado na igualdade jurídica e na não intervenção.",
 "A Paz de Westfália, de 1648, é tradicionalmente apontada como marco da extinção dos Estados soberanos na Europa e da criação de um império universal.",
 "Westfália.","inverte significado","q09w")
P("Q09",["12"],"conceito_correto","excecao_omitida",4,
 "Para Tilly, a formação dos Estados europeus relacionou-se à guerra e à extração de recursos, resumida na ideia de que a guerra fez o Estado e o Estado fez a guerra.",
 "Para Tilly, a formação dos Estados europeus decorreu de pactos pacíficos de cooperação, e a guerra não teve papel na extração de recursos nem na construção estatal.",
 "Tilly.","nega papel da guerra","q09x")
# Atom 13/34: interpretações do Brasil (Q10)
P("Q10",["13"],"conceito_correto","confusao_instituto",3,
 "Para Sérgio Buarque de Holanda, o homem cordial é marcado pela predominância de vínculos pessoais e afetivos, o que dificulta a separação entre o público e o privado.",
 "Para Sérgio Buarque de Holanda, o homem cordial é marcado pela polidez e pela impessoalidade, o que garante a nítida separação entre o público e o privado.",
 "Buarque de Holanda, Raízes do Brasil.","inverte cordialidade","q10g")
P("Q10",["13"],"conceito_correto","excecao_omitida",4,
 "Raymundo Faoro identifica no patrimonialismo estamental, herdado de Portugal, a chave para entender o Estado brasileiro, dominado por um estamento burocrático.",
 "Raymundo Faoro identifica no feudalismo, herdado de Portugal, a chave para entender o Estado brasileiro, dominado por uma burguesia industrial.",
 "Faoro, Os Donos do Poder.","troca categoria","q10h")
P("Q10",["13"],"conceito_correto","excecao_omitida",4,
 "Victor Nunes Leal explica o coronelismo como um compromisso entre o poder público, fortalecido, e o poder privado decadente dos proprietários rurais, em que o voto é trocado por favores.",
 "Victor Nunes Leal explica o coronelismo como a expressão da força autônoma e crescente dos proprietários rurais frente a um poder público ausente, sem troca de favores.",
 "Nunes Leal, Coronelismo, Enxada e Voto.","inverte compromisso","q10i")
P("Q10",["13"],"conceito_correto","excecao_omitida",4,
 "José Murilo de Carvalho aponta a estadania, na qual o Estado, e não a participação, é o principal vetor de acesso a direitos, e a cultura de dependência do Executivo.",
 "José Murilo de Carvalho aponta a participação ativa da sociedade civil como principal vetor de acesso a direitos no Brasil, em contraste com a dependência do Executivo.",
 "Carvalho, Cidadania no Brasil.","inverte estadania","q10j")
P("Q10",["13"],"conceito_correto","excecao_omitida",4,
 "Wanderley Guilherme dos Santos cunhou o conceito de cidadania regulada, em que a cidadania se vincula à profissão reconhecida em lei, de modo que quem não tem ofício regulamentado fica à margem dos direitos.",
 "Wanderley Guilherme dos Santos cunhou o conceito de cidadania regulada, em que a cidadania é universal e independente da profissão, de modo que todos têm acesso igual a direitos.",
 "W. G. dos Santos, Cidadania e Justiça.","inverte cidadania regulada","q10k")
P("Q10",["34"],"conceito_correto","excecao_omitida",3,
 "Gilberto Freyre, em Casa-Grande & Senzala, valoriza a miscigenação e a contribuição de índios e africanos para a formação social brasileira, tese por vezes associada ao mito da democracia racial.",
 "Gilberto Freyre, em Casa-Grande & Senzala, sustenta a superioridade racial dos colonizadores europeus e condena a miscigenação como causa do atraso brasileiro.",
 "Freyre, Casa-Grande & Senzala.","inverte tese","q10l")
P("Q10",["34"],"conceito_correto","excecao_omitida",4,
 "Oliveira Vianna defendia um Estado forte e centralizado para organizar uma sociedade que considerava fragmentada em clãs rurais, em visão autoritária e elitista.",
 "Oliveira Vianna defendia um Estado mínimo e descentralizado, por considerar a sociedade brasileira naturalmente organizada e participativa.",
 "Oliveira Vianna.","inverte posição","q10m")
P("Q10",["34"],"conceito_correto","excecao_omitida",4,
 "Caio Prado Júnior, em Formação do Brasil Contemporâneo, define o sentido da colonização como o de fornecer produtos tropicais ao mercado europeu, a partir de uma perspectiva marxista.",
 "Caio Prado Júnior, em Formação do Brasil Contemporâneo, define o sentido da colonização como a construção de uma sociedade autônoma voltada ao mercado interno, a partir de uma perspectiva liberal.",
 "Caio Prado Jr.","inverte sentido da colonização","q10n")
P("Q10",["34"],"conceito_correto","excecao_omitida",4,
 "Florestan Fernandes, em A Revolução Burguesa no Brasil, descreve uma modernização conservadora, em que a burguesia se consolida sem romper com estruturas oligárquicas.",
 "Florestan Fernandes, em A Revolução Burguesa no Brasil, descreve uma revolução radical, em que a burguesia rompe totalmente com as estruturas oligárquicas.",
 "Florestan Fernandes.","inverte modernização","q10o")
P("Q10",["34"],"conceito_correto","excecao_omitida",4,
 "Celso Furtado, em Formação Econômica do Brasil, analisa o subdesenvolvimento como resultado de um processo histórico específico, e não como uma etapa anterior ao desenvolvimento.",
 "Celso Furtado, em Formação Econômica do Brasil, analisa o subdesenvolvimento como mera etapa natural pela qual todos os países passam antes de alcançar o desenvolvimento.",
 "Furtado.","reduz subdesenvolvimento a etapa","q10p")
# Atom 14/15 história do voto e partidos (Q11)
P("Q11",["14"],"conceito_correto","excecao_omitida",3,
 "O voto feminino foi instituído no Brasil, em âmbito nacional, pelo Código Eleitoral de 1932, e consolidado como obrigatório para as mulheres que exercessem função pública remunerada, na Constituição de 1934.",
 "O voto feminino foi instituído no Brasil, em âmbito nacional, somente pela Constituição de 1988, que o estendeu às mulheres pela primeira vez.",
 "História do voto.","troca data","q11a")
P("Q11",["14"],"conceito_correto","excecao_omitida",3,
 "A Constituição de 1988 facultou o voto aos analfabetos, aos maiores de setenta anos e aos maiores de dezesseis e menores de dezoito anos.",
 "A Constituição de 1988 tornou obrigatório o voto dos analfabetos, dos maiores de setenta anos e dos maiores de dezesseis e menores de dezoito anos.",
 "CF, art. 14, § 1º, II.","inverte facultatividade","q11b",lei=True)
P("Q11",["14"],"conceito_correto","excecao_omitida",4,
 "A Emenda Constitucional 25/1985 concedeu o direito de voto aos analfabetos, que a Constituição de 1988 manteve de forma facultativa.",
 "A Emenda Constitucional 25/1985 manteve a proibição do voto dos analfabetos, que a Constituição de 1988 tornou obrigatório.",
 "Redemocratização.","inverte efeitos","q11c")
P("Q11",["14"],"conceito_correto","excecao_omitida",4,
 "Durante a Primeira República, o voto era aberto, não secreto, e as eleições eram marcadas por fraude e pelo controle dos chefes locais, em um sistema conhecido como política dos governadores.",
 "Durante a Primeira República, o voto era secreto e as eleições eram limpas e livres de controle dos chefes locais, em um sistema conhecido como política dos governadores.",
 "República Velha.","inverte caráter do voto","q11d")
P("Q11",["14"],"conceito_correto","excecao_omitida",4,
 "O Código Eleitoral de 1932 instituiu o voto secreto e criou a Justiça Eleitoral, que passou a organizar o alistamento e a apuração das eleições.",
 "O Código Eleitoral de 1932 manteve o voto aberto e extinguiu a Justiça Eleitoral, que voltou a ser conduzida pelos chefes locais.",
 "Código Eleitoral de 1932.","inverte reforma","q11e")
P("Q11",["15"],"conceito_correto","excecao_omitida",3,
 "O Ato Institucional 2, de 1965, extinguiu os partidos existentes e instituiu o bipartidarismo, com a Arena e o MDB, e a reforma partidária de 1979 restabeleceu o pluripartidarismo.",
 "O Ato Institucional 2, de 1965, instituiu o pluripartidarismo, e a reforma partidária de 1979 extinguiu os partidos e restabeleceu o bipartidarismo com a Arena e o MDB.",
 "AI-2/1965; Lei 6.767/1979.","inverte sequência","q11f")
P("Q11",["15"],"conceito_correto","excecao_omitida",4,
 "O período de 1945 a 1964 é conhecido como experiência pluripartidária, com partidos de âmbito nacional como PSD, UDN e PTB.",
 "O período de 1945 a 1964 é conhecido como experiência de partido único, em que o PSD absorveu a UDN e o PTB.",
 "República de 1946.","afirma partido único","q11g")
P("Q11",["15"],"conceito_correto","excecao_omitida",3,
 "Durante o Estado Novo, os partidos políticos foram extintos, e a Constituição de 1937 foi outorgada por Getúlio Vargas.",
 "Durante o Estado Novo, os partidos políticos foram fortalecidos, e a Constituição de 1937 foi promulgada por uma assembleia constituinte eleita.",
 "Estado Novo.","inverte situação dos partidos","q11h")
# Novas variações nos pontos fracos: Q04 poderes
P("Q04",["5"],"caso_concreto","caso_concreto",4,
 "Em regime presidencialista de coalizão, o Presidente distribui ministérios a partidos aliados em troca de apoio legislativo, e a literatura aponta como instrumentos para a governabilidade o poder de agenda e a edição de medidas provisórias.",
 "Em regime presidencialista de coalizão, o Presidente distribui ministérios a partidos aliados em troca de apoio legislativo, e a literatura aponta que tal prática é vedada pela Constituição e inexiste na prática política brasileira.",
 "Abranches, presidencialismo de coalizão.","nega existência do fenômeno","q04p")
P("Q04",["5"],"conceito_correto","excecao_omitida",3,
 "Em Montesquieu, a liberdade política exige que o poder contenha o poder, e a separação entre legislativo, executivo e judiciário é o meio para evitar o abuso.",
 "Em Montesquieu, a liberdade política exige a concentração dos três poderes em um único órgão, para garantir a unidade da ação estatal.",
 "Montesquieu, O Espírito das Leis.","inverte separação","q04q")
P("Q04",["5"],"conceito_correto","excecao_omitida",3,
 "O sistema de freios e contrapesos, de origem norte-americana, supõe que os poderes se controlem reciprocamente, como o veto presidencial e o controle de constitucionalidade.",
 "O sistema de freios e contrapesos, de origem norte-americana, supõe que os poderes se mantenham totalmente isolados, sem qualquer forma de controle recíproco.",
 "Federalista; checks and balances.","nega controle recíproco","q04r")
# Q02 sistemas e formas de governo
P("Q02",["3"],"conceito_correto","confusao_instituto",3,
 "No parlamentarismo, o governo depende da confiança do Parlamento e há distinção entre chefe de Estado e chefe de governo, ao passo que no presidencialismo o Presidente acumula as duas funções.",
 "No parlamentarismo, o chefe de governo é eleito diretamente pelo povo para mandato fixo e acumula a chefia de Estado, ao passo que no presidencialismo há distinção entre as duas funções.",
 "Sistemas de governo.","inverte características","q02o")
P("Q02",["3"],"caso_concreto","caso_concreto",4,
 "A República Federativa do Brasil adota a forma de governo republicana e o sistema de governo presidencialista, o que foi mantido pelo plebiscito de 1993 em detrimento da monarquia e do parlamentarismo.",
 "A República Federativa do Brasil adota a forma de governo monárquica e o sistema presidencialista, o que foi confirmado pelo plebiscito de 1993 em detrimento da república e do parlamentarismo.",
 "ADCT, art. 2º; plebiscito de 1993.","troca forma de governo","q02p",lei=True)
P("Q02",["3"],"conceito_correto","excecao_omitida",3,
 "O semipresidencialismo combina um Presidente eleito diretamente com um Primeiro-Ministro responsável perante o Parlamento, como se vê na França.",
 "O semipresidencialismo combina um Presidente indicado pelo Parlamento sem poderes com um Primeiro-Ministro eleito diretamente, como se vê nos Estados Unidos.",
 "Duverger; Sartori.","troca modelo","q02q")
# Q08 internacional
P("Q08",["32"],"conceito_correto","confusao_instituto",3,
 "O realismo nas relações internacionais enfatiza o Estado como ator central, a anarquia do sistema internacional e a busca de poder e segurança, ao passo que o liberalismo valoriza a cooperação e as instituições.",
 "O realismo nas relações internacionais enfatiza a cooperação e as instituições internacionais como fator de paz, ao passo que o liberalismo valoriza a anarquia e a busca de poder.",
 "Morgenthau; Waltz; Keohane.","inverte teorias","q08g")
P("Q08",["32"],"conceito_correto","excecao_omitida",4,
 "O construtivismo, de Wendt, sustenta que as identidades e os interesses dos Estados são socialmente construídos, e que a anarquia é aquilo que os Estados fazem dela.",
 "O construtivismo, de Wendt, sustenta que as identidades e os interesses dos Estados são dados materialmente e imutáveis, e que a anarquia determina sua conduta.",
 "Wendt, Social Theory of International Politics.","nega construção social","q08h")
P("Q08",["32"],"conceito_correto","excecao_omitida",3,
 "A Organização Mundial do Comércio sucedeu o GATT e dispõe de mecanismo de solução de controvérsias, e o Mercosul tem como membros plenos, entre outros, Argentina, Brasil, Paraguai e Uruguai.",
 "A Organização Mundial do Comércio foi criada antes do GATT e não dispõe de mecanismo de solução de controvérsias, e o Mercosul é formado apenas por Argentina e Brasil.",
 "OMC; Mercosul.","troca história e membros","q08i")
P("Q08",["32"],"conceito_correto","excecao_omitida",3,
 "Os acordos de Bretton Woods, de 1944, criaram o Fundo Monetário Internacional e o Banco Mundial, para a reconstrução econômica e a estabilidade monetária no pós-guerra.",
 "Os acordos de Bretton Woods, de 1944, criaram a Organização das Nações Unidas e a OTAN, para a manutenção da paz no pós-guerra.",
 "Bretton Woods.","troca instituições","q08j")
P("Q08",["32"],"conceito_correto","excecao_omitida",4,
 "A teoria da dependência sustenta que o subdesenvolvimento da periferia está relacionado à sua inserção subordinada no sistema capitalista mundial, e são autores associados a ela Cardoso e Faletto e Gunder Frank.",
 "A teoria da dependência sustenta que o subdesenvolvimento da periferia decorre exclusivamente de fatores culturais internos, sem relação com o sistema capitalista mundial.",
 "Cardoso e Faletto; Gunder Frank.","nega fator externo","q08k")
P("Q08",["37"],"conceito_correto","excecao_omitida",3,
 "Compete ao Presidente da República manter relações com Estados estrangeiros e celebrar tratados, convenções e atos internacionais, sujeitos a referendo do Congresso Nacional.",
 "Compete ao Congresso Nacional manter relações com Estados estrangeiros e celebrar tratados, sujeitos a referendo do Presidente da República.",
 "CF, art. 84, VII e VIII.","inverte competências","q08l",lei=True)
P("Q08",["37"],"conceito_correto","excecao_omitida",3,
 "Compete ao Congresso Nacional resolver definitivamente sobre tratados, acordos ou atos internacionais que acarretem encargos ou compromissos gravosos ao patrimônio nacional.",
 "Compete ao Presidente da República resolver definitivamente, sem manifestação do Congresso Nacional, sobre tratados que acarretem encargos gravosos ao patrimônio nacional.",
 "CF, art. 49, I.","retira competência do Congresso","q08m",lei=True)
P("Q08",["37"],"conceito_correto","excecao_omitida",3,
 "O Barão do Rio Branco é associado à consolidação das fronteiras brasileiras por meios diplomáticos, e a política externa brasileira é tradicionalmente caracterizada pelo universalismo e pela busca de solução pacífica de controvérsias.",
 "O Barão do Rio Branco é associado à ampliação das fronteiras brasileiras por meio de guerras de conquista, e a política externa brasileira é tradicionalmente caracterizada pelo isolacionismo.",
 "Rio Branco; Itamaraty.","inverte tradição","q08n")
P("Q08",["37"],"conceito_correto","excecao_omitida",4,
 "O Brasil integra o G4, com Alemanha, Índia e Japão, que pleiteia reforma do Conselho de Segurança da ONU para ampliar o número de membros permanentes.",
 "O Brasil integra o G4, com Estados Unidos, Rússia e China, que são membros permanentes do Conselho de Segurança da ONU com poder de veto.",
 "G4; Conselho de Segurança.","troca membros do G4","q08o")
P("Q08",["10"],"conceito_correto","excecao_omitida",3,
 "A República Federativa do Brasil rege-se nas suas relações internacionais, entre outros, pelos princípios da independência nacional, da prevalência dos direitos humanos, da autodeterminação dos povos, da não intervenção e da igualdade entre os Estados.",
 "A República Federativa do Brasil rege-se nas suas relações internacionais, entre outros, pelos princípios da intervenção humanitária irrestrita, da hierarquia entre Estados e da supremacia das decisões de organismos regionais sobre a Constituição.",
 "CF, art. 4º.","troca princípios","q08p",lei=True)
P("Q08",["10"],"conceito_correto","excecao_omitida",3,
 "O Brasil buscará a integração econômica, política, social e cultural dos povos da América Latina, visando à formação de uma comunidade latino-americana de nações.",
 "O Brasil buscará exclusivamente a integração econômica com países desenvolvidos, sendo vedada a integração política ou cultural dos povos da América Latina.",
 "CF, art. 4º, parágrafo único.","restringe integração","q08q",lei=True)
# Q07 organização política brasileira
P("Q07",["9"],"conceito_correto","excecao_omitida",3,
 "Todo o poder emana do povo, que o exerce por meio de representantes eleitos ou diretamente, nos termos da Constituição, e o Brasil se constitui em Estado Democrático de Direito.",
 "Todo o poder emana do Estado, que o exerce por meio de representantes designados pelo Presidente, e o Brasil se constitui em Estado confessional de Direito.",
 "CF, art. 1º.","troca fundamento","q07m",lei=True)
P("Q07",["9"],"conceito_correto","excecao_omitida",3,
 "O alistamento eleitoral e o voto são obrigatórios para os maiores de dezoito anos e facultativos para os analfabetos, os maiores de setenta anos e os maiores de dezesseis e menores de dezoito anos.",
 "O alistamento eleitoral e o voto são facultativos para os maiores de dezoito anos e obrigatórios para os analfabetos, os maiores de setenta anos e os maiores de dezesseis e menores de dezoito anos.",
 "CF, art. 14, § 1º.","inverte obrigatoriedade","q07n",lei=True)
P("Q07",["9"],"conceito_correto","excecao_omitida",3,
 "Não podem alistar-se como eleitores os estrangeiros e, durante o período do serviço militar obrigatório, os conscritos.",
 "Podem alistar-se como eleitores os estrangeiros residentes há mais de cinco anos e os conscritos durante o serviço militar obrigatório.",
 "CF, art. 14, § 2º.","admite estrangeiros e conscritos","q07o",lei=True)
P("Q07",["9"],"conceito_correto","excecao_omitida",3,
 "A soberania popular é exercida pelo sufrágio universal e pelo voto direto e secreto, com valor igual para todos, e, nos termos da lei, mediante plebiscito, referendo e iniciativa popular.",
 "A soberania popular é exercida pelo voto direto e secreto, com valor proporcional à renda do eleitor, e é vedado o uso de plebiscito, referendo e iniciativa popular.",
 "CF, art. 14.","troca característica do voto","q07p",lei=True)
P("Q07",["26"],"caso_concreto","caso_concreto",4,
 "Um Estado com população pequena elege oito Deputados Federais, e outro, muito populoso, elege setenta, de modo que a representação não é estritamente proporcional à população, o que a literatura chama de malapportionment.",
 "Um Estado com população pequena elege oito Deputados Federais, e outro, muito populoso, elege setenta, de modo que a representação é estritamente proporcional à população, o que a literatura chama de distritão.",
 "Malapportionment; CF, art. 45, § 1º.","troca conceito","q07q")
# Q01 casos e conceitos
P("Q01",["1"],"caso_concreto","caso_concreto",4,
 "Em um país em que se realizam eleições periódicas, mas o governo restringe a imprensa independente e persegue opositores, a literatura classifica o regime como autoritarismo competitivo, ou democracia iliberal.",
 "Em um país em que se realizam eleições periódicas, mas o governo restringe a imprensa independente e persegue opositores, a literatura classifica o regime como poliarquia plena, pois o voto basta à democracia.",
 "Levitsky e Way; Zakaria.","classifica regime como poliarquia","q01q")
P("Q01",["1"],"conceito_correto","excecao_omitida",4,
 "Dahl chama poliarquia o regime caracterizado por alta contestação pública e alta inclusão, por entender que a democracia plena seria um ideal inalcançável.",
 "Dahl chama poliarquia o regime caracterizado por baixa contestação pública e baixa inclusão, por entender que a democracia plena já se realizou nas sociedades modernas.",
 "Dahl, Poliarquia.","inverte contestação e inclusão","q01r")
P("Q01",["1"],"conceito_correto","excecao_omitida",4,
 "Arendt e Friedrich e Brzezinski descrevem o totalitarismo como regime de ideologia oficial, partido único, terror policial e controle da sociedade, ao passo que o autoritarismo, em Linz, tem pluralismo limitado e sem mobilização intensa.",
 "Arendt e Friedrich e Brzezinski descrevem o totalitarismo como regime de pluralismo político amplo e baixa intervenção do Estado, ao passo que o autoritarismo, em Linz, tem ideologia elaborada e mobilização intensa.",
 "Arendt; Linz.","inverte características","q01s")
P("Q01",["2"],"conceito_correto","excecao_omitida",4,
 "Para Huntington, a terceira onda de democratização teve início em 1974, com a Revolução dos Cravos em Portugal, e, segundo o autor, está associada à crise de legitimidade dos regimes autoritários e ao crescimento econômico.",
 "Para Huntington, a terceira onda de democratização teve início em 1945, com o fim da Segunda Guerra, e, segundo o autor, nenhuma outra onda ocorreu depois dela.",
 "Huntington, A Terceira Onda.","troca marco","q01t")
P("Q01",["2"],"conceito_correto","excecao_omitida",4,
 "Em Lijphart, a democracia consensual caracteriza-se por governos de coalizão amplos, representação proporcional e federalismo, ao passo que a majoritária concentra o poder na maioria.",
 "Em Lijphart, a democracia consensual caracteriza-se por governos de partido único, voto majoritário e unitarismo, ao passo que a majoritária dispersa o poder em coalizões.",
 "Lijphart, Modelos de Democracia.","inverte modelos","q01u")
# Q03 representação
P("Q03",["4"],"conceito_correto","excecao_omitida",3,
 "Na representação por mandato livre, o parlamentar representa a nação e não está juridicamente vinculado às instruções dos eleitores, ao passo que no mandato imperativo é obrigado a seguir a vontade dos representados.",
 "Na representação por mandato imperativo, o parlamentar representa a nação e não está vinculado às instruções dos eleitores, ao passo que no mandato livre é obrigado a seguir a vontade dos representados.",
 "Burke; Sieyès.","inverte mandatos","q03q")
P("Q03",["4"],"conceito_correto","excecao_omitida",4,
 "Pitkin distingue as dimensões formalista, descritiva, simbólica e substantiva da representação política.",
 "Pitkin distingue apenas duas dimensões da representação política, a jurídica e a econômica, sendo irrelevantes as dimensões simbólica e descritiva.",
 "Pitkin, The Concept of Representation.","reduz dimensões","q03r")
P("Q03",["4"],"conceito_correto","excecao_omitida",3,
 "A democracia semidireta combina representação com institutos de participação direta, como o plebiscito, o referendo e a iniciativa popular, que a Constituição brasileira admite.",
 "A democracia semidireta elimina a representação e a substitui integralmente pela deliberação direta de todos os cidadãos, o que a Constituição brasileira adota.",
 "CF, art. 1º, parágrafo único.","elimina representação","q03s",lei=True)
