# Responsabilidade civil do Estado — lote L8 (edital 6)
Q = []
TAILS=[" Essa seria a orientação adotada pela doutrina e pela jurisprudência no direito brasileiro.",
 " Trata-se de entendimento aplicável à responsabilidade civil das pessoas jurídicas de direito público no Brasil.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática constitucional da responsabilidade do Estado.",
 " Essa seria a regra para os danos causados a terceiros no exercício da função pública."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
FD={"tipo":"doutrina_jurisprudencia","ref":"CF art. 37, §6º; CC art. 43; doutrina majoritária","versao":"conhecimento do autor","conferida":"conhecimento"}
FJ={"tipo":"jurisprudencia","ref":"Teses de repercussão geral do STF (tesesesumulas.com.br, 2026-10-16)","versao":"conhecimento verificado em fonte secundária","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, jur=False, lei=False):
    ex = {}
    if lei: ex["fonte"]={"tipo":"lei","ref":"CF art. 37, §6º; CC art. 43","versao":"vigente","conferida":"conhecimento"}
    elif jur: ex["fonte"]=FJ; ex["risco"]=["jurisprudencia_conhecimento"]
    else: ex["fonte"]=FD; ex["risco"]=["doutrina_conhecimento"]
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# R01
P("R01",["1"],"conceito_correto","troca_efeito",2,
 "Segundo a Constituição Federal, as pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos respondem pelos danos que seus agentes, nessa qualidade, causarem a terceiros, assegurado o direito de regresso contra o responsável nos casos de dolo ou culpa.",
 "Segundo a Constituição Federal, as pessoas jurídicas de direito público respondem pelos danos que seus agentes, nessa qualidade, causarem a terceiros, assegurado o direito de regresso contra o responsável mesmo que ausentes dolo e culpa, sendo excluídas as prestadoras de serviço público de direito privado.",
 "CF, art. 37, § 6º.","amplia regresso e exclui prestadoras","r01a",lei=True)
P("R01",["3"],"conceito_correto","confusao_instituto",3,
 "No direito brasileiro, a regra geral para a responsabilidade civil do Estado é a teoria do risco administrativo, em que bastam a conduta, o dano e o nexo causal, admitindo-se, porém, excludentes de responsabilidade como a culpa exclusiva da vítima.",
 "No direito brasileiro, a regra geral para a responsabilidade civil do Estado é a teoria do risco integral, em que bastam a conduta, o dano e o nexo causal, não se admitindo excludentes de responsabilidade, nem mesmo a culpa exclusiva da vítima.",
 "Teorias da responsabilidade do Estado.","troca risco administrativo por integral","r01b")
P("R01",["3"],"conceito_correto","confusao_instituto",3,
 "Pela teoria da culpa administrativa (faute du service), a responsabilidade do Estado surge quando o serviço público não funcionou, funcionou mal ou funcionou com atraso, dispensando-se a identificação do agente causador do dano.",
 "Pela teoria da culpa administrativa (faute du service), a responsabilidade do Estado depende da identificação do agente causador do dano e da prova de seu dolo, não bastando que o serviço tenha funcionado mal ou com atraso.",
 "Teorias da responsabilidade do Estado.","exige identificar o agente e dolo","r01c")
P("R01",["2"],"conceito_correto","excecao_omitida",3,
 "O Código Civil prevê que as pessoas jurídicas de direito público interno são civilmente responsáveis por atos dos seus agentes que, nessa qualidade, causem danos a terceiros, ressalvado o direito regressivo contra os causadores do dano, se houver, por parte destes, culpa ou dolo.",
 "O Código Civil prevê que as pessoas jurídicas de direito público interno são civilmente responsáveis apenas pelos atos culposos dos seus agentes, não havendo previsão de direito regressivo contra os causadores do dano.",
 "CC, art. 43.","afasta regresso e exige culpa","r01d",lei=True)
# R02
P("R02",["4"],"conceito_correto","excecao_omitida",3,
 "A responsabilidade objetiva do Estado exige conduta de agente público nessa qualidade, dano jurídico indenizável e nexo causal, dispensando-se a prova de culpa do agente ou do serviço e podendo decorrer até de atos lícitos, como uma obra pública que cause dano anormal e específico a particular.",
 "A responsabilidade objetiva do Estado exige conduta ilícita e culposa de agente público, não podendo decorrer de atos lícitos, como uma obra pública que cause dano anormal e específico a particular.",
 "Pressupostos da responsabilidade objetiva.","exige ilicitude e culpa","r02a")
P("R02",["4"],"conceito_correto","excecao_omitida",4,
 "Para ser indenizável, todo dano causado pela atuação estatal deve ser certo, atingir bem juridicamente protegido e ser especial e anormal, isto é, recair sobre pessoa ou grupo determinado e exceder os inconvenientes ordinários da vida em sociedade.",
 "Para ser indenizável, basta que o dano causado pela atuação estatal seja potencial, ainda que genérico e suportável por toda a coletividade, pois a responsabilidade objetiva dispensa exame da natureza do dano.",
 "Pressupostos da responsabilidade objetiva.","dispensa dano certo, especial e anormal","r02b")
P("R02",["4"],"caso_concreto","caso_concreto",4,
 "Viatura da polícia federal, em perseguição regular a criminosos, colide com veículo de passeio e causa danos materiais ao proprietário. A União responde objetivamente pelos danos, bastando ao particular demonstrar a conduta do agente, o dano e o nexo de causalidade, sem necessidade de provar culpa do motorista da viatura.",
 "Viatura da polícia federal, em perseguição regular a criminosos, colide com veículo de passeio e causa danos materiais ao proprietário. A União somente responde se o particular provar a culpa do motorista da viatura, pois a atuação em perseguição regular é ato lícito, que afasta a responsabilidade objetiva do Estado.",
 "CF, art. 37, § 6º.","exige culpa em ato lícito","r02c")
P("R02",["1","4"],"conceito_correto","excecao_omitida",3,
 "O agente cujo comportamento causou o dano, quando agiu nessa qualidade, não responde diretamente perante o terceiro lesado, que deve acionar somente a pessoa jurídica de direito público ou a prestadora de serviço público, cabendo a esta o direito de regresso contra o agente em caso de dolo ou culpa.",
 "O agente cujo comportamento causou o dano, quando agiu nessa qualidade, responde solidária e diretamente perante o terceiro lesado, que pode escolher livremente acionar a pessoa jurídica de direito público ou o agente, ainda que este tenha agido sem dolo ou culpa.",
 "CF, art. 37, § 6º; Tema 940.","admite ação direta contra o agente","r02d",jur=True)
# R03
P("R03",["5"],"conceito_correto","excecao_omitida",4,
 "Segundo o STF, a responsabilidade civil das pessoas jurídicas de direito privado prestadoras de serviço público é objetiva em relação a terceiros usuários e não usuários do serviço, nos termos do art. 37, § 6º, da Constituição.",
 "Segundo o STF, a responsabilidade civil das pessoas jurídicas de direito privado prestadoras de serviço público é objetiva apenas em relação aos usuários do serviço, sendo subjetiva em relação a terceiros não usuários.",
 "STF, Tema 130 (RE 591.874).","restringe aos usuários","r03a",jur=True)
P("R03",["5"],"caso_concreto","caso_concreto",4,
 "Pedestre que não utiliza o serviço de transporte coletivo é atropelado por ônibus de empresa concessionária de serviço público. A concessionária responde objetivamente pelo dano, ainda que a vítima não seja usuária do serviço.",
 "Pedestre que não utiliza o serviço de transporte coletivo é atropelado por ônibus de empresa concessionária de serviço público. A concessionária somente responderia se a vítima fosse usuária do serviço, já que a responsabilidade objetiva não alcança terceiros estranhos à relação de consumo.",
 "STF, Tema 130.","exige condição de usuário","r03b",jur=True)
# R04
P("R04",["6"],"conceito_correto","confusao_instituto",4,
 "Na omissão genérica do Estado, a responsabilidade civil, segundo a doutrina e o STJ majoritariamente, é subjetiva, exigindo-se a demonstração de culpa anônima (falta do serviço); na omissão específica, em que o Estado atua como garantidor, a jurisprudência do STF aplica a responsabilidade objetiva.",
 "Na omissão genérica do Estado, a responsabilidade civil é sempre objetiva, bastando o dano e o nexo causal; na omissão específica, em que o Estado atua como garantidor, a jurisprudência do STF exige a demonstração de culpa anônima.",
 "Omissão do Estado.","inverte genérica e específica","r04a")
P("R04",["6"],"caso_concreto","caso_concreto",5,
 "Moradora sofre danos em razão de alagamento causado por falta de manutenção regular, e prolongada, do sistema de drenagem municipal. Trata-se de omissão genérica, e a responsabilidade do Município, para a corrente majoritária, depende de comprovação de culpa por falta do serviço.",
 "Detento morre assassinado por outro preso em cela de presídio estadual, sem que o Estado tenha adotado medidas mínimas de proteção. Trata-se de omissão genérica, e a responsabilidade do Estado, segundo o STF, depende da comprovação de culpa por falta do serviço.",
 "Omissão genérica x específica; STF, Tema 592.","trata omissão específica como genérica","r04b")
P("R04",["6"],"conceito_correto","excecao_omitida",3,
 "Na omissão específica, o Estado tem dever concreto e individualizado de agir para impedir o dano, situando-se na posição de garantidor, e a omissão é considerada causa do dano, o que justifica a responsabilidade objetiva.",
 "Na omissão específica, o Estado não tem dever concreto de agir, e a omissão é apenas condição do dano, o que afasta a responsabilidade e justifica a necessidade de prova de dolo do agente público.",
 "Omissão do Estado.","nega dever concreto","r04c")
# R05
P("R05",["7"],"conceito_correto","excecao_omitida",4,
 "Segundo o STF, o Estado responde pela morte de detento quando descumpre o dever específico de proteção previsto no art. 5º, XLIX, da Constituição, que assegura aos presos o respeito à integridade física e moral.",
 "Segundo o STF, o Estado não responde pela morte de detento ocorrida no interior do estabelecimento prisional quando o ato for praticado por outro preso, por tratar-se de fato de terceiro que rompe o nexo causal.",
 "STF, Tema 592 (RE 841.526).","fato de terceiro sempre exclui","r05a",jur=True)
P("R05",["7"],"conceito_correto","troca_efeito",4,
 "Segundo o STF, o Estado tem o dever de manter em seus presídios padrões mínimos de humanidade, respondendo pela obrigação de ressarcir os danos, inclusive morais, comprovadamente causados aos detentos pela falta ou insuficiência das condições legais de encarceramento.",
 "Segundo o STF, a superlotação e as condições degradantes do sistema prisional não geram dever de indenizar o detento, pois o Estado está vinculado à reserva do possível e a lesão é de natureza difusa.",
 "STF, Tema 365 (RE 580.252).","afasta indenização por superlotação","r05b",jur=True)
P("R05",["7"],"conceito_correto","excecao_omitida",4,
 "Segundo o STF, não se caracteriza a responsabilidade civil objetiva do Estado por danos decorrentes de crime praticado por pessoa foragida do sistema prisional quando não demonstrado o nexo causal direto entre o momento da fuga e a conduta criminosa.",
 "Segundo o STF, caracteriza-se a responsabilidade civil objetiva do Estado por crime praticado por pessoa foragida do sistema prisional, ainda que tenha decorrido longo tempo entre a fuga e o crime, bastando a prova da fuga.",
 "STF, Tema 362 (RE 608.880).","dispensa nexo direto","r05c",jur=True)
# R06
P("R06",["8"],"conceito_correto","troca_efeito",3,
 "Na teoria do risco administrativo, são excludentes do nexo causal a culpa exclusiva da vítima, o fato exclusivo de terceiro e o caso fortuito ou a força maior, ao passo que a culpa concorrente da vítima atenua a responsabilidade do Estado e reduz a indenização.",
 "Na teoria do risco administrativo, a culpa concorrente da vítima exclui por completo a responsabilidade do Estado, enquanto a culpa exclusiva da vítima apenas atenua a indenização a ser paga.",
 "Excludentes e atenuantes.","inverte exclusão e atenuação","r06a")
P("R06",["8","14"],"conceito_correto","troca_autoridade",4,
 "Segundo o STF, nas mortes e ferimentos decorrentes de operações de segurança pública, o Estado responde pela teoria do risco administrativo, cabendo ao ente federativo o ônus de demonstrar as excludentes de responsabilidade, e a perícia inconclusiva sobre a origem do disparo não basta, por si só, para afastá-la.",
 "Segundo o STF, nas mortes e ferimentos decorrentes de operações de segurança pública, cabe à vítima ou a seus familiares o ônus de demonstrar a ausência de excludentes de responsabilidade, e a perícia inconclusiva sobre a origem do disparo afasta a responsabilidade do Estado.",
 "STF, Tema 1.237 (ARE 1.385.315).","inverte ônus e efeito da perícia","r06b",jur=True)
P("R06",["9"],"conceito_correto","confusao_instituto",4,
 "A teoria do risco integral, que não admite excludentes de responsabilidade, é aplicada excepcionalmente, como nos casos de dano nuclear e de dano ambiental.",
 "A teoria do risco integral, que não admite excludentes de responsabilidade, é a regra geral aplicável a todos os danos causados por agentes públicos, nos termos do art. 37, § 6º, da Constituição.",
 "Risco integral.","generaliza risco integral","r06c")
P("R06",["14"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, a imunidade material parlamentar configura excludente da responsabilidade civil objetiva do Estado por opiniões, palavras e votos; o parlamentar que extrapola a imunidade responde pessoalmente, sob regime subjetivo.",
 "Segundo o STF, a imunidade material parlamentar não afasta a responsabilidade civil objetiva do Estado por opiniões, palavras e votos, respondendo a União pelos danos causados pelo parlamentar.",
 "STF, Tema 950 (RE 632.115).","nega excludente da imunidade","r06d",jur=True)
P("R06",["14"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, o Estado responde objetivamente por jornalista ferido por agentes policiais em tumulto, podendo ser admitida a culpa exclusiva da vítima quando ela descumpre advertência clara sobre as áreas delimitadas, com grave risco à integridade física.",
 "Segundo o STF, o Estado responde objetivamente por jornalista ferido por agentes policiais em tumulto, não se admitindo a culpa exclusiva da vítima como excludente, ainda que ela descumpra advertência clara.",
 "STF, Tema 1.055 (RE 1.209.429).","nega excludente","r06e",jur=True)
# R07
P("R07",["10"],"conceito_correto","troca_autoridade",4,
 "Segundo o STF, a ação por danos causados por agente público deve ser ajuizada somente contra o Estado ou a pessoa jurídica de direito privado prestadora de serviço público, sendo parte ilegítima o autor do ato, assegurado o direito de regresso.",
 "Segundo o STF, a ação por danos causados por agente público deve ser ajuizada diretamente contra o agente, sendo parte ilegítima o Estado, que responde apenas subsidiariamente após o esgotamento do patrimônio do agente.",
 "STF, Tema 940 (RE 1.027.633).","inverte legitimidade passiva","r07a",jur=True)
P("R07",["10"],"conceito_correto","excecao_omitida",3,
 "A ação regressiva do Estado contra o agente público causador do dano depende da comprovação de dolo ou culpa do agente, e a denunciação da lide ao agente, na ação indenizatória proposta pelo lesado, não é obrigatória.",
 "A ação regressiva do Estado contra o agente público causador do dano independe de dolo ou culpa do agente, e a denunciação da lide ao agente, na ação indenizatória proposta pelo lesado, é obrigatória sob pena de perda do direito de regresso.",
 "CF, art. 37, § 6º; STJ.","dispensa dolo ou culpa e torna obrigatória a denunciação","r07b")
P("R07",["11"],"conceito_correto","troca_numero",3,
 "A pretensão de indenização contra a Fazenda Pública por danos causados por seus agentes prescreve em cinco anos, nos termos do Decreto 20.910/1932 e da Lei 9.494/1997, e não no prazo do Código Civil.",
 "A pretensão de indenização contra a Fazenda Pública por danos causados por seus agentes prescreve em três anos, nos termos do Código Civil, que prevalece sobre o Decreto 20.910/1932 e sobre a Lei 9.494/1997.",
 "Decreto 20.910/1932, art. 1º; Lei 9.494/1997, art. 1º-C.","troca prazo e norma aplicável","r07c")
P("R07",["11"],"conceito_correto","excecao_omitida",4,
 "Segundo o STF, é prescritível a ação de reparação de danos à Fazenda Pública decorrente de ilícito civil.",
 "Segundo o STF, é imprescritível a ação de reparação de danos à Fazenda Pública decorrente de qualquer ilícito civil, por aplicação do art. 37, § 5º, da Constituição.",
 "STF, Tema 666 (RE 669.069).","generaliza imprescritibilidade","r07d",jur=True)
# R08
P("R08",["12"],"conceito_correto","excecao_omitida",4,
 "Quanto aos atos judiciais, em regra o Estado não responde, mas a Constituição prevê que o Estado indenizará o condenado por erro judiciário, assim como o que ficar preso além do tempo fixado na sentença.",
 "Quanto aos atos judiciais, o Estado responde, objetivamente, por decisão judicial reformada em instância superior, sendo irrelevante a existência de erro judiciário ou de prisão além do tempo fixado na sentença.",
 "CF, art. 5º, LXXV.","generaliza responsabilidade por atos judiciais","r08a",lei=True)
P("R08",["12"],"conceito_correto","troca_autoridade",4,
 "Em dano decorrente de obra pública executada por empreiteira contratada pela Administração, a empreiteira responde diretamente, e o Estado responde subsidiariamente, se a empresa não puder arcar com a indenização.",
 "Em dano decorrente de obra pública executada por empreiteira contratada pela Administração, o Estado responde de forma exclusiva, sendo afastada a responsabilidade da empreiteira.",
 "Obras públicas.","exclui a empreiteira","r08b")
P("R08",["13"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, o Estado responde objetivamente pelos danos que tabeliães e oficiais de registro, no exercício de suas funções, causem a terceiros, assegurado o direito de regresso contra o responsável em caso de dolo ou culpa.",
 "Segundo o STF, o Estado não responde pelos danos causados por tabeliães e oficiais de registro, que atuam em caráter privado, respondendo estes de forma direta pelos danos a terceiros.",
 "STF, Tema 777 (RE 842.846).","afasta responsabilidade do Estado","r08c",jur=True)
P("R08",["15"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, quando concurso público organizado por pessoa jurídica de direito privado é anulado por indícios de fraude, o Estado responde subsidiariamente pelos danos materiais causados aos candidatos.",
 "Segundo o STF, quando concurso público organizado por pessoa jurídica de direito privado é anulado por indícios de fraude, o Estado não responde pelos danos materiais causados aos candidatos, que devem acionar exclusivamente a organizadora.",
 "STF, Tema 512 (RE 662.405).","afasta responsabilidade subsidiária","r08d",jur=True)
P("R08",["15"],"conceito_correto","troca_efeito",5,
 "Segundo o STF, o adiamento de concurso público por razões de biossegurança durante a pandemia da Covid-19 não impõe ao Estado o dever de indenizar os candidatos.",
 "Segundo o STF, o adiamento de concurso público por razões de biossegurança durante a pandemia da Covid-19 impõe ao Estado o dever de indenizar os candidatos pelos danos materiais e morais sofridos.",
 "STF, Tema 1.347 (RE 1.455.038).","inverte efeito","r08e",jur=True)
P("R08",["15"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, para responsabilizar o Estado por explosão de fogos de artifício em residência, exige-se a violação de dever jurídico específico de agir, o que ocorre, por exemplo, quando a licença é concedida sem as cautelas legais ou quando o poder público conhece irregularidades e não atua.",
 "Segundo o STF, o Estado responde objetivamente por explosão de fogos de artifício em residência quando tenha concedido licença de funcionamento à fábrica, ainda que observadas todas as cautelas legais e sem conhecimento de irregularidades.",
 "STF, Tema 366 (RE 136.861).","dispensa dever específico","r08f",jur=True)
P("R08",["12"],"conceito_correto","excecao_omitida",4,
 "Quanto aos atos legislativos, a regra é a irresponsabilidade do Estado, admitindo-se a responsabilização, entre outras hipóteses, quando a lei for declarada inconstitucional ou produzir efeitos concretos causadores de dano a particular.",
 "Quanto aos atos legislativos, o Estado responde objetivamente pelo dano decorrente da edição de leis, ainda que constitucionais e de efeitos gerais e abstratos.",
 "Atos legislativos.","generaliza responsabilidade por leis","r08g")
