# LGPD — lote L5, parte b (G09–G15)
Q = []
TAILS=[
 " Essa disciplina integra a Lei Geral de Proteção de Dados Pessoais e alcança o tratamento realizado no território nacional, ainda que por meios digitais.",
 " Trata-se de regra aplicável a qualquer operação de tratamento de dados pessoais, realizada por pessoa natural ou jurídica, de direito público ou privado.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática geral da LGPD, que se aplica aos agentes de tratamento em todas as fases da operação.",
 " Essa seria a orientação extraída da lei para as hipóteses em que o tratamento envolve dados de pessoas naturais identificadas ou identificáveis.",
]
def tail(E,C,i):
    if len(E) < 0.97*len(C):
        need=len(C)-len(E)
        t=TAILS[i%len(TAILS)]
        return E+t if need>60 else E+t[:0]
    return E

def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, ex=None, comE=None):
    ex = ex or {}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, comE or com, terro, tag, ex))
# ---- G09
P("G09",["23"],"conceito_correto","excecao_omitida",3,
 "O tratamento de dados pessoais pelas pessoas jurídicas de direito público referidas na Lei de Acesso à Informação deverá ser realizado para o atendimento de sua finalidade pública, na persecução do interesse público, com o objetivo de executar as competências legais ou cumprir as atribuições legais do serviço público, desde que sejam informadas as hipóteses em que realizam o tratamento, em veículos de fácil acesso, preferencialmente em seus sítios eletrônicos, e seja indicado um encarregado.",
 "O tratamento de dados pessoais pelas pessoas jurídicas de direito público poderá ser realizado para finalidades definidas pelo gestor, dispensada a divulgação das hipóteses em que realizam o tratamento e a indicação de encarregado, que é obrigatório apenas para o setor privado.",
 "Art. 23, I e III.","dispensa publicidade e encarregado","g09a")
P("G09",["23"],"conceito_correto","troca_efeito",3,
 "O disposto na LGPD não dispensa as pessoas jurídicas de direito público de instituir as autoridades de que trata a Lei de Acesso à Informação, e os prazos e procedimentos para exercício dos direitos do titular perante o Poder Público observarão a legislação específica, em especial a Lei do Habeas Data, a Lei Geral do Processo Administrativo e a Lei de Acesso à Informação.",
 "A LGPD dispensa as pessoas jurídicas de direito público de instituir as autoridades de que trata a Lei de Acesso à Informação, e os prazos e procedimentos para exercício dos direitos do titular perante o Poder Público seguirão exclusivamente o regulamento da ANPD.",
 "Art. 23, §§ 2.º e 3.º.","afasta LAI e leis de procedimento","g09b")
P("G09",["23"],"conceito_correto","excecao_omitida",3,
 "Os serviços notariais e de registro exercidos em caráter privado, por delegação do Poder Público, terão o mesmo tratamento dispensado às pessoas jurídicas de direito público, e os órgãos notariais e de registro devem fornecer acesso aos dados por meio eletrônico para a administração pública.",
 "Os serviços notariais e de registro exercidos em caráter privado, por delegação do Poder Público, terão o mesmo tratamento dispensado às pessoas jurídicas de direito privado, ficando dispensados de fornecer acesso eletrônico aos dados para a administração pública.",
 "Art. 23, §§ 4.º e 5.º.","troca tratamento","g09c")
P("G09",["24"],"conceito_correto","excecao_omitida",3,
 "As empresas públicas e as sociedades de economia mista que atuam em regime de concorrência terão o mesmo tratamento dispensado às pessoas jurídicas de direito privado particulares; quando operacionalizarem políticas públicas, no âmbito da execução delas, terão o mesmo tratamento dispensado aos órgãos e entidades do Poder Público.",
 "As empresas públicas e as sociedades de economia mista terão sempre o mesmo tratamento dispensado aos órgãos do Poder Público, inclusive quando atuarem em regime de concorrência, sujeitas ao art. 173 da Constituição Federal.",
 "Art. 24 e parágrafo único.","ignora regime de concorrência","g09d")
P("G09",["26"],"conceito_correto","excecao_omitida",4,
 "É vedado ao Poder Público transferir a entidades privadas dados pessoais constantes de bases de dados a que tenha acesso, exceto, entre outros casos, na execução descentralizada de atividade pública que exija a transferência, exclusivamente para esse fim específico e determinado, quando os dados forem acessíveis publicamente, quando houver previsão legal ou respaldo em contratos, convênios ou instrumentos congêneres, ou para prevenção de fraudes e irregularidades.",
 "É permitido ao Poder Público transferir a entidades privadas dados pessoais constantes de bases de dados a que tenha acesso, sempre que houver interesse comercial da entidade, dispensada a comunicação à autoridade nacional dos contratos e convênios que respaldem a transferência.",
 "Art. 26, § 1.º, I, III, IV e V, e § 2.º.","libera a transferência","g09e")
P("G09",["26","27"],"conceito_correto","excecao_omitida",4,
 "A comunicação ou o uso compartilhado de dados pessoais de pessoa jurídica de direito público a pessoa de direito privado será informado à autoridade nacional e dependerá de consentimento do titular, exceto nas hipóteses de dispensa de consentimento previstas na lei, nos casos de uso compartilhado com publicidade e nas exceções do art. 26, § 1.º.",
 "A comunicação ou o uso compartilhado de dados pessoais de pessoa jurídica de direito público a pessoa de direito privado independe de informe à autoridade nacional e de consentimento do titular, em qualquer hipótese.",
 "Art. 27, caput e I a III.","dispensa consentimento e informe","g09f")
P("G09",["25","26"],"conceito_correto","troca_efeito",3,
 "Os dados deverão ser mantidos em formato interoperável e estruturado para o uso compartilhado, com vistas à execução de políticas públicas, à prestação de serviços públicos, à descentralização da atividade pública e à disseminação e ao acesso das informações pelo público em geral; o uso compartilhado pelo Poder Público deve atender a finalidades específicas e respeitar os princípios do art. 6.º.",
 "Os dados deverão ser mantidos em formato proprietário e protegido, para impedir o uso compartilhado fora do órgão que os coletou, e o uso compartilhado pelo Poder Público independe de finalidade específica e dos princípios do art. 6.º.",
 "Arts. 25 e 26, caput.","contraria interoperabilidade","g09g")
P("G09",["29","31","32"],"conceito_correto","troca_autoridade",4,
 "A autoridade nacional poderá solicitar, a qualquer momento, aos órgãos e entidades do poder público informações específicas sobre o âmbito e a natureza dos dados e outros detalhes do tratamento, poderá enviar informe com medidas cabíveis para fazer cessar a violação quando houver infração por órgãos públicos e poderá solicitar a publicação de relatórios de impacto à proteção de dados.",
 "A autoridade nacional somente poderá solicitar informações aos órgãos e entidades do poder público mediante autorização judicial, e, havendo infração por órgãos públicos, deverá aplicar-lhes multa simples e multa diária.",
 "Arts. 29, 31 e 32; art. 52, § 3.º.","exige autorização judicial e multa","g09h")
# ---- G10
P("G10",["33"],"conceito_correto","excecao_omitida",3,
 "A transferência internacional de dados pessoais somente é permitida, entre outros casos, para países ou organismos internacionais que proporcionem grau de proteção adequado ao previsto na lei, quando o controlador oferecer e comprovar garantias de cumprimento dos princípios e direitos do titular, na forma de cláusulas contratuais específicas, cláusulas-padrão contratuais, normas corporativas globais ou selos, certificados e códigos de conduta, ou quando a autoridade nacional a autorizar.",
 "A transferência internacional de dados pessoais é livre, independentemente do grau de proteção do país de destino, bastando que o controlador comunique a transferência à autoridade nacional no prazo de trinta dias.",
 "Art. 33, I, II e V.","libera a transferência","g10a")
P("G10",["33"],"conceito_correto","excecao_omitida",4,
 "A transferência internacional é permitida também quando necessária à cooperação jurídica internacional entre órgãos públicos de inteligência, de investigação e de persecução, à proteção da vida ou da incolumidade física do titular ou de terceiro, ou à execução de política pública ou atribuição legal do serviço público, com publicidade, ou quando o titular tiver fornecido consentimento específico e em destaque, com informação prévia sobre o caráter internacional da operação.",
 "A transferência internacional é permitida quando o titular tiver fornecido consentimento genérico nos termos de uso do serviço, dispensada a informação prévia sobre o caráter internacional da operação, desde que esta se distinga das demais finalidades apenas no contrato.",
 "Art. 33, III, IV, VII e VIII.","consentimento genérico","g10b")
P("G10",["34"],"conceito_correto","troca_autoridade",3,
 "O nível de proteção de dados do país estrangeiro ou do organismo internacional será avaliado pela autoridade nacional, que levará em consideração as normas gerais e setoriais da legislação em vigor, a natureza dos dados, a observância dos princípios gerais, a adoção de medidas de segurança, a existência de garantias judiciais e institucionais e outras circunstâncias específicas.",
 "O nível de proteção de dados do país estrangeiro será avaliado pelo controlador que realizar a transferência, que levará em consideração exclusivamente as normas gerais da legislação do país de destino.",
 "Art. 34.","atribui avaliação ao controlador","g10c")
P("G10",["35","36"],"conceito_correto","troca_autoridade",4,
 "A definição do conteúdo de cláusulas-padrão contratuais, bem como a verificação de cláusulas contratuais específicas, normas corporativas globais ou selos, certificados e códigos de conduta, será realizada pela autoridade nacional, que poderá designar organismos de certificação sob sua fiscalização; as alterações nas garantias apresentadas como suficientes deverão ser comunicadas à autoridade nacional.",
 "A definição do conteúdo de cláusulas-padrão contratuais será realizada pelo controlador, que poderá designar organismos de certificação, e as alterações nas garantias apresentadas como suficientes independem de comunicação à autoridade nacional.",
 "Arts. 35 e 36.","atribui definição ao controlador","g10d")
# ---- G11
P("G11",["37","38","39"],"conceito_correto","troca_efeito",3,
 "O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem, especialmente quando baseado no legítimo interesse; o operador deverá realizar o tratamento segundo as instruções fornecidas pelo controlador, que verificará a observância das instruções e das normas sobre a matéria.",
 "O registro das operações de tratamento de dados pessoais é obrigação exclusiva do operador, e o controlador está dispensado de verificar a observância de suas instruções, que o operador pode adaptar segundo seu próprio juízo.",
 "Arts. 37 e 39.","atribui só ao operador","g11a")
P("G11",["38"],"conceito_correto","excecao_omitida",3,
 "A autoridade nacional poderá determinar ao controlador que elabore relatório de impacto à proteção de dados pessoais, inclusive de dados sensíveis, que deverá conter, no mínimo, a descrição dos tipos de dados coletados, a metodologia utilizada para a coleta e para a garantia da segurança das informações e a análise do controlador sobre as medidas, salvaguardas e mecanismos de mitigação de risco adotados.",
 "A elaboração de relatório de impacto à proteção de dados pessoais é obrigatória em todo tratamento, e dele deverá constar apenas a descrição dos tipos de dados coletados, sendo vedada a abordagem de dados sensíveis.",
 "Art. 38 e parágrafo único.","generaliza e restringe conteúdo","g11b")
P("G11",["41"],"conceito_correto","excecao_omitida",3,
 "O controlador deverá indicar encarregado pelo tratamento de dados pessoais, cuja identidade e informações de contato deverão ser divulgadas publicamente, de forma clara e objetiva, preferencialmente no sítio eletrônico do controlador.",
 "O operador deverá indicar encarregado pelo tratamento de dados pessoais, cuja identidade e informações de contato deverão ser mantidas em sigilo para preservar a segurança do profissional.",
 "Art. 41, caput e § 1.º.","troca quem indica e publicidade","g11c")
P("G11",["41"],"conceito_correto","excecao_omitida",3,
 "As atividades do encarregado consistem em aceitar reclamações e comunicações dos titulares, prestar esclarecimentos e adotar providências, receber comunicações da autoridade nacional e adotar providências, orientar funcionários e contratados quanto às práticas de proteção de dados pessoais e executar as demais atribuições determinadas pelo controlador ou estabelecidas em normas complementares.",
 "As atividades do encarregado consistem em aplicar sanções aos agentes de tratamento que descumprirem a lei, representar a autoridade nacional perante os titulares e fiscalizar a atuação do operador, vedada a orientação de funcionários.",
 "Art. 41, § 2.º, I a IV.","atribui poder sancionatório","g11d")
P("G11",["41"],"conceito_correto","troca_autoridade",4,
 "A autoridade nacional poderá estabelecer normas complementares sobre a definição e as atribuições do encarregado, inclusive hipóteses de dispensa da necessidade de sua indicação, conforme a natureza e o porte da entidade ou o volume de operações de tratamento de dados.",
 "A indicação do encarregado é obrigatória para todos os agentes de tratamento, não podendo a autoridade nacional estabelecer hipóteses de dispensa em razão da natureza, do porte da entidade ou do volume de operações.",
 "Art. 41, § 3.º.","impede dispensa","g11e")
P("G11",["42"],"conceito_correto","troca_efeito",3,
 "O controlador ou o operador que, em razão do exercício de atividade de tratamento de dados pessoais, causar a outrem dano patrimonial, moral, individual ou coletivo, em violação à legislação de proteção de dados pessoais, é obrigado a repará-lo.",
 "Somente o controlador responde pelo dano patrimonial causado em razão do tratamento de dados pessoais, ficando afastada a reparação de dano moral e de dano coletivo, que dependem de legislação específica.",
 "Art. 42, caput.","limita responsabilidade","g11f")
P("G11",["42"],"conceito_correto","troca_efeito",4,
 "O operador responde solidariamente pelos danos causados pelo tratamento quando descumprir as obrigações da legislação de proteção de dados ou quando não tiver seguido as instruções lícitas do controlador, equiparando-se ao controlador, e os controladores diretamente envolvidos no tratamento do qual decorreram danos respondem solidariamente.",
 "O operador responde subsidiariamente pelos danos causados pelo tratamento, apenas após a excussão dos bens do controlador, e os controladores envolvidos no tratamento respondem na proporção de sua participação, vedada a solidariedade.",
 "Art. 42, § 1.º, I e II.","troca solidariedade","g11g")
P("G11",["42"],"conceito_correto","excecao_omitida",3,
 "O juiz, no processo civil, poderá inverter o ônus da prova a favor do titular dos dados quando, a seu juízo, for verossímil a alegação, houver hipossuficiência para fins de produção de prova ou quando a produção de prova pelo titular resultar-lhe excessivamente onerosa; e quem reparar o dano ao titular tem direito de regresso contra os demais responsáveis, na medida de sua participação.",
 "O ônus da prova nas ações de reparação por danos decorrentes do tratamento de dados pessoais recai sempre sobre o titular, vedada a inversão, e quem reparar o dano não tem direito de regresso contra os demais responsáveis.",
 "Art. 42, §§ 2.º e 4.º.","veda inversão e regresso","g11h")
P("G11",["43"],"conceito_correto","troca_efeito",3,
 "Os agentes de tratamento só não serão responsabilizados quando provarem que não realizaram o tratamento que lhes é atribuído, que, embora o tenham realizado, não houve violação à legislação de proteção de dados, ou que o dano é decorrente de culpa exclusiva do titular dos dados ou de terceiro.",
 "Os agentes de tratamento não serão responsabilizados quando provarem que o dano decorreu de caso fortuito ou força maior ou de culpa concorrente do titular dos dados ou de terceiro, ainda que tenha havido violação à legislação de proteção de dados.",
 "Art. 43, I a III.","altera excludentes","g11i")
P("G11",["44","45"],"conceito_correto","troca_efeito",4,
 "O tratamento de dados pessoais será irregular quando deixar de observar a legislação ou quando não fornecer a segurança que o titular dele pode esperar, consideradas as circunstâncias relevantes; as hipóteses de violação do direito do titular nas relações de consumo permanecem sujeitas às regras de responsabilidade da legislação pertinente.",
 "O tratamento de dados pessoais será irregular somente quando houver violação expressa da legislação, sendo irrelevante a segurança que o titular dele pode esperar, e as violações nas relações de consumo passam a se submeter exclusivamente às regras de responsabilidade da LGPD.",
 "Arts. 44 e 45.","afasta legislação de consumo","g11j")
# ---- G12
P("G12",["46"],"conceito_correto","excecao_omitida",3,
 "Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas, observadas desde a fase de concepção do produto ou do serviço até a sua execução, e a autoridade nacional poderá dispor sobre padrões técnicos mínimos.",
 "Os agentes de tratamento devem adotar medidas de segurança somente a partir da fase de execução do produto ou do serviço, e a autoridade nacional não poderá dispor sobre padrões técnicos mínimos para tornar aplicável essa obrigação.",
 "Art. 46, caput e §§ 1.º e 2.º (privacy by design).","limita à execução","g12a")
P("G12",["47","49"],"conceito_correto","troca_efeito",3,
 "Os agentes de tratamento ou qualquer outra pessoa que intervenha em uma das fases do tratamento obrigam-se a garantir a segurança da informação em relação aos dados pessoais, mesmo após o seu término; e os sistemas utilizados devem ser estruturados de forma a atender aos requisitos de segurança, aos padrões de boas práticas e de governança e aos princípios gerais da lei.",
 "A obrigação de garantir a segurança da informação em relação aos dados pessoais cessa com o término do tratamento, e os sistemas utilizados dispensam requisitos de governança desde que o controlador tenha obtido o consentimento do titular.",
 "Arts. 47 e 49.","encerra o dever com o término","g12b")
P("G12",["48"],"conceito_correto","troca_autoridade",3,
 "O controlador deverá comunicar à autoridade nacional e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante aos titulares, em prazo razoável, conforme definido pela autoridade nacional.",
 "O controlador deverá comunicar somente ao titular a ocorrência de incidente de segurança, no prazo de setenta e duas horas, fixado em lei, ficando a comunicação à autoridade nacional dependente de requisição desta.",
 "Art. 48, caput e § 1.º: prazo razoável, conforme definido pela ANPD.","fixa prazo e dispensa comunicação à ANPD","g12c")
P("G12",["48"],"conceito_correto","excecao_omitida",4,
 "A comunicação do incidente deverá mencionar, no mínimo, a descrição da natureza dos dados afetados, as informações sobre os titulares envolvidos, as medidas técnicas e de segurança utilizadas, os riscos relacionados ao incidente, os motivos da demora, no caso de comunicação não imediata, e as medidas adotadas ou que serão adotadas para reverter ou mitigar os efeitos do prejuízo.",
 "A comunicação do incidente deverá mencionar apenas a data do incidente e o número de titulares afetados, ficando dispensada a indicação das medidas técnicas utilizadas e dos riscos relacionados.",
 "Art. 48, § 1.º, I a VI.","reduz conteúdo","g12d")
P("G12",["48"],"conceito_correto","excecao_omitida",4,
 "Verificada a gravidade do incidente, a autoridade nacional poderá determinar ao controlador a adoção de providências, como a ampla divulgação do fato em meios de comunicação e medidas para reverter ou mitigar os efeitos do incidente, avaliando, no juízo de gravidade, a eventual comprovação de que foram adotadas medidas técnicas que tornem os dados ininteligíveis a terceiros não autorizados.",
 "A autoridade nacional não poderá determinar a divulgação do incidente em meios de comunicação, e a adoção de medidas que tornem os dados ininteligíveis para terceiros é irrelevante para o juízo de gravidade.",
 "Art. 48, §§ 2.º e 3.º.","afasta providências","g12e")
P("G12",["50"],"conceito_correto","troca_efeito",3,
 "Os controladores e operadores, no âmbito de suas competências, individualmente ou por meio de associações, poderão formular regras de boas práticas e de governança, que deverão ser publicadas e atualizadas periodicamente e poderão ser reconhecidas e divulgadas pela autoridade nacional.",
 "Somente a autoridade nacional poderá formular regras de boas práticas e de governança, que serão de observância obrigatória pelos controladores e operadores, vedada a formulação por meio de associações.",
 "Art. 50, caput e § 3.º.","atribui só à ANPD","g12f")
P("G12",["50"],"conceito_correto","excecao_omitida",4,
 "O controlador poderá implementar programa de governança em privacidade que, no mínimo, demonstre o comprometimento em adotar processos e políticas internas, seja aplicável a todo o conjunto de dados sob seu controle, seja adaptado à estrutura, escala e volume das operações, estabeleça salvaguardas com base em avaliação sistemática de impactos e riscos, conte com planos de resposta a incidentes e seja atualizado constantemente.",
 "O programa de governança em privacidade é obrigatório para todo controlador, deve aplicar-se apenas aos dados coletados por meio digital, independe da escala das operações e dispensa planos de resposta a incidentes.",
 "Art. 50, § 2.º, I, a a h.","torna obrigatório e restringe","g12g")
P("G12",["51"],"conceito_correto","troca_autoridade",2,
 "A autoridade nacional estimulará a adoção de padrões técnicos que facilitem o controle pelos titulares dos seus dados pessoais.",
 "A autoridade nacional imporá a adoção de padrões técnicos únicos, que dispensam o controle pelos titulares sobre seus dados pessoais.",
 "Art. 51.","impõe padrão único","g12h")
# ---- G13
P("G13",["52"],"conceito_correto","troca_numero",3,
 "A multa simples aplicável pela autoridade nacional é de até 2% do faturamento da pessoa jurídica de direito privado, grupo ou conglomerado no Brasil no seu último exercício, excluídos os tributos, limitada, no total, a R$ 50.000.000,00 por infração.",
 "A multa simples aplicável pela autoridade nacional é de até 5% do faturamento da pessoa jurídica de direito privado, grupo ou conglomerado no Brasil no seu último exercício, incluídos os tributos, limitada, no total, a R$ 100.000.000,00 por infração.",
 "Art. 52, II.","troca percentual e limite","g13a")
P("G13",["52"],"conceito_correto","excecao_omitida",3,
 "Entre as sanções administrativas aplicáveis pela autoridade nacional estão a advertência, com indicação de prazo para adoção de medidas corretivas, a multa simples, a multa diária, a publicização da infração após apurada e confirmada, o bloqueio e a eliminação dos dados pessoais a que se refere a infração.",
 "Entre as sanções administrativas aplicáveis pela autoridade nacional estão a prisão administrativa do responsável, a cassação do registro da empresa, o bloqueio das contas da pessoa jurídica e a publicização da infração independentemente de apuração definitiva.",
 "Art. 52, I a VI.","inclui sanções inexistentes","g13b")
P("G13",["52"],"conceito_correto","troca_numero",4,
 "A suspensão parcial do funcionamento do banco de dados a que se refere a infração e a suspensão do exercício da atividade de tratamento são aplicáveis pelo período máximo de seis meses, prorrogável por igual período, e a proibição parcial ou total do exercício de atividades relacionadas a tratamento de dados também está entre as sanções previstas.",
 "A suspensão parcial do funcionamento do banco de dados a que se refere a infração e a suspensão do exercício da atividade de tratamento são aplicáveis pelo período máximo de doze meses, improrrogável, e a proibição do exercício de atividades relacionadas a tratamento de dados somente pode ser determinada pelo Poder Judiciário.",
 "Art. 52, X a XII.","troca prazo e autoridade","g13c")
P("G13",["52"],"conceito_correto","excecao_omitida",4,
 "As sanções serão aplicadas após procedimento administrativo que possibilite a ampla defesa, de forma gradativa, isolada ou cumulativa, de acordo com as peculiaridades do caso concreto, considerados, entre outros, a gravidade e a natureza das infrações, a boa-fé do infrator, a vantagem auferida, a condição econômica, a reincidência, o grau do dano, a cooperação e a pronta adoção de medidas corretivas.",
 "As sanções serão aplicadas de ofício, independentemente de procedimento administrativo, de forma cumulativa e uniforme para todos os infratores, sendo irrelevantes a boa-fé do infrator, a reincidência e a cooperação.",
 "Art. 52, § 1.º, I a XI.","dispensa procedimento e critérios","g13d")
P("G13",["52"],"conceito_correto","troca_efeito",4,
 "As sanções de advertência, publicização da infração, bloqueio, eliminação, suspensão parcial do banco de dados, suspensão da atividade de tratamento e proibição parcial ou total do exercício de atividades poderão ser aplicadas às entidades e aos órgãos públicos, sem prejuízo da Lei n.º 8.112/1990, da Lei n.º 8.429/1992 e da Lei n.º 12.527/2011; as multas simples e diária não se aplicam ao poder público.",
 "Todas as sanções administrativas da lei, inclusive a multa simples e a multa diária, poderão ser aplicadas às entidades e aos órgãos públicos, que ficam, por esse motivo, isentos da responsabilização prevista na Lei n.º 8.112/1990 e na Lei de Improbidade Administrativa.",
 "Art. 52, § 3.º: aplicáveis os incisos I, IV, V, VI, X, XI e XII.","aplica multa ao poder público","g13e")
P("G13",["52"],"conceito_correto","troca_efeito",4,
 "As sanções de suspensão do banco de dados, suspensão da atividade de tratamento e proibição de atividades somente serão aplicadas após já ter sido imposta ao menos uma das sanções de multa simples, multa diária, publicização, bloqueio ou eliminação para o mesmo caso concreto.",
 "As sanções de suspensão do banco de dados, suspensão da atividade de tratamento e proibição de atividades poderão ser aplicadas isoladamente e de imediato, ainda que não tenha sido imposta nenhuma outra sanção para o caso.",
 "Art. 52, § 6.º, I.","dispensa sanção prévia","g13f")
P("G13",["52"],"conceito_correto","excecao_omitida",3,
 "O produto da arrecadação das multas aplicadas pela ANPD será destinado ao Fundo de Defesa de Direitos Difusos, e os vazamentos individuais ou acessos não autorizados poderão ser objeto de conciliação direta entre controlador e titular, sujeitando-se o controlador, caso não haja acordo, às penalidades da lei.",
 "O produto da arrecadação das multas aplicadas pela ANPD constitui receita própria da autoridade, e os vazamentos individuais ou acessos não autorizados não admitem conciliação direta entre controlador e titular.",
 "Art. 52, §§ 5.º e 7.º.","troca destinação","g13g")
P("G13",["53","54"],"conceito_correto","troca_autoridade",4,
 "A autoridade nacional definirá, por meio de regulamento próprio sobre sanções administrativas, que deverá ser objeto de consulta pública, as metodologias que orientarão o cálculo do valor-base das sanções de multa; o valor da multa diária deve observar a gravidade da falta e a extensão do dano e ser fundamentado.",
 "A metodologia de cálculo do valor-base das multas será definida pelo controlador em cada processo, dispensada a publicação prévia, e o valor da multa diária independe da gravidade da falta, devendo ser fixo.",
 "Arts. 53 e 54.","dispensa publicação","g13h")
# ---- G14
P("G14",["55A"],"conceito_correto","confusao_instituto",3,
 "A Autoridade Nacional de Proteção de Dados (ANPD) é autarquia de natureza especial, dotada de autonomia técnica e decisória, com patrimônio próprio e com sede e foro no Distrito Federal.",
 "A Autoridade Nacional de Proteção de Dados (ANPD) é órgão da administração direta, integrante da estrutura da Casa Civil da Presidência da República, subordinado hierarquicamente ao Ministro de Estado, com sede e foro no Distrito Federal.",
 "Art. 55-A (natureza jurídica de autarquia especial, conforme a Lei 14.460/2022).","mantém natureza de órgão","g14a")
P("G14",["55C"],"conceito_correto","excecao_omitida",3,
 "A ANPD é composta pelo Conselho Diretor, órgão máximo de direção, pelo Conselho Nacional de Proteção de Dados Pessoais e da Privacidade, pela Corregedoria, pela Ouvidoria, pela Procuradoria e pelas unidades administrativas e especializadas necessárias à aplicação da lei.",
 "A ANPD é composta apenas pelo Conselho Diretor e pelo Conselho Nacional de Proteção de Dados Pessoais e da Privacidade, sendo vedada a criação de Corregedoria, Ouvidoria ou Procuradoria próprias.",
 "Art. 55-C.","reduz estrutura","g14b")
P("G14",["55D"],"conceito_correto","troca_numero",3,
 "O Conselho Diretor da ANPD será composto de cinco diretores, incluído o Diretor-Presidente, escolhidos pelo Presidente da República e por ele nomeados, após aprovação pelo Senado Federal, com mandato de quatro anos.",
 "O Conselho Diretor da ANPD será composto de sete diretores, incluído o Diretor-Presidente, escolhidos e nomeados pelo Presidente da República, dispensada a aprovação do Senado Federal, com mandato de cinco anos.",
 "Art. 55-D, caput e §§ 1.º e 3.º.","troca número, aprovação e mandato","g14c")
P("G14",["55D"],"conceito_correto","excecao_omitida",4,
 "Os mandatos dos primeiros membros do Conselho Diretor nomeados foram de dois, três, quatro, cinco e seis anos, conforme estabelecido no ato de nomeação, e, na hipótese de vacância do cargo no curso do mandato, o prazo remanescente será completado pelo sucessor.",
 "Os mandatos dos primeiros membros do Conselho Diretor nomeados foram todos de quatro anos, e, na hipótese de vacância do cargo no curso do mandato, o sucessor cumprirá novo mandato integral de quatro anos.",
 "Art. 55-D, §§ 4.º e 5.º.","uniformiza mandatos","g14d")
P("G14",["55E"],"conceito_correto","troca_autoridade",4,
 "Os membros do Conselho Diretor somente perderão seus cargos em virtude de renúncia, condenação judicial transitada em julgado ou pena de demissão decorrente de processo administrativo disciplinar, instaurado pelo Ministro de Estado Chefe da Casa Civil e julgado pelo Presidente da República.",
 "Os membros do Conselho Diretor poderão ser exonerados ad nutum pelo Presidente da República a qualquer tempo, e o processo administrativo disciplinar será instaurado e julgado pela própria ANPD.",
 "Art. 55-E, caput e §§ 1.º e 2.º.","admite exoneração livre","g14e")
P("G14",["55J"],"conceito_correto","excecao_omitida",3,
 "Compete à ANPD, entre outras atribuições, zelar pela proteção dos dados pessoais, elaborar diretrizes para a Política Nacional de Proteção de Dados Pessoais e da Privacidade, fiscalizar e aplicar sanções mediante processo administrativo que assegure o contraditório, a ampla defesa e o direito de recurso, e apreciar petições de titular contra controlador após comprovada a apresentação de reclamação ao controlador não solucionada.",
 "Compete à ANPD, entre outras atribuições, julgar ações de reparação de danos movidas por titulares contra controladores, aplicar sanções independentemente de processo administrativo e apreciar petições de titular sem exigir reclamação prévia ao controlador.",
 "Art. 55-J, I, III, IV e V.","atribui competência jurisdicional","g14f")
P("G14",["55J"],"conceito_correto","excecao_omitida",4,
 "Compete também à ANPD editar normas simplificadas e diferenciadas para microempresas, empresas de pequeno porte e startups, deliberar, na esfera administrativa, em caráter terminativo, sobre a interpretação da lei e os casos omissos, celebrar compromisso com agentes de tratamento para eliminar irregularidade e realizar ou determinar auditorias.",
 "Compete à ANPD aplicar as mesmas regras e prazos a todos os agentes de tratamento, vedadas normas diferenciadas para microempresas e startups, e suas deliberações sobre a interpretação da lei estão sujeitas a homologação do Ministério da Justiça.",
 "Art. 55-J, XVI, XVII, XVIII e XX.","veda normas diferenciadas","g14g")
P("G14",["55J"],"conceito_correto","excecao_omitida",4,
 "Ao impor condicionantes administrativas ao tratamento de dados por agente privado, a ANPD deve observar a exigência de mínima intervenção; seus regulamentos e normas devem ser precedidos de consulta e audiência públicas e de análises de impacto regulatório.",
 "Ao impor condicionantes administrativas ao tratamento de dados por agente privado, a ANPD deve adotar a máxima intervenção possível, e seus regulamentos dispensam consulta e audiência públicas.",
 "Art. 55-J, §§ 1.º e 2.º.","inverte mínima intervenção","g14h")
P("G14",["55K"],"conceito_correto","troca_autoridade",4,
 "A aplicação das sanções previstas na LGPD compete exclusivamente à ANPD, cujas competências prevalecerão, no que se refere à proteção de dados pessoais, sobre as competências correlatas de outras entidades ou órgãos da administração pública, e a ANPD será o órgão central de interpretação da lei.",
 "A aplicação das sanções previstas na LGPD compete concorrentemente à ANPD e aos órgãos de defesa do consumidor, prevalecendo, em caso de conflito, a competência do órgão que primeiro instaurar o procedimento.",
 "Art. 55-K e parágrafo único.","atribui competência concorrente","g14i")
# ---- G15
P("G15",["7","8","18"],"caso_concreto","caso_concreto",4,
 "Aplicativo de entregas coletou dados de cliente com base em consentimento fornecido em cláusula genérica dos termos de uso, para finalidades não especificadas. Posteriormente, o cliente revogou o consentimento. Nesse caso, a autorização genérica é nula, e, caso fosse válido o consentimento, a revogação seria possível a qualquer momento, por procedimento gratuito e facilitado, ratificados os tratamentos anteriores enquanto não houvesse requerimento de eliminação.",
 "Aplicativo de entregas coletou dados de cliente com base em consentimento fornecido em cláusula genérica dos termos de uso, para finalidades não especificadas. Posteriormente, o cliente revogou o consentimento. Nesse caso, a autorização genérica é válida, e a revogação só produz efeitos mediante pagamento do custo de eliminação e invalida os tratamentos anteriores.",
 "Art. 8.º, §§ 1.º, 4.º e 5.º.","valida autorização genérica","g15a")
P("G15",["14"],"caso_concreto","caso_concreto",4,
 "Plataforma de jogos on-line voltada a crianças exigiu o preenchimento de endereço residencial completo para liberar o acesso. A exigência contraria a LGPD, que veda condicionar a participação de crianças em jogos ao fornecimento de informações pessoais além das estritamente necessárias, e o tratamento depende de consentimento específico e em destaque de pelo menos um dos pais.",
 "Plataforma de jogos on-line voltada a crianças exigiu o preenchimento de endereço residencial completo para liberar o acesso. A exigência é compatível com a LGPD, que autoriza condicionar a participação ao fornecimento de qualquer informação pessoal, bastando o consentimento do próprio usuário menor.",
 "Art. 14, §§ 1.º e 4.º.","autoriza condicionamento","g15b")
P("G15",["42","43"],"caso_concreto","caso_concreto",5,
 "Empresa contratou operador para tratar dados de clientes. O operador, descumprindo instruções lícitas do controlador, divulgou os dados e causou dano a titulares. Nessa hipótese, o operador responde solidariamente pelos danos e equipara-se ao controlador, salvo se provar alguma das excludentes do art. 43, e quem reparar o dano tem direito de regresso na medida da participação de cada um.",
 "Empresa contratou operador para tratar dados de clientes. O operador, descumprindo instruções lícitas do controlador, divulgou os dados e causou dano a titulares. Nessa hipótese, somente o controlador responde perante os titulares, cabendo ao operador responder apenas regressivamente, sem que se lhe aplique excludente algum.",
 "Art. 42, §§ 1.º, I, e 4.º, e art. 43.","afasta responsabilidade do operador","g15c")
P("G15",["48","52"],"caso_concreto","caso_concreto",5,
 "Empresa privada sofreu incidente de segurança com vazamento de dados sensíveis de milhares de titulares e não comunicou a ANPD nem os titulares. Em tese, a empresa poderá sofrer sanções administrativas, após procedimento com ampla defesa, como advertência, multa de até 2% do faturamento no Brasil limitada a R$ 50 milhões por infração e, após aplicada outra sanção, a suspensão do banco de dados.",
 "Empresa privada sofreu incidente de segurança com vazamento de dados sensíveis de milhares de titulares e não comunicou a ANPD nem os titulares. A empresa só poderá ser sancionada se houver decisão judicial, sendo vedada à ANPD a aplicação de multa e a determinação de divulgação do incidente.",
 "Art. 48 e art. 52, II, X e §§ 1.º e 6.º.","exige decisão judicial","g15d")
P("G15",["23","26","27"],"caso_concreto","caso_concreto",5,
 "Ministério federal pretende transferir a uma empresa privada, por contrato de execução descentralizada de atividade pública, dados pessoais de beneficiários de programa social, exclusivamente para essa finalidade. A transferência é admitida pela LGPD em hipótese de exceção, e o contrato deve ser comunicado à autoridade nacional.",
 "Ministério federal pretende transferir a uma empresa privada, por contrato de execução descentralizada de atividade pública, dados pessoais de beneficiários de programa social, que a empresa poderá usar também para fins comerciais próprios. A transferência é admitida pela LGPD, dispensada a comunicação à autoridade nacional.",
 "Art. 26, § 1.º, I, e § 2.º.","admite uso para outras finalidades","g15e")
