# Direito administrativo disciplinar — lote L13
Q = []
TAILS=[" Essa seria a orientação adotada pela doutrina e pela jurisprudência no direito brasileiro.",
 " Trata-se de entendimento aplicável à responsabilidade civil das pessoas jurídicas de direito público no Brasil.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática constitucional da responsabilidade do Estado.",
 " Essa seria a regra para os danos causados a terceiros no exercício da função pública."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
FD={"tipo":"doutrina_jurisprudencia","ref":"doutrina majoritária; Lei 8.112/1990; súmulas do STF e STJ","versao":"conhecimento do autor","conferida":"conhecimento"}
FJ={"tipo":"jurisprudencia","ref":"Súmulas e Súmulas Vinculantes do STF e do STJ","versao":"conhecimento do autor","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, jur=False, lei=False):
    ex = {}
    if lei: ex["fonte"]={"tipo":"lei","ref":"Lei 8.112/1990","versao":"vigente","conferida":"conhecimento"}
    elif jur: ex["fonte"]=FJ; ex["risco"]=["jurisprudencia_conhecimento"]
    else: ex["fonte"]=FD; ex["risco"]=["doutrina_conhecimento"]
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# D01
P("D01",["1"],"conceito_correto","excecao_omitida",3,
 "A Lei 8.112/1990 rege o processo disciplinar dos servidores públicos civis federais, aplicando-se a Lei 9.784/1999 apenas de forma subsidiária, nos termos do art. 69 desta última.",
 "A Lei 9.784/1999 rege o processo disciplinar dos servidores públicos civis federais, aplicando-se a Lei 8.112/1990 apenas de forma subsidiária, nos termos do art. 69 da Lei 9.784/1999.",
 "Lei 9.784/1999, art. 69.","inverte aplicação subsidiária","d01a",lei=True)
P("D01",["2"],"conceito_correto","excecao_omitida",4,
 "No direito disciplinar, a tipicidade das infrações é atenuada, admitindo-se conceitos abertos, como a conduta escandalosa, ao passo que as penalidades devem estar previstas em lei.",
 "No direito disciplinar, vigora a tipicidade estrita das infrações, a exemplo do direito penal, sendo vedado o uso de conceitos abertos, e as penalidades podem ser criadas por regulamento.",
 "Tipicidade no direito disciplinar.","exige tipicidade estrita","d01b")
P("D01",["2"],"conceito_correto","confusao_instituto",3,
 "O princípio do non bis in idem veda a imposição de nova punição ao servidor pelo mesmo fato, e, segundo a Súmula 19 do STF, é inadmissível segunda punição baseada no mesmo processo em que se fundou a primeira.",
 "O princípio do non bis in idem veda apenas a cumulação de sanções penais e administrativas pelo mesmo fato, sendo admissível, segundo a Súmula 19 do STF, segunda punição baseada no mesmo processo em que se fundou a primeira.",
 "STF, Súmula 19.","limita non bis in idem","d01c",jur=True)
P("D01",["2"],"conceito_correto","troca_efeito",4,
 "A nulidade no processo disciplinar, em regra, exige a demonstração de prejuízo à defesa, e o excesso de prazo para a conclusão do processo só causa nulidade se houver demonstração desse prejuízo.",
 "A nulidade no processo disciplinar independe de demonstração de prejuízo, e o excesso de prazo para a conclusão do processo causa, por si só, a nulidade do procedimento.",
 "STJ, Súmula 592; Lei 8.112/1990, art. 169, § 1º.","dispensa prejuízo","d01d",jur=True)
# D02
P("D02",["3"],"conceito_correto","confusao_instituto",3,
 "As sanções civis, penais e administrativas poderão cumular-se, sendo independentes entre si, e a responsabilidade administrativa do servidor será afastada no caso de absolvição criminal que negue a existência do fato ou sua autoria.",
 "As sanções civis, penais e administrativas não podem cumular-se, e a responsabilidade administrativa do servidor será afastada em qualquer caso de absolvição criminal, ainda que por falta de provas.",
 "Lei 8.112/1990, arts. 125 e 126.","veda cumulação e amplia efeito da absolvição","d02a",lei=True)
P("D02",["3"],"caso_concreto","caso_concreto",4,
 "Servidor é absolvido na esfera penal por insuficiência de provas quanto ao crime de peculato. Nesse caso, a absolvição criminal não impede a instauração de processo disciplinar nem a aplicação de penalidade administrativa pelos mesmos fatos.",
 "Servidor é absolvido na esfera penal por insuficiência de provas quanto ao crime de peculato. Nesse caso, a absolvição criminal afasta a responsabilidade administrativa, impedindo a aplicação de penalidade disciplinar pelos mesmos fatos.",
 "Lei 8.112/1990, art. 126.","atribui efeito à absolvição por falta de provas","d02b",lei=True)
P("D02",["3"],"conceito_correto","excecao_omitida",4,
 "Segundo a Súmula 18 do STF, pela falta residual, não compreendida na absolvição pelo juízo criminal, é admissível a punição administrativa do servidor público.",
 "Segundo a Súmula 18 do STF, uma vez absolvido o servidor pelo juízo criminal, é inadmissível a punição administrativa por qualquer falta relacionada aos mesmos fatos.",
 "STF, Súmula 18.","veda punição por falta residual","d02c",jur=True)
P("D02",["3"],"conceito_correto","excecao_omitida",3,
 "O servidor responde civil, penal e administrativamente pelo exercício irregular de suas atribuições.",
 "O servidor responde apenas administrativamente pelo exercício irregular de suas atribuições, sendo excluída a responsabilidade civil e penal pelos atos praticados no exercício do cargo.",
 "Lei 8.112/1990, art. 121.","exclui responsabilidade civil e penal","d02d",lei=True)
# D03
P("D03",["4"],"conceito_correto","excecao_omitida",3,
 "A autoridade que tiver ciência de irregularidade no serviço público é obrigada a promover a sua apuração imediata, mediante sindicância ou processo administrativo disciplinar, assegurada ao acusado ampla defesa.",
 "A autoridade que tiver ciência de irregularidade no serviço público pode, a seu critério, promover ou não a sua apuração, mediante sindicância ou processo administrativo disciplinar.",
 "Lei 8.112/1990, art. 143.","torna apuração facultativa","d03a",lei=True)
P("D03",["4"],"conceito_correto","troca_autoridade",4,
 "Segundo a Súmula 650 do STJ, a autoridade administrativa não dispõe de discricionariedade para aplicar ao servidor pena menos gravosa que a demissão quando caracterizadas as hipóteses previstas no art. 132 da Lei 8.112/1990.",
 "Segundo a Súmula 650 do STJ, a autoridade administrativa dispõe de discricionariedade para aplicar ao servidor pena menos gravosa que a demissão, ainda que caracterizadas as hipóteses previstas no art. 132 da Lei 8.112/1990.",
 "STJ, Súmula 650.","admite discricionariedade","d03b",jur=True)
P("D03",["4"],"conceito_correto","excecao_omitida",5,
 "Segundo a Súmula 651 do STJ, compete à autoridade administrativa aplicar a servidor público a pena de demissão em razão da prática de improbidade administrativa, independentemente de prévia condenação, por autoridade judiciária, à perda da função pública.",
 "Segundo a Súmula 651 do STJ, a pena de demissão do servidor em razão da prática de improbidade administrativa somente pode ser aplicada pela autoridade administrativa após prévia condenação judicial à perda da função pública.",
 "STJ, Súmula 651.","exige condenação judicial prévia","d03c",jur=True)
P("D03",["4"],"conceito_correto","excecao_omitida",4,
 "No controle judicial do processo disciplinar, o Poder Judiciário examina a legalidade, a regularidade do procedimento e a proporcionalidade da sanção, mas não revê o mérito administrativo.",
 "No controle judicial do processo disciplinar, o Poder Judiciário pode rever o mérito do ato punitivo, substituindo a penalidade aplicada pela que considerar mais adequada, mesmo que o processo tenha sido regular.",
 "Controle judicial do ato disciplinar.","admite revisão do mérito","d03d")
# D04
P("D04",["5"],"conceito_correto","confusao_instituto",4,
 "A sindicância investigativa, ou preparatória, não tem acusado nem contraditório obrigatório e não aplica penalidade, ao passo que a sindicância acusatória, ou punitiva, assegura contraditório e ampla defesa e pode resultar em advertência ou suspensão de até trinta dias.",
 "A sindicância investigativa, ou preparatória, tem acusado e assegura contraditório e ampla defesa, podendo resultar em demissão, ao passo que a sindicância acusatória, ou punitiva, não tem acusado e não aplica penalidade.",
 "Lei 8.112/1990, art. 145.","inverte sindicâncias","d04a")
P("D04",["5"],"conceito_correto","troca_numero",3,
 "O prazo para a conclusão da sindicância não excederá trinta dias, podendo ser prorrogado por igual período, a critério da autoridade superior.",
 "O prazo para a conclusão da sindicância não excederá sessenta dias, podendo ser prorrogado por igual período, a critério da comissão sindicante.",
 "Lei 8.112/1990, art. 145, parágrafo único.","troca prazo e competência","d04b",lei=True)
P("D04",["5"],"conceito_correto","excecao_omitida",3,
 "É obrigatória a instauração de processo disciplinar sempre que o ilícito ensejar a imposição de suspensão por mais de trinta dias, demissão, cassação de aposentadoria ou disponibilidade ou destituição de cargo em comissão.",
 "É obrigatória a instauração de processo disciplinar sempre que o ilícito ensejar a imposição de qualquer penalidade, inclusive advertência e suspensão de até trinta dias.",
 "Lei 8.112/1990, art. 146.","amplia obrigatoriedade do PAD","d04c",lei=True)
P("D04",["5"],"conceito_correto","troca_numero",3,
 "O processo disciplinar se desenvolve nas fases de instauração, inquérito administrativo, que compreende instrução, defesa e relatório, e julgamento, e seu prazo de conclusão não excederá sessenta dias, admitida a prorrogação por igual prazo.",
 "O processo disciplinar se desenvolve nas fases de instauração, instrução e julgamento, sendo a defesa realizada após o julgamento, e seu prazo de conclusão não excederá noventa dias, vedada a prorrogação.",
 "Lei 8.112/1990, arts. 151 e 152.","troca fases e prazo","d04d",lei=True)
# D05
P("D05",["6"],"conceito_correto","excecao_omitida",3,
 "O processo disciplinar será conduzido por comissão composta de três servidores estáveis, cujo presidente deverá ocupar cargo efetivo superior ou de mesmo nível, ou ter nível de escolaridade igual ou superior ao do indiciado.",
 "O processo disciplinar será conduzido por comissão composta de dois servidores, estáveis ou não, cujo presidente poderá ocupar cargo de nível inferior ao do indiciado.",
 "Lei 8.112/1990, art. 149.","troca composição","d05a",lei=True)
P("D05",["6"],"conceito_correto","troca_numero",3,
 "No prazo de vinte dias, contados do recebimento do processo, a autoridade julgadora proferirá a sua decisão, e o julgamento fora do prazo legal não implica nulidade do processo.",
 "No prazo de dez dias, contados do recebimento do processo, a autoridade julgadora proferirá a sua decisão, e o julgamento fora do prazo legal implica nulidade do processo.",
 "Lei 8.112/1990, arts. 167 e 169, § 1º.","troca prazo e efeito","d05b",lei=True)
P("D05",["6"],"conceito_correto","excecao_omitida",4,
 "O julgamento acatará o relatório da comissão, salvo quando contrário às provas dos autos, caso em que a autoridade julgadora poderá, motivadamente, agravar a penalidade proposta, abrandá-la ou isentar o servidor de responsabilidade.",
 "O julgamento acatará sempre o relatório da comissão, ainda que contrário às provas dos autos, não podendo a autoridade julgadora agravar a penalidade proposta nem isentar o servidor de responsabilidade.",
 "Lei 8.112/1990, art. 168.","vincula autoridade ao relatório","d05c",lei=True)
P("D05",["6"],"conceito_correto","excecao_omitida",4,
 "Verificado vício insanável, a autoridade que determinou a instauração ou outra de hierarquia superior declarará a nulidade, total ou parcial, do processo e ordenará, no mesmo ato, a constituição de outra comissão para a instauração de novo processo.",
 "Verificado vício insanável, a autoridade que determinou a instauração declarará a nulidade do processo e arquivará os autos, sendo vedada a instauração de novo processo pelos mesmos fatos.",
 "Lei 8.112/1990, art. 169.","veda novo processo","d05d",lei=True)
P("D05",["6"],"conceito_correto","excecao_omitida",3,
 "Não poderá participar de comissão de sindicância ou de inquérito cônjuge, companheiro ou parente do acusado, consanguíneo ou afim, em linha reta ou colateral, até o terceiro grau.",
 "Não poderá participar de comissão de sindicância ou de inquérito cônjuge, companheiro ou parente do acusado, consanguíneo ou afim, em linha reta ou colateral, até o segundo grau, admitida a participação de parente de terceiro grau.",
 "Lei 8.112/1990, art. 149, § 2º.","troca grau de parentesco","d05e",lei=True)
# D06
P("D06",["7"],"conceito_correto","excecao_omitida",4,
 "Segundo a Súmula Vinculante 5, a falta de defesa técnica por advogado no processo administrativo disciplinar não ofende a Constituição.",
 "Segundo a Súmula Vinculante 5, a falta de defesa técnica por advogado no processo administrativo disciplinar ofende a Constituição, sendo obrigatória a presença de advogado em todas as fases.",
 "SV 5.","exige advogado","d06a",jur=True)
P("D06",["7"],"conceito_correto","excecao_omitida",4,
 "Segundo a Súmula 21 do STF, o funcionário em estágio probatório não pode ser exonerado nem demitido sem inquérito ou sem as formalidades legais de apuração de sua capacidade.",
 "Segundo a Súmula 21 do STF, o funcionário em estágio probatório pode ser exonerado livremente, sem inquérito ou formalidades legais de apuração de sua capacidade, por ausência de estabilidade.",
 "STF, Súmula 21.","dispensa formalidades no estágio","d06b",jur=True)
P("D06",["7"],"conceito_correto","excecao_omitida",4,
 "Segundo a Súmula 20 do STF, é necessário processo administrativo, com ampla defesa, para a demissão de funcionário admitido por concurso.",
 "Segundo a Súmula 20 do STF, é dispensável o processo administrativo para a demissão de funcionário admitido por concurso quando a infração for grave.",
 "STF, Súmula 20.","dispensa processo","d06c",jur=True)
P("D06",["7"],"conceito_correto","excecao_omitida",5,
 "Segundo a Súmula 591 do STJ, é permitida a prova emprestada no processo administrativo disciplinar, desde que devidamente autorizada pelo juízo competente e respeitados o contraditório e a ampla defesa.",
 "Segundo a Súmula 591 do STJ, é vedada a prova emprestada no processo administrativo disciplinar, ainda que autorizada pelo juízo competente e respeitados o contraditório e a ampla defesa.",
 "STJ, Súmula 591.","veda prova emprestada","d06d",jur=True)
P("D06",["7"],"conceito_correto","excecao_omitida",5,
 "Segundo a Súmula 611 do STJ, desde que devidamente motivada e com amparo em investigação ou sindicância, é permitida a instauração de processo administrativo disciplinar com base em denúncia anônima.",
 "Segundo a Súmula 611 do STJ, é vedada a instauração de processo administrativo disciplinar com base em denúncia anônima, ainda que motivada e amparada em investigação ou sindicância.",
 "STJ, Súmula 611.","veda denúncia anônima","d06e",jur=True)
# D07
P("D07",["8"],"conceito_correto","troca_numero",3,
 "A ação disciplinar prescreve em cinco anos quanto às infrações puníveis com demissão, cassação de aposentadoria ou disponibilidade e destituição de cargo em comissão, em dois anos quanto à suspensão e em cento e oitenta dias quanto à advertência.",
 "A ação disciplinar prescreve em cinco anos quanto às infrações puníveis com suspensão, em dois anos quanto à demissão e à cassação de aposentadoria e em um ano quanto à advertência.",
 "Lei 8.112/1990, art. 142.","troca prazos","d07a",lei=True)
P("D07",["8"],"conceito_correto","excecao_omitida",4,
 "O prazo de prescrição da ação disciplinar começa a correr da data em que o fato se tornou conhecido, e os prazos previstos na lei penal aplicam-se às infrações disciplinares capituladas também como crime.",
 "O prazo de prescrição da ação disciplinar começa a correr da data em que o fato foi praticado, e os prazos previstos na lei penal não se aplicam às infrações disciplinares capituladas também como crime.",
 "Lei 8.112/1990, art. 142, §§ 1º e 2º.","troca termo inicial e nega prazo penal","d07b",lei=True)
P("D07",["8"],"conceito_correto","troca_numero",5,
 "Segundo a Súmula 635 do STJ, os prazos prescricionais iniciam-se na data em que a autoridade competente para instaurar o processo toma conhecimento do fato, interrompem-se com o primeiro ato de instauração válido e voltam a fluir por inteiro após decorridos cento e quarenta dias desde a interrupção.",
 "Segundo a Súmula 635 do STJ, os prazos prescricionais iniciam-se na data do fato, interrompem-se com o julgamento do processo e voltam a fluir por inteiro após decorridos cento e oitenta dias desde a interrupção.",
 "STJ, Súmula 635.","troca marcos e prazo","d07c",jur=True)
P("D07",["9"],"conceito_correto","excecao_omitida",3,
 "São penalidades disciplinares a advertência, a suspensão, a demissão, a cassação de aposentadoria ou disponibilidade, a destituição de cargo em comissão e a destituição de função comissionada.",
 "São penalidades disciplinares a advertência, a suspensão, a multa, a demissão, a cassação de aposentadoria ou disponibilidade e a perda de função pública mediante decisão judicial.",
 "Lei 8.112/1990, art. 127.","altera rol","d07d",lei=True)
P("D07",["9"],"conceito_correto","excecao_omitida",3,
 "Na aplicação das penalidades serão consideradas a natureza e a gravidade da infração, os danos para o serviço público, as circunstâncias agravantes ou atenuantes e os antecedentes funcionais, e o ato de imposição mencionará sempre o fundamento legal e a causa da sanção.",
 "Na aplicação das penalidades serão consideradas apenas a natureza da infração e a hierarquia do servidor, dispensando-se a menção ao fundamento legal e à causa da sanção no ato de imposição.",
 "Lei 8.112/1990, art. 128.","reduz critérios e dispensa motivação","d07e",lei=True)
P("D07",["9"],"conceito_correto","troca_numero",4,
 "A suspensão não pode exceder noventa dias e, quando houver conveniência para o serviço, pode ser convertida em multa, na base de cinquenta por cento por dia de vencimento ou remuneração, ficando o servidor obrigado a permanecer em serviço.",
 "A suspensão não pode exceder cento e vinte dias e, quando houver conveniência para o serviço, pode ser convertida em multa, na base de cem por cento por dia de vencimento ou remuneração, dispensado o servidor de permanecer em serviço.",
 "Lei 8.112/1990, art. 130.","troca prazo e percentual","d07f",lei=True)
P("D07",["9"],"conceito_correto","troca_numero",4,
 "Os registros das penalidades de advertência e de suspensão são cancelados após o decurso de três e cinco anos de efetivo exercício, respectivamente, se não houver nova infração, e o cancelamento não surte efeitos retroativos.",
 "Os registros das penalidades de advertência e de suspensão são cancelados após o decurso de cinco e três anos de efetivo exercício, respectivamente, se não houver nova infração, e o cancelamento surte efeitos retroativos.",
 "Lei 8.112/1990, art. 131.","troca prazos e efeitos","d07g",lei=True)
