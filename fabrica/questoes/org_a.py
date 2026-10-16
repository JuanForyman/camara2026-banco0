# Organização administrativa — lote L10
Q = []
TAILS=[" Essa seria a orientação adotada pela doutrina e pela jurisprudência no direito brasileiro.",
 " Trata-se de entendimento aplicável à responsabilidade civil das pessoas jurídicas de direito público no Brasil.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática constitucional da responsabilidade do Estado.",
 " Essa seria a regra para os danos causados a terceiros no exercício da função pública."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
FD={"tipo":"doutrina_jurisprudencia","ref":"doutrina majoritária; DL 200/67; CF","versao":"conhecimento do autor","conferida":"conhecimento"}
FJ={"tipo":"jurisprudencia","ref":"Teses de repercussão geral do STF (tesesesumulas.com.br, 2026-10-16)","versao":"conhecimento verificado em fonte secundária","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, jur=False, lei=False):
    ex = {}
    if lei: ex["fonte"]={"tipo":"lei","ref":"DL 200/67; CF","versao":"vigente","conferida":"conhecimento"}
    elif jur: ex["fonte"]=FJ; ex["risco"]=["jurisprudencia_conhecimento"]
    else: ex["fonte"]=FD; ex["risco"]=["doutrina_conhecimento"]
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# O01
P("O01",["1"],"conceito_correto","confusao_instituto",2,
 "Em sentido subjetivo, formal ou orgânico, a Administração Pública é o conjunto de órgãos, entidades e agentes que exercem a função administrativa; em sentido objetivo ou material, é a própria atividade administrativa.",
 "Em sentido objetivo, formal ou orgânico, a Administração Pública é o conjunto de órgãos, entidades e agentes que exercem a função administrativa; em sentido subjetivo ou material, é a própria atividade administrativa.",
 "Sentidos de Administração Pública.","inverte sentidos","o01a")
P("O01",["1"],"conceito_correto","excecao_omitida",2,
 "O governo exerce função política, de comando e de fixação de diretrizes, ao passo que a Administração Pública executa os planos de governo, e a função administrativa é exercida de forma atípica pelo Legislativo e pelo Judiciário.",
 "O governo exerce função meramente executiva dos atos da Administração Pública, e a função administrativa é exercida exclusivamente pelo Poder Executivo, não podendo ser exercida pelo Legislativo e pelo Judiciário.",
 "Governo e Administração.","atribui função administrativa só ao Executivo","o01b")
# O02
P("O02",["2"],"conceito_correto","confusao_instituto",3,
 "A desconcentração é a distribuição interna de competências entre órgãos de uma mesma pessoa jurídica, mantendo-se o vínculo hierárquico, ao passo que a descentralização é a transferência da execução do serviço a pessoa jurídica distinta.",
 "A descentralização é a distribuição interna de competências entre órgãos de uma mesma pessoa jurídica, mantendo-se o vínculo hierárquico, ao passo que a desconcentração é a transferência da execução do serviço a pessoa jurídica distinta.",
 "Descentralização e desconcentração.","inverte conceitos","o02a")
P("O02",["2"],"conceito_correto","excecao_omitida",4,
 "Na descentralização por outorga, a lei transfere a titularidade e a execução do serviço a pessoa jurídica da Administração indireta, ao passo que na descentralização por delegação transfere-se somente a execução, por contrato ou ato.",
 "Na descentralização por delegação, a lei transfere a titularidade e a execução do serviço a pessoa jurídica da Administração indireta, ao passo que na descentralização por outorga transfere-se somente a execução, por contrato ou ato.",
 "Outorga e delegação.","inverte outorga e delegação","o02b")
P("O02",["2","9"],"conceito_correto","troca_efeito",3,
 "Entre o órgão desconcentrado e a pessoa jurídica de que faz parte há subordinação hierárquica, ao passo que, entre a Administração direta e as entidades descentralizadas, há apenas vinculação e controle finalístico.",
 "Entre a Administração direta e as entidades descentralizadas há subordinação hierárquica, ao passo que, entre o órgão desconcentrado e a pessoa jurídica de que faz parte, há apenas vinculação e controle finalístico.",
 "Hierarquia e vinculação.","troca controle","o02c")
# O03
P("O03",["3"],"conceito_correto","excecao_omitida",3,
 "Segundo o Decreto-Lei 200/1967, a Administração Indireta compreende as autarquias, as empresas públicas, as sociedades de economia mista e as fundações públicas, vinculadas ao Ministério em cuja área de competência estiver enquadrada sua principal atividade.",
 "Segundo o Decreto-Lei 200/1967, a Administração Indireta compreende as autarquias, as empresas públicas, as sociedades de economia mista, as fundações públicas e os Ministérios, vinculadas diretamente à Presidência da República.",
 "DL 200/67, arts. 4º e 5º.","inclui ministérios na indireta","o03a",lei=True)
P("O03",["3"],"conceito_correto","troca_autoridade",3,
 "A sociedade de economia mista é entidade de direito privado, criada por lei, sob a forma de sociedade anônima, cujas ações com direito a voto pertencem em sua maioria à União ou a entidade da Administração indireta.",
 "A sociedade de economia mista é entidade de direito público, criada por lei, sob a forma de sociedade limitada, cujo capital pertence integralmente à União ou a entidade da Administração indireta.",
 "DL 200/67, art. 5º, III.","troca forma e capital","o03b",lei=True)
P("O03",["3"],"conceito_correto","excecao_omitida",3,
 "A autarquia é o serviço autônomo criado por lei, com personalidade jurídica, patrimônio e receita próprios, para executar atividades típicas da Administração Pública que requeiram gestão administrativa e financeira descentralizada.",
 "A autarquia é entidade de direito privado, criada por autorização legislativa, para exploração de atividade econômica que o Governo seja levado a exercer por força de contingência ou de conveniência administrativa.",
 "DL 200/67, art. 5º, I.","descreve empresa pública","o03c",lei=True)
# O04
P("O04",["4"],"conceito_correto","confusao_instituto",3,
 "A autarquia é criada diretamente por lei específica, ao passo que a instituição de empresa pública, de sociedade de economia mista e de fundação é apenas autorizada por lei específica.",
 "A autarquia tem sua instituição autorizada por lei específica, ao passo que a criação de empresa pública, de sociedade de economia mista e de fundação é feita diretamente pela lei.",
 "CF, art. 37, XIX.","inverte criação e autorização","o04a",lei=True)
P("O04",["4"],"conceito_correto","excecao_omitida",4,
 "Compete à lei complementar definir as áreas de atuação das fundações cuja instituição seja autorizada por lei específica.",
 "Compete à lei complementar definir as áreas de atuação das autarquias e das empresas estatais cuja instituição seja autorizada por lei específica.",
 "CF, art. 37, XIX.","amplia para autarquias e empresas","o04b",lei=True)
P("O04",["4"],"conceito_correto","excecao_omitida",3,
 "A criação de subsidiárias das entidades da Administração indireta, assim como a participação de qualquer delas em empresa privada, depende de autorização legislativa, em cada caso.",
 "A criação de subsidiárias das entidades da Administração indireta depende de autorização legislativa, mas a participação delas em empresa privada pode ser realizada por decisão do administrador, sem autorização legislativa.",
 "CF, art. 37, XX.","dispensa autorização para participação","o04c",lei=True)
# O05
P("O05",["5"],"conceito_correto","excecao_omitida",3,
 "As autarquias são pessoas jurídicas de direito público cujos bens são públicos e cujos débitos judiciais são pagos mediante precatórios, e gozam de imunidade tributária recíproca quanto ao patrimônio, à renda e aos serviços vinculados às suas finalidades essenciais.",
 "As autarquias são pessoas jurídicas de direito privado cujos bens são penhoráveis e cujos débitos judiciais são pagos diretamente, sem precatórios, e não gozam de imunidade tributária recíproca.",
 "Regime das autarquias.","atribui regime privado","o05a")
P("O05",["5"],"conceito_correto","excecao_omitida",4,
 "As agências reguladoras são autarquias em regime especial, com autonomia reforçada, ausência de subordinação hierárquica ao Ministro e dirigentes com mandato fixo, nos termos da Lei 13.848/2019.",
 "As agências reguladoras são autarquias em regime especial subordinadas hierarquicamente ao Ministro de Estado, cujas decisões podem ser revistas de ofício por ele, e com dirigentes demissíveis ad nutum.",
 "Lei 13.848/2019.","hierarquia e demissão ad nutum","o05b",lei=True)
P("O05",["5"],"conceito_correto","excecao_omitida",4,
 "A fundação pública pode ter personalidade jurídica de direito público, hipótese em que tem natureza autárquica, ou de direito privado, entendendo o STF que a fundação estatal de direito público é espécie de autarquia.",
 "A fundação pública tem sempre personalidade jurídica de direito privado, sendo vedado, segundo o STF, que a fundação estatal tenha natureza autárquica.",
 "STF, jurisprudência sobre fundações estatais de direito público.","nega fundação de direito público","o05c",jur=True)
# O06
P("O06",["6"],"conceito_correto","troca_autoridade",3,
 "A empresa estatal exploradora de atividade econômica sujeita-se ao regime jurídico próprio das empresas privadas quanto aos direitos e obrigações civis, comerciais, trabalhistas e tributários, não podendo gozar de privilégios fiscais não extensivos ao setor privado.",
 "A empresa estatal exploradora de atividade econômica sujeita-se ao regime jurídico de direito público quanto aos direitos e obrigações civis, comerciais, trabalhistas e tributários, podendo gozar de privilégios fiscais não extensivos ao setor privado.",
 "CF, art. 173, §§ 1º e 2º.","atribui regime público e privilégios","o06a",lei=True)
P("O06",["6"],"conceito_correto","excecao_omitida",3,
 "Os empregados das empresas públicas e das sociedades de economia mista são regidos pela CLT e admitidos mediante concurso público.",
 "Os empregados das empresas públicas e das sociedades de economia mista são regidos pelo regime estatutário e admitidos sem necessidade de concurso público, por se tratar de entidades de direito privado.",
 "CF, art. 37, II.","estatutário sem concurso","o06b",lei=True)
P("O06",["6"],"conceito_correto","excecao_omitida",5,
 "O teto remuneratório constitucional aplica-se às empresas estatais que receberem recursos da União, dos Estados, do Distrito Federal ou dos Municípios para pagamento de despesas de pessoal ou de custeio em geral.",
 "O teto remuneratório constitucional aplica-se a todas as empresas estatais, ainda que não recebam recursos públicos para pagamento de despesas de pessoal ou de custeio em geral.",
 "CF, art. 37, § 9º.","omite condição","o06c",lei=True)
P("O06",["6"],"conceito_correto","troca_autoridade",4,
 "Segundo o STF, a Empresa Brasileira de Correios e Telégrafos, prestadora de serviço público em regime de monopólio, equipara-se à Fazenda Pública quanto à impenhorabilidade de seus bens e ao pagamento de débitos por precatório.",
 "Segundo o STF, a Empresa Brasileira de Correios e Telégrafos, por ser empresa pública de direito privado, não se equipara à Fazenda Pública, devendo pagar seus débitos judiciais sem precatório e tendo bens penhoráveis.",
 "STF, RE 220.906.","nega equiparação à Fazenda","o06d",jur=True)
P("O06",["6"],"conceito_correto","troca_numero",3,
 "A empresa pública é entidade de direito privado cujo capital social é integralmente detido pelo ente federativo, admitida a participação de outras pessoas de direito público interno e de entidades da Administração indireta, desde que a maioria do capital votante permaneça com a pessoa federada.",
 "A empresa pública é entidade de direito privado cujo capital social pode ser detido majoritariamente por particulares, desde que o ente federativo mantenha ao menos trinta por cento do capital votante.",
 "Lei 13.303/2016, art. 3º.","admite maioria privada","o06e",lei=True)
# O07
P("O07",["7"],"conceito_correto","confusao_instituto",3,
 "A organização social firma contrato de gestão com o Poder Público, ao passo que a OSCIP firma termo de parceria, e as organizações da sociedade civil, nos termos da Lei 13.019/2014, firmam termo de colaboração, termo de fomento ou acordo de cooperação.",
 "A organização social firma termo de parceria com o Poder Público, ao passo que a OSCIP firma contrato de gestão, e as organizações da sociedade civil, nos termos da Lei 13.019/2014, firmam apenas contrato administrativo regido pela Lei 14.133/2021.",
 "Leis 9.637/98, 9.790/99 e 13.019/14.","troca instrumentos","o07a",lei=True)
P("O07",["7"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, é constitucional a dispensa de licitação para a celebração do contrato de gestão com organizações sociais, desde que o procedimento de qualificação e de celebração observe critérios objetivos e impessoais, de acordo com os princípios do art. 37 da Constituição.",
 "Segundo o STF, é inconstitucional a dispensa de licitação para a celebração do contrato de gestão com organizações sociais, devendo ser aplicada a Lei 14.133/2021 a todos os contratos de gestão.",
 "STF, ADI 1.923.","inverte decisão","o07b",jur=True)
P("O07",["7"],"conceito_correto","excecao_omitida",3,
 "As entidades do terceiro setor não integram a Administração Pública, direta ou indireta, e são pessoas jurídicas de direito privado sem fins lucrativos que atuam em colaboração com o Estado.",
 "As entidades do terceiro setor integram a Administração indireta e são pessoas jurídicas de direito público que atuam como braços do Estado.",
 "Terceiro setor.","inclui na indireta","o07c")
P("O07",["7"],"conceito_correto","excecao_omitida",4,
 "Os serviços sociais autônomos, que compõem o chamado Sistema S, são entidades privadas mantidas por contribuições parafiscais, sujeitas ao controle do Tribunal de Contas da União e que, em regra, adotam regulamentos próprios de contratação.",
 "Os serviços sociais autônomos, que compõem o chamado Sistema S, são autarquias mantidas por contribuições parafiscais, não sujeitas ao controle do Tribunal de Contas da União.",
 "Serviços sociais autônomos.","autarquias não sujeitas a controle","o07d")
P("O07",["7"],"conceito_correto","excecao_omitida",3,
 "O termo de colaboração e o termo de fomento são, em regra, precedidos de chamamento público, e o acordo de cooperação é o instrumento sem transferência de recursos financeiros.",
 "O termo de colaboração e o termo de fomento prescindem de chamamento público, e o acordo de cooperação é o instrumento que prevê transferência de recursos financeiros.",
 "Lei 13.019/2014.","inverte exigências","o07e",lei=True)
# O08
P("O08",["8"],"conceito_correto","excecao_omitida",3,
 "Os órgãos públicos não têm personalidade jurídica própria, mas podem ter, de forma excepcional, capacidade processual para a defesa de suas prerrogativas institucionais.",
 "Os órgãos públicos têm personalidade jurídica própria e podem ser sujeitos de direitos e obrigações em nome próprio, respondendo diretamente pelos danos causados por seus agentes.",
 "Teoria do órgão; Súmula 525 do STJ.","atribui personalidade","o08a")
P("O08",["8"],"conceito_correto","troca_autoridade",3,
 "Nos termos da Lei 9.784/1999, órgão é a unidade de atuação integrante da estrutura da Administração direta e da indireta, entidade é a unidade de atuação dotada de personalidade jurídica, e autoridade é o servidor ou agente público dotado de poder de decisão.",
 "Nos termos da Lei 9.784/1999, órgão é a unidade de atuação dotada de personalidade jurídica, entidade é a unidade de atuação integrante da estrutura da Administração direta, e autoridade é qualquer servidor público.",
 "Lei 9.784/99, art. 1º, § 2º.","troca definições","o08b",lei=True)
P("O08",["8"],"conceito_correto","confusao_instituto",3,
 "Quanto à composição, os órgãos classificam-se em singulares ou unipessoais, que atuam por um único agente, e colegiados ou pluripessoais, que atuam por manifestação conjunta de seus membros.",
 "Quanto à composição, os órgãos classificam-se em singulares ou pluripessoais, que atuam por manifestação conjunta de seus membros, e colegiados ou unipessoais, que atuam por um único agente.",
 "Classificação dos órgãos.","inverte conceitos","o08c")
P("O08",["8"],"conceito_correto","excecao_omitida",4,
 "Segundo a Súmula 525 do STJ, a Câmara de Vereadores não possui personalidade jurídica, apenas personalidade judiciária, e somente pode demandar em juízo para defender os seus direitos institucionais.",
 "Segundo a Súmula 525 do STJ, a Câmara de Vereadores possui personalidade jurídica própria e pode demandar em juízo para defender quaisquer direitos do Município.",
 "STJ, Súmula 525.","atribui personalidade e legitimidade ampla","o08d",jur=True)
# O09
P("O09",["9"],"conceito_correto","confusao_instituto",3,
 "O controle exercido pela Administração direta sobre as entidades da Administração indireta é finalístico, também chamado de supervisão ministerial ou tutela, e depende de previsão legal.",
 "O controle exercido pela Administração direta sobre as entidades da Administração indireta decorre de hierarquia e independe de previsão legal, permitindo a revisão de ofício de todos os seus atos pelo Ministro.",
 "DL 200/67, arts. 19 a 29.","atribui hierarquia","o09a")
P("O09",["10"],"conceito_correto","excecao_omitida",4,
 "O consórcio público pode revestir a forma de associação pública, com personalidade de direito público e natureza autárquica, ou de pessoa jurídica de direito privado, e é constituído por contrato precedido de protocolo de intenções ratificado por lei.",
 "O consórcio público somente pode revestir a forma de pessoa jurídica de direito privado e é constituído por simples protocolo de intenções, dispensada a ratificação por lei de cada ente consorciado.",
 "Lei 11.107/2005.","exclui associação pública","o09b",lei=True)
P("O09",["10"],"conceito_correto","excecao_omitida",5,
 "A União somente pode participar de consórcio público em que também façam parte todos os Estados em cujos territórios estejam situados os Municípios consorciados.",
 "A União pode participar livremente de consórcio público formado apenas por Municípios, sem necessidade de participação dos Estados em que estejam situados.",
 "Lei 11.107/2005, art. 1º, § 2º.","dispensa participação dos Estados","o09c",lei=True)
