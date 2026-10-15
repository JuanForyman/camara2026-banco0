# Decreto 9.203/2017 — lote L6
Q = []
TAILS=[
 " Essa disciplina consta do Decreto que institui a política de governança da administração pública federal direta, autárquica e fundacional.",
 " Trata-se de regra aplicável aos órgãos e às entidades da administração pública federal direta, autárquica e fundacional.",
 " Tal compreensão decorreria, segundo esse entendimento, da sistemática geral da política de governança pública federal.",
 " Essa seria a orientação extraída do decreto para a organização e o funcionamento da governança no âmbito federal.",
]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# D01
P("D01",["2.I"],"conceito_correto","confusao_instituto",2,
 "Governança pública é o conjunto de mecanismos de liderança, estratégia e controle postos em prática para avaliar, direcionar e monitorar a gestão, com vistas à condução de políticas públicas e à prestação de serviços de interesse da sociedade.",
 "Governança pública é o conjunto de mecanismos de planejamento, execução e fiscalização postos em prática pelos órgãos de controle externo para avaliar a legalidade dos atos de gestão, com vistas à responsabilização dos agentes públicos.",
 "Art. 2º, I.","troca elementos do conceito","d9203a")
P("D01",["2.II"],"conceito_correto","troca_efeito",3,
 "Valor público corresponde aos produtos e resultados gerados, preservados ou entregues pelas atividades de uma organização que representem respostas efetivas e úteis às necessidades ou às demandas de interesse público e modifiquem aspectos do conjunto da sociedade ou de alguns grupos específicos reconhecidos como destinatários legítimos de bens e serviços públicos.",
 "Valor público corresponde exclusivamente ao resultado financeiro positivo gerado pelas atividades de uma organização estatal, medido pela economia de recursos obtida em relação ao orçamento aprovado.",
 "Art. 2º, II.","reduz a resultado financeiro","d9203b")
P("D01",["2.III"],"conceito_correto","troca_numero",4,
 "Para os efeitos do Decreto, integram a alta administração os Ministros de Estado, os ocupantes de cargos de natureza especial, os ocupantes de cargo de nível 6 do Grupo-Direção e Assessoramento Superiores (DAS) e os presidentes e diretores de autarquias, inclusive as especiais, e de fundações públicas, ou autoridades de hierarquia equivalente.",
 "Para os efeitos do Decreto, integram a alta administração os Ministros de Estado, os ocupantes de cargos de natureza especial, os ocupantes de cargo de nível 4 ou superior do Grupo-Direção e Assessoramento Superiores (DAS) e os chefes de unidades de assessoramento de quaisquer órgãos federais.",
 "Art. 2º, III: DAS nível 6.","troca nível do DAS","d9203c")
P("D01",["2.IV"],"conceito_correto","troca_autoridade",3,
 "A gestão de riscos é o processo de natureza permanente, estabelecido, direcionado e monitorado pela alta administração, que contempla as atividades de identificar, avaliar e gerenciar potenciais eventos que possam afetar a organização, destinado a fornecer segurança razoável quanto à realização de seus objetivos.",
 "A gestão de riscos é o processo de natureza eventual, estabelecido e monitorado pela unidade de auditoria interna, que contempla as atividades de identificar e punir os responsáveis por eventos que afetem a organização, destinado a fornecer segurança absoluta quanto à realização de seus objetivos.",
 "Art. 2º, IV.","troca natureza, responsável e grau de segurança","d9203d")
# D02
P("D02",["3"],"conceito_correto","troca_numero",3,
 "São princípios da governança pública a capacidade de resposta, a integridade, a confiabilidade, a melhoria regulatória, a prestação de contas e responsabilidade e a transparência.",
 "São princípios da governança pública a legalidade, a impessoalidade, a moralidade, a publicidade e a eficiência, nos mesmos termos do caput do art. 37 da Constituição Federal.",
 "Art. 3º, I a VI.","substitui pelos princípios do art. 37 da CF","d9203e")
P("D02",["3"],"conceito_correto","excecao_omitida",3,
 "A melhoria regulatória e a prestação de contas e responsabilidade integram o rol de princípios da governança pública, ao lado da capacidade de resposta, da integridade, da confiabilidade e da transparência.",
 "A economicidade e a participação social integram o rol de princípios da governança pública, ao lado da capacidade de resposta, da integridade, da confiabilidade e da transparência.",
 "Art. 3º, IV e V.","inclui princípios inexistentes","d9203f")
P("D02",["4.VI"],"conceito_correto","troca_efeito",3,
 "Entre as diretrizes da governança pública está a implementação de controles internos fundamentados na gestão de risco, que privilegiará ações estratégicas de prevenção antes de processos sancionadores.",
 "Entre as diretrizes da governança pública está a implementação de controles internos fundamentados na gestão de risco, que privilegiará a instauração de processos sancionadores antes de ações estratégicas de prevenção.",
 "Art. 4º, VI.","inverte prevenção e sanção","d9203g")
P("D02",["4.V"],"conceito_correto","troca_autoridade",3,
 "Constitui diretriz da governança pública fazer incorporar padrões elevados de conduta pela alta administração para orientar o comportamento dos agentes públicos, em consonância com as funções e as atribuições de seus órgãos e de suas entidades.",
 "Constitui diretriz da governança pública fazer incorporar padrões elevados de conduta pelos agentes públicos de nível operacional para orientar o comportamento da alta administração, em consonância com as funções e as atribuições dos órgãos de controle.",
 "Art. 4º, V.","inverte quem orienta quem","d9203h")
P("D02",["4.II","4.XI"],"conceito_correto","excecao_omitida",3,
 "São diretrizes da governança pública promover a simplificação administrativa, a modernização da gestão pública e a integração dos serviços públicos, especialmente os prestados por meio eletrônico, e promover a comunicação aberta, voluntária e transparente das atividades e dos resultados da organização.",
 "São diretrizes da governança pública restringir a divulgação das atividades e dos resultados da organização ao público interno, a fim de preservar a imagem institucional, e priorizar os serviços presenciais em detrimento dos prestados por meio eletrônico.",
 "Art. 4º, II e XI.","inverte transparência","d9203i")
P("D02",["4.VIII","4.IX"],"conceito_correto","excecao_omitida",3,
 "Constituem diretrizes da governança pública manter processo decisório orientado pelas evidências, pela conformidade legal, pela qualidade regulatória, pela desburocratização e pelo apoio à participação da sociedade, bem como editar e revisar atos normativos, realizando consultas públicas sempre que conveniente.",
 "Constituem diretrizes da governança pública manter processo decisório orientado pela experiência pessoal da alta administração, dispensada a conformidade legal quando houver urgência, bem como editar atos normativos, sendo obrigatória a realização de consulta pública em todos os casos.",
 "Art. 4º, VIII e IX (consultas públicas quando conveniente).","torna obrigatória a consulta","d9203j")
P("D02",["4.X","4.III"],"conceito_correto","excecao_omitida",3,
 "É diretriz da governança pública definir formalmente as funções, as competências e as responsabilidades das estruturas e dos arranjos institucionais, assim como monitorar o desempenho e avaliar a concepção, a implementação e os resultados das políticas e das ações prioritárias.",
 "É diretriz da governança pública deixar informal a definição das funções e das responsabilidades das estruturas institucionais, para conferir flexibilidade, e avaliar os resultados das políticas somente após o seu encerramento.",
 "Art. 4º, III e X.","nega a definição formal","d9203k")
# D03
P("D03",["5"],"conceito_correto","troca_numero",2,
 "São mecanismos para o exercício da governança pública a liderança, a estratégia e o controle.",
 "São mecanismos para o exercício da governança pública a liderança, a estratégia, o controle e a auditoria independente.",
 "Art. 5º, I a III.","acrescenta mecanismo","d9203l")
P("D03",["5.I"],"conceito_correto","excecao_omitida",3,
 "Na liderança, as condições mínimas para o exercício da boa governança são a integridade, a competência, a responsabilidade e a motivação.",
 "Na liderança, as condições mínimas para o exercício da boa governança são a integridade, a competência, a transparência e a legalidade.",
 "Art. 5º, I, a a d.","troca elementos da liderança","d9203m")
P("D03",["5.III"],"conceito_correto","troca_efeito",3,
 "O controle, como mecanismo de governança, compreende processos estruturados para mitigar os possíveis riscos com vistas ao alcance dos objetivos institucionais e para garantir a execução ordenada, ética, econômica, eficiente e eficaz das atividades da organização, com preservação da legalidade e da economicidade no dispêndio de recursos públicos.",
 "O controle, como mecanismo de governança, compreende a definição de diretrizes, objetivos, planos e ações, além de critérios de priorização e alinhamento entre organizações e partes interessadas, para que os serviços e produtos alcancem o resultado pretendido.",
 "Art. 5º, II e III (definição trocada pela de estratégia).","troca controle por estratégia","d9203n")
P("D03",["6"],"conceito_correto","troca_autoridade",3,
 "Cabe à alta administração dos órgãos e das entidades implementar e manter mecanismos, instâncias e práticas de governança em consonância com os princípios e as diretrizes do Decreto, que incluirão, no mínimo, formas de acompanhamento de resultados, soluções para melhoria do desempenho das organizações e instrumentos de promoção do processo decisório fundamentado em evidências.",
 "Cabe exclusivamente ao Comitê Interministerial de Governança implementar e manter mecanismos, instâncias e práticas de governança nos órgãos e entidades, que incluirão, no mínimo, formas de acompanhamento de resultados, ficando dispensadas soluções para melhoria do desempenho.",
 "Art. 6º, caput e parágrafo único.","atribui ao CIG","d9203o")
# D04
P("D04",["7A"],"conceito_correto","troca_autoridade",3,
 "O Comitê Interministerial de Governança (CIG) tem por finalidade assessorar o Presidente da República na condução da política de governança da administração pública federal.",
 "O Comitê Interministerial de Governança (CIG) tem por finalidade assessorar o Tribunal de Contas da União na condução da política de governança da administração pública federal e substituir os órgãos de controle interno.",
 "Art. 7º-A.","troca destinatário do assessoramento","d9203p")
P("D04",["7A","8B"],"conceito_correto","troca_numero",4,
 "O CIG se reunirá, em caráter ordinário, trimestralmente e, em caráter extraordinário, sempre que necessário; o quórum de reunião é de maioria simples dos membros e o de aprovação, de maioria absoluta, e o Coordenador, além do voto ordinário, tem voto de qualidade em caso de empate.",
 "O CIG se reunirá, em caráter ordinário, mensalmente e, em caráter extraordinário, sempre que necessário; o quórum de reunião é de maioria absoluta dos membros e o de aprovação, de maioria simples, e o Coordenador não tem voto de qualidade em caso de empate.",
 "Art. 8º-B, caput e §§ 1º e 2º.","troca periodicidade e quórum","d9203q")
P("D04",["7A"],"conceito_correto","excecao_omitida",3,
 "Representantes de outros órgãos e entidades da administração pública federal poderão ser convidados a participar de reuniões do CIG, sem direito a voto, e os membros do CIG poderão ser substituídos, em suas ausências e impedimentos, pelos respectivos Secretários-Executivos.",
 "Representantes de outros órgãos e entidades da administração pública federal poderão ser convidados a participar de reuniões do CIG, com direito a voto, e os membros do CIG não poderão ser substituídos em suas ausências e impedimentos.",
 "Art. 7º-A, §§ 1º e 3º.","dá voto aos convidados","d9203r")
P("D04",["9A"],"conceito_correto","troca_autoridade",4,
 "Compete ao CIG propor medidas, mecanismos e práticas organizacionais para o atendimento aos princípios e às diretrizes de governança pública, aprovar manuais e guias, aprovar recomendações aos colegiados temáticos, incentivar e monitorar a aplicação das melhores práticas de governança e editar as resoluções necessárias ao exercício de suas competências.",
 "Compete ao CIG executar diretamente a política de governança nos órgãos e entidades, aplicar sanções aos dirigentes que descumprirem os manuais e guias e editar decretos necessários ao exercício de suas competências.",
 "Art. 9º-A, I a V.","atribui poder sancionatório e de decreto","d9203s")
P("D04",["9A"],"conceito_correto","excecao_omitida",4,
 "Os manuais e os guias aprovados pelo CIG deverão conter recomendações que possam ser implementadas nos órgãos e nas entidades definidos na resolução que os aprovar e ser observados pelos comitês internos de governança.",
 "Os manuais e os guias aprovados pelo CIG são de observância facultativa pelos comitês internos de governança, e suas recomendações vinculam todos os órgãos da administração pública federal independentemente de definição na resolução que os aprovar.",
 "Art. 9º-A, § 1º, I e II.","torna facultativos e vincula todos","d9203t")
P("D04",["9A"],"conceito_correto","confusao_instituto",4,
 "Para fins do Decreto, o colegiado temático é a comissão, o comitê, o grupo de trabalho ou outra forma de colegiado interministerial instituído com o objetivo de implementar, promover ou executar políticas ou programas de governança relativos a temas específicos.",
 "Para fins do Decreto, o colegiado temático é o comitê interno de governança instituído em cada órgão ou entidade com o objetivo de auxiliar a alta administração na implementação e na manutenção de processos e estruturas de governança.",
 "Art. 9º-A, § 2º (distinto do comitê interno do art. 15-A).","confunde colegiado temático com comitê interno","d9203u")
P("D04",["10B"],"conceito_correto","troca_numero",4,
 "Os grupos de trabalho instituídos pelo CIG serão compostos na forma de ato do CIG, não poderão ter mais de cinco membros, terão caráter temporário e duração não superior a um ano e estarão limitados a três operando simultaneamente.",
 "Os grupos de trabalho instituídos pelo CIG serão compostos na forma de ato do Presidente da República, não poderão ter mais de sete membros, terão caráter permanente e estarão limitados a cinco operando simultaneamente.",
 "Art. 10-B, I a IV.","troca limites dos GT","d9203v")
P("D04",["10A"],"conceito_correto","troca_autoridade",3,
 "Representantes de órgãos e entidades públicas e privadas poderão ser convidados a participar dos grupos de trabalho constituídos pelo CIG, que definirá no ato de instituição os seus objetivos específicos, a sua composição e o prazo para conclusão dos trabalhos.",
 "Somente representantes de órgãos e entidades públicas poderão ser convidados a participar dos grupos de trabalho constituídos pelo CIG, e a composição e o prazo para conclusão dos trabalhos serão definidos pelo Presidente da República.",
 "Art. 10-A, §§ 1º e 2º.","restringe convidados e troca autoridade","d9203w")
P("D04",["11A"],"conceito_correto","troca_autoridade",3,
 "A Secretaria-Executiva do CIG é exercida pela Secretaria Especial de Relações Governamentais da Casa Civil da Presidência da República, e a ela compete, entre outras atribuições, receber, instruir e encaminhar aos membros do CIG as propostas recebidas e encaminhar a pauta, a documentação e os registros das reuniões.",
 "A Secretaria-Executiva do CIG é exercida pela Controladoria-Geral da União, e a ela compete, entre outras atribuições, deliberar sobre as propostas recebidas e convocar as reuniões extraordinárias do CIG.",
 "Art. 11-A (redação do Decreto 10.907/2021) e parágrafo único.","troca órgão e funções","d9203x",
 {"risco":["nomenclatura_superada"]})
P("D04",["13A"],"conceito_correto","excecao_omitida",3,
 "Compete aos órgãos e às entidades da administração pública federal direta, autárquica e fundacional executar a política de governança pública, incorporando os princípios e as diretrizes do Decreto e as recomendações de manuais, guias e resoluções do CIG, e encaminhar ao CIG propostas relacionadas às competências previstas no art. 9º-A.",
 "Compete aos órgãos e às entidades da administração pública federal direta, autárquica e fundacional apenas executar a política de governança pública, sendo vedado encaminhar ao CIG propostas relacionadas às competências do Comitê.",
 "Art. 13-A, I e II.","veda proposta ao CIG","d9203y")
P("D04",["15A"],"conceito_correto","troca_autoridade",3,
 "Os comitês internos de governança, instituídos pelos órgãos e entidades, têm competência para auxiliar a alta administração na implementação e na manutenção de processos, estruturas e mecanismos adequados à incorporação dos princípios e das diretrizes da governança, promover e acompanhar a implementação das medidas definidas pelo CIG e elaborar manifestação técnica relativa aos temas de sua competência.",
 "Os comitês internos de governança, instituídos pelos órgãos e entidades, têm competência para editar as resoluções que vinculam o CIG, aplicar sanções aos servidores que descumprirem as medidas de governança e substituir a alta administração na implementação dos processos.",
 "Art. 15-A, I a IV.","inverte relação com o CIG","d9203z")
P("D04",["16"],"conceito_correto","excecao_omitida",3,
 "Os comitês internos de governança publicarão suas atas e suas resoluções em sítio eletrônico, ressalvado o conteúdo sujeito a sigilo.",
 "Os comitês internos de governança manterão suas atas e suas resoluções em sigilo, divulgando-as em sítio eletrônico apenas mediante requerimento fundamentado de interessado.",
 "Art. 16.","inverte publicidade e sigilo","d9203aa")
# D05
P("D05",["17"],"conceito_correto","troca_autoridade",3,
 "A alta administração das organizações da administração pública federal direta, autárquica e fundacional deverá estabelecer, manter, monitorar e aprimorar sistema de gestão de riscos e controles internos com vistas à identificação, à avaliação, ao tratamento, ao monitoramento e à análise crítica de riscos que possam impactar a implementação da estratégia e a consecução dos objetivos da organização.",
 "A unidade de auditoria interna das organizações da administração pública federal direta, autárquica e fundacional deverá estabelecer, manter e executar sistema de gestão de riscos e controles internos, ficando a alta administração dispensada dessa atribuição.",
 "Art. 17, caput.","atribui à auditoria interna","d9203ab")
P("D05",["17"],"conceito_correto","troca_numero",4,
 "Entre os princípios da gestão de riscos estão a implementação de forma sistemática, estruturada, oportuna e documentada, subordinada ao interesse público, a integração ao planejamento estratégico e o estabelecimento de controles internos proporcionais aos riscos, observada a relação custo-benefício.",
 "Entre os princípios da gestão de riscos estão a implementação de forma sigilosa e informal, subordinada ao interesse da organização, a independência em relação ao planejamento estratégico e o estabelecimento de controles internos uniformes, desconsiderada a relação custo-benefício.",
 "Art. 17, I a III.","inverte princípios","d9203ac")
P("D05",["17"],"conceito_correto","excecao_omitida",3,
 "Segundo o Decreto, os resultados da gestão de riscos devem ser utilizados para apoio à melhoria contínua do desempenho e dos processos de gerenciamento de risco, controle e governança.",
 "Segundo o Decreto, os resultados da gestão de riscos devem ser utilizados exclusivamente para fundamentar a responsabilização dos agentes públicos que deram causa aos eventos de risco.",
 "Art. 17, IV.","restringe à responsabilização","d9203ad")
P("D05",["18"],"conceito_correto","troca_efeito",3,
 "A auditoria interna governamental deverá adicionar valor e melhorar as operações das organizações, por meio da realização de trabalhos de avaliação e consultoria de forma independente, da adoção de abordagem baseada em risco para planejar suas atividades e da promoção à prevenção, à detecção e à investigação de fraudes praticadas por agentes públicos ou privados na utilização de recursos públicos federais.",
 "A auditoria interna governamental deverá limitar-se a verificar a conformidade formal dos atos de gestão, abstendo-se de consultoria, por comprometer a independência, e adotará planejamento uniforme, sem abordagem baseada em risco.",
 "Art. 18, I a III.","afasta consultoria e risco","d9203ae")
P("D05",["19"],"conceito_correto","troca_numero",3,
 "Os órgãos e as entidades da administração direta, autárquica e fundacional instituirão programa de integridade, com o objetivo de promover a adoção de medidas e ações institucionais destinadas à prevenção, à detecção, à punição e à remediação de fraudes e atos de corrupção.",
 "Os órgãos e as entidades da administração direta, autárquica e fundacional poderão instituir, facultativamente, programa de integridade, com o objetivo exclusivo de punir fraudes e atos de corrupção já praticados.",
 "Art. 19, caput.","torna facultativo","d9203af")
P("D05",["19"],"conceito_correto","excecao_omitida",4,
 "O programa de integridade dos órgãos e entidades estrutura-se nos eixos de comprometimento e apoio da alta administração, existência de unidade responsável pela implementação, análise, avaliação e gestão dos riscos associados ao tema da integridade e monitoramento contínuo dos atributos do programa.",
 "O programa de integridade dos órgãos e entidades estrutura-se nos eixos de comprometimento da alta administração, existência de canal de denúncias externo, aplicação de sanções disciplinares e auditoria anual realizada pelo Tribunal de Contas da União.",
 "Art. 19, I a IV.","troca eixos","d9203ag")
# casos concretos
P("D05",["17","19"],"caso_concreto","caso_concreto",4,
 "Uma autarquia federal instituiu programa de integridade com apoio expresso do seu presidente, designou unidade responsável pela implementação e realiza monitoramento contínuo dos atributos do programa, mas ainda não analisou os riscos associados ao tema da integridade. Nessa situação, falta ao programa o eixo de análise, avaliação e gestão dos riscos associados à integridade.",
 "Uma autarquia federal instituiu programa de integridade com apoio expresso do seu presidente, designou unidade responsável pela implementação e realiza monitoramento contínuo dos atributos do programa, mas ainda não analisou os riscos associados ao tema da integridade. Nessa situação, o programa está completo, pois a análise de riscos é eixo exclusivo do sistema de gestão de riscos do art. 17 e não do programa de integridade.",
 "Art. 19, III.","afasta eixo de riscos","d9203ah")
P("D03",["4.VI","6"],"caso_concreto","caso_concreto",4,
 "Ministério federal pretende reforçar a governança de suas políticas, de modo que a alta administração implemente mecanismos de acompanhamento de resultados e instrumentos de decisão baseada em evidências, aplicando controles internos baseados em gestão de risco que priorizem a prevenção antes dos processos sancionadores. A medida está em consonância com o Decreto 9.203/2017.",
 "Ministério federal pretende reforçar a governança de suas políticas, de modo que a alta administração implemente mecanismos de acompanhamento de resultados e instrumentos de decisão baseada em evidências, aplicando controles internos baseados em gestão de risco que priorizem os processos sancionadores antes da prevenção. A medida está em consonância com o Decreto 9.203/2017.",
 "Art. 4º, VI, e art. 6º.","inverte ordem entre prevenção e sanção","d9203ai")
