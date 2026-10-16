"""Atribui a cada questão do banco o 'campo' (q.f): grupo de átomos vizinhos que o motor trata como um mesmo terreno
(acertar em um reduz a urgência dos irmãos; uma questão por campo por bloco; campo dominado é revisado espaçado).
Uso: python3 -I campos.py <banco.json> <campos.json>   (idempotente). Regimentos: sem agrupamento (campo = átomo)."""
import json, re, sys
ROM = {"I":1,"V":5,"X":10,"L":50,"C":100}
def rom(s):
    n = 0
    for i, c in enumerate(s):
        v = ROM[c]; n += -v if i+1 < len(s) and ROM[s[i+1]] > v else v
    return n
# (art_ini, art_fim, id, nome)
CF = [(1,4,"CF-princ","Princípios fundamentais (arts. 1º a 4º)"),(6,6,"CF-sociais","Direitos sociais: rol (art. 6º)"),(7,7,"CF-art7","Direitos dos trabalhadores (art. 7º)"),(8,11,"CF-sindic","Sindicatos, greve e representação (arts. 8º a 11)"),
 (12,13,"CF-nac","Nacionalidade (arts. 12 e 13)"),(14,16,"CF-polit","Direitos políticos (arts. 14 a 16)"),(17,17,"CF-partidos","Partidos políticos (art. 17)"),
 (18,19,"CF-fed","Entes federativos e vedações (arts. 18 e 19)"),(20,20,"CF-bens","Bens da União (art. 20)"),(21,21,"CF-c21","Competência material da União (art. 21)"),(22,22,"CF-c22","Competência legislativa privativa da União (art. 22)"),(23,23,"CF-c23","Competência comum (art. 23)"),(24,24,"CF-c24","Competência legislativa concorrente (art. 24)"),
 (25,28,"CF-estados","Estados federados (arts. 25 a 28)"),(29,31,"CF-municipios","Municípios (arts. 29 a 31)"),(32,33,"CF-dfterr","Distrito Federal e Territórios (arts. 32 e 33)"),(34,36,"CF-interv","Intervenção (arts. 34 a 36)"),
 (37,38,"CF-adm","Princípios e regras da administração pública (arts. 37 e 38)"),(39,40,"CF-servidores","Servidores civis: regime e previdência (arts. 39 e 40)"),(41,41,"CF-estab","Estabilidade do servidor (art. 41)"),(42,42,"CF-militares","Servidores militares (arts. 42, 142 e 143)"),(43,43,"CF-regioes","Regiões (art. 43)"),(142,143,"CF-militares","Servidores militares (arts. 42, 142 e 143)"),
 (44,47,"CF-congresso","Estrutura do Congresso Nacional (arts. 44 a 47)"),(48,48,"CF-art48","Matérias de lei do Congresso com sanção (art. 48)"),(49,52,"CF-compcasas","Competências do Congresso, da Câmara e do Senado (arts. 49 a 52)"),
 (53,56,"CF-parl","Estatuto dos parlamentares (arts. 53 a 56)"),(57,58,"CF-func","Funcionamento e comissões (arts. 57 e 58)"),
 (59,59,"CF-pl-esp","Espécies normativas (art. 59)"),(60,60,"CF-emenda","Emendas à Constituição (art. 60)"),(61,67,"CF-pl","Processo legislativo: iniciativa, MP, sanção e veto (arts. 61 a 67)"),
 (68,69,"CF-deleg","Leis delegadas e complementares (arts. 68 e 69)"),(70,75,"CF-controle","Fiscalização e controle externo (arts. 70 a 75)")]
# art. 5º por intervalos de inciso
C5 = [(1,15,"CF5-liberd","Art. 5º: igualdade, liberdades e intimidade (I a XV)"),(16,21,"CF5-assoc","Art. 5º: reunião e associação (XVI a XXI)"),
 (22,31,"CF5-prop","Art. 5º: propriedade (XXII a XXXI)"),(32,40,"CF5-garant","Art. 5º: garantias gerais e legalidade penal (XXXII a XL)"),
 (41,52,"CF5-penal","Art. 5º: crimes, penas e extradição (XLI a LII)"),(53,68,"CF5-proc","Art. 5º: devido processo e prisão (LIII a LXVIII)"),
 (69,73,"CF5-remedios","Art. 5º: remédios constitucionais (LXIX a LXXIII)"),(74,78,"CF5-acesso","Art. 5º: assistência, indenização e duração do processo (LXXIV a LXXVIII)")]
L9784 = [(1,2,"L9784-disp","Lei 9.784: disposições gerais e princípios (arts. 1º e 2º)"),(3,4,"L9784-dir","Lei 9.784: direitos e deveres do administrado (arts. 3º e 4º)"),(5,8,"L9784-inicio","Lei 9.784: início do processo (arts. 5º a 8º)"),
 (9,10,"L9784-interess","Lei 9.784: interessados (arts. 9º e 10)"),(11,17,"L9784-comp","Lei 9.784: competência (arts. 11 a 17)"),(18,21,"L9784-imped","Lei 9.784: impedimento e suspeição (arts. 18 a 21)"),
 (22,28,"L9784-atos","Lei 9.784: forma, tempo, lugar e comunicação dos atos (arts. 22 a 28)"),(29,47,"L9784-instr","Lei 9.784: instrução (arts. 29 a 47)"),(48,55,"L9784-decisao","Lei 9.784: dever de decidir, motivação, anulação e revogação (arts. 48 a 55)"),
 (56,65,"L9784-recurso","Lei 9.784: recurso administrativo e revisão (arts. 56 a 65)"),(66,69,"L9784-prazos","Lei 9.784: prazos, sanções e disposições finais (arts. 66 a 69)")]
L8112 = [(2,5,"L8112-cargo","Lei 8.112: conceitos, cargo e requisitos (arts. 2º a 5º)"),(6,12,"L8112-nom","Lei 8.112: provimento, nomeação e concurso (arts. 6º a 12)"),(13,19,"L8112-posse","Lei 8.112: posse, exercício e jornada (arts. 13 a 19)"),
 (20,22,"L8112-estag","Lei 8.112: estágio probatório e estabilidade (arts. 20 a 22)"),(24,32,"L8112-deriv","Lei 8.112: readaptação, reversão, reintegração, recondução e aproveitamento (arts. 24 a 32)"),(33,35,"L8112-vac","Lei 8.112: vacância e exoneração (arts. 33 a 35)"),
 (36,39,"L8112-remocao","Lei 8.112: remoção, redistribuição e substituição (arts. 36 a 39)"),(40,48,"L8112-venc","Lei 8.112: vencimento, remuneração, teto e descontos (arts. 40 a 48)"),(49,60,"L8112-indeniz","Lei 8.112: indenizações (arts. 49 a 60-E)"),
 (61,76,"L8112-grat","Lei 8.112: gratificações e adicionais (arts. 61 a 76-A)"),(77,80,"L8112-ferias","Lei 8.112: férias (arts. 77 a 80)"),(81,92,"L8112-lic","Lei 8.112: licenças (arts. 81 a 92)"),(93,96,"L8112-afast","Lei 8.112: cessão, mandato eletivo e afastamentos (arts. 93 a 96-A)"),
 (97,103,"L8112-tempo","Lei 8.112: concessões e tempo de serviço (arts. 97 a 103)"),(104,115,"L8112-peticao","Lei 8.112: direito de petição e prescrição (arts. 104 a 115)"),(116,120,"L8112-deveres","Lei 8.112: deveres, proibições e acumulação (arts. 116 a 120)"),
 (121,126,"L8112-resp","Lei 8.112: responsabilidades (arts. 121 a 126-A)"),(127,137,"L8112-penal","Lei 8.112: penalidades disciplinares (arts. 127 a 137)"),(138,142,"L8112-presc","Lei 8.112: abandono, inassiduidade e prescrição (arts. 138 a 142)"),
 (143,150,"L8112-sind","Lei 8.112: sindicância e comissão processante (arts. 143 a 150)"),(151,173,"L8112-pad","Lei 8.112: processo administrativo disciplinar (arts. 151 a 173)"),(174,182,"L8112-rev","Lei 8.112: revisão do processo disciplinar (arts. 174 a 182)"),
 (183,201,"L8112-seg","Lei 8.112: seguridade social e benefícios (arts. 183 a 201)"),(202,214,"L8112-saude","Lei 8.112: licenças de saúde, maternidade e acidente (arts. 202 a 214)"),(215,230,"L8112-pensao","Lei 8.112: pensão e demais benefícios (arts. 215 a 230)")]
L8429 = [(1,3,"L8429-disp","Lei 8.429: sistema, dolo, sujeitos e sucessão (arts. 1º a 3º, 8º e 8º-A)"),(8,8,"L8429-disp","Lei 8.429: sistema, dolo, sujeitos e sucessão (arts. 1º a 3º, 8º e 8º-A)"),(7,7,"L8429-repr","Lei 8.429: declaração de bens e representação (arts. 7º, 13 a 15, 19 e 22)"),
 (9,9,"L8429-art9","Lei 8.429: enriquecimento ilícito (art. 9º)"),(10,10,"L8429-art10","Lei 8.429: lesão ao erário (art. 10)"),(11,11,"L8429-art11","Lei 8.429: violação a princípios (art. 11)"),(12,12,"L8429-sanc","Lei 8.429: sanções (art. 12)"),
 (13,15,"L8429-repr","Lei 8.429: declaração de bens e representação (arts. 7º, 13 a 15, 19 e 22)"),(16,16,"L8429-indisp","Lei 8.429: indisponibilidade de bens (art. 16)"),(17,17,"L8429-acao","Lei 8.429: ação de improbidade e acordo (arts. 17 a 17-B)"),
 (18,18,"L8429-sent","Lei 8.429: sentença, ressarcimento e unificação de sanções (arts. 17-C a 18-A)"),(19,19,"L8429-repr","Lei 8.429: declaração de bens e representação (arts. 7º, 13 a 15, 19 e 22)"),(20,21,"L8429-afast","Lei 8.429: afastamento e independência de instâncias (arts. 20 e 21)"),
 (22,22,"L8429-repr","Lei 8.429: declaração de bens e representação (arts. 7º, 13 a 15, 19 e 22)"),(23,23,"L8429-presc","Lei 8.429: prescrição (art. 23)"),(24,26,"L8429-fim","Lei 8.429: capacitação, custas e partidos (arts. 23-A a 23-C)")]
L12527 = [(1,6,"LAI-disp","LAI: objeto, âmbito, diretrizes e deveres (arts. 1º a 6º)"),(4,4,"LAI-conc","LAI: conceitos (art. 4º)"),(7,7,"LAI-acesso","LAI: direito de acesso (art. 7º)"),(8,9,"LAI-ativa","LAI: transparência ativa e serviço de informações (arts. 8º e 9º)"),
 (10,14,"LAI-pedido","LAI: pedido de acesso, prazos e custos (arts. 10 a 14)"),(15,20,"LAI-recurso","LAI: recursos (arts. 15 a 20)"),(21,24,"LAI-restr","LAI: restrições e classificação (arts. 21 a 24)"),
 (25,30,"LAI-proced","LAI: proteção, competência e procedimento de classificação (arts. 25 a 30)"),(31,31,"LAI-pessoal","LAI: informações pessoais (art. 31)"),(32,34,"LAI-resp","LAI: responsabilidades e sanções (arts. 32 a 34)"),(35,47,"LAI-fim","LAI: CMRI e disposições finais (arts. 35 a 47)")]
L13709 = [(1,4,"LGPD-disp","LGPD: objeto, âmbito, fundamentos e conceitos (arts. 1º a 5º)"),(5,5,"LGPD-disp","LGPD: objeto, âmbito, fundamentos e conceitos (arts. 1º a 5º)"),(6,6,"LGPD-princ","LGPD: princípios (art. 6º)"),(7,10,"LGPD-bases","LGPD: bases legais e consentimento (arts. 7º a 10)"),
 (11,13,"LGPD-sens","LGPD: dados sensíveis e anonimização (arts. 11 a 13)"),(14,16,"LGPD-crianca","LGPD: crianças, adolescentes e término do tratamento (arts. 14 a 16)"),(17,22,"LGPD-titular","LGPD: direitos do titular (arts. 17 a 22)"),
 (23,32,"LGPD-publico","LGPD: tratamento pelo Poder Público (arts. 23 a 32)"),(33,36,"LGPD-intl","LGPD: transferência internacional (arts. 33 a 36)"),(37,45,"LGPD-agentes","LGPD: agentes, encarregado e responsabilidade (arts. 37 a 45)"),
 (46,51,"LGPD-seg","LGPD: segurança, incidentes e governança (arts. 46 a 51)"),(52,54,"LGPD-sanc","LGPD: sanções administrativas (arts. 52 a 54)"),(55,99,"LGPD-anpd","LGPD: ANPD e CNPD (arts. 55-A a 55-L, 58-A, 58-B)")]
D9203 = [(1,2,"D9203-conc","Decreto 9.203: objeto e conceitos (arts. 1º e 2º)"),(3,4,"D9203-princ","Decreto 9.203: princípios e diretrizes (arts. 3º e 4º)"),(5,6,"D9203-mec","Decreto 9.203: mecanismos e dever da alta administração (arts. 5º e 6º)"),
 (7,16,"D9203-cig","Decreto 9.203: CIG e comitês internos (arts. 7º-A a 16)"),(17,18,"D9203-risco","Decreto 9.203: gestão de riscos e auditoria interna (arts. 17 e 18)"),(19,21,"D9203-integ","Decreto 9.203: programa de integridade (art. 19)")]
L14133 = [(1,4,"L14133-ambito","Lei 14.133: âmbito, objetivos e princípios (arts. 1º a 5º)"),(5,5,"L14133-ambito","Lei 14.133: âmbito, objetivos e princípios (arts. 1º a 5º)"),(6,6,"L14133-def","Lei 14.133: definições (art. 6º)"),(7,10,"L14133-agentes","Lei 14.133: agentes públicos e dever de motivar (arts. 7º a 10)"),
 (11,17,"L14133-proc","Lei 14.133: processo licitatório, objetivos e fases (arts. 11 a 17)"),(18,22,"L14133-prep","Lei 14.133: fase preparatória e matriz de riscos (arts. 18 a 22)"),(23,24,"L14133-valor","Lei 14.133: valor estimado e orçamento sigiloso (arts. 23 e 24)"),
 (25,27,"L14133-edital","Lei 14.133: edital, divulgação e preferências (arts. 25 a 27)"),(28,32,"L14133-mod","Lei 14.133: modalidades e diálogo competitivo (arts. 28 a 32)"),(33,39,"L14133-crit","Lei 14.133: critérios de julgamento (arts. 33 a 39)"),
 (40,47,"L14133-compras","Lei 14.133: compras, obras e regimes de execução (arts. 40 a 52)"),(48,52,"L14133-compras","Lei 14.133: compras, obras e regimes de execução (arts. 40 a 52)"),(53,54,"L14133-juridico","Lei 14.133: controle prévio e divulgação (arts. 53 e 54)"),
 (55,58,"L14133-apres","Lei 14.133: apresentação de propostas, prazos e garantia de proposta (arts. 55 a 58)"),(59,60,"L14133-julg","Lei 14.133: julgamento, desclassificação e desempate (arts. 59 e 60)"),(61,71,"L14133-hab","Lei 14.133: negociação, habilitação e encerramento (arts. 61 a 71)"),
 (72,75,"L14133-direta","Lei 14.133: contratação direta (arts. 72 a 75)"),(76,77,"L14133-alien","Lei 14.133: alienação de bens (arts. 76 e 77)"),(78,88,"L14133-aux","Lei 14.133: procedimentos auxiliares (arts. 78 a 88)"),
 (89,102,"L14133-contrato","Lei 14.133: formalização, garantias e instrumento (arts. 89 a 102)"),(103,104,"L14133-risco","Lei 14.133: matriz de riscos e prerrogativas (arts. 103 e 104)"),(105,114,"L14133-dur","Lei 14.133: duração dos contratos (arts. 105 a 114)"),
 (115,123,"L14133-exec","Lei 14.133: execução, fiscalização e responsabilidades (arts. 115 a 123)"),(124,139,"L14133-alt","Lei 14.133: alterações, equilíbrio e extinção (arts. 124 a 139)"),(140,146,"L14133-rec","Lei 14.133: recebimento e pagamento (arts. 140 a 146)"),
 (147,154,"L14133-nul","Lei 14.133: nulidade e meios alternativos (arts. 147 a 154)"),(155,163,"L14133-sanc","Lei 14.133: infrações e sanções (arts. 155 a 163)"),(164,168,"L14133-recurso","Lei 14.133: impugnação e recursos (arts. 164 a 168)"),(169,173,"L14133-ctrl","Lei 14.133: controle das contratações (arts. 169 a 173)"),
 (174,200,"L14133-fim","Lei 14.133: PNCP e disposições finais (arts. 174 a 194)")]
RCE = {1:("RCE-fundamento","Responsabilidade civil do Estado: fundamento, teorias e pressupostos"),2:("RCE-fundamento","Responsabilidade civil do Estado: fundamento, teorias e pressupostos"),3:("RCE-fundamento","Responsabilidade civil do Estado: fundamento, teorias e pressupostos"),4:("RCE-fundamento","Responsabilidade civil do Estado: fundamento, teorias e pressupostos"),5:("RCE-prestadoras","Responsabilidade civil do Estado: prestadoras de serviço público e usuários"),6:("RCE-omissao","Responsabilidade civil do Estado: omissão"),7:("RCE-presos","Responsabilidade civil do Estado: presos e dever específico"),8:("RCE-excludentes","Responsabilidade civil do Estado: excludentes, atenuantes e risco integral"),9:("RCE-excludentes","Responsabilidade civil do Estado: excludentes, atenuantes e risco integral"),10:("RCE-regresso","Responsabilidade civil do Estado: regresso, legitimidade e prescrição"),11:("RCE-regresso","Responsabilidade civil do Estado: regresso, legitimidade e prescrição")}
ATO = {1: ('ATO-elementos', 'Ato administrativo: elementos e atributos'), 2: ('ATO-elementos', 'Ato administrativo: elementos e atributos'), 3: ('ATO-discricionariedade', 'Ato administrativo: discricionariedade, mérito e motivos determinantes'), 10: ('ATO-discricionariedade', 'Ato administrativo: discricionariedade, mérito e motivos determinantes'), 4: ('ATO-classificacao', 'Ato administrativo: classificação, espécies e parecer'), 5: ('ATO-classificacao', 'Ato administrativo: classificação, espécies e parecer'), 6: ('ATO-classificacao', 'Ato administrativo: classificação, espécies e parecer'), 7: ('ATO-extincao', 'Ato administrativo: extinção, convalidação e decadência'), 8: ('ATO-extincao', 'Ato administrativo: extinção, convalidação e decadência'), 9: ('ATO-extincao', 'Ato administrativo: extinção, convalidação e decadência'), 11: ('ATO-poderes', 'Poderes administrativos e abuso de poder'), 12: ('ATO-poderes', 'Poderes administrativos e abuso de poder')}
ORG = {1: ('ORG-conceitos', 'Organização administrativa: conceitos e formas de atuação'), 2: ('ORG-conceitos', 'Organização administrativa: conceitos e formas de atuação'), 3: ('ORG-entidades', 'Organização administrativa: entidades da Administração indireta'), 4: ('ORG-entidades', 'Organização administrativa: entidades da Administração indireta'), 5: ('ORG-entidades', 'Organização administrativa: entidades da Administração indireta'), 6: ('ORG-entidades', 'Organização administrativa: entidades da Administração indireta'), 7: ('ORG-colab', 'Organização administrativa: terceiro setor, órgãos e controle'), 8: ('ORG-colab', 'Organização administrativa: terceiro setor, órgãos e controle'), 9: ('ORG-colab', 'Organização administrativa: terceiro setor, órgãos e controle'), 10: ('ORG-colab', 'Organização administrativa: terceiro setor, órgãos e controle')}
GES = {1: ('GES-modelos', 'Modelos de gestão pública: patrimonialismo, burocracia e gerencialismo'), 2: ('GES-modelos', 'Modelos de gestão pública: patrimonialismo, burocracia e gerencialismo'), 3: ('GES-modelos', 'Modelos de gestão pública: patrimonialismo, burocracia e gerencialismo'), 4: ('GES-modelos', 'Modelos de gestão pública: patrimonialismo, burocracia e gerencialismo'), 5: ('GES-modelos', 'Modelos de gestão pública: patrimonialismo, burocracia e gerencialismo'), 6: ('GES-nova-governanca', 'Nova Governança Pública, redes, coprodução e valor público'), 7: ('GES-nova-governanca', 'Nova Governança Pública, redes, coprodução e valor público'), 8: ('GES-nova-governanca', 'Nova Governança Pública, redes, coprodução e valor público'), 9: ('GES-nova-governanca', 'Nova Governança Pública, redes, coprodução e valor público'), 10: ('GES-governanca', 'Governança pública: governabilidade, mecanismos e avaliação de impacto'), 11: ('GES-governanca', 'Governança pública: governabilidade, mecanismos e avaliação de impacto'), 12: ('GES-governanca', 'Governança pública: governabilidade, mecanismos e avaliação de impacto')}
AGP = {1: ('AGP-ingresso', 'Agentes públicos: ingresso, concurso e cargos em comissão'), 2: ('AGP-ingresso', 'Agentes públicos: ingresso, concurso e cargos em comissão'), 3: ('AGP-ingresso', 'Agentes públicos: ingresso, concurso e cargos em comissão'), 4: ('AGP-direitos', 'Agentes públicos: greve, remuneração, teto e acumulação'), 5: ('AGP-direitos', 'Agentes públicos: greve, remuneração, teto e acumulação'), 6: ('AGP-direitos', 'Agentes públicos: greve, remuneração, teto e acumulação'), 7: ('AGP-regime', 'Agentes públicos: mandato eletivo, estabilidade e conceitos'), 8: ('AGP-regime', 'Agentes públicos: mandato eletivo, estabilidade e conceitos'), 9: ('AGP-regime', 'Agentes públicos: mandato eletivo, estabilidade e conceitos'), 10: ('AGP-regime', 'Agentes públicos: mandato eletivo, estabilidade e conceitos'), 11: ('AGP-regime', 'Agentes públicos: mandato eletivo, estabilidade e conceitos')}
def campo(atom):
    mp = re.match(r"A-AGP-(\d+)", atom)
    if mp: return AGP[int(mp.group(1))]
    mg = re.match(r"A-GES-(\d+)", atom)
    if mg: return GES[int(mg.group(1))]
    mo = re.match(r"A-ORG-(\d+)", atom)
    if mo: return ORG[int(mo.group(1))]
    ma = re.match(r"A-ATO-(\d+)", atom)
    if ma: return ATO[int(ma.group(1))]
    mr = re.match(r"A-RCE-(\d+)", atom)
    if mr: return RCE.get(int(mr.group(1)), ("RCE-casos","Responsabilidade civil do Estado: atos legislativos, judiciais e casos específicos"))
    m14 = re.match(r"A-L14133-(\d+)", atom)
    if m14:
        a = int(m14.group(1))
        for lo, hi, cid, nm in L14133:
            if lo <= a <= hi: return (cid, nm)
        return None
    md = re.match(r"A-D9203-(\d+)", atom)
    if md:
        a = int(md.group(1))
        for lo, hi, cid, nm in D9203:
            if lo <= a <= hi: return (cid, nm)
        return None
    ml3 = re.match(r"A-L13709-(\d+)", atom)
    if ml3:
        a = int(ml3.group(1))
        for lo, hi, cid, nm in L13709:
            if lo <= a <= hi: return (cid, nm)
        return None
    ml2 = re.match(r"A-L12527-(\d+)", atom)
    if ml2:
        a = int(ml2.group(1))
        for lo, hi, cid, nm in (L12527[1:2] + L12527[0:1] + L12527[2:]):
            if lo <= a <= hi: return (cid, nm)
        return None
    m9 = re.match(r"A-L8429-(\d+)([A-Z]?)", atom)
    if m9:
        a = int(m9.group(1)); sf = m9.group(2)
        if sf and a == 17: return ("L8429-acao", "Lei 8.429: ação de improbidade e acordo (arts. 17 a 17-B)") if sf == "B" else ("L8429-sent", "Lei 8.429: sentença, ressarcimento e unificação de sanções (arts. 17-C a 18-A)")
        if sf and a == 18: return ("L8429-sent", "Lei 8.429: sentença, ressarcimento e unificação de sanções (arts. 17-C a 18-A)")
        if sf and a == 23: return ("L8429-fim", "Lei 8.429: capacitação, custas e partidos (arts. 23-A a 23-C)")
        for lo, hi, cid, nm in L8429:
            if lo <= a <= hi: return (cid, nm)
        return None
    m8 = re.match(r"A-L8112-(\d+)", atom)
    if m8:
        a = int(m8.group(1))
        for lo, hi, cid, nm in L8112:
            if lo <= a <= hi: return (cid, nm)
        return None
    ml = re.match(r"A-L9784-(\d+)", atom)
    if ml:
        a = int(ml.group(1))
        for lo, hi, cid, nm in L9784:
            if lo <= a <= hi: return (cid, nm)
        return None
    m = re.match(r"A-CF-(\d+)(?:\.([IVXLC]+))?$", atom)
    if not m: return None
    a = int(m.group(1))
    if a == 5:
        if not m.group(2): return ("CF5-par", "Art. 5º: caput e parágrafos")
        i = rom(m.group(2))
        for lo, hi, cid, nm in C5:
            if lo <= i <= hi: return (cid, nm)
    for lo, hi, cid, nm in CF:
        if lo <= a <= hi: return (cid, nm)
    return None
B = json.load(open(sys.argv[1], encoding="utf-8")); names = {}
for q in B:
    q.pop("f", None)
    cs = {campo(a) for a in q.get("a", []) if campo(a)}
    if len(cs) == 1:
        cid, nm = next(iter(cs)); q["f"] = cid; names[cid] = nm
json.dump(B, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(names, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(sum("f" in q for q in B), "questões com campo;", len(names), "campos")
