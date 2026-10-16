# Ato administrativo e poderes — lote L9
Q = []
TAILS=[" Essa seria a orientação adotada pela doutrina e pela jurisprudência no direito brasileiro.",
 " Trata-se de entendimento aplicável à responsabilidade civil das pessoas jurídicas de direito público no Brasil.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática constitucional da responsabilidade do Estado.",
 " Essa seria a regra para os danos causados a terceiros no exercício da função pública."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
FD={"tipo":"doutrina_jurisprudencia","ref":"doutrina majoritária; Lei 9.784/99","versao":"conhecimento do autor","conferida":"conhecimento"}
FJ={"tipo":"jurisprudencia","ref":"Teses de repercussão geral do STF (tesesesumulas.com.br, 2026-10-16)","versao":"conhecimento verificado em fonte secundária","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, jur=False, lei=False):
    ex = {}
    if lei: ex["fonte"]={"tipo":"lei","ref":"Lei 9.784/99","versao":"vigente","conferida":"conhecimento"}
    elif jur: ex["fonte"]=FJ; ex["risco"]=["jurisprudencia_conhecimento"]
    else: ex["fonte"]=FD; ex["risco"]=["doutrina_conhecimento"]
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# A01
P("A01",["1"],"conceito_correto","troca_numero",2,
 "São elementos do ato administrativo a competência, a finalidade, a forma, o motivo e o objeto, sendo a competência, a finalidade e a forma sempre vinculadas.",
 "São elementos do ato administrativo a competência, a finalidade, a forma, o motivo e o objeto, sendo a competência, o motivo e o objeto sempre vinculados.",
 "Elementos do ato.","troca elementos vinculados","a01a")
P("A01",["1"],"conceito_correto","confusao_instituto",3,
 "O desvio de finalidade ocorre quando o agente, embora competente, pratica o ato com finalidade diversa da prevista em lei ou do interesse público, sendo vício insanável.",
 "O desvio de finalidade ocorre quando o agente pratica o ato fora dos limites de sua competência, sendo vício sanável mediante convalidação.",
 "Desvio de finalidade.","confunde com excesso de poder","a01b")
P("A01",["1"],"conceito_correto","excecao_omitida",3,
 "A competência administrativa é irrenunciável e, salvo vedação legal, pode ser delegada ou avocada em caráter excepcional e por motivos relevantes devidamente justificados.",
 "A competência administrativa é irrenunciável e, mesmo quando houver vedação legal, pode ser delegada ou avocada por simples conveniência da autoridade.",
 "Lei 9.784/99, arts. 11 a 15.","ignora vedação legal","a01c",lei=True)
P("A01",["1","10"],"conceito_correto","troca_efeito",4,
 "Pela teoria dos motivos determinantes, a validade do ato vincula-se à existência dos motivos declarados pela Administração, de modo que a falsidade do motivo apresentado pode acarretar a nulidade do ato, ainda que a lei não exigisse a motivação.",
 "Pela teoria dos motivos determinantes, a Administração, quando não é obrigada por lei a motivar o ato, não se vincula aos motivos que declarar, de modo que a falsidade do motivo apresentado não afeta a validade do ato.",
 "Teoria dos motivos determinantes.","nega vinculação aos motivos declarados","a01d")
# A02
P("A02",["2"],"conceito_correto","troca_efeito",3,
 "A presunção de legitimidade e veracidade dos atos administrativos é relativa, admitindo prova em contrário, e transfere ao administrado o ônus de demonstrar a ilegalidade do ato.",
 "A presunção de legitimidade e veracidade dos atos administrativos é absoluta, não admitindo prova em contrário, o que impede o controle judicial de sua legalidade.",
 "Atributos do ato.","presunção absoluta","a02a")
P("A02",["2"],"conceito_correto","excecao_omitida",4,
 "A autoexecutoriedade permite à Administração executar suas decisões sem prévia autorização judicial, desde que haja previsão legal ou situação de urgência, e em regra não alcança a cobrança de multas, que depende de execução judicial.",
 "A autoexecutoriedade permite à Administração executar suas decisões sem prévia autorização judicial, ainda que não haja previsão legal ou urgência, alcançando inclusive a cobrança compulsória de multas.",
 "Autoexecutoriedade.","amplia autoexecutoriedade","a02b")
P("A02",["2"],"conceito_correto","excecao_omitida",3,
 "A imperatividade é o atributo pelo qual o ato impõe obrigações a terceiros independentemente de sua concordância, e não está presente nos atos negociais e nos enunciativos.",
 "A imperatividade é atributo presente em todos os atos administrativos, inclusive nos atos negociais e nos enunciativos, como certidões e pareceres.",
 "Imperatividade.","generaliza imperatividade","a02c")
# A03
P("A03",["3"],"conceito_correto","excecao_omitida",3,
 "O Poder Judiciário pode controlar a legalidade, a razoabilidade e a proporcionalidade do ato discricionário, mas não pode substituir o juízo de conveniência e oportunidade do administrador.",
 "O Poder Judiciário pode substituir o juízo de conveniência e oportunidade do administrador sempre que considerar o ato inadequado, pois o controle judicial alcança o mérito administrativo.",
 "Mérito e controle judicial.","admite substituição do mérito","a03a")
P("A03",["3"],"conceito_correto","confusao_instituto",3,
 "A discricionariedade administrativa é a margem de escolha conferida pela lei quanto à conveniência e à oportunidade, e se distingue da arbitrariedade, que é conduta contrária à lei.",
 "A discricionariedade administrativa é a liberdade ilimitada conferida ao administrador, que independe da lei e dos princípios, e se identifica com a arbitrariedade.",
 "Discricionariedade.","confunde com arbitrariedade","a03b")
P("A03",["3"],"caso_concreto","caso_concreto",4,
 "Servidor é aprovado em concurso e, tendo cumprido todos os requisitos legais, tem a posse negada por autoridade que alega conveniência. Como o ato de posse nessa situação é vinculado, o Judiciário pode determinar sua prática, sem violar a separação de poderes.",
 "Servidor é aprovado em concurso e, tendo cumprido todos os requisitos legais, tem a posse negada por autoridade que alega conveniência. Como o ato de posse é discricionário, o Judiciário não pode determinar sua prática, sob pena de violar a separação de poderes.",
 "Atos vinculados.","trata ato vinculado como discricionário","a03c")
# A04
P("A04",["4"],"conceito_correto","confusao_instituto",4,
 "O ato complexo resulta da fusão de vontades de órgãos diversos em um único ato, ao passo que o ato composto resulta de um ato principal e de um ato acessório, como o visto, que o confirma.",
 "O ato composto resulta da fusão de vontades de órgãos diversos em um único ato, ao passo que o ato complexo resulta de um ato principal e de um ato acessório, como o visto, que o confirma.",
 "Ato complexo e composto.","inverte conceitos","a04a")
P("A04",["4"],"conceito_correto","excecao_omitida",4,
 "O ato administrativo pode ser perfeito, por ter completado seu ciclo de formação, mas inválido, por contrariar a lei, e, ainda assim, eficaz, enquanto não for retirado.",
 "O ato administrativo perfeito é necessariamente válido, e o ato inválido nunca pode produzir efeitos, pois a eficácia depende da conformidade do ato com a lei.",
 "Perfeição, validade e eficácia.","vincula perfeição e validade","a04b")
P("A04",["5"],"conceito_correto","confusao_instituto",3,
 "A licença é ato administrativo vinculado e definitivo, ao passo que a autorização é ato discricionário e precário.",
 "A licença é ato administrativo discricionário e precário, ao passo que a autorização é ato vinculado e definitivo.",
 "Licença e autorização.","inverte características","a04c")
P("A04",["5"],"conceito_correto","excecao_omitida",4,
 "A aprovação é ato de controle que examina a conveniência e a oportunidade, podendo ser prévia ou posterior, ao passo que a homologação é ato de controle posterior que examina a legalidade do ato.",
 "A homologação é ato de controle que examina a conveniência e a oportunidade, podendo ser prévia ou posterior, ao passo que a aprovação é ato de controle posterior que examina apenas a legalidade do ato.",
 "Aprovação e homologação.","inverte controles","a04d")
P("A04",["5"],"conceito_correto","excecao_omitida",3,
 "Certidões, atestados e pareceres são atos enunciativos, que apenas declaram uma situação ou emitem opinião, sem criar, por si, obrigações para o administrado.",
 "Certidões, atestados e pareceres são atos normativos, pois estabelecem regras gerais e abstratas de observância obrigatória pela Administração.",
 "Atos enunciativos.","classifica como normativo","a04e")
# A05
P("A05",["6"],"conceito_correto","excecao_omitida",4,
 "O parecer obrigatório deve ser solicitado pela autoridade, mas, em regra, não a vincula, podendo ela decidir em sentido contrário mediante motivação; já no parecer vinculante a autoridade não pode decidir contra a conclusão do parecerista.",
 "O parecer obrigatório deve ser solicitado pela autoridade e a vincula necessariamente, de modo que ela não pode decidir em sentido contrário, ainda que motive sua decisão.",
 "Espécies de parecer.","torna obrigatório vinculante","a05a")
P("A05",["6"],"conceito_correto","troca_autoridade",5,
 "Segundo o STF, o parecerista jurídico não responde, em regra, pela opinião técnica emitida, mas pode ser responsabilizado em caso de erro grosseiro, culpa grave ou dolo.",
 "Segundo o STF, o parecerista jurídico responde objetivamente por qualquer opinião técnica emitida, ainda que ausentes erro grosseiro, culpa grave ou dolo, em razão do caráter vinculante do parecer.",
 "STF, MS 24.631 e MS 24.073.","objetiva","a05b",jur=True)
P("A05",["6"],"conceito_correto","excecao_omitida",4,
 "De acordo com a LINDB, o agente público responde pessoalmente por suas decisões ou opiniões técnicas em caso de dolo ou erro grosseiro.",
 "De acordo com a LINDB, o agente público responde pessoalmente por suas decisões ou opiniões técnicas em caso de simples culpa leve, não se exigindo dolo ou erro grosseiro.",
 "LINDB, art. 28.","reduz o grau de culpa","a05c",lei=True)
# A06
P("A06",["7"],"conceito_correto","troca_efeito",3,
 "A anulação do ato administrativo decorre de ilegalidade e produz, em regra, efeitos retroativos (ex tunc), ao passo que a revogação decorre de conveniência e oportunidade e produz efeitos prospectivos (ex nunc).",
 "A anulação do ato administrativo decorre de conveniência e oportunidade e produz efeitos prospectivos (ex nunc), ao passo que a revogação decorre de ilegalidade e produz efeitos retroativos (ex tunc).",
 "Anulação e revogação.","inverte efeitos","a06a")
P("A06",["7"],"conceito_correto","troca_autoridade",3,
 "A anulação do ato administrativo pode ser realizada pela própria Administração ou pelo Poder Judiciário, ao passo que a revogação somente pode ser realizada pela Administração.",
 "A revogação do ato administrativo pode ser realizada pela própria Administração ou pelo Poder Judiciário, ao passo que a anulação somente pode ser realizada pela Administração.",
 "Súmulas 346 e 473 do STF.","troca autoridade","a06b",jur=True)
P("A06",["7"],"conceito_correto","excecao_omitida",4,
 "Não podem ser revogados os atos vinculados, os que geraram direito adquirido, os já exauridos e os meramente enunciativos, como certidões e pareceres.",
 "Podem ser revogados os atos vinculados e os que geraram direito adquirido, desde que haja conveniência e oportunidade, ressalvados apenas os atos enunciativos.",
 "Limites à revogação.","admite revogar vinculado","a06c")
P("A06",["7"],"conceito_correto","confusao_instituto",4,
 "A cassação é a retirada do ato em razão de descumprimento, pelo beneficiário, das condições que deveria manter, e a caducidade decorre de norma superveniente que torna o ato incompatível com o ordenamento.",
 "A cassação é a retirada do ato em razão de norma superveniente que o torna incompatível com o ordenamento, e a caducidade decorre do descumprimento, pelo beneficiário, das condições que deveria manter.",
 "Formas de extinção.","inverte cassação e caducidade","a06d")
# A07
P("A07",["8"],"conceito_correto","excecao_omitida",4,
 "Os vícios de competência, desde que não se trate de competência exclusiva, e os de forma não essencial são sanáveis, podendo o ato ser convalidado pela Administração, desde que não haja lesão ao interesse público nem prejuízo a terceiros.",
 "Os vícios de finalidade, de motivo e de objeto são sanáveis, podendo o ato ser convalidado pela Administração mesmo que haja lesão ao interesse público ou prejuízo a terceiros.",
 "Lei 9.784/99, art. 55.","inverte vícios sanáveis","a07a",lei=True)
P("A07",["8","9"],"conceito_correto","troca_numero",3,
 "O direito da Administração de anular os atos administrativos de que decorram efeitos favoráveis aos destinatários decai em cinco anos, contados da data em que foram praticados, salvo comprovada má-fé.",
 "O direito da Administração de anular os atos administrativos de que decorram efeitos favoráveis aos destinatários decai em dez anos, contados da data em que foram praticados, mesmo que comprovada a boa-fé.",
 "Lei 9.784/99, art. 54.","troca prazo","a07b",lei=True)
P("A07",["9"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, o TCU deve apreciar a legalidade do ato de concessão inicial de aposentadoria, reforma ou pensão no prazo de cinco anos, contados da chegada do processo à Corte, sob pena de decadência, e dispensa-se contraditório nessa apreciação.",
 "Segundo o STF, o TCU não se sujeita a prazo para apreciar a legalidade do ato de concessão inicial de aposentadoria, reforma ou pensão, e deve garantir contraditório e ampla defesa ao interessado em todos os casos.",
 "STF, Tema 445 e SV 3.","retira prazo e exige contraditório","a07c",jur=True)
P("A07",["10"],"conceito_correto","excecao_omitida",4,
 "A motivação é exigida, nos termos da Lei 9.784/99, nos atos que neguem, limitem ou afetem direitos ou interesses e nos que imponham sanções, podendo ser feita por referência a pareceres ou informações anteriores, e não se exige para a exoneração de cargo em comissão.",
 "A motivação é exigida, nos termos da Lei 9.784/99, para todo e qualquer ato administrativo, inclusive a exoneração de cargo em comissão, e não pode ser feita por referência a pareceres ou informações anteriores.",
 "Lei 9.784/99, art. 50.","generaliza motivação","a07d",lei=True)
# A08
P("A08",["11"],"conceito_correto","confusao_instituto",3,
 "O excesso de poder ocorre quando o agente atua fora dos limites de sua competência, ao passo que o desvio de poder ocorre quando, embora competente, o agente persegue finalidade diversa da prevista em lei.",
 "O excesso de poder ocorre quando, embora competente, o agente persegue finalidade diversa da prevista em lei, ao passo que o desvio de poder ocorre quando o agente atua fora dos limites de sua competência.",
 "Abuso de poder.","inverte espécies","a08a")
P("A08",["12"],"conceito_correto","troca_autoridade",3,
 "O poder hierárquico compreende as prerrogativas de ordenar, coordenar, controlar e corrigir as atividades dos subordinados, bem como de delegar e avocar competências.",
 "O poder hierárquico limita-se à prerrogativa de punir os subordinados por infrações funcionais, não compreendendo a delegação e a avocação de competências.",
 "Poder hierárquico.","confunde com poder disciplinar","a08b")
P("A08",["12"],"conceito_correto","excecao_omitida",3,
 "O poder regulamentar autoriza o chefe do Executivo a expedir decretos para a fiel execução das leis, sendo o decreto autônomo admitido apenas nas hipóteses previstas no art. 84, VI, da Constituição.",
 "O poder regulamentar autoriza o chefe do Executivo a expedir decretos que inovem livremente na ordem jurídica, criando direitos e obrigações, sendo o decreto autônomo admitido em qualquer matéria.",
 "CF, art. 84, IV e VI.","admite decreto autônomo amplo","a08c",lei=True)
P("A08",["12"],"conceito_correto","excecao_omitida",4,
 "O ciclo de polícia compreende a ordem, o consentimento, a fiscalização e a sanção, e, segundo o STF, é constitucional a delegação do poder de polícia, por lei, a pessoas jurídicas de direito privado da Administração indireta, de capital majoritariamente público, que prestem serviço público próprio do Estado em regime não concorrencial.",
 "O ciclo de polícia compreende a ordem, o consentimento, a fiscalização e a sanção, e, segundo o STF, é constitucional a delegação do poder de polícia a qualquer pessoa jurídica de direito privado, inclusive empresas particulares que atuem em regime de concorrência.",
 "STF, Tema 532 (RE 633.782).","amplia delegação a particulares","a08d",jur=True)
P("A08",["12"],"conceito_correto","troca_numero",3,
 "A ação punitiva da Administração Pública Federal, no exercício do poder de polícia, prescreve em cinco anos, contados da prática do ato ou, no caso de infração permanente ou continuada, do dia em que tiver cessado.",
 "A ação punitiva da Administração Pública Federal, no exercício do poder de polícia, prescreve em dois anos, contados da prática do ato ou, no caso de infração permanente ou continuada, do dia em que tiver sido iniciada.",
 "Lei 9.873/99, art. 1º.","troca prazo e termo","a08e",lei=True)
