# Lei 14.133/2021 — lote L7 parte e (arts. 76 a 91)
Q = []
TAILS=[" Essa disciplina consta da Lei n.º 14.133/2021 e se aplica às licitações e contratações por ela regidas.",
 " Trata-se de regra do regime geral de licitações e contratos da Administração Pública, nos termos da Lei n.º 14.133/2021.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática geral da nova Lei de Licitações e Contratos Administrativos.",
 " Essa seria a orientação extraída da lei para o procedimento de licitação de que ela trata."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, risco=None):
    ex = {"risco": risco} if risco else {}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# T26
P("T26",["76"],"conceito_correto","excecao_omitida",3,
 "A alienação de bens da Administração Pública, subordinada à existência de interesse público devidamente justificado, será precedida de avaliação; tratando-se de bens imóveis, exigirá autorização legislativa e dependerá de licitação na modalidade leilão, ressalvados os casos de dispensa previstos em lei.",
 "A alienação de bens imóveis da Administração Pública, subordinada à existência de interesse público devidamente justificado, dependerá de licitação na modalidade concorrência e dispensará avaliação prévia e autorização legislativa.",
 "Art. 76, caput e I.","troca leilão por concorrência","t26a")
P("T26",["76"],"conceito_correto","excecao_omitida",4,
 "Tratando-se de bens móveis, a alienação dependerá de licitação na modalidade leilão, dispensada nos casos de doação exclusivamente para fins e uso de interesse social, permuta exclusivamente entre órgãos ou entidades da Administração Pública, venda de ações em bolsa, venda de títulos, venda de bens produzidos ou comercializados por entidades da Administração em virtude de suas finalidades e venda de materiais e equipamentos sem utilização previsível para outros órgãos ou entidades da Administração.",
 "Tratando-se de bens móveis, a alienação dependerá sempre de licitação na modalidade leilão, sendo vedada a dispensa de licitação, inclusive para doação para fins de interesse social e permuta entre órgãos da Administração Pública.",
 "Art. 76, II.","veda qualquer dispensa","t26b")
P("T26",["76"],"conceito_correto","troca_efeito",4,
 "A alienação de bens imóveis da Administração Pública cuja aquisição tenha sido derivada de procedimentos judiciais ou de dação em pagamento dispensará autorização legislativa e exigirá apenas avaliação prévia e licitação na modalidade leilão.",
 "A alienação de bens imóveis da Administração Pública cuja aquisição tenha sido derivada de procedimentos judiciais ou de dação em pagamento exigirá autorização legislativa e dispensará avaliação prévia e licitação.",
 "Art. 76, § 1º.","inverte exigências","t26c")
P("T26",["76"],"conceito_correto","troca_efeito",4,
 "Os imóveis doados a outro órgão ou entidade da Administração Pública, cessadas as razões que justificaram sua doação, serão revertidos ao patrimônio da pessoa jurídica doadora, vedada sua alienação pelo beneficiário.",
 "Os imóveis doados a outro órgão ou entidade da Administração Pública, cessadas as razões que justificaram sua doação, passarão ao patrimônio do beneficiário, que poderá aliená-los livremente.",
 "Art. 76, § 2º.","retira reversão","t26d")
P("T26",["76"],"conceito_correto","troca_numero",4,
 "Entende-se por investidura a alienação, ao proprietário de imóvel lindeiro, de área remanescente ou resultante de obra pública que se tornar inaproveitável isoladamente, por preço que não seja inferior ao da avaliação nem superior a 50% do valor máximo permitido para dispensa de licitação de bens e serviços previsto na Lei n.º 14.133/2021.",
 "Entende-se por investidura a alienação, a qualquer interessado, de área remanescente ou resultante de obra pública, por preço que não seja inferior ao da avaliação nem superior a 100% do valor máximo permitido para dispensa de licitação de bens e serviços previsto na Lei n.º 14.133/2021.",
 "Art. 76, § 5º, I.","troca beneficiário e percentual","t26e")
P("T26",["76"],"conceito_correto","excecao_omitida",4,
 "A doação com encargo será licitada, e de seu instrumento constarão, obrigatoriamente, os encargos, o prazo de seu cumprimento e a cláusula de reversão, sob pena de nulidade do ato, dispensada a licitação em caso de interesse público devidamente justificado; se o donatário necessitar oferecer o imóvel em garantia de financiamento, a cláusula de reversão e as demais obrigações serão garantidas por hipoteca em segundo grau em favor do doador.",
 "A doação com encargo dispensa sempre a licitação, e de seu instrumento não precisam constar o prazo de cumprimento nem a cláusula de reversão; se o donatário oferecer o imóvel em garantia de financiamento, a reversão será garantida por hipoteca em primeiro grau em favor do doador.",
 "Art. 76, §§ 6º e 7º.","dispensa sempre e troca grau da hipoteca","t26f")
P("T26",["77"],"conceito_correto","troca_efeito",3,
 "Para a venda de bens imóveis, será concedido direito de preferência ao licitante que, submetendo-se a todas as regras do edital, comprove a ocupação do imóvel objeto da licitação.",
 "Para a venda de bens imóveis, será concedido direito de preferência ao ocupante do imóvel, ainda que não participe da licitação, dispensado do cumprimento das regras do edital.",
 "Art. 77.","dispensa participação","t26g")
# T27
P("T27",["78"],"conceito_correto","excecao_omitida",3,
 "São procedimentos auxiliares das licitações e das contratações regidas pela Lei n.º 14.133/2021 o credenciamento, a pré-qualificação, o procedimento de manifestação de interesse, o sistema de registro de preços e o registro cadastral, que obedecerão a critérios claros e objetivos definidos em regulamento.",
 "São procedimentos auxiliares das licitações e das contratações regidas pela Lei n.º 14.133/2021 o credenciamento, a pré-qualificação, o diálogo competitivo, o sistema de registro de preços e o registro cadastral, que obedecerão a critérios definidos em edital de cada licitação.",
 "Art. 78, I a V e § 1º.","troca MIP por diálogo competitivo","t27a")
P("T27",["78"],"conceito_correto","troca_efeito",4,
 "O julgamento que decorrer dos procedimentos auxiliares da pré-qualificação e do procedimento de manifestação de interesse seguirá o mesmo procedimento das licitações.",
 "O julgamento que decorrer dos procedimentos auxiliares do credenciamento e do registro cadastral seguirá o mesmo procedimento das licitações.",
 "Art. 78, § 2º.","troca procedimentos","t27b")
P("T27",["79"],"conceito_correto","excecao_omitida",4,
 "O credenciamento poderá ser usado nas hipóteses de contratação paralela e não excludente, com seleção a critério de terceiros e em mercados fluidos.",
 "O credenciamento poderá ser usado exclusivamente na hipótese de contratação paralela e não excludente, vedada sua utilização em mercados fluidos ou com seleção a critério de terceiros.",
 "Art. 79, I a III.","restringe hipóteses","t27c")
P("T27",["79"],"conceito_correto","excecao_omitida",4,
 "Nos procedimentos de credenciamento, a Administração deverá divulgar edital de chamamento de interessados em sítio eletrônico oficial, de modo a permitir o cadastramento permanente de novos interessados, e não será permitido o cometimento a terceiros do objeto contratado sem autorização expressa da Administração.",
 "Nos procedimentos de credenciamento, o edital de chamamento de interessados terá prazo fechado para cadastramento, vedado o ingresso de novos interessados após seu término, e é permitida a subcontratação do objeto sem autorização da Administração.",
 "Art. 79, parágrafo único, I e V.","fecha cadastramento e libera subcontratação","t27d")
P("T27",["79"],"conceito_correto","troca_efeito",5,
 "No credenciamento, o edital deverá prever as condições padronizadas de contratação e, nas hipóteses de contratação paralela e não excludente e de seleção a critério de terceiros, definir o valor da contratação; em mercados fluidos, a Administração deverá registrar as cotações de mercado vigentes no momento da contratação; é admitida a denúncia por qualquer das partes nos prazos fixados no edital.",
 "No credenciamento, o edital deverá prever condições de contratação específicas para cada credenciado e, em mercados fluidos, definir valor fixo da contratação por todo o período; não é admitida a denúncia por qualquer das partes.",
 "Art. 79, parágrafo único, III, IV e VI.","valor fixo e veda denúncia","t27e")
P("T27",["80"],"conceito_correto","troca_numero",3,
 "A pré-qualificação é o procedimento técnico-administrativo para selecionar previamente licitantes que reúnam condições de habilitação para participar de futura licitação ou de licitação vinculada a programas de obras ou serviços objetivamente definidos, e bens que atendam às exigências técnicas ou de qualidade estabelecidas pela Administração; ficará permanentemente aberta para a inscrição de interessados e terá validade de, no máximo, 1 ano.",
 "A pré-qualificação é o procedimento técnico-administrativo para selecionar previamente apenas licitantes, vedada a seleção de bens; ficará aberta por período determinado no edital e terá validade de, no máximo, 5 anos.",
 "Art. 80, caput, I e II, §§ 2º e 8º.","restringe objeto e troca validade","t27f")
P("T27",["80"],"conceito_correto","troca_numero",4,
 "A apresentação de documentos na pré-qualificação far-se-á perante órgão ou comissão indicada pela Administração, que deverá examiná-los no prazo máximo de 10 dias úteis e determinar correção ou reapresentação de documentos, quando for o caso, com vistas à ampliação da competição.",
 "A apresentação de documentos na pré-qualificação far-se-á perante o agente de contratação, que deverá examiná-los no prazo máximo de 30 dias corridos, vedada a determinação de correção ou reapresentação de documentos.",
 "Art. 80, § 4º.","troca prazo e veda correção","t27g")
P("T27",["80"],"conceito_correto","excecao_omitida",4,
 "A pré-qualificação poderá ser parcial ou total, com alguns ou todos os requisitos técnicos ou de habilitação necessários à contratação, assegurada, em qualquer hipótese, a igualdade de condições entre os concorrentes; os licitantes e os bens pré-qualificados serão obrigatoriamente divulgados, e a licitação que se seguir poderá ser restrita a licitantes ou bens pré-qualificados.",
 "A pré-qualificação será sempre total, com todos os requisitos de habilitação necessários à contratação; os licitantes e os bens pré-qualificados terão divulgação facultativa, e a licitação que se seguir deverá ser restrita a licitantes pré-qualificados.",
 "Art. 80, §§ 7º, 9º e 10.","torna total e obrigatória restrição","t27h")
P("T27",["80"],"conceito_correto","excecao_omitida",4,
 "Quando a pré-qualificação for aberta a licitantes, poderão ser dispensados os documentos que já constarem do registro cadastral; quando aberta a bens, poderá ser exigida a comprovação de qualidade; e os bens e serviços pré-qualificados deverão integrar o catálogo de bens e serviços da Administração.",
 "Quando a pré-qualificação for aberta a licitantes, os documentos constantes do registro cadastral deverão ser reapresentados; quando aberta a bens, é vedada a exigência de comprovação de qualidade; e os bens pré-qualificados não integrarão o catálogo da Administração.",
 "Art. 80, §§ 1º e 5º.","inverte regras","t27i")
# T28
P("T28",["81"],"conceito_correto","troca_efeito",4,
 "A realização, pela iniciativa privada, de estudos, investigações, levantamentos e projetos em decorrência do procedimento de manifestação de interesse não atribuirá ao realizador direito de preferência no processo licitatório, não obrigará o poder público a realizar licitação e não implicará, por si só, direito a ressarcimento de valores envolvidos em sua elaboração.",
 "A realização, pela iniciativa privada, de estudos, investigações, levantamentos e projetos em decorrência do procedimento de manifestação de interesse atribuirá ao realizador direito de preferência no processo licitatório, obrigará o poder público a realizar licitação e garantirá ressarcimento dos valores envolvidos.",
 "Art. 81, § 2º, I a III.","inverte efeitos","t28a")
P("T28",["81"],"conceito_correto","troca_autoridade",4,
 "Os estudos realizados em decorrência do procedimento de manifestação de interesse serão remunerados somente pelo vencedor da licitação, vedada, em qualquer hipótese, a cobrança de valores do poder público; o procedimento poderá ser restrito a startups, exigida, na seleção definitiva da inovação, validação prévia fundamentada em métricas objetivas.",
 "Os estudos realizados em decorrência do procedimento de manifestação de interesse serão remunerados pelo poder público, que poderá cobrar do vencedor da licitação o equivalente; o procedimento não poderá ser restrito a startups.",
 "Art. 81, §§ 2º, IV, e 4º.","inverte remuneração","t28b")
P("T28",["81"],"conceito_correto","excecao_omitida",3,
 "A Administração poderá solicitar à iniciativa privada, mediante procedimento aberto de manifestação de interesse iniciado com a publicação de edital de chamamento público, a propositura e a realização de estudos, investigações, levantamentos e projetos de soluções inovadoras que contribuam com questões de relevância pública, na forma de regulamento.",
 "A Administração poderá solicitar à iniciativa privada, mediante convite direto a empresas previamente selecionadas, a propositura e a realização de estudos e projetos de soluções inovadoras, dispensada a publicação de edital de chamamento público.",
 "Art. 81, caput.","dispensa chamamento público","t28c")
# T29
P("T29",["82"],"conceito_correto","excecao_omitida",4,
 "No sistema de registro de preços, o critério de julgamento da licitação será o de menor preço ou o de maior desconto sobre tabela de preços praticada no mercado, e o edital deverá prever o registro de mais de um fornecedor, desde que aceitem cotar o objeto em preço igual ao do licitante vencedor, assegurada a preferência de contratação de acordo com a ordem de classificação.",
 "No sistema de registro de preços, o critério de julgamento da licitação poderá ser o de técnica e preço, e o edital vedará o registro de mais de um fornecedor, ainda que aceitem cotar o objeto em preço igual ao do licitante vencedor.",
 "Art. 82, V e VII.","troca critério e veda pluralidade","t29a")
P("T29",["82"],"conceito_correto","excecao_omitida",5,
 "O critério de julgamento de menor preço por grupo de itens somente poderá ser adotado no registro de preços quando for demonstrada a inviabilidade de se promover a adjudicação por item e for evidenciada a sua vantagem técnica e econômica, e a contratação posterior de item específico constante de grupo de itens exigirá prévia pesquisa de mercado e demonstração de sua vantagem para o órgão ou entidade.",
 "O critério de julgamento de menor preço por grupo de itens poderá ser adotado livremente no registro de preços, e a contratação posterior de item específico constante de grupo de itens dispensa pesquisa de mercado.",
 "Art. 82, §§ 1º e 2º.","libera grupo de itens","t29b")
P("T29",["82"],"conceito_correto","excecao_omitida",5,
 "É permitido registro de preços com indicação limitada a unidades de contratação, sem indicação do total a ser adquirido, apenas quando for a primeira licitação para o objeto e o órgão não tiver registro de demandas anteriores, no caso de alimento perecível e no caso em que o serviço estiver integrado ao fornecimento de bens; nessas situações é obrigatória a indicação do valor máximo da despesa e é vedada a participação de outro órgão ou entidade na ata.",
 "É permitido registro de preços sem indicação do total a ser adquirido em qualquer situação, a critério do órgão gerenciador; nessas hipóteses é facultativa a indicação do valor máximo da despesa e é permitida a participação de outros órgãos na ata.",
 "Art. 82, §§ 3º e 4º.","generaliza exceção","t29c")
P("T29",["82"],"conceito_correto","excecao_omitida",4,
 "O sistema de registro de preços poderá ser usado para a contratação de bens e serviços, inclusive de obras e serviços de engenharia, observadas condições como a realização prévia de ampla pesquisa de mercado, o desenvolvimento obrigatório de rotina de controle, a atualização periódica dos preços registrados e a definição do período de validade do registro; poderá também, na forma de regulamento, ser utilizado nas hipóteses de inexigibilidade e de dispensa de licitação para aquisição de bens ou contratação de serviços por mais de um órgão ou entidade.",
 "O sistema de registro de preços poderá ser usado apenas para a contratação de bens e serviços comuns, vedada sua utilização para obras e serviços de engenharia e nas hipóteses de inexigibilidade e de dispensa de licitação.",
 "Art. 82, §§ 5º e 6º; art. 85.","veda obras e contratação direta","t29d")
P("T29",["83"],"conceito_correto","troca_efeito",3,
 "A existência de preços registrados implicará compromisso de fornecimento nas condições estabelecidas, mas não obrigará a Administração a contratar, facultada a realização de licitação específica para a aquisição pretendida, desde que devidamente motivada.",
 "A existência de preços registrados obrigará a Administração a contratar o quantitativo registrado, sendo vedada a realização de licitação específica para a aquisição pretendida.",
 "Art. 83.","torna obrigatória a contratação","t29e")
P("T29",["84"],"conceito_correto","troca_numero",3,
 "O prazo de vigência da ata de registro de preços será de 1 ano e poderá ser prorrogado, por igual período, desde que comprovado o preço vantajoso; o contrato decorrente da ata terá sua vigência estabelecida em conformidade com as disposições nela contidas.",
 "O prazo de vigência da ata de registro de preços será de 2 anos e poderá ser prorrogado, por até 5 anos, independentemente de comprovação de preço vantajoso; o contrato decorrente da ata terá vigência de, no máximo, 1 ano.",
 "Art. 84, caput e parágrafo único.","troca prazos","t29f")
P("T29",["85"],"conceito_correto","excecao_omitida",4,
 "A Administração poderá contratar a execução de obras e serviços de engenharia pelo sistema de registro de preços, desde que atendidos os requisitos de existência de projeto padronizado, sem complexidade técnica e operacional, e de necessidade permanente ou frequente de obra ou serviço a ser contratado.",
 "A Administração poderá contratar a execução de obras e serviços de engenharia pelo sistema de registro de preços, desde que exista projeto padronizado, bastando a necessidade eventual da obra ou serviço, ainda que complexo tecnicamente.",
 "Art. 85, I e II.","relaxa requisitos","t29g")
P("T29",["86"],"conceito_correto","troca_numero",4,
 "O órgão ou entidade gerenciadora deverá, na fase preparatória do processo licitatório, para fins de registro de preços, realizar procedimento público de intenção de registro de preços para, nos termos de regulamento, possibilitar, pelo prazo mínimo de 8 dias úteis, a participação de outros órgãos ou entidades na respectiva ata; o procedimento será dispensável quando o órgão gerenciador for o único contratante.",
 "O órgão ou entidade gerenciadora deverá, após a homologação da licitação, realizar procedimento público de intenção de registro de preços pelo prazo mínimo de 3 dias úteis; o procedimento é obrigatório mesmo quando o órgão gerenciador for o único contratante.",
 "Art. 86, caput e § 1º.","troca fase, prazo e dispensa","t29h")
P("T29",["86"],"conceito_correto","excecao_omitida",5,
 "Os órgãos e entidades que não participaram do procedimento de intenção de registro de preços poderão aderir à ata na condição de não participantes, mediante justificativa da vantagem da adesão, demonstração de compatibilidade dos valores com os praticados no mercado e prévias consulta e aceitação do órgão gerenciador e do fornecedor.",
 "Os órgãos e entidades que não participaram do procedimento de intenção de registro de preços poderão aderir à ata na condição de não participantes mediante simples comunicação ao órgão gerenciador, sendo dispensada a aceitação do fornecedor.",
 "Art. 86, § 2º.","dispensa aceitação do fornecedor","t29i")
P("T29",["86"],"conceito_correto","troca_numero",5,
 "As aquisições ou contratações adicionais por adesão não poderão exceder, por órgão ou entidade, a 50% dos quantitativos dos itens registrados na ata para o órgão gerenciador e os participantes, e o quantitativo decorrente das adesões não poderá exceder, na totalidade, ao dobro do quantitativo de cada item registrado, independentemente do número de órgãos não participantes que aderirem.",
 "As aquisições ou contratações adicionais por adesão não poderão exceder, por órgão ou entidade, a 100% dos quantitativos dos itens registrados na ata, e o quantitativo decorrente das adesões não poderá exceder, na totalidade, ao triplo do quantitativo de cada item registrado.",
 "Art. 86, §§ 4º e 5º.","troca limites da carona","t29j")
P("T29",["86"],"conceito_correto","excecao_omitida",5,
 "A adesão à ata de registro de preços de órgão do Poder Executivo federal por órgãos estaduais, distritais e municipais poderá ser exigida para fins de transferências voluntárias, não ficando sujeita ao limite do dobro se destinada à execução descentralizada de programa ou projeto federal e comprovada a compatibilidade dos preços; é vedada aos órgãos e entidades da Administração Pública federal a adesão à ata gerenciada por órgão estadual, distrital ou municipal.",
 "Os órgãos da Administração Pública federal poderão aderir a ata de registro de preços gerenciada por órgão estadual, distrital ou municipal, observados os limites legais; a adesão por entes subnacionais a ata federal nunca poderá ser exigida para transferências voluntárias.",
 "Art. 86, §§ 6º e 8º.","permite adesão federal a ata estadual","t29k")
P("T29",["86"],"caso_concreto","caso_concreto",5,
 "Um município, que não participou do procedimento de intenção de registro de preços, deseja aderir à ata gerenciada por órgão federal. Para isso, deve apresentar justificativa da vantagem, demonstrar a compatibilidade dos preços com o mercado e obter a prévia aceitação do órgão gerenciador e do fornecedor, respeitado o limite de 50% dos quantitativos registrados para o órgão gerenciador e os participantes.",
 "Um órgão federal, que não participou do procedimento de intenção de registro de preços, deseja aderir à ata gerenciada por município. Para isso, basta demonstrar a vantagem da adesão e a compatibilidade dos preços, dispensada a aceitação do órgão gerenciador, respeitado o limite do dobro dos quantitativos.",
 "Art. 86, §§ 2º, 4º e 8º.","federal não pode aderir a ata municipal","t29l")
# T30
P("T30",["87"],"conceito_correto","excecao_omitida",3,
 "Os órgãos e entidades da Administração Pública deverão utilizar o sistema de registro cadastral unificado disponível no PNCP; ele será público, permanentemente aberto aos interessados, com chamamento público pela internet, no mínimo anualmente, para atualização dos registros existentes e ingresso de novos interessados, sendo proibida a exigência de registro cadastral complementar para acesso a edital e anexos.",
 "Cada órgão ou entidade manterá seu próprio sistema de registro cadastral, que será aberto apenas por ocasião de cada licitação, sendo permitida a exigência de registro cadastral complementar para acesso a edital e anexos.",
 "Art. 87, caput, §§ 1º e 2º.","descentraliza cadastro","t30a")
P("T30",["87"],"conceito_correto","troca_efeito",4,
 "A Administração poderá realizar licitação restrita a fornecedores cadastrados, atendidos os critérios, condições e limites do regulamento e a ampla publicidade dos procedimentos de cadastramento; nesse caso, será admitido fornecedor que realize seu cadastro dentro do prazo previsto no edital para apresentação de propostas.",
 "A Administração poderá realizar licitação restrita a fornecedores cadastrados, não sendo admitido fornecedor que realize seu cadastro após a publicação do edital.",
 "Art. 87, §§ 3º e 4º.","veda cadastro até propostas","t30b")
P("T30",["88"],"conceito_correto","excecao_omitida",4,
 "O inscrito no registro cadastral será classificado por categorias, subdivididas em grupos, segundo a qualificação técnica e econômico-financeira avaliada, de acordo com regras objetivas divulgadas em sítio eletrônico oficial; receberá certificado, renovável sempre que atualizar o registro, e seu registro poderá ser alterado, suspenso ou cancelado a qualquer tempo se deixar de satisfazer as exigências legais.",
 "O inscrito no registro cadastral será classificado discricionariamente pela comissão, sem regras objetivas divulgadas; receberá certificado de validade indeterminada, e seu registro não poderá ser alterado, suspenso ou cancelado após a inscrição.",
 "Art. 88, §§ 1º, 2º e 5º.","classificação discricionária","t30c")
P("T30",["88"],"conceito_correto","troca_efeito",4,
 "O interessado que requerer o cadastro poderá participar de processo licitatório até a decisão da Administração, e a celebração do contrato ficará condicionada à emissão do certificado de registro cadastral.",
 "O interessado que requerer o cadastro somente poderá participar de processo licitatório após a decisão da Administração, mas a celebração do contrato independe da emissão do certificado de registro cadastral.",
 "Art. 88, § 6º.","inverte participação e contrato","t30d")
# T31
P("T31",["89"],"conceito_correto","excecao_omitida",3,
 "Os contratos regulados pela Lei n.º 14.133/2021 regular-se-ão pelas suas cláusulas e pelos preceitos de direito público, aplicando-se-lhes, supletivamente, os princípios da teoria geral dos contratos e as disposições de direito privado.",
 "Os contratos regulados pela Lei n.º 14.133/2021 regular-se-ão exclusivamente pelas disposições de direito privado, aplicando-se-lhes, supletivamente, os preceitos de direito público.",
 "Art. 89, caput.","inverte regime jurídico","t31a")
P("T31",["89"],"conceito_correto","excecao_omitida",3,
 "Todo contrato deverá mencionar os nomes das partes e os de seus representantes, a finalidade, o ato que autorizou sua lavratura, o número do processo da licitação ou da contratação direta e a sujeição dos contratantes às normas da lei e às cláusulas contratuais.",
 "O contrato dispensa a menção ao ato que autorizou sua lavratura e ao número do processo da licitação ou da contratação direta, bastando a identificação das partes e do objeto.",
 "Art. 89, § 1º.","dispensa menções","t31b")
P("T31",["90"],"conceito_correto","troca_numero",4,
 "A Administração convocará regularmente o licitante vencedor para assinar o termo de contrato ou para aceitar ou retirar o instrumento equivalente, dentro do prazo e nas condições estabelecidas no edital, sob pena de decair o direito à contratação, sem prejuízo das sanções legais; o prazo de convocação poderá ser prorrogado 1 vez, por igual período, mediante solicitação da parte durante seu transcurso, devidamente justificada, e desde que o motivo seja aceito pela Administração.",
 "A Administração convocará o licitante vencedor para assinar o termo de contrato no prazo de 5 dias úteis, fixado em lei, sob pena de decair o direito à contratação; o prazo poderá ser prorrogado por até 3 vezes, mediante solicitação da parte, independentemente de aceitação da Administração.",
 "Art. 90, caput e § 1º.","fixa prazo e prorrogações","t31c")
P("T31",["90"],"conceito_correto","excecao_omitida",4,
 "Quando o convocado não assinar o termo de contrato ou não aceitar ou retirar o instrumento equivalente no prazo e nas condições estabelecidas, é facultado à Administração convocar os licitantes remanescentes, na ordem de classificação, para a celebração do contrato nas condições propostas pelo licitante vencedor.",
 "Quando o convocado não assinar o termo de contrato no prazo estabelecido, a Administração é obrigada a revogar a licitação, sendo vedada a convocação dos licitantes remanescentes.",
 "Art. 90, § 2º.","obriga revogação","t31d")
P("T31",["90"],"conceito_correto","excecao_omitida",5,
 "Se nenhum dos licitantes remanescentes aceitar a contratação nas condições do vencedor, a Administração, observados o valor estimado e sua eventual atualização nos termos do edital, poderá convocá-los para negociação, na ordem de classificação, com vistas à obtenção de preço melhor, mesmo que acima do preço do adjudicatário, e adjudicar e celebrar o contrato nas condições ofertadas pelos remanescentes quando frustrada a negociação de melhor condição.",
 "Se nenhum dos licitantes remanescentes aceitar a contratação nas condições do vencedor, a Administração deverá obrigatoriamente realizar nova licitação, sendo vedada a negociação de preço acima do ofertado pelo adjudicatário.",
 "Art. 90, § 4º, I e II.","veda negociação","t31e")
P("T31",["90"],"conceito_correto","troca_efeito",5,
 "A recusa injustificada do adjudicatário em assinar o contrato ou em aceitar ou retirar o instrumento equivalente no prazo estabelecido caracterizará o descumprimento total da obrigação assumida e o sujeitará às penalidades legais e à imediata perda da garantia de proposta; essa regra não se aplica aos licitantes remanescentes convocados para negociação com vistas a preço melhor.",
 "A recusa injustificada do adjudicatário em assinar o contrato caracterizará descumprimento parcial da obrigação, sem perda da garantia de proposta; a regra aplica-se igualmente aos licitantes remanescentes convocados para negociação com vistas a preço melhor.",
 "Art. 90, §§ 5º e 6º.","descumprimento parcial e extensão","t31f")
P("T31",["90"],"conceito_correto","excecao_omitida",4,
 "Decorrido o prazo de validade da proposta indicado no edital sem convocação para a contratação, ficarão os licitantes liberados dos compromissos assumidos; é facultada à Administração a convocação dos demais licitantes classificados para a contratação de remanescente de obra, serviço ou fornecimento em consequência de rescisão contratual.",
 "Decorrido o prazo de validade da proposta indicado no edital sem convocação para a contratação, os licitantes permanecerão vinculados até a efetiva assinatura do contrato; é vedada a convocação de licitantes classificados para contratação de remanescente em consequência de rescisão contratual.",
 "Art. 90, §§ 3º e 7º.","mantém vinculação e veda remanescente","t31g")
P("T31",["91"],"conceito_correto","excecao_omitida",3,
 "Os contratos e seus aditamentos terão forma escrita e serão juntados ao processo que tiver dado origem à contratação, divulgados e mantidos à disposição do público em sítio eletrônico oficial; admite-se o sigilo quando imprescindível à segurança da sociedade e do Estado, nos termos da legislação de acesso à informação.",
 "Os contratos e seus aditamentos poderão ser verbais quando de pequeno valor e terão sigilo como regra até o término da execução, divulgando-se apenas o extrato ao final.",
 "Art. 91, caput e § 1º.","admite forma verbal e sigilo como regra","t31h")
P("T31",["91"],"conceito_correto","troca_autoridade",4,
 "Contratos relativos a direitos reais sobre imóveis serão formalizados por escritura pública lavrada em notas de tabelião, cujo teor deverá ser divulgado e mantido à disposição do público em sítio eletrônico oficial; será admitida a forma eletrônica na celebração de contratos e termos aditivos, atendidas as exigências do regulamento.",
 "Contratos relativos a direitos reais sobre imóveis serão formalizados por termo administrativo lavrado pela própria Administração, vedada a forma eletrônica na celebração de contratos e termos aditivos.",
 "Art. 91, §§ 2º e 3º.","troca escritura por termo","t31i")
P("T31",["91"],"conceito_correto","excecao_omitida",4,
 "Antes de formalizar ou prorrogar o prazo de vigência do contrato, a Administração deverá verificar a regularidade fiscal do contratado, consultar o Ceis e o Cnep, emitir as certidões negativas de inidoneidade, de impedimento e de débitos trabalhistas e juntá-las ao respectivo processo.",
 "Antes de formalizar o contrato, a Administração deverá verificar a regularidade fiscal do contratado, sendo dispensada tal verificação e a consulta ao Ceis e ao Cnep por ocasião da prorrogação do prazo de vigência.",
 "Art. 91, § 4º.","dispensa na prorrogação","t31j")
