# Língua Inglesa — onda 2. Itens curtos em inglês; comentário em português (≤25 palavras).
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
PT_={23:"EN01",24:"EN01",22:"EN03",21:"EN03",26:"EN04",28:"EN04"}
def X(atom, padE, dif, C, E, com, terro):
    _n[0]+=1
    P(PT_.get(atom,"EN02"),[str(atom)],"conceito_correto",padE,dif,C,E,com,terro,f"f{_n[0]:03d}")
def J(atom, padE, dif, texto, C, E, com, terro):
    t="“"+texto+"” — "
    X(atom, padE, dif, t+C, t+E, com, terro)


# 19 básico: artigos, plurais, there is/are
X(19,"norma_culta",1,"The plural of 'child' is 'children'.","The plural of 'child' is 'childs'.","Plural irregular.","plural regular")
X(19,"norma_culta",1,"The plural of 'person' is usually 'people'.","The plural of 'person' is always 'persons'.","People é o usual.","absolutiza")
X(19,"norma_culta",2,"'Information' is uncountable, so 'informations' is incorrect.","'Information' is countable, so 'informations' is correct.","Information é incontável.","trata como contável")
X(19,"norma_culta",2,"'The news is encouraging' is correct, because 'news' takes a singular verb.","'The news are encouraging' is correct, because 'news' ends in -s.","News = singular.","verbo no plural")
X(19,"norma_culta",2,"We say 'an hour' because the word starts with a vowel sound.","We say 'a hour' because the word starts with the letter h.","Conta o som, não a letra.","guia-se pela letra")
X(19,"norma_culta",1,"'There are two amendments' uses 'are' because 'amendments' is plural.","'There is two amendments' is the correct form.","There are + plural.","is com plural")
X(19,"norma_culta",2,"'Advice' is uncountable; we say 'a piece of advice'.","'Advice' is countable; we say 'an advice'.","Advice incontável.","usa artigo indefinido")
X(19,"norma_culta",2,"'The' is used when the noun is already known to the reader.","'The' is used only before plural nouns.","The = específico.","restringe ao plural")
X(19,"norma_culta",3,"We say 'a university' because the first sound is /j/, a consonant sound.","We say 'an university' because 'u' is a vowel letter.","Som de consoante.","guia-se pela letra")
X(19,"norma_culta",2,"'Men', 'women' and 'feet' are irregular plurals.","'Men', 'women' and 'feet' are singular nouns.","Plurais irregulares.","lê plural como singular")
# 20 básico: pronomes e auxiliares
X(20,"norma_culta",1,"'He doesn't work here' is correct.","'He doesn't works here' is correct.","Após doesn't, verbo base.","verbo com -s")
X(20,"norma_culta",1,"'Does she know the answer?' is correct.","'Does she knows the answer?' is correct.","Após does, verbo base.","verbo com -s")
X(20,"norma_culta",2,"'Its' is a possessive, as in 'The court issued its decision'.","'Its' means 'it is', as in 'The court issued its decision'.","Its = posse; it's = it is.","confunde its e it's")
X(20,"norma_culta",2,"In 'It's late', 'it's' is a contraction of 'it is'.","In 'It's late', 'it's' is a possessive form.","It's = it is.","lê como posse")
X(20,"norma_culta",1,"'Them' is an object pronoun; 'they' is a subject pronoun.","'Them' is a subject pronoun; 'they' is an object pronoun.","Them = objeto.","inverte")
X(20,"norma_culta",1,"In 'We gave them the report', 'them' refers to other people.","In 'We gave them the report', 'them' refers to the speakers.","Them ≠ we.","retoma o falante")
X(20,"norma_culta",2,"'Their' shows possession, as in 'their votes'.","'Their' means 'in that place', as in 'their votes'.","Their = deles; there = lá.","troca por there")
X(20,"norma_culta",2,"'Did you sign?' uses the base form 'sign' after 'did'.","'Did you signed?' is the standard form.","Did + base.","passado após did")
X(20,"norma_culta",2,"'Do they agree?' is correct for a plural subject.","'Does they agree?' is correct for a plural subject.","Does só 3ª sing.","does com they")
X(20,"norma_culta",1,"'She' replaces a female subject; 'he' replaces a male one.","'She' and 'he' can be used for both genders.","Gênero distinto.","iguala os pronomes")
# 21 phrasal verbs
X(21,"confusao_instituto",2,"'The committee carried out an investigation' means it conducted an investigation.","'The committee carried out an investigation' means it cancelled an investigation.","Carry out = realizar.","troca por cancelar")
X(21,"confusao_instituto",2,"'He turned down the offer' means he refused it.","'He turned down the offer' means he accepted it.","Turn down = recusar.","inverte")
X(21,"confusao_instituto",3,"'The minister stepped down' means the minister resigned.","'The minister stepped down' means the minister was promoted.","Step down = renunciar.","troca por promoção")
X(21,"confusao_instituto",2,"'The group called for reform' means it demanded reform.","'The group called for reform' means it telephoned the reformers.","Call for = exigir.","sentido literal")
X(21,"confusao_instituto",3,"'The agency will look into the complaint' means it will investigate it.","'The agency will look into the complaint' means it will ignore it.","Look into = investigar.","troca por ignorar")
X(21,"confusao_instituto",2,"'To point out' a problem means to call attention to it.","'To point out' a problem means to hide it.","Point out = ressaltar.","troca por ocultar")
X(21,"confusao_instituto",3,"'The government set up a fund' means it created a fund.","'The government set up a fund' means it closed a fund.","Set up = instituir.","troca por encerrar")
X(21,"confusao_instituto",3,"'To back up a claim' means to support it with evidence.","'To back up a claim' means to deny it.","Back up = apoiar.","troca por negar")
X(21,"confusao_instituto",3,"'The company rolled out a new service' means it launched it.","'The company rolled out a new service' means it withdrew it.","Roll out = lançar.","troca por retirar")
X(21,"confusao_instituto",3,"'To cut down on spending' means to reduce spending.","'To cut down on spending' means to increase spending.","Cut down on = reduzir.","inverte")
X(21,"confusao_instituto",4,"'The talks broke down' means the negotiations failed.","'The talks broke down' means the negotiations were concluded successfully.","Break down = fracassar.","inverte")
# 22 vocabulário de notícias
X(22,"confusao_instituto",2,"A 'pledge' is a formal promise or commitment.","A 'pledge' is a formal complaint.","Pledge = compromisso.","troca por queixa")
X(22,"confusao_instituto",2,"A 'ban' is an official prohibition.","A 'ban' is an official authorization.","Ban = proibição.","inverte")
X(22,"confusao_instituto",3,"A 'budget surplus' means that revenue is greater than spending.","A 'budget surplus' means that spending is greater than revenue.","Surplus = superávit.","confunde com déficit")
X(22,"confusao_instituto",2,"A tax 'hike' is an increase in taxes.","A tax 'hike' is a reduction in taxes.","Hike = aumento.","inverte")
X(22,"confusao_instituto",2,"An opinion 'poll' measures what people think.","An opinion 'poll' is a type of tax.","Poll = pesquisa.","troca por tributo")
X(22,"confusao_instituto",3,"'Voter turnout' is the number of voters who actually vote.","'Voter turnout' is the number of candidates in an election.","Turnout = comparecimento.","troca por candidatos")
X(22,"confusao_instituto",3,"A 'watchdog' in politics is an organization that monitors the authorities.","A 'watchdog' in politics is an official who protects the president.","Watchdog = fiscalizador.","troca por segurança")
X(22,"confusao_instituto",3,"To 'veto' a bill means to reject it.","To 'veto' a bill means to approve it.","Veto = vetar.","inverte")
X(22,"confusao_instituto",3,"To 'ratify' a treaty means to confirm it formally.","To 'ratify' a treaty means to withdraw from it.","Ratify = ratificar.","troca por retirada")
X(22,"confusao_instituto",3,"A 'crackdown' on corruption is a strict enforcement campaign.","A 'crackdown' on corruption is a tolerant policy.","Crackdown = endurecimento.","inverte")
X(22,"confusao_instituto",2,"A 'lawsuit' is a legal action brought before a court.","A 'lawsuit' is a clothing item worn by lawyers.","Lawsuit = ação judicial.","jogo de palavras")
# 23 hedging
J(23,"generalizacao",3,"The new drug may reduce the risk of heart disease.","The text does not say that the drug certainly reduces the risk.","The text says that the drug certainly reduces the risk.","May = possibilidade.","transforma em certeza")
J(23,"generalizacao",3,"Some voters said they were undecided.","The text refers to part of the voters, not all of them.","The text refers to all voters.","Some ≠ all.","generaliza")
J(23,"generalizacao",3,"The funds were allegedly misused.","The text does not confirm that the funds were misused.","The text confirms that the funds were misused.","Allegedly = alegadamente.","afirma como fato")
J(23,"generalizacao",3,"Most students passed the exam.","The text indicates that the majority passed, not necessarily all.","The text indicates that all students passed.","Most = a maioria.","generaliza")
J(23,"generalizacao",4,"The results suggest that the policy has worked so far.","The author presents the success of the policy as provisional.","The author presents the success of the policy as final.","Suggest + so far.","apaga a cautela")
J(23,"generalizacao",3,"Unemployment seems to be falling.","The author uses a cautious verb to describe the fall.","The author states categorically that unemployment fell.","Seems = parece.","apaga a cautela")
J(23,"generalizacao",3,"Nearly 70% of the workers approved the plan.","The share of approval was just below 70%.","The share of approval was clearly above 70%.","Nearly = quase.","troca quase por mais de")
J(23,"atribuicao_autor",4,"The mayor says the road will be ready in May. Residents doubt it.","The text separates the mayor's claim from the residents' doubt.","The text confirms that the road will be ready in May.","Says × doubt.","trata a promessa como fato")
J(23,"generalizacao",3,"The company reportedly lost millions last year.","The loss is presented as reported by others, not as confirmed.","The loss is presented as officially confirmed.","Reportedly.","afirma como fato")
J(23,"generalizacao",3,"Few lawmakers attended the session.","The text implies that attendance was low.","The text implies that attendance was high.","Few = poucos.","inverte")
# 24 verbos de relato
J(24,"atribuicao_autor",3,"The minister admitted that the plan had failed.","The minister recognized the failure of the plan.","The minister denied the failure of the plan.","Admit = reconhecer.","inverte admit e deny")
J(24,"atribuicao_autor",3,"The company denied any wrongdoing.","The company said it did nothing wrong.","The company confessed to wrongdoing.","Deny = negar.","inverte")
J(24,"atribuicao_autor",3,"Experts warn that prices may rise.","The experts are alerting to a risk.","The experts are celebrating a benefit.","Warn = alertar.","troca o tom")
J(24,"atribuicao_autor",4,"According to the report, crime fell by 10%.","The 10% figure comes from the report, not necessarily from the author.","The 10% figure is the author's own personal opinion.","According to = fonte.","atribui ao autor")
J(24,"atribuicao_autor",3,"The opposition claims that the vote was rigged.","The opposition says the vote was rigged; the text does not confirm it.","The text confirms that the vote was rigged.","Claim = alega.","trata alegação como fato")
J(24,"atribuicao_autor",3,"The union urged the government to negotiate.","The union asked the government strongly to negotiate.","The union forbade the government to negotiate.","Urge = instar.","troca o sentido")
J(24,"atribuicao_autor",3,"The author argues that taxes should fall.","The author defends a reduction of taxes.","The author opposes a reduction of taxes.","Argue = defender.","inverte")
J(24,"atribuicao_autor",4,"The mayor insisted that the project would go ahead.","The mayor firmly maintained that the project would continue.","The mayor hesitated about continuing the project.","Insist = insistir.","troca por hesitação")
J(24,"atribuicao_autor",3,"Officials pointed out that funding was limited.","Officials called attention to the limited funding.","Officials hid the limited funding.","Point out = ressaltar.","troca por ocultar")
J(24,"atribuicao_autor",4,"The senator conceded that the bill had flaws.","The senator accepted that the bill had flaws.","The senator denied that the bill had flaws.","Concede = admitir.","inverte")
# 25 preposições
X(25,"norma_culta",2,"'It depends on the result' is correct.","'It depends of the result' is correct.","Depend on.","depend of")
X(25,"norma_culta",2,"'She is interested in politics' is correct.","'She is interested on politics' is correct.","Interested in.","interested on")
X(25,"norma_culta",2,"'The committee consists of ten members' is correct.","'The committee consists in ten members' is correct.","Consist of.","consist in")
X(25,"norma_culta",2,"'He is responsible for the budget' is correct.","'He is responsible of the budget' is correct.","Responsible for.","responsible of")
X(25,"norma_culta",2,"'The vote is on Friday' uses 'on' with a day of the week.","'The vote is in Friday' uses 'in' with a day of the week.","On + dia.","in + dia")
X(25,"norma_culta",2,"'The session starts at 9 am' uses 'at' with a clock time.","'The session starts on 9 am' uses 'on' with a clock time.","At + hora.","on + hora")
X(25,"norma_culta",2,"'The law took effect in 2024' uses 'in' with a year.","'The law took effect at 2024' uses 'at' with a year.","In + ano.","at + ano")
X(25,"norma_culta",3,"'This text is different from that one' is standard usage.","'This text is different of that one' is standard usage.","Different from.","different of")
X(25,"norma_culta",2,"'She apologized for the delay' is correct.","'She apologized of the delay' is correct.","Apologize for.","apologize of")
X(25,"norma_culta",2,"'Listen to the speaker' is correct.","'Listen the speaker' is correct.","Listen to.","omite a preposição")
# 26 inglês digital
X(26,"confusao_instituto",2,"'Algorithmic bias' means systematic unfairness in the results of a system.","'Algorithmic bias' means a very fast calculation.","Bias = viés.","troca por velocidade")
X(26,"confusao_instituto",1,"'Password' means 'senha'.","'Password' means 'usuário'.","Password = senha.","troca o sentido")
X(26,"confusao_instituto",2,"'To opt out' of data collection means to choose not to take part.","'To opt out' of data collection means to agree to take part.","Opt out = optar por sair.","inverte")
X(26,"confusao_instituto",2,"'Cloud storage' means 'armazenamento em nuvem'.","'Cloud storage' means 'armazenamento de clima'.","Cloud = nuvem.","traduz mal")
X(26,"confusao_instituto",2,"To 'upload' a file is to send it to a server.","To 'upload' a file is to receive it from a server.","Upload = enviar.","troca por download")
X(26,"confusao_instituto",3,"'Open source' software has code that anyone can inspect and modify.","'Open source' software has code kept secret by its owner.","Open source = código aberto.","inverte")
X(26,"confusao_instituto",3,"To 'hack' a system, in the news, usually means to break into it.","To 'hack' a system, in the news, usually means to repair it.","Hack = invadir.","troca por consertar")
X(26,"confusao_instituto",2,"A 'chatbot' is a program that simulates conversation.","A 'chatbot' is a person who moderates online forums.","Chatbot = programa.","troca por pessoa")
X(26,"confusao_instituto",3,"A 'dataset' is a structured collection of data.","A 'dataset' is a device used to store passwords.","Dataset = conjunto de dados.","troca por dispositivo")
X(26,"confusao_instituto",3,"'Cybersecurity' refers to protecting systems and data from attacks.","'Cybersecurity' refers to the speed of an internet connection.","Cybersecurity = segurança.","troca por velocidade")
# 27 palavras que confundem
X(27,"confusao_instituto",3,"'Affect' is usually a verb; 'effect' is usually a noun.","'Affect' is usually a noun; 'effect' is usually a verb.","Affect = afetar.","inverte as classes")
X(27,"confusao_instituto",2,"'Lose' means 'perder'; 'loose' means 'frouxo'.","'Lose' means 'frouxo'; 'loose' means 'perder'.","Lose = perder.","inverte")
X(27,"confusao_instituto",2,"'Than' is used in comparisons; 'then' means 'então'.","'Then' is used in comparisons; 'than' means 'então'.","Than compara.","inverte")
X(27,"confusao_instituto",3,"'Principle' means 'princípio'; 'principal' can mean 'diretor' or 'principal'.","'Principle' means 'diretor'; 'principal' means 'princípio'.","Principle = princípio.","inverte")
X(27,"confusao_instituto",3,"'He has lived here for ten years' uses 'for' with a period of time.","'He has lived here since ten years' uses 'since' with a period of time.","For + duração; since + início.","since + duração")
X(27,"confusao_instituto",3,"'She has lived here since 2020' uses 'since' with a starting point.","'She has lived here for 2020' uses 'for' with a starting point.","Since + ponto inicial.","for + ponto inicial")
X(27,"confusao_instituto",3,"'Besides' means 'além disso'; 'beside' means 'ao lado de'.","'Besides' means 'ao lado de'; 'beside' means 'além disso'.","Besides = além de.","inverte")
X(27,"confusao_instituto",2,"'They're' means 'they are'; 'there' indicates a place.","'They're' indicates a place; 'there' means 'they are'.","They're = they are.","inverte")
X(27,"confusao_instituto",3,"'Economic' relates to the economy; 'economical' means 'econômico, que poupa'.","'Economic' means 'que poupa'; 'economical' relates to the economy.","Economic × economical.","inverte")
X(27,"confusao_instituto",3,"'Sensible' means 'sensato'; 'sensitive' means 'sensível'.","'Sensible' means 'sensível'; 'sensitive' means 'sensato'.","Sensible = sensato.","falso cognato")
# 28 siglas
X(28,"confusao_instituto",2,"'e.g.' introduces examples, as in 'fruits, e.g. apples'.","'e.g.' introduces a rewording, as in 'fruits, e.g. apples'.","e.g. = por exemplo.","troca por i.e.")
X(28,"confusao_instituto",2,"'i.e.' introduces a clarification, meaning 'isto é'.","'i.e.' introduces a list of examples, meaning 'por exemplo'.","i.e. = isto é.","troca por e.g.")
X(28,"confusao_instituto",1,"'GDP' stands for 'gross domestic product' (PIB).","'GDP' stands for 'general data protection'.","GDP = PIB.","troca a sigla")
X(28,"confusao_instituto",2,"'NGO' stands for 'non-governmental organization' (ONG).","'NGO' stands for 'national government office'.","NGO = ONG.","troca a sigla")
X(28,"confusao_instituto",2,"'WHO' is the World Health Organization (OMS).","'WHO' is the World Hunger Office.","WHO = OMS.","troca a sigla")
X(28,"confusao_instituto",2,"'IMF' is the International Monetary Fund (FMI).","'IMF' is the International Military Force.","IMF = FMI.","troca a sigla")
X(28,"confusao_instituto",2,"'CEO' means chief executive officer.","'CEO' means central election office.","CEO = diretor-executivo.","troca a sigla")
X(28,"confusao_instituto",1,"'vs.' means 'versus', that is, 'contra'.","'vs.' means 'very special'.","Vs. = versus.","troca o sentido")
X(28,"confusao_instituto",2,"'N/A' in a form usually means 'not applicable'.","'N/A' in a form usually means 'no answer yet'.","N/A = não se aplica.","troca o sentido")
X(28,"confusao_instituto",2,"'FAQ' stands for 'frequently asked questions'.","'FAQ' stands for 'formal annual query'.","FAQ = perguntas frequentes.","troca a sigla")
