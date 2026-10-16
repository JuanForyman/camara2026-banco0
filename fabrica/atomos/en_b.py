"""Língua Inglesa — onda 2: átomos 19-28. Uso: python3 -I fabrica/atomos/en_b.py (idempotente)."""
import json, os
ATOMOS = {
"19": ["Básico: artigos, plurais, there is/are",
 "A/an = um (an antes de som de vogal: an hour, a university). The = específico/já mencionado. Plurais irregulares: man → men, child → children, person → people. Incontáveis não têm plural: information, advice, news, equipment. There is + singular/incontável; there are + plural.",
 "Exemplos: 'The news is good' (news é singular). 'There are three bills on the table.'",
 "Pegadinha: pluralizar incontáveis (informations, advices) ou usar 'are' com 'news'."],
"20": ["Básico: pronomes, possessivos e verbos auxiliares",
 "Sujeito: I, you, he, she, it, we, they. Objeto: me, him, her, us, them. Possessivos: my, your, his, her, its, our, their. Does/doesn't na 3ª pessoa do singular (he does not work); do/don't nas demais. Após does/did o verbo fica na forma base: 'Does she work?'. Its = dele(a) (coisa); it's = it is.",
 "Exemplos: 'He doesn't know' (sem -s); 'The court issued its ruling'.",
 "Pegadinha: colocar -s no verbo após does, ou confundir its com it's."],
"21": ["Phrasal verbs de notícias",
 "carry out = realizar; set up = criar/instituir; call for = exigir/pedir; point out = ressaltar; turn down = recusar; back up = apoiar/confirmar; step down = renunciar; roll out = lançar; find out = descobrir; look into = investigar; cut down on = reduzir; break down = falhar/decompor; bring about = provocar; carry on = continuar.",
 "Exemplos: 'The committee set up a task force.' 'He turned down the offer.'",
 "Pegadinha: traduzir o phrasal pela soma literal das palavras (turn down ≠ virar para baixo)."],
"22": ["Vocabulário de notícias e políticas públicas",
 "pledge = promessa/compromisso; ban = proibir/proibição; ruling = decisão judicial; poll = pesquisa de opinião; lawsuit = ação judicial; crackdown = repressão/endurecimento; hike = aumento; cut = corte; deficit = déficit; surplus = superávit; scandal = escândalo; watchdog = órgão fiscalizador; lawmaker = parlamentar; turnout = comparecimento; to ratify = ratificar; to veto = vetar.",
 "Exemplos: 'A tax hike' = aumento de imposto. 'Voter turnout was low' = comparecimento baixo.",
 "Pegadinha: o item troca o sentido por um termo parecido (surplus × déficit; hike × queda)."],
"23": ["Leitura: fato, opinião e hedging",
 "Hedging suaviza a afirmação: may, might, could, suggests, appears, seems, likely, reportedly, allegedly, so far. 'The drug may reduce risk' ≠ 'The drug reduces risk'. Allegedly/reportedly = segundo se diz (não confirmado). Quantificadores: some, most, all, none, nearly, about.",
 "Exemplo: 'Allegedly, the funds were misused' não afirma que foram desviados.",
 "Pegadinha: o item transforma possibilidade em certeza ou 'some' em 'all'."],
"24": ["Leitura: atribuição e verbos de relato",
 "Verbos de relato mostram posição do autor: claim (afirma, mas duvidoso), argue (defende), admit (reconhece), deny (nega), warn (alerta), point out (ressalta), urge (insta), suggest (sugere/propõe). 'According to X' = fonte, não a opinião do autor.",
 "Exemplo: 'The minister admitted the error' = ele reconheceu o erro; 'denied' = negou.",
 "Pegadinha: atribuir ao autor o que é só voz de outra pessoa, ou trocar admit por deny."],
"25": ["Preposições regidas e de tempo/lugar",
 "depend on, consist of, responsible for, interested in, good at, afraid of, different from, similar to, fond of, rely on, apologize for, listen to. Tempo: at (hora: at 5 pm), on (dia: on Monday), in (mês/ano: in May, in 2026). Lugar: at (ponto), in (dentro), on (sobre/superfície).",
 "Exemplos: 'The result depends on the vote.' 'The meeting is on Friday, at 9 am, in June.'",
 "Pegadinha: trocar a preposição regida (depend of, interested on) ou in/on/at."],
"26": ["Inglês digital, tecnologia e IA",
 "cloud = nuvem; algorithm = algoritmo; bias = viés; privacy = privacidade; cybersecurity = segurança cibernética; to hack = invadir; password = senha; to log in = entrar (conta); to download/upload = baixar/enviar; machine learning = aprendizado de máquina; chatbot; dataset = conjunto de dados; open source = código aberto; to opt out = optar por sair.",
 "Exemplo: 'Algorithmic bias' = viés algorítmico (resultado enviesado); 'to opt out' = escolher não participar.",
 "Pegadinha: o item troca o sentido do termo técnico (bias = viés, não 'preferência legítima')."],
"27": ["Palavras que confundem",
 "affect (verbo: afetar) × effect (substantivo: efeito); lose (perder) × loose (frouxo); than (comparação) × then (então); its × it's; their (deles) × there (lá) × they're (eles são); principal (diretor; principal) × principle (princípio); since (desde; já que) × for (duração); beside (ao lado de) × besides (além de).",
 "Exemplos: 'The law will affect prices' / 'The law had an effect on prices.' 'for two years' × 'since 2024'.",
 "Pegadinha: trocar affect/effect, then/than ou for/since."],
"28": ["Siglas e abreviaturas em textos oficiais",
 "e.g. = por exemplo; i.e. = isto é; etc. = e assim por diante; vs. = versus; approx. = aproximadamente; Inc. = sociedade anônima; GDP = PIB; CEO = diretor-executivo; NGO = ONG; UN = ONU; EU = União Europeia; WHO = OMS; IMF = FMI; FAQ = perguntas frequentes; N/A = não se aplica.",
 "Exemplo: 'Fruits, e.g. apples' (exemplos) × 'a fruit, i.e. a pear' (explicação).",
 "Pegadinha: trocar e.g. por i.e. ou traduzir sigla com o sentido de outra (WHO, IMF)."],
}
if __name__ == "__main__":
    tp = "dados/leis/en.json"
    d = json.load(open(tp, encoding="utf-8"))
    for k, v in ATOMOS.items(): d[k] = v
    json.dump(d, open(tp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bp = "fabrica/blueprints/en.json"
    b = json.load(open(bp, encoding="utf-8"))
    for k, v in ATOMOS.items(): b["rotulos"][k] = v[0]
    json.dump(b, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(ATOMOS), "átomos; total", len(d))
