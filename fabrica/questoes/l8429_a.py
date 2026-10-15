# Lei 8.429/92 (com Lei 14.230/21) — lote L3, parte a (Q01–Q06: dolo, sujeitos, arts. 9, 10, 11 e 12)
Q = []
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# ---- Q01
P("Q01",["1"],"conceito_correto","troca_efeito",2,
 "Segundo a Lei n.º 8.429/1992, com as alterações da Lei n.º 14.230/2021, consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9.º, 10 e 11, ressalvados os tipos previstos em leis especiais.",
 "Segundo a Lei n.º 8.429/1992, com as alterações da Lei n.º 14.230/2021, consideram-se atos de improbidade administrativa as condutas dolosas ou culposas tipificadas nos arts. 9.º, 10 e 11, ressalvados os tipos previstos em leis especiais, sendo a culpa admitida apenas na lesão ao erário.",
 "Art. 1.º, § 1.º: só condutas dolosas; a modalidade culposa do art. 10 foi suprimida.","admite culpa no art. 10","q01a")
P("Q01",["1"],"conceito_correto","restricao_indevida",2,
 "Considera-se dolo, para fins de improbidade administrativa, a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9.º, 10 e 11 da Lei n.º 8.429/1992, não bastando a mera voluntariedade do agente.",
 "Considera-se dolo, para fins de improbidade administrativa, a simples voluntariedade do agente na prática da conduta descrita nos arts. 9.º, 10 e 11 da Lei n.º 8.429/1992, dispensada a vontade livre e consciente de alcançar o resultado ilícito tipificado.",
 "Art. 1.º, § 2.º: dolo = vontade livre e consciente de alcançar o resultado ilícito; não basta a voluntariedade.","dispensa dolo específico","q01b")
P("Q01",["1"],"conceito_correto","regra_como_excecao",2,
 "O mero exercício da função ou o desempenho de competências públicas, sem comprovação de ato doloso com fim ilícito, afasta a responsabilidade por ato de improbidade administrativa.",
 "O mero exercício da função ou o desempenho de competências públicas, ainda que sem comprovação de ato doloso com fim ilícito, não afasta a responsabilidade por ato de improbidade quando a conduta do agente resulte em ilegalidade administrativa.",
 "Art. 1.º, § 3.º: sem dolo com fim ilícito não há improbidade; ilegalidade não qualificada pelo dolo é mera irregularidade (art. 17-C, § 1.º).","ilegalidade basta","q01c")
P("Q01",["1"],"conceito_correto","excecao_omitida",3,
 "Não configura improbidade administrativa a ação ou omissão decorrente de divergência interpretativa da lei, baseada em jurisprudência, ainda que não pacificada, mesmo que não venha a ser posteriormente prevalecente nas decisões dos órgãos de controle ou dos tribunais.",
 "Não configura improbidade administrativa a ação ou omissão decorrente de divergência interpretativa da lei, desde que baseada em jurisprudência pacificada que venha a ser posteriormente confirmada como prevalecente nas decisões dos órgãos de controle ou dos tribunais.",
 "Art. 1.º, § 8.º: basta jurisprudência, ainda que não pacificada, mesmo que não prevaleça depois.","exige pacificação","q01d")
P("Q01",["1"],"conceito_correto","generalizacao",2,
 "Aplicam-se ao sistema da improbidade administrativa disciplinado na Lei n.º 8.429/1992 os princípios constitucionais do direito administrativo sancionador.",
 "O sistema da improbidade administrativa disciplinado na Lei n.º 8.429/1992 tem natureza exclusivamente civil, razão pela qual não se lhe aplicam os princípios constitucionais do direito administrativo sancionador.",
 "Art. 1.º, § 4.º.","nega natureza sancionadora","q01e")
P("Q01",["1"],"conceito_correto","restricao_indevida",3,
 "Sujeitam-se às sanções da Lei de Improbidade os atos praticados contra o patrimônio de entidade privada que receba subvenção, benefício ou incentivo, fiscal ou creditício, de entes públicos; nas entidades para cuja criação ou custeio o erário concorra, o ressarcimento limita-se à repercussão do ilícito sobre a contribuição dos cofres públicos.",
 "Sujeitam-se às sanções da Lei de Improbidade somente os atos praticados contra o patrimônio da administração direta e indireta; os atos lesivos a entidades privadas que recebam subvenção ou incentivo público, ainda que para sua criação ou custeio o erário concorra, devem ser apurados exclusivamente pela legislação civil e penal comum.",
 "Art. 1.º, §§ 5.º a 7.º: entidades privadas subvencionadas ou custeadas pelo erário também são protegidas (ressarcimento limitado, no § 7.º).","exclui entidades privadas","q01f")
P("Q01",["1","17C"],"caso_concreto","caso_concreto",3,
 "Secretário municipal de saúde, amparado em parecer jurídico e em decisão de Tribunal de Justiça estadual que, embora não pacificada, admitia a contratação direta em situação análoga, dispensou licitação. O Tribunal de Contas, depois, entendeu irregular a dispensa. Nessa situação, a divergência interpretativa baseada em jurisprudência afasta a configuração de improbidade, ainda que a tese do gestor não tenha prevalecido.",
 "Secretário municipal de saúde, amparado em parecer jurídico e em decisão de Tribunal de Justiça estadual que, embora não pacificada, admitia a contratação direta em situação análoga, dispensou licitação. O Tribunal de Contas, depois, entendeu irregular a dispensa. Nessa situação, como a tese do gestor não prevaleceu nos órgãos de controle, está configurada a improbidade administrativa, pois a divergência interpretativa só protege o agente quando a tese vier a ser confirmada.",
 "Art. 1.º, § 8.º: divergência interpretativa baseada em jurisprudência, ainda que não pacificada ou não prevalecente depois, afasta a improbidade.","exige que a tese prevaleça","q01g")
# ---- Q02
P("Q02",["2"],"conceito_correto","restricao_indevida",2,
 "Para os efeitos da Lei de Improbidade, é agente público aquele que exerce, ainda que transitoriamente ou sem remuneração, por eleição, nomeação, designação, contratação ou qualquer outra forma de investidura ou vínculo, mandato, cargo, emprego ou função nas entidades protegidas pela lei.",
 "Para os efeitos da Lei de Improbidade, só é agente público aquele que exerce cargo, emprego ou função de forma permanente e remunerada, por nomeação ou eleição, nas entidades protegidas pela lei, excluídos os que atuam transitoriamente ou sem remuneração.",
 "Art. 2.º: conceito amplo; vale transitoriedade e ausência de remuneração.","restringe conceito","q02a")
P("Q02",["2"],"conceito_correto","restricao_indevida",3,
 "Sujeita-se às sanções da Lei de Improbidade, quanto a recursos de origem pública, o particular, pessoa física ou jurídica, que celebra com a administração pública convênio, contrato de repasse, contrato de gestão, termo de parceria, termo de cooperação ou ajuste equivalente.",
 "Sujeita-se às sanções da Lei de Improbidade, quanto a recursos de origem pública, apenas o particular pessoa física que celebra com a administração pública convênio ou termo de parceria, não alcançando a pessoa jurídica de direito privado nem os demais ajustes administrativos equivalentes.",
 "Art. 2.º, parágrafo único.","exclui pessoa jurídica","q02b")
P("Q02",["3"],"conceito_correto","troca_efeito",2,
 "As disposições da Lei de Improbidade aplicam-se, no que couber, àquele que, mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade.",
 "As disposições da Lei de Improbidade aplicam-se, no que couber, àquele que, mesmo não sendo agente público, induza ou concorra, ainda que culposamente, para a prática do ato de improbidade, desde que dele se beneficie.",
 "Art. 3.º: terceiro responde só se induzir ou concorrer dolosamente.","admite culpa","q02c")
P("Q02",["3"],"conceito_correto","excecao_omitida",3,
 "Os sócios, cotistas, diretores e colaboradores de pessoa jurídica de direito privado não respondem pelo ato de improbidade imputado à pessoa jurídica, salvo se, comprovadamente, houver participação e benefícios diretos, caso em que responderão nos limites de sua participação.",
 "Os sócios, cotistas, diretores e colaboradores de pessoa jurídica de direito privado respondem solidariamente pelo ato de improbidade imputado à pessoa jurídica, independentemente de comprovação de sua participação ou de benefício direto, limitada a responsabilidade ao valor do capital social.",
 "Art. 3.º, § 1.º.","responsabilização objetiva dos sócios","q02d")
P("Q02",["3","12"],"consequencia","troca_efeito",3,
 "As sanções da Lei de Improbidade não se aplicarão à pessoa jurídica se o ato de improbidade for também sancionado como ato lesivo à administração pública, nos termos da Lei Anticorrupção (Lei n.º 12.846/2013).",
 "As sanções da Lei de Improbidade aplicam-se cumulativamente às da Lei Anticorrupção (Lei n.º 12.846/2013) à pessoa jurídica que praticar o mesmo ato, sem prejuízo do princípio do non bis in idem, que se limita às sanções pecuniárias.",
 "Art. 3.º, § 2.º, e art. 12, § 7.º: se também sancionado pela Lei 12.846, não se aplicam à PJ as sanções da LIA.","admite cumulação","q02e")
P("Q02",["8"],"conceito_correto","troca_efeito",3,
 "O sucessor ou o herdeiro daquele que causar dano ao erário ou que se enriquecer ilicitamente está sujeito apenas à obrigação de repará-lo até o limite do valor da herança ou do patrimônio transferido.",
 "O sucessor ou o herdeiro daquele que causar dano ao erário ou que se enriquecer ilicitamente está sujeito a todas as sanções da Lei de Improbidade, inclusive multa civil, até o limite do valor da herança ou do patrimônio transferido.",
 "Art. 8.º: sucessor responde apenas pela reparação do dano, limitada à herança.","amplia sanções ao sucessor","q02f")
P("Q02",["8A"],"conceito_correto","excecao_omitida",3,
 "Na fusão e na incorporação societárias, a responsabilidade da sucessora restringe-se à reparação integral do dano até o limite do patrimônio transferido, não lhe sendo aplicáveis as demais sanções da lei por atos anteriores à operação, exceto em caso de simulação ou de evidente intuito de fraude.",
 "Na fusão e na incorporação societárias, a sucessora responde por todas as sanções da Lei de Improbidade decorrentes de atos anteriores à operação, inclusive a multa civil, ainda que não haja simulação nem evidente intuito de fraude.",
 "Art. 8.º-A, parágrafo único.","ignora a restrição","q02g")
P("Q02",["3","8A"],"caso_concreto","caso_concreto",4,
 "A sociedade empresária Alfa, após a prática de ato de improbidade por seus administradores, foi incorporada pela Beta, sem simulação ou fraude. Nessa hipótese, Beta responderá pela reparação integral do dano, até o limite do patrimônio transferido, mas não será alcançada pelas demais sanções da lei relativas a fatos anteriores à incorporação.",
 "A sociedade empresária Alfa, após a prática de ato de improbidade por seus administradores, foi incorporada pela Beta, sem simulação ou fraude. Nessa hipótese, Beta responderá pelo dano e também pela multa civil e pela proibição de contratar com o poder público, por serem sanções que acompanham o patrimônio da sociedade sucedida.",
 "Art. 8.º-A, parágrafo único.","estende sanções à sucessora","q02h")
# ---- Q03
P("Q03",["9"],"conceito_correto","troca_efeito",2,
 "Constitui improbidade por enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida em razão do exercício de cargo, mandato, função, emprego ou atividade nas entidades protegidas pela Lei n.º 8.429/1992.",
 "Constitui improbidade por enriquecimento ilícito auferir, por ação dolosa ou culposa, qualquer vantagem patrimonial indevida em razão do exercício de cargo, mandato, função, emprego ou atividade nas entidades protegidas pela Lei n.º 8.429/1992.",
 "Art. 9.º, caput: ato doloso.","admite culpa","q03a")
P("Q03",["9"],"conceito_correto","regra_como_excecao",3,
 "O rol de condutas dos incisos do art. 9.º da Lei n.º 8.429/1992 é exemplificativo, pois o caput prevê que o enriquecimento ilícito se configura “e notadamente” pelas hipóteses enumeradas.",
 "O rol de condutas dos incisos do art. 9.º da Lei n.º 8.429/1992 é taxativo, pois, após a Lei n.º 14.230/2021, somente as hipóteses enumeradas configuram enriquecimento ilícito.",
 "A taxatividade, após a Lei 14.230/21, vale para o art. 11; os arts. 9.º e 10 mantêm o “notadamente” (rol exemplificativo).","confunde art. 9 com art. 11","q03b")
P("Q03",["9.I"],"conceito_correto","excecao_omitida",3,
 "Receber, para si ou para outrem, dinheiro ou qualquer outra vantagem econômica a título de comissão, percentagem, gratificação ou presente de quem tenha interesse, direto ou indireto, que possa ser atingido ou amparado por ação ou omissão decorrente das atribuições do agente público configura enriquecimento ilícito.",
 "Receber, para si ou para outrem, dinheiro ou qualquer outra vantagem econômica a título de presente configura enriquecimento ilícito, ainda que o doador não tenha interesse que possa ser atingido ou amparado por ação ou omissão decorrente das atribuições do agente público.",
 "Art. 9.º, I: exige interesse do doador atingível pelas atribuições do agente.","suprime elemento do tipo","q03c")
P("Q03",["9.VII"],"conceito_correto","excecao_omitida",4,
 "Adquirir, no exercício de cargo ou função pública e em razão deles, bens cujo valor seja desproporcional à evolução do patrimônio ou à renda do agente, em decorrência dos atos descritos no caput, configura enriquecimento ilícito, assegurada ao agente a demonstração da licitude da origem dessa evolução.",
 "Adquirir bens cujo valor seja desproporcional à evolução do patrimônio ou à renda do agente público configura enriquecimento ilícito por presunção absoluta, dispensada a demonstração de que a aquisição decorre dos atos descritos no caput e vedada ao agente a prova da licitude da origem dos bens.",
 "Art. 9.º, VII: aquisição em razão do cargo e decorrente dos atos do caput; assegurada a demonstração de licitude.","presunção absoluta","q03d")
P("Q03",["9.VIII"],"conceito_correto","troca_numero",3,
 "Aceitar emprego, comissão ou exercer atividade de consultoria ou assessoramento para pessoa física ou jurídica que tenha interesse suscetível de ser atingido por ação ou omissão decorrente das atribuições do agente público, durante a atividade, configura enriquecimento ilícito.",
 "Aceitar emprego, comissão ou exercer atividade de consultoria ou assessoramento para pessoa que tenha interesse suscetível de ser atingido por ação ou omissão decorrente das atribuições do agente público configura enriquecimento ilícito apenas se ocorrer após a cessação da atividade pública, em quarentena de seis meses.",
 "Art. 9.º, VIII: durante a atividade; não há quarentena na tipificação.","inverte o momento","q03e")
P("Q03",["9.XI","9.XII"],"conceito_correto","confusao_instituto",3,
 "Incorporar ao patrimônio, por qualquer forma, bens, rendas, verbas ou valores integrantes do acervo patrimonial das entidades do art. 1.º, ou usá-los em proveito próprio, configura enriquecimento ilícito do agente.",
 "Incorporar ao patrimônio do agente bens, rendas, verbas ou valores integrantes do acervo das entidades do art. 1.º configura improbidade por lesão ao erário, e usá-los em proveito próprio configura violação a princípios da administração pública.",
 "Art. 9.º, XI e XII: ambos são enriquecimento ilícito.","reclassifica o tipo","q03f")
P("Q03",["9.IV"],"caso_concreto","caso_concreto",3,
 "Prefeito, dolosamente, determinou que servidores municipais, em horário de expediente, reformassem sua casa de campo com materiais do almoxarifado da prefeitura. A conduta pode configurar improbidade por enriquecimento ilícito, por utilização de bens e trabalho de servidores em obra particular.",
 "Prefeito, dolosamente, determinou que servidores municipais, em horário de expediente, reformassem sua casa de campo com materiais do almoxarifado da prefeitura. Como o prefeito não recebeu dinheiro de terceiros, a conduta não pode configurar enriquecimento ilícito, restando apenas a responsabilização por violação a princípios.",
 "Art. 9.º, IV: utilizar em obra particular bem público ou trabalho de servidores.","exige recebimento em dinheiro","q03g")
# ---- Q04
P("Q04",["10"],"conceito_correto","troca_efeito",2,
 "Constitui improbidade que causa lesão ao erário qualquer ação ou omissão dolosa que enseje, efetiva e comprovadamente, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres das entidades referidas no art. 1.º.",
 "Constitui improbidade que causa lesão ao erário qualquer ação ou omissão, dolosa ou culposa, que enseje perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres das entidades referidas no art. 1.º.",
 "Art. 10, caput: só dolo; perda efetiva e comprovada.","reintroduz culpa","q04a")
P("Q04",["10"],"conceito_correto","restricao_indevida",3,
 "Nos casos em que a inobservância de formalidades legais ou regulamentares não implicar perda patrimonial efetiva, não ocorrerá imposição de ressarcimento, vedado o enriquecimento sem causa das entidades públicas.",
 "Nos casos em que a inobservância de formalidades legais ou regulamentares não implicar perda patrimonial efetiva, o dano ao erário é presumido, impondo-se o ressarcimento em valor equivalente ao do ato praticado em desacordo com as formalidades.",
 "Art. 10, § 1.º.","presume dano","q04b")
P("Q04",["10"],"conceito_correto","excecao_omitida",3,
 "A mera perda patrimonial decorrente da atividade econômica não acarretará improbidade administrativa, salvo se comprovado ato doloso praticado com essa finalidade.",
 "A perda patrimonial decorrente da atividade econômica exercida pelo ente público acarreta improbidade administrativa culposa sempre que o gestor não adotar as cautelas usuais do mercado.",
 "Art. 10, § 2.º.","admite culpa","q04c")
P("Q04",["10"],"conceito_correto","regra_como_excecao",3,
 "O rol de condutas do art. 10 da Lei n.º 8.429/1992 é exemplificativo, em razão da expressão “e notadamente” constante do caput.",
 "O rol de condutas do art. 10 da Lei n.º 8.429/1992 é taxativo, de modo que a lesão ao erário somente se configura nas hipóteses descritas nos seus incisos.",
 "Art. 10, caput: “e notadamente”; só o art. 11 tem rol taxativo.","confunde com art. 11","q04d")
P("Q04",["10.VIII"],"conceito_correto","excecao_omitida",3,
 "Frustrar a licitude de processo licitatório ou de processo seletivo para celebração de parcerias com entidades sem fins lucrativos, ou dispensá-los indevidamente, configura lesão ao erário quando acarretar perda patrimonial efetiva.",
 "Frustrar a licitude de processo licitatório, ou dispensá-lo indevidamente, configura lesão ao erário ainda que não acarrete perda patrimonial efetiva, pois o dano decorre da própria ofensa ao princípio da competitividade.",
 "Art. 10, VIII: exige perda patrimonial efetiva.","dispensa dano","q04e")
P("Q04",["10.X"],"literalidade_util","troca_efeito",3,
 "Agir ilicitamente na arrecadação de tributo ou de renda, bem como no que diz respeito à conservação do patrimônio público, configura improbidade por lesão ao erário.",
 "Agir negligentemente na arrecadação de tributo ou de renda, bem como no que diz respeito à conservação do patrimônio público, configura improbidade por lesão ao erário.",
 "Art. 10, X (redação da Lei 14.230/21): agir ilicitamente; a negligência deixou de ser tipificada.","mantém a negligência","q04f")
P("Q04",["10.IV","10.V"],"conceito_correto","troca_numero",3,
 "Permitir ou facilitar a alienação de bem público por preço inferior ao de mercado, ou a aquisição de bem ou serviço por preço superior ao de mercado, configura lesão ao erário.",
 "Permitir ou facilitar a alienação de bem público por preço inferior ao de mercado, ou a aquisição de bem ou serviço por preço superior ao de mercado, configura enriquecimento ilícito do agente, independentemente de ele auferir vantagem.",
 "Art. 10, IV e V. O art. 9.º, II e III, exige que o agente perceba vantagem econômica.","confunde com art. 9","q04g")
P("Q04",["10"],"caso_concreto","caso_concreto",4,
 "Gestor de autarquia, dolosamente, homologou compra de equipamentos por preço 40% superior ao de mercado, comprovado em perícia, em favor de empresa de amigo, sem receber qualquer vantagem. A conduta se amolda ao art. 10, pois houve perda patrimonial efetiva, e não ao art. 9.º, porque o gestor não auferiu vantagem.",
 "Gestor de autarquia, dolosamente, homologou compra de equipamentos por preço 40% superior ao de mercado, comprovado em perícia, em favor de empresa de amigo, sem receber qualquer vantagem. A conduta se amolda ao art. 9.º, pois o beneficiamento de amigo caracteriza vantagem indevida em razão do cargo, e não ao art. 10, que exige proveito do agente.",
 "Art. 10, V, e art. 9.º, II: sem vantagem ao agente, o tipo é lesão ao erário; cada ato se enquadra em um único tipo (art. 17, § 10-D).","inverte o tipo","q04h")
# ---- Q05
P("Q05",["11"],"conceito_correto","troca_autoridade",3,
 "Constitui improbidade que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade, caracterizada por uma das condutas previstas nos incisos do art. 11.",
 "Constitui improbidade que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade, de legalidade e de lealdade às instituições, caracterizada por uma das condutas previstas nos incisos do art. 11.",
 "Art. 11, caput (Lei 14.230/21): honestidade, imparcialidade e legalidade; a “lealdade às instituições” constava da redação anterior.","mantém redação revogada","q05a")
P("Q05",["11"],"conceito_correto","regra_como_excecao",3,
 "O rol de condutas do art. 11 da Lei n.º 8.429/1992 é taxativo, pois o caput exige que a violação aos princípios seja caracterizada por uma das condutas nele previstas.",
 "O rol de condutas do art. 11 da Lei n.º 8.429/1992 é exemplificativo, pois a violação aos deveres de honestidade, imparcialidade e legalidade pode ser caracterizada por outras condutas além das previstas nos incisos.",
 "Art. 11, caput: “caracterizada por uma das seguintes condutas”.","exemplificativo","q05b")
P("Q05",["11"],"conceito_correto","excecao_omitida",3,
 "Somente haverá improbidade por violação a princípios quando for comprovado, na conduta funcional do agente público, o fim de obter proveito ou benefício indevido para si ou para outra pessoa ou entidade.",
 "Haverá improbidade por violação a princípios sempre que o agente público praticar uma das condutas do art. 11, sendo prescindível demonstrar o fim de obter proveito ou benefício indevido, bastando o dolo genérico.",
 "Art. 11, § 1.º (e § 2.º: vale para todos os atos de improbidade).","dispensa proveito indevido","q05c")
P("Q05",["11"],"conceito_correto","excecao_omitida",3,
 "O enquadramento da conduta funcional na categoria de violação a princípios pressupõe a demonstração objetiva da prática de ilegalidade no exercício da função pública, com a indicação das normas constitucionais, legais ou infralegais violadas.",
 "O enquadramento da conduta funcional na categoria de violação a princípios pode fundar-se na afronta a princípios abstratos da administração, dispensada a indicação das normas constitucionais, legais ou infralegais violadas.",
 "Art. 11, § 3.º.","dispensa indicação de normas","q05d")
P("Q05",["11"],"conceito_correto","troca_efeito",3,
 "Os atos de improbidade por violação a princípios exigem lesividade relevante ao bem jurídico tutelado para serem passíveis de sancionamento e independem do reconhecimento de dano ao erário e de enriquecimento ilícito.",
 "Os atos de improbidade por violação a princípios exigem, para serem passíveis de sancionamento, o reconhecimento de dano ao erário ou de enriquecimento ilícito, dispensada a demonstração de lesividade relevante ao bem jurídico tutelado.",
 "Art. 11, § 4.º.","inverte exigência","q05e")
P("Q05",["11"],"conceito_correto","excecao_omitida",3,
 "Não se configura improbidade a mera nomeação ou indicação política por parte dos detentores de mandatos eletivos, sendo necessária a aferição de dolo com finalidade ilícita por parte do agente.",
 "Configura improbidade por violação a princípios a nomeação ou indicação política, por detentores de mandatos eletivos, de pessoas sem qualificação técnica, independentemente da aferição de dolo com finalidade ilícita.",
 "Art. 11, § 5.º.","dispensa dolo","q05f")
P("Q05",["11.XI"],"conceito_correto","troca_numero",3,
 "Nomear cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, da autoridade nomeante ou de servidor da mesma pessoa jurídica investido em cargo de direção, chefia ou assessoramento, para cargo em comissão ou de confiança ou função gratificada, configura, nos termos da lei, improbidade por violação a princípios.",
 "Nomear cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o quarto grau, da autoridade nomeante ou de servidor da mesma pessoa jurídica investido em cargo de direção, chefia ou assessoramento, para cargo em comissão ou de confiança ou função gratificada, configura, nos termos da lei, improbidade por violação a princípios.",
 "Art. 11, XI: até o terceiro grau, inclusive.","altera o grau de parentesco","q05g")
P("Q05",["11.I","11.II"],"conceito_correto","regra_como_excecao",4,
 "Foram revogadas, pela Lei n.º 14.230/2021, as hipóteses de improbidade por violação a princípios consistentes em praticar ato visando a fim proibido em lei ou diverso do previsto na regra de competência e em retardar ou deixar de praticar, indevidamente, ato de ofício.",
 "Permanecem tipificadas, após a Lei n.º 14.230/2021, como improbidade por violação a princípios, as condutas de praticar ato visando a fim proibido em lei ou diverso do previsto na regra de competência e de retardar ou deixar de praticar, indevidamente, ato de ofício.",
 "Art. 11, I e II: revogados.","mantém tipos revogados","q05h")
P("Q05",["11.VI"],"conceito_correto","excecao_omitida",3,
 "Deixar de prestar contas quando esteja obrigado a fazê-lo configura improbidade por violação a princípios desde que o agente disponha das condições para isso e haja o fim de ocultar irregularidades.",
 "Deixar de prestar contas quando esteja obrigado a fazê-lo configura, por si só, improbidade por violação a princípios, ainda que o agente não disponha das condições para prestá-las e não vise a ocultar irregularidades.",
 "Art. 11, VI.","suprime requisitos","q05i")
P("Q05",["11.XI","11"],"caso_concreto","caso_concreto",4,
 "Governador nomeou o próprio irmão para a chefia de gabinete de uma secretaria, cargo em comissão, sem qualquer demonstração de que a nomeação visasse a proveito indevido ou de que o nomeado fosse desqualificado. Nesse caso, a nomeação de parente até o terceiro grau pode configurar o art. 11, XI, mas a lei exige demonstração de dolo com finalidade ilícita e lesividade relevante para a condenação.",
 "Governador nomeou o próprio irmão para a chefia de gabinete de uma secretaria, cargo em comissão, sem qualquer demonstração de que a nomeação visasse a proveito indevido ou de que o nomeado fosse desqualificado. Nesse caso, a só nomeação de parente até o terceiro grau, por si, basta para a condenação por improbidade, sendo desnecessária a demonstração de dolo com finalidade ilícita.",
 "Art. 11, XI, §§ 1.º, 4.º e 5.º.","dispensa dolo e lesividade","q05j")
# ---- Q06
P("Q06",["12"],"conceito_correto","troca_numero",2,
 "No caso de enriquecimento ilícito, o responsável poderá sofrer perda dos bens acrescidos ilicitamente, perda da função pública, suspensão dos direitos políticos até quatorze anos, multa civil equivalente ao valor do acréscimo patrimonial e proibição de contratar com o poder público pelo prazo não superior a quatorze anos.",
 "No caso de enriquecimento ilícito, o responsável poderá sofrer perda dos bens acrescidos ilicitamente, perda da função pública, suspensão dos direitos políticos até doze anos, multa civil equivalente ao valor do acréscimo patrimonial e proibição de contratar com o poder público pelo prazo não superior a doze anos.",
 "Art. 12, I: 14 anos (suspensão e proibição de contratar).","troca 14 por 12","q06a")
P("Q06",["12"],"conceito_correto","troca_numero",2,
 "No caso de lesão ao erário, as sanções incluem suspensão dos direitos políticos até doze anos, multa civil equivalente ao valor do dano e proibição de contratar com o poder público pelo prazo não superior a doze anos.",
 "No caso de lesão ao erário, as sanções incluem suspensão dos direitos políticos até quatorze anos, multa civil equivalente ao dobro do valor do dano e proibição de contratar com o poder público pelo prazo não superior a doze anos.",
 "Art. 12, II: 12 anos; multa igual ao valor do dano (o dobro só pelo § 2.º, se ineficaz).","troca 12 por 14","q06b")
P("Q06",["12"],"conceito_correto","troca_efeito",3,
 "No caso de violação a princípios da administração pública, as sanções são o pagamento de multa civil de até vinte e quatro vezes o valor da remuneração percebida pelo agente e a proibição de contratar com o poder público por prazo não superior a quatro anos.",
 "No caso de violação a princípios da administração pública, as sanções incluem, além da multa civil de até vinte e quatro vezes o valor da remuneração e da proibição de contratar por até quatro anos, a suspensão dos direitos políticos por até quatro anos.",
 "Art. 12, III: não há suspensão de direitos políticos nem perda da função pública no art. 11.","acrescenta suspensão de direitos políticos","q06c")
P("Q06",["12"],"conceito_correto","excecao_omitida",3,
 "A sanção de perda da função pública, nos casos de enriquecimento ilícito e lesão ao erário, atinge apenas o vínculo de mesma qualidade e natureza que o agente detinha com o poder público na época do cometimento da infração, podendo o magistrado, no caso de enriquecimento ilícito e em caráter excepcional, estendê-la aos demais vínculos.",
 "A sanção de perda da função pública atinge todos os vínculos que o agente mantenha com o poder público na data da condenação, qualquer que seja a espécie de improbidade, sem necessidade de justificação excepcional do magistrado.",
 "Art. 12, § 1.º.","amplia perda a todos os vínculos","q06d")
P("Q06",["12"],"conceito_correto","troca_efeito",3,
 "A multa civil pode ser aumentada até o dobro se o juiz considerar que, em virtude da situação econômica do réu, o valor calculado na forma dos incisos do art. 12 é ineficaz para reprovação e prevenção do ato de improbidade.",
 "A multa civil pode ser aumentada até o triplo se o juiz considerar que, em virtude da situação econômica do réu, o valor calculado na forma dos incisos do art. 12 é ineficaz para reprovação e prevenção do ato de improbidade.",
 "Art. 12, § 2.º: até o dobro.","troca dobro por triplo","q06e")
P("Q06",["12"],"conceito_correto","troca_efeito",3,
 "No caso de atos de menor ofensa aos bens jurídicos tutelados pela lei, a sanção limitar-se-á à aplicação de multa, sem prejuízo do ressarcimento do dano e da perda dos valores obtidos, quando for o caso.",
 "No caso de atos de menor ofensa aos bens jurídicos tutelados pela lei, a sanção limitar-se-á à advertência e à multa, ficando afastados o ressarcimento do dano e a perda dos valores obtidos.",
 "Art. 12, § 5.º.","afasta ressarcimento","q06f")
P("Q06",["12"],"conceito_correto","troca_efeito",3,
 "As sanções previstas no art. 12 somente poderão ser executadas após o trânsito em julgado da sentença condenatória, e, para a contagem do prazo da suspensão dos direitos políticos, computa-se retroativamente o intervalo entre a decisão colegiada e o trânsito em julgado.",
 "As sanções previstas no art. 12 poderão ser executadas após a confirmação da sentença condenatória por decisão colegiada, e, para a contagem do prazo da suspensão dos direitos políticos, não se computa o tempo decorrido até o trânsito em julgado.",
 "Art. 12, §§ 9.º e 10.","execução após decisão colegiada","q06g")
P("Q06",["12"],"conceito_correto","excecao_omitida",3,
 "Em caráter excepcional e por motivos relevantes devidamente justificados, a proibição de contratação com o poder público pode extrapolar o ente público lesado pelo ato de improbidade, observados os impactos econômicos e sociais, de forma a preservar a função social da pessoa jurídica.",
 "A proibição de contratação com o poder público, imposta a pessoa jurídica por ato de improbidade, abrange sempre todos os entes da Federação, não sendo admitida limitação territorial, ainda que em decisão judicial fundamentada.",
 "Art. 12, §§ 3.º, 4.º e 8.º: regra é o ente lesado; extrapolação é excepcional; limitações territoriais constam do CEIS.","generaliza abrangência","q06h")
P("Q06",["12"],"caso_concreto","caso_concreto",4,
 "Servidor público federal, condenado por enriquecimento ilícito com trânsito em julgado, ocupava, na data dos fatos, um cargo efetivo e, depois, passou a exercer cargo em comissão. Nessa hipótese, a perda da função alcança o vínculo que o agente detinha à época dos fatos, podendo ser estendida aos demais vínculos apenas em caráter excepcional.",
 "Servidor público federal, condenado por enriquecimento ilícito com trânsito em julgado, ocupava, na data dos fatos, um cargo efetivo e, depois, passou a exercer cargo em comissão. Nessa hipótese, a perda da função alcança necessariamente ambos os vínculos, por ser vedado ao juiz graduar o alcance da sanção.",
 "Art. 12, § 1.º.","retira discricionariedade do juiz","q06i")
