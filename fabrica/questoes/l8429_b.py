# Lei 8.429/92 (com Lei 14.230/21) — lote L3, parte b (Q07–Q12: declaração/representação, indisponibilidade, processo, ANPC, sentença, afastamento)
Q = []
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# ---- Q07
P("Q07",["13"],"conceito_correto","troca_autoridade",2,
 "A posse e o exercício de agente público ficam condicionados à apresentação de declaração de imposto de renda e proventos de qualquer natureza que tenha sido apresentada à Secretaria Especial da Receita Federal do Brasil, a fim de ser arquivada no serviço de pessoal competente.",
 "A posse e o exercício de agente público ficam condicionados à apresentação de declaração de bens e valores do seu patrimônio privado, a ser entregue ao Tribunal de Contas da respectiva esfera, a fim de ser arquivada em seus registros.",
 "Art. 13, caput: declaração de imposto de renda entregue à Receita, arquivada no serviço de pessoal.","troca documento e destinatário","q07a")
P("Q07",["13"],"conceito_correto","troca_numero",2,
 "A declaração de bens exigida para a posse será atualizada anualmente e na data em que o agente público deixar o exercício do mandato, do cargo, do emprego ou da função.",
 "A declaração de bens exigida para a posse será atualizada a cada dois anos e apenas na data em que o agente público assumir novo mandato, cargo, emprego ou função.",
 "Art. 13, § 2.º.","altera periodicidade","q07b")
P("Q07",["13"],"conceito_correto","troca_efeito",2,
 "Será apenado com a pena de demissão, sem prejuízo de outras sanções cabíveis, o agente público que se recusar a prestar a declaração de bens dentro do prazo determinado ou que prestar declaração falsa.",
 "Será apenado com a pena de suspensão por até noventa dias, sem prejuízo de outras sanções cabíveis, o agente público que se recusar a prestar a declaração de bens dentro do prazo determinado ou que prestar declaração falsa.",
 "Art. 13, § 3.º: demissão.","troca a penalidade","q07c")
P("Q07",["14"],"conceito_correto","restricao_indevida",2,
 "Qualquer pessoa poderá representar à autoridade administrativa competente para que seja instaurada investigação destinada a apurar a prática de ato de improbidade.",
 "Somente o cidadão no gozo de seus direitos políticos poderá representar à autoridade administrativa competente para que seja instaurada investigação destinada a apurar a prática de ato de improbidade.",
 "Art. 14, caput.","restringe legitimidade","q07d")
P("Q07",["14"],"conceito_correto","excecao_omitida",3,
 "A autoridade administrativa rejeitará, em despacho fundamentado, a representação que não contenha as formalidades legais (escrita ou reduzida a termo e assinada, com qualificação do representante, informações sobre o fato e indicação de provas), sem que a rejeição impeça a representação ao Ministério Público.",
 "A autoridade administrativa que rejeitar, em despacho fundamentado, a representação que não contenha as formalidades legais encerrará a apuração, pois a rejeição impede nova representação ao Ministério Público quanto aos mesmos fatos.",
 "Art. 14, §§ 1.º e 2.º.","rejeição impede representação ao MP","q07e")
P("Q07",["15"],"conceito_correto","troca_autoridade",3,
 "A comissão processante dará conhecimento ao Ministério Público e ao Tribunal ou Conselho de Contas da existência de procedimento administrativo para apurar a prática de ato de improbidade, podendo esses órgãos designar representante para acompanhar o procedimento.",
 "A comissão processante dará conhecimento apenas ao Ministério Público da existência de procedimento administrativo para apurar a prática de ato de improbidade, podendo este designar representante para acompanhar o procedimento; o Tribunal de Contas só será comunicado após a conclusão.",
 "Art. 15 e parágrafo único.","omite o Tribunal de Contas","q07f")
P("Q07",["22"],"conceito_correto","restricao_indevida",3,
 "Para apurar qualquer ilícito previsto na Lei de Improbidade, o Ministério Público, de ofício, a requerimento de autoridade administrativa ou mediante representação, poderá instaurar inquérito civil ou procedimento investigativo assemelhado e requisitar a instauração de inquérito policial.",
 "Para apurar qualquer ilícito previsto na Lei de Improbidade, o Ministério Público somente poderá instaurar inquérito civil mediante representação formulada nos termos do art. 14, vedada a atuação de ofício e a requisição de inquérito policial.",
 "Art. 22, caput.","restringe atuação do MP","q07g")
P("Q07",["22"],"conceito_correto","excecao_omitida",3,
 "Na apuração dos ilícitos previstos na Lei de Improbidade, será garantida ao investigado a oportunidade de manifestação por escrito e de juntada de documentos que comprovem suas alegações e auxiliem na elucidação dos fatos.",
 "Na apuração dos ilícitos previstos na Lei de Improbidade, por ser o inquérito civil de natureza inquisitorial, não se admite a manifestação por escrito do investigado nem a juntada de documentos antes do ajuizamento da ação.",
 "Art. 22, parágrafo único (Lei 14.230/21).","nega contraditório na investigação","q07h")
P("Q07",["7"],"conceito_correto","troca_autoridade",2,
 "Havendo indícios de ato de improbidade, a autoridade que conhecer dos fatos representará ao Ministério Público competente, para as providências necessárias.",
 "Havendo indícios de ato de improbidade, a autoridade que conhecer dos fatos representará ao Tribunal de Contas competente, que decidirá sobre o encaminhamento ao Ministério Público.",
 "Art. 7.º.","troca o destinatário","q07i")
# ---- Q08
P("Q08",["16"],"conceito_correto","restricao_indevida",2,
 "Na ação por improbidade administrativa poderá ser formulado, em caráter antecedente ou incidente, pedido de indisponibilidade de bens dos réus, a fim de garantir a integral recomposição do erário ou do acréscimo patrimonial resultante de enriquecimento ilícito.",
 "Na ação por improbidade administrativa poderá ser formulado, apenas em caráter incidente, pedido de indisponibilidade de bens dos réus, a fim de garantir a integral recomposição do erário, não se aplicando a medida às hipóteses de enriquecimento ilícito.",
 "Art. 16, caput.","restringe cabimento","q08a")
P("Q08",["16"],"conceito_correto","excecao_omitida",3,
 "A indisponibilidade de bens apenas será deferida mediante a demonstração, no caso concreto, de perigo de dano irreparável ou de risco ao resultado útil do processo, desde que o juiz se convença da probabilidade dos atos descritos na inicial, após a oitiva do réu em cinco dias.",
 "A indisponibilidade de bens será deferida mediante a demonstração da probabilidade dos atos descritos na inicial, presumindo-se o perigo de dano irreparável ou o risco ao resultado útil do processo nas ações fundadas no art. 10, e sem necessidade de prévia oitiva do réu.",
 "Art. 16, §§ 3.º e 4.º: perigo de dano ou risco ao resultado útil comprovados; oitiva em 5 dias; urgência não pode ser presumida.","presume urgência","q08b")
P("Q08",["16"],"conceito_correto","excecao_omitida",3,
 "A indisponibilidade de bens poderá ser decretada sem a oitiva prévia do réu sempre que o contraditório prévio puder comprovadamente frustrar a efetividade da medida ou houver outras circunstâncias que recomendem a proteção liminar, não podendo a urgência ser presumida.",
 "A indisponibilidade de bens poderá ser decretada sem a oitiva prévia do réu sempre que o juiz presumir que o contraditório prévio possa frustrar a efetividade da medida, bastando a gravidade em abstrato da conduta imputada.",
 "Art. 16, § 4.º.","admite presunção de urgência","q08c")
P("Q08",["16"],"conceito_correto","troca_numero",3,
 "Havendo mais de um réu na ação, a somatória dos valores declarados indisponíveis não poderá superar o montante indicado na petição inicial como dano ao erário ou como enriquecimento ilícito.",
 "Havendo mais de um réu na ação, o valor indisponível de cada réu poderá alcançar o total indicado na petição inicial como dano ao erário, respondendo solidariamente todos os demandados.",
 "Art. 16, § 5.º.","admite solidariedade","q08d")
P("Q08",["16"],"conceito_correto","troca_efeito",3,
 "A indisponibilidade recairá sobre bens que assegurem exclusivamente o integral ressarcimento do dano ao erário, sem incidir sobre os valores a serem eventualmente aplicados a título de multa civil ou sobre acréscimo patrimonial decorrente de atividade lícita.",
 "A indisponibilidade recairá sobre bens que assegurem o integral ressarcimento do dano ao erário e o pagamento da multa civil, incidindo também sobre o acréscimo patrimonial decorrente de atividade lícita, se necessário.",
 "Art. 16, § 10.","inclui multa","q08e")
P("Q08",["16"],"conceito_correto","troca_efeito",3,
 "A ordem de indisponibilidade deverá priorizar veículos de via terrestre, bens imóveis, bens móveis em geral e outros bens enumerados na lei e, apenas na inexistência desses, o bloqueio de contas bancárias, de forma a garantir a subsistência do acusado e a manutenção da atividade empresária.",
 "A ordem de indisponibilidade deverá priorizar o bloqueio de contas bancárias e aplicações financeiras, por serem os ativos de maior liquidez, e somente na sua insuficiência recair sobre veículos, bens imóveis e demais bens enumerados na lei.",
 "Art. 16, § 11.","inverte a ordem","q08f")
P("Q08",["16"],"conceito_correto","troca_numero",3,
 "É vedada a decretação de indisponibilidade da quantia de até quarenta salários mínimos depositados em caderneta de poupança, em outras aplicações financeiras ou em conta-corrente.",
 "É vedada a decretação de indisponibilidade da quantia de até cem salários mínimos depositados em caderneta de poupança, em outras aplicações financeiras ou em conta-corrente.",
 "Art. 16, § 13: 40 salários mínimos.","altera o valor","q08g")
P("Q08",["16"],"conceito_correto","excecao_omitida",3,
 "É vedada a decretação de indisponibilidade do bem de família do réu, salvo se comprovado que o imóvel seja fruto de vantagem patrimonial indevida, conforme descrito no art. 9.º da lei.",
 "É vedada a decretação de indisponibilidade do bem de família do réu, salvo se comprovado que o imóvel tenha sido adquirido com recursos desviados do erário, conforme descrito no art. 10 da lei.",
 "Art. 16, § 14: a exceção é a vantagem patrimonial indevida (art. 9.º).","troca o artigo da exceção","q08h")
P("Q08",["16"],"caso_concreto","caso_concreto",4,
 "Em ação de improbidade por lesão ao erário, o Ministério Público pediu a indisponibilidade de R$ 2 milhões, valor do dano indicado na inicial, contra três réus. O juiz decretou o bloqueio de R$ 2 milhões de cada réu, incluindo a multa civil, a cada um. A decisão contraria a lei, pois a soma dos valores indisponíveis não pode superar o dano indicado na inicial e a medida não alcança a multa civil.",
 "Em ação de improbidade por lesão ao erário, o Ministério Público pediu a indisponibilidade de R$ 2 milhões, valor do dano indicado na inicial, contra três réus. O juiz decretou o bloqueio de R$ 2 milhões de cada réu, incluindo a multa civil, a cada um. A decisão está de acordo com a lei, pois cada réu responde pela integralidade do dano e a indisponibilidade pode abranger a multa civil.",
 "Art. 16, §§ 5.º e 10.","admite bloqueio solidário e da multa","q08i")
# ---- Q09
P("Q09",["17"],"conceito_correto","troca_autoridade",3,
 "A ação de improbidade administrativa deverá ser proposta perante o foro do local onde ocorrer o dano ou da pessoa jurídica prejudicada, e a sua propositura previne a competência do juízo para todas as ações posteriores com a mesma causa de pedir ou o mesmo objeto.",
 "A ação de improbidade administrativa deverá ser proposta perante o foro do domicílio do réu, e a sua propositura previne a competência do juízo apenas para as ações posteriores que tenham as mesmas partes.",
 "Art. 17, §§ 4.º-A e 5.º.","altera o foro e a prevenção","q09a")
P("Q09",["17"],"conceito_correto","excecao_omitida",3,
 "A petição inicial deverá individualizar a conduta do réu e apontar os elementos probatórios mínimos que demonstrem a ocorrência das hipóteses dos arts. 9.º, 10 e 11 e de sua autoria, salvo impossibilidade devidamente fundamentada.",
 "A petição inicial poderá imputar genericamente aos réus a prática dos atos de improbidade, dispensada a individualização da conduta de cada um e a indicação de elementos probatórios mínimos, que serão produzidos na instrução.",
 "Art. 17, § 6.º, I.","dispensa individualização","q09b")
P("Q09",["17"],"conceito_correto","troca_numero",2,
 "Estando a petição inicial em devida forma, o juiz mandará autuá-la e ordenará a citação dos requeridos para que a contestem no prazo comum de trinta dias.",
 "Estando a petição inicial em devida forma, o juiz mandará autuá-la e ordenará a citação dos requeridos para que a contestem no prazo comum de quinze dias, dobrado quando houver litisconsortes com procuradores diferentes.",
 "Art. 17, § 7.º: prazo comum de 30 dias.","troca prazo","q09c")
P("Q09",["17"],"conceito_correto","excecao_omitida",3,
 "Havendo possibilidade de solução consensual, as partes poderão requerer ao juiz a interrupção do prazo para a contestação, por prazo não superior a noventa dias.",
 "Havendo possibilidade de solução consensual, as partes poderão requerer ao juiz a suspensão do prazo para a contestação, por prazo não superior a cento e oitenta dias, prorrogável uma vez.",
 "Art. 17, § 10-A: interrupção por até 90 dias.","altera prazo e instituto","q09d")
P("Q09",["17"],"conceito_correto","restricao_indevida",4,
 "Após a réplica do Ministério Público, o juiz proferirá decisão na qual indicará com precisão a tipificação do ato imputável ao réu, sendo-lhe vedado modificar o fato principal e a capitulação legal apresentada pelo autor.",
 "Após a réplica do Ministério Público, o juiz proferirá decisão na qual indicará a tipificação do ato imputável ao réu, podendo, com fundamento no princípio iura novit curia, alterar a capitulação legal apresentada pelo autor, desde que mantido o fato principal.",
 "Art. 17, § 10-C.","admite mudança de capitulação","q09e")
P("Q09",["17"],"conceito_correto","excecao_omitida",3,
 "Para cada ato de improbidade deverá necessariamente ser indicado apenas um tipo dentre os previstos nos arts. 9.º, 10 e 11, e será nula a decisão de mérito que condenar o réu por tipo diverso daquele definido na petição inicial.",
 "Para cada ato de improbidade poderão ser indicados cumulativamente os tipos dos arts. 9.º, 10 e 11, e a decisão de mérito que condenar o réu por tipo diverso do da petição inicial é válida, desde que respeitado o contraditório.",
 "Art. 17, §§ 10-D e 10-F, I.","admite cumulação de tipos","q09f")
P("Q09",["17"],"conceito_correto","troca_efeito",3,
 "Será nula a decisão de mérito, total ou parcial, da ação de improbidade que condenar o requerido sem a produção das provas por ele tempestivamente especificadas.",
 "Será anulável, mediante comprovação de prejuízo, a decisão de mérito da ação de improbidade que condenar o requerido sem a produção das provas por ele tempestivamente especificadas, salvo se o juiz as considerar protelatórias.",
 "Art. 17, § 10-F, II.","relativiza a nulidade","q09g")
P("Q09",["17"],"conceito_correto","troca_efeito",3,
 "Não se aplicam à ação de improbidade administrativa a presunção de veracidade dos fatos alegados pelo autor em caso de revelia, nem a imposição de ônus da prova ao réu na forma dos §§ 1.º e 2.º do art. 373 do CPC.",
 "Aplica-se à ação de improbidade administrativa a presunção de veracidade dos fatos alegados pelo autor em caso de revelia, mas é vedada a imposição de ônus da prova ao réu na forma dos §§ 1.º e 2.º do art. 373 do CPC.",
 "Art. 17, § 19, I e II.","aplica presunção de revelia","q09h")
P("Q09",["17"],"conceito_correto","excecao_omitida",3,
 "Em qualquer momento do processo, se o juiz identificar ilegalidades ou irregularidades administrativas a sanar sem que estejam presentes todos os requisitos para a imposição das sanções, poderá, em decisão motivada, converter a ação de improbidade em ação civil pública, cabendo agravo de instrumento dessa decisão.",
 "Em qualquer momento do processo, se o juiz identificar ilegalidades ou irregularidades administrativas a sanar sem que estejam presentes todos os requisitos para as sanções, deverá extinguir a ação sem resolução do mérito, vedada a conversão em ação civil pública.",
 "Art. 17, §§ 16 e 17.","veda conversão","q09i")
P("Q09",["17"],"conceito_correto","troca_efeito",3,
 "Ao réu será assegurado o direito de ser interrogado sobre os fatos de que trata a ação, e a sua recusa ou o seu silêncio não implicarão confissão.",
 "Ao réu será assegurado o direito de ser interrogado sobre os fatos de que trata a ação, e a sua recusa ou o seu silêncio implicarão confissão ficta quanto aos fatos que lhe forem imputados.",
 "Art. 17, § 18.","silêncio como confissão","q09j")
P("Q09",["17"],"conceito_correto","excecao_omitida",3,
 "Não se aplica na ação de improbidade o ajuizamento de mais de uma ação pelo mesmo fato, competindo ao Conselho Nacional do Ministério Público dirimir conflitos de atribuições entre membros de Ministérios Públicos distintos.",
 "Admite-se o ajuizamento de mais de uma ação de improbidade pelo mesmo fato, uma por cada ente lesado, competindo ao Superior Tribunal de Justiça dirimir conflitos de atribuições entre membros de Ministérios Públicos distintos.",
 "Art. 17, § 19, III.","troca autoridade e admite duplicidade","q09k")
P("Q09",["17"],"conceito_correto","troca_autoridade",3,
 "A assessoria jurídica que emitiu parecer atestando a legalidade prévia dos atos praticados pelo administrador público ficará obrigada a defendê-lo judicialmente, caso ele responda por ação de improbidade, até que a decisão transite em julgado.",
 "A assessoria jurídica que emitiu parecer atestando a legalidade prévia dos atos praticados pelo administrador público responderá solidariamente com ele na ação de improbidade, por ter concorrido para o ato.",
 "Art. 17, § 20.","atribui responsabilidade solidária","q09l")
P("Q09",["17"],"caso_concreto","caso_concreto",4,
 "Em ação de improbidade, o réu, regularmente citado, não apresentou contestação. O juiz, ao decretar a revelia, considerou verdadeiros os fatos alegados pelo autor e julgou procedente o pedido. A decisão é incompatível com a lei, pois na ação de improbidade não incide a presunção de veracidade dos fatos em caso de revelia.",
 "Em ação de improbidade, o réu, regularmente citado, não apresentou contestação. O juiz, ao decretar a revelia, considerou verdadeiros os fatos alegados pelo autor e julgou procedente o pedido. A decisão é compatível com a lei, pois, na ausência de contestação, o ônus de impugnar os fatos recai integralmente sobre o réu.",
 "Art. 17, § 19, I.","aplica presunção na revelia","q09m")
# ---- Q10
P("Q10",["17B"],"conceito_correto","excecao_omitida",3,
 "O Ministério Público poderá, conforme as circunstâncias do caso concreto, celebrar acordo de não persecução civil, desde que dele advenham, ao menos, o integral ressarcimento do dano e a reversão à pessoa jurídica lesada da vantagem indevida obtida, ainda que oriunda de agentes privados.",
 "O Ministério Público poderá celebrar acordo de não persecução civil, desde que dele advenha, ao menos, o ressarcimento de metade do dano e a reversão à pessoa jurídica lesada da vantagem indevida, limitada esta aos valores obtidos por agentes públicos.",
 "Art. 17-B, I e II.","ressarcimento parcial","q10a")
P("Q10",["17B"],"conceito_correto","excecao_omitida",3,
 "A celebração do acordo de não persecução civil dependerá, cumulativamente, da oitiva do ente federativo lesado, da aprovação pelo órgão do Ministério Público competente para apreciar arquivamento de inquéritos civis, no prazo de até sessenta dias, se anterior ao ajuizamento da ação, e de homologação judicial.",
 "A celebração do acordo de não persecução civil dependerá da oitiva do ente federativo lesado e da aprovação pelo órgão do Ministério Público competente, dispensada a homologação judicial quando o acordo for celebrado antes do ajuizamento da ação de improbidade.",
 "Art. 17-B, § 1.º: homologação judicial sempre, antes ou depois da ação.","dispensa homologação","q10b")
P("Q10",["17B"],"conceito_correto","troca_autoridade",3,
 "Para fins de apuração do valor do dano a ser ressarcido no acordo de não persecução civil, deverá ser realizada a oitiva do Tribunal de Contas competente, que se manifestará, com indicação dos parâmetros utilizados, no prazo de noventa dias.",
 "Para fins de apuração do valor do dano a ser ressarcido no acordo de não persecução civil, a manifestação do Tribunal de Contas competente, no prazo de trinta dias, vincula o Ministério Público e o juiz que o homologará.",
 "Art. 17-B, § 3.º: oitiva, 90 dias; manifestação não vinculante.","atribui efeito vinculante e altera prazo","q10c")
P("Q10",["17B"],"conceito_correto","restricao_indevida",3,
 "O acordo de não persecução civil poderá ser celebrado no curso da investigação, no curso da ação de improbidade ou no momento da execução da sentença condenatória.",
 "O acordo de não persecução civil somente poderá ser celebrado no curso da investigação, antes do ajuizamento da ação de improbidade, não se admitindo após a propositura da ação ou na fase de execução.",
 "Art. 17-B, § 4.º.","limita o momento","q10d")
P("Q10",["17B"],"conceito_correto","troca_numero",3,
 "Em caso de descumprimento do acordo de não persecução civil, o investigado ou demandado ficará impedido de celebrar novo acordo pelo prazo de cinco anos, contado do conhecimento pelo Ministério Público do efetivo descumprimento.",
 "Em caso de descumprimento do acordo de não persecução civil, o investigado ou demandado ficará impedido de celebrar novo acordo pelo prazo de dez anos, contado da data da homologação judicial do acordo descumprido.",
 "Art. 17-B, § 7.º: 5 anos, contados do conhecimento do descumprimento pelo MP.","altera prazo e termo inicial","q10e")
P("Q10",["17B"],"conceito_correto","excecao_omitida",3,
 "As negociações do acordo de não persecução civil ocorrerão entre o Ministério Público, de um lado, e, de outro, o investigado ou demandado e o seu defensor, e o acordo poderá contemplar mecanismos internos de integridade, auditoria e incentivo à denúncia de irregularidades.",
 "As negociações do acordo de não persecução civil ocorrerão entre o juiz e o investigado ou demandado, assistido por seu defensor, podendo o Ministério Público intervir como fiscal da ordem jurídica, e o acordo não poderá impor mecanismos de integridade à pessoa jurídica.",
 "Art. 17-B, §§ 5.º e 6.º.","atribui negociação ao juiz","q10f")
P("Q10",["17B"],"caso_concreto","caso_concreto",4,
 "Servidor investigado em inquérito civil por lesão ao erário propôs ao Ministério Público acordo de não persecução civil. O acordo prevê o ressarcimento integral do dano, a reversão da vantagem indevida e o pagamento de multa. Para sua eficácia, deverá o acordo ser aprovado pelo órgão do MP competente para apreciar arquivamento de inquéritos civis, no prazo legal, ouvido o ente lesado e o Tribunal de Contas quanto ao valor do dano, e homologado em juízo.",
 "Servidor investigado em inquérito civil por lesão ao erário propôs ao Ministério Público acordo de não persecução civil. O acordo prevê o ressarcimento integral do dano, a reversão da vantagem indevida e o pagamento de multa. Como o acordo foi celebrado antes do ajuizamento da ação, basta a aprovação do órgão do MP competente, sendo dispensadas a oitiva do ente lesado e a homologação em juízo.",
 "Art. 17-B, §§ 1.º e 3.º.","dispensa oitiva e homologação","q10g")
# ---- Q11
P("Q11",["17C"],"conceito_correto","troca_efeito",3,
 "Na hipótese de litisconsórcio passivo na ação de improbidade, a condenação ocorrerá no limite da participação e dos benefícios diretos de cada réu, vedada qualquer solidariedade.",
 "Na hipótese de litisconsórcio passivo na ação de improbidade, a condenação ao ressarcimento do dano será solidária entre todos os réus, respondendo cada um pela integralidade do prejuízo.",
 "Art. 17-C, § 2.º.","solidariedade","q11a")
P("Q11",["17C"],"conceito_correto","troca_efeito",2,
 "Não haverá remessa necessária nas sentenças proferidas nos processos de improbidade administrativa.",
 "Haverá remessa necessária nas sentenças de improcedência proferidas nos processos de improbidade administrativa, por se tratar de ação que tutela o patrimônio público.",
 "Art. 17-C, § 3.º, e art. 17, § 19, IV.","exige remessa necessária","q11b")
P("Q11",["17C"],"conceito_correto","excecao_omitida",3,
 "A ilegalidade sem a presença de dolo que a qualifique não configura ato de improbidade, e a sentença deverá indicar de modo preciso os fundamentos que demonstrem os elementos dos arts. 9.º, 10 e 11, que não podem ser presumidos.",
 "A ilegalidade praticada com culpa grave configura ato de improbidade, e a sentença poderá presumir os elementos dos arts. 9.º, 10 e 11 quando a conduta for manifestamente contrária à lei.",
 "Art. 17-C, caput, I, e § 1.º.","admite culpa grave e presunção","q11c")
P("Q11",["17D"],"conceito_correto","confusao_instituto",3,
 "A ação por improbidade administrativa é repressiva e de caráter sancionatório, destinada à aplicação de sanções de caráter pessoal, e não constitui ação civil, sendo vedado seu ajuizamento para o controle de legalidade de políticas públicas e para a proteção do patrimônio público e social, do meio ambiente e de outros interesses difusos.",
 "A ação por improbidade administrativa constitui espécie de ação civil pública, destinada à proteção do patrimônio público e social e ao controle de legalidade de políticas públicas, além da aplicação das sanções pessoais previstas na lei.",
 "Art. 17-D.","equipara à ação civil pública","q11d")
P("Q11",["18"],"conceito_correto","troca_autoridade",3,
 "A sentença que julgar procedente a ação fundada nos arts. 9.º e 10 condenará ao ressarcimento dos danos e à perda ou reversão dos bens e valores ilicitamente adquiridos em favor da pessoa jurídica prejudicada pelo ilícito.",
 "A sentença que julgar procedente a ação fundada nos arts. 9.º, 10 e 11 condenará ao ressarcimento dos danos e à perda ou reversão dos bens e valores ilicitamente adquiridos em favor do Fundo de Defesa de Direitos Difusos.",
 "Art. 18, caput: em favor da pessoa jurídica prejudicada; só arts. 9.º e 10.","troca beneficiário","q11e")
P("Q11",["18"],"conceito_correto","troca_numero",3,
 "Se a pessoa jurídica prejudicada não adotar as providências de liquidação e cumprimento da sentença no prazo de seis meses, contado do trânsito em julgado, caberá ao Ministério Público proceder à liquidação do dano e ao cumprimento da sentença de ressarcimento.",
 "Se a pessoa jurídica prejudicada não adotar as providências de liquidação e cumprimento da sentença no prazo de um ano, contado da publicação da sentença, caberá ao Ministério Público proceder à liquidação do dano e ao cumprimento da sentença de ressarcimento.",
 "Art. 18, § 2.º: 6 meses do trânsito em julgado.","altera prazo e termo","q11f")
P("Q11",["18"],"conceito_correto","troca_numero",3,
 "O juiz poderá autorizar o parcelamento, em até quarenta e oito parcelas mensais corrigidas monetariamente, do débito resultante de condenação por improbidade, se o réu demonstrar incapacidade financeira de saldá-lo de imediato.",
 "O juiz poderá autorizar o parcelamento, em até sessenta parcelas mensais, sem correção monetária, do débito resultante de condenação por improbidade, se o réu demonstrar incapacidade financeira de saldá-lo de imediato.",
 "Art. 18, § 4.º: 48 parcelas corrigidas.","altera parcelas","q11g")
P("Q11",["18"],"conceito_correto","excecao_omitida",3,
 "Para fins de apuração do valor do ressarcimento, deverão ser descontados os serviços efetivamente prestados.",
 "Para fins de apuração do valor do ressarcimento, o dano corresponderá à integralidade dos valores pagos, sendo vedado descontar os serviços efetivamente prestados, em razão da nulidade do contrato.",
 "Art. 18, § 3.º.","veda desconto","q11h")
P("Q11",["18A"],"conceito_correto","troca_numero",4,
 "A requerimento do réu, na fase de cumprimento da sentença, o juiz unificará as sanções com outras já impostas em outros processos; na continuidade de ilícito aplicará a maior sanção aumentada de um terço ou a soma das penas, o que for mais benéfico ao réu, e as sanções de suspensão de direitos políticos e de proibição de contratar observarão o limite de vinte anos.",
 "A requerimento do réu, na fase de cumprimento da sentença, o juiz unificará as sanções com outras já impostas em outros processos; na continuidade de ilícito aplicará a maior sanção aumentada de metade ou a soma das penas, o que for mais benéfico ao réu, e as sanções de suspensão de direitos políticos e de proibição de contratar observarão o limite de trinta anos.",
 "Art. 18-A: aumento de 1/3; limite de 20 anos; unificação a requerimento do réu.","altera fração e limite","q11i")
# ---- Q12
P("Q12",["20"],"conceito_correto","troca_efeito",2,
 "A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória.",
 "A perda da função pública e a suspensão dos direitos políticos efetivam-se com a confirmação da sentença condenatória por decisão de órgão colegiado, ainda que pendente recurso.",
 "Art. 20, caput.","antecipa efeitos","q12a")
P("Q12",["20"],"conceito_correto","troca_numero",3,
 "A autoridade judicial poderá determinar o afastamento do agente público do cargo, sem prejuízo da remuneração, quando necessário à instrução processual ou para evitar a iminente prática de novos ilícitos, pelo prazo de até noventa dias, prorrogável uma única vez por igual prazo, mediante decisão motivada.",
 "A autoridade judicial poderá determinar o afastamento do agente público do cargo, com suspensão da remuneração, quando necessário à instrução processual ou para evitar a iminente prática de novos ilícitos, pelo prazo de até cento e oitenta dias, prorrogável enquanto durar a instrução.",
 "Art. 20, §§ 1.º e 2.º: sem prejuízo da remuneração; 90 dias + 90.","suspende remuneração e prazo","q12b")
P("Q12",["21"],"conceito_correto","excecao_omitida",3,
 "A aplicação das sanções da Lei de Improbidade independe da efetiva ocorrência de dano ao patrimônio público, salvo quanto à pena de ressarcimento e às condutas previstas no art. 10, e da aprovação ou rejeição das contas pelo órgão de controle.",
 "A aplicação das sanções da Lei de Improbidade independe da efetiva ocorrência de dano ao patrimônio público em todas as hipóteses, inclusive quanto à pena de ressarcimento e às condutas do art. 10, e fica condicionada à rejeição das contas pelo Tribunal de Contas.",
 "Art. 21, I e II.","omite exceções e condiciona à rejeição de contas","q12c")
P("Q12",["21"],"conceito_correto","troca_efeito",3,
 "A absolvição criminal em ação que discuta os mesmos fatos, confirmada por decisão colegiada, impede o trâmite da ação de improbidade, havendo comunicação com todos os fundamentos de absolvição previstos no art. 386 do Código de Processo Penal.",
 "A absolvição criminal em ação que discuta os mesmos fatos, ainda que por insuficiência de provas, não repercute na ação de improbidade, em razão da independência das instâncias, que é absoluta.",
 "Art. 21, § 4.º.","independência absoluta","q12d")
P("Q12",["21"],"conceito_correto","excecao_omitida",3,
 "As sentenças civis e penais produzirão efeitos em relação à ação de improbidade quando concluírem pela inexistência da conduta ou pela negativa da autoria, e as sanções aplicadas em outras esferas deverão ser compensadas com as aplicadas na ação de improbidade.",
 "As sentenças civis e penais produzirão efeitos em relação à ação de improbidade quando concluírem pela inexistência de provas suficientes, mas as sanções aplicadas em outras esferas não se compensam com as da ação de improbidade.",
 "Art. 21, §§ 3.º e 5.º.","troca fundamento","q12e")
P("Q12",["21"],"conceito_correto","troca_efeito",3,
 "Os atos do órgão de controle interno ou externo serão considerados pelo juiz quando tiverem servido de fundamento para a conduta do agente público, e as provas produzidas perante esses órgãos deverão ser consideradas na formação da convicção do juiz, sem prejuízo da análise do dolo.",
 "As decisões dos órgãos de controle interno ou externo vinculam o juiz da ação de improbidade quando tiverem servido de fundamento para a conduta do agente público, ficando dispensada a análise do dolo.",
 "Art. 21, §§ 1.º e 2.º.","vincula o juiz","q12f")
P("Q12",["20","21"],"caso_concreto","caso_concreto",4,
 "Prefeito foi condenado por improbidade em primeira instância, com perda do cargo. O recurso de apelação ainda está pendente. Durante a instrução, o juiz determinou seu afastamento por noventa dias, sem prejuízo da remuneração. A perda do cargo só se efetivará com o trânsito em julgado, e o afastamento cautelar poderá ser prorrogado uma única vez por igual prazo.",
 "Prefeito foi condenado por improbidade em primeira instância, com perda do cargo. O recurso de apelação ainda está pendente. Durante a instrução, o juiz determinou seu afastamento por noventa dias, sem prejuízo da remuneração. A perda do cargo se efetivou com a sentença, e o afastamento cautelar poderá ser prorrogado quantas vezes forem necessárias à instrução.",
 "Art. 20, caput e §§ 1.º e 2.º.","antecipa perda e admite prorrogações","q12g")
