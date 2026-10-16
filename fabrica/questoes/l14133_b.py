# Lei 14.133/2021 — lote L7 parte b (arts. 23 a 41)
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
# T07
P("T07",["23"],"conceito_correto","troca_numero",4,
 "No processo licitatório para aquisição de bens e contratação de serviços em geral, o valor estimado será definido com base no melhor preço aferido por meio de parâmetros adotados de forma combinada ou não, entre os quais a pesquisa direta com no mínimo 3 fornecedores, mediante solicitação formal de cotação, desde que não tenham sido obtidos os orçamentos com mais de 6 meses de antecedência da data de divulgação do edital.",
 "No processo licitatório para aquisição de bens e contratação de serviços em geral, o valor estimado será definido com base no melhor preço aferido por meio de parâmetros adotados de forma combinada ou não, entre os quais a pesquisa direta com no mínimo 5 fornecedores, desde que não tenham sido obtidos os orçamentos com mais de 12 meses de antecedência da data de divulgação do edital.",
 "Art. 23, § 1º, IV.","troca número de fornecedores e prazo","t07a")
P("T07",["23"],"conceito_correto","troca_efeito",4,
 "Para contratação de obras e serviços de engenharia, o valor estimado, acrescido do percentual de BDI de referência e dos Encargos Sociais cabíveis, será definido por meio de parâmetros na seguinte ordem: composição de custos unitários menores ou iguais à mediana do Sicro ou do Sinapi, dados de pesquisa publicada em mídia especializada, contratações similares da Administração e pesquisa na base nacional de notas fiscais eletrônicas.",
 "Para contratação de obras e serviços de engenharia, o valor estimado, acrescido do percentual de BDI de referência, será definido por meio de parâmetros adotados livremente, em qualquer ordem, dispensada a utilização do Sicro e do Sinapi, que se restringem às contratações de bens e serviços em geral.",
 "Art. 23, § 2º, I a IV.","afasta ordem e sistemas de custos","t07b")
P("T07",["23"],"conceito_correto","excecao_omitida",4,
 "Nas contratações diretas por inexigibilidade ou por dispensa, quando não for possível estimar o valor do objeto na forma estabelecida nos §§ 1º, 2º e 3º do art. 23, o contratado deverá comprovar previamente que os preços estão em conformidade com os praticados em contratações semelhantes de objetos de mesma natureza, por meio da apresentação de notas fiscais emitidas para outros contratantes no período de até 1 ano anterior à data da contratação, ou por outro meio idôneo.",
 "Nas contratações diretas por inexigibilidade ou por dispensa, quando não for possível estimar o valor do objeto, o contratado fica dispensado de comprovar a compatibilidade dos preços, bastando declaração de que o valor praticado é compatível com o de mercado.",
 "Art. 23, § 4º.","dispensa comprovação","t07c")
P("T07",["23"],"conceito_correto","troca_autoridade",3,
 "Nas contratações realizadas por Municípios, Estados e Distrito Federal, desde que não envolvam recursos da União, o valor previamente estimado da contratação poderá ser definido por meio da utilização de outros sistemas de custos adotados pelo respectivo ente federativo.",
 "Nas contratações realizadas por Municípios, Estados e Distrito Federal, ainda que envolvam recursos da União, o valor previamente estimado da contratação poderá ser definido por outros sistemas de custos adotados pelo respectivo ente federativo.",
 "Art. 23, § 3º.","admite recursos da União","t07d")
P("T07",["24"],"conceito_correto","excecao_omitida",3,
 "Desde que justificado, o orçamento estimado da contratação poderá ter caráter sigiloso, sem prejuízo da divulgação do detalhamento dos quantitativos e das demais informações necessárias para a elaboração das propostas; o sigilo não prevalecerá para os órgãos de controle interno e externo.",
 "Desde que justificado, o orçamento estimado da contratação poderá ter caráter sigiloso, inclusive quanto aos quantitativos e às demais informações necessárias para a elaboração das propostas, e o sigilo prevalecerá também perante os órgãos de controle interno e externo.",
 "Art. 24, caput e I.","estende sigilo ao controle","t07e")
P("T07",["24"],"conceito_correto","troca_efeito",3,
 "Na licitação em que for adotado o critério de julgamento por maior desconto, o preço estimado ou o máximo aceitável constará do edital da licitação, ainda que a Administração tenha optado pelo orçamento sigiloso em outras hipóteses.",
 "Na licitação em que for adotado o critério de julgamento por maior desconto, o orçamento estimado será sempre sigiloso, não podendo o preço estimado ou o máximo aceitável constar do edital da licitação.",
 "Art. 24, parágrafo único.","inverte regra do maior desconto","t07f")
# T08
P("T08",["25"],"conceito_correto","excecao_omitida",3,
 "O edital deverá conter o objeto da licitação e as regras relativas à convocação, ao julgamento, à habilitação, aos recursos e às penalidades da licitação, à fiscalização e à gestão do contrato, à entrega do objeto e às condições de pagamento; todos os elementos do edital, incluídos minuta de contrato, termos de referência, anteprojeto e projetos, deverão ser divulgados em sítio eletrônico oficial na mesma data de divulgação do edital, sem necessidade de registro ou identificação para acesso.",
 "O edital deverá conter o objeto da licitação e as regras relativas à convocação, ao julgamento e à habilitação, ficando a divulgação da minuta de contrato, dos termos de referência e dos projetos condicionada ao registro prévio do interessado em sítio eletrônico oficial, após a publicação do edital.",
 "Art. 25, caput e § 3º.","exige registro e divulgação posterior","t08a")
P("T08",["25"],"conceito_correto","troca_numero",4,
 "Nas contratações de obras, serviços e fornecimentos de grande vulto, o edital deverá prever a obrigatoriedade de implantação de programa de integridade pelo licitante vencedor, no prazo de 6 meses, contado da celebração do contrato, conforme regulamento.",
 "Nas contratações de obras, serviços e fornecimentos de grande vulto, o edital poderá prever a implantação de programa de integridade pelo licitante vencedor, no prazo de 12 meses, contado da homologação da licitação, conforme regulamento.",
 "Art. 25, § 4º.","torna facultativo, troca prazo e marco","t08b")
P("T08",["25"],"conceito_correto","excecao_omitida",3,
 "O edital poderá prever a responsabilidade do contratado pela obtenção do licenciamento ambiental e pela realização da desapropriação autorizada pelo poder público, e os licenciamentos ambientais de obras e serviços de engenharia licitados nos termos da Lei terão prioridade de tramitação nos órgãos do Sisnama.",
 "O edital não poderá prever a responsabilidade do contratado pela obtenção do licenciamento ambiental nem pela realização da desapropriação autorizada pelo poder público, que são atribuições indelegáveis da Administração.",
 "Art. 25, §§ 5º e 6º.","veda transferência","t08c")
P("T08",["25"],"conceito_correto","troca_efeito",4,
 "Independentemente do prazo de duração do contrato, será obrigatória a previsão no edital de índice de reajustamento de preço, com data-base vinculada à data do orçamento estimado e com a possibilidade de ser estabelecido mais de um índice específico ou setorial.",
 "A previsão no edital de índice de reajustamento de preço será obrigatória somente nos contratos com duração superior a doze meses, com data-base vinculada à data da assinatura do contrato, vedada a adoção de mais de um índice.",
 "Art. 25, § 7º.","exige prazo mínimo e data-base distinta","t08d")
P("T08",["25"],"conceito_correto","confusao_instituto",4,
 "Nas licitações de serviços contínuos, observado o interregno mínimo de 1 ano, o critério de reajustamento será por reajustamento em sentido estrito, quando não houver regime de dedicação exclusiva de mão de obra ou predominância de mão de obra, ou por repactuação, quando houver, mediante demonstração analítica da variação dos custos.",
 "Nas licitações de serviços contínuos, observado o interregno mínimo de 1 ano, o critério de reajustamento será por repactuação, quando não houver regime de dedicação exclusiva de mão de obra, ou por reajustamento em sentido estrito, quando houver, mediante demonstração analítica da variação dos custos.",
 "Art. 25, § 8º, I e II.","troca reajuste e repactuação","t08e")
P("T08",["25"],"conceito_correto","excecao_omitida",3,
 "O edital poderá, na forma disposta em regulamento, exigir que percentual mínimo da mão de obra responsável pela execução do objeto da contratação seja constituído por mulheres vítimas de violência doméstica e por oriundos ou egressos do sistema prisional.",
 "O edital deverá, independentemente de regulamento, exigir que metade da mão de obra responsável pela execução do objeto da contratação seja constituída por mulheres vítimas de violência doméstica e por oriundos ou egressos do sistema prisional.",
 "Art. 25, § 9º.","torna obrigatório e fixa percentual","t08f")
# T09
P("T09",["26"],"conceito_correto","troca_numero",3,
 "No processo de licitação, poderá ser estabelecida margem de preferência para bens manufaturados e serviços nacionais que atendam a normas técnicas brasileiras e para bens reciclados, recicláveis ou biodegradáveis; a margem poderá ser de até 10% sobre o preço dos bens e serviços que não se enquadrem nessas hipóteses, e de até 20% para bens e serviços nacionais resultantes de desenvolvimento e inovação tecnológica no País.",
 "No processo de licitação, poderá ser estabelecida margem de preferência para bens manufaturados e serviços nacionais que atendam a normas técnicas brasileiras e para bens reciclados, recicláveis ou biodegradáveis; a margem poderá ser de até 20% sobre o preço dos bens e serviços que não se enquadrem nessas hipóteses, e de até 40% para bens e serviços nacionais resultantes de inovação tecnológica.",
 "Art. 26, caput, § 1º, II, e § 2º.","dobra os percentuais","t09a",["valor_atualizado_por_decreto"])
P("T09",["26"],"conceito_correto","troca_autoridade",3,
 "A margem de preferência para bens manufaturados e serviços nacionais que atendam a normas técnicas brasileiras será definida em decisão fundamentada do Poder Executivo federal, e poderá ser estendida a bens manufaturados e serviços originários de Estados Partes do Mercosul, desde que haja reciprocidade prevista em acordo internacional aprovado pelo Congresso Nacional e ratificado pelo Presidente da República.",
 "A margem de preferência para bens manufaturados e serviços nacionais que atendam a normas técnicas brasileiras será definida pelo agente de contratação em cada licitação, e é vedada a sua extensão a bens e serviços originários de Estados Partes do Mercosul.",
 "Art. 26, § 1º, I e III.","troca autoridade e veda Mercosul","t09b")
P("T09",["26"],"conceito_correto","excecao_omitida",4,
 "A margem de preferência não se aplica aos bens manufaturados nacionais e aos serviços nacionais se a capacidade de produção desses bens ou de prestação desses serviços no País for inferior à quantidade a ser adquirida ou contratada, ou aos quantitativos fixados em razão do parcelamento do objeto, quando for o caso.",
 "A margem de preferência aplica-se aos bens manufaturados nacionais e aos serviços nacionais mesmo que a capacidade de produção desses bens ou de prestação desses serviços no País seja inferior à quantidade a ser adquirida ou contratada.",
 "Art. 26, § 5º.","aplica margem sem capacidade","t09c")
P("T09",["26","27"],"conceito_correto","excecao_omitida",3,
 "Será divulgada, em sítio eletrônico oficial, a cada exercício financeiro, a relação de empresas favorecidas em decorrência da margem de preferência, com indicação do volume de recursos destinados a cada uma delas; os editais poderão exigir, mediante prévia justificativa, medidas de compensação comercial, industrial ou tecnológica.",
 "A relação de empresas favorecidas em decorrência da margem de preferência será mantida em sigilo no órgão contratante, divulgando-se apenas, a cada exercício, o volume total de recursos destinado às empresas favorecidas; as medidas de compensação comercial, industrial ou tecnológica são vedadas nos editais.",
 "Art. 26, § 6º, e art. 27.","sigilo e veda compensação","t09d")
# T10
P("T10",["28"],"conceito_correto","troca_numero",2,
 "São modalidades de licitação o pregão, a concorrência, o concurso, o leilão e o diálogo competitivo, sendo vedada a criação de outras modalidades de licitação ou, ainda, a combinação daquelas referidas na lei.",
 "São modalidades de licitação o pregão, a concorrência, o concurso, o leilão, o diálogo competitivo, a tomada de preços e o convite, sendo admitida a combinação entre elas quando motivada.",
 "Art. 28, caput e § 2º.","mantém modalidades extintas","t10a")
P("T10",["28"],"conceito_correto","confusao_instituto",3,
 "Além das modalidades de licitação, a Administração pode servir-se dos procedimentos auxiliares previstos no art. 78 da Lei, que não constituem modalidades de licitação.",
 "O credenciamento, a pré-qualificação e o sistema de registro de preços previstos no art. 78 da Lei constituem modalidades de licitação autônomas, que se somam ao pregão e à concorrência.",
 "Art. 28, § 1º, e art. 78.","trata auxiliares como modalidades","t10b")
P("T10",["29"],"conceito_correto","excecao_omitida",3,
 "A concorrência e o pregão seguem o rito procedimental comum, adotando-se o pregão sempre que o objeto possuir padrões de desempenho e qualidade que possam ser objetivamente definidos pelo edital; o pregão não se aplica às contratações de serviços técnicos especializados de natureza predominantemente intelectual e de obras e serviços de engenharia, exceto os serviços comuns de engenharia.",
 "A concorrência e o pregão seguem ritos procedimentais distintos, adotando-se o pregão sempre que o objeto for de menor valor; o pregão aplica-se a todas as obras e serviços de engenharia, inclusive os especiais, e aos serviços técnicos especializados de natureza intelectual.",
 "Art. 29, caput e parágrafo único.","troca rito e estende pregão","t10c")
P("T10",["30"],"conceito_correto","troca_efeito",3,
 "Nos concursos destinados à elaboração de projeto, o vencedor deverá ceder à Administração Pública todos os direitos patrimoniais relativos ao projeto e autorizar sua execução conforme juízo de conveniência e oportunidade das autoridades competentes; o edital do concurso indicará a qualificação exigida dos participantes, as diretrizes e formas de apresentação do trabalho e o prêmio ou a remuneração.",
 "Nos concursos destinados à elaboração de projeto, o vencedor conservará todos os direitos patrimoniais relativos ao projeto, sendo a execução condicionada à sua autorização; o edital do concurso indicará apenas o prêmio ou a remuneração.",
 "Art. 30, caput e parágrafo único.","mantém direitos patrimoniais","t10d")
P("T10",["31"],"conceito_correto","excecao_omitida",4,
 "O leilão poderá ser cometido a leiloeiro oficial ou a servidor designado pela autoridade competente; se optar por leiloeiro oficial, a Administração deverá selecioná-lo mediante credenciamento ou licitação na modalidade pregão e adotar o critério de julgamento de maior desconto para as comissões a serem cobradas, utilizados como parâmetro máximo os percentuais definidos na lei que regula a profissão.",
 "O leilão deverá ser cometido exclusivamente a leiloeiro oficial; a Administração poderá selecioná-lo livremente, mediante contratação direta, adotando o critério de menor preço para as comissões, vedado o uso dos percentuais da lei que regula a profissão como parâmetro.",
 "Art. 31, caput e § 1º.","exige leiloeiro e contratação direta","t10e")
P("T10",["31"],"conceito_correto","troca_efeito",4,
 "O leilão não exigirá registro cadastral prévio, não terá fase de habilitação e deverá ser homologado assim que concluída a fase de lances, superada a fase recursal e efetivado o pagamento pelo licitante vencedor, na forma definida no edital.",
 "O leilão exigirá registro cadastral prévio e fase de habilitação e deverá ser homologado imediatamente após a fase de lances, independentemente da fase recursal ou do pagamento pelo licitante vencedor.",
 "Art. 31, § 4º.","inverte regras do leilão","t10f")
P("T10",["31"],"conceito_correto","excecao_omitida",3,
 "O edital do leilão será divulgado em sítio eletrônico oficial, conterá a descrição do bem, o valor pelo qual foi avaliado, o preço mínimo pelo qual poderá ser alienado, as condições de pagamento e a especificação de eventuais ônus, gravames ou pendências, e será também afixado em local de ampla circulação de pessoas na sede da Administração.",
 "O edital do leilão será divulgado apenas em sítio eletrônico oficial, não conterá o valor da avaliação do bem, para estimular a competição, e dispensa a especificação de ônus, gravames ou pendências existentes sobre os bens leiloados.",
 "Art. 31, §§ 2º e 3º.","omite avaliação e ônus","t10g")
P("T10",["32"],"conceito_correto","troca_numero",4,
 "Na modalidade diálogo competitivo, a Administração apresentará, por ocasião da divulgação do edital, suas necessidades e as exigências já definidas e estabelecerá prazo mínimo de 25 dias úteis para manifestação de interesse na participação da licitação; concluído o diálogo, abrirá prazo não inferior a 60 dias úteis para a apresentação das propostas pelos licitantes pré-selecionados.",
 "Na modalidade diálogo competitivo, a Administração estabelecerá prazo mínimo de 10 dias úteis para manifestação de interesse na participação da licitação; concluído o diálogo, abrirá prazo não inferior a 30 dias úteis para a apresentação das propostas pelos licitantes pré-selecionados.",
 "Art. 32, § 1º, I e VIII.","troca prazos","t10h")
P("T10",["32"],"conceito_correto","troca_efeito",4,
 "No diálogo competitivo, a divulgação de informações de modo discriminatório que possa implicar vantagem para algum licitante será vedada, a Administração não poderá revelar a outros licitantes as soluções propostas ou as informações sigilosas comunicadas por um licitante sem o seu consentimento, e as reuniões com os licitantes pré-selecionados serão registradas em ata e gravadas em áudio e vídeo.",
 "No diálogo competitivo, a Administração poderá revelar a todos os licitantes as soluções propostas por um deles, independentemente de consentimento, para garantir a isonomia, e as reuniões com os licitantes pré-selecionados dispensam registro em ata e gravação.",
 "Art. 32, § 1º, III, IV e VI.","permite divulgação de soluções","t10i")
P("T10",["32"],"conceito_correto","troca_autoridade",4,
 "O diálogo competitivo será conduzido por comissão de contratação composta de pelo menos 3 servidores efetivos ou empregados públicos pertencentes aos quadros permanentes da Administração, admitida a contratação de profissionais para assessoramento técnico da comissão, que assinarão termo de confidencialidade e abster-se-ão de atividades que possam configurar conflito de interesses.",
 "O diálogo competitivo será conduzido pelo pregoeiro, auxiliado por equipe de apoio, sendo vedada a contratação de profissionais para assessoramento técnico, que poderiam comprometer a confidencialidade das soluções.",
 "Art. 32, § 1º, XI, e § 2º.","troca condutor e veda assessoria","t10j")
# T11
P("T11",["33"],"conceito_correto","troca_numero",2,
 "O julgamento das propostas será realizado de acordo com os critérios de menor preço, maior desconto, melhor técnica ou conteúdo artístico, técnica e preço, maior lance, no caso de leilão, e maior retorno econômico.",
 "O julgamento das propostas será realizado de acordo com os critérios de menor preço, maior desconto, melhor técnica ou conteúdo artístico, técnica e preço, maior lance, em qualquer modalidade, e menor prazo de entrega.",
 "Art. 33, I a VI.","inclui critério inexistente","t11a")
P("T11",["34"],"conceito_correto","troca_efeito",4,
 "O julgamento por menor preço ou maior desconto considerará o menor dispêndio para a Administração, atendidos os parâmetros mínimos de qualidade definidos no edital; os custos indiretos relacionados ao ciclo de vida do objeto poderão ser considerados, sempre que objetivamente mensuráveis, e o maior desconto terá como referência o preço global fixado no edital, estendendo-se o desconto aos eventuais termos aditivos.",
 "O julgamento por menor preço ou maior desconto considerará exclusivamente o valor nominal da proposta, sendo vedada a consideração dos custos indiretos ligados ao ciclo de vida do objeto, e o maior desconto terá como referência o preço unitário, não se estendendo aos termos aditivos.",
 "Art. 34, caput, § 1º e § 2º.","veda ciclo de vida e restringe desconto","t11b")
P("T11",["35"],"conceito_correto","excecao_omitida",3,
 "O julgamento por melhor técnica ou conteúdo artístico considerará exclusivamente as propostas técnicas ou artísticas apresentadas pelos licitantes, e o edital deverá definir o prêmio ou a remuneração que será atribuída aos vencedores, podendo esse critério ser utilizado para a contratação de projetos e trabalhos de natureza técnica, científica ou artística.",
 "O julgamento por melhor técnica ou conteúdo artístico considerará as propostas técnicas e as propostas de preço apresentadas pelos licitantes, e esse critério somente poderá ser utilizado para a contratação de obras e serviços de engenharia.",
 "Art. 35 e parágrafo único.","inclui preço e restringe objeto","t11c")
P("T11",["36"],"conceito_correto","troca_numero",4,
 "No julgamento por técnica e preço, deverão ser avaliadas e ponderadas as propostas técnicas e, em seguida, as propostas de preço, na proporção máxima de 70% de valoração para a proposta técnica; o desempenho pretérito na execução de contratos com a Administração deverá ser considerado na pontuação técnica.",
 "No julgamento por técnica e preço, deverão ser avaliadas e ponderadas as propostas de preço e, em seguida, as propostas técnicas, na proporção mínima de 70% de valoração para a proposta técnica; o desempenho pretérito na execução de contratos com a Administração não pode ser considerado na pontuação técnica.",
 "Art. 36, §§ 2º e 3º.","troca máximo por mínimo e veda desempenho","t11d")
P("T11",["36"],"conceito_correto","excecao_omitida",4,
 "O critério de julgamento de técnica e preço será escolhido quando estudo técnico preliminar demonstrar que a avaliação e a ponderação da qualidade técnica das propostas que superarem os requisitos mínimos forem relevantes para a Administração, entre outras, nas licitações para contratação de serviços técnicos especializados de natureza predominantemente intelectual, caso em que deverá ser preferencialmente empregado, e de obras e serviços especiais de engenharia.",
 "O critério de julgamento de técnica e preço será utilizado, em regra, em todas as licitações de bens e serviços comuns, dispensado o estudo técnico preliminar, e é vedado para a contratação de serviços técnicos especializados de natureza predominantemente intelectual.",
 "Art. 36, § 1º, I e IV.","vedação indevida e dispensa de ETP","t11e")
P("T11",["37"],"conceito_correto","troca_numero",4,
 "No julgamento por melhor técnica ou por técnica e preço, a banca que atribui notas a quesitos de natureza qualitativa terá no mínimo 3 membros e poderá ser composta de servidores efetivos ou empregados públicos dos quadros permanentes ou de profissionais contratados por conhecimento técnico, experiência ou renome, desde que seus trabalhos sejam supervisionados por profissionais designados conforme o art. 7º.",
 "No julgamento por melhor técnica ou por técnica e preço, a banca que atribui notas a quesitos de natureza qualitativa terá no mínimo 5 membros e será composta exclusivamente de servidores efetivos, sendo vedada a contratação de profissionais por conhecimento técnico, experiência ou renome.",
 "Art. 37, II e § 1º.","troca número e veda contratados","t11f")
P("T11",["37"],"conceito_correto","troca_numero",5,
 "Ressalvados os casos de inexigibilidade, na licitação para contratação dos serviços técnicos especializados de natureza predominantemente intelectual previstos nas alíneas a, d e h do inciso XVIII do art. 6º, cujo valor estimado da contratação seja superior a R$ 300.000,00, o julgamento será por melhor técnica ou por técnica e preço, na proporção de 70% de valoração da proposta técnica, conforme a redação original da lei.",
 "Ressalvados os casos de inexigibilidade, na licitação para contratação dos serviços técnicos especializados de natureza predominantemente intelectual previstos nas alíneas a, d e h do inciso XVIII do art. 6º, cujo valor estimado da contratação seja superior a R$ 300.000,00, o julgamento será por menor preço, na proporção de 30% de valoração da proposta técnica, conforme a redação original da lei.",
 "Art. 37, § 2º. Valor atualizado por decreto.","troca critério e proporção","t11g",["valor_atualizado_por_decreto"])
P("T11",["38"],"conceito_correto","troca_efeito",3,
 "No julgamento por melhor técnica ou por técnica e preço, a obtenção de pontuação devido à capacitação técnico-profissional exigirá que a execução do respectivo contrato tenha participação direta e pessoal do profissional correspondente.",
 "No julgamento por melhor técnica ou por técnica e preço, a obtenção de pontuação devido à capacitação técnico-profissional dispensa a participação direta e pessoal do profissional na execução do contrato, bastando a comprovação do vínculo com a empresa.",
 "Art. 38.","dispensa participação do profissional","t11h")
P("T11",["39"],"conceito_correto","confusao_instituto",4,
 "O julgamento por maior retorno econômico é utilizado exclusivamente para a celebração de contrato de eficiência e considerará a maior economia para a Administração, devendo a remuneração ser fixada em percentual que incidirá de forma proporcional à economia efetivamente obtida; se a economia prevista não for gerada, a diferença entre a economia contratada e a efetivamente obtida será descontada da remuneração do contratado.",
 "O julgamento por maior retorno econômico é utilizado em contratos de obras de grande vulto e considerará o menor preço ofertado, devendo a remuneração ser fixa; se a economia prevista não for gerada, nenhum desconto incidirá sobre a remuneração do contratado.",
 "Art. 39, caput, §§ 1º a 4º.","troca objeto e efeito","t11i")
# T12
P("T12",["40"],"conceito_correto","excecao_omitida",3,
 "O planejamento de compras deverá considerar a expectativa de consumo anual e observar, entre outros, condições de aquisição e pagamento semelhantes às do setor privado, o processamento por meio de sistema de registro de preços, quando pertinente, e o atendimento aos princípios da padronização, do parcelamento, quando for tecnicamente viável e economicamente vantajoso, e da responsabilidade fiscal.",
 "O planejamento de compras deverá considerar a expectativa de consumo mensal e observar condições de aquisição e pagamento próprias do setor público, vedado o processamento por sistema de registro de preços e dispensado o atendimento ao princípio do parcelamento.",
 "Art. 40, caput, I, II e V.","troca consumo e veda registro de preços","t12a")
P("T12",["40"],"conceito_correto","excecao_omitida",4,
 "O parcelamento não será adotado quando a economia de escala, a redução de custos de gestão de contratos ou a maior vantagem na contratação recomendar a compra do item do mesmo fornecedor, quando o objeto configurar sistema único e integrado e houver risco ao conjunto do objeto pretendido ou quando o processo de padronização ou de escolha de marca levar a fornecedor exclusivo.",
 "O parcelamento será sempre adotado nas compras, ainda que o objeto configure sistema único e integrado e haja risco ao conjunto do objeto pretendido, e a padronização ou a escolha de marca que leve a fornecedor exclusivo é, por si só, causa de nulidade da licitação.",
 "Art. 40, § 3º, I a III.","torna o parcelamento absoluto","t12b")
P("T12",["40"],"conceito_correto","excecao_omitida",3,
 "Na aplicação do princípio do parcelamento nas compras, deverão ser considerados a viabilidade da divisão do objeto em lotes, o aproveitamento das peculiaridades do mercado local, com vistas à economicidade, e o dever de buscar a ampliação da competição e de evitar a concentração de mercado.",
 "Na aplicação do princípio do parcelamento nas compras, deverá ser considerada apenas a divisão do objeto em lotes, sendo vedado o aproveitamento das peculiaridades do mercado local, para evitar tratamento diferenciado entre os licitantes.",
 "Art. 40, § 2º, I a III.","restringe fatores","t12c")
P("T12",["41"],"conceito_correto","excecao_omitida",4,
 "Na licitação que envolva o fornecimento de bens, a Administração poderá excepcionalmente indicar uma ou mais marcas ou modelos, desde que formalmente justificado, entre outras hipóteses, em decorrência da necessidade de padronização do objeto ou de manter a compatibilidade com plataformas e padrões já adotados pela Administração.",
 "Na licitação que envolva o fornecimento de bens, a Administração poderá indicar livremente marcas ou modelos, sem necessidade de justificativa formal, sempre que isso facilitar a compreensão do objeto pelos licitantes.",
 "Art. 41, I, a e b.","dispensa justificativa","t12d")
P("T12",["41"],"conceito_correto","troca_efeito",4,
 "A Administração poderá exigir amostra ou prova de conceito do bem no procedimento de pré-qualificação permanente, na fase de julgamento das propostas ou de lances, ou no período de vigência do contrato ou da ata de registro de preços, desde que previsto no edital e justificada a necessidade; quando realizada na fase de julgamento das propostas ou de lances, a exigência restringir-se-á ao licitante provisoriamente vencedor.",
 "A Administração poderá exigir amostra ou prova de conceito do bem somente após a assinatura do contrato, ainda que não prevista no edital, e, quando realizada na fase de julgamento das propostas ou de lances, a exigência alcançará todos os licitantes participantes.",
 "Art. 41, II e parágrafo único.","estende a todos os licitantes","t12e")
P("T12",["41"],"conceito_correto","excecao_omitida",3,
 "A Administração poderá vedar a contratação de marca ou produto quando, mediante processo administrativo, restar comprovado que produtos adquiridos e utilizados anteriormente não atendem a requisitos indispensáveis ao pleno adimplemento da obrigação contratual, e poderá solicitar, motivadamente, carta de solidariedade emitida pelo fabricante no caso de licitante revendedor ou distribuidor.",
 "A Administração poderá vedar a contratação de marca ou produto por simples preferência do gestor, independentemente de processo administrativo, e não poderá solicitar carta de solidariedade do fabricante no caso de licitante revendedor ou distribuidor.",
 "Art. 41, III e IV.","dispensa processo administrativo","t12f")
