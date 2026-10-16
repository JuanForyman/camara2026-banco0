# Lei 14.133/2021 — lote L7 parte a (arts. 1º a 22)
Q = []
TAILS=[" Essa disciplina consta da Lei n.º 14.133/2021 e alcança as contratações regidas pelo regime geral de licitações e contratos administrativos.",
 " Trata-se de regra do regime geral de licitações e contratos da Administração Pública, aplicável conforme a Lei n.º 14.133/2021.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática geral da nova Lei de Licitações e Contratos Administrativos.",
 " Essa seria a orientação extraída da lei para os procedimentos de licitação e contratação de que ela trata."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, risco=None):
    ex = {"risco": risco} if risco else {}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# ---- T01
P("T01",["1"],"conceito_correto","excecao_omitida",3,
 "A Lei n.º 14.133/2021 não abrange as empresas públicas, as sociedades de economia mista e as suas subsidiárias, regidas pela Lei n.º 13.303/2016, ressalvado o disposto no art. 178, que trata dos crimes em licitações e contratos administrativos; abrange, contudo, os órgãos dos Poderes Legislativo e Judiciário, quando no desempenho de função administrativa, e os fundos especiais.",
 "A Lei n.º 14.133/2021 abrange as empresas públicas, as sociedades de economia mista e as suas subsidiárias, que se sujeitam às suas normas ainda que haja lei específica, e não alcança os órgãos dos Poderes Legislativo e Judiciário, ainda que no desempenho de função administrativa.",
 "Art. 1º, caput, I e II, e § 1º.","inclui estatais e exclui Legislativo e Judiciário","t01a")
P("T01",["1"],"conceito_correto","troca_autoridade",3,
 "As contratações realizadas no âmbito das repartições públicas sediadas no exterior obedecerão às peculiaridades locais e aos princípios básicos da Lei n.º 14.133/2021, na forma de regulamentação específica a ser editada por ministro de Estado.",
 "As contratações realizadas no âmbito das repartições públicas sediadas no exterior obedecerão exclusivamente à legislação do país de sede, sem submissão aos princípios da Lei n.º 14.133/2021, na forma de regulamentação editada pelo Presidente da República.",
 "Art. 1º, § 2º.","afasta princípios e troca autoridade","t01b")
P("T01",["1"],"conceito_correto","excecao_omitida",4,
 "Nas licitações e contratações que envolvam recursos provenientes de empréstimo ou doação oriundos de agência oficial de cooperação estrangeira ou de organismo financeiro de que o Brasil seja parte, podem ser admitidas condições decorrentes de acordos internacionais aprovados pelo Congresso Nacional e ratificados pelo Presidente da República, e condições peculiares às normas da agência ou do organismo, desde que não conflitem com os princípios constitucionais em vigor.",
 "Nas licitações e contratações que envolvam recursos provenientes de empréstimo ou doação oriundos de agência oficial de cooperação estrangeira ou de organismo financeiro de que o Brasil seja parte, podem ser admitidas as condições peculiares às normas da agência ou do organismo, ainda que conflitem com os princípios constitucionais em vigor, desde que previstas no contrato de empréstimo ou doação.",
 "Art. 1º, § 3º, I e II, b.","admite conflito com princípios constitucionais","t01c")
P("T01",["2"],"conceito_correto","excecao_omitida",2,
 "A Lei n.º 14.133/2021 aplica-se, entre outros, à alienação e concessão de direito real de uso de bens, à compra, inclusive por encomenda, à locação, à concessão e permissão de uso de bens públicos, à prestação de serviços, às obras e serviços de arquitetura e engenharia e às contratações de tecnologia da informação e de comunicação.",
 "A Lei n.º 14.133/2021 aplica-se à compra, à locação e à prestação de serviços, mas não alcança a alienação de bens, a concessão e permissão de uso de bens públicos nem as contratações de tecnologia da informação e de comunicação.",
 "Art. 2º, I a VII.","reduz o rol","t01d")
P("T01",["3"],"conceito_correto","excecao_omitida",3,
 "Não se subordinam ao regime da Lei n.º 14.133/2021 os contratos que tenham por objeto operação de crédito, interno ou externo, e gestão de dívida pública, incluídas as contratações de agente financeiro e a concessão de garantia relacionadas a esses contratos, nem as contratações sujeitas a normas previstas em legislação própria.",
 "Subordinam-se ao regime da Lei n.º 14.133/2021 os contratos que tenham por objeto operação de crédito, interno ou externo, e gestão de dívida pública, incluídas as contratações de agente financeiro relacionadas a esses contratos, sendo excluídas apenas as contratações sujeitas a legislação própria.",
 "Art. 3º, I e II.","inclui operações de crédito","t01e")
P("T01",["4"],"conceito_correto","excecao_omitida",4,
 "Aplicam-se às licitações e contratos da Lei n.º 14.133/2021 as disposições dos arts. 42 a 49 da Lei Complementar n.º 123/2006, que tratam do tratamento favorecido às microempresas e empresas de pequeno porte, as quais não se aplicam, na contratação de obras e serviços de engenharia, às licitações cujo valor estimado seja superior à receita bruta máxima admitida para enquadramento como empresa de pequeno porte.",
 "Aplicam-se às licitações e contratos da Lei n.º 14.133/2021 as disposições dos arts. 42 a 49 da Lei Complementar n.º 123/2006, que tratam do tratamento favorecido às microempresas e empresas de pequeno porte, as quais se aplicam, inclusive, às licitações de obras e serviços de engenharia de valor estimado superior à receita bruta máxima admitida para o enquadramento como empresa de pequeno porte.",
 "Art. 4º, caput e § 1º, II.","afasta limite de valor","t01f")
P("T01",["4"],"conceito_correto","troca_efeito",4,
 "A obtenção dos benefícios da LC n.º 123/2006 nas licitações fica limitada às microempresas e às empresas de pequeno porte que, no ano-calendário de realização da licitação, ainda não tenham celebrado contratos com a Administração Pública cujos valores somados extrapolem a receita bruta máxima admitida para o enquadramento como empresa de pequeno porte, devendo o órgão exigir do licitante declaração de observância desse limite.",
 "A obtenção dos benefícios da LC n.º 123/2006 nas licitações fica limitada às microempresas e às empresas de pequeno porte que, nos cinco anos anteriores à licitação, não tenham celebrado contratos com a Administração Pública, sendo dispensada a declaração do licitante quanto à observância desse limite.",
 "Art. 4º, § 2º.","troca período e dispensa declaração","t01g")
# ---- T02
P("T02",["5"],"conceito_correto","excecao_omitida",3,
 "Na aplicação da Lei n.º 14.133/2021, serão observados, entre outros, os princípios do planejamento, da transparência, da eficácia, da segregação de funções, da motivação, da segurança jurídica, da competitividade, da celeridade, da economicidade e do desenvolvimento nacional sustentável, assim como as disposições da Lei de Introdução às Normas do Direito Brasileiro.",
 "Na aplicação da Lei n.º 14.133/2021, serão observados, entre outros, os princípios da supremacia do interesse privado, da finalidade, da autotutela, da continuidade do serviço público e da hierarquia, sem aplicação das disposições da Lei de Introdução às Normas do Direito Brasileiro.",
 "Art. 5º.","troca princípios e afasta LINDB","t02a")
P("T02",["5"],"conceito_correto","excecao_omitida",3,
 "Entre os princípios expressamente previstos no art. 5º da Lei n.º 14.133/2021 estão a vinculação ao edital, o julgamento objetivo, a razoabilidade, a proporcionalidade, a probidade administrativa e a igualdade.",
 "Entre os princípios expressamente previstos no art. 5º da Lei n.º 14.133/2021 estão a vinculação ao instrumento convocatório, o julgamento subjetivo, a razoabilidade, a proporcionalidade, a probidade administrativa e a igualdade.",
 "Art. 5º.","troca julgamento objetivo por subjetivo","t02b")
P("T02",["5"],"conceito_correto","excecao_omitida",3,
 "O princípio da segregação de funções está expressamente previsto no art. 5º da Lei n.º 14.133/2021 e orienta, no art. 7º, § 1º, a vedação de que o mesmo agente público seja designado para atuação simultânea em funções mais suscetíveis a riscos, a fim de reduzir a possibilidade de ocultação de erros e de fraudes na contratação.",
 "O princípio da segregação de funções não consta do art. 5º da Lei n.º 14.133/2021, razão pela qual se admite a designação do mesmo agente público para atuação simultânea em funções mais suscetíveis a riscos, desde que haja motivação.",
 "Art. 5º e art. 7º, § 1º.","nega o princípio","t02c")
# ---- T03
P("T03",["6.XXII"],"conceito_correto","troca_numero",3,
 "Consideram-se obras, serviços e fornecimentos de grande vulto aqueles cujo valor estimado supera R$ 200.000.000,00, conforme a redação original da Lei n.º 14.133/2021.",
 "Consideram-se obras, serviços e fornecimentos de grande vulto aqueles cujo valor estimado supera R$ 20.000.000,00, conforme a redação original da Lei n.º 14.133/2021.",
 "Art. 6º, XXII. O valor foi atualizado por decreto (Dec. 12.343/2024); a questão especifica a redação original.","troca valor","t03a",["valor_atualizado_por_decreto"])
P("T03",["6.XLI"],"conceito_correto","confusao_instituto",3,
 "O pregão é a modalidade de licitação obrigatória para aquisição de bens e serviços comuns, cujo critério de julgamento poderá ser o de menor preço ou o de maior desconto.",
 "O pregão é a modalidade de licitação obrigatória para contratação de bens e serviços especiais, cujo critério de julgamento poderá ser o de melhor técnica ou o de técnica e preço.",
 "Art. 6º, XLI.","troca objeto e critérios","t03b")
P("T03",["6.XXXVIII"],"conceito_correto","excecao_omitida",4,
 "A concorrência é a modalidade de licitação para contratação de bens e serviços especiais e de obras e serviços comuns e especiais de engenharia, e seu critério de julgamento poderá ser o de menor preço, melhor técnica ou conteúdo artístico, técnica e preço, maior retorno econômico ou maior desconto.",
 "A concorrência é a modalidade de licitação para contratação de bens e serviços comuns, cujo critério de julgamento poderá ser o de menor preço, técnica e preço ou maior lance, sendo vedada a sua utilização para obras e serviços de engenharia.",
 "Art. 6º, XXXVIII.","troca objeto e critérios","t03c")
P("T03",["6.XXXIX","6.XL"],"conceito_correto","confusao_instituto",3,
 "O concurso é a modalidade de licitação para escolha de trabalho técnico, científico ou artístico, cujo critério de julgamento será o de melhor técnica ou conteúdo artístico, e para concessão de prêmio ou remuneração ao vencedor; já o leilão é a modalidade para alienação de bens imóveis ou de bens móveis inservíveis ou legalmente apreendidos a quem oferecer o maior lance.",
 "O concurso é a modalidade de licitação para escolha de trabalho técnico, científico ou artístico, cujo critério de julgamento será o de menor preço; já o leilão é a modalidade para aquisição de bens móveis inservíveis a quem oferecer o menor lance.",
 "Art. 6º, XXXIX e XL.","troca critério e objeto","t03d")
P("T03",["6.XLII"],"conceito_correto","troca_efeito",4,
 "O diálogo competitivo é a modalidade de licitação para contratação de obras, serviços e compras em que a Administração Pública realiza diálogos com licitantes previamente selecionados mediante critérios objetivos, com o intuito de desenvolver uma ou mais alternativas capazes de atender às suas necessidades, devendo os licitantes apresentar proposta final após o encerramento dos diálogos.",
 "O diálogo competitivo é a modalidade de licitação para contratação de bens e serviços comuns em que a Administração Pública realiza diálogos com quaisquer interessados, que apresentam suas propostas finais durante o desenvolvimento dos diálogos, antes da definição das alternativas pela Administração.",
 "Art. 6º, XLII.","troca objeto e fluxo","t03e")
P("T03",["6.XIII","6.XIV"],"conceito_correto","troca_efeito",3,
 "Bens e serviços comuns são aqueles cujos padrões de desempenho e qualidade podem ser objetivamente definidos pelo edital, por meio de especificações usuais de mercado; os bens e serviços especiais, por sua alta heterogeneidade ou complexidade, não podem ser assim descritos, exigindo justificativa prévia do contratante.",
 "Bens e serviços comuns são aqueles de menor valor, independentemente de seus padrões de desempenho e qualidade; os bens e serviços especiais são aqueles de valor mais elevado, dispensada a justificativa prévia do contratante.",
 "Art. 6º, XIII e XIV.","define por valor","t03f")
P("T03",["6.XXXII","6.XXXIII"],"conceito_correto","confusao_instituto",4,
 "Na contratação integrada, o contratado é responsável por elaborar e desenvolver os projetos básico e executivo, executar obras e serviços de engenharia e realizar as operações necessárias à entrega final do objeto; na contratação semi-integrada, o contratado é responsável por elaborar e desenvolver o projeto executivo, e não o básico.",
 "Na contratação integrada, o contratado é responsável por elaborar e desenvolver apenas o projeto executivo; na contratação semi-integrada, o contratado é responsável por elaborar e desenvolver os projetos básico e executivo.",
 "Art. 6º, XXXII e XXXIII.","inverte os regimes","t03g")
P("T03",["6.XXVIII","6.XXIX","6.XXX"],"conceito_correto","confusao_instituto",3,
 "A empreitada por preço unitário é a contratação da execução da obra ou do serviço por preço certo de unidades determinadas; a empreitada por preço global, por preço certo e total; e a empreitada integral, a contratação de empreendimento em sua integralidade, sob inteira responsabilidade do contratado até sua entrega em condições de entrada em operação.",
 "A empreitada por preço unitário é a contratação da execução da obra ou do serviço por preço certo e total; a empreitada por preço global, por preço certo de unidades determinadas; e a empreitada integral, a contratação apenas das etapas de execução da obra, sem responsabilidade do contratado pela entrada em operação.",
 "Art. 6º, XXVIII a XXX.","troca preço unitário e global","t03h")
P("T03",["6.LX"],"conceito_correto","troca_autoridade",3,
 "O agente de contratação é a pessoa designada pela autoridade competente, entre servidores efetivos ou empregados públicos dos quadros permanentes da Administração Pública, para tomar decisões, acompanhar o trâmite da licitação, dar impulso ao procedimento e executar as atividades necessárias ao bom andamento do certame até a homologação.",
 "O agente de contratação é a pessoa designada pela autoridade competente, preferencialmente entre ocupantes de cargo em comissão, para tomar decisões, acompanhar o trâmite da licitação e executar as atividades necessárias ao certame até a assinatura do contrato.",
 "Art. 6º, LX.","troca vínculo e marco final","t03i")
P("T03",["6.XLV","6.XLVI"],"conceito_correto","excecao_omitida",3,
 "O sistema de registro de preços é o conjunto de procedimentos para realização, mediante contratação direta ou licitação nas modalidades pregão ou concorrência, de registro formal de preços para contratações futuras; a ata de registro de preços é documento vinculativo e obrigacional, com característica de compromisso para futura contratação.",
 "O sistema de registro de preços é o conjunto de procedimentos para realização, mediante licitação exclusivamente na modalidade pregão, de registro de preços para contratações futuras; a ata de registro de preços é documento meramente informativo, sem compromisso para futura contratação.",
 "Art. 6º, XLV e XLVI.","retira concorrência e vínculo","t03j")
P("T03",["6.LVI","6.LVII"],"conceito_correto","confusao_instituto",4,
 "Sobrepreço é o preço orçado para licitação ou contratado em valor expressivamente superior aos preços referenciais de mercado; superfaturamento é o dano provocado ao patrimônio da Administração, caracterizado, entre outras situações, por medição de quantidades superiores às efetivamente executadas ou fornecidas.",
 "Sobrepreço é o dano provocado ao patrimônio da Administração caracterizado por medição de quantidades superiores às efetivamente executadas; superfaturamento é o preço orçado para licitação em valor expressivamente superior aos preços referenciais de mercado.",
 "Art. 6º, LVI e LVII.","troca sobrepreço e superfaturamento","t03k")
P("T03",["6.LVIII","6.LIX"],"conceito_correto","confusao_instituto",4,
 "O reajustamento em sentido estrito consiste na aplicação do índice de correção monetária previsto no contrato; a repactuação é a forma de manutenção do equilíbrio econômico-financeiro utilizada para serviços contínuos com regime de dedicação exclusiva de mão de obra ou predominância de mão de obra, por meio da análise da variação dos custos contratuais.",
 "O reajustamento em sentido estrito é a forma de manutenção do equilíbrio utilizada para serviços contínuos com dedicação exclusiva de mão de obra, por meio da análise da variação dos custos; a repactuação consiste na aplicação do índice de correção monetária previsto no contrato.",
 "Art. 6º, LVIII e LIX.","troca reajuste e repactuação","t03l")
P("T03",["6.XXVII"],"conceito_correto","excecao_omitida",4,
 "A matriz de riscos é cláusula contratual definidora de riscos e de responsabilidades entre as partes e caracterizadora do equilíbrio econômico-financeiro inicial do contrato, em termos de ônus financeiro decorrente de eventos supervenientes à contratação.",
 "A matriz de riscos é cláusula do edital que lista os riscos da licitação, vedado que defina responsabilidades entre as partes ou caracterize o equilíbrio econômico-financeiro inicial do contrato, que será definido apenas após eventos supervenientes.",
 "Art. 6º, XXVII.","reduz matriz a lista de riscos","t03m")
# ---- T04
P("T04",["7"],"conceito_correto","troca_autoridade",3,
 "Caberá à autoridade máxima do órgão ou da entidade, ou a quem as normas de organização administrativa indicarem, promover gestão por competências e designar agentes públicos para o desempenho das funções essenciais à execução da lei, que sejam, preferencialmente, servidores efetivos ou empregados públicos dos quadros permanentes da Administração Pública.",
 "Caberá ao órgão de controle interno promover gestão por competências e designar agentes públicos para o desempenho das funções essenciais à execução da lei, que devem ser, obrigatoriamente, ocupantes de cargo em comissão de livre nomeação.",
 "Art. 7º, caput e I.","troca autoridade e vínculo","t04a")
P("T04",["7"],"conceito_correto","excecao_omitida",4,
 "Os agentes públicos designados para as funções essenciais à execução da lei não podem ser cônjuge ou companheiro de licitantes ou contratados habituais da Administração, nem ter com eles vínculo de parentesco, colateral ou por afinidade, até o terceiro grau, ou de natureza técnica, comercial, econômica, financeira, trabalhista e civil; essas regras aplicam-se também aos órgãos de assessoramento jurídico e de controle interno.",
 "Os agentes públicos designados para as funções essenciais à execução da lei não podem ser cônjuge ou companheiro de licitantes ou contratados habituais da Administração, nem ter com eles vínculo de parentesco até o segundo grau; essas regras não se aplicam aos órgãos de assessoramento jurídico e de controle interno.",
 "Art. 7º, III e § 2º.","reduz grau e afasta órgãos de assessoramento","t04b")
P("T04",["8"],"conceito_correto","troca_efeito",4,
 "O agente de contratação será auxiliado por equipe de apoio e responderá individualmente pelos atos que praticar, salvo quando induzido a erro pela atuação da equipe.",
 "O agente de contratação será auxiliado por equipe de apoio e responderá solidariamente com os membros da equipe pelos atos que praticar, ainda que induzido a erro pela atuação da equipe.",
 "Art. 8º, § 1º.","troca responsabilidade","t04c")
P("T04",["8"],"conceito_correto","troca_numero",4,
 "Em licitação que envolva bens ou serviços especiais, o agente de contratação poderá ser substituído por comissão de contratação formada por, no mínimo, três membros, que responderão solidariamente por todos os atos praticados pela comissão, ressalvado o membro que expressar posição individual divergente fundamentada e registrada em ata.",
 "Em licitação que envolva bens ou serviços comuns, o agente de contratação poderá ser substituído por comissão de contratação formada por, no mínimo, cinco membros, que responderão solidariamente por todos os atos da comissão, sem ressalva para o membro divergente.",
 "Art. 8º, § 2º.","troca objeto, número e ressalva","t04d")
P("T04",["8"],"conceito_correto","excecao_omitida",3,
 "Em licitação na modalidade pregão, o agente responsável pela condução do certame será designado pregoeiro; e, em licitação que envolva bens ou serviços especiais cujo objeto não seja rotineiramente contratado, poderá ser contratado, por prazo determinado, serviço de empresa ou de profissional especializado para assessorar os agentes públicos responsáveis pela condução da licitação.",
 "Em licitação na modalidade pregão, o agente responsável pela condução do certame será designado agente de contratação, vedada a designação de pregoeiro; e é proibida a contratação de empresa ou profissional especializado para assessorar os agentes públicos, ainda que o objeto não seja rotineiramente contratado.",
 "Art. 8º, §§ 4º e 5º.","extingue pregoeiro e veda assessoria","t04e")
P("T04",["9"],"conceito_correto","excecao_omitida",3,
 "É vedado ao agente público designado para atuar na área de licitações e contratos admitir, prever, incluir ou tolerar, nos atos que praticar, situações que comprometam, restrinjam ou frustrem o caráter competitivo do processo licitatório, estabeleçam preferências em razão da naturalidade, da sede ou do domicílio dos licitantes ou sejam impertinentes ou irrelevantes para o objeto específico do contrato, ressalvados os casos previstos em lei.",
 "É permitido ao agente público designado para atuar na área de licitações e contratos estabelecer preferências em razão da naturalidade, da sede ou do domicílio dos licitantes, desde que motivadas, e estabelecer tratamento diferenciado entre empresas brasileiras e estrangeiras quanto a moeda, modalidade e local de pagamento.",
 "Art. 9º, I, b, e II.","permite preferência territorial","t04f")
P("T04",["9"],"conceito_correto","troca_autoridade",4,
 "Não poderá participar, direta ou indiretamente, da licitação ou da execução do contrato agente público de órgão ou entidade licitante ou contratante, devendo ser observadas as situações que possam configurar conflito de interesses no exercício ou após o exercício do cargo ou emprego; as vedações estendem-se a terceiro que auxilie a condução da contratação como integrante de equipe de apoio, profissional especializado ou funcionário ou representante de empresa que preste assessoria técnica.",
 "Poderá participar da licitação, desde que não integre a comissão de contratação, o agente público de órgão ou entidade licitante ou contratante, e as vedações do art. 9º não se estendem a terceiro que auxilie a condução da contratação na qualidade de profissional especializado ou de representante de empresa que preste assessoria técnica.",
 "Art. 9º, §§ 1º e 2º.","permite participação do agente","t04g")
P("T04",["10"],"conceito_correto","excecao_omitida",4,
 "Se as autoridades competentes e os servidores que tiverem participado dos procedimentos de licitação e contratos precisarem defender-se nas esferas administrativa, controladora ou judicial em razão de ato praticado com estrita observância de orientação constante em parecer jurídico, a advocacia pública promoverá, a critério do agente público, sua representação, salvo se provas da prática de atos ilícitos dolosos constarem nos autos; a regra vale mesmo que o agente não mais ocupe o cargo.",
 "Se as autoridades competentes e os servidores que tiverem participado dos procedimentos de licitação e contratos precisarem defender-se nas esferas administrativa, controladora ou judicial em razão de ato praticado com observância de parecer jurídico, a advocacia pública promoverá obrigatoriamente sua representação, mesmo que haja provas de atos ilícitos dolosos, desde que o agente ainda ocupe o cargo.",
 "Art. 10, caput, § 1º, II, e § 2º.","obriga representação e exige permanência no cargo","t04h")
# ---- T05
P("T05",["11"],"conceito_correto","excecao_omitida",3,
 "O processo licitatório tem por objetivos assegurar a seleção da proposta apta a gerar o resultado de contratação mais vantajoso para a Administração Pública, inclusive quanto ao ciclo de vida do objeto, assegurar tratamento isonômico entre os licitantes e a justa competição, evitar contratações com sobrepreço, preços manifestamente inexequíveis e superfaturamento e incentivar a inovação e o desenvolvimento nacional sustentável.",
 "O processo licitatório tem por objetivos assegurar a seleção da proposta de menor preço, desconsiderado o ciclo de vida do objeto, assegurar tratamento isonômico entre os licitantes e a justa competição e evitar contratações com sobrepreço, não se incluindo entre seus objetivos o desenvolvimento nacional sustentável.",
 "Art. 11, I a IV.","reduz objetivos","t05a")
P("T05",["11"],"conceito_correto","troca_autoridade",3,
 "A alta administração do órgão ou entidade é responsável pela governança das contratações e deve implementar processos e estruturas, inclusive de gestão de riscos e controles internos, para avaliar, direcionar e monitorar os processos licitatórios e os respectivos contratos.",
 "O órgão de controle externo é responsável pela governança das contratações e deve implementar processos e estruturas, inclusive de gestão de riscos e controles internos, para avaliar, direcionar e monitorar os processos licitatórios e os respectivos contratos.",
 "Art. 11, parágrafo único.","troca responsável pela governança","t05b")
P("T05",["12"],"conceito_correto","excecao_omitida",3,
 "No processo licitatório, o desatendimento de exigências meramente formais que não comprometam a aferição da qualificação do licitante ou a compreensão do conteúdo de sua proposta não importará seu afastamento da licitação ou a invalidação do processo, e o reconhecimento de firma somente será exigido quando houver dúvida de autenticidade, salvo imposição legal.",
 "No processo licitatório, o desatendimento de qualquer exigência formal importará o afastamento do licitante, ainda que não comprometa a compreensão de sua proposta, e o reconhecimento de firma será exigido em todos os documentos particulares.",
 "Art. 12, III e V.","rigor formal","t05c")
P("T05",["12"],"conceito_correto","excecao_omitida",3,
 "No processo licitatório, os valores, os preços e os custos utilizados terão como expressão monetária a moeda corrente nacional, ressalvado o disposto no art. 51 da Lei, e os atos serão preferencialmente digitais, de forma a permitir que sejam produzidos, comunicados, armazenados e validados por meio eletrônico.",
 "No processo licitatório, os valores, os preços e os custos poderão ser expressos em moeda estrangeira em qualquer hipótese, e os atos serão obrigatoriamente praticados em meio físico, admitido o meio eletrônico apenas para a divulgação do edital.",
 "Art. 12, II e VI.","admite moeda estrangeira e exige meio físico","t05d")
P("T05",["13"],"conceito_correto","troca_efeito",3,
 "Os atos praticados no processo licitatório são públicos, ressalvadas as hipóteses de informações cujo sigilo seja imprescindível à segurança da sociedade e do Estado, e a publicidade será diferida quanto ao conteúdo das propostas, até a respectiva abertura, e quanto ao orçamento da Administração, nos termos do art. 24 da Lei.",
 "Os atos praticados no processo licitatório são sigilosos até a homologação, e a publicidade será diferida apenas quanto ao conteúdo das propostas, devendo o orçamento da Administração ser sempre divulgado desde a publicação do edital.",
 "Art. 13 e parágrafo único.","inverte publicidade e sigilo","t05e")
P("T05",["14"],"conceito_correto","excecao_omitida",4,
 "Não poderão disputar licitação ou participar da execução de contrato, direta ou indiretamente, o autor do anteprojeto, do projeto básico ou do projeto executivo, quando a licitação versar sobre obra, serviços ou fornecimento de bens a ele relacionados, e a empresa responsável pela elaboração do projeto ou da qual o autor do projeto seja dirigente, gerente, controlador, acionista ou detentor de mais de 5% do capital com direito a voto.",
 "Poderão disputar licitação ou participar da execução de contrato o autor do anteprojeto, do projeto básico ou do projeto executivo, quando a licitação versar sobre obra ou fornecimento de bens a ele relacionados, desde que o autor do projeto não seja detentor de mais de 20% do capital da empresa participante.",
 "Art. 14, I e II.","libera o autor do projeto","t05f")
P("T05",["14"],"conceito_correto","troca_numero",4,
 "Não poderá disputar licitação a pessoa física ou jurídica que, nos 5 anos anteriores à divulgação do edital, tenha sido condenada judicialmente, com trânsito em julgado, por exploração de trabalho infantil, por submissão de trabalhadores a condições análogas às de escravo ou por contratação de adolescentes nos casos vedados pela legislação trabalhista.",
 "Não poderá disputar licitação a pessoa física ou jurídica que, nos 2 anos anteriores à divulgação do edital, tenha sido condenada judicialmente, ainda que sem trânsito em julgado, por exploração de trabalho infantil ou por submissão de trabalhadores a condições análogas às de escravo.",
 "Art. 14, VI.","troca prazo e trânsito em julgado","t05g")
P("T05",["14"],"conceito_correto","excecao_omitida",4,
 "A critério da Administração e exclusivamente a seu serviço, o autor dos projetos e a empresa a que se referem os incisos I e II do art. 14 poderão participar no apoio das atividades de planejamento da contratação, de execução da licitação ou de gestão do contrato, desde que sob supervisão exclusiva de agentes públicos do órgão ou entidade; equiparam-se aos autores do projeto as empresas integrantes do mesmo grupo econômico.",
 "O autor dos projetos e a empresa a que se referem os incisos I e II do art. 14 não poderão, em nenhuma hipótese, participar do apoio às atividades de planejamento da contratação, de execução da licitação ou de gestão do contrato; as empresas do mesmo grupo econômico não se equiparam aos autores do projeto.",
 "Art. 14, §§ 2º e 3º.","veda apoio em qualquer hipótese","t05h")
P("T05",["15"],"conceito_correto","troca_numero",3,
 "Salvo vedação devidamente justificada no processo licitatório, pessoa jurídica poderá participar de licitação em consórcio; o edital deverá estabelecer para o consórcio acréscimo de 10% a 30% sobre o valor exigido de licitante individual para a habilitação econômico-financeira, salvo justificação, acréscimo que não se aplica aos consórcios compostos, em sua totalidade, de microempresas e pequenas empresas.",
 "Salvo vedação devidamente justificada no processo licitatório, pessoa jurídica poderá participar de licitação em consórcio; o edital deverá estabelecer para o consórcio acréscimo de 5% a 15% sobre o valor exigido de licitante individual para a habilitação econômico-financeira, inclusive para os consórcios compostos apenas de microempresas e pequenas empresas.",
 "Art. 15, caput, §§ 1º e 2º.","troca percentuais e inclui MPEs","t05i")
P("T05",["15"],"conceito_correto","excecao_omitida",4,
 "Na licitação em consórcio, admite-se, para efeito de habilitação técnica, o somatório dos quantitativos de cada consorciado e, para efeito de habilitação econômico-financeira, o somatório dos valores de cada consorciado; é impedida a empresa consorciada de participar, na mesma licitação, de mais de um consórcio ou de forma isolada, e os integrantes respondem solidariamente pelos atos praticados em consórcio.",
 "Na licitação em consórcio, admite-se somente a habilitação técnica da empresa líder, sem somatório de quantitativos; a empresa consorciada pode participar, na mesma licitação, de mais de um consórcio, e os integrantes respondem subsidiariamente pelos atos praticados em consórcio.",
 "Art. 15, III, IV e V.","troca somatório, exclusividade e solidariedade","t05j")
P("T05",["15"],"conceito_correto","troca_autoridade",4,
 "A substituição de consorciado deverá ser expressamente autorizada pelo órgão ou entidade contratante e condicionada à comprovação de que a nova empresa possui, no mínimo, os mesmos quantitativos para efeito de habilitação técnica e os mesmos valores para efeito de qualificação econômico-financeira apresentados pela empresa substituída.",
 "A substituição de consorciado independe de autorização do órgão ou entidade contratante, bastando a comunicação ao consórcio líder e a comprovação de regularidade fiscal da nova empresa.",
 "Art. 15, § 5º.","dispensa autorização","t05k")
P("T05",["16"],"conceito_correto","excecao_omitida",4,
 "Os profissionais organizados sob a forma de cooperativa poderão participar de licitação quando a cooperativa observar as regras da legislação aplicável, apresentar demonstrativo de atuação em regime cooperado, com repartição de receitas e despesas entre os cooperados, e qualquer cooperado, com igual qualificação, for capaz de executar o objeto contratado, vedado à Administração indicar nominalmente pessoas.",
 "Os profissionais organizados sob a forma de cooperativa poderão participar de licitação quando a Administração indicar nominalmente os cooperados que executarão o objeto contratado, dispensado o demonstrativo de atuação em regime cooperado.",
 "Art. 16, II e III.","permite indicação nominal","t05l")
P("T05",["17"],"conceito_correto","troca_numero",3,
 "O processo de licitação observará, em sequência, as fases preparatória, de divulgação do edital, de apresentação de propostas e lances, quando for o caso, de julgamento, de habilitação, recursal e de homologação.",
 "O processo de licitação observará, em sequência, as fases preparatória, de divulgação do edital, de habilitação, de apresentação de propostas e lances, de julgamento, de homologação e recursal.",
 "Art. 17, I a VII.","inverte a ordem das fases","t05m")
P("T05",["17"],"conceito_correto","excecao_omitida",4,
 "A fase de habilitação poderá, mediante ato motivado com explicitação dos benefícios decorrentes, anteceder as fases de apresentação de propostas e lances e de julgamento, desde que expressamente previsto no edital de licitação.",
 "A fase de habilitação poderá anteceder as fases de apresentação de propostas e lances e de julgamento por decisão discricionária do agente de contratação durante o certame, ainda que não prevista no edital de licitação.",
 "Art. 17, § 1º.","dispensa previsão em edital","t05n")
P("T05",["17"],"conceito_correto","troca_efeito",3,
 "As licitações serão realizadas preferencialmente sob a forma eletrônica, admitida a utilização da forma presencial, desde que motivada, devendo a sessão pública ser registrada em ata e gravada em áudio e vídeo.",
 "As licitações serão realizadas preferencialmente sob a forma presencial, admitida a utilização da forma eletrônica, desde que motivada, devendo a sessão pública ser registrada em ata, dispensada a gravação em áudio e vídeo.",
 "Art. 17, § 2º e § 5º.","inverte preferência e dispensa gravação","t05o")
# ---- T06
P("T06",["18"],"conceito_correto","excecao_omitida",3,
 "A fase preparatória do processo licitatório é caracterizada pelo planejamento e deve compatibilizar-se com o plano de contratações anual, sempre que elaborado, e com as leis orçamentárias; compreende, entre outros itens, a descrição da necessidade da contratação fundamentada em estudo técnico preliminar, o orçamento estimado, a elaboração do edital e a análise dos riscos que possam comprometer o sucesso da licitação.",
 "A fase preparatória do processo licitatório é caracterizada pela execução e dispensa a compatibilização com o plano de contratações anual e com as leis orçamentárias; compreende o orçamento estimado e a elaboração do edital, não incluindo a análise de riscos nem o estudo técnico preliminar.",
 "Art. 18, caput, I, IV, V e X.","retira ETP e riscos","t06a")
P("T06",["18"],"conceito_correto","excecao_omitida",4,
 "O estudo técnico preliminar deverá conter ao menos a descrição da necessidade da contratação, as estimativas das quantidades, a estimativa do valor da contratação, as justificativas para o parcelamento ou não da contratação e o posicionamento conclusivo sobre a adequação da contratação, e, quando não contemplar os demais elementos, apresentar as devidas justificativas.",
 "O estudo técnico preliminar deverá conter obrigatoriamente todos os treze elementos previstos na lei, sendo vedado deixar de contemplar qualquer deles, ainda que justificadamente.",
 "Art. 18, §§ 1º e 2º.","torna todos os elementos obrigatórios","t06b")
P("T06",["18"],"conceito_correto","excecao_omitida",4,
 "Em se tratando de estudo técnico preliminar para contratação de obras e serviços comuns de engenharia, se demonstrada a inexistência de prejuízo para a aferição dos padrões de desempenho e qualidade almejados, a especificação do objeto poderá ser realizada apenas em termo de referência ou em projeto básico, dispensada a elaboração de projetos.",
 "Em se tratando de estudo técnico preliminar para contratação de obras e serviços especiais de engenharia, a especificação do objeto poderá ser realizada apenas em termo de referência, dispensada a elaboração de projetos, ainda que haja prejuízo para a aferição dos padrões de desempenho.",
 "Art. 18, § 3º.","estende a dispensa aos serviços especiais","t06c")
P("T06",["19"],"conceito_correto","excecao_omitida",3,
 "Os órgãos da Administração com competências regulamentares relativas a materiais, obras, serviços, licitações e contratos deverão instituir instrumentos que permitam, preferencialmente, a centralização dos procedimentos de aquisição, criar catálogo eletrônico de padronização de compras, serviços e obras, instituir sistema informatizado de acompanhamento de obras e instituir modelos de minutas de editais, termos de referência e contratos padronizados.",
 "Os órgãos da Administração com competências regulamentares relativas a materiais, obras, serviços, licitações e contratos deverão, obrigatoriamente, descentralizar os procedimentos de aquisição, sendo vedada a adoção, por outros entes, do catálogo eletrônico de padronização e das minutas do Poder Executivo federal.",
 "Art. 19, I, II e IV.","veda centralização e adoção do catálogo federal","t06d")
P("T06",["19"],"conceito_correto","troca_efeito",4,
 "A não utilização do catálogo eletrônico de padronização ou dos modelos de minutas deverá ser justificada por escrito e anexada ao respectivo processo licitatório; nas licitações de obras e serviços de engenharia e arquitetura, sempre que adequada ao objeto, será preferencialmente adotada a Modelagem da Informação da Construção (BIM).",
 "A não utilização do catálogo eletrônico de padronização ou dos modelos de minutas independe de justificativa; nas licitações de obras e serviços de engenharia e arquitetura, será obrigatoriamente adotada a Modelagem da Informação da Construção (BIM) em qualquer hipótese.",
 "Art. 19, §§ 2º e 3º.","dispensa justificativa e torna BIM obrigatório","t06e")
P("T06",["20"],"conceito_correto","excecao_omitida",3,
 "Os itens de consumo adquiridos para suprir as demandas das estruturas da Administração Pública deverão ser de qualidade comum, não superior à necessária para cumprir as finalidades às quais se destinam, vedada a aquisição de artigos de luxo, e os Poderes Executivo, Legislativo e Judiciário definirão em regulamento os limites para o enquadramento dos bens de consumo nas categorias comum e luxo.",
 "Os itens de consumo adquiridos para suprir as demandas das estruturas da Administração Pública poderão ser de qualidade superior à necessária, admitida a aquisição de artigos de luxo mediante motivação, e o Poder Executivo federal definirá, para todos os Poderes, os limites das categorias comum e luxo.",
 "Art. 20, caput e § 1º.","admite luxo","t06f")
P("T06",["21"],"conceito_correto","troca_numero",3,
 "A Administração poderá convocar, com antecedência mínima de 8 dias úteis, audiência pública, presencial ou a distância, na forma eletrônica, sobre licitação que pretenda realizar, com disponibilização prévia de informações pertinentes, inclusive de estudo técnico preliminar e elementos do edital, e poderá também submeter a licitação a prévia consulta pública.",
 "A Administração deverá convocar, com antecedência mínima de 15 dias corridos, audiência pública presencial sobre toda licitação que pretenda realizar, vedada a realização a distância na forma eletrônica, dispensada a disponibilização prévia do estudo técnico preliminar.",
 "Art. 21, caput e parágrafo único.","torna obrigatória e troca prazo","t06g")
P("T06",["22"],"conceito_correto","excecao_omitida",4,
 "O edital poderá contemplar matriz de alocação de riscos entre o contratante e o contratado; quando a contratação se referir a obras e serviços de grande vulto ou forem adotados os regimes de contratação integrada e semi-integrada, o edital obrigatoriamente contemplará essa matriz.",
 "O edital poderá contemplar matriz de alocação de riscos entre o contratante e o contratado, sendo vedada a sua adoção nas obras e serviços de grande vulto e nos regimes de contratação integrada e semi-integrada, nos quais os riscos serão sempre suportados pela Administração.",
 "Art. 22, caput e § 3º.","veda matriz nos casos obrigatórios","t06h")
P("T06",["22"],"conceito_correto","troca_efeito",4,
 "Nas contratações integradas ou semi-integradas, os riscos decorrentes de fatos supervenientes à contratação associados à escolha da solução de projeto básico pelo contratado deverão ser alocados como de sua responsabilidade na matriz de riscos.",
 "Nas contratações integradas ou semi-integradas, os riscos decorrentes de fatos supervenientes à contratação associados à escolha da solução de projeto básico pelo contratado deverão ser alocados como de responsabilidade da Administração na matriz de riscos.",
 "Art. 22, § 4º.","inverte a responsabilidade","t06i")
