# LGPD — lote L5, parte a (G01–G08)
Q = []
TAILS=[
 " Essa disciplina integra a Lei Geral de Proteção de Dados Pessoais e alcança o tratamento realizado no território nacional, ainda que por meios digitais.",
 " Trata-se de regra aplicável a qualquer operação de tratamento de dados pessoais, realizada por pessoa natural ou jurídica, de direito público ou privado.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática geral da LGPD, que se aplica aos agentes de tratamento em todas as fases da operação.",
 " Essa seria a orientação extraída da lei para as hipóteses em que o tratamento envolve dados de pessoas naturais identificadas ou identificáveis.",
]
def tail(E,C,i):
    if len(E) < 0.97*len(C):
        need=len(C)-len(E)
        t=TAILS[i%len(TAILS)]
        return E+t if need>60 else E+t[:0]
    return E

def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# ---- G01
P("G01",["1"],"conceito_correto","restricao_indevida",2,
 "A LGPD dispõe sobre o tratamento de dados pessoais, inclusive nos meios digitais, por pessoa natural ou por pessoa jurídica de direito público ou privado, com o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural.",
 "A LGPD dispõe sobre o tratamento de dados pessoais realizado exclusivamente nos meios digitais, por pessoa jurídica de direito privado, com o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural.",
 "Art. 1.º, caput.","restringe meio e sujeitos","g01a")
P("G01",["1"],"conceito_correto","troca_efeito",2,
 "As normas gerais contidas na LGPD são de interesse nacional e devem ser observadas pela União, Estados, Distrito Federal e Municípios.",
 "As normas gerais contidas na LGPD têm caráter supletivo e somente se aplicam aos Estados, ao Distrito Federal e aos Municípios que não editarem legislação própria sobre proteção de dados pessoais.",
 "Art. 1.º, parágrafo único.","torna supletiva","g01b")
P("G01",["2"],"conceito_correto","troca_autoridade",3,
 "São fundamentos da disciplina da proteção de dados pessoais, entre outros, o respeito à privacidade, a autodeterminação informativa, a liberdade de expressão, de informação, de comunicação e de opinião, o desenvolvimento econômico e tecnológico e a inovação, e a livre iniciativa, a livre concorrência e a defesa do consumidor.",
 "São fundamentos da disciplina da proteção de dados pessoais, entre outros, o respeito à privacidade, a autodeterminação informativa, a soberania digital, a segurança nacional e a livre iniciativa, a livre concorrência e a defesa do consumidor.",
 "Art. 2.º: soberania digital e segurança nacional não são fundamentos listados.","inclui fundamentos inexistentes","g01c")
P("G01",["3"],"conceito_correto","excecao_omitida",3,
 "A LGPD aplica-se a qualquer operação de tratamento realizada por pessoa natural ou jurídica, de direito público ou privado, independentemente do meio, do país de sua sede ou do país onde estejam localizados os dados, desde que a operação seja realizada no território nacional, tenha por objetivo a oferta de bens ou serviços a indivíduos localizados no território nacional ou os dados tenham sido coletados no território nacional.",
 "A LGPD aplica-se apenas às operações de tratamento realizadas por pessoa jurídica com sede no território nacional, não alcançando o tratamento realizado por empresa estrangeira, ainda que ofereça serviços a indivíduos localizados no Brasil.",
 "Art. 3.º, I a III.","exige sede no Brasil","g01d")
P("G01",["3"],"conceito_correto","troca_efeito",3,
 "Consideram-se coletados no território nacional os dados pessoais cujo titular nele se encontre no momento da coleta.",
 "Consideram-se coletados no território nacional apenas os dados pessoais de titular com nacionalidade brasileira, independentemente do local em que se encontre no momento da coleta.",
 "Art. 3.º, § 1.º.","troca critério","g01e")
P("G01",["4"],"conceito_correto","troca_efeito",3,
 "A LGPD não se aplica ao tratamento de dados pessoais realizado por pessoa natural para fins exclusivamente particulares e não econômicos, nem ao realizado para fins exclusivamente jornalístico e artísticos.",
 "A LGPD aplica-se ao tratamento de dados pessoais realizado por pessoa natural para fins particulares, ainda que não econômicos, e ao realizado para fins jornalísticos e artísticos, que se submetem apenas aos princípios do art. 6.º.",
 "Art. 4.º, I e II, a.","reduz as exceções","g01f")
P("G01",["4"],"conceito_correto","excecao_omitida",3,
 "A LGPD não se aplica ao tratamento realizado para fins exclusivamente acadêmicos, aplicando-se a essa hipótese os arts. 7.º e 11, nem ao realizado para fins exclusivos de segurança pública, defesa nacional, segurança do Estado ou atividades de investigação e repressão de infrações penais.",
 "A LGPD não se aplica ao tratamento realizado para fins exclusivamente acadêmicos, hipótese em que também são inaplicáveis os arts. 7.º e 11, nem ao realizado para fins de segurança pública, que se regem integralmente pela LGPD quando houver uso comercial.",
 "Art. 4.º, II, b, e III.","afasta bases legais da hipótese acadêmica","g01g")
P("G01",["4"],"conceito_correto","excecao_omitida",4,
 "O tratamento de dados para fins de segurança pública, defesa nacional, segurança do Estado e atividades de investigação e repressão de infrações penais será regido por legislação específica, e é vedado seu tratamento por pessoa de direito privado, exceto em procedimentos sob tutela de pessoa jurídica de direito público, objeto de informe específico à autoridade nacional.",
 "O tratamento de dados para fins de segurança pública, defesa nacional, segurança do Estado e atividades de investigação e repressão de infrações penais poderá ser realizado livremente por pessoa de direito privado, mediante comunicação prévia à autoridade nacional.",
 "Art. 4.º, §§ 1.º e 2.º.","libera tratamento por privados","g01h")
P("G01",["4"],"conceito_correto","excecao_omitida",4,
 "Em nenhum caso a totalidade dos dados pessoais de banco de dados utilizado para segurança pública, defesa nacional, segurança do Estado ou investigação penal poderá ser tratada por pessoa de direito privado, salvo por aquela que possua capital integralmente constituído pelo poder público.",
 "A totalidade dos dados pessoais de banco de dados utilizado para segurança pública ou investigação penal poderá ser tratada por pessoa de direito privado que possua capital majoritariamente constituído pelo poder público.",
 "Art. 4.º, § 4.º: capital integralmente público.","troca integral por majoritário","g01i")
# ---- G02
P("G02",["5"],"conceito_correto","confusao_instituto",2,
 "Dado pessoal é a informação relacionada a pessoa natural identificada ou identificável; dado pessoal sensível é o dado sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural.",
 "Dado pessoal é a informação relacionada a pessoa natural ou jurídica identificada ou identificável; dado pessoal sensível é o dado sobre origem racial, convicção religiosa, opinião política, situação financeira, dado referente à saúde ou à vida sexual ou dado biométrico, ainda que não vinculado a pessoa natural.",
 "Art. 5.º, I e II: pessoa natural; situação financeira não integra o rol de sensíveis.","altera conceito","g02a")
P("G02",["5"],"conceito_correto","confusao_instituto",3,
 "Dado anonimizado é o dado relativo a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento; anonimização é a utilização desses meios, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo.",
 "Dado anonimizado é o dado que, embora relativo a titular, possa ser identificado mediante informação adicional mantida pelo controlador em ambiente controlado e seguro; anonimização é o processo reversível de ocultação dos dados.",
 "Art. 5.º, III e XI (a descrição da E é de pseudonimização, art. 13, § 4.º).","confunde com pseudonimização","g02b")
P("G02",["5"],"conceito_correto","confusao_instituto",2,
 "Controlador é a pessoa natural ou jurídica, de direito público ou privado, a quem competem as decisões referentes ao tratamento de dados pessoais; operador é a pessoa que realiza o tratamento em nome do controlador; agentes de tratamento são o controlador e o operador.",
 "Controlador é a pessoa natural ou jurídica, de direito público ou privado, que realiza o tratamento de dados pessoais em nome do operador, a quem competem as decisões sobre o tratamento; agentes de tratamento são o controlador e o encarregado.",
 "Art. 5.º, VI, VII e IX.","inverte controlador e operador","g02c")
P("G02",["5"],"conceito_correto","troca_autoridade",3,
 "Encarregado é a pessoa indicada pelo controlador e operador para atuar como canal de comunicação entre o controlador, os titulares dos dados e a Autoridade Nacional de Proteção de Dados (ANPD).",
 "Encarregado é a pessoa indicada pela Autoridade Nacional de Proteção de Dados (ANPD) para atuar como canal de comunicação entre o controlador, os titulares dos dados e o operador, e para fiscalizar o tratamento realizado.",
 "Art. 5.º, VIII.","troca quem indica e função","g02d")
P("G02",["5"],"conceito_correto","confusao_instituto",3,
 "Consentimento é a manifestação livre, informada e inequívoca pela qual o titular concorda com o tratamento de seus dados pessoais para uma finalidade determinada.",
 "Consentimento é a manifestação livre, expressa e específica pela qual o titular autoriza, de forma genérica e por prazo indeterminado, o tratamento de seus dados pessoais para as finalidades que o controlador indicar.",
 "Art. 5.º, XII; art. 8.º, § 4.º.","admite autorização genérica","g02e")
P("G02",["5"],"conceito_correto","confusao_instituto",3,
 "Bloqueio é a suspensão temporária de qualquer operação de tratamento, mediante guarda do dado pessoal ou do banco de dados; eliminação é a exclusão de dado ou de conjunto de dados armazenados em banco de dados, independentemente do procedimento empregado.",
 "Bloqueio é a exclusão definitiva de dado ou de conjunto de dados armazenados em banco de dados; eliminação é a suspensão temporária de qualquer operação de tratamento, mediante guarda do dado.",
 "Art. 5.º, XIII e XIV.","inverte bloqueio e eliminação","g02f")
P("G02",["5"],"conceito_correto","confusao_instituto",3,
 "Transferência internacional de dados é a transferência de dados pessoais para país estrangeiro ou organismo internacional do qual o país seja membro, e relatório de impacto à proteção de dados pessoais é a documentação do controlador que descreve os processos de tratamento que podem gerar riscos às liberdades civis e aos direitos fundamentais, com medidas e mecanismos de mitigação.",
 "Transferência internacional de dados é qualquer comunicação de dados pessoais a empresa com sede no exterior, e relatório de impacto à proteção de dados pessoais é a documentação elaborada pela ANPD que descreve os riscos do tratamento realizado pelos agentes de tratamento.",
 "Art. 5.º, XV e XVII.","troca definição e autor","g02g")
P("G02",["5"],"conceito_correto","troca_autoridade",3,
 "Autoridade nacional é o órgão da administração pública responsável por zelar, implementar e fiscalizar o cumprimento da LGPD em todo o território nacional; órgão de pesquisa pode ser órgão ou entidade da administração pública ou pessoa jurídica de direito privado sem fins lucrativos, com sede e foro no País, cuja missão inclua pesquisa básica ou aplicada.",
 "Autoridade nacional é o órgão da administração pública responsável por zelar pelo cumprimento da LGPD apenas no âmbito federal; órgão de pesquisa pode ser qualquer pessoa jurídica de direito privado, com ou sem fins lucrativos, ainda que sediada no exterior.",
 "Art. 5.º, XVIII e XIX.","amplia órgão de pesquisa","g02h")
# ---- G03
P("G03",["6"],"conceito_correto","confusao_instituto",3,
 "Pelo princípio da finalidade, o tratamento deve ser realizado para propósitos legítimos, específicos, explícitos e informados ao titular, sem possibilidade de tratamento posterior de forma incompatível com essas finalidades; pelo princípio da adequação, deve haver compatibilidade do tratamento com as finalidades informadas, de acordo com o contexto do tratamento.",
 "Pelo princípio da finalidade, o tratamento deve ser limitado ao mínimo necessário para a realização de suas finalidades; pelo princípio da adequação, deve haver compatibilidade do tratamento com as finalidades informadas ao titular, ainda que o tratamento posterior seja incompatível.",
 "Art. 6.º, I a III.","troca finalidade por necessidade","g03a")
P("G03",["6"],"conceito_correto","confusao_instituto",3,
 "Pelo princípio da necessidade, o tratamento deve limitar-se ao mínimo necessário para a realização de suas finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos em relação às finalidades.",
 "Pelo princípio da necessidade, o tratamento deve abranger a totalidade dos dados pessoais disponíveis, para garantir a qualidade dos dados e a eficácia do tratamento em relação às suas finalidades.",
 "Art. 6.º, III.","contraria minimização","g03b")
P("G03",["6"],"conceito_correto","confusao_instituto",3,
 "O princípio do livre acesso garante aos titulares consulta facilitada e gratuita sobre a forma e a duração do tratamento, bem como sobre a integralidade de seus dados; o princípio da qualidade dos dados garante exatidão, clareza, relevância e atualização dos dados.",
 "O princípio do livre acesso garante aos titulares consulta facilitada, mediante ressarcimento do custo, sobre a forma e a duração do tratamento; o princípio da qualidade dos dados garante apenas a exatidão dos dados no momento da coleta.",
 "Art. 6.º, IV e V.","admite cobrança e restringe qualidade","g03c")
P("G03",["6"],"conceito_correto","troca_efeito",3,
 "O princípio da transparência garante aos titulares informações claras, precisas e facilmente acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento, observados os segredos comercial e industrial.",
 "O princípio da transparência garante aos titulares informações claras, precisas e facilmente acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento, afastando em qualquer hipótese os segredos comercial e industrial.",
 "Art. 6.º, VI.","afasta segredos","g03d")
P("G03",["6"],"conceito_correto","confusao_instituto",3,
 "Segurança é a utilização de medidas técnicas e administrativas aptas a proteger os dados de acessos não autorizados e de situações acidentais ou ilícitas; prevenção é a adoção de medidas para prevenir a ocorrência de danos em virtude do tratamento; não discriminação é a impossibilidade de tratamento para fins discriminatórios ilícitos ou abusivos.",
 "Segurança é a adoção de medidas para prevenir a ocorrência de danos em virtude do tratamento; prevenção é a utilização de medidas técnicas aptas a proteger os dados; não discriminação é a vedação de qualquer tratamento que diferencie titulares, ainda que por fins lícitos.",
 "Art. 6.º, VII a IX.","troca segurança e prevenção","g03e")
P("G03",["6"],"conceito_correto","troca_efeito",3,
 "O princípio da responsabilização e prestação de contas exige a demonstração, pelo agente, da adoção de medidas eficazes e capazes de comprovar a observância e o cumprimento das normas de proteção de dados pessoais e, inclusive, da eficácia dessas medidas.",
 "O princípio da responsabilização e prestação de contas exige apenas que o agente adote medidas de proteção de dados, cabendo ao titular ou à autoridade nacional comprovar eventual descumprimento das normas.",
 "Art. 6.º, X.","inverte o ônus","g03f")
# ---- G04
P("G04",["7"],"conceito_correto","excecao_omitida",3,
 "O tratamento de dados pessoais poderá ser realizado, entre outras hipóteses, para o cumprimento de obrigação legal ou regulatória pelo controlador, para a execução de contrato do qual seja parte o titular, a pedido deste, para o exercício regular de direitos em processo judicial, administrativo ou arbitral e para a proteção do crédito.",
 "O tratamento de dados pessoais somente poderá ser realizado mediante consentimento do titular, sendo vedado ao controlador invocar o cumprimento de obrigação legal, a execução de contrato ou a proteção do crédito para dispensá-lo.",
 "Art. 7.º, I, II, V, VI e X.","exige sempre consentimento","g04a")
P("G04",["7"],"conceito_correto","troca_efeito",3,
 "A administração pública pode tratar e compartilhar dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres, independentemente de consentimento, observadas as disposições do Capítulo IV da lei.",
 "A administração pública somente pode tratar e compartilhar dados necessários à execução de políticas públicas mediante consentimento do titular, sendo inaplicáveis as disposições do Capítulo IV da lei aos órgãos do Poder Executivo.",
 "Art. 7.º, III.","exige consentimento","g04b")
P("G04",["7"],"conceito_correto","excecao_omitida",3,
 "O tratamento de dados para a tutela da saúde somente pode ocorrer, sem consentimento, exclusivamente em procedimento realizado por profissionais de saúde, serviços de saúde ou autoridade sanitária.",
 "O tratamento de dados para a tutela da saúde pode ser realizado, sem consentimento, por qualquer controlador, inclusive operadoras de planos de saúde e empresas de tecnologia, para fins de pesquisa de mercado.",
 "Art. 7.º, VIII.","amplia os agentes","g04c")
P("G04",["7"],"conceito_correto","excecao_omitida",4,
 "Os dados tornados manifestamente públicos pelo titular dispensam o consentimento, resguardados os direitos do titular e os princípios da lei; e o tratamento de dados pessoais cujo acesso é público deve considerar a finalidade, a boa-fé e o interesse público que justificaram sua disponibilização.",
 "O tratamento de dados pessoais cujo acesso é público independe de qualquer análise de finalidade, boa-fé ou interesse público, e o consentimento é dispensado para qualquer novo tratamento posterior, ainda que com finalidade incompatível.",
 "Art. 7.º, §§ 3.º, 4.º e 7.º.","libera dados públicos","g04d")
P("G04",["7"],"conceito_correto","troca_efeito",3,
 "O controlador que obteve o consentimento e necessitar comunicar ou compartilhar dados pessoais com outros controladores deverá obter consentimento específico do titular para esse fim, ressalvadas as hipóteses de dispensa de consentimento; e a dispensa do consentimento não desobriga os agentes de tratamento das demais obrigações da lei.",
 "O controlador que obteve o consentimento poderá compartilhar os dados pessoais com outros controladores sem novo consentimento, e a dispensa do consentimento desobriga os agentes de tratamento da observância dos princípios gerais e dos direitos do titular.",
 "Art. 7.º, §§ 5.º e 6.º.","dispensa novo consentimento e demais obrigações","g04e")
P("G04",["10"],"conceito_correto","troca_efeito",4,
 "O legítimo interesse do controlador somente poderá fundamentar tratamento de dados pessoais para finalidades legítimas, consideradas a partir de situações concretas; quando o tratamento for baseado nele, somente os dados estritamente necessários para a finalidade pretendida poderão ser tratados.",
 "O legítimo interesse do controlador pode fundamentar tratamento de dados pessoais para qualquer finalidade, ainda que genérica, e autoriza o tratamento de todos os dados pessoais de que o controlador disponha, inclusive os sensíveis.",
 "Art. 10, caput e § 1.º.","amplia legítimo interesse","g04f")
P("G04",["10"],"conceito_correto","excecao_omitida",4,
 "O controlador deverá adotar medidas para garantir a transparência do tratamento baseado em seu legítimo interesse, e a autoridade nacional poderá solicitar-lhe relatório de impacto à proteção de dados pessoais, observados os segredos comercial e industrial.",
 "O tratamento baseado no legítimo interesse do controlador dispensa medidas de transparência, e a autoridade nacional somente poderá solicitar relatório de impacto quando houver incidente de segurança.",
 "Art. 10, §§ 2.º e 3.º.","dispensa transparência","g04g")
# ---- G05
P("G05",["8"],"conceito_correto","troca_efeito",2,
 "O consentimento deverá ser fornecido por escrito ou por outro meio que demonstre a manifestação de vontade do titular, e, se fornecido por escrito, deverá constar de cláusula destacada das demais cláusulas contratuais.",
 "O consentimento deverá ser fornecido exclusivamente por escrito, podendo constar de cláusula contratual genérica, desde que o titular tenha assinado o instrumento.",
 "Art. 8.º, caput e § 1.º.","exige escrita e dispensa destaque","g05a")
P("G05",["8"],"conceito_correto","troca_autoridade",3,
 "Cabe ao controlador o ônus da prova de que o consentimento foi obtido em conformidade com a lei, sendo vedado o tratamento de dados pessoais mediante vício de consentimento.",
 "Cabe ao titular o ônus da prova de que o consentimento não foi obtido em conformidade com a lei, sendo admitido o tratamento de dados mediante vício de consentimento, desde que o titular não revogue a autorização.",
 "Art. 8.º, §§ 2.º e 3.º.","inverte o ônus da prova","g05b")
P("G05",["8"],"conceito_correto","troca_efeito",3,
 "O consentimento deverá referir-se a finalidades determinadas, e as autorizações genéricas para o tratamento de dados pessoais serão nulas.",
 "O consentimento poderá referir-se a finalidades indeterminadas, e as autorizações genéricas para o tratamento de dados pessoais serão anuláveis a pedido do titular.",
 "Art. 8.º, § 4.º.","admite autorização genérica","g05c")
P("G05",["8"],"conceito_correto","excecao_omitida",4,
 "O consentimento pode ser revogado a qualquer momento mediante manifestação expressa do titular, por procedimento gratuito e facilitado, ratificados os tratamentos realizados sob amparo do consentimento anteriormente manifestado enquanto não houver requerimento de eliminação.",
 "O consentimento somente pode ser revogado mediante procedimento judicial, e a revogação invalida os tratamentos realizados sob amparo do consentimento anteriormente manifestado.",
 "Art. 8.º, § 5.º.","exige revogação judicial e efeito retroativo","g05d")
P("G05",["8","9"],"conceito_correto","troca_efeito",4,
 "Em caso de alteração da finalidade específica, da forma e duração do tratamento, da identificação do controlador ou do uso compartilhado de dados, o controlador deverá informar ao titular, com destaque, o teor das alterações, podendo o titular, nos casos em que o consentimento é exigido, revogá-lo caso discorde.",
 "Em caso de alteração da finalidade específica, da forma e duração do tratamento, da identificação do controlador ou do uso compartilhado de dados, o controlador poderá prosseguir com o tratamento, dispensada a informação ao titular se o consentimento original não previu prazo.",
 "Art. 8.º, § 6.º, e art. 9.º, I, II, III e V.","dispensa informação","g05e")
P("G05",["9"],"conceito_correto","excecao_omitida",3,
 "O titular tem direito ao acesso facilitado às informações sobre o tratamento de seus dados, disponibilizadas de forma clara, adequada e ostensiva, acerca, entre outras características, da finalidade específica, da forma e duração do tratamento, da identificação e contato do controlador, do uso compartilhado de dados, das responsabilidades dos agentes e dos direitos do titular.",
 "O titular tem direito ao acesso às informações sobre o tratamento de seus dados apenas mediante requerimento fundamentado, e o controlador está dispensado de informar a duração do tratamento, a identificação do controlador e os direitos do titular previstos na lei.",
 "Art. 9.º, caput e I a VII.","reduz informações","g05f")
P("G05",["9"],"conceito_correto","troca_efeito",3,
 "O consentimento será considerado nulo caso as informações fornecidas ao titular tenham conteúdo enganoso ou abusivo ou não tenham sido apresentadas previamente com transparência, de forma clara e inequívoca.",
 "O consentimento será considerado válido ainda que as informações fornecidas ao titular tenham conteúdo enganoso, desde que o titular tenha manifestado sua concordância por escrito.",
 "Art. 9.º, § 1.º.","valida consentimento viciado","g05g")
P("G05",["9"],"conceito_correto","excecao_omitida",3,
 "Quando o tratamento de dados pessoais for condição para o fornecimento de produto ou de serviço ou para o exercício de direito, o titular será informado com destaque sobre esse fato e sobre os meios pelos quais poderá exercer os direitos do art. 18.",
 "Quando o tratamento de dados pessoais for condição para o fornecimento de produto ou de serviço, o controlador está dispensado de informar o titular sobre esse fato, bastando constar nos termos de uso.",
 "Art. 9.º, § 3.º.","dispensa informação destacada","g05h")
# ---- G06
P("G06",["11"],"conceito_correto","excecao_omitida",3,
 "O tratamento de dados pessoais sensíveis somente poderá ocorrer quando o titular ou seu responsável legal consentir, de forma específica e destacada, para finalidades específicas, ou, sem consentimento, nas hipóteses em que for indispensável para as situações previstas no art. 11, II.",
 "O tratamento de dados pessoais sensíveis poderá ocorrer mediante consentimento do titular, de forma genérica, ou, sem consentimento, em qualquer das hipóteses do art. 7.º, inclusive para atender a interesses legítimos do controlador.",
 "Art. 11, I e II: o legítimo interesse não é base legal para dados sensíveis.","aplica as bases do art. 7º aos sensíveis","g06a")
P("G06",["11"],"conceito_correto","excecao_omitida",4,
 "Sem consentimento do titular, o tratamento de dados sensíveis pode ocorrer quando indispensável para o cumprimento de obrigação legal ou regulatória, para a execução de políticas públicas, estudos por órgão de pesquisa, exercício regular de direitos, proteção da vida, tutela da saúde e garantia da prevenção à fraude e à segurança do titular em processos de identificação e autenticação de cadastro.",
 "Sem consentimento do titular, o tratamento de dados sensíveis pode ocorrer para a execução de contrato do qual o titular seja parte, para a proteção do crédito e para o atendimento a interesses legítimos do controlador ou de terceiro.",
 "Art. 11, II, a a g: contrato, proteção do crédito e legítimo interesse não figuram.","inclui bases não previstas","g06b")
P("G06",["11"],"conceito_correto","troca_efeito",4,
 "É vedada a comunicação ou o uso compartilhado entre controladores de dados pessoais sensíveis referentes à saúde com objetivo de obter vantagem econômica, exceto nas hipóteses relativas a prestação de serviços de saúde, assistência farmacêutica e assistência à saúde, e é vedado às operadoras de planos privados de assistência à saúde o tratamento de dados de saúde para a prática de seleção de riscos.",
 "É permitida a comunicação ou o uso compartilhado entre controladores de dados sensíveis referentes à saúde com objetivo de obter vantagem econômica, e é facultado às operadoras de planos privados de assistência à saúde o tratamento de dados de saúde para seleção de riscos na contratação.",
 "Art. 11, §§ 4.º e 5.º.","permite vantagem econômica e seleção de riscos","g06c")
P("G06",["12"],"conceito_correto","excecao_omitida",4,
 "Os dados anonimizados não serão considerados dados pessoais, salvo quando o processo de anonimização for revertido, utilizando exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido; e poderão ser considerados dados pessoais aqueles utilizados para formação do perfil comportamental de determinada pessoa natural, se identificada.",
 "Os dados anonimizados nunca serão considerados dados pessoais, ainda que o processo de anonimização possa ser revertido com esforços razoáveis, e os dados utilizados para formação de perfil comportamental de pessoa identificada não se submetem à lei.",
 "Art. 12, caput e § 2.º.","afasta reversibilidade e perfil comportamental","g06d")
P("G06",["13"],"conceito_correto","excecao_omitida",4,
 "Na realização de estudos em saúde pública, os órgãos de pesquisa poderão ter acesso a bases de dados pessoais, tratados exclusivamente dentro do órgão, em ambiente controlado e seguro, com anonimização ou pseudonimização sempre que possível, sendo vedada a transferência dos dados a terceiro e a divulgação de resultados que revelem dados pessoais.",
 "Na realização de estudos em saúde pública, os órgãos de pesquisa poderão ter acesso a bases de dados pessoais e transferi-las a terceiros contratados, desde que haja anonimização, podendo os resultados divulgados identificar os titulares com autorização do órgão.",
 "Art. 13, caput e §§ 1.º e 2.º.","permite transferência e divulgação","g06e")
P("G06",["13"],"conceito_correto","confusao_instituto",3,
 "Pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro.",
 "Pseudonimização é o tratamento por meio do qual um dado perde de forma irreversível a possibilidade de associação a um indivíduo, sem manutenção de qualquer informação adicional que permita a reidentificação.",
 "Art. 13, § 4.º.","confunde com anonimização","g06f")
# ---- G07
P("G07",["14"],"conceito_correto","troca_efeito",3,
 "O tratamento de dados pessoais de crianças e de adolescentes deverá ser realizado em seu melhor interesse, e o de crianças deverá ser realizado com o consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal.",
 "O tratamento de dados pessoais de crianças deverá ser realizado com o consentimento específico e em destaque de ambos os pais, e o de adolescentes exige, em qualquer caso, o mesmo consentimento.",
 "Art. 14, caput e § 1.º: um dos pais ou o responsável legal.","exige ambos os pais e estende aos adolescentes","g07a")
P("G07",["14"],"conceito_correto","excecao_omitida",4,
 "Poderão ser coletados dados pessoais de crianças sem o consentimento dos pais quando a coleta for necessária para contatar os pais ou o responsável legal, utilizados uma única vez e sem armazenamento, ou para sua proteção, e em nenhum caso poderão ser repassados a terceiro sem o consentimento.",
 "Poderão ser coletados dados pessoais de crianças sem o consentimento dos pais sempre que o controlador entender que a coleta atende ao interesse da criança, podendo os dados ser armazenados e repassados a terceiros parceiros.",
 "Art. 14, § 3.º.","amplia exceção","g07b")
P("G07",["14"],"conceito_correto","excecao_omitida",3,
 "Os controladores não deverão condicionar a participação de crianças em jogos, aplicações de internet ou outras atividades ao fornecimento de informações pessoais além das estritamente necessárias à atividade, e devem realizar todos os esforços razoáveis para verificar que o consentimento foi dado pelo responsável pela criança.",
 "Os controladores poderão condicionar a participação de crianças em jogos e aplicações de internet ao fornecimento das informações pessoais que julgarem úteis, bastando declaração do próprio menor de que obteve a autorização do responsável.",
 "Art. 14, §§ 4.º e 5.º.","autoriza condicionamento","g07c")
P("G07",["15"],"conceito_correto","excecao_omitida",3,
 "O término do tratamento de dados pessoais ocorrerá quando verificado que a finalidade foi alcançada ou que os dados deixaram de ser necessários, no fim do período de tratamento, por comunicação do titular, inclusive revogação do consentimento, resguardado o interesse público, ou por determinação da autoridade nacional, quando houver violação à lei.",
 "O término do tratamento de dados pessoais ocorrerá apenas quando alcançada a finalidade ou no fim do período de tratamento, não produzindo efeito a comunicação do titular nem a determinação da autoridade nacional.",
 "Art. 15, I a IV.","restringe hipóteses de término","g07d")
P("G07",["16"],"conceito_correto","excecao_omitida",3,
 "Os dados pessoais serão eliminados após o término de seu tratamento, autorizada a conservação para cumprimento de obrigação legal ou regulatória pelo controlador, estudo por órgão de pesquisa, transferência a terceiro, respeitados os requisitos de tratamento, ou uso exclusivo do controlador, vedado acesso por terceiro e desde que anonimizados.",
 "Os dados pessoais serão mantidos pelo controlador após o término de seu tratamento pelo prazo de dez anos, podendo ser utilizados em seu exclusivo interesse comercial, ainda que não anonimizados, vedado o acesso por terceiro.",
 "Art. 16, I a IV.","autoriza conservação irrestrita","g07e")
# ---- G08
P("G08",["18"],"conceito_correto","excecao_omitida",3,
 "O titular dos dados pessoais tem direito a obter do controlador, a qualquer momento e mediante requisição, confirmação da existência de tratamento, acesso aos dados, correção de dados incompletos, inexatos ou desatualizados, e anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com a lei.",
 "O titular dos dados pessoais tem direito a obter do controlador, uma vez por ano e mediante requisição fundamentada, confirmação da existência de tratamento e acesso aos dados, sendo vedado exigir correção ou eliminação de dados tratados com base em legítimo interesse.",
 "Art. 18, caput e I a IV.","limita periodicidade e exige fundamentação","g08a")
P("G08",["18"],"conceito_correto","excecao_omitida",3,
 "O titular tem direito à portabilidade dos dados a outro fornecedor de serviço ou produto, mediante requisição expressa, de acordo com a regulamentação da autoridade nacional, observados os segredos comercial e industrial, não incluídos os dados já anonimizados pelo controlador.",
 "O titular tem direito à portabilidade dos dados a outro fornecedor de serviço ou produto, independentemente de regulamentação da autoridade nacional, abrangendo inclusive os dados já anonimizados pelo controlador e os segredos comercial e industrial.",
 "Art. 18, V e § 7.º.","inclui anonimizados e segredos","g08b")
P("G08",["18"],"conceito_correto","troca_efeito",3,
 "O titular tem direito à eliminação dos dados pessoais tratados com o seu consentimento, exceto nas hipóteses de conservação previstas no art. 16, e à informação das entidades públicas e privadas com as quais o controlador realizou uso compartilhado de dados.",
 "O titular tem direito à eliminação de todos os dados pessoais tratados pelo controlador, independentemente da base legal e das hipóteses de conservação do art. 16, mas não tem direito à informação sobre as entidades com as quais houve uso compartilhado.",
 "Art. 18, VI e VII.","amplia eliminação e retira direito","g08c")
P("G08",["18"],"conceito_correto","excecao_omitida",4,
 "O titular tem o direito de peticionar em relação aos seus dados contra o controlador perante a autoridade nacional, direito que também poderá ser exercido perante os organismos de defesa do consumidor; e pode opor-se a tratamento realizado com fundamento em hipótese de dispensa de consentimento, em caso de descumprimento da lei.",
 "O titular somente poderá peticionar contra o controlador perante o Poder Judiciário, sendo vedado o exercício do direito perante a autoridade nacional ou organismos de defesa do consumidor, e não pode se opor a tratamento fundado em dispensa de consentimento.",
 "Art. 18, §§ 1.º, 2.º e 8.º.","restringe a via","g08d")
P("G08",["18"],"conceito_correto","excecao_omitida",3,
 "Os direitos do art. 18 serão exercidos mediante requerimento expresso do titular ou de representante legalmente constituído a agente de tratamento, atendido sem custos para o titular, nos prazos e termos previstos em regulamento.",
 "Os direitos do art. 18 serão exercidos mediante requerimento verbal do titular, podendo o controlador cobrar o custo do atendimento, nos prazos que fixar em suas políticas internas.",
 "Art. 18, §§ 3.º e 5.º.","admite cobrança","g08e")
P("G08",["18"],"conceito_correto","excecao_omitida",4,
 "Em caso de impossibilidade de adoção imediata da providência requerida, o controlador enviará ao titular resposta em que poderá comunicar que não é agente de tratamento dos dados, indicando, sempre que possível, o agente, ou indicar as razões de fato ou de direito que impedem a adoção imediata; e deverá informar imediatamente aos agentes com os quais compartilhou dados a correção, eliminação, anonimização ou bloqueio, salvo impossibilidade comprovada ou esforço desproporcional.",
 "Em caso de impossibilidade de adoção imediata da providência requerida, o controlador poderá arquivar o requerimento sem resposta ao titular, e não precisará informar aos agentes com os quais compartilhou dados a correção, eliminação, anonimização ou bloqueio realizados.",
 "Art. 18, §§ 4.º e 6.º.","dispensa resposta e comunicação","g08f")
P("G08",["19"],"conceito_correto","troca_numero",3,
 "A confirmação de existência ou o acesso a dados pessoais serão providenciados, mediante requisição do titular, em formato simplificado, imediatamente, ou por meio de declaração clara e completa, que indique a origem dos dados, a inexistência de registro, os critérios utilizados e a finalidade do tratamento, fornecida no prazo de até quinze dias contado da data do requerimento.",
 "A confirmação de existência ou o acesso a dados pessoais serão providenciados, mediante requisição do titular, em formato simplificado, no prazo de até trinta dias, ou por meio de declaração clara e completa, que indique a origem dos dados e a finalidade do tratamento, fornecida no prazo de até sessenta dias.",
 "Art. 19, I e II: imediatamente; 15 dias.","altera prazos","g08g")
P("G08",["19"],"conceito_correto","excecao_omitida",3,
 "Quando o tratamento tiver origem no consentimento do titular ou em contrato, o titular poderá solicitar cópia eletrônica integral de seus dados pessoais, observados os segredos comercial e industrial, em formato que permita a sua utilização subsequente, inclusive em outras operações de tratamento.",
 "Mesmo quando o tratamento tiver origem em obrigação legal, o titular poderá solicitar cópia eletrônica integral de seus dados pessoais, em qualquer formato, inclusive os protegidos por segredo comercial e industrial.",
 "Art. 19, § 3.º.","amplia o direito","g08h")
P("G08",["20"],"conceito_correto","troca_efeito",3,
 "O titular dos dados tem direito a solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado de dados pessoais que afetem seus interesses, incluídas as decisões destinadas a definir o seu perfil pessoal, profissional, de consumo e de crédito ou os aspectos de sua personalidade.",
 "O titular dos dados tem direito a solicitar que a revisão de decisões baseadas em tratamento automatizado de dados pessoais seja realizada necessariamente por pessoa natural, vedadas as decisões destinadas a definir o seu perfil de consumo e de crédito.",
 "Art. 20, caput (a exigência de revisão por pessoa natural foi vetada).","atribui exigência vetada","g08i")
P("G08",["20"],"conceito_correto","excecao_omitida",4,
 "O controlador deverá fornecer, sempre que solicitadas, informações claras e adequadas a respeito dos critérios e dos procedimentos utilizados para a decisão automatizada, observados os segredos comercial e industrial; em caso de não oferecimento fundado nesses segredos, a autoridade nacional poderá realizar auditoria para verificação de aspectos discriminatórios.",
 "O controlador não está obrigado a fornecer informações sobre os critérios utilizados para a decisão automatizada, e a invocação de segredo comercial e industrial impede a realização de auditoria pela autoridade nacional.",
 "Art. 20, §§ 1.º e 2.º.","afasta dever e auditoria","g08j")
P("G08",["21","22"],"conceito_correto","troca_efeito",3,
 "Os dados pessoais referentes ao exercício regular de direitos pelo titular não podem ser utilizados em seu prejuízo, e a defesa dos interesses e direitos dos titulares poderá ser exercida em juízo, individual ou coletivamente, na forma da legislação pertinente.",
 "Os dados pessoais referentes ao exercício regular de direitos pelo titular podem ser utilizados em seu prejuízo quando houver legítimo interesse do controlador, e a defesa dos direitos dos titulares somente poderá ser exercida individualmente em juízo.",
 "Arts. 21 e 22.","admite uso prejudicial e veda tutela coletiva","g08k")
