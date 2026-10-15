# Lei 12.527/11 (LAI) — lote L4, parte a (R01–R06)
Q = []
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# ---- R01
P("R01",["1"],"conceito_correto","troca_autoridade",2,
 "Subordinam-se ao regime da Lei de Acesso à Informação os órgãos públicos integrantes da administração direta dos Poderes Executivo, Legislativo, incluindo as Cortes de Contas, e Judiciário e do Ministério Público, bem como as autarquias, fundações públicas, empresas públicas, sociedades de economia mista e demais entidades controladas direta ou indiretamente pelos entes federativos.",
 "Subordinam-se ao regime da Lei de Acesso à Informação os órgãos da administração direta e indireta do Poder Executivo, estando excluídos os Poderes Legislativo e Judiciário, as Cortes de Contas e o Ministério Público, que se regem por normas internas próprias, nos termos da Lei de Acesso à Informação.",
 "Art. 1.º, parágrafo único.","exclui poderes e órgãos","r01a")
P("R01",["1"],"conceito_correto","restricao_indevida",2,
 "A Lei de Acesso à Informação dispõe sobre os procedimentos a serem observados pela União, Estados, Distrito Federal e Municípios, a fim de garantir o acesso a informações previsto no art. 5.º, XXXIII, no art. 37, § 3.º, II, e no art. 216, § 2.º, da Constituição Federal.",
 "A Lei de Acesso à Informação dispõe sobre os procedimentos a serem observados exclusivamente pela União, a fim de garantir o acesso a informações previsto no art. 5.º, XXXIII, da Constituição Federal, cabendo a Estados e Municípios legislar livremente sobre a matéria.",
 "Art. 1.º, caput; art. 45: normas gerais nacionais; entes definem regras específicas.","restringe âmbito federativo","r01b")
P("R01",["2"],"conceito_correto","excecao_omitida",3,
 "Aplicam-se as disposições da Lei de Acesso à Informação, no que couber, às entidades privadas sem fins lucrativos que recebam recursos públicos para realização de ações de interesse público; a publicidade a que se submetem refere-se à parcela dos recursos públicos recebidos e à sua destinação.",
 "Aplicam-se as disposições da Lei de Acesso à Informação, no que couber, às entidades privadas sem fins lucrativos que recebam recursos públicos para ações de interesse público, devendo ser divulgada a integralidade de sua contabilidade, inclusive a parcela de recursos privados.",
 "Art. 2.º e parágrafo único.","amplia a publicidade","r01c")
P("R01",["3"],"conceito_correto","regra_como_excecao",2,
 "Entre as diretrizes da Lei de Acesso à Informação estão a observância da publicidade como preceito geral e do sigilo como exceção e a divulgação de informações de interesse público, independentemente de solicitações.",
 "Entre as diretrizes da Lei de Acesso à Informação estão a observância do sigilo como preceito geral e da publicidade como exceção, devendo a divulgação de informações de interesse público depender de solicitação do interessado.",
 "Art. 3.º, I e II.","inverte regra e exceção","r01d")
P("R01",["3"],"conceito_correto","excecao_omitida",3,
 "São diretrizes da lei a utilização de meios de comunicação viabilizados pela tecnologia da informação, o fomento ao desenvolvimento da cultura de transparência na administração pública e o desenvolvimento do controle social da administração pública.",
 "São diretrizes da lei a utilização exclusiva de meios de comunicação físicos, para preservar a autenticidade das informações, o fomento à cultura de transparência e o desenvolvimento do controle interno da administração pública.",
 "Art. 3.º, III a V.","troca diretrizes","r01e")
P("R01",["5","6"],"conceito_correto","troca_efeito",2,
 "É dever do Estado garantir o direito de acesso à informação, que será franqueada mediante procedimentos objetivos e ágeis, de forma transparente, clara e em linguagem de fácil compreensão.",
 "É dever do Estado garantir o direito de acesso à informação, que será franqueada, a critério da autoridade competente, mediante procedimentos formais, de forma técnica e em linguagem especializada, a fim de preservar a segurança jurídica.",
 "Art. 5.º.","troca qualificadores","r01f")
P("R01",["6"],"conceito_correto","excecao_omitida",3,
 "Cabe aos órgãos e entidades do poder público assegurar a gestão transparente da informação, a proteção da informação, garantindo-se sua disponibilidade, autenticidade e integridade, e a proteção da informação sigilosa e da informação pessoal.",
 "Cabe aos órgãos e entidades do poder público assegurar a gestão transparente da informação e a proteção da informação sigilosa, ficando a proteção da informação pessoal sujeita à legislação específica e fora do alcance da Lei de Acesso à Informação.",
 "Art. 6.º, I a III.","exclui informação pessoal","r01g")
# ---- R02
P("R02",["4"],"conceito_correto","confusao_instituto",2,
 "Informação sigilosa é aquela submetida temporariamente à restrição de acesso público em razão de sua imprescindibilidade para a segurança da sociedade e do Estado, ao passo que informação pessoal é aquela relacionada à pessoa natural identificada ou identificável.",
 "Informação sigilosa é aquela relacionada à pessoa natural identificada ou identificável, ao passo que informação pessoal é aquela submetida temporariamente à restrição de acesso público em razão de sua imprescindibilidade para a segurança da sociedade e do Estado.",
 "Art. 4.º, III e IV.","inverte conceitos","r02a")
P("R02",["4"],"conceito_correto","confusao_instituto",3,
 "Disponibilidade é a qualidade da informação que pode ser conhecida e utilizada por indivíduos, equipamentos ou sistemas autorizados; autenticidade é a qualidade da informação produzida, expedida, recebida ou modificada por determinado indivíduo, equipamento ou sistema.",
 "Disponibilidade é a qualidade da informação não modificada, inclusive quanto à origem, trânsito e destino; autenticidade é a qualidade da informação coletada na fonte, com o máximo de detalhamento possível, sem modificações, segundo a disciplina da Lei n.º 12.527/2011.",
 "Art. 4.º, VI e VII (integridade = não modificada; primariedade = coletada na fonte).","troca conceitos","r02b")
P("R02",["4"],"conceito_correto","confusao_instituto",3,
 "Integridade é a qualidade da informação não modificada, inclusive quanto à origem, trânsito e destino, e primariedade é a qualidade da informação coletada na fonte, com o máximo de detalhamento possível, sem modificações.",
 "Integridade é a qualidade da informação coletada na fonte, com o máximo de detalhamento possível, e primariedade é a qualidade da informação não modificada, inclusive quanto à origem, trânsito e destino.",
 "Art. 4.º, VIII e IX.","inverte integridade e primariedade","r02c")
P("R02",["4"],"conceito_correto","troca_efeito",2,
 "Para os efeitos da lei, informação é o conjunto de dados, processados ou não, que podem ser utilizados para produção e transmissão de conhecimento, contidos em qualquer meio, suporte ou formato, e documento é a unidade de registro de informações, qualquer que seja o suporte ou formato.",
 "Para os efeitos da lei, informação é apenas o dado processado, utilizado para produção e transmissão de conhecimento, contido em suporte físico, e documento é o registro formal de informações em papel, assinado por autoridade competente, de acordo com o regime geral da lei.",
 "Art. 4.º, I e II.","restringe suporte e formato","r02d")
P("R02",["4"],"conceito_correto","excecao_omitida",3,
 "Tratamento da informação é o conjunto de ações referentes à produção, recepção, classificação, utilização, acesso, reprodução, transporte, transmissão, distribuição, arquivamento, armazenamento, eliminação, avaliação, destinação ou controle da informação.",
 "Tratamento da informação é o conjunto de ações restrito à classificação, ao arquivamento e à eliminação da informação, não abrangendo a sua produção, recepção, transmissão ou o seu controle, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 4.º, V.","restringe ações","r02e")
# ---- R03
P("R03",["7"],"conceito_correto","excecao_omitida",3,
 "O acesso à informação compreende, entre outros, os direitos de obter informação produzida ou custodiada por pessoa física ou entidade privada decorrente de qualquer vínculo com órgãos ou entidades públicos, mesmo que esse vínculo já tenha cessado.",
 "O acesso à informação compreende o direito de obter informação produzida ou custodiada por pessoa física ou entidade privada com vínculo com órgãos ou entidades públicos, desde que o vínculo esteja vigente na data do pedido.",
 "Art. 7.º, III.","exige vínculo vigente","r03a")
P("R03",["7"],"conceito_correto","restricao_indevida",3,
 "O acesso à informação compreende o direito de obter informações relativas à administração do patrimônio público, à utilização de recursos públicos, a licitações e a contratos administrativos, bem como ao resultado de inspeções, auditorias, prestações e tomadas de contas, incluindo as relativas a exercícios anteriores.",
 "O acesso à informação compreende o direito de obter informações relativas à administração do patrimônio público e a contratos administrativos, ficando as relativas a auditorias e prestações de contas sujeitas a sigilo até o julgamento definitivo pelo órgão de controle, na forma prevista na Lei de Acesso à Informação.",
 "Art. 7.º, VI e VII, b.","impõe sigilo a auditorias","r03b")
P("R03",["7"],"conceito_correto","excecao_omitida",3,
 "O acesso à informação previsto na lei não compreende as informações referentes a projetos de pesquisa e desenvolvimento científicos ou tecnológicos cujo sigilo seja imprescindível à segurança da sociedade e do Estado.",
 "O acesso à informação previsto na lei compreende todas as informações referentes a projetos de pesquisa e desenvolvimento científicos ou tecnológicos, ainda que o sigilo seja imprescindível à segurança da sociedade e do Estado, que serão apenas classificadas.",
 "Art. 7.º, § 1.º.","retira a exceção","r03c")
P("R03",["7"],"conceito_correto","troca_efeito",3,
 "Quando não for autorizado acesso integral à informação por ser ela parcialmente sigilosa, é assegurado o acesso à parte não sigilosa por meio de certidão, extrato ou cópia com ocultação da parte sob sigilo.",
 "Quando a informação for parcialmente sigilosa, o acesso será negado integralmente, por inviabilidade de separar a parte sigilosa, cabendo ao requerente recorrer para obter a parte não sigilosa.",
 "Art. 7.º, § 2.º.","nega acesso parcial","r03d")
P("R03",["7"],"conceito_correto","troca_efeito",3,
 "O direito de acesso aos documentos ou às informações neles contidos utilizados como fundamento da tomada de decisão e do ato administrativo será assegurado com a edição do ato decisório respectivo.",
 "O direito de acesso aos documentos utilizados como fundamento da tomada de decisão e do ato administrativo somente será assegurado após o trânsito em julgado administrativo da decisão, independentemente da edição do ato decisório.",
 "Art. 7.º, § 3.º.","posterga o acesso","r03e")
P("R03",["7"],"conceito_correto","troca_numero",3,
 "Informado do extravio da informação solicitada, o interessado poderá requerer à autoridade competente a imediata abertura de sindicância para apurar o desaparecimento da documentação, e o responsável pela guarda deverá, no prazo de dez dias, justificar o fato e indicar testemunhas que comprovem sua alegação.",
 "Informado do extravio da informação solicitada, o interessado poderá requerer à autoridade competente a abertura de processo administrativo disciplinar, e o responsável pela guarda deverá, no prazo de vinte dias, justificar o fato e indicar testemunhas que comprovem sua alegação.",
 "Art. 7.º, §§ 5.º e 6.º: sindicância; 10 dias.","troca instituto e prazo","r03f")
P("R03",["7"],"conceito_correto","excecao_omitida",3,
 "A negativa de acesso às informações objeto de pedido formulado, quando não fundamentada, sujeitará o responsável a medidas disciplinares, nos termos do art. 32 da lei.",
 "A negativa de acesso às informações objeto de pedido formulado, ainda que não fundamentada, não gera responsabilização do agente se a informação for de interesse particular do requerente.",
 "Art. 7.º, § 4.º.","afasta responsabilização","r03g")
# ---- R04
P("R04",["8"],"conceito_correto","troca_efeito",2,
 "É dever dos órgãos e entidades públicas promover, independentemente de requerimentos, a divulgação em local de fácil acesso, no âmbito de suas competências, de informações de interesse coletivo ou geral por eles produzidas ou custodiadas.",
 "É dever dos órgãos e entidades públicas divulgar informações de interesse coletivo ou geral por eles produzidas ou custodiadas somente quando houver requerimento de interessado que demonstre o interesse público na informação.",
 "Art. 8.º, caput (transparência ativa).","exige requerimento","r04a")
P("R04",["8"],"conceito_correto","excecao_omitida",3,
 "Na divulgação ativa de informações deverão constar, no mínimo, o registro das competências e estrutura organizacional, os registros de repasses ou transferências de recursos financeiros e de despesas, as informações sobre licitações e contratos e as respostas a perguntas mais frequentes da sociedade.",
 "Na divulgação ativa de informações deverão constar, no mínimo, o registro das competências e estrutura organizacional e as informações sobre licitações, ficando facultativa a divulgação dos repasses de recursos, das despesas e das respostas a perguntas frequentes, nos termos da Lei de Acesso à Informação.",
 "Art. 8.º, § 1.º, I a VI.","torna facultativo","r04b")
P("R04",["8"],"conceito_correto","troca_efeito",3,
 "Para cumprimento da divulgação ativa, os órgãos e entidades públicas deverão utilizar todos os meios e instrumentos legítimos de que dispuserem, sendo obrigatória a divulgação em sítios oficiais da rede mundial de computadores.",
 "Para cumprimento da divulgação ativa, os órgãos e entidades públicas poderão optar entre os meios e instrumentos legítimos de que dispuserem, sendo facultativa a divulgação em sítios oficiais da rede mundial de computadores.",
 "Art. 8.º, § 2.º.","torna a internet facultativa","r04c")
P("R04",["8"],"conceito_correto","excecao_omitida",3,
 "Os sítios oficiais devem, entre outros requisitos, conter ferramenta de pesquisa de conteúdo, possibilitar a gravação de relatórios em formatos eletrônicos abertos e não proprietários, permitir o acesso automatizado por sistemas externos em formatos abertos, estruturados e legíveis por máquina e garantir acessibilidade a pessoas com deficiência.",
 "Os sítios oficiais devem, entre outros requisitos, possibilitar a gravação de relatórios apenas em formato proprietário que garanta a autenticidade, vedado o acesso automatizado por sistemas externos, e garantir acessibilidade a pessoas com deficiência, segundo a disciplina da Lei n.º 12.527/2011.",
 "Art. 8.º, § 3.º.","inverte requisitos","r04d")
P("R04",["8"],"conceito_correto","troca_numero",3,
 "Os Municípios com população de até dez mil habitantes ficam dispensados da divulgação obrigatória na internet, mantida a obrigatoriedade de divulgação, em tempo real, de informações relativas à execução orçamentária e financeira, nos critérios e prazos da Lei de Responsabilidade Fiscal.",
 "Os Municípios com população de até vinte mil habitantes ficam integralmente dispensados da divulgação obrigatória na internet, inclusive das informações relativas à execução orçamentária e financeira, de acordo com o regime geral da lei.",
 "Art. 8.º, § 4.º: até 10 mil habitantes; execução orçamentária e financeira continua obrigatória.","altera o limite e a dispensa","r04e")
P("R04",["9"],"conceito_correto","excecao_omitida",3,
 "O acesso a informações públicas será assegurado mediante criação de serviço de informações ao cidadão, em local com condições apropriadas para atender e orientar o público, informar sobre a tramitação de documentos e protocolizar requerimentos, e mediante realização de audiências ou consultas públicas e incentivo à participação popular.",
 "O acesso a informações públicas será assegurado exclusivamente mediante criação de serviço de informações ao cidadão, que atenderá o público e protocolizará requerimentos, não se exigindo a realização de audiências ou consultas públicas, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 9.º, I e II.","exclusividade do serviço","r04f")
# ---- R05
P("R05",["10"],"conceito_correto","excecao_omitida",2,
 "Qualquer interessado poderá apresentar pedido de acesso a informações aos órgãos e entidades sujeitos à lei, por qualquer meio legítimo, devendo o pedido conter a identificação do requerente e a especificação da informação requerida.",
 "Qualquer interessado poderá apresentar pedido de acesso a informações, exclusivamente por meio de formulário próprio, devendo o pedido conter a identificação do requerente, a especificação da informação e a justificativa do interesse.",
 "Art. 10, caput e § 3.º.","exige formulário e motivação","r05a")
P("R05",["10"],"conceito_correto","troca_efeito",3,
 "São vedadas quaisquer exigências relativas aos motivos determinantes da solicitação de informações de interesse público, e a identificação do requerente não pode conter exigências que inviabilizem a solicitação.",
 "O órgão poderá exigir do requerente a indicação dos motivos determinantes da solicitação de informações de interesse público sempre que a informação seja de difícil obtenção, na forma prevista na Lei de Acesso à Informação.",
 "Art. 10, §§ 1.º e 3.º.","admite exigência de motivo","r05b")
P("R05",["10"],"conceito_correto","excecao_omitida",3,
 "Os órgãos e entidades do poder público devem viabilizar alternativa de encaminhamento de pedidos de acesso por meio de seus sítios oficiais na internet.",
 "Os órgãos e entidades do poder público podem restringir o encaminhamento de pedidos de acesso ao atendimento presencial, vedada a utilização de seus sítios oficiais na internet para esse fim.",
 "Art. 10, § 2.º.","veda pedido por internet","r05c")
P("R05",["11"],"conceito_correto","troca_numero",2,
 "Não sendo possível conceder o acesso imediato, o órgão ou entidade que receber o pedido deverá, em prazo não superior a vinte dias, comunicar a data, local e modo para a consulta, indicar as razões de recusa ou comunicar que não possui a informação, podendo o prazo ser prorrogado por mais dez dias, mediante justificativa expressa.",
 "Não sendo possível conceder o acesso imediato, o órgão ou entidade que receber o pedido deverá, em prazo não superior a trinta dias, comunicar a data, local e modo para a consulta, indicar as razões de recusa ou comunicar que não possui a informação, podendo o prazo ser prorrogado por mais quinze dias, mediante justificativa expressa.",
 "Art. 11, § 1.º (20 dias) e § 2.º (+10 dias, com justificativa expressa e ciência do requerente).","troca prazos","r05d")
P("R05",["11"],"conceito_correto","excecao_omitida",3,
 "Se o órgão não possuir a informação, deverá comunicar o fato, indicar, se for do seu conhecimento, o órgão ou entidade que a detém ou remeter o requerimento a esse órgão, cientificando o interessado da remessa de seu pedido.",
 "Se o órgão não possuir a informação, deverá arquivar o pedido, cabendo ao requerente formular novo pedido ao órgão que detém a informação, que o órgão ao qual o primeiro pedido foi dirigido não está obrigado a indicar.",
 "Art. 11, § 1.º, III.","dispensa indicação e remessa","r05e")
P("R05",["11"],"conceito_correto","excecao_omitida",3,
 "Quando não for autorizado o acesso por se tratar de informação total ou parcialmente sigilosa, o requerente deverá ser informado sobre a possibilidade de recurso, prazos e condições para sua interposição, devendo ser-lhe indicada a autoridade competente para sua apreciação.",
 "Quando não for autorizado o acesso por se tratar de informação total ou parcialmente sigilosa, o órgão ficará dispensado de informar ao requerente sobre a possibilidade de recurso, bastando a comunicação do grau de sigilo da informação, nos termos da Lei de Acesso à Informação.",
 "Art. 11, § 4.º.","dispensa informar sobre recurso","r05f")
P("R05",["11"],"conceito_correto","excecao_omitida",3,
 "A informação armazenada em formato digital será fornecida nesse formato, caso haja anuência do requerente; e, se a informação já estiver disponível ao público em formato impresso, eletrônico ou outro meio de acesso universal, bastará informar por escrito o lugar e a forma de consultá-la, salvo se o requerente declarar não dispor de meios para fazê-lo.",
 "A informação armazenada em formato digital será sempre fornecida em meio impresso, mesmo sem anuência do requerente; e, se já estiver disponível ao público em meio de acesso universal, o órgão deverá fornecê-la diretamente, ainda que o requerente disponha de meios para obtê-la, segundo a disciplina da Lei n.º 12.527/2011.",
 "Art. 11, §§ 5.º e 6.º.","impõe formato e fornecimento direto","r05g")
P("R05",["12"],"conceito_correto","excecao_omitida",3,
 "O serviço de busca e fornecimento da informação é gratuito, salvo nas hipóteses de reprodução de documentos, situação em que poderá ser cobrado exclusivamente o valor necessário ao ressarcimento do custo dos serviços e dos materiais utilizados, estando isento aquele cuja situação econômica não lhe permita fazê-lo, declarada nos termos da Lei n.º 7.115/1983.",
 "O serviço de busca e fornecimento da informação poderá ser cobrado em valor fixado livremente pelo órgão, para custear a estrutura de atendimento, estando isento apenas aquele que comprovar a hipossuficiência por certidão da Defensoria Pública, de acordo com o regime geral da lei.",
 "Art. 12 e parágrafo único.","admite cobrança livre","r05h")
P("R05",["13","14"],"conceito_correto","troca_efeito",3,
 "Quando a manipulação do documento puder prejudicar sua integridade, deverá ser oferecida a consulta de cópia, com certificação de que esta confere com o original; e é direito do requerente obter o inteiro teor de decisão de negativa de acesso, por certidão ou cópia.",
 "Quando a manipulação do documento puder prejudicar sua integridade, o acesso será negado por inviabilidade de consulta; e a decisão de negativa de acesso será comunicada ao requerente apenas em resumo, sem direito a obter o inteiro teor.",
 "Arts. 13 e 14.","nega cópia e inteiro teor","r05i")
# ---- R06
P("R06",["15"],"conceito_correto","troca_numero",2,
 "No caso de indeferimento de acesso a informações ou às razões da negativa, poderá o interessado interpor recurso no prazo de dez dias a contar da sua ciência, dirigido à autoridade hierarquicamente superior à que exarou a decisão, que deverá se manifestar no prazo de cinco dias.",
 "No caso de indeferimento de acesso a informações ou às razões da negativa, poderá o interessado interpor recurso no prazo de quinze dias a contar da sua ciência, dirigido à própria autoridade que exarou a decisão, que deverá se manifestar no prazo de dez dias.",
 "Art. 15 e parágrafo único: 10 dias; autoridade superior; 5 dias.","troca prazos e destinatário","r06a")
P("R06",["16"],"conceito_correto","troca_autoridade",3,
 "Negado o acesso a informação pelos órgãos ou entidades do Poder Executivo Federal, o requerente poderá recorrer à Controladoria-Geral da União, que deliberará no prazo de cinco dias, desde que o recurso tenha sido antes submetido à apreciação de pelo menos uma autoridade hierarquicamente superior àquela que exarou a decisão.",
 "Negado o acesso a informação pelos órgãos ou entidades do Poder Executivo Federal, o requerente poderá recorrer diretamente à Controladoria-Geral da União, que deliberará no prazo de dez dias, dispensada a prévia apreciação por autoridade hierarquicamente superior, conforme o regramento da Lei de Acesso à Informação.",
 "Art. 16, caput e § 1.º.","dispensa instância prévia","r06b")
P("R06",["16"],"conceito_correto","excecao_omitida",4,
 "O recurso à Controladoria-Geral da União cabe quando o acesso a informação não classificada como sigilosa for negado, quando a negativa quanto à informação classificada não indicar a autoridade classificadora ou a hierarquicamente superior a quem possa ser dirigido pedido de acesso ou desclassificação, quando não observados os procedimentos de classificação ou quando descumpridos prazos ou outros procedimentos da lei.",
 "O recurso à Controladoria-Geral da União cabe quando o acesso a qualquer informação, classificada ou não como sigilosa, for negado, sendo irrelevante a observância dos procedimentos de classificação ou dos prazos da lei, na forma prevista na Lei de Acesso à Informação.",
 "Art. 16, I a IV.","amplia hipóteses de cabimento","r06c")
P("R06",["16"],"conceito_correto","troca_autoridade",3,
 "Negado o acesso à informação pela Controladoria-Geral da União, poderá ser interposto recurso à Comissão Mista de Reavaliação de Informações.",
 "Negado o acesso à informação pela Controladoria-Geral da União, cabe recurso ao Ministro de Estado da área ou ao Presidente da República, sem possibilidade de recurso à Comissão Mista de Reavaliação de Informações.",
 "Art. 16, § 3.º.","troca instância","r06d")
P("R06",["17"],"conceito_correto","troca_autoridade",4,
 "No caso de indeferimento de pedido de desclassificação de informação protocolado em órgão da administração pública federal, poderá o requerente recorrer ao Ministro de Estado da área; indeferido o recurso que tenha por objeto a desclassificação de informação secreta ou ultrassecreta, caberá recurso à Comissão Mista de Reavaliação de Informações.",
 "No caso de indeferimento de pedido de desclassificação de informação protocolado em órgão da administração pública federal, poderá o requerente recorrer diretamente à Comissão Mista de Reavaliação de Informações, sendo vedado o recurso ao Ministro de Estado da área, nos termos da Lei de Acesso à Informação.",
 "Art. 17, caput e § 2.º.","inverte instâncias","r06e")
P("R06",["18","19"],"conceito_correto","troca_autoridade",4,
 "Os procedimentos de revisão de decisões denegatórias e de revisão de classificação de documentos sigilosos serão objeto de regulamentação própria dos Poderes Legislativo e Judiciário e do Ministério Público, em seus respectivos âmbitos; os órgãos do Poder Judiciário e do Ministério Público informarão ao CNJ e ao CNMP, respectivamente, as decisões que, em grau de recurso, negarem acesso a informações de interesse público.",
 "Os procedimentos de revisão de decisões denegatórias dos Poderes Legislativo e Judiciário e do Ministério Público seguirão o regulamento do Poder Executivo Federal, cabendo recurso à Controladoria-Geral da União, que informará ao CNJ e ao CNMP as decisões denegatórias, segundo a disciplina da Lei n.º 12.527/2011.",
 "Arts. 18 e 19, § 2.º.","submete outros Poderes à CGU","r06f")
P("R06",["20"],"conceito_correto","troca_autoridade",2,
 "Aplica-se subsidiariamente, no que couber, a Lei n.º 9.784/1999 ao procedimento de acesso à informação de que trata o Capítulo III da Lei de Acesso à Informação.",
 "Aplica-se subsidiariamente, no que couber, a Lei n.º 8.112/1990 ao procedimento de acesso à informação de que trata o Capítulo III da Lei de Acesso à Informação.",
 "Art. 20.","troca a lei subsidiária","r06g")
