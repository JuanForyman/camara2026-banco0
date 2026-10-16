# Modelos de gestão e governança — lote L11
Q = []
TAILS=[" Essa seria a orientação adotada pela doutrina e pela jurisprudência no direito brasileiro.",
 " Trata-se de entendimento aplicável à responsabilidade civil das pessoas jurídicas de direito público no Brasil.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática constitucional da responsabilidade do Estado.",
 " Essa seria a regra para os danos causados a terceiros no exercício da função pública."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
FD={"tipo":"doutrina_jurisprudencia","ref":"doutrina majoritária; Plano Diretor da Reforma do Aparelho do Estado","versao":"conhecimento do autor","conferida":"conhecimento"}
FJ={"tipo":"jurisprudencia","ref":"Teses de repercussão geral do STF (tesesesumulas.com.br, 2026-10-16)","versao":"conhecimento verificado em fonte secundária","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, jur=False, lei=False):
    ex = {}
    if lei: ex["fonte"]={"tipo":"lei","ref":"Plano Diretor 1995; Decreto 9.203/2017","versao":"vigente","conferida":"conhecimento"}
    elif jur: ex["fonte"]=FJ; ex["risco"]=["jurisprudencia_conhecimento"]
    else: ex["fonte"]=FD; ex["risco"]=["doutrina_conhecimento"]
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# G01
P("G01",["1"],"conceito_correto","confusao_instituto",2,
 "A administração patrimonialista caracteriza-se pela confusão entre o patrimônio público e o privado do governante, sendo associada ao nepotismo, ao clientelismo e à corrupção.",
 "A administração patrimonialista caracteriza-se pela separação rigorosa entre o patrimônio público e o privado, pela profissionalização dos servidores e pelo controle rígido dos processos.",
 "Patrimonialismo.","atribui traços do modelo burocrático","g01a")
P("G01",["2"],"conceito_correto","confusao_instituto",3,
 "A administração burocrática surge para combater o patrimonialismo, baseando-se na impessoalidade, no formalismo, na hierarquia funcional e no mérito profissional, com controle a priori dos processos.",
 "A administração burocrática surge para combater a ineficiência do modelo gerencial, baseando-se na flexibilização das regras, na competição administrada e no controle a posteriori dos resultados.",
 "Administração burocrática.","atribui traços do modelo gerencial","g01b")
P("G01",["2"],"conceito_correto","excecao_omitida",3,
 "A ideia central da administração burocrática é o controle dos abusos por regras e procedimentos, e uma de suas disfunções é a ênfase no processo, e não no resultado, com risco de rigidez e autorreferência.",
 "A ideia central da administração burocrática é a orientação para o cidadão-cliente e para os resultados, e uma de suas virtudes é a flexibilidade na gestão, que evita o apego às normas e a autorreferência.",
 "Weber; disfunções da burocracia.","inverte virtudes e disfunções","g01c")
P("G01",["1","2"],"conceito_correto","troca_efeito",3,
 "O concurso público, a carreira e o critério do mérito são marcas da administração burocrática, que se contrapõe à prática patrimonialista de provimento dos cargos por indicação pessoal.",
 "O provimento dos cargos por indicação pessoal e a ausência de carreira são marcas da administração burocrática, que se contrapõe à prática gerencial de seleção por mérito.",
 "Patrimonialismo x burocracia.","inverte marcas dos modelos","g01d")
# G02
P("G02",["3"],"conceito_correto","confusao_instituto",3,
 "A administração gerencial, ou Nova Gestão Pública, privilegia o controle de resultados, a eficiência e a orientação ao cidadão-cliente, e admite a descentralização e a contratualização do desempenho.",
 "A administração gerencial, ou Nova Gestão Pública, privilegia o controle rígido dos processos, a hierarquia centralizada e o formalismo, e rejeita a contratualização do desempenho.",
 "NPM.","atribui traços do modelo burocrático","g02a")
P("G02",["3"],"conceito_correto","excecao_omitida",4,
 "Entre as críticas dirigidas à Nova Gestão Pública estão o risco de perda de accountability e de fragmentação das organizações e a redução do cidadão à condição de cliente, em vez de titular de direitos.",
 "Entre as críticas dirigidas à Nova Gestão Pública está o excesso de participação social na formulação das políticas, que enfraquece a eficiência, e a ausência de indicadores de desempenho.",
 "Críticas ao NPM.","atribui críticas inexistentes","g02b")
P("G02",["3"],"conceito_correto","troca_efeito",3,
 "Na Nova Gestão Pública o Estado tende a reduzir seu papel de executor direto e a ampliar o de regulador e promotor, e a competição administrada entre prestadores é um de seus instrumentos.",
 "Na Nova Gestão Pública o Estado tende a ampliar seu papel de executor direto de todos os serviços, e a competição entre prestadores é considerada incompatível com o modelo.",
 "NPM.","inverte papel do Estado","g02c")
# G03
P("G03",["4"],"conceito_correto","excecao_omitida",3,
 "O Plano Diretor da Reforma do Aparelho do Estado, de 1995, dividiu o Estado em núcleo estratégico, atividades exclusivas, serviços não exclusivos e produção de bens e serviços para o mercado.",
 "O Plano Diretor da Reforma do Aparelho do Estado, de 1995, dividiu o Estado em núcleo estratégico, atividades de apoio, serviços universais e produção de bens e serviços para o terceiro setor.",
 "Plano Diretor, 1995.","troca setores","g03a")
P("G03",["4"],"conceito_correto","troca_autoridade",4,
 "Segundo o Plano Diretor de 1995, os serviços não exclusivos do Estado, como saúde e educação, deveriam ser executados por entidades de propriedade pública não estatal, por meio da publicização, com organizações sociais e contratos de gestão.",
 "Segundo o Plano Diretor de 1995, os serviços não exclusivos do Estado, como saúde e educação, deveriam ser privatizados e executados por empresas privadas com fins lucrativos, sem contrato de gestão.",
 "Plano Diretor, 1995.","confunde publicização e privatização","g03b")
P("G03",["4"],"conceito_correto","excecao_omitida",4,
 "A Emenda Constitucional 19/1998 incluiu a eficiência entre os princípios expressos da Administração Pública, no art. 37 da Constituição, e previu o contrato de gestão como instrumento de ampliação da autonomia gerencial de órgãos e entidades.",
 "A Emenda Constitucional 19/1998 incluiu a eficiência entre os princípios da Administração Pública, no art. 5º da Constituição, e proibiu a celebração de contrato de gestão por órgãos e entidades da Administração.",
 "EC 19/1998; CF, art. 37, caput e § 8º.","troca dispositivo e proíbe contrato","g03c",lei=True)
P("G03",["5"],"conceito_correto","troca_numero",3,
 "O DASP, criado na Era Vargas, é considerado marco da reforma burocrática no Brasil, e o Decreto-Lei 200/1967 é apontado como tentativa pioneira de reforma gerencial.",
 "O DASP, criado na Era Vargas, é considerado marco da reforma gerencial no Brasil, e o Decreto-Lei 200/1967 é apontado como marco da reforma burocrática.",
 "Evolução da gestão pública no Brasil.","inverte marcos","g03d")
P("G03",["5"],"conceito_correto","excecao_omitida",4,
 "Para os formuladores da reforma de 1995, a Constituição de 1988 representou um retrocesso burocrático, por enrijecer o regime jurídico dos servidores e os controles sobre a Administração.",
 "Para os formuladores da reforma de 1995, a Constituição de 1988 representou um avanço gerencial, por flexibilizar o regime jurídico dos servidores e os controles sobre a Administração.",
 "Reforma de 1995.","inverte avaliação","g03e")
# G04
P("G04",["6"],"conceito_correto","confusao_instituto",3,
 "A Nova Governança Pública enfatiza as redes, as parcerias e a interdependência entre organizações, reconhecendo que o Estado deixa de ser o único ator na construção e na entrega das políticas públicas.",
 "A Nova Governança Pública enfatiza a competição de mercado entre organizações isoladas e a primazia do Estado como único ator na construção e na entrega das políticas públicas.",
 "NPG.","atribui traços do NPM","g04a")
P("G04",["6"],"conceito_correto","excecao_omitida",4,
 "A evolução dos modelos pode ser sintetizada na sequência administração pública tradicional, Nova Gestão Pública e Nova Governança Pública, esta última voltada à coordenação horizontal em rede e à produção de valor público.",
 "A evolução dos modelos pode ser sintetizada na sequência Nova Governança Pública, Nova Gestão Pública e administração pública tradicional, esta última voltada à coordenação horizontal em rede.",
 "Evolução dos modelos.","inverte sequência","g04b")
P("G04",["7"],"conceito_correto","excecao_omitida",3,
 "A ação pública em redes envolve colaboração entre órgãos governamentais, setor privado e terceiro setor, com compartilhamento de recursos e responsabilidades, e traz o desafio da accountability difusa.",
 "A ação pública em redes envolve apenas a colaboração entre órgãos governamentais, sendo vedada a participação do setor privado e do terceiro setor, e elimina o problema da accountability.",
 "Redes de cooperação.","exclui setor privado","g04c")
P("G04",["8"],"conceito_correto","confusao_instituto",3,
 "A coprodução do bem público pressupõe que os cidadãos participem, junto com o Estado, da produção e da entrega dos serviços e das políticas, e não apenas como seus destinatários.",
 "A coprodução do bem público pressupõe que os cidadãos sejam apenas destinatários passivos dos serviços, cabendo exclusivamente ao Estado produzi-los e entregá-los.",
 "Coprodução.","exclui participação","g04d")
P("G04",["8"],"conceito_correto","confusao_instituto",3,
 "A transparência ativa consiste na divulgação de informações de interesse coletivo por iniciativa do próprio órgão, independentemente de requerimento, ao passo que a transparência passiva depende de pedido do interessado.",
 "A transparência ativa consiste na disponibilização de informações em atendimento a pedido do interessado, ao passo que a transparência passiva consiste na divulgação por iniciativa do órgão.",
 "Lei 12.527/2011, art. 8º.","inverte ativa e passiva","g04e",lei=True)
P("G04",["9"],"conceito_correto","confusao_instituto",4,
 "Na cadeia de valor público, os insumos são transformados, por meio de processos, em produtos, que geram resultados e impactos para a sociedade.",
 "Na cadeia de valor público, os impactos geram resultados, que determinam os produtos, os quais são transformados, por meio de processos, em insumos.",
 "Cadeia de valor público.","inverte cadeia","g04f")
P("G04",["9"],"conceito_correto","confusao_instituto",4,
 "Para Mark Moore, a criação de valor público pelo gestor exige o alinhamento entre o valor público a ser entregue, a legitimidade e o apoio político e a capacidade operacional da organização.",
 "Para Mark Moore, a criação de valor público pelo gestor exige apenas a maximização do lucro e a redução de custos da organização, independentemente de legitimidade e apoio político.",
 "Triângulo estratégico de Moore.","reduz a lucro","g04g")
# G05
P("G05",["10"],"conceito_correto","confusao_instituto",3,
 "A governança diz respeito à capacidade técnica e institucional do Estado de formular e implementar políticas, ao passo que a governabilidade se refere às condições políticas do exercício do poder, como apoio e legitimidade.",
 "A governabilidade diz respeito à capacidade técnica e institucional do Estado de formular e implementar políticas, ao passo que a governança se refere às condições políticas do exercício do poder, como apoio e legitimidade.",
 "Governança x governabilidade.","inverte conceitos","g05a")
P("G05",["10"],"conceito_correto","troca_autoridade",3,
 "Nos termos do Decreto 9.203/2017, governança pública é o conjunto de mecanismos de liderança, estratégia e controle postos em prática para avaliar, direcionar e monitorar a gestão, com vistas à condução de políticas públicas e à prestação de serviços de interesse da sociedade.",
 "Nos termos do Decreto 9.203/2017, governança pública é o conjunto de mecanismos de planejamento, execução e fiscalização postos em prática para executar a gestão, com vistas à condução exclusiva das políticas econômicas.",
 "Decreto 9.203/2017, art. 2º, I.","troca mecanismos e finalidade","g05b",lei=True)
P("G05",["10"],"conceito_correto","confusao_instituto",4,
 "Enquanto a governança direciona, avalia e monitora a gestão, a gestão é responsável pela execução e pela operação das ações, no âmbito da estratégia definida.",
 "Enquanto a gestão direciona, avalia e monitora a governança, a governança é responsável pela execução e pela operação das ações, no âmbito da estratégia definida.",
 "Governança x gestão.","inverte governança e gestão","g05c")
P("G05",["10"],"conceito_correto","excecao_omitida",3,
 "São princípios da governança pública, nos termos do Decreto 9.203/2017, a capacidade de resposta, a integridade, a confiabilidade, a melhoria regulatória, a prestação de contas e responsabilidade e a transparência.",
 "São princípios da governança pública, nos termos do Decreto 9.203/2017, a capacidade de resposta, o sigilo, a confiabilidade, a maximização do lucro, a prestação de contas e responsabilidade e a transparência.",
 "Decreto 9.203/2017, art. 3º.","troca princípios","g05d",lei=True)
P("G05",["11"],"conceito_correto","troca_numero",3,
 "Os mecanismos de governança compreendem liderança, estratégia e controle, e o controle abrange a gestão de riscos, os controles internos, a auditoria interna e a prestação de contas.",
 "Os mecanismos de governança compreendem liderança, execução e controle, e o controle abrange apenas a prestação de contas, excluídas a gestão de riscos e a auditoria interna.",
 "Mecanismos de governança.","troca mecanismo e restringe controle","g05e")
P("G05",["11"],"conceito_correto","excecao_omitida",4,
 "No mecanismo de estratégia, as organizações públicas devem ouvir as partes interessadas, definir diretrizes e acompanhar a execução, e o de liderança envolve integridade, competência, responsabilidade e motivação.",
 "No mecanismo de liderança, as organizações públicas devem ouvir as partes interessadas, definir diretrizes e acompanhar a execução, e o de estratégia envolve integridade, competência, responsabilidade e motivação.",
 "Mecanismos de governança.","troca liderança e estratégia","g05f")
# G06
P("G06",["12"],"conceito_correto","troca_efeito",4,
 "A avaliação de impactos busca aferir o efeito causal da política sobre a população-alvo e se distingue do monitoramento, que acompanha a execução de insumos e produtos.",
 "A avaliação de impactos busca apenas acompanhar a execução de insumos e produtos da política, e se confunde com o monitoramento, que afere o efeito causal sobre a população-alvo.",
 "Avaliação de impactos.","confunde avaliação e monitoramento","g06a")
P("G06",["9","12"],"conceito_correto","confusao_instituto",4,
 "A eficiência relaciona insumos e produtos, a eficácia refere-se ao alcance das metas e dos resultados previstos, e a efetividade refere-se ao impacto da política sobre a realidade social.",
 "A eficácia relaciona insumos e produtos, a efetividade refere-se ao alcance das metas previstas, e a eficiência refere-se ao impacto da política sobre a realidade social.",
 "Eficiência, eficácia e efetividade.","troca conceitos","g06b")
P("G06",["12"],"conceito_correto","excecao_omitida",3,
 "A avaliação ex ante analisa a viabilidade da política antes de sua implementação, e a avaliação ex post examina os resultados e impactos depois de implementada.",
 "A avaliação ex post analisa a viabilidade da política antes de sua implementação, e a avaliação ex ante examina os resultados e impactos depois de implementada.",
 "Avaliação de políticas.","inverte ex ante e ex post","g06c")
P("G06",["12"],"conceito_correto","excecao_omitida",3,
 "A geração de valor público pressupõe a entrega de resultados à sociedade e a observância da sustentabilidade, entendida em suas dimensões econômica, social e ambiental, e no tempo.",
 "A geração de valor público dispensa a observância da sustentabilidade, que é considerada de responsabilidade exclusiva do setor privado, pois o Estado atua apenas na dimensão social.",
 "Valor público e sustentabilidade.","exclui sustentabilidade","g06d")
