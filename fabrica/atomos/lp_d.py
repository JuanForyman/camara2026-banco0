"""Língua Portuguesa — L21, onda 4: regência (30–31), crase (32–33), pronomes/colocação (34–35), classes (36), verbos (37), léxico (38–39), tipologia (40), ortografia (41)."""
import json
ATOMOS = {
"30": ["Regência verbal: verbos mais cobrados",
 "Assistir (ver) e aspirar (almejar) pedem 'a': 'Assistimos ao julgamento'; 'aspira a um cargo'. Preferir X a Y (sem 'mais… do que'). Obedecer/desobedecer: 'a'. Implicar (acarretar) é direto: 'implica custos', sem 'em'.",
 "Informar admite 'algo a alguém' e 'alguém de algo'. Esquecer: 'Esqueci o prazo' ou 'Esqueci-me do prazo' (nunca 'esqueci-me o prazo').",
 "Pegadinha: tirar a preposição exigida ou pôr preposição onde o verbo é direto."],
"31": ["Regência nominal e relativo com preposição",
 "Acessível a; aversão a/por; compatível com; preferível a (não 'do que'). Nomes e adjetivos pedem a preposição do seu complemento.",
 "Com pronome relativo, a preposição do verbo vem antes dele: 'a lei a que o relator se referiu' (referir-se a).",
 "Pegadinha: omitir a preposição antes do relativo ou trocar a preposição do nome."],
"32": ["Crase: regra geral e casos de proibição",
 "Crase = preposição 'a' + artigo 'a' (ou 'aquele/aquela/aquilo'): 'Fui à Câmara'; 'Refiro-me àquela decisão'. Teste: troque por masculino ('Fui ao Senado').",
 "Não há crase diante de: verbo, palavra masculina, pronome pessoal, nome no plural sem artigo ('Referiu-se a reuniões'), cidade sem especificação ('Voltou a Brasília' × 'à Brasília dos anos 60').",
 "Pegadinha: crase onde não há artigo (verbo, pronome pessoal, masculino)."],
"33": ["Crase: casos obrigatórios, facultativos e especiais",
 "Obrigatória: horas determinadas ('às nove'), locuções femininas ('à noite', 'às pressas', 'à luz de'). Facultativa: possessivo feminino ('à/a sua chefe'), nome próprio feminino de pessoa ('à/a Maria').",
 "Não há crase antes de 'que' ('a empresa a que me refiro') nem em locuções com palavras repetidas ('frente a frente', 'cara a cara').",
 "Pegadinha: chamar de obrigatório o que é facultativo, ou o inverso."],
"34": ["Pronomes pessoais e de tratamento",
 "Após preposição, oblíquo tônico: 'entre mim e ele', 'para mim' (sem verbo). Sujeito de infinitivo é reto: 'para eu ler'. Lhe = objeto indireto; o/a/os/as = objeto direto.",
 "Pronomes de tratamento: verbo e possessivos na 3ª pessoa ('Vossa Excelência trouxe seus documentos'). 'Vossa' fala-se COM o interlocutor; 'Sua', fala-se DELE.",
 "Pegadinha: 'entre eu e ele', 'para mim ler', 'vossos' com Vossa Excelência."],
"35": ["Colocação pronominal",
 "Próclise (antes): negação, relativo, indefinido, advérbio, conjunção subordinativa, 'em + gerúndio' ('Em se tratando'). Ênclise (depois): verbo no início do período ('Disseram-me'). Mesóclise: futuro, em registro formal ('Dar-lhe-ei').",
 "Não se coloca o pronome átono depois de particípio ('Tinha-me avisado', e não 'tinha avisado-me') nem depois de verbo no futuro ('Darei-lhe' é inadequado).",
 "Pegadinha: ênclise após palavra atrativa; 'Me disseram' no início."],
"36": ["Palavras que variam ou não; porque; mal/mau",
 "Advérbio é invariável: 'meio cansada', 'bastante cansados', 'menos pessoas' (nunca 'menas'). 'Mesmo' como reforço concorda: 'ela mesma'.",
 "Aonde = a onde (movimento); onde = lugar fixo. Por que (pergunta); porque (resposta); porquê (substantivo: 'o porquê'); por quê (final de frase). Mal ↔ bem; mau ↔ bom.",
 "Pegadinha: flexionar advérbio, trocar aonde/onde, porquê em pergunta."],
"37": ["Verbos: futuro do subjuntivo, correlação e modos",
 "Futuro do subjuntivo: ver → vir; vir → vier; propor → propuser; pôr → puser; ter → tiver. 'Se ele vir', 'quando vier', 'se puser'. Correlação: 'Se eu fosse… rejeitaria'.",
 "Desejo e dúvida pedem subjuntivo ('Espero que aprove'). Em locução verbal, o infinitivo não varia ('devem entregar'). Imperativo de 'você' = subjuntivo ('Faça').",
 "Pegadinha: infinitivo no lugar do futuro do subjuntivo ('se ver', 'se propor') e confusão entre vir e ver."],
"38": ["Parônimos e homônimos mais cobrados",
 "Ratificar = confirmar; retificar = corrigir. Infringir = violar; infligir = aplicar pena. Eminente = notável; iminente = prestes a ocorrer. Deferir = conceder; diferir = adiar. Mandado = ordem; mandato = exercício.",
 "Descriminar = tirar o caráter de crime; discriminar = distinguir/segregar. Emigrar = sair; imigrar = entrar. Comprimento = extensão; cumprimento = saudação/execução. Sessão = reunião; seção = divisão; cessão = ato de ceder.",
 "Pegadinha: o item troca os significados de um par."],
"39": ["Sentido contextual, polissemia e sinonímia",
 "A palavra muda de sentido pelo contexto: 'cargo vago' (desocupado) × 'ideia vaga' (imprecisa). Sinônimo só vale se preserva o sentido no contexto: suspensa = interrompida (≠ encerrada).",
 "Corroborar = confirmar; dirimir = resolver; mitigar = atenuar.",
 "Pegadinha: substituir por termo mais forte ou de sentido oposto."],
"40": ["Tipos e gêneros textuais",
 "Narração: ações no tempo (pretérito). Descrição: qualidades. Dissertação: tese + argumentos. Exposição: explica sem defender tese. Injunção: orienta a agir (imperativo).",
 "Gêneros: ofício e memorando (redação oficial); notícia (referencial, informa fato recente); crônica e soneto (literários).",
 "Pegadinha: confundir tipo com gênero ou atribuir função expressiva à notícia."],
"41": ["Acentuação, hífen e grafia",
 "Sem acento: ideia, assembleia, heroico, jiboia (ditongo aberto em paroxítona). Com acento: pôr (verbo), têm (plural), oxítonas em a/e/o (jacaré, cipó). Hífen: mesma vogal (anti-inflamatório); sem hífen: vogais diferentes (autoescola).",
 "Grafia: exceção (não 'excessão'). Sessão/seção/cessão são homófonas, de sentidos diferentes.",
 "Pegadinha: manter acento extinto ou hífen indevido."],
}
if __name__ == "__main__":
    tp = "dados/leis/lp.json"; d = json.load(open(tp, encoding="utf-8"))
    for k, v in ATOMOS.items(): d[k] = v
    json.dump(d, open(tp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bp = "fabrica/blueprints/lp.json"; b = json.load(open(bp, encoding="utf-8"))
    for k, v in ATOMOS.items(): b["rotulos"][k] = v[0]
    json.dump(b, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(ATOMOS), "átomos; total", len(d))
