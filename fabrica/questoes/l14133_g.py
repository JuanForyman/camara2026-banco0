# Lei 14.133/2021 — lote L7 parte g (arts. 126 a 183)
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
# T39
P("T39",["126","127","128"],"conceito_correto","excecao_omitida",4,
 "As alterações unilaterais não poderão transfigurar o objeto da contratação; se o contrato não contemplar preços unitários para obras ou serviços cujo aditamento se fizer necessário, esses serão fixados pela aplicação da relação geral entre os valores da proposta e o do orçamento-base sobre os preços referenciais ou de mercado vigentes na data do aditamento, respeitados os limites do art. 125; e, nas obras e serviços de engenharia, a diferença percentual entre o valor global do contrato e o preço global de referência não poderá ser reduzida em favor do contratado em decorrência de aditamentos.",
 "As alterações unilaterais poderão transfigurar o objeto da contratação, desde que respeitado o limite de 25%; os preços unitários não previstos serão fixados livremente pelas partes na data do aditamento; e, nas obras e serviços de engenharia, a diferença percentual entre o valor global e o preço de referência poderá ser reduzida em favor do contratado nos aditamentos.",
 "Arts. 126 a 128.","permite transfigurar objeto","t39a")
P("T39",["129","130","131"],"conceito_correto","troca_efeito",4,
 "Na supressão de obras, bens ou serviços, se o contratado já houver adquirido os materiais e os colocado no local dos trabalhos, a Administração os pagará pelos custos de aquisição regularmente comprovados e monetariamente reajustados; na alteração unilateral que aumente ou diminua os encargos do contratado, o equilíbrio econômico-financeiro inicial será restabelecido no mesmo termo aditivo; e a extinção do contrato não configura óbice ao reconhecimento do desequilíbrio, concedida a indenização por termo indenizatório.",
 "Na supressão de obras, bens ou serviços, os materiais já adquiridos pelo contratado não serão indenizados pela Administração; na alteração unilateral que aumente os encargos do contratado, o equilíbrio será restabelecido em momento posterior, por termo próprio; e a extinção do contrato impede o reconhecimento de desequilíbrio econômico-financeiro.",
 "Arts. 129 a 131.","nega indenização e equilíbrio","t39b")
P("T39",["131","132"],"conceito_correto","troca_efeito",5,
 "O pedido de restabelecimento do equilíbrio econômico-financeiro deverá ser formulado durante a vigência do contrato e antes de eventual prorrogação; e a formalização do termo aditivo é condição para a execução, pelo contratado, das prestações determinadas pela Administração no curso da execução, salvo nos casos de justificada necessidade de antecipação de seus efeitos, hipótese em que a formalização deverá ocorrer no prazo máximo de 1 mês.",
 "O pedido de restabelecimento do equilíbrio econômico-financeiro poderá ser formulado a qualquer tempo, inclusive após a extinção do contrato; e as prestações determinadas pela Administração podem ser executadas antes da formalização do termo aditivo sem qualquer prazo para sua formalização.",
 "Arts. 131, parágrafo único, e 132.","retira prazo","t39c")
P("T39",["133"],"conceito_correto","excecao_omitida",5,
 "Nas hipóteses de contratação integrada ou semi-integrada, é vedada a alteração dos valores contratuais, exceto para restabelecimento do equilíbrio por caso fortuito ou força maior, por necessidade de alteração do projeto ou das especificações a pedido da Administração, desde que não decorrente de erros ou omissões do contratado, por alteração do projeto nas semi-integradas e por evento superveniente alocado na matriz de riscos como de responsabilidade da Administração.",
 "Nas hipóteses de contratação integrada ou semi-integrada, a alteração dos valores contratuais é livre, e a alteração de projeto decorrente de erros ou omissões do contratado dá ensejo a aumento do valor contratual.",
 "Art. 133, I a IV.","libera alteração de valores","t39d")
P("T39",["134"],"conceito_correto","troca_efeito",3,
 "Os preços contratados serão alterados, para mais ou para menos, conforme o caso, se houver, após a data da apresentação da proposta, criação, alteração ou extinção de quaisquer tributos ou encargos legais ou superveniência de disposições legais, com comprovada repercussão sobre os preços contratados.",
 "Os preços contratados somente serão alterados para mais, e não para menos, se houver, após a apresentação da proposta, criação ou majoração de tributos, independentemente de comprovação de repercussão sobre os preços contratados.",
 "Art. 134.","só para mais e sem comprovação","t39e")
P("T39",["135"],"conceito_correto","troca_numero",5,
 "Nos contratos de serviços contínuos com dedicação exclusiva ou predominância de mão de obra, os preços serão repactuados mediante demonstração analítica da variação dos custos, com data vinculada à da proposta para os custos de mercado e ao acordo, convenção ou dissídio coletivo para os custos de mão de obra; a repactuação observará o interregno mínimo de 1 ano e será precedida de solicitação do contratado, acompanhada da planilha de custos ou do novo acordo, convenção ou sentença normativa.",
 "Nos contratos de serviços contínuos com dedicação exclusiva ou predominância de mão de obra, os preços serão reajustados por índice setorial, com data vinculada à da proposta para todos os custos; a repactuação poderá ocorrer a qualquer tempo, de ofício pela Administração, sem demonstração analítica dos custos.",
 "Art. 135, caput, I e II, §§ 3º e 6º.","confunde repactuação com reajuste","t39f")
P("T39",["135"],"conceito_correto","excecao_omitida",5,
 "A Administração não se vinculará às disposições de acordos, convenções ou dissídios coletivos que tratem de matéria não trabalhista, de participação dos trabalhadores nos lucros ou resultados do contratado, ou que estabeleçam direitos não previstos em lei, e é vedado ao órgão contratante vincular-se às disposições que tratem de obrigações e direitos que somente se aplicam aos contratos com a Administração Pública.",
 "A Administração fica vinculada a todas as disposições de acordos, convenções ou dissídios coletivos de trabalho aplicáveis à categoria do contratado, inclusive as que somente se apliquem aos contratos com a Administração Pública.",
 "Art. 135, §§ 1º e 2º.","vincula a toda convenção","t39g")
P("T39",["136"],"conceito_correto","excecao_omitida",3,
 "Registros que não caracterizam alteração do contrato podem ser realizados por simples apostila, dispensada a celebração de termo aditivo, como a variação do valor contratual para fazer face ao reajuste ou à repactuação previstos no contrato, atualizações e compensações financeiras decorrentes das condições de pagamento, alterações na razão ou denominação social do contratado e empenho de dotações orçamentárias.",
 "Exigem termo aditivo, não podendo ser feitos por simples apostila, a variação do valor contratual decorrente de reajuste previsto no contrato, as alterações na razão social do contratado e o empenho de dotações orçamentárias.",
 "Art. 136, I a IV.","exige aditivo para apostilas","t39h")
# T40
P("T40",["137"],"conceito_correto","excecao_omitida",3,
 "Constituem motivos para extinção do contrato, que deverá ser formalmente motivada nos autos, assegurados o contraditório e a ampla defesa, o não cumprimento ou cumprimento irregular de cláusulas contratuais, o desatendimento das determinações regulares do fiscal, a decretação de falência, a dissolução da sociedade ou o falecimento do contratado, o caso fortuito ou força maior impeditivos da execução e razões de interesse público justificadas pela autoridade máxima do órgão.",
 "Constituem motivos para extinção do contrato, dispensados o contraditório e a ampla defesa quando houver inadimplemento, a decretação de falência, o falecimento do contratado e razões de interesse público justificadas pelo fiscal do contrato.",
 "Art. 137, caput e I a IX.","dispensa defesa e troca autoridade","t40a")
P("T40",["137"],"conceito_correto","troca_numero",5,
 "O contratado terá direito à extinção do contrato quando a Administração suprimir obras, serviços ou compras além do limite do art. 125, suspender a execução por ordem escrita por prazo superior a 3 meses, promover repetidas suspensões que totalizem 90 dias úteis, atrasar por mais de 2 meses, contados da emissão da nota fiscal, os pagamentos devidos ou não liberar área, local ou objeto nos prazos contratuais.",
 "O contratado terá direito à extinção do contrato quando a Administração suprimir obras, serviços ou compras além do limite de 10%, suspender a execução por prazo superior a 6 meses, promover repetidas suspensões que totalizem 30 dias úteis ou atrasar por mais de 15 dias os pagamentos devidos.",
 "Art. 137, § 2º, I a V.","troca prazos","t40b")
P("T40",["137"],"conceito_correto","excecao_omitida",5,
 "As hipóteses de extinção por suspensão superior a 3 meses, repetidas suspensões e atraso de pagamentos superior a 2 meses não serão admitidas em caso de calamidade pública, grave perturbação da ordem interna ou guerra, nem quando decorrerem de ato ou fato que o contratado tenha praticado ou para o qual tenha contribuído, e assegurarão ao contratado o direito de optar pela suspensão do cumprimento das obrigações até a normalização da situação; os emitentes das garantias deverão ser notificados do início do processo de apuração de descumprimento.",
 "As hipóteses de extinção por suspensão superior a 3 meses, repetidas suspensões e atraso de pagamentos serão admitidas inclusive em caso de calamidade pública ou guerra, e o contratado não poderá optar pela suspensão do cumprimento das obrigações; é dispensada a notificação dos emitentes das garantias.",
 "Art. 137, §§ 3º e 4º.","admite em calamidade e dispensa notificação","t40c")
P("T40",["138"],"conceito_correto","excecao_omitida",4,
 "A extinção do contrato poderá ser determinada por ato unilateral e escrito da Administração, exceto no caso de descumprimento decorrente de sua própria conduta; consensual, por acordo entre as partes, por conciliação, mediação ou comitê de resolução de disputas, desde que haja interesse da Administração; ou determinada por decisão arbitral ou judicial.",
 "A extinção do contrato poderá ser determinada por ato unilateral da Administração, inclusive no caso de descumprimento decorrente de sua própria conduta, ou por acordo entre as partes, independentemente de interesse da Administração; é vedada a extinção por decisão arbitral.",
 "Art. 138, I a III.","admite unilateral por culpa da Administração e veda arbitral","t40d")
P("T40",["138"],"conceito_correto","troca_efeito",4,
 "A extinção unilateral e a consensual deverão ser precedidas de autorização escrita e fundamentada da autoridade competente e reduzidas a termo no processo; quando a extinção decorrer de culpa exclusiva da Administração, o contratado será ressarcido pelos prejuízos comprovados e terá direito à devolução da garantia, aos pagamentos devidos pela execução até a data da extinção e ao pagamento do custo da desmobilização.",
 "A extinção unilateral dispensa autorização escrita e fundamentada da autoridade competente; quando a extinção decorrer de culpa exclusiva da Administração, o contratado não terá direito à devolução da garantia nem ao custo da desmobilização.",
 "Art. 138, §§ 1º e 2º.","nega direitos do contratado","t40e")
P("T40",["139"],"conceito_correto","excecao_omitida",4,
 "A extinção determinada por ato unilateral da Administração poderá acarretar, sem prejuízo das sanções, a assunção imediata do objeto no estado e local em que se encontrar, a ocupação e utilização do local, instalações, equipamentos, material e pessoal necessários à continuidade, a execução da garantia contratual e a retenção dos créditos até o limite dos prejuízos e das multas; a ocupação exigirá autorização expressa do ministro de Estado, do secretário estadual ou do secretário municipal competente.",
 "A extinção determinada por ato unilateral da Administração acarretará obrigatoriamente a assunção do objeto e a ocupação de instalações e pessoal do contratado, sem necessidade de autorização, vedadas a execução da garantia e a retenção de créditos.",
 "Art. 139, I a IV e §§ 1º e 2º.","torna obrigatório e veda garantia","t40f")
# T41
P("T41",["140"],"conceito_correto","troca_numero",4,
 "Em obras e serviços, o objeto do contrato será recebido provisoriamente, pelo responsável por seu acompanhamento e fiscalização, em até 15 dias da comunicação escrita do contratado, e definitivamente, por servidor ou comissão designada pela autoridade, mediante termo detalhado que comprove o atendimento das exigências contratuais; o objeto poderá ser rejeitado, no todo ou em parte, quando em desacordo com o contrato.",
 "Em obras e serviços, o objeto do contrato será recebido provisoriamente, pelo contratado, em até 90 dias da conclusão, e definitivamente, pelo fiscal, sem termo detalhado; o objeto não poderá ser rejeitado após o recebimento provisório.",
 "Art. 140, I e § 1º.","troca prazo e agentes","t41a")
P("T41",["140"],"conceito_correto","troca_efeito",5,
 "O recebimento provisório ou definitivo não excluirá a responsabilidade civil pela solidez e pela segurança da obra ou serviço nem a responsabilidade ético-profissional pela perfeita execução do contrato; em se tratando de obra, o recebimento definitivo não eximirá o contratado, pelo prazo mínimo de 5 anos, da responsabilidade objetiva pela solidez e segurança dos materiais e serviços e pela funcionalidade da construção.",
 "O recebimento definitivo exclui a responsabilidade civil do contratado pela solidez e segurança da obra; em se tratando de obra, a responsabilidade do contratado pela solidez e segurança cessa após 1 ano do recebimento definitivo, vedada a previsão de prazo superior no edital.",
 "Art. 140, §§ 2º e 6º.","exclui responsabilidade e reduz prazo","t41b")
P("T41",["140"],"conceito_correto","excecao_omitida",4,
 "Salvo disposição em contrário constante do edital ou de ato normativo, os ensaios, testes e demais provas para aferição da boa execução do objeto exigidos por normas técnicas oficiais correrão por conta do contratado; em se tratando de projeto de obra, o recebimento definitivo não eximirá o projetista ou consultor da responsabilidade objetiva por todos os danos causados por falha de projeto.",
 "Salvo disposição em contrário constante do edital, os ensaios e testes exigidos por normas técnicas correrão por conta da Administração; em se tratando de projeto de obra, o recebimento definitivo eximirá o projetista da responsabilidade por falha de projeto.",
 "Art. 140, §§ 4º e 5º.","inverte custos e responsabilidade do projetista","t41c")
# T42
P("T42",["141"],"conceito_correto","excecao_omitida",4,
 "No dever de pagamento pela Administração, será observada a ordem cronológica para cada fonte diferenciada de recursos, subdividida nas categorias de fornecimento de bens, locações, prestação de serviços e realização de obras; a ordem poderá ser alterada, mediante prévia justificativa da autoridade competente e posterior comunicação ao controle interno e ao tribunal de contas, exclusivamente nas situações previstas em lei.",
 "No dever de pagamento pela Administração, será observada uma única ordem cronológica para todas as fontes de recursos e categorias de contratos, e a ordem poderá ser alterada livremente pela autoridade competente, sem comunicação ao controle interno ou ao tribunal de contas.",
 "Art. 141, caput e § 1º.","ordem única e alteração livre","t42a")
P("T42",["141"],"conceito_correto","excecao_omitida",5,
 "A ordem cronológica de pagamentos poderá ser alterada, entre outras hipóteses legais, em caso de grave perturbação da ordem, emergência ou calamidade pública, para pagamento a microempresa, empresa de pequeno porte, agricultor familiar, produtor rural pessoa física, microempreendedor individual e cooperativa, desde que demonstrado o risco de descontinuidade do objeto, e para pagamento de direitos oriundos de contratos em caso de falência, recuperação judicial ou dissolução da empresa contratada.",
 "A ordem cronológica de pagamentos poderá ser alterada sempre que o credor for microempresa ou empresa de pequeno porte, independentemente de risco de descontinuidade do objeto do contrato, e jamais em caso de falência ou recuperação judicial do contratado.",
 "Art. 141, § 1º, I a V.","generaliza exceção ME/EPP","t42b")
P("T42",["141"],"conceito_correto","troca_efeito",4,
 "A inobservância imotivada da ordem cronológica de pagamentos ensejará a apuração de responsabilidade do agente responsável, cabendo aos órgãos de controle a sua fiscalização, e o órgão ou entidade deverá disponibilizar, mensalmente, em seção específica de acesso à informação em seu sítio, a ordem cronológica de seus pagamentos e as justificativas de eventual alteração.",
 "A inobservância imotivada da ordem cronológica de pagamentos não enseja apuração de responsabilidade, e a divulgação da ordem de pagamentos e de suas alterações é facultativa e anual.",
 "Art. 141, §§ 2º e 3º.","afasta responsabilidade e torna divulgação facultativa","t42c")
P("T42",["142","143"],"conceito_correto","excecao_omitida",3,
 "Disposição expressa no edital ou no contrato poderá prever pagamento em conta vinculada ou pagamento pela efetiva comprovação do fato gerador; e, no caso de controvérsia sobre a execução do objeto quanto à dimensão, qualidade e quantidade, a parcela incontroversa deverá ser liberada no prazo previsto para pagamento.",
 "No caso de controvérsia sobre a execução do objeto quanto à dimensão, qualidade e quantidade, nenhum pagamento será liberado até a solução da controvérsia; e é vedado prever pagamento em conta vinculada.",
 "Arts. 142 e 143.","retém parcela incontroversa","t42d")
P("T42",["144"],"conceito_correto","excecao_omitida",4,
 "Na contratação de obras, fornecimentos e serviços, inclusive de engenharia, poderá ser estabelecida remuneração variável vinculada ao desempenho do contratado, com base em metas, padrões de qualidade, critérios de sustentabilidade ambiental e prazos de entrega definidos no edital e no contrato; sua utilização será motivada e respeitará o limite orçamentário fixado pela Administração.",
 "Na contratação de obras, fornecimentos e serviços, a remuneração variável vinculada ao desempenho do contratado é vedada, ainda que prevista no edital, por ofensa ao limite orçamentário.",
 "Art. 144, caput e § 2º.","veda remuneração variável","t42e")
P("T42",["145"],"conceito_correto","excecao_omitida",5,
 "Não será permitido pagamento antecipado, parcial ou total, relativo a parcelas contratuais vinculadas ao fornecimento de bens, à execução de obras ou à prestação de serviços, salvo se a antecipação propiciar sensível economia de recursos ou representar condição indispensável para a obtenção do bem ou para a prestação do serviço, previamente justificada no processo e expressamente prevista no edital; a Administração poderá exigir garantia adicional, e, se o objeto não for executado no prazo, o valor antecipado deverá ser devolvido.",
 "É permitido pagamento antecipado, parcial ou total, quando o contratado o requerer, independentemente de previsão no edital; a Administração não poderá exigir garantia adicional e, se o objeto não for executado, o valor antecipado será compensado em futuros contratos.",
 "Art. 145, caput e §§ 1º a 3º.","libera antecipação","t42f")
# T43
P("T43",["147"],"conceito_correto","troca_efeito",4,
 "Constatada irregularidade no procedimento licitatório ou na execução contratual, caso não seja possível o saneamento, a decisão sobre a suspensão da execução ou a declaração de nulidade do contrato somente será adotada se se revelar medida de interesse público, com avaliação, entre outros aspectos, dos impactos econômicos e financeiros do atraso, dos riscos sociais e ambientais, do custo da deterioração das parcelas executadas e do custo para nova licitação.",
 "Constatada irregularidade no procedimento licitatório ou na execução contratual, a nulidade do contrato será sempre declarada, independentemente de avaliação do interesse público, do custo da deterioração das parcelas executadas e do custo para nova licitação.",
 "Art. 147, caput e I a XI.","nulidade automática","t43a")
P("T43",["147","148"],"conceito_correto","excecao_omitida",4,
 "Caso a paralisação ou anulação não se revele medida de interesse público, o poder público deverá optar pela continuidade do contrato e pela solução da irregularidade por meio de indenização por perdas e danos, sem prejuízo da apuração de responsabilidade e da aplicação de penalidades cabíveis; se não for possível o retorno à situação fática anterior, a nulidade será resolvida pela indenização por perdas e danos.",
 "Caso a paralisação ou anulação não se revele medida de interesse público, o poder público deverá, ainda assim, declarar a nulidade do contrato, vedada a solução da irregularidade por indenização por perdas e danos e a apuração de responsabilidade.",
 "Art. 147, parágrafo único, e art. 148, § 1º.","veda indenização","t43b")
P("T43",["148","149"],"conceito_correto","troca_numero",5,
 "A declaração de nulidade do contrato operará retroativamente, impedindo os efeitos jurídicos que o contrato deveria produzir ordinariamente e desconstituindo os já produzidos; a autoridade poderá decidir que ela só tenha eficácia em momento futuro, suficiente para efetuar nova contratação, por prazo de até 6 meses, prorrogável uma única vez; e a nulidade não exonerará a Administração do dever de indenizar o contratado pelo que houver executado até a data em que for declarada ou tornada eficaz, desde que não lhe seja imputável.",
 "A declaração de nulidade do contrato operará apenas a partir da decisão, preservando os efeitos já produzidos; a autoridade poderá postergar sua eficácia por até 2 anos, prorrogável por tempo indeterminado; e a nulidade exonera a Administração do dever de indenizar o contratado pelo que houver executado.",
 "Art. 148, caput e § 2º; art. 149.","troca eficácia e prazo e exonera indenização","t43c")
P("T43",["150"],"conceito_correto","excecao_omitida",3,
 "Nenhuma contratação será feita sem a caracterização adequada de seu objeto e sem a indicação dos créditos orçamentários para pagamento das parcelas contratuais vincendas no exercício em que for realizada a contratação, sob pena de nulidade do ato e de responsabilização de quem lhe tiver dado causa.",
 "A contratação poderá ser feita sem a indicação de créditos orçamentários para pagamento das parcelas vincendas no exercício da contratação, desde que o objeto esteja adequadamente caracterizado, sem prejuízo de responsabilização posterior.",
 "Art. 150.","dispensa crédito orçamentário","t43d")
# T44
P("T44",["151","152","153","154"],"conceito_correto","excecao_omitida",4,
 "Nas contratações regidas pela Lei n.º 14.133/2021, poderão ser utilizados meios alternativos de prevenção e resolução de controvérsias, notadamente a conciliação, a mediação, o comitê de resolução de disputas e a arbitragem, aplicáveis às controvérsias relacionadas a direitos patrimoniais disponíveis, como o restabelecimento do equilíbrio econômico-financeiro, o inadimplemento de obrigações e o cálculo de indenizações; a arbitragem será sempre de direito e observará o princípio da publicidade.",
 "Nas contratações regidas pela Lei n.º 14.133/2021, a arbitragem é vedada, por tratar de interesse público indisponível; admitem-se apenas conciliação e mediação, e a arbitragem, se instaurada, será de equidade e sigilosa.",
 "Arts. 151 a 154.","veda arbitragem e troca direito por equidade","t44a")
P("T44",["153","154"],"conceito_correto","excecao_omitida",3,
 "Os contratos poderão ser aditados para permitir a adoção dos meios alternativos de resolução de controvérsias, e o processo de escolha dos árbitros, dos colegiados arbitrais e dos comitês de resolução de disputas observará critérios isonômicos, técnicos e transparentes.",
 "Os contratos já celebrados não poderão ser aditados para permitir a adoção dos meios alternativos de resolução de controvérsias, e a escolha dos árbitros e dos comitês será livre, a critério da Administração.",
 "Arts. 153 e 154.","veda aditivo e escolha livre","t44b")
# T45
P("T45",["155"],"conceito_correto","excecao_omitida",3,
 "O licitante ou o contratado será responsabilizado administrativamente, entre outras infrações, por dar causa à inexecução parcial ou total do contrato, deixar de entregar a documentação exigida, não manter a proposta salvo fato superveniente justificado, não celebrar o contrato quando convocado dentro do prazo de validade da proposta, apresentar declaração ou documentação falsa, fraudar a licitação, comportar-se de modo inidôneo e praticar ato lesivo previsto no art. 5º da Lei n.º 12.846/2013.",
 "O licitante ou o contratado somente será responsabilizado administrativamente por dar causa à inexecução total do contrato e por fraudar a licitação, não sendo infração a apresentação de declaração falsa nem o ato lesivo previsto na Lei n.º 12.846/2013.",
 "Art. 155, I a XII.","reduz rol de infrações","t45a")
P("T45",["156"],"conceito_correto","excecao_omitida",3,
 "Serão aplicadas ao responsável pelas infrações administrativas previstas na lei as sanções de advertência, multa, impedimento de licitar e contratar e declaração de inidoneidade para licitar ou contratar; na aplicação, serão considerados a natureza e a gravidade da infração, as peculiaridades do caso, as circunstâncias agravantes ou atenuantes, os danos à Administração e a implantação ou aperfeiçoamento de programa de integridade.",
 "Serão aplicadas ao responsável pelas infrações administrativas as sanções de advertência, multa, suspensão temporária de participação em licitação e declaração de inidoneidade; na aplicação, será considerado apenas o valor do dano causado à Administração.",
 "Art. 156, caput e § 1º.","troca suspensão por impedimento e reduz critérios","t45b")
P("T45",["156"],"conceito_correto","excecao_omitida",4,
 "A advertência será aplicada exclusivamente pela infração de dar causa à inexecução parcial do contrato, quando não se justificar a imposição de penalidade mais grave.",
 "A advertência será aplicada pela infração de dar causa à inexecução total do contrato e pela apresentação de documentação falsa, quando não se justificar penalidade mais grave.",
 "Art. 156, § 2º.","amplia advertência","t45c")
P("T45",["156"],"conceito_correto","troca_numero",5,
 "A multa, calculada na forma do edital ou do contrato, não poderá ser inferior a 0,5% nem superior a 30% do valor do contrato licitado ou celebrado com contratação direta e será aplicada ao responsável por qualquer das infrações administrativas previstas no art. 155.",
 "A multa, calculada na forma do edital ou do contrato, não poderá ser inferior a 1% nem superior a 20% do valor do contrato, e será aplicada apenas ao responsável pelas infrações mais graves previstas no art. 155.",
 "Art. 156, § 3º.","troca faixa da multa","t45d")
P("T45",["156"],"conceito_correto","troca_numero",5,
 "A sanção de impedimento de licitar e contratar impedirá o responsável de licitar ou contratar no âmbito da Administração direta e indireta do ente federativo que tiver aplicado a sanção, pelo prazo máximo de 3 anos; a declaração de inidoneidade impedirá o responsável de licitar ou contratar no âmbito da Administração de todos os entes federativos, pelo prazo mínimo de 3 anos e máximo de 6 anos.",
 "A sanção de impedimento de licitar e contratar impedirá o responsável de licitar ou contratar no âmbito de todos os entes federativos, pelo prazo máximo de 5 anos; a declaração de inidoneidade impedirá o responsável de licitar ou contratar no âmbito do ente que a aplicou, pelo prazo mínimo de 1 ano e máximo de 3 anos.",
 "Art. 156, §§ 4º e 5º.","inverte abrangência e prazos","t45e")
P("T45",["156"],"conceito_correto","troca_autoridade",5,
 "A declaração de inidoneidade será precedida de análise jurídica; quando aplicada por órgão do Poder Executivo, será de competência exclusiva de ministro de Estado, secretário estadual ou secretário municipal e, quando aplicada por autarquia ou fundação, de competência exclusiva da autoridade máxima da entidade; nos Poderes Legislativo e Judiciário, será de autoridade de nível hierárquico equivalente, na forma de regulamento.",
 "A declaração de inidoneidade dispensa análise jurídica e poderá ser aplicada pelo agente de contratação ou pelo fiscal do contrato; nos Poderes Legislativo e Judiciário, será aplicada pelo ordenador de despesas.",
 "Art. 156, § 6º.","troca autoridade competente","t45f")
P("T45",["156"],"conceito_correto","excecao_omitida",4,
 "As sanções de advertência, impedimento de licitar e contratar e declaração de inidoneidade poderão ser aplicadas cumulativamente com a multa; se a multa e as indenizações forem superiores ao valor de pagamento eventualmente devido ao contratado, a diferença será descontada da garantia ou cobrada judicialmente; e a aplicação das sanções não exclui, em hipótese alguma, a obrigação de reparação integral do dano.",
 "As sanções de advertência, impedimento de licitar e declaração de inidoneidade não poderão ser aplicadas cumulativamente com a multa; e, aplicadas as sanções, fica excluída a obrigação de reparação integral do dano à Administração.",
 "Art. 156, §§ 7º a 9º.","veda cumulação e exclui reparação","t45g")
# T46
P("T46",["157","158"],"conceito_correto","troca_numero",5,
 "Na aplicação da multa, será facultada a defesa do interessado no prazo de 15 dias úteis, contado da intimação; a aplicação das sanções de impedimento de licitar e de declaração de inidoneidade requererá processo de responsabilização conduzido por comissão de 2 ou mais servidores estáveis, que intimará o licitante ou contratado para, no prazo de 15 dias úteis, apresentar defesa escrita e especificar as provas que pretenda produzir.",
 "Na aplicação da multa, será facultada a defesa do interessado no prazo de 5 dias úteis; a aplicação das sanções de impedimento e de inidoneidade será decidida pela autoridade, dispensado processo de responsabilização conduzido por comissão, bastando intimação para defesa em 3 dias úteis.",
 "Arts. 157 e 158.","troca prazos e dispensa comissão","t46a")
P("T46",["158"],"conceito_correto","excecao_omitida",5,
 "Em órgão cujo quadro funcional não seja formado de servidores estatutários, a comissão do processo de responsabilização será composta de 2 ou mais empregados públicos dos quadros permanentes, preferencialmente com no mínimo 3 anos de tempo de serviço; deferida a produção de novas provas, o licitante poderá apresentar alegações finais em 15 dias úteis; e serão indeferidas, mediante decisão fundamentada, provas ilícitas, impertinentes, desnecessárias, protelatórias ou intempestivas.",
 "Em órgão cujo quadro funcional não seja formado de servidores estatutários, a comissão será composta de empregados contratados temporariamente; deferida a produção de novas provas, não haverá alegações finais; e as provas serão indeferidas livremente, sem necessidade de fundamentação.",
 "Art. 158, §§ 1º a 3º.","troca composição e dispensa fundamentação","t46b")
P("T46",["158"],"conceito_correto","troca_numero",5,
 "A prescrição das infrações administrativas ocorrerá em 5 anos, contados da ciência da infração pela Administração, e será interrompida pela instauração do processo de responsabilização, suspensa pela celebração de acordo de leniência da Lei n.º 12.846/2013 e suspensa por decisão judicial que inviabilize a conclusão da apuração administrativa.",
 "A prescrição das infrações administrativas ocorrerá em 10 anos, contados da prática da infração, e será suspensa pela instauração do processo de responsabilização e interrompida pela celebração de acordo de leniência.",
 "Art. 158, § 4º.","troca prazo e termos","t46c")
P("T46",["159","160"],"conceito_correto","excecao_omitida",4,
 "Os atos previstos como infrações administrativas na Lei n.º 14.133/2021 que também sejam tipificados como atos lesivos na Lei n.º 12.846/2013 serão apurados e julgados conjuntamente, nos mesmos autos, observados o rito e a autoridade competente definidos naquela Lei; a personalidade jurídica poderá ser desconsiderada quando utilizada com abuso do direito para facilitar, encobrir ou dissimular a prática dos atos ilícitos ou provocar confusão patrimonial, observados o contraditório, a ampla defesa e a análise jurídica prévia.",
 "Os atos previstos como infrações administrativas na Lei n.º 14.133/2021 que também sejam tipificados como atos lesivos na Lei n.º 12.846/2013 serão apurados em processos separados, observado o rito da Lei de Licitações; a desconsideração da personalidade jurídica depende de decisão judicial e não alcança sócios nem empresas coligadas.",
 "Arts. 159 e 160.","separa apuração e restringe desconsideração","t46d")
P("T46",["161"],"conceito_correto","troca_numero",4,
 "Os órgãos e entidades dos Poderes Executivo, Legislativo e Judiciário de todos os entes federativos deverão, no prazo máximo de 15 dias úteis, contado da data de aplicação da sanção, informar e manter atualizados os dados relativos às sanções para fins de publicidade no Ceis e no Cnep.",
 "Apenas os órgãos do Poder Executivo federal deverão informar as sanções aplicadas ao Ceis e ao Cnep, no prazo de 60 dias corridos, contado da data de aplicação da sanção.",
 "Art. 161.","restringe e troca prazo","t46e")
# T47
P("T47",["162"],"conceito_correto","excecao_omitida",3,
 "O atraso injustificado na execução do contrato sujeitará o contratado a multa de mora, na forma prevista em edital ou contrato; a aplicação de multa de mora não impedirá que a Administração a converta em compensatória e promova a extinção unilateral do contrato com a aplicação cumulada de outras sanções.",
 "O atraso injustificado na execução do contrato sujeitará o contratado a multa de mora, que, uma vez aplicada, impede a Administração de convertê-la em compensatória e de promover a extinção unilateral do contrato.",
 "Art. 162.","impede conversão","t47a")
P("T47",["163"],"conceito_correto","troca_numero",5,
 "É admitida a reabilitação do licitante ou contratado perante a própria autoridade que aplicou a penalidade, exigidos, cumulativamente, a reparação integral do dano, o pagamento da multa, o transcurso do prazo mínimo de 1 ano da aplicação, no caso de impedimento, ou de 3 anos, no caso de inidoneidade, o cumprimento das condições definidas no ato punitivo e a análise jurídica prévia.",
 "É admitida a reabilitação do licitante ou contratado perante a autoridade superior à que aplicou a penalidade, exigidos, alternativamente, a reparação do dano ou o pagamento da multa, e o transcurso do prazo mínimo de 3 anos, no caso de impedimento, ou de 6 anos, no caso de inidoneidade.",
 "Art. 163, I a V.","troca autoridade e prazos","t47b")
P("T47",["163"],"conceito_correto","excecao_omitida",5,
 "A sanção pelas infrações de apresentar declaração ou documentação falsa e de praticar ato lesivo previsto no art. 5º da Lei n.º 12.846/2013 exigirá, como condição de reabilitação, a implantação ou aperfeiçoamento de programa de integridade pelo responsável.",
 "A sanção pelas infrações de dar causa à inexecução parcial do contrato e de não manter a proposta exigirá, como condição de reabilitação, a implantação de programa de integridade pelo responsável.",
 "Art. 163, parágrafo único.","troca infrações","t47c")
# T48
P("T48",["164"],"conceito_correto","troca_numero",4,
 "Qualquer pessoa é parte legítima para impugnar edital de licitação por irregularidade na aplicação da lei ou para solicitar esclarecimento sobre seus termos, devendo protocolar o pedido até 3 dias úteis antes da data de abertura do certame; a resposta será divulgada em sítio eletrônico oficial no prazo de até 3 dias úteis, limitado ao último dia útil anterior à data da abertura.",
 "Somente o licitante é parte legítima para impugnar edital de licitação, devendo protocolar o pedido até 10 dias úteis antes da data de abertura do certame; a resposta será divulgada em até 5 dias úteis, ainda que após a abertura do certame.",
 "Art. 164 e parágrafo único.","restringe legitimidade e troca prazos","t48a")
P("T48",["165"],"conceito_correto","troca_numero",4,
 "Dos atos da Administração decorrentes da aplicação da lei cabem recurso, no prazo de 3 dias úteis, contado da intimação ou da lavratura da ata, em face, entre outros, do julgamento das propostas, do ato de habilitação ou inabilitação e da anulação ou revogação da licitação, e pedido de reconsideração, no prazo de 3 dias úteis, relativamente a ato do qual não caiba recurso hierárquico.",
 "Dos atos da Administração decorrentes da aplicação da lei cabem recurso, no prazo de 10 dias úteis, em face do julgamento das propostas e do ato de habilitação, e pedido de reconsideração, no prazo de 15 dias úteis, relativamente a ato do qual caiba recurso hierárquico.",
 "Art. 165, I e II.","troca prazos","t48b")
P("T48",["165"],"conceito_correto","excecao_omitida",5,
 "Quanto ao recurso contra o julgamento das propostas ou a habilitação, a intenção de recorrer deverá ser manifestada imediatamente, sob pena de preclusão, e a apreciação dar-se-á em fase única; o recurso será dirigido à autoridade que editou o ato, que, se não reconsiderar em 3 dias úteis, o encaminhará à autoridade superior, a qual decidirá em até 10 dias úteis, contado do recebimento dos autos.",
 "Quanto ao recurso contra o julgamento das propostas ou a habilitação, a intenção de recorrer poderá ser manifestada no prazo do recurso, sem risco de preclusão, e a apreciação dar-se-á em fases sucessivas; o recurso será dirigido diretamente à autoridade superior, que decidirá em até 30 dias úteis.",
 "Art. 165, §§ 1º e 2º.","remove preclusão e troca autoridade","t48c")
P("T48",["165"],"conceito_correto","troca_efeito",4,
 "O acolhimento do recurso implicará invalidação apenas de ato insuscetível de aproveitamento; o prazo para contrarrazões será o mesmo do recurso e terá início na data de intimação pessoal ou de divulgação da interposição; e será assegurado ao licitante vista dos elementos indispensáveis à defesa de seus interesses.",
 "O acolhimento do recurso implicará invalidação de todos os atos do processo licitatório; o prazo para contrarrazões será de 24 horas; e a vista dos autos dependerá de autorização da autoridade julgadora.",
 "Art. 165, §§ 3º a 5º.","invalida todos os atos","t48d")
P("T48",["166","167"],"conceito_correto","troca_numero",5,
 "Da aplicação das sanções de advertência, multa e impedimento de licitar e contratar caberá recurso no prazo de 15 dias úteis, contado da intimação, a ser reconsiderado em 5 dias úteis ou encaminhado à autoridade superior, que decidirá em até 20 dias úteis; da declaração de inidoneidade caberá apenas pedido de reconsideração, no prazo de 15 dias úteis, decidido em até 20 dias úteis.",
 "Da aplicação das sanções de advertência, multa e impedimento de licitar e contratar caberá recurso no prazo de 3 dias úteis, decidido em até 10 dias úteis; da declaração de inidoneidade caberá recurso hierárquico, no prazo de 15 dias úteis, decidido em até 60 dias úteis.",
 "Arts. 166 e 167.","troca prazos e meio de impugnação","t48e")
P("T48",["168"],"conceito_correto","troca_efeito",3,
 "O recurso e o pedido de reconsideração terão efeito suspensivo do ato ou da decisão recorrida até que sobrevenha decisão final da autoridade competente, que será auxiliada pelo órgão de assessoramento jurídico na elaboração de suas decisões.",
 "O recurso e o pedido de reconsideração terão efeito apenas devolutivo, não suspendendo o ato ou a decisão recorrida, e a autoridade competente decidirá sem auxílio do órgão de assessoramento jurídico.",
 "Art. 168.","retira efeito suspensivo","t48f")
P("T48",["166"],"caso_concreto","caso_concreto",5,
 "Empresa contratada sofre multa por atraso na execução do contrato. Intimada, ela poderá interpor recurso no prazo de 15 dias úteis, contado da intimação, dirigido à autoridade que proferiu a decisão, que, se não reconsiderar em 5 dias úteis, o encaminhará à autoridade superior.",
 "Empresa contratada sofre declaração de inidoneidade por fraude na execução do contrato. Intimada, ela poderá interpor recurso hierárquico no prazo de 3 dias úteis, dirigido à autoridade superior à que proferiu a decisão.",
 "Arts. 166 e 167.","aplica recurso à inidoneidade","t48g")
# T49
P("T49",["169"],"conceito_correto","excecao_omitida",4,
 "As contratações públicas deverão submeter-se a práticas contínuas e permanentes de gestão de riscos e de controle preventivo, subordinadas ao controle social e às linhas de defesa: a primeira, integrada por servidores, empregados públicos, agentes de licitação e autoridades da governança do órgão; a segunda, pelas unidades de assessoramento jurídico e de controle interno do próprio órgão; e a terceira, pelo órgão central de controle interno da Administração e pelo tribunal de contas.",
 "As contratações públicas deverão submeter-se a práticas de gestão de riscos e de controle preventivo, subordinadas às linhas de defesa: a primeira, integrada pelo órgão central de controle interno e pelo tribunal de contas; a segunda, pelos servidores e agentes de licitação; e a terceira, pelas unidades de assessoramento jurídico do próprio órgão.",
 "Art. 169, I a III.","inverte linhas de defesa","t49a")
P("T49",["169"],"conceito_correto","excecao_omitida",5,
 "Constatada simples impropriedade formal, os integrantes das linhas de defesa adotarão medidas para o seu saneamento e a mitigação de riscos de nova ocorrência; constatada irregularidade que configure dano à Administração, adotarão as providências para apuração das infrações administrativas, observadas a segregação de funções e a individualização das condutas, e remeterão ao Ministério Público cópias dos documentos cabíveis; os órgãos de controle terão acesso irrestrito aos documentos, inclusive os classificados, tornando-se corresponsáveis pelo sigilo.",
 "Constatada simples impropriedade formal, os integrantes das linhas de defesa deverão instaurar processo sancionador contra o agente; constatada irregularidade que configure dano, aguardarão decisão do tribunal de contas antes de qualquer providência; os órgãos de controle não terão acesso a documentos classificados.",
 "Art. 169, §§ 2º e 3º.","impropriedade formal gera sanção; nega acesso","t49b")
P("T49",["170"],"conceito_correto","excecao_omitida",4,
 "Os órgãos de controle adotarão, na fiscalização, critérios de oportunidade, materialidade, relevância e risco e considerarão as razões apresentadas pelos órgãos e entidades responsáveis e os resultados obtidos com a contratação; as razões deverão ser encaminhadas até a conclusão da fase de instrução e não poderão ser desentranhadas dos autos; e a omissão na prestação das informações não impedirá as deliberações do controle nem retardará seus prazos.",
 "Os órgãos de controle adotarão, na fiscalização, apenas o critério de legalidade estrita, desconsiderando os resultados obtidos com a contratação; as razões dos gestores poderão ser desentranhadas dos autos; e a omissão na prestação das informações suspenderá os prazos do controle.",
 "Art. 170, caput e §§ 1º e 2º.","troca critérios e efeito da omissão","t49c")
P("T49",["171"],"conceito_correto","troca_numero",5,
 "Ao suspender cautelarmente o processo licitatório, o tribunal de contas deverá pronunciar-se definitivamente sobre o mérito da irregularidade no prazo de 25 dias úteis, contado do recebimento das informações, prorrogável por igual período uma única vez; o órgão intimado da suspensão deverá, no prazo de 10 dias úteis, admitida a prorrogação, informar as medidas adotadas, prestar as informações cabíveis e apurar responsabilidade, se for o caso.",
 "Ao suspender cautelarmente o processo licitatório, o tribunal de contas deverá pronunciar-se definitivamente sobre o mérito no prazo de 90 dias corridos, prorrogável indefinidamente; o órgão intimado da suspensão terá o prazo de 3 dias úteis, improrrogável, para informar as medidas adotadas.",
 "Art. 171, §§ 1º e 2º.","troca prazos","t49d")
P("T49",["170"],"conceito_correto","troca_efeito",3,
 "Qualquer licitante, contratado ou pessoa física ou jurídica poderá representar aos órgãos de controle interno ou ao tribunal de contas competente contra irregularidades na aplicação da Lei n.º 14.133/2021.",
 "Somente o licitante e o contratado poderão representar aos órgãos de controle interno ou ao tribunal de contas contra irregularidades na aplicação da Lei n.º 14.133/2021, vedada a representação por qualquer outra pessoa.",
 "Art. 170, § 4º.","restringe legitimidade","t49e")
# T50
P("T50",["174"],"conceito_correto","excecao_omitida",3,
 "O Portal Nacional de Contratações Públicas (PNCP) é sítio eletrônico oficial destinado à divulgação centralizada e obrigatória dos atos exigidos pela lei e à realização facultativa das contratações pelos órgãos e entidades dos Poderes Executivo, Legislativo e Judiciário de todos os entes federativos.",
 "O Portal Nacional de Contratações Públicas (PNCP) é sítio eletrônico oficial destinado à divulgação facultativa dos atos exigidos pela lei e à realização obrigatória das contratações pelos órgãos do Poder Executivo federal.",
 "Art. 174, I e II.","inverte obrigatório e facultativo","t50a")
P("T50",["174"],"conceito_correto","troca_numero",4,
 "O PNCP será gerido pelo Comitê Gestor da Rede Nacional de Contratações Públicas, presidido por representante indicado pelo Presidente da República e composto de 3 representantes da União, 2 dos Estados e do Distrito Federal, indicados pelo Conselho Nacional de Secretários de Estado da Administração, e 2 dos Municípios, indicados pela Confederação Nacional de Municípios.",
 "O PNCP será gerido pelo Comitê Gestor da Rede Nacional de Contratações Públicas, presidido por representante do Tribunal de Contas da União e composto de 2 representantes da União, 3 dos Estados e do Distrito Federal e 3 dos Municípios, indicados pelo Presidente da República.",
 "Art. 174, § 1º.","troca composição","t50b")
P("T50",["174"],"conceito_correto","excecao_omitida",3,
 "O PNCP conterá, entre outras, as informações sobre planos de contratação anuais, catálogos eletrônicos de padronização, editais de credenciamento e de pré-qualificação, avisos de contratação direta, editais de licitação, atas de registro de preços, contratos e termos aditivos e notas fiscais eletrônicas, e adotará o formato de dados abertos.",
 "O PNCP conterá apenas os editais de licitação e os contratos celebrados, vedada a inclusão de planos de contratação anuais, atas de registro de preços e notas fiscais eletrônicas, e adotará formato de dados fechados.",
 "Art. 174, §§ 2º e 4º.","restringe conteúdo","t50c")
P("T50",["175","176"],"conceito_correto","excecao_omitida",4,
 "Os entes federativos poderão instituir sítio eletrônico oficial para divulgação complementar e realização das respectivas contratações, e, desde que mantida a integração com o PNCP, as contratações poderão ser realizadas por meio de sistema eletrônico fornecido por pessoa jurídica de direito privado, na forma de regulamento; os Municípios com até 20.000 habitantes tinham o prazo de 6 anos, contado da publicação da lei, para cumprimento de determinados requisitos, como a licitação eletrônica e a divulgação em sítio eletrônico oficial.",
 "Os entes federativos não poderão instituir sítio eletrônico próprio, devendo utilizar exclusivamente o PNCP, e as contratações não poderão ser realizadas por sistema eletrônico fornecido por pessoa jurídica de direito privado.",
 "Arts. 175 e 176.","veda sítio próprio e sistema privado","t50d")
P("T50",["181"],"conceito_correto","excecao_omitida",3,
 "Os entes federativos instituirão centrais de compras, com o objetivo de realizar compras em grande escala, para atender a diversos órgãos e entidades sob sua competência; no caso de Municípios com até 10.000 habitantes, serão preferencialmente constituídos consórcios públicos para essa finalidade.",
 "A instituição de centrais de compras é facultativa e restrita à União; no caso de Municípios com até 10.000 habitantes, é vedada a constituição de consórcios públicos para a realização de compras.",
 "Art. 181 e parágrafo único.","torna facultativo e veda consórcios","t50e")
P("T50",["182"],"conceito_correto","troca_autoridade",4,
 "O Poder Executivo federal atualizará, a cada dia 1º de janeiro, pelo IPCA-E ou por índice que venha a substituí-lo, os valores fixados pela lei, os quais serão divulgados no PNCP.",
 "O Tribunal de Contas da União atualizará, a cada dia 1º de julho, pelo IGP-M, os valores fixados pela lei, os quais serão divulgados no Diário Oficial da União.",
 "Art. 182.","troca autoridade, data e índice","t50f")
P("T50",["183"],"conceito_correto","excecao_omitida",4,
 "Os prazos previstos na lei serão contados com exclusão do dia do começo e inclusão do dia do vencimento; os prazos em dias úteis computam somente os dias em que ocorrer expediente administrativo no órgão competente; e, salvo disposição em contrário, considera-se dia do começo do prazo o primeiro dia útil seguinte ao da disponibilização da informação na internet.",
 "Os prazos previstos na lei serão contados com inclusão do dia do começo e exclusão do dia do vencimento; os prazos em dias úteis computam todos os dias da semana, exceto domingos; e considera-se dia do começo do prazo o próprio dia da disponibilização da informação na internet.",
 "Art. 183, caput, III e § 1º, I.","inverte contagem","t50g")
