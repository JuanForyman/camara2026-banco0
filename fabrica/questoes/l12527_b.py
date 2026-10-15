# Lei 12.527/11 (LAI) — lote L4, parte b (R07–R12)
Q = []
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# ---- R07
P("R07",["21"],"conceito_correto","excecao_omitida",3,
 "Não poderá ser negado acesso à informação necessária à tutela judicial ou administrativa de direitos fundamentais, e as informações ou documentos que versem sobre condutas que impliquem violação dos direitos humanos praticada por agentes públicos ou a mando de autoridades públicas não poderão ser objeto de restrição de acesso.",
 "Poderá ser negado acesso à informação necessária à tutela judicial ou administrativa de direitos fundamentais quando classificada como sigilosa, e as informações sobre violações de direitos humanos praticadas por agentes públicos poderão ser restringidas por até vinte e cinco anos, de acordo com o regime geral da lei.",
 "Art. 21 e parágrafo único.","admite restrição","r07a")
P("R07",["22"],"conceito_correto","regra_como_excecao",3,
 "O disposto na Lei de Acesso à Informação não exclui as demais hipóteses legais de sigilo e de segredo de justiça nem as hipóteses de segredo industrial decorrentes da exploração direta de atividade econômica pelo Estado ou por pessoa física ou entidade privada que tenha vínculo com o poder público.",
 "O disposto na Lei de Acesso à Informação revoga as demais hipóteses legais de sigilo, inclusive o segredo de justiça e o segredo industrial, que passam a se submeter exclusivamente ao regime de classificação da lei, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 22.","revoga outros sigilos","r07b")
P("R07",["23"],"conceito_correto","excecao_omitida",3,
 "São consideradas imprescindíveis à segurança da sociedade ou do Estado, e portanto passíveis de classificação, as informações cuja divulgação ou acesso irrestrito possam pôr em risco a defesa e a soberania nacionais ou a integridade do território, a vida, a segurança ou a saúde da população, ou comprometer atividades de inteligência e de investigação ou fiscalização em andamento.",
 "São passíveis de classificação as informações cuja divulgação possa causar constrangimento a autoridades públicas, bem como aquelas cuja divulgação possa pôr em risco a defesa e a soberania nacionais ou a vida, a segurança ou a saúde da população, na forma prevista na Lei de Acesso à Informação.",
 "Art. 23, I, III e VIII.","inclui hipótese inexistente","r07c")
P("R07",["23"],"conceito_correto","excecao_omitida",3,
 "Também são passíveis de classificação as informações cuja divulgação possa oferecer elevado risco à estabilidade financeira, econômica ou monetária do País, prejudicar planos ou operações estratégicos das Forças Armadas ou pôr em risco a segurança de instituições ou de altas autoridades nacionais ou estrangeiras e seus familiares.",
 "Não são passíveis de classificação as informações cuja divulgação possa oferecer elevado risco à estabilidade financeira, econômica ou monetária do País, por serem de interesse público geral, mas são as que possam prejudicar planos ou operações estratégicos das Forças Armadas, nos termos da Lei de Acesso à Informação.",
 "Art. 23, IV, V e VII.","retira hipótese","r07d")
P("R07",["24"],"conceito_correto","troca_numero",2,
 "A informação em poder dos órgãos e entidades públicas poderá ser classificada como ultrassecreta, secreta ou reservada, e os prazos máximos de restrição de acesso são de vinte e cinco anos para a ultrassecreta, quinze anos para a secreta e cinco anos para a reservada.",
 "A informação em poder dos órgãos e entidades públicas poderá ser classificada como ultrassecreta, secreta ou reservada, e os prazos máximos de restrição de acesso são de trinta anos para a ultrassecreta, vinte anos para a secreta e dez anos para a reservada.",
 "Art. 24, caput e § 1.º: 25, 15 e 5 anos.","troca prazos","r07e")
P("R07",["24"],"conceito_correto","troca_numero",3,
 "Os prazos máximos de restrição de acesso à informação classificada vigoram a partir da data de sua produção.",
 "Os prazos máximos de restrição de acesso à informação classificada vigoram a partir da data da decisão de classificação.",
 "Art. 24, § 1.º.","muda termo inicial","r07f")
P("R07",["24"],"conceito_correto","excecao_omitida",3,
 "As informações que puderem colocar em risco a segurança do Presidente e Vice-Presidente da República e respectivos cônjuges e filhos serão classificadas como reservadas e ficarão sob sigilo até o término do mandato em exercício ou do último mandato, em caso de reeleição.",
 "As informações que puderem colocar em risco a segurança do Presidente e Vice-Presidente da República e respectivos cônjuges e filhos serão classificadas como secretas e ficarão sob sigilo por quinze anos, contados da data de sua produção, segundo a disciplina da Lei n.º 12.527/2011.",
 "Art. 24, § 2.º.","troca grau e prazo","r07g")
P("R07",["24"],"conceito_correto","excecao_omitida",3,
 "Alternativamente aos prazos máximos, poderá ser estabelecida como termo final de restrição de acesso a ocorrência de determinado evento, desde que este ocorra antes do transcurso do prazo máximo de classificação; transcorrido o prazo ou consumado o evento, a informação tornar-se-á automaticamente de acesso público.",
 "Alternativamente aos prazos máximos, poderá ser estabelecida como termo final de restrição de acesso a ocorrência de determinado evento, ainda que posterior ao prazo máximo; transcorrido o prazo, a informação só se tornará pública após decisão da autoridade classificadora, de acordo com o regime geral da lei.",
 "Art. 24, §§ 3.º e 4.º.","exige decisão para desclassificar","r07h")
P("R07",["24"],"conceito_correto","troca_efeito",3,
 "Para a classificação da informação em determinado grau de sigilo, deverá ser observado o interesse público da informação e utilizado o critério menos restritivo possível, considerados a gravidade do risco ou dano à segurança da sociedade e do Estado e o prazo máximo de restrição ou o evento que defina seu termo final.",
 "Para a classificação da informação em determinado grau de sigilo, deverá ser utilizado o critério mais restritivo possível, em favor da segurança da sociedade e do Estado, considerando-se apenas a gravidade do risco ou dano potencial, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 24, § 5.º.","inverte critério","r07i")
# ---- R08
P("R08",["25","26"],"conceito_correto","excecao_omitida",3,
 "O acesso, a divulgação e o tratamento de informação classificada como sigilosa ficarão restritos a pessoas que tenham necessidade de conhecê-la e que sejam devidamente credenciadas na forma do regulamento, e o acesso à informação classificada cria a obrigação, para aquele que a obteve, de resguardar o sigilo.",
 "O acesso, a divulgação e o tratamento de informação classificada como sigilosa ficarão restritos aos agentes públicos ocupantes de cargo efetivo, independentemente de credenciamento, e quem obtiver o acesso ficará desobrigado de resguardar o sigilo após o término do vínculo.",
 "Art. 25, §§ 1.º e 2.º.","dispensa credenciamento e dever de sigilo","r08a")
P("R08",["26"],"conceito_correto","excecao_omitida",3,
 "A pessoa física ou entidade privada que, em razão de vínculo com o poder público, executar atividades de tratamento de informações sigilosas adotará as providências necessárias para que seus empregados, prepostos ou representantes observem as medidas e procedimentos de segurança das informações.",
 "A pessoa física ou entidade privada que, em razão de vínculo com o poder público, executar atividades de tratamento de informações sigilosas não se submete às medidas de segurança da lei, que obrigam somente os agentes públicos, na forma prevista na Lei de Acesso à Informação.",
 "Art. 26, parágrafo único.","exclui privados","r08b")
P("R08",["27"],"conceito_correto","troca_autoridade",3,
 "No âmbito da administração pública federal, a classificação no grau de ultrassecreto é de competência do Presidente da República, do Vice-Presidente, dos Ministros de Estado e autoridades com as mesmas prerrogativas, dos Comandantes da Marinha, do Exército e da Aeronáutica e dos Chefes de Missões Diplomáticas e Consulares permanentes no exterior.",
 "No âmbito da administração pública federal, a classificação no grau de ultrassecreto é de competência do Presidente da República, do Vice-Presidente, dos Ministros de Estado, dos Comandantes das Forças Armadas e dos titulares de autarquias, fundações ou empresas públicas e sociedades de economia mista, nos termos da Lei de Acesso à Informação.",
 "Art. 27, I: os titulares de autarquias, fundações, empresas públicas e sociedades de economia mista só classificam até o grau secreto.","inclui autoridades no grau ultrassecreto","r08c")
P("R08",["27"],"conceito_correto","troca_autoridade",3,
 "No grau de secreto, a classificação é de competência das autoridades que podem classificar como ultrassecreto e dos titulares de autarquias, fundações ou empresas públicas e sociedades de economia mista.",
 "No grau de secreto, a classificação é de competência exclusiva das autoridades que podem classificar como ultrassecreto, não alcançando os titulares de autarquias, fundações, empresas públicas e sociedades de economia mista.",
 "Art. 27, II.","exclui titulares de entidades da administração indireta","r08d")
P("R08",["27"],"conceito_correto","excecao_omitida",3,
 "No grau de reservado, a classificação é de competência das autoridades que podem classificar nos graus superiores e das que exerçam funções de direção, comando ou chefia, nível DAS 101.5 ou superior, ou de hierarquia equivalente, de acordo com regulamentação específica de cada órgão ou entidade.",
 "No grau de reservado, a classificação é de competência de qualquer servidor público que, por dever de ofício, produza ou custodie a informação, independentemente de função de direção ou chefia, segundo a disciplina da Lei n.º 12.527/2011.",
 "Art. 27, III.","amplia competência","r08e")
P("R08",["27"],"conceito_correto","excecao_omitida",4,
 "A competência para classificar como ultrassecreta e secreta poderá ser delegada pela autoridade responsável a agente público, inclusive em missão no exterior, vedada a subdelegação; e a classificação como ultrassecreta pelos Comandantes das Forças Armadas e pelos Chefes de Missões Diplomáticas deverá ser ratificada pelos respectivos Ministros de Estado.",
 "A competência para classificar como ultrassecreta e secreta poderá ser delegada pela autoridade responsável a agente público, admitida a subdelegação, e a classificação como ultrassecreta pelos Comandantes das Forças Armadas e pelos Chefes de Missões Diplomáticas independe de ratificação, de acordo com o regime geral da lei.",
 "Art. 27, §§ 1.º e 2.º.","admite subdelegação e dispensa ratificação","r08f")
P("R08",["27","28"],"conceito_correto","troca_autoridade",4,
 "A autoridade ou agente público que classificar informação como ultrassecreta deverá encaminhar a decisão de classificação à Comissão Mista de Reavaliação de Informações, no prazo previsto em regulamento.",
 "A autoridade ou agente público que classificar informação como reservada deverá encaminhar a decisão de classificação à Comissão Mista de Reavaliação de Informações, no prazo previsto em regulamento.",
 "Art. 27, § 3.º: só a ultrassecreta.","troca o grau","r08g")
P("R08",["28"],"conceito_correto","excecao_omitida",3,
 "A classificação de informação em qualquer grau de sigilo deverá ser formalizada em decisão que conterá, no mínimo, o assunto sobre o qual versa a informação, o fundamento da classificação, a indicação do prazo de sigilo ou do evento que defina seu termo final e a identificação da autoridade que a classificou.",
 "A classificação de informação em qualquer grau de sigilo poderá ser feita verbalmente, devendo a decisão escrita conter apenas o assunto da informação e o prazo de sigilo, dispensada a identificação da autoridade classificadora, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 28, I a IV.","dispensa elementos","r08h")
P("R08",["29"],"conceito_correto","excecao_omitida",3,
 "A classificação das informações será reavaliada pela autoridade classificadora ou por autoridade hierarquicamente superior, mediante provocação ou de ofício, com vistas à sua desclassificação ou à redução do prazo de sigilo; na redução do prazo, o novo prazo manterá como termo inicial a data da produção da informação.",
 "A classificação das informações somente será reavaliada mediante provocação do interessado, com vistas à sua desclassificação, não se admitindo a redução do prazo de sigilo; na hipótese de redução, o novo prazo contará da data da decisão, na forma prevista na Lei de Acesso à Informação.",
 "Art. 29, caput e § 3.º.","restringe reavaliação","r08i")
P("R08",["30"],"conceito_correto","excecao_omitida",3,
 "A autoridade máxima de cada órgão ou entidade publicará, anualmente, em sítio na internet, o rol das informações desclassificadas nos últimos doze meses, o rol de documentos classificados em cada grau de sigilo e relatório estatístico com a quantidade de pedidos de informação recebidos, atendidos e indeferidos.",
 "A autoridade máxima de cada órgão ou entidade publicará, a cada cinco anos, apenas o rol das informações desclassificadas, ficando o rol de documentos classificados em cada grau de sigilo mantido em sigilo para fins de segurança, nos termos da Lei de Acesso à Informação.",
 "Art. 30, I a III.","altera periodicidade e conteúdo","r08j")
# ---- R09
P("R09",["31"],"conceito_correto","troca_numero",3,
 "As informações pessoais relativas à intimidade, vida privada, honra e imagem terão seu acesso restrito, independentemente de classificação de sigilo e pelo prazo máximo de cem anos a contar da sua data de produção, a agentes públicos legalmente autorizados e à pessoa a que se referirem.",
 "As informações pessoais relativas à intimidade, vida privada, honra e imagem terão seu acesso restrito, mediante classificação de sigilo e pelo prazo máximo de vinte e cinco anos a contar da sua data de produção, a agentes públicos legalmente autorizados e à pessoa a que se referirem.",
 "Art. 31, § 1.º, I: independem de classificação; 100 anos.","exige classificação e troca prazo","r09a")
P("R09",["31"],"conceito_correto","excecao_omitida",3,
 "As informações pessoais poderão ter autorizada sua divulgação ou acesso por terceiros diante de previsão legal ou consentimento expresso da pessoa a que se referirem, e aquele que obtiver acesso a elas será responsabilizado por seu uso indevido.",
 "As informações pessoais poderão ter autorizada sua divulgação ou acesso por terceiros mediante simples requerimento fundamentado do interessado, não respondendo por seu uso indevido quem as obtiver licitamente, segundo a disciplina da Lei n.º 12.527/2011.",
 "Art. 31, § 1.º, II, e § 2.º.","dispensa consentimento e responsabilidade","r09b")
P("R09",["31"],"conceito_correto","excecao_omitida",4,
 "O consentimento do titular não será exigido quando as informações pessoais forem necessárias à prevenção e diagnóstico médico quando a pessoa estiver física ou legalmente incapaz, a estatísticas e pesquisas científicas de evidente interesse público, ao cumprimento de ordem judicial, à defesa de direitos humanos ou à proteção do interesse público e geral preponderante.",
 "O consentimento do titular será sempre exigido para a divulgação de informações pessoais, inclusive para o cumprimento de ordem judicial e para a defesa de direitos humanos, ressalvada apenas a prevenção e o diagnóstico médico de pessoa incapaz, de acordo com o regime geral da lei.",
 "Art. 31, § 3.º, I a V.","retira exceções","r09c")
P("R09",["31"],"conceito_correto","troca_efeito",4,
 "A restrição de acesso à informação relativa à vida privada, honra e imagem de pessoa não poderá ser invocada com o intuito de prejudicar processo de apuração de irregularidades em que o titular das informações estiver envolvido, bem como em ações voltadas para a recuperação de fatos históricos de maior relevância.",
 "A restrição de acesso à informação relativa à vida privada, honra e imagem de pessoa poderá ser invocada em processo de apuração de irregularidades em que o titular estiver envolvido, bem como em ações de recuperação de fatos históricos, por serem direitos fundamentais da personalidade.",
 "Art. 31, § 4.º.","admite invocar a restrição","r09d")
# ---- R10
P("R10",["32"],"conceito_correto","excecao_omitida",3,
 "Constitui conduta ilícita que enseja responsabilidade do agente público ou militar recusar-se a fornecer informação requerida nos termos da lei, retardar deliberadamente o seu fornecimento ou fornecê-la intencionalmente de forma incorreta, incompleta ou imprecisa.",
 "Constitui conduta ilícita que enseja responsabilidade do agente público ou militar recusar-se a fornecer informação requerida, ou retardar seu fornecimento ainda que por negligência, mas não fornecê-la de forma incompleta ou imprecisa, mesmo que intencionalmente.",
 "Art. 32, I.","altera o tipo","r10a")
P("R10",["32"],"conceito_correto","excecao_omitida",3,
 "Constituem condutas ilícitas impor sigilo à informação para obter proveito pessoal ou de terceiro, ou para fins de ocultação de ato ilegal cometido por si ou por outrem, e destruir ou subtrair documentos concernentes a possíveis violações de direitos humanos por parte de agentes do Estado.",
 "Constituem condutas ilícitas impor sigilo à informação para obter proveito pessoal, mas não para fins de ocultação de ato ilegal de terceiro, e destruir documentos concernentes a violações de direitos humanos, desde que já arquivados definitivamente, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 32, V e VII.","restringe condutas","r10b")
P("R10",["32"],"conceito_correto","troca_efeito",4,
 "Atendido o princípio do contraditório, da ampla defesa e do devido processo legal, as condutas ilícitas previstas na lei serão consideradas, para fins da Lei n.º 8.112/1990, infrações administrativas que deverão ser apenadas, no mínimo, com suspensão, segundo os critérios nela estabelecidos.",
 "Atendido o princípio do contraditório, da ampla defesa e do devido processo legal, as condutas ilícitas previstas na lei serão consideradas, para fins da Lei n.º 8.112/1990, infrações administrativas que deverão ser apenadas, no mínimo, com demissão, na forma prevista na Lei de Acesso à Informação.",
 "Art. 32, § 1.º, II.","troca penalidade mínima","r10c")
P("R10",["32"],"conceito_correto","excecao_omitida",3,
 "Pelas condutas ilícitas descritas na lei, o militar ou agente público poderá responder, também, por improbidade administrativa, conforme o disposto nas Leis n.º 1.079/1950 e n.º 8.429/1992.",
 "Pelas condutas ilícitas descritas na lei, o militar ou agente público responderá apenas na esfera disciplinar, vedada a responsabilização por improbidade administrativa, por ser específica a sanção da Lei de Acesso à Informação.",
 "Art. 32, § 2.º.","afasta improbidade","r10d")
P("R10",["33"],"conceito_correto","troca_numero",3,
 "A pessoa física ou entidade privada que detiver informações em virtude de vínculo com o poder público e deixar de observar a lei estará sujeita às sanções de advertência, multa, rescisão do vínculo, suspensão temporária de participar em licitação e impedimento de contratar com a administração por prazo não superior a dois anos e declaração de inidoneidade.",
 "A pessoa física ou entidade privada que detiver informações em virtude de vínculo com o poder público e deixar de observar a lei estará sujeita às sanções de advertência, multa, rescisão do vínculo e suspensão temporária de participar em licitação e impedimento de contratar por prazo não superior a cinco anos, vedada a declaração de inidoneidade.",
 "Art. 33, I a V.","altera prazo e exclui sanção","r10e")
P("R10",["33"],"conceito_correto","troca_autoridade",4,
 "A aplicação da declaração de inidoneidade para licitar ou contratar com a administração pública é de competência exclusiva da autoridade máxima do órgão ou entidade pública, facultada a defesa do interessado no prazo de dez dias da abertura de vista; a reabilitação só será autorizada com o ressarcimento dos prejuízos e após decorrido o prazo da suspensão.",
 "A aplicação da declaração de inidoneidade para licitar ou contratar com a administração pública é de competência da Controladoria-Geral da União, facultada a defesa no prazo de quinze dias; a reabilitação independe do ressarcimento dos prejuízos, nos termos da Lei de Acesso à Informação.",
 "Art. 33, §§ 2.º e 3.º.","troca autoridade e requisito","r10f")
P("R10",["34"],"conceito_correto","troca_efeito",4,
 "Os órgãos e entidades públicas respondem diretamente pelos danos causados em decorrência da divulgação não autorizada ou utilização indevida de informações sigilosas ou pessoais, cabendo a apuração de responsabilidade funcional nos casos de dolo ou culpa, assegurado o direito de regresso.",
 "Somente o agente público responde pelos danos causados em decorrência da divulgação não autorizada ou utilização indevida de informações sigilosas ou pessoais, não respondendo o órgão ou entidade, que não possui direito de regresso, segundo a disciplina da Lei n.º 12.527/2011.",
 "Art. 34.","afasta responsabilidade do órgão","r10g")
# ---- R11
P("R11",["35"],"conceito_correto","troca_autoridade",3,
 "A Comissão Mista de Reavaliação de Informações decide, no âmbito da administração pública federal, sobre o tratamento e a classificação de informações sigilosas, podendo rever a classificação de informações ultrassecretas ou secretas, de ofício ou mediante provocação, e prorrogar o prazo de sigilo da ultrassecreta, sempre por prazo determinado.",
 "A Comissão Mista de Reavaliação de Informações decide, no âmbito da administração pública federal, sobre o tratamento e a classificação de informações sigilosas, podendo rever a classificação de informações de qualquer grau, inclusive reservadas, e prorrogar indefinidamente o prazo de sigilo, de acordo com o regime geral da lei.",
 "Art. 35, § 1.º, I a III.","amplia competência","r11a")
P("R11",["35"],"conceito_correto","troca_numero",4,
 "A prorrogação do prazo de sigilo da informação ultrassecreta pela Comissão Mista é limitada a uma única renovação, e a revisão de ofício de documentos ultrassecretos ou secretos deverá ocorrer, no máximo, a cada quatro anos.",
 "A prorrogação do prazo de sigilo da informação ultrassecreta pela Comissão Mista pode ser renovada quantas vezes forem necessárias, e a revisão de ofício de documentos ultrassecretos ou secretos deverá ocorrer, no máximo, a cada dois anos.",
 "Art. 35, §§ 2.º e 3.º.","altera renovação e prazo","r11b")
P("R11",["35"],"conceito_correto","troca_efeito",4,
 "A não deliberação da Comissão Mista de Reavaliação de Informações sobre a revisão nos prazos previstos implicará a desclassificação automática das informações, e os integrantes da Comissão terão mandato de dois anos, conforme dispuser o regulamento.",
 "A não deliberação da Comissão Mista de Reavaliação de Informações sobre a revisão nos prazos previstos implicará a manutenção da classificação até a deliberação, e os integrantes da Comissão terão mandato de cinco anos, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 35, §§ 4.º e 5.º.","inverte efeito da omissão","r11c")
P("R11",["39"],"conceito_correto","troca_efeito",4,
 "As informações classificadas como secretas e ultrassecretas que não foram reavaliadas no prazo de dois anos, contado do termo inicial de vigência da lei, foram consideradas automaticamente de acesso público.",
 "As informações classificadas como secretas e ultrassecretas que não foram reavaliadas no prazo de dois anos, contado do termo inicial de vigência da lei, tiveram o sigilo mantido até a reavaliação, que podia ser feita a qualquer tempo.",
 "Art. 39, caput e § 4.º.","mantém o sigilo","r11d")
P("R11",["40"],"conceito_correto","troca_autoridade",3,
 "O dirigente máximo de cada órgão ou entidade da administração pública federal direta e indireta designará autoridade que lhe seja diretamente subordinada para assegurar o cumprimento das normas relativas ao acesso a informação, monitorar a implementação da lei e orientar as respectivas unidades.",
 "O Poder Executivo Federal designará um único órgão central, que ficará responsável por assegurar o cumprimento da lei nos órgãos e entidades da administração pública federal, sendo vedada a designação de autoridade em cada órgão, na forma prevista na Lei de Acesso à Informação.",
 "Art. 40, I a IV.","centraliza a autoridade","r11e")
P("R11",["45"],"conceito_correto","troca_autoridade",3,
 "Cabe aos Estados, ao Distrito Federal e aos Municípios, em legislação própria, obedecidas as normas gerais estabelecidas na Lei de Acesso à Informação, definir regras específicas, especialmente quanto ao acesso a informações públicas (art. 9.º) e aos recursos (Seção II do Capítulo III).",
 "Os Estados, o Distrito Federal e os Municípios não possuem competência para legislar sobre acesso à informação, aplicando-se a eles diretamente e de forma exclusiva as regras específicas da Lei de Acesso à Informação, nos termos da Lei de Acesso à Informação.",
 "Art. 45: regras específicas, especialmente quanto ao art. 9.º e à Seção II do Capítulo III (recursos).","nega competência legislativa","r11f")
P("R11",["38","43","44"],"conceito_correto","confusao_instituto",4,
 "A Lei de Acesso à Informação alterou a Lei n.º 8.112/1990 para dispor que o servidor deve levar as irregularidades de que tiver ciência à autoridade superior ou, havendo suspeita de envolvimento desta, a outra autoridade competente, e que nenhum servidor poderá ser responsabilizado por dar ciência de informação concernente à prática de crimes ou improbidade.",
 "A Lei de Acesso à Informação alterou a Lei n.º 8.112/1990 para dispor que o servidor somente deve levar as irregularidades de que tiver ciência à autoridade superior, mesmo que esta esteja envolvida, sob pena de responder administrativamente por violação de sigilo, segundo a disciplina da Lei n.º 12.527/2011.",
 "Arts. 43 e 44 (art. 116, VI, e art. 126-A da Lei 8.112).","inverte a proteção ao informante","r11g")
# ---- R12
P("R12",["11","15","16"],"caso_concreto","caso_concreto",4,
 "Cidadã solicitou a um ministério, pela internet, cópia de contrato administrativo. O pedido foi indeferido sem justificativa. Nesse caso, ela poderá recorrer, em dez dias, à autoridade hierarquicamente superior, que deverá manifestar-se em cinco dias; mantida a negativa, poderá recorrer à Controladoria-Geral da União.",
 "Cidadã solicitou a um ministério, pela internet, cópia de contrato administrativo. O pedido foi indeferido sem justificativa. Nesse caso, ela poderá recorrer, em dez dias, diretamente à Controladoria-Geral da União, independentemente de apreciação por autoridade hierarquicamente superior no âmbito do ministério.",
 "Arts. 7.º, § 4.º, 15 e 16, § 1.º.","dispensa instância prévia","r12a")
P("R12",["10","11"],"caso_concreto","caso_concreto",4,
 "Jornalista pediu a uma autarquia federal, por escrito, dados sobre despesas com diárias de servidores e deixou de informar o motivo do pedido. A autarquia não podia dispor imediatamente da informação. Nessa situação, o pedido não poderia ser recusado por falta de motivação e a autarquia teria, em regra, vinte dias para responder, prorrogáveis por mais dez mediante justificativa.",
 "Jornalista pediu a uma autarquia federal, por escrito, dados sobre despesas com diárias de servidores e deixou de informar o motivo do pedido. A autarquia não podia dispor imediatamente da informação. Nessa situação, o pedido poderia ser indeferido por falta de motivação, e, se aceito, a autarquia teria trinta dias para responder, prorrogáveis por mais quinze.",
 "Art. 10, § 3.º; art. 11, §§ 1.º e 2.º.","exige motivo e altera prazos","r12b")
P("R12",["24","27"],"caso_concreto","caso_concreto",5,
 "O presidente de uma empresa pública federal classificou determinada informação como ultrassecreta, por considerá-la imprescindível à segurança do Estado. A classificação é inválida, pois os titulares de empresas públicas só podem classificar informações até o grau secreto.",
 "O presidente de uma empresa pública federal classificou determinada informação como ultrassecreta, por considerá-la imprescindível à segurança do Estado. A classificação é válida, pois os titulares de empresas públicas têm competência para classificar em qualquer grau, desde que submetam a decisão à Comissão Mista de Reavaliação.",
 "Art. 27, I e II.","amplia competência","r12c")
P("R12",["31"],"caso_concreto","caso_concreto",4,
 "Pesquisador solicitou a um hospital público federal prontuários de pacientes para estatística de interesse público previsto em lei, sem pedir consentimento dos titulares. O acesso pode ser concedido sem consentimento, desde que vedada a identificação das pessoas a que as informações se referirem.",
 "Pesquisador solicitou a um hospital público federal prontuários de pacientes para estatística de interesse público previsto em lei, sem pedir consentimento dos titulares. O acesso deve ser negado, pois a lei exige consentimento expresso em todas as hipóteses de acesso por terceiros a informações pessoais de saúde.",
 "Art. 31, § 3.º, II.","exige consentimento sempre","r12d")
P("R12",["32"],"caso_concreto","caso_concreto",4,
 "Servidor federal destruiu documentos que tratavam de possíveis violações de direitos humanos praticadas por agentes do Estado. A conduta configura ilícito da Lei de Acesso à Informação e, no âmbito da Lei n.º 8.112/1990, deve ser apenada, no mínimo, com suspensão, sem prejuízo de responder também por improbidade.",
 "Servidor federal destruiu documentos que tratavam de possíveis violações de direitos humanos praticadas por agentes do Estado. A conduta configura apenas infração disciplinar leve, sujeita a advertência, e não admite responsabilização por improbidade administrativa, de acordo com o regime geral da lei.",
 "Art. 32, VII, § 1.º, II, e § 2.º.","minimiza a sanção","r12e")
