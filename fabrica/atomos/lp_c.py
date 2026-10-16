"""Língua Portuguesa — L20, onda 3: interpretação (átomos 24–29), microtextos ≤50 palavras."""
import json
ATOMOS = {
"24": ["Inferência × extrapolação",
 "Inferir é concluir o que o texto sustenta por implicação ('adiou até concluir o estudo' → o estudo não foi concluído). Extrapolar é acrescentar o que o texto não diz ('adiou' → 'cancelou').",
 "Teste: a conclusão decorre necessariamente das palavras do texto? Adiar ≠ cancelar; suspender ≠ extinguir; 'real' ≠ 'nominal'; prazo 'até 18h' exclui 19h.",
 "Pegadinha: o item troca o verbo por outro mais forte ou inventa causa, consequência ou resultado."],
"25": ["Ideia central, tese e estrutura",
 "A ideia central é a tese que o texto sustenta; exemplos e dados a apoiam. 'Não basta' = insuficiente (não é 'desnecessário'). 'Embora/contudo/porém' contrapõem uma visão comum à tese do autor.",
 "Marcadores de causa ('eis por que', 'porque') e de consequência ('de modo que', 'por isso') organizam o texto. Distinga posição do autor de posição de terceiros.",
 "Pegadinha: atribuir ao autor a opinião de 'muitos', inverter causa e consequência, ver consenso onde há conflito."],
"26": ["Sentido contextual, ironia e figuras",
 "O sentido depende do contexto: 'engavetado' (paralisado), 'saiu do papel' (começou). Ironia: o elogio aparente que critica ('Brilhante ideia: ninguém compareceria'). Comparação: 'como uma bomba' = forte impacto; 'como quem cruza um campo minado' = cautela.",
 "Descubra o juízo do autor pelos adjetivos e pelo contexto ('longo e confuso' = crítica). 'Ou… ou' apresenta alternativas excludentes.",
 "Pegadinha: ler a ironia como elogio, o figurado como literal, ou inverter o efeito da comparação."],
"27": ["Autoria, modalização e fato × opinião",
 "Modalizadores indicam o grau de certeza: 'talvez', 'pode' (possibilidade); 'é inegável' (certeza). 'Infelizmente', 'felizmente' revelam juízo do autor. Dado numérico é fato verificável.",
 "'Segundo X', 'X declarou que' atribuem a afirmação a X; o autor apenas relata, sem ratificar. Identifique quem diz o quê.",
 "Pegadinha: tratar relato como afirmação do autor, ou possibilidade como certeza."],
"28": ["Relações lógicas entre trechos",
 "Causa ('porque'), consequência ('de modo que'), concessão ('apesar de', 'mesmo com': a expectativa é contrariada), condição ('se'), proporção ('quanto mais… maior'), oposição ('contudo', 'mas').",
 "Ao julgar, localize o conectivo e diga a relação; depois compare com a afirmativa. 'Mesmo com o recurso, a decisão foi mantida' = o recurso não alterou a decisão.",
 "Pegadinha: inverter causa e consequência, ou ler concessão como causa."],
"29": ["Armadilhas: ressalvas, quantificadores e comparações",
 "'Em geral', 'alguns', 'sugere', 'não significa' são ressalvas: o item que as apaga (transformando indício em prova, 'alguns' em 'todos') está errado. 'Não por X' exclui X.",
 "Em comparações, confira o sentido: 'mais eficiente, porém mais caro' ≠ 'mais barato'. Em ordem temporal, 'antes de' ≠ 'após'.",
 "Pegadinha: generalizar, apagar a ressalva ou inverter a comparação ou a ordem."],
}
if __name__ == "__main__":
    tp = "dados/leis/lp.json"; d = json.load(open(tp, encoding="utf-8"))
    for k, v in ATOMOS.items(): d[k] = v
    json.dump(d, open(tp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bp = "fabrica/blueprints/lp.json"; b = json.load(open(bp, encoding="utf-8"))
    for k, v in ATOMOS.items(): b["rotulos"][k] = v[0]
    json.dump(b, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(ATOMOS), "átomos; total", len(d))
