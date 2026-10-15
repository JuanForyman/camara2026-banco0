# Lei 9.784/99 — complemento: art. 69-A (Lei 12.008/2009) e art. 69
Q = []
TAILS=[" Essa disciplina consta da Lei do Processo Administrativo no âmbito da Administração Pública Federal.",
 " Trata-se de regra aplicável aos procedimentos administrativos regidos pela Lei n.º 9.784/1999."]
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 50: E += TAILS[len(Q)%2]
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, {}))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, {}))
P("P24",["69A"],"conceito_correto","troca_numero",3,
 "Terão prioridade na tramitação, em qualquer órgão ou instância, os procedimentos administrativos em que figure como parte ou interessado pessoa com idade igual ou superior a 60 anos ou pessoa portadora de deficiência, física ou mental.",
 "Terão prioridade na tramitação, apenas no órgão de origem, os procedimentos administrativos em que figure como parte ou interessado pessoa com idade igual ou superior a 65 anos ou pessoa portadora de deficiência física.",
 "Art. 69-A, caput, I e II.","troca idade, abrangência e restringe deficiência","e1")
P("P24",["69A"],"conceito_correto","excecao_omitida",3,
 "A prioridade na tramitação alcança também a pessoa portadora de doença grave, com base em conclusão da medicina especializada, mesmo que a doença tenha sido contraída após o início do processo.",
 "A prioridade na tramitação alcança a pessoa portadora de doença grave, com base em conclusão da medicina especializada, desde que a doença tenha sido contraída antes do início do processo.",
 "Art. 69-A, IV.","exige doença anterior ao processo","e2")
P("P24",["69A"],"conceito_correto","troca_autoridade",3,
 "A pessoa interessada na obtenção do benefício da prioridade, juntando prova de sua condição, deverá requerê-lo à autoridade administrativa competente, que determinará as providências a serem cumpridas.",
 "A prioridade na tramitação será concedida de ofício pela autoridade administrativa, independentemente de requerimento ou de prova da condição do interessado, que será presumida.",
 "Art. 69-A, § 1º.","dispensa requerimento e prova","e3")
P("P24",["69A"],"conceito_correto","troca_efeito",2,
 "Deferida a prioridade, os autos receberão identificação própria que evidencie o regime de tramitação prioritária.",
 "Deferida a prioridade, os autos serão apartados e remetidos a unidade especializada, sem identificação própria, para impedir a exposição da condição do interessado.",
 "Art. 69-A, § 2º.","troca efeito do deferimento","e4")
P("P24",["69"],"conceito_correto","confusao_instituto",3,
 "Os processos administrativos específicos continuarão a reger-se por lei própria, aplicando-se-lhes apenas subsidiariamente os preceitos da Lei n.º 9.784/1999.",
 "Os processos administrativos específicos passam a reger-se integralmente pela Lei n.º 9.784/1999, que revoga as leis próprias naquilo em que forem com ela incompatíveis, sendo estas aplicadas apenas subsidiariamente.",
 "Art. 69.","inverte subsidiariedade","e5")
P("P24",["69A"],"caso_concreto","caso_concreto",4,
 "Servidor com 62 anos de idade, interessado em procedimento administrativo que tramita em órgão federal, juntou prova da sua condição e requereu prioridade de tramitação à autoridade competente. Nessa hipótese, deferida a prioridade, os autos receberão identificação própria que evidencie o regime prioritário.",
 "Servidor com 62 anos de idade, interessado em procedimento administrativo que tramita em órgão federal, deixou de juntar prova da sua condição, mas requereu prioridade de tramitação à autoridade competente. Nessa hipótese, a prioridade será deferida de plano, e os autos receberão identificação própria que evidencie o regime prioritário.",
 "Art. 69-A, I e §§ 1º e 2º.","dispensa prova","e6")
