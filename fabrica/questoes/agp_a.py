# Agentes públicos — lote L12
Q = []
TAILS=[" Essa seria a orientação adotada pela doutrina e pela jurisprudência no direito brasileiro.",
 " Trata-se de entendimento aplicável à responsabilidade civil das pessoas jurídicas de direito público no Brasil.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática constitucional da responsabilidade do Estado.",
 " Essa seria a regra para os danos causados a terceiros no exercício da função pública."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
FD={"tipo":"doutrina_jurisprudencia","ref":"doutrina majoritária; CF arts. 37 a 41","versao":"conhecimento do autor","conferida":"conhecimento"}
FJ={"tipo":"jurisprudencia","ref":"Teses de repercussão geral do STF (tesesesumulas.com.br, 2026-10-16)","versao":"conhecimento verificado em fonte secundária","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, jur=False, lei=False):
    ex = {}
    if lei: ex["fonte"]={"tipo":"lei","ref":"CF arts. 37, 38 e 41","versao":"vigente","conferida":"conhecimento"}
    elif jur: ex["fonte"]=FJ; ex["risco"]=["jurisprudencia_conhecimento"]
    else: ex["fonte"]=FD; ex["risco"]=["doutrina_conhecimento"]
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# S01
P("S01",["1"],"conceito_correto","troca_numero",2,
 "O prazo de validade do concurso público será de até dois anos, prorrogável uma vez, por igual período.",
 "O prazo de validade do concurso público será de até dois anos, prorrogável por tantas vezes quantas forem necessárias, por igual período.",
 "CF, art. 37, III.","admite prorrogações ilimitadas","s01a",lei=True)
P("S01",["1"],"conceito_correto","troca_efeito",3,
 "Durante o prazo improrrogável previsto no edital de convocação, o aprovado em concurso público será convocado com prioridade sobre novos concursados para assumir cargo ou emprego, na carreira.",
 "Durante o prazo improrrogável previsto no edital de convocação, o aprovado em concurso público será convocado com a mesma prioridade dos novos concursados para assumir cargo ou emprego, na carreira.",
 "CF, art. 37, IV.","equipara aprovados e novos concursados","s01b",lei=True)
P("S01",["1"],"conceito_correto","excecao_omitida",3,
 "A investidura em cargo ou emprego público depende de aprovação prévia em concurso público, ressalvadas as nomeações para cargo em comissão declarado em lei de livre nomeação e exoneração.",
 "A investidura em cargo ou emprego público depende de aprovação prévia em concurso público, sem nenhuma ressalva, inclusive para os cargos em comissão e as funções de confiança.",
 "CF, art. 37, II.","omite ressalva dos cargos em comissão","s01c",lei=True)
P("S01",["1"],"conceito_correto","excecao_omitida",3,
 "Os cargos, empregos e funções públicas são acessíveis aos brasileiros que preencham os requisitos estabelecidos em lei, assim como aos estrangeiros, na forma da lei.",
 "Os cargos, empregos e funções públicas são acessíveis exclusivamente aos brasileiros natos, vedado o acesso de estrangeiros em qualquer hipótese.",
 "CF, art. 37, I.","exclui estrangeiros","s01d",lei=True)
P("S01",["2"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, o candidato aprovado dentro do número de vagas previsto no edital tem direito subjetivo à nomeação durante o prazo de validade do concurso, ressalvadas situações excepcionais, devidamente motivadas, de superveniência, imprevisibilidade e gravidade.",
 "Segundo o STF, o candidato aprovado dentro do número de vagas previsto no edital tem mera expectativa de direito à nomeação, cabendo à Administração decidir livremente sobre a convocação, sem necessidade de motivação.",
 "STF, RE 598.099 (Tema 161).","reduz a expectativa de direito","s01e",jur=True)
P("S01",["2"],"conceito_correto","troca_autoridade",4,
 "Segundo a Súmula Vinculante 44, só por lei se pode sujeitar a exame psicotécnico a habilitação de candidato a cargo público.",
 "Segundo a Súmula Vinculante 44, a exigência de exame psicotécnico para a habilitação de candidato a cargo público pode ser instituída por previsão exclusiva do edital do concurso.",
 "SV 44.","admite previsão apenas em edital","s01f",jur=True)
P("S01",["2"],"conceito_correto","excecao_omitida",4,
 "Segundo a Súmula 683 do STF, o limite de idade para a inscrição em concurso público só se legitima quando possa ser justificado pela natureza das atribuições do cargo a ser preenchido.",
 "Segundo a Súmula 683 do STF, o limite de idade para a inscrição em concurso público pode ser fixado livremente pela Administração, independentemente da natureza das atribuições do cargo.",
 "STF, Súmula 683.","admite limite livre de idade","s01g",jur=True)
P("S01",["2"],"conceito_correto","confusao_instituto",4,
 "A Súmula Vinculante 43 reputa inconstitucional toda modalidade de provimento que propicie ao servidor investir-se, sem prévia aprovação em concurso público destinado ao seu provimento, em cargo que não integra a carreira na qual anteriormente investido.",
 "A Súmula Vinculante 43 reputa constitucional a ascensão funcional, que permite ao servidor investir-se, sem concurso, em cargo de carreira diversa da sua, desde que tenha mais de cinco anos de serviço.",
 "SV 43.","valida ascensão","s01h",jur=True)
# S02
P("S02",["3"],"conceito_correto","confusao_instituto",3,
 "As funções de confiança são exercidas exclusivamente por servidores ocupantes de cargo efetivo, e os cargos em comissão devem ser preenchidos por servidores de carreira nos casos, condições e percentuais mínimos previstos em lei.",
 "Os cargos em comissão são exercidos exclusivamente por servidores ocupantes de cargo efetivo, ao passo que as funções de confiança podem ser ocupadas por pessoas sem vínculo efetivo, de livre escolha da autoridade.",
 "CF, art. 37, V.","inverte funções e cargos","s02a",lei=True)
P("S02",["3"],"conceito_correto","excecao_omitida",3,
 "As funções de confiança e os cargos em comissão destinam-se apenas às atribuições de direção, chefia e assessoramento.",
 "As funções de confiança e os cargos em comissão destinam-se a quaisquer atribuições, inclusive as de natureza técnica, burocrática ou operacional, a critério da autoridade nomeante.",
 "CF, art. 37, V.","amplia atribuições","s02b",lei=True)
P("S02",["3"],"conceito_correto","excecao_omitida",3,
 "A lei estabelecerá os casos de contratação por tempo determinado para atender a necessidade temporária de excepcional interesse público.",
 "A Administração poderá contratar por tempo determinado, independentemente de lei que estabeleça os casos, sempre que houver necessidade de pessoal, inclusive para atividades permanentes.",
 "CF, art. 37, IX.","dispensa lei","s02c",lei=True)
# S03
P("S03",["4"],"conceito_correto","excecao_omitida",3,
 "O direito de greve dos servidores públicos civis será exercido nos termos e nos limites definidos em lei específica, e, enquanto não editada, o STF determinou a aplicação, por analogia, da Lei 7.783/1989.",
 "O direito de greve dos servidores públicos civis é norma constitucional de eficácia plena e independe de lei, sendo vedado ao Judiciário determinar a aplicação, por analogia, da Lei 7.783/1989.",
 "CF, art. 37, VII; STF, MI 708.","nega necessidade de lei","s03a",jur=True)
P("S03",["4"],"conceito_correto","troca_efeito",5,
 "Segundo o STF, a Administração deve proceder ao desconto dos dias não trabalhados em razão de greve, permitida a compensação em caso de acordo, salvo se a greve tiver sido provocada por conduta ilícita do Poder Público.",
 "Segundo o STF, a Administração não pode proceder ao desconto dos dias não trabalhados em razão de greve, por se tratar de direito constitucional, ainda que a greve não tenha sido provocada por conduta ilícita do Poder Público.",
 "STF, RE 693.456 (Tema 531).","veda desconto","s03b",jur=True)
P("S03",["4"],"conceito_correto","excecao_omitida",3,
 "A Constituição garante ao servidor público civil o direito à livre associação sindical, e veda aos militares a sindicalização e a greve.",
 "A Constituição veda ao servidor público civil o direito à livre associação sindical, e garante aos militares a sindicalização e a greve.",
 "CF, art. 37, VI, e art. 142, § 3º, IV.","inverte direitos","s03c",lei=True)
P("S03",["4"],"conceito_correto","excecao_omitida",3,
 "A lei reservará percentual dos cargos e empregos públicos para as pessoas com deficiência e definirá os critérios de sua admissão.",
 "A Constituição fixa, diretamente, o percentual de vinte por cento dos cargos e empregos públicos para as pessoas com deficiência, dispensando a edição de lei.",
 "CF, art. 37, VIII.","fixa percentual constitucional","s03d",lei=True)
# S04
P("S04",["5"],"conceito_correto","excecao_omitida",3,
 "A remuneração e o subsídio dos servidores somente poderão ser fixados ou alterados por lei específica, assegurada revisão geral anual, sempre na mesma data e sem distinção de índices.",
 "A remuneração e o subsídio dos servidores poderão ser fixados ou alterados por decreto do chefe do Executivo, assegurada revisão geral anual, em datas e com índices distintos para cada categoria.",
 "CF, art. 37, X.","admite decreto e índices distintos","s04a",lei=True)
P("S04",["5"],"conceito_correto","troca_autoridade",4,
 "Nos Estados, o limite remuneratório no Poder Judiciário é o subsídio mensal dos Desembargadores do Tribunal de Justiça, limitado a noventa inteiros e vinte e cinco centésimos por cento do subsídio mensal dos Ministros do Supremo Tribunal Federal.",
 "Nos Estados, o limite remuneratório no Poder Judiciário é o subsídio mensal do Governador, limitado a noventa inteiros e vinte e cinco centésimos por cento do subsídio mensal dos Ministros do Supremo Tribunal Federal.",
 "CF, art. 37, XI.","troca limite do Judiciário","s04b",lei=True)
P("S04",["5"],"conceito_correto","excecao_omitida",5,
 "Segundo o STF, nos casos de acumulação de cargos constitucionalmente autorizada, o teto remuneratório incide sobre a remuneração de cada vínculo isoladamente, e não sobre o somatório.",
 "Segundo o STF, nos casos de acumulação de cargos constitucionalmente autorizada, o teto remuneratório incide sobre o somatório das remunerações percebidas nos dois vínculos.",
 "STF, RE 612.975 e RE 602.043.","aplica teto ao somatório","s04c",jur=True)
P("S04",["5"],"conceito_correto","confusao_instituto",3,
 "É vedada a vinculação ou equiparação de quaisquer espécies remuneratórias para o efeito de remuneração de pessoal do serviço público, e os acréscimos pecuniários não serão computados nem acumulados para fins de concessão de acréscimos ulteriores.",
 "É permitida a vinculação de espécies remuneratórias entre cargos de mesmo nível dos diferentes Poderes, e os acréscimos pecuniários serão computados cumulativamente para fins de concessão de acréscimos ulteriores.",
 "CF, art. 37, XIII e XIV.","admite vinculação e efeito cascata","s04d",lei=True)
P("S04",["5"],"conceito_correto","excecao_omitida",4,
 "Nos termos da Súmula Vinculante 37, não cabe ao Poder Judiciário, que não tem função legislativa, aumentar vencimentos de servidores públicos sob o fundamento de isonomia.",
 "Nos termos da Súmula Vinculante 37, cabe ao Poder Judiciário aumentar vencimentos de servidores públicos sob o fundamento de isonomia, quando a distinção entre cargos for injustificada.",
 "SV 37.","admite aumento judicial","s04e",jur=True)
P("S04",["6"],"conceito_correto","excecao_omitida",3,
 "É vedada a acumulação remunerada de cargos públicos, exceto, havendo compatibilidade de horários, a de dois cargos de professor, a de um cargo de professor com outro técnico ou científico e a de dois cargos ou empregos privativos de profissionais de saúde, com profissões regulamentadas.",
 "É vedada a acumulação remunerada de cargos públicos, exceto, havendo compatibilidade de horários, a de dois cargos de professor, a de um cargo de professor com outro de natureza administrativa e a de três cargos privativos de profissionais de saúde.",
 "CF, art. 37, XVI.","altera hipóteses","s04f",lei=True)
P("S04",["6"],"conceito_correto","excecao_omitida",4,
 "A proibição de acumular cargos estende-se a empregos e funções e abrange autarquias, fundações, empresas públicas, sociedades de economia mista, suas subsidiárias e as sociedades controladas, direta ou indiretamente, pelo poder público.",
 "A proibição de acumular cargos alcança apenas os cargos da Administração direta, não se estendendo a empregos e funções nem às entidades da Administração indireta.",
 "CF, art. 37, XVII.","restringe a vedação","s04g",lei=True)
P("S04",["6"],"conceito_correto","excecao_omitida",4,
 "É vedada a percepção simultânea de proventos de aposentadoria decorrentes do art. 40 da Constituição com a remuneração de cargo, emprego ou função pública, ressalvados os cargos acumuláveis, os cargos eletivos e os cargos em comissão declarados em lei de livre nomeação e exoneração.",
 "É permitida a percepção simultânea de proventos de aposentadoria decorrentes do art. 40 da Constituição com a remuneração de qualquer cargo, emprego ou função pública, sem nenhuma ressalva.",
 "CF, art. 37, § 10.","permite sem ressalva","s04h",lei=True)
# S05
P("S05",["7"],"conceito_correto","troca_autoridade",3,
 "O servidor da Administração direta, autárquica e fundacional investido no mandato de Prefeito será afastado do cargo, emprego ou função, sendo-lhe facultado optar pela sua remuneração.",
 "O servidor da Administração direta, autárquica e fundacional investido no mandato de Prefeito permanece no exercício do cargo, desde que haja compatibilidade de horários, percebendo as duas remunerações.",
 "CF, art. 38, II.","confunde com vereador","s05a",lei=True)
P("S05",["7"],"conceito_correto","excecao_omitida",4,
 "O servidor investido no mandato de Vereador, havendo compatibilidade de horários, perceberá as vantagens de seu cargo sem prejuízo da remuneração do cargo eletivo, e, não havendo compatibilidade, aplica-se a regra do Prefeito.",
 "O servidor investido no mandato de Vereador será sempre afastado de seu cargo, emprego ou função, sendo-lhe facultado optar pela remuneração, ainda que haja compatibilidade de horários.",
 "CF, art. 38, III.","ignora compatibilidade de horários","s05b",lei=True)
P("S05",["7"],"conceito_correto","excecao_omitida",4,
 "Em qualquer caso que exija o afastamento para o exercício de mandato eletivo, o tempo de serviço do servidor será contado para todos os efeitos legais, exceto para promoção por merecimento.",
 "Em qualquer caso que exija o afastamento para o exercício de mandato eletivo, o tempo de serviço do servidor será contado para todos os efeitos legais, inclusive para promoção por merecimento.",
 "CF, art. 38, IV.","omite exceção","s05c",lei=True)
P("S05",["8"],"conceito_correto","troca_numero",2,
 "São estáveis após três anos de efetivo exercício os servidores nomeados para cargo de provimento efetivo em virtude de concurso público.",
 "São estáveis após dois anos de efetivo exercício os servidores nomeados para cargo de provimento efetivo ou em comissão, em virtude de concurso público.",
 "CF, art. 41, caput.","troca prazo e abrangência","s05d",lei=True)
P("S05",["8"],"conceito_correto","excecao_omitida",3,
 "O servidor público estável só perderá o cargo em virtude de sentença judicial transitada em julgado, mediante processo administrativo em que lhe seja assegurada ampla defesa, ou mediante procedimento de avaliação periódica de desempenho, na forma de lei complementar.",
 "O servidor público estável só perderá o cargo em virtude de sentença judicial transitada em julgado ou mediante procedimento de avaliação periódica de desempenho, na forma de lei ordinária, vedada a perda do cargo por processo administrativo.",
 "CF, art. 41, § 1º.","exclui processo administrativo","s05e",lei=True)
P("S05",["8"],"conceito_correto","excecao_omitida",4,
 "Extinto o cargo ou declarada a sua desnecessidade, o servidor estável ficará em disponibilidade, com remuneração proporcional ao tempo de serviço, até seu adequado aproveitamento em outro cargo.",
 "Extinto o cargo ou declarada a sua desnecessidade, o servidor estável será exonerado, com direito à indenização, sem direito a aproveitamento em outro cargo.",
 "CF, art. 41, § 3º.","troca disponibilidade por exoneração","s05f",lei=True)
P("S05",["8"],"conceito_correto","excecao_omitida",4,
 "Invalidada por sentença judicial a demissão do servidor estável, será ele reintegrado, e o eventual ocupante da vaga, se estável, reconduzido ao cargo de origem, sem direito a indenização, aproveitado em outro cargo ou posto em disponibilidade.",
 "Invalidada por sentença judicial a demissão do servidor estável, será ele reintegrado, e o eventual ocupante da vaga, se estável, será exonerado, com direito a indenização.",
 "CF, art. 41, § 2º.","troca destino do ocupante","s05g",lei=True)
P("S05",["8"],"conceito_correto","confusao_instituto",3,
 "Como condição para a aquisição da estabilidade, é obrigatória a avaliação especial de desempenho por comissão instituída para essa finalidade, e a estabilidade não alcança os ocupantes de cargo em comissão.",
 "Como condição para a aquisição da estabilidade, basta o decurso do prazo de efetivo exercício, dispensada a avaliação especial de desempenho, e a estabilidade alcança os ocupantes de cargo em comissão.",
 "CF, art. 41, § 4º.","dispensa avaliação e inclui comissão","s05h",lei=True)
# S06
P("S06",["9"],"conceito_correto","confusao_instituto",3,
 "Cargo público é o conjunto de atribuições e responsabilidades previstas na estrutura organizacional e cometidas a um servidor, ao passo que a função pública é a atribuição exercida sem a ocupação de cargo ou emprego, como as funções de confiança.",
 "Função pública é o conjunto de atribuições e responsabilidades previstas na estrutura organizacional e cometidas a um servidor, ao passo que o cargo público é a atribuição exercida sem a ocupação de emprego, como as funções de confiança.",
 "Lei 8.112/1990, art. 3º.","inverte cargo e função","s06a",lei=True)
P("S06",["9"],"conceito_correto","excecao_omitida",3,
 "O regime estatutário aplica-se aos ocupantes de cargo público, o regime celetista aos ocupantes de emprego público, e o regime especial ou temporário aos contratados por tempo determinado para necessidade temporária de excepcional interesse público.",
 "O regime celetista aplica-se aos ocupantes de cargo público, o regime estatutário aos ocupantes de emprego público, e o regime especial ou temporário aos ocupantes de cargo em comissão.",
 "Regimes de pessoal.","inverte regimes","s06b")
P("S06",["9"],"conceito_correto","excecao_omitida",4,
 "Os cargos vitalícios, como os dos magistrados, só podem ser perdidos por sentença judicial transitada em julgado, e a vitaliciedade dos magistrados de primeiro grau é adquirida, em regra, após dois anos de exercício.",
 "Os cargos vitalícios, como os dos magistrados, podem ser perdidos por decisão administrativa do tribunal a que o magistrado esteja vinculado, e a vitaliciedade é adquirida desde a posse.",
 "CF, art. 95, I.","admite perda por decisão administrativa","s06c",lei=True)
P("S06",["10"],"conceito_correto","excecao_omitida",3,
 "Considera-se agente público toda pessoa física que exerce função pública, ainda que transitoriamente ou sem remuneração, o que inclui os particulares em colaboração com o Poder Público.",
 "Considera-se agente público somente a pessoa física que ocupa cargo público remunerado, o que exclui os particulares em colaboração com o Poder Público.",
 "Lei 8.429/1992, art. 2º.","restringe agente a ocupante de cargo","s06d",lei=True)
P("S06",["10","11"],"conceito_correto","confusao_instituto",3,
 "Os jurados e os mesários requisitados exercem função pública sem serem servidores e enquadram-se, segundo a doutrina, na categoria dos particulares em colaboração com o Poder Público.",
 "Os jurados e os mesários requisitados são servidores públicos estatutários e enquadram-se, segundo a doutrina, na categoria dos agentes políticos.",
 "Particulares em colaboração.","classifica como servidores","s06e")
P("S06",["11"],"conceito_correto","excecao_omitida",3,
 "No caso de iminente perigo público, a autoridade competente poderá usar de propriedade particular, assegurada ao proprietário indenização ulterior, se houver dano.",
 "No caso de iminente perigo público, a autoridade competente poderá usar de propriedade particular, assegurada ao proprietário indenização prévia e em dinheiro, em qualquer hipótese.",
 "CF, art. 5º, XXV.","exige indenização prévia","s06f",lei=True)
