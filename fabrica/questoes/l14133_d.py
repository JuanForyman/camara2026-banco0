# Lei 14.133/2021 — lote L7 parte d (arts. 61 a 75)
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
# T19
P("T19",["61"],"conceito_correto","troca_autoridade",3,
 "Definido o resultado do julgamento, a Administração poderá negociar condições mais vantajosas com o primeiro colocado; a negociação poderá ser feita com os demais licitantes, segundo a ordem de classificação inicialmente estabelecida, quando o primeiro colocado, mesmo após a negociação, for desclassificado em razão de sua proposta permanecer acima do preço máximo definido pela Administração.",
 "Definido o resultado do julgamento, a Administração deverá negociar condições mais vantajosas com todos os licitantes simultaneamente, sendo vedada a negociação com os demais colocados quando o primeiro for desclassificado por proposta acima do preço máximo.",
 "Art. 61, caput e § 1º.","torna obrigatória e veda negociação com os demais","t19a")
P("T19",["61"],"conceito_correto","excecao_omitida",3,
 "A negociação será conduzida por agente de contratação ou comissão de contratação, na forma de regulamento, e, depois de concluída, terá seu resultado divulgado a todos os licitantes e anexado aos autos do processo licitatório.",
 "A negociação será conduzida pela autoridade superior, e, depois de concluída, terá seu resultado mantido em sigilo até a homologação, sem necessidade de anexá-lo aos autos do processo licitatório.",
 "Art. 61, § 2º.","troca condutor e publicidade","t19b")
P("T19",["62"],"conceito_correto","troca_numero",2,
 "A habilitação é a fase da licitação em que se verifica o conjunto de informações e documentos necessários e suficientes para demonstrar a capacidade do licitante de realizar o objeto da licitação, dividindo-se em habilitação jurídica, técnica, fiscal, social e trabalhista e econômico-financeira.",
 "A habilitação é a fase da licitação em que se verifica o conjunto de informações e documentos necessários e suficientes para demonstrar a capacidade do licitante de realizar o objeto da licitação, dividindo-se em habilitação jurídica, técnica, fiscal, social e trabalhista, econômico-financeira e ambiental.",
 "Art. 62, I a IV.","acrescenta modalidade de habilitação","t19c")
P("T19",["63"],"conceito_correto","excecao_omitida",4,
 "Na fase de habilitação, será exigida a apresentação dos documentos apenas pelo licitante vencedor, exceto quando a fase de habilitação anteceder a de julgamento, e os documentos relativos à regularidade fiscal serão exigidos, em qualquer caso, somente em momento posterior ao julgamento das propostas e apenas do licitante mais bem classificado.",
 "Na fase de habilitação, será exigida a apresentação dos documentos de todos os licitantes, antes do julgamento das propostas, inclusive os relativos à regularidade fiscal, em qualquer caso.",
 "Art. 63, II e III.","exige de todos e antes do julgamento","t19d")
P("T19",["63"],"conceito_correto","troca_efeito",4,
 "Quando a avaliação prévia do local de execução for imprescindível, o edital poderá prever, sob pena de inabilitação, que o licitante ateste que conhece o local e as condições da obra ou serviço, assegurado o direito de vistoria prévia; o edital sempre deverá prever a possibilidade de substituição da vistoria por declaração formal assinada pelo responsável técnico do licitante.",
 "Quando a avaliação prévia do local de execução for imprescindível, o edital exigirá, sob pena de inabilitação, a realização de vistoria prévia pelo licitante, sendo vedada a substituição por declaração formal do responsável técnico.",
 "Art. 63, §§ 2º e 3º.","veda substituição da vistoria","t19e")
P("T19",["64"],"conceito_correto","excecao_omitida",4,
 "Após a entrega dos documentos para habilitação, não será permitida a substituição ou a apresentação de novos documentos, salvo em sede de diligência, para complementação de informações acerca dos documentos já apresentados, desde que necessária para apurar fatos existentes à época da abertura do certame, e para atualização de documentos cuja validade tenha expirado após a data de recebimento das propostas.",
 "Após a entrega dos documentos para habilitação, é permitida, a qualquer tempo, a substituição ou a apresentação de novos documentos pelo licitante, inclusive para comprovar fatos ocorridos após a abertura do certame.",
 "Art. 64, I e II.","libera novos documentos","t19f")
P("T19",["64"],"conceito_correto","troca_efeito",4,
 "Na análise dos documentos de habilitação, a comissão de licitação poderá sanar erros ou falhas que não alterem a substância dos documentos e sua validade jurídica, mediante despacho fundamentado registrado e acessível a todos; quando a fase de habilitação anteceder a de julgamento e já tiver sido encerrada, não caberá exclusão de licitante por motivo relacionado à habilitação, salvo em razão de fatos supervenientes ou só conhecidos após o julgamento.",
 "Na análise dos documentos de habilitação, a comissão de licitação não poderá sanar nenhum erro ou falha dos documentos; quando a fase de habilitação anteceder a de julgamento e já tiver sido encerrada, caberá exclusão de licitante por qualquer motivo de habilitação, ainda que conhecido antes do julgamento.",
 "Art. 64, §§ 1º e 2º.","veda saneamento e permite exclusão tardia","t19g")
P("T19",["65"],"conceito_correto","excecao_omitida",3,
 "As empresas criadas no exercício financeiro da licitação deverão atender a todas as exigências da habilitação e ficarão autorizadas a substituir os demonstrativos contábeis pelo balanço de abertura.",
 "As empresas criadas no exercício financeiro da licitação ficam dispensadas de atender às exigências da habilitação econômico-financeira e de apresentar balanço de abertura.",
 "Art. 65, § 1º.","dispensa habilitação","t19h")
# T20
P("T20",["66"],"conceito_correto","excecao_omitida",3,
 "A habilitação jurídica visa a demonstrar a capacidade de o licitante exercer direitos e assumir obrigações, e a documentação a ser apresentada por ele limita-se à comprovação de existência jurídica da pessoa e, quando cabível, de autorização para o exercício da atividade a ser contratada.",
 "A habilitação jurídica visa a demonstrar a regularidade do licitante perante a Fazenda Pública, e a documentação a ser apresentada por ele compreende, além da existência jurídica, as certidões negativas de débitos tributários.",
 "Art. 66.","confunde habilitação jurídica com fiscal","t20a")
P("T20",["67"],"conceito_correto","troca_numero",4,
 "A exigência de atestados de qualificação técnica será restrita às parcelas de maior relevância ou valor significativo do objeto da licitação, assim consideradas as que tenham valor individual igual ou superior a 4% do valor total estimado da contratação, e será admitida a exigência de atestados com quantidades mínimas de até 50% dessas parcelas, vedadas limitações de tempo e de locais específicos.",
 "A exigência de atestados de qualificação técnica será restrita às parcelas de maior relevância ou valor significativo do objeto da licitação, assim consideradas as que tenham valor individual igual ou superior a 10% do valor total estimado da contratação, e será admitida a exigência de atestados com quantidades mínimas de até 80% dessas parcelas, admitidas limitações de tempo e de locais específicos.",
 "Art. 67, §§ 1º e 2º.","troca percentuais e permite limitação","t20b")
P("T20",["67"],"conceito_correto","excecao_omitida",4,
 "A documentação relativa à qualificação técnico-profissional e técnico-operacional será restrita, entre outros itens, à apresentação de profissional registrado no conselho competente, detentor de atestado de responsabilidade técnica por execução de obra ou serviço de características semelhantes, a certidões ou atestados que demonstrem capacidade operacional em serviços similares, à indicação do pessoal técnico, das instalações e do aparelhamento adequados e disponíveis e à prova de requisitos de lei especial.",
 "A documentação relativa à qualificação técnico-profissional e técnico-operacional poderá abranger quaisquer documentos que a Administração julgar úteis, inclusive balanço patrimonial e comprovação de faturamento mínimo anterior, não se limitando ao rol da lei.",
 "Art. 67, I a V.","amplia rol","t20c")
P("T20",["67"],"conceito_correto","troca_efeito",4,
 "Salvo na contratação de obras e serviços de engenharia, as exigências de atestado de profissional e de capacidade operacional poderão, a critério da Administração, ser substituídas por outra prova de que o profissional ou a empresa possui conhecimento técnico e experiência prática na execução de serviço de características semelhantes, hipótese em que as provas alternativas aceitáveis deverão ser previstas em regulamento.",
 "Em qualquer contratação, inclusive de obras e serviços de engenharia, as exigências de atestado de profissional e de capacidade operacional poderão ser substituídas por simples declaração do licitante, sem necessidade de previsão em regulamento.",
 "Art. 67, § 3º.","estende substituição às obras","t20d")
P("T20",["67"],"conceito_correto","troca_numero",4,
 "Em se tratando de serviços contínuos, o edital poderá exigir certidão ou atestado que demonstre que o licitante tenha executado serviços similares ao objeto da licitação, em períodos sucessivos ou não, por um prazo mínimo que não poderá ser superior a 3 anos; e o edital poderá prever que a qualificação técnica seja demonstrada por atestados relativos a potencial subcontratado, limitado a 25% do objeto a ser licitado.",
 "Em se tratando de serviços contínuos, o edital poderá exigir certidão ou atestado que demonstre que o licitante tenha executado serviços similares ao objeto da licitação por um prazo mínimo de 5 anos ininterruptos; e o edital poderá prever atestados relativos a potencial subcontratado, limitado a 50% do objeto a ser licitado.",
 "Art. 67, §§ 5º e 9º.","troca prazo e limite","t20e")
P("T20",["67"],"conceito_correto","excecao_omitida",4,
 "Serão aceitos atestados ou outros documentos hábeis emitidos por entidades estrangeiras quando acompanhados de tradução para o português, salvo se comprovada a inidoneidade da entidade emissora; e os profissionais indicados pelo licitante deverão participar da obra ou serviço objeto da licitação, admitida a sua substituição por profissionais de experiência equivalente ou superior, desde que aprovada pela Administração.",
 "Não serão aceitos atestados emitidos por entidades estrangeiras em nenhuma hipótese; e os profissionais indicados pelo licitante poderão ser livremente substituídos, sem aprovação da Administração, por profissionais de experiência inferior.",
 "Art. 67, §§ 4º e 6º.","veda atestado estrangeiro","t20f")
P("T20",["67"],"conceito_correto","confusao_instituto",5,
 "Se o atestado de desempenho anterior tiver sido emitido em favor de consórcio homogêneo e não identificar a atividade desempenhada por cada consorciado, as experiências atestadas serão reconhecidas para cada empresa na proporção quantitativa de sua participação, salvo nas licitações de serviços técnicos especializados de natureza predominantemente intelectual, em que todas as experiências serão reconhecidas para cada empresa consorciada.",
 "Se o atestado de desempenho anterior tiver sido emitido em favor de consórcio homogêneo e não identificar a atividade desempenhada por cada consorciado, as experiências atestadas serão reconhecidas integralmente apenas para a empresa líder, inclusive nas licitações de serviços técnicos especializados de natureza predominantemente intelectual.",
 "Art. 67, § 10, I.","atribui só à líder","t20g")
# T21
P("T21",["68"],"conceito_correto","excecao_omitida",3,
 "As habilitações fiscal, social e trabalhista serão aferidas mediante a verificação da inscrição no CPF ou no CNPJ, da inscrição no cadastro de contribuintes estadual ou municipal, se houver, da regularidade perante a Fazenda federal, estadual ou municipal, da regularidade relativa à Seguridade Social e ao FGTS, da regularidade perante a Justiça do Trabalho e do cumprimento do inciso XXXIII do art. 7º da Constituição Federal.",
 "As habilitações fiscal, social e trabalhista serão aferidas exclusivamente mediante a verificação da inscrição no CNPJ e da regularidade perante a Fazenda federal, dispensada a comprovação de regularidade perante a Justiça do Trabalho e relativa ao FGTS.",
 "Art. 68, I a VI.","reduz requisitos","t21a")
P("T21",["69"],"conceito_correto","troca_numero",4,
 "A habilitação econômico-financeira visa a demonstrar a aptidão econômica do licitante para cumprir as obrigações do futuro contrato, devendo ser comprovada de forma objetiva, por coeficientes e índices econômicos previstos no edital, devidamente justificados, e será restrita ao balanço patrimonial, à demonstração de resultado de exercício e demais demonstrações contábeis dos 2 últimos exercícios sociais e à certidão negativa de feitos sobre falência.",
 "A habilitação econômico-financeira visa a demonstrar a aptidão econômica do licitante para cumprir as obrigações do futuro contrato, devendo ser comprovada de forma subjetiva, a critério do agente de contratação, e será restrita ao balanço patrimonial e demais demonstrações contábeis dos 5 últimos exercícios sociais.",
 "Art. 69, caput, I e II.","troca período e critério","t21b")
P("T21",["69"],"conceito_correto","excecao_omitida",4,
 "Para a habilitação econômico-financeira, é vedada a exigência de valores mínimos de faturamento anterior e de índices de rentabilidade ou lucratividade, bem como a exigência de índices e valores não usualmente adotados para a avaliação da situação econômico-financeira suficiente para o cumprimento das obrigações da licitação.",
 "Para a habilitação econômico-financeira, é admitida a exigência de valores mínimos de faturamento anterior e de índices de rentabilidade ou lucratividade, desde que previstos no edital e justificados no processo licitatório.",
 "Art. 69, §§ 2º e 5º.","admite faturamento mínimo","t21c")
P("T21",["69"],"conceito_correto","troca_numero",4,
 "A Administração, nas compras para entrega futura e na execução de obras e serviços, poderá estabelecer no edital a exigência de capital mínimo ou de patrimônio líquido mínimo equivalente a até 10% do valor estimado da contratação; os documentos contábeis limitar-se-ão ao último exercício no caso de pessoa jurídica constituída há menos de 2 anos.",
 "A Administração, nas compras para entrega futura e na execução de obras e serviços, poderá estabelecer no edital a exigência de capital mínimo ou de patrimônio líquido mínimo equivalente a até 30% do valor estimado da contratação; os documentos contábeis limitar-se-ão ao último exercício no caso de pessoa jurídica constituída há menos de 5 anos.",
 "Art. 69, §§ 4º e 6º.","troca percentuais e prazo","t21d")
P("T21",["70"],"conceito_correto","excecao_omitida",4,
 "A documentação de habilitação poderá ser apresentada em original, por cópia ou por outro meio admitido pela Administração, ou substituída por registro cadastral emitido por órgão ou entidade pública, desde que previsto no edital; poderá ainda ser dispensada, total ou parcialmente, nas contratações para entrega imediata e nas contratações em valores inferiores a 1/4 do limite para dispensa de licitação para compras em geral.",
 "A documentação de habilitação deverá ser apresentada exclusivamente em original, sendo vedada a sua substituição por registro cadastral; a dispensa da documentação só é admitida nas contratações de valor superior ao limite de dispensa para compras em geral.",
 "Art. 70, I a III.","exige original e inverte dispensa","t21e")
# T22
P("T22",["71"],"conceito_correto","troca_autoridade",3,
 "Encerradas as fases de julgamento e habilitação, e exauridos os recursos administrativos, o processo licitatório será encaminhado à autoridade superior, que poderá determinar o retorno dos autos para saneamento de irregularidades, revogar a licitação por motivo de conveniência e oportunidade, anulá-la, de ofício ou mediante provocação de terceiros, sempre que presente ilegalidade insanável, ou adjudicar o objeto e homologar a licitação.",
 "Encerradas as fases de julgamento e habilitação, e exauridos os recursos administrativos, o processo licitatório será encaminhado ao agente de contratação, que poderá revogar a licitação por motivo de conveniência e oportunidade ou anulá-la apenas mediante provocação de terceiros, sendo vedado o retorno dos autos para saneamento.",
 "Art. 71, I a IV.","troca autoridade e limita anulação","t22a")
P("T22",["71"],"conceito_correto","troca_efeito",4,
 "O motivo determinante para a revogação do processo licitatório deverá ser resultante de fato superveniente devidamente comprovado, e, nos casos de anulação e revogação, deverá ser assegurada a prévia manifestação dos interessados.",
 "O motivo determinante para a revogação do processo licitatório poderá ser resultante de fato anterior ou superveniente, a critério da autoridade, e, nos casos de anulação e revogação, é dispensada a prévia manifestação dos interessados.",
 "Art. 71, §§ 2º e 3º.","dispensa fato superveniente e contraditório","t22b")
P("T22",["71"],"conceito_correto","excecao_omitida",4,
 "Ao pronunciar a nulidade da licitação, a autoridade indicará expressamente os atos com vícios insanáveis, tornando sem efeito todos os subsequentes que deles dependam, e dará ensejo à apuração de responsabilidade de quem lhes tenha dado causa; o disposto no art. 71 aplica-se, no que couber, à contratação direta e aos procedimentos auxiliares da licitação.",
 "Ao pronunciar a nulidade da licitação, a autoridade tornará sem efeito todos os atos praticados no processo, sem necessidade de indicar os atos viciados, e o disposto no art. 71 não se aplica à contratação direta nem aos procedimentos auxiliares da licitação.",
 "Art. 71, §§ 1º e 4º.","anula tudo e afasta contratação direta","t22c")
# T23
P("T23",["72"],"conceito_correto","excecao_omitida",3,
 "O processo de contratação direta, que compreende os casos de inexigibilidade e de dispensa de licitação, deverá ser instruído, entre outros documentos, com o documento de formalização de demanda, a estimativa de despesa, o parecer jurídico, a demonstração da compatibilidade da previsão de recursos orçamentários, a comprovação de que o contratado preenche os requisitos de habilitação, a razão da escolha do contratado, a justificativa de preço e a autorização da autoridade competente.",
 "O processo de contratação direta, que compreende os casos de inexigibilidade e de dispensa de licitação, dispensa a instrução com parecer jurídico, razão da escolha do contratado e justificativa de preço, bastando a autorização da autoridade competente e a demonstração de disponibilidade orçamentária.",
 "Art. 72, I a VIII.","dispensa documentos essenciais","t23a")
P("T23",["72"],"conceito_correto","troca_efeito",3,
 "O ato que autoriza a contratação direta ou o extrato decorrente do contrato deverá ser divulgado e mantido à disposição do público em sítio eletrônico oficial.",
 "O ato que autoriza a contratação direta será mantido em sigilo até a assinatura do contrato, divulgando-se apenas o extrato do contrato, em jornal de grande circulação.",
 "Art. 72, parágrafo único.","substitui sítio por sigilo","t23b")
P("T23",["73"],"conceito_correto","troca_efeito",4,
 "Na hipótese de contratação direta indevida ocorrida com dolo, fraude ou erro grosseiro, o contratado e o agente público responsável responderão solidariamente pelo dano causado ao erário, sem prejuízo de outras sanções legais cabíveis.",
 "Na hipótese de contratação direta indevida, ainda que ocorrida sem dolo, fraude ou erro grosseiro, apenas o agente público responsável responderá, de forma subsidiária, pelo dano causado ao erário, ficando o contratado isento de responsabilidade.",
 "Art. 73.","retira solidariedade e exige","t23c")
# T24
P("T24",["74"],"conceito_correto","excecao_omitida",3,
 "É inexigível a licitação quando inviável a competição, em especial nos casos de aquisição de materiais, equipamentos ou serviços que só possam ser fornecidos por produtor, empresa ou representante comercial exclusivos, de contratação de profissional do setor artístico consagrado pela crítica ou pela opinião pública, de serviços técnicos especializados de natureza predominantemente intelectual com profissionais ou empresas de notória especialização, de objetos que devam ou possam ser contratados por credenciamento e de aquisição ou locação de imóvel cujas características tornem necessária sua escolha.",
 "É inexigível a licitação apenas nos casos taxativamente enumerados no art. 74, entre os quais a contratação de qualquer profissional do setor artístico, independentemente de ser consagrado pela crítica ou pela opinião pública, e a contratação de serviços de publicidade e divulgação de notória especialização.",
 "Art. 74, caput, I a V (rol exemplificativo; vedada a inexigibilidade para publicidade e divulgação).","trata rol como taxativo e admite publicidade","t24a")
P("T24",["74"],"conceito_correto","excecao_omitida",4,
 "Para fins de inexigibilidade por fornecedor exclusivo, a Administração deverá demonstrar a inviabilidade de competição mediante atestado de exclusividade, contrato de exclusividade, declaração do fabricante ou outro documento idôneo capaz de comprovar que o objeto é fornecido ou prestado por produtor, empresa ou representante comercial exclusivos, vedada a preferência por marca específica.",
 "Para fins de inexigibilidade por fornecedor exclusivo, basta a preferência da Administração por determinada marca, dispensada a apresentação de atestado, contrato de exclusividade ou declaração do fabricante.",
 "Art. 74, § 1º.","admite preferência por marca","t24b")
P("T24",["74"],"conceito_correto","troca_efeito",4,
 "Considera-se empresário exclusivo a pessoa física ou jurídica que possua contrato, declaração, carta ou outro documento que ateste a exclusividade permanente e contínua de representação, no País ou em Estado específico, do profissional do setor artístico, afastada a possibilidade de contratação direta por inexigibilidade por meio de empresário com representação restrita a evento ou local específico.",
 "Considera-se empresário exclusivo a pessoa que possua contrato ou declaração que ateste a exclusividade de representação do profissional do setor artístico apenas para o evento ou local específico a ser contratado, admitida a inexigibilidade nessa hipótese.",
 "Art. 74, § 2º.","admite exclusividade restrita","t24c")
P("T24",["74"],"conceito_correto","excecao_omitida",4,
 "Nas contratações por inexigibilidade para serviços técnicos especializados de natureza predominantemente intelectual com profissionais ou empresas de notória especialização, é vedada a subcontratação de empresas ou a atuação de profissionais distintos daqueles que tenham justificado a inexigibilidade.",
 "Nas contratações por inexigibilidade para serviços técnicos especializados de natureza predominantemente intelectual com profissionais ou empresas de notória especialização, é admitida a subcontratação livre de empresas e a atuação de profissionais distintos daqueles que justificaram a inexigibilidade.",
 "Art. 74, § 4º.","admite subcontratação","t24d")
P("T24",["74"],"conceito_correto","troca_autoridade",4,
 "Nas contratações por inexigibilidade para aquisição ou locação de imóvel cujas características de instalações e de localização tornem necessária sua escolha, devem ser observados a avaliação prévia do bem, a certificação da inexistência de imóveis públicos vagos e disponíveis que atendam ao objeto e as justificativas que demonstrem a singularidade do imóvel e a vantagem para a Administração.",
 "Nas contratações por inexigibilidade para aquisição ou locação de imóvel, dispensam-se a avaliação prévia do bem e a certificação da inexistência de imóveis públicos vagos, bastando a indicação do imóvel pelo dirigente do órgão.",
 "Art. 74, § 5º, I a III.","dispensa requisitos","t24e")
P("T24",["74"],"conceito_correto","confusao_instituto",3,
 "Considera-se de notória especialização o profissional ou a empresa cujo conceito no campo de sua especialidade, decorrente de desempenho anterior, estudos, experiência, publicações, organização, aparelhamento, equipe técnica ou outros requisitos relacionados com suas atividades, permita inferir que o seu trabalho é essencial e reconhecidamente adequado à plena satisfação do objeto do contrato.",
 "Considera-se de notória especialização o profissional ou a empresa que apresentar o menor preço entre os consultados pela Administração, independentemente de desempenho anterior, estudos ou experiência, desde que inscritos em cadastro oficial.",
 "Art. 74, § 3º e art. 6º, XIX.","troca por menor preço","t24f")
# T25
P("T25",["75"],"conceito_correto","troca_numero",3,
 "É dispensável a licitação, conforme os valores da redação original da lei, para contratação que envolva valores inferiores a R$ 100.000,00, no caso de obras e serviços de engenharia ou de serviços de manutenção de veículos automotores, e inferiores a R$ 50.000,00, no caso de outros serviços e compras.",
 "É dispensável a licitação, conforme os valores da redação original da lei, para contratação que envolva valores inferiores a R$ 50.000,00, no caso de obras e serviços de engenharia, e inferiores a R$ 100.000,00, no caso de outros serviços e compras.",
 "Art. 75, I e II. Valores atualizados por decreto (Dec. 12.343/2024: R$ 125.451,15 e R$ 62.725,59).","inverte valores","t25a",["valor_atualizado_por_decreto"])
P("T25",["75"],"conceito_correto","excecao_omitida",4,
 "Para aferição dos valores de dispensa por baixo valor, deverão ser observados o somatório do que for despendido no exercício financeiro pela respectiva unidade gestora e o somatório da despesa realizada com objetos de mesma natureza, entendidos como tais aqueles relativos a contratações no mesmo ramo de atividade; esses valores serão duplicados para contratações por consórcio público ou por autarquia ou fundação qualificadas como agências executivas.",
 "Para aferição dos valores de dispensa por baixo valor, deverá ser considerado apenas o valor de cada contratação isoladamente, sem somatório da despesa por unidade gestora ou por ramo de atividade; esses valores não são duplicados em nenhuma hipótese.",
 "Art. 75, §§ 1º e 2º.","afasta somatório e duplicação","t25b")
P("T25",["75"],"conceito_correto","excecao_omitida",4,
 "As contratações por dispensa em razão do baixo valor serão preferencialmente precedidas de divulgação de aviso em sítio eletrônico oficial, pelo prazo mínimo de 3 dias úteis, com a especificação do objeto e a manifestação de interesse da Administração em obter propostas adicionais, e preferencialmente pagas por meio de cartão de pagamento, cujo extrato deverá ser divulgado no PNCP.",
 "As contratações por dispensa em razão do baixo valor serão obrigatoriamente precedidas de aviso em sítio eletrônico oficial, pelo prazo mínimo de 15 dias úteis, e pagas exclusivamente mediante ordem bancária, sem divulgação do extrato do pagamento.",
 "Art. 75, §§ 3º e 4º.","torna obrigatório e troca prazo","t25c")
P("T25",["75"],"conceito_correto","excecao_omitida",4,
 "É dispensável a licitação para contratação que mantenha todas as condições definidas em edital de licitação realizada há menos de 1 ano, quando se verificar que naquela licitação não surgiram licitantes interessados ou não foram apresentadas propostas válidas, ou quando as propostas apresentadas consignaram preços manifestamente superiores aos praticados no mercado.",
 "É dispensável a licitação para contratação que altere as condições definidas em edital de licitação realizada há menos de 2 anos, quando se verificar que naquela licitação surgiram licitantes interessados mas todos foram inabilitados.",
 "Art. 75, III, a e b.","troca prazo e condições","t25d")
P("T25",["75"],"conceito_correto","troca_efeito",5,
 "Nos casos de emergência ou de calamidade pública, a dispensa de licitação é cabível somente para a aquisição dos bens necessários ao atendimento da situação emergencial ou calamitosa e para as parcelas de obras e serviços que possam ser concluídas no prazo máximo de 1 ano, contado da data de ocorrência da emergência ou da calamidade, vedadas a prorrogação dos respectivos contratos e a recontratação de empresa já contratada com base nesse inciso.",
 "Nos casos de emergência ou de calamidade pública, a dispensa de licitação é cabível para a contratação da totalidade das obras e serviços necessários, sem limite de prazo, sendo admitidas a prorrogação dos contratos e a recontratação de empresa já contratada com base nesse inciso.",
 "Art. 75, VIII.","retira limites da emergência","t25e")
P("T25",["75"],"conceito_correto","excecao_omitida",4,
 "Para os fins da dispensa por emergência, considera-se emergencial a contratação por dispensa com objetivo de manter a continuidade do serviço público, devendo ser observados os valores praticados pelo mercado na forma do art. 23 e adotadas as providências necessárias para a conclusão do processo licitatório, sem prejuízo de apuração de responsabilidade dos agentes públicos que deram causa à situação emergencial.",
 "Para os fins da dispensa por emergência, a contratação independe da observância dos valores praticados pelo mercado e da adoção de providências para a conclusão do processo licitatório, ficando afastada a apuração de responsabilidade dos agentes que deram causa à situação emergencial.",
 "Art. 75, § 6º.","afasta preço de mercado e responsabilidade","t25f")
P("T25",["75"],"conceito_correto","confusao_instituto",4,
 "É dispensável a licitação para a contratação de associação de pessoas com deficiência, sem fins lucrativos e de comprovada idoneidade, para a prestação de serviços, desde que o preço contratado seja compatível com o praticado no mercado e os serviços sejam prestados exclusivamente por pessoas com deficiência.",
 "É inexigível a licitação para a contratação de associação de pessoas com deficiência, sem fins lucrativos, para a prestação de serviços, ainda que o preço contratado seja superior ao praticado no mercado, desde que parte dos serviços seja prestada por pessoas com deficiência.",
 "Art. 75, XIV.","troca dispensa por inexigibilidade","t25g")
P("T25",["75"],"conceito_correto","excecao_omitida",3,
 "É dispensável a licitação para a contratação de hortifrutigranjeiros, pães e outros gêneros perecíveis, no período necessário para a realização dos processos licitatórios correspondentes, hipótese em que a contratação será realizada diretamente com base no preço do dia.",
 "É dispensável a licitação para a contratação de hortifrutigranjeiros, pães e outros gêneros perecíveis, por prazo indeterminado, hipótese em que a contratação será realizada com base no menor preço registrado nos últimos seis meses.",
 "Art. 75, IV, e.","troca prazo e preço do dia","t25h")
P("T25",["75"],"caso_concreto","caso_concreto",4,
 "Um órgão federal precisa contratar serviço de manutenção de seus veículos oficiais, estimado em valor inferior ao limite de dispensa para serviços de manutenção de veículos automotores. Nesse caso, a licitação é dispensável, e a contratação deve ser preferencialmente precedida de aviso em sítio eletrônico oficial por pelo menos 3 dias úteis, com a manifestação de interesse em obter propostas adicionais.",
 "Um órgão federal precisa contratar serviço de manutenção de seus veículos oficiais, estimado em valor inferior ao limite de dispensa para serviços de manutenção de veículos automotores. Nesse caso, a licitação é inexigível, e a contratação é vedada se precedida de aviso em sítio eletrônico oficial, para preservar a rapidez do procedimento.",
 "Art. 75, I, e § 3º.","troca dispensa por inexigibilidade","t25i")
P("T25",["74"],"caso_concreto","caso_concreto",4,
 "Prefeitura pretende contratar apresentação de cantor consagrado pela opinião pública por meio de empresário que possui contrato escrito de exclusividade permanente e contínua de representação do artista em todo o País. Nessa situação, é possível a contratação direta por inexigibilidade de licitação.",
 "Prefeitura pretende contratar apresentação de cantor consagrado pela opinião pública por meio de empresário cuja carta de exclusividade vale apenas para o evento da cidade contratante. Nessa situação, é possível a contratação direta por inexigibilidade de licitação, pois a exclusividade restrita ao evento é suficiente.",
 "Art. 74, II e § 2º.","admite exclusividade restrita a evento","t25j")
