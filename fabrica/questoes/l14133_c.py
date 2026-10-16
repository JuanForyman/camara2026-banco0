# Lei 14.133/2021 — lote L7 parte c (arts. 42 a 60)
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
# T13
P("T13",["42"],"conceito_correto","excecao_omitida",4,
 "A prova de qualidade de produto apresentado como similar ao das marcas indicadas no edital será admitida por comprovação de conformidade com normas técnicas oficiais, da ABNT ou de entidade credenciada pelo Inmetro, por declaração de atendimento satisfatório emitida por outro órgão de nível federativo equivalente ou superior, ou por certificação ou laudo laboratorial emitido por instituição oficial ou entidade credenciada.",
 "A prova de qualidade de produto apresentado como similar ao das marcas indicadas no edital será admitida exclusivamente por declaração do próprio fabricante, sendo vedada a utilização de laudo laboratorial ou de declaração emitida por outro órgão adquirente do produto.",
 "Art. 42, I a III.","restringe meios de prova","t13a")
P("T13",["42"],"conceito_correto","troca_autoridade",4,
 "A Administração poderá, nos termos do edital, oferecer protótipo do objeto pretendido e exigir, na fase de julgamento das propostas, amostras do licitante provisoriamente vencedor, para atender a diligência ou, após o julgamento, como condição para firmar contrato; as amostras poderão ser examinadas por instituição com reputação ético-profissional na especialidade do objeto, previamente indicada no edital.",
 "A Administração poderá exigir, na fase de julgamento das propostas, amostras de todos os licitantes, ainda que o edital seja omisso, e as amostras serão necessariamente examinadas pela própria Administração, vedado o exame por instituição externa.",
 "Art. 42, §§ 2º e 3º.","estende a todos e veda instituição externa","t13b")
P("T13",["43"],"conceito_correto","excecao_omitida",3,
 "O processo de padronização deverá conter parecer técnico sobre o produto, despacho motivado da autoridade superior com a adoção do padrão e síntese da justificativa e descrição sucinta do padrão definido, divulgadas em sítio eletrônico oficial; é permitida a padronização com base em processo de outro órgão ou entidade de nível federativo igual ou superior, mediante ato motivado.",
 "O processo de padronização dispensa parecer técnico sobre o produto, bastando despacho da autoridade superior, e não é permitida a padronização com base em processo de outro órgão ou entidade, ainda que de nível federativo superior.",
 "Art. 43, caput e § 1º.","dispensa parecer e veda padrão de outro órgão","t13c")
P("T13",["44"],"conceito_correto","troca_efeito",3,
 "Quando houver a possibilidade de compra ou de locação de bens, o estudo técnico preliminar deverá considerar os custos e os benefícios de cada opção, com indicação da alternativa mais vantajosa.",
 "Quando houver a possibilidade de compra ou de locação de bens, a Administração deverá optar pela compra, dispensado o estudo dos custos e benefícios de cada opção.",
 "Art. 44.","impõe a compra","t13d")
P("T13",["45"],"conceito_correto","excecao_omitida",3,
 "As licitações de obras e serviços de engenharia devem respeitar, especialmente, as normas relativas à disposição final ambientalmente adequada dos resíduos sólidos, à mitigação por condicionantes e compensação ambiental, à redução do consumo de energia e de recursos naturais, à avaliação de impacto de vizinhança, à proteção do patrimônio histórico, cultural, arqueológico e imaterial e à acessibilidade.",
 "As licitações de obras e serviços de engenharia devem respeitar, especialmente, as normas relativas à disposição final dos resíduos sólidos e à avaliação de impacto de vizinhança, ficando as normas de acessibilidade e de proteção do patrimônio histórico e cultural restritas às obras de grande vulto.",
 "Art. 45, I a VI.","restringe aos de grande vulto","t13e")
# T14
P("T14",["46"],"conceito_correto","troca_numero",3,
 "Na execução indireta de obras e serviços de engenharia, são admitidos os regimes de empreitada por preço unitário, empreitada por preço global, empreitada integral, contratação por tarefa, contratação integrada, contratação semi-integrada e fornecimento e prestação de serviço associado.",
 "Na execução indireta de obras e serviços de engenharia, são admitidos os regimes de empreitada por preço unitário, empreitada por preço global, empreitada integral, contratação por tarefa, contratação integrada, contratação semi-integrada, administração contratada e fornecimento e prestação de serviço associado.",
 "Art. 46, I a VII.","inclui regime inexistente","t14a")
P("T14",["46"],"conceito_correto","excecao_omitida",3,
 "É vedada a realização de obras e serviços de engenharia sem projeto executivo, ressalvada a hipótese em que, para obras e serviços comuns de engenharia, se demonstre a inexistência de prejuízo para a aferição dos padrões de desempenho e qualidade e a especificação seja feita apenas em termo de referência ou projeto básico.",
 "É vedada a realização de obras e serviços de engenharia sem projeto básico, sem qualquer ressalva, ainda que no regime de contratação integrada, em que o contratado apenas executa a obra.",
 "Art. 46, § 1º, c/c art. 18, § 3º.","nega exceção","t14b")
P("T14",["46"],"conceito_correto","confusao_instituto",4,
 "A Administração é dispensada da elaboração de projeto básico nos casos de contratação integrada, hipótese em que deverá ser elaborado anteprojeto de acordo com metodologia definida em ato do órgão competente; após a elaboração do projeto básico pelo contratado, o conjunto de desenhos, especificações, memoriais e cronograma físico-financeiro deverá ser submetido à aprovação da Administração.",
 "A Administração é dispensada da elaboração de projeto executivo nos casos de contratação integrada, hipótese em que deverá ser elaborado projeto básico completo; após a elaboração do projeto executivo pelo contratado, a aprovação da Administração é dispensada.",
 "Art. 46, §§ 2º e 3º.","troca projeto básico e executivo","t14c")
P("T14",["46"],"conceito_correto","troca_efeito",4,
 "Na contratação semi-integrada, mediante prévia autorização da Administração, o projeto básico poderá ser alterado, desde que demonstrada a superioridade das inovações propostas pelo contratado em termos de redução de custos, aumento da qualidade, redução do prazo de execução ou facilidade de manutenção ou operação, assumindo o contratado a responsabilidade integral pelos riscos associados à alteração do projeto básico.",
 "Na contratação semi-integrada, o contratado poderá alterar o projeto básico por iniciativa própria, sem prévia autorização da Administração, que assumirá os riscos associados à alteração, desde que haja redução de custos.",
 "Art. 46, § 5º.","dispensa autorização e transfere risco","t14d")
P("T14",["46"],"conceito_correto","excecao_omitida",5,
 "Os regimes de execução de empreitada por preço global, empreitada integral, contratação por tarefa, contratação integrada e contratação semi-integrada serão licitados por preço global e adotarão sistemática de medição e pagamento associada à execução de etapas do cronograma físico-financeiro vinculadas ao cumprimento de metas de resultado, vedada a adoção de sistemática de remuneração orientada por preços unitários.",
 "Os regimes de execução de empreitada por preço global, empreitada integral, contratação por tarefa, contratação integrada e contratação semi-integrada serão licitados por preço unitário e adotarão sistemática de medição e pagamento baseada na execução de quantidades de itens unitários.",
 "Art. 46, § 9º.","inverte sistemática de medição","t14e")
P("T14",["46"],"conceito_correto","troca_autoridade",3,
 "Nos regimes de contratação integrada e semi-integrada, o edital e o contrato, sempre que for o caso, deverão prever as providências necessárias para a efetivação de desapropriação autorizada pelo poder público, incluindo o responsável por cada fase do procedimento expropriatório e a responsabilidade pelo pagamento das indenizações devidas; a execução de cada etapa será obrigatoriamente precedida da conclusão e da aprovação, pela autoridade competente, dos trabalhos relativos às etapas anteriores.",
 "Nos regimes de contratação integrada e semi-integrada, a desapropriação é de responsabilidade exclusiva do contratado, não precisando o edital e o contrato prever as providências para sua efetivação; as etapas da execução poderão ser iniciadas independentemente da aprovação das etapas anteriores.",
 "Art. 46, §§ 4º e 6º.","transfere desapropriação ao contratado","t14f")
P("T14",["47"],"conceito_correto","excecao_omitida",3,
 "As licitações de serviços atenderão aos princípios da padronização e do parcelamento, quando tecnicamente viável e economicamente vantajoso; na aplicação do parcelamento serão considerados a responsabilidade técnica, o custo para a Administração de vários contratos frente às vantagens da redução de custos com divisão do objeto em itens e o dever de buscar a ampliação da competição e de evitar a concentração de mercado.",
 "As licitações de serviços atenderão ao princípio do parcelamento em todos os casos, sem consideração da responsabilidade técnica ou dos custos para a Administração de vários contratos, vedada a padronização de serviços.",
 "Art. 47, caput e § 1º.","torna parcelamento absoluto","t14g")
# T15
P("T15",["48"],"conceito_correto","excecao_omitida",4,
 "Poderão ser objeto de execução por terceiros as atividades materiais acessórias, instrumentais ou complementares aos assuntos que constituam área de competência legal do órgão ou da entidade, vedado à Administração, na contratação do serviço terceirizado, indicar pessoas expressamente nominadas para executar o objeto, fixar salário inferior ao definido em lei ou ato normativo e estabelecer vínculo de subordinação com funcionário da empresa prestadora.",
 "Poderão ser objeto de execução por terceiros as atividades que constituam área de competência legal do órgão ou da entidade, admitido à Administração, na contratação do serviço terceirizado, indicar pessoas nominadas para executar o objeto, desde que respeitado o salário definido em lei, e estabelecer vínculo de subordinação com funcionário da empresa prestadora.",
 "Art. 48, caput, I a III.","admite indicação nominal e subordinação","t15a")
P("T15",["48"],"conceito_correto","excecao_omitida",4,
 "Durante a vigência do contrato, é vedado ao contratado contratar cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, de dirigente do órgão ou entidade contratante ou de agente público que desempenhe função na licitação ou atue na fiscalização ou na gestão do contrato, devendo essa proibição constar expressamente do edital de licitação.",
 "Durante a vigência do contrato, é vedado ao contratado contratar cônjuge, companheiro ou parente em linha reta até o segundo grau de dirigente do órgão ou entidade contratante, não alcançando a vedação os parentes de agentes públicos que atuem na fiscalização ou na gestão do contrato.",
 "Art. 48, parágrafo único.","reduz grau e abrangência","t15b")
P("T15",["49"],"conceito_correto","excecao_omitida",4,
 "A Administração poderá, mediante justificativa expressa, contratar mais de uma empresa ou instituição para executar o mesmo serviço, desde que essa contratação não implique perda de economia de escala, quando o objeto puder ser executado de forma concorrente e simultânea por mais de um contratado e a múltipla execução for conveniente para atender à Administração, mantendo o controle individualizado da execução relativamente a cada contratado.",
 "A Administração poderá contratar mais de uma empresa para executar o mesmo serviço, independentemente de justificativa e ainda que haja perda de economia de escala, dispensado o controle individualizado da execução relativamente a cada contratado.",
 "Art. 49, caput e parágrafo único.","dispensa justificativa e controle","t15c")
P("T15",["50"],"conceito_correto","excecao_omitida",3,
 "Nas contratações de serviços com regime de dedicação exclusiva de mão de obra, o contratado deverá apresentar, quando solicitado pela Administração, sob pena de multa, comprovação do cumprimento das obrigações trabalhistas e com o FGTS em relação aos empregados diretamente envolvidos na execução do contrato, em especial quanto a registro de ponto, recibo de pagamento de salários, comprovante de depósito do FGTS e recibo de férias.",
 "Nas contratações de serviços com regime de dedicação exclusiva de mão de obra, a comprovação do cumprimento das obrigações trabalhistas e com o FGTS será exigida do contratado apenas ao final do contrato, sem previsão de multa pelo descumprimento.",
 "Art. 50.","exige só ao final e sem multa","t15d")
P("T15",["51"],"conceito_correto","excecao_omitida",3,
 "Ressalvado o disposto no inciso V do caput do art. 74 da Lei, a locação de imóveis deverá ser precedida de licitação e avaliação prévia do bem, do seu estado de conservação, dos custos de adaptações e do prazo de amortização dos investimentos necessários.",
 "A locação de imóveis pela Administração será sempre precedida de licitação, não se admitindo contratação direta em nenhuma hipótese, e dispensa avaliação prévia do estado de conservação do bem.",
 "Art. 51.","nega exceção do art. 74, V","t15e")
P("T15",["52"],"conceito_correto","troca_efeito",4,
 "Nas licitações de âmbito internacional, quando for permitido ao licitante estrangeiro cotar preço em moeda estrangeira, o licitante brasileiro igualmente poderá fazê-lo, e o pagamento feito ao licitante brasileiro eventualmente contratado será efetuado em moeda corrente nacional.",
 "Nas licitações de âmbito internacional, quando for permitido ao licitante estrangeiro cotar preço em moeda estrangeira, o licitante brasileiro não poderá fazê-lo, e o pagamento feito ao licitante brasileiro será efetuado na moeda da cotação.",
 "Art. 52, §§ 1º e 2º.","inverte regras de moeda","t15f")
P("T15",["52"],"conceito_correto","excecao_omitida",4,
 "Nas licitações internacionais, o edital não poderá prever condições de habilitação, classificação e julgamento que constituam barreiras de acesso ao licitante estrangeiro, admitida a previsão de margem de preferência para bens produzidos no País e serviços nacionais que atendam às normas técnicas brasileiras, e as garantias de pagamento ao licitante brasileiro serão equivalentes àquelas oferecidas ao licitante estrangeiro.",
 "Nas licitações internacionais, o edital poderá prever condições de habilitação mais rigorosas para o licitante estrangeiro, vedada a margem de preferência para bens produzidos no País, e as garantias de pagamento ao licitante brasileiro poderão ser inferiores às oferecidas ao estrangeiro.",
 "Art. 52, §§ 3º e 6º.","admite barreiras ao estrangeiro","t15g")
# T16
P("T16",["53"],"conceito_correto","troca_autoridade",3,
 "Ao final da fase preparatória, o processo licitatório seguirá para o órgão de assessoramento jurídico da Administração, que realizará controle prévio de legalidade mediante análise jurídica da contratação, redigindo sua manifestação em linguagem simples e compreensível, de forma clara e objetiva, com exposição dos pressupostos de fato e de direito levados em consideração.",
 "Ao final da fase de julgamento, o processo licitatório seguirá para o órgão de controle externo, que realizará controle prévio de legalidade mediante análise técnica da contratação, redigindo sua manifestação em linguagem técnica, sem necessidade de exposição dos pressupostos de fato e de direito.",
 "Art. 53, caput e § 1º, II.","troca momento e órgão","t16a")
P("T16",["53"],"conceito_correto","excecao_omitida",4,
 "O órgão de assessoramento jurídico também realizará controle prévio de legalidade de contratações diretas, acordos, termos de cooperação, convênios, ajustes, adesões a atas de registro de preços, outros instrumentos congêneres e de seus termos aditivos; é dispensável a análise jurídica nas hipóteses previamente definidas em ato da autoridade jurídica máxima competente, considerados o baixo valor, a baixa complexidade da contratação, a entrega imediata do bem ou a utilização de minutas padronizadas.",
 "O controle prévio de legalidade pelo órgão de assessoramento jurídico restringe-se às licitações, não alcançando as contratações diretas e as adesões a atas de registro de preços; a análise jurídica é obrigatória em todas as contratações, inclusive as de baixo valor e as que utilizem minutas padronizadas.",
 "Art. 53, §§ 4º e 5º.","restringe controle e veda dispensa","t16b")
P("T16",["54"],"conceito_correto","troca_autoridade",3,
 "A publicidade do edital de licitação será realizada mediante divulgação e manutenção do inteiro teor do ato convocatório e de seus anexos no Portal Nacional de Contratações Públicas (PNCP); sem prejuízo disso, é obrigatória a publicação de extrato do edital no Diário Oficial do ente federativo, bem como em jornal diário de grande circulação.",
 "A publicidade do edital de licitação será realizada mediante divulgação do inteiro teor do ato convocatório exclusivamente em sítio eletrônico do órgão licitante, sendo facultativa a divulgação no Portal Nacional de Contratações Públicas (PNCP) e dispensada a publicação de extrato em jornal diário de grande circulação.",
 "Art. 54, caput e § 1º.","troca PNCP por sítio e facultativiza jornal","t16c",["vigencia_alterada"])
P("T16",["54"],"conceito_correto","excecao_omitida",4,
 "É facultada a divulgação adicional do inteiro teor do edital e de seus anexos em sítio eletrônico oficial do ente federativo, admitida a divulgação direta a interessados devidamente cadastrados; após a homologação, serão disponibilizados no PNCP os documentos elaborados na fase preparatória que porventura não tenham integrado o edital e seus anexos.",
 "É vedada a divulgação adicional do inteiro teor do edital em sítio eletrônico oficial do ente federativo e a divulgação direta a interessados cadastrados; os documentos da fase preparatória que não integrarem o edital permanecerão em sigilo mesmo após a homologação.",
 "Art. 54, §§ 2º e 3º.","veda divulgação adicional e mantém sigilo","t16d")
# T17
P("T17",["55"],"conceito_correto","troca_numero",4,
 "Os prazos mínimos para apresentação de propostas e lances, contados a partir da divulgação do edital, são de 8 dias úteis para aquisição de bens quando adotado o critério de menor preço ou maior desconto e de 15 dias úteis nas demais hipóteses de aquisição de bens.",
 "Os prazos mínimos para apresentação de propostas e lances, contados a partir da divulgação do edital, são de 5 dias úteis para aquisição de bens quando adotado o critério de menor preço ou maior desconto e de 10 dias úteis nas demais hipóteses de aquisição de bens.",
 "Art. 55, I, a e b.","reduz prazos","t17a",["texto_complementado_por_conhecimento"])
P("T17",["55"],"conceito_correto","troca_numero",4,
 "No caso de serviços e obras, o prazo mínimo para apresentação de propostas é de 10 dias úteis para serviços comuns e obras e serviços comuns de engenharia, de 25 dias úteis para serviços especiais e obras e serviços especiais de engenharia, de 60 dias úteis na contratação integrada e de 35 dias úteis na semi-integrada.",
 "No caso de serviços e obras, o prazo mínimo para apresentação de propostas é de 15 dias úteis para serviços comuns e obras e serviços comuns de engenharia, de 35 dias úteis para serviços especiais e obras e serviços especiais de engenharia, de 25 dias úteis na contratação integrada e de 60 dias úteis na semi-integrada.",
 "Art. 55, II, a a d.","embaralha prazos","t17b",["texto_complementado_por_conhecimento"])
P("T17",["55"],"conceito_correto","troca_numero",4,
 "Na licitação em que se adote o critério de julgamento de maior lance, o prazo mínimo para apresentação de propostas e lances é de 15 dias úteis; adotado o critério de técnica e preço ou de melhor técnica ou conteúdo artístico, o prazo mínimo é de 35 dias úteis.",
 "Na licitação em que se adote o critério de julgamento de maior lance, o prazo mínimo para apresentação de propostas e lances é de 35 dias úteis; adotado o critério de técnica e preço ou de melhor técnica ou conteúdo artístico, o prazo mínimo é de 15 dias úteis.",
 "Art. 55, III e IV.","inverte prazos","t17c")
P("T17",["55"],"conceito_correto","troca_efeito",4,
 "Eventuais modificações no edital implicarão nova divulgação na mesma forma de sua divulgação inicial, além do cumprimento dos mesmos prazos dos atos e procedimentos originais, exceto quando a alteração não comprometer a formulação das propostas; os prazos poderão, mediante decisão fundamentada, ser reduzidos até a metade nas licitações do Ministério da Saúde, no âmbito do SUS.",
 "Eventuais modificações no edital dispensam nova divulgação e reabertura de prazos, ainda que comprometam a formulação das propostas; os prazos poderão ser reduzidos até a metade em qualquer licitação, a critério do agente de contratação.",
 "Art. 55, §§ 1º e 2º.","dispensa nova divulgação","t17d")
P("T17",["56"],"conceito_correto","excecao_omitida",4,
 "O modo de disputa poderá ser, isolada ou conjuntamente, aberto, com lances públicos e sucessivos, crescentes ou decrescentes, ou fechado, com propostas em sigilo até a data e hora designadas para sua divulgação; a utilização isolada do modo fechado é vedada quando adotados os critérios de menor preço ou maior desconto, e a utilização do modo aberto é vedada quando adotado o critério de técnica e preço.",
 "O modo de disputa poderá ser, exclusivamente, aberto ou fechado, vedada a utilização conjunta; a utilização isolada do modo fechado é obrigatória quando adotados os critérios de menor preço ou maior desconto, e a utilização do modo aberto é obrigatória no critério de técnica e preço.",
 "Art. 56, I e II e §§ 1º e 2º.","inverte vedações","t17e")
P("T17",["56"],"conceito_correto","troca_numero",4,
 "Após a definição da melhor proposta, se a diferença em relação à proposta classificada em segundo lugar for de pelo menos 5%, a Administração poderá admitir o reinício da disputa aberta, nos termos estabelecidos no instrumento convocatório, para a definição das demais colocações.",
 "Após a definição da melhor proposta, se a diferença em relação à proposta classificada em segundo lugar for de pelo menos 10%, a Administração deverá reiniciar a disputa aberta, independentemente de previsão no instrumento convocatório, para a definição da melhor proposta.",
 "Art. 56, § 4º.","troca percentual e obrigatoriedade","t17f")
P("T17",["57"],"conceito_correto","excecao_omitida",3,
 "O edital de licitação poderá estabelecer intervalo mínimo de diferença de valores entre os lances, que incidirá tanto em relação aos lances intermediários quanto em relação à proposta que cobrir a melhor oferta.",
 "O edital de licitação não poderá estabelecer intervalo mínimo de diferença de valores entre os lances, para não restringir a competitividade, mas poderá fixá-lo em relação à proposta que cobrir a melhor oferta.",
 "Art. 57.","veda intervalo mínimo","t17g")
P("T17",["58"],"conceito_correto","troca_numero",4,
 "Poderá ser exigida, no momento da apresentação da proposta, a comprovação do recolhimento de quantia a título de garantia de proposta, como requisito de pré-habilitação, que não poderá ser superior a 1% do valor estimado para a contratação e será devolvida aos licitantes no prazo de 10 dias úteis, contado da assinatura do contrato ou da data em que for declarada fracassada a licitação.",
 "Poderá ser exigida, no momento da apresentação da proposta, a comprovação do recolhimento de quantia a título de garantia de proposta, como requisito de habilitação, que não poderá ser superior a 5% do valor estimado para a contratação e será devolvida aos licitantes no prazo de 30 dias corridos, contado da homologação.",
 "Art. 58, caput e §§ 1º e 2º.","troca percentual e prazo","t17h")
P("T17",["58"],"conceito_correto","troca_efeito",4,
 "Implicará execução do valor integral da garantia de proposta a recusa em assinar o contrato ou a não apresentação dos documentos para a contratação, e a garantia de proposta poderá ser prestada nas modalidades previstas para a garantia contratual, como caução em dinheiro, seguro-garantia e fiança bancária.",
 "Implicará execução de metade do valor da garantia de proposta a recusa em assinar o contrato, e a garantia de proposta somente poderá ser prestada em dinheiro, vedadas as modalidades de seguro-garantia e fiança bancária.",
 "Art. 58, §§ 3º e 4º.","reduz execução e restringe modalidades","t17i")
# T18
P("T18",["59"],"conceito_correto","excecao_omitida",3,
 "Serão desclassificadas as propostas que contiverem vícios insanáveis, não obedecerem às especificações técnicas pormenorizadas no edital, apresentarem preços inexequíveis ou permanecerem acima do orçamento estimado, não tiverem sua exequibilidade demonstrada, quando exigido pela Administração, ou apresentarem desconformidade insanável com outras exigências do edital.",
 "Serão desclassificadas as propostas que contiverem qualquer vício, ainda que sanável, e as que apresentarem preços acima do orçamento estimado, ficando vedado à Administração exigir que o licitante demonstre a exequibilidade de sua proposta.",
 "Art. 59, I a V.","desclassifica vício sanável e veda diligência","t18a")
P("T18",["59"],"conceito_correto","troca_numero",4,
 "No caso de obras e serviços de engenharia, serão consideradas inexequíveis as propostas cujos valores forem inferiores a 75% do valor orçado pela Administração; e será exigida garantia adicional do licitante vencedor cuja proposta for inferior a 85% do valor orçado, equivalente à diferença entre este último e o valor da proposta.",
 "No caso de obras e serviços de engenharia, serão consideradas inexequíveis as propostas cujos valores forem inferiores a 85% do valor orçado pela Administração; e será exigida garantia adicional do licitante vencedor cuja proposta for inferior a 75% do valor orçado, equivalente à diferença entre este último e o valor da proposta.",
 "Art. 59, §§ 4º e 5º.","inverte 75% e 85%","t18b")
P("T18",["59"],"conceito_correto","excecao_omitida",3,
 "A verificação da conformidade das propostas poderá ser feita exclusivamente em relação à proposta mais bem classificada, e a Administração poderá realizar diligências para aferir a exequibilidade das propostas ou exigir dos licitantes que ela seja demonstrada.",
 "A verificação da conformidade das propostas deverá ser feita em relação a todas as propostas apresentadas, e a Administração não poderá realizar diligências para aferir a exequibilidade das propostas.",
 "Art. 59, §§ 1º e 2º.","exige verificação de todas","t18c")
P("T18",["60"],"conceito_correto","troca_numero",4,
 "Em caso de empate entre duas ou mais propostas, serão utilizados os seguintes critérios de desempate, nesta ordem: disputa final, avaliação do desempenho contratual prévio dos licitantes, desenvolvimento pelo licitante de ações de equidade entre homens e mulheres no ambiente de trabalho e desenvolvimento pelo licitante de programa de integridade.",
 "Em caso de empate entre duas ou mais propostas, serão utilizados os seguintes critérios de desempate, nesta ordem: sorteio, desenvolvimento pelo licitante de programa de integridade, avaliação do desempenho contratual prévio dos licitantes e ações de equidade entre homens e mulheres no ambiente de trabalho.",
 "Art. 60, I a IV.","troca a ordem do desempate","t18d")
P("T18",["60"],"conceito_correto","troca_efeito",4,
 "Em igualdade de condições, se não houver desempate pelos critérios do art. 60, será assegurada preferência, sucessivamente, aos bens e serviços produzidos ou prestados por empresas estabelecidas no território do Estado ou do Distrito Federal do órgão licitante, por empresas brasileiras, por empresas que invistam em pesquisa e desenvolvimento de tecnologia no País e por empresas que comprovem a prática de mitigação nos termos da Lei n.º 12.187/2009; tais regras não prejudicam a aplicação do art. 44 da LC n.º 123/2006.",
 "Em igualdade de condições, se não houver desempate pelos critérios do art. 60, será assegurada preferência, sucessivamente, às empresas brasileiras, às empresas estabelecidas no território do Estado do órgão licitante e às empresas que invistam em pesquisa; tais regras afastam a aplicação do art. 44 da LC n.º 123/2006.",
 "Art. 60, § 1º e § 2º.","inverte ordem e afasta LC 123","t18e")
