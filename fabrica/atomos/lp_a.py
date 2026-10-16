"""Língua Portuguesa (P1, edital 1) — L18, onda 1: pontuação (atomos 1–6) e concordância (7–12).
Cada átomo é uma miniaula curta (regra, exemplos, pegadinha da banca). Cria o blueprint lp.json se não existir.
Uso: python3 -I fabrica/atomos/lp_a.py  (idempotente)."""
import json, os
ATOMOS = {
"1": ["Vírgula entre sujeito, verbo e complementos",
 "Regra: não se separa por vírgula o sujeito do verbo, nem o verbo de seus complementos (objeto direto, indireto, predicativo, oração subjetiva ou objetiva). Errado: 'Os deputados da bancada, aprovaram a emenda.' Certo: 'Os deputados da bancada aprovaram a emenda.'",
 "Exceção: termo intercalado entre sujeito e verbo vem entre DUAS vírgulas (ou nenhuma): 'A proposta, apresentada ontem, foi rejeitada.' Vocativo também se isola: 'Senhores deputados, a sessão está aberta.'",
 "Pegadinha da banca: o item mostra a frase com uma só vírgula depois do sujeito e pergunta se ela é 'obrigatória' ou 'facultativa'; ou apresenta só uma das duas vírgulas do intercalado e afirma que a pontuação está correta."],
"2": ["Vírgula e orações adjetivas; apostos",
 "Oração adjetiva restritiva (sem vírgula) delimita o antecedente: 'Os servidores que faltaram foram advertidos' = só parte deles faltou. Explicativa (entre vírgulas) acrescenta informação: 'Os servidores, que faltaram, foram advertidos' = todos faltaram.",
 "Com 'o qual', 'cujo', 'quem' a regra é a mesma: explicativa tem vírgulas obrigatórias; restritiva não pode tê-las. Aposto explicativo vem entre vírgulas ('Brasília, capital federal, sedia os Poderes'); aposto restritivo não ('O poeta Camões').",
 "Pegadinha: acrescentar ou retirar as vírgulas muda o sentido (de 'alguns' para 'todos'); a banca pergunta se o sentido foi mantido."],
"3": ["Vírgula com adjuntos adverbiais, conjunções e conectivos",
 "Adjunto adverbial curto antecipado: vírgula facultativa ('Ontem o plenário votou'). Longo ou intercalado: vírgula recomendada/obrigatória ('Apesar das divergências entre os partidos que compõem a base, o governo aprovou...'; 'O governo, em razão da crise, adiou a votação').",
 "Conjunções adversativas, conclusivas e explicativas vêm isoladas por vírgula ('mas', 'porém', 'portanto', 'pois' após o verbo); intercaladas, entre duas vírgulas ('A proposta é, portanto, inconstitucional'). A conjunção 'e' em regra dispensa vírgula, mas admite-se quando liga orações de sujeitos diferentes.",
 "Pegadinha: afirmar que a vírgula é 'indevida' onde é obrigatória (intercalação) ou 'obrigatória' onde é facultativa (adjunto curto)."],
"4": ["Vírgula: subordinadas adverbiais, expressões explicativas, enumeração, elipse e datas",
 "Oração subordinada adverbial anteposta: vírgula ('Quando o relator concluiu, o presidente abriu a discussão'). Posposta: vírgula facultativa. Expressões explicativas ('isto é', 'ou seja', 'por exemplo') vêm entre vírgulas.",
 "Enumeração: vírgulas entre os itens, sem vírgula antes do 'e' final. Elipse do verbo: vírgula no lugar do verbo omitido ('O Senado aprovou o projeto; a Câmara, a emenda'). Local e data: 'Brasília, 16 de outubro de 2026.'",
 "Pegadinha: tratar a vírgula da elipse como separação entre sujeito e verbo; exigir vírgula antes do 'e' da enumeração."],
"5": ["Ponto e vírgula, dois-pontos, travessão, parênteses e aspas",
 "Ponto e vírgula: separa itens longos, sobretudo se já têm vírgulas internas, e orações coordenadas com autonomia. Dois-pontos: introduzem enumeração, citação ou explicação ('Dois temas dominaram: saúde e educação'); não se usam entre verbo e complemento ('Os temas foram: saúde...' é inadequado).",
 "Travessão duplo isola termo com ênfase maior que a das vírgulas; parênteses isolam informação acessória; aspas marcam citação, estrangeirismo e ironia.",
 "Pegadinha: restringir o uso do sinal ('apenas citação', 'jamais adjunto adverbial') ou inverter a ênfase entre vírgula, travessão e parênteses."],
"6": ["Pontuação e efeito de sentido",
 "A pontuação pode mudar o sentido: 'Não, quero ajuda' (nega algo e pede ajuda) × 'Não quero ajuda' (recusa ajuda); 'Vamos comer, João' (vocativo) × 'Vamos comer João' (objeto). Vírgula entre verbo e oração completiva é indevida ('O ministro disse, que votaria...').",
 "'Porém', 'contudo', 'entretanto' deslocados para o interior da oração ficam entre vírgulas ('O projeto, porém, foi vetado'). 'Nem... nem' admite vírgula antes do segundo 'nem'.",
 "Pegadinha: a reescrita 'mantém o sentido' quando a vírgula foi movida ou retirada, mas o sentido mudou."],
"7": ["Concordância verbal: sujeito composto",
 "Sujeito composto anteposto: verbo no plural ('O ministro e o secretário chegaram'). Composto posposto: plural ou concordância com o mais próximo. Ligado por 'ou', o singular vale se houver exclusão (só um fará o ato). Ligado por 'com' (adjunto de companhia), o verbo fica no singular.",
 "Pessoas diferentes: 1ª pessoa prevalece sobre a 2ª e a 3ª ('Eu e o relator votamos'). Sujeito resumido por 'tudo', 'nada', 'ninguém': o verbo concorda com o pronome ('Votos, emendas, tudo se resolveu'). Núcleos sinônimos ou em gradação admitem singular.",
 "Pegadinha: composto no singular ('O ministro e o secretário chegou'), ou 'com' tratado como 'e'."],
"8": ["Concordância verbal: verbos impessoais e partícula 'se'",
 "Haver (existir) e fazer (tempo decorrido) são impessoais: ficam no singular ('Há muitos projetos'; 'Faz dois anos'; 'Houve problemas'). Existir NÃO é impessoal: concorda com o sujeito ('Existem falhas').",
 "'Se' apassivador: verbo transitivo direto concorda com o sujeito ('Vendem-se casas', 'Alugam-se salas'). 'Se' índice de indeterminação: verbo intransitivo, transitivo indireto ou de ligação fica no singular ('Precisa-se de servidores'; 'Trata-se de projetos').",
 "Pegadinha: 'Houveram problemas', 'Fazem dois anos', 'Existe falhas', 'Precisam-se de servidores'."],
"9": ["Concordância verbal: coletivos, 'mais de um', 'um dos que', 'cerca de', 'que/quem', 'cada um'",
 "'A maioria dos deputados votou/votaram' (singular ou plural). 'Mais de um deputado votou' (singular). 'Um dos deputados que votaram contra' (plural; singular só se a ação for exclusiva). 'Cerca de cem deputados faltaram' (concorda com o numeral). 'Mais de dez deputados faltaram' (plural).",
 "Relativo 'que': concorda com o antecedente ('Somos nós que decidimos'). 'Cada um dos deputados apresentou' (singular). Nomes próprios no plural com artigo: 'Os Estados Unidos apoiaram'.",
 "Pegadinha: concordar com 'cerca' em vez do numeral; plural com 'mais de um'."],
"10": ["Concordância verbal: horas, datas e verbos que indicam horas",
 "Com horas, o verbo concorda com o numeral: 'Era uma hora', 'Eram duas horas'. Verbos 'bater', 'dar', 'soar' com horas concordam com o numeral: 'Bateram cinco horas'.",
 "Pegadinha: 'Eram uma hora', 'Bateu cinco horas'."],
"11": ["Concordância nominal: meio, bastante, anexo, obrigado, mesmo, menos, possível, proibido",
 "Advérbios são invariáveis: 'meio cansada', 'bastante preocupadas', 'menos servidores' (nunca 'menas'). Adjetivos concordam: 'bastantes razões', 'seguem anexos os documentos', 'elas mesmas', 'as melhores condições possíveis'. 'Obrigado' concorda com quem fala ('Obrigada', disse a ministra).",
 "'É proibido/necessário/bom' fica invariável sem artigo ('É proibido entrada'); com artigo concorda ('É proibida a entrada').",
 "Pegadinha: 'meia cansada', 'bastantes preocupadas', 'seguem anexo os documentos', 'obrigado' dito por mulher, 'menas'."],
"12": ["Concordância: locuções verbais com impessoais e voz passiva",
 "O auxiliar de locução com impessoal fica no singular: 'Deve haver problemas'. Locução com existir concorda: 'Podem existir falhas'. Voz passiva analítica: o auxiliar concorda com o sujeito paciente ('Devem ser votados dois projetos').",
 "Pegadinha: 'Devem haver problemas' (errado), 'Pode existir falhas' (errado), 'Deve ser votados dois projetos' (errado)."],
}
PONTOS = [
 ("LP01","Pontuação","P1-M1-5","1.5.4","alta"),("LP02","Concordância verbal e nominal","P1-M1-5","1.5.5","alta"),
 ("LP03","Reescrita de frases e parágrafos","P1-M1-6","1.6","alta"),("LP04","Coesão textual: conectores e referenciação","P1-M1-4","1.4","alta"),
 ("LP05","Interpretação de textos","P1-M1-1","1.1","alta"),("LP06","Orações coordenadas e subordinadas","P1-M1-5","1.5.3","alta"),
 ("LP07","Sintaxe da oração e termos","P1-M1-5","1.5","alta"),("LP08","Significação das palavras","P1-M1-6","1.6.1","alta"),
 ("LP09","Tempos e modos verbais","P1-M1-4","1.4.2","media"),("LP10","Regência verbal e nominal","P1-M1-5","1.5.6","media"),
 ("LP11","Crase","P1-M1-5","1.5.7","media"),("LP12","Pronomes e colocação pronominal","P1-M1-5","1.5.8","media"),
 ("LP13","Classes de palavras","P1-M1-5","1.5.1","media"),("LP14","Tipos e gêneros textuais","P1-M1-2","1.2","media"),
 ("LP15","Ortografia e acentuação","P1-M1-3","1.3","media")]
def blueprint():
    return {"parte":"Língua Portuguesa (P1, edital 1)","sigla":"LP","topico":"P1-M1-5","materia":"Língua Portuguesa","bloco":"P1","item_edital":"1.5",
     "nome_curto":"LP","fonte":{"tipo":"gramatica","ref":"norma-padrão (Bechara, Cegalla, Cunha e Cintra); Manual de Redação da Presidência; raio-x de questões do Cebraspe 2025–2026","versao":"conhecimento do autor","conferida":"conhecimento"},
     "nota_calibracao":"Matéria de P1 (Língua Portuguesa, edital 1). Pesos pelo raio-x de 1.661 questões do Cebraspe (2025–2026): interpretação 25,6%, pontuação 7,6%, reescrita 7,6%, concordância 7,1%, coesão 7%, sintaxe da oração e orações ~17%, sentido de palavras 5,7%. Itens curtos (frase-regra, reescrita, microtexto até ~50 palavras). Não reproduz questões reais.",
     "pendencias":["Gramática por conhecimento do autor; itens controversos (vírgula facultativa, concordância facultativa) evitados ou marcados na explicação"],"descartar_tags":[],
     "rotulos":{},"pontos":[{"id":p[0],"titulo":p[1],"incidencia":p[4],"armadilhas":[]} for p in PONTOS],
     "topico_por_ponto":{p[0]:p[2] for p in PONTOS},"item_edital_por_ponto":{p[0]:p[3] for p in PONTOS}}
if __name__ == "__main__":
    tp = "dados/leis/lp.json"
    d = json.load(open(tp, encoding="utf-8")) if os.path.exists(tp) else {}
    for k, v in ATOMOS.items(): d[k] = v
    json.dump(d, open(tp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bp = "fabrica/blueprints/lp.json"
    b = json.load(open(bp, encoding="utf-8")) if os.path.exists(bp) else blueprint()
    for k, v in ATOMOS.items(): b["rotulos"][k] = v[0]
    json.dump(b, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(ATOMOS), "átomos; total", len(d))
