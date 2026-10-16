# Língua Portuguesa — L20 onda 3: interpretação (LP05) com microtextos. Itens curtos; comentário objetivo (regra + pegadinha).
Q = []
TAILS=[" Essa seria a orientação predominante nas gramáticas normativas.",
 " Trata-se de entendimento corrente na norma-padrão.",
 " Tal solução decorreria, segundo esse entendimento, da estrutura da frase.",
 " Essa seria a leitura mais aceita pelos gramáticos."]
SHORT=[" Isso é consenso."," Essa é a regra geral."," Trata-se de prática corrente."," Esse é o uso padrão."]
def tail(E,C,i):
    gap=len(C)-len(E)
    if len(E) < 0.97*len(C) and gap > 60: return E+TAILS[i%len(TAILS)]
    if len(E) < 0.95*len(C) and gap > 8: return E+SHORT[i%len(SHORT)]
    return E
FG={"tipo":"gramatica","ref":"norma-padrão (Bechara; Cegalla; Cunha e Cintra)","versao":"conhecimento do autor","conferida":"conhecimento"}
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag):
    ex={"fonte":FG,"risco":["doutrina_conhecimento"]}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
_n=[0]
def S(ponto, atom, padE, dif, C, E, com, terro):
    _n[0]+=1
    P(ponto,[str(atom)],"conceito_correto",padE,dif,C,E,com,terro,f"r{_n[0]:02d}")

def I(atom, padE, dif, texto, C, E, com, terro):
    t="“"+texto+"” — "
    S("LP05", atom, padE, dif, t+C, t+E, com, terro)

# 24 inferência × extrapolação
I(24,"generalizacao",2,"A prefeitura adiou a obra do viaduto até que o estudo de impacto seja concluído.","O texto permite inferir que o estudo de impacto ainda não foi concluído.","O texto permite inferir que a obra foi cancelada definitivamente.","Adiar não é cancelar.","extrapola: adiou virou cancelou")
I(24,"generalizacao",3,"Embora o parecer seja favorável, o relator pediu vista para examinar as emendas.","Depreende-se que o relator ainda não votou o parecer.","Depreende-se que o parecer foi rejeitado.","Pedir vista adia o voto.","inventa a rejeição")
I(24,"generalizacao",3,"Poucos servidores concluíram o curso no prazo, o que levou o órgão a prorrogá-lo.","A prorrogação decorre do baixo número de concluintes no prazo.","A prorrogação decorre da falta de interesse dos servidores.","Causa dada: poucos concluíram.","atribui causa não dita")
I(24,"troca_efeito",4,"O orçamento cresceu 5% em 2025, mas a inflação do período foi de 6%.","Houve queda do orçamento em termos reais.","O orçamento diminuiu em valores nominais.","Real ≠ nominal.","confunde real e nominal")
I(24,"troca_efeito",3,"Só serão aceitas inscrições feitas até sexta-feira, às 18h.","Inscrição feita no sábado não será aceita.","Inscrição feita na sexta-feira, às 19h, será aceita.","Prazo vencido às 18h.","ignora o horário-limite")
I(24,"troca_efeito",3,"A comissão não aprovou o requerimento, ainda que tenha reconhecido sua relevância.","A comissão reconheceu a relevância do requerimento e, mesmo assim, não o aprovou.","A comissão aprovou o requerimento por reconhecer sua relevância.","Ainda que = concessão.","lê concessão como causa")
I(24,"generalizacao",3,"Nas últimas eleições, o comparecimento foi menor que o das anteriores.","O comparecimento diminuiu em relação aos pleitos anteriores.","O voto passou a ser facultativo nas últimas eleições.","Texto só compara comparecimento.","extrapola para a regra do voto")
I(24,"troca_efeito",3,"Ninguém contestou o resultado, embora alguns tenham manifestado surpresa.","Houve quem se surpreendesse com o resultado sem contestá-lo.","Alguns contestaram o resultado em razão da surpresa.","Surpresa ≠ contestação.","contradiz 'ninguém contestou'")
# 25 ideia central
I(25,"troca_efeito",2,"A transparência pública não se esgota na publicação de dados: exige que a informação seja compreensível e útil ao cidadão.","O texto defende que publicar dados não basta para haver transparência.","O texto defende que a publicação de dados é desnecessária à transparência.","Não basta ≠ é desnecessário.","troca 'insuficiente' por 'desnecessário'")
I(25,"troca_efeito",3,"O voto obrigatório garante alta participação, mas não assegura engajamento: comparecer às urnas é diferente de se informar.","O texto distingue participação formal de engajamento.","O texto afirma que o voto obrigatório reduz a participação.","Distinção, não redução.","inverte o efeito do voto obrigatório")
I(25,"atribuicao_autor",3,"Muitos veem na burocracia um entrave; contudo, seus procedimentos protegem o cidadão contra o arbítrio.","O autor contrapõe a visão comum sobre a burocracia a um benefício que ela traz.","O autor endossa a visão de que a burocracia é, em essência, um entrave.","'Contudo' contrapõe a visão comum.","atribui ao autor a opinião de 'muitos'")
I(25,"troca_efeito",2,"Primeiro, o prazo era exíguo. Depois, faltaram servidores. Por fim, o sistema falhou. Eis por que o projeto atrasou.","O trecho enumera causas do atraso do projeto.","O trecho enumera consequências do atraso do projeto.","'Eis por que' introduz causas.","troca causa por consequência")
I(25,"atribuicao_autor",2,"Segundo o relator, a emenda é inconstitucional; a defesa, porém, sustenta o contrário.","O texto apresenta posições opostas sobre a constitucionalidade da emenda.","O texto apresenta consenso sobre a constitucionalidade da emenda.","'Porém' marca oposição.","vê consenso onde há conflito")
I(25,"generalizacao",3,"A inteligência artificial agiliza a triagem de documentos, mas não substitui a revisão humana.","O texto reconhece um benefício da inteligência artificial e aponta um limite.","O texto defende que a revisão humana deve ser abolida.","Limite da IA, não abolição.","extrapola a tese")
I(25,"troca_efeito",3,"A cidade cresceu sem planejamento; hoje paga o preço em trânsito e enchentes.","O texto relaciona o crescimento sem planejamento aos problemas atuais da cidade.","O texto atribui o trânsito e as enchentes ao excesso de planejamento.","Falta de planejamento é a causa.","inverte a causa")
# 26 sentido, ironia, função
I(26,"troca_efeito",2,"Brilhante a ideia de marcar a votação para o feriado: assim ninguém compareceria.","O adjetivo “brilhante” é empregado com ironia.","O adjetivo “brilhante” é empregado em sentido literal, elogiando a ideia.","Elogio que critica = ironia.","lê a ironia como elogio")
I(26,"conceito_correto",2,"O projeto foi engavetado antes mesmo de chegar ao plenário.","“Engavetado” tem sentido figurado: paralisado, deixado sem andamento.","“Engavetado” tem sentido literal: guardado fisicamente em uma gaveta.","Sentido figurado.","lê o figurado como literal")
I(26,"troca_efeito",2,"A decisão caiu como uma bomba entre os servidores.","A comparação indica o forte impacto da decisão.","A comparação indica que a decisão foi recebida com alívio.","Bomba = impacto negativo.","inverte o efeito da comparação")
I(26,"troca_efeito",3,"O ministro, que prometera transparência, recusou-se a divulgar a lista; coerência, afinal, é artigo raro.","A última oração ironiza a incoerência do ministro.","A última oração elogia a coerência do ministro.","Ironia contra o ministro.","lê ironia como elogio")
I(26,"troca_efeito",3,"O parecer, longo e confuso, parecia escrito para não ser lido.","O trecho critica a falta de clareza do parecer.","O trecho elogia a clareza do parecer.","'Confuso' é crítica.","inverte a avaliação")
I(26,"conceito_correto",2,"A reforma saiu do papel, mas parou no meio do caminho.","“Saiu do papel” indica que a reforma começou a ser executada.","“Saiu do papel” indica que a reforma foi concluída.","Saiu do papel ≠ concluída.","exagera o alcance da expressão")
I(26,"troca_efeito",3,"O relator navegou entre as emendas como quem cruza um campo minado.","A comparação sugere cautela diante de riscos.","A comparação sugere displicência diante das emendas.","Campo minado = cuidado.","inverte o sentido da comparação")
I(26,"conceito_correto",3,"Ou fazemos as reformas agora, ou o sistema colapsa.","O período apresenta duas alternativas excludentes e destaca a urgência das reformas.","O período apresenta as duas alternativas como igualmente desejáveis.","Ou… ou: uma exclui a outra.","vê alternativas desejáveis")
# 27 autoria, modalização, fato × opinião
I(27,"troca_efeito",3,"Para o consultor, a medida pode reduzir custos, embora ainda faltem estudos.","O verbo “pode” atenua a afirmação, indicando possibilidade.","O verbo “pode” indica certeza quanto à redução de custos.","Poder = possibilidade.","lê possibilidade como certeza")
I(27,"atribuicao_autor",3,"O governo afirma que a inflação cairá; os economistas, porém, duvidam.","A previsão de queda da inflação é atribuída ao governo, não ao autor.","A previsão de queda da inflação é apresentada como posição dos economistas.","Quem afirma: o governo.","troca o autor da afirmação")
I(27,"atribuicao_autor",3,"O prefeito declarou que as obras terminarão em março.","O texto relata uma declaração, sem que o autor a ratifique.","O texto afirma, por conta própria, que as obras terminarão em março.","Relato ≠ afirmação própria.","confunde citação e afirmação")
I(27,"troca_efeito",2,"Talvez o prazo seja prorrogado.","O advérbio “talvez” marca incerteza.","O advérbio “talvez” marca certeza.","Talvez = dúvida.","inverte o grau de certeza")
I(27,"atribuicao_autor",3,"Infelizmente, o projeto foi rejeitado.","O advérbio “infelizmente” revela juízo de valor do autor.","O advérbio “infelizmente” é neutro e não revela avaliação do autor.","Infelizmente = avaliação.","lê juízo como neutralidade")
I(27,"atribuicao_autor",2,"Em 2025, o órgão recebeu 4 mil pedidos de acesso à informação.","O trecho expõe um dado verificável, não uma opinião.","O trecho expressa opinião subjetiva do autor.","Número = dado.","lê dado como opinião")
I(27,"atribuicao_autor",3,"Segundo especialistas, o modelo é eficiente, mas a decisão de adotá-lo cabe ao Congresso.","A avaliação da eficiência é atribuída a especialistas, e a decisão de adotar o modelo, ao Congresso.","A decisão de adotar o modelo é atribuída aos especialistas.","Quem decide: o Congresso.","troca o sujeito da decisão")
I(27,"troca_efeito",2,"É inegável que a medida trouxe avanços.","A expressão “é inegável” reforça o grau de certeza do autor.","A expressão “é inegável” atenua a afirmação do autor.","Inegável = reforço.","inverte reforço e atenuação")
# 28 relações lógicas
I(28,"troca_efeito",2,"O prazo foi cumprido porque a equipe trabalhou em regime de plantão.","O trabalho em plantão é apresentado como causa do cumprimento do prazo.","O trabalho em plantão é apresentado como consequência do cumprimento do prazo.","Porque = causa.","inverte causa e consequência")
I(28,"troca_efeito",3,"Apesar do corte de verbas, o programa ampliou o atendimento.","A ampliação do atendimento contraria a expectativa gerada pelo corte de verbas.","O corte de verbas é apresentado como causa da ampliação do atendimento.","Apesar de = concessão.","lê concessão como causa")
I(28,"troca_efeito",2,"Se o quórum não for atingido, a sessão será suspensa.","A suspensão da sessão está condicionada à ausência de quórum.","A suspensão da sessão ocorre independentemente do quórum.","Se = condição.","ignora a condição")
I(28,"troca_efeito",3,"Quanto mais o prazo se aproximava, maior era a pressão sobre a equipe.","O texto estabelece relação de proporção entre a aproximação do prazo e a pressão.","O texto estabelece relação de oposição entre a aproximação do prazo e a pressão.","Quanto mais… maior = proporção.","troca proporção por oposição")
I(28,"troca_efeito",2,"A lei foi sancionada; contudo, não produziu efeitos imediatos.","O segundo trecho se opõe à expectativa criada pelo primeiro.","O segundo trecho reforça, como conclusão, o primeiro.","Contudo = oposição.","lê oposição como conclusão")
I(28,"troca_efeito",2,"O sistema falhou, de modo que as votações foram adiadas.","O adiamento das votações é consequência da falha do sistema.","A falha do sistema é consequência do adiamento das votações.","De modo que = consequência.","inverte causa e consequência")
I(28,"conceito_correto",2,"A medida é impopular, mas necessária.","O texto reconhece um aspecto negativo e destaca um positivo da medida.","O texto reconhece dois aspectos positivos da medida.","Mas opõe os dois juízos.","ignora o contraste")
I(28,"troca_efeito",2,"Mesmo com o recurso, a decisão foi mantida.","O recurso não alterou a decisão.","O recurso alterou a decisão.","Mesmo com = concessão.","inverte o resultado")
# 29 armadilhas
I(29,"generalizacao",3,"Em geral, os prazos são cumpridos, ainda que haja exceções.","O texto admite exceções ao cumprimento dos prazos.","O texto afirma que os prazos são cumpridos sem exceções.","'Em geral' admite exceções.","apaga a ressalva")
I(29,"generalizacao",3,"Alguns servidores aderiram ao sistema.","O texto não permite concluir que a totalidade dos servidores aderiu.","O texto permite concluir que nenhum servidor deixou de aderir.","'Alguns' não autoriza o total.","generaliza")
I(29,"troca_efeito",3,"O programa é mais eficiente que o anterior, porém mais caro.","O texto compara os dois programas quanto à eficiência e ao custo.","O texto afirma que o programa é mais barato que o anterior.","'Porém mais caro'.","inverte a comparação")
I(29,"generalizacao",3,"O estudo sugere que a medida reduz acidentes.","O texto apresenta a redução de acidentes como indício, não como fato comprovado.","O texto apresenta a redução de acidentes como fato comprovado.","'Sugere' = indício.","transforma indício em prova")
I(29,"restricao_indevida",3,"O deputado votou contra o projeto, mas defendeu a necessidade de debatê-lo.","O deputado rejeitou o projeto sem negar a importância do debate.","O deputado rejeitou o projeto e também a realização do debate.","'Mas' preserva o debate.","amplia a rejeição")
I(29,"troca_efeito",3,"A empresa foi multada por atraso na entrega, não por má qualidade.","O texto exclui a má qualidade como motivo da multa.","O texto aponta a má qualidade como motivo da multa.","'Não por' exclui.","ignora a negação")
I(29,"generalizacao",4,"Houve queda de 10% nas denúncias, o que não significa menos irregularidades.","O texto faz ressalva à interpretação da queda nas denúncias.","O texto interpreta a queda nas denúncias como prova de menos irregularidades.","'Não significa' ressalva.","ignora a ressalva")
I(29,"troca_efeito",2,"Antes de aprovar a lei, o Congresso ouviu especialistas.","A oitiva dos especialistas antecedeu a aprovação da lei.","A oitiva dos especialistas ocorreu após a aprovação da lei.","Antes de = anterioridade.","inverte a ordem")
