# Língua Inglesa — onda 1. Itens curtos em inglês; comentário em português (≤25 palavras).
Q = []
TAILS=[" This is the standard interpretation."," This reading is widely accepted."," This is the usual meaning in context."," This is the common usage."]
SHORT=[" This is correct."," This is the rule."," This is the usual use."]
def tail(E,C,i):
    gap=len(C)-len(E)
    if len(E) < 0.97*len(C) and gap > 60: return E+TAILS[i%len(TAILS)]
    if len(E) < 0.95*len(C) and gap > 8: return E+SHORT[i%len(SHORT)]
    return E
FG={"tipo":"gramatica","ref":"gramática da língua inglesa (Murphy; Swan; Oxford/Longman) e vocabulário geral","versao":"conhecimento do autor","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag):
    ex={"fonte":FG,"risco":["doutrina_conhecimento"]}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
_n=[0]
PT_={14:"EN01",15:"EN01",16:"EN04",1:"EN03",12:"EN03",13:"EN03",17:"EN03"}
def X(atom, padE, dif, C, E, com, terro):
    _n[0]+=1
    P(PT_.get(atom,"EN02"),[str(atom)],"conceito_correto",padE,dif,C,E,com,terro,f"e{_n[0]:03d}")
def J(atom, padE, dif, texto, C, E, com, terro):
    t="“"+texto+"” — "
    X(atom, padE, dif, t+C, t+E, com, terro)

# 1 falsos cognatos
X(1,"confusao_instituto",2,"In 'He pretended to be sick', 'pretended' means 'fingiu'.","In 'He pretended to be sick', 'pretended' means 'pretendeu'.","Pretend = fingir.","traduz pelo falso cognato")
X(1,"confusao_instituto",2,"In 'Actually, I disagree', 'actually' means 'na verdade'.","In 'Actually, I disagree', 'actually' means 'atualmente'.","Actually = na verdade.","traduz pelo falso cognato")
X(1,"confusao_instituto",1,"'Library' means 'biblioteca'.","'Library' means 'livraria'.","Library = biblioteca.","livraria")
X(1,"confusao_instituto",3,"In 'The bill was eventually approved', 'eventually' means 'por fim'.","In 'The bill was eventually approved', 'eventually' means 'eventualmente'.","Eventually = por fim.","traduz pelo falso cognato")
X(1,"confusao_instituto",3,"In 'I realized I was wrong', 'realized' means 'percebi'.","In 'I realized I was wrong', 'realized' means 'realizei'.","Realize = perceber.","traduz pelo falso cognato")
X(1,"confusao_instituto",2,"To 'attend a meeting' means to be present at it.","To 'attend a meeting' means to answer the phone during it.","Attend = comparecer.","traduz como 'atender'")
X(1,"confusao_instituto",2,"'Parents' means a person's mother and father.","'Parents' means a person's relatives in general.","Parents = pais.","parentes")
X(1,"confusao_instituto",3,"In 'Talks will resume on Monday', 'resume' means 'retomar', not 'resumir'.","In 'Talks will resume on Monday', 'resume' means 'resumir'.","Resume (verbo) = retomar.","traduz pelo falso cognato")
X(1,"confusao_instituto",3,"'Fabric' means 'tecido'.","'Fabric' means 'fábrica'.","Fabric = tecido; factory = fábrica.","fábrica")
# 2 conectores
X(2,"troca_efeito",2,"In 'The law was approved; however, it faced criticism', 'however' introduces a contrast.","In 'The law was approved; however, it faced criticism', 'however' introduces a result.","However = contraste.","troca contraste por resultado")
X(2,"troca_efeito",2,"'Although' introduces a concession, as in 'Although it rained, they went out'.","'Although' introduces a reason, as in 'Although it rained, they went out'.","Although = embora.","troca concessão por causa")
X(2,"troca_efeito",2,"In 'Despite the delay, the vote took place', 'despite' means 'apesar de'.","In 'Despite the delay, the vote took place', 'despite' means 'por causa de'.","Despite = apesar de.","troca concessão por causa")
X(2,"troca_efeito",2,"'Therefore' and 'thus' indicate a consequence.","'Therefore' and 'thus' indicate a contrast.","Therefore = portanto.","troca consequência por contraste")
X(2,"troca_efeito",3,"In 'Some voted yes, whereas others voted no', 'whereas' marks a contrast.","In 'Some voted yes, whereas others voted no', 'whereas' marks a condition.","Whereas = enquanto (contraste).","troca contraste por condição")
X(2,"troca_efeito",3,"'Unless' means 'a menos que' (if ... not).","'Unless' means 'porque'.","Unless = a menos que.","troca condição por causa")
X(2,"troca_efeito",3,"In 'Since he was late, he missed the vote', 'since' expresses reason.","In 'Since he was late, he missed the vote', 'since' expresses contrast.","Since (aqui) = já que.","troca causa por contraste")
X(2,"troca_efeito",2,"'Moreover' and 'furthermore' add information.","'Moreover' and 'furthermore' introduce a contrast.","Moreover = além disso.","troca adição por contraste")
X(2,"troca_efeito",3,"'Nevertheless' means 'no entanto'.","'Nevertheless' means 'por isso'.","Nevertheless = no entanto.","troca contraste por consequência")
# 3 tempos
X(3,"troca_efeito",3,"In 'She has worked here since 2020', the present perfect shows an action that began in the past and continues now.","In 'She has worked here since 2020', the present perfect shows a finished action with no link to the present.","Has worked + since = ainda trabalha.","vê ação encerrada")
X(3,"norma_culta",3,"'I saw him yesterday' uses the simple past because the time is finished.","'I have seen him yesterday' is the standard form because the time is finished.","Yesterday + simple past.","present perfect com tempo terminado")
X(3,"troca_efeito",3,"In 'When I arrived, the meeting had started', the meeting started before I arrived.","In 'When I arrived, the meeting had started', the meeting started after I arrived.","Had started = antes.","inverte a ordem")
X(3,"troca_efeito",2,"'They are voting now' describes an action in progress.","'They are voting now' describes a habit.","Present continuous = em andamento.","troca andamento por hábito")
X(3,"conceito_correto",3,"In 'Look at the clouds! It is going to rain', 'is going to' expresses a prediction based on present evidence.","In 'Look at the clouds! It is going to rain', 'is going to' expresses a past habit.","Going to = previsão com evidência.","troca previsão por hábito passado")
X(3,"troca_efeito",2,"'He used to smoke' means he no longer smokes.","'He used to smoke' means he smokes now.","Used to = não mais.","lê hábito passado como atual")
X(3,"troca_efeito",3,"'The bill has just been approved' refers to a recent event.","'The bill has just been approved' refers to an event from many years ago.","Just = há pouco.","lê evento recente como antigo")
# 4 modais
X(4,"confusao_instituto",3,"'You must not enter' expresses prohibition.","'You must not enter' means it is not necessary to enter.","Must not = proibido.","confunde proibição e dispensa")
X(4,"confusao_instituto",3,"'You don't have to attend' means attendance is not obligatory.","'You don't have to attend' means attendance is prohibited.","Don't have to = não precisa.","confunde dispensa e proibição")
X(4,"troca_efeito",2,"'She might be at home' expresses possibility.","'She might be at home' expresses obligation.","Might = talvez.","troca possibilidade por obrigação")
X(4,"troca_efeito",4,"'He can't be the author' expresses a negative deduction: it is impossible that he is the author.","'He can't be the author' expresses the lack of ability to write.","Can't be = não pode ser.","lê dedução como habilidade")
X(4,"troca_efeito",2,"'You should read the report' is advice.","'You should read the report' is a prohibition.","Should = deveria (conselho).","troca conselho por proibição")
X(4,"troca_efeito",3,"'They could have voted' means they had the possibility but did not vote.","'They could have voted' means they did vote.","Could have = poderiam ter (não votaram).","lê possibilidade como fato")
X(4,"troca_efeito",3,"'He must be tired' expresses a logical deduction.","'He must be tired' expresses permission.","Must (dedução) = deve estar.","troca dedução por permissão")
X(4,"troca_efeito",2,"'May I come in?' asks for permission.","'May I come in?' expresses a prediction.","May I = posso?","troca permissão por previsão")
# 5 condicionais
X(5,"troca_efeito",3,"'If you heat ice, it melts' is a zero conditional, expressing a general truth.","'If you heat ice, it melts' expresses a hypothetical future.","Zero conditional = verdade geral.","lê verdade geral como hipótese")
X(5,"troca_efeito",3,"'If the bill passes, taxes will rise' presents a real possibility in the future.","'If the bill passes, taxes will rise' presents an unreal situation in the present.","First conditional = possibilidade real.","lê possibilidade real como irreal")
X(5,"troca_efeito",3,"'If I were president, I would change the law' presents an unreal situation.","'If I were president, I would change the law' presents a real possibility.","Second conditional = irreal.","lê irreal como real")
X(5,"troca_efeito",4,"'If they had voted earlier, the law would have passed' refers to the past, and the law did not pass.","'If they had voted earlier, the law would have passed' refers to a future possibility.","Third conditional = passado irreal.","lê passado como futuro")
X(5,"confusao_instituto",3,"'Unless you sign, the contract is void' means 'if you do not sign, the contract is void'.","'Unless you sign, the contract is void' means 'if you sign, the contract is void'.","Unless = if not.","lê unless como if")
X(5,"troca_efeito",3,"'I wish I knew the answer' means I do not know the answer now.","'I wish I knew the answer' means I know the answer now.","Wish + passado = lamento no presente.","inverte o sentido")
X(5,"troca_efeito",3,"'Provided that' and 'as long as' introduce conditions.","'Provided that' and 'as long as' introduce contrasts.","Provided that = desde que.","troca condição por contraste")
# 6 passiva
X(6,"conceito_correto",1,"'The law was approved by Congress' is in the passive voice.","'The law was approved by Congress' is in the active voice.","Was approved by = passiva.","lê passiva como ativa")
X(6,"troca_efeito",3,"'The report has been published' does not say who published it.","'The report has been published' says that the author published it.","Agente omitido.","inventa o agente")
X(6,"troca_efeito",2,"The active form of 'The bill was rejected by the Senate' is 'The Senate rejected the bill'.","The active form of 'The bill was rejected by the Senate' is 'The bill rejected the Senate'.","Agente vira sujeito.","inverte os papéis")
X(6,"troca_efeito",3,"'The new rule is being discussed' means the discussion is in progress.","'The new rule is being discussed' means the discussion is finished.","Is being + particípio = em andamento.","lê andamento como fim")
X(6,"confusao_instituto",4,"'She had her car repaired' means that someone else repaired the car.","'She had her car repaired' means that she repaired the car herself.","Causativa: outro fez.","lê causativa como ação própria")
X(6,"troca_efeito",3,"In 'Mistakes were made', the agent is omitted.","In 'Mistakes were made', the agent is named.","Passiva sem agente.","inventa o agente")
# 7 discurso indireto
X(7,"troca_efeito",3,"'She said she was tired' reports the direct speech 'I am tired'.","'She said she was tired' reports the direct speech 'I will be tired'.","Said + was = I am.","muda o tempo original")
X(7,"troca_efeito",3,"'He told me that he would come' reports 'I will come'.","'He told me that he would come' reports 'I came'.","Would = will.","muda o tempo original")
X(7,"conceito_correto",3,"'She asked whether I had finished' reports a question.","'She asked whether I had finished' reports a command.","Asked whether = pergunta.","lê pergunta como ordem")
X(7,"norma_culta",4,"The sentence 'He told that he was late' is inadequate, because 'tell' normally requires an object ('told me').","The sentence 'He told that he was late' is adequate, because 'tell' does not require an object.","Tell pede objeto.","trata tell como say")
X(7,"troca_efeito",4,"'The minister denied having signed the document' means he said he did not sign it.","'The minister denied having signed the document' means he admitted signing it.","Deny = negar.","inverte o sentido")
X(7,"troca_efeito",3,"'He urged them to vote' reports an urgent request to vote.","'He urged them to vote' reports a prohibition to vote.","Urge = instar.","lê pedido como proibição")
# 8 relativos e referentes
X(8,"atribuicao_autor",2,"In 'The senator who proposed the bill resigned', 'who' refers to 'the senator'.","In 'The senator who proposed the bill resigned', 'who' refers to 'the bill'.","Who = pessoa.","aponta o referente errado")
X(8,"conceito_correto",2,"'Whose' indicates possession, as in 'the man whose car was stolen'.","'Whose' indicates time, as in 'the man whose car was stolen'.","Whose = cujo.","troca posse por tempo")
X(8,"confusao_instituto",4,"In 'The report, which was long, was rejected', the clause 'which was long' adds extra information.","In 'The report, which was long, was rejected', the clause 'which was long' identifies which report is meant among several.","Com vírgulas: informação extra.","lê explicativa como restritiva")
X(8,"atribuicao_autor",2,"In 'The company said it would hire more staff', 'it' refers to 'the company'.","In 'The company said it would hire more staff', 'it' refers to 'staff'.","It = the company.","aponta o referente errado")
X(8,"atribuicao_autor",4,"In 'He lost the election, which surprised everyone', 'which' refers to the fact that he lost.","In 'He lost the election, which surprised everyone', 'which' refers to 'everyone'.","Which = a ideia toda.","aponta o referente errado")
X(8,"conceito_correto",2,"In 'This is the city where I was born', 'where' refers to a place.","In 'This is the city where I was born', 'where' refers to a person.","Where = lugar.","troca lugar por pessoa")
X(8,"norma_culta",3,"In 'the book that I read', 'that' can be omitted: 'the book I read'.","In 'the book that I read', 'that' cannot be omitted.","That objeto pode sair.","exige o 'that'")
# 9 quantificadores
X(9,"confusao_instituto",3,"'Few lawmakers attended' suggests that almost nobody attended, while 'a few lawmakers attended' suggests some did.","'Few lawmakers attended' and 'a few lawmakers attended' have the same meaning.","Few = quase nenhum; a few = alguns.","trata few e a few como iguais")
X(9,"confusao_instituto",3,"'There is little time' means there is not enough time.","'There is little time' means there is plenty of time.","Little = pouco.","inverte o sentido")
X(9,"norma_culta",3,"'Fewer' is used with countable nouns, as in 'fewer people', and 'less' with uncountable nouns, as in 'less money'.","'Fewer' is used with uncountable nouns, as in 'fewer money', and 'less' with countable nouns.","Fewer + contável; less + incontável.","inverte contável e incontável")
X(9,"troca_efeito",3,"'The more he explained, the less I understood' shows a proportional relation.","'The more he explained, the less I understood' shows a simple condition.","The more… the less = proporção.","troca proporção por condição")
X(9,"troca_efeito",2,"'This bill is as important as the last one' means the two bills have equal importance.","'This bill is as important as the last one' means the last one is more important.","As… as = igualdade.","lê igualdade como superioridade")
X(9,"norma_culta",2,"'Much' is used with uncountable nouns and 'many' with countable nouns.","'Much' is used with countable nouns and 'many' with uncountable nouns.","Much + incontável; many + contável.","inverte")
X(9,"troca_efeito",3,"'Neither of the parties agreed' means that none of the two parties agreed.","'Neither of the parties agreed' means that both parties agreed.","Neither = nenhum dos dois.","inverte o sentido")
# 10 negação
X(10,"troca_efeito",2,"'He hardly speaks' means he speaks very little.","'He hardly speaks' means he speaks a lot.","Hardly = quase não.","inverte o sentido")
X(10,"troca_efeito",2,"'Rarely' and 'seldom' mean 'raramente'.","'Rarely' and 'seldom' mean 'frequentemente'.","Rarely/seldom = raramente.","inverte o sentido")
X(10,"troca_efeito",3,"In 'barely enough food', 'barely' means 'quase não'.","In 'barely enough food', 'barely' means 'mais do que'.","Barely = mal, quase não.","inverte o sentido")
X(10,"troca_efeito",3,"In 'Not only did she win, but she also set a record', 'not only… but also' adds information.","In 'Not only did she win, but she also set a record', 'not only… but also' contrasts two ideas.","Not only… but also = adição.","troca adição por contraste")
X(10,"troca_efeito",3,"'Neither… nor' joins two negative options.","'Neither… nor' joins two positive options.","Neither… nor = nem… nem.","inverte o sentido")
X(10,"troca_efeito",4,"'No sooner had he arrived than the meeting started' means the meeting started right after he arrived.","'No sooner had he arrived than the meeting started' means the meeting started before he arrived.","No sooner… than = logo que.","inverte a ordem")
X(10,"troca_efeito",3,"'Scarcely any money' means almost no money.","'Scarcely any money' means a lot of money.","Scarcely = quase nada.","inverte o sentido")
# 11 phrasal verbs
X(11,"confusao_instituto",2,"'Carry out an investigation' means 'realizar uma investigação'.","'Carry out an investigation' means 'carregar uma investigação para fora'.","Carry out = realizar.","tradução literal")
X(11,"confusao_instituto",2,"'Call off' means 'cancelar'.","'Call off' means 'convocar'.","Call off = cancelar.","troca pelo sentido oposto")
X(11,"confusao_instituto",2,"'Put off the vote' means 'adiar a votação'.","'Put off the vote' means 'antecipar a votação'.","Put off = adiar.","troca pelo sentido oposto")
X(11,"confusao_instituto",2,"'Point out' means 'apontar' or 'destacar'.","'Point out' means 'esquecer'.","Point out = apontar.","sentido sem relação")
X(11,"confusao_instituto",3,"'Run out of time' means 'ficar sem tempo'.","'Run out of time' means 'ter tempo de sobra'.","Run out of = acabar.","troca pelo sentido oposto")
X(11,"confusao_instituto",2,"'Turn down an offer' means 'recusar uma oferta'.","'Turn down an offer' means 'aceitar uma oferta'.","Turn down = recusar.","troca pelo sentido oposto")
X(11,"confusao_instituto",3,"'Set up a committee' means 'criar uma comissão'.","'Set up a committee' means 'dissolver uma comissão'.","Set up = criar.","troca pelo sentido oposto")
X(11,"confusao_instituto",2,"'Give up' means 'desistir'.","'Give up' means 'insistir'.","Give up = desistir.","troca pelo sentido oposto")
# 12 prefixos e sufixos
X(12,"troca_efeito",1,"The prefix 'un-' in 'unfair' gives the word the opposite meaning.","The prefix 'un-' in 'unfair' makes the word stronger.","Un- = oposto.","lê negação como intensificação")
X(12,"troca_efeito",2,"The suffix '-less' means 'sem', as in 'jobless'.","The suffix '-less' means 'com', as in 'jobless'.","-less = sem.","troca sem por com")
X(12,"troca_efeito",2,"The suffix '-ful' means 'cheio de', as in 'hopeful'.","The suffix '-ful' means 'sem', as in 'hopeful'.","-ful = cheio de.","troca com por sem")
X(12,"troca_efeito",2,"The prefix 'mis-' indicates error, as in 'misunderstand'.","The prefix 'mis-' indicates repetition, as in 'misunderstand'.","Mis- = erro.","troca erro por repetição")
X(12,"troca_efeito",2,"The prefix 're-' indicates repetition, as in 'rewrite'.","The prefix 're-' indicates opposition, as in 'rewrite'.","Re- = de novo.","troca repetição por oposição")
X(12,"troca_efeito",2,"The suffix '-able' means 'possível de', as in 'readable'.","The suffix '-able' means 'impossível de', as in 'readable'.","-able = possível.","inverte o sentido")
X(12,"troca_efeito",3,"The prefix 'over-' indicates excess, as in 'overworked'.","The prefix 'over-' indicates lack, as in 'overworked'.","Over- = excesso.","inverte o sentido")
X(12,"troca_efeito",2,"The prefix 'dis-' indicates negation, as in 'disagree'.","The prefix 'dis-' indicates agreement, as in 'disagree'.","Dis- = negação.","inverte o sentido")
# 13 vocabulário legislativo
X(13,"confusao_instituto",3,"In legislative contexts, a 'bill' is a proposed law that has not yet been enacted.","In legislative contexts, a 'bill' is a law already in force.","Bill = projeto de lei.","lê projeto como lei vigente")
X(13,"confusao_instituto",2,"'Lawmakers' are legislators, such as members of Congress.","'Lawmakers' are lawyers who defend clients in court.","Lawmaker = parlamentar.","confunde com advogados")
X(13,"confusao_instituto",3,"'To enact a law' means 'editar ou promulgar uma lei'.","'To enact a law' means 'revogar uma lei'.","Enact = editar.","troca por 'revogar'")
X(13,"confusao_instituto",3,"'To repeal a law' means 'revogar uma lei'.","'To repeal a law' means 'sancionar uma lei'.","Repeal = revogar.","troca por 'sancionar'")
X(13,"confusao_instituto",4,"'Oversight' can mean 'fiscalização' or 'descuido', depending on the context.","'Oversight' means 'fiscalização' in every context.","Oversight: dois sentidos.","fixa um só sentido")
X(13,"confusao_instituto",3,"'Stakeholders' are people or groups with an interest in a decision or project.","'Stakeholders' are inspectors who check the accounts.","Stakeholders = partes interessadas.","troca por fiscais")
X(13,"confusao_instituto",3,"'Accountable' means 'responsável', that is, someone who must explain their actions.","'Accountable' means 'que pode ser contado'.","Accountable = que presta contas.","traduz pela forma")
X(13,"confusao_instituto",2,"'Amendment' means 'emenda'.","'Amendment' means 'acordo'.","Amendment = emenda.","troca o sentido")
X(13,"confusao_instituto",3,"A court 'ruling' is a decision made by a court.","A court 'ruling' is an informal rule among judges.","Ruling = decisão judicial.","troca por regra informal")
X(13,"confusao_instituto",2,"'Funding' means 'financiamento'.","'Funding' means 'diversão'.","Funding = financiamento.","troca o sentido")
# 14 leitura: ideia principal
J(14,"generalizacao",3,"Remote work has grown since 2020. Many employees save time and money, but some report feeling isolated from colleagues.","The text presents both advantages and a disadvantage of remote work.","The text argues that remote work should be abolished.","Vantagens e desvantagem.","extrapola a tese")
J(14,"atribuicao_autor",3,"The city council approved a new bike lane program. Supporters say it will reduce traffic, while critics worry about the cost.","Critics are concerned about the cost of the program.","Supporters are concerned about the cost of the program.","Critics = custo.","troca a fonte")
J(14,"generalizacao",4,"Although the study included only 200 participants, its authors believe the results may apply to larger groups.","The authors are cautious: they say the results may apply to larger groups.","The authors say the study included thousands of participants.","200 participantes.","inverte um dado")
J(14,"troca_efeito",2,"The airline cancelled 40 flights on Monday because of a storm. Passengers were offered hotel rooms.","The cancellations were caused by bad weather.","The cancellations were caused by a strike.","Because of a storm.","troca a causa")
J(14,"troca_efeito",2,"Renewable energy now supplies a third of the country's electricity, up from 10% a decade ago.","The share of renewable energy has increased over ten years.","The share of renewable energy has decreased over ten years.","Up from 10% = aumento.","inverte a tendência")
J(14,"generalizacao",3,"The minister declined to comment on the report, saying only that an investigation was under way.","The minister did not comment on the content of the report.","The minister praised the report.","Declined to comment.","inventa um fato")
J(14,"atribuicao_autor",3,"Not every voter supports the proposal; a recent poll found that 45% oppose it.","According to the poll, 45% of voters are against the proposal.","According to the poll, 45% of voters support the proposal.","Oppose = ser contra.","inverte o dado")
J(14,"generalizacao",3,"Experts warn that the new software may reduce errors, but it cannot replace human judgment.","The experts see a limit to what the software can do.","The experts say the software can replace human judgment.","Cannot replace.","apaga a ressalva")
# 15 leitura: inferência, referência, tom
J(15,"generalizacao",3,"After three hours of debate, the committee had still not reached an agreement.","It can be inferred that the debate was long and inconclusive.","It can be inferred that the committee approved the proposal.","Still not reached.","inventa o resultado")
J(15,"generalizacao",4,"The report was released late on Friday, when few people were paying attention.","The author suggests that the timing may have reduced attention to the report.","The author says the report received wide media coverage.","Late Friday, few people.","contradiz o texto")
J(15,"atribuicao_autor",2,"Critics call the plan “ambitious”; supporters call it “necessary”.","The text reports two different views of the plan.","The text shows that everyone agrees about the plan.","Critics × supporters.","vê consenso")
J(15,"generalizacao",4,"The company says the data leak affected “a small number” of users, but did not give a figure.","The company did not state how many users were affected.","The company stated the exact number of users affected.","Did not give a figure.","inventa um dado")
J(15,"atribuicao_autor",3,"The senators approved the budget, which had been delayed for months.","In the sentence, “which” refers to the budget.","In the sentence, “which” refers to the senators.","Which = the budget.","aponta o referente errado")
J(15,"troca_efeito",2,"Thanks to the new app, queues at the clinic are shorter. Patients no longer wait outside.","The new app has improved the situation at the clinic.","The new app has made the queues longer.","Thanks to = por causa de (positivo).","inverte o efeito")
J(15,"troca_efeito",4,"What a surprise! The meeting finished early for once.","The author's tone suggests that meetings usually do not finish early.","The author's tone suggests that meetings usually finish early.","For once = dessa vez.","inverte o tom")
J(15,"generalizacao",4,"Unlike last year, this year's budget includes funds for training.","It can be inferred that last year's budget did not include funds for training.","It can be inferred that both budgets include funds for training.","Unlike = ao contrário de.","ignora o contraste")
# 16 inglês contemporâneo
X(16,"conceito_correto",1,"“AI” stands for “artificial intelligence”.","“AI” stands for “automatic internet”.","AI = inteligência artificial.","troca a sigla")
X(16,"conceito_correto",2,"“Fake news” refers to false information presented as news.","“Fake news” refers to news about fashion.","Fake news = notícia falsa.","troca o sentido")
X(16,"conceito_correto",2,"A “data breach” is an incident in which data is exposed or stolen.","A “data breach” is a contract for data storage.","Data breach = vazamento.","troca o sentido")
X(16,"conceito_correto",2,"In informal English, “gonna” is a contraction of “going to”.","In informal English, “gonna” is a contraction of “got to”.","Gonna = going to.","troca a contração")
X(16,"conceito_correto",2,"“ASAP” means “as soon as possible”.","“ASAP” means “always send a package”.","ASAP = o quanto antes.","troca a sigla")
X(16,"conceito_correto",2,"“A piece of cake” is an idiom that means something very easy.","“A piece of cake” is an idiom that means something very expensive.","Piece of cake = moleza.","troca o sentido")
X(16,"conceito_correto",2,"“To go viral” means to spread quickly online.","“To go viral” means to get sick online.","Go viral = viralizar.","tradução literal")
X(16,"conceito_correto",3,"A “deepfake” is media altered by AI to imitate a real person.","A “deepfake” is a type of encryption.","Deepfake = mídia falsa por IA.","troca o sentido")
# 17 números e tendências
X(17,"troca_efeito",1,"“Prices doubled” means that prices became twice as high.","“Prices doubled” means that prices fell by half.","Doubled = dobrou.","inverte o sentido")
X(17,"troca_efeito",2,"“Sales plunged by 30%” indicates a sharp fall.","“Sales plunged by 30%” indicates a slight rise.","Plunge = despencar.","inverte o sentido")
X(17,"troca_efeito",3,"“Unemployment fell from 9% to 6%” shows a decrease of three percentage points.","“Unemployment fell from 9% to 6%” shows an increase of three percentage points.","Fell = caiu.","inverte o sentido")
X(17,"troca_efeito",2,"“Soar” and “surge” indicate a sharp rise.","“Soar” and “surge” indicate stability.","Soar/surge = disparar.","inverte o sentido")
X(17,"troca_efeito",2,"“Remained stable” means that something did not change significantly.","“Remained stable” means that something changed sharply.","Stable = estável.","inverte o sentido")
X(17,"troca_efeito",3,"“A threefold increase” means that the value became three times larger.","“A threefold increase” means that the value increased by 3%.","Threefold = triplo.","confunde triplo com 3%")
X(17,"troca_efeito",3,"“Nearly half of the voters” means slightly less than 50%.","“Nearly half of the voters” means slightly more than 50%.","Nearly = quase.","troca quase por mais de")
X(17,"troca_efeito",2,"“Over 60%” means more than 60%.","“Over 60%” means less than 60%.","Over = mais de.","inverte o sentido")
# 18 gerúndio, infinitivo etc.
X(18,"norma_culta",3,"In “He enjoys reading reports”, the verb “enjoy” is followed by a gerund.","In “He enjoys reading reports”, the verb “enjoy” is followed by “to + infinitive”.","Enjoy + -ing.","troca gerúndio por infinitivo")
X(18,"norma_culta",3,"In “She decided to resign”, the verb “decide” is followed by an infinitive.","In “She decided to resign”, the verb “decide” is followed by a gerund.","Decide + to.","troca infinitivo por gerúndio")
X(18,"conceito_correto",1,"In “Please sign here”, the verb “sign” is in the imperative.","In “Please sign here”, the verb “sign” is in the past tense.","Imperativo = verbo base.","lê imperativo como passado")
X(18,"conceito_correto",2,"In “the senator's office”, the apostrophe + s shows possession.","In “the senator's office”, the apostrophe + s is a contraction of “is”.","'s = posse.","lê posse como contração")
X(18,"conceito_correto",3,"The question tag in “The vote was fair, wasn't it?” seeks confirmation.","The question tag in “The vote was fair, wasn't it?” introduces a new topic.","Tag pede confirmação.","troca confirmação por tema novo")
X(18,"conceito_correto",4,"In “It is important that he be present”, the verb “be” is in the subjunctive.","In “It is important that he be present”, the verb “be” is in the indicative.","Subjuntivo: be.","troca subjuntivo por indicativo")
X(18,"conceito_correto",3,"In “I did call you!”, the auxiliary “did” emphasizes the verb.","In “I did call you!”, the auxiliary “did” makes the sentence negative.","Did enfático.","lê ênfase como negação")
X(18,"confusao_instituto",4,"“Stop smoking” means to quit smoking, while “stop to smoke” means to pause in order to smoke.","“Stop smoking” means to pause in order to smoke, while “stop to smoke” means to quit smoking.","Stop -ing = parar; stop to = parar para.","inverte os dois")
